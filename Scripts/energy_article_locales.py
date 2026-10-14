"""Editorial electricity estimates; all wattages and tariffs are hypothetical."""
COPY = {}
def add(locale, title, intro, headings, body):
    COPY[locale] = dict(title=title, intro=intro, headings=headings.split('|'), paragraphs=[s.strip().split('\n\n') for s in body.strip().split('\n---\n')])

add('ko', 'AI에게 야근시키면 전기요금은 누가 낼까?',
'밤새 켜 둔 맥북의 전기요금은 얼마일까요? 8시간 작업을 가정해 계산하고, 클라우드 AI 사용료와 내 Mac의 전력 소비를 구분해 봅니다.',
'AI의 야근 비용은 두 곳에서 나온다|8시간 켜 두면 얼마일까?|충전기에 적힌 W로 계산하면 안 되는 이유|내 작업의 전력량을 재는 방법|pika는 전기요금 절약 앱일까?|밤새 맡기기 전에 정할 세 가지|계산 기준과 참고 자료',
'''“이 작업 끝내 놔.” AI에게 부탁하고 노트북을 덮는 순간, 작은 궁금증이 생깁니다. 내가 자는 동안 일하는 이 동료는 전기를 얼마나 쓸까요?

내 Mac이 쓴 전기는 내 전기요금에 반영됩니다. 클라우드 AI 이용료는 별도입니다. 계산이 어디서 이루어지는지부터 나눠 볼까요? 클라우드 AI에 요청하면 모델의 주요 계산은 서비스 제공자의 서버에서 수행됩니다. 그래도 내 Mac에서 파일을 읽고, 코드를 실행하고, 테스트를 돌린다면 그 작업에는 내 전기가 듭니다. 반대로 모델 자체를 Mac에서 실행하는 로컬 AI는 모델 계산도 내 컴퓨터가 맡습니다.

따라서 집의 전기요금과 AI 서비스 이용료는 별개의 비용입니다. 구독이나 API 사용료만 보고 전체 비용을 알 수 없고, 콘센트에서 잰 전력량만으로 데이터센터까지 포함한 AI의 총에너지를 알 수도 없습니다.
---
계산은 간단합니다. 평균 소비전력(W)에 시간(h)을 곱하고 1,000으로 나누면 전력량(kWh)이 됩니다. 여기에 kWh당 단가를 곱하면 해당 사용량의 비용을 추정할 수 있습니다.

아래는 하루 8시간, 30일을 켜 둔 가상 비교입니다. 평균 소비전력은 10·30·60W, 단가는 1kWh당 200원으로 가정했습니다. 특정 맥북의 측정값이나 한국의 실제 요금표가 아닙니다. 낮은 값이 클라우드, 높은 값이 로컬 AI를 뜻하지도 않습니다.

평균 10W라면 하루 0.08kWh, 16원입니다. 30일이면 2.4kWh, 480원입니다.

평균 30W라면 하루 0.24kWh, 48원입니다. 30일이면 7.2kWh, 1,440원입니다.

평균 60W라면 하루 0.48kWh, 96원입니다. 30일이면 14.4kWh, 2,880원입니다.

실제 청구액에는 지역·계약·누진 구간·세금 등이 영향을 줍니다. 이 숫자는 원래 잠들어 있었을 때와 비교한 추가 비용도 아닙니다. 추가 비용을 알고 싶다면 같은 시간 동안 잠자기 상태의 전력량도 재서 빼야 합니다.
---
충전기에 70W라고 적혀 있어도 Mac이 밤새 70W를 일정하게 소비한다는 뜻은 아닙니다. 충전기의 출력 능력과 실제로 사용하는 전력은 다릅니다.

배터리를 충전하는 중인지, 외장 화면을 연결했는지, 빌드와 테스트가 얼마나 무거운지에 따라 값이 달라집니다. AI가 응답을 기다리는 시간과 로컬 코드를 실행하는 시간도 같은 부하라고 볼 수 없습니다.

화면을 끄면 디스플레이에 쓰는 전력을 줄일 수 있지만, 절감량을 모든 Mac에 같은 숫자로 적용할 수는 없습니다. Mac 기종만 보고 추정하기보다 실제 작업의 전력량을 재는 편이 유용합니다.
---
누적 전력량(kWh)을 표시하는 콘센트형 전력계가 있다면, 설명서에 따라 충전기와 콘센트 사이에 연결하세요. 배터리 잔량과 주변기기 조건을 기록한 뒤 실제 작업을 일정 시간 실행하고 전력량을 읽습니다.

예를 들어 2시간에 0.06kWh를 썼다면 그 구간의 평균은 30W입니다. 같은 부하가 8시간 이어진다고 가정할 때 0.24kWh로 추정할 수 있습니다. 잠깐 측정한 작업이 밤새 반복되지 않는다면 이 환산은 맞지 않을 수 있습니다.

가능하면 작업 전체를 측정하세요. 외장 모니터와 독을 별도 콘센트에 꽂았다면 그 전력은 Mac 충전기 측정에 포함되지 않습니다. 비교할 때는 시작·종료 배터리 잔량도 비슷하게 맞춰 충전량 차이를 줄이는 편이 좋습니다.
---
pika는 Mac이 잠들어 중단될 수 있는 작업을 유지하기 위한 앱입니다. 전력량을 측정하거나 AI 사용료를 줄이는 앱은 아닙니다. 원래 잠들었을 Mac을 계속 실행시키므로, 사용 방식에 따라 전력 사용이 늘 수 있습니다.

덮개를 닫고 실행할 작업이 있다면 보조 서비스 상태를 확인하고 Session을 ON으로 준비하세요. 화면 유지가 필요 없다면 Monitor는 OFF로 두고, 짧게 덮었다 열어 실제 작업이 진행되는지 확인합니다. 끝난 뒤에는 Session을 OFF로 돌리세요.

Mac이 깨어 있어도 AI가 승인 요청 앞에서 기다리거나 네트워크 오류로 멈출 수 있습니다. pika가 그 결정을 대신하거나 작업 완료를 자동으로 판정해 주지는 않습니다.
---
첫째, 끝났다는 기준을 정하세요. “계속 개선해”보다 “이 테스트를 통과하면 결과를 저장하고 종료해”가 작업 범위를 판단하기 쉽습니다. 다만 지시만으로 자동 종료가 보장되지는 않으므로 사용하는 도구의 동작을 확인해야 합니다.

둘째, 사용 중인 서비스에서 제공한다면 사용량 한도와 알림을 설정하세요. 전기요금과 AI 사용료 중 무엇이 더 큰지는 실제 사용 내역을 봐야 합니다. 구독료를 별도 추가 비용으로 중복 계산하지 않는 것도 중요합니다.

셋째, 전원을 연결하고 통풍되는 단단한 책상 위에 두세요. 가방이나 이불 안에 넣고 실행하지 마세요. 밤새 켜 두는 습관보다, 할 일이 있는 시간만 유지하고 결과를 확인하는 습관이 더 유용합니다.
---
이 글은 pika 제작자가 작성했습니다. 전력량 계산식은 Virginia Cooperative Extension의 안내를 참고했고, 설치 환경은 Apple의 온도 관리 안내를 참고했습니다. 표기한 소비전력과 200원/kWh는 계산을 설명하기 위한 가정입니다. 기기 실측, 특정 국가의 요금 견적 또는 AI 서비스별 비용 비교가 아닙니다.
''')

