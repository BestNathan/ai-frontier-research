# Research Roadmap

研究目标：把 Agent Coding 的瓶颈研究延伸至完整的软件工程交付链；任务以 GitHub Issue 追踪，按可验证产物收敛，不预设技术答案。

## Phase 0 — 研究底座

- [x] 研究框架与北极星
- [x] 官方来源与项目雷达
- [x] 研究 / 实验模板
- [x] Scion、Managed Agents、Harness Engineering、Symphony 首批笔记
- [ ] 定期跟踪并复核资料变化

## Phase 1 — Runtime / Context / Source Control

- [ ] Git Mirror、Worktree、Lazy Fetch 在 10/100/1000 Agent 下的尾延迟和资源实验
- [ ] 版本化 Code Search：远程索引 + 未提交本地文件的一致性
- [ ] Durable Session、工具副作用去重、Sandbox 故障恢复
- [ ] Agent Session/Run/Issue/Workspace 关系和资源调度

## Phase 2 — CI / Review / Merge

- [ ] 以 Diff/依赖分析选择测试的遗漏率与速度
- [ ] E2E 环境复用及绑定 SHA/配置/环境指纹的可信证据
- [ ] 按风险分层的 Review 与合并门禁
- [ ] Merge Queue vs Post-merge Verification 的吞吐/正确性对比

## Phase 3 — Release / Economics

- [ ] 发布灰度、回滚与可观测驱动的归因
- [ ] 人工介入分钟数、真实缺陷逃逸率、单位稳定交付成本
- [ ] Agent 团队与长期自治任务的安全和维护质量

## 选择研究顺序

先找到真实瓶颈并量化，再提出设计约束，最后验证性能和正确性；不得将别人内部的效果直接预测为我们的收益。
