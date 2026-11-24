"""Localized, beginner-friendly guide to parallel AI work with Git worktrees."""
COPY = {}


def add(locale, title, intro, headings, flow, body):
    COPY[locale] = dict(title=title, intro=intro, headings=headings.split('|'), flow=flow.split('|'),
        paragraphs=[s.strip().split('\n\n') for s in body.strip().split('\n---\n')])


add('en', 'Two AI agents editing the same files? Give them separate folders.',
'Git worktree gives each AI agent its own working folder. Here is how to separate tasks, review changes, and bring them together without mixing unfinished work.',
'One folder, two agents: where edits collide|Start with a reviewed baseline|Create two working folders|Give each agent a folder and a clear task|Review before bringing work together|Where pika fits|Sources and scope',
'Separate folders|Assign tasks|Review changes|Integrate one at a time', '''
One agent updates the interface while another writes tests. If both use the same folder, they see and can change the same files. Creating two branch names does not give that one folder two independent sets of files. Switching branches there also changes the files the other agent is using.

A Git worktree is another working folder attached to the same repository. Each folder can have its own branch and checked-out files, while sharing repository history. It separates work in progress; it does not prevent two agents from eventually proposing conflicting changes.
---
Run the command below in your existing Git project. This example requires at least one commit, so HEAD points to a committed baseline. An empty status output means Git reports no tracked changes or untracked files; ignored files may still be present.

If anything is listed, review it first. Save only the intended, reviewed changes in a commit, or choose an already committed baseline. Do not blindly stage the entire folder: credentials and unrelated work must stay out. The new folders start from HEAD, not from your uncommitted edits.
---
The commands below create ai-ui and ai-tests branches, with working folders beside your current project. Run both from the original project. Use branch names and destination paths that do not already exist; if they are taken, choose different names rather than forcing an overwrite.

These folders share Git history, but they do not automatically copy installed dependencies, ignored .env files, or every local setting. Install dependencies as required by the project. Supply only the credentials each task needs, and use different ports if both tasks start development servers. Worktrees are not security sandboxes: tools may still access other folders if their permissions allow it.
---
Open one agent in project-ai-ui and the other in project-ai-tests. Give each its exact absolute folder path and a narrow task: for example, “Edit only the interface component” and “Add tests for existing behavior; do not change application code.”

Name shared files that require coordination, such as dependency manifests and lockfiles. If both tasks need the same file, handle them in sequence or agree on which agent owns it. Ask each agent to report changed files, checks performed, and unfinished work before you accept its result.
---
In each working folder, run the three commands below. Status lists changed and untracked files. The first diff shows unstaged tracked edits; the cached diff shows staged edits. New untracked files do not appear in these diffs: open and review them separately.

Run the project's relevant checks, review the result, and commit the intended changes on that folder's branch. Then return to the original project and review and integrate one branch at a time into your intended destination branch. Worktrees never merge the results automatically. If changes overlap, resolve the conflict and check the combined result before adding the next branch.
---
pika can help keep your Mac awake while local agents work, subject to its session settings and safety protections. It does not assign tasks, merge branches, or resolve conflicts. In pika 1.3, QR access shows Mac status and approved power controls, not AI output or a reliable AI completion percentage. Use each agent's own output and your project checks to judge whether the work is done.
---
This guide is written by the maker of no-sleep-pika. The workflow follows Git's official documentation and uses generic AI agents; it does not assume a particular agent's permissions or features. Follow your project's contribution and secret-handling rules as well.
''')

add('ko', 'AI 에이전트 둘이 같은 파일을 고치면? 작업 폴더부터 나누세요',
'AI에게 동시에 일을 맡길 때는 작업 폴더도 나누세요. Git worktree로 변경 사항이 섞이지 않게 작업하고, 결과를 검토한 뒤 합치는 방법을 설명합니다.',
'한 폴더에서 둘이 일하면 생기는 문제|먼저 출발점을 확인하세요|작업 폴더를 두 개 만드세요|에이전트마다 폴더와 담당 범위를 정하세요|각각 검토하고 하나씩 합치세요|오래 걸리는 작업과 pika|공식 자료와 이 글의 범위',
'폴더 나누기|작업 맡기기|변경 검토하기|하나씩 합치기', '''
한 AI에게 화면 수정을, 다른 AI에게 테스트 작성을 맡겼다고 해볼게요. 둘 다 같은 폴더를 쓰면 같은 파일을 보고 고칩니다. 브랜치 이름을 두 개 만드는 것만으로 그 폴더 속 파일까지 두 벌이 되지는 않습니다. 그곳에서 브랜치를 바꾸면 다른 AI가 작업 중인 파일도 바뀝니다.

브랜치는 변경을 쌓아 가는 작업 갈래입니다. Git worktree는 같은 저장소에 연결된 작업 폴더를 추가하는 기능입니다. 변경 이력은 공유하면서, 폴더마다 별도 브랜치와 파일을 둘 수 있습니다. 진행 중인 작업을 나누는 데 도움이 되지만, 나중에 합칠 때 충돌이 없다는 뜻은 아닙니다.
---
기존 Git 프로젝트 폴더에서 아래 명령부터 실행하세요. 커밋은 변경 내용을 Git에 기록한 것입니다. 이 예시는 커밋이 하나 이상 있어야 합니다. HEAD는 현재 커밋된 출발점을 가리킵니다. 결과가 비어 있으면 Git이 확인하는 변경 파일과 미추적 파일이 없다는 뜻입니다. Git에서 제외한 파일은 남아 있을 수 있습니다.

목록에 파일이 나오면 먼저 내용을 확인하세요. 필요한 변경만 검토해서 커밋하거나, 이미 커밋된 출발점을 선택해야 합니다. 폴더 전체를 무작정 추가하면 비밀키나 관련 없는 작업까지 섞일 수 있습니다. 새 작업 폴더에는 아직 커밋하지 않은 변경이 복사되지 않습니다. HEAD가 가리키는 커밋에서 시작합니다.
---
아래 두 명령을 원래 프로젝트 폴더에서 실행하면 ai-ui, ai-tests 브랜치와 작업 폴더가 생깁니다. 새 폴더는 현재 프로젝트 폴더의 옆에 만들어집니다. 브랜치 이름과 경로가 이미 사용 중이면 다른 이름을 고르세요. 기존 폴더를 덮어쓰거나 지울 필요는 없습니다.

변경 이력을 공유해도 설치한 라이브러리나 Git에서 제외한 .env 파일, 로컬 설정이 모두 복사되지는 않습니다. 프로젝트 안내에 따라 필요한 항목을 준비하고, 비밀키는 작업에 필요한 것만 제공하세요. 개발 서버를 두 개 띄운다면 포트도 나누세요. worktree는 보안 격리 공간이 아니므로, 권한이 있는 도구는 다른 폴더에도 접근할 수 있습니다.
---
한 에이전트는 project-ai-ui에서, 다른 에이전트는 project-ai-tests에서 시작하세요. 각각 정확한 절대 경로와 좁은 작업 범위를 알려주세요. 예를 들어 “화면 컴포넌트만 수정”과 “기존 동작의 테스트 추가, 앱 코드는 수정하지 않기”처럼 나눌 수 있습니다.

의존성 목록이나 잠금 파일처럼 함께 건드리기 쉬운 파일은 담당자를 정하세요. 같은 파일을 꼭 수정해야 한다면 순서대로 작업하는 편이 낫습니다. 완료 보고에는 바꾼 파일, 실행한 검사, 남은 일을 적게 하면 검토하기 쉽습니다.
---
각 작업 폴더에서 아래 세 명령을 실행하세요. status는 변경 파일과 새로 생긴 미추적 파일을 보여줍니다. git diff는 아직 커밋 대상으로 올리지 않은 기존 파일의 변경을, git diff --cached는 커밋 대상으로 올린 변경을 보여줍니다. 새 미추적 파일은 이 diff에 나오지 않으니 직접 열어 확인하세요.

프로젝트에 필요한 검사를 실행하고, 의도한 변경만 해당 폴더의 브랜치에 커밋하세요. 원래 프로젝트로 돌아온 뒤에는 합칠 대상 브랜치에서 결과를 하나씩 검토하고 반영합니다. worktree가 자동으로 합쳐주지는 않습니다. 겹친 수정은 직접 해결하고, 합쳐진 결과를 확인한 뒤 다음 브랜치를 반영하세요.
---
pika는 세션 설정과 안전 보호 조건에 따라 로컬 AI가 일하는 동안 맥이 깨어 있도록 도울 수 있습니다. 작업 배분이나 브랜치 병합, 충돌 해결을 대신하지는 않습니다. pika 1.3의 QR 연결에서 확인하는 것은 맥 상태와 허용된 전원 제어이며, AI의 출력이나 정확한 완료율이 아닙니다. 완료 여부는 에이전트의 결과와 프로젝트 검사로 확인하세요.
---
이 글은 no-sleep-pika 제작자가 Git 공식 자료를 바탕으로 작성한 일반적인 AI 작업 안내입니다. 특정 AI 도구의 기능이나 접근 권한을 전제로 하지 않습니다. 프로젝트의 기여 규칙과 비밀정보 관리 규칙도 함께 따르세요.
''')

