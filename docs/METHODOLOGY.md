# Evidence-Based Research Methodology

## Epistemic categories

| Label | Meaning | Required attribution |
| --- | --- | --- |
| Verified | Supported by an identified source or direct reproducible observation | Who said/implemented it, where, and when |
| Inferred | Derived from verified evidence and stated assumptions | Mechanism and plausible counterexample |
| Hypothesis | Testable prediction, not yet substantiated | Experimental falsification plan |
| Unknown | Relevant detail that available evidence cannot resolve | Missing evidence and consequence |

**Vendor-reported** results must not be treated as independently reproduced measurements. For source-code claims, give an immutable commit SHA and relevant files/tests.

## Study workflow

1. **Define the concept:** system boundary, inputs, outputs, user, attacker, and shared state.
2. **Identify invariants:** version consistency, isolation, durability, authorization, evidence trust.
3. **Model failures:** crashes, replay, race, stale cache, lost results, network partitions, semantic regressions.
4. **Identify options:** at least two viable architectures and their operational costs.
5. **Study implementations:** primary documentation and pinned code. Distinguish announcement from deployment and author performance reports.
6. **Design experiments:** fixed code SHA, workload, environment, instrumentation, baseline, repetitions, and resource budget.
7. **Synthesize:** limitations, threats to validity, what is transferable, and which facts would reverse the conclusion.

## Performance comparison checklist

- Baseline and intervention are identical except for controlled changes.
- Report warm and cold cache separately.
- Report P50/P95, throughput, error rate, resource cost, and the denominator.
- Evaluate both **correctness** and **speed**; a shorter test suite may introduce false negatives.
- Capture human intervention and recovery, not just completed PRs or model tokens.
- Maintain raw data, environment fingerprint, and experiment artifacts.

## Source handling

Register publication date and observation date separately. A public article is evidence that its author **reports** a mechanism or result; it does not establish all unpublished internal details. Do not infer that a service deployed for an internal monorepo also runs in every public product.

## Acceptance criteria

- [ ] Concept and failure modes stand independently of any vendor.
- [ ] Primary sources have dates and stable URLs.
- [ ] Verified / Inferred / Hypothesis / Unknown are explicit.
- [ ] Comparable alternatives, scale limits, trust boundaries, and costs are discussed.
- [ ] Reproducibility plan or explicit limitation exists.
- [ ] Review identifies risks of inaccurate conclusions and outdated evidence.

Templates: [domain study](../templates/research.md) and [experiment](../templates/experiment.md).
