# KAIROS STD 003 Part 0, authoring brief, system composition

Status: version 1, Proposed. Authored 2026-08-17 by the design side for the research thread. This brief commissions Part 0 of `KAIROS STD 003`, which specifies how the thirteen components compose into one system.

Read this alongside the authoring brief for parts one through thirteen. Part 0 is numbered zero because it is read first. It is authored last, after the thirteen exist, because it is written against them rather than ahead of them.

Part 0 does not use the thirteen section template. Its own structure is set in section 3 below, because it specifies interaction rather than a component.

## 1. Why this part exists

Section 12 of each part declares that part's boundaries pairwise. Thirteen documents each describing its own edges do not describe a system. A boundary says what a component must not absorb. Composition says what happens when all thirteen are running at once.

The gap between those two is where enterprise systems fail. A value crosses a boundary and is transformed. Two components hold the same fact and disagree. An absence in one component reads as a value in another. A component returns undecidable and its caller has no representation for it, so it becomes a false negative. None of those failures is visible in any single component's specification, and every one of them is a composition defect.

Part 0 is the specification that makes those failures representable, and therefore preventable.

## 2. The same constraints as the other parts

**No reference to any existing implementation.** Part 0 specifies how these thirteen components compose in general, for any organisation. If the author knows how a particular system composes them, the part must not show it. A composition document written against one implementation is that implementation's architecture diagram, which is worthless as a standard.

Clauses with RFC 2119 modalities, each a single testable statement, with a clause index at the head.

Every value that crosses a boundary carries its type, its cardinality and what its absence means.

Sources cited by specification and section where a claim rests on specification text, marked as practice where it does not.

What could not be established is reported rather than inferred.

## 3. The structure of Part 0

**Section 1. Scope.** What Part 0 specifies and what it leaves to the thirteen.

**Section 2. Terminology.** Only terms Part 0 introduces, being terms about composition itself. Every component term is owned by its own part and cited rather than redefined.

**Section 3. The component map.** All thirteen, each with what it owns stated in one sentence, and a diagram or table showing which components exchange what.

**Section 4. The authority model.** At any moment exactly one component owns a given fact and the others read it. State the ownership of every fact that more than one component touches, and where two could plausibly own something, say which does and why. A fact owned by two components is a defect this section exists to prevent.

**Section 5. The primary flows.** Each traced end to end, naming at every step which component holds authority, what artifact passes, and what the receiving component may assume about it. At minimum:

A unit of work arriving from outside and reaching a decision.

A rule evaluating and its verdict reaching the audit record.

A human task opening, a person deciding, and the decision taking effect.

A definition changing, and what that invalidates in work already done or in progress.

A determination being reconstructed years later from the audit record alone, with the system not running.

**Section 6. The seams.** The section that earns this part. Every place a value crosses a component boundary and could be transformed, lost, duplicated or renamed. Every place two components could disagree about the same fact. Every place an absence in one component reads as a value in another. For each seam, state what must hold, how it is checked, and what a violation looks like in the record.

**Section 7. Failure and non result propagation.** Each component's outcome taxonomy includes values that are neither success nor failure, being undecidable, not applicable, not evaluated and their equivalents. Specify what a caller does with each, and what happens when a component receives a value its own taxonomy has no representation for. A non result silently becoming a negative is the failure mode this section prevents.

**Section 8. Consistency and ordering.** What must be true across components at any moment, what may be eventually consistent and for how long, and what ordering guarantees a component may assume of another. Where a guarantee cannot be provided, say what the caller must do instead.

**Section 9. Versioning across components.** Each part specifies its own versioning. Specify what happens when two components hold different versions of a shared definition, how a version is pinned across a unit of work, and what makes a composition of versions valid or invalid.

**Section 10. What is deliberately not composed.** Components that must not know about each other, with the reason. A specification that connects everything to everything has specified nothing.

**Section 11. Composition anti patterns.** Known failure designs of composition rather than of components, each with its evidence and its consequence. Distributed monolith, shared mutable state across a boundary, a component reaching past its neighbour, a chatty boundary, and whatever else the literature names.

**Section 12. Deployment and topology considerations.** What the specification requires of deployment and what it leaves open. Whether components may be colocated, whether any must be separate, and what changes when a boundary becomes a network boundary rather than a function call.

**Section 13. What could not be established.**

## 4. Two things to get right

**Section 6 is the deliverable.** If Part 0 is thin anywhere else it remains useful; if section 6 is thin it is a diagram with paragraphs. A seam is a specific place, named, with a specific thing that must hold. Not a general caution about integration.

**Section 4 must be decisive.** Where two components could own a fact, the part chooses and gives the reason. Recording that either could is not an answer, and it is the precise ambiguity that produces two authorings of one fact.

## 5. What the author should not do

Do not restate the thirteen parts. Part 0 cites them and specifies only what none of them can specify alone.

Do not connect components the flows do not require. Every declared interaction needs a flow in section 5 that uses it.

Do not resolve a disagreement in the literature quietly. Name the positions.

Do not fill a gap with a plausible design.