add('ja', 'AIエージェント2つが同じファイルを編集？まず作業フォルダを分けよう',
'Git worktreeでAIごとに作業フォルダを用意。作業の切り分けから変更の確認、統合までをやさしく説明します。',
'同じフォルダで編集がぶつかる理由|確認済みのコミットから始める|作業フォルダを2つ作る|フォルダと担当範囲を指定する|確認して1つずつ統合する|pikaができること|資料と対象範囲',
'フォルダを分ける|作業を割り当てる|変更を確認する|順番に統合する', '''
画面の修正とテスト作成を別々のAIに頼んでも、同じフォルダなら同じファイルを編集します。ブランチ名を2つ作るだけでは、ファイルは2組になりません。その場でブランチを切り替えると、もう一方が使うファイルも変わります。

Git worktreeは同じリポジトリに別の作業フォルダを追加する機能です。履歴を共有しつつ、フォルダごとにブランチとファイルを持てます。ただし、後で変更を統合する際の競合までは防ぎません。
---
既存のGitプロジェクトで次のコマンドを実行します。この例には少なくとも1つのコミットが必要で、HEADがその出発点です。出力が空なら変更や未追跡ファイルは報告されていません。無視されたファイルは存在する場合があります。

一覧が出たら内容を確認し、意図した変更だけをコミットするか、既存のコミットを出発点にします。秘密情報や無関係な作業をまとめて追加しないでください。新しいフォルダは未コミットの編集ではなくHEADから始まります。
---
元のプロジェクトで次の2つのコマンドを実行すると、隣に作業フォルダとai-ui、ai-testsブランチが作られます。未使用の名前とパスを使い、既存のものを強制的に上書きしないでください。

インストール済みの依存関係、無視された.env、ローカル設定は自動では揃いません。プロジェクトの手順で準備し、必要な秘密情報だけを渡します。サーバーを同時に起動するならポートも分けます。worktreeはセキュリティ用の隔離環境ではなく、権限があれば他のフォルダにアクセスできます。
---
一方をproject-ai-ui、もう一方をproject-ai-testsで起動し、絶対パスと狭い担当範囲を伝えます。例えば「画面コンポーネントのみ修正」と「既存動作のテストのみ追加、アプリコードは変更しない」です。

依存関係一覧やロックファイルなど共有しやすいファイルは担当を決めます。同じファイルの編集が必要なら順番に進めましょう。変更したファイル、実施した確認、残作業を報告してもらいます。
---
各フォルダで次の3つを実行します。statusは変更と未追跡ファイル、diffはステージ前の追跡済みファイルの変更、diff --cachedはステージ済みの変更を表示します。未追跡ファイルはdiffに出ないため、個別に開いて確認します。

必要なチェックを行い、意図した変更を各ブランチにコミットします。元のプロジェクトに戻り、統合先のブランチで1つずつ確認して取り込みます。自動的には統合されません。競合を解決し、統合後の動作を確認してから次を取り込みます。
---
pikaはセッション設定と安全保護の条件に応じて、ローカルAIの作業中にMacを起こしておく手助けをします。担当分けやマージ、競合解決は行いません。pika 1.3のQR接続はMacの状態と許可された電源操作を表示し、AIの出力や正確な進捗率は表示しません。完了はAIの結果とプロジェクトのチェックで判断してください。
---
no-sleep-pikaの開発者がGit公式資料に基づいて書いた一般的な手順です。特定のAIの機能や権限を前提にしていません。プロジェクトの貢献規則と秘密情報の扱いにも従ってください。
''')

add('zh-CN', '两个 AI 同时改同一份文件？先把工作文件夹分开',
'用 Git worktree 为每个 AI 准备独立的工作文件夹，再检查修改、逐一合并，避免未完成的工作混在一起。',
'同一个文件夹为什么容易冲突|先确认提交起点|创建两个工作文件夹|明确文件夹和任务范围|检查后逐一整合|pika 能帮什么忙|资料与适用范围',
'分开文件夹|分配任务|检查修改|逐一整合', '''
让一个 AI 改界面、另一个写测试，如果都在同一文件夹里，它们仍会读写同一批文件。创建两个分支名不会让这个文件夹自动拥有两套文件。在这里切换分支，也会改变另一个 AI 正在使用的文件。

Git worktree 可以为同一仓库增加工作文件夹。各文件夹有自己的分支和检出文件，但共享仓库历史。它能分开进行中的修改，却不能保证以后合并时没有冲突。
---
在现有 Git 项目中运行下面的命令。本例要求至少已有一次提交，HEAD 指向提交起点。输出为空表示没有报告修改或未跟踪文件；被忽略的文件仍可能存在。

如果出现文件列表，先检查内容，只提交确实需要的修改，或选择已有提交作为起点。不要盲目添加整个文件夹，以免混入密钥或无关修改。新文件夹从 HEAD 开始，不会带上未提交的编辑。
---
在原项目运行这两条命令，会在旁边创建工作文件夹，以及 ai-ui 和 ai-tests 分支。分支名和目标路径都必须未被占用；已有同名项目时换一个名字，不要强行覆盖。

已安装的依赖、被忽略的 .env 和本地设置不会全部自动复制。按项目说明准备，只提供任务需要的凭据。如果同时启动开发服务器，应使用不同端口。worktree 不是安全沙箱：有权限的工具仍可访问其他文件夹。
---
分别在 project-ai-ui 和 project-ai-tests 启动 AI，明确告诉它绝对路径和有限的任务范围。例如“只改界面组件”和“为现有行为添加测试，不修改应用代码”。

依赖清单、锁文件等容易共同修改的文件要指定负责人。确实需要编辑同一文件时，按顺序处理。要求 AI 报告修改的文件、执行的检查和未完成事项。
---
在每个工作文件夹执行下面三条命令。status 列出修改和未跟踪文件；diff 显示已跟踪文件尚未暂存的修改；diff --cached 显示已暂存的修改。未跟踪的新文件不出现在这些 diff 中，需要另行打开检查。

运行项目所需检查，将确认后的修改提交到各自分支。再回到原项目，在目标分支上逐一审查和整合。worktree 不会自动合并结果。遇到重叠修改，解决冲突并检查整合后的结果，再处理下一个分支。
---
pika 可根据会话设置和安全保护条件，帮助本地 AI 工作时让 Mac 保持唤醒。它不会分配任务、合并分支或解决冲突。pika 1.3 的 QR 连接显示 Mac 状态和获准的电源控制，不显示 AI 输出或准确完成百分比。是否完成仍应检查 AI 结果和项目测试。
---
本文由 no-sleep-pika 开发者依据 Git 官方文档编写，适用于一般 AI 工作流程，不假定某款 AI 的具体功能或权限。也请遵守项目的贡献规范和机密信息管理要求。
''')

