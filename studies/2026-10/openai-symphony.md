# Case Note: OpenAI Symphony

- **Observed:** 2026-10-18
- **Source:** https://openai.com/index/open-source-codex-orchestration-symphony/ (2026-04-27)
- **Code:** https://github.com/openai/symphony
- **Primary concept:** [Orchestration and coordination](../../domains/orchestration.md)
- **Type:** official engineering article; pinned source-code audit pending

## Engineering problem

When agents can implement work without continuous guidance, human context switching across many active sessions becomes a primary constraint.

## Verified (as reported by OpenAI)

Symphony proposes an issue/project-management control plane and continuously supervised agents, with independent workspaces for active tasks. The authors report agent interactions with PR feedback, CI and merge/rebase processes. The publication offers an open specification and a reference implementation. One reported early team gain in merged PR volume must not be generalized.

## Inferred

Task desired state and execution attempt must have distinct identifiers and lifecycle policies. A PR merged event is not by itself a requirement acceptance result. Durable orchestration needs leases, retries and side-effect reconciliation.

## Unknown

No complete cross-repository global scheduling and semantic-conflict solution can be inferred from the article.

## Research test

Inject duplicate issue events, crashes, stale refs and concurrent PR changes. Measure duplicate assignments, successful recovery and verified end-to-end completion.
