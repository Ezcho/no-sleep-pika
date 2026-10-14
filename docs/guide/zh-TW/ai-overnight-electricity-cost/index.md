Source: https://no-sleep-pika.online/guide/zh-TW/ai-overnight-electricity-cost/
Language: zh-TW

MAC GUIDE · 2026-10-15

# 讓 AI 加班一整晚，電費誰來付？

用假設數據估算 Mac 運作八小時的費用，區分家中電費與 AI 服務費。

## 兩種不同的帳單

雲端AI的模型運算主要由服務商的伺服器完成，但Mac上的建置、測試和檔案操作仍會耗電。本機模型則也在Mac運算。家中電費與訂閱或API費用是兩筆帳；插座量測不包含資料中心的耗電。

## 八小時要花多少？

平均功率W × 小時 ÷ 1,000 = kWh，再乘以電價。假設每天八小時、三十天、0.20美元/kWh：10W每天0.08kWh、0.016美元，三十天2.4kWh、0.48美元；30W每天0.24kWh、0.048美元，三十天7.2kWh、1.44美元；60W每天0.48kWh、0.096美元，三十天14.4kWh、2.88美元。

這不是MacBook實測值或臺灣電價。實際帳單受稅費、契約與級距影響。要比較睡眠時的額外費用，還須量測並減去同時間的睡眠耗電。

## 充電器瓦數不是實際耗電

70W充電器不表示電腦持續消耗70W。輸出能力與實際耗電不同，充電、螢幕和本機工作都會改變負載。關閉螢幕的節省量也不固定。

## 量測自己的工作

依說明使用可記錄累計kWh的插座電力計。兩小時0.06kWh相當於平均30W；只有負載相近才可推算八小時0.24kWh。最好量測完整工作並記錄電池電量。獨立供電的螢幕與擴充基座不在充電器讀數內。

## pika 能省電嗎？

pika維持可能被系統睡眠中斷的工作，不是電力計，也不會降低AI服務費。持續喚醒可能增加耗電。確認輔助服務，開啟Session，不需維持顯示時關閉Monitor，短暫闔蓋測試進度。完成後關閉Session；核准等待、網路錯誤與工作完成判斷仍需另外處理。

[下載 pika](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.0.13/pika-1.0.13.pkg) · [安裝說明](https://no-sleep-pika.online/install/)

## 離開前的三個決定

定義完成條件與停止方式，並在服務支援時設定用量上限或通知。別將既有訂閱重複計為新增費用。接上電源，放在通風的硬質桌面，不要在包包或寢具內運作。

假設與來源

pika製作者撰寫。公式參考Virginia Cooperative Extension，放置建議參考Apple。功率與美元單價皆為假設。

- [Virginia Cooperative Extension · Estimating appliance energy use](https://ext.vt.edu/content/pubs_ext_vt_edu/en/2901/2901-9014/2901-9014.html)

- [Apple · Mac operating temperatures](https://support.apple.com/en-us/102336)

由 no-sleep-pika 開發者撰寫，包含自家產品。

[下載 pika](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.0.13/pika-1.0.13.pkg)[讓 Mac 不進入睡眠的方法：闔蓋模式、caffeinate 與 pika →](https://no-sleep-pika.online/guide/zh-TW/keep-mac-awake/)[Markdown](https://no-sleep-pika.online/guide/zh-TW/ai-overnight-electricity-cost/index.md)