add('zh-TW', '兩個 AI 同時改同一份檔案？先把工作資料夾分開',
'用 Git worktree 為每個 AI 準備獨立工作資料夾，再檢查修改、逐一整合，避免尚未完成的工作混在一起。',
'同一個資料夾為什麼容易衝突|先確認提交起點|建立兩個工作資料夾|指定資料夾與任務範圍|檢查後逐一整合|pika 能幫什麼忙|資料與適用範圍',
'分開資料夾|分配任務|檢查修改|逐一整合', '''
讓一個 AI 改介面、另一個寫測試，如果都在同一資料夾，它們仍會讀寫同一批檔案。建立兩個分支名稱，不會讓資料夾自動有兩套檔案。在這裡切換分支，也會改變另一個 AI 正在使用的檔案。

Git worktree 能為同一儲存庫增加工作資料夾。各資料夾有自己的分支與取出的檔案，但共享版本歷史。它能分開進行中的修改，卻不保證日後整合時沒有衝突。
---
在現有 Git 專案執行以下指令。本例至少需要一筆提交，HEAD 指向提交起點。沒有輸出表示未回報修改或未追蹤檔案；被忽略的檔案仍可能存在。

若出現清單，先確認內容，只提交必要修改，或選擇已有提交作為起點。別盲目加入整個資料夾，以免包含金鑰或無關工作。新資料夾從 HEAD 開始，不會帶入尚未提交的編輯。
---
在原專案執行這兩條指令，會在旁邊建立工作資料夾及 ai-ui、ai-tests 分支。分支名稱和目標路徑必須尚未使用；若已存在，請換名稱，不要強制覆寫。

已安裝的相依套件、被忽略的 .env 與本機設定不會全部自動複製。依專案說明準備，只提供任務需要的憑證。同時啟動開發伺服器時，也要分開連接埠。worktree 不是安全沙箱：有權限的工具仍可存取其他資料夾。
---
分別在 project-ai-ui 和 project-ai-tests 啟動 AI，提供絕對路徑與明確的小任務。例如「只改介面元件」和「為現有行為新增測試，不修改應用程式碼」。

相依套件清單與鎖定檔等共用檔案應指定負責人。若必須修改同一檔案，就依序處理。請 AI 回報變動檔案、完成的檢查，以及剩餘工作。
---
在每個工作資料夾執行以下三條指令。status 列出修改與未追蹤檔案；diff 顯示已追蹤檔案尚未暫存的修改；diff --cached 顯示已暫存的修改。未追蹤的新檔案不會出現在這些 diff，需另外開啟檢查。

執行專案需要的檢查，把確認後的修改提交到各自分支。回到原專案，在目標分支逐一檢查並整合。worktree 不會自動合併結果。有重疊修改時，先解決衝突並確認整合結果，再處理下一個分支。
---
pika 可依工作階段設定與安全保護條件，協助本機 AI 工作時讓 Mac 保持喚醒。它不會分派任務、合併分支或解決衝突。pika 1.3 的 QR 連線顯示 Mac 狀態與獲准的電源控制，不顯示 AI 輸出或準確完成百分比。是否完成仍需檢查 AI 結果與專案測試。
---
本文由 no-sleep-pika 開發者依 Git 官方文件撰寫，說明一般 AI 工作流程，不假設特定 AI 的功能或權限。也請遵守專案的貢獻規則與機密資訊管理規範。
''')

add('es', '¿Dos agentes de IA editando los mismos archivos? Separa sus carpetas.',
'Con Git worktree, cada agente trabaja en su propia carpeta. Aprende a repartir tareas, revisar los cambios e integrarlos sin mezclar trabajo pendiente.',
'El problema de compartir una carpeta|Prepara un punto de partida revisado|Crea dos carpetas de trabajo|Asigna carpeta y tarea|Revisa e integra una rama cada vez|El papel de pika|Fuentes y alcance',
'Separar carpetas|Asignar tareas|Revisar cambios|Integrar por turnos', '''
Un agente modifica la interfaz y otro escribe pruebas. Si comparten carpeta, leen y cambian los mismos archivos. Crear dos nombres de rama no crea dos copias independientes en esa carpeta. Cambiar de rama allí también cambia los archivos que utiliza el otro agente.

Git worktree añade otra carpeta de trabajo al mismo repositorio. Cada una tiene sus archivos y puede usar su propia rama, compartiendo el historial. Separa el trabajo pendiente, pero no garantiza que las modificaciones sean compatibles al integrarlas.
---
Ejecuta el siguiente comando en un proyecto Git existente. Debe haber al menos un commit: HEAD será el punto de partida. Si no hay salida, Git no informa de cambios ni archivos sin seguimiento; aún puede haber archivos ignorados.

Si aparece una lista, revísala y confirma solo los cambios deseados, o elige un commit existente. No añadas toda la carpeta a ciegas: puede contener secretos o trabajo ajeno. Las nuevas carpetas parten de HEAD, no de las ediciones sin confirmar.
---
Ejecuta ambos comandos desde el proyecto original. Crean las ramas ai-ui y ai-tests y sus carpetas junto al proyecto. Los nombres y las rutas deben estar libres. Si ya existen, elige otros en lugar de forzar una sobrescritura.

Las dependencias instaladas, los archivos .env ignorados y los ajustes locales no se copian automáticamente. Sigue las instrucciones del proyecto, facilita solo las credenciales necesarias y usa puertos distintos para servidores simultáneos. Un worktree no es un entorno de seguridad aislado: una herramienta con permisos puede acceder a otras carpetas.
---
Abre un agente en project-ai-ui y otro en project-ai-tests. Indica la ruta absoluta y una tarea acotada: «modifica solo el componente visual» y «añade pruebas del comportamiento actual sin cambiar el código de la aplicación».

Asigna un responsable para archivos compartidos, como manifiestos de dependencias y archivos de bloqueo. Si ambos necesitan modificar el mismo archivo, trabaja por turnos. Pide una lista de archivos cambiados, comprobaciones realizadas y trabajo pendiente.
---
Ejecuta los tres comandos en cada carpeta. Status muestra cambios y archivos sin seguimiento. Diff muestra cambios no preparados en archivos seguidos; diff --cached muestra los preparados. Los archivos nuevos sin seguimiento no aparecen en estos diff: ábrelos por separado.

Ejecuta las comprobaciones pertinentes y confirma los cambios revisados en la rama de cada carpeta. Después vuelve al proyecto original e integra una rama cada vez en la rama de destino. Worktree no combina resultados automáticamente. Resuelve cualquier conflicto y comprueba el resultado conjunto antes de incorporar la siguiente rama.
---
pika ayuda a mantener el Mac despierto durante el trabajo local, según la configuración de sesión y sus protecciones. No reparte tareas, fusiona ramas ni resuelve conflictos. La conexión QR de pika 1.3 muestra el estado del Mac y controles de energía autorizados, no la salida de la IA ni un porcentaje fiable de finalización. Verifica los resultados del agente y las pruebas del proyecto.
---
Guía del creador de no-sleep-pika basada en la documentación oficial de Git. Se aplica a agentes genéricos, sin presuponer funciones o permisos de un producto concreto. Respeta también las normas del proyecto y el manejo de secretos.
''')

