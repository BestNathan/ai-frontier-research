# AI-native Software Engineering — Research Framework

## 北极星

衡量的不是 Token/代码行数/生成 PR 数，而是「单位时间内以合理成本、低人工干预、可恢复且可验证地交付正确软件变更」。

| 层次 | 研究方向 | 关键问题 |
| --- | --- | --- |
| L0 | Model & Reasoning | 推理策略、可靠性、路由和不确定性 |
| L1 | Context & Agentic Search | 文件定位、符号/语义检索、上下文及版本一致性 |
| L2 | Harness & Tools | Loop、Skills、MCP、工具边界、权限 |
| L3 | Durable Runtime | Session、事件日志、Checkpoint、Waker、Sandbox 替换 |
| L4 | Source Control | Git / Scion、对象缓存、Worktree、提交和冲突 |
| L5 | Orchestration | Issue-centric Workflow、依赖 DAG、多 Agent 调度 |
| L6 | CI & Verification | 增量构建、选测、Unit/E2E、真实验收及可信证据 |
| L7 | Review & Integration | 风险门禁、Review、Merge Queue、Post-merge |
| L8 | Release & Operation | 灰度、回滚、归因、日志/指标/Trace |
| L9 | Evaluation & Economics | 已验证交付率、缺陷逃逸、人工成本、恢复率与总成本 |

## 核心不变量

- 每次读取、搜索、Diff、测试和验收都应绑定可识别的源码 SHA 与环境。
- Agent、Workspace、Run、Issue、PR 是不同身份，不能互相混淆。
- 状态与事件可恢复，外部 Tool 副作用考虑幂等。
- 权限按用户、Agent、Run、工具和风险分层。
- 失败与排队尾延迟必须计量，不只看平均吞吐量。
- 发布安全约束不能因为 Agent 擅长修复而直接跳过。

研究类型：机制拆解、源码审计、项目雷达、横向对比、可复现实验和架构决策。详见 [方法论](METHODOLOGY.md)、[指标](METRICS.md)、[Roadmap](ROADMAP.md)。
