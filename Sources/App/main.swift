import AppKit
import OSLog

@MainActor
final class AppDelegate: NSObject, NSApplicationDelegate, NSMenuDelegate, NSWindowDelegate {
    private let logger = Logger(subsystem: AppIdentity.bundleID, category: "Lifecycle")
    let model = AppModel()
    private let controlServer = LocalControlServer()
    private let remotePairing = RemotePairing()
    private var statusItem: NSStatusItem!
    private var statusIcon: PikaStatusIcon?
    private let menu = NSMenu()
    private let sessionRow = MenuSwitchRow(title: "Session")
    private let monitorRow = MenuSwitchRow(title: "Monitor")
    private let setupItem = NSMenuItem(title: "권한 허용…", action: #selector(prepareService), keyEquivalent: "")
    private let errorItem = NSMenuItem(title: "안내…", action: #selector(showMessage), keyEquivalent: "")
    private let removeItem = NSMenuItem(title: "보조 서비스 제거", action: #selector(removeService), keyEquivalent: "")
    private let modeItem = NSMenuItem(title: "", action: nil, keyEquivalent: "")
    private let windowMode = NSTextField(wrappingLabelWithString: "")
    private var pendingTermination = false
    private var updateHandoff = false
    private var updater: AppUpdateController!
    private let updateItem = NSMenuItem(title: "업데이트 확인…", action: #selector(checkForUpdates), keyEquivalent: "")
    private var controlWindow: NSWindow?
    private var setupWindow: SetupWindowController?
    private var power: PowerController!
    private var powerWindow: PowerWindowController?
    private var remoteApproval: NSAlert?
    private let remoteControlItem = NSMenuItem(title: "원격 제어 허용 안 됨", action: #selector(revokeRemoteControl), keyEquivalent: "")
    private let powerStatusItem = NSMenuItem(title: "", action: nil, keyEquivalent: "")
    private let powerTimerItem = NSMenuItem(title: "", action: nil, keyEquivalent: "")
    private let windowSessionRow = MenuSwitchRow(title: "Session")
    private let windowMonitorRow = MenuSwitchRow(title: "Monitor")
    private let windowSetup = NSButton(title: "권한 허용…", target: nil, action: nil)
    private let windowMessage = NSButton(title: "안내…", target: nil, action: nil)

    func applicationDidFinishLaunching(_ notification: Notification) {
        let peers = NSRunningApplication.runningApplications(withBundleIdentifier: AppIdentity.bundleID)
        if let existing = peers.first(where: { $0.processIdentifier != ProcessInfo.processInfo.processIdentifier }) {
            let runningVersion = existing.bundleURL.flatMap { Bundle(url: $0) }?.object(forInfoDictionaryKey: "CFBundleVersion") as? String
            let thisVersion = Bundle.main.object(forInfoDictionaryKey: "CFBundleVersion") as? String
            if runningVersion != thisVersion || existing.bundleURL?.standardizedFileURL != Bundle.main.bundleURL.standardizedFileURL {
                NSApp.setActivationPolicy(.accessory)
                NSApp.activate(ignoringOtherApps: true)
                let alert = NSAlert()
                alert.messageText = "이전 앱을 먼저 종료해 주세요"
                alert.informativeText = "다른 pika 또는 Always Awake가 실행 중입니다. 기존 앱에서 Session을 OFF로 바꾸고 종료한 뒤 pika \(AppIdentity.version)을 다시 실행해 주세요."
                alert.addButton(withTitle: "확인")
                alert.runModal()
                NSApp.terminate(nil)
                return
            }
            if let url = existing.bundleURL {
                let configuration = NSWorkspace.OpenConfiguration()
                configuration.activates = true
                NSWorkspace.shared.openApplication(at: url, configuration: configuration)
            }
            NSApp.terminate(nil)
            return
        }
        NSApp.setActivationPolicy(.accessory)
        menu.autoenablesItems = false
        menu.delegate = self
        let sessionItem = NSMenuItem(title: "Session", action: #selector(toggleSession), keyEquivalent: "")
        sessionItem.target = self
        sessionItem.view = sessionRow
        menu.addItem(sessionItem)
        let monitorItem = NSMenuItem(title: "Monitor", action: #selector(toggleMonitor), keyEquivalent: "")
        monitorItem.target = self
        monitorItem.view = monitorRow
        menu.addItem(monitorItem)
        sessionRow.action = { [weak self] in self?.toggleSession() }
        monitorRow.action = { [weak self] in self?.toggleMonitor() }
        modeItem.isEnabled = false
        menu.addItem(modeItem)
        menu.addItem(.separator())
        let openItem = NSMenuItem(title: "제어창 열기", action: #selector(showControlWindow), keyEquivalent: "")
        openItem.target = self
        menu.addItem(openItem)
        for item in [setupItem, errorItem] { item.target = self; menu.addItem(item) }

        let settingsItem = NSMenuItem(title: "설정", action: nil, keyEquivalent: "")
        let settings = NSMenu()
        settings.autoenablesItems = false
        let guide = NSMenuItem(title: "사용 안내", action: #selector(openGuide), keyEquivalent: "")
        guide.target = self
        settings.addItem(guide)
        let setupGuide = NSMenuItem(title: "설치 안내…", action: #selector(showSetupWindow), keyEquivalent: "")
        setupGuide.target = self
        settings.addItem(setupGuide)
        removeItem.target = self
        settings.addItem(removeItem)
        settingsItem.submenu = settings
        menu.addItem(settingsItem)
        let quit = NSMenuItem(title: "종료", action: #selector(quitApp), keyEquivalent: "q")
        quit.target = self
        menu.addItem(quit)

        statusItem = NSStatusBar.system.statusItem(withLength: NSStatusItem.squareLength)
        statusItem.autosaveName = "AlwaysAwake"
        statusItem.isVisible = true
        logger.notice("Menu bar item created")
        statusItem.button?.target = self
        statusItem.button?.action = #selector(statusClick)
        statusItem.button?.sendAction(on: [.leftMouseUp, .rightMouseUp])
        if let button = statusItem.button { statusIcon = PikaStatusIcon(button: button) }
        updater = AppUpdateController(model: model) { [weak self] in
            guard let self, !self.model.active, !self.model.recoveryRequired else { return }
            self.updateHandoff = true
            NSApp.terminate(nil)
        }
        updater.onChange = { [weak self] in self?.updateItem.title = self?.updater.menuTitle ?? "업데이트 확인…" }
        updateItem.target = self
        menu.insertItem(updateItem, at: menu.numberOfItems - 1)
        let remoteItem = NSMenuItem(title: "휴대폰 연결 해제", action: #selector(revokeRemote), keyEquivalent: "")
        remoteItem.target = self
        menu.insertItem(remoteItem, at: menu.numberOfItems - 1)
        power = PowerController(model: model)
        power.isVisible = { [weak self] in self?.powerWindow?.window?.isVisible == true }
        power.onChange = { [weak self] in self?.updatePowerUI() }
        let powerItem = NSMenuItem(title: "전원 및 타이머…", action: #selector(showPowerWindow), keyEquivalent: "")
        powerItem.target = self
        menu.insertItem(powerItem, at: 3)
        powerStatusItem.isEnabled = false
        powerTimerItem.isEnabled = false
        menu.insertItem(powerStatusItem, at: 3)
        menu.insertItem(powerTimerItem, at: 4)
        power.refresh()
        remoteControlItem.target = self
        remoteControlItem.isEnabled = false
        menu.insertItem(remoteControlItem, at: menu.numberOfItems - 1)
        remotePairing.requestApproval = { [weak self] completion in self?.askRemoteApproval(completion) }
        remotePairing.executeCommand = { [weak self] command, completion in
            guard let self else { completion(false,"failed"); return }
            self.executeRemote(command,completion:completion)
        }
        remotePairing.onControlReset = { [weak self] in
            self?.power.cancelRemoteActions()
            if let alert = self?.remoteApproval { NSApp.endSheet(alert.window,returnCode:NSApplication.ModalResponse.abort.rawValue); alert.window.orderOut(nil); self?.remoteApproval=nil }
        }
        remotePairing.onPermissionChange = { [weak self] enabled in
            self?.remoteControlItem.title = enabled ? "원격 제어 허용됨 · 해제" : "원격 제어 허용 안 됨"
            self?.remoteControlItem.isEnabled = enabled
        }
        model.onChange = { [weak self] in self?.updateMenu() }
        do {
            try controlServer.start { [weak self] request, reply in
                MainActor.assumeIsolated {
                    guard let self else { reply(ControlWire.failure("app_closed", "pika is closing")); return }
                    if let operation = request["operation"] as? String, ["remote_pair", "remote_revoke"].contains(operation) {
                        self.remotePairing.handle(request, status: { [weak self] in self?.remoteStatus() ?? ["ok": false] }, completion: reply)
                    } else { self.model.handleAutomation(request, completion: reply) }
                }
            }
        } catch { logger.error("MCP local control unavailable: \(error.localizedDescription)") }
        updateMenu()
        showControlWindow()
        model.checkHelperConnection()
        updater.checkAutomatically()
    }

    func applicationDidBecomeActive(_ notification: Notification) {
        updater?.checkAutomatically()
        model.checkHelperConnection()
    }

    @objc private func showSetupWindow() {
        menu.cancelTracking()
        if setupWindow == nil {
            setupWindow = SetupWindowController(onInstallHelper: { [weak self] in
                guard let self, !self.model.busy else { return }
                let alert = NSAlert()
                alert.messageText = "pika PKG를 다시 받을까요?"
                alert.informativeText = "앱과 보조 서비스가 함께 들어 있는 PKG를 내려받아 Finder에 표시합니다. 다운로드 완료 후 시작 안내의 ‘pika 종료’를 누르고, 선택된 PKG를 열어 설치해 주세요."
                alert.addButton(withTitle: "다운로드")
                alert.addButton(withTitle: "취소")
                if alert.runModal() == .alertFirstButtonReturn { self.model.installHelper() }
            }, onQuit: { [weak self] in self?.quitApp() }, onOpenPrivacySettings: {
                let settings = URL(string: "x-apple.systempreferences:com.apple.preference.security?General")!
                if !NSWorkspace.shared.open(settings) {
                    NSWorkspace.shared.open(URL(fileURLWithPath: "/System/Applications/System Settings.app"))
                }
            }, onContinue: { [weak self] in
                self?.setupWindow?.close()
                self?.showControlWindow()
            })
        }
        setupWindow?.present(helperReady: model.helperConnected, busy: model.busy, status: model.setupStatus ?? model.error)
    }

    @objc private func showControlWindow() {
        if controlWindow == nil {
            let window = NSWindow(contentRect: NSRect(x: 0, y: 0, width: 264, height: 184),
                                  styleMask: [.titled, .closable, .miniaturizable], backing: .buffered, defer: false)
            window.title = "pika · \(AppIdentity.version)"
            window.delegate = self
            window.isReleasedWhenClosed = false
            window.collectionBehavior = [.moveToActiveSpace]
            window.center()
            windowSessionRow.frame.origin = NSPoint(x: 24, y: 132)
            windowMonitorRow.frame.origin = NSPoint(x: 24, y: 92)
            windowSessionRow.action = { [weak self] in self?.toggleSession() }
            windowMonitorRow.action = { [weak self] in self?.toggleMonitor() }
            windowSetup.target = self
            windowSetup.action = #selector(prepareService)
            windowMessage.target = self
            windowMessage.action = #selector(showMessage)
            for (button, x) in [(windowSetup, CGFloat(24)), (windowMessage, CGFloat(144))] {
                button.bezelStyle = .rounded
                button.controlSize = .small
                button.frame = NSRect(x: x, y: 12, width: 100, height: 26)
            }
            let updateButton = NSButton(title: "업데이트…", target: self, action: #selector(checkForUpdates))
            updateButton.bezelStyle = .rounded
            updateButton.controlSize = .mini
            updateButton.frame = NSRect(x: 172, y: 163, width: 80, height: 20)
            window.contentView?.addSubview(updateButton)
            let powerButton = NSButton(title: "전원·타이머…", target: self, action: #selector(showPowerWindow))
            powerButton.bezelStyle = .rounded
            powerButton.controlSize = .mini
            powerButton.frame = NSRect(x: 24, y: 163, width: 130, height: 20)
            window.contentView?.addSubview(powerButton)
            windowMode.font = .systemFont(ofSize: 11)
            windowMode.textColor = .secondaryLabelColor
            windowMode.frame = NSRect(x: 24, y: 46, width: 216, height: 34)
            for view in [windowSessionRow, windowMonitorRow, windowSetup, windowMessage, windowMode] as [NSView] {
                window.contentView?.addSubview(view)
            }
            controlWindow = window
        }
        power?.refresh()
        updateMenu()
        NSApp.activate(ignoringOtherApps: true)
        controlWindow?.makeKeyAndOrderFront(nil)
        logger.notice("Control window opened")
    }

    func windowWillClose(_ notification: Notification) {
        logger.notice("Control window closed; app remains running")
    }

    @objc func statusClick() {
        if NSApp.currentEvent?.modifierFlags.contains(.option) == true {
            toggleSession()
        } else { showMenu() }
    }

    private func showMenu() {
        guard let button = statusItem?.button else { return }
        statusItem.menu = menu
        button.performClick(nil)
        statusItem.menu = nil
    }

    func menuWillOpen(_ menu: NSMenu) { model.refreshService(); power?.refresh(); updateMenu() }

    private func updateMenu() {
        setupWindow?.update(helperReady: model.helperConnected, busy: model.busy, status: model.setupStatus ?? model.error)
        sessionRow.update(on: model.active, enabled: !model.busy)
        monitorRow.update(on: model.monitorOn, enabled: model.active && !model.busy)
        windowSessionRow.update(on: model.active, enabled: !model.busy)
        windowMonitorRow.update(on: model.monitorOn, enabled: model.active && !model.busy)
        let notice = model.sessionNotice ?? ""
        windowMode.stringValue = notice
        modeItem.title = notice
        modeItem.isHidden = notice.isEmpty
        modeItem.toolTip = notice
        windowSetup.title = "설치 안내…"
        windowSetup.isHidden = model.helperConnected
        windowSetup.isEnabled = !model.busy
        windowMessage.isHidden = model.error == nil && !model.recoveryRequired
        windowMessage.title = model.recoveryRequired ? "복구 필요…" : "안내…"
        setupItem.title = "설치 안내…"
        setupItem.isHidden = model.helperConnected
        setupItem.isEnabled = !model.busy
        errorItem.isHidden = model.error == nil && !model.recoveryRequired
        errorItem.title = model.recoveryRequired ? "복구 필요…" : "안내…"
        errorItem.toolTip = model.error
        removeItem.isHidden = !model.serviceReady && !model.needsApproval
        removeItem.isEnabled = !model.busy
        statusIcon?.update(model.recoveryRequired ? .recovery : model.active ? .on : .off)
    }

    @objc private func toggleSession() {
        guard !model.busy else { return }
        // End menu tracking before starting XPC work or presenting an approval/error.
        menu.cancelTracking()
        DispatchQueue.main.async { [weak self] in
            guard let self else { return }
            self.logger.notice("Session toggle requested")
            self.model.toggleSession { [weak self] in
                guard let self else { return }
                self.updateMenu()
                self.logger.notice("Session toggle completed: active=\(self.model.active)")
                if self.model.error != nil {
                    // A start failure is a runtime diagnostic, not first-run setup.
                    self.showControlWindow()
                    self.showMessage()
                }
            }
        }
    }
    private func remoteStatus() -> [String:Any] {
        var status = model.automationStatus()
        status["power"] = power.remoteStatus
        return status
    }
    private func askRemoteApproval(_ completion: @escaping (Bool) -> Void) {
        guard remoteApproval == nil, !model.busy, !power.executing else { completion(false); return }
        showControlWindow()
        guard let window = controlWindow, window.attachedSheet == nil else { completion(false); return }
        let alert = NSAlert()
        alert.messageText = "연결된 휴대폰의 Mac 제어를 허용할까요?"
        alert.informativeText = "QR을 스캔한 기기에서 Session·Monitor, 타이머, 전원 조건, Mac 종료·재시동을 제어할 수 있습니다. 본인이 요청한 경우만 허용하세요. 종료·재시동은 60초 카운트다운 후 요청되며 취소할 수 있습니다. 재연결하면 다시 승인해야 합니다."
        alert.addButton(withTitle: "허용 안 함")
        alert.addButton(withTitle: "이 연결에 허용")
        remoteApproval = alert
        alert.beginSheetModal(for:window) { [weak self, weak alert] response in
            guard let self, self.remoteApproval === alert else { completion(false); return }
            self.remoteApproval = nil
            completion(response == .alertSecondButtonReturn)
        }
    }
    @objc private func revokeRemoteControl() { remotePairing.revokeControl() }
    private func executeRemote(_ command: RemoteCommand, completion: @escaping (Bool,String) -> Void) {
        if case .cancel = command {
            guard power.schedule != nil || power.executing else { completion(false,"failed"); return }
            power.cancel(); completion(true,"cancelled"); return
        }
        guard !model.busy, !power.executing else { completion(false,"busy"); return }
        switch command {
        case .session(let enabled), .monitor(let enabled):
            let operation: String
            if case .session = command { operation = "set_session" } else { operation = "set_monitor" }
            model.handleAutomation(["operation":operation,"enabled":enabled]) { result in
                let ok = result["ok"] as? Bool == true
                completion(ok, ok ? "accepted" : "failed")
            }
        case .conditions(let conditions): power.conditions = conditions; completion(true,"accepted")
        case .schedule(let minutes, let action): power.arm(minutes:minutes,action:action,remote:true); completion(true,"accepted")
        case .shutdown: power.armRemotePower(.shutdown); showPowerWindow(); completion(true,"accepted")
        case .restart: power.armRemotePower(.restart); showPowerWindow(); completion(true,"accepted")
        case .cancel: break
        }
    }
    private func updatePowerUI() {
        powerStatusItem.title = power.statusText
        powerTimerItem.title = power.timerText
        powerTimerItem.isHidden = power.schedule == nil
        powerWindow?.update()
    }
    @objc private func showPowerWindow() {
        menu.cancelTracking()
        if powerWindow == nil { powerWindow = PowerWindowController(power: power) }
        powerWindow?.present()
    }
    @objc private func toggleMonitor() { model.setMonitor(!model.monitorOn) }
    @objc private func prepareService() { showSetupWindow() }
    @objc private func removeService() { menu.cancelTracking(); model.removeService() }
    @objc private func checkForUpdates() { menu.cancelTracking(); updater.present() }
    @objc private func openGuide() {
        if let url = Bundle.main.url(forResource: "Guide", withExtension: "html") { NSWorkspace.shared.open(url) }
    }
    @objc private func showMessage() {
        menu.cancelTracking()
        let alert = NSAlert()
        alert.messageText = model.recoveryRequired ? "잠자기 설정 복구" : "pika"
        alert.informativeText = model.error ?? "Session 스위치를 눌러 잠자기 설정을 복구해 주세요."
        alert.addButton(withTitle: "확인")
        NSApp.activate(ignoringOtherApps: true)
        alert.runModal()
    }
    @objc private func revokeRemote() {
        Task {
            let result = await remotePairing.revoke()
            let alert = NSAlert()
            alert.messageText = result["ok"] as? Bool == true ? "휴대폰 연결이 해제되었습니다" : "서버 연결 해제 확인 필요"
            alert.informativeText = result["message"] as? String ?? "Mac의 Session 설정은 유지됩니다."
            alert.runModal()
        }
    }
    @objc private func quitApp() { menu.cancelTracking(); NSApp.terminate(nil) }
    func applicationShouldHandleReopen(_ sender: NSApplication, hasVisibleWindows flag: Bool) -> Bool { showControlWindow(); return true }
    func applicationShouldTerminateAfterLastWindowClosed(_ sender: NSApplication) -> Bool { false }
    func applicationWillTerminate(_ notification: Notification) { power?.invalidate(); remotePairing.stopConnection(); statusIcon?.invalidate() }

    func applicationShouldTerminate(_ sender: NSApplication) -> NSApplication.TerminateReply {
        if updateHandoff && !model.active && !model.recoveryRequired { model.client.invalidate(); return .terminateNow }
        guard model.active || model.recoveryRequired || model.busy else { model.client.invalidate(); return .terminateNow }
        guard !pendingTermination else { return .terminateCancel }
        if model.busy { return .terminateCancel }
        pendingTermination = true
        model.stop { [weak self] success in
            self?.pendingTermination = false
            sender.reply(toApplicationShouldTerminate: success)
            if !success { self?.showMenu() }
        }
        return .terminateLater
    }
}

MainActor.assumeIsolated {
    if CommandLine.arguments.contains("--unregister-service") {
        ServiceDiagnostics.unregisterLegacyService()
        RunLoop.main.run()
        exit(1)
    }
    if CommandLine.arguments.contains("--repair-service") {
        ServiceDiagnostics.repairRegistration()
        RunLoop.main.run()
        exit(1)
    }
    if CommandLine.arguments.contains("--check-service") || CommandLine.arguments.contains("--test-session") {
        ServiceDiagnostics.run(testSession: CommandLine.arguments.contains("--test-session"))
        RunLoop.main.run()
        exit(1)
    }
    let app = NSApplication.shared
    let delegate = AppDelegate()
    app.delegate = delegate
    withExtendedLifetime(delegate) { app.run() }
}
