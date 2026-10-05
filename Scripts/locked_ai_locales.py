"""Localized editorial copy, 2026-10-05. No claims of uninterrupted AI execution."""
COPY = {}
def add(locale, title, intro, headings, body):
    COPY[locale] = {'title': title, 'intro': intro, 'headings': headings.split('|'), 'paragraphs': [section.strip().split('\n\n') for section in body.strip().split('\n---\n')]}

add('ko', '맥북 화면은 잠겼는데 Claude Code·Codex 작업은 계속될까?',
'화면 잠금, 화면 꺼짐, 시스템 절전은 다릅니다. Claude Code와 Codex의 로컬 작업이 멈추는 이유와 덮개를 닫기 전후 확인법, pika 설정을 정리합니다.',
'화면 잠금과 작업 중단은 같은 말이 아니다|로컬 세션인가, 클라우드 작업인가?|멈춘 것 같다면 이 순서로 확인|잠금 전후 3분 확인 방법|덮개를 닫을 때 pika 설정|자주 묻는 질문|공식 자료와 확인 범위',
'''
화면에 암호 입력창이 나타났다고 해서 AI 작업이 종료됐다는 뜻은 아닙니다. 화면 잠금은 다른 사람이 내 세션을 사용하지 못하게 하는 상태입니다. 시스템이 깨어 있고 필요한 앱과 네트워크가 살아 있다면 일반적인 터미널 빌드나 파일 처리 작업은 잠금 상태에서도 계속될 수 있습니다. 다만 화면을 직접 클릭하는 자동화나 사용자 인증을 요구하는 작업은 잠금 때문에 진행하지 못할 수 있습니다.

화면 꺼짐은 디스플레이 상태이고, 시스템 잠자기는 컴퓨터의 실행 상태입니다. 검은 화면만 보고 둘을 구별할 수는 없습니다. 잠근 직후에는 진행되다가 나중에 자동 잠자기에 들어가 멈추는 경우도 있습니다. 따라서 ‘잠금 화면을 봤다’보다 ‘자리를 비운 동안 로그와 결과물이 실제로 갱신됐는가’를 확인하는 것이 중요합니다.

Apple의 전원 설정에는 화면이 꺼져 있어도 전원 어댑터 사용 중 자동 잠자기를 방지하는 옵션이 있습니다. 제공 여부와 위치는 모델·macOS에 따라 다르며, 이 옵션만으로 덮개를 닫은 모든 상황까지 해결된다고 보면 안 됩니다. 암호 요구나 화면 잠금을 해제할 필요도 없습니다.
---
Codex CLI의 파일 읽기·수정·명령 실행은 내 컴퓨터에서 이뤄집니다. Codex Cloud에 명시적으로 맡긴 작업은 별도의 클라우드 환경에서 실행됩니다. 모델의 응답이 서버에서 생성된다고 로컬 도구 실행까지 클라우드로 옮겨지는 것은 아닙니다. 같은 Codex를 쓰더라도 현재 작업의 실행 위치를 먼저 확인하세요.

Claude Code Remote Control도 휴대폰으로 보인다는 이유만으로 클라우드 작업이 되는 것은 아닙니다. Anthropic 문서에 따르면 로컬 세션에 연결하는 방식이며 컴퓨터와 claude 프로세스가 실행 중이어야 합니다. 문서에 재연결 기능이 안내되어 있어도, 잠자거나 연결이 끊긴 동안 로컬 작업이 계속 실행됐다는 의미는 아닙니다.

클라우드에서 독립적으로 실행되는 작업에는 내 맥북의 절전 방지가 필요하지 않을 수 있습니다. 반대로 로컬 저장소, 터미널, MCP 서버에 의존하는 단계는 해당 Mac의 상태에 영향을 받습니다. pika는 AI 작업을 클라우드로 이전하거나 원격 실행해 주는 도구가 아닙니다.
---
먼저 AI 세션의 마지막 메시지를 읽으세요. 명령 실행 승인, 파일 접근 허용, 추가 질문에 대한 응답을 기다리는 상태라면 컴퓨터가 깨어 있어도 더 진행되지 않습니다. 작업이 이미 끝났거나 오류로 종료된 경우도 있으므로 출력이 조용하다는 이유로 절전부터 의심할 필요는 없습니다.

다음으로 앱이나 터미널이 종료되지 않았는지, Wi-Fi·VPN 연결과 로그인 상태가 유지되는지 확인하세요. Mac의 절전을 막아도 공유기 재연결, VPN 만료, API 오류나 사용량 제한까지 해결되지는 않습니다. 네트워크 복구 후 자동 재시도 여부는 각 도구와 작업 상태에 따라 달라집니다.

마지막으로 잠자기 기록과 실제 작업 로그를 비교합니다. 아래 명령은 현재 전원 assertion과 최근 전원 이벤트를 조회할 뿐 설정을 바꾸지 않습니다. assertion이 존재하는 것은 특정 잠자기를 막도록 요청한 상태라는 뜻이지, AI 작업 완료의 증거는 아닙니다. 로그 형식과 항목은 macOS 버전마다 다를 수 있습니다. CPU 사용량이 낮다는 사실만으로 중단을 판단하지 마세요.
---
중요한 작업을 맡기기 전에 덮개를 연 채 짧게 확인해 보세요. 아래 반복문은 10초마다 현재 시각을 터미널에 표시합니다. 해당 터미널을 종료하지 말고 화면만 잠근 뒤 약 3분 후 잠금을 풀어 출력 간격을 확인합니다. 확인이 끝나면 Ctrl+C로 반복문을 중단하세요.

시간 출력 사이에 긴 공백이 생겼다면 시스템 잠자기 기록과 비교해 보세요. 이 확인은 간단한 로컬 프로세스가 실행됐는지만 보여 줍니다. 출력 간격이 고르더라도 AI의 네트워크 요청, 승인 단계, 최종 결과까지 정상이라는 보장은 아닙니다. AI 작업 로그의 시각이나 결과 파일의 수정 시각도 함께 확인하세요.

잠금 상태에서 정상임을 확인했다면 같은 전원·네트워크 조건에서 덮개 닫힘을 별도로 시험합니다. 덮개를 열어 둔 결과를 닫힌 상태에 그대로 적용하지 마세요. 여기 제시한 절차는 사용자가 자신의 환경에서 수행하는 점검법이며, 모든 Mac에서의 연속 실행을 검증했다는 주장은 아닙니다.
---
pika PKG 설치와 보조 서비스 연결을 마친 뒤 Session을 ON으로 준비합니다. 화면을 유지할 필요가 없다면 Monitor는 OFF로 두고 덮개를 닫습니다. 현재 pika는 덮개를 연 채 Session을 켜거나 Monitor를 바꿨다는 이유만으로 화면을 즉시 끄도록 설계되지 않았으며, 덮개가 닫혔을 때 화면 정책을 적용합니다.

Session은 잠자기 방지를 준비하는 제어이고 Monitor는 화면 유지 여부의 제어입니다. Monitor OFF는 AI 작업을 종료하는 버튼이 아닙니다. 또한 macOS의 잠금·암호 요구와 별개이므로 잠금 화면이 나타났다는 이유로 실패라고 판단하지 말고 앞 절의 로그 확인법으로 점검하세요. Session OFF는 잠자기 방지를 해제하고 Monitor도 OFF로 표시하며, 화면을 즉시 끄는 동작은 아닙니다.

pika의 배터리·열 상태 보호가 작동하거나 보조 서비스 연결에 문제가 생기면 세션이 중단될 수 있습니다. 장시간 작업은 전원을 연결하고 통풍되는 책상 위에서 먼저 확인하세요. 닫힌 가방 안에 실행 중인 Mac을 넣어 두는 사용법을 권장하지 않습니다. 작업이 끝나면 Session을 OFF로 돌립니다. pika는 승인 응답, AI 오류 복구, 네트워크 연결이나 작업 완료까지 보장하지 않습니다.
---
‘화면이 잠겨도 괜찮나요?’ 일반적인 백그라운드 계산은 조건이 맞으면 계속될 수 있지만, GUI 조작이나 인증이 필요한 단계는 따로 확인해야 합니다. 잠금은 유지하고 실제 결과로 판단하세요.

‘caffeinate나 tmux를 쓰면 끝인가요?’ caffeinate는 선택한 종류의 잠자기를 막도록 요청하는 도구이며 승인 대기·네트워크 장애 해결책은 아닙니다. tmux는 터미널 연결과 세션을 분리할 때 도움이 되지만 잠든 컴퓨터에서 계산을 계속시키지는 못합니다. 덮개 닫힘 조건도 별도로 확인해야 합니다.

‘MCP가 연결되어 있으면 AI가 계속 일하나요?’ MCP 서버의 실행 여부와 AI 세션의 진행 여부는 다릅니다. pika MCP의 상태 조회는 pika의 Session·덮개 상태 등을 확인하는 데 쓰이며, Claude Code나 Codex의 모든 작업을 추적하거나 자동 승인한다는 뜻은 아닙니다.
---
2026년 10월 5일 기준 공식 문서와 pika 소스의 현재 동작을 바탕으로 작성했습니다. 앱·CLI·운영체제 버전에 따라 메뉴와 복구 동작은 달라질 수 있습니다. 아래 공식 문서와 앞선 잠자기 방지 방법 비교 글을 함께 참고하세요. 이 글은 pika 제작자가 작성한 사용 안내입니다.
''')

