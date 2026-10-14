Source: https://no-sleep-pika.online/guide/ja/mac-locked-ai-running/
Language: ja

MAC GUIDE · 2026-10-05

# MacをロックしてもClaude Code・Codexは動き続ける？

画面ロックとスリープを区別し、ローカルAIの進行状況、接続、ふたを閉じる前の設定を確認します。

## ロックとスリープの違い

ロック画面が出ても作業終了とは限りません。Macが起きていてアプリと必要な接続が動いていれば、通常のバックグラウンド処理は続行できます。ただしGUI操作や認証はロック解除が必要な場合があります。画面消灯の後にシステムが眠ることもあります。

## ローカルかクラウドか

Codex CLIはローカルでファイルやコマンドを扱います。Codex Cloudへ委任した処理は別の環境で動きます。Claude Code Remote Controlもローカルセッションへの接続です。再接続できても、スリープ中に処理が進んだ証拠にはなりません。

[Codex CLI](https://learn.chatgpt.com/docs/codex/cli) · [Codex Cloud](https://learn.chatgpt.com/docs/cloud) · [Claude Code Remote Control](https://code.claude.com/docs/en/remote-control)

## 停止の原因を確認

最後のメッセージで承認待ち、質問、完了、エラーを確認します。次にアプリ、Wi-Fi、VPN、認証を確認してください。下の読み取り専用コマンドは電源要求と履歴を表示します。要求の存在やCPU使用率だけではAIの進行を証明できません。

```
pmset -g assertions
```

```
pmset -g log | tail -n 60
```

## 3分間の確認

ふたを開けたまま下のループを実行し、ターミナルを閉じずに約3分ロックします。解除後に時刻の間隔を調べ、Ctrl+Cで終了します。長い空白は電源履歴と比較してください。これは単純なローカル処理の確認です。AIのログも確認し、ふたを閉じた状態は別途試します。

```
while true; do date "+%Y-%m-%d %H:%M:%S"; sleep 10; done
```

## pikaの設定

pikaと補助サービスを準備し、Session ON、画面維持が不要ならMonitor OFFにしてふたを閉じます。画面ポリシーはふたを閉じた後に適用されます。Session OFFはスリープ防止を解除し、直ちに画面を消す操作ではありません。電源と通風を確保し、閉じたバッグ内では使わないでください。保護機能や接続障害で停止する場合があります。

[pikaをダウンロード](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.0.13/pika-1.0.13.pkg) · [インストール案内](https://no-sleep-pika.online/install/)

## よくある質問

Monitor OFFはAIの停止ではありません。tmuxはシステムのスリープを防ぎません。caffeinateもネットワークや承認待ちを解決しません。pika MCPの状態はpikaの状態であり、すべてのAI作業の進行状況ではありません。

出典と範囲

2026年10月5日に公式資料とpikaの実装を確認。pika制作者による案内で、全機種の連続動作を保証するものではありません。

- [Apple · Sleep and wake settings](https://support.apple.com/guide/mac-help/set-sleep-and-wake-settings-mchle41a6ccd/mac)

- [OpenAI · Codex CLI](https://learn.chatgpt.com/docs/codex/cli)

- [OpenAI · Codex Cloud](https://learn.chatgpt.com/docs/cloud)

- [Anthropic · Claude Code Remote Control](https://code.claude.com/docs/en/remote-control)

[AIに夜勤を頼むと、電気代は誰が払う？ →](https://no-sleep-pika.online/guide/ja/ai-overnight-electricity-cost/)

[MacBookのダウンロードが止まる原因：画面オフ・スリープ・ふたの違い →](https://no-sleep-pika.online/guide/ja/macbook-downloads-stop/)

pika開発者による、自社アプリを含む比較です。

[pikaをダウンロード](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.0.13/pika-1.0.13.pkg)[Macをスリープさせない方法：クラムシェル・caffeinate・pika →](https://no-sleep-pika.online/guide/ja/keep-mac-awake/)[Markdown](https://no-sleep-pika.online/guide/ja/mac-locked-ai-running/index.md)
