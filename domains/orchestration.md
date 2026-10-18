# Multi-Agent Orchestration and Coordination

## Concept

Allocate long-running work to agents and resources while preserving task ownership, dependencies and safe concurrency.

## Core distinctions

Issue = desired outcome; task/run = an execution attempt; session = recoverable history; workspace = isolated code environment; commit/PR = output artifacts.

## Invariants

Stable identity, leases with fencing tokens, retry/backoff, bounded budget, idempotent event consumption, dependency transitions and explicit completion criteria.

## Options

Issue-triggered CI; long-lived supervisor; workflow DAG engine; event-driven runtime with wake-up queues; human-led task delegation.

## Failure modes

Duplicate runners, dependency deadlock, out-of-order webhooks, simultaneous incompatible edits, orphaned resources and inconsistent status projections.

## Evidence

[OpenAI Symphony study](../studies/2026-10/openai-symphony.md), [Anthropic recent research digest](../observations/anthropic/2026-09-18_to_2026-10-18.md).

## Measurements

Queue delay, throughput of verified outcomes, blocked time, duplicate assignments, recovery cost, resource utilization.
