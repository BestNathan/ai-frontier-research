# Research Roadmap

The plan is structured around **infrastructure capabilities and unresolved system invariants**, not a company's publication schedule.

## Phase 0 — Establish the ontology and evidence process

- [x] Define the delivery north star and research methodology.
- [x] Establish infrastructure domain briefs and linked company observations.
- [x] Convert repository content and contribution workflow to English.
- [x] Add first Anthropic/OpenAI recent-publication landscape snapshot.
- [ ] Pin representative open-source implementations to specific revisions.
- [ ] Develop repeatable source tracking with review before digest updates.

## Phase 1 — Infrastructure required for concurrent agents

- [ ] Version-correct code discovery across central indexes and local changes.
- [ ] Workspaces using shared Git objects, separate writers, and bounded disk/network cost.
- [ ] Event-backed durable runtime with explicit effect reconciliation on replay.
- [ ] Multi-agent leases, task ownership, backpressure, and dependencies.

## Phase 2 — Reliable software integration

- [ ] Incremental build/test selection without uncontrolled false negatives.
- [ ] Immutable provenance for exact SHA, test definition, dependency and environment.
- [ ] Risk-based review policy with quantified error escape.
- [ ] Merge concurrency, semantic regression, and post-merge validation.

## Phase 3 — Sustained production operation

- [ ] Canary, rollback, failure detection, and change attribution.
- [ ] Agent/tool security controls and active monitoring.
- [ ] Verified delivery cost, human-attention cost, and long-term maintenance drift.

## Decision policy

Priority follows measured bottlenecks. No deployment decision follows solely from an Anthropic, OpenAI, or open-source article; validate in our own target workload.
