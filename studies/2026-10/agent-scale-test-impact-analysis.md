# Case Note: Trustworthy Incremental Test Selection at Agent Scale

- **Research issue:** [#12 — Trustworthy incremental CI at agent scale](https://github.com/BestNathan/ai-frontier-research/issues/12)
- **Observed:** 2026-10-21
- **Primary source:** [Agentic coding is straining CI. Here's how we scaled test impact analysis at Anthropic](https://claude.com/blog/agentic-coding-is-straining-ci-heres-how-we-scaled-test-impact-analysis-at-anthropic)
- **Source author / publication:** Sachin Malhotra, Anthropic, 2026-09-14
- **Type:** first-party engineering disclosure; operational figures are vendor-reported, **not** independently reproduced
- **Primary domain:** [Verification and incremental CI](../../domains/verification.md)
- **Related domains:** [Delivery](../../domains/delivery.md), [Evaluation](../../domains/evaluation.md)
- **Scope:** CI test-selection control plane and evidence ingestion, not a claim about all Anthropic products or its full CI implementation

## Engineering concept and system boundary

When autonomous agents produce more, smaller changes at all hours, running every test for every change can exhaust CI capacity. Incremental verification must reduce redundant work **without turning incomplete or stale observations into unjustified confidence**.

Four distinct functions should be modeled rather than conflated:

1. **Trigger policy:** which changes create which kinds of verification obligations.
2. **Test selector:** choose relevant tests using dependency relevance, history and risk policy.
3. **Executor:** run chosen tests against an identified artifact and environment.
4. **Evidence ingester/projector:** capture and aggregate results for future selection and audit.

The stateful feedback loop is: CI executions → observed result events → test history → selection decision → CI executions. A successful workflow run and a fresh, complete test-selection history are separate properties.

## Invariants and failure modes

| Invariant (research requirement) | Failure mode | Required control to test |
| --- | --- | --- |
| Each gating result identifies source SHA, test definition/version, environment, policy and execution time | Reused result validates the wrong revision | Immutable evidence identity and freshness checks |
| Every accepted result event is eventually either materialized or explicitly rejected/reconciled | Listener restarts, queue loss, partial ingestion | Ingress-vs-applied counters, replay, dead-letter visibility |
| Out-of-order and repeated events cannot corrupt the decision model | Duplicate callbacks, retry races and late results | Idempotency keys, per-key ordering/monotonic offsets |
| Selecting fewer tests never silently disables mandatory risk/security checks | Misclassified path-only changes or stale dependency graph | Risk-tier floor, test-policy version, conservative fallback |
| Loss of selection-state freshness produces a visible degraded mode | Flaky tests or fixed/new tests misrepresented | Lag and history-age thresholds, broader testing or blocked gate |
| Agents cannot silently weaken CI policy via their own changes | Untrusted workflow edits or selector configuration | Protected policy ownership and review of CI-control changes |

These are proposed engineering requirements, **not claims that Anthropic implements all of them**.

## Candidate architectures and trade-offs

| Approach | Strength | Scaling / correctness risk |
| --- | --- | --- |
| All tests on every change | Simple and broad coverage | Cost, queue contention and slow agent iteration |
| Static dependency/path selection | Cheap and explainable with a maintained graph | Dynamic dependencies, workflow/config edits and cross-module effects can be missed |
| Stateful history-based selector with a single listener | Test-result feedback can avoid repeated irrelevant failures | Memory and ingress throughput tied to one process; stale state during backlog |
| Package-sharded stateful listeners | Per-package order with parallelism | Hot shards, worker memory and rebalancing remain constraints |
| Stateless listeners + shared journal + materialized history | Independent ingestion scale and fast selector reads | Extra infrastructure; journal semantics, durability, replay and projection lag must be defined |
| **Recommended hypothesis:** hybrid dependency + history + mandatory risk floors | Cost reduction with explicit correctness fallback | More policy and evaluation complexity |

## Verified — what Anthropic publicly reports

The following points are **verified as claims present in the primary article**, not independent measurements:

- Its engineers were shipping approximately **8× as much code per quarter** as in the 2021–2025 comparison period; it attributes **80% of authored code** to Claude. Test count increased **10×**, while CI job volume increased **25× over six months**. These are different denominators and must not be multiplied together.
- The deterministic test impact analysis service used package relevance and previous test results. A **listener** ingested CI outcomes and a **selector** read their history to pick tests for opened PRs.
- The original design maintained per-test running history inside **one process / writer**. The article says **20 minutes** of listener lag could mean tens of thousands of test updates unavailable to the selector. It describes stale results causing irrelevant reds, flaky failures and delayed recognition of fixed/new tests.
- Three successive mitigation steps were insufficient: **doubling cores** (about **70 days** before another fix), **sharding state and workers by package** (about **29 days**), and **daily restarts** (less than a day of relief). The article reports memory-limit pressure and multi-hour lag during the restart period.
- During extended lag, **some CI job results were not recorded by the listener**. The author explicitly clarifies that this **does not mean the CI tests never ran or untested code was deployed**. The documented failure was degraded *future test-selection data*, not proven bypass of execution gates.
- The redesigned service puts a journal in an **in-memory data store**. Any listener worker can append a result and retain no in-process test history; a separate small consumer rolls journal entries into per-test history **every few seconds**; the selector reads that materialization.
- Anthropic reports the redesign is **more expensive to run**, but horizontally scalable and easier to profile. A single engineer completed it in **three weeks**, compared with the author's counterfactual estimate of roughly a quarter under earlier development conditions; the latter is not a controlled productivity benchmark.
- Its post-cutover backlog chart is reported as effectively flat after tuning, with no independently published throughput distribution, failure rate, or cost breakdown.
- The author recommends planning for **10–20×** initial headroom where budgets permit and suggests operating under a **25× / two-quarter** growth scenario. These are recommendations from experience, **not** a measured universal forecast.

**Primary-source trace:** [architecture, patches, redesign and retrospective](https://claude.com/blog/agentic-coding-is-straining-ci-heres-how-we-scaled-test-impact-analysis-at-anthropic) (2026-09-14). No Anthropic internal repository SHA or system source code is available for code-level verification.

## Inferred — transferable systems implications

1. **Ingestion completeness and CI execution correctness are separate.** A check may run while its result fails to enter the selector's feedback history. Therefore an ordinary green PR badge does not prove the test-selection control plane is healthy.
2. **Decouple cheap parallel ingestion from sequential projection.** Per-key order belongs where test history is materialized, not necessarily at every ingress worker. The journal becomes the synchronization boundary.
3. **Stale history is a correctness issue, not only an operations issue.** The selector needs a freshness watermark and an explicit degraded policy so it does not silently exclude recently added or affected tests.
4. **Agent-driven small PRs amplify fixed per-PR overhead.** Deduplication, event-aware triggers, batchable infrastructure and cheap targeted checks matter independently of raw test-run parallelism.
5. **An in-memory journal is not by itself a durability guarantee.** Whether events survive process or store loss depends on persistence, acknowledgment, replay, replication and retention details not supplied in the article.
6. **Optimizing CI trigger volume and optimizing test selection are complementary.** A policy that skips E2E on a documentation-only PR solves different waste from the impact-analysis service; neither substitutes for post-merge verification.

These are architectural inferences, not descriptions of unpublished Anthropic code.

## Unknown — evidence gaps

- Named data-store technology, journal persistence and retention, replica/failover model, acknowledgment boundary and replay guarantees.
- Whether repeated test-result events are idempotent and how out-of-order results, partial writes, dropped callbacks, re-sharding and crash recovery work.
- Freshness thresholds or failure behavior when the selector cannot trust current history; any use of full-suite or periodic control runs.
- Exact selection algorithm, dependency graph coverage, recall, missed-regression/false-negative rate, treatment of test definitions changed in a PR, and test classification.
- Before/after cost, latency P50/P95, workers, CPU/memory, storage expenditure, absolute job rate and operator burden.
- Evidence-binding protocols for merged SHAs and acceptance environments; authorization model for agents changing CI policy.
- Whether this internal service is available in Claude Code or used by external organizations; the article does not establish either.

## Proposed test-trigger and selection policy (not Anthropic disclosure)

| Change class | Event/trigger recommendation | Test-selection rule | Safe fallback |
| --- | --- | --- | --- |
| Docs / non-executable metadata only | Cheap lint/link/integrity gate | No heavyweight E2E by default | Run more if generated docs/config have executable effects |
| Localized implementation changes | Unit + impacted integration | Dependency + history + invariant smoke tests | Expand to package-level or full suite on missing/stale metadata |
| Public API, protocol, schema, shared library | Broader integration and contract checks | Dependents and cross-boundary tests | Full relevant suite on ambiguous reachability |
| CI workflow, test harness, selector or security-policy edits | Dedicated workflow validation and protected review | CI self-tests, test-discovery, policy integrity | Block or isolate sensitive mutations until verified |
| Pre-merge / post-merge integration state | Gate against exact commit; re-verify merge SHA where required | Risk-tier policy plus impact selection | Fail closed or run widened suite if evidence no longer matches |

Only trusted policy owners should change the classification and fallback. An agent may propose a narrower plan, but must not self-authorize an exemption from mandatory gates.

## Hypothesis and falsifiable experiment

**Hypothesis:** At bursty agent-scale job loads, stateless ingress + bounded journal projection + a guarded hybrid selector can improve P95 selection freshness and throughput over a singleton while retaining mandatory test coverage and bounded cost.

- **Fixed inputs:** choose and pin a repository commit, a stable dependency graph, test definitions, representative recorded CI-result streams, selector policy version and executor environment fingerprint. Record all revisions before running; no unpinned open-source code claims.
- **Baselines:** (A) all-tests policy, (B) static dependency selection, (C) monolithic history ingester, (D) distributed journal + projected history + risk floors.
- **Load:** steady 1× baseline; 10× and 25× synthetic arrivals; bursts, overnight traffic and many small PRs. Keep the test/workload mix identical across candidates.
- **Fault injection:** duplicate and out-of-order results, listener kill/restart, consumer pause, journal truncation/store restart, delayed events, stale dependency graph and new/renamed tests.
- **Instrumentation:** ingress and applied counts, lowest unmaterialized offset / age, selector decision watermark, backlog P50/P95/max, first-result-to-visible lag, queue drain time, missing/duplicate events, false negatives on an injected known-regression corpus, full-suite controls, compute and storage cost per verified delivery.
- **Safety:** never merge changes on a synthetic selector-only signal. Require exact-SHA checks and mandatory risk floors; degraded-state alerts must be visible to both humans and agents.
- **Success/falsification:** sustained backlog drain at 25× without silent event loss; zero missed *known seeded regressions* in the fixed corpus; correct fallback during every injected data-quality fault; and improved time-to-decision per unit cost relative to baselines. This does **not** establish a universal zero false-negative rate.

## Synthesis and next actions

**Decision for investigation:** prioritize event-aware CI triggers and observable, failure-safe test selection ahead of brute-force workflow fan-out. Prototype shared-journal ingestion only once actual lag and cost measurements justify extra stateful infrastructure.

1. Collect a pinned CI workload and build a baseline trigger/selector decision log.
2. Define the result-event ID, acknowledgment/replay protocol, history watermark and fallback contract.
3. Implement load/restart/reorder fault tests before selecting a journal backend or asserting scalability.
4. Compare full-test controls against selected tests for missed regressions and compute per verified delivery.
5. Revisit the findings if Anthropic publishes code, selector quality metrics or failure-recovery semantics.

**Change log:** 2026-10-21 — first concept-led study based on the 2026-09-14 first-party engineering report. This report predates the existing Sep 18–Oct 18 monthly publication snapshot and is deliberately recorded as a standalone case note.