add('en', 'Mac locked: will Claude Code and Codex keep working?',
'Locking the screen, turning off the display and sleeping the Mac are different. Check local AI progress, approvals and network access before leaving a closed MacBook running.',
'Locking is not the same as stopping|Local session or cloud task?|Check these causes first|A three-minute check|Using pika with the lid closed|Common questions|Sources and scope',
'''
A password screen does not prove that an AI task stopped. Ordinary background commands can continue while the Mac remains awake, the app stays open and required services remain available. Screen-driven automation or authentication steps can still need an unlocked session. Keep the screen lock enabled.

Display sleep only describes the screen; system sleep affects execution. A Mac can lock first and sleep later. Apple provides a setting on supported configurations to prevent automatic sleep on power while the display is off. Do not treat that as a universal closed-lid override.
---
Codex CLI reads files and runs commands locally. A task explicitly delegated to Codex Cloud runs in a separate cloud environment. Server-side model inference does not move local tools into the cloud.

Claude Code Remote Control connects to a session on your computer. Its documented reconnection behavior does not mean local commands ran during sleep. Independently hosted cloud tasks may not need your Mac awake; steps depending on local files or MCP servers do. pika does not migrate AI work to the cloud.
---
Read the last agent message for approval requests, questions, completion or errors. Then check that the app or terminal is still running and that Wi-Fi, VPN and authentication remain available. Preventing sleep does not fix API failures or usage limits.

The read-only commands below show current power assertions and recent power events. An assertion is a request to prevent a kind of sleep, not proof that an AI task finished. Compare timestamps with the actual task log. Low CPU use alone is not evidence of failure.
---
With the lid open, run the loop below in a terminal you leave open. Lock the screen for about three minutes, unlock and compare the timestamps. Stop the loop with Ctrl+C. Investigate large gaps alongside power logs.

This only checks a simple local process, not AI requests or approvals. Also inspect task output and file modification times. Test lid closure separately under the same power and network conditions; an open-lid result does not establish closed-lid behavior. This is a procedure for your own device, not a claimed hardware benchmark.
---
Install pika and its helper, prepare Session ON, leave Monitor OFF if display retention is unnecessary, then close the lid. In the current design, open-lid toggles do not immediately blank the display; the display policy is applied after lid closure. Monitor OFF is not an instruction to end your AI task and does not disable macOS locking.

Session OFF releases sleep prevention and shows Monitor OFF without immediately blanking the screen. Battery or thermal protection and helper failures can stop a session. Start with power connected on a ventilated desk, never rely on operation inside a closed bag, and turn Session OFF when finished. pika cannot guarantee connectivity or task completion.
---
Does a locked screen mean failure? No: check real progress, and distinguish ordinary commands from GUI or authentication steps. Does tmux or caffeinate solve everything? No: terminal persistence and power assertions do not solve system sleep in every lid state, approvals or network failures.

Does an MCP connection prove the agent is working? No. pika status describes pika, not the complete progress of every Claude Code or Codex task, and it does not automatically approve actions.
---
Checked against official documentation and current pika source on October 5, 2026. Behavior varies by app and macOS version. This guide is written by the pika maker; use the sources and the linked sleep-prevention comparison for additional context.
''')

