# Reproducible Infrastructure Experiments

Every experiment starts with a **concept and falsifiable claim**, not a product comparison for its own sake.

## Required record

- Hypothesis and target invariant
- Baseline, treatment and controlled variables
- Fixed repository SHA, tool/model/Harness versions, OS and hardware
- Workload, concurrency, sample size, warm/cold cache and spend cap
- Commands/scripts, raw evidence and artifact hashes
- P50/P95, failure rate, consistency checks and total cost
- Validity limitations and threats to generalization

Use [experiment template](../templates/experiment.md). Put experiments under `experiments/<id>/`; don't commit private records, secrets or large raw files. Link externally stored artifacts with checksums.

## Candidate experiments

1. Workspace density vs full clone, mirror+worktree and partial clone.
2. Revision-pinned remote search under local uncommitted overlays.
3. Durable agent failure injection after an externally completed tool action.
4. Incremental CI selection with measured missed regressions.
5. Concurrent merge integration vs serial queue under a fixed risk policy.

**Status:** planned experiments, not completed benchmark results.
