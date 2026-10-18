# Case Note: OpenAI Harness Engineering

- **Observed:** 2026-10-18
- **Source:** https://openai.com/index/harness-engineering/ (2026-02-11)
- **Primary concept:** [Verification](../../domains/verification.md)
- **Type:** vendor engineering disclosure

## Engineering problem

How can an agent produce validated, maintainable changes without relying on a human to constantly reproduce bugs, inspect the UI and run tests?

## Verified (as reported by OpenAI)

OpenAI described a codebase developed through Codex-generated application code, tests, CI, tooling and documentation, reporting approximately 1,500 merged PRs over five months. The project made per-worktree application instances, browser interaction, ephemeral observability stacks and architectural lint rules available to agents. Engineers shifted toward specifying requirements, executable constraints and feedback loops.

## Inferred

An agent's reliability depends heavily on whether requirements and runtime evidence are discoverable and machine-checkable. Architectural guardrails act as compressed repeatable human judgement.

## Unknown / limitations

Results from one internal application do not justify removing blocking CI in high-risk production systems. The article does not demonstrate that all post-merge semantics are universally safe without human review.

## Proposed test

Use a fixed issue set and model budget to compare a normal repository with one exposing architecture checks, application E2E, logs and traces. Track accepted change rate, defect escapes, human time, and repeated repair loops.
