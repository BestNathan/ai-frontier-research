# OpenClaw — Project Profile

- **官方仓库**：https://github.com/openclaw/openclaw
- **观察日期**：2026-10-18
- **状态**：待固定 SHA 深入审计

## 研究问题

- Gateway / Channel / Agent / Tools / Skills 如何界定职责、生命周期和配置？
- 会话恢复、进程重启、工具调用失败与外部副作用如何处理？
- 扩展入口是插件、Skills 还是自定义工具？权限和凭证怎样传递？
- 多用户、多 Agent 并行时如何管理隔离、预算和观测？

## 当前证据

已确认官方开源仓库存在，尚未完成对应固定 Commit SHA 的代码级验证；内部实现细节暂不作确定判断。

## 后续验收

- [ ] 固定代码 SHA、画出关键类型和调用链
- [ ] 完整追踪一个 Tool Call（权限 → 执行 → 返回 → 持久化）
- [ ] 故障注入观察 Session/Tool 恢复及重复副作用
- [ ] 对照 OpenCode/DSH 的接口和隔离不变量
