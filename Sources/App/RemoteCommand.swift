import Foundation
import CoreFoundation

enum RemoteCommand {
    case session(Bool), monitor(Bool), conditions(PowerConditions), schedule(Int, PowerAction), cancel, shutdown, restart
    static func parse(_ action: String, _ args: [String: Any]) -> RemoteCommand? {
        func keys(_ values: [String]) -> Bool { Set(args.keys) == Set(values) }
        func boolean(_ key: String) -> Bool? {
            guard let n = args[key] as? NSNumber, CFGetTypeID(n) == CFBooleanGetTypeID() else { return nil }
            return n.boolValue
        }
        func integer(_ key: String) -> Int? {
            guard let n = args[key] as? NSNumber, CFGetTypeID(n) != CFBooleanGetTypeID(), n.doubleValue.isFinite,
                  n.doubleValue >= 0, n.doubleValue <= 1000, n.doubleValue.rounded() == n.doubleValue else { return nil }
            return n.intValue
        }
        switch action {
        case "set_session": if keys(["enabled"]), let v = boolean("enabled") { return .session(v) }
        case "set_monitor": if keys(["enabled"]), let v = boolean("enabled") { return .monitor(v) }
        case "set_conditions":
            if keys(["acOnly","stopOnDisconnect","batteryFloor"]), let ac = boolean("acOnly"), let stop = boolean("stopOnDisconnect"), let floor = integer("batteryFloor"), [0,30,40,50].contains(floor) {
                return .conditions(PowerConditions(acOnly: ac, stopOnDisconnect: stop, batteryFloor: floor))
            }
        case "schedule":
            if keys(["minutes","action"]), let m = integer("minutes"), [15,30,60,180,360].contains(m), let raw = args["action"] as? String, let a = PowerAction(rawValue: raw) { return .schedule(m,a) }
        case "cancel_timer": if args.isEmpty { return .cancel }
        case "shutdown": if args.isEmpty { return .shutdown }
        case "restart": if args.isEmpty { return .restart }
        default: break
        }
        return nil
    }
}

/// Connection-specific permission; no grant survives reconnect or app restart.
struct RemoteAuthorization {
    private(set) var viewer: String?
    private(set) var approved: String?
    private(set) var grant: String?
    private var seen = Set<String>()
    mutating func connect(_ id: String?) {
        if viewer != id { viewer = id; approved = nil; grant = nil; seen.removeAll() }
    }
    mutating func approve(_ id: String) -> Bool {
        guard viewer == id else { return false }; approved = id; grant = UUID().uuidString.lowercased(); return true
    }
    mutating func revoke() { approved = nil; grant = nil; seen.removeAll() }
    mutating func accept(id: String, viewer: String, expires: Double, cancel: Bool, now: Double, grantID: String) -> Bool {
        guard self.viewer == viewer, approved == viewer, grant == grantID.lowercased(), UUID(uuidString: id) != nil,
              expires.isFinite, expires > now, expires <= now + 20_000, !seen.contains(id.lowercased()) else { return false }
        // Cancellation remains available after the mutation budget is exhausted.
        guard cancel || seen.count < 256 else { return false }
        if seen.count < 256 { seen.insert(id.lowercased()) }
        return true
    }
}
