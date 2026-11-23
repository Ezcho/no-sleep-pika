import AppKit

@MainActor
final class PowerController {
    private let model: AppModel
    private let defaults: UserDefaults
    private let send: (PowerAction) throws -> Void
    private var timer: Timer?
    private var sleepObserver: NSObjectProtocol?
    private var intent = UUID()
    private var previousAC: Bool?
    private var wasActive = false
    private(set) var executing = false
    private(set) var schedule: PowerSchedule?
    private(set) var reading = HardwareReading.current()
    private(set) var message = ""
    var onChange: (() -> Void)?
    var isVisible: (() -> Bool)?
    var conditions: PowerConditions {
        didSet {
            defaults.set(conditions.acOnly, forKey: "power.acOnly")
            defaults.set(conditions.stopOnDisconnect, forKey: "power.stopOnDisconnect")
            defaults.set(conditions.batteryFloor, forKey: "power.batteryFloor")
            refresh()
        }
    }

    init(model: AppModel, defaults: UserDefaults = .standard,
         send: @escaping (PowerAction) throws -> Void = MacPowerRequest.send) {
        self.model = model
        self.defaults = defaults
        self.send = send
        let floor = defaults.integer(forKey: "power.batteryFloor")
        conditions = PowerConditions(acOnly: defaults.bool(forKey: "power.acOnly"),
                                     stopOnDisconnect: defaults.bool(forKey: "power.stopOnDisconnect"),
                                     batteryFloor: [0, 30, 40, 50].contains(floor) ? floor : 0)
        model.sessionStartIssue = { [weak self] in
            guard let self else { return nil }
            let reading = HardwareReading.current()
            self.previousAC = reading.onAC
            self.wasActive = true
            return self.conditions.reason(reading: reading, previouslyOnAC: nil)
        }
        let tick = Timer(timeInterval: 5, repeats: true) { [weak self] _ in
            Task { @MainActor in
                guard let self else { return }
                if self.model.active || self.schedule != nil || self.isVisible?() == true { self.refresh() }
            }
        }
        tick.tolerance = 1
        RunLoop.main.add(tick, forMode: .common)
        timer = tick
        sleepObserver = NSWorkspace.shared.notificationCenter.addObserver(forName: NSWorkspace.willSleepNotification, object: nil, queue: .main) { [weak self] _ in
            MainActor.assumeIsolated {
                guard let self, self.schedule != nil || self.executing else { return }
                self.cancel()
                self.message = "Mac이 잠자기에 들어가 예약을 취소했습니다."
                self.onChange?()
            }
        }
    }

    var statusText: String {
        let battery = reading.batteryPercent.map { "배터리 \($0)%" } ?? "배터리 정보 없음"
        return "\(battery) · \(reading.onAC ? "외부 전원" : "배터리 전원") · 발열 \(reading.heat.label)"
    }
    var timerText: String {
        guard let schedule else { return "예약 없음" }
        let minutes = max(0, Int(ceil(schedule.deadline.timeIntervalSinceNow / 60)))
        return "\(schedule.action.title) · 약 \(minutes)분 후"
    }
    func arm(minutes: Int, action: PowerAction) {
        guard !executing, !model.busy, [15,30,60,180,360].contains(minutes) else { return }
        schedule = PowerSchedule(deadline: Date().addingTimeInterval(Double(minutes * 60)), action: action)
        message = "예약은 pika 종료 시 취소됩니다. 잠든 Mac을 깨우지는 않습니다."
        onChange?()
    }
    func cancel() {
        intent = UUID()
        schedule = nil
        message = "예약을 취소했습니다."
        onChange?()
    }
    func refresh(now: Date = Date()) {
        reading = HardwareReading.current()
        let prior = wasActive ? previousAC : nil
        defer { onChange?() }
        guard !executing, !model.busy else { return }
        previousAC = reading.onAC
        wasActive = model.active
        if model.active, let reason = conditions.reason(reading: reading, previouslyOnAC: prior) {
            // A power condition wins over a scheduled shutdown. It only releases Session.
            schedule = nil
            perform(.release, reason: reason)
            return
        }
        if let scheduled = schedule, scheduled.isDue(at: now) {
            schedule = nil // Consume before any asynchronous stop; never retry a power event.
            if scheduled.isStale(at: now) {
                message = "예약 시간이 지나 취소했습니다. 잠자기 후 자동 실행하지 않습니다."
                return
            }
            perform(scheduled.action, reason: "예약 시간이 되었습니다.")
        }
    }
    func perform(_ action: PowerAction, reason: String = "") {
        guard !executing, !model.busy else { return }
        schedule = nil
        executing = true
        intent = UUID()
        let requestedIntent = intent
        let finish: (Bool) -> Void = { [weak self] success in
            guard let self else { return }
            defer { self.executing = false; self.onChange?() }
            guard self.intent == requestedIntent else { return }
            guard success, !self.model.active, !self.model.recoveryRequired else {
                self.message = "잠자기 설정 복구 실패 · 전원 동작을 취소했습니다."
                return
            }
            do {
                try self.send(action)
                self.message = action == .release ? (reason.isEmpty ? "세션을 해제했습니다." : reason) : "\(action.title) 요청을 보냈습니다. 저장 확인 또는 앱의 취소로 완료되지 않을 수 있습니다."
            } catch { self.message = error.localizedDescription }
        }
        if model.active || model.recoveryRequired { model.stop(completion: finish) }
        else { finish(true) }
    }
    func invalidate() {
        intent = UUID()
        timer?.invalidate(); timer = nil; schedule = nil
        if let sleepObserver { NSWorkspace.shared.notificationCenter.removeObserver(sleepObserver) }
        sleepObserver = nil
    }
}