add('fr', 'Deux agents IA modifient les mêmes fichiers ? Séparez leurs dossiers.',
'Git worktree donne à chaque agent son propre dossier. Répartissez les tâches, vérifiez les changements puis intégrez-les sans mélanger les travaux en cours.',
'Pourquoi un dossier partagé pose problème|Préparer un point de départ vérifié|Créer deux dossiers de travail|Attribuer un dossier et une tâche|Vérifier puis intégrer une branche à la fois|Le rôle de pika|Sources et périmètre',
'Séparer les dossiers|Répartir les tâches|Vérifier les changements|Intégrer à tour de rôle', '''
Un agent modifie l’interface, l’autre écrit des tests. Dans un même dossier, ils lisent et modifient les mêmes fichiers. Deux noms de branche ne créent pas deux copies indépendantes. Changer de branche dans ce dossier change aussi les fichiers utilisés par l’autre agent.

Git worktree ajoute un dossier de travail au même dépôt. Chaque dossier peut avoir sa branche et ses fichiers, tout en partageant l’historique. Cela sépare les travaux en cours, sans garantir une intégration sans conflit.
---
Lancez la commande suivante dans un projet Git existant. Il faut au moins un commit : HEAD désigne le point de départ enregistré. Une sortie vide signifie qu’aucune modification ni fichier non suivi n’est signalé. Des fichiers ignorés peuvent toutefois être présents.

Si une liste apparaît, examinez-la puis enregistrez uniquement les modifications voulues, ou choisissez un commit existant. N’ajoutez pas tout le dossier sans vérification : secrets et travaux sans rapport doivent rester à l’écart. Les nouveaux dossiers partent de HEAD, pas des modifications non commitées.
---
Depuis le projet d’origine, ces commandes créent les branches ai-ui et ai-tests et deux dossiers voisins. Choisissez des noms de branche et des chemins encore inutilisés. S’ils existent déjà, changez de nom plutôt que de forcer un écrasement.

Les dépendances installées, les fichiers .env ignorés et les réglages locaux ne sont pas tous copiés. Suivez les instructions du projet, ne fournissez que les identifiants nécessaires et utilisez des ports différents pour les serveurs simultanés. Un worktree n’est pas une isolation de sécurité : les permissions peuvent permettre l’accès à d’autres dossiers.
---
Ouvrez un agent dans project-ai-ui et l’autre dans project-ai-tests. Donnez le chemin absolu et une mission précise : « modifier seulement le composant d’interface » et « ajouter des tests du comportement actuel sans changer le code de l’application ».

Attribuez les fichiers communs, notamment les listes de dépendances et les fichiers de verrouillage. Si les deux tâches touchent le même fichier, avancez dans l’ordre. Demandez les fichiers modifiés, les vérifications effectuées et le travail restant.
---
Lancez les trois commandes dans chaque dossier. Status liste les modifications et fichiers non suivis. Diff montre les modifications non indexées des fichiers suivis ; diff --cached montre celles déjà indexées. Les nouveaux fichiers non suivis n’apparaissent pas dans ces diff : ouvrez-les séparément.

Effectuez les vérifications du projet et créez un commit des modifications validées sur chaque branche. Revenez ensuite au projet initial pour examiner et intégrer une branche à la fois dans la branche cible. Worktree ne fusionne rien automatiquement. Résolvez les conflits et vérifiez le résultat combiné avant la branche suivante.
---
pika peut garder le Mac éveillé pendant le travail local, selon les réglages de session et les protections. Il ne répartit pas les tâches et ne gère ni fusion ni conflit. Le QR de pika 1.3 présente l’état du Mac et les commandes d’alimentation autorisées, pas la sortie de l’IA ni un pourcentage fiable d’avancement. Vérifiez les résultats de l’agent et les tests du projet.
---
Ce guide du créateur de no-sleep-pika suit les documents officiels de Git. Il concerne des agents génériques, sans supposer les fonctions ou permissions d’un produit. Respectez aussi les règles du projet et de gestion des secrets.
''')

add('de', 'Zwei KI-Agenten ändern dieselben Dateien? Erst die Ordner trennen.',
'Mit Git worktree bekommt jeder Agent einen eigenen Arbeitsordner. So verteilst du Aufgaben, prüfst Änderungen und führst Ergebnisse Schritt für Schritt zusammen.',
'Warum ein gemeinsamer Ordner problematisch ist|Einen geprüften Ausgangspunkt wählen|Zwei Arbeitsordner anlegen|Ordner und Aufgabe klar zuweisen|Prüfen und einzeln zusammenführen|Was pika dabei leistet|Quellen und Geltungsbereich',
'Ordner trennen|Aufgaben zuweisen|Änderungen prüfen|Einzeln integrieren', '''
Ein Agent ändert die Oberfläche, ein anderer schreibt Tests. Im selben Ordner lesen und bearbeiten beide dieselben Dateien. Zwei Branch-Namen erzeugen dort keine zwei unabhängigen Dateisätze. Ein Branch-Wechsel verändert auch die Dateien, mit denen der andere Agent arbeitet.

Git worktree fügt demselben Repository einen Arbeitsordner hinzu. Jeder Ordner kann seinen eigenen Branch und ausgecheckte Dateien haben; die Historie bleibt gemeinsam. Laufende Änderungen sind getrennt, spätere Konflikte beim Zusammenführen bleiben trotzdem möglich.
---
Führe den folgenden Befehl im bestehenden Git-Projekt aus. Mindestens ein Commit muss vorhanden sein; HEAD bezeichnet den gespeicherten Ausgangspunkt. Keine Ausgabe bedeutet keine gemeldeten Änderungen oder unversionierten Dateien. Ignorierte Dateien können dennoch vorhanden sein.

Prüfe aufgelistete Dateien zuerst. Committe nur gewünschte, geprüfte Änderungen oder wähle einen vorhandenen Commit. Nimm nicht blind den ganzen Ordner auf: Geheimnisse und fremde Änderungen gehören nicht hinein. Neue Ordner beginnen bei HEAD, nicht bei uncommitteten Änderungen.
---
Beide Befehle werden im ursprünglichen Projekt ausgeführt. Sie erstellen ai-ui und ai-tests sowie benachbarte Arbeitsordner. Branch-Namen und Zielpfade müssen unbenutzt sein. Wähle sonst andere Namen, statt etwas zu überschreiben.

Installierte Abhängigkeiten, ignorierte .env-Dateien und lokale Einstellungen werden nicht vollständig übernommen. Bereite sie nach Projektanleitung vor, gib nur nötige Zugangsdaten weiter und nutze unterschiedliche Ports für gleichzeitige Server. Worktrees sind keine Sicherheits-Sandbox: Werkzeuge können mit passenden Rechten andere Ordner erreichen.
---
Starte einen Agenten in project-ai-ui, den anderen in project-ai-tests. Nenne den absoluten Pfad und eine enge Aufgabe: etwa „nur die Oberflächenkomponente ändern“ und „Tests für bestehendes Verhalten ergänzen, keinen Anwendungscode ändern“.

Lege Zuständigkeiten für gemeinsame Dateien wie Abhängigkeitslisten und Lockfiles fest. Müssen beide dieselbe Datei ändern, arbeite nacheinander. Lass geänderte Dateien, ausgeführte Prüfungen und offene Punkte melden.
---
Führe die drei Befehle in jedem Ordner aus. Status zeigt Änderungen und unversionierte Dateien. Diff zeigt nicht vorgemerkte Änderungen an versionierten Dateien, diff --cached die vorgemerkten. Neue unversionierte Dateien fehlen in diesen Diffs; öffne sie zusätzlich.

Führe passende Projektprüfungen aus und committe die geprüften Änderungen im jeweiligen Branch. Kehre dann zum ursprünglichen Projekt zurück und prüfe und integriere einen Branch nach dem anderen in den Zielbranch. Worktree führt Ergebnisse nicht automatisch zusammen. Löse Konflikte und prüfe das Gesamtergebnis vor dem nächsten Branch.
---
pika kann den Mac während lokaler KI-Arbeit wach halten, abhängig von Sitzungseinstellungen und Schutzfunktionen. Es verteilt keine Aufgaben und löst weder Merges noch Konflikte. Der QR-Zugang von pika 1.3 zeigt Mac-Status und erlaubte Stromsteuerung, keine KI-Ausgabe oder verlässliche Fertigstellungsquote. Prüfe dafür die Agentenergebnisse und Projekttests.
---
Dieser Leitfaden vom Hersteller von no-sleep-pika folgt der offiziellen Git-Dokumentation. Er gilt für allgemeine KI-Agenten und setzt keine bestimmten Produktfunktionen oder Rechte voraus. Beachte zusätzlich die Projektregeln und den Umgang mit Geheimnissen.
''')