add('en', 'Who pays the electricity bill when AI works overnight?',
'Estimate an eight-hour Mac session, separate your electricity bill from AI service fees, and measure your own workload instead of guessing from charger wattage.',
'Two places incur costs|What could eight hours cost?|Charger wattage is not consumption|Measure your actual workload|Does pika save electricity?|Three decisions before leaving|Assumptions and sources',
'''You leave an AI task running and go to bed. Who supplies the energy for that overnight shift?

For cloud AI, the provider’s servers perform the main model computation. Your Mac still uses power for local file operations, builds and tests. With a model running locally, the Mac also performs the model computation. These are different workloads, not fixed low-power and high-power categories.

Your home electricity bill and the service subscription or API bill are separate. A meter at your outlet does not capture the data center’s energy use.
---
Energy in kWh equals average watts multiplied by hours, divided by 1,000. Multiply that energy by your applicable price per kWh to estimate its cost.

Consider eight hours per day for 30 days at hypothetical averages of 10, 30 and 60W. These are hypothetical inputs, not MacBook measurements or a local tariff quote. Assume USD 0.20/kWh.

At 10W: 0.08kWh over eight hours, costing 1.6 US cents. Over 30 nights: 2.4kWh, costing USD 0.48.

At 30W: 0.24kWh over eight hours, costing 4.8 US cents. Over 30 nights: 7.2kWh, costing USD 1.44.

At 60W: 0.48kWh over eight hours, costing 9.6 US cents. Over 30 nights: 14.4kWh, costing USD 2.88.

Taxes, tiers and contracts affect actual bills. The figures above are total session estimates, not extra cost relative to sleeping: measure and subtract the sleep baseline for that comparison.
---
A 70W adapter does not mean a Mac continuously consumes 70W. Its output capacity is different from actual draw. Charging, displays and local builds change consumption; waiting for a response is not the same load as running code.

Turning off a display can reduce display energy, but there is no universal saving for every Mac and workload.
---
If you have a plug-in meter that records cumulative kWh, follow its instructions and measure the charger during a representative task. Record battery levels and peripherals. A reading of 0.06kWh over two hours corresponds to an average of 30W.

Extrapolating that to eight hours gives 0.24kWh only if the average load stays similar. Prefer measuring the whole task. Separately powered displays and docks are outside the charger measurement; match starting and ending battery levels when comparing runs.
---
pika maintains work that system sleep could interrupt. It does not measure electricity or reduce AI service fees. Keeping a Mac awake can consume more energy than allowing it to sleep.

For closed-lid work, check that the helper service is running, then turn Session ON. Leave Monitor OFF if you do not need to keep the display on. Briefly close and reopen the lid to check that your task keeps running. Turn Session OFF after finishing. An awake Mac cannot resolve an AI approval prompt or a network failure by itself; pika does not automatically decide when your task is complete.
---
First, define a result and stopping condition, then verify how the tool actually stops.

Second, set usage limits or alerts where the service supports them. Compare real service charges and electricity usage; do not count an existing subscription twice as an additional expense.

Third, connect your Mac to power and use a firm, ventilated desk. Do not run the Mac inside a bag or under bedding. Keep it awake for useful work and check the result afterward.
---
Written by pika’s maker. The energy formula follows Virginia Cooperative Extension; placement guidance follows Apple. Wattages and USD 0.20/kWh are illustrative assumptions, not device benchmarks, local tariffs or service pricing comparisons.
''')

