# Metrics for Reliable Agent Productivity

## North-star outcome

**Verified Delivery Rate** = accepted requirements completed, integrated, and validated under the stated policy, divided by elapsed time.

A generated pull request, a passing unit test, or a model response is *not* itself a verified delivery.

## Required guardrails

| Metric | Definition |
| --- | --- |
| Change failure rate | Releases causing an incident, rollback, or failed post-release check / total releases |
| Escaped defect rate | Valid defects first identified after delivery / delivered requirements |
| Human intervention | Human triage, rework, approval, and incident minutes / delivered requirement |
| Cost per verified delivery | Attributable tokens, compute, CI, storage, and operations cost / verified delivery |
| Recovery success | Fault injections successfully reconciled without lost state/duplicated effects / injections |
| End-to-end lead time | Ready-to-start requirement → policy-compliant completed delivery |

## Infrastructure metrics

- Context: Recall@K, stale results, bytes fetched, time to correct location.
- Runtime: checkpoint integrity, retry duplicates, durable recovery P50/P95.
- SCM: clone/checkout P50/P95, cache hit, I/O, workspace density, merge conflicts.
- Orchestration: scheduler utilization, queue time, dependency-blocked time, duplicate leases.
- CI: build-cache hit rate, selected-test false-negative rate, flaky failures, evidence re-use validity, inbound-vs-applied result counts, test-history freshness P50/P95, oldest pending result age, selector fallback frequency, journal replay success and cost per verified delivery.
- Review: reviewer cost and missed defects across risk classes.
- Delivery: deployment frequency, change failure rate, MTTR, rollback success.

Results must include workload, source SHA, agent/model configuration, environment fingerprint, date, units, and provenance. Always distinguish authors' measurements from our experiments.
