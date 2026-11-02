import Foundation
import Vision
import AppKit
@main struct QRTests {
    @MainActor static func main() async throws {
        let text = "https://pika-remote.example.workers.dev/#room=" + String(repeating:"a",count:43) + "&token=" + String(repeating:"b",count:43)
        let result = try RemotePairing.qr(text)
        let data = Data(base64Encoded:result.png)!
        let request = VNDetectBarcodesRequest()
        request.symbologies = [.qr]
        request.usesCPUOnly = true
        try VNImageRequestHandler(data:data).perform([request])
        precondition(request.results?.first?.payloadStringValue == text, "QR must decode to exact pairing URL")
        let wire = try JSONSerialization.data(withJSONObject:["ok":true,"url":text,"qrText":result.text,"qrPNG":result.png])
        precondition(wire.count < ControlWire.limit, "QR must fit local control frame")
        precondition(!RemotePairing.valid("../bad") && RemotePairing.valid(String(repeating:"a",count:43)))
        print("PASS native QR decoding and IPC frame size (\(wire.count) bytes)")
        let config = URLSessionConfiguration.ephemeral; config.protocolClasses = [MockGateway.self]
        let gateway = URL(string:"https://unit.test")!
        let bridge = RemotePairing(session:URLSession(configuration:config),gateway:gateway)
        MockGateway.reset();MockGateway.delayCreate = true
        let first = Task { @MainActor in await withCheckedContinuation { continuation in bridge.handle(["operation":"remote_pair"],status:{["ok":true]}) { continuation.resume(returning:$0) } } }
        try await Task.sleep(nanoseconds:80_000_000)
        _ = await bridge.revoke()
        let canceled = await first.value
        precondition(canceled["code"] as? String == "remote_pair_cancelled")
        precondition(MockGateway.revokes == 1, "Late-created server room must be revoked")
        print("PASS revoke during create prevents late connection")
        MockGateway.reset()
        let success = await withCheckedContinuation { continuation in bridge.handle(["operation":"remote_pair"],status:{["ok":true]}) { continuation.resume(returning:$0) } }
        precondition(success["ok"] as? Bool == true)
        MockGateway.delayFirstRevoke = true
        let replacement = Task { @MainActor in await withCheckedContinuation { continuation in bridge.handle(["operation":"remote_pair"],status:{["ok":true]}) { continuation.resume(returning:$0) } } }
        try await Task.sleep(nanoseconds:80_000_000)
        _ = await bridge.revoke()
        let stopped = await replacement.value
        precondition(stopped["code"] as? String == "remote_pair_cancelled", "Expected cancellation: \(stopped) counts: \(MockGateway.creates), \(MockGateway.revokes)")
        precondition(MockGateway.creates == 1, "Cancel during old revoke must prevent replacement creation")
        print("PASS revoke during replacement cleanup cancels generation intent")
    }
}

final class MockGateway: URLProtocol, @unchecked Sendable {
    static let lock = NSLock()
    static var creates = 0
    static var revokes = 0
    static var delayCreate = false
    static var delayFirstRevoke = false
    static func reset() { lock.lock();defer{lock.unlock()};creates=0;revokes=0;delayCreate=false;delayFirstRevoke=false }
    override class func canInit(with request: URLRequest) -> Bool { request.url?.scheme == "https" }
    override class func canonicalRequest(for request: URLRequest) -> URLRequest { request }
    override func startLoading() {
        if request.url!.path.hasSuffix("/socket") { client?.urlProtocol(self,didFailWithError:URLError(.cancelled)); return }
        Self.lock.lock()
        let pair = request.url!.path == "/api/pair"
        if pair {Self.creates += 1} else {Self.revokes += 1}
        let delay = (pair && Self.delayCreate) || (!pair && Self.delayFirstRevoke && Self.revokes==1)
        Self.lock.unlock()
        let data: [String:Any] = pair ? ["id":String(repeating:"a",count:43),"hostToken":String(repeating:"b",count:43),"pairToken":String(repeating:"c",count:43),"expiresAt":Date().addingTimeInterval(86400).timeIntervalSince1970*1000,"pairUntil":Date().addingTimeInterval(300).timeIntervalSince1970*1000] : ["ok":true]
        DispatchQueue.global().asyncAfter(deadline:.now() + (delay ? 0.3 : 0.01)) { [self] in
            client?.urlProtocol(self,didReceive:HTTPURLResponse(url:request.url!,statusCode:200,httpVersion:nil,headerFields:nil)!,cacheStoragePolicy:.notAllowed)
            client?.urlProtocol(self,didLoad:try! JSONSerialization.data(withJSONObject:data))
            client?.urlProtocolDidFinishLoading(self)
        }
    }
    override func stopLoading() {}
}
