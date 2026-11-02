Source: https://no-sleep-pika.online/guide/ja/local-on-device-ai/
Language: ja

MAC GUIDE · 2026-10-22

# Claude CodeもローカルAI？Llama・Qwenで学ぶオンデバイスAI

Macにインストールした場所と、モデルが計算する場所は別です。ツール・モデル・実行場所を整理します。

左は機器内の計算、右はリモートサーバーへの接続を表す概念図です。

## インストール場所と計算場所

ターミナルのClaude Codeがファイルを編集しても、回答までMac内で計算しているとは限りません。手元のツールが内容をサーバーへ送り、モデルの回答を受け取る構成もあります。ツール、モデル、計算場所を分けて考えましょう。

## ローカルとオンデバイス

ローカルAIは自分で管理するコンピューターや近くのサーバーでモデルを動かす構成を指すことが多く、オンデバイスは使用中の機器そのものを強調します。自宅の別サーバーで動けば、Mac自体の計算ではありません。回答を作る計算は「推論」で、モデルを教える「学習」とは別です。最初から学習させる必要はありません。

## 三つの役割を分ける

Claude Codeはファイルやコマンドを扱う作業ツール。LlamaとQwenはサイズや用途が異なるモデルの系列です。Ollamaはモデルを実行・接続するソフトウェアで、Claude Codeをローカルまたはクラウドモデルにつなぐ方法を案内しています。すべてのモデルで同じ機能が使えるわけではありません。表は性能順位ではなく役割の比較です。

三つの役割を分ける
| 名前 | 役割 | 確認すること
| Claude Code | ファイルとコマンドの作業ツール | モデル提供元と接続先
| Llama · Qwen | モデル系列 | ローカルかサーバーか
| Ollama | モデルの実行・接続 | 選択モデルの実行場所

## ローカルで変わること

必要なソフトとモデルを用意すればローカル推論はオフラインでも可能な場合がありますが、Web検索や外部サービスは通信が必要です。

メモリーと速度はモデルの大きさ、圧縮方法、同時に扱う会話量で変わります。ローカルが必ず速いとは限りません。外部の推論料金を避けられても機器・電気・保守の費用は残ります。

入力を機器内で処理できても、同期、ログ、拡張機能が外部に送信する可能性は別に確認します。

## 確認する三つのポイント

一つ目は選択モデルと接続先。LlamaやQwenでもサーバー提供の場合があり、Ollamaもクラウドに対応します。

二つ目は通信が必要な機能。準備後、重要な作業がないときに接続を切って短い新規回答を試せます。ただし普段の送信がない証明にはなりません。

三つ目は設定と文書。OllamaにはクラウドモデルとWeb検索を無効にする設定がありますが、他アプリの通信までは止めません。機密でない短文で速度と品質を確認しましょう。

## pikaの役割

Macが処理する仕事はスリープで止まったり遅れたりします。独立したリモート処理とは区別が必要です。pikaはモデルを動かすアプリではなく、必要な作業中にMacを起こしておく役割です。補助サービスを確認しSessionをON、短時間の閉蓋テストを行い、電源と通気のよい机を使い、終了後はOFFにします。

[pikaをダウンロード](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.1.0/pika-1.1.0.pkg) · [インストール案内](https://no-sleep-pika.online/install/)

出典と範囲

2026年10月22日に公式資料を確認したpika制作者の入門記事です。全モデルの速度やMac対応を実測した比較ではなく、接続機能はバージョンで変わります。

- [Anthropic · Claude Code overview](https://code.claude.com/docs/en/overview)

- [Ollama · Claude Code integration](https://docs.ollama.com/integrations/claude-code)

- [Ollama · Local-only mode and data](https://docs.ollama.com/faq)

- [Qwen · Run locally with Ollama](https://qwen.readthedocs.io/en/latest/run_locally/ollama.html)

- [Meta · Llama models](https://github.com/meta-llama/llama-models)

pika開発者による、自社アプリを含む比較です。

[pikaをダウンロード](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.1.0/pika-1.1.0.pkg)[Macをスリープさせない方法：クラムシェル・caffeinate・pika →](https://no-sleep-pika.online/guide/ja/keep-mac-awake/)[Markdown](https://no-sleep-pika.online/guide/ja/local-on-device-ai/index.md)
