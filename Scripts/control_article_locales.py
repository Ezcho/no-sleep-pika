"""pika 1.3.0 web-control article, published after the matching app release."""
COPY = {}
def add(locale, title, intro, headings, body):
    COPY[locale] = dict(title=title, intro=intro, headings=headings.split('|'), paragraphs=[s.strip().split('\n\n') for s in body.strip().split('\n---\n')])

add('ko', 'QR 하나로 Mac을 제어하세요: 휴대폰에서 세션·타이머·종료까지',
'집에 둔 Mac을 계속 켜 둘지, 언제 쉬게 할지 휴대폰에서 정하세요. pika 1.3.0의 QR 연결과 Mac 승인 절차, 원격 제어 범위를 설명합니다.',
'이제 상태 확인 다음 단계까지|먼저 Mac에서 1.3.0으로 업데이트|QR 스캔 후 Mac에서 한 번 승인|휴대폰에서 바꿀 수 있는 것|종료 예약과 60초 취소 시간|연결을 끊으면 권한도 끝납니다|자료와 글의 범위',
'''Mac에 빌드나 다운로드를 맡기고 다른 방으로 이동했습니다. 배터리를 확인하는 것에서 그치지 않고, 이제는 휴대폰으로 세션을 끄거나 종료 시간을 정할 수 있습니다. pika 1.3.0은 기존 QR 상태 화면에 제어 기능을 더했습니다.

예를 들어 세션을 1시간 뒤 해제하도록 예약하거나, 충전기가 빠지면 잠자기 방지를 끝내도록 설정할 수 있습니다. Mac을 종료하거나 재시동하는 요청도 보낼 수 있습니다.

다만 AI에게 새 코딩 지시를 보내는 기능은 아닙니다. AI 대화, 터미널 출력, 작업 진행률이나 화면은 보여주지 않습니다. pika가 제어하는 대상은 Mac의 세션과 전원 동작입니다.
---
먼저 Mac의 pika를 1.3.0 이상으로 업데이트하고 실행해 두세요. 보조 서비스가 정상 연결되어 있어야 덮개를 닫은 상태의 잠자기 방지 기능을 사용할 수 있습니다. Mac과 휴대폰 모두 인터넷 연결이 필요합니다.

개발자를 확인할 수 없다는 경고가 나오면, 공식 홈페이지에서 받은 파일인지 먼저 확인하세요.

파일을 열어 본 뒤 시스템 설정 → 개인정보 보호 및 보안에서 해당 파일의 ‘그래도 열기(버전에 따라 확인 없이 열기)’를 선택하고 macOS의 확인·인증 절차를 진행합니다. 버튼 이름과 위치는 OS 버전에 따라 다를 수 있습니다. 보안 기능 전체를 끄는 명령은 필요하지 않습니다. 막힌 단계에서는 아래 설치 안내를 함께 보세요. 파일이 손상되었거나 악성 소프트웨어가 있다는 경고는 이 허용 절차의 대상이 아닙니다.
---
AI 채팅에 pika 도구를 연결한 상태(pika MCP)에서 ‘pika QR을 만들어 줘’라고 요청하세요. 처음이라면 홈페이지의 MCP 연결 안내부터 따라 하세요. QR은 생성 후 5분 동안 한 번 사용할 수 있습니다. 휴대폰 카메라로 스캔한 뒤 ‘이 Mac에 연결’을 누르세요. 처음에는 상태를 읽는 권한만 있습니다. QR을 만든다고 Session이 자동으로 켜지지는 않습니다.

휴대폰에서 ‘Mac에 제어 허용 요청’을 누르세요. 다음으로 Mac에 뜬 승인 창에서 ‘이 연결에 허용’을 누릅니다. 지금 연결한 휴대폰에 제어 권한을 주는 단계이므로, 외출하기 전에 두 화면을 함께 보며 완료하는 편이 좋습니다. Mac에서 승인하지 않으면 휴대폰은 제어할 수 없습니다.
---
Session은 잠자기 방지를 켜거나 해제하는 스위치입니다. Monitor는 Session이 켜졌을 때만 바꿀 수 있습니다. 덮개 모드에서는 덮개를 닫아야 준비된 화면 설정이 적용됩니다. Monitor 표시는 요청한 설정이며, 실제 화면을 촬영해 확인한 결과는 아닙니다.

전원 조건에서는 ‘충전 중에만 유지’, ‘충전기 분리 시 해제’, 배터리 30·40·50% 이하에서 해제를 선택할 수 있습니다. 기존 배터리·발열 보호는 계속 적용됩니다. 상태 화면의 발열은 정상·주의·높음·위험 단계이며, 섭씨 온도 측정값이 아닙니다.
---
타이머는 15분, 30분, 1시간, 3시간, 6시간 중에서 고릅니다. 시간이 되면 세션 해제, 잠자기, Mac 종료 또는 재시동을 요청하도록 정할 수 있습니다. ‘세션 해제’는 잠자기 방지를 끝내는 동작이며 실행 중인 앱을 강제로 닫지 않습니다.

휴대폰에서 즉시 종료·재시동을 선택하면 먼저 확인을 거치고, Mac에서 60초 카운트다운이 시작됩니다. 잘못 눌렀다면 ‘예약·카운트다운 취소’를 누르세요. 실행 시에는 먼저 원래 잠자기 설정으로 되돌린 뒤 macOS에 요청합니다. 저장되지 않은 문서의 확인 창 때문에 종료가 늦어지거나 취소될 수 있으므로, 요청을 보냈다는 표시를 완료로 해석하지 마세요.
---
원격 제어는 현재 승인한 연결에만 적용됩니다. 연결이 끊기거나 권한을 해제하면 원격 예약과 카운트다운도 취소됩니다. 다시 연결한 경우 제어 권한을 다시 승인해야 합니다. 연결은 QR 발급 시점부터 최대 24시간이며, pika 종료나 Mac 잠자기 상태에서도 예약을 계속 실행하는 기능은 아닙니다.

QR은 다른 사람과 공유하지 마세요. 이동 전에는 중요하지 않은 작업으로 Session 변경과 타이머 취소를 짧게 확인하세요. 연결이 끊겼다면 마지막 상태가 표시될 수 있으므로, 새 상태가 들어오기 전에는 Mac이 꺼졌다고 단정하지 마세요. 잠자기 방지는 인터넷 연결이나 AI 작업의 완료를 보장하지 않습니다.
---
이 글은 no-sleep-pika 제작자가 작성한 자사 앱 사용 안내입니다. pika 1.3.0의 앱·웹 제어 범위를 기준으로 2026년 11월 23일 작성했습니다. 설치 경고의 종류와 설정 경로는 Apple의 공식 안내도 함께 확인하세요.
''')
add('en', 'Control your Mac with a QR code: sessions, timers and shutdown from your phone',
'Choose when your Mac keeps working and when it rests. Learn how pika 1.3.0 pairs your phone, asks for Mac approval and limits remote control.',
'Go beyond checking status|Update the Mac app first|Scan, then approve on your Mac|What the phone can control|Timers and a 60-second cancellation window|Access ends with the connection|Sources and scope',
'''You left a build or download running on your Mac and moved to another room. With pika 1.3.0, the QR dashboard can do more than show status: you can change Session, set a timer, or request shutdown and restart.

This controls pika and Mac power actions. It does not send instructions to an AI agent or show its conversation, terminal output, progress percentage or screen.
---
Update pika on the Mac to 1.3.0 or later and leave it running. Closed-lid sleep prevention needs a working helper service. Both devices need an internet connection.

If macOS cannot verify the developer, first check that the file came from the official site. After trying to open it, use System Settings → Privacy & Security → Open Anyway for that file, then follow macOS confirmation and authentication. Labels vary by OS. Use the installation guide below; do not disable system-wide security.
---
In an AI chat with pika MCP connected, ask for a pika QR. Scan it with your phone camera and connect within five minutes. It is single-use. Pairing initially gives read-only access and does not turn Session on.

Request remote control on the phone, then approve the prompt on the Mac. Do this before leaving, while you can see both devices. Without Mac approval, the phone cannot control it.
---
Session enables or releases sleep prevention. Monitor is available only while Session is on; in closed-lid mode its prepared display policy applies after lid closure. The Monitor value is a requested setting, not a camera view of the physical display.

Power conditions can require external power, release Session when the charger disconnects, or stop at 30, 40 or 50% battery. Existing battery and thermal protections still apply. Heat is a macOS level, not a Celsius reading.
---
Choose a 15-, 30-, 60-, 180- or 360-minute timer, then choose Session release, sleep, shutdown or restart. Releasing Session ends sleep prevention; it does not force-close your apps.

An immediate shutdown or restart request asks for confirmation and starts a 60-second countdown on the Mac. Cancel the timer if you change your mind. pika first restores its sleep settings, then asks macOS to act. Unsaved-document prompts may delay or cancel shutdown. A request sent is not proof that it completed.
---
Control belongs to the currently approved connection. Disconnecting or revoking permission cancels remote timers and countdowns; a new connection needs approval again. Access lasts at most 24 hours from QR issuance. Timers do not continue through pika exit or Mac sleep.

Keep the QR private. Before leaving, try a harmless Session change and timer cancellation. A disconnected page may show its last known values, not proof of shutdown. Sleep prevention cannot guarantee network connectivity or an AI job’s completion.
---
Written by the no-sleep-pika maker on November 23, 2026, for pika 1.3.0. This is a guide to our own app. See Apple’s guidance for installation alerts and current settings names.
''')
add('zh-CN','用一个二维码控制 Mac：手机管理会话、定时与关机',
'pika 1.3.0 让手机不只查看状态，还能在 Mac 授权后管理 Session、定时任务和电源操作。',
'从查看状态到操作|先更新 Mac 上的 pika|扫码后在 Mac 上授权|手机可以控制什么|定时与 60 秒取消时间|连接结束，权限也结束|资料与范围',
'''把编译或下载留在 Mac 上运行后，你可以用手机调整 Session、设置定时，或请求关机、重新启动。pika 1.3.0 在原有二维码状态页中加入了控制功能。

它不负责向 AI 发送新指令，也不显示 AI 对话、终端输出、工作进度或远程桌面。
---
先把 Mac 上的 pika 更新至 1.3.0 或更新版本，并保持运行。合盖防睡眠需要辅助服务正常连接；Mac 和手机都需要联网。

如果 macOS 无法验证开发者，请先确认文件来自官网。尝试打开后，在“系统设置 → 隐私与安全性”中为该文件选择“仍要打开”，再完成系统确认或认证。名称可能随系统版本变化；请参考下方安装说明，不要关闭整机安全保护。
---
在已连接 pika MCP 的 AI 聊天中请求生成 pika 二维码，用手机相机扫描并连接。二维码五分钟内有效，只能使用一次。连接最初只有查看权限，不会自动开启 Session。

在手机上请求远程控制，再到 Mac 的提示窗口批准。建议外出前同时看着两台设备完成；没有 Mac 授权就不能控制。
---
Session 用于开启或解除防睡眠。Monitor 仅在 Session 开启时可选；合盖模式会在盖子关闭后应用已准备的屏幕策略。Monitor 显示请求的设置，不是实际屏幕画面。

电源条件包括仅接电时保持、拔掉充电器时解除，以及电量降到 30、40、50% 时解除。原有电池和发热保护仍有效。发热显示是 macOS 状态等级，不是摄氏温度。
---
定时可选 15、30、60、180、360 分钟，到时解除 Session、睡眠、关机或重新启动。解除 Session 只结束防睡眠，不会强制关闭应用。

立即关机或重新启动需要确认，随后 Mac 开始 60 秒倒计时，可用取消定时撤销。pika 先恢复睡眠设置，再向 macOS 发出请求。未保存文档的提示可能推迟或取消关机；发送成功不等于执行完成。
---
控制权限只属于当前获准的连接。断线或撤销权限会取消远程定时和倒计时，重新连接需要再次批准。连接自二维码发放起最多 24 小时；退出 pika 或 Mac 睡眠后，定时不会继续执行。

不要分享二维码。外出前先测试一次无关紧要的 Session 操作和取消定时。断线页面可能只保留最后状态，不能据此认定 Mac 已关机；防睡眠也不保证网络或 AI 工作完成。
---
本文由 no-sleep-pika 制作者于 2026 年 11 月 23 日编写，说明自家应用 1.3.0 的功能。安装警告和设置名称也请参阅 Apple 官方说明。
''')
add('zh-TW','用一個 QR Code 控制 Mac：手機管理工作階段、計時與關機',
'pika 1.3.0 讓手機不只查看狀態，還能在 Mac 授權後管理 Session、計時器和電源操作。',
'從查看狀態到操作|先更新 Mac 上的 pika|掃碼後在 Mac 上授權|手機可以控制什麼|計時與 60 秒取消時間|連線結束，權限也結束|資料與範圍',
'''把建置或下載留在 Mac 上執行後，你可以用手機調整 Session、設定計時器，或要求關機、重新啟動。pika 1.3.0 在原有 QR 狀態頁加入了控制功能。

它不負責向 AI 傳送新指示，也不顯示 AI 對話、終端機輸出、工作進度或遠端桌面。
---
先將 Mac 上的 pika 更新至 1.3.0 或更新版本，並保持執行。闔蓋防睡眠需要輔助服務正常連線；Mac 和手機都需要網路。

若 macOS 無法驗證開發者，請先確認檔案來自官網。嘗試開啟後，在「系統設定 → 隱私權與安全性」為該檔案選擇「強制打開」，再完成系統確認或認證。名稱會隨版本變動；請參考下方安裝說明，不要關閉整機安全防護。
---
在已連接 pika MCP 的 AI 聊天中要求產生 pika QR Code，用手機相機掃描並連線。QR Code 五分鐘內有效，只能使用一次。初始連線只有查看權限，不會自動開啟 Session。

在手機要求遠端控制，再到 Mac 提示視窗批准。建議外出前同時看著兩台裝置完成；未經 Mac 授權就不能控制。
---
Session 用來開啟或解除防睡眠。Monitor 僅在 Session 開啟時可用；闔蓋模式會在蓋子關閉後套用準備好的螢幕策略。Monitor 顯示要求的設定，不是實際螢幕影像。

電源條件包括僅接電時保持、拔掉充電器時解除，以及電量降到 30、40、50% 時解除。原有電池與發熱保護仍有效。發熱顯示是 macOS 狀態等級，不是攝氏溫度。
---
計時可選 15、30、60、180、360 分鐘，到時解除 Session、睡眠、關機或重新啟動。解除 Session 只結束防睡眠，不會強制關閉 App。

立即關機或重新啟動需要確認，隨後 Mac 開始 60 秒倒數，可用取消計時撤銷。pika 先恢復睡眠設定，再向 macOS 發出要求。未儲存文件的提示可能延遲或取消關機；傳送成功不代表執行完成。
---
控制權限只屬於目前獲准的連線。斷線或撤銷權限會取消遠端計時與倒數，重新連線需要再次批准。連線自 QR 發放起最多 24 小時；退出 pika 或 Mac 睡眠後，計時不會繼續執行。

不要分享 QR Code。外出前先測試不重要的 Session 操作與取消計時。斷線頁面可能只保留最後狀態，不能據此認定 Mac 已關機；防睡眠也不保證網路或 AI 工作完成。
---
本文由 no-sleep-pika 製作者於 2026 年 11 月 23 日撰寫，說明自家 App 1.3.0 的功能。安裝警告與設定名稱也請參閱 Apple 官方說明。
''')
add('ja','QRコードでMacを操作：スマホからセッション・タイマー・電源を管理',
'pika 1.3.0では、Macで承認したスマホからSessionやタイマーを変更し、システム終了を要求できます。接続から解除までを紹介します。',
'状態確認の次の操作へ|Macのアプリを先に更新|QRを読み取り、Macで承認|スマホで操作できること|タイマーと60秒の取消時間|接続とともに権限も終了|資料と対象範囲',
'''Macでビルドやダウンロードを続けながら別の部屋へ。pika 1.3.0なら、スマホで状態を見るだけでなく、Sessionの変更、タイマー設定、システム終了や再起動の要求ができます。

AIへの新しい指示、会話やターミナル出力の閲覧、進捗率の表示、リモートデスクトップは提供しません。
---
Macのpikaを1.3.0以降に更新し、起動したままにします。ふたを閉じてスリープを防ぐには補助サービスが正常に接続されている必要があります。両方の端末にインターネット接続が必要です。

開発元を確認できない警告が出たら、公式サイトから入手したファイルか確認してください。一度開こうとしてから「システム設定 → プライバシーとセキュリティ」で対象の「このまま開く」を選び、macOSの確認・認証に従います。名称はOSで異なるため下のインストール案内も参照し、保護全体を無効にしないでください。
---
pika MCPを接続したAIチャットでpikaのQR作成を依頼し、スマホのカメラで読み取ります。QRは5分以内に1回だけ使用できます。最初は閲覧専用で、接続してもSessionは自動的にONになりません。

スマホで操作権限を要求し、Macの確認画面で許可します。外出前に両端末を見ながら済ませましょう。Macで承認しなければ操作できません。
---
Sessionはスリープ防止を開始・解除します。MonitorはSessionがONのときだけ変更でき、閉じたふた用の画面設定はふたを閉じてから適用されます。Monitorの値は要求した設定であり、実画面の確認結果ではありません。

電源条件ではAC接続時のみ維持、充電器を外したら解除、残量30・40・50%で解除を選べます。既存のバッテリー・熱保護は有効です。発熱表示はmacOSの状態区分で、摂氏温度ではありません。
---
15・30・60・180・360分後にSession解除、スリープ、システム終了、再起動を予約できます。Session解除はスリープ防止を終えるだけで、アプリを強制終了しません。

今すぐ終了・再起動を選ぶと確認後にMacで60秒のカウントダウンが始まります。取り消すにはタイマー取消を使います。pikaがスリープ設定を復元してからmacOSへ要求します。未保存書類の確認で遅延・取消される場合があるため、送信済みを完了とみなさないでください。
---
権限は承認された現在の接続だけに有効です。切断・権限解除で遠隔タイマーとカウントダウンも取り消され、再接続時は再承認が必要です。QR発行から最大24時間で、pika終了やMacのスリープをまたいで予約が動き続けるものではありません。

QRは共有せず、外出前に重要でないSession操作とタイマー取消を試してください。切断後の表示は最後に受信した値の場合があり、Macの終了を証明しません。ネットワークやAI作業の完了も保証しません。
---
no-sleep-pikaの制作者が2026年11月23日に自社アプリ1.3.0について執筆しました。インストール警告と設定名はAppleの公式案内も確認してください。
''')
add('hi','एक QR से Mac नियंत्रित करें: फ़ोन से सेशन, टाइमर और शटडाउन',
'pika 1.3.0 में Mac की अनुमति के बाद फ़ोन से Session, पावर की शर्तें और बंद करने का समय बदलें।',
'सिर्फ़ स्थिति देखने से आगे|पहले Mac ऐप अपडेट करें|स्कैन करें, Mac पर अनुमति दें|फ़ोन से क्या बदल सकता है|टाइमर और 60 सेकंड में रद्द करना|कनेक्शन के साथ अनुमति भी समाप्त|स्रोत और दायरा',
'''Mac पर बिल्ड या डाउनलोड चल रहा है और आप दूसरे कमरे में हैं। pika 1.3.0 के QR पेज से Session बदलें, टाइमर लगाएँ या Mac बंद करने और रीस्टार्ट का अनुरोध भेजें।

यह AI को नया निर्देश नहीं देता। AI चैट, टर्मिनल आउटपुट, काम का प्रतिशत या Mac की स्क्रीन नहीं दिखाई जाती।
---
Mac पर pika 1.3.0 या नया संस्करण चलाएँ। ढक्कन बंद होने पर स्लीप रोकने के लिए सहायक सेवा काम करनी चाहिए। दोनों डिवाइस इंटरनेट से जुड़े रहें।

डेवलपर की पहचान वाली चेतावनी आए तो आधिकारिक वेबसाइट से मिली फ़ाइल की जाँच करें। खोलने की कोशिश के बाद System Settings → Privacy & Security → Open Anyway चुनें और macOS की पुष्टि पूरी करें। नाम बदल सकते हैं; नीचे की इंस्टॉलेशन मदद देखें। सुरक्षा पूरी तरह बंद न करें।
---
pika MCP से जुड़े AI चैट में pika QR बनाने को कहें। फ़ोन के कैमरे से पाँच मिनट के भीतर स्कैन करें; QR एक बार इस्तेमाल होता है। शुरुआत में केवल स्थिति देख सकते हैं। QR बनाने से Session ON नहीं होता।

फ़ोन से नियंत्रण माँगें, फिर Mac पर आए संदेश में अनुमति दें। बाहर जाने से पहले दोनों डिवाइस सामने रखकर यह करें। Mac की अनुमति के बिना नियंत्रण नहीं मिलता।
---
Session स्लीप रोकना चालू या समाप्त करता है। Monitor केवल Session ON होने पर बदलता है; बंद ढक्कन वाली स्क्रीन नीति ढक्कन बंद होने के बाद लागू होती है। उसका मान चुनी गई सेटिंग है, स्क्रीन का वास्तविक दृश्य नहीं।

केवल बाहरी बिजली पर चलाना, चार्जर हटने पर Session समाप्त करना, या बैटरी 30/40/50% पर समाप्त करना चुनें। मौजूदा बैटरी और ताप सुरक्षा बनी रहती है। ताप का स्तर macOS से आता है, °C माप नहीं।
---
15, 30, 60, 180 या 360 मिनट बाद Session समाप्त, स्लीप, शटडाउन या रीस्टार्ट चुनें। Session समाप्त करने से ऐप ज़बरदस्ती बंद नहीं होते।

तुरंत शटडाउन या रीस्टार्ट के लिए पुष्टि के बाद 60 सेकंड की उलटी गिनती होती है; टाइमर रद्द कर सकते हैं। pika पहले स्लीप सेटिंग बहाल करता है। बिना सहेजे दस्तावेज़ का संदेश शटडाउन रोक सकता है: अनुरोध भेजना, पूरा होना नहीं है।
---
अनुमति सिर्फ़ वर्तमान स्वीकृत कनेक्शन की है। डिस्कनेक्ट या अनुमति हटने पर दूरस्थ टाइमर और उलटी गिनती रद्द होते हैं। दोबारा जुड़ने पर फिर अनुमति दें। QR जारी होने से अधिकतम 24 घंटे मिलते हैं; pika बंद या Mac स्लीप होने पर टाइमर नहीं चलता रहता।

QR साझा न करें। पहले छोटे, गैरज़रूरी काम पर Session और रद्द करने की जाँच करें। पुरानी स्थिति दिखने का अर्थ Mac बंद होना नहीं है। नेटवर्क या AI काम पूरा होने की गारंटी नहीं है।
---
no-sleep-pika के निर्माता की अपनी ऐप 1.3.0 की गाइड, 23 नवंबर 2026। इंस्टॉलेशन चेतावनियों के लिए Apple की आधिकारिक मदद भी देखें।
''')
add('id','Kendalikan Mac dengan QR: sesi, timer, dan matikan dari ponsel',
'pika 1.3.0 memungkinkan ponsel mengatur Session dan daya setelah Anda menyetujui koneksinya di Mac.',
'Lebih dari melihat status|Perbarui aplikasi Mac dahulu|Pindai lalu izinkan di Mac|Yang bisa dikendalikan|Timer dan waktu pembatalan 60 detik|Izin berakhir bersama koneksi|Sumber dan cakupan',
'''Tinggalkan proses build atau unduhan di Mac, lalu atur Session, timer, atau permintaan matikan dan mulai ulang dari ponsel. pika 1.3.0 menambahkan kendali pada halaman status QR.

Ini bukan kendali percakapan AI. Tidak ada instruksi baru untuk agen, keluaran terminal, persentase kemajuan pekerjaan, atau tampilan layar Mac.
---
Jalankan pika 1.3.0 atau lebih baru di Mac. Pencegahan tidur saat tutup tertutup memerlukan layanan pembantu yang bekerja. Kedua perangkat memerlukan internet.

Jika pengembang tidak dapat diverifikasi, pastikan berkas berasal dari situs resmi. Setelah mencoba membukanya, buka System Settings → Privacy & Security → Open Anyway untuk berkas itu, lalu ikuti konfirmasi macOS. Nama dapat berbeda; lihat panduan instalasi di bawah. Jangan menonaktifkan seluruh perlindungan.
---
Minta QR pika dalam percakapan AI yang sudah terhubung ke pika MCP. Pindai dengan kamera ponsel dalam lima menit. QR sekali pakai; awalnya hanya memberi akses baca dan tidak menyalakan Session.

Minta kendali dari ponsel, lalu setujui dialog di Mac. Selesaikan saat kedua perangkat masih di depan Anda. Tanpa persetujuan Mac, kendali tidak tersedia.
---
Session menyalakan atau melepas pencegahan tidur. Monitor hanya dapat diubah saat Session ON; kebijakan layar mode tutup tertutup diterapkan setelah tutup ditutup. Nilai Monitor adalah pengaturan yang diminta, bukan bukti keadaan layar fisik.

Pilih hanya saat daya tersambung, lepas Session saat pengisi daya dicabut, atau pada baterai 30/40/50%. Perlindungan baterai dan panas tetap berlaku. Panas adalah tingkat macOS, bukan suhu °C.
---
Pilih 15, 30, 60, 180, atau 360 menit untuk melepas Session, tidur, mematikan, atau memulai ulang. Melepas Session tidak menutup paksa aplikasi.

Permintaan matikan atau mulai ulang langsung memerlukan konfirmasi, lalu hitung mundur 60 detik yang dapat dibatalkan. pika memulihkan pengaturan tidur dahulu. Dialog dokumen belum tersimpan dapat menunda atau membatalkan tindakan; terkirim tidak berarti selesai.
---
Izin berlaku untuk koneksi yang sedang disetujui. Putus koneksi atau cabut izin membatalkan timer jarak jauh dan hitung mundur; sambungan baru perlu persetujuan baru. Akses maksimal 24 jam sejak QR diterbitkan. Timer tidak berjalan terus setelah pika keluar atau Mac tidur.

Jangan bagikan QR. Uji perubahan Session dan pembatalan timer dengan pekerjaan yang tidak penting dahulu. Status lama saat terputus bukan bukti Mac mati. Jaringan dan penyelesaian tugas AI tidak dijamin.
---
Ditulis pembuat no-sleep-pika pada 23 November 2026 untuk aplikasi sendiri, versi 1.3.0. Periksa juga panduan resmi Apple untuk peringatan instalasi.
''')
add('es','Controla tu Mac con un QR: sesiones, temporizadores y apagado desde el móvil',
'pika 1.3.0 permite controlar Session y las opciones de energía desde el móvil, después de aprobar la conexión en el Mac.',
'Más que consultar el estado|Actualiza primero la app del Mac|Escanea y autoriza en el Mac|Qué puedes controlar|Temporizadores y 60 segundos para cancelar|El permiso termina con la conexión|Fuentes y alcance',
'''Deja una compilación o descarga en el Mac y cambia Session, programa un temporizador o solicita apagar y reiniciar desde el móvil. pika 1.3.0 añade controles a la página de estado QR.

No envía nuevas instrucciones a un agente de IA ni muestra conversaciones, salida del terminal, porcentaje de avance o escritorio remoto.
---
Abre pika 1.3.0 o posterior en el Mac. Evitar el reposo con la tapa cerrada requiere un servicio auxiliar operativo. Ambos dispositivos necesitan internet.

Si macOS no verifica al desarrollador, comprueba que el archivo procede del sitio oficial. Tras intentar abrirlo, entra en Ajustes del Sistema → Privacidad y seguridad → Abrir igualmente para ese archivo y sigue la confirmación del sistema. Los nombres varían; consulta la guía de instalación. No desactives la seguridad global.
---
Pide un QR de pika en un chat de IA conectado a pika MCP. Escanéalo con la cámara del móvil en cinco minutos: es de un solo uso. La conexión comienza en modo lectura y no activa Session.

Solicita control en el móvil y acepta el aviso del Mac. Hazlo antes de salir, con ambos dispositivos delante. Sin aprobación en el Mac, no hay control.
---
Session activa o libera la prevención del reposo. Monitor solo se cambia con Session ON; la política de pantalla del modo de tapa cerrada se aplica al cerrar la tapa. Su valor expresa la opción solicitada, no el estado físico comprobado de la pantalla.

Puedes exigir alimentación externa, liberar Session al desconectar el cargador o al llegar al 30, 40 o 50% de batería. Las protecciones existentes siguen vigentes. El calor se muestra como nivel de macOS, no en °C.
---
Programa 15, 30, 60, 180 o 360 minutos y elige liberar Session, reposo, apagado o reinicio. Liberar Session no fuerza el cierre de las aplicaciones.

El apagado o reinicio inmediato pide confirmación e inicia una cuenta atrás cancelable de 60 segundos. pika restaura primero sus ajustes de reposo. Un documento sin guardar puede retrasar o cancelar la acción: solicitud enviada no significa acción completada.
---
El permiso corresponde a la conexión aprobada actual. Desconectar o revocar cancela los temporizadores remotos y la cuenta atrás; una conexión nueva necesita otra aprobación. El acceso dura hasta 24 horas desde la emisión del QR. Los temporizadores no continúan al salir de pika o entrar el Mac en reposo.

No compartas el QR. Prueba primero un cambio de Session y la cancelación con tareas sin importancia. Una página desconectada puede mostrar datos antiguos, no demostrar que el Mac se apagó. No se garantiza la red ni la finalización de tareas de IA.
---
Guía del creador de no-sleep-pika sobre su aplicación 1.3.0, escrita el 23 de noviembre de 2026. Consulta también la documentación oficial de Apple sobre avisos de instalación.
''')
add('fr','Contrôlez votre Mac avec un QR : sessions, minuteurs et extinction depuis le téléphone',
'pika 1.3.0 permet de gérer Session et l’alimentation depuis votre téléphone après une autorisation sur le Mac.',
'Au-delà de la consultation|Mettez d’abord le Mac à jour|Scannez puis autorisez sur le Mac|Les commandes disponibles|Minuteurs et 60 secondes pour annuler|La permission suit la connexion|Sources et portée',
'''Laissez une compilation ou un téléchargement sur le Mac et utilisez votre téléphone pour changer Session, régler un minuteur ou demander l’extinction et le redémarrage. pika 1.3.0 ajoute des commandes à la page QR.

Il ne transmet pas de consignes à un agent IA et n’affiche ni conversations, ni sortie du terminal, ni progression du travail, ni bureau distant.
---
Gardez pika 1.3.0 ou une version ultérieure ouvert sur le Mac. Le maintien éveillé avec le capot fermé nécessite un service auxiliaire fonctionnel. Les deux appareils ont besoin d’internet.

Si macOS ne peut pas vérifier le développeur, vérifiez la provenance officielle du fichier. Après avoir essayé de l’ouvrir, allez dans Réglages Système → Confidentialité et sécurité → Ouvrir quand même pour ce fichier, puis confirmez dans macOS. Les intitulés varient : consultez le guide d’installation sans désactiver la protection générale.
---
Demandez un QR pika dans un chat IA relié à pika MCP. Scannez-le avec l’appareil photo du téléphone dans les cinq minutes. Il est à usage unique. La connexion débute en lecture seule et n’active pas Session.

Demandez le contrôle sur le téléphone, puis acceptez sur le Mac. Faites-le avant de partir, avec les deux appareils devant vous. Sans accord sur le Mac, aucune commande n’est autorisée.
---
Session active ou libère le maintien éveillé. Monitor n’est modifiable que lorsque Session est ON ; sa politique d’affichage en mode capot fermé s’applique à la fermeture. Sa valeur représente le réglage demandé, pas une vérification physique de l’écran.

Vous pouvez exiger le secteur, libérer Session au débranchement ou à 30, 40 ou 50% de batterie. Les protections existantes restent actives. La chaleur est un niveau macOS, pas une température en °C.
---
Réglez 15, 30, 60, 180 ou 360 minutes, puis choisissez libération de Session, veille, extinction ou redémarrage. Libérer Session ne ferme pas les applications de force.

Une demande immédiate d’extinction ou de redémarrage exige une confirmation, puis lance un décompte annulable de 60 secondes. pika restaure d’abord ses réglages de veille. Un document non enregistré peut retarder ou annuler l’opération : envoyé ne veut pas dire terminé.
---
L’autorisation concerne la connexion actuelle. Une déconnexion ou une révocation annule les minuteurs distants et le décompte ; il faut approuver une nouvelle connexion. L’accès dure au maximum 24 heures depuis la création du QR. Les minuteurs ne persistent pas après fermeture de pika ou mise en veille du Mac.

Ne partagez pas le QR. Testez d’abord Session et l’annulation sur une tâche sans importance. Des données anciennes après déconnexion ne prouvent pas que le Mac est éteint. Le réseau et la fin d’un travail IA ne sont pas garantis.
---
Guide de l’auteur de no-sleep-pika sur sa propre application 1.3.0, rédigé le 23 novembre 2026. Consultez aussi Apple pour les avertissements d’installation.
''')
add('de','Mac per QR steuern: Sitzungen, Timer und Ausschalten vom Smartphone',
'Mit pika 1.3.0 steuern Sie Session und Energieoptionen vom Smartphone, nachdem Sie die Verbindung am Mac freigegeben haben.',
'Mehr als den Status ansehen|Zuerst die Mac-App aktualisieren|Scannen und am Mac bestätigen|Diese Funktionen sind steuerbar|Timer und 60 Sekunden zum Abbrechen|Berechtigung gilt nur für die Verbindung|Quellen und Geltungsbereich',
'''Ein Build oder Download läuft auf dem Mac, während Sie in einem anderen Raum sind. Mit pika 1.3.0 ändern Sie Session, setzen Timer oder fordern Ausschalten und Neustart vom Smartphone an.

Neue Aufträge an einen KI-Agenten, KI-Chats, Terminalausgaben, Arbeitsfortschritt oder ein Remote-Desktop sind nicht enthalten.
---
Lassen Sie pika 1.3.0 oder neuer auf dem Mac laufen. Für den Betrieb bei geschlossenem Deckel muss der Hilfsdienst funktionieren. Beide Geräte benötigen Internet.

Kann macOS den Entwickler nicht prüfen, kontrollieren Sie zuerst die offizielle Herkunft der Datei. Nach einem Öffnungsversuch wählen Sie für diese Datei in Systemeinstellungen → Datenschutz & Sicherheit „Dennoch öffnen“ und folgen der Systembestätigung. Namen können abweichen; die Installationshilfe erklärt den Weg. Deaktivieren Sie nicht den gesamten Schutz.
---
Bitten Sie einen mit pika MCP verbundenen KI-Chat um einen pika-QR. Scannen Sie ihn innerhalb von fünf Minuten mit der Handykamera. Er ist einmalig verwendbar. Zunächst erhalten Sie nur Lesezugriff; Session wird dadurch nicht eingeschaltet.

Fordern Sie am Smartphone die Steuerung an und bestätigen Sie am Mac. Erledigen Sie dies vor dem Weggehen mit beiden Geräten vor sich. Ohne Mac-Freigabe ist keine Steuerung möglich.
---
Session schaltet die Ruhezustandsverhinderung ein oder gibt sie frei. Monitor ist nur bei Session ON veränderbar; die Bildschirmregel für geschlossenen Deckel greift nach dem Zuklappen. Der Wert zeigt die angeforderte Einstellung, nicht den überprüften Bildschirmzustand.

Sie können Netzbetrieb verlangen, Session beim Abziehen des Ladegeräts oder bei 30, 40 oder 50% Akku beenden. Vorhandener Akku- und Hitzeschutz bleibt aktiv. Wärme wird als macOS-Stufe angezeigt, nicht in °C.
---
Wählen Sie 15, 30, 60, 180 oder 360 Minuten und danach Session freigeben, Ruhezustand, Ausschalten oder Neustart. Die Session-Freigabe beendet keine App zwangsweise.

Sofortiges Ausschalten oder Neustarten verlangt eine Bestätigung und startet einen abbrechbaren 60-Sekunden-Countdown. pika stellt zuvor seine Energieeinstellungen wieder her. Ungespeicherte Dokumente können die Aktion verzögern oder abbrechen. Gesendet bedeutet nicht abgeschlossen.
---
Die Freigabe gilt nur für die aktuelle Verbindung. Trennung oder Widerruf verwirft entfernte Timer und Countdowns; beim Neuverbinden ist erneut Zustimmung nötig. Der Zugang gilt höchstens 24 Stunden ab QR-Ausgabe. Timer laufen nach Beenden von pika oder Ruhezustand des Mac nicht weiter.

Teilen Sie den QR nicht. Testen Sie Session und Timerabbruch zunächst mit unwichtigen Aufgaben. Alte Werte nach Verbindungsabbruch belegen kein Ausschalten. Netzwerk und Abschluss einer KI-Aufgabe werden nicht garantiert.
---
Anleitung des no-sleep-pika-Herstellers zur eigenen App 1.3.0, erstellt am 23. November 2026. Beachten Sie auch Apples offizielle Hinweise zu Installationswarnungen.
''')
add('pt-BR','Controle o Mac por QR: sessões, temporizadores e desligamento pelo celular',
'O pika 1.3.0 permite controlar Session e energia pelo celular depois de autorizar a conexão no Mac.',
'Além de consultar o estado|Atualize primeiro o aplicativo do Mac|Escaneie e autorize no Mac|O que pode ser controlado|Temporizadores e 60 segundos para cancelar|A permissão acompanha a conexão|Fontes e escopo',
'''Deixe uma compilação ou download no Mac e use o celular para mudar Session, programar um temporizador ou solicitar desligamento e reinício. O pika 1.3.0 acrescenta controles à página do QR.

Ele não envia novas instruções a agentes de IA nem mostra conversas, saída do terminal, porcentagem de progresso ou área de trabalho remota.
---
Mantenha o pika 1.3.0 ou mais recente aberto no Mac. Evitar repouso com a tampa fechada exige um serviço auxiliar funcionando. Os dois aparelhos precisam de internet.

Se o macOS não verificar o desenvolvedor, confira a origem oficial do arquivo. Depois de tentar abri-lo, use Ajustes do Sistema → Privacidade e Segurança → Abrir Mesmo Assim para esse arquivo e siga a confirmação do sistema. Os nomes variam; veja o guia de instalação. Não desative a segurança geral nem use esse procedimento para avisos de malware ou arquivo danificado.
---
Peça um QR do pika no chat de IA conectado às ferramentas pika por MCP. Escaneie com a câmera em até cinco minutos e toque para conectar ao Mac. O QR só funciona uma vez; o acesso inicial é de leitura e não liga Session.

Peça permissão de controle no celular e aceite o aviso no Mac. Faça isso antes de sair, com os dois aparelhos à vista. Sem aprovação no Mac não há controle. A página inicial explica como conectar o MCP se for sua primeira vez.
---
Session ativa ou libera a prevenção de repouso. Monitor só muda com Session ON; no modo de tampa fechada, a configuração de tela é aplicada ao fechar a tampa. O valor Monitor é a configuração solicitada, não uma verificação da tela física.

Escolha manter apenas na tomada, liberar ao desconectar o carregador ou com 30, 40 ou 50% de bateria. As proteções existentes continuam. O calor é um nível do macOS, não uma medida em °C.
---
Escolha 15, 30, 60, 180 ou 360 minutos para liberar Session, repousar, desligar ou reiniciar. Liberar Session não fecha os aplicativos à força.

Desligar ou reiniciar imediatamente exige confirmação e começa uma contagem regressiva cancelável de 60 segundos. Use o botão de cancelar agendamento/contagem. O pika restaura as configurações de repouso antes da solicitação. Documentos não salvos podem atrasar ou cancelar a ação: enviado não significa concluído.
---
A permissão vale para a conexão aprovada atual. Desconectar ou revogar cancela temporizadores remotos e contagens; uma nova conexão exige nova aprovação. O acesso dura no máximo 24 horas a partir da emissão do QR. Os temporizadores não continuam se o pika sair ou o Mac entrar em repouso.

Não compartilhe o QR. Teste primeiro uma alteração simples de Session e o cancelamento. Dados antigos em uma página desconectada não provam que o Mac desligou. Não há garantia de rede ou conclusão de tarefas de IA.
---
Guia do criador do no-sleep-pika sobre o próprio aplicativo 1.3.0, escrito em 23 de novembro de 2026. Consulte também a orientação oficial da Apple sobre avisos de instalação.
''')
add('ru','Управляйте Mac по QR: сеансы, таймеры и выключение с телефона',
'pika 1.3.0 позволяет менять Session и параметры питания с телефона после разрешения на самом Mac.',
'Не только просмотр состояния|Сначала обновите приложение Mac|Сканирование и разрешение на Mac|Доступные команды|Таймеры и 60 секунд для отмены|Разрешение действует в рамках соединения|Источники и область применения',
'''Оставьте сборку или загрузку на Mac и меняйте Session, ставьте таймер либо запрашивайте выключение и перезапуск с телефона. В pika 1.3.0 на странице QR появились команды управления.

Это не управление диалогом с ИИ: новые задания агенту, вывод терминала, процент выполнения и удалённый рабочий стол не доступны.
---
Запустите pika 1.3.0 или новее на Mac. Для работы с закрытой крышкой нужна исправная вспомогательная служба. Оба устройства должны быть в интернете.

Если macOS не может проверить разработчика, проверьте официальный источник файла. После попытки открыть его перейдите в «Системные настройки → Конфиденциальность и безопасность» и разрешите открытие именно этого файла, затем подтвердите в macOS. Названия зависят от ОС; смотрите инструкцию установки. Не отключайте всю защиту и не применяйте этот путь к предупреждениям о вредоносном или повреждённом файле.
---
Попросите QR pika в чате ИИ, где подключены инструменты pika через MCP. Сканируйте камерой в течение пяти минут и нажмите подключение к Mac. QR одноразовый; сначала доступно только чтение, Session автоматически не включается.

Запросите управление на телефоне и разрешите его в окне Mac. Сделайте это до выхода, когда оба устройства перед вами. Без согласия на Mac команды недоступны. Первичное подключение MCP описано на главной странице.
---
Session включает или снимает запрет сна. Monitor меняется только при Session ON; настройка экрана в режиме закрытой крышки применяется после её закрытия. Значение Monitor — запрошенная настройка, а не подтверждение фактического состояния экрана.

Можно требовать питание от сети, снимать Session при отключении зарядки или при заряде 30, 40, 50%. Прежняя защита батареи и от перегрева сохраняется. Нагрев — уровень macOS, а не температура в °C.
---
Выберите 15, 30, 60, 180 или 360 минут и действие: снять Session, сон, выключение, перезапуск. Снятие Session не закрывает приложения принудительно.

Немедленное выключение или перезапуск требует подтверждения и запускает отменяемый отсчёт 60 секунд. Нажмите отмену таймера/отсчёта, если передумали. pika сначала восстанавливает настройки сна. Несохранённый документ может задержать или отменить действие: отправленный запрос не равен завершению.
---
Разрешение относится только к текущему одобренному соединению. Разрыв связи или отзыв отменяет удалённые таймеры и отсчёты; новое соединение нужно одобрить снова. Доступ действует до 24 часов от создания QR. Таймеры не продолжаются после выхода из pika или сна Mac.

Не делитесь QR. Сначала проверьте простое изменение Session и отмену. Старая информация на отключённой странице не доказывает выключение Mac. Сеть и завершение задачи ИИ не гарантируются.
---
Руководство создателя no-sleep-pika о собственном приложении 1.3.0, 23 ноября 2026 года. Для предупреждений установки смотрите также официальную справку Apple.
''')
add('ar','تحكّم في Mac برمز QR: الجلسات والمؤقتات والإيقاف من هاتفك',
'يتيح pika 1.3.0 تغيير Session وإعدادات الطاقة من الهاتف بعد الموافقة على الاتصال من جهاز Mac نفسه.',
'أكثر من عرض الحالة|حدّث تطبيق Mac أولاً|امسح الرمز ثم وافق على Mac|ما الذي يمكنك التحكم فيه؟|المؤقتات ومهلة إلغاء 60 ثانية|تنتهي الصلاحية بانتهاء الاتصال|المصادر ونطاق المقال',
'''اترك عملية بناء أو تنزيل تعمل على Mac، ثم غيّر Session أو اضبط مؤقتاً أو اطلب إيقاف التشغيل وإعادة التشغيل من هاتفك. يضيف pika 1.3.0 أدوات تحكم إلى صفحة QR.

لا يرسل تعليمات جديدة إلى وكيل الذكاء الاصطناعي، ولا يعرض المحادثات أو مخرجات الطرفية أو نسبة تقدم العمل أو سطح مكتب بعيداً.
---
شغّل pika 1.3.0 أو أحدث على Mac. منع السكون مع غطاء مغلق يحتاج إلى خدمة مساعدة تعمل بشكل صحيح. يحتاج الجهازان إلى الإنترنت.

إذا تعذر على macOS التحقق من المطور، تأكد أولاً من أن الملف من الموقع الرسمي. بعد محاولة فتحه، استخدم إعدادات النظام ← الخصوصية والأمان ← فتح على أي حال لهذا الملف، ثم أكمل تأكيد النظام. قد تختلف الأسماء؛ راجع دليل التثبيت. لا تعطّل الحماية العامة ولا تستخدم هذا الإجراء لتحذير من برمجيات ضارة أو ملف تالف.
---
اطلب رمز pika من محادثة AI متصلة بأدوات pika عبر MCP. امسحه بكاميرا الهاتف خلال خمس دقائق واضغط الاتصال بجهاز Mac. الرمز للاستخدام مرة واحدة؛ تبدأ الجلسة بصلاحية القراءة فقط ولا تشغّل Session تلقائياً.

اطلب التحكم من الهاتف ثم وافق في النافذة على Mac. نفّذ ذلك قبل المغادرة وأنت ترى الجهازين. لا يوجد تحكم دون موافقة Mac. يشرح الموقع الرئيسي ربط MCP للمرة الأولى.
---
تشغّل Session منع السكون أو تنهيه. يمكن تغيير Monitor فقط عند تشغيل Session؛ ويطبّق إعداد الشاشة في وضع الغطاء المغلق بعد إغلاقه. قيمته هي الإعداد المطلوب، وليست تأكيداً لحالة الشاشة الفعلية.

يمكن اشتراط الطاقة الخارجية، أو إنهاء Session عند فصل الشاحن، أو عند بطارية 30 أو 40 أو 50%. تبقى حماية البطارية والحرارة الحالية فعالة. الحرارة مستوى من macOS وليست قياساً بالدرجة المئوية.
---
اختر 15 أو 30 أو 60 أو 180 أو 360 دقيقة، ثم إنهاء Session أو السكون أو إيقاف التشغيل أو إعادة التشغيل. إنهاء Session لا يغلق التطبيقات بالقوة.

يتطلب طلب الإيقاف أو إعادة التشغيل الفوري تأكيداً، ثم يبدأ عدّ تنازلي قابل للإلغاء مدته 60 ثانية. استخدم زر إلغاء المؤقت والعدّ. يعيد pika إعدادات السكون أولاً. قد يؤخر مستند غير محفوظ العملية أو يلغيها؛ إرسال الطلب لا يعني اكتمالها.
---
تخص الصلاحية الاتصال المعتمد الحالي فقط. قطع الاتصال أو سحب الإذن يلغي المؤقتات والعدّ البعيد، والاتصال الجديد يحتاج موافقة جديدة. الحد الأقصى 24 ساعة من إصدار QR. لا تستمر المؤقتات بعد إغلاق pika أو دخول Mac في السكون.

لا تشارك QR. اختبر تغييراً بسيطاً في Session والإلغاء أولاً. قد تعرض الصفحة المنقطعة آخر حالة فقط، ولا تثبت إيقاف Mac. لا توجد ضمانات لاستمرار الشبكة أو إتمام عمل AI.
---
دليل من صانع no-sleep-pika لتطبيقه 1.3.0، بتاريخ 23 نوفمبر 2026. راجع أيضاً إرشادات Apple الرسمية لتحذيرات التثبيت.
''')
add('vi','Điều khiển Mac bằng QR: phiên, hẹn giờ và tắt máy từ điện thoại',
'pika 1.3.0 cho phép đổi Session và điều kiện nguồn điện trên điện thoại sau khi bạn chấp thuận ngay trên Mac.',
'Không chỉ xem trạng thái|Cập nhật ứng dụng Mac trước|Quét rồi chấp thuận trên Mac|Những gì có thể điều khiển|Hẹn giờ và 60 giây để hủy|Quyền đi cùng kết nối|Nguồn và phạm vi',
'''Để Mac tiếp tục build hoặc tải xuống, rồi dùng điện thoại đổi Session, đặt hẹn giờ hay yêu cầu tắt và khởi động lại. pika 1.3.0 bổ sung điều khiển vào trang trạng thái QR.

Tính năng này không gửi lệnh mới cho AI, không hiển thị hội thoại, đầu ra terminal, phần trăm công việc hay màn hình điều khiển từ xa.
---
Chạy pika 1.3.0 trở lên trên Mac. Chống ngủ khi đóng nắp cần dịch vụ hỗ trợ hoạt động bình thường. Cả hai thiết bị cần internet.

Nếu macOS không xác minh được nhà phát triển, kiểm tra tệp đến từ trang chính thức. Sau khi thử mở, vào Cài đặt hệ thống → Quyền riêng tư & Bảo mật → Vẫn mở cho tệp đó rồi làm theo xác nhận của macOS. Tên có thể khác; xem hướng dẫn cài đặt. Không tắt bảo vệ toàn hệ thống và không áp dụng cách này cho cảnh báo phần mềm độc hại hoặc tệp hỏng.
---
Yêu cầu tạo QR pika trong cuộc trò chuyện AI đã nối công cụ pika qua MCP. Quét bằng camera trong năm phút rồi bấm kết nối Mac. QR dùng một lần; ban đầu chỉ được xem trạng thái và Session không tự bật.

Yêu cầu quyền điều khiển trên điện thoại, rồi chấp thuận cửa sổ trên Mac. Làm trước khi rời đi, lúc thấy cả hai thiết bị. Không có chấp thuận từ Mac thì không điều khiển được. Trang chủ có hướng dẫn nối MCP lần đầu.
---
Session bật hoặc giải phóng chống ngủ. Monitor chỉ đổi được khi Session ON; cấu hình màn hình ở chế độ đóng nắp áp dụng sau khi đóng. Giá trị Monitor là thiết lập đã yêu cầu, không phải xác nhận màn hình thực tế.

Chọn chỉ duy trì khi cắm nguồn, dừng Session khi rút sạc, hoặc ở mức pin 30, 40, 50%. Bảo vệ pin và nhiệt hiện có vẫn hoạt động. Nhiệt là mức trạng thái macOS, không phải số °C.
---
Chọn 15, 30, 60, 180 hoặc 360 phút, rồi giải phóng Session, ngủ, tắt máy hoặc khởi động lại. Giải phóng Session không buộc ứng dụng đóng.

Tắt hoặc khởi động lại ngay cần xác nhận, sau đó Mac đếm ngược 60 giây và có thể hủy. Dùng nút hủy lịch/đếm ngược nếu đổi ý. pika khôi phục thiết lập ngủ trước. Hộp thoại tài liệu chưa lưu có thể trì hoãn hoặc hủy thao tác: gửi yêu cầu không có nghĩa là đã xong.
---
Quyền chỉ dành cho kết nối đang được duyệt. Ngắt kết nối hoặc thu hồi quyền hủy hẹn giờ từ xa và đếm ngược; kết nối mới cần duyệt lại. Tối đa 24 giờ từ lúc tạo QR. Hẹn giờ không tiếp tục sau khi thoát pika hoặc Mac ngủ.

Không chia sẻ QR. Thử thay đổi Session đơn giản và hủy trước. Trang mất kết nối có thể chỉ hiện trạng thái cũ, không chứng minh Mac đã tắt. Mạng và việc AI hoàn tất không được bảo đảm.
---
Hướng dẫn do nhà phát triển no-sleep-pika viết cho ứng dụng 1.3.0 ngày 23 tháng 11 năm 2026. Xem thêm hướng dẫn chính thức của Apple về cảnh báo cài đặt.
''')
add('th','ควบคุม Mac ด้วย QR: เซสชัน ตัวตั้งเวลา และปิดเครื่องผ่านมือถือ',
'pika 1.3.0 ให้คุณเปลี่ยน Session และเงื่อนไขพลังงานจากมือถือ หลังอนุมัติการเชื่อมต่อบน Mac',
'มากกว่าการดูสถานะ|อัปเดตแอปบน Mac ก่อน|สแกนแล้วอนุมัติบน Mac|มือถือควบคุมอะไรได้บ้าง|ตัวตั้งเวลาและเวลา 60 วินาทีเพื่อยกเลิก|สิทธิ์สิ้นสุดพร้อมการเชื่อมต่อ|แหล่งข้อมูลและขอบเขต',
'''ปล่อยให้ Mac บิลด์งานหรือดาวน์โหลดต่อ แล้วใช้มือถือเปลี่ยน Session ตั้งเวลา หรือขอปิดและเริ่มเครื่องใหม่ pika 1.3.0 เพิ่มปุ่มควบคุมในหน้าสถานะ QR

นี่ไม่ใช่การส่งคำสั่งใหม่ให้ AI และไม่แสดงแชต ผลลัพธ์เทอร์มินัล เปอร์เซ็นต์ความคืบหน้า หรือเดสก์ท็อประยะไกล
---
เปิด pika 1.3.0 หรือใหม่กว่าค้างไว้บน Mac การป้องกันพักเครื่องขณะปิดฝาต้องมีบริการเสริมที่ทำงานได้ ทั้งสองอุปกรณ์ต้องเชื่อมต่ออินเทอร์เน็ต

หาก macOS ยืนยันผู้พัฒนาไม่ได้ ให้ตรวจสอบว่าไฟล์มาจากเว็บไซต์ทางการ หลังลองเปิดไฟล์แล้ว ไปที่การตั้งค่าระบบ → ความเป็นส่วนตัวและความปลอดภัย → เปิดต่อไปสำหรับไฟล์นั้น แล้วทำตามการยืนยันของระบบ ชื่ออาจต่างกัน จึงควรดูคู่มือติดตั้งด้านล่าง อย่าปิดระบบป้องกันทั้งหมดหรือใช้ขั้นตอนนี้กับคำเตือนมัลแวร์หรือไฟล์เสียหาย
---
ขอ QR ของ pika ในแชต AI ที่เชื่อมเครื่องมือ pika ผ่าน MCP สแกนด้วยกล้องภายในห้านาทีแล้วกดเชื่อมต่อ Mac ใช้ QR ได้ครั้งเดียว เริ่มต้นด้วยสิทธิ์ดูอย่างเดียว และไม่ได้เปิด Session อัตโนมัติ

ขอสิทธิ์ควบคุมจากมือถือ แล้วอนุมัติหน้าต่างบน Mac ทำก่อนออกจากบ้านขณะเห็นทั้งสองเครื่อง หากไม่อนุมัติบน Mac จะควบคุมไม่ได้ หน้าแรกมีวิธีเชื่อม MCP สำหรับครั้งแรก
---
Session เปิดหรือยุติการป้องกันพักเครื่อง เปลี่ยน Monitor ได้เมื่อ Session ON เท่านั้น ในโหมดปิดฝา การตั้งค่าจอจะทำงานหลังปิดฝา ค่า Monitor คือสิ่งที่ร้องขอ ไม่ใช่การยืนยันจอจริง

เลือกทำงานเฉพาะเมื่อเสียบไฟ ยุติ Session เมื่อถอดสายชาร์จ หรือเมื่อแบตเตอรี่เหลือ 30, 40 หรือ 50% ระบบป้องกันแบตเตอรี่และความร้อนเดิมยังทำงาน ความร้อนเป็นระดับจาก macOS ไม่ใช่อุณหภูมิ °C
---
เลือก 15, 30, 60, 180 หรือ 360 นาที แล้วเลือกยุติ Session พักเครื่อง ปิดเครื่อง หรือเริ่มใหม่ การยุติ Session ไม่บังคับปิดแอป

การขอปิดหรือเริ่มใหม่ทันทีต้องยืนยัน แล้วมีนับถอยหลัง 60 วินาทีให้ยกเลิก ใช้ปุ่มยกเลิกกำหนดเวลา/นับถอยหลังหากเปลี่ยนใจ pika คืนค่าการพักเครื่องก่อนส่งคำขอ เอกสารที่ยังไม่บันทึกอาจทำให้ล่าช้าหรือยกเลิก จึงไม่ควรถือว่าส่งคำขอแล้วคือทำสำเร็จ
---
สิทธิ์ใช้ได้เฉพาะการเชื่อมต่อที่อนุมัติอยู่ การตัดการเชื่อมต่อหรือถอนสิทธิ์จะยกเลิกตัวตั้งเวลาระยะไกลและการนับถอยหลัง เชื่อมใหม่ต้องอนุมัติใหม่ ใช้ได้สูงสุด 24 ชั่วโมงนับจากสร้าง QR และตัวตั้งเวลาไม่ทำงานต่อเมื่อออกจาก pika หรือ Mac พักเครื่อง

อย่าแชร์ QR ลองเปลี่ยน Session และยกเลิกกับงานที่ไม่สำคัญก่อน หน้าที่ขาดการเชื่อมต่ออาจแสดงค่าเดิม ซึ่งไม่ยืนยันว่า Mac ปิดแล้ว ระบบไม่รับประกันเครือข่ายหรือการทำงานของ AI จนสำเร็จ
---
คู่มือแอป 1.3.0 ของตนเองโดยผู้พัฒนา no-sleep-pika วันที่ 23 พฤศจิกายน 2026 ดูคำแนะนำทางการของ Apple เรื่องคำเตือนติดตั้งประกอบด้วย
''')

