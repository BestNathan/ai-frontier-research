# Case Note: Anthropic Managed Agents

- **Observed:** 2026-10-18
- **Source:** https://www.anthropic.com/engineering/managed-agents (2026-04-08)
- **Primary concept:** [Durable agent execution](../../domains/durable-execution.md)
- **Type:** vendor engineering disclosure

## Engineering problem

Long-lived agent sessions should persist independently of the process performing reasoning and the sandbox in which a tool operates.

## Verified (as reported by Anthropic)

Anthropic described separating **Session** (persistent append-only event history), **Harness** (model/tool execution loop), and **Sandbox** (execution environment). A sandbox no longer has to be allocated before useful reasoning begins. The authors reported lower time-to-first-token: roughly 60% P50 and more than 90% P95 reductions in their observed setting.

## Inferred

Event durability supports replay, but replay safety requires stable tool identities and reconciliation with the external world. Sandbox loss should not imply loss of a session; isolation and credential boundaries matter as much as performance.

## Unknown

The article does not establish exactly-once external tool effects or full distributed concurrency semantics for all managed-agent deployments.

## Tests

Kill the harness after an externally successful write but before receipt persistence; kill the sandbox while the harness survives; inject timeout and duplicate wake-ups. Measure replay correctness, duplicate writes, recovery time and cost.
