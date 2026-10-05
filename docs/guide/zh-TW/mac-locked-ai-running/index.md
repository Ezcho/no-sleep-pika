Source: https://no-sleep-pika.online/guide/zh-TW/mac-locked-ai-running/
Language: zh-TW

MAC GUIDE · 2026-10-05

# Mac 鎖定螢幕後，Claude Code 與 Codex 還會繼續工作嗎？

分辨鎖定、關閉顯示器和系統睡眠，檢查本機 AI 工作、網路與闔蓋設定。

## 鎖定不等於停止

出現密碼畫面不代表工作結束。Mac 保持喚醒、應用程式與所需連線正常時，一般背景命令可以繼續。畫面操作或身分驗證可能需要解鎖。顯示器關閉與系統睡眠不同，鎖定後仍可能進入睡眠。請保留密碼保護。

## 本機或雲端工作

Codex CLI 在本機處理檔案與命令，明確交給 Codex Cloud 的工作在獨立雲端環境執行。Claude Code Remote Control 仍連接本機工作階段。重新連線不代表睡眠期間持續執行；pika 不會把工作搬到雲端。

[Codex CLI](https://learn.chatgpt.com/docs/codex/cli) · [Codex Cloud](https://learn.chatgpt.com/docs/cloud) · [Claude Code Remote Control](https://code.claude.com/docs/en/remote-control)

## 先檢查停止原因

先看最後訊息是否等待核准、提問、完成或發生錯誤，再檢查應用程式、Wi-Fi、VPN 和登入。下方唯讀命令顯示電源要求與近期事件；要求存在或 CPU 用量低都不能證明 AI 工作進度。

```
pmset -g assertions
```

```
pmset -g log | tail -n 60
```

## 三分鐘檢查

開蓋執行下方迴圈，保持終端機開啟，鎖定約三分鐘後檢查時間間隔。按 Ctrl+C 結束。長空白要與電源紀錄比較，也要查看 AI 紀錄與檔案修改時間。這只檢查簡單本機程序，闔蓋需另外測試。

```
while true; do date "+%Y-%m-%d %H:%M:%S"; sleep 10; done
```

## 闔蓋使用 pika

安裝 pika 與輔助服務，開啟 Session；不需維持畫面時將 Monitor 關閉，再闔蓋。畫面策略在闔蓋後套用。Session OFF 解除防睡眠並顯示 Monitor OFF，不會立即關閉畫面。接上電源、保持通風，勿放在密閉包內執行。保護機制或服務故障可能停止工作階段。

[下載 pika](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.0.13/pika-1.0.13.pkg) · [安裝說明](https://no-sleep-pika.online/install/)

## 常見問題

Monitor OFF 不會下令結束 AI 工作。tmux 不會防止系統睡眠；caffeinate 不處理網路或核准等待。pika MCP 的狀態也不是所有 AI 工作的進度。

資料與範圍

依 2026 年 10 月 5 日官方文件與 pika 實作撰寫。本文由 pika 製作者提供，不保證所有硬體持續運作。

- [Apple · Sleep and wake settings](https://support.apple.com/guide/mac-help/set-sleep-and-wake-settings-mchle41a6ccd/mac)

- [OpenAI · Codex CLI](https://learn.chatgpt.com/docs/codex/cli)

- [OpenAI · Codex Cloud](https://learn.chatgpt.com/docs/cloud)

- [Anthropic · Claude Code Remote Control](https://code.claude.com/docs/en/remote-control)

由 no-sleep-pika 開發者撰寫，包含自家產品。

[下載 pika](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.0.13/pika-1.0.13.pkg)[讓 Mac 不進入睡眠的方法：闔蓋模式、caffeinate 與 pika →](https://no-sleep-pika.online/guide/zh-TW/keep-mac-awake/)[Markdown](https://no-sleep-pika.online/guide/zh-TW/mac-locked-ai-running/index.md)
