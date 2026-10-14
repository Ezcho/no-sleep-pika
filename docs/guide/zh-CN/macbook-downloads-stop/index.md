Source: https://no-sleep-pika.online/guide/zh-CN/macbook-downloads-stop/
Language: zh-CN

MAC GUIDE · 2026-10-15

# MacBook 下载停止：关屏、睡眠和合盖有什么不同？

先排查网络和空间，再选择 caffeinate 或 pika 保持任务运行。

## 先找出停止时点

先看下载应用是否提示暂停、网络错误、空间不足或需要登录。使用中也会停止时，先查 Wi-Fi、VPN、服务器和剩余空间。防睡眠不能修复过期链接。

## 关屏不等于睡眠

屏幕关闭时，系统保持唤醒仍可能继续传输；锁屏后也可能随后自动睡眠。支持的 Mac 可检查接电时防止自动睡眠的选项。无需关闭密码保护。

## 开盖使用 caffeinate

下方命令请求一小时内防止空闲系统睡眠。保持终端打开，在原应用下载；提前结束按 Ctrl+C。-t 单位为秒，-i 针对空闲系统睡眠，-d 针对显示器。它不恢复网络，也不覆盖所有睡眠情况。

```
caffeinate -i -t 3600
```

```
man caffeinate
```

## 合盖的条件不同

外接显示器配置需检查电源、外接键鼠和机型支持条件。只有充电器不等于完整配置。不接外屏时，应单独进行短传输测试，比较合盖前后接收量。

## 使用 pika 保持下载

准备 pika 及辅助服务，开始下载后开启 Session；无需保留屏幕则 Monitor OFF，然后合盖。屏幕策略在合盖后应用。结束时关闭 Session。使用电源和通风桌面，不要在密闭包内运行。保护机制或服务故障可能停止会话。

[下载 pika](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.0.13/pika-1.0.13.pkg) · [安装帮助](https://no-sleep-pika.online/install/)

## 确认下载完成

查看应用完成状态、文件大小，以及发布者提供的校验和。使用应用支持的恢复功能。pika 不代替网络恢复或检测下载完成，关闭屏幕也不保证加速。

参考资料

2026 年 10 月 11 日核对 Apple 文档、caffeinate(8) 和 pika 实现。本文由 pika 制作者撰写。

- [Apple · Sleep and wake settings](https://support.apple.com/guide/mac-help/set-sleep-and-wake-settings-mchle41a6ccd/mac)

- [Apple · External displays](https://support.apple.com/en-us/102501)

- `man caffeinate` · macOS System Manager’s Manual

[让 AI 加班一整晚，电费谁来付？ →](https://no-sleep-pika.online/guide/zh-CN/ai-overnight-electricity-cost/)

由 no-sleep-pika 开发者撰写，包含自家应用的比较。

[下载 pika](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.0.13/pika-1.0.13.pkg)[让 Mac 不进入睡眠的方法：合盖模式、caffeinate 与 pika →](https://no-sleep-pika.online/guide/zh-CN/keep-mac-awake/)[Markdown](https://no-sleep-pika.online/guide/zh-CN/macbook-downloads-stop/index.md)
