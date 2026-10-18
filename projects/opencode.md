# OpenCode Implementation Observation

- **Repository:** https://github.com/anomalyco/opencode
- **Observed:** 2026-10-18
- **Status:** README-level observations; source-code audit pending
- **Concepts:** [context](../domains/context-and-retrieval.md), [execution](../domains/durable-execution.md), [security](../domains/security.md)

## Verified (project description)

The project documents Build and Plan modes and supporting agent workflows. This observation does not establish the enforcement implementation.

## Research questions

Are Plan/Build tool permissions enforced by a shared policy layer? How are sessions, tools and subagents persisted? What is the behavior under worktree changes or tool failures?

## Inferred

Agent mode names do not by themselves guarantee isolation or safe read-only execution.

## Next audit

Pin a release SHA and examine one plan-mode forbidden write, one tool failure and one subagent lifecycle end-to-end.
