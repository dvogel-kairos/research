# Questions inherited by Part 0

Derived by `Standards/tools/build_registers.py`. As at 2026-08-28.
Do not edit by hand. Part 0 is authored last and inherits every question
each part handed forward rather than answering.

| Part | Section | Questions |
| --- | --- | --- |
| 1 | 13.14 | 6 |
| 2 | 13.14 | 7 |
| 3 | 13.11 | 8 |
| 4 | 13.9 | 8 |
| 5 | 13.9 | 9 |
| 6 | 13.9 | 8 |
| 7 | 13.9 | 8 |
| **All** | | **54** |

## The questions, in full

### From Part 1, section 13.14

1. What a component receiving `NOT_IN_FORCE_AT_TIME` must record, and what it must not conclude.
2. Which component holds authority over the identity of an actor, since this part treats it as opaque and at least three other parts need it.
3. How a version is pinned across a unit of work that touches several components, so that all of them resolve against the same version.
4. What happens when a determination's provenance in `Part 3` and a citation resolution in this component disagree about which version was used.
5. Whether a retention obligation recorded here can bind the disposal behaviour of `Part 11` and `Part 3`, which hold copies of or references to the same content.
6. How the divergence signal of clause P1-3.101 reaches the owner of a determination made years earlier in a component that may since have been replaced.

### From Part 2, section 13.14

1. What a component receiving an `INDETERMINATE` verdict must record, and what it must not conclude, per subclass.
2. How one rule set version is pinned across a unit of work that touches this component and `Part 5`, so that a decision and the verdicts it consumed rest on the same rules.
3. What happens when `Part 3`'s record of a determination and this component's record of the verdict it consumed disagree.
4. Whether a retention obligation recorded in `Part 1` can bind the disposal of a verdict here and of the report copy held in `Part 11`, given clause P2-8.31 requires rule artifacts to outlive their verdicts.
5. How the drift signal of section 3.7 reaches the owner of a determination made years earlier on the strength of a verdict from a rule whose authority has since been withdrawn.
6. Which component holds authority over the identity of an actor, since this part treats it as opaque and needs it for authorship, correspondence claims and access records.
7. Whether an evaluation spanning subjects owned by several components can pin a consistent state across them, which the model of section 3.12 assumes and does not provide.

### From Part 3, section 13.11

1. How the obligation to register a determination is imposed, given that this part can refuse a defective registration and cannot compel a missing one.
2. What a component must do when it cannot satisfy the registration preconditions of section 4.2, given that the alternative to registering is no record at all.
3. What happens when this component's record of a determination and the owning component's own record disagree, which `Part 2` section 13.14 also hands forward.
4. How a unit of work spanning several components yields one determination, or several with a declared relation, so that a chain is not fragmented at component boundaries.
5. What a component must do with each indeterminacy subclass of `Part 2` section 7.2 and each non result subclass of `Part 1` section 7.2, and how the disposition it chose reaches the `non_result_acceptance` record of section 3.9.
6. Whether the structural pattern this standard has now repeated three times, that the governed record does not transition and the assertions about it do, should be stated once for the whole standard.
7. Which component holds authority over actor identity, since three parts now treat it as opaque and this one requires a delegation chain over it.
8. Whether the erasure and retention tension recorded in `Part 1` section 13.2 and in section 13.10 here has one answer for the whole standard or three different ones.

### From Part 4, section 13.9

1. How the dependency registration obligation of section 3.16 is imposed on components that have no incentive to meet it, given that an unpopulated index makes every impact analysis a data flow traversal.
2. What a component must do when it holds a meaning this registry refuses to record, since every refusal in section 7.5 is detectable only at recording and none is remediable here.
3. How a concept supersession propagates: which component compels a dependent to rebind, and what the estate does about the dependents that do not.
4. Whether the absent, withheld, unknown and not applicable distinctions maintained by `Part 1`, `Part 2` and `Part 3` and declared here as null semantics have one enterprise wide answer or one per representation.
5. How a unit of work spanning this component and `Part 9` pins one definition version across both, so that a schema and the definition it realises cannot drift within a release.
6. Whether the frontier concept, the immutable record with stateful assertions pattern, and the asymmetric bridge pattern should each be specified once for the whole standard, per section 13.7.
7. Which component holds authority over actor identity, since four parts now treat it as opaque and this one requires a steward who can be asked what a concept means.
8. Whether the retention obligations now committed by four parts, each requiring its records to outlive something another part holds, are jointly satisfiable, since this part's clause P4-8.34 requires a definition to outlive a `Part 3` determination, `Part 3` clause P3-8.31 requires rule artifacts to outlive verdicts, and `Part 1` section 13.2 records the erasure tension unresolved.

