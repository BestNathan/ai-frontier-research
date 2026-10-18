# Research Framework: AI-Native Software Infrastructure

## North star

We study how to deliver **verified, secure, recoverable, maintainable software changes** at high agent throughput and bounded human attention and infrastructure cost.

## System boundary

```text
Intent and specification
       ↓
Context / retrieval / reasoning
       ↓
Durable agent runtime + tools
       ↓
Workspaces / source control / collaboration
       ↓
Build / test / acceptance / provenance
       ↓
Review / integration / release / operations
       ↖──────── evidence and incident feedback ────────↗
```

This chain is a model of engineering constraints, not a prescription that all systems must execute sequentially.

## Domain-first map

| Domain | Invariant | Bottleneck or failure |
| --- | --- | --- |
| Context and retrieval | Results match workspace revision and local changes | Wrong file, stale index, excess download |
| Durable execution | Session and external effects can be reconciled after failure | Lost progress, duplicated writes |
| Source control | Isolated writers and consistent shared references | Clone storms, locks, conflicts |
| Orchestration | Task dependencies, leases, and bounded resources hold | Oversubscription, duplicated tasks |
| Verification | Evidence is attributable to exact source/config/environment | Stale tests, false acceptance |
| Integration and release | Risk gates remain enforced under throughput | Unsafe merges, unbounded rollback |
| Security | Least-privilege capabilities are maintained end to end | Tool escape, leaked credentials |
| Evaluation | Correct delivery and total cost are measured | Benchmark gaming, hidden human effort |

Explore these in [domains](../domains/README.md).

## Method for each concept

1. **Define** it without referencing a vendor.
2. **Specify** its threat model, invariants, consistency semantics, and scale threshold.
3. **Compare** plausible implementations and where they fail.
4. **Observe** how Anthropic, OpenAI, and open-source projects approach it.
5. **Verify** claims against source code, public disclosures, or reproducible experiments.
6. **Evaluate** correct delivery, tail latency, cost, failure rate, and human intervention.
7. **Decide** what is generalizable; document unknowns.

Company reports are [observations](../observations/README.md), never the primary ontology.

## Research artifact types

- **Domain brief:** stable concepts, system model, failure cases, competing designs.
- **Implementation observation:** dated vendor/project evidence with confidence and source.
- **Experiment:** reproducible inputs, fixed versions, results, counterexamples.
- **Decision record:** objective constraints and why one approach was adopted or rejected.

See [methodology](METHODOLOGY.md) and [evaluation metrics](METRICS.md).
