# Cross-System Case Note: Bottleneck Migration in AI-Driven Delivery

- **Observed:** 2026-10-18
- **Source:** See the linked primary notes below.
- **Primary concepts:** [source control](../../domains/source-control.md), [execution](../../domains/durable-execution.md), [verification](../../domains/verification.md), [delivery](../../domains/delivery.md)
- **Status:** synthesis from publications, not independent experimental proof

## Engineering question

As agents reduce implementation time, which physical, correctness and organizational constraints become rate limiters?

## Verified: cited implementation reports

- [Scion](anthropic-scion.md) reports an internal response to SCM checkout and merge throughput limitations.
- [Incremental CI test impact analysis](agent-scale-test-impact-analysis.md) reports Anthropic's response to result-ingestion lag and horizontal scaling of a history-based test selector; its operational metrics are author-reported.
- [Managed Agents](anthropic-managed-agents.md) reports decoupling the session log and sandbox lifecycle.
- [OpenAI Harness Engineering](openai-harness-engineering.md) reports increasing application/test legibility and executable architecture constraints.
- [Symphony](openai-symphony.md) describes persistent issue-directed agent supervision.

## Inferred bottleneck progression

Model output → context retrieval → workspace preparation → version control and merge → build/test selection → review and acceptance → release/monitoring and maintenance.

These can overlap in practice; the path is a hypothesis about shifting relative costs, not a fixed ordering.

## Competing approaches

- Reduce per-run work by caching, lazy materialization and remote APIs.
- Improve throughput with concurrent isolated workspaces and queue-aware integration.
- Improve correctness with immutable evidence, executable requirements and risk-based checks.
- Reduce future drag with continuous maintenance and controlled cleanup agents.

## Hypothesis and measurement

Compare systems on verified deliveries/day and escaped defects, while measuring P95 latency, human effort and total compute cost. Increasing PR count without controlling those outcomes does not establish improved productivity.

## Unknown

No public case note proves that a single end-to-end approach is optimal for all repository sizes and release-risk classes.