add('ja', 'MacをロックしてもClaude Code・Codexは動き続ける？',
'画面ロックとスリープを区別し、ローカルAIの進行状況、接続、ふたを閉じる前の設定を確認します。',
'ロックとスリープの違い|ローカルかクラウドか|停止の原因を確認|3分間の確認|pikaの設定|よくある質問|出典と範囲',
'''ロック画面が出ても作業終了とは限りません。Macが起きていてアプリと必要な接続が動いていれば、通常のバックグラウンド処理は続行できます。ただしGUI操作や認証はロック解除が必要な場合があります。画面消灯の後にシステムが眠ることもあります。
---
Codex CLIはローカルでファイルやコマンドを扱います。Codex Cloudへ委任した処理は別の環境で動きます。Claude Code Remote Controlもローカルセッションへの接続です。再接続できても、スリープ中に処理が進んだ証拠にはなりません。
---
最後のメッセージで承認待ち、質問、完了、エラーを確認します。次にアプリ、Wi-Fi、VPN、認証を確認してください。下の読み取り専用コマンドは電源要求と履歴を表示します。要求の存在やCPU使用率だけではAIの進行を証明できません。
---
ふたを開けたまま下のループを実行し、ターミナルを閉じずに約3分ロックします。解除後に時刻の間隔を調べ、Ctrl+Cで終了します。長い空白は電源履歴と比較してください。これは単純なローカル処理の確認です。AIのログも確認し、ふたを閉じた状態は別途試します。
---
pikaと補助サービスを準備し、Session ON、画面維持が不要ならMonitor OFFにしてふたを閉じます。画面ポリシーはふたを閉じた後に適用されます。Session OFFはスリープ防止を解除し、直ちに画面を消す操作ではありません。電源と通風を確保し、閉じたバッグ内では使わないでください。保護機能や接続障害で停止する場合があります。
---
Monitor OFFはAIの停止ではありません。tmuxはシステムのスリープを防ぎません。caffeinateもネットワークや承認待ちを解決しません。pika MCPの状態はpikaの状態であり、すべてのAI作業の進行状況ではありません。
---
2026年10月5日に公式資料とpikaの実装を確認。pika制作者による案内で、全機種の連続動作を保証するものではありません。''')

add('zh-CN', 'Mac 锁屏后，Claude Code 和 Codex 还会继续工作吗？',
'区分锁屏、关闭显示器和系统睡眠，检查本地 AI 任务、网络与合盖设置。',
'锁屏不等于停止|本地还是云端任务|先排查这些原因|三分钟检查|合盖时使用 pika|常见问题|资料与范围',
'''看到密码界面不代表任务结束。Mac 保持唤醒、应用运行且所需连接正常时，一般后台命令可以继续。操作屏幕或身份验证可能需要解锁。显示器关闭与系统睡眠不同，锁屏后仍可能自动睡眠。无需关闭密码保护。
---
Codex CLI 在本机处理文件和命令，明确交给 Codex Cloud 的任务在独立云环境执行。Claude Code Remote Control 连接的仍是本地会话。恢复连接不等于睡眠期间任务一直运行。pika 不会把本地工作迁移到云端。
---
先看最后一条消息是否等待批准、提问、完成或报错，再检查应用、Wi-Fi、VPN 和登录。下方只读命令查看电源请求与近期事件。电源请求的存在或低 CPU 占用都不能证明 AI 任务的进度。
---
打开盖子运行下方循环，保留终端，锁屏约三分钟后查看时间间隔。用 Ctrl+C 结束。明显间断应对照电源日志；同时检查 AI 日志和文件修改时间。这只验证简单本地进程，合盖情况应另行测试。
---
安装 pika 及辅助服务后开启 Session；不需保持屏幕时关闭 Monitor，再合盖。屏幕策略在合盖后应用。关闭 Session 会释放防睡眠并显示 Monitor OFF，不会立即关闭屏幕。接通电源、保持通风，不要放入封闭包内运行。电池、温度保护或辅助服务故障可能中止会话。
---
Monitor OFF 不是结束 AI 任务。tmux 不阻止系统睡眠；caffeinate 不解决网络故障或批准等待。pika MCP 状态也不代表所有 Claude Code、Codex 任务都在推进。
---
依据 2026 年 10 月 5 日官方文档与 pika 实现编写。本文由 pika 制作者提供，不是所有硬件的连续运行保证。''')

