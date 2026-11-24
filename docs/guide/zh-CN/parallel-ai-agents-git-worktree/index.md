Source: https://no-sleep-pika.online/guide/zh-CN/parallel-ai-agents-git-worktree/
Language: zh-CN

MAC GUIDE · 2026-11-24

# 两个 AI 同时改同一份文件？先把工作文件夹分开

用 Git worktree 为每个 AI 准备独立的工作文件夹，再检查修改、逐一合并，避免未完成的工作混在一起。

## 同一个文件夹为什么容易冲突

让一个 AI 改界面、另一个写测试，如果都在同一文件夹里，它们仍会读写同一批文件。创建两个分支名不会让这个文件夹自动拥有两套文件。在这里切换分支，也会改变另一个 AI 正在使用的文件。

Git worktree 可以为同一仓库增加工作文件夹。各文件夹有自己的分支和检出文件，但共享仓库历史。它能分开进行中的修改，却不能保证以后合并时没有冲突。

- 1 分开文件夹

- 2 分配任务

- 3 检查修改

- 4 逐一整合

## 先确认提交起点

在现有 Git 项目中运行下面的命令。本例要求至少已有一次提交，HEAD 指向提交起点。输出为空表示没有报告修改或未跟踪文件；被忽略的文件仍可能存在。

如果出现文件列表，先检查内容，只提交确实需要的修改，或选择已有提交作为起点。不要盲目添加整个文件夹，以免混入密钥或无关修改。新文件夹从 HEAD 开始，不会带上未提交的编辑。

```
git status --short
```

## 创建两个工作文件夹

在原项目运行这两条命令，会在旁边创建工作文件夹，以及 ai-ui 和 ai-tests 分支。分支名和目标路径都必须未被占用；已有同名项目时换一个名字，不要强行覆盖。

已安装的依赖、被忽略的 .env 和本地设置不会全部自动复制。按项目说明准备，只提供任务需要的凭据。如果同时启动开发服务器，应使用不同端口。worktree 不是安全沙箱：有权限的工具仍可访问其他文件夹。

```
git worktree add -b ai-ui ../project-ai-ui HEAD
git worktree add -b ai-tests ../project-ai-tests HEAD
```

## 明确文件夹和任务范围

分别在 project-ai-ui 和 project-ai-tests 启动 AI，明确告诉它绝对路径和有限的任务范围。例如“只改界面组件”和“为现有行为添加测试，不修改应用代码”。

依赖清单、锁文件等容易共同修改的文件要指定负责人。确实需要编辑同一文件时，按顺序处理。要求 AI 报告修改的文件、执行的检查和未完成事项。

## 检查后逐一整合

在每个工作文件夹执行下面三条命令。status 列出修改和未跟踪文件；diff 显示已跟踪文件尚未暂存的修改；diff --cached 显示已暂存的修改。未跟踪的新文件不出现在这些 diff 中，需要另行打开检查。

运行项目所需检查，将确认后的修改提交到各自分支。再回到原项目，在目标分支上逐一审查和整合。worktree 不会自动合并结果。遇到重叠修改，解决冲突并检查整合后的结果，再处理下一个分支。

```
git status --short
git diff
git diff --cached
```

## pika 能帮什么忙

pika 可根据会话设置和安全保护条件，帮助本地 AI 工作时让 Mac 保持唤醒。它不会分配任务、合并分支或解决冲突。pika 1.3 的 QR 连接显示 Mac 状态和获准的电源控制，不显示 AI 输出或准确完成百分比。是否完成仍应检查 AI 结果和项目测试。

[下载 pika](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.3.0/pika-1.3.0.pkg) · [安装帮助](https://no-sleep-pika.online/install/)

资料与适用范围

本文由 no-sleep-pika 开发者依据 Git 官方文档编写，适用于一般 AI 工作流程，不假定某款 AI 的具体功能或权限。也请遵守项目的贡献规范和机密信息管理要求。

- [Git · git-worktree](https://git-scm.com/docs/git-worktree)

- [Git · git-status](https://git-scm.com/docs/git-status)

- [Git · git-diff](https://git-scm.com/docs/git-diff)

由 no-sleep-pika 开发者撰写，包含自家应用的比较。

[让 Mac 不进入睡眠的方法：合盖模式、caffeinate 与 pika →](https://no-sleep-pika.online/guide/zh-CN/keep-mac-awake/)[Markdown](https://no-sleep-pika.online/guide/zh-CN/parallel-ai-agents-git-worktree/index.md)
