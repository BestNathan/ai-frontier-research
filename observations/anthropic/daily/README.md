# Anthropic / Claude Frontier Engineering Research

This index displays the curated, date-stamped evidence intakes from the
[daily scheduled research task](../../../docs/CLAUDE_RESOURCES_WATCH.md).
The repository's main organization remains [engineering domains](../../../domains/README.md),
rather than vendor-specific news.

## Latest research

| Observation date | Publication coverage | Topics | Research |
| --- | --- | --- | --- |
| 2026-11-17 | 2026-11-16 (new technical article) | Commit-bound verification evidence, protected review policies, E2E/property/differential tests, diff-triggered reliability checks | [Verification evidence and falsifiable experiment](2026-11-17.md) |
| 2026-11-16 | 2026-04-10 and 2026-09-23 (curated backfill) | Model-adaptive tool interfaces, progressive disclosure and agent clarification; measured performance optimization, lab-to-field calibration and CI ratchets | [Two technical analyses and falsifiable experiments](2026-11-16.md) |
| 2026-11-15 | 2026-06-02–2026-11-06 (curated backfill) | Risk-weighted code review and review convergence; dynamic task-specific harnesses; uncertainty-aware scientific model search | [Three technical analyses with experiments](2026-11-15.md) |
| 2026-11-14 | 2026-10-08–2026-11-13 | Always-on event inbox/outbox; safety eval design; binary formal verification; subagent consolidation; reliable automations | [Five new technical analyses and verification plans](2026-11-14.md) |
| 2026-11-13 | 2026-11-02–2026-11-12 | Agent memory; Message threads; 1,000-agent isolation and coordination; self-hosted Managed Agents; zkML proof of inference | [Five evidence-backed technical analyses](2026-11-13.md) |

## Review requirements

- Treat vendor metrics as author-reported, never independently replicated.
- Record publication dates separately from observation dates.
- Start with engineering invariants, failure models and competing designs.
- Each entry links to its original article and separates Verified, Inferred,
  Hypothesis and Unknown.
- Do not create duplicate daily entries when no new original source is found.
- Update this index in the same PR as each new intake.
- Keep older snapshots unchanged so source claims can be audited over time.

The automated daily task reports its result in ChatGPT and writes source-linked
English research through GitHub branches/PRs. GitHub review and CI remain
necessary; a reported discovery is not the same as a merged study.

## Earlier observations

- [Initial curated Claude Resources intake (2026-10-22)](../weekly/2026-10-22.md)
- [September–October 2026 Anthropic publication review](../2026-09-18_to_2026-10-18.md)