add('zh-TW', 'Mac 鎖定螢幕後，Claude Code 與 Codex 還會繼續工作嗎？',
'分辨鎖定、關閉顯示器和系統睡眠，檢查本機 AI 工作、網路與闔蓋設定。',
'鎖定不等於停止|本機或雲端工作|先檢查停止原因|三分鐘檢查|闔蓋使用 pika|常見問題|資料與範圍',
'''出現密碼畫面不代表工作結束。Mac 保持喚醒、應用程式與所需連線正常時，一般背景命令可以繼續。畫面操作或身分驗證可能需要解鎖。顯示器關閉與系統睡眠不同，鎖定後仍可能進入睡眠。請保留密碼保護。
---
Codex CLI 在本機處理檔案與命令，明確交給 Codex Cloud 的工作在獨立雲端環境執行。Claude Code Remote Control 仍連接本機工作階段。重新連線不代表睡眠期間持續執行；pika 不會把工作搬到雲端。
---
先看最後訊息是否等待核准、提問、完成或發生錯誤，再檢查應用程式、Wi-Fi、VPN 和登入。下方唯讀命令顯示電源要求與近期事件；要求存在或 CPU 用量低都不能證明 AI 工作進度。
---
開蓋執行下方迴圈，保持終端機開啟，鎖定約三分鐘後檢查時間間隔。按 Ctrl+C 結束。長空白要與電源紀錄比較，也要查看 AI 紀錄與檔案修改時間。這只檢查簡單本機程序，闔蓋需另外測試。
---
安裝 pika 與輔助服務，開啟 Session；不需維持畫面時將 Monitor 關閉，再闔蓋。畫面策略在闔蓋後套用。Session OFF 解除防睡眠並顯示 Monitor OFF，不會立即關閉畫面。接上電源、保持通風，勿放在密閉包內執行。保護機制或服務故障可能停止工作階段。
---
Monitor OFF 不會下令結束 AI 工作。tmux 不會防止系統睡眠；caffeinate 不處理網路或核准等待。pika MCP 的狀態也不是所有 AI 工作的進度。
---
依 2026 年 10 月 5 日官方文件與 pika 實作撰寫。本文由 pika 製作者提供，不保證所有硬體持續運作。''')

add('es', 'Mac bloqueado: ¿siguen trabajando Claude Code y Codex?',
'Distingue bloqueo, pantalla apagada y reposo antes de dejar una tarea de IA local con la tapa cerrada.',
'Bloqueo y reposo|Local o nube|Qué revisar primero|Prueba de tres minutos|Configurar pika|Preguntas frecuentes|Fuentes y alcance',
'''La pantalla de contraseña no demuestra que la tarea haya terminado. Los comandos en segundo plano pueden continuar si el Mac está despierto y la aplicación y sus conexiones siguen disponibles. La automatización visual o la autenticación pueden necesitar desbloqueo. El sistema puede entrar en reposo después de bloquearse; conserva la protección por contraseña.
---
Codex CLI trabaja con archivos y comandos locales; una tarea delegada a Codex Cloud se ejecuta en otro entorno. Claude Code Remote Control sigue conectado a una sesión local. Reconectar no significa haber trabajado durante el reposo. pika no traslada tareas a la nube.
---
Revisa el último mensaje: aprobación, pregunta, finalización o error. Comprueba después aplicación, Wi-Fi, VPN y sesión iniciada. Los comandos de consulta siguientes muestran solicitudes de energía y eventos; no prueban el progreso de la IA ni lo demuestra un uso bajo de CPU.
---
Con la tapa abierta, ejecuta el bucle, deja la terminal abierta y bloquea unos tres minutos. Compara las horas y termina con Ctrl+C. Contrasta huecos con registros de energía y comprueba también los resultados de la IA. Solo verifica un proceso simple; prueba la tapa cerrada por separado.
---
Instala pika y su servicio auxiliar. Activa Session, deja Monitor OFF si no necesitas la pantalla y cierra la tapa. La política de pantalla se aplica al cerrarla. Session OFF libera la prevención del reposo sin apagar inmediatamente la pantalla. Usa alimentación y una mesa ventilada, nunca una bolsa cerrada. La protección o fallos del servicio pueden detener la sesión.
---
Monitor OFF no ordena terminar la IA. tmux no impide el reposo y caffeinate no soluciona aprobaciones ni fallos de red. El estado de pika MCP no refleja todos los trabajos de Claude Code o Codex.
---
Documentación oficial e implementación de pika revisadas el 5 de octubre de 2026. Guía del creador de pika, sin garantía de ejecución continua en todos los equipos.''')

add('fr', 'Mac verrouillé : Claude Code et Codex continuent-ils à travailler ?',
'Distinguez verrouillage, écran éteint et veille pour vérifier vos tâches IA locales avant de fermer le MacBook.',
'Verrouillage et veille|Local ou cloud|Causes à vérifier|Un contrôle de trois minutes|Configurer pika|Questions courantes|Sources et portée',
'''L’écran de mot de passe ne prouve pas l’arrêt d’une tâche. Les commandes en arrière-plan peuvent continuer si le Mac reste éveillé, avec l’application et les connexions nécessaires. Les opérations graphiques ou d’authentification peuvent nécessiter un déverrouillage. Le Mac peut se mettre en veille après le verrouillage ; gardez la protection par mot de passe.
---
Codex CLI utilise des fichiers et commandes locaux ; une tâche déléguée à Codex Cloud s’exécute dans un autre environnement. Claude Code Remote Control reste une connexion à une session locale. Une reconnexion ne prouve pas une activité pendant la veille. pika ne transfère pas les tâches vers le cloud.
---
Lisez le dernier message : autorisation, question, fin ou erreur. Vérifiez ensuite application, Wi-Fi, VPN et connexion au compte. Les commandes en lecture seule ci-dessous montrent les demandes d’énergie et événements, pas la réussite de l’IA. Une faible activité CPU ne suffit pas non plus.
---
Couvercle ouvert, lancez la boucle, laissez le terminal ouvert et verrouillez environ trois minutes. Comparez les heures puis arrêtez avec Ctrl+C. Confrontez les interruptions aux journaux d’énergie et aux résultats de l’IA. Ce test ne vérifie qu’un processus simple ; testez séparément le couvercle fermé.
---
Installez pika et son service auxiliaire. Activez Session, laissez Monitor OFF si l’écran est inutile et fermez le couvercle. La politique d’affichage s’applique alors. Session OFF libère la prévention de veille sans éteindre immédiatement l’écran. Utilisez une alimentation et un bureau ventilé, jamais un sac fermé. Protection ou panne du service peuvent arrêter la session.
---
Monitor OFF ne termine pas la tâche IA. tmux ne bloque pas la veille et caffeinate ne résout ni autorisations ni réseau. L’état de pika MCP ne représente pas la progression de toutes les tâches IA.
---
Sources officielles et code pika consultés le 5 octobre 2026. Guide rédigé par le créateur de pika, sans garantie de fonctionnement continu sur tous les appareils.''')

