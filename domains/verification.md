# Verification, Incremental CI and Evidence Provenance

## Concept

Establish a machine-verifiable connection between an intended requirement, exact code revision, executable check, observed environment and result.

## Invariants

Evidence identity includes code SHA, test definition/version, dependency lock/configuration, environment fingerprint, tool revision, time and result. A passing check against PR head is not automatically proof of the merge SHA.

## Competing approaches

Run all tests; change-impact test selection; reusable build artifacts; reusable E2E environments; isolated validation runner; post-merge verification. Selection saves cost but may miss dependencies.

## Failure cases

False-negative test selection, flakes, test artifact reuse after configuration drift, forged results, stale environment, incomplete coverage, human over-trust.

## Evaluation

P50/P95 total verification time, false-negative rate, selected-test coverage, reproducibility, environment preparation cost, trustworthy evidence acceptance.

## Evidence

[OpenAI Harness Engineering study](../studies/2026-10/openai-harness-engineering.md), [Anthropic source control study](../studies/2026-10/anthropic-scion.md).