# The current phone UI uses Korean labels; preserve them so readers can find the buttons.
UI_STEPS = {
'en': 'The phone buttons currently read “이 Mac에 연결” (connect), then “Mac에 제어 허용 요청” (request control). Approve on the Mac. “예약·카운트다운 취소” cancels a timer or countdown. New to pika MCP? Follow the connection guide linked below first.',
'ko': '아래 MCP 연결 안내를 열면 AI 채팅에 pika 도구를 연결하는 방법을 볼 수 있습니다.',
'zh-CN': '手机按钮目前显示韩语：先点“이 Mac에 연결”（连接），再点“Mac에 제어 허용 요청”（请求控制），最后在 Mac 批准。“예약·카운트다운 취소”用于取消定时或倒计时。首次使用 MCP，请先看下方连接说明。',
'zh-TW': '手機按鈕目前顯示韓文：先點「이 Mac에 연결」（連線），再點「Mac에 제어 허용 요청」（要求控制），最後在 Mac 批准。「예약·카운트다운 취소」用來取消計時或倒數。初次使用 MCP，請先看下方連線說明。',
'ja': 'スマホのボタンは現在韓国語です。「이 Mac에 연결」（接続）→「Mac에 제어 허용 요청」（操作を要求）→Macで承認、の順です。「예약·카운트다운 취소」で予約・カウントダウンを取り消します。MCPが初めてなら下の接続案内から始めてください。',
'hi': 'फ़ोन के बटन अभी कोरियाई में हैं: पहले “이 Mac에 연결” (जोड़ें), फिर “Mac에 제어 허용 요청” (अनुमति माँगें), फिर Mac पर स्वीकृति। “예약·카운트다운 취소” टाइमर रद्द करता है। पहली बार MCP के लिए नीचे की गाइड देखें।',
'id': 'Tombol ponsel saat ini berbahasa Korea: “이 Mac에 연결” untuk terhubung, lalu “Mac에 제어 허용 요청” untuk meminta kendali, kemudian izinkan di Mac. “예약·카운트다운 취소” membatalkan timer. Untuk MCP pertama kali, ikuti panduan di bawah.',
'es': 'Los botones del móvil están actualmente en coreano: “이 Mac에 연결” conecta, “Mac에 제어 허용 요청” solicita control y después autorizas en el Mac. “예약·카운트다운 취소” cancela el temporizador. Para conectar MCP por primera vez, usa la guía siguiente.',
'fr': 'Les boutons du téléphone sont actuellement en coréen : “이 Mac에 연결” pour connecter, puis “Mac에 제어 허용 요청” pour demander le contrôle, avant d’accepter sur le Mac. “예약·카운트다운 취소” annule le minuteur. Le guide ci-dessous explique la première connexion MCP.',
'de': 'Die Handy-Schaltflächen sind derzeit koreanisch: „이 Mac에 연결“ verbindet, „Mac에 제어 허용 요청“ fordert die Steuerung an, danach bestätigen Sie am Mac. „예약·카운트다운 취소“ bricht Timer und Countdown ab. Für die erste MCP-Verbindung nutzen Sie die Anleitung unten.',
'pt-BR': 'Os botões do celular estão em coreano: “이 Mac에 연결” conecta, “Mac에 제어 허용 요청” pede controle e depois você autoriza no Mac. “예약·카운트다운 취소” cancela o temporizador. O guia abaixo explica a primeira conexão MCP.',
'ru': 'Кнопки телефона пока на корейском: «이 Mac에 연결» подключает, «Mac에 제어 허용 요청» запрашивает управление, затем подтвердите на Mac. «예약·카운트다운 취소» отменяет таймер и отсчёт. Первое подключение MCP описано ниже.',
'ar': 'أسماء الأزرار على الهاتف حالياً بالكورية: «이 Mac에 연결» للاتصال، ثم «Mac에 제어 허용 요청» لطلب التحكم، وبعدها الموافقة على Mac. «예약·카운트다운 취소» يلغي المؤقت والعدّ. يشرح الدليل أدناه أول اتصال MCP.',
'vi': 'Nút trên điện thoại hiện bằng tiếng Hàn: “이 Mac에 연결” để nối, “Mac에 제어 허용 요청” để xin quyền, rồi chấp thuận trên Mac. “예약·카운트다운 취소” hủy lịch và đếm ngược. Xem hướng dẫn dưới đây để nối MCP lần đầu.',
'th': 'ปุ่มมือถือขณะนี้เป็นภาษาเกาหลี: “이 Mac에 연결” เพื่อเชื่อมต่อ แล้ว “Mac에 제어 허용 요청” เพื่อขอควบคุม จากนั้นอนุมัติบน Mac ปุ่ม “예약·카운트다운 취소” ใช้ยกเลิกเวลาและนับถอยหลัง ดูคู่มือด้านล่างสำหรับการเชื่อม MCP ครั้งแรก',
}
INSTALL_DISTINCTION = {
'en': 'Warnings about malware or a damaged file are different; do not use this opening exception for those alerts.',
'zh-CN': '恶意软件或文件损坏警告属于不同情况，不应使用此放行步骤。',
'zh-TW': '惡意軟體或檔案損壞警告屬於不同情況，不應使用這項放行步驟。',
'ja': 'マルウェアや破損ファイルの警告は別の問題です。この許可手順を使わず、インストール案内で区別してください。',
'hi': 'मैलवेयर या खराब फ़ाइल की चेतावनी अलग है; उसके लिए यह अनुमति वाला तरीका न अपनाएँ।',
'id': 'Peringatan malware atau berkas rusak adalah masalah berbeda; jangan gunakan pengecualian membuka ini untuk peringatan tersebut.',
'es': 'Los avisos de malware o archivo dañado son distintos; no uses esta excepción para ellos.',
'fr': 'Les alertes de logiciel malveillant ou de fichier endommagé sont différentes : n’utilisez pas cette exception pour les contourner.',
'de': 'Warnungen vor Schadsoftware oder beschädigten Dateien sind ein anderer Fall; verwenden Sie dafür nicht diese Öffnungsausnahme.',
}
MCP_LABELS = {
'en':'MCP connection guide','ko':'MCP 연결 안내','zh-CN':'MCP 连接说明','zh-TW':'MCP 連線說明','ja':'MCP接続ガイド','hi':'MCP कनेक्शन गाइड','id':'Panduan koneksi MCP','es':'Guía de conexión MCP','fr':'Guide de connexion MCP','de':'MCP-Verbindungsanleitung','pt-BR':'Guia de conexão MCP','ru':'Подключение MCP','ar':'دليل اتصال MCP','vi':'Hướng dẫn kết nối MCP','th':'คู่มือเชื่อมต่อ MCP',
}
for locale, copy in COPY.items():
    copy['paragraphs'][2].append(UI_STEPS[locale])
    copy['mcp_guide'] = MCP_LABELS[locale]
    if locale in INSTALL_DISTINCTION:
        copy['paragraphs'][1].append(INSTALL_DISTINCTION[locale])

