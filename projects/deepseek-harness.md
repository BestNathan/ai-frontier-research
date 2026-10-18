# DeepSeek Harness Implementation Observation

- **Repository:** https://github.com/deepseek-ai/deepseek-harness
- **Documentation:** https://deepseek-harness.github.io/deepseek-harness/
- **Observed:** 2026-10-18
- **Status:** README-level observations; pinned-source audit pending
- **Concepts:** [execution](../domains/durable-execution.md), [security](../domains/security.md), [orchestration](../domains/orchestration.md)

## Verified (project description)

DeepSeek Harness publicly describes an everything-is-a-plugin architecture based on Cordis. It warns that the developer preview can include breaking changes.

## Research questions

What are the stable host/plugin protocols and lifecycle hooks? How are dependencies, tool permissions, state ownership and failures scoped? What is the observable event sequence for a tool call?

## Inferred

Uniform plugin abstraction can improve modularity but increases the importance of versioned contracts and dependency validation.

## Next audit

Pin SHA, trace plugin initialization and disposal, instrument a tool invocation and inject plugin failure/upgrade incompatibility.
