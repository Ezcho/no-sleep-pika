import Foundation

enum PowerAction: String, CaseIterable {
    case release, sleep, shutdown, restart
    var title: String {
        switch self {
        case .release: return "세션 해제"
        case .sleep: return "Mac 잠자기"
        case .shutdown: return "Mac 종료"
        case .restart: return "Mac 재시동"
        }
    }
}

struct PowerConditions {
    var acOnly = false
    var stopOnDisconnect = false
    var batteryFloor = 0

    func reason(reading: SafetyReading, previouslyOnAC: Bool?) -> String? {
        if acOnly && !reading.onAC { return "충전 중에만 유지하도록 설정되어 세션을 해제합니다." }
        if stopOnDisconnect && previouslyOnAC == true && !reading.onAC {
            return "충전기가 분리되어 세션을 해제합니다."
        }
        if batteryFloor > 0 && !reading.onAC {
            guard let percent = reading.batteryPercent else { return "배터리 잔량을 확인할 수 없어 세션을 해제합니다." }
            if percent <= batteryFloor { return "배터리 \(percent)% · 설정한 기준에 도달하여 세션을 해제합니다." }
        }
        return nil
    }
}

struct PowerSchedule {
    let deadline: Date
    let action: PowerAction
    var remote = false
    var countdown = false
    // A sleeping Mac must not unexpectedly shut down when the user opens it later.
    func isStale(at now: Date) -> Bool { now.timeIntervalSince(deadline) > 60 }
    func isDue(at now: Date) -> Bool { now >= deadline }
}