### From Part 5, section 13.9

1. What a caller must do with each of the four undecidable outcomes, given that a caller with no representation for them will retry, default or fail.
2. How the acyclicity between this component and `Part 2` is enforced, given that clause P5-12.12 and clause P2-12.14 each forbid one direction and neither component can observe the other.
3. How a unit of work pins one rule set version and one criterion version together, so that a decision and the eligibility it rested on cannot be against different vintages of policy.
4. Which component is authoritative where this component's decision record and `Part 3`'s determination record disagree, which section 13.4 records as this part's least comfortable boundary.
5. Whether the treatment of an indeterminate input has one enterprise wide answer or one per decision class.
6. Whether an override recorded here, a `Part 8` case and a `Part 3` determination of the override are one act or three, and which is authoritative for what was finally acted upon.
7. Whether the five repeated structures of section 13.7 should each be stated once for the whole standard, which is now a decision worth taking before `Part 6` rather than after `Part 13`.
8. Which component holds authority over actor identity, since five parts now treat it as opaque and this one requires a named reviewer whose override rate is a governance measure.
9. Whether the entitlement test of section 12.7 is the right boundary between a business decision and an authorisation, given that a decision determining a credit limit constrains later authorisations and a decision determining which approver is required is consumed by one.

### From Part 6, section 13.9

1. How the disposability requirement is enforced across the estate, given that this part can demonstrate its own compliance and cannot prevent a consumer from building a report over its instances.
2. What the estate does when an orchestrator is replaced with instances in flight, given that instances are pinned to definition versions the replacement may not hold.
3. Who owns a residue by default where no assignment is made, since clause P6-3.69 requires an assignment and cannot compel one.
4. How a unit of work spanning this component, `Part 2` and `Part 5` pins one rule set version, one criterion version and one definition version together.
5. Whether a review obligation raised here, a `Part 8` task and a `Part 3` determination of its discharge are one act or three, which is the same shape as the question `Part 5` section 13.9 hands forward about an override.
6. What a component must do when this component's activity outcome and the invoked component's own record of the invocation disagree, which is the concrete form of `Part 3` section 13.11's question.
7. Whether the engine's observation of elapsed time, which section 6.5 permits as the one occurrence time a component may originate, should be permitted to any other component or reserved to this one.
8. Whether the six repeated structures of section 13.7 should each be stated once for the whole standard, and whether the frontier concept's three vocabularies should be reconciled before `Part 7`.

### From Part 7, section 13.9

1. How a token scope relates to a decision, and whether an estate may rely on a scope in place of a decision under declared conditions.
2. Who is accountable for an enforcement point that does not report, given that this part makes the population attributable and has no authority over the point.
3. Whether the response to a not applicable is a per enforcement point declaration or an enterprise wide position, since a heterogeneous set of responses means one request denied at one point and permitted at another.
4. How a unit of work spanning this component, `Part 2` and `Part 5` pins one policy version, one rule set version and one criterion version together.
5. Whether an authorisation decision about a natural person falls within the automated decision provisions `Part 5` section 10.5 records, which would attach explanation and intervention obligations this part does not specify.
6. Whether a review obligation raised here, a `Part 8` task and a `Part 3` determination of its discharge are one act or three, which three consecutive parts have now handed forward.
7. Whether the withholding marking vocabulary should be specified once for the estate, since four parts consume the distinction and each names it differently.
8. Whether the divergence recorded in section 13.7, in which `Part 5` and this part treat the third value differently in adjacent components that exchange values, should be resolved before `Part 8`.

