Source: https://no-sleep-pika.online/guide/ja/control-mac-from-phone-qr/
Language: ja

MAC GUIDE · 2026-11-23

# QRコードでMacを操作：スマホからセッション・タイマー・電源を管理

pika 1.3.0では、Macで承認したスマホからSessionやタイマーを変更し、システム終了を要求できます。接続から解除までを紹介します。

## 状態確認の次の操作へ

Macでビルドやダウンロードを続けながら別の部屋へ。pika 1.3.0なら、スマホで状態を見るだけでなく、Sessionの変更、タイマー設定、システム終了や再起動の要求ができます。

AIへの新しい指示、会話やターミナル出力の閲覧、進捗率の表示、リモートデスクトップは提供しません。

## Macのアプリを先に更新

Macのpikaを1.3.0以降に更新し、起動したままにします。ふたを閉じてスリープを防ぐには補助サービスが正常に接続されている必要があります。両方の端末にインターネット接続が必要です。

開発元を確認できない警告が出たら、公式サイトから入手したファイルか確認してください。一度開こうとしてから「システム設定 → プライバシーとセキュリティ」で対象の「このまま開く」を選び、macOSの確認・認証に従います。名称はOSで異なるため下のインストール案内も参照し、保護全体を無効にしないでください。

マルウェアや破損ファイルの警告は別の問題です。この許可手順を使わず、インストール案内で区別してください。

[pikaをダウンロード](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.3.0/pika-1.3.0.pkg) · [インストール案内](https://no-sleep-pika.online/install/)

## QRを読み取り、Macで承認

pika MCPを接続したAIチャットでpikaのQR作成を依頼し、スマホのカメラで読み取ります。QRは5分以内に1回だけ使用できます。最初は閲覧専用で、接続してもSessionは自動的にONになりません。

スマホで操作権限を要求し、Macの確認画面で許可します。外出前に両端末を見ながら済ませましょう。Macで承認しなければ操作できません。

スマホのボタンは現在韓国語です。「이 Mac에 연결」（接続）→「Mac에 제어 허용 요청」（操作を要求）→Macで承認、の順です。「예약·카운트다운 취소」で予約・カウントダウンを取り消します。MCPが初めてなら下の接続案内から始めてください。

[MCP接続ガイド →](https://no-sleep-pika.online/ja/#mcp)

## スマホで操作できること

Sessionはスリープ防止を開始・解除します。MonitorはSessionがONのときだけ変更でき、閉じたふた用の画面設定はふたを閉じてから適用されます。Monitorの値は要求した設定であり、実画面の確認結果ではありません。

電源条件ではAC接続時のみ維持、充電器を外したら解除、残量30・40・50%で解除を選べます。既存のバッテリー・熱保護は有効です。発熱表示はmacOSの状態区分で、摂氏温度ではありません。

## タイマーと60秒の取消時間

15・30・60・180・360分後にSession解除、スリープ、システム終了、再起動を予約できます。Session解除はスリープ防止を終えるだけで、アプリを強制終了しません。

今すぐ終了・再起動を選ぶと確認後にMacで60秒のカウントダウンが始まります。取り消すにはタイマー取消を使います。pikaがスリープ設定を復元してからmacOSへ要求します。未保存書類の確認で遅延・取消される場合があるため、送信済みを完了とみなさないでください。

## 接続とともに権限も終了

権限は承認された現在の接続だけに有効です。切断・権限解除で遠隔タイマーとカウントダウンも取り消され、再接続時は再承認が必要です。QR発行から最大24時間で、pika終了やMacのスリープをまたいで予約が動き続けるものではありません。

切断の検知には数十秒かかる場合があります。終了を止めるには切断せず、「예약·카운트다운 취소」を押して取消済みの状態を確認してください。遠隔タイマーにはブラウザから継続的な接続信号が必要です。他のアプリへ移りブラウザがバックグラウンドになると、接続や予約が取り消される場合があります。

QRは共有せず、外出前に重要でないSession操作とタイマー取消を試してください。切断後の表示は最後に受信した値の場合があり、Macの終了を証明しません。ネットワークやAI作業の完了も保証しません。

資料と対象範囲

no-sleep-pikaの制作者が2026年11月23日に自社アプリ1.3.0について執筆しました。インストール警告と設定名はAppleの公式案内も確認してください。

- [pika 1.3.0 · Release notes](https://github.com/Ezcho/no-sleep-pika/releases/tag/v1.3.0)

- [pika · Remote connection and permissions](https://github.com/Ezcho/no-sleep-pika/blob/v1.3.0/Remote/README.md)

- [Apple · Safely open apps on your Mac](https://support.apple.com/en-us/102445)

[AIエージェント2つが同じファイルを編集？まず作業フォルダを分けよう →](https://no-sleep-pika.online/guide/ja/parallel-ai-agents-git-worktree/)

pika開発者による、自社アプリを含む比較です。

[pikaをダウンロード](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.3.0/pika-1.3.0.pkg)[Macをスリープさせない方法：クラムシェル・caffeinate・pika →](https://no-sleep-pika.online/guide/ja/keep-mac-awake/)[Markdown](https://no-sleep-pika.online/guide/ja/control-mac-from-phone-qr/index.md)