add('pt-BR', 'Dois agentes de IA editando os mesmos arquivos? Separe as pastas.',
'Com Git worktree, cada agente ganha sua própria pasta. Divida tarefas, revise alterações e integre os resultados sem misturar trabalho inacabado.',
'O risco de dividir a mesma pasta|Prepare um ponto de partida revisado|Crie duas pastas de trabalho|Defina pasta e responsabilidade|Revise e integre uma branch por vez|Onde o pika ajuda|Fontes e escopo',
'Separar pastas|Distribuir tarefas|Revisar alterações|Integrar por etapas', '''
Um agente ajusta a interface, outro escreve testes. Na mesma pasta, ambos leem e alteram os mesmos arquivos. Criar dois nomes de branch não cria duas cópias independentes ali. Trocar a branch também muda os arquivos usados pelo outro agente.

Git worktree adiciona outra pasta de trabalho ao mesmo repositório. Cada pasta pode ter sua branch e seus arquivos, compartilhando o histórico. Isso separa o trabalho em andamento, mas não elimina possíveis conflitos na integração.
---
Execute o comando abaixo no projeto Git existente. É necessário pelo menos um commit: HEAD indica esse ponto de partida. Saída vazia significa que não foram relatadas alterações ou arquivos não rastreados; arquivos ignorados ainda podem existir.

Se aparecer uma lista, revise-a e faça commit apenas das mudanças desejadas, ou escolha um commit existente. Não adicione a pasta inteira sem conferir: segredos e trabalho sem relação devem ficar de fora. As novas pastas partem de HEAD, não das edições sem commit.
---
Execute os dois comandos no projeto original. Eles criam ai-ui e ai-tests e pastas ao lado do projeto. Os nomes de branch e os caminhos precisam estar livres. Se já existirem, escolha outros, sem forçar substituições.

Dependências instaladas, arquivos .env ignorados e ajustes locais não são todos copiados. Prepare o necessário conforme o projeto, forneça apenas as credenciais exigidas e use portas diferentes para servidores simultâneos. Worktree não é uma barreira de segurança: ferramentas com permissão podem acessar outras pastas.
---
Abra um agente em project-ai-ui e outro em project-ai-tests. Informe o caminho absoluto e uma tarefa limitada: “alterar apenas o componente visual” e “adicionar testes do comportamento atual, sem mudar o código da aplicação”.

Defina quem cuida de arquivos compartilhados, como listas de dependências e arquivos de lock. Se ambos precisarem mudar o mesmo arquivo, trabalhe em sequência. Peça um resumo dos arquivos alterados, verificações realizadas e pendências.
---
Execute os três comandos em cada pasta. Status lista mudanças e arquivos não rastreados. Diff mostra alterações ainda não preparadas em arquivos rastreados; diff --cached mostra as preparadas. Arquivos novos não rastreados não aparecem nesses diffs: abra-os separadamente.

Execute as verificações do projeto e faça commit das mudanças revisadas na respectiva branch. Volte ao projeto original e revise e integre uma branch por vez na branch de destino. Worktree não combina resultados automaticamente. Resolva conflitos e verifique o resultado conjunto antes de integrar a próxima.
---
O pika pode manter o Mac acordado durante o trabalho local, conforme as configurações de sessão e as proteções. Ele não distribui tarefas, faz merges ou resolve conflitos. O QR do pika 1.3 mostra o estado do Mac e controles de energia autorizados, não a saída da IA ou uma porcentagem confiável de conclusão. Confira os resultados do agente e os testes do projeto.
---
Guia do criador do no-sleep-pika baseado na documentação oficial do Git. Trata de agentes genéricos, sem presumir recursos ou permissões de um produto. Siga também as regras do projeto e de proteção de segredos.
''')

add('ru', 'Два ИИ-агента меняют одни файлы? Сначала разделите папки.',
'Git worktree дает каждому агенту отдельную рабочую папку. Разделите задачи, проверьте изменения и объедините результаты по очереди.',
'Чем мешает общая папка|Подготовьте проверенную исходную версию|Создайте две рабочие папки|Назначьте папку и границы задачи|Проверьте и объединяйте по очереди|Чем поможет pika|Источники и рамки статьи',
'Разделить папки|Назначить задачи|Проверить изменения|Объединить по очереди', '''
Один агент меняет интерфейс, другой пишет тесты. В общей папке они читают и редактируют одни и те же файлы. Два названия веток не создают в ней два независимых набора файлов. Переключение ветки меняет и файлы, с которыми работает второй агент.

Git worktree добавляет рабочую папку к тому же репозиторию. У каждой папки могут быть своя ветка и файлы при общей истории. Текущая работа разделяется, но конфликты при будущем объединении все равно возможны.
---
Выполните команду ниже в существующем Git-проекте. Нужен хотя бы один коммит: HEAD указывает на исходную сохраненную версию. Пустой вывод означает, что изменений и неотслеживаемых файлов не обнаружено; игнорируемые файлы могут оставаться.

Если есть список, сначала проверьте его. Сохраните коммитом только нужные изменения либо выберите существующий коммит. Не добавляйте всю папку вслепую: там могут быть секреты и посторонняя работа. Новые папки начинают с HEAD, а не с незакоммиченных правок.
---
Запустите обе команды из исходного проекта. Они создадут ветки ai-ui и ai-tests и соседние рабочие папки. Имена веток и пути должны быть свободны. Иначе выберите другие имена, не перезаписывая существующее.

Установленные зависимости, игнорируемые .env и локальные настройки не копируются автоматически целиком. Подготовьте их по инструкции проекта, передавайте только нужные учетные данные и используйте разные порты для параллельных серверов. Worktree не является защитной песочницей: при наличии прав инструменты могут обращаться к другим папкам.
---
Запустите одного агента в project-ai-ui, другого — в project-ai-tests. Укажите абсолютный путь и узкую задачу: «менять только компонент интерфейса» и «добавить тесты текущего поведения, не менять код приложения».

Назначьте ответственных за общие файлы, например списки зависимостей и lock-файлы. Если обе задачи затрагивают один файл, выполняйте их последовательно. Просите перечислить измененные файлы, выполненные проверки и оставшуюся работу.
---
В каждой папке выполните три команды ниже. Status показывает изменения и неотслеживаемые файлы. Diff показывает неиндексированные изменения отслеживаемых файлов, а diff --cached — подготовленные к коммиту. Новые неотслеживаемые файлы в этих diff не видны: откройте их отдельно.

Выполните проверки проекта и закоммитьте проверенные изменения в соответствующей ветке. Затем вернитесь в исходный проект, чтобы проверять и объединять ветки с целевой по одной. Worktree не объединяет результаты автоматически. Разрешите конфликты и проверьте общий результат перед следующей веткой.
---
pika помогает поддерживать бодрствование Mac во время локальной работы с учетом настроек сеанса и защитных ограничений. Он не распределяет задачи, не объединяет ветки и не разрешает конфликты. QR-подключение pika 1.3 показывает состояние Mac и разрешенные действия с питанием, а не вывод ИИ или точный процент готовности. Завершение оценивайте по результату агента и проверкам проекта.
---
Статья автора no-sleep-pika опирается на официальные документы Git. Речь об обычных ИИ-агентах без предположений о возможностях и правах конкретного продукта. Соблюдайте также правила проекта и обращения с секретами.
''')

add('id', 'Dua agen AI mengedit berkas yang sama? Pisahkan foldernya dulu.',
'Git worktree memberi setiap agen folder kerja sendiri. Bagi tugas, tinjau perubahan, lalu gabungkan hasil tanpa mencampur pekerjaan yang belum selesai.',
'Masalah satu folder bersama|Siapkan titik awal yang sudah ditinjau|Buat dua folder kerja|Tentukan folder dan lingkup tugas|Tinjau dan gabungkan satu per satu|Peran pika|Sumber dan batas pembahasan',
'Pisahkan folder|Bagi tugas|Tinjau perubahan|Gabungkan bergiliran', '''
Satu agen mengubah antarmuka, yang lain menulis pengujian. Jika memakai folder yang sama, keduanya membaca dan mengubah berkas yang sama. Dua nama branch tidak membuat dua salinan berkas di folder itu. Berpindah branch juga mengubah berkas yang sedang dipakai agen lain.

Git worktree menambahkan folder kerja ke repositori yang sama. Setiap folder dapat memiliki branch dan berkasnya sendiri sambil berbagi riwayat. Ini memisahkan pekerjaan yang berlangsung, tetapi tidak menjamin hasil akhirnya bebas konflik.
---
Jalankan perintah berikut di proyek Git yang sudah ada. Harus ada setidaknya satu commit; HEAD menjadi titik awal yang tersimpan. Keluaran kosong berarti tidak ada perubahan atau berkas tak terlacak yang dilaporkan. Berkas yang diabaikan masih mungkin ada.

Jika muncul daftar, periksa dahulu. Commit hanya perubahan yang memang diperlukan atau pilih commit yang sudah ada. Jangan menambahkan seluruh folder tanpa memeriksa rahasia dan pekerjaan lain. Folder baru dimulai dari HEAD, bukan dari perubahan yang belum di-commit.
---
Jalankan kedua perintah dari proyek asli. Perintah ini membuat branch ai-ui dan ai-tests serta folder di sebelah proyek. Gunakan nama branch dan jalur yang belum dipakai; pilih nama lain jika sudah ada, bukan menimpa paksa.

Dependensi terpasang, .env yang diabaikan, dan pengaturan lokal tidak semuanya disalin otomatis. Siapkan sesuai petunjuk proyek, berikan hanya kredensial yang diperlukan, dan gunakan port berbeda untuk server bersamaan. Worktree bukan sandbox keamanan: alat yang memiliki izin tetap bisa mengakses folder lain.
---
Buka satu agen di project-ai-ui dan satu di project-ai-tests. Berikan jalur absolut dan tugas terbatas, misalnya “ubah hanya komponen antarmuka” dan “tambahkan pengujian perilaku saat ini tanpa mengubah kode aplikasi”.

Tentukan penanggung jawab berkas bersama, seperti daftar dependensi dan lockfile. Jika keduanya perlu mengedit berkas yang sama, kerjakan bergiliran. Minta laporan berkas yang diubah, pemeriksaan yang dilakukan, dan pekerjaan tersisa.
---
Jalankan tiga perintah berikut di setiap folder. Status menampilkan perubahan dan berkas tak terlacak. Diff menampilkan perubahan berkas terlacak yang belum di-stage; diff --cached menampilkan yang sudah di-stage. Berkas baru tak terlacak tidak muncul di diff ini: buka dan periksa terpisah.

Jalankan pemeriksaan proyek, lalu commit perubahan yang disetujui pada branch masing-masing. Kembali ke proyek asli untuk meninjau dan menggabungkan satu branch setiap kali ke branch tujuan. Worktree tidak menggabungkan hasil otomatis. Selesaikan konflik dan periksa hasil gabungan sebelum melanjutkan.
---
pika membantu Mac tetap terjaga selama pekerjaan lokal sesuai pengaturan sesi dan perlindungannya. pika tidak membagi tugas, menggabungkan branch, atau menyelesaikan konflik. QR pika 1.3 menunjukkan status Mac dan kontrol daya yang diizinkan, bukan keluaran AI atau persentase selesai yang andal. Nilai penyelesaian dari hasil agen dan pemeriksaan proyek.
---
Panduan pembuat no-sleep-pika ini berdasarkan dokumentasi resmi Git. Pembahasan memakai agen umum tanpa mengasumsikan fitur atau izin produk tertentu. Ikuti juga aturan kontribusi proyek dan penanganan rahasia.
''')