CONNECTION_NOTE = {
'ko': '연결 끊김을 감지하기까지 수십 초가 걸릴 수 있습니다. 종료를 막으려면 연결을 끊는 대신 ‘예약·카운트다운 취소’를 누르고 취소된 상태를 확인하세요. 원격 예약은 브라우저의 연결 신호가 계속 필요합니다. 휴대폰에서 다른 앱으로 이동해 브라우저가 백그라운드로 전환되면 연결과 예약이 취소될 수 있습니다.',
'en': 'Detecting a lost connection can take tens of seconds. To prevent shutdown, use “예약·카운트다운 취소” and check the canceled state instead of disconnecting. Remote timers need continuing browser connection signals; moving the browser into the background may disconnect it and cancel the timer.',
'zh-CN': '检测断线可能需要数十秒。要阻止关机，请点击“예약·카운트다운 취소”并确认已取消，不要依靠断开连接。远程定时需要浏览器持续发送连接信号；切换到其他应用、让浏览器进入后台，可能导致断线并取消定时。',
'zh-TW': '偵測斷線可能需要數十秒。若要阻止關機，請點「예약·카운트다운 취소」並確認已取消，不要依靠中斷連線。遠端計時需要瀏覽器持續傳送連線訊號；切換到其他 App、讓瀏覽器進入背景，可能導致斷線並取消計時。',
'ja': '切断の検知には数十秒かかる場合があります。終了を止めるには切断せず、「예약·카운트다운 취소」を押して取消済みの状態を確認してください。遠隔タイマーにはブラウザから継続的な接続信号が必要です。他のアプリへ移りブラウザがバックグラウンドになると、接続や予約が取り消される場合があります。',
'hi': 'कनेक्शन टूटने का पता लगने में कई दसियों सेकंड लग सकते हैं। शटडाउन रोकने के लिए डिस्कनेक्ट करने के बजाय “예약·카운트다운 취소” दबाएँ और रद्द स्थिति जाँचें। दूरस्थ टाइमर को ब्राउज़र के लगातार कनेक्शन संकेत चाहिए; ब्राउज़र बैकग्राउंड में जाने पर कनेक्शन और टाइमर रद्द हो सकते हैं।',
'id': 'Putus koneksi dapat memerlukan puluhan detik untuk terdeteksi. Untuk mencegah Mac mati, tekan “예약·카운트다운 취소” dan pastikan status batal, bukan sekadar memutus koneksi. Timer jarak jauh memerlukan sinyal koneksi browser berkelanjutan; memindahkan browser ke latar belakang dapat memutus koneksi dan membatalkan timer.',
'es': 'Detectar una desconexión puede tardar decenas de segundos. Para evitar el apagado, pulsa “예약·카운트다운 취소” y confirma el estado cancelado, en lugar de desconectar. Los temporizadores remotos necesitan señales continuas del navegador; pasar este a segundo plano puede cortar la conexión y cancelar el temporizador.',
'fr': 'La détection d’une coupure peut prendre plusieurs dizaines de secondes. Pour empêcher l’extinction, utilisez “예약·카운트다운 취소” et vérifiez l’annulation plutôt que de vous déconnecter. Les minuteurs distants exigent des signaux réguliers du navigateur ; le passage en arrière-plan peut couper la connexion et annuler le minuteur.',
'de': 'Eine Trennung wird unter Umständen erst nach einigen zehn Sekunden erkannt. Zum Verhindern des Ausschaltens drücken Sie „예약·카운트다운 취소“ und prüfen den Abbruchstatus, statt nur zu trennen. Entfernte Timer benötigen fortlaufende Verbindungssignale des Browsers; im Hintergrund kann die Verbindung abbrechen und der Timer verfallen.',
'pt-BR': 'Detectar uma desconexão pode levar dezenas de segundos. Para impedir o desligamento, pressione “예약·카운트다운 취소” e confira o cancelamento, em vez de apenas desconectar. Temporizadores remotos precisam de sinais contínuos do navegador; colocá-lo em segundo plano pode desconectar e cancelar o temporizador.',
'ru': 'Обнаружение разрыва может занять десятки секунд. Чтобы предотвратить выключение, нажмите «예약·카운트다운 취소» и убедитесь в отмене, а не просто отключайте связь. Удалённым таймерам нужны постоянные сигналы браузера; переход браузера в фон может оборвать связь и отменить таймер.',
'ar': 'قد يستغرق اكتشاف انقطاع الاتصال عشرات الثواني. لمنع الإيقاف، اضغط «예약·카운트다운 취소» وتحقق من حالة الإلغاء بدلاً من قطع الاتصال. تحتاج المؤقتات البعيدة إلى إشارات اتصال مستمرة من المتصفح؛ انتقاله إلى الخلفية قد يقطع الاتصال ويلغي المؤقت.',
'vi': 'Phát hiện mất kết nối có thể mất hàng chục giây. Để ngăn tắt máy, bấm “예약·카운트다운 취소” và xác nhận trạng thái đã hủy thay vì chỉ ngắt kết nối. Hẹn giờ từ xa cần tín hiệu kết nối liên tục từ trình duyệt; đưa trình duyệt xuống nền có thể làm mất kết nối và hủy hẹn giờ.',
'th': 'การตรวจพบว่าขาดการเชื่อมต่ออาจใช้เวลาหลายสิบวินาที หากต้องการหยุดการปิดเครื่อง ให้กด “예약·카운트다운 취소” และตรวจว่าถูกยกเลิกแล้ว แทนการตัดการเชื่อมต่อ ตัวตั้งเวลาระยะไกลต้องมีสัญญาณจากเบราว์เซอร์ต่อเนื่อง การนำเบราว์เซอร์ไปทำงานเบื้องหลังอาจตัดการเชื่อมต่อและยกเลิกเวลา',
}
for locale, copy in COPY.items():
    copy['paragraphs'][5].insert(1, CONNECTION_NOTE[locale])
