Source: https://no-sleep-pika.online/guide/zh-CN/mac-locked-ai-running/
Language: zh-CN

MAC GUIDE · 2026-10-05

# Mac 锁屏后，Claude Code 和 Codex 还会继续工作吗？

区分锁屏、关闭显示器和系统睡眠，检查本地 AI 任务、网络与合盖设置。

## 锁屏不等于停止

看到密码界面不代表任务结束。Mac 保持唤醒、应用运行且所需连接正常时，一般后台命令可以继续。操作屏幕或身份验证可能需要解锁。显示器关闭与系统睡眠不同，锁屏后仍可能自动睡眠。无需关闭密码保护。

## 本地还是云端任务

Codex CLI 在本机处理文件和命令，明确交给 Codex Cloud 的任务在独立云环境执行。Claude Code Remote Control 连接的仍是本地会话。恢复连接不等于睡眠期间任务一直运行。pika 不会把本地工作迁移到云端。

[Codex CLI](https://learn.chatgpt.com/docs/codex/cli) · [Codex Cloud](https://learn.chatgpt.com/docs/cloud) · [Claude Code Remote Control](https://code.claude.com/docs/en/remote-control)

## 先排查这些原因

先看最后一条消息是否等待批准、提问、完成或报错，再检查应用、Wi-Fi、VPN 和登录。下方只读命令查看电源请求与近期事件。电源请求的存在或低 CPU 占用都不能证明 AI 任务的进度。

```
pmset -g assertions
```

```
pmset -g log | tail -n 60
```

## 三分钟检查

打开盖子运行下方循环，保留终端，锁屏约三分钟后查看时间间隔。用 Ctrl+C 结束。明显间断应对照电源日志；同时检查 AI 日志和文件修改时间。这只验证简单本地进程，合盖情况应另行测试。

```
while true; do date "+%Y-%m-%d %H:%M:%S"; sleep 10; done
```

## 合盖时使用 pika

安装 pika 及辅助服务后开启 Session；不需保持屏幕时关闭 Monitor，再合盖。屏幕策略在合盖后应用。关闭 Session 会释放防睡眠并显示 Monitor OFF，不会立即关闭屏幕。接通电源、保持通风，不要放入封闭包内运行。电池、温度保护或辅助服务故障可能中止会话。

[下载 pika](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.0.13/pika-1.0.13.pkg) · [安装帮助](https://no-sleep-pika.online/install/)

## 常见问题

Monitor OFF 不是结束 AI 任务。tmux 不阻止系统睡眠；caffeinate 不解决网络故障或批准等待。pika MCP 状态也不代表所有 Claude Code、Codex 任务都在推进。

资料与范围

依据 2026 年 10 月 5 日官方文档与 pika 实现编写。本文由 pika 制作者提供，不是所有硬件的连续运行保证。

- [Apple · Sleep and wake settings](https://support.apple.com/guide/mac-help/set-sleep-and-wake-settings-mchle41a6ccd/mac)

- [OpenAI · Codex CLI](https://learn.chatgpt.com/docs/codex/cli)

- [OpenAI · Codex Cloud](https://learn.chatgpt.com/docs/cloud)

- [Anthropic · Claude Code Remote Control](https://code.claude.com/docs/en/remote-control)

[让 AI 加班一整晚，电费谁来付？ →](https://no-sleep-pika.online/guide/zh-CN/ai-overnight-electricity-cost/)

[MacBook 下载停止：关屏、睡眠和合盖有什么不同？ →](https://no-sleep-pika.online/guide/zh-CN/macbook-downloads-stop/)

由 no-sleep-pika 开发者撰写，包含自家应用的比较。

[下载 pika](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.0.13/pika-1.0.13.pkg)[让 Mac 不进入睡眠的方法：合盖模式、caffeinate 与 pika →](https://no-sleep-pika.online/guide/zh-CN/keep-mac-awake/)[Markdown](https://no-sleep-pika.online/guide/zh-CN/mac-locked-ai-running/index.md)
