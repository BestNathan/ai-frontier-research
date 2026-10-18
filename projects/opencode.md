# OpenCode — Project Profile

- **官方仓库**：https://github.com/anomalyco/opencode
- **观察日期**：2026-10-18
- **状态**：README 初查，待固定 SHA 审计

## Verified（官方 README 描述）

OpenCode 是开源 Coding Agent，提供 Build（执行开发）与 Plan（偏只读分析）等 Agent 模式，并描述可处理多步任务的 Subagent。

这些是公开功能描述，不能据此推断具体的权限继承、Session 一致性或恢复机制。

## 研究问题

- Session、Message、Tool Call 和 Agent 如何持久化？
- Plan/Build 权限切换是否在 Tool 层强制约束？
- Subagent 是否有独立上下文、预算和错误隔离？
- 文件定位、LSP、Git、Worktree 与远程工具如何协调？
- 长时间/跨设备运行时，如何处理恢复和授权？

## 下一步

- [ ] 固定 SHA 与源码入口
- [ ] 跟踪一次从 Prompt 到 Tool 的执行路径
- [ ] 验证跨 Agent 的状态和权限边界
- [ ] 与 Codex/DSH 进行同口径比较
