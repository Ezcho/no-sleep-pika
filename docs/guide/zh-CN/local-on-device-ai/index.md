Source: https://no-sleep-pika.online/guide/zh-CN/local-on-device-ai/
Language: zh-CN

MAC GUIDE · 2026-10-22

# Claude Code 也是本地 AI 吗？用 Llama、Qwen 理解端侧 AI

应用装在 Mac 上，不代表模型也在 Mac 上计算。分清工具、模型与运行位置。

概念图：左侧在设备内计算，右侧连接远程服务器。

## 安装位置不等于计算位置

Claude Code 在终端里读写文件，并不证明答案全部在 Mac 内生成。本地工具也可能把内容发给远程模型。请分别看你使用的工具、计算答案的模型和计算地点。

## 本地 AI 与端侧 AI

本地 AI 通常指在自己管理的电脑或附近服务器上运行模型；端侧 AI 强调在当前设备自身计算。家里的独立服务器不是 Mac 本机。生成回答的计算叫推理，与训练不同；开始使用本地模型不必从头训练它。不同产品的用语可能略有差异。

## 工具与模型不是一回事

Claude Code 是处理文件与命令的工作工具。Llama、Qwen 是包含不同大小和用途的模型系列。Ollama 用于运行或连接模型，其文档说明了 Claude Code 的本地和云端连接方式。不是所有模型都支持同样的工具功能；表格比较的是角色，不是能力排名。

工具与模型不是一回事
| 名称 | 角色 | 检查项
| Claude Code | 处理文件与命令的工具 | 模型提供方和连接地址
| Llama · Qwen | 模型系列 | 本地还是服务器运行
| Ollama | 模型运行与连接软件 | 所选模型的运行位置

## 本地运行会改变什么？

提前准备模型与软件后，本地推理可能离线运行，但网页搜索、远程服务与依赖下载仍需要网络。

模型大小、压缩方式和一次处理的对话量影响内存与速度。本地不一定更快。不调用外部推理服务时可以避免那部分按请求收费，但硬件、电力和维护仍有成本。

本地处理输入不等于整个应用从不上传。同步、日志、扩展和联网工具需要单独检查。

## 三个检查步骤

第一，看模型和连接地址。Llama 或 Qwen 也可能由远程服务提供，Ollama 同时支持本地与云端。

第二，区分联网功能。完成准备且没有重要任务时，可断网尝试生成一个短的新回答；这不证明平时完全没有数据传输。

第三，看设置和文档。Ollama 可关闭其云端模型和网页搜索，但不会代替你阻断其他应用的网络。先用非敏感短文测试速度与质量。

## pika 的作用

Mac 本地工作可能因睡眠中断或延迟，独立运行的远程任务则不同。pika 不运行模型，也不会把云端 AI 变成本地 AI，而是在需要时保持 Mac 唤醒。确认辅助服务、打开 Session 并短暂合盖测试，连接电源，放在通风桌面，完成后关闭 Session。

[下载 pika](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.0.13/pika-1.0.13.pkg) · [安装帮助](https://no-sleep-pika.online/install/)

来源与范围

pika 制作者于2026年10月22日核对官方资料撰写。这是入门说明，不是所有模型或 Mac 的实测对比；兼容性可能随版本变化。

- [Anthropic · Claude Code overview](https://code.claude.com/docs/en/overview)

- [Ollama · Claude Code integration](https://docs.ollama.com/integrations/claude-code)

- [Ollama · Local-only mode and data](https://docs.ollama.com/faq)

- [Qwen · Run locally with Ollama](https://qwen.readthedocs.io/en/latest/run_locally/ollama.html)

- [Meta · Llama models](https://github.com/meta-llama/llama-models)

由 no-sleep-pika 开发者撰写，包含自家应用的比较。

[下载 pika](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.0.13/pika-1.0.13.pkg)[让 Mac 不进入睡眠的方法：合盖模式、caffeinate 与 pika →](https://no-sleep-pika.online/guide/zh-CN/keep-mac-awake/)[Markdown](https://no-sleep-pika.online/guide/zh-CN/local-on-device-ai/index.md)
