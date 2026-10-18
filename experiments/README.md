# Experiments — 可复验工程实验

目录规范：每项实验独立存放于 experiments/<experiment-id>/，包含 README、脚本、配置、指标/结果（或可信 Artifact URL）。

记录实验问题、可证伪假设、实验/对照组、固定仓库 SHA、环境、模型/Harness 版本、并发、预算、冷/热缓存条件、重复次数，以及 P50/P95、错误率、成本和局限。

大体积、敏感数据不能进入 Git；使用脱敏 Artifact 与哈希引用。详细模板见 [Experiment Template](../templates/experiment.md)。

首批计划（尚未有实验结果）：

- git-workspace-concurrency：每 Agent Clone vs Bare Mirror + Worktree
- code-search-version-consistency：远程索引与 Workspace SHA 一致性
- durable-agent-fault-injection：Runner/Harness/Sandbox 失败恢复
- incremental-ci-evidence：基于 SHA + 环境指纹的选测和证据复用

每个实验通过 Issue 确定预算、验收和停止条件，避免无限制地消耗模型与计算资源。