add('de', 'Mac gesperrt: Arbeiten Claude Code und Codex weiter?',
'Unterscheide Bildschirmsperre, ausgeschaltetes Display und Ruhezustand bei lokalen KI-Aufgaben.',
'Sperre oder Ruhezustand|Lokal oder Cloud|Ursachen prüfen|Drei Minuten testen|pika einrichten|Häufige Fragen|Quellen und Geltungsbereich',
'''Ein Passwortbildschirm beweist keinen Aufgabenabbruch. Hintergrundbefehle können weiterlaufen, wenn Mac, App und benötigte Verbindungen aktiv bleiben. Grafische Bedienung oder Authentifizierung kann Entsperren erfordern. Nach der Sperre kann später der Ruhezustand folgen. Lass den Passwortschutz eingeschaltet.
---
Codex CLI verarbeitet Dateien und Befehle lokal; an Codex Cloud übergebene Aufgaben laufen in einer anderen Umgebung. Claude Code Remote Control verbindet weiterhin eine lokale Sitzung. Wiederverbinden beweist keine Ausführung während des Schlafens. pika verschiebt Aufgaben nicht in die Cloud.
---
Prüfe die letzte Nachricht auf Freigaben, Fragen, Abschluss oder Fehler. Prüfe dann App, WLAN, VPN und Anmeldung. Die folgenden Lesebefehle zeigen Energieanforderungen und Ereignisse, nicht den KI-Fortschritt. Auch geringe CPU-Last beweist keinen Stillstand.
---
Starte die Schleife bei offenem Deckel, lass das Terminal offen und sperre etwa drei Minuten. Vergleiche die Zeitstempel und beende mit Ctrl+C. Vergleiche Lücken mit Energieprotokollen und KI-Ergebnissen. Dies testet nur einen einfachen Prozess; geschlossenen Deckel separat testen.
---
Installiere pika samt Hilfsdienst, aktiviere Session und lasse Monitor OFF, falls kein Display nötig ist. Schließe dann den Deckel; erst dann greift die Display-Richtlinie. Session OFF gibt den Ruhezustand wieder frei, ohne das Display sofort auszuschalten. Nutze Stromversorgung und einen belüfteten Tisch, keine geschlossene Tasche. Schutzfunktionen oder Dienstfehler können die Sitzung stoppen.
---
Monitor OFF beendet nicht die KI. tmux verhindert keinen Systemschlaf; caffeinate löst weder Netzwerkprobleme noch Freigaben. Der pika-MCP-Status ist kein Fortschrittsbericht sämtlicher KI-Aufgaben.
---
Offizielle Quellen und pika-Code geprüft am 5. Oktober 2026. Vom pika-Entwickler verfasst; keine Garantie für unterbrechungsfreien Betrieb auf jedem Gerät.''')

add('pt-BR', 'Mac bloqueado: Claude Code e Codex continuam trabalhando?',
'Entenda bloqueio, tela apagada e repouso ao acompanhar tarefas locais de IA.',
'Bloqueio não é repouso|Local ou nuvem|O que verificar|Teste de três minutos|Configurar pika|Perguntas comuns|Fontes e escopo',
'''A tela de senha não comprova que o trabalho parou. Comandos em segundo plano podem continuar com o Mac acordado, aplicativo aberto e conexões disponíveis. Automação visual e autenticação podem exigir desbloqueio. O repouso pode ocorrer depois do bloqueio. Mantenha a proteção por senha.
---
Codex CLI usa arquivos e comandos locais; tarefas delegadas ao Codex Cloud executam em outro ambiente. Claude Code Remote Control ainda conecta uma sessão local. Reconectar não significa executar durante o repouso. pika não transfere tarefas à nuvem.
---
Leia a última mensagem: aprovação, pergunta, conclusão ou erro. Depois confira aplicativo, Wi-Fi, VPN e login. Os comandos de leitura abaixo mostram solicitações de energia e eventos, não o progresso da IA. CPU baixa também não prova falha.
---
Com a tampa aberta, execute o loop, mantenha o terminal e bloqueie por cerca de três minutos. Compare horários e encerre com Ctrl+C. Confira lacunas nos registros de energia e os resultados da IA. Isso testa apenas um processo simples; teste a tampa fechada separadamente.
---
Instale pika e o serviço auxiliar, ligue Session, mantenha Monitor OFF se não precisar da tela e feche a tampa. A política de tela é aplicada ao fechar. Session OFF libera o repouso sem apagar imediatamente a tela. Use energia e mesa ventilada, nunca bolsa fechada. Proteções ou falhas do serviço podem parar a sessão.
---
Monitor OFF não encerra a IA. tmux não impede o repouso; caffeinate não resolve rede nem aprovações. O estado de pika MCP não representa todos os trabalhos de IA.
---
Fontes oficiais e implementação verificadas em 5 de outubro de 2026. Guia do criador de pika, sem garantia de execução contínua em todos os dispositivos.''')

