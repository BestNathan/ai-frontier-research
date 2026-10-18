# Integration, Release and Operational Feedback

## Concept

Safely advance rapidly produced changes from isolated branches into shared production states, with explicit risk and recovery policy.

## Design questions

- Which changes require pre-merge blocking checks and human approval?
- Which low-risk checks can run post-merge or pre-deploy?
- How are merge-base drift, dependent changes and semantic conflicts discovered?
- What is the canary, rollback and incident attribution strategy?

## Mechanisms

Risk-based review policy; bounded merge concurrency; post-merge acceptance; pre-deploy verification; progressive rollout; automated detection with human escalation.

## Invariants

An integrated artifact is identifiable. Policy cannot be bypassed by agents. Rollback/forward-fix is justified with observed evidence. High-risk changes use stronger gates.

## Failure modes

Batch regression, test-pass before merge but failure after merge, unbounded hotfix loop, irreversible migration, incorrect culprit attribution, monitoring blind spots.

## Sources and metrics

[Anthropic observations](../observations/anthropic/2026-09-18_to_2026-10-18.md), [OpenAI observations](../observations/openai/2026-09-18_to_2026-10-18.md), [metrics](../docs/METRICS.md).
