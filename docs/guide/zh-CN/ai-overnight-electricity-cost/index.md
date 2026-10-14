Source: https://no-sleep-pika.online/guide/zh-CN/ai-overnight-electricity-cost/
Language: zh-CN

MAC GUIDE · 2026-10-15

# 让 AI 加班一整晚，电费谁来付？

用假设数据估算 Mac 运行八小时的费用，并区分家庭电费与 AI 服务费。

## 两种不同的账单

云端 AI 的模型计算主要由服务商的服务器完成，但 Mac 上的构建、测试和文件操作仍会耗电。本地模型则也在 Mac 上计算。家庭电费与订阅或 API 费用是两笔账；插座测量不包含数据中心的耗电。

## 八小时要花多少？

平均功率 W × 小时 ÷ 1,000 = kWh，再乘以电价。假设每天八小时、连续三十天、电价为0.20美元/kWh：10W每天0.08kWh、0.016美元，三十天2.4kWh、0.48美元；30W每天0.24kWh、0.048美元，三十天7.2kWh、1.44美元；60W每天0.48kWh、0.096美元，三十天14.4kWh、2.88美元。

这些不是 MacBook 实测数据或当地电价。实际账单受税费、合同与阶梯电价影响。要算相对睡眠状态增加的费用，还需测量并减去同时间的睡眠耗电。

## 充电器功率不是实际耗电

70W充电器不代表电脑一直消耗70W。输出能力与实际耗电不同；充电、显示器和本地任务都会改变负载。关屏节省多少也没有统一数值。

## 测量自己的任务

按说明使用可记录累计kWh的插座电量计。两小时0.06kWh对应平均30W；只有负载相近时，才能推算八小时0.24kWh。尽量测完整任务，记录电池电量。独立供电的屏幕和扩展坞不在充电器读数内。

## pika 能省电吗？

pika用于维持可能因系统睡眠中断的任务，不是电量计或AI费用优化器。持续唤醒可能增加耗电。确认辅助服务，打开Session，不需维持显示时关闭Monitor，短暂合盖验证任务进度。完成后关闭Session；审批等待、网络错误和任务完成判断仍需另行处理。

[下载 pika](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.0.13/pika-1.0.13.pkg) · [安装帮助](https://no-sleep-pika.online/install/)

## 离开前做三个决定

先定义完成条件和停止方法，再按服务支持情况设置用量上限或提醒。不要把已有订阅重复算作新增费用。接通电源，放在通风的硬质桌面上，不要在包内或被褥里运行。

假设与来源

由pika制作者撰写。公式参考Virginia Cooperative Extension，摆放建议参考Apple。功率与美元单价均为示例假设。

- [Virginia Cooperative Extension · Estimating appliance energy use](https://ext.vt.edu/content/pubs_ext_vt_edu/en/2901/2901-9014/2901-9014.html)

- [Apple · Mac operating temperatures](https://support.apple.com/en-us/102336)

由 no-sleep-pika 开发者撰写，包含自家应用的比较。

[下载 pika](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.0.13/pika-1.0.13.pkg)[让 Mac 不进入睡眠的方法：合盖模式、caffeinate 与 pika →](https://no-sleep-pika.online/guide/zh-CN/keep-mac-awake/)[Markdown](https://no-sleep-pika.online/guide/zh-CN/ai-overnight-electricity-cost/index.md)