add('ru', 'Mac заблокирован: продолжат ли работу Claude Code и Codex?',
'Разберитесь в блокировке, выключении экрана и сне при работе с локальными ИИ-задачами.',
'Блокировка и сон|Локально или в облаке|Что проверить|Проверка за три минуты|Настройка pika|Частые вопросы|Источники и рамки',
'''Экран пароля не доказывает остановку задачи. Фоновые команды могут выполняться, пока Mac бодрствует, приложение открыто и нужные соединения доступны. Управлению интерфейсом и авторизации может потребоваться разблокировка. После блокировки система может позднее уснуть. Не отключайте пароль.
---
Codex CLI работает с локальными файлами и командами; задачи Codex Cloud выполняются в другой среде. Claude Code Remote Control также подключается к локальной сессии. Переподключение не означает работу во время сна. pika не переносит задачи в облако.
---
Проверьте последнее сообщение: ожидание разрешения, вопрос, завершение или ошибка. Затем приложение, Wi-Fi, VPN и вход в аккаунт. Команды ниже только читают запросы питания и события; они не доказывают прогресс ИИ. Низкая загрузка CPU тоже не означает сбой.
---
С открытой крышкой запустите цикл, оставьте терминал открытым и заблокируйте экран примерно на три минуты. Сравните время и завершите Ctrl+C. Сопоставьте пропуски с журналом питания и результатами ИИ. Проверяется лишь простой процесс; закрытую крышку тестируйте отдельно.
---
Установите pika и вспомогательную службу, включите Session, оставьте Monitor OFF, если экран не нужен, и закройте крышку. Политика экрана применяется после закрытия. Session OFF снимает запрет сна без немедленного выключения экрана. Используйте питание и проветриваемый стол, не закрытую сумку. Защита или сбой службы могут остановить сессию.
---
Monitor OFF не завершает ИИ-задачу. tmux не предотвращает сон; caffeinate не решает проблемы сети и разрешений. Статус pika MCP не показывает ход всех задач ИИ.
---
Официальные источники и код pika проверены 5 октября 2026 года. Материал автора pika, без гарантии непрерывной работы на любом устройстве.''')

add('id', 'Mac terkunci: apakah Claude Code dan Codex tetap bekerja?',
'Bedakan layar terkunci, layar mati, dan tidur sistem saat memeriksa pekerjaan AI lokal.',
'Kunci layar dan tidur|Lokal atau cloud|Periksa penyebabnya|Uji tiga menit|Pengaturan pika|Pertanyaan umum|Sumber dan cakupan',
'''Layar kata sandi bukan bukti pekerjaan berhenti. Perintah latar dapat berjalan jika Mac tetap terjaga, aplikasi terbuka, dan koneksi tersedia. Otomasi tampilan atau autentikasi mungkin perlu membuka kunci. Sistem juga bisa tidur setelah layar terkunci. Pertahankan perlindungan kata sandi.
---
Codex CLI memakai berkas dan perintah lokal; pekerjaan Codex Cloud berjalan di lingkungan terpisah. Claude Code Remote Control tetap terhubung ke sesi lokal. Tersambung kembali bukan berarti pekerjaan berjalan selama tidur. pika tidak memindahkan pekerjaan ke cloud.
---
Baca pesan terakhir: persetujuan, pertanyaan, selesai, atau kesalahan. Lalu periksa aplikasi, Wi-Fi, VPN, dan login. Perintah baca-saja di bawah menunjukkan permintaan daya dan kejadian, bukan kemajuan AI. CPU rendah juga bukan bukti kegagalan.
---
Jalankan loop dengan penutup terbuka, biarkan terminal terbuka, lalu kunci sekitar tiga menit. Bandingkan waktu dan hentikan dengan Ctrl+C. Cocokkan jeda dengan log daya serta hasil AI. Ini hanya menguji proses sederhana; uji penutup tertutup secara terpisah.
---
Pasang pika dan layanan pendamping, aktifkan Session, pilih Monitor OFF bila layar tidak diperlukan, lalu tutup penutup. Kebijakan layar berlaku setelah penutup ditutup. Session OFF melepas pencegahan tidur tanpa langsung mematikan layar. Gunakan daya dan meja berventilasi, bukan tas tertutup. Perlindungan atau gangguan layanan dapat menghentikan sesi.
---
Monitor OFF bukan perintah menghentikan AI. tmux tidak mencegah tidur; caffeinate tidak mengatasi jaringan atau persetujuan. Status pika MCP bukan kemajuan semua pekerjaan AI.
---
Dokumentasi resmi dan implementasi diperiksa 5 Oktober 2026. Panduan dari pembuat pika, tanpa jaminan operasi tanpa putus pada semua perangkat.''')

