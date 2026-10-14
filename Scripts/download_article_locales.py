"""Download troubleshooting guide, published 2026-10-11."""
COPY = {}
def add(locale, title, intro, headings, body):
    COPY[locale] = dict(title=title, intro=intro, headings=headings.split('|'), paragraphs=[s.strip().split('\n\n') for s in body.strip().split('\n---\n')])

add('ko','맥북 다운로드가 멈출 때: 화면 끄기·잠자기·덮개 닫힘 구분하기',
'대용량 파일을 받다가 Mac 다운로드가 멈췄나요? 네트워크·저장 공간부터 확인하고, caffeinate와 pika로 작업을 유지하는 방법을 알아봅니다.',
'다운로드가 멈춘 시점부터 확인하기|화면을 꺼도 다운로드는 계속될까?|덮개를 열어 둔다면 caffeinate|덮개를 닫으면 조건이 달라진다|pika로 덮고 다운로드 유지하기|완료 확인과 자주 묻는 질문|참고 자료',
'''대용량 파일을 받기 시작하고 자리를 비웠는데, 돌아와 보니 진행률이 그대로인 경우가 있습니다. 먼저 다운로드 앱에서 ‘일시 정지’, ‘네트워크 오류’, ‘저장 공간 부족’, ‘로그인 필요’ 같은 메시지를 확인하세요. 화면이 어두워졌다는 사실만으로 절전이 원인이라고 단정할 수는 없습니다.

덮개를 열어 놓고 사용 중인데도 전송이 끊긴다면 Wi-Fi·VPN, 다운로드 서버, 남은 저장 공간부터 점검하는 편이 빠릅니다. 특히 시간이 지나면 만료되는 다운로드 링크는 Mac을 깨워 두어도 실패할 수 있습니다. 받던 앱을 종료했거나 다운로드를 취소한 경우도 절전 방지로 복구되지 않습니다.

반대로 화면을 잠그거나 덮개를 닫은 직후에만 반복해서 멈춘다면 전원 상태를 함께 확인하세요. ‘어느 시점에, 어떤 오류와 함께 멈췄는가’를 기록하면 설정을 여러 개 바꾸지 않고도 원인을 좁힐 수 있습니다.
---
화면 꺼짐은 디스플레이 상태이고 시스템 잠자기는 컴퓨터의 실행 상태입니다. 화면이 꺼져 있거나 잠겨 있어도 Mac이 깨어 있고 다운로드 앱과 연결이 정상이라면 전송을 계속할 수 있습니다. 하지만 잠근 뒤 나중에 시스템이 자동 잠자기에 들어갈 수도 있으므로, 검은 화면만으로 진행 여부를 알 수 없습니다.

전원을 연결하고 덮개를 열어 사용하는 경우, 지원되는 Mac에서는 시스템 설정의 배터리 → 옵션에 있는 ‘전원 어댑터 사용 시 디스플레이가 꺼져 있을 때 자동으로 잠자지 않게 하기’ 항목을 확인할 수 있습니다. 위치와 제공 여부는 모델과 macOS에 따라 달라집니다. 잠금 암호를 끄거나 디스플레이를 계속 밝게 유지할 필요는 없습니다.

‘네트워크 접근 시 깨우기’는 임의의 다운로드를 밤새 계속 실행하는 설정과 같지 않습니다. Apple은 이를 공유 서비스 접근 등을 위한 짧은 깨우기로 설명합니다. 다운로드 작업의 진행 여부는 직접 확인해야 합니다.
---
일회성 다운로드라면 macOS 기본 명령어 caffeinate로 일정 시간 동안 유휴 잠자기를 막도록 요청할 수 있습니다. 아래 명령은 1시간 동안 유휴 시스템 잠자기 방지 요청을 유지합니다. 명령을 실행한 터미널을 열어 두고 별도의 브라우저나 다운로드 앱에서 전송을 진행하세요. 미리 끝내려면 해당 터미널에서 Ctrl+C를 누릅니다.

화면까지 계속 켜 두려는 목적이 아니라면 -d 옵션을 덧붙일 필요는 없습니다. caffeinate의 -i는 유휴 시스템 잠자기, -d는 디스플레이 잠자기와 관련된 옵션입니다. -t의 시간 단위는 초입니다. 1시간이 지나면 요청이 끝나므로 다운로드 예상 시간보다 너무 짧게 잡지 마세요.

이 명령은 네트워크 재시도나 전송 재개를 해주는 다운로드 관리자가 아닙니다. 수동 잠자기, 덮개 닫힘, 전원 부족 등 모든 상황의 연속 실행을 보장하지도 않습니다. 실제 옵션 설명은 자신의 Mac에서 man caffeinate로 확인할 수 있습니다.
---
덮개를 연 상태에서 성공했다고 닫은 상태에서도 같다고 생각하면 안 됩니다. 외장 디스플레이로 일하는 클램쉘 구성은 전원과 외장 키보드·마우스, 해당 Mac이 지원하는 디스플레이 조건을 확인해야 합니다. 충전기만 연결한 상태를 완성된 클램쉘 구성으로 볼 수는 없습니다.

외장 화면 없이 덮고 백그라운드 전송만 유지하려는 경우는 별도로 확인해야 합니다. 먼저 중요하지 않은 짧은 전송으로 테스트하고, 덮기 전 파일 크기나 받은 용량을 기록한 뒤 다시 열었을 때 늘었는지 비교하세요. 앱 창이 그대로 남아 있다는 것만으로 덮여 있던 동안 전송이 진행됐다고 판단하지 마세요.
---
pika를 설치하고 보조 서비스가 준비된 상태에서 다운로드를 시작합니다. Session을 ON으로 준비하고, 화면 유지가 필요 없다면 Monitor는 OFF로 둔 다음 덮개를 닫으세요. 현재 pika는 덮개를 연 채 Session이나 Monitor를 변경했다는 이유만으로 화면을 즉시 끄는 방식이 아니며 화면 정책은 덮개를 닫은 뒤 적용합니다.

몇 분 후 다시 열어 다운로드 앱의 받은 용량과 상태를 확인하세요. 완료 후에는 Session을 OFF로 돌립니다. Session OFF는 잠자기 방지를 해제하고 Monitor 표시도 OFF로 바꾸지만, 그 순간 화면을 즉시 끄는 명령은 아닙니다. pika가 다운로드 앱의 오류를 대신 처리하거나 전송 완료를 판단해 주는 것은 아닙니다.

장시간 전송은 전원을 연결하고 통풍되는 책상 위에서 먼저 확인하세요. 배터리·열 보호나 보조 서비스 문제로 세션이 중단될 수 있습니다. 밀폐된 가방에 넣고 계속 실행하는 용도로 생각하지 마세요.
---
진행률이 100%로 보이는 것과 파일이 정상적으로 저장됐다는 것은 구분해서 확인하는 편이 좋습니다. 다운로드 앱이 완료로 표시하는지, 파일 크기가 예상과 맞는지, 제공자가 체크섬을 공개했다면 무결성이 맞는지 확인하세요. 실패한 전송은 해당 앱이 지원하는 재개 기능을 사용하고, 링크가 만료됐다면 원래 배포 페이지에서 다시 받아야 할 수 있습니다.

‘모니터를 끄면 더 빨라지나요?’ 화면 상태만으로 다운로드 속도가 빨라진다고 볼 근거는 없습니다. 속도는 네트워크·서버·저장 장치 등의 영향을 받습니다. ‘pika를 켜면 Wi-Fi도 유지되나요?’ 잠자기 방지와 공유기·VPN·서버 연결 보장은 다릅니다.

‘밤새 받아도 되나요?’ 먼저 짧은 테스트로 전원과 전송 상태를 확인한 뒤 필요한 시간만 유지하세요. 이 글의 절차는 점검 방법이며, 모든 모델·다운로드 앱의 연속 동작을 검증했다는 뜻은 아닙니다.
---
2026년 10월 11일 Apple 공식 전원·외장 화면 안내, macOS caffeinate(8) 매뉴얼과 pika 구현을 확인했습니다. pika 제작자가 작성한 사용 안내이며, 출처와 관련 설정은 아래 링크에서 확인할 수 있습니다.
''')
add('en','MacBook downloads stop: screen off, sleep or a closed lid?',
'Find out why a Mac download pauses, when caffeinate helps, and what to check before downloading with the lid closed.',
'Identify when the transfer stops|Screen off is not system sleep|Use caffeinate with the lid open|Closing the lid changes the conditions|Use pika for closed-lid downloads|Check completion and common questions|Sources',
'''Read the download app’s last message first: paused transfer, network error, storage shortage or sign-in required. If it fails while you are actively using the Mac, check Wi-Fi, VPN, the server and free space before changing power settings. Expiring links and a closed download app are separate problems.

If the failure consistently follows locking or closing the lid, note the timing and check power behavior. A dark screen alone does not identify the cause.
---
A display can be off while the system continues working. Locking does not itself prove a transfer stopped, but automatic system sleep can follow later. On supported Macs, Apple provides an option to prevent automatic sleep on power while the display is off. Keep password protection enabled.

Wake for network access is not a general promise to keep arbitrary downloads running overnight; Apple describes brief wakeups for shared services.
---
The command below requests prevention of idle system sleep for one hour. Keep that terminal open and download in your usual app. Stop early with Ctrl+C. The -t value is in seconds; the assertion ends after the timeout.

-i concerns idle system sleep; -d concerns display sleep and is unnecessary just to allow the screen to turn off. caffeinate does not resume failed downloads, guarantee connectivity, or override every sleep condition. Consult man caffeinate on your own Mac.
---
An open-lid test does not establish closed-lid behavior. For an external-display setup, check the Mac’s supported display configuration, power, external keyboard and mouse. A charger alone does not establish that configuration.

Without an external screen, test a short noncritical transfer separately. Compare bytes received before and after closing the lid; finding the app still open is not proof of continuous progress.
---
Install pika and prepare its helper. Start the download, turn Session ON, leave Monitor OFF if display retention is unnecessary, then close the lid. Open-lid toggles do not immediately blank the display; the display policy applies after lid closure.

Reopen after a short interval and inspect progress. Turn Session OFF when finished; this releases sleep prevention without immediately blanking the screen. Use power on a ventilated desk, not inside a closed bag. Protection thresholds or helper failures may stop the session. pika does not handle download errors or detect transfer completion for you.
---
Check that the download app reports completion and the saved file has the expected size. Verify a checksum if the publisher supplies one. Resume through the app’s supported workflow; an expired link may require returning to the original download page.

Screen state does not guarantee faster transfer. Preventing sleep does not guarantee Wi-Fi, VPN or server availability. Start with a short test; these steps are not a claim of uninterrupted operation across all hardware and apps.
---
Checked October 11, 2026 against Apple documentation, the local caffeinate(8) manual and pika source. Written by the pika maker. Sources are linked below.
''')
add('ja','MacBookのダウンロードが止まる原因：画面オフ・スリープ・ふたの違い','通信と電源を切り分け、caffeinateとpikaの使い方を確認します。','停止した時点を確認|画面オフとスリープ|開いたままcaffeinateを使う|ふたを閉じる条件|pikaでダウンロードを維持|完了の確認|参考資料',
'''まずダウンロードアプリの一時停止、通信エラー、容量不足、ログイン要求を確認します。使用中にも止まるならWi-Fi、VPN、サーバー、空き容量を先に調べます。期限切れリンクはスリープ防止では直りません。
---
画面が消えてもMacが起きていれば転送できる場合があります。ロック後に自動スリープへ移ることもあります。対応機種では電源接続時の自動スリープ防止設定を確認します。パスワード保護は維持してください。
---
下のコマンドは1時間、アイドル時のシステムスリープ防止を要求します。ターミナルを開いたまま通常のアプリでダウンロードし、早く終えるならCtrl+C。-tは秒、-iはシステム、-dは画面に関する指定です。通信復旧やすべてのスリープ防止を保証しません。
---
外部画面を使う場合は電源、外部キーボード・マウス、対応ディスプレイ構成を確認します。充電器だけでは十分とはいえません。外部画面なしで閉じる場合は別に短い転送を試し、受信量を比較してください。
---
pikaと補助サービスを準備し、転送開始後にSession ON、画面が不要ならMonitor OFFにして閉じます。画面ポリシーは閉じた後に適用されます。完了後はSession OFF。通風のよい机と電源を使い、閉じたバッグ内で動かさないでください。保護機能やサービス障害で停止する場合があります。
---
アプリの完了表示、保存容量、提供されていればチェックサムを確認します。再開はアプリの対応機能を使います。pikaは通信復旧や完了検出を代行しません。画面を消すだけで高速になるわけではありません。
---
2026年10月11日、Apple資料、caffeinate(8)、pika実装を確認。pika制作者による案内です。''')
add('zh-CN','MacBook 下载停止：关屏、睡眠和合盖有什么不同？','先排查网络和空间，再选择 caffeinate 或 pika 保持任务运行。','先找出停止时点|关屏不等于睡眠|开盖使用 caffeinate|合盖的条件不同|使用 pika 保持下载|确认下载完成|参考资料',
'''先看下载应用是否提示暂停、网络错误、空间不足或需要登录。使用中也会停止时，先查 Wi-Fi、VPN、服务器和剩余空间。防睡眠不能修复过期链接。
---
屏幕关闭时，系统保持唤醒仍可能继续传输；锁屏后也可能随后自动睡眠。支持的 Mac 可检查接电时防止自动睡眠的选项。无需关闭密码保护。
---
下方命令请求一小时内防止空闲系统睡眠。保持终端打开，在原应用下载；提前结束按 Ctrl+C。-t 单位为秒，-i 针对空闲系统睡眠，-d 针对显示器。它不恢复网络，也不覆盖所有睡眠情况。
---
外接显示器配置需检查电源、外接键鼠和机型支持条件。只有充电器不等于完整配置。不接外屏时，应单独进行短传输测试，比较合盖前后接收量。
---
准备 pika 及辅助服务，开始下载后开启 Session；无需保留屏幕则 Monitor OFF，然后合盖。屏幕策略在合盖后应用。结束时关闭 Session。使用电源和通风桌面，不要在密闭包内运行。保护机制或服务故障可能停止会话。
---
查看应用完成状态、文件大小，以及发布者提供的校验和。使用应用支持的恢复功能。pika 不代替网络恢复或检测下载完成，关闭屏幕也不保证加速。
---
2026 年 10 月 11 日核对 Apple 文档、caffeinate(8) 和 pika 实现。本文由 pika 制作者撰写。''')
add('zh-TW','MacBook 下載停止：關閉螢幕、睡眠與闔蓋有何不同？','先檢查網路與空間，再選擇 caffeinate 或 pika 維持工作。','先確認停止時點|關螢幕不等於睡眠|開蓋使用 caffeinate|闔蓋的條件不同|使用 pika 維持下載|確認下載完成|參考資料',
'''先看下載程式是否提示暫停、網路錯誤、空間不足或需要登入。使用中也停止時，先檢查 Wi-Fi、VPN、伺服器和剩餘空間。防睡眠不能修復過期連結。
---
螢幕關閉而系統仍醒著時，傳輸可能繼續；鎖定後也可能自動睡眠。支援的 Mac 可檢查接電時防止自動睡眠的選項。不必取消密碼保護。
---
下方命令要求一小時內防止閒置系統睡眠。保持終端機開啟，在原程式下載；提前結束按 Ctrl+C。-t 單位為秒，-i 針對閒置系統睡眠，-d 針對顯示器。它不修復網路，也不涵蓋所有睡眠情況。
---
外接顯示器需確認電源、外接鍵鼠及機型支援條件。充電器本身不等於完整配置。不接外屏時，請另做短傳輸測試，比較闔蓋前後收到的資料量。
---
準備 pika 與輔助服務，開始下載後開啟 Session；不需維持畫面則 Monitor OFF，再闔蓋。畫面政策在闔蓋後套用。完成後關閉 Session。使用電源及通風桌面，勿在密閉袋中執行。保護機制或服務錯誤可能中止工作階段。
---
確認程式完成狀態、檔案大小，以及發布者提供的校驗碼。透過程式支援的功能續傳。pika 不代替連線恢復或偵測下載完成，關閉螢幕也不保證加速。
---
2026 年 10 月 11 日核對 Apple 文件、caffeinate(8) 與 pika 實作。本文由 pika 製作者撰寫。''')
add('es','Descargas detenidas en MacBook: pantalla, reposo y tapa','Revisa red y almacenamiento antes de elegir caffeinate o pika.','Cuándo se detiene|Pantalla y reposo|caffeinate con tapa abierta|Condiciones al cerrar|Descargar con pika|Verificar el resultado|Fuentes',
'''Revisa pausa, error de red, espacio o inicio de sesión en la aplicación. Si falla mientras usas el Mac, comprueba Wi-Fi, VPN y servidor. Evitar el reposo no repara enlaces caducados.
---
Una pantalla apagada no implica que el sistema duerma. Puede seguir transfiriendo, aunque el reposo automático llegue después del bloqueo. En equipos compatibles revisa la opción de evitar reposo con alimentación. Conserva la contraseña.
---
El comando siguiente solicita evitar reposo por inactividad durante una hora. Mantén la terminal abierta y descarga en tu aplicación. Ctrl+C termina antes; -t usa segundos, -i afecta al sistema y -d a la pantalla. No garantiza conectividad ni evita todo tipo de reposo.
---
Con pantalla externa revisa alimentación, teclado, ratón y compatibilidad del Mac. El cargador solo no completa la configuración. Sin monitor externo, prueba una transferencia corta y compara bytes antes y después de cerrar.
---
Prepara pika y su servicio auxiliar, inicia la descarga, activa Session y deja Monitor OFF si no necesitas pantalla. Cierra la tapa para aplicar su política de pantalla. Al acabar, Session OFF. Usa una mesa ventilada y alimentación, nunca una bolsa cerrada. La protección o fallos pueden detener la sesión.
---
Confirma finalización, tamaño del archivo y checksum si está disponible. Reanuda con las funciones de la aplicación. pika no recupera la red ni detecta el final; apagar la pantalla no garantiza más velocidad.
---
Revisado el 11 de octubre de 2026 con Apple, caffeinate(8) y código pika. Guía del creador de pika.''')
add('fr','Téléchargement arrêté sur MacBook : écran, veille et couvercle','Vérifiez réseau et stockage avant de choisir caffeinate ou pika.','Identifier l’arrêt|Écran et veille|caffeinate couvercle ouvert|Conditions de fermeture|Télécharger avec pika|Vérifier le résultat|Sources',
'''Vérifiez pause, erreur réseau, espace libre et connexion au compte dans l’application. Si le transfert échoue pendant l’utilisation, contrôlez Wi-Fi, VPN et serveur. Empêcher la veille ne répare pas un lien expiré.
---
Un écran éteint ne signifie pas que le système dort. Le transfert peut continuer, mais une veille automatique peut suivre le verrouillage. Vérifiez l’option de maintien éveillé sur secteur si disponible. Gardez le mot de passe.
---
La commande suivante demande d’empêcher la veille inactive pendant une heure. Laissez le terminal ouvert et téléchargez dans votre application. Ctrl+C arrête la demande ; -t est en secondes, -i concerne le système, -d l’écran. Cela ne garantit ni réseau ni absence de toute veille.
---
Avec un écran externe, vérifiez alimentation, clavier, souris et compatibilité. Le chargeur seul ne suffit pas à établir cette configuration. Sans écran externe, testez un petit transfert et comparez les octets avant et après fermeture.
---
Préparez pika et son service, démarrez le transfert, activez Session et laissez Monitor OFF si l’écran est inutile. Fermez le couvercle pour appliquer la politique d’affichage. Terminez avec Session OFF. Utilisez un bureau ventilé et l’alimentation, jamais un sac fermé. Protection ou panne peuvent arrêter la session.
---
Vérifiez fin du transfert, taille et somme de contrôle fournie. Reprenez avec les fonctions de l’application. pika ne rétablit pas le réseau et ne détecte pas la fin ; éteindre l’écran ne garantit pas une accélération.
---
Vérifié le 11 octobre 2026 avec Apple, caffeinate(8) et le code pika. Guide du créateur de pika.''')
add('de','MacBook-Download stoppt: Display, Ruhezustand oder Deckel?','Prüfe Netzwerk und Speicher, bevor du caffeinate oder pika einsetzt.','Zeitpunkt prüfen|Display und Ruhezustand|caffeinate bei offenem Deckel|Bedingungen beim Schließen|Mit pika herunterladen|Ergebnis prüfen|Quellen',
'''Prüfe Pause, Netzwerkfehler, Speicherplatz und Anmeldung in der Download-App. Scheitert der Transfer auch während der Nutzung, prüfe WLAN, VPN und Server. Schlafverhinderung repariert keine abgelaufenen Links.
---
Ein dunkles Display bedeutet nicht automatisch Systemschlaf. Der Transfer kann weiterlaufen, später kann aber automatischer Schlaf folgen. Prüfe bei unterstützten Macs die Option zum Wachbleiben am Netzteil. Behalte den Passwortschutz.
---
Der folgende Befehl fordert eine Stunde Schutz vor Leerlaufschlaf an. Lass das Terminal offen und nutze deine Download-App. Ctrl+C beendet früher; -t zählt Sekunden, -i betrifft das System, -d das Display. Netzwerk und alle Schlafzustände sind damit nicht abgesichert.
---
Für externe Displays prüfe Netzteil, Tastatur, Maus und Modellunterstützung. Ein Ladegerät allein ist keine vollständige Konfiguration. Ohne externes Display teste einen kurzen Transfer und vergleiche empfangene Bytes vor und nach dem Schließen.
---
Bereite pika und Hilfsdienst vor, starte den Download, aktiviere Session und lasse Monitor OFF, falls kein Display nötig ist. Die Display-Richtlinie greift nach dem Schließen. Danach Session OFF. Nutze Strom und einen belüfteten Tisch, keine geschlossene Tasche. Schutzfunktionen oder Fehler können die Sitzung stoppen.
---
Prüfe Abschluss, Dateigröße und angebotene Prüfsumme. Nutze die Fortsetzungsfunktion der App. pika repariert keine Verbindung und erkennt keinen Downloadabschluss. Ein ausgeschaltetes Display garantiert keinen Geschwindigkeitsgewinn.
---
Geprüft am 11. Oktober 2026 anhand von Apple, caffeinate(8) und pika-Code. Anleitung des pika-Entwicklers.''')
add('pt-BR','Download parado no MacBook: tela, repouso ou tampa?','Confira rede e armazenamento antes de usar caffeinate ou pika.','Quando parou|Tela e repouso|caffeinate com tampa aberta|Condições ao fechar|Baixar com pika|Verificar o resultado|Fontes',
'''Veja pausa, erro de rede, espaço e login no aplicativo. Se falha durante o uso, confira Wi-Fi, VPN e servidor. Evitar repouso não recupera links expirados.
---
Tela apagada não significa sistema dormindo. A transferência pode continuar, mas o repouso automático pode ocorrer depois do bloqueio. Confira a opção de manter acordado na tomada, se disponível. Mantenha a senha.
---
O comando abaixo solicita uma hora sem repouso por inatividade. Deixe o terminal aberto e baixe no aplicativo habitual. Ctrl+C encerra antes; -t usa segundos, -i é do sistema e -d da tela. Não garante rede nem impede todo tipo de repouso.
---
Com monitor externo, confira energia, teclado, mouse e suporte do modelo. Só o carregador não completa essa configuração. Sem monitor externo, teste uma transferência curta e compare bytes antes e depois de fechar.
---
Prepare pika e o serviço auxiliar, inicie o download, ligue Session e deixe Monitor OFF se não precisar da tela. Feche a tampa para aplicar a política de tela. Termine com Session OFF. Use energia e mesa ventilada, nunca bolsa fechada. Proteção ou falhas podem parar a sessão.
---
Confira conclusão, tamanho e checksum fornecido. Retome pelas funções do aplicativo. pika não recupera a rede nem detecta o fim; apagar a tela não garante mais velocidade.
---
Verificado em 11 de outubro de 2026 com Apple, caffeinate(8) e código pika. Guia do criador de pika.''')
add('ru','Загрузка на MacBook остановилась: экран, сон или крышка?','Проверьте сеть и место на диске, затем выберите caffeinate или pika.','Когда остановилось|Экран и сон|caffeinate с открытой крышкой|Условия закрытой крышки|Загрузка с pika|Проверка результата|Источники',
'''Проверьте паузу, ошибку сети, место и вход в приложение. Если сбой возникает при работе, начните с Wi-Fi, VPN и сервера. Запрет сна не исправит просроченную ссылку.
---
Тёмный экран не означает сон системы. Передача может продолжаться, но после блокировки возможен автоматический сон. На поддерживаемых Mac проверьте запрет автоматического сна при питании. Сохраните защиту паролем.
---
Команда ниже запрашивает час без сна от бездействия. Оставьте терминал открытым и загружайте в приложении. Ctrl+C завершает раньше; -t задаёт секунды, -i относится к системе, -d к экрану. Это не гарантия связи и не блокировка всех видов сна.
---
Для внешнего экрана проверьте питание, клавиатуру, мышь и поддержку модели. Одного зарядного устройства недостаточно. Без внешнего экрана отдельно проверьте короткую передачу, сравнив объём до и после закрытия.
---
Подготовьте pika и службу, начните загрузку, включите Session и оставьте Monitor OFF, если экран не нужен. Политика экрана применяется после закрытия. По завершении Session OFF. Используйте питание и проветриваемый стол, не закрытую сумку. Защита или ошибки могут остановить сессию.
---
Проверьте завершение, размер и контрольную сумму, если она опубликована. Возобновляйте средствами приложения. pika не восстанавливает сеть и не определяет окончание. Выключение экрана не гарантирует ускорение.
---
Проверено 11 октября 2026 года по Apple, caffeinate(8) и коду pika. Материал автора pika.''')
add('id','Unduhan MacBook berhenti: layar mati, tidur, atau penutup?','Periksa jaringan dan penyimpanan sebelum memakai caffeinate atau pika.','Kapan berhenti|Layar dan tidur|caffeinate dengan penutup terbuka|Syarat menutup penutup|Mengunduh dengan pika|Periksa hasil|Sumber',
'''Periksa jeda, kesalahan jaringan, ruang kosong, dan login aplikasi. Jika gagal saat digunakan, cek Wi-Fi, VPN, dan server. Pencegahan tidur tidak memperbaiki tautan kedaluwarsa.
---
Layar mati tidak berarti sistem tidur. Transfer bisa berlanjut, tetapi tidur otomatis dapat menyusul penguncian. Periksa opsi tetap terjaga saat tersambung daya jika tersedia. Tetap gunakan kata sandi.
---
Perintah berikut meminta pencegahan tidur karena tidak aktif selama satu jam. Biarkan terminal terbuka dan unduh melalui aplikasi biasa. Ctrl+C mengakhiri lebih awal; -t dalam detik, -i untuk sistem, -d untuk layar. Ini tidak menjamin jaringan atau mencegah semua keadaan tidur.
---
Dengan monitor eksternal, periksa daya, keyboard, mouse, dan dukungan model. Pengisi daya saja belum cukup. Tanpa monitor, uji transfer singkat dan bandingkan jumlah byte sebelum dan setelah menutup.
---
Siapkan pika dan layanan pendamping, mulai unduhan, aktifkan Session, pilih Monitor OFF jika layar tidak diperlukan, lalu tutup. Kebijakan layar berlaku setelah penutup ditutup. Akhiri dengan Session OFF. Gunakan daya dan meja berventilasi, bukan tas tertutup. Perlindungan atau gangguan dapat menghentikan sesi.
---
Periksa status selesai, ukuran, dan checksum jika disediakan. Lanjutkan lewat fitur aplikasi. pika tidak memulihkan jaringan atau mendeteksi selesai; mematikan layar tidak menjamin lebih cepat.
---
Diperiksa 11 Oktober 2026 berdasarkan Apple, caffeinate(8), dan kode pika. Panduan pembuat pika.''')
add('vi','Tải xuống trên MacBook bị dừng: tắt màn hình, ngủ hay đóng nắp?','Kiểm tra mạng và dung lượng trước khi chọn caffeinate hoặc pika.','Xác định lúc dừng|Màn hình và ngủ|caffeinate khi mở nắp|Điều kiện đóng nắp|Tải với pika|Kiểm tra kết quả|Nguồn',
'''Xem trạng thái tạm dừng, lỗi mạng, dung lượng và đăng nhập. Nếu lỗi cả khi đang dùng máy, kiểm tra Wi-Fi, VPN và máy chủ. Ngăn ngủ không sửa liên kết hết hạn.
---
Màn hình tắt không có nghĩa hệ thống ngủ. Tải có thể tiếp tục, nhưng tự động ngủ có thể xảy ra sau khi khóa. Kiểm tra tùy chọn giữ thức khi cắm nguồn nếu được hỗ trợ. Giữ mật khẩu bảo vệ.
---
Lệnh dưới yêu cầu ngăn ngủ do nhàn rỗi trong một giờ. Giữ terminal mở và tải bằng ứng dụng thường dùng. Ctrl+C kết thúc sớm; -t tính bằng giây, -i cho hệ thống, -d cho màn hình. Không bảo đảm mạng hay ngăn mọi kiểu ngủ.
---
Với màn hình ngoài, kiểm tra nguồn, bàn phím, chuột và hỗ trợ của máy. Chỉ bộ sạc chưa đủ. Không có màn hình ngoài thì thử tải ngắn và so sánh lượng dữ liệu trước và sau đóng nắp.
---
Chuẩn bị pika và dịch vụ hỗ trợ, bắt đầu tải, bật Session, để Monitor OFF nếu không cần màn hình rồi đóng nắp. Chính sách màn hình áp dụng sau khi đóng. Xong thì Session OFF. Dùng nguồn và bàn thoáng, không để trong túi kín. Bảo vệ hoặc lỗi có thể dừng phiên.
---
Kiểm tra trạng thái hoàn tất, kích thước và checksum nếu có. Tiếp tục bằng chức năng của ứng dụng. pika không phục hồi mạng hay phát hiện tải xong; tắt màn hình không bảo đảm nhanh hơn.
---
Kiểm tra ngày 11 tháng 10 năm 2026 theo Apple, caffeinate(8) và mã pika. Hướng dẫn của nhà phát triển pika.''')
add('hi','MacBook डाउनलोड रुकता है: स्क्रीन बंद, स्लीप या ढक्कन?','caffeinate या pika चुनने से पहले नेटवर्क और खाली जगह जाँचें।','रुकने का समय देखें|स्क्रीन और स्लीप|खुले ढक्कन में caffeinate|ढक्कन बंद करने की शर्तें|pika से डाउनलोड|परिणाम जाँचें|स्रोत',
'''ऐप में रुका हुआ डाउनलोड, नेटवर्क त्रुटि, जगह और लॉगिन देखें। इस्तेमाल करते समय भी रुकता है तो Wi-Fi, VPN और सर्वर जाँचें। स्लीप रोकने से समाप्त लिंक ठीक नहीं होता।
---
स्क्रीन बंद होना सिस्टम स्लीप नहीं है। डाउनलोड चल सकता है, लेकिन लॉक के बाद स्वचालित स्लीप हो सकता है। उपलब्ध हो तो बिजली पर जागे रहने की सेटिंग देखें। पासवर्ड सुरक्षा रखें।
---
नीचे का कमांड एक घंटे तक निष्क्रियता वाली सिस्टम स्लीप रोकने का अनुरोध करता है। टर्मिनल खुला रखें और सामान्य ऐप में डाउनलोड करें। Ctrl+C से पहले रोक सकते हैं; -t सेकंड, -i सिस्टम और -d स्क्रीन से संबंधित है। यह हर स्लीप या नेटवर्क समस्या नहीं रोकता।
---
बाहरी स्क्रीन के लिए बिजली, कीबोर्ड, माउस और मॉडल समर्थन देखें। सिर्फ चार्जर पर्याप्त नहीं है। बिना बाहरी स्क्रीन छोटा डाउनलोड आजमाएँ और ढक्कन बंद करने से पहले व बाद के बाइट की तुलना करें।
---
pika और सहायक सेवा तैयार करें, डाउनलोड शुरू करें, Session ON और स्क्रीन न चाहिए तो Monitor OFF रखें, फिर ढक्कन बंद करें। स्क्रीन नीति इसके बाद लागू होती है। अंत में Session OFF करें। हवादार मेज और बिजली उपयोग करें, बंद बैग नहीं। सुरक्षा या त्रुटि सत्र रोक सकती है।
---
समाप्ति, फ़ाइल आकार और उपलब्ध checksum जाँचें। ऐप की सुविधा से दोबारा शुरू करें। pika नेटवर्क नहीं सुधारता और समाप्ति नहीं पहचानता; स्क्रीन बंद करने से गति की गारंटी नहीं है।
---
11 अक्टूबर 2026 को Apple, caffeinate(8) और pika कोड से जाँच की गई। pika निर्माता की गाइड।''')
add('ar','توقف التنزيل على MacBook: الشاشة أم السكون أم الغطاء؟','افحص الشبكة والمساحة قبل اختيار caffeinate أو pika.','حدد وقت التوقف|الشاشة والسكون|caffeinate والغطاء مفتوح|شروط إغلاق الغطاء|التنزيل مع pika|تحقق من النتيجة|المصادر',
'''افحص رسائل الإيقاف المؤقت والشبكة والمساحة وتسجيل الدخول. إذا توقف أثناء الاستخدام، افحص Wi-Fi وVPN والخادم أولاً. منع السكون لا يصلح رابطاً منتهي الصلاحية.
---
انطفاء الشاشة لا يعني سكون النظام. قد يستمر النقل لكن السكون التلقائي قد يأتي بعد القفل. افحص خيار البقاء مستيقظاً على الطاقة إن كان متاحاً. أبقِ حماية كلمة المرور.
---
يطلب الأمر أدناه منع سكون الخمول لساعة. اترك الطرفية مفتوحة ونزّل بالتطبيق المعتاد. يوقفه Ctrl+C مبكراً؛ -t بالثواني، و-i للنظام و-d للشاشة. لا يضمن الشبكة ولا يمنع كل أنواع السكون.
---
مع شاشة خارجية افحص الطاقة ولوحة المفاتيح والفأرة ودعم الطراز. الشاحن وحده لا يكمل الإعداد. دون شاشة خارجية اختبر نقلاً قصيراً وقارن البايتات قبل الإغلاق وبعده.
---
جهّز pika وخدمته، ابدأ التنزيل وفعّل Session واترك Monitor OFF إن لم تحتج الشاشة، ثم أغلق الغطاء. تطبق سياسة الشاشة بعد الإغلاق. عند الانتهاء استخدم Session OFF. استخدم الطاقة ومكتباً مهوّى لا حقيبة مغلقة. قد توقف الحماية أو الأخطاء الجلسة.
---
تحقق من الاكتمال وحجم الملف وقيمة التحقق إن توفرت. استأنف عبر التطبيق. لا يصلح pika الشبكة ولا يكتشف انتهاء التنزيل؛ إطفاء الشاشة لا يضمن السرعة.
---
رُوجع في 11 أكتوبر 2026 وفق Apple وcaffeinate(8) وكود pika. دليل من صانع pika.''')
add('th','ดาวน์โหลดบน MacBook หยุด: ปิดจอ พักเครื่อง หรือปิดฝา?','ตรวจเครือข่ายและพื้นที่ก่อนเลือกใช้ caffeinate หรือ pika','ดูว่าหยุดเมื่อใด|จอกับการพักเครื่อง|ใช้ caffeinate เมื่อเปิดฝา|เงื่อนไขเมื่อปิดฝา|ดาวน์โหลดด้วย pika|ตรวจผลลัพธ์|แหล่งข้อมูล',
'''ตรวจข้อความหยุดชั่วคราว เครือข่าย พื้นที่ และการเข้าสู่ระบบในแอป หากหยุดขณะใช้งานให้ตรวจ Wi-Fi VPN และเซิร์ฟเวอร์ก่อน การกันพักเครื่องไม่แก้ลิงก์หมดอายุ
---
จอดับไม่ได้แปลว่าระบบพักเครื่อง การส่งข้อมูลอาจทำต่อแต่ระบบอาจพักภายหลังการล็อก ตรวจตัวเลือกไม่พักอัตโนมัติเมื่อเสียบไฟหากรองรับ คงรหัสผ่านไว้
---
คำสั่งด้านล่างขอกันพักเครื่องจากการไม่ใช้งานหนึ่งชั่วโมง เปิดเทอร์มินัลไว้และดาวน์โหลดในแอปเดิม หยุดก่อนด้วย Ctrl+C โดย -t เป็นวินาที -i สำหรับระบบและ -d สำหรับจอ ไม่รับประกันเครือข่ายหรือกันการพักทุกกรณี
---
เมื่อใช้จอนอกให้ตรวจไฟเลี้ยง คีย์บอร์ด เมาส์ และรุ่นที่รองรับ มีเพียงที่ชาร์จยังไม่ครบ หากไม่มีจอนอกให้ลองดาวน์โหลดสั้น ๆ และเทียบปริมาณก่อนกับหลังปิดฝา
---
เตรียม pika และบริการช่วย เริ่มดาวน์โหลด เปิด Session และให้ Monitor OFF หากไม่ต้องใช้จอ แล้วปิดฝา นโยบายจอทำงานหลังปิดฝา เสร็จแล้ว Session OFF ใช้ไฟและโต๊ะระบายอากาศ ไม่ใช่กระเป๋าปิด ระบบป้องกันหรือข้อผิดพลาดอาจหยุดเซสชัน
---
ตรวจสถานะเสร็จ ขนาดไฟล์ และ checksum หากมี ใช้ฟังก์ชันของแอปเพื่อดาวน์โหลดต่อ pika ไม่แก้เครือข่ายหรือตรวจการเสร็จสิ้น และจอดับไม่รับประกันความเร็ว
---
ตรวจวันที่ 11 ตุลาคม 2026 จาก Apple, caffeinate(8) และโค้ด pika คู่มือโดยผู้สร้าง pika''')
