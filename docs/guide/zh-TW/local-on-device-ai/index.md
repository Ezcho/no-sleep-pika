Source: https://no-sleep-pika.online/guide/zh-TW/local-on-device-ai/
Language: zh-TW

MAC GUIDE · 2026-10-22

# Claude Code 也是本機 AI 嗎？用 Llama、Qwen 理解裝置端 AI

應用程式裝在 Mac 上，不代表模型也在 Mac 上計算。分清工具、模型與執行位置。

概念圖：左側在裝置內計算，右側連接遠端伺服器。

## 安裝位置不等於計算位置

Claude Code 在終端機讀寫檔案，並不證明答案全在 Mac 內產生。本機工具也可能把內容送給遠端模型。請分別看使用的工具、計算答案的模型和計算地點。

## 本機 AI 與裝置端 AI

本機 AI 通常指在自己管理的電腦或附近伺服器執行模型；裝置端 AI 強調在目前設備本身計算。家中的獨立伺服器不是 Mac 本機。產生回答的計算叫推論，與訓練不同；開始使用本機模型不必從頭訓練。各產品用語可能不同。

## 工具與模型的不同角色

Claude Code 是處理檔案與指令的工作工具。Llama、Qwen 是不同大小和用途的模型系列。Ollama 用來執行或連接模型，其文件說明了 Claude Code 的本機及雲端連線方式。並非所有模型支援相同工具功能；表格比較角色，不是效能排名。

工具與模型的不同角色
| 名稱 | 角色 | 檢查項目
| Claude Code | 處理檔案和指令的工具 | 模型提供者與連線地址
| Llama · Qwen | 模型系列 | 本機或伺服器執行
| Ollama | 模型執行與連線軟體 | 所選模型的執行位置

## 本機執行會改變什麼？

事先準備模型與軟體後，本機推論可能離線運作，但網頁搜尋、外部服務與套件下載仍需網路。

模型大小、壓縮方式及一次處理的對話量影響記憶體與速度，本機不一定比較快。避免外部推論服務費不表示沒有硬體、電力和維護成本。

本機處理輸入不等於整個應用程式不會傳送資料。同步、紀錄、擴充功能和網路工具須另外確認。

## 三個檢查步驟

第一，查看模型與連線地址。Llama 或 Qwen 也可能由遠端服務提供，Ollama 同時支援本機與雲端。

第二，分清網路功能。準備完成且沒有重要工作時，可斷網試著產生短的新回答；這無法證明平常完全不傳送資料。

第三，檢查設定與文件。Ollama 可關閉其雲端模型和網頁搜尋，但不會阻擋其他應用程式連網。先以非敏感短文測試速度與品質。

## pika 的角色

Mac 本機工作可能因睡眠中斷或延遲，獨立遠端工作則不同。pika 不執行模型，也不把雲端 AI 變成本機 AI，而是在需要時保持 Mac 喚醒。確認輔助服務、開啟 Session 並短暫闔蓋測試，接上電源，放在通風桌面，完成後關閉 Session。

[下載 pika](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.0.13/pika-1.0.13.pkg) · [安裝說明](https://no-sleep-pika.online/install/)

來源與範圍

pika 製作者於2026年10月22日核對官方資料撰寫。本文是入門說明，不是所有模型或 Mac 的實測比較；相容性可能隨版本變動。

- [Anthropic · Claude Code overview](https://code.claude.com/docs/en/overview)

- [Ollama · Claude Code integration](https://docs.ollama.com/integrations/claude-code)

- [Ollama · Local-only mode and data](https://docs.ollama.com/faq)

- [Qwen · Run locally with Ollama](https://qwen.readthedocs.io/en/latest/run_locally/ollama.html)

- [Meta · Llama models](https://github.com/meta-llama/llama-models)

由 no-sleep-pika 開發者撰寫，包含自家產品。

[下載 pika](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.0.13/pika-1.0.13.pkg)[讓 Mac 不進入睡眠的方法：闔蓋模式、caffeinate 與 pika →](https://no-sleep-pika.online/guide/zh-TW/keep-mac-awake/)[Markdown](https://no-sleep-pika.online/guide/zh-TW/local-on-device-ai/index.md)
