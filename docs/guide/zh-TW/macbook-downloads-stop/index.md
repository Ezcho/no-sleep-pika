Source: https://no-sleep-pika.online/guide/zh-TW/macbook-downloads-stop/
Language: zh-TW

MAC GUIDE · 2026-10-15

# MacBook 下載停止：關閉螢幕、睡眠與闔蓋有何不同？

先檢查網路與空間，再選擇 caffeinate 或 pika 維持工作。

## 先確認停止時點

先看下載程式是否提示暫停、網路錯誤、空間不足或需要登入。使用中也停止時，先檢查 Wi-Fi、VPN、伺服器和剩餘空間。防睡眠不能修復過期連結。

## 關螢幕不等於睡眠

螢幕關閉而系統仍醒著時，傳輸可能繼續；鎖定後也可能自動睡眠。支援的 Mac 可檢查接電時防止自動睡眠的選項。不必取消密碼保護。

## 開蓋使用 caffeinate

下方命令要求一小時內防止閒置系統睡眠。保持終端機開啟，在原程式下載；提前結束按 Ctrl+C。-t 單位為秒，-i 針對閒置系統睡眠，-d 針對顯示器。它不修復網路，也不涵蓋所有睡眠情況。

```
caffeinate -i -t 3600
```

```
man caffeinate
```

## 闔蓋的條件不同

外接顯示器需確認電源、外接鍵鼠及機型支援條件。充電器本身不等於完整配置。不接外屏時，請另做短傳輸測試，比較闔蓋前後收到的資料量。

## 使用 pika 維持下載

準備 pika 與輔助服務，開始下載後開啟 Session；不需維持畫面則 Monitor OFF，再闔蓋。畫面政策在闔蓋後套用。完成後關閉 Session。使用電源及通風桌面，勿在密閉袋中執行。保護機制或服務錯誤可能中止工作階段。

[下載 pika](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.0.13/pika-1.0.13.pkg) · [安裝說明](https://no-sleep-pika.online/install/)

## 確認下載完成

確認程式完成狀態、檔案大小，以及發布者提供的校驗碼。透過程式支援的功能續傳。pika 不代替連線恢復或偵測下載完成，關閉螢幕也不保證加速。

參考資料

2026 年 10 月 11 日核對 Apple 文件、caffeinate(8) 與 pika 實作。本文由 pika 製作者撰寫。

- [Apple · Sleep and wake settings](https://support.apple.com/guide/mac-help/set-sleep-and-wake-settings-mchle41a6ccd/mac)

- [Apple · External displays](https://support.apple.com/en-us/102501)

- `man caffeinate` · macOS System Manager’s Manual

[讓 AI 加班一整晚，電費誰來付？ →](https://no-sleep-pika.online/guide/zh-TW/ai-overnight-electricity-cost/)

由 no-sleep-pika 開發者撰寫，包含自家產品。

[下載 pika](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.0.13/pika-1.0.13.pkg)[讓 Mac 不進入睡眠的方法：闔蓋模式、caffeinate 與 pika →](https://no-sleep-pika.online/guide/zh-TW/keep-mac-awake/)[Markdown](https://no-sleep-pika.online/guide/zh-TW/macbook-downloads-stop/index.md)
