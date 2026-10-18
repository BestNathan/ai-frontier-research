# Agent-Scale Source Control and Workspaces

## Concept

Provide many independently writable workspaces from a shared version graph without an explosion of cloned objects, ref contention or consistency failures.

## Design dimensions

- Data plane: full clone, shared bare mirror, sparse/partial clone, content-addressed remote storage and layered cache.
- Control plane: per-agent changes, immutable revisions, shared-ref updates, merge/rebase, conflict resolution.
- Search interface: revision-pinned tree, history, diff and blame without requiring complete checkout.
- Coordination: local worktree isolation, cross-host cache coherence, branch/commit ownership and merge policy.

## Invariants

Workspaces are private writers. Shared objects are immutable or versioned. Branch-ref changes are atomic. Validation is tied to the **integrated** revision, not just the pre-merge head.

## Failure cases and costs

Clone storms, hot-ref CAS contention, stale mirrors, corrupted shared cache, simultaneous edits, semantic conflicts, inode/disk exhaustion.

## Candidate approaches

Git+bare mirror+worktrees; Git+partial/sparse clone; managed workspace service; Scion-style client/server SCM. Different scales justify different choices.

## Supporting sources

[Anthropic Scion study](../studies/2026-10/anthropic-scion.md), [recent Anthropic observations](../observations/anthropic/2026-09-18_to_2026-10-18.md).

## Experiment

Fix repo SHA and task mix; measure N=10/100/1000 concurrent starts, cold/warm data, P50/P95, memory, disk, network, conflict/retry rates. Confirm whether a cheaper Git-based option is sufficient.