add('vi', 'Hai tác nhân AI cùng sửa một tệp? Hãy tách thư mục trước.',
'Git worktree tạo thư mục làm việc riêng cho từng tác nhân. Chia việc, kiểm tra thay đổi rồi lần lượt hợp nhất để tránh trộn công việc chưa xong.',
'Vì sao dùng chung thư mục dễ chồng chéo|Chuẩn bị điểm xuất phát đã kiểm tra|Tạo hai thư mục làm việc|Giao rõ thư mục và phạm vi|Kiểm tra rồi hợp nhất từng nhánh|pika giúp ở đâu|Nguồn và phạm vi bài viết',
'Tách thư mục|Giao nhiệm vụ|Kiểm tra thay đổi|Hợp nhất lần lượt', '''
Một tác nhân sửa giao diện, tác nhân kia viết kiểm thử. Nếu chung thư mục, cả hai vẫn đọc và sửa cùng các tệp. Tạo hai tên nhánh không tạo hai bộ tệp độc lập trong thư mục đó. Chuyển nhánh ở đây cũng đổi các tệp tác nhân kia đang dùng.

Git worktree thêm thư mục làm việc vào cùng kho mã. Mỗi thư mục có thể có nhánh và tệp riêng nhưng chia sẻ lịch sử. Cách này tách công việc đang làm, không bảo đảm hết xung đột khi hợp nhất sau đó.
---
Chạy lệnh dưới đây trong dự án Git hiện có. Cần ít nhất một commit; HEAD trỏ tới điểm xuất phát đã lưu vào Git. Không có đầu ra nghĩa là không báo thay đổi hoặc tệp chưa được theo dõi. Tệp bị bỏ qua vẫn có thể tồn tại.

Nếu có danh sách, kiểm tra trước. Chỉ commit thay đổi cần thiết đã xem xét hoặc chọn một commit có sẵn. Đừng thêm cả thư mục mà không kiểm tra thông tin bí mật và việc ngoài phạm vi. Thư mục mới bắt đầu từ HEAD, không mang theo chỉnh sửa chưa commit.
---
Chạy cả hai lệnh từ dự án gốc để tạo nhánh ai-ui, ai-tests và hai thư mục bên cạnh. Tên nhánh và đường dẫn phải chưa được sử dụng. Nếu đã có, chọn tên khác thay vì ghi đè cưỡng bức.

Các thư viện đã cài, tệp .env bị bỏ qua và cấu hình cục bộ không tự động được sao chép đầy đủ. Chuẩn bị theo hướng dẫn dự án, chỉ cấp thông tin xác thực cần thiết và dùng cổng khác nhau cho các máy chủ chạy cùng lúc. Worktree không phải vùng cách ly bảo mật: công cụ có quyền vẫn có thể truy cập thư mục khác.
---
Mở một tác nhân ở project-ai-ui, tác nhân kia ở project-ai-tests. Ghi rõ đường dẫn tuyệt đối và nhiệm vụ hẹp: “chỉ sửa thành phần giao diện” và “thêm kiểm thử cho hành vi hiện có, không sửa mã ứng dụng”.

Chỉ định người phụ trách các tệp chung như danh sách thư viện và tệp khóa phiên bản. Nếu cả hai phải sửa cùng tệp, làm lần lượt. Yêu cầu báo cáo tệp đã đổi, kiểm tra đã chạy và phần còn lại.
---
Chạy ba lệnh dưới đây ở từng thư mục. Status liệt kê thay đổi và tệp chưa theo dõi. Diff hiển thị sửa đổi chưa đưa vào vùng chuẩn bị commit của tệp đã theo dõi; diff --cached hiển thị phần đã chuẩn bị. Tệp mới chưa theo dõi không xuất hiện trong các diff này, cần mở riêng để xem.

Chạy kiểm tra phù hợp và commit thay đổi đã duyệt vào từng nhánh. Về dự án gốc, xem xét và hợp nhất từng nhánh vào nhánh đích. Worktree không tự động hợp nhất kết quả. Giải quyết xung đột và kiểm tra kết quả chung trước khi thêm nhánh tiếp theo.
---
pika giúp Mac duy trì trạng thái thức khi AI chạy cục bộ, tùy cài đặt phiên và cơ chế bảo vệ. Nó không giao việc, hợp nhất nhánh hay giải quyết xung đột. QR của pika 1.3 hiển thị trạng thái Mac và điều khiển nguồn được phép, không phải đầu ra AI hay tỷ lệ hoàn thành chính xác. Hãy đánh giá bằng kết quả tác nhân và kiểm tra dự án.
---
Bài viết của nhà phát triển no-sleep-pika dựa trên tài liệu Git chính thức, nói về tác nhân nói chung, không giả định tính năng hay quyền của sản phẩm cụ thể. Hãy tuân thủ thêm quy tắc đóng góp và bảo vệ bí mật của dự án.
''')

