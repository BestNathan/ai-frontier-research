# Anthropic Managed Agents — Session、Harness、Sandbox 解耦

- **研究时间**：2026-10-18
- **状态**：一手文章解读；未独立复验
- **来源**：https://www.anthropic.com/engineering/managed-agents （2026-04-08）

## Verified：官方披露

初期把 Session、Harness、Sandbox 放在同一个容器中，造成生命周期绑定：进程失效时难以恢复，也需要为每个会话提前准备容器与仓库。

Anthropic 将三个概念抽象出来：**Session** 为持久化追加式事件日志，**Harness** 为模型和工具调用控制循环，**Sandbox** 为通过执行接口按需创建/替换的环境。Session 的持续性不依赖 Harness 或 Sandbox 进程。

文章报告 TTFT 的 P50 下降约 60%，P95 下降超过 90%。这是作者的实测披露，不是本仓库复验结果。

## Inferred

- 持久事件不等于恰好执行一次外部副作用；必须为 Tool Call 设计稳定 ID、幂等恢复和最终状态核验。
- 长任务恢复需要分开处理 Agent 思考历史、文件系统状态、外部 GitHub/CI 状态。
- 隔离环境可以延迟分配、故障后替换；凭证不应随任务复制到不可信 Sandbox。

## 实验

强制终止 Harness、Sandbox，注入断网和工具超时，比较单容器与分离式 Session 的 P95 首响应、已完成工具数、重复副作用及完全恢复比例。

## 尚不明确

跨多个同时活动 Sandbox 的一致性与全部 Tool 副作用语义，原文未公开完整协议。