add('vi', 'Mac đã khóa: Claude Code và Codex có tiếp tục chạy không?',
'Phân biệt khóa màn hình, tắt màn hình và ngủ hệ thống để kiểm tra tác vụ AI cục bộ.',
'Khóa khác với ngủ|Cục bộ hay đám mây|Kiểm tra nguyên nhân|Thử trong ba phút|Thiết lập pika|Câu hỏi thường gặp|Nguồn và phạm vi',
'''Màn hình mật khẩu không chứng minh tác vụ đã dừng. Lệnh nền có thể tiếp tục khi Mac còn thức, ứng dụng mở và kết nối cần thiết hoạt động. Tự động hóa giao diện hoặc xác thực có thể cần mở khóa. Máy cũng có thể ngủ sau khi khóa. Hãy giữ bảo vệ mật khẩu.
---
Codex CLI xử lý tệp và lệnh cục bộ; tác vụ giao cho Codex Cloud chạy ở môi trường khác. Claude Code Remote Control vẫn kết nối phiên cục bộ. Kết nối lại không có nghĩa là đã chạy trong lúc ngủ. pika không chuyển tác vụ lên đám mây.
---
Đọc thông báo cuối: chờ duyệt, câu hỏi, hoàn tất hay lỗi. Sau đó kiểm tra ứng dụng, Wi-Fi, VPN và đăng nhập. Lệnh chỉ đọc bên dưới hiển thị yêu cầu nguồn và sự kiện, không chứng minh tiến độ AI. CPU thấp cũng không chứng minh lỗi.
---
Mở nắp, chạy vòng lặp, giữ terminal mở và khóa khoảng ba phút. So sánh thời gian, dừng bằng Ctrl+C. Đối chiếu khoảng trống với nhật ký nguồn và kết quả AI. Đây chỉ là kiểm tra tiến trình đơn giản; cần thử đóng nắp riêng.
---
Cài pika và dịch vụ hỗ trợ, bật Session, để Monitor OFF nếu không cần màn hình, rồi đóng nắp. Chính sách màn hình áp dụng sau khi đóng. Session OFF bỏ ngăn ngủ mà không tắt ngay màn hình. Dùng nguồn điện và bàn thoáng, không đặt trong túi kín. Bảo vệ hoặc lỗi dịch vụ có thể dừng phiên.
---
Monitor OFF không kết thúc AI. tmux không ngăn ngủ; caffeinate không xử lý mạng hoặc chờ duyệt. Trạng thái pika MCP không phản ánh mọi tác vụ AI.
---
Đối chiếu tài liệu chính thức và mã pika ngày 5 tháng 10 năm 2026. Hướng dẫn do nhà phát triển pika viết, không bảo đảm chạy liên tục trên mọi máy.''')

add('hi', 'Mac लॉक होने पर क्या Claude Code और Codex काम करते रहते हैं?',
'स्थानीय AI काम के लिए स्क्रीन लॉक, डिस्प्ले बंद होने और सिस्टम स्लीप का अंतर समझें।',
'लॉक और स्लीप अलग हैं|स्थानीय या क्लाउड|पहले क्या जाँचें|तीन मिनट की जाँच|pika की सेटिंग|आम सवाल|स्रोत और दायरा',
'''पासवर्ड स्क्रीन दिखना काम रुकने का प्रमाण नहीं है। Mac जागा रहे, ऐप खुला हो और आवश्यक कनेक्शन उपलब्ध हों तो सामान्य बैकग्राउंड कमांड चल सकते हैं। स्क्रीन पर क्लिक या प्रमाणीकरण वाले चरणों में अनलॉक करना पड़ सकता है। लॉक के बाद सिस्टम स्लीप में जा सकता है। पासवर्ड सुरक्षा बनाए रखें।
---
Codex CLI स्थानीय फ़ाइलों और कमांड पर काम करता है; Codex Cloud को सौंपे काम अलग वातावरण में चलते हैं। Claude Code Remote Control भी स्थानीय सत्र से जुड़ता है। दोबारा जुड़ना स्लीप के दौरान काम होने का प्रमाण नहीं है। pika काम को क्लाउड में नहीं भेजता।
---
आखिरी संदेश में अनुमति, सवाल, समाप्ति या त्रुटि देखें। फिर ऐप, Wi-Fi, VPN और लॉगिन जाँचें। नीचे के केवल पढ़ने वाले कमांड पावर अनुरोध और घटनाएँ दिखाते हैं, AI की प्रगति नहीं। कम CPU उपयोग भी विफलता का प्रमाण नहीं है।
---
ढक्कन खुला रखकर लूप चलाएँ, टर्मिनल खुला छोड़ें और लगभग तीन मिनट लॉक करें। समय की तुलना करें और Ctrl+C से रोकें। बड़े अंतर को पावर लॉग और AI परिणामों से मिलाएँ। यह केवल साधारण प्रक्रिया जाँचता है; बंद ढक्कन का परीक्षण अलग करें।
---
pika और सहायक सेवा स्थापित करें, Session ON करें, स्क्रीन आवश्यक न हो तो Monitor OFF रखें और ढक्कन बंद करें। स्क्रीन नीति ढक्कन बंद होने के बाद लागू होती है। Session OFF स्लीप रोकना हटाता है, तुरंत स्क्रीन बंद नहीं करता। बिजली और हवादार मेज का उपयोग करें, बंद बैग का नहीं। सुरक्षा या सेवा त्रुटि सत्र रोक सकती है।
---
Monitor OFF AI समाप्त करने का आदेश नहीं है। tmux स्लीप नहीं रोकता; caffeinate नेटवर्क या अनुमति की समस्या नहीं सुलझाता। pika MCP की स्थिति सभी AI काम की प्रगति नहीं दर्शाती।
---
5 अक्टूबर 2026 को आधिकारिक दस्तावेज़ और pika कोड जाँचे गए। pika निर्माता की गाइड; हर उपकरण पर लगातार चलने की गारंटी नहीं।''')