add('hi', 'दो AI एजेंट एक ही फ़ाइल बदल रहे हैं? पहले काम के फ़ोल्डर अलग करें।',
'Git worktree से हर AI एजेंट को अपना काम का फ़ोल्डर मिलता है। काम बाँटें, बदलाव जाँचें और नतीजे एक-एक करके जोड़ें।',
'एक फ़ोल्डर में काम क्यों टकराता है|पहले जाँचा हुआ शुरुआती कमिट चुनें|दो काम के फ़ोल्डर बनाएँ|फ़ोल्डर और काम की सीमा तय करें|जाँचकर एक-एक शाखा जोड़ें|pika की भूमिका|स्रोत और लेख की सीमा',
'फ़ोल्डर अलग करें|काम बाँटें|बदलाव जाँचें|एक-एक करके जोड़ें', '''
एक एजेंट इंटरफ़ेस बदलता है और दूसरा टेस्ट लिखता है। अगर दोनों एक फ़ोल्डर इस्तेमाल करें, तो वही फ़ाइलें पढ़ते और बदलते हैं। दो ब्रांच के नाम बनाने से उस फ़ोल्डर में फ़ाइलों की दो स्वतंत्र प्रतियाँ नहीं बनतीं। वहाँ ब्रांच बदलने पर दूसरे एजेंट की इस्तेमाल की जा रही फ़ाइलें भी बदल जाती हैं।

Git worktree उसी रिपॉज़िटरी से जुड़ा एक और काम का फ़ोल्डर बनाता है। हर फ़ोल्डर की अपनी ब्रांच और फ़ाइलें हो सकती हैं, जबकि इतिहास साझा रहता है। यह चल रहे काम को अलग करता है, लेकिन बाद में बदलाव जोड़ते समय टकराव रोकने की गारंटी नहीं देता।
---
मौजूदा Git प्रोजेक्ट में नीचे की कमांड चलाएँ। कम से कम एक कमिट होना चाहिए; HEAD उसी दर्ज शुरुआती स्थिति को दर्शाता है। खाली आउटपुट का अर्थ है कि बदलाव या अनट्रैक्ड फ़ाइलें रिपोर्ट नहीं हुईं। अनदेखी की गई फ़ाइलें फिर भी मौजूद हो सकती हैं।

सूची आए तो पहले जाँचें। केवल ज़रूरी और जाँचे हुए बदलाव कमिट करें या पहले से मौजूद कमिट चुनें। पूरा फ़ोल्डर बिना जाँचे न जोड़ें: उसमें गोपनीय जानकारी या असंबंधित काम हो सकता है। नए फ़ोल्डर HEAD से शुरू होते हैं, बिना कमिट वाले बदलावों से नहीं।
---
मूल प्रोजेक्ट से दोनों कमांड चलाएँ। ये ai-ui और ai-tests ब्रांच तथा प्रोजेक्ट के पास दो फ़ोल्डर बनाती हैं। ब्रांच के नाम और रास्ते पहले से इस्तेमाल में नहीं होने चाहिए। मौजूद हों तो नया नाम चुनें, जबरन ओवरराइट न करें।

इंस्टॉल की गई निर्भरताएँ, अनदेखी .env फ़ाइलें और स्थानीय सेटिंग अपने आप पूरी तरह कॉपी नहीं होतीं। प्रोजेक्ट के निर्देश मानें, केवल ज़रूरी क्रेडेंशियल दें और साथ चलने वाले सर्वर के लिए अलग पोर्ट रखें। Worktree सुरक्षा सैंडबॉक्स नहीं है: अनुमति वाले टूल दूसरे फ़ोल्डर भी पढ़ सकते हैं।
---
एक एजेंट project-ai-ui में और दूसरा project-ai-tests में शुरू करें। पूरा absolute path और सीमित काम दें: जैसे “सिर्फ़ इंटरफ़ेस घटक बदलें” और “मौजूदा व्यवहार के टेस्ट जोड़ें, ऐप कोड न बदलें।”

निर्भरता सूची और लॉक फ़ाइल जैसे साझा दस्तावेज़ों का ज़िम्मेदार तय करें। दोनों को एक फ़ाइल बदलनी हो तो क्रम से काम कराएँ। बदली फ़ाइलों, की गई जाँच और बचे काम की रिपोर्ट माँगें।
---
हर फ़ोल्डर में नीचे की तीन कमांड चलाएँ। Status बदलाव और अनट्रैक्ड फ़ाइलें दिखाता है। Diff ट्रैक की गई फ़ाइलों के स्टेज न किए बदलाव दिखाता है; diff --cached स्टेज किए बदलाव दिखाता है। नई अनट्रैक्ड फ़ाइलें इन diff में नहीं दिखतीं, उन्हें अलग खोलकर जाँचें।

प्रोजेक्ट की ज़रूरी जाँच चलाएँ और सही बदलाव संबंधित ब्रांच में कमिट करें। फिर मूल प्रोजेक्ट में लौटकर लक्ष्य ब्रांच पर एक-एक शाखा जाँचें और जोड़ें। Worktree अपने आप मर्ज नहीं करता। टकराव सुलझाएँ और संयुक्त परिणाम जाँचने के बाद अगली शाखा जोड़ें।
---
pika सेशन सेटिंग और सुरक्षा शर्तों के अनुसार स्थानीय AI के काम करते समय Mac को जागा रखने में मदद कर सकता है। यह काम बाँटता, ब्रांच मर्ज करता या टकराव सुलझाता नहीं है। pika 1.3 का QR कनेक्शन Mac की स्थिति और अनुमत पावर नियंत्रण दिखाता है, AI आउटपुट या भरोसेमंद पूर्णता प्रतिशत नहीं। काम पूरा हुआ या नहीं, एजेंट के नतीजों और प्रोजेक्ट की जाँच से तय करें।
---
no-sleep-pika के निर्माता का यह लेख Git के आधिकारिक दस्तावेज़ों पर आधारित है। इसमें सामान्य AI एजेंट हैं; किसी खास उत्पाद की सुविधा या अनुमति नहीं मानी गई है। प्रोजेक्ट के योगदान और गोपनीय जानकारी के नियम भी मानें।
''')

add('ar', 'وكيلان للذكاء الاصطناعي يعدّلان الملفات نفسها؟ افصل مجلدات العمل أولاً.',
'يمنح Git worktree كل وكيل مجلد عمل خاصاً. قسّم المهام وراجع التغييرات ثم ادمج النتائج بالتتابع دون خلط العمل الجاري.',
'لماذا يسبب المجلد المشترك تداخلاً؟|ابدأ من نسخة محفوظة ومراجعة|أنشئ مجلدَي عمل|حدّد المجلد ونطاق المهمة|راجع ثم ادمج فرعاً في كل مرة|دور pika|المصادر ونطاق المقال',
'فصل المجلدات|توزيع المهام|مراجعة التغييرات|الدمج بالتتابع', '''
يعدّل وكيل الواجهة ويكتب آخر الاختبارات. إذا استخدما المجلد نفسه فسيقرآن ويعدّلان الملفات نفسها. إنشاء اسمَي فرع لا ينشئ نسختين مستقلتين من الملفات داخل ذلك المجلد. وتبديل الفرع فيه يغيّر أيضاً الملفات التي يستخدمها الوكيل الآخر.

يضيف Git worktree مجلد عمل إلى المستودع نفسه. يمكن لكل مجلد أن يملك فرعه وملفاته مع مشاركة سجل التغييرات. يفصل ذلك العمل الجاري، لكنه لا يضمن غياب التعارضات عند دمج النتائج لاحقاً.
---
شغّل الأمر التالي في مشروع Git موجود. يلزم وجود commit واحد على الأقل؛ يشير HEAD إلى نقطة البداية المحفوظة. عدم ظهور مخرجات يعني عدم الإبلاغ عن تغييرات أو ملفات غير متتبعة. وقد تبقى ملفات يتجاهلها Git.

إذا ظهرت قائمة فراجعها أولاً. احفظ فقط التغييرات المطلوبة والمراجعة في commit، أو اختر commit موجوداً. لا تضف المجلد كله دون فحص كي لا تضم أسراراً أو عملاً غير مرتبط. تبدأ المجلدات الجديدة من HEAD، لا من التعديلات التي لم تُسجّل في commit.
---
شغّل الأمرين من المشروع الأصلي. سينشئان الفرعين ai-ui وai-tests ومجلدين بجوار المشروع. يجب أن تكون أسماء الفروع والمسارات غير مستخدمة. إن كانت موجودة فاختر أسماء أخرى بدلاً من فرض الاستبدال.

لا تُنسخ تلقائياً كل الاعتماديات المثبتة وملفات .env المتجاهلة والإعدادات المحلية. جهّزها وفق تعليمات المشروع، ووفّر بيانات الاعتماد الضرورية فقط، واستخدم منافذ مختلفة للخوادم المتزامنة. Worktree ليس عزلاً أمنياً: قد تصل الأدوات إلى مجلدات أخرى إذا سمحت صلاحياتها بذلك.
---
افتح وكيلاً في project-ai-ui والآخر في project-ai-tests. أعطِ كلاً منهما المسار المطلق ومهمة محدودة، مثل «عدّل مكوّن الواجهة فقط» و«أضف اختبارات للسلوك الحالي دون تغيير كود التطبيق».

عيّن مسؤولاً عن الملفات المشتركة مثل قوائم الاعتماديات وملفات القفل. إذا احتاج الطرفان إلى تعديل الملف نفسه فاعمل بالتتابع. اطلب تقريراً بالملفات المعدلة والفحوص المنفذة والعمل المتبقي.
---
نفّذ الأوامر الثلاثة التالية في كل مجلد. يعرض status التغييرات والملفات غير المتتبعة. يعرض diff تغييرات الملفات المتتبعة التي لم تُجهّز للـ commit، ويعرض diff --cached التغييرات المجهّزة. الملفات الجديدة غير المتتبعة لا تظهر في هذه المقارنات؛ افتحها وراجعها بشكل منفصل.

نفّذ فحوص المشروع وسجّل التغييرات المراجعة في فرع كل مجلد. ثم عد إلى المشروع الأصلي وراجع وادمج فرعاً واحداً في كل مرة في الفرع المستهدف. لا يدمج worktree النتائج تلقائياً. عالج التعارضات وافحص النتيجة المشتركة قبل إضافة الفرع التالي.
---
يساعد pika على إبقاء Mac مستيقظاً أثناء العمل المحلي بحسب إعدادات الجلسة وضوابط الحماية. لا يوزّع المهام ولا يدمج الفروع ولا يحل التعارضات. يعرض اتصال QR في pika 1.3 حالة Mac وتحكمات الطاقة المسموح بها، وليس مخرجات الذكاء الاصطناعي أو نسبة إنجاز موثوقة. قيّم الاكتمال من نتائج الوكيل وفحوص المشروع.
---
كتب هذا الدليل مطوّر no-sleep-pika استناداً إلى وثائق Git الرسمية. يتناول وكلاء عامّين دون افتراض ميزات أو صلاحيات لمنتج محدد. اتبع أيضاً قواعد المساهمة وحماية الأسرار الخاصة بمشروعك.
''')

