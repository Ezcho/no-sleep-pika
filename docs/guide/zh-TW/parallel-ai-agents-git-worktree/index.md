Source: https://no-sleep-pika.online/guide/zh-TW/parallel-ai-agents-git-worktree/
Language: zh-TW

MAC GUIDE · 2026-11-24

# 兩個 AI 同時改同一份檔案？先把工作資料夾分開

用 Git worktree 為每個 AI 準備獨立工作資料夾，再檢查修改、逐一整合，避免尚未完成的工作混在一起。

## 同一個資料夾為什麼容易衝突

讓一個 AI 改介面、另一個寫測試，如果都在同一資料夾，它們仍會讀寫同一批檔案。建立兩個分支名稱，不會讓資料夾自動有兩套檔案。在這裡切換分支，也會改變另一個 AI 正在使用的檔案。

Git worktree 能為同一儲存庫增加工作資料夾。各資料夾有自己的分支與取出的檔案，但共享版本歷史。它能分開進行中的修改，卻不保證日後整合時沒有衝突。

- 1 分開資料夾

- 2 分配任務

- 3 檢查修改

- 4 逐一整合

## 先確認提交起點

在現有 Git 專案執行以下指令。本例至少需要一筆提交，HEAD 指向提交起點。沒有輸出表示未回報修改或未追蹤檔案；被忽略的檔案仍可能存在。

若出現清單，先確認內容，只提交必要修改，或選擇已有提交作為起點。別盲目加入整個資料夾，以免包含金鑰或無關工作。新資料夾從 HEAD 開始，不會帶入尚未提交的編輯。

```
git status --short
```

## 建立兩個工作資料夾

在原專案執行這兩條指令，會在旁邊建立工作資料夾及 ai-ui、ai-tests 分支。分支名稱和目標路徑必須尚未使用；若已存在，請換名稱，不要強制覆寫。

已安裝的相依套件、被忽略的 .env 與本機設定不會全部自動複製。依專案說明準備，只提供任務需要的憑證。同時啟動開發伺服器時，也要分開連接埠。worktree 不是安全沙箱：有權限的工具仍可存取其他資料夾。

```
git worktree add -b ai-ui ../project-ai-ui HEAD
git worktree add -b ai-tests ../project-ai-tests HEAD
```

## 指定資料夾與任務範圍

分別在 project-ai-ui 和 project-ai-tests 啟動 AI，提供絕對路徑與明確的小任務。例如「只改介面元件」和「為現有行為新增測試，不修改應用程式碼」。

相依套件清單與鎖定檔等共用檔案應指定負責人。若必須修改同一檔案，就依序處理。請 AI 回報變動檔案、完成的檢查，以及剩餘工作。

## 檢查後逐一整合

在每個工作資料夾執行以下三條指令。status 列出修改與未追蹤檔案；diff 顯示已追蹤檔案尚未暫存的修改；diff --cached 顯示已暫存的修改。未追蹤的新檔案不會出現在這些 diff，需另外開啟檢查。

執行專案需要的檢查，把確認後的修改提交到各自分支。回到原專案，在目標分支逐一檢查並整合。worktree 不會自動合併結果。有重疊修改時，先解決衝突並確認整合結果，再處理下一個分支。

```
git status --short
git diff
git diff --cached
```

## pika 能幫什麼忙

pika 可依工作階段設定與安全保護條件，協助本機 AI 工作時讓 Mac 保持喚醒。它不會分派任務、合併分支或解決衝突。pika 1.3 的 QR 連線顯示 Mac 狀態與獲准的電源控制，不顯示 AI 輸出或準確完成百分比。是否完成仍需檢查 AI 結果與專案測試。

[下載 pika](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.3.0/pika-1.3.0.pkg) · [安裝說明](https://no-sleep-pika.online/install/)

資料與適用範圍

本文由 no-sleep-pika 開發者依 Git 官方文件撰寫，說明一般 AI 工作流程，不假設特定 AI 的功能或權限。也請遵守專案的貢獻規則與機密資訊管理規範。

- [Git · git-worktree](https://git-scm.com/docs/git-worktree)

- [Git · git-status](https://git-scm.com/docs/git-status)

- [Git · git-diff](https://git-scm.com/docs/git-diff)

由 no-sleep-pika 開發者撰寫，包含自家產品。

[讓 Mac 不進入睡眠的方法：闔蓋模式、caffeinate 與 pika →](https://no-sleep-pika.online/guide/zh-TW/keep-mac-awake/)[Markdown](https://no-sleep-pika.online/guide/zh-TW/parallel-ai-agents-git-worktree/index.md)