add('ja','AIに夜勤を頼むと、電気代は誰が払う？','Macを一晩動かす費用を仮の数値で計算し、AIの利用料と家庭の電気代を分けて考えます。','費用は二つに分かれる|8時間の計算例|充電器のW数とは違う|自分の作業を測る|pikaは節電アプリ？|離席前に決めること|前提と出典','''クラウドAIのモデル計算は主に提供元のサーバーで行われますが、Mac上のビルドやテストにも電力が必要です。ローカルモデルなら、その計算もMacが担当します。家庭の電気代と購読・API料金は別の費用です。コンセントの測定だけではデータセンターの電力まで分かりません。
---
平均W × 時間 ÷ 1,000でkWhを求め、単価を掛けます。1日8時間、30日、仮に0.20米ドル/kWhとすると、10Wは1日0.08kWh・0.016ドル、30日で2.4kWh・0.48ドル。30Wは0.24kWh・0.048ドル、30日で7.2kWh・1.44ドル。60Wは0.48kWh・0.096ドル、30日で14.4kWh・2.88ドルです。

これはMacの実測値でも日本の料金表でもありません。税・契約・段階料金は含めていません。スリープ時との差額を知るには、同じ時間のスリープ時消費量を測って差し引きます。
---
70Wの充電器でも常時70Wを使うわけではありません。出力能力と消費電力は別です。充電状態、画面、ビルド処理で負荷は変わり、画面を消した場合の削減量も一律ではありません。
---
積算kWhを測れるコンセント型電力計を説明書どおりに使います。2時間で0.06kWhなら平均30W。同じ負荷なら8時間で0.24kWhですが、できれば作業全体を測りましょう。バッテリー残量を記録し、別電源の画面やドックは測定対象外であることも確認します。
---
pikaはスリープによる作業中断を防ぐためのアプリで、電力計でもAI料金の節約機能でもありません。Macを起こし続ければ消費が増える場合があります。補助サービスを確認し、SessionをON、画面維持が不要ならMonitorをOFFにして短時間の閉蓋テストを行います。終了後はSessionをOFFに。承認待ちや通信エラーは別に対応が必要です。
---
完了条件と停止方法を決め、サービスが対応していれば利用上限や通知を設定します。購読料を追加費用として二重計上しないようにしましょう。電源をつなぎ、通気のよい硬い机で使い、かばんや寝具の中で動かさないでください。
---
pika制作者による記事です。計算式はVirginia Cooperative Extension、設置環境はAppleを参照。W数とドル単価は説明用の仮定です。''')
add('zh-CN','让 AI 加班一整晚，电费谁来付？','用假设数据估算 Mac 运行八小时的费用，并区分家庭电费与 AI 服务费。','两种不同的账单|八小时要花多少？|充电器功率不是实际耗电|测量自己的任务|pika 能省电吗？|离开前做三个决定|假设与来源','''云端 AI 的模型计算主要由服务商的服务器完成，但 Mac 上的构建、测试和文件操作仍会耗电。本地模型则也在 Mac 上计算。家庭电费与订阅或 API 费用是两笔账；插座测量不包含数据中心的耗电。
---
平均功率 W × 小时 ÷ 1,000 = kWh，再乘以电价。假设每天八小时、连续三十天、电价为0.20美元/kWh：10W每天0.08kWh、0.016美元，三十天2.4kWh、0.48美元；30W每天0.24kWh、0.048美元，三十天7.2kWh、1.44美元；60W每天0.48kWh、0.096美元，三十天14.4kWh、2.88美元。

这些不是 MacBook 实测数据或当地电价。实际账单受税费、合同与阶梯电价影响。要算相对睡眠状态增加的费用，还需测量并减去同时间的睡眠耗电。
---
70W充电器不代表电脑一直消耗70W。输出能力与实际耗电不同；充电、显示器和本地任务都会改变负载。关屏节省多少也没有统一数值。
---
按说明使用可记录累计kWh的插座电量计。两小时0.06kWh对应平均30W；只有负载相近时，才能推算八小时0.24kWh。尽量测完整任务，记录电池电量。独立供电的屏幕和扩展坞不在充电器读数内。
---
pika用于维持可能因系统睡眠中断的任务，不是电量计或AI费用优化器。持续唤醒可能增加耗电。确认辅助服务，打开Session，不需维持显示时关闭Monitor，短暂合盖验证任务进度。完成后关闭Session；审批等待、网络错误和任务完成判断仍需另行处理。
---
先定义完成条件和停止方法，再按服务支持情况设置用量上限或提醒。不要把已有订阅重复算作新增费用。接通电源，放在通风的硬质桌面上，不要在包内或被褥里运行。
---
由pika制作者撰写。公式参考Virginia Cooperative Extension，摆放建议参考Apple。功率与美元单价均为示例假设。''')
add('zh-TW','讓 AI 加班一整晚，電費誰來付？','用假設數據估算 Mac 運作八小時的費用，區分家中電費與 AI 服務費。','兩種不同的帳單|八小時要花多少？|充電器瓦數不是實際耗電|量測自己的工作|pika 能省電嗎？|離開前的三個決定|假設與來源','''雲端AI的模型運算主要由服務商的伺服器完成，但Mac上的建置、測試和檔案操作仍會耗電。本機模型則也在Mac運算。家中電費與訂閱或API費用是兩筆帳；插座量測不包含資料中心的耗電。
---
平均功率W × 小時 ÷ 1,000 = kWh，再乘以電價。假設每天八小時、三十天、0.20美元/kWh：10W每天0.08kWh、0.016美元，三十天2.4kWh、0.48美元；30W每天0.24kWh、0.048美元，三十天7.2kWh、1.44美元；60W每天0.48kWh、0.096美元，三十天14.4kWh、2.88美元。

這不是MacBook實測值或臺灣電價。實際帳單受稅費、契約與級距影響。要比較睡眠時的額外費用，還須量測並減去同時間的睡眠耗電。
---
70W充電器不表示電腦持續消耗70W。輸出能力與實際耗電不同，充電、螢幕和本機工作都會改變負載。關閉螢幕的節省量也不固定。
---
依說明使用可記錄累計kWh的插座電力計。兩小時0.06kWh相當於平均30W；只有負載相近才可推算八小時0.24kWh。最好量測完整工作並記錄電池電量。獨立供電的螢幕與擴充基座不在充電器讀數內。
---
pika維持可能被系統睡眠中斷的工作，不是電力計，也不會降低AI服務費。持續喚醒可能增加耗電。確認輔助服務，開啟Session，不需維持顯示時關閉Monitor，短暫闔蓋測試進度。完成後關閉Session；核准等待、網路錯誤與工作完成判斷仍需另外處理。
---
定義完成條件與停止方式，並在服務支援時設定用量上限或通知。別將既有訂閱重複計為新增費用。接上電源，放在通風的硬質桌面，不要在包包或寢具內運作。
---
pika製作者撰寫。公式參考Virginia Cooperative Extension，放置建議參考Apple。功率與美元單價皆為假設。''')
add('es','Si la IA trabaja de noche, ¿quién paga la electricidad?','Calculamos ocho horas de trabajo con supuestos explícitos y separamos la factura eléctrica del coste del servicio de IA.','Dos costes distintos|Un ejemplo de ocho horas|El cargador no indica el consumo real|Mide tu trabajo|¿pika ahorra energía?|Antes de ausentarte|Supuestos y fuentes','''En la IA en la nube, el proveedor realiza el cálculo principal del modelo, pero las compilaciones y pruebas locales siguen consumiendo energía en tu Mac. Un modelo local también se ejecuta en el Mac. La electricidad doméstica y la suscripción o API son costes separados; un medidor doméstico no incluye el centro de datos.
---
Energía: vatios medios × horas ÷ 1.000. Multiplica los kWh por tu tarifa. Ejemplo ficticio: ocho horas diarias durante treinta días, a 0,20 USD/kWh. A 10W: 0,08kWh y 0,016 USD por noche; 2,4kWh y 0,48 USD en treinta noches. A 30W: 0,24kWh y 0,048 USD; 7,2kWh y 1,44 USD. A 60W: 0,48kWh y 0,096 USD; 14,4kWh y 2,88 USD.

No son mediciones de un MacBook ni tarifas locales. Los impuestos y tramos modifican la factura. Para calcular el coste adicional frente al reposo, mide y resta el consumo en reposo durante el mismo tiempo.
---
Un cargador de 70W no implica consumir 70W continuamente. La carga de batería, las pantallas y las tareas cambian la demanda. Apagar la pantalla puede reducir su consumo, sin una cifra universal de ahorro.
---
Usa un medidor de enchufe con kWh acumulados siguiendo sus instrucciones. 0,06kWh en dos horas equivale a 30W medios. Extrapolar a ocho horas da 0,24kWh solo si la carga es similar. Mide preferiblemente todo el trabajo y registra la batería; las pantallas con alimentación independiente quedan fuera de esa medición.
---
pika mantiene tareas que el reposo podría interrumpir; no mide energía ni reduce tarifas de IA. Mantener el Mac despierto puede aumentar el consumo. Comprueba el servicio auxiliar, activa Session, deja Monitor apagado si no necesitas mantener la pantalla y prueba brevemente con la tapa cerrada. Desactiva Session al terminar. Las aprobaciones pendientes y los fallos de red requieren atención aparte.
---
Define el resultado y cómo detener el trabajo. Configura límites o avisos cuando el servicio los permita y evita contar dos veces una suscripción existente como gasto adicional. Conecta la alimentación y utiliza una mesa firme y ventilada, nunca una bolsa ni ropa de cama.
---
Artículo del creador de pika. Fórmula: Virginia Cooperative Extension. Ventilación: Apple. Potencias y precio en USD son supuestos ilustrativos.''')
add('fr','Quand l’IA travaille la nuit, qui paie l’électricité ?','Estimons huit heures de travail avec des hypothèses explicites, en séparant électricité domestique et frais du service d’IA.','Deux dépenses distinctes|Le coût de huit heures|La puissance du chargeur ne suffit pas|Mesurer sa propre tâche|pika économise-t-il l’énergie ?|Avant de partir|Hypothèses et sources','''Avec l’IA dans le cloud, le fournisseur effectue le calcul principal du modèle. Votre Mac consomme encore pour les compilations et tests locaux. Avec un modèle local, il effectue aussi le calcul du modèle. Abonnement ou API et électricité sont deux dépenses différentes ; une mesure à la prise ne comprend pas le centre de données.
---
Énergie : puissance moyenne en W × heures ÷ 1 000. Multipliez les kWh par votre tarif. Exemple hypothétique : huit heures par jour, trente jours, 0,20 USD/kWh. À 10W : 0,08kWh et 0,016 USD par nuit, puis 2,4kWh et 0,48 USD sur trente nuits. À 30W : 0,24kWh et 0,048 USD, puis 7,2kWh et 1,44 USD. À 60W : 0,48kWh et 0,096 USD, puis 14,4kWh et 2,88 USD.

Ce ne sont ni des mesures de MacBook ni un tarif local. Taxes et tranches peuvent modifier la facture. Pour le surcoût par rapport à la veille, mesurez puis soustrayez la consommation en veille sur la même durée.
---
Un chargeur de 70W ne signifie pas une consommation constante de 70W. Batterie, écrans et tâches locales modifient la demande. Éteindre l’écran peut réduire son énergie, sans économie identique pour tous les Mac.
---
Utilisez un wattmètre de prise mesurant les kWh cumulés, selon sa notice. 0,06kWh en deux heures correspond à 30W moyens. Cela donne 0,24kWh sur huit heures uniquement à charge comparable. Mesurez de préférence toute la tâche, notez les niveaux de batterie et excluez explicitement les écrans alimentés séparément.
---
pika maintient les tâches que la veille pourrait interrompre. Il ne mesure pas l’électricité et ne réduit pas les frais d’IA. Garder le Mac éveillé peut augmenter sa consommation. Vérifiez le service auxiliaire, activez Session, laissez Monitor désactivé si l’écran n’est pas nécessaire, puis testez brièvement le couvercle fermé. Désactivez Session à la fin. Les demandes d’autorisation et erreurs réseau restent à traiter séparément.
---
Définissez le résultat attendu et la manière d’arrêter. Configurez limites ou alertes si disponibles ; ne comptez pas deux fois un abonnement existant comme dépense supplémentaire. Branchez le Mac sur une table ferme et ventilée, jamais dans un sac ou sous la literie.
---
Article du créateur de pika. Calcul : Virginia Cooperative Extension. Ventilation : Apple. Puissances et tarif en USD sont hypothétiques.''')
add('de','Wenn die KI nachts arbeitet: Wer zahlt den Strom?','Acht Stunden Mac-Betrieb als Rechenbeispiel – getrennt von Abonnement- und API-Kosten.','Zwei getrennte Kosten|Was kosten acht Stunden?|Netzteilleistung ist nicht Verbrauch|Die eigene Arbeit messen|Spart pika Strom?|Vor dem Weggehen|Annahmen und Quellen','''Bei Cloud-KI übernimmt der Anbieter die eigentliche Modellberechnung. Lokale Builds und Tests verbrauchen trotzdem Strom auf deinem Mac. Ein lokales Modell wird ebenfalls dort berechnet. Haushaltsstrom und KI-Gebühren sind getrennte Kosten; eine Steckdosenmessung erfasst nicht das Rechenzentrum.
---
Mittlere Watt × Stunden ÷ 1.000 ergibt kWh. Multipliziere mit deinem Tarif. Fiktives Beispiel: acht Stunden täglich, dreißig Tage, 0,20 USD/kWh. Bei 10W: 0,08kWh und 0,016 USD pro Nacht; 2,4kWh und 0,48 USD für dreißig Nächte. Bei 30W: 0,24kWh und 0,048 USD; 7,2kWh und 1,44 USD. Bei 60W: 0,48kWh und 0,096 USD; 14,4kWh und 2,88 USD.

Das sind keine MacBook-Messwerte oder örtlichen Tarife. Steuern und Tarifstaffeln verändern die Rechnung. Für Mehrkosten gegenüber dem Ruhezustand dessen Verbrauch über dieselbe Zeit messen und abziehen.
---
Ein 70W-Netzteil bedeutet keinen dauerhaften Verbrauch von 70W. Akkuladung, Displays und lokale Aufgaben verändern die Last. Ein ausgeschaltetes Display kann Strom sparen, aber nicht bei jedem Gerät denselben Betrag.
---
Ein Steckdosenmessgerät mit kumulierten kWh nach Anleitung verwenden. 0,06kWh in zwei Stunden entsprechen durchschnittlich 30W. Acht Stunden ergeben nur bei ähnlicher Last 0,24kWh. Möglichst die ganze Aufgabe messen, Akkustände notieren und separat versorgte Displays berücksichtigen: Sie fehlen in der Netzteilmessung.
---
pika hält Aufgaben am Laufen, die der Ruhezustand unterbrechen könnte. Es misst keinen Strom und senkt keine KI-Gebühren. Wachhalten kann mehr Strom verbrauchen. Hilfsdienst prüfen, Session einschalten, Monitor bei unnötiger Anzeige ausschalten und kurz mit geschlossenem Deckel testen. Danach Session ausschalten. Freigaben, Netzwerkfehler und die Erkennung des Aufgabenendes bleiben separate Themen.
---
Ergebnis und Abbruchbedingung festlegen. Falls angeboten, Nutzungsgrenzen oder Warnungen einstellen; ein bestehendes Abo nicht doppelt als Zusatzkosten zählen. Netzstrom und eine feste, gut belüftete Tischfläche nutzen, keine Tasche oder Bettdecke.
---
Vom pika-Entwickler verfasst. Formel: Virginia Cooperative Extension. Belüftung: Apple. Wattwerte und USD-Tarif sind Annahmen.''')
add('pt-BR','Se a IA trabalha à noite, quem paga a eletricidade?','Uma estimativa de oito horas de uso do Mac, separando energia doméstica e cobrança do serviço de IA.','Dois custos diferentes|Quanto custam oito horas?|Potência do carregador não é consumo|Meça sua tarefa|pika economiza energia?|Antes de sair|Premissas e fontes','''Na IA em nuvem, o provedor faz o cálculo principal do modelo, mas compilações e testes locais ainda usam energia no Mac. Um modelo local também roda nele. Assinatura ou API e eletricidade são contas diferentes; medir a tomada não mede o centro de dados.
---
Potência média em W × horas ÷ 1.000 = kWh. Multiplique pela tarifa. Exemplo fictício: oito horas por dia, trinta dias, US$ 0,20/kWh. Com 10W: 0,08kWh e US$ 0,016 por noite; 2,4kWh e US$ 0,48 em trinta noites. Com 30W: 0,24kWh e US$ 0,048; 7,2kWh e US$ 1,44. Com 60W: 0,48kWh e US$ 0,096; 14,4kWh e US$ 2,88.

Não são medições de MacBook nem tarifas brasileiras. Impostos e faixas mudam a conta. Para calcular o adicional em relação ao repouso, meça e subtraia o consumo em repouso no mesmo período.
---
Um carregador de 70W não significa consumo contínuo de 70W. Bateria, monitores e tarefas mudam a demanda. Desligar a tela pode reduzir seu consumo, sem uma economia universal.
---
Use um medidor de tomada com kWh acumulados conforme o manual. 0,06kWh em duas horas equivale a 30W médios. Projetar 0,24kWh para oito horas só funciona com carga semelhante. Prefira medir toda a tarefa e registrar a bateria. Monitores alimentados separadamente ficam fora da medição do carregador.
---
pika mantém tarefas que o repouso poderia interromper; não mede energia nem reduz tarifas de IA. Manter o Mac acordado pode aumentar o consumo. Verifique o serviço auxiliar, ative Session, deixe Monitor desligado quando dispensável e teste brevemente com a tampa fechada. Desative Session ao terminar. Aprovações pendentes e erros de rede precisam de atenção separada.
---
Defina o resultado e como parar. Configure limites ou alertas se disponíveis, sem contar uma assinatura existente duas vezes como gasto extra. Use energia conectada e uma mesa firme e ventilada, nunca uma bolsa ou roupa de cama.
---
Texto do criador de pika. Fórmula: Virginia Cooperative Extension. Ventilação: Apple. Potências e preço em dólar são hipóteses.''')
add('ru','Если ИИ работает ночью, кто платит за электричество?','Считаем восемь часов работы Mac на условных данных и отделяем электричество от оплаты ИИ-сервиса.','Два разных расхода|Цена восьми часов|Мощность зарядки — не потребление|Измерьте свою задачу|Экономит ли pika энергию?|Перед уходом|Допущения и источники','''В облачном ИИ основные вычисления модели выполняет сервер провайдера, но локальные сборки и тесты расходуют энергию Mac. Локальная модель вычисляется на самом Mac. Электричество и подписка или API оплачиваются отдельно; прибор у розетки не измеряет энергию дата-центра.
---
Средние ватты × часы ÷ 1 000 дают кВт·ч. Умножьте на свой тариф. Условный пример: восемь часов в день, тридцать дней, 0,20 доллара США/кВт·ч. При 10Вт: 0,08кВт·ч и 0,016 доллара за ночь; 2,4кВт·ч и 0,48 доллара за тридцать ночей. При 30Вт: 0,24кВт·ч и 0,048 доллара; 7,2кВт·ч и 1,44 доллара. При 60Вт: 0,48кВт·ч и 0,096 доллара; 14,4кВт·ч и 2,88 доллара.

Это не измерения MacBook и не местный тариф. Налоги и тарифные ступени меняют счёт. Для сравнения со сном измерьте и вычтите потребление спящего Mac за то же время.
---
Зарядка на 70Вт не означает постоянный расход 70Вт. Заряд аккумулятора, экраны и локальные задачи меняют нагрузку. Выключение экрана может уменьшить его потребление, но универсальной величины экономии нет.
---
Используйте розеточный измеритель накопленных кВт·ч по инструкции. 0,06кВт·ч за два часа — в среднем 30Вт. Прогноз 0,24кВт·ч за восемь часов верен только при сходной нагрузке. Лучше измерить задачу целиком и записать заряд батареи. Отдельно питающиеся мониторы не входят в показания зарядки.
---
pika сохраняет работу, которую может прервать сон, но не измеряет энергию и не снижает тарифы ИИ. Бодрствующий Mac может расходовать больше. Проверьте вспомогательную службу, включите Session, выключите Monitor, если экран не нужен, и ненадолго закройте и откройте крышку для проверки. После работы выключите Session. Ожидание разрешения и ошибки сети требуют отдельного внимания.
---
Определите результат и условие остановки. Настройте лимиты или уведомления, если сервис их поддерживает; не учитывайте существующую подписку дважды как дополнительную трату. Подключите питание и поставьте Mac на твёрдый проветриваемый стол, не в сумку или постель.
---
Статья автора pika. Формула: Virginia Cooperative Extension. Вентиляция: Apple. Мощности и долларовый тариф — допущения.''')
add('id','Jika AI bekerja semalaman, siapa membayar listriknya?','Hitung delapan jam penggunaan Mac dengan asumsi yang jelas, terpisah dari biaya layanan AI.','Dua biaya berbeda|Biaya delapan jam|Daya pengisi bukan konsumsi nyata|Ukur tugas sendiri|Apakah pika menghemat listrik?|Sebelum meninggalkan Mac|Asumsi dan sumber','''Pada AI cloud, server penyedia melakukan komputasi utama model, tetapi build dan pengujian lokal tetap memakai listrik Mac. Model lokal juga dihitung di Mac. Tagihan listrik dan langganan atau API adalah biaya terpisah; meter stopkontak tidak mencakup pusat data.
---
Watt rata-rata × jam ÷ 1.000 menghasilkan kWh. Kalikan dengan tarif. Contoh hipotetis: delapan jam sehari, tiga puluh hari, USD 0,20/kWh. Pada 10W: 0,08kWh dan USD 0,016 per malam; 2,4kWh dan USD 0,48 untuk tiga puluh malam. Pada 30W: 0,24kWh dan USD 0,048; 7,2kWh dan USD 1,44. Pada 60W: 0,48kWh dan USD 0,096; 14,4kWh dan USD 2,88.

Ini bukan pengukuran MacBook atau tarif Indonesia. Pajak dan golongan tarif memengaruhi tagihan. Untuk biaya tambahan dibanding tidur, ukur lalu kurangi konsumsi saat tidur selama durasi yang sama.
---
Pengisi 70W tidak berarti konsumsi terus-menerus 70W. Baterai, layar dan tugas lokal mengubah beban. Mematikan layar dapat mengurangi energi layar, tetapi tidak dengan angka penghematan universal.
---
Gunakan meter stopkontak dengan kWh kumulatif sesuai petunjuk. 0,06kWh dalam dua jam berarti rata-rata 30W. Perkiraan 0,24kWh selama delapan jam hanya berlaku jika bebannya serupa. Sebaiknya ukur seluruh tugas dan catat baterai. Layar dengan daya terpisah tidak termasuk pembacaan pengisi.
---
pika menjaga tugas yang mungkin terhenti karena tidur sistem, bukan mengukur listrik atau menurunkan biaya AI. Menjaga Mac tetap aktif dapat menambah konsumsi. Periksa layanan pembantu, aktifkan Session, matikan Monitor jika layar tidak diperlukan, lalu uji dengan menutup dan membuka tutup sebentar. Matikan Session setelah selesai. Persetujuan tertunda dan gangguan jaringan perlu ditangani terpisah.
---
Tentukan hasil dan cara berhenti. Atur batas atau pemberitahuan jika tersedia, tanpa menghitung langganan yang sudah ada dua kali sebagai biaya tambahan. Sambungkan daya dan gunakan meja kokoh berventilasi, bukan tas atau tempat tidur.
---
Ditulis pembuat pika. Rumus: Virginia Cooperative Extension. Ventilasi: Apple. Daya dan tarif USD hanyalah asumsi.''')
add('vi','AI làm việc suốt đêm thì ai trả tiền điện?','Ước tính tám giờ chạy Mac bằng giả định rõ ràng, tách tiền điện khỏi phí dịch vụ AI.','Hai khoản chi khác nhau|Tám giờ tốn bao nhiêu?|Công suất sạc không phải điện tiêu thụ|Đo tác vụ của bạn|pika có tiết kiệm điện không?|Trước khi rời máy|Giả định và nguồn','''Với AI đám mây, máy chủ của nhà cung cấp xử lý phần tính toán chính của mô hình, nhưng việc biên dịch và kiểm thử trên Mac vẫn dùng điện. Mô hình cục bộ cũng tính toán trên Mac. Tiền điện và phí thuê bao hoặc API là hai khoản riêng; đo tại ổ cắm không bao gồm trung tâm dữ liệu.
---
Công suất trung bình W × giờ ÷ 1.000 = kWh. Nhân với đơn giá. Ví dụ giả định: tám giờ mỗi ngày, ba mươi ngày, 0,20 USD/kWh. 10W: 0,08kWh và 0,016 USD mỗi đêm; 2,4kWh và 0,48 USD cho ba mươi đêm. 30W: 0,24kWh và 0,048 USD; 7,2kWh và 1,44 USD. 60W: 0,48kWh và 0,096 USD; 14,4kWh và 2,88 USD.

Đây không phải số đo MacBook hay biểu giá Việt Nam. Thuế và bậc giá ảnh hưởng hóa đơn. Muốn tính phần tăng thêm so với chế độ ngủ, hãy đo rồi trừ điện năng lúc ngủ trong cùng thời gian.
---
Sạc 70W không có nghĩa máy luôn dùng 70W. Sạc pin, màn hình và công việc cục bộ làm tải thay đổi. Tắt màn hình có thể giảm điện cho màn hình nhưng không có mức tiết kiệm chung.
---
Dùng thiết bị đo ổ cắm ghi kWh tích lũy theo hướng dẫn. 0,06kWh trong hai giờ tương đương trung bình 30W. Chỉ khi tải tương tự mới suy ra 0,24kWh cho tám giờ. Nên đo trọn tác vụ và ghi mức pin. Màn hình dùng nguồn riêng không nằm trong số đo của bộ sạc.
---
pika duy trì công việc có thể bị chế độ ngủ ngắt, không đo điện hay giảm phí AI. Giữ Mac thức có thể tăng tiêu thụ. Kiểm tra dịch vụ hỗ trợ, bật Session, tắt Monitor nếu không cần giữ màn hình, rồi đóng và mở nắp trong thời gian ngắn để thử. Tắt Session khi xong. Chờ phê duyệt và lỗi mạng cần xử lý riêng.
---
Xác định kết quả và cách dừng. Đặt giới hạn hoặc thông báo nếu dịch vụ hỗ trợ; đừng tính thuê bao hiện có hai lần thành chi phí mới. Cắm nguồn và đặt máy trên bàn cứng thông thoáng, không để trong túi hay chăn đệm.
---
Bài của người tạo pika. Công thức: Virginia Cooperative Extension. Thông gió: Apple. Công suất và giá USD là giả định.''')
add('hi','AI रात भर काम करे तो बिजली का बिल कौन भरेगा?','स्पष्ट मान्यताओं से Mac के आठ घंटे का खर्च निकालें और बिजली को AI सेवा शुल्क से अलग समझें।','दो अलग खर्च|आठ घंटे का हिसाब|चार्जर की क्षमता और खपत|अपना काम मापें|क्या pika बिजली बचाता है?|जाने से पहले तीन फैसले|मान्यताएँ और स्रोत','''क्लाउड AI में मॉडल की मुख्य गणना प्रदाता के सर्वर पर होती है, लेकिन Mac पर स्थानीय बिल्ड और परीक्षण भी बिजली लेते हैं। स्थानीय मॉडल की गणना भी Mac करता है। घर की बिजली और सदस्यता या API शुल्क अलग खर्च हैं। सॉकेट पर मापने से डेटा सेंटर की ऊर्जा नहीं मापी जाती।
---
औसत वाट × घंटे ÷ 1,000 से kWh मिलता है। इसे दर से गुणा करें। काल्पनिक उदाहरण: प्रतिदिन आठ घंटे, तीस दिन और 0.20 अमेरिकी डॉलर/kWh। 10W पर प्रति रात 0.08kWh और 0.016 डॉलर; तीस रातों में 2.4kWh और 0.48 डॉलर। 30W पर 0.24kWh और 0.048 डॉलर; तीस रातों में 7.2kWh और 1.44 डॉलर। 60W पर 0.48kWh और 0.096 डॉलर; तीस रातों में 14.4kWh और 2.88 डॉलर।

ये MacBook के वास्तविक माप या भारतीय दरें नहीं हैं। कर और दरों के स्लैब बिल बदलते हैं। स्लीप की तुलना में अतिरिक्त खर्च जानने के लिए उतने ही समय की स्लीप खपत मापकर घटाएँ।
---
70W चार्जर का अर्थ लगातार 70W खपत नहीं है। बैटरी चार्जिंग, स्क्रीन और स्थानीय काम से भार बदलता है। स्क्रीन बंद करने से उसकी ऊर्जा घट सकती है, लेकिन बचत का एक सार्वभौमिक आँकड़ा नहीं है।
---
कुल kWh दर्ज करने वाला प्लग-इन मीटर उसके निर्देशों के अनुसार इस्तेमाल करें। दो घंटे में 0.06kWh यानी औसतन 30W। आठ घंटे के लिए 0.24kWh का अनुमान तभी उचित है जब भार समान रहे। पूरा काम मापना बेहतर है; बैटरी स्तर भी लिखें। अलग बिजली वाले मॉनिटर चार्जर के माप में नहीं आते।
---
pika स्लीप से रुकने वाले काम को जारी रखने के लिए है; यह ऊर्जा मीटर नहीं और AI शुल्क नहीं घटाता। Mac को जागृत रखने से खपत बढ़ सकती है। सहायक सेवा जाँचें, Session ON करें, स्क्रीन जरूरी न हो तो Monitor OFF रखें और ढक्कन थोड़ी देर बंद करके फिर खोलकर प्रगति जाँचें। काम के बाद Session OFF करें। अनुमति का इंतजार और नेटवर्क त्रुटियाँ अलग समस्याएँ हैं।
---
काम का परिणाम और रुकने की शर्त तय करें। सेवा में उपलब्ध हों तो उपयोग सीमा या सूचना लगाएँ; मौजूदा सदस्यता को अतिरिक्त खर्च में दो बार न गिनें। बिजली से जोड़कर ठोस, हवादार मेज पर रखें; बैग या बिस्तर के अंदर न चलाएँ।
---
pika निर्माता का लेख। सूत्र: Virginia Cooperative Extension। हवा के प्रवाह की सलाह: Apple। वाट और डॉलर दर केवल काल्पनिक उदाहरण हैं।''')
add('ar','إذا عمل الذكاء الاصطناعي طوال الليل، فمن يدفع فاتورة الكهرباء؟','نحسب ثماني ساعات من تشغيل Mac بافتراضات واضحة، ونفصل كهرباء المنزل عن رسوم خدمة الذكاء الاصطناعي.','تكلفتان منفصلتان|كم تكلف ثماني ساعات؟|قدرة الشاحن ليست الاستهلاك|قس عملك الفعلي|هل يوفر pika الكهرباء؟|قبل مغادرة الجهاز|الافتراضات والمصادر','''في الذكاء الاصطناعي السحابي يجري خادم المزود الحساب الرئيسي للنموذج، لكن البناء والاختبارات المحلية تستهلك كهرباء Mac أيضاً. أما النموذج المحلي فيُحسب على Mac. الكهرباء والاشتراك أو API تكاليف منفصلة؛ قياس المقبس لا يشمل مركز البيانات.
---
متوسط الواط × الساعات ÷ 1,000 يعطي kWh، ثم نضربه بسعر الوحدة. مثال افتراضي: ثماني ساعات يومياً لثلاثين يوماً بسعر 0.20 دولار أمريكي/kWh. عند 10W: ‏0.08kWh و0.016 دولار لليلة؛ و2.4kWh و0.48 دولار لثلاثين ليلة. عند 30W: ‏0.24kWh و0.048 دولار؛ و7.2kWh و1.44 دولار. عند 60W: ‏0.48kWh و0.096 دولار؛ و14.4kWh و2.88 دولار.

هذه ليست قياسات MacBook ولا تعرفة محلية. الضرائب وشرائح الأسعار تؤثر في الفاتورة. لحساب الزيادة مقارنة بالسكون، قس استهلاك السكون خلال المدة نفسها واطرحه.
---
شاحن 70W لا يعني استهلاك 70W باستمرار. شحن البطارية والشاشات والمهام المحلية تغير الحمل. إطفاء الشاشة قد يقلل طاقتها، لكن لا توجد قيمة توفير موحدة.
---
استخدم مقياس مقبس يسجل kWh التراكمية وفق تعليماته. استهلاك 0.06kWh خلال ساعتين يعني متوسط 30W. تقدير 0.24kWh لثماني ساعات صحيح فقط إذا كان الحمل مشابهاً. يفضل قياس المهمة كاملة وتسجيل شحن البطارية. الشاشات ذات الطاقة المنفصلة لا تدخل في قراءة الشاحن.
---
pika يحافظ على المهام التي قد يقطعها السكون؛ ليس مقياس طاقة ولا يخفض رسوم الذكاء الاصطناعي. إبقاء Mac مستيقظاً قد يزيد الاستهلاك. تحقق من الخدمة المساعدة، شغّل Session وأوقف Monitor إن لم تحتج الشاشة، ثم أغلق الغطاء وافتحه بعد فترة قصيرة للتحقق. أوقف Session بعد الانتهاء. انتظار الموافقات وأخطاء الشبكة يحتاجان معالجة منفصلة.
---
حدد النتيجة وطريقة التوقف. اضبط حدود الاستخدام أو التنبيهات إذا كانت مدعومة، ولا تحسب الاشتراك الموجود مرتين كتكلفة إضافية. وصّل الطاقة واستخدم طاولة صلبة جيدة التهوية، لا حقيبة أو فراشاً.
---
كتبه مطور pika. المعادلة من Virginia Cooperative Extension وإرشادات التهوية من Apple. القدرة وسعر الدولار افتراضات توضيحية.''')
add('th','ให้ AI ทำงานทั้งคืน ใครจ่ายค่าไฟ?','ลองคำนวณการเปิด Mac แปดชั่วโมงด้วยสมมติฐานที่ชัดเจน และแยกค่าไฟออกจากค่าบริการ AI','ค่าใช้จ่ายสองส่วน|แปดชั่วโมงคิดเป็นเท่าไร?|กำลังชาร์จไม่ใช่ไฟที่ใช้จริง|วัดงานของคุณเอง|pika ช่วยประหยัดไฟไหม?|ก่อนออกไปทำอย่างอื่น|สมมติฐานและแหล่งข้อมูล','''AI บนคลาวด์ใช้เซิร์ฟเวอร์ของผู้ให้บริการคำนวณโมเดลเป็นหลัก แต่การบิลด์และทดสอบบน Mac ยังใช้ไฟของคุณ โมเดลภายในเครื่องก็คำนวณบน Mac เช่นกัน ค่าไฟกับค่าสมาชิกหรือ API เป็นคนละส่วน การวัดที่ปลั๊กไม่รวมพลังงานของศูนย์ข้อมูล
---
กำลังเฉลี่ย W × ชั่วโมง ÷ 1,000 ได้ kWh แล้วคูณราคาต่อหน่วย ตัวอย่างสมมติ: วันละแปดชั่วโมง สามสิบวัน ราคา 0.20 ดอลลาร์สหรัฐ/kWh ที่ 10W ใช้คืนละ 0.08kWh ราคา 0.016 ดอลลาร์ รวมสามสิบคืน 2.4kWh ราคา 0.48 ดอลลาร์ ที่ 30W ใช้ 0.24kWh ราคา 0.048 ดอลลาร์ รวม 7.2kWh ราคา 1.44 ดอลลาร์ ที่ 60W ใช้ 0.48kWh ราคา 0.096 ดอลลาร์ รวม 14.4kWh ราคา 2.88 ดอลลาร์

นี่ไม่ใช่ผลวัด MacBook หรืออัตราค่าไฟไทย ภาษีและขั้นอัตรามีผลต่อบิล หากต้องการค่าใช้จ่ายที่เพิ่มจากการพักเครื่อง ให้หักพลังงานที่วัดขณะพักในเวลาเท่ากัน
---
ที่ชาร์จ 70W ไม่ได้หมายความว่าใช้ 70W ตลอดเวลา การชาร์จแบตเตอรี่ จอภาพ และงานในเครื่องทำให้โหลดเปลี่ยน การปิดจออาจลดไฟของจอ แต่ไม่มีตัวเลขประหยัดที่ใช้ได้กับทุกเครื่อง
---
ใช้มิเตอร์แบบเสียบปลั๊กที่บันทึก kWh สะสมตามคู่มือ หากสองชั่วโมงใช้ 0.06kWh จะเฉลี่ย 30W การคาดว่าแปดชั่วโมงใช้ 0.24kWh ใช้ได้เมื่อโหลดใกล้เคียงกัน ควรวัดทั้งงานและบันทึกระดับแบตเตอรี่ จอที่ใช้ไฟแยกไม่รวมในค่าของที่ชาร์จ
---
pika รักษางานที่อาจหยุดเพราะเครื่องพัก ไม่ได้วัดไฟหรือลดค่าบริการ AI การให้ Mac ตื่นต่ออาจใช้ไฟเพิ่ม ตรวจบริการช่วยเหลือ เปิด Session ปิด Monitor ถ้าไม่ต้องคงจอไว้ แล้วปิดและเปิดฝาสั้น ๆ เพื่อตรวจงาน เมื่อเสร็จให้ปิด Session การรออนุมัติและปัญหาเครือข่ายต้องจัดการแยก
---
กำหนดผลลัพธ์และวิธีหยุด ตั้งขีดจำกัดหรือการแจ้งเตือนหากบริการรองรับ และอย่านับค่าสมาชิกเดิมซ้ำเป็นค่าใช้จ่ายเพิ่ม ต่อไฟและวางบนโต๊ะแข็งที่ระบายอากาศดี ไม่ใช่ในกระเป๋าหรือเครื่องนอน
---
เขียนโดยผู้สร้าง pika สูตรจาก Virginia Cooperative Extension และคำแนะนำการระบายอากาศจาก Apple กำลังไฟและราคาเป็นสมมติฐานเท่านั้น''')