add('ar', 'هل يواصل Claude Code وCodex العمل عند قفل Mac؟',
'ميّز بين قفل الشاشة وإطفائها وسكون النظام عند متابعة مهام الذكاء الاصطناعي المحلية.',
'القفل ليس السكون|محلي أم سحابي|ما الذي تفحصه أولاً|اختبار ثلاث دقائق|إعداد pika|أسئلة شائعة|المصادر والنطاق',
'''ظهور شاشة كلمة المرور لا يثبت توقف المهمة. قد تستمر أوامر الخلفية إذا بقي Mac مستيقظاً والتطبيق والاتصالات اللازمة متاحة. قد تتطلب أتمتة الواجهة أو المصادقة فتح القفل. وقد يدخل النظام السكون بعد القفل. أبقِ حماية كلمة المرور مفعلة.
---
يستخدم Codex CLI الملفات والأوامر المحلية، بينما تعمل المهمة المفوضة إلى Codex Cloud في بيئة منفصلة. يتصل Claude Code Remote Control أيضاً بجلسة محلية. إعادة الاتصال لا تعني استمرار التنفيذ أثناء السكون. لا ينقل pika المهام إلى السحابة.
---
اقرأ الرسالة الأخيرة بحثاً عن طلب موافقة أو سؤال أو انتهاء أو خطأ. ثم افحص التطبيق وWi-Fi وVPN وتسجيل الدخول. تعرض أوامر القراءة أدناه طلبات الطاقة والأحداث، ولا تثبت تقدم الذكاء الاصطناعي. انخفاض استخدام المعالج لا يثبت الفشل أيضاً.
---
شغّل الحلقة والغطاء مفتوح، واترك الطرفية مفتوحة واقفل الشاشة نحو ثلاث دقائق. قارن الأوقات وأوقف الحلقة باستخدام Ctrl+C. قارن الفجوات بسجلات الطاقة ونتائج المهمة. هذا يفحص عملية بسيطة فقط؛ اختبر إغلاق الغطاء بشكل منفصل.
---
ثبّت pika وخدمته المساعدة، وفعّل Session واترك Monitor OFF إن لم تحتج الشاشة، ثم أغلق الغطاء. تطبق سياسة الشاشة بعد الإغلاق. يحرر Session OFF منع السكون دون إطفاء الشاشة فوراً. استخدم الطاقة ومكتباً جيد التهوية، لا حقيبة مغلقة. قد توقف الحماية أو أخطاء الخدمة الجلسة.
---
Monitor OFF ليس أمراً بإنهاء مهمة الذكاء الاصطناعي. لا يمنع tmux سكون النظام، ولا يحل caffeinate مشكلات الشبكة أو الموافقات. حالة pika MCP لا تمثل تقدم جميع المهام.
---
رُوجعت الوثائق الرسمية وتنفيذ pika في 5 أكتوبر 2026. دليل من صانع pika، وليس ضماناً للتشغيل المتواصل على كل الأجهزة.''')

add('th', 'ล็อก Mac แล้ว Claude Code และ Codex ยังทำงานต่อหรือไม่?',
'แยกการล็อกหน้าจอ ปิดจอ และพักเครื่อง เพื่อตรวจงาน AI ที่ทำบน Mac ก่อนปิดฝา',
'ล็อกกับพักเครื่องต่างกัน|ทำงานในเครื่องหรือคลาวด์|ตรวจสาเหตุก่อน|ทดสอบสามนาที|ตั้งค่า pika|คำถามทั่วไป|แหล่งข้อมูลและขอบเขต',
'''หน้าจอรหัสผ่านไม่ได้ยืนยันว่างานหยุด คำสั่งเบื้องหลังอาจทำต่อได้หาก Mac ยังตื่น แอปเปิด และการเชื่อมต่อพร้อม แต่การควบคุมหน้าจอหรือยืนยันตัวตนอาจต้องปลดล็อก ระบบอาจพักเครื่องภายหลังการล็อก ควรคงการป้องกันด้วยรหัสผ่านไว้
---
Codex CLI ใช้ไฟล์และคำสั่งในเครื่อง ส่วนงานที่ส่งให้ Codex Cloud ทำงานในสภาพแวดล้อมอื่น Claude Code Remote Control ก็ยังเชื่อมกับเซสชันในเครื่อง การเชื่อมใหม่ไม่ได้แปลว่าทำงานระหว่างพักเครื่อง pika ไม่ได้ย้ายงานขึ้นคลาวด์
---
อ่านข้อความล่าสุดว่ารออนุมัติ คำตอบ จบงาน หรือมีข้อผิดพลาด แล้วตรวจแอป Wi-Fi VPN และการเข้าสู่ระบบ คำสั่งอ่านอย่างเดียวด้านล่างแสดงคำขอพลังงานและเหตุการณ์ ไม่ใช่หลักฐานความคืบหน้า AI และ CPU ต่ำก็ไม่ได้ยืนยันว่างานเสีย
---
เปิดฝา รันลูป เปิดเทอร์มินัลค้างไว้ แล้วล็อกประมาณสามนาที เปรียบเทียบเวลาและหยุดด้วย Ctrl+C เทียบช่วงเวลาที่หายไปกับบันทึกพลังงานและผลลัพธ์ AI วิธีนี้ตรวจเพียงโปรเซสง่าย ๆ ต้องทดสอบตอนปิดฝาแยกต่างหาก
---
ติดตั้ง pika และบริการช่วย เปิด Session และให้ Monitor OFF หากไม่ต้องใช้จอ แล้วปิดฝา นโยบายจอใช้หลังปิดฝา Session OFF ยกเลิกการป้องกันพักเครื่องโดยไม่ดับจอทันที ใช้ไฟเลี้ยงและโต๊ะระบายอากาศ ไม่ใช้ในกระเป๋าปิด ระบบป้องกันหรือบริการผิดพลาดอาจหยุดเซสชัน
---
Monitor OFF ไม่ได้สั่งจบงาน AI ส่วน tmux ไม่ป้องกันพักเครื่อง และ caffeinate ไม่แก้เครือข่ายหรือการรออนุมัติ สถานะ pika MCP ไม่ใช่ความคืบหน้าของงาน AI ทั้งหมด
---
ตรวจเอกสารทางการและโค้ด pika วันที่ 5 ตุลาคม 2026 คู่มือโดยผู้สร้าง pika ไม่ได้รับประกันการทำงานต่อเนื่องบนทุกเครื่อง''')
