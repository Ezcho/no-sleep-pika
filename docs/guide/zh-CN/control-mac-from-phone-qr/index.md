Source: https://no-sleep-pika.online/guide/zh-CN/control-mac-from-phone-qr/
Language: zh-CN

MAC GUIDE · 2026-11-23

# 用一个二维码控制 Mac：手机管理会话、定时与关机

pika 1.3.0 让手机不只查看状态，还能在 Mac 授权后管理 Session、定时任务和电源操作。

## 从查看状态到操作

把编译或下载留在 Mac 上运行后，你可以用手机调整 Session、设置定时，或请求关机、重新启动。pika 1.3.0 在原有二维码状态页中加入了控制功能。

它不负责向 AI 发送新指令，也不显示 AI 对话、终端输出、工作进度或远程桌面。

## 先更新 Mac 上的 pika

先把 Mac 上的 pika 更新至 1.3.0 或更新版本，并保持运行。合盖防睡眠需要辅助服务正常连接；Mac 和手机都需要联网。

如果 macOS 无法验证开发者，请先确认文件来自官网。尝试打开后，在“系统设置 → 隐私与安全性”中为该文件选择“仍要打开”，再完成系统确认或认证。名称可能随系统版本变化；请参考下方安装说明，不要关闭整机安全保护。

恶意软件或文件损坏警告属于不同情况，不应使用此放行步骤。

[下载 pika](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.3.0/pika-1.3.0.pkg) · [安装帮助](https://no-sleep-pika.online/install/)

## 扫码后在 Mac 上授权

在已连接 pika MCP 的 AI 聊天中请求生成 pika 二维码，用手机相机扫描并连接。二维码五分钟内有效，只能使用一次。连接最初只有查看权限，不会自动开启 Session。

在手机上请求远程控制，再到 Mac 的提示窗口批准。建议外出前同时看着两台设备完成；没有 Mac 授权就不能控制。

手机按钮目前显示韩语：先点“이 Mac에 연결”（连接），再点“Mac에 제어 허용 요청”（请求控制），最后在 Mac 批准。“예약·카운트다운 취소”用于取消定时或倒计时。首次使用 MCP，请先看下方连接说明。

[MCP 连接说明 →](https://no-sleep-pika.online/zh-CN/#mcp)

## 手机可以控制什么

Session 用于开启或解除防睡眠。Monitor 仅在 Session 开启时可选；合盖模式会在盖子关闭后应用已准备的屏幕策略。Monitor 显示请求的设置，不是实际屏幕画面。

电源条件包括仅接电时保持、拔掉充电器时解除，以及电量降到 30、40、50% 时解除。原有电池和发热保护仍有效。发热显示是 macOS 状态等级，不是摄氏温度。

## 定时与 60 秒取消时间

定时可选 15、30、60、180、360 分钟，到时解除 Session、睡眠、关机或重新启动。解除 Session 只结束防睡眠，不会强制关闭应用。

立即关机或重新启动需要确认，随后 Mac 开始 60 秒倒计时，可用取消定时撤销。pika 先恢复睡眠设置，再向 macOS 发出请求。未保存文档的提示可能推迟或取消关机；发送成功不等于执行完成。

## 连接结束，权限也结束

控制权限只属于当前获准的连接。断线或撤销权限会取消远程定时和倒计时，重新连接需要再次批准。连接自二维码发放起最多 24 小时；退出 pika 或 Mac 睡眠后，定时不会继续执行。

检测断线可能需要数十秒。要阻止关机，请点击“예약·카운트다운 취소”并确认已取消，不要依靠断开连接。远程定时需要浏览器持续发送连接信号；切换到其他应用、让浏览器进入后台，可能导致断线并取消定时。

不要分享二维码。外出前先测试一次无关紧要的 Session 操作和取消定时。断线页面可能只保留最后状态，不能据此认定 Mac 已关机；防睡眠也不保证网络或 AI 工作完成。

资料与范围

本文由 no-sleep-pika 制作者于 2026 年 11 月 23 日编写，说明自家应用 1.3.0 的功能。安装警告和设置名称也请参阅 Apple 官方说明。

- [pika 1.3.0 · Release notes](https://github.com/Ezcho/no-sleep-pika/releases/tag/v1.3.0)

- [pika · Remote connection and permissions](https://github.com/Ezcho/no-sleep-pika/blob/v1.3.0/Remote/README.md)

- [Apple · Safely open apps on your Mac](https://support.apple.com/en-us/102445)

[两个 AI 同时改同一份文件？先把工作文件夹分开 →](https://no-sleep-pika.online/guide/zh-CN/parallel-ai-agents-git-worktree/)

由 no-sleep-pika 开发者撰写，包含自家应用的比较。

[下载 pika](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.3.0/pika-1.3.0.pkg)[让 Mac 不进入睡眠的方法：合盖模式、caffeinate 与 pika →](https://no-sleep-pika.online/guide/zh-CN/keep-mac-awake/)[Markdown](https://no-sleep-pika.online/guide/zh-CN/control-mac-from-phone-qr/index.md)
