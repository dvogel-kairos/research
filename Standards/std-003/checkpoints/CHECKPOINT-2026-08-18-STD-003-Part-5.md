# Session checkpoint: KAIROS STD 003 Part 5

**Date.** 2026-08-18.
**Session intent as stated.** Author Part 5, decision engine, covering the selection of one outcome from inputs, distinct from constraint evaluation.
**Deliverable state.** Complete and delivered as `KAIROS-STD-003-Part-5-v1.0-Proposed.md`. Version 1.0.0, status Proposed, not approved and not effective.

## What was produced

One document, 51,525 words, 433 clauses across the thirteen mandated sections. Validation clean: every identifier unique, in ascending document order, contiguous from 1 within its section. Every internal clause citation resolves, and all twenty cross part clause citations were verified against the delivered text of Parts 1 through 4.

305 clauses are MUST, 122 MUST NOT, 6 SHOULD. Section 3 carries 118, section 6 carries 47, section 12 carries 42.

## Rehydration performed

Read section 12.5 of all four prior parts. Six reciprocal declarations were outstanding and all six are discharged in sections 12.1 through 12.4.

`Part 2` handed this part the largest inheritance in the standard so far: every hit policy, every default and fallback, every precedence and priority, and every aggregation of verdicts. Sections 3.9, 3.10 and 3.11 specify all of them as artifacts rather than behaviours.

## Positions taken that a reviewer may want to overturn

The four parts of a decision are separated: candidate set with declared completeness, eligibility obtained from `Part 2`, criterion, selection. The conflation that does the damage is eligibility with preference, and clause P5-3.8 forbids exclusion by a threshold on a criterion score.

Nine closed criterion kinds, each declaring whether ties, cycles and incomparability are possible. `DOMINANCE_ONLY` is the only kind that never resolves an incomparability and almost no engine offers it.

Four undecidable outcomes as first class members: tie, incomparability, intransitivity, and eligibility indeterminate. There is no residual fallback, per clause P5-6.13.

**The First and Rule order hit policies are refused.** Priority and Output order reference a list of output values, which is a governable artifact; First and Rule order reference the sequence of rows, which is a physical property of a table's layout. First is the most used hit policy in practice, so this is the most contestable position in the part and 13.3 records the cost honestly.

Every criterion parameter requires a justification and a justification basis, with `UNJUSTIFIED` admissible and countable. Weights are the policy.

Margin computed per criterion kind, with marginality against a declared threshold, and for weighted criteria the smallest weight perturbation that would reverse the outcome.

Human involvement and decisive automation are separately recorded. A record showing a person approved the outcome does not establish that the decision was not automated.

## Research findings

**DMN hit policy structure confirmed from four independent implementation accounts.** Seven policies; Priority and Output order order output values, First and Rule order order rules. That distinction is the whole basis of section 3.9 and the specification text was not obtained, so 13.1 flags it as the most load bearing unverified claim.

**XACML 3.0 Plus Errata 01, 12 July 2017**, contains the best normative treatment found anywhere of combining several results into one: twelve named algorithms in a normative appendix, plus extended indeterminate values that record what a result could have been. Its only one applicable algorithm returns indeterminate where more than one policy applies, which is the precedent for this part's refusal to arbitrate.

**CJEU Case C-634/21, December 2023**, supplies the test this part adopts for decisive automation: whether the final decision was decisively based on a preceding automated determination, even where the person had formal and substantive decision making power. This is a substantive test rather than a formal one and it makes a review control measurable.

**A live regulatory uncertainty I could not resolve.** The EU AI Act's high risk obligations, including Article 14 human oversight, were scheduled to apply from 2 August 2026, sixteen days before the date of this part. A Commission Digital Omnibus package was reported as proposing to condition them on harmonised standards, with deadlines no later than December 2027 or August 2028. Whether that was enacted could not be established. Clause P5-10.3 requires an implementation to establish the position itself.

Arrow's impossibility theorem and the Condorcet paradox are cited as literature, on the same basis Part 2 cites Kleene and Łukasiewicz. Arrow supplies the reason every aggregation rule embeds a choice not derivable from the inputs, which is this part's definition of a criterion.

## Open, carried forward

13.2: no bridge is specified between a criterion's statement and its computation. `Part 2` has worked examples and `Part 4` has classification instances; this part has nothing, and that is an omission rather than a position. The remedy is structurally identical and cheap.

13.3: the refusal of rule order selection, with the honest cost that an ordered fall through table is genuinely more readable than a precedence over outcome values, and a middle position that was not adopted.

13.4: the overlap with `Part 3`. Both hold a record of the same decision and nothing compares them. This is the first component for which `Part 3` section 13.11's question is concrete.

13.5: the boundary with optimisation. A candidate set too large to compare exhaustively is presently refused, which pushes the work outside the standard entirely.

13.6: whether an indeterminate eligibility should carry the set of possible values, as XACML's extended indeterminate does.

## The repeated structure question, now urgent, 13.7

Five patterns have now been independently specified across five parts: the immutable record with stateful assertions about it (five parts), the declared completeness of a set (four), the frontier as a declared terminus (two, and this part uses the concept without the name), the asymmetric bridge that disproves and cannot prove (two, and this part should have a third), and the honest undeclared value (five).

**Drift has already begun.** `Part 3`'s frontier kinds and `Part 4`'s are different sets for the same concept. Factoring these is cheap now and will not be after Part 13.

## Gaps declared in 13.8

No criterion kind for a voting rule, which is where Arrow's result bites hardest and which any organisation with committee approvals needs.

No treatment of decisions under time pressure where declining to decide is unavailable.

No guidance on what a good weight justification is, which is the question a steward will actually ask.

Nothing costed. The comparison grain of section 8.2 is the largest volume this part requires.

## Next actions

Verify the 13.1 claims before approval. Priority: the DMN hit policy semantics, since clause P5-3.59 refuses two policies on the strength of them; the XACML only one applicable behaviour; and the Case C-634/21 holding, on which section 3.16 entirely rests.

Establish the EU AI Act application position independently, per clause P5-10.3.

Examine the three United States state instruments, none of which was assessed and all of which may bear on sections 3.16 and 8.6.

Part 6, workflow and process orchestration, is next in the brief's order. Sections 12.6 of all five completed parts now commit reciprocal statements it must honour, including from this part that it does not own decisions, criteria or outcomes and that an undecidable outcome must be recorded before any referral is raised.

`Part 0` now inherits thirty eight composition questions: six from Part 1, seven from Part 2, eight from Part 3, eight from Part 4, and nine from Part 5.

## Pending confirmation

Whether the refusal of the First hit policy stands. It is the position most likely to be rejected on adoption grounds and 13.3 gives you the middle option.

Whether the entitlement test in section 12.7 is the right boundary with `Part 7`, given that a credit limit decision constrains later authorisations and an approver selection is consumed by one.

Whether the five repeated structures should be factored now, before Part 6, rather than left to Part 0. My recommendation is now rather than later, and it is the third time this has come up.
