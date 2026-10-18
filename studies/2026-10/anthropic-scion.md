# Case Note: Anthropic Scion

- **Observed:** 2026-10-18
- **Original publication:** 2026-10-13 (updated Oct 15)
- **Source:** https://www.anthropic.com/engineering/redesigning-source-control
- **Primary concept:** [Agent-scale source control](../../domains/source-control.md)
- **Type:** vendor engineering disclosure; not an independent benchmark

## Engineering problem

Frequent short-lived agent and CI sessions repeatedly need immutable code, metadata, diffs and checkouts, while concurrent commits contend for shared refs.

## Verified (as reported by Anthropic)

- Anthropic reported internal monorepo merges increased from approximately 2,500/day in May 2026 to over 30,000/day in September, with roughly 25 million CI checkouts/day.
- After attempting shallow/sparse/partial clone and Git mirror approaches, it migrated its internal monorepo to the client/server Scion version-control system.
- Scion uses content-addressed objects, multiple cache layers, incremental changesets and server-side operations on source-control metadata.
- It decouples creating immutable changesets from atomically changing shared branch references. Related systems include Antique code review, code search and IAM.
- Infrastructure performance claims in the blog are vendor-reported and workload-specific.

## Inferred engineering implications

A common immutable object cache is scalable independently of mutable workspace state. Shared branch-ref mutation is a different coordination problem from creating commits. As checkout costs shrink, review, test selection and integration become increasingly visible bottlenecks.

## Unknown

The public Claude Code GitHub integration is **not proven** to use Scion. The article does not fully describe its Code Search index, local overlay semantics, or agent task coordination for simultaneous edits.

## Alternatives / tests

Compare (a) per-agent clone, (b) shared bare Git mirror with isolated worktrees, (c) partial clone with sparse materialization, and (d) a remote object service prototype. Fix SHA and workload, report cold/hot startup P95, network and disk, conflicts and consistency errors.

## Related

[Recent Anthropic digest](../../observations/anthropic/2026-09-18_to_2026-10-18.md), [CI verification](../../domains/verification.md).
