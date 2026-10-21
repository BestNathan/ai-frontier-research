# Verification, Incremental CI and Evidence Provenance

## Concept

Establish a machine-verifiable connection between an intended requirement, exact code revision, executable check, observed environment and result, **without running an unnecessarily expensive full suite on every agent-authored change**.

## System boundary and invariants

Separate the **workflow trigger**, **test selection decision**, **execution**, and **result ingestion / projection**. Reducing the number of triggered workflows is a different optimization from choosing tests within a workflow.

1. **Evidence identity:** source SHA (including merge SHA when applicable), test definition/version, dependency lock/configuration, environment fingerprint, selection policy revision, observation time and result.
2. **Policy floor:** selected tests must include mandatory security, smoke, contract and release-risk gates; agents cannot bypass policy by modifying their own workflows.
3. **History freshness:** selector decisions must expose which ingested results and dependency graph revision they were based on. Incomplete, stale or unavailable history must trigger a conservative widening or a blocked gate.
4. **Ingestion integrity:** every accepted CI result is materialized or explicitly reconciled; duplicate and out-of-order updates must not silently corrupt history.
5. **Auditability:** test exclusions must be explainable and reproducible against the exact revision and policy. A passing check against PR head does not automatically validate the final integrated merge SHA.

## Competing architectures

| Approach | Benefit | Main limitation |
| --- | --- | --- |
| Full suite per change | Simple, broad detection | Agent-scale CI fan-out, queue pressure and cost |
| Path / dependency impact | Cheap, deterministic selection | Generated/config/runtime coupling and graph staleness |
| Historical test impact analysis | Uses observed relevance and failure history | Feedback-loop lag and risk of selector false negatives |
| Stateful, per-package listener shards | Parallel ingestion while retaining package order | Hot shards, memory/state relocation and restart lag |
| Stateless listeners + shared journal + projected test history | Scale result ingestion separately from selector reads | Persistence, replay, ordering and materialization lag must be engineered |
| Risk-aware hybrid selector | Static and historical signals plus invariant tests | Higher policy complexity and need for independent full-suite controls |

These are design options, not an assertion that any one implementation guarantees correctness.

## Triggering versus selecting

- Documentation-only changes ordinarily need inexpensive document checks, not automatic E2E; executable docs, generated artifacts or config-affecting changes require further classification.
- Implementation changes need selected unit/integration tests and shared invariant checks.
- API/protocol/schema changes expand contract and dependent-package testing.
- Workflow, selector, test-harness and policy changes require protected review and special validation; path-based exclusion of CI files is unsafe.
- Pre-merge and post-merge checkpoints may differ; cached evidence must be reevaluated when code, environment or policy fingerprints change.

A selector recommendation is **not a merge authorization**. Approval remains bound to independent trust and risk policy.

## Failure model and fallback

False-negative selection, history backlog, missed result events, stale dependency graphs, flaky or widespread-failing tests, duplicate/out-of-order callbacks, journal/store crashes, test-definition changes, forged results and stale evidence.

Instrument ingress vs applied counts; oldest pending event age; journal offsets and replay; decision watermark; missing-event rate; fallback activations; false negatives against known regressions. When freshness/completeness cannot be demonstrated, **widen tests or fail closed according to risk tier**, not silently mark checks unnecessary.

## Evaluation

Compare fixed-SHA baselines on P50/P95 verification lead time, selection lag, backlog drain rate, missed known regressions, flaky failures, percentage of impacted tests selected, reproducibility, human triage and **compute/storage cost per verified delivery**. Fault-inject crashes, restarts, duplicates, reordering and selector staleness under 1× / 10× / 25× traffic.

A vendor-published performance claim is not a controlled benchmark. Run periodic broader suites and attribute any discovered missed regression to the selection policy that excluded it.

## Evidence and open questions

- [Agent-scale test impact analysis study](../studies/2026-10/agent-scale-test-impact-analysis.md) — Anthropic's 2026-09-14 first-party report on listener bottlenecks, journal-based redesign, freshness risks, costs, and a proposed reproducible experiment. The report does not disclose durability guarantees or test-selection false-negative rates.
- [OpenAI Harness Engineering study](../studies/2026-10/openai-harness-engineering.md) — enforceable architecture constraints and checks.
- [Anthropic source control study](../studies/2026-10/anthropic-scion.md) — source-control throughput and bottleneck migration.
- [Reliable delivery](delivery.md) and [measurement definitions](../docs/METRICS.md).

**Research tracking:** [Issue #12 — Trustworthy incremental CI at agent scale](https://github.com/BestNathan/ai-frontier-research/issues/12).
