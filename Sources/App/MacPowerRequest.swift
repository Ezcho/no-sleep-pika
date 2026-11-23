import AppKit
import Carbon

// Ask loginwindow to use the normal application-quit sequence. Never invoke
// shutdown(8), force-quit apps, elevate privileges, or bypass unsaved documents.
enum MacPowerRequest {
    static func send(_ action: PowerAction) throws {
        let eventID: AEEventID
        switch action {
        case .release: return
        case .sleep: eventID = AEEventID(kAESleep)
        case .shutdown: eventID = AEEventID(kAEShutDown)
        case .restart: eventID = AEEventID(kAERestart)
        }
        var psn = ProcessSerialNumber(highLongOfPSN: 0, lowLongOfPSN: UInt32(kSystemProcess))
        var target = AEAddressDesc()
        var event = AppleEvent()
        var reply = AppleEvent()
        let targetStatus = AECreateDesc(DescType(typeProcessSerialNumber), &psn, MemoryLayout.size(ofValue: psn), &target)
        guard targetStatus == noErr else { throw AwakeError("전원 요청 대상을 찾지 못했습니다 (\(targetStatus)).") }
        defer { AEDisposeDesc(&target) }
        let createStatus = AECreateAppleEvent(AEEventClass(kCoreEventClass), eventID, &target,
                                             AEReturnID(kAutoGenerateReturnID), AETransactionID(kAnyTransactionID), &event)
        guard createStatus == noErr else { throw AwakeError("전원 요청을 만들지 못했습니다 (\(createStatus)).") }
        defer { AEDisposeDesc(&event); AEDisposeDesc(&reply) }
        let status = AESendMessage(&event, &reply, AESendMode(kAENoReply), 60)
        guard status == noErr else { throw AwakeError("macOS가 전원 요청을 받지 못했습니다 (\(status)). Apple 메뉴에서 직접 실행해 주세요.") }
    }
}
