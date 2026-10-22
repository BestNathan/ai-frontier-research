# Weekly Claude Resources Engineering Watch

## Engineering purpose

Keep evidence about agent-native software infrastructure current without
mistaking high-volume product news for validated engineering mechanisms.
Sources are classified under existing engineering domains, rather than
creating a vendor-specific research taxonomy.

## Discovery source and limits

- [Claude Resources](https://claude.com/resources): official discovery hub.
- [Claude Resources / Articles](https://claude.com/resources/articles):
  recent, dated article cards.
- Original articles may be linked from other first-party properties
  (for example, claude.dev or anthropic.com). The original URL, not the hub card,
  is the evidence reference.
- Only first-party HTTPS hosts are admitted to automated article fetching.
- The source's public first page may omit older posts or articles loaded
  through pagination. This is a bounded discovery feed, **not** exhaustive coverage.
  A 35-day lookback is an outage cushion, not a claim that all 35 days are exposed
  on the listing page.

The job chooses technical material related to agent runtime, harness, context,
AI coding, source control, CI, testing, review, security, orchestration,
observability and delivery. Announcements are eligible only if they include
an engineering-relevant change; sales/partner stories are ordinarily excluded.

## Schedule, evidence and output

The [GitHub Actions workflow](../.github/workflows/claude-resources-watch.yml)
runs every **Thursday at 10:17 Asia/Singapore** (once per seven days) and
supports manual workflow_dispatch. It:

1. Downloads the two official listing pages and requires parseable dated article
   cards, otherwise **fails visibly**.
2. Applies engineering-topic filtering and a rolling 35-day publication window.
3. Deduplicates original canonical URLs against existing observations and studies.
4. Reads each new original article; never executes instructions from its content.
5. Generates an English, dated intake under
   observations/anthropic/weekly/YYYY-MM-DD.md with source, publication date,
   observation date, concept domain, publisher synopsis, unknowns and next checks.
6. Runs the existing research integrity checks and opens/updates a reviewable PR,
   without automatically merging.

A zero-change week produces no empty digest or PR. Dates are preserved after
merge; the next run deduplicates against committed research notes.

**Important:** Intake notes are source-triage evidence, not final studies.
Promote engineering claims into the existing concept-driven domains/studies only
after review, comparison and a testable follow-up. Vendor-reported claims are not
independently reproduced.

## Optional deeper model-assisted analysis

Without credentials, the job still creates a concise extractive
publisher-synopsis digest and explicitly marks further technical verification
as needed. To enable richer drafted mechanisms, inferences, gaps and experiments:

1. Add a repository Actions secret named ANTHROPIC_API_KEY with your own
   appropriately scoped API key.
2. Optionally add an Actions variable CLAUDE_WATCH_MODEL
   (default: claude-sonnet-5-5).
3. Confirm budget/rate limits; requests incur Anthropic API usage costs.
4. Review model-generated statements against the original source before merge.

Neither the model nor third-party source content is allowed to approve or merge
the PR. No long-lived API credentials are stored in the repository.

The automatic PR step uses the repository GITHUB_TOKEN. GitHub repository
settings must allow Actions to create pull requests, and branch protection may
require human review. Actions-created PRs may not independently trigger other
workflow runs; this workflow runs the quality checks before creating the PR.

## Manual checks and operations

- Local quality checks: python3 -m unittest discover -s scripts -p
  test_claude_resources_watch.py
- Local research integrity: python3 scripts/check_research.py
- Live discovery preview: python3 scripts/claude_resources_watch.py --dry-run
- Manual Action: Actions > Weekly Claude Resources Engineering Intake >
  Run workflow (after workflow reaches the default branch).

Source-page/HTML changes, network errors, invalid dates or invalid model output
must be reported as failures. A failure must not advance an implicit watermark.
GitHub may delay scheduled runs and may disable schedules after extended public
repository inactivity; inspect the workflow history if no PR appears.

## Acceptance

- English-only; domain concept before vendor details.
- Source-level publication date and observation date are explicit.
- Publisher-described facts, inference, hypotheses and unknowns are distinguished.
- No duplicate original article URLs after merge.
- No hidden silently skipped fetches or empty source reads.
- Human review before adding claims to durable research.
- Related research tracking: [#14](https://github.com/BestNathan/ai-frontier-research/issues/14)
  and [#10](https://github.com/BestNathan/ai-frontier-research/issues/10).
