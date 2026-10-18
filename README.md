# AI Frontier Research

**Infrastructure and engineering research for reliable AI-powered software production.**

This repository asks a systems question before studying any company, model, or agent product:

> What must change in engineering infrastructure when AI agents become major producers and maintainers of software?

The objective is **reliable, verifiable, secure, maintainable delivery**, not more generated code, tool calls, or pull requests.

## Research model: concept first, implementations second

```text
Engineering concept and constraint
    → failure modes and invariants
    → competing architectural approaches
    → evidence from real systems
    → reproducible experiments
    → synthesis, decisions, and open questions
```

Anthropic, OpenAI, OpenClaw, OpenCode, DeepSeek Harness, and other systems are **case studies and sources of evidence**, not the organizing principle of this knowledge base. A domain may cite multiple vendors; a single article may inform several domains.

## Infrastructure domains

| Domain | Core problem |
| --- | --- |
| [Context and repository intelligence](domains/context-and-retrieval.md) | Find the correct code at the correct revision without materializing everything. |
| [Durable agent execution](domains/durable-execution.md) | Recover long-running work across model, process, network, and sandbox failures. |
| [Source control and workspaces](domains/source-control.md) | Support concurrent agents without clone storms, state drift, or unsafe merges. |
| [Orchestration and coordination](domains/orchestration.md) | Schedule dependent work, manage bounded concurrency, and preserve ownership. |
| [Verification and evidence](domains/verification.md) | Prove which change was tested under which environment and policy. |
| [Delivery and release](domains/delivery.md) | Integrate, deploy, observe, and recover without making speed the only goal. |
| [Security and governance](domains/security.md) | Contain agent capabilities, secrets, external effects, and malicious inputs. |
| [Evaluation and economics](domains/evaluation.md) | Measure correct deliveries, failure recovery, attention, and total cost. |

Start with the [research framework](docs/RESEARCH_FRAMEWORK.md), [methodology](docs/METHODOLOGY.md), [metrics](docs/METRICS.md), and [roadmap](docs/ROADMAP.md).

## Publication research and frontier monitoring

- **[Latest monthly review: Anthropic and OpenAI (Sep 18–Oct 18, 2026)](observations/2026-09-18_to_2026-10-18.md)**
- [Anthropic original-linked article notes and technical interpretation](observations/anthropic/2026-09-18_to_2026-10-18.md)
- [OpenAI original-linked article notes and technical interpretation](observations/openai/2026-09-18_to_2026-10-18.md)
- [Primary source registry](docs/SOURCE_REGISTRY.md)
- [Open-source project catalog](projects/README.md)
- [Reproducible experiments](experiments/README.md)
- [Earlier article case studies](studies/2026-10/agentic-delivery-bottlenecks.md)

**The research unit is the engineering concept**, not the company, model or blog post. Dated publication reviews are supporting evidence, not the repository taxonomy.

## Working principles

1. **Problem before vendor** — frame constraints and alternatives before surveying implementations.
2. **Evidence before belief** — distinguish confirmed disclosures, code inspection, inference, hypotheses, and unknowns.
3. **Versions matter** — tie observations to date, artifact, source revision, and execution environment.
4. **Failure paths matter** — reliability includes retry, recovery, permission boundaries, and semantic regressions.
5. **End-to-end value matters** — prefer verified deliveries per unit cost over PR count.
6. **English throughout** — repository content, titles, templates, CI messages, and GitHub research artifacts are in English.

Use [AGENTS.md](AGENTS.md) for contributor instructions. Research updates go through an Issue, evidence-based changes, a reviewable PR, and CI.

_Research baseline: 2026-10-18. Monthly digests are curated, scoped snapshots of first-party publications, not an exhaustive index of every corporate announcement._
