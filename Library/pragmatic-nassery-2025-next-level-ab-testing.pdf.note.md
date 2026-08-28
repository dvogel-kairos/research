# Next-Level A/B Testing

author: Leemay Nassery
publisher: Pragmatic Bookshelf
edition date: 2025-06-09 (from PDF CreationDate)
pages: 220
placed: 2026-08-28
original filename: next-level-ab-testing_P1_0.pdf

## Completeness

Complete. 220 pages. The `_P1_0` suffix is a download-tool artifact.

## Currency

2025. The most current of the three sources placed on 2026-08-28.

## Trust tier

**Secondary. Practitioner book.** Usable for SHOULD, not as sole basis for a
MUST NOT.

## Proposed tags, and this one is a genuine judgement call

proposed_stage: 3, 8, 9
proposed_azure_components: Azure Monitor / Log Analytics

**A/B testing is not Stage 7 testing, and the naming collision is a trap.** Stage
7 in `Standards/registers/taxonomy.md` governs test strategy, automation and
formal acceptance criteria: verifying a system behaves as specified. A/B testing
verifies nothing about specified behaviour. It is a controlled experiment on live
users to discover which of two specified behaviours is preferable. That is
ideation input (Stage 3), it runs through the release mechanism (Stage 8), and it
operates continuously against production (Stage 9).

Tagging this Stage 7 because both activities are called testing would put an
experimentation source inside a conformance and verification series, and would
also collide it with STD 003 Part 12. Recommend against.

## Series fit

**No fit among the thirteen proposed series.** KAIROS-QA is the one that would
attract it by name, and per the reasoning above that would be the wrong home.
Nothing in the thirteen covers product experimentation. This is the second of
three sources placed on 2026-08-28 that falls outside the series taxonomy, which
is itself a finding about the taxonomy's coverage rather than about the sources.
