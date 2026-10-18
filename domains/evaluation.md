# Evaluation and Engineering Economics

## Concept

Judge an AI production system on outcome correctness, reproducibility, safety, sustainability and all-in cost.

## Counter-metrics

Generated tokens/second, lines of code and opened PRs may rise while defect escape, human attention and operations costs worsen.

## Measurement model

Require Verified Delivery Rate and guardrails: change failure rate, lead time P50/P95, recovery success, repeat side effects, reviewer effort, build/test cost, incident MTTR and long-term maintenance drift.

## Method

Controlled workloads; fixed base SHA; matched resource limits; instrument every stage from task accepted to validated integrated output. Make the source of each number explicit (vendor report vs independent reproduction).

## Signals to monitor

[Anthropic productivity research](../observations/anthropic/2026-09-18_to_2026-10-18.md), [OpenAI maintenance research](../observations/openai/2026-09-18_to_2026-10-18.md), [metrics definitions](../docs/METRICS.md).
