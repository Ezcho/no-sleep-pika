import AppKit

@MainActor
final class PowerWindowController: NSWindowController {
    private let power: PowerController
    private let status = NSTextField(wrappingLabelWithString: "")
    private let timerLabel = NSTextField(labelWithString: "")
    private let message = NSTextField(wrappingLabelWithString: "")
    private let acOnly = NSButton(checkboxWithTitle: "충전 중에만 Session 유지", target: nil, action: nil)
    private let disconnect = NSButton(checkboxWithTitle: "충전기 분리 시 Session 해제", target: nil, action: nil)
    private let floor = NSPopUpButton(frame: .zero, pullsDown: false)
    private let duration = NSPopUpButton(frame: .zero, pullsDown: false)
    private let action = NSPopUpButton(frame: .zero, pullsDown: false)
    private var controls: [NSControl] = []
    private let minutes = [15,30,60,180,360]
    private let floors = [0,30,40,50]
    private let actions: [PowerAction] = [.release, .sleep, .shutdown, .restart]

    init(power: PowerController) {
        self.power = power
        let window = NSWindow(contentRect: NSRect(x: 0, y: 0, width: 440, height: 482),
                              styleMask: [.titled, .closable], backing: .buffered, defer: false)
        window.title = "pika · 전원 및 타이머"
        window.isReleasedWhenClosed = false
        super.init(window: window)
        window.center()
        func add(_ view: NSView, _ x: CGFloat, _ y: CGFloat, _ width: CGFloat, _ height: CGFloat) {
            view.frame = NSRect(x: x, y: y, width: width, height: height)
            window.contentView?.addSubview(view)
        }
        status.font = .systemFont(ofSize: 13, weight: .medium)
        add(status, 24, 420, 392, 40)
        let thermalNote = NSTextField(labelWithString: "발열은 macOS 상태 기준이며 °C 측정값이 아닙니다.")
        thermalNote.font = .systemFont(ofSize: 11); thermalNote.textColor = .secondaryLabelColor
        add(thermalNote, 24, 397, 392, 20)
        acOnly.target = self; acOnly.action = #selector(changeConditions)
        disconnect.target = self; disconnect.action = #selector(changeConditions)
        add(acOnly, 24, 355, 392, 25); add(disconnect, 24, 325, 392, 25)
        add(NSTextField(labelWithString: "배터리 사용 시 해제 기준"), 24, 292, 200, 22)
        floor.addItems(withTitles: ["기본 보호", "30% 이하", "40% 이하", "50% 이하"])
        floor.target = self; floor.action = #selector(changeConditions)
        add(floor, 255, 289, 160, 28)
        let protection = NSTextField(wrappingLabelWithString: "기존 보호 기준이 우선 적용됩니다. 조건에 따른 해제는 Mac 종료 명령이 아닙니다.")
        protection.font = .systemFont(ofSize: 11); protection.textColor = .secondaryLabelColor
        add(protection, 24, 245, 392, 36)
        duration.addItems(withTitles: ["15분 후", "30분 후", "1시간 후", "3시간 후", "6시간 후"])
        duration.selectItem(at: 2)
        action.addItems(withTitles: actions.map(\.title))
        add(duration, 24, 205, 112, 28); add(action, 142, 205, 142, 28)
        let arm = NSButton(title: "예약…", target: self, action: #selector(armTimer))
        arm.bezelStyle = .rounded; add(arm, 300, 205, 116, 28)
        add(timerLabel, 24, 171, 290, 24)
        let cancel = NSButton(title: "예약 취소", target: self, action: #selector(cancelTimer))
        cancel.bezelStyle = .rounded; add(cancel, 316, 169, 100, 28)
        let shutdown = NSButton(title: "Mac 종료…", target: self, action: #selector(shutdownNow))
        let restart = NSButton(title: "재시동…", target: self, action: #selector(restartNow))
        for button in [shutdown, restart] { button.bezelStyle = .rounded }
        add(shutdown, 24, 122, 150, 30); add(restart, 184, 122, 150, 30)
        message.font = .systemFont(ofSize: 11); message.textColor = .secondaryLabelColor
        add(message, 24, 20, 392, 90)
        controls = [acOnly, disconnect, floor, duration, action, arm, shutdown, restart]
        update()
    }
    required init?(coder: NSCoder) { fatalError("init(coder:) has not been implemented") }
    func present() { power.refresh(); update(); NSApp.activate(ignoringOtherApps: true); showWindow(nil); window?.makeKeyAndOrderFront(nil) }
    func update() {
        status.stringValue = power.statusText
        timerLabel.stringValue = power.timerText
        message.stringValue = power.message
        if power.message.isEmpty { message.stringValue = "예약은 pika 실행 중에만 유효합니다. 앱 종료 시 취소되며, 잠든 Mac을 깨우지 않습니다. 종료·재시동은 저장 확인으로 지연되거나 취소될 수 있습니다." }
        acOnly.state = power.conditions.acOnly ? .on : .off
        disconnect.state = power.conditions.stopOnDisconnect ? .on : .off
        floor.selectItem(at: floors.firstIndex(of: power.conditions.batteryFloor) ?? 0)
        controls.forEach { $0.isEnabled = !power.executing }
    }
    @objc private func changeConditions() {
        power.conditions = PowerConditions(acOnly: acOnly.state == .on, stopOnDisconnect: disconnect.state == .on,
                                          batteryFloor: floors[max(0, floor.indexOfSelectedItem)])
    }
    private func confirm(_ title: String) -> Bool {
        let alert = NSAlert()
        alert.messageText = title
        alert.informativeText = "실행 전 Session을 해제합니다. 종료·재시동 시 실행 중인 작업이 중단되며, 앱의 저장 확인으로 지연되거나 취소될 수 있습니다. 강제 종료하지 않습니다. 예약은 pika를 종료하면 취소됩니다."
        alert.addButton(withTitle: "취소")
        alert.addButton(withTitle: "확인")
        return alert.runModal() == .alertSecondButtonReturn
    }
    @objc private func armTimer() {
        let selected = actions[max(0, action.indexOfSelectedItem)]
        let delay = minutes[max(0, duration.indexOfSelectedItem)]
        if confirm("\(delay)분 후 \(selected.title)을 예약할까요?") { power.arm(minutes: delay, action: selected) }
    }
    @objc private func cancelTimer() { power.cancel() }
    @objc private func shutdownNow() { if confirm("Mac을 종료할까요?") { power.perform(.shutdown) } }
    @objc private func restartNow() { if confirm("Mac을 재시동할까요?") { power.perform(.restart) } }
}
