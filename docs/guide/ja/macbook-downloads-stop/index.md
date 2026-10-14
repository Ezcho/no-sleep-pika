Source: https://no-sleep-pika.online/guide/ja/macbook-downloads-stop/
Language: ja

MAC GUIDE · 2026-10-15

# MacBookのダウンロードが止まる原因：画面オフ・スリープ・ふたの違い

通信と電源を切り分け、caffeinateとpikaの使い方を確認します。

## 停止した時点を確認

まずダウンロードアプリの一時停止、通信エラー、容量不足、ログイン要求を確認します。使用中にも止まるならWi-Fi、VPN、サーバー、空き容量を先に調べます。期限切れリンクはスリープ防止では直りません。

## 画面オフとスリープ

画面が消えてもMacが起きていれば転送できる場合があります。ロック後に自動スリープへ移ることもあります。対応機種では電源接続時の自動スリープ防止設定を確認します。パスワード保護は維持してください。

## 開いたままcaffeinateを使う

下のコマンドは1時間、アイドル時のシステムスリープ防止を要求します。ターミナルを開いたまま通常のアプリでダウンロードし、早く終えるならCtrl+C。-tは秒、-iはシステム、-dは画面に関する指定です。通信復旧やすべてのスリープ防止を保証しません。

```
caffeinate -i -t 3600
```

```
man caffeinate
```

## ふたを閉じる条件

外部画面を使う場合は電源、外部キーボード・マウス、対応ディスプレイ構成を確認します。充電器だけでは十分とはいえません。外部画面なしで閉じる場合は別に短い転送を試し、受信量を比較してください。

## pikaでダウンロードを維持

pikaと補助サービスを準備し、転送開始後にSession ON、画面が不要ならMonitor OFFにして閉じます。画面ポリシーは閉じた後に適用されます。完了後はSession OFF。通風のよい机と電源を使い、閉じたバッグ内で動かさないでください。保護機能やサービス障害で停止する場合があります。

[pikaをダウンロード](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.0.13/pika-1.0.13.pkg) · [インストール案内](https://no-sleep-pika.online/install/)

## 完了の確認

アプリの完了表示、保存容量、提供されていればチェックサムを確認します。再開はアプリの対応機能を使います。pikaは通信復旧や完了検出を代行しません。画面を消すだけで高速になるわけではありません。

参考資料

2026年10月11日、Apple資料、caffeinate(8)、pika実装を確認。pika制作者による案内です。

- [Apple · Sleep and wake settings](https://support.apple.com/guide/mac-help/set-sleep-and-wake-settings-mchle41a6ccd/mac)

- [Apple · External displays](https://support.apple.com/en-us/102501)

- `man caffeinate` · macOS System Manager’s Manual

[AIに夜勤を頼むと、電気代は誰が払う？ →](https://no-sleep-pika.online/guide/ja/ai-overnight-electricity-cost/)

pika開発者による、自社アプリを含む比較です。

[pikaをダウンロード](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.0.13/pika-1.0.13.pkg)[Macをスリープさせない方法：クラムシェル・caffeinate・pika →](https://no-sleep-pika.online/guide/ja/keep-mac-awake/)[Markdown](https://no-sleep-pika.online/guide/ja/macbook-downloads-stop/index.md)
