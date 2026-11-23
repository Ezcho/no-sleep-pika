import Foundation
import AppKit

// Inert collaborators: no XPC, real power events or installed app changes.
enum HardwareReading {
    static var reading = SafetyReading(batteryPercent: 80, onAC: true, lidClosed: false, hasExternalDisplay: false, heat: .normal)
    static func current() -> SafetyReading { reading }
}
enum MacPowerRequest { static func send(_ action: PowerAction) throws { fatalError("Real power actions forbidden in tests") } }
@MainActor final class AppModel {
    var active = false
    var busy = false
    var recoveryRequired = false
    var sessionStartIssue: (() -> String?)?
    var stopCount = 0
    var pending: ((Bool) -> Void)?
    func stop(completion: ((Bool) -> Void)? = nil) { busy = true; stopCount += 1; pending = completion }
    func complete(_ success: Bool) { busy = false; if success { active = false; recoveryRequired = false }; let callback = pending; pending = nil; callback?(success) }
}
var checks = 0
func check(_ condition: Bool, _ name: String) {
    precondition(condition, name); checks += 1; print("PASS \(name)")
}
MainActor.assumeIsolated {
    let suite = "pika.power.tests.\(UUID().uuidString)"
    let defaults = UserDefaults(suiteName: suite)!
    defer { defaults.removePersistentDomain(forName: suite) }
    let model = AppModel()
    var requests: [PowerAction] = []
    let power = PowerController(model: model, defaults: defaults, send: { requests.append($0) })
    defer { power.invalidate() }
    model.active = true
    power.perform(.shutdown)
    check(requests.isEmpty && model.stopCount == 1, "shutdown waits for restoration")
    model.complete(false)
    check(requests.isEmpty && !power.executing, "failed restoration blocks shutdown")
    power.perform(.restart)
    power.cancel()
    model.complete(true)
    check(requests.isEmpty && !power.executing, "cancel while restoration pending prevents restart")
    model.active = true
    power.perform(.shutdown)
    NSWorkspace.shared.notificationCenter.post(name: NSWorkspace.willSleepNotification, object: nil)
    model.complete(true)
    check(requests.isEmpty, "sleep during restoration cancels pending shutdown")
    power.arm(minutes: 15, action: .shutdown)
    NSWorkspace.shared.notificationCenter.post(name: NSWorkspace.willSleepNotification, object: nil)
    check(power.schedule == nil, "sleep cancels armed timer")
    model.active = true
    power.perform(.restart)
    model.complete(true)
    check(requests == [.restart], "restored session permits one restart request")
    power.arm(minutes: 15, action: .shutdown)
    let due = power.schedule!.deadline
    power.refresh(now: due)
    power.refresh(now: due.addingTimeInterval(1))
    check(requests == [.restart, .shutdown], "deadline fires only once")
    power.arm(minutes: 15, action: .shutdown)
    power.refresh(now: power.schedule!.deadline.addingTimeInterval(61))
    check(requests.count == 2 && power.schedule == nil, "overdue schedule is canceled")
    power.arm(minutes: -1, action: .shutdown)
    check(power.schedule == nil, "invalid duration rejected")
    HardwareReading.reading.onAC = false
    power.conditions = PowerConditions(acOnly: true)
    check(model.sessionStartIssue?() != nil, "AC-only condition blocks local and MCP start")
    power.conditions = PowerConditions(stopOnDisconnect: true)
    HardwareReading.reading.onAC = true
    _ = model.sessionStartIssue?()
    model.active = true
    HardwareReading.reading.onAC = false
    power.refresh()
    check(model.pending != nil, "disconnect after session start releases session")
    model.complete(true)
    check(requests.last == .release, "power conditions never shut down Mac")
    let count = requests.count
    power.refresh()
    check(requests.count == count, "idle state does not repeatedly release")
    var reading = HardwareReading.reading
    reading.batteryPercent = 30
    let conditions = PowerConditions(batteryFloor: 30)
    check(conditions.reason(reading: reading, previouslyOnAC: nil) != nil, "battery threshold is inclusive")
    reading.batteryPercent = nil
    check(conditions.reason(reading: reading, previouslyOnAC: nil) != nil, "unknown battery fails closed when threshold set")
    reading.onAC = true
    check(conditions.reason(reading: reading, previouslyOnAC: nil) == nil, "battery threshold does not stop AC session")
    check(conditions.batteryFloor > SafetyProfile.closed.batteryFloor, "custom thresholds cannot weaken existing closed-lid protection")
    model.active = false
    power.armRemotePower(.shutdown)
    check(power.schedule?.countdown == true && power.schedule!.deadline.timeIntervalSinceNow > 59, "remote shutdown has 60-second countdown")
    power.cancelRemoteActions()
    check(power.schedule == nil, "disconnect cancels remote countdown")
    power.arm(minutes: 15, action: .shutdown, remote: true)
    model.active = true
    power.conditions = PowerConditions()
    power.refresh(now: power.schedule!.deadline)
    power.cancelRemoteActions()
    let beforeRemoteStop = requests.count
    model.complete(true)
    check(requests.count == beforeRemoteStop, "disconnect cancels remote execution awaiting restoration")
    power.arm(minutes: 15, action: .release)
    power.cancelRemoteActions()
    check(power.schedule != nil, "remote revocation preserves local timer")
    power.cancel()
    let reopened = PowerController(model: AppModel(), defaults: defaults, send: { _ in })
    check(reopened.schedule == nil, "restart never restores destructive timer")
    reopened.invalidate()
}
print("\(checks) power checks passed")
