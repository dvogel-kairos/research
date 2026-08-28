# Session checkpoint: KAIROS STD 003 Part 6

**Date.** 2026-08-18.
**Session intent as stated.** Author Part 6, workflow and process orchestration, covering control flow, joins, loops, compensation and process state.
**Deliverable state.** Complete and delivered as `KAIROS-STD-003-Part-6-v1.0-Proposed.md`. Version 1.0.0, status Proposed, not approved and not effective.

## What was produced

One document, 52,497 words, 456 clauses across the thirteen mandated sections. Validation clean: every identifier unique, in ascending document order, contiguous from 1 within its section. Every internal clause citation resolves, and all eighteen cross part clause citations were verified against the delivered text of Parts 1 through 5.

346 clauses are MUST, 104 MUST NOT, 5 SHOULD, 1 MAY. Section 3 carries 122, section 6 carries 51.

## Rehydration performed

Read section 12.6 of all five prior parts. Five reciprocals were outstanding and all five say substantially the same thing in five vocabularies: the component's own state must be correct without reference to any process instance, and must remain correct where the orchestrator is replaced or its instances are disposed of. Every prior part also required that this part's retention not govern the retention of what it routed.

**Those five reciprocals became the spine of the part.** Clause P6-1.3 requires a periodic demonstration that disposing of every process instance would leave every business fact intact and answerable. Section 3.12 closes the set of value kinds a process instance may hold so that no kind admits a business fact.

## Positions taken that a reviewer may want to overturn

**Explicit termination is mandatory and a stall is a state.** BPMN and most engines permit an instance to end when no tokens remain, which makes a deadlock indistinguishable from a completion. This is the largest divergence in the part and it is what makes the stalled population visible.

**The inclusive join is admitted only in block structured regions** with no cancellation and no arbitrary cycle, because the construct's semantics require global state, published formalisations disagree, and the underlying reachability question is undecidable with cancellation. Section 13.3 records the cost honestly and offers a middle position I did not adopt.

**Exclusive split conditions must be mutually exclusive.** BPMN takes the first true condition in a defined order, which is selection by branch order and is exactly what `Part 5` clause P5-3.59 refused. A non exclusive selection must be a `Part 5` decision.

**Compensation gets a six member outcome taxonomy** with partial, impossible and failed as distinct members, plus a residue model with registered kinds and mandatory assignment. This is the part's principal contribution and it has no source in any reviewed standard.

**Invocation attempts are separate from activity outcomes**, and `OUTCOME_UNKNOWN` is a state distinct from failure. An engine that records only completed invocations cannot distinguish an invocation never made from one whose result was lost.

**Forced outcomes are marked permanently.** An outcome supplied by an operator under pressure is never recorded as an outcome the invoked component reported.

**Instances are pinned to their start definition version.** Migration only under an exhaustive, soundness assessed, approved mapping.

## Research findings

**BPMN has had no major revision since January 2011.** 2.0.2 is current, the OMG formal document is dated December 2013, and issues are still being filed against it in 2024.

**An unresolved discrepancy.** The ISO/IEC 19510 front matter says it is identical with BPMN 2.0.1; the OMG's own page says 2.0.2 was published by ISO as the 2013 edition. Both were obtained and they cannot both be right, so a citation to the ISO number does not identify a maintenance release. Clause P6-10.3 requires an implementation to say which document it read.

**The OMG's own account of the inclusive gateway requires global information about the state of the whole model.** That is the basis of section 3.7's restriction.

**WS-BPEL 2.0's compensation ordering has two accounts in circulation.** The specification text says reverse order of completion; its own issue resolution settled on respecting only explicitly modelled control dependencies; and the literature identifies anomalies where control links cross scope boundaries. Section 3.9 requires the order to be declared rather than resolving the conflict.

**Soundness is undecidable for workflow nets with reset arcs**, which is how cancellation is modelled. This is a mathematical fact, not an implementation limit, and it means declaring a cancellation region moves a definition out of the class where its correctness can be established at all. Clause P6-6.38 requires the honest report. It is also part of why section 3.7 restricts the inclusive join: keeping definitions inside the decidable class has value.

## Open, carried forward

13.2: this part offers **recoverability of a recorded execution**, not reproducibility. Weaker than the four prior parts and forced rather than chosen, because the engine's inputs include real time, event arrival order and external availability. A candidate improvement, declaring per definition which external timings a path may legitimately depend on, was not designed.

13.3: the cost of restricting the inclusive join, with a middle position.

13.4: where the flow ends and the work item begins. The test in section 12.8 leaves three cases on the line, and the `waiting_on` projection cannot say whether anybody is actually working on a human activity.

13.5: whether compensation availability should expire, and what the expiry should do.

13.6: the volume. One entry per invocation attempt and one per iteration, uncosted.

## The repeated structure question, third consecutive part

Six patterns now appear across six parts, and the drift is observable rather than predicted. **The frontier concept now has three vocabularies**: `Part 3` names it for chains of reasoning, `Part 4` names it differently for lineage, `Part 5` uses the concept without the name, and this part's stall is structurally `FRONTIER_UNDECLARED` applied to an execution. **The asymmetric bridge is missing from two parts that should have one**, this part included; its candidate here would be recorded executions with asserted paths, run at definition recording, which would catch the commonest defect in process modelling.

This is the third consecutive part to raise it and the second to recommend acting before the next part.

## Gaps declared in 13.8

No notation and no interchange format, so a definition cannot move between conforming implementations on the strength of this part.

No treatment of cross organisational choreography, where no single component holds the flow.

No treatment of ad hoc or unstructured work, where the performer chooses the order.

No treatment of a generated process definition, which would need the triad `Part 2` requires of a rule.

## Next actions

Verify the 13.1 claims before approval. Priority: the BPMN exclusive gateway's order dependence, since clause P6-3.32 refuses a construct on its strength; the inclusive gateway's global semantics; the four WS-BPEL compensation rules; and the undecidability result, which is the most consequential literature claim in the part.

Resolve the ISO/IEC 19510 discrepancy, which is a one lookup answer for anyone with catalogue access.

Examine five sources not assessed: CMMN, which bears directly on the `Part 8` boundary; SCXML; ISO/IEC 15909; XPDL; and the exception handling pattern literature, which is the most likely source for anything in section 3.10 that section 10.8 currently records as unsourced.

Part 7, policy decision point and authorisation, is next in the brief's order. Sections 12.7 of all six completed parts now commit reciprocal statements it must honour. `Part 5` section 12.7 in particular hands it the contestable entitlement test, and XACML 3.0's combining algorithms and extended indeterminate values, established during Part 5's research, are directly on point.

`Part 0` now inherits forty six composition questions: six from Part 1, seven from Part 2, eight from Part 3, eight from Part 4, nine from Part 5, and eight from Part 6.

## Pending confirmation

Whether mandatory explicit termination stands. It is the largest divergence from ordinary practice in the part and it is the requirement that makes the stalled population visible.

Whether the inclusive join restriction stands, or whether the middle position in 13.3 is preferable.

Whether the six repeated structures should be factored now. Third time asking; the frontier concept already has three vocabularies and reconciling them before Part 7 is cheaper than after Part 13.
