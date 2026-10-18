# From Coding to Delivery — AI 生产力瓶颈迁移

- **研究时间**：2026-10-18
- **状态**：跨来源初步综合结论，待验证
- **来源**：本目录 Scion、Managed Agents、Harness Engineering、Symphony 四篇附原始官方链接的研究笔记

## 核心观察（Verified）

- **Anthropic**：大规模 Agent 引发仓库对象获取、历史计算、Review 和合并吞吐瓶颈，内部 Scion/Antique 等属于为该负载做出的基础设施改造。
- **OpenAI**：Codex-first 开发实践推动把不变量、自动化测试、观测与真实应用验收编码进仓库；Symphony 减少人类同时管理多 Agent 的切换成本。
- **Anthropic Managed Agents**：Session、Harness 与 Sandbox 解耦，降低恢复与环境准备耦合。

## 对照矩阵

| 瓶颈 | Anthropic | OpenAI | 研究空白 |
| --- | --- | --- | --- |
| 仓库获取 | Scion 按需读取、分层缓存 | 独立工作区、Agent 工具 | Git 优化何时到极限？ |
| 长任务 | Durable Session + 可替换 Sandbox | Issue 持续监督 | exactly-once 副作用与跨宿主恢复 |
| 正确性反馈 | Post-merge/Pre-deploy 强化 | Linter、不变量、E2E、CI | 增量选测误漏率和回归逃逸 |
| Review/Merge | Antique、风险控制 | 自动 Review/CI 修复 | 每个门禁的最优等待与安全平衡 |
| 发布 | Pre-deploy 披露 | 发布工具/工程闭环 | Canary/rollback 大规模自动化的公开证据不足 |

## Inferred：未来的架构方向

1. Agent 产生 Changeset 与集成/验证是两个不同的平面，不能一 PR 一全量 CI 地无限伸缩。
2. 搜索、构建、测试和验收的缓存必须绑定不可变代码版本及关键环境指纹。
3. 通过可信 Evidence Graph 将 Issue → Agent Run → Workspace → SHA → CI/E2E → Merge → Release 关联。
4. 对不同风险的变更使用不同门禁；后置测试可以增加吞吐，但不是删除安全验证的理由。

## 实验候选（Hypothesis）

- 共享对象缓存可以显著降低大量短 Agent Run 的检出成本。
- 基于变更影响图的选测可以降低测试成本，但需测 False Negative。
- 已经验证的 SHA/环境组合可以复用证据，但更改环境后不得直接继承。
- 在合理风险场景中，部分并发合并 + 快速 Post-merge 检测能提高吞吐，前提是回归逃逸不增加。

**结论**：真正的北极星是经验证且可恢复的真实交付，不是模型生成速度。下一步优先实验 Source/Runtime 和增量 CI / Evidence。
