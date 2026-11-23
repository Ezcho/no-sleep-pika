Source: https://no-sleep-pika.online/guide/zh-TW/control-mac-from-phone-qr/
Language: zh-TW

MAC GUIDE · 2026-11-23

# 用一個 QR Code 控制 Mac：手機管理工作階段、計時與關機

pika 1.3.0 讓手機不只查看狀態，還能在 Mac 授權後管理 Session、計時器和電源操作。

## 從查看狀態到操作

把建置或下載留在 Mac 上執行後，你可以用手機調整 Session、設定計時器，或要求關機、重新啟動。pika 1.3.0 在原有 QR 狀態頁加入了控制功能。

它不負責向 AI 傳送新指示，也不顯示 AI 對話、終端機輸出、工作進度或遠端桌面。

## 先更新 Mac 上的 pika

先將 Mac 上的 pika 更新至 1.3.0 或更新版本，並保持執行。闔蓋防睡眠需要輔助服務正常連線；Mac 和手機都需要網路。

若 macOS 無法驗證開發者，請先確認檔案來自官網。嘗試開啟後，在「系統設定 → 隱私權與安全性」為該檔案選擇「強制打開」，再完成系統確認或認證。名稱會隨版本變動；請參考下方安裝說明，不要關閉整機安全防護。

惡意軟體或檔案損壞警告屬於不同情況，不應使用這項放行步驟。

[下載 pika](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.3.0/pika-1.3.0.pkg) · [安裝說明](https://no-sleep-pika.online/install/)

## 掃碼後在 Mac 上授權

在已連接 pika MCP 的 AI 聊天中要求產生 pika QR Code，用手機相機掃描並連線。QR Code 五分鐘內有效，只能使用一次。初始連線只有查看權限，不會自動開啟 Session。

在手機要求遠端控制，再到 Mac 提示視窗批准。建議外出前同時看著兩台裝置完成；未經 Mac 授權就不能控制。

手機按鈕目前顯示韓文：先點「이 Mac에 연결」（連線），再點「Mac에 제어 허용 요청」（要求控制），最後在 Mac 批准。「예약·카운트다운 취소」用來取消計時或倒數。初次使用 MCP，請先看下方連線說明。

[MCP 連線說明 →](https://no-sleep-pika.online/zh-TW/#mcp)

## 手機可以控制什麼

Session 用來開啟或解除防睡眠。Monitor 僅在 Session 開啟時可用；闔蓋模式會在蓋子關閉後套用準備好的螢幕策略。Monitor 顯示要求的設定，不是實際螢幕影像。

電源條件包括僅接電時保持、拔掉充電器時解除，以及電量降到 30、40、50% 時解除。原有電池與發熱保護仍有效。發熱顯示是 macOS 狀態等級，不是攝氏溫度。

## 計時與 60 秒取消時間

計時可選 15、30、60、180、360 分鐘，到時解除 Session、睡眠、關機或重新啟動。解除 Session 只結束防睡眠，不會強制關閉 App。

立即關機或重新啟動需要確認，隨後 Mac 開始 60 秒倒數，可用取消計時撤銷。pika 先恢復睡眠設定，再向 macOS 發出要求。未儲存文件的提示可能延遲或取消關機；傳送成功不代表執行完成。

## 連線結束，權限也結束

控制權限只屬於目前獲准的連線。斷線或撤銷權限會取消遠端計時與倒數，重新連線需要再次批准。連線自 QR 發放起最多 24 小時；退出 pika 或 Mac 睡眠後，計時不會繼續執行。

偵測斷線可能需要數十秒。若要阻止關機，請點「예약·카운트다운 취소」並確認已取消，不要依靠中斷連線。遠端計時需要瀏覽器持續傳送連線訊號；切換到其他 App、讓瀏覽器進入背景，可能導致斷線並取消計時。

不要分享 QR Code。外出前先測試不重要的 Session 操作與取消計時。斷線頁面可能只保留最後狀態，不能據此認定 Mac 已關機；防睡眠也不保證網路或 AI 工作完成。

資料與範圍

本文由 no-sleep-pika 製作者於 2026 年 11 月 23 日撰寫，說明自家 App 1.3.0 的功能。安裝警告與設定名稱也請參閱 Apple 官方說明。

- [pika 1.3.0 · Release notes](https://github.com/Ezcho/no-sleep-pika/releases/tag/v1.3.0)

- [pika · Remote connection and permissions](https://github.com/Ezcho/no-sleep-pika/blob/v1.3.0/Remote/README.md)

- [Apple · Safely open apps on your Mac](https://support.apple.com/en-us/102445)

由 no-sleep-pika 開發者撰寫，包含自家產品。

[下載 pika](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.3.0/pika-1.3.0.pkg)[讓 Mac 不進入睡眠的方法：闔蓋模式、caffeinate 與 pika →](https://no-sleep-pika.online/guide/zh-TW/keep-mac-awake/)[Markdown](https://no-sleep-pika.online/guide/zh-TW/control-mac-from-phone-qr/index.md)
