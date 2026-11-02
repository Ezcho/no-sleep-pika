import AppKit
import CoreImage

/// App-owned read-only bridge. No shell, raw IPC or remote power operations.
@MainActor
final class RemotePairing {
    private var socket: URLSessionWebSocketTask?
    private var timer: Timer?
    private var heartbeat: Timer?
    private var generation = UUID()
    private var creating = false
    private var creationIntent: UUID?
    private var pendingForce = false
    private var credentials: (base: URL, id: String, host: String, expires: Date)?
    private var status: (() -> [String: Any])?
    private var viewer = false
    private var lastStatus: Data?
    private var lastSent = Date.distantPast
    private var preview: URL?
    private var pairUntil: Date?
    private var hasPaired = false
    private let session: URLSession
    private let gatewayOverride: URL?
    init(session: URLSession? = nil, gateway: URL? = nil) {
        self.session = session ?? Self.makeSession()
        self.gatewayOverride = gateway
    }
    private static func makeSession() -> URLSession {
        let c = URLSessionConfiguration.ephemeral
        c.timeoutIntervalForRequest = 6
        c.timeoutIntervalForResource = 8
        c.httpCookieStorage = nil
        c.urlCache = nil
        return URLSession(configuration: c)
    }

    func handle(_ request: [String: Any], status: @escaping () -> [String: Any], completion: @escaping ([String: Any]) -> Void) {
        guard request.count == 1 else { completion(ControlWire.failure("invalid_request", "Remote tools take no arguments")); return }
        if request["operation"] as? String == "remote_revoke" {
            Task { completion(await revoke()) }; return
        }
        guard !creating else { completion(ControlWire.failure("busy", "QR generation is already in progress")); return }
        // Deployment sets this trusted endpoint in the app configuration, never in tool arguments.
        guard let value = gatewayOverride?.absoluteString ?? Bundle.main.object(forInfoDictionaryKey: "PikaRemoteGateway") as? String,
              let base = URL(string: value), base.scheme == "https", base.host != nil,
              base.user == nil, base.password == nil, base.query == nil, base.fragment == nil,
              base.path.isEmpty || base.path == "/" else {
            completion(ControlWire.failure("remote_not_configured", "This build has no remote gateway configured.")); return
        }
        creating = true
        let intent = UUID(); creationIntent = intent
        Task {
            defer { creating = false }
            let revoked = await revoke(invalidateCreation: false)
            guard creationIntent == intent else { completion(ControlWire.failure("remote_pair_cancelled", "QR creation was cancelled")); return }
            guard revoked["ok"] as? Bool == true else { completion(revoked); return }
            self.status = status
            let creationGeneration = generation
            do {
                var req = URLRequest(url: base.appendingPathComponent("api/pair")); req.httpMethod = "POST"
                let (data, response) = try await session.data(for: req)
                guard (response as? HTTPURLResponse)?.statusCode == 200,
                      let info = try JSONSerialization.jsonObject(with: data) as? [String: Any],
                      let id = info["id"] as? String, Self.valid(id),
                      let host = info["hostToken"] as? String, Self.valid(host),
                      let pair = info["pairToken"] as? String, Self.valid(pair),
                      let expiry = info["expiresAt"] as? Double, let until = info["pairUntil"] as? Double,
                      expiry > Date().timeIntervalSince1970 * 1000,
                      expiry <= Date().addingTimeInterval(86410).timeIntervalSince1970 * 1000 else { throw URLError(.badServerResponse) }
                guard generation == creationGeneration, creationIntent == intent else {
                    var cancel = URLRequest(url: base.appendingPathComponent("api/room/\(id)/revoke"))
                    cancel.httpMethod = "POST"; cancel.setValue("Bearer \(host)", forHTTPHeaderField: "Authorization")
                    _ = try? await session.data(for: cancel)
                    completion(ControlWire.failure("remote_pair_cancelled", "QR creation was cancelled. No local bridge was started.")); return
                }
                credentials = (base, id, host, Date(timeIntervalSince1970: expiry/1000))
                pairUntil = Date(timeIntervalSince1970: until/1000); hasPaired = false
                var url = URLComponents(url: base, resolvingAgainstBaseURL: false)!
                url.path = "/"; url.fragment = "room=\(id)&token=\(pair)"
                let link = url.url!.absoluteString
                let qr = try Self.qr(link)
                let dir = FileManager.default.temporaryDirectory.appendingPathComponent("pika-qr-\(UUID().uuidString)", isDirectory: true)
                try FileManager.default.createDirectory(at: dir, withIntermediateDirectories: false, attributes: [.posixPermissions: 0o700])
                let html = dir.appendingPathComponent("pair.html")
                let markup = "<!doctype html><meta charset=utf-8><meta name=referrer content=no-referrer><title>pika QR</title><body style='background:white;color:black;text-align:center;font-family:system-ui'><h1>pika · 읽기 전용 연결</h1><img width=360 height=360 alt='pika 연결 QR' src='data:image/png;base64,\(qr.png)'><p>휴대폰 카메라로 스캔하세요. 5분 · 1회 사용</p><p>공유하지 마세요. 연결은 최대 24시간 유지됩니다.</p>"
                try Data(markup.utf8).write(to: html, options: .atomic)
                try FileManager.default.setAttributes([.posixPermissions: 0o600], ofItemAtPath: html.path)
                preview = html
                connect()
                timer = Timer.scheduledTimer(withTimeInterval: 5, repeats: true) { [weak self] _ in Task { @MainActor in self?.tick() } }
                completion(["ok":true,"readOnly":true,"pairUntil":until,"expiresAt":expiry,"url":link,"qrText":qr.text,"qrPreviewPath":html.path,"qrPNG":qr.png,
                            "message":"Text QR may not scan in proportional fonts. Open qrPreviewPath for a black-on-white QR. Revoking remote access does not stop the local Session."])
            } catch {
                _ = await revoke()
                completion(ControlWire.failure("remote_pair_failed", "Could not create QR connection. Check gateway connectivity and retry."))
            }
        }
    }
    static func valid(_ value: String) -> Bool { value.range(of: "^[A-Za-z0-9_-]{43}$", options: .regularExpression) != nil }
    func revoke(invalidateCreation: Bool = true) async -> [String: Any] {
        if invalidateCreation { creationIntent = nil }
        stopConnection()
        guard let c = credentials else { return ["ok":true] }
        do {
            var r = URLRequest(url: c.base.appendingPathComponent("api/room/\(c.id)/revoke")); r.httpMethod="POST"
            r.setValue("Bearer \(c.host)", forHTTPHeaderField:"Authorization")
            let (_, response) = try await session.data(for:r)
            guard let code = (response as? HTTPURLResponse)?.statusCode, code == 200 || code == 403 else { throw URLError(.badServerResponse) }
            if credentials?.id == c.id && credentials?.host == c.host { credentials=nil }; return ["ok":true]
        } catch {
            // Preserve host credential so local retry can revoke the server-side pairing.
            return ControlWire.failure("remote_revoke_pending", "Local connection stopped; server revocation could not be confirmed. Retry revoke. Server access expires within 24 hours.")
        }
    }
    func stopConnection() {
        generation=UUID(); timer?.invalidate();timer=nil;heartbeat?.invalidate();heartbeat=nil
        socket?.cancel(with:.goingAway,reason:nil);socket=nil;viewer=false;lastStatus=nil;lastSent = .distantPast;pendingForce=false
        if let preview { try? FileManager.default.removeItem(at:preview.deletingLastPathComponent()) }; preview=nil
    }
    private func connect() {
        guard let c=credentials, c.expires>Date() else { return }
        let g=generation
        var components=URLComponents(url:c.base.appendingPathComponent("api/room/\(c.id)/socket"),resolvingAgainstBaseURL:false)!
        components.scheme="wss"
        let task=session.webSocketTask(with:components.url!);task.maximumMessageSize=16384;socket=task;task.resume()
        send(["type":"auth","role":"host","token":c.host]); receive(task,g)
    }
    private func receive(_ task: URLSessionWebSocketTask,_ g: UUID) {
        Task { [weak self] in
            do {
                let frame=try await task.receive()
                guard let self, self.generation==g, self.socket===task else { return }
                if case let .string(text)=frame, let data=text.data(using:.utf8), let m=(try? JSONSerialization.jsonObject(with:data)) as? [String:Any] {
                    if m["type"] as? String == "presence" { self.viewer=m["viewer"] as? Bool ?? false; self.hasPaired = self.hasPaired || self.viewer; self.publish(force:true) }
                    if m["type"] as? String == "refresh" { self.publish(force:true) }
                    if m["type"] as? String == "ready" {
                        self.hasPaired = self.hasPaired || (m["paired"] as? Bool ?? false)
                        self.heartbeat?.invalidate()
                        self.heartbeat=Timer.scheduledTimer(withTimeInterval:45,repeats:true) { [weak self] _ in Task { @MainActor in try? await self?.socket?.send(.string("ping")) } }
                    }
                }
                self.receive(task,g)
            } catch {
                guard let self,self.generation==g,self.socket===task else { return }
                self.viewer=false;self.heartbeat?.invalidate();self.heartbeat=nil
                if [4001,4003].contains(task.closeCode.rawValue) || task.closeCode == .policyViolation { self.stopConnection();return }
                try? await Task.sleep(nanoseconds:5_000_000_000)
                guard self.generation==g else{return};self.connect()
            }
        }
    }
    private func tick() {
        guard let c=credentials else{return}
        if Date()>=c.expires || (!hasPaired && Date()>=(pairUntil ?? c.expires)) { Task { _ = await revoke() }; return }
        if let preview, Date()>=(pairUntil ?? c.expires) { try? FileManager.default.removeItem(at:preview.deletingLastPathComponent());self.preview=nil }
        publish(force:false)
    }
    private func publish(force:Bool) {
        pendingForce = pendingForce || force
        guard Date().timeIntervalSince(lastSent) >= 3, viewer,let value=status?(),let data=try? JSONSerialization.data(withJSONObject:value,options:.sortedKeys) else{return}
        guard pendingForce || data != lastStatus else{return};lastStatus=data;lastSent=Date();pendingForce=false
        // Gateway independently allowlists fields; keep raw diagnostics off the wire here too.
        var safe:[String:Any]=[:]
        for key in ["ok","sessionOn","monitorOn","busy","recoveryRequired","waitingForLid","lidEngaged","serviceRegistered"] { safe[key]=value[key] }
        if let safety=value["safety"] as? [String:Any] { var filtered:[String:Any]=[:];for key in ["batteryPercent","onAC","lidClosed","hasExternalDisplay","thermalState"] { filtered[key]=safety[key] };safe["safety"]=filtered }
        send(["type":"status","status":safe])
    }
    private func send(_ value:[String:Any]) { guard let d=try? JSONSerialization.data(withJSONObject:value),let s=String(data:d,encoding:.utf8),let socket else{return};Task {try? await socket.send(.string(s))} }
    static func qr(_ text:String) throws -> (text:String,png:String) {
        let filter=CIFilter(name:"CIQRCodeGenerator")!;filter.setValue(Data(text.utf8),forKey:"inputMessage");filter.setValue("M",forKey:"inputCorrectionLevel")
        guard let output=filter.outputImage else{throw URLError(.cannotDecodeContentData)}
        let n=Int(output.extent.width),size=n+8
        var pixels=[UInt8](repeating:255,count:n*n)
        CIContext().render(output,toBitmap:&pixels,rowBytes:n,bounds:output.extent,format:.L8,colorSpace:CGColorSpaceCreateDeviceGray())
        func black(_ x:Int,_ y:Int)->Bool {x>=4 && y>=4 && x<n+4 && y<n+4 && pixels[(y-4)*n+x-4]<128}
        var lines=[String]()
        for y in 0..<size { var line=""; for x in 0..<size {line += black(x,y) ? "██" : "  "};lines.append(line) }
        let scale=6,bitmap=NSBitmapImageRep(bitmapDataPlanes:nil,pixelsWide:size*scale,pixelsHigh:size*scale,bitsPerSample:8,samplesPerPixel:1,hasAlpha:false,isPlanar:false,colorSpaceName:.deviceWhite,bytesPerRow:size*scale,bitsPerPixel:8)!
        for y in 0..<size*scale {for x in 0..<size*scale {bitmap.bitmapData![y*size*scale+x]=black(x/scale,y/scale) ? 0 : 255}}
        guard let png=bitmap.representation(using:.png,properties:[:]) else{throw URLError(.cannotDecodeContentData)}
        return (lines.joined(separator:"\n"),png.base64EncodedString())
    }
}
