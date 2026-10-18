# Infrastructure Domains

**These concepts, not vendors or articles, are the primary organization of the research.**

| Problem domain | Key invariant | Brief |
| --- | --- | --- |
| Context and retrieval | Search corresponds to a consistent source view | [Context](context-and-retrieval.md) |
| Durable execution | Recover and reconcile agent work after crashes | [Execution](durable-execution.md) |
| Source control | Concurrent writers don't share mutable working state | [Source control](source-control.md) |
| Orchestration | Single accountable owner, bounded concurrent resources | [Orchestration](orchestration.md) |
| Verification | Evidence proves a specific artifact and environment | [Verification](verification.md) |
| Delivery | Integration, rollout, and rollback honor risk policy | [Delivery](delivery.md) |
| Security | Least-privilege and observable side effects | [Security](security.md) |
| Evaluation | Measure verified outcomes and total cost | [Evaluation](evaluation.md) |

Each brief is a **problem map and set of candidate mechanisms**. Linked vendor observations are examples, not conclusions. Start from a constraint, then search for implementation evidence and tests.
