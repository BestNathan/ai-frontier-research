# Metrics for Reliable AI Productivity

## 北极星

**Verified Delivery Rate** = 一定时间内完成质量门禁并集成、经过必要后置验收的需求数量 / 时间。

不能只用 PR 数量、生成代码行数或 Token TPS 表示生产力。

## 守护指标

| 指标 | 口径 |
| --- | --- |
| Change Failure Rate | 已发布变更中导致回滚/事故的比例 |
| Escape Defect Rate | 交付后被发现的真实缺陷 / 已交付需求 |
| Human Intervention | 单个需求的人工判断、救火和协调分钟数 |
| Cost per Verified Delivery | Token + CPU + CI + 存储等 / 成功交付需求 |
| Recovery Success Rate | 注入故障后在约定时限成功恢复且不丢进度的比例 |
| Lead Time | 从需求 Ready 到验证完成、可以使用的时间 |

## 按子系统拆分

- Retrieval：候选文件 Recall@K、搜索版本漂移、检索 P50/P95。
- Runtime：重复工具副作用、Crash 后恢复时间、失败率。
- SCM：冷/热 Checkout、IO、磁盘峰值、锁等待、合并冲突率。
- Orchestration：任务等待、依赖阻塞、Agent 有效利用率。
- CI：构建缓存、选测覆盖/漏检、E2E Flaky、单位变更验证成本。
- Review/Merge：Review 等待、合并吞吐、未经发现回归数量。
- Release：发布耗时、异常发现与回滚成功率。

每个实验结果带任务/Issue、Run、SHA、版本、配置、环境指纹、时间和数据出处，且区分作者报告与本仓库实测。尤其应报告尾延迟，不得仅报告平均值。
