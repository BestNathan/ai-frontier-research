# Durable Agent Execution

## Concept

Separate persistent work identity and history from transient model calls, harness processes, tools and sandboxes.

## Invariants

- Each run has stable identity and an append-only or otherwise auditable state history.
- Tool calls have durable IDs and explicit lifecycle states.
- External side effects are reconciled after restart; retry alone never guarantees exactly-once execution.
- Sandbox allocation and disposal should not silently erase required execution state.

## Alternatives

Co-located in-memory agent, external session log + restartable harness, durable workflow engine, checkpoint/snapshot plus event log.

## Failure model

Runner crash, lost tool response after successful external write, expired credentials, race between wake-up and checkpoint, stranded sandbox, stale lease.

## Metrics

Successful recoveries, duplicated side effects, P95 resume latency, wasted tool/model cost, lost committed progress.

## Implementation evidence

[Anthropic Managed Agents study](../studies/2026-10/anthropic-managed-agents.md) and [OpenAI observation digest](../observations/openai/2026-09-18_to_2026-10-18.md). Both are sources for the concept, not its definition.
