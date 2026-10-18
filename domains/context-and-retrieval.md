# Context and Repository Intelligence

## Concept

Provide an agent with **the minimal correct context** for a task, even when repositories, indexes, and in-flight local modifications are distributed.

## Invariants and competing designs

- Search and read must identify the code revision; local uncommitted changes require explicit overlay semantics.
- Index freshness must be measurable. A matching path in a new main commit may not exist in the agent's workspace.
- Options: local grep/LSP after checkout, remote path/symbol/content index, staged repository materialization, hybrid remote coarse search plus local fine search.
- Avoid mistaking a remote GitHub MCP tool adapter for the underlying search/index service.

## Failure cases

Stale results, symbol rename, ignored/generated files, untracked local edits, missing context, excessive download and token usage.

## Measurements

Recall@K, time to correct symbol, downloaded bytes, token use, index lag, revision mismatch rate.

## Evidence to examine

[Anthropic technical publication index](../observations/anthropic/2026-09-18_to_2026-10-18.md), [OpenAI observations](../observations/openai/2026-09-18_to_2026-10-18.md), [implementation catalog](../projects/README.md).

## Hypotheses

Hybrid remote search with revision-pinned file retrieval and local overlays can reduce I/O without degrading locate accuracy. Reproduce it with a cross-revision search suite and injected stale indexes.
