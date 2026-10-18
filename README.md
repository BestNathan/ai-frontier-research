# AI Frontier Research

> 研究 AI 如何从“会写代码”走向“能够稳定、可验证、可持续地交付真实生产成果”。

本仓库持续跟踪 **Anthropic、OpenAI** 及前沿开源项目（**OpenClaw、OpenCode、DeepSeek Harness / DSH** 等）在 Agent Engineering、Coding Infrastructure 和 AI-native Software Delivery 上的技术进展。重点不在追新闻或展示模型基准成绩，而在于**识别真实瓶颈、研究工程机制、设计可复现实验、沉淀可落地的基础设施演进方案**。

## 核心问题

当 Coding Agent 可以高吞吐地产生代码后，什么限制了真实产出？

```text
需求定义 → 探索/定位 → 规划 → Agent执行 → 版本控制与工作区
                                              ↓
反馈与修复 ← 生产观测 ← 发布与回滚 ← 合并/CI/测试/验收/Review
```

研究对象既包括模型前后的 Context / Tool / Harness，也包括代码生成**下游**的 Source Control、Build、Test、Review、Merge、Release、Observability。我们的终极目标不是最大化 Token 或 PR 数，而是**单位时间内稳定交付经过验证的正确变更**。

## 研究全景

| 研究方向 | 关键问题 |
| --- | --- |
| Agent Harness & Runtime | 长任务如何持久化、恢复、调度，如何分离 Session / Harness / Sandbox？ |
| Context Engineering & Search | 如何在大仓库低成本地定位文件、符号、历史与相关上下文？ |
| Source Control & Workspaces | 大量 Agent 如何共享对象缓存、隔离工作区、按版本提交？ |
| Multi-Agent & Orchestration | 如何按 Issue/目标编排 Agent、限制并发与协调依赖？ |
| CI / Testing / Acceptance | 如何按变更选测、复用环境、保存可信证据、定位 Flaky？ |
| Review / Merge / Release | 如何根据风险配置门禁、减少等待、验证集成后的 SHA、回滚？ |
| Security & Governance | 如何隔离凭证、控制 Tool 权限、抵御提示注入和保护证据？ |
| Evaluation & Economics | 如何衡量正确性、端到端交付周期、人工干预、可靠性与成本？ |

详见 [研究框架](docs/RESEARCH_FRAMEWORK.md) 与 [方法论](docs/METHODOLOGY.md)。

## 从哪里开始

- **研究框架**：[docs/RESEARCH_FRAMEWORK.md](docs/RESEARCH_FRAMEWORK.md)
- **证据和研究规范**：[docs/METHODOLOGY.md](docs/METHODOLOGY.md)
- **主要来源登记**：[docs/SOURCE_REGISTRY.md](docs/SOURCE_REGISTRY.md)
- **技术演进路线**：[docs/ROADMAP.md](docs/ROADMAP.md)
- **指标体系**：[docs/METRICS.md](docs/METRICS.md)
- **起始横向专题**：[Agent-scale 软件交付瓶颈](studies/2026-10/agentic-delivery-bottlenecks.md)
- **项目雷达**：[projects/README.md](projects/README.md)
- **实验目录**：[experiments/README.md](experiments/README.md)

### 起始研究

| 主题 | 研究笔记 |
| --- | --- |
| Anthropic Scion / Antique：Agent 规模下的版本控制 | [阅读](studies/2026-10/anthropic-scion.md) |
| Anthropic Managed Agents：Session/Harness/Sandbox 解耦 | [阅读](studies/2026-10/anthropic-managed-agents.md) |
| OpenAI Harness Engineering：约束、测试与反馈闭环 | [阅读](studies/2026-10/openai-harness-engineering.md) |
| OpenAI Symphony：Issue 驱动长期编排 | [阅读](studies/2026-10/openai-symphony.md) |

## 研究如何推进

1. **发现**：登记一手资料（技术博客、设计文档、源代码、Issue、PR），记录日期、来源及其适用范围。
2. **分析**：分别标注 **事实（Verified）**、**推论（Inferred）**、**假设（Hypothesis）**，不把作者声明当成独立实验结果。
3. **验证**：设计可重复的实验，固定版本/SHA、输入、环境、指标和基线。
4. **沉淀**：产生专题结论、架构不变量、决策记录、可复用基准与实施建议。
5. **更新**：技术演进时增量修订，保留出处、变更时间和被推翻的旧结论。

每项研究使用 GitHub Issue 跟踪，完成的研究报告通过 PR 进入主干。研究结论不是静态“最佳实践”：有新的证据就更新。

## 原则

- **可靠产出优先于生成速度**：重视最终交付质量、可恢复性和人工注意力成本。
- **原始证据优先**：优先官方工程博客、源码与 Commit；没有证据不编造内部实现。
- **问题优先于技术选型**：识别瓶颈，提出可以被证伪的方案和实验。
- **厂商中立**：横向比较 Anthropic/OpenAI/开源实现，不进行未经验证的能力排名。
- **可复现**：实验记录版本、环境、方法、原始结果和限制。
- **风险分级**：高风险变更不能仅因为 Agent 可以快速修复就跳过门禁。

欢迎通过 Issue 追加研究问题；给 AI Agent 的仓库工作说明见 [AGENTS.md](AGENTS.md)。

---
初始研究基线：2026-10-18。文中关于公开产品与技术的判断以各研究笔记的具体来源和日期为准。
