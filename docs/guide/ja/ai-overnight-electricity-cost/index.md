Source: https://no-sleep-pika.online/guide/ja/ai-overnight-electricity-cost/
Language: ja

MAC GUIDE · 2026-10-15

# AIに夜勤を頼むと、電気代は誰が払う？

Macを一晩動かす費用を仮の数値で計算し、AIの利用料と家庭の電気代を分けて考えます。

## 費用は二つに分かれる

クラウドAIのモデル計算は主に提供元のサーバーで行われますが、Mac上のビルドやテストにも電力が必要です。ローカルモデルなら、その計算もMacが担当します。家庭の電気代と購読・API料金は別の費用です。コンセントの測定だけではデータセンターの電力まで分かりません。

## 8時間の計算例

平均W × 時間 ÷ 1,000でkWhを求め、単価を掛けます。1日8時間、30日、仮に0.20米ドル/kWhとすると、10Wは1日0.08kWh・0.016ドル、30日で2.4kWh・0.48ドル。30Wは0.24kWh・0.048ドル、30日で7.2kWh・1.44ドル。60Wは0.48kWh・0.096ドル、30日で14.4kWh・2.88ドルです。

これはMacの実測値でも日本の料金表でもありません。税・契約・段階料金は含めていません。スリープ時との差額を知るには、同じ時間のスリープ時消費量を測って差し引きます。

## 充電器のW数とは違う

70Wの充電器でも常時70Wを使うわけではありません。出力能力と消費電力は別です。充電状態、画面、ビルド処理で負荷は変わり、画面を消した場合の削減量も一律ではありません。

## 自分の作業を測る

積算kWhを測れるコンセント型電力計を説明書どおりに使います。2時間で0.06kWhなら平均30W。同じ負荷なら8時間で0.24kWhですが、できれば作業全体を測りましょう。バッテリー残量を記録し、別電源の画面やドックは測定対象外であることも確認します。

## pikaは節電アプリ？

pikaはスリープによる作業中断を防ぐためのアプリで、電力計でもAI料金の節約機能でもありません。Macを起こし続ければ消費が増える場合があります。補助サービスを確認し、SessionをON、画面維持が不要ならMonitorをOFFにして短時間の閉蓋テストを行います。終了後はSessionをOFFに。承認待ちや通信エラーは別に対応が必要です。

[pikaをダウンロード](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.0.13/pika-1.0.13.pkg) · [インストール案内](https://no-sleep-pika.online/install/)

## 離席前に決めること

完了条件と停止方法を決め、サービスが対応していれば利用上限や通知を設定します。購読料を追加費用として二重計上しないようにしましょう。電源をつなぎ、通気のよい硬い机で使い、かばんや寝具の中で動かさないでください。

前提と出典

pika制作者による記事です。計算式はVirginia Cooperative Extension、設置環境はAppleを参照。W数とドル単価は説明用の仮定です。

- [Virginia Cooperative Extension · Estimating appliance energy use](https://ext.vt.edu/content/pubs_ext_vt_edu/en/2901/2901-9014/2901-9014.html)

- [Apple · Mac operating temperatures](https://support.apple.com/en-us/102336)

pika開発者による、自社アプリを含む比較です。

[pikaをダウンロード](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.0.13/pika-1.0.13.pkg)[Macをスリープさせない方法：クラムシェル・caffeinate・pika →](https://no-sleep-pika.online/guide/ja/keep-mac-awake/)[Markdown](https://no-sleep-pika.online/guide/ja/ai-overnight-electricity-cost/index.md)
