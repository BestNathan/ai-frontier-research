# Agent Security and Governance

## Concept

Treat autonomous agents and their tools as constrained principals whose actions may affect untrusted data, infrastructure, source code and external systems.

## Invariants

Least privilege; credentials kept outside untrusted execution; explicit tool and network capabilities; audit trail for writes; isolation and containment; trusted validation of irreversible actions.

## Threat model

Prompt injection, confused deputy, permission escalation, unintended network effects, malicious dependencies, long-running credential leakage, output laundering, false security findings.

## Mechanisms and open choices

Sandbox containment vs fine-grained policy engines; ephemeral credentials; out-of-band authorization; monitoring of external effects; automated incident response; security review at merge and deploy.

## Research signals

[Anthropic recent observations](../observations/anthropic/2026-09-18_to_2026-10-18.md) include unintended model actions and an open-source vulnerability scanner. These reveal both autonomous defensive capacity and the need to contain agents. [OpenAI observations](../observations/openai/2026-09-18_to_2026-10-18.md) include Codex Security Cloud as a product announcement.

## Experiments

Simulate forbidden tool use, stale grants and duplicate writes in controlled environments, record false blocks vs successful containment. Do not run real exploitation outside explicit authorization.
