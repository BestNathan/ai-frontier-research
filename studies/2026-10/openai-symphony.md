# OpenAI Symphony — Issue 作为长时间运行 Agent 的控制平面

- **研究时间**：2026-10-18
- **状态**：一手资料解读；源码实现待固定 SHA 审计
- **来源**：https://openai.com/index/open-source-codex-orchestration-symphony/ （2026-04-27）
- **代码**：https://github.com/openai/symphony

## Verified：官方披露

- Symphony 把 Linear 一类 Issue Tracker 升级为 Agent 控制平面。
- 每个活动 Issue 对应独立 Workspace 和 Agent；长期运行的监督服务观察任务并继续推进。
- Agent 不限于写代码，还能处理 PR、Review 意见、CI、Rebase 和失败重试。
- 开源规范以 SPEC 为核心，附有 Elixir 参考实现；它是参考设计而非 OpenAI 宣称会长期维护的独立产品。
- 官方称部分团队上线后三周已成功合并 PR 数提升 500%；这是特定团队观察，不是通用 Benchmark。

## 关键概念

Issue 是**目标**，Run 是**一次执行**，Session 是**交互/事件历史**，Workspace 是**工作资源**，PR/Commit 是**中间产物**。一个 Issue 可以跨多个 PR 和执行，不能用「PR merged」替代「需求已验收」。

## Inferred

需要一个 Supervisor 负责调度、租约、依赖与恢复，同时 Harness 独立执行步骤；运行证据绑定 Issue、Run、SHA、CI 和 Acceptance。

## 未解决的问题

高并发关联需求的全局冲突、幂等 Webhook、资源配额与长期成本；多 Agent 的集成版本验证仍需更严格的量化研究。
