# Session checkpoint: KAIROS STD 003 Part 7

**Date.** 2026-08-18.
**Session intent as stated.** Author Part 7, policy decision point and authorisation, covering policy evaluation, obligations and combining algorithms.
**Deliverable state.** Complete and delivered as `KAIROS-STD-003-Part-7-v1.0-Proposed.md`. Version 1.0.0, status Proposed, not approved and not effective.

## What was produced

One document, 52,300 words, 463 clauses across the thirteen mandated sections. Validation clean: every identifier unique, in ascending document order, contiguous from 1 within its section. Every internal clause citation resolves, and all thirty two cross part clause citations were verified against the delivered text of Parts 1 through 6.

353 clauses are MUST, 106 MUST NOT, 4 SHOULD. Section 3 carries 118, section 6 carries 52.

## Rehydration performed

Read section 12.7 of all six prior parts. Six reciprocals were outstanding and all six are discharged in sections 12.1 through 12.6. Two were concrete requirements rather than declarations: `Part 2` clause P2-12.18 and `Part 3` clause P3-12.18 both require this component to identify what it restricted as **withheld** rather than removing it. Section 3.11 specifies the withholding obligation and it is the requirement this part owes most heavily to the rest of the standard.

`Part 3` and `Part 4` both allocate **delegation validity** here, and `Part 3` clause P3-12.17 forbids that component from assessing it. Section 3.13 owns the question.

## Positions taken that a reviewer may want to overturn

**The decision is advice until it is enforced.** The spine. This component can prove what it decided and cannot prove what happened. Decision and enforcement report are two records, never merged, and the absence of a report is the ordinary case rather than an error. The honest count of unreported decisions is the measure of how much of an estate's access control is unverified.

**Not applicable is never returned as deny.** The most important requirement in the part. Default deny is a correct enforcement point behaviour and a catastrophic decision point behaviour, because it makes the coverage gap permanently invisible.

**Extended indeterminate adopted.** Three values recording what an incomplete evaluation could have been, which is what makes a fail safe response principled rather than a guess.

**Obligations get a six member outcome taxonomy and a residue model.** The reviewed standard specifies when an obligation is attached and what an enforcement point must do if it cannot discharge one, and says nothing about partial, impossible or unreported fulfilment. A permit carrying an unfulfilled obligation is, under that standard's own rule, an operation that should not have proceeded, and clause P7-3.72 makes the population countable.

**Obligation kinds must be registered.** The reviewed standard states that obligation meanings rest on bilateral agreement between policy author and enforcement point. This part refuses that: an obligation whose meaning is private is a control no third party can audit.

**First applicable is refused.** Fourth consecutive part to refuse selection by declaration order.

**Ordered combining variants are admitted for obligation sequencing only**, not as decision rules, which preserves order independence while giving authors the sequencing they need.

**Collapsing algorithms are fenced to the outermost policy set**, authorised, and required to record the outcome the collapse concealed.

**Emergency access is a declared policy** with three mandatory obligations, not a bypass outside the model.

## Research findings, two of which post date my knowledge

**OpenID Authorization API 1.0 was published as an OpenID Final Specification on 11 March 2026**, five months before the date of this part, by the AuthZEN Working Group. Vote: 81 approve, 1 object, 25 abstain. It standardises the decision point to enforcement point interface and deliberately does not define a policy language. **Its core evaluation returns a boolean**, which conflicts directly with this part's four value requirement, and section 10.5 states the conflict. Note that the boolean claim rests on a technical summary, not the specification text, so the conflict may be narrower than stated.

**XACML 4.0 Committee Specification Draft 01 was published 18 February 2026**, six months before this part. XACML 3.0 Plus Errata 01 of 12 July 2017 remains the stable release. The draft adds JSON and YAML representations and there is a live discussion about renaming the language. A reviewer should read it: a draft successor to this part's principal source, published six months before the part was written, is the most likely thing to invalidate a position taken here.

**The obligation rule was obtained verbatim in effect** from the specification: a conforming enforcement point must deny unless it **understands and can discharge** every obligation. Two conditions, not one. Sections 3.9 and 3.10 rest on it.

## Open, carried forward

13.2: the decision response is a document where an application wants a boolean, and nothing is costed.

13.3: the cost of refusing first applicable. The middle position `Part 6` proposed for its own refusal now stands unadopted in two parts and deserves a decision.

13.4: the boundary with `Part 5` is a governance allocation, not a derivable fact. A per operation declaration is probably better than a test.

13.5: **the largest gap in the part.** This component cannot compel an enforcement report. Three constructions were considered and none pursued; sampling with independent attestation via `Part 12` is probably the right answer and was not designed.

13.6: one attribute value entry per use and one condition entry per evaluation, at authorisation transaction volumes. Uncosted.

## The repeated structure question, and the first observed divergence

Section 13.7 records eight patterns across seven parts, and one is no longer a repetition.

**`Part 5` and this part treat the third value differently in adjacent components that exchange values.** `Part 5` section 13.6 records that it considered extended indeterminacy for eligibility and did not adopt it, and that the omission may have been a mistake. This part adopts it because its source supplies it. That is an inconsistency rather than a pattern, and it should be resolved before it is inherited.

Also: the residue model now exists twice, in `Part 6` and here, with two vocabularies for one structure. And three consecutive parts have now identified the same missing asymmetric bridge device.

This is the fourth consecutive part to record the question and the third to recommend acting before the next part.

## Gaps declared in 13.8

**No enforcement point is specified.** This part says what one must be told and what it must declare, and nothing about how it works, so the most consequential component in the authorisation path is outside this standard entirely.

No policy language, and no wire format. Exposing the new AuthZEN API as a projection makes conformance to both standards awkward.

No cross organisational authorisation, where neither party can compel the other.

No delegation of policy administration.

## Next actions

Verify the 13.1 claims before approval. Priority: the XACML normative appendix on combining algorithms, since clause P7-3.51 refuses first applicable and clause P7-3.52 admits the ordered variants on the strength of secondary description; the extended indeterminate section; the AuthZEN boolean decision claim; and the XACML 4.0 draft in full.

Part 8, human task and case management, is next in the brief's order. Sections 12.8 of all seven completed parts now commit reciprocal statements it must honour. `Part 6` section 12.8 in particular records the flow against work item boundary as the most delicate in that part, and `Part 6` section 13.4 leaves three cases on the line. CMMN, unassessed in Part 6's research, is directly on point.

`Part 0` now inherits fifty four composition questions: six from Part 1, seven from Part 2, eight from Part 3, eight from Part 4, nine from Part 5, eight from Part 6, and eight from Part 7.

## Pending confirmation

Whether the refusal of a two valued interface stands, given that a standard published five months ago specifies one. My position is that a boolean may be a projection over a recorded fuller decision but never the record; a reviewer might reasonably prefer conformance to the newer standard.

Whether not applicable must never be returned as deny. It is the most important requirement in the part and the one an implementer will most want to relax.

Whether the `Part 5` divergence in 13.7 should be resolved now. This is no longer a tidiness question: two adjacent components exchange values and treat the third value differently.