add('th', 'AI สองตัวแก้ไฟล์เดียวกัน? แยกโฟลเดอร์ทำงานก่อน',
'ใช้ Git worktree ให้ AI แต่ละตัวมีโฟลเดอร์ของตัวเอง แบ่งงาน ตรวจการเปลี่ยนแปลง แล้วรวมผลทีละส่วนโดยไม่ปนงานที่ยังไม่เสร็จ',
'ทำไมโฟลเดอร์เดียวถึงทำให้งานชนกัน|เริ่มจากคอมมิตที่ตรวจแล้ว|สร้างโฟลเดอร์ทำงานสองชุด|ระบุโฟลเดอร์และขอบเขตงาน|ตรวจแล้วรวมทีละบรานช์|pika ช่วยตรงไหน|แหล่งข้อมูลและขอบเขต',
'แยกโฟลเดอร์|มอบหมายงาน|ตรวจการเปลี่ยนแปลง|รวมทีละส่วน', '''
AI ตัวหนึ่งแก้หน้าจอ อีกตัวเขียนการทดสอบ ถ้าใช้โฟลเดอร์เดียวกัน ทั้งคู่จะอ่านและแก้ไฟล์ชุดเดียวกัน การสร้างชื่อบรานช์สองชื่อไม่ได้สร้างไฟล์สองชุดในโฟลเดอร์นั้น เมื่อสลับบรานช์ ไฟล์ที่อีกตัวใช้อยู่ก็เปลี่ยนด้วย

Git worktree เพิ่มโฟลเดอร์ทำงานที่เชื่อมกับคลัง Git เดียวกัน แต่ละโฟลเดอร์มีบรานช์และไฟล์ของตนเองได้ โดยใช้ประวัติร่วมกัน ช่วยแยกงานระหว่างทำ แต่ไม่ได้รับประกันว่าจะไม่มีข้อขัดแย้งตอนรวมงาน
---
รันคำสั่งด้านล่างในโครงการ Git ที่มีอยู่ ต้องมีอย่างน้อยหนึ่งคอมมิต โดย HEAD ชี้ไปยังจุดเริ่มต้นที่บันทึกแล้ว ถ้าไม่มีผลลัพธ์ แสดงว่าไม่พบการเปลี่ยนแปลงหรือไฟล์ที่ยังไม่ได้ติดตาม แต่อาจมีไฟล์ที่ Git ละเว้นอยู่

ถ้ามีรายชื่อไฟล์ ให้ตรวจสอบก่อน คอมมิตเฉพาะการเปลี่ยนแปลงที่ต้องการและตรวจแล้ว หรือเลือกคอมมิตที่มีอยู่ อย่าเพิ่มทั้งโฟลเดอร์โดยไม่ดู เพราะอาจมีข้อมูลลับหรืองานอื่น โฟลเดอร์ใหม่เริ่มจาก HEAD ไม่ใช่การแก้ไขที่ยังไม่คอมมิต
---
รันทั้งสองคำสั่งจากโครงการเดิม เพื่อสร้างบรานช์ ai-ui และ ai-tests พร้อมโฟลเดอร์ข้างโครงการ ชื่อบรานช์และเส้นทางปลายทางต้องยังไม่มีผู้ใช้ ถ้ามีแล้วให้เลือกชื่ออื่น ไม่ต้องบังคับเขียนทับ

ไลบรารีที่ติดตั้ง ไฟล์ .env ที่ถูกละเว้น และการตั้งค่าเฉพาะเครื่องไม่ได้คัดลอกทั้งหมดโดยอัตโนมัติ เตรียมตามคู่มือโครงการ ให้เฉพาะข้อมูลยืนยันตัวตนที่จำเป็น และใช้พอร์ตต่างกันเมื่อเปิดเซิร์ฟเวอร์พร้อมกัน Worktree ไม่ใช่พื้นที่แยกด้านความปลอดภัย เครื่องมือที่มีสิทธิ์ยังเข้าถึงโฟลเดอร์อื่นได้
---
เปิด AI หนึ่งตัวใน project-ai-ui และอีกตัวใน project-ai-tests ระบุเส้นทางแบบเต็มกับงานที่ชัดเจน เช่น “แก้เฉพาะส่วนหน้าจอ” และ “เพิ่มการทดสอบพฤติกรรมเดิม ห้ามแก้โค้ดแอป”

กำหนดผู้ดูแลไฟล์ร่วม เช่น รายการไลบรารีและไฟล์ล็อก ถ้าต้องแก้ไฟล์เดียวกันให้ทำตามลำดับ ขอรายงานไฟล์ที่เปลี่ยน การตรวจที่ทำ และงานที่ยังเหลือ
---
รันสามคำสั่งด้านล่างในแต่ละโฟลเดอร์ Status แสดงการเปลี่ยนแปลงและไฟล์ที่ยังไม่ติดตาม Diff แสดงการแก้ไขไฟล์ที่ติดตามแล้วแต่ยังไม่เตรียมคอมมิต ส่วน diff --cached แสดงที่เตรียมไว้แล้ว ไฟล์ใหม่ที่ยังไม่ติดตามไม่อยู่ใน diff เหล่านี้ ต้องเปิดตรวจแยก

รันการตรวจที่โครงการต้องใช้ แล้วคอมมิตเฉพาะการเปลี่ยนแปลงที่ผ่านการตรวจในบรานช์นั้น กลับไปโครงการเดิมเพื่อตรวจและรวมทีละบรานช์เข้าเป้าหมาย Worktree ไม่รวมผลให้อัตโนมัติ แก้ข้อขัดแย้งและตรวจผลรวมก่อนเพิ่มบรานช์ถัดไป
---
pika ช่วยให้ Mac ตื่นระหว่าง AI ทำงานในเครื่องได้ตามการตั้งค่าเซสชันและระบบป้องกัน แต่ไม่ได้แบ่งงาน รวมบรานช์ หรือแก้ข้อขัดแย้ง QR ของ pika 1.3 แสดงสถานะ Mac และการควบคุมพลังงานที่อนุญาต ไม่ได้แสดงผลลัพธ์ AI หรือเปอร์เซ็นต์ความสำเร็จที่แน่นอน ให้ดูผลงานของ AI และผลตรวจโครงการเพื่อตัดสินว่างานเสร็จหรือยัง
---
บทความนี้เขียนโดยผู้พัฒนา no-sleep-pika ตามเอกสารทางการของ Git กล่าวถึง AI ทั่วไปโดยไม่สมมติความสามารถหรือสิทธิ์ของผลิตภัณฑ์เฉพาะ โปรดทำตามกฎการร่วมพัฒนาและการจัดการข้อมูลลับของโครงการด้วย
''')
