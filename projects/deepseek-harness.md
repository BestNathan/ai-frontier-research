# DeepSeek Harness (DSH) — Project Profile

- **官方仓库**：https://github.com/deepseek-ai/deepseek-harness
- **文档**：https://deepseek-harness.github.io/deepseek-harness/
- **观察日期**：2026-10-18
- **状态**：README 初查，待固定 SHA 审计

## Verified（官方 README 描述）

DeepSeek AI 将 DSH 描述为「Everything is a Plugin」的开源 Harness，基于 Cordis；目前仍是 Developer Preview，明确提醒可能出现破坏性兼容变更。

## 研究问题

- 插件依赖注入、加载顺序、生命周期、Scope 与错误隔离如何设计？
- Agent Loop、工具、UI、Session 和存储是否都通过统一插件抽象连接？
- 插件版本、扩展协议和 Handler 的不变量是否可自动化校验？
- 不可信插件与宿主之间如何管理权限和资源预算？
- 同一条 Tool Call 的事件流与错误链路如何追踪？

## 下一步

- [ ] 固定 SHA，建立 Cordis/Plugin 依赖和生命周期图
- [ ] 跟踪一条完整 Tool Call 和错误路径
- [ ] 验证插件崩溃/破坏性升级的恢复行为
- [ ] 对照 OpenClaw / OpenCode 的扩展边界
