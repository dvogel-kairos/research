# KAIROS STD 003 Part 12: Conformance and Assurance Harness

**Standard.** KAIROS STD 003, the enterprise architecture standard.
**Part.** Part 12 of 14 (Part 0 and Parts 1 through 13). Cited as `KAIROS STD 003 Part 12`.
**Title.** Conformance and assurance harness.
**Version.** 1.0.0.
**Status.** Proposed. This part has not been approved and is not effective. It is issued for review against the authoring brief of 2026-08-17.
**Date of issue.** 2026-08-18.
**Supersedes.** Nothing. This is the first version.

## Binding of requirement language

The key words MUST, MUST NOT, SHOULD, SHOULD NOT and MAY in this part are to be interpreted as described in RFC 2119 and RFC 8174, and only in the upper case forms. This part does not use SHALL, SHALL NOT, REQUIRED, RECOMMENDED, NOT RECOMMENDED or OPTIONAL as requirement keywords.

Every requirement in this part is a numbered clause. A clause identifier has the form `P12-S.N`, where `S` is the section number and `N` is the ordinal of the clause within that section. Clause identifiers are permanent. A clause that is later removed has its identifier retired and never reissued. A clause that is later added to a section takes the next unused ordinal in that section, so ordinals are stable but not contiguous over the life of the part.

Text that is not a numbered clause is not binding. Narrative, tables, algorithms, examples and the discussion of standards are provided to make the clauses intelligible and testable, and where a table carries normative content a clause says so explicitly and names the table.

Where a clause carries a **Source.** note, the note states the specification or published work on which the clause's subject rests and whether this part adopts that treatment or departs from it. The note is narrative and not binding; the clause governs.

## Conformance

An implementation conforms to this part if it satisfies every MUST and MUST NOT clause and records, for each SHOULD and SHOULD NOT clause it does not satisfy, the reason. This part does not define conformance levels, profiles or a certification scheme.

This part is the part that defines assessment method for the standard, and it therefore has a problem no other part has: it cannot be the assessor of its own conformance. Section 3.4 and section 6.11 specify how an implementation of this part is assessed, and clause P12-1.30 forbids it from assessing itself. A conformance claim about an implementation of this part that rests on that implementation's own assessment is void by the terms of this part.

## Clause index

The index below is generated from the clause text of this document. It lists every clause identifier, its modality and its subject label. The counts that follow the index are derived by the same extraction and are stated with the grain at which they were counted.

| Clause | Modality | Subject |
| --- | --- | --- |
| P12-1.1 | MUST | Clause register owned |
| P12-1.2 | MUST | Assessability classification owned |
| P12-1.3 | MUST | Claims owned |
| P12-1.4 | MUST | Assessment plans owned |
| P12-1.5 | MUST | Evidence items owned |
| P12-1.6 | MUST | Findings owned |
| P12-1.7 | MUST | Assurance statements owned |
| P12-1.8 | MUST | Probes and elicitations owned |
| P12-1.9 | MUST | Frame declarations owned |
| P12-1.10 | MUST | Independence declarations owned |
| P12-1.11 | MUST | The trust base owned |
| P12-1.12 | MUST | Nonconformity records owned |
| P12-1.13 | MUST | Surveillance schedules owned |
| P12-1.14 | MUST | Its own external assessment record owned |
| P12-1.15 | MUST NOT | Not the author of the criteria |
| P12-1.16 | MUST NOT | Not a remediator |
| P12-1.17 | MUST NOT | Not an authority over any assessed component's state |
| P12-1.18 | MUST NOT | Not a decision point for access |
| P12-1.19 | MUST NOT | Not the audit ledger |
| P12-1.20 | MUST NOT | Not a rules engine |
| P12-1.21 | MUST NOT | Not a certification body |
| P12-1.22 | MUST NOT | Not an accreditor |
| P12-1.23 | MUST NOT | Not the owner of any nonconformity |
| P12-1.24 | MUST NOT | Not a schema, document, reference or artifact authority |
| P12-1.25 | MUST NOT | Not a work manager |
| P12-1.26 | MUST | Assessment is of clauses, not of systems |
| P12-1.27 | MUST NOT | No assessment anticipated of anything outside this standard |
| P12-1.28 | MUST | Scope of every assessment declared |
| P12-1.29 | MUST NOT | No conformance level defined |
| P12-1.30 | MUST NOT | No self assessment |
| P12-2.1 | MUST NOT | No redefinition of another part's terms |
| P12-2.2 | MUST NOT | Assurance not equated with conformity |
| P12-2.3 | MUST NOT | Not falsified not equated with true |
| P12-2.4 | MUST NOT | Finding not equated with assurance statement |
| P12-2.5 | MUST NOT | Coverage not equated with depth |
| P12-2.6 | MUST NOT | Evidence not equated with testimony |
| P12-2.7 | MUST NOT | Attestation not equated with assessment |
| P12-2.8 | MUST NOT | Trust base not equated with scope exclusion |
| P12-2.9 | MUST | Kinds registered before use |
| P12-3.1 | MUST | Types declared |
| P12-3.2 | MUST | Criterion references carry the part version |
| P12-3.3 | MUST NOT | No representation dependent identity |
| P12-3.4 | MUST | Assurance expressed negatively |
| P12-3.5 | MUST | Method, depth, coverage and frame mandatory |
| P12-3.6 | MUST | What was not established recorded |
| P12-3.7 | MUST | Falsification attempts enumerated |
| P12-3.8 | MUST NOT | No universal claim from a sample |
| P12-3.9 | MUST | One counterexample decisive |
| P12-3.10 | MUST NOT | No aggregation of a falsification into a rate |
| P12-3.11 | MUST | Inventory normative |
| P12-3.12 | MUST | Immutability observed |
| P12-3.13 | MUST | External assessment obtained |
| P12-3.14 | MUST NOT | No self assessment recorded as an assessment |
| P12-3.15 | MUST | Absence of an external assessment declared |
| P12-3.16 | MUST | Mutual assessment where more than one assessor exists |
| P12-3.17 | MUST | Trust base enumerated |
| P12-3.18 | MUST NOT | No unenumerated assumption |
| P12-3.19 | MUST | Trust base reviewed on a declared cadence |
| P12-3.20 | MUST | Trust base items classed by consequence |
| P12-3.21 | MUST NOT | No termination claimed |
| P12-3.22 | MUST | Criteria resolved, never transcribed |
| P12-3.23 | MUST NOT | No interpretation recorded as the criterion |
| P12-3.24 | MUST | Register versioned per part version |
| P12-3.25 | MUST | Clause count derived, not asserted |
| P12-3.26 | MUST | Permissive criteria registered and excluded from conformance |
| P12-3.27 | MUST | Advisory criteria assessed for the recorded reason |
| P12-3.28 | MUST | Every criterion classified |
| P12-3.29 | MUST | Classification reasoned |
| P12-3.30 | MUST | Not assessable published per part |
| P12-3.31 | MUST NOT | No not assessable criterion counted as satisfied |
| P12-3.32 | MUST | Denominator declared with every proportion |
| P12-3.33 | MUST | Reclassification recorded, not overwritten |
| P12-3.34 | MUST | Classification exposed to the part's author |
| P12-3.35 | MUST NOT | No clause rewritten here |
| P12-3.36 | MUST | Plan declared before evidence |
| P12-3.37 | MUST | Unfalsifiable claims recorded as such |
| P12-3.38 | MUST | Quantification recorded |
| P12-3.39 | MUST NOT | No universal claim assessed as statistical |
| P12-3.40 | MUST | Determination statements traceable to criteria |
| P12-3.41 | MUST | One statement, one property |
| P12-3.42 | MUST NOT | No plan amended after evidence |
| P12-3.43 | MUST | Provenance recorded on every item |
| P12-3.44 | MUST NOT | No self reported item described otherwise |
| P12-3.45 | MUST | Independent reconstruction defined by non reliance |
| P12-3.46 | MUST | Influence recorded |
| P12-3.47 | MUST | Evidence held by address |
| P12-3.48 | MUST | Contradicting evidence retained |
| P12-3.49 | MUST NOT | No evidence discarded on a favourable finding |
| P12-3.50 | MUST | Frame declared on every assessment |
| P12-3.51 | MUST | Frame declaration examined independently where the assessed component declared it |
| P12-3.52 | MUST NOT | No sampling of a non enumerable frame |
| P12-3.53 | MUST | Partial enumerability handled as two populations |
| P12-3.54 | MUST | Sampling scheme declared before drawing |
| P12-3.55 | MUST | Sample recorded in full |
| P12-3.56 | MUST NOT | No convenience sample presented as probabilistic |
| P12-3.57 | MUST | Assessed component excluded from selection |
| P12-3.58 | MUST | Finding requires evidence |
| P12-3.59 | MUST | Strongest provenance recorded |
| P12-3.60 | MUST NOT | No satisfied finding on self report alone |
| P12-3.61 | MUST | Depth and coverage achieved recorded, not planned |
| P12-3.62 | MUST | Shortfall against plan recorded |
| P12-3.63 | MUST | Findings immutable, disputes separate |
| P12-3.64 | MUST | Dispute does not withdraw the finding |
| P12-3.65 | MUST | Validity interval mandatory |
| P12-3.66 | MUST | Decay basis mandatory |
| P12-3.67 | MUST | Party class recorded |
| P12-3.68 | MUST NOT | No first party statement presented as independent |
| P12-3.69 | MUST | Object version pinned |
| P12-3.70 | MUST | Statement superseded on object change |
| P12-3.71 | MUST NOT | No expired statement presented as current |
| P12-3.72 | MUST | Expected outcome declared before introduction |
| P12-3.73 | MUST | Permission cited |
| P12-3.74 | MUST | Instance class recorded |
| P12-3.75 | MUST NOT | No conclusion about production from an isolated instance |
| P12-3.76 | MUST | Side effects declared and withdrawn |
| P12-3.77 | MUST | Detection recorded |
| P12-3.78 | MUST | Detected probes invalidate the inference |
| P12-3.79 | MUST | Probe instances unpredictable |
| P12-3.80 | MUST | Three forms declared separately |
| P12-3.81 | MUST NOT | No independence claimed where any form is absent |
| P12-3.82 | MUST | Competence basis recorded |
| P12-3.83 | MUST NOT | No assessment outside the registered scope |
| P12-3.84 | MUST NOT | No advisor as assessor |
| P12-3.85 | MUST | Funded by the object owner recorded as a conflict |
| P12-3.86 | MUST | Owner outside this component |
| P12-3.87 | MUST | Acceptance bounded and authorised |
| P12-3.88 | MUST NOT | No closure without a reassessment |
| P12-3.89 | MUST | Expired acceptance reopens |
| P12-3.90 | MUST | Accepted population exposed |
| P12-3.91 | MUST | Surveillance schedule per statement class |
| P12-3.92 | MUST | Iterations recorded, including those that found nothing |
| P12-3.93 | MUST | Lapse recorded, not silent |
| P12-3.94 | MUST | Overdue surveillance population exposed |
| P12-3.95 | MUST | Projections marked as such |
| P12-3.96 | MUST | Aggregate carries its denominator |
| P12-3.97 | MUST NOT | No single figure for a part |
| P12-3.98 | MUST NOT | No colour or grade as a projection |
| P12-4.1 | MUST | Operations defined over the entities of section 3 |
| P12-4.2 | MUST | Idempotency key accepted |
| P12-4.3 | MUST | Authorisation obtained per operation |
| P12-4.4 | MUST | One outcome per operation |
| P12-4.5 | MUST | Refusals recorded |
| P12-4.6 | MUST NOT | No operation that alters a finding or an evidence item |
| P12-4.7 | MUST NOT | No write to an assessed component outside a probe |
| P12-4.8 | MUST | Registration refused without a part version |
| P12-4.9 | MUST | Classification refused without a reason where not externally observable |
| P12-4.10 | MUST | Plan refused without a frame |
| P12-4.11 | MUST | Plan refused without an independence declaration |
| P12-4.12 | MUST | Plan refused where the assessor is out of scope |
| P12-4.13 | MUST | Probe registration refused without an expected outcome |
| P12-4.14 | MUST | Trust base item refused without a consequence |
| P12-4.15 | MUST | Evidence refused without provenance |
| P12-4.16 | MUST | Probe refused without a permission citation |
| P12-4.17 | MUST | Finding refused without evidence |
| P12-4.18 | MUST | Satisfied finding refused on self report alone |
| P12-4.19 | MUST | Statement refused without method, depth, coverage and frame |
| P12-4.20 | MUST | Statement refused without a validity interval and decay basis |
| P12-4.21 | MUST | Nonconformity refused with this component as owner |
| P12-4.22 | MUST | Acceptance refused without expiry, authorisation and reason |
| P12-4.23 | MUST | Closure refused without a reassessment finding |
| P12-4.24 | MUST | Run closure records the shortfall |
| P12-4.25 | MUST | Findings retrievable by criterion and by object |
| P12-4.26 | MUST | Point in time query supported |
| P12-4.27 | MUST | Assessability classification published |
| P12-4.28 | MUST | Trust base published |
| P12-4.29 | MUST NOT | No state change from a read |
| P12-4.30 | MUST | Expired statements returned as expired |
| P12-4.31 | MUST | Qualifications returned with every statement |
| P12-4.32 | MUST NOT | No assumption of conformance |
| P12-4.33 | MUST NOT | No assumption that an unassessed criterion is satisfied |
| P12-4.34 | MUST NOT | No assumption of currency |
| P12-4.35 | MUST NOT | No assumption of independence |
| P12-4.36 | MUST NOT | No assumption that this component was itself assessed |
| P12-4.37 | MUST | Coverage bounds every inference |
| P12-4.38 | MUST | Reads treated as fallible |
| P12-4.39 | MUST NOT | No proceeding on an authorisation failure |
| P12-4.40 | MUST | Unavailability recorded as unavailability |
| P12-4.41 | MUST | Event per finding and per statement |
| P12-4.42 | MUST | Event carries the qualifications |
| P12-4.43 | MUST | Events delivered to the ledger |
| P12-4.44 | MUST | Falsification event distinct |
| P12-4.45 | MUST | Reclassification event |
| P12-4.46 | MUST | Trust base change event |
| P12-4.47 | MUST | Acceptance expiry event |
| P12-4.48 | MUST | Probe detection event |
| P12-4.49 | SHOULD | Self report reliance signal |
| P12-5.1 | MUST | States held as transitions |
| P12-5.2 | MUST | One state per axis per instant |
| P12-5.3 | MUST NOT | No derivation of one axis from another |
| P12-5.4 | MUST | Transitions carry authorisation where required |
| P12-5.5 | MUST | Illegal transitions recorded |
| P12-5.6 | MUST NOT | No unlisted transition |
| P12-5.7 | MUST | Reclassification always permitted and always recorded |
| P12-5.8 | MUST | Findings tied to the class in force |
| P12-5.9 | MUST | Reclassification to assessable reopens the population |
| P12-5.10 | MUST | Abandonment reasoned |
| P12-5.11 | MUST | Invalidation propagates to statements |
| P12-5.12 | MUST NOT | No reopening of a closed run |
| P12-5.13 | MUST | Overdue surveillance visible in the state |
| P12-5.14 | MUST | Falsified is terminal and retained |
| P12-5.15 | MUST NOT | No reinstatement |
| P12-5.16 | MUST | Superseded distinguished from expired |
| P12-5.17 | MUST | Criterion withdrawal closes without a claim of remediation |
| P12-5.18 | MUST | Dispute does not close |
| P12-5.19 | MUST | Acceptance expiry automatic |
| P12-5.20 | MUST | Abandoned in place recorded, never silent |
| P12-5.21 | MUST | Compromised probes retired |
| P12-5.22 | MUST NOT | No probe deleted from the record |
| P12-5.23 | MUST | Falsified assumption escalated |
| P12-5.24 | MUST | Assumption removal recorded |
| P12-6.1 | MUST | Six functions distinguished |
| P12-6.2 | MUST | Determination separated from decision |
| P12-6.3 | MUST | Review recorded |
| P12-6.4 | MUST NOT | No attestation without a decision |
| P12-6.5 | MUST | Reviewer distinct from determiner where depth is comprehensive |
| P12-6.6 | MUST | Finding reproducible from its evidence |
| P12-6.7 | MUST | Re-performance supported |
| P12-6.8 | MUST NOT | No finding dependent on the assessor's identity |
| P12-6.9 | MUST | Divergence between assessors exposed |
| P12-6.10 | MUST NOT | No clock in a finding |
| P12-6.11 | MUST | Criteria extracted by a declared method |
| P12-6.12 | MUST | Extraction count reconciled against the part |
| P12-6.13 | MUST | Discrepancy reported to the part's author |
| P12-6.14 | MUST NOT | No assessment against an unresolved criterion |
| P12-6.15 | MUST | Version change triggers reclassification review |
| P12-6.16 | MUST | Method appropriate to the class |
| P12-6.17 | MUST | Depth and coverage declared per method application |
| P12-6.18 | MUST NOT | No interview as sole evidence for a mechanism |
| P12-6.19 | MUST NOT | No examination of documentation as sole evidence for a behaviour |
| P12-6.20 | MUST | Elicitation required where the class requires it |
| P12-6.21 | MUST | Construction only findings marked as inspection |
| P12-6.22 | MUST | Weight ordered and declared |
| P12-6.23 | MUST NOT | No satisfied finding at self reported provenance |
| P12-6.24 | MUST | Reliance proportion computed |
| P12-6.25 | MUST | Contradicting evidence resolved explicitly |
| P12-6.26 | MUST NOT | No preference for the assessed component's account |
| P12-6.27 | MUST | Absence of evidence distinguished from evidence of absence |
| P12-6.28 | MUST | Enumerability determined before sampling |
| P12-6.29 | MUST NOT | No sample from a non enumerable frame |
| P12-6.30 | MUST | Attestation obtained by an independent channel |
| P12-6.31 | MUST | Assessed component's figure tested, not accepted |
| P12-6.32 | MUST NOT | No acceptance of a reported population figure as a finding |
| P12-6.33 | MUST | Unenumerable residue reported with every coverage figure |
| P12-6.34 | MUST NOT | No estimate of a residue presented as measured |
| P12-6.35 | MUST | Second enumeration used where one exists |
| P12-6.36 | MUST | Non response recorded as non response |
| P12-6.37 | MUST | Non response rate published |
| P12-6.38 | MUST | Permission required per part |
| P12-6.39 | MUST | Coverage gap declared where permission is absent |
| P12-6.40 | MUST | Conformance instance used where production is forbidden |
| P12-6.41 | MUST | Expected outcome fixed before introduction |
| P12-6.42 | MUST | Probe selection unpredictable |
| P12-6.43 | MUST | Method class published, instances withheld |
| P12-6.44 | MUST | Indistinguishability tested, not assumed |
| P12-6.45 | MUST | Detection invalidates the ordinary inference |
| P12-6.46 | MUST | Side effects bounded and reversed |
| P12-6.47 | MUST NOT | No probe that could cause a nonconformity |
| P12-6.48 | MUST | Decision cites the findings |
| P12-6.49 | MUST NOT | No decision beyond the findings |
| P12-6.50 | MUST | Attestation party class determined by independence |
| P12-6.51 | MUST NOT | No attestation of an object the attesting party provided |
| P12-6.52 | MUST | Scope of attestation recorded |
| P12-6.53 | MUST | Cadence applied per statement class |
| P12-6.54 | MUST | Object change detected, not awaited |
| P12-6.55 | MUST | Frame change treated as an object change |
| P12-6.56 | MUST NOT | No extension of a validity interval |
| P12-6.57 | MUST | Lapse exposed |
| P12-6.58 | MUST | Concurrent findings on one statement serialised |
| P12-6.59 | MUST | Repeated evidence recording idempotent |
| P12-6.60 | MUST | Assessment effort bound declared |
| P12-6.61 | MUST | Bound reached recorded in coverage |
| P12-6.62 | MUST | Own criteria registered |
| P12-6.63 | MUST | Own classification performed by the external assessor |
| P12-6.64 | MUST | Own findings recorded as received, not made |
| P12-6.65 | MUST NOT | No amendment of a received finding |
| P12-6.66 | MUST | Own nonconformities exposed identically |
| P12-6.67 | MUST | Absence of external assessment exposed as a nonconformity |
| P12-6.68 | MUST NOT | No remediation |
| P12-6.69 | MUST NOT | No criterion interpretation binding on the part |
| P12-6.70 | MUST NOT | No risk judgement |
| P12-6.71 | MUST NOT | No prioritisation of nonconformities |
| P12-6.72 | MUST | Severity derived from modality only where derived at all |
| P12-7.1 | MUST | One enumeration per value |
| P12-7.2 | MUST NOT | No value outside the enumerations |
| P12-7.3 | MUST | Properties of an outcome exposed |
| P12-7.4 | MUST | Satisfied requires provenance above self report |
| P12-7.5 | MUST NOT | No collapse to satisfied |
| P12-7.6 | MUST NOT | No collapse to not satisfied |
| P12-7.7 | MUST | Five unassessable causes distinguished |
| P12-7.8 | MUST | Out of scope distinguished from not reached |
| P12-7.9 | MUST | Access refused attributed |
| P12-7.10 | MUST | Elicitation forbidden attributed to the part |
| P12-7.11 | MUST | Conflict retained, not resolved by preference |
| P12-7.12 | MUST NOT | No conformance outcome |
| P12-7.13 | MUST NOT | No aggregate outcome over a part |
| P12-7.14 | MUST NOT | No pass or fail vocabulary |
| P12-7.15 | MUST | Satisfied bounded to the statement |
| P12-7.16 | MUST | Not falsified is the strongest outcome |
| P12-7.17 | MUST NOT | No not falsified without an attempt |
| P12-7.18 | MUST | Unfalsifiable claims reported to their author |
| P12-7.19 | MUST | Partial falsification enumerated on both sides |
| P12-7.20 | MUST | Inconclusive reasoned |
| P12-7.21 | MUST | Refusal reasons distinguished |
| P12-7.22 | MUST | Self assessment refusal explicit |
| P12-7.23 | MUST | Three properties exposed |
| P12-7.24 | MUST NOT | No fault reported as a finding |
| P12-7.25 | MUST | Invariant violation halts issuance |
| P12-7.26 | MUST | Outcome carried with its qualifications |
| P12-7.27 | MUST NOT | No aggregation losing the distinctions |
| P12-7.28 | MUST | Counts report each outcome as its own category |
| P12-7.29 | MUST | Non results retained where unconsumed |
| P12-8.1 | MUST | Completeness of each record declared |
| P12-8.2 | MUST NOT | No coverage figure without its frame provenance |
| P12-8.3 | MUST | Grain stated with every count |
| P12-8.4 | MUST | Criterion counts state their assessability classes |
| P12-8.5 | MUST | Finding counts state their provenance distribution |
| P12-8.6 | MUST NOT | No count spanning part versions |
| P12-8.7 | MUST | Object grain stated |
| P12-8.8 | MUST | Every plan recorded before its evidence |
| P12-8.9 | MUST | Every evidence item recorded with provenance |
| P12-8.10 | MUST | Every finding recorded with its qualifications |
| P12-8.11 | MUST | Every elicitation recorded |
| P12-8.12 | MUST | Every sample recorded in full |
| P12-8.13 | MUST | Every frame examination recorded |
| P12-8.14 | MUST | Every reclassification recorded |
| P12-8.15 | MUST | Every acceptance and expiry recorded |
| P12-8.16 | MUST | Every dispute recorded |
| P12-8.17 | MUST | Every trust base change recorded |
| P12-8.18 | MUST | Every external assessment of itself recorded |
| P12-8.19 | MUST | The plan behind any finding |
| P12-8.20 | MUST | The evidence behind any finding |
| P12-8.21 | MUST | The clause text a finding was made against |
| P12-8.22 | MUST | The independence of any assessment |
| P12-8.23 | MUST | The frame and the sample |
| P12-8.24 | MUST | The assessability history of any criterion |
| P12-8.25 | MUST | The trust base at any instant |
| P12-8.26 | MUST | Whether this component was itself assessed at any instant |
| P12-8.27 | MUST NOT | No reconstruction dependent on this component running |
| P12-8.28 | MUST | Unassessable criterion population per part |
| P12-8.29 | MUST | Elicitation forbidden population |
| P12-8.30 | MUST | Self report reliance proportion |
| P12-8.31 | MUST | Never assessed criterion population |
| P12-8.32 | MUST | Coverage over unenumerable frames |
| P12-8.33 | MUST | Non response rate per attested sample |
| P12-8.34 | MUST | Overdue surveillance population |
| P12-8.35 | MUST | Expired and superseded statement population |
| P12-8.36 | MUST | Accepted nonconformity population |
| P12-8.37 | MUST | Repeatedly accepted population |
| P12-8.38 | MUST | Disputed finding population |
| P12-8.39 | MUST | Probes in place population |
| P12-8.40 | MUST | Compromised probe population |
| P12-8.41 | MUST | Assessor divergence population |
| P12-8.42 | MUST | Its own nonconformity population |
| P12-8.43 | SHOULD | Trust base growth signal |
| P12-8.44 | MUST | Package assemblable for a finding |
| P12-8.45 | MUST | Package assemblable for a statement |
| P12-8.46 | MUST | Package states what it omits |
| P12-8.47 | MUST | Package integrity protected |
| P12-8.48 | MUST | Records outlive the object |
| P12-8.49 | MUST NOT | No alteration of a finding, evidence item, plan or issued statement |
| P12-8.50 | MUST NOT | No deletion of contradicting evidence |
| P12-8.51 | MUST NOT | No removal of a nonconformity |
| P12-8.52 | MUST | Retention notified to the components relied upon |
| P12-9.1 | MUST | Closed sets not extended |
| P12-9.2 | MUST | Open sets extended only through a registry |
| P12-9.3 | MUST NOT | No new outcome for a new subject |
| P12-9.4 | MUST | Registration before use |
| P12-9.5 | MUST | Definition mandatory at registration |
| P12-9.6 | MUST | Registration attributable |
| P12-9.7 | MUST NOT | No meaning change under a registered identifier |
| P12-9.8 | MUST | Retirement recorded, findings retained |
| P12-9.9 | MUST | Probe kind semantics registered |
| P12-9.10 | MUST | Indistinguishability method registered |
| P12-9.11 | MUST | Applicability recorded per part |
| P12-9.12 | MUST | Selection method registered |
| P12-9.13 | MUST | Enumerability requirement recorded |
| P12-9.14 | MUST NOT | No scheme registered that operates on a non enumerable frame |
| P12-9.15 | MUST | Scope recorded per assessor |
| P12-9.16 | MUST | Competence basis recorded |
| P12-9.17 | MUST | Mutual assessment recorded |
| P12-9.18 | MUST NOT | No assessor registered as its own peer |
| P12-9.19 | MUST | Parts registered with their versions |
| P12-9.20 | MUST | Elicitation permission recorded per part |
| P12-9.21 | MUST | Read only requirement recorded per part |
| P12-9.22 | MUST | Conflicting requirements recorded |
| P12-10.1 | MUST | Cited edition recorded |
| P12-10.2 | MUST | Basis marked |
| P12-10.3 | MUST | Requirements of this part alone identified |
| P12-11.1 | MUST NOT | No single figure per component |
| P12-11.2 | MUST NOT | No satisfied finding at self reported provenance |
| P12-11.3 | MUST | Not assessed reported as its own outcome |
| P12-11.4 | MUST | Denominator declared |
| P12-11.5 | MUST NOT | No plan amended after evidence |
| P12-11.6 | MUST NOT | No convenience sample described as probabilistic |
| P12-11.7 | MUST NOT | No sample from a non enumerable frame |
| P12-11.8 | MUST NOT | No expired statement presented as current |
| P12-11.9 | MUST | Not established set carried with the statement |
| P12-11.10 | MUST | Indistinguishability tested |
| P12-11.11 | MUST NOT | No advance publication of probe instances |
| P12-11.12 | MUST NOT | No advisor as assessor |
| P12-11.13 | MUST NOT | No remediation by the harness |
| P12-11.14 | MUST | Absence of external assessment recorded as a nonconformity |
| P12-11.15 | MUST | Trust base enumerated and published |
| P12-11.16 | MUST NOT | No conformance grade defined |
| P12-11.17 | MUST | Coverage expressed over a declared frame |
| P12-11.18 | MUST | Repeated acceptance exposed |
| P12-11.19 | MUST NOT | No closure without a reassessment |
| P12-11.20 | MUST | Statement superseded on object change |
| P12-11.21 | MUST NOT | No interview as sole evidence for a mechanism |
| P12-11.22 | MUST | Absence distinguished from not found |
| P12-11.23 | MUST | Finding re-performable from its record |
| P12-11.24 | MUST | Trust base reviewed on a cadence |
| P12-12.1 | MUST | Clause text resolved, not held |
| P12-12.2 | MUST | Point in time resolution required |
| P12-12.3 | MUST | Records treated as records |
| P12-12.4 | MUST | Retention obligation notified |
| P12-12.5 | MUST | Declarative statements evaluated by Part 2 |
| P12-12.6 | MUST NOT | No non verdict recorded as a finding |
| P12-12.7 | MUST | Events emitted to the ledger |
| P12-12.8 | MUST NOT | No chain asserted |
| P12-12.9 | MUST | Ledger assessed like any other component |
| P12-12.10 | MUST | Definitions resolved, not interpreted |
| P12-12.11 | MUST | Definition change triggers a reclassification review |
| P12-12.12 | MUST NOT | No risk or priority computed |
| P12-12.13 | MUST | Findings supplied as inputs |
| P12-12.14 | MUST | Run state is a fact |
| P12-12.15 | MUST NOT | No finding gated by a process |
| P12-12.16 | MUST | Authorisation obtained per operation |
| P12-12.17 | MUST NOT | No authorisation decision rendered |
| P12-12.18 | MUST | Read only assessment where the part requires it |
| P12-12.19 | MUST | Declared spaces examined, not accepted |
| P12-12.20 | MUST | Remediation work obtained, not performed |
| P12-12.21 | MUST NOT | No closure from task completion |
| P12-12.22 | MUST | Interview conducted as work, recorded as evidence |
| P12-12.23 | MUST NOT | No validation performed |
| P12-12.24 | MUST | Evaluated extent assessed by elicitation |
| P12-12.25 | MUST NOT | No acceptance of a reported coverage figure |
| P12-12.26 | MUST | Attestation obtained independently of the reporting component |
| P12-12.27 | MUST | Unreported population treated as a claim |
| P12-12.28 | MUST | Party identities obtained |
| P12-12.29 | MUST NOT | No evidence octets held |
| P12-12.30 | MUST | Address recomputed independently |
| P12-12.31 | MUST | Outcome taxonomy elicited |
| P12-12.32 | MUST | Durability and independence treated as claims |
| P12-12.33 | MUST | Model produced determination recorded as evidence, not as a finding |
| P12-12.34 | MUST | Human decision required for a finding |
| P12-12.35 | MUST | Non determinism recorded |
| P12-12.36 | MUST | Model use in an assessment declared |
| P12-12.37 | MUST | Authority declared, not assumed |
| P12-12.38 | MUST | Composition clauses assessed as clauses |
| P12-12.39 | MUST | Cross part conflicts reported to composition |
| P12-12.40 | MUST | Assessment gap exposed to composition |
| P12-13.1 | MUST | Unverified reciprocals declared |
| P12-13.2 | SHOULD | Register maintained |
| P12-13.3 | MUST | Gaps declared, not filled |
| P12-13.4 | SHOULD | Open questions carried forward |

### Derived counts

Every figure below is derived by extraction from the clause text of this document and not asserted independently. The grain of counting is stated for each figure. A clause is one line of the document matching the clause heading form given under Binding of requirement language, that is, an identifier of the form `P12-S.N`, a modality in parentheses, and a subject label. Narrative sentences containing a requirement keyword are not clauses and are not counted; per that same section they are not binding. No clause of this part states a requirement keyword in its prose, so the modality of a clause is unambiguous.

**Total clauses.** 456. Grain: one clause heading.

**By modality.** Grain: one clause heading, counted once against its single declared modality.

| Modality | Clauses | Share |
| --- | --- | --- |
| MUST | 331 | 72.6% |
| MUST NOT | 121 | 26.5% |
| SHOULD | 4 | 0.9% |
| SHOULD NOT | 0 | 0.0% |
| MAY | 0 | 0.0% |
| **All** | **456** | **100.0%** |

**Absolute requirements.** 452 clauses carry MUST or MUST NOT and are therefore conditions of conformance. 4 carry SHOULD or SHOULD NOT and require a recorded reason where not satisfied. 0 carry MAY and constrain nothing. Grain: one clause heading. These three figures sum to the total.

**By section.** Grain: one clause heading, attributed to the numbered section in which its heading appears.

| Section | Title | Clauses | MUST | MUST NOT | SHOULD | SHOULD NOT | MAY |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Scope and responsibilities | 30 | 16 | 14 | 0 | 0 | 0 |
| 2 | Terminology | 9 | 1 | 8 | 0 | 0 | 0 |
| 3 | Data model | 98 | 73 | 25 | 0 | 0 | 0 |
| 4 | Interfaces | 49 | 39 | 9 | 1 | 0 | 0 |
| 5 | State model | 24 | 19 | 5 | 0 | 0 | 0 |
| 6 | Execution semantics | 72 | 52 | 20 | 0 | 0 | 0 |
| 7 | Outcome and failure taxonomy | 29 | 20 | 9 | 0 | 0 | 0 |
| 8 | Observability and the audit record | 52 | 45 | 6 | 1 | 0 | 0 |
| 9 | Extension model | 22 | 18 | 4 | 0 | 0 | 0 |
| 10 | Standards and specifications | 3 | 3 | 0 | 0 | 0 | 0 |
| 11 | Anti patterns | 24 | 12 | 12 | 0 | 0 | 0 |
| 12 | Boundaries with other parts | 40 | 31 | 9 | 0 | 0 | 0 |
| 13 | What could not be established | 4 | 2 | 0 | 2 | 0 | 0 |
| **All** | | **456** | **331** | **121** | **4** | **0** | **0** |

**Ordinal integrity.** In this version, the highest ordinal in each section equals the number of clauses in that section, so no identifier has yet been retired. This will cease to be true at the first clause removal, and the count rather than the highest ordinal is then the figure to rely on.

**Sourced clauses.** 10 clauses carry a **Source.** note naming the specification or published work their subject rests on. Grain: one clause heading carrying at least one Source note. Section 10.1 states how the notes are to be read and section 13.1 lists the sources not obtained in full text.

**Cross part citations.** This part cites nine clauses of other parts: P7-12.32, P7-12.34, P8-12-31, P8-12-32, P9-12-34, P9-12-35, P11-3.48, P11-12.35 and P11-12.36. Every one was verified against the delivered text of the part concerned. Grain: one distinct clause identifier cited.

## 1. Scope and responsibilities

### 1.1 What this component is

This component determines whether the other twelve components do what this standard requires of them, and it does so knowing that its own conclusions are claims of the same kind it evaluates.

Twelve parts have now written some five thousand clauses of the form an implementation must do this. Nine of those parts contain a clause forbidding a component from presenting its own analysis as assurance, and each delegates the assessment here. This component is therefore the place where the standard's claims about itself either become evidenced or are revealed as unevidenced, and the most useful thing it can produce is not a conformance report but an honest account of which of those five thousand clauses can be assessed at all.

**P12-1.1 (MUST) Clause register owned.** An implementation must own the register of every clause of this standard it assesses against, resolved from the part that states it and recorded with that part's version.

**P12-1.2 (MUST) Assessability classification owned.** An implementation must own the classification of every registered clause by whether and how it can be assessed, per section 3.6.

**P12-1.3 (MUST) Claims owned.** An implementation must own the claim register, being the record of every proposition about a component that this component evaluates.

**P12-1.4 (MUST) Assessment plans owned.** An implementation must own the assessment plan, being the declared objectives, determination statements, methods, objects, depth, coverage and frame of an assessment before it is performed.

**P12-1.5 (MUST) Evidence items owned.** An implementation must own every item of evidence it gathers, with its provenance.

**P12-1.6 (MUST) Findings owned.** An implementation must own the finding, being the determination reached about one clause for one component from stated evidence.

**P12-1.7 (MUST) Assurance statements owned.** An implementation must own the assurance statement, being a conclusion about a claim carrying its method, its depth, its coverage, its validity interval and what it did not establish.

**P12-1.8 (MUST) Probes and elicitations owned.** An implementation must own the probe, being an input of known expected outcome introduced in order to elicit behaviour, and the record of every elicitation performed.

**P12-1.9 (MUST) Frame declarations owned.** An implementation must own the frame declaration, being the statement of the population an assessment covers and whether that population can be enumerated.

**P12-1.10 (MUST) Independence declarations owned.** An implementation must own the declaration of the independence of every assessor from the object it assesses.

**P12-1.11 (MUST) The trust base owned.** An implementation must own the trust base, being the enumerated set of propositions it assumes and does not assess.

**P12-1.12 (MUST) Nonconformity records owned.** An implementation must own the nonconformity record, its owner and its disposition.

**P12-1.13 (MUST) Surveillance schedules owned.** An implementation must own the schedule by which an assurance statement is maintained or allowed to lapse.

**P12-1.14 (MUST) Its own external assessment record owned.** An implementation must own the record of the assessment of itself performed by a party other than itself.

### 1.2 What this component is not

**P12-1.15 (MUST NOT) Not the author of the criteria.** An implementation must not write, amend or interpret the clauses it assesses against, and must resolve them from the part that states them.

**P12-1.16 (MUST NOT) Not a remediator.** An implementation must not correct, configure or repair any component it assesses, and must not accept a remediation task in respect of a nonconformity it recorded.

**P12-1.17 (MUST NOT) Not an authority over any assessed component's state.** An implementation must not write to an assessed component except under a declared elicitation permission per section 6.7.

**P12-1.18 (MUST NOT) Not a decision point for access.** An implementation must not decide whether a party may read an assessment result, and must obtain that decision from `Part 7`.

**P12-1.19 (MUST NOT) Not the audit ledger.** An implementation must not represent its own records as the evidentiary chain of any determination another component made, and must emit its events to `Part 3`.

**P12-1.20 (MUST NOT) Not a rules engine.** An implementation must not evaluate a business constraint, and where a determination statement requires the evaluation of a declarative rule it must obtain the verdict from `Part 2`.

**P12-1.21 (MUST NOT) Not a certification body.** An implementation must not issue a statement of conformity of the kind a third party certification scheme issues, and must not represent an assurance statement as a certificate.

**P12-1.22 (MUST NOT) Not an accreditor.** An implementation must not attest to the competence of any assessor including itself, and must record such an attestation as obtained from outside the system where one exists.

**P12-1.23 (MUST NOT) Not the owner of any nonconformity.** An implementation must record the owner of every nonconformity as a party outside itself and must not own one.

**P12-1.24 (MUST NOT) Not a schema, document, reference or artifact authority.** An implementation must not version a schema, govern a document, hold reference content or store artifact octets, and must obtain each from `Part 9`, `Part 1`, `Part 10` and `Part 11`.

**P12-1.25 (MUST NOT) Not a work manager.** An implementation must not manage the work by which a nonconformity is remediated or a finding is disputed, and must obtain the work item from `Part 8`.

### 1.3 The three failures this part exists to prevent

*The assurance that asserts conformity.* An assessment reaches a conclusion and the conclusion is written as a statement that the component conforms. It cannot be. A finite assessment establishes that a finite set of falsification attempts failed under a stated method at a stated depth over a stated population, and the strongest honest expression of that is that the claim was not falsified. Section 3.2 states the position and section 7.3 removes the vocabulary in which the stronger statement could be made: no outcome of this part means conformant. A reviewer who finds this pedantic should consider that every conformance report they have read asserted a universal from a sample without stating the sample.

*The satisfied finding that rests on the component's own word.* The assessor asks, the component answers, the answer is recorded as evidence and the clause is marked satisfied. Nine parts forbid a component from presenting its own analysis as assurance, and an assessor that accepts the component's analysis as evidence has laundered the same claim through a second party without adding anything. Section 3.8 classifies evidence by provenance and section 7.2 provides a distinct finding for a clause assessed on self report alone, so that the proportion of an assessment resting on the assessed party's testimony is countable.

*The regress concealed by one more layer.* Who verifies the verifier is a question with no terminating answer inside any system, and the failure is not that it does not terminate but that implementations pretend it does. This part terminates it in three declared places: an external assessment of this component by a party outside it, a mutual assessment among assessors rather than a hierarchy above them, and an enumerated trust base of propositions assumed without assessment. Section 3.4 specifies all three. The trust base is the important one, because every assurance system has one and the ones that do not write it down are asserting confidence in things nobody has looked at.

### 1.4 The reader this part is written for

A reviewer should read section 3.2, then section 3.6, then section 7.2. Section 3.2 establishes that assurance is asymmetric, which determines the vocabulary of the whole part. Section 3.6 classifies clauses by assessability and is the section whose output will be most unwelcome, because it requires this component to publish how many of the standard's own clauses cannot be assessed. Section 7.2 is where the part is testable.

Three things in this part are most likely to be wrong. Section 13.2 records that an assurance statement expressed as not falsified may be unusable by the parties who need assurance, and that the pressure to convert it into a conformance claim will be constant and will come from people with legitimate needs. Section 13.4 records that the mechanism this part supplies for the three unreported populations that `Part 7`, `Part 10` and `Part 11` handed forward works only over a frame that can be enumerated, and that making the frame enumerable is not this component's to do. And section 13.6 records that publishing an assessment method makes the method satisfiable without the property, which is a problem this part constrains and does not solve.

**P12-1.26 (MUST) Assessment is of clauses, not of systems.** An implementation must express every finding against a named clause of a named part at a named version and must not express a finding against a component as a whole.

**P12-1.27 (MUST NOT) No assessment anticipated of anything outside this standard.** An implementation must not represent an assessment against this standard as an assessment against any other body of requirements.

**P12-1.28 (MUST) Scope of every assessment declared.** An implementation must declare, for every assessment, the parts, clauses, components, instances and interval it covers, and must not perform an assessment whose scope is undeclared.

**P12-1.29 (MUST NOT) No conformance level defined.** An implementation must not define or assign a graded conformance level, and must express depth and coverage as declared attributes of an assessment rather than as a grade of the object.

**P12-1.30 (MUST NOT) No self assessment.** An implementation must not assess its own conformance to this part, and must obtain that assessment from a party outside itself per section 3.4.

## 2. Terminology

### 2.1 Terms owned by this part

**Criterion.** One clause of one part of this standard at one version, resolved from that part and not restated. The criteria of an assessment are its clauses and nothing else.

**Object of assessment.** The thing a finding is about: an implementation of a part, an instance of it, a record it holds or a behaviour it exhibits. The term is taken from the conformity assessment vocabulary, which uses object of conformity assessment for the entity to which specified requirements apply.

**Claim.** A proposition about an object of assessment that is capable of being false. A component makes claims explicitly, by publishing a figure, and implicitly, by operating as though it conformed.

**Assessment.** The activity of gathering evidence about claims against criteria and reaching findings.

**Assessment plan.** The declaration, made before evidence is gathered, of the objectives, determination statements, methods, objects, depth, coverage, frame and sampling of an assessment.

**Determination statement.** One statement, derived from one criterion, whose truth or falsity the assessment seeks to establish. The construction is taken from the security control assessment guidance, in which an assessment objective comprises determination statements linked to the content of the control so that findings are traceable to the requirement.

**Assessment method.** The means by which evidence is gathered. This part adopts four: examine, interview, test and elicit. The first three are taken from the security control assessment guidance; the fourth is added by this part and section 6.7 gives the reason.

**Assessment object.** The kind of thing a method is applied to: a specification, a mechanism, an activity, an individual or a record. The four kinds other than record are taken from the same guidance.

**Depth.** The declared rigour and level of detail of a method as applied. Taken from the same guidance, which defines depth with the values basic, focused and comprehensive.

**Coverage.** The declared scope and breadth of a method as applied, being which and how many objects were examined, tested or elicited and which individuals were interviewed. Taken from the same guidance, with the same three values, and extended by this part to require the frame over which coverage is expressed.

**Frame.** The population an assessment's coverage is expressed over.

**Frame enumerability.** Whether the members of a frame can be listed. A frame that cannot be enumerated cannot be sampled, and section 6.6 makes that a refusal rather than an approximation.

**Evidence item.** One record supporting or contradicting a determination statement, carrying its provenance.

**Evidence provenance.** How an evidence item was obtained: self reported by the assessed party, observed by the assessor, reconstructed independently by the assessor, or elicited by a probe. The four are a closed set and section 3.8 states the weight of each.

**Finding.** The determination reached about one determination statement for one object, from stated evidence, with an outcome from section 7.2.

**Assurance statement.** A conclusion about a claim, carrying the method, depth, coverage, frame, validity interval, the findings it rests on and what it did not establish. It is never a statement that a component conforms.

**Falsification attempt.** An act designed to produce evidence that a claim is false.

**Not falsified.** The strongest outcome available to an assurance statement, meaning that the declared falsification attempts did not succeed at the declared depth over the declared coverage of the declared frame.

**Probe.** An input of known expected outcome introduced into an assessed component in order to elicit a behaviour that could not be observed passively.

**Probe indistinguishability.** The property that an assessed component cannot distinguish a probe from ordinary input. Where it fails, elicited evidence is evidence about how the component treats probes.

**Elicitation permission.** The declaration, made by the part being assessed, of whether and under what conditions this component may introduce a probe into an implementation of it.

**Attestation.** The issue of a statement, based on a decision following review, that fulfilment of specified requirements has been demonstrated. The definition is that of the conformity assessment vocabulary and is adopted unchanged.

**First party attestation.** An attestation by the party that provides the object. The vocabulary calls this a declaration.

**Second party attestation.** An attestation by a party with a user interest in the object. The vocabulary records that no special term exists for it.

**Third party attestation.** An attestation by a party independent of the provider of the object and of user interests in it. The vocabulary calls the product of this certification, except where the object is a conformity assessment body, in which case it is accreditation.

**Independence.** The absence of a relationship between an assessor and an object that would be expected to affect the assessment. This part requires three forms to be declared separately: technical, managerial and financial.

**Peer assessment.** Assessment of a body against specified requirements by representatives of other bodies in, or candidates for, an agreement group. The vocabulary defines it, and this part adopts it as one of the three terminations of the regress.

**Trust base.** The enumerated set of propositions an assurance system assumes without assessing.

**Surveillance.** The systematic iteration of assessment activities as a basis for maintaining the validity of an assurance statement. The definition follows the conformity assessment vocabulary.

**Assurance decay.** The declared loss of the validity of an assurance statement with the passage of time or with a change to its object.

**Nonconformity.** A finding that a determination statement is not satisfied.

**Accepted nonconformity.** A nonconformity that an accountable party outside this component has accepted for a bounded interval with a recorded reason.

**Assessability class.** The classification of a criterion by whether and how it can be assessed, from the closed set in section 3.6.

### 2.2 Clauses governing terminology

**P12-2.1 (MUST NOT) No redefinition of another part's terms.** An implementation must not redefine a term this standard allocates to another part, and must use it with the meaning that part gives it.

**P12-2.2 (MUST NOT) Assurance not equated with conformity.** An implementation must not use assurance, assured or verified to mean that a component conforms.

**P12-2.3 (MUST NOT) Not falsified not equated with true.** An implementation must not present an outcome of not falsified as establishing that a claim is true.

**P12-2.4 (MUST NOT) Finding not equated with assurance statement.** An implementation must not present a finding about one determination statement as an assurance statement about a claim.

**P12-2.5 (MUST NOT) Coverage not equated with depth.** An implementation must not report one in place of the other and must report both.

**P12-2.6 (MUST NOT) Evidence not equated with testimony.** An implementation must not describe a self reported item as observed, reconstructed or elicited.

**P12-2.7 (MUST NOT) Attestation not equated with assessment.** An implementation must not treat the issue of a statement as the activity that produced it.

**P12-2.8 (MUST NOT) Trust base not equated with scope exclusion.** An implementation must not record an assumed proposition as merely out of scope, since the first is relied upon and the second is not.

**P12-2.9 (MUST) Kinds registered before use.** An implementation must register every assessment method, probe kind, sampling scheme, assessor and independence form before an assessment uses it, per section 9.

## 3. Data model

### 3.1 Type vocabulary

Types in this section are abstract and impose no representation. `identifier` is an opaque immutable string unique within its declared scope. `criterion-ref` is a reference to one clause of one part at one version. `instant` is a point in time with an offset from UTC and at least millisecond resolution. `interval` is a pair of instants, either bound of which may be open. `pin` is a reference resolving to a stated version of a stated object as it stood at a stated instant. `address` is a content address held by `Part 11`. `enum(...)` is a closed set unless the field description states otherwise.

**P12-3.1 (MUST) Types declared.** An implementation must declare the concrete representation it adopts for every abstract type in section 3.1 and must not vary it between records of one class.

**P12-3.2 (MUST) Criterion references carry the part version.** An implementation must include the version of the part in every criterion reference and must reject a reference that names a clause without one.

**P12-3.3 (MUST NOT) No representation dependent identity.** An implementation must not derive the identity of any record from its representation.

### 3.2 Assurance is asymmetric

This is the position on which the part turns, and it is the reason the part has no outcome meaning conformant.

An assessment applies a finite set of methods, at a declared depth, to a declared coverage of a declared frame, over a bounded interval. What it can establish is that a claim is false: one counterexample suffices, and a single failing probe disproves a universal claim about a component's behaviour completely and permanently. What it cannot establish is that a claim is true, because no finite number of successful checks exhausts the cases the claim quantifies over, and because the checks were selected by a method that determined what could be found.

The consequence is not that assurance is worthless. It is that the honest expression of a successful assessment is negative in form: the declared falsification attempts did not succeed. That statement is genuinely informative, and its information content is a function of how hard the attempts were, which is why depth, coverage and frame are mandatory on every assurance statement and why a statement without them says almost nothing. An assessment that examined documentation at basic depth over a convenience sample and found nothing wrong has established very little, and an assessment that planted a thousand probes across an enumerated frame and found nothing wrong has established a great deal, and both would be reported identically by a component whose vocabulary contains only conformant.

The standards this part rests on are more careful here than practice is. The conformity assessment vocabulary defines attestation as the issue of a statement that fulfilment has been demonstrated, which is a claim about a demonstration and not about the world. The security evaluation standards grade the rigour of an evaluation rather than the security of the product, so that a high evaluation assurance level is a statement about how hard anyone looked. Practice then converts both into a badge, and the badge is read as a property of the object.

**P12-3.4 (MUST) Assurance expressed negatively.** An implementation must express the strongest positive outcome of an assurance statement as not falsified and must not express any outcome as conformant, compliant or verified.

**P12-3.5 (MUST) Method, depth, coverage and frame mandatory.** An implementation must record the method, depth, coverage and frame on every assurance statement and must refuse to issue one that lacks any of the four.

**P12-3.6 (MUST) What was not established recorded.** An implementation must record, on every assurance statement, the determination statements within its scope that it did not assess and the assessability classes that prevented assessment.

**P12-3.7 (MUST) Falsification attempts enumerated.** An implementation must record the falsification attempts an assurance statement rests on, so that the strength of a not falsified outcome is derivable from the record rather than asserted.

**P12-3.8 (MUST NOT) No universal claim from a sample.** An implementation must not express a finding over a frame broader than the coverage it achieved.

**P12-3.9 (MUST) One counterexample decisive.** An implementation must record a claim as falsified on a single sound counterexample and must not require a proportion of failures.

**P12-3.10 (MUST NOT) No aggregation of a falsification into a rate.** An implementation must not present a falsified claim as a percentage of checks passed.

Clause P12-3.10 prevents the most common way a disproof is neutralised. A component claims that it never returns a certain value; one probe shows that it does; the result is reported as a 99.9 per cent pass rate. The claim was universal and it is false, and the rate describes the sample rather than the claim.

### 3.3 Entity inventory

The table is normative as to which entities exist and which component owns each.

| Entity | Immutable once written | Owned here |
|---|---|---|
| Criterion registration | yes, per part version | yes |
| Assessability classification | no, its class may be revised with a reason | yes |
| Claim | yes | yes |
| Assessment plan | yes | yes |
| Assessment run | no, its state changes | yes |
| Evidence item | yes | yes |
| Finding | yes | yes |
| Assurance statement | no, its state changes | yes |
| Probe definition | no, versions are | yes |
| Elicitation record | yes | yes |
| Frame declaration | yes | yes |
| Sampling record | yes | yes |
| Independence declaration | no | yes |
| Assessor registration | no | yes |
| Trust base item | no, its state changes | yes |
| Nonconformity record | no, its disposition changes | yes |
| Surveillance schedule | no | yes |
| External assessment record | yes | yes |
| The clauses themselves | — | no, the part that states them |
| Authorisation decision | — | no, `Part 7` |
| Evidentiary chain | — | no, `Part 3` |
| Evidence artifact octets | — | no, `Part 11` |
| Remediation work | — | no, `Part 8` |

**P12-3.11 (MUST) Inventory normative.** An implementation must hold every entity the table in section 3.3 marks as owned here and must not hold as its own any entity the table allocates to another part.

**P12-3.12 (MUST) Immutability observed.** An implementation must not modify any record the table in section 3.3 marks immutable once written, and must express a correction as a new record superseding it.

### 3.4 The regress, and its three terminations

The brief for this part asks for the verification of the verifications. There is no answer of the form a higher verifier, because the higher verifier is a system with claims of its own. There are three answers that are not regresses, and this part requires all three.

The first is external assessment. This component's conformance to this part is assessed by a party that is not this component, and the record of that assessment is held here as evidence rather than produced here as a conclusion. That does not terminate the regress; it moves it one step and makes the step visible.

The second is mutual assessment rather than hierarchy. The conformity assessment world terminates its own chain horizontally: a body attesting to an object is certified, a body attesting to a body is accredited, and the accreditation bodies are peer assessed by representatives of other bodies in an agreement group. Nothing sits above the group. The confidence rests on the group members having an interest in each other's rigour and on the assessment being mutual. This part adopts the structure: where more than one assessor exists, they assess each other, and the results are recorded here.

The third is the declared trust base. Every assurance system rests on propositions it does not assess: that the clock is approximately right, that the records it reads were not fabricated by the party that produced them, that the cryptographic primitives hold, that the assessor's own tooling computes what it claims. These are not eliminable. They are enumerable, and the difference between a system that enumerates them and one that does not is the difference between bounded and unbounded confidence. Metrology solves the same problem the same way, terminating a traceability chain at a primary standard maintained outside the measuring system and stating an uncertainty rather than claiming exactness.

**P12-3.13 (MUST) External assessment obtained.** An implementation must obtain an assessment of its own conformance to this part from a party that is not itself, and must record it as an external assessment record.

**P12-3.14 (MUST NOT) No self assessment recorded as an assessment.** An implementation must not record its own examination of itself as an assessment of its conformance to this part, and may record it only as a self declaration.

**P12-3.15 (MUST) Absence of an external assessment declared.** An implementation must publish the fact that no external assessment of itself exists, where none does, and must not present its own declaration in place of one.

**P12-3.16 (MUST) Mutual assessment where more than one assessor exists.** An implementation must record, where the estate registers more than one assessor, the assessments those assessors made of each other. **Source.** The conformity assessment vocabulary defines peer assessment as assessment of a body against specified requirements by representatives of other bodies in, or candidates for, an agreement group, and it is the mechanism by which the accreditation chain terminates without a superior authority.

**P12-3.17 (MUST) Trust base enumerated.** An implementation must publish the trust base as an enumerated set of propositions, each with the reason it is not assessed.

**P12-3.18 (MUST NOT) No unenumerated assumption.** An implementation must not rely on an unassessed proposition that is not in the published trust base.

**P12-3.19 (MUST) Trust base reviewed on a declared cadence.** An implementation must review the trust base at a declared cadence and must record each review, since an assumption that was reasonable when made is the thing most likely to have become false without anyone noticing.

**P12-3.20 (MUST) Trust base items classed by consequence.** An implementation must record, for every trust base item, what would be unassessable if the proposition were false.

**P12-3.21 (MUST NOT) No termination claimed.** An implementation must not represent the three terminations as removing the regress, and must record that they bound it.

### 3.5 The criterion register

| Field | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `criterion_registration_id` | identifier | yes | 1 | Not possible |
| `criterion_ref` | criterion-ref | yes | 1 | Not possible |
| `part` | identifier | yes | 1 | Not possible |
| `part_version` | string | yes | 1 | Not possible |
| `clause_identifier` | string | yes | 1 | Not possible |
| `modality` | enum(`MUST`,`MUST NOT`,`SHOULD`,`SHOULD NOT`,`MAY`) | yes | 1 | Not possible |
| `subject_label` | string | yes | 1 | Not possible |
| `text_address` | address | yes | 1 | Not possible; the octets of the clause as stated, held by `Part 11` |
| `resolved_at` | instant | yes | 1 | Not possible |
| `assessability_class` | enum, section 3.6 | yes | 1 | Not possible |
| `determination_statements` | identifier | no | 0..n | No determination statement has been derived, which forbids assessment of the criterion |
| `superseded_by` | identifier | no | 0..1 | The registration is current for the part version it names |

**P12-3.22 (MUST) Criteria resolved, never transcribed.** An implementation must resolve every criterion from the part that states it and must hold the content address of the clause text rather than a copy it maintains.

**P12-3.23 (MUST NOT) No interpretation recorded as the criterion.** An implementation must not record its reading of a clause as the clause, and must record any interpretation as a determination statement attributed to itself.

**P12-3.24 (MUST) Register versioned per part version.** An implementation must hold a separate criterion registration for each version of each part it assesses against.

**P12-3.25 (MUST) Clause count derived, not asserted.** An implementation must derive the count of criteria it registers per part from the register and must state the grain of the count.

**P12-3.26 (MUST) Permissive criteria registered and excluded from conformance.** An implementation must register criteria carrying a permissive modality and must not assess them for conformance, since they constrain nothing.

**P12-3.27 (MUST) Advisory criteria assessed for the recorded reason.** An implementation must assess a criterion carrying an advisory modality by determining whether it was satisfied or, where it was not, whether a reason was recorded, and must report the two conditions distinctly.

### 3.6 Assessability classification

This is the section whose output is most unwelcome and most useful. Twelve parts state requirements. Not all of them state properties anyone can check, and a harness that does not say which is which will produce a conformance figure over the assessable subset and present it as a figure over the whole.

The classification is a closed set of seven classes.

| Class | Meaning |
|---|---|
| `externally_observable` | The property can be determined from the component's ordinary interfaces without privileged access |
| `observable_with_privilege` | The property can be determined from interfaces or stores available only to an assessor with granted access |
| `record_derivable` | The property can be determined only from records the component holds about past behaviour |
| `elicitation_required` | The property can be determined only by introducing a probe, because the behaviour does not occur otherwise |
| `construction_only` | The property can be determined only by inspecting design, code or configuration, and not from behaviour |
| `process_only` | The property is about what people do, and can be determined only by interview or by examining process records |
| `not_assessable` | The clause states no property that any method of this part can determine |

**P12-3.28 (MUST) Every criterion classified.** An implementation must assign exactly one assessability class to every registered criterion.

**P12-3.29 (MUST) Classification reasoned.** An implementation must record, for every criterion classified other than `externally_observable`, the reason that class was assigned.

**P12-3.30 (MUST) Not assessable published per part.** An implementation must publish, per part and per part version, the count and the identifiers of criteria classified `not_assessable`.

**P12-3.31 (MUST NOT) No not assessable criterion counted as satisfied.** An implementation must not include a criterion classified `not_assessable` in any count of satisfied criteria and must not exclude it from the denominator of a conformance proportion without stating that it did.

**P12-3.32 (MUST) Denominator declared with every proportion.** An implementation must state, with every proportion of criteria satisfied, which assessability classes are in the denominator.

**P12-3.33 (MUST) Reclassification recorded, not overwritten.** An implementation must record a change of assessability class with the prior class, the instant and the reason, since a criterion reclassified as assessable may have been reported as unassessable for years.

**P12-3.34 (MUST) Classification exposed to the part's author.** An implementation must expose its assessability classification of a part's criteria, so that the author of the part can see which of its clauses state no checkable property. **Source.** The conformity assessment standards include guidance for drafting normative documents suitable for conformity assessment, whose purpose is that requirements be written so that fulfilment can be determined; a classification fed back to the drafter is the mechanism by which a clause that cannot be assessed is either rewritten or acknowledged.

**P12-3.35 (MUST NOT) No clause rewritten here.** An implementation must not amend a clause it classifies as not assessable and must confine itself to reporting the classification.

### 3.7 Claims, plans and determination statements

| Field, claim | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `claim_id` | identifier | yes | 1 | Not possible |
| `object_ref` | pin | yes | 1 | Not possible |
| `proposition` | text | yes | 1 | Not possible |
| `criterion_refs` | criterion-ref | no | 0..n | The claim is not derived from a criterion, which is permitted for a published figure |
| `source` | enum(`derived_from_criterion`,`published_by_component`,`asserted_by_operator`) | yes | 1 | Not possible |
| `falsifiable` | boolean | yes | 1 | Not possible; see P12-3.37 |
| `quantification` | enum(`universal`,`existential`,`statistical`,`unquantified`) | yes | 1 | Not possible |
| `registered_at` | instant | yes | 1 | Not possible |

| Field, assessment plan | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `plan_id` | identifier | yes | 1 | Not possible |
| `scope` | structure: parts, criteria, objects, interval | yes | 1 | Not possible |
| `determination_statements` | identifier | yes | 1..n | Not possible |
| `methods_planned` | structure: statement, method, object kind, depth, coverage | yes | 1..n | Not possible |
| `frame_declaration_id` | identifier | yes | 1 | Not possible |
| `sampling_scheme_id` | identifier | no | 0..1 | No sampling is planned, which requires the coverage to be complete over the frame |
| `elicitation_planned` | boolean | yes | 1 | Not possible |
| `declared_at` | instant | yes | 1 | Not possible; the plan is declared before evidence is gathered |
| `assessor_id` | identifier | yes | 1 | Not possible |
| `independence_declaration_id` | identifier | yes | 1 | Not possible |

**P12-3.36 (MUST) Plan declared before evidence.** An implementation must declare the assessment plan before it gathers any evidence for it and must record the instant of declaration.

**P12-3.37 (MUST) Unfalsifiable claims recorded as such.** An implementation must record a claim that no evidence could contradict as not falsifiable and must not assess it.

**P12-3.38 (MUST) Quantification recorded.** An implementation must record whether a claim is universal, existential, statistical or unquantified, since the evidence that would falsify each differs.

**P12-3.39 (MUST NOT) No universal claim assessed as statistical.** An implementation must not report a universal claim as supported by a proportion of passing checks, and must report it as not falsified over the coverage achieved.

**P12-3.40 (MUST) Determination statements traceable to criteria.** An implementation must link every determination statement to the criterion it derives from, so that a finding is traceable to the requirement. **Source.** The security control assessment guidance constructs an assessment objective from determination statements linked to the content of the control expressly so that assessment results are traceable back to the requirement.

**P12-3.41 (MUST) One statement, one property.** An implementation must derive a determination statement that asserts one property and must derive more than one statement from a criterion that asserts more than one.

**P12-3.42 (MUST NOT) No plan amended after evidence.** An implementation must not amend a declared plan after evidence gathering has begun, and must record an amendment as a new plan superseding the first with the evidence already gathered attributed to the first.

Clause P12-3.42 prevents the commonest way an assessment becomes an exercise in confirmation. A plan amended after a failing result, so that the failing check falls outside the scope, produces a clean assessment of a narrower thing, and nothing in the output says the scope moved.

### 3.8 Evidence and its provenance

| Field | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `evidence_item_id` | identifier | yes | 1 | Not possible |
| `determination_statement_id` | identifier | yes | 1 | Not possible |
| `provenance` | enum(`self_reported`,`observed`,`independently_reconstructed`,`elicited`) | yes | 1 | Not possible |
| `obtained_at` | instant | yes | 1 | Not possible |
| `obtained_by` | identifier | yes | 1 | Not possible |
| `method` | enum(`examine`,`interview`,`test`,`elicit`) | yes | 1 | Not possible |
| `object_kind` | enum(`specification`,`mechanism`,`activity`,`individual`,`record`) | yes | 1 | Not possible |
| `depth` | enum(`basic`,`focused`,`comprehensive`) | yes | 1 | Not possible |
| `content_address` | address | yes | 1 | Not possible; the octets of the evidence held by `Part 11` |
| `supports` | enum(`supports`,`contradicts`,`neutral`) | yes | 1 | Not possible |
| `component_could_have_influenced` | boolean | yes | 1 | Not possible; see P12-3.46 |
| `elicitation_record_id` | identifier | no | 0..1 | The provenance is not `elicited` |

**P12-3.43 (MUST) Provenance recorded on every item.** An implementation must record the provenance of every evidence item from the closed set of four and must not record an item without one.

**P12-3.44 (MUST NOT) No self reported item described otherwise.** An implementation must not record an item obtained from the assessed party's own statement or own computation as observed, independently reconstructed or elicited.

**P12-3.45 (MUST) Independent reconstruction defined by non reliance.** An implementation must record an item as independently reconstructed only where it recomputed the property from primary inputs without relying on the assessed component's computation of it.

**P12-3.46 (MUST) Influence recorded.** An implementation must record, for every evidence item, whether the assessed component could have influenced what the item shows, and must treat an item it could have influenced as self reported for the purpose of section 7.2.

**P12-3.47 (MUST) Evidence held by address.** An implementation must hold the octets of every evidence item by content address in `Part 11` and must not hold them inline.

**P12-3.48 (MUST) Contradicting evidence retained.** An implementation must retain every evidence item that contradicts a determination statement, including where the finding was later satisfied on other evidence.

**P12-3.49 (MUST NOT) No evidence discarded on a favourable finding.** An implementation must not discard evidence because the finding it contributed to was favourable.

### 3.9 The frame declaration and sampling

| Field, frame declaration | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `frame_declaration_id` | identifier | yes | 1 | Not possible |
| `population_description` | text | yes | 1 | Not possible |
| `declared_by` | enum(`assessor`,`assessed_component`,`operator`) | yes | 1 | Not possible; see P12-3.51 |
| `enumerability` | enum(`enumerable`,`partially_enumerable`,`not_enumerable`) | yes | 1 | Not possible |
| `enumerated_size` | integer | no | 0..1 | The frame is not enumerable, or the enumeration was not performed |
| `enumeration_source` | identifier | no | 0..1 | No enumeration exists |
| `independent_enumeration_source` | identifier | no | 0..1 | No second, independent enumeration exists, which bounds what can be said about the frame's completeness |
| `residual_unknown_described` | text | no | 0..1 | The frame is fully enumerable |
| `examined_independently` | boolean | yes | 1 | Not possible; see P12-3.51 |

**P12-3.50 (MUST) Frame declared on every assessment.** An implementation must declare the frame of every assessment and must not express coverage without one.

**P12-3.51 (MUST) Frame declaration examined independently where the assessed component declared it.** An implementation must examine independently every frame declaration made by the assessed component and must record the examination, since a coverage figure over a self declared population is only as sound as the declaration. **Source.** Required of this component by `Part 7` clause P7-12.34, which requires that component to expose the declared request space against which every coverage figure was computed expressly so that this component can assess whether the figure means anything.

**P12-3.52 (MUST NOT) No sampling of a non enumerable frame.** An implementation must not draw a sample from a frame it has recorded as not enumerable, and must record the population as unassessed.

**P12-3.53 (MUST) Partial enumerability handled as two populations.** An implementation must treat a partially enumerable frame as an enumerable population and a residual unknown, must sample only the first, and must report the second as unassessed with its description.

**P12-3.54 (MUST) Sampling scheme declared before drawing.** An implementation must declare the sampling scheme, including the selection method and the intended confidence, before drawing a sample.

**P12-3.55 (MUST) Sample recorded in full.** An implementation must record every member of every sample it drew, so that the sample can be examined for bias after the fact.

**P12-3.56 (MUST NOT) No convenience sample presented as probabilistic.** An implementation must not describe a sample selected by availability, by the assessed component's suggestion or by any non probabilistic means as a probability sample.

**P12-3.57 (MUST) Assessed component excluded from selection.** An implementation must not permit the assessed component to select, propose or influence the members of a sample, and must record any case in which it did.

### 3.10 Findings

| Field | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `finding_id` | identifier | yes | 1 | Not possible |
| `determination_statement_id` | identifier | yes | 1 | Not possible |
| `object_ref` | pin | yes | 1 | Not possible |
| `outcome` | enum, section 7.2 | yes | 1 | Not possible |
| `evidence_item_ids` | identifier | yes | 1..n | Not possible; a finding without evidence may not be recorded |
| `strongest_provenance` | enum, per section 3.8 | yes | 1 | Not possible; the strongest provenance among the supporting items |
| `depth_achieved` | enum(`basic`,`focused`,`comprehensive`) | yes | 1 | Not possible |
| `coverage_achieved` | structure: objects examined, objects in frame | yes | 1 | Not possible |
| `assessed_at` | instant | yes | 1 | Not possible |
| `assessor_id` | identifier | yes | 1 | Not possible |
| `disputed` | boolean | yes | 1 | Not possible |
| `dispute_record_id` | identifier | no | 0..1 | The finding is not disputed |
| `superseded_by` | identifier | no | 0..1 | The finding is current |

**P12-3.58 (MUST) Finding requires evidence.** An implementation must not record a finding with no evidence item, including a finding of not assessed, which must cite the record of the attempt.

**P12-3.59 (MUST) Strongest provenance recorded.** An implementation must record the strongest provenance among the items supporting a finding, and must not record a stronger provenance than any item carries.

**P12-3.60 (MUST NOT) No satisfied finding on self report alone.** An implementation must not record an outcome of satisfied where every supporting item is self reported or was influenceable by the assessed component, and must record the outcome that names the reliance.

**P12-3.61 (MUST) Depth and coverage achieved recorded, not planned.** An implementation must record the depth and coverage actually achieved and must not record the planned values as achieved.

**P12-3.62 (MUST) Shortfall against plan recorded.** An implementation must record, where achieved depth or coverage fell short of the plan, the shortfall and its cause.

**P12-3.63 (MUST) Findings immutable, disputes separate.** An implementation must not alter a finding and must record a dispute as its own record referencing it.

**P12-3.64 (MUST) Dispute does not withdraw the finding.** An implementation must retain a disputed finding with its outcome unchanged and must record the dispute's own resolution separately.

### 3.11 Assurance statements

| Field | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `assurance_statement_id` | identifier | yes | 1 | Not possible |
| `claim_id` | identifier | yes | 1 | Not possible |
| `outcome` | enum, section 7.4 | yes | 1 | Not possible |
| `finding_ids` | identifier | yes | 1..n | Not possible |
| `method_summary` | structure: methods used, counts | yes | 1 | Not possible |
| `depth` | enum(`basic`,`focused`,`comprehensive`) | yes | 1 | Not possible |
| `coverage` | structure: objects assessed, frame size, proportion | yes | 1 | Not possible |
| `frame_declaration_id` | identifier | yes | 1 | Not possible |
| `falsification_attempts` | structure: attempt kind, count, outcome | yes | 1..n | Not possible |
| `not_established` | structure: statement, assessability class | no | 0..n | Every statement in scope was assessed |
| `validity_interval` | interval | yes | 1 | Not possible |
| `decay_basis` | enum(`fixed_term`,`until_object_changes`,`until_frame_changes`,`surveillance_dependent`) | yes | 1 | Not possible |
| `state` | enum, section 5.4 | yes | 1 | Not possible |
| `attestation_party_class` | enum(`first`,`second`,`third`) | yes | 1 | Not possible |
| `independence_declaration_id` | identifier | yes | 1 | Not possible |
| `object_version` | pin | yes | 1 | Not possible |
| `superseded_by` | identifier | no | 0..1 | The statement is current for its object version |

**P12-3.65 (MUST) Validity interval mandatory.** An implementation must record a validity interval on every assurance statement and must not issue one that is open ended.

**P12-3.66 (MUST) Decay basis mandatory.** An implementation must record the basis on which an assurance statement loses validity.

**P12-3.67 (MUST) Party class recorded.** An implementation must record whether an assurance statement is a first, second or third party attestation. **Source.** The conformity assessment vocabulary distinguishes first party attestation, which it calls a declaration, from third party attestation, which it calls certification, and records that no special term exists for second party attestation; the distinction is about the relationship of the attesting party to the object and is the primary determinant of the statement's weight.

**P12-3.68 (MUST NOT) No first party statement presented as independent.** An implementation must not present a first party attestation as independent of the object.

**P12-3.69 (MUST) Object version pinned.** An implementation must pin the version of the object an assurance statement concerns, so that a change to the object can invalidate the statement.

**P12-3.70 (MUST) Statement superseded on object change.** An implementation must mark an assurance statement superseded when the object version it names changes in a respect the assessment covered, and must not silently carry it forward.

**P12-3.71 (MUST NOT) No expired statement presented as current.** An implementation must not present an assurance statement whose validity interval has ended as current, and must record every request that resolved to an expired statement.

### 3.12 Probes and elicitation

| Field, probe definition | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `probe_definition_id` | identifier | yes | 1 | Not possible |
| `probe_kind` | identifier | yes | 1 | Not possible; a registered kind |
| `target_criterion_refs` | criterion-ref | yes | 1..n | Not possible |
| `expected_outcome` | text | yes | 1 | Not possible; the outcome a conforming component must produce |
| `indistinguishability_claim` | enum(`indistinguishable`,`distinguishable`,`unknown`) | yes | 1 | Not possible |
| `side_effect_declaration` | text | yes | 1 | Not possible; what the probe changes in the assessed component |
| `reversibility` | enum(`none_required`,`reversible`,`irreversible`) | yes | 1 | Not possible |
| `version` | string | yes | 1 | Not possible |

| Field, elicitation record | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `elicitation_record_id` | identifier | yes | 1 | Not possible |
| `probe_definition_id` | identifier | yes | 1 | Not possible |
| `object_ref` | pin | yes | 1 | Not possible |
| `permission_ref` | criterion-ref | yes | 1 | Not possible; the clause of the assessed part permitting elicitation |
| `authorisation_ref` | pin to `Part 7` | yes | 1 | Not possible |
| `instance_class` | enum(`production`,`conformance_instance`,`isolated`) | yes | 1 | Not possible |
| `introduced_at` | instant | yes | 1 | Not possible |
| `observed_outcome` | text | yes | 1 | Not possible |
| `matched_expected` | boolean | yes | 1 | Not possible |
| `detected_as_probe` | enum(`no_evidence`,`evidence_of_detection`,`known_detected`) | yes | 1 | Not possible |
| `withdrawn_at` | instant | no | 0..1 | The probe was not withdrawn, which is a defect for a reversible probe |

**P12-3.72 (MUST) Expected outcome declared before introduction.** An implementation must declare the outcome a conforming component must produce before it introduces a probe, and must not determine the expected outcome from what happened.

**P12-3.73 (MUST) Permission cited.** An implementation must cite the clause of the assessed part that permits elicitation, and must not introduce a probe into a component whose part does not permit it.

**P12-3.74 (MUST) Instance class recorded.** An implementation must record whether a probe was introduced into a production instance, a conformance instance or an isolated instance, since the three support different conclusions.

**P12-3.75 (MUST NOT) No conclusion about production from an isolated instance.** An implementation must not express a finding about a production instance from a probe introduced into an isolated one, and must record the instance class in the finding's coverage.

**P12-3.76 (MUST) Side effects declared and withdrawn.** An implementation must declare what a probe changes and must withdraw every reversible probe, recording the withdrawal.

**P12-3.77 (MUST) Detection recorded.** An implementation must record whether there is evidence that the assessed component detected a probe as a probe.

**P12-3.78 (MUST) Detected probes invalidate the inference.** An implementation must record a finding resting on a probe known to have been detected as evidence about how the component treats probes and not about its ordinary behaviour.

**P12-3.79 (MUST) Probe instances unpredictable.** An implementation must select probe instances by a means the assessed component cannot anticipate, and must record the selection method without publishing the instances in advance.

### 3.13 Independence and assessors

| Field, assessor registration | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `assessor_id` | identifier | yes | 1 | Not possible |
| `party_ref` | pin to party | yes | 1 | Not possible |
| `competence_basis` | enum(`declared`,`assessed_by_peer`,`accredited_externally`,`none`) | yes | 1 | Not possible |
| `scope_of_registration` | criterion-ref | yes | 1..n | Not possible; which criteria this assessor may assess |
| `registered_at` | instant | yes | 1 | Not possible |
| `withdrawn_at` | instant | no | 0..1 | The registration is current |

| Field, independence declaration | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `independence_declaration_id` | identifier | yes | 1 | Not possible |
| `assessor_id` | identifier | yes | 1 | Not possible |
| `object_ref` | pin | yes | 1 | Not possible |
| `technical_independence` | enum(`independent`,`shared`,`same`) | yes | 1 | Not possible |
| `managerial_independence` | enum(`independent`,`common_management`,`same_management`) | yes | 1 | Not possible |
| `financial_independence` | enum(`independent`,`common_budget`,`funded_by_object_owner`) | yes | 1 | Not possible |
| `conflicts_declared` | text | no | 0..n | No conflict was declared, which is not evidence that none exists |
| `declared_at` | instant | yes | 1 | Not possible |

**P12-3.80 (MUST) Three forms declared separately.** An implementation must declare technical, managerial and financial independence separately for every assessment and must not report a single independence value. **Source.** The software verification and validation standards distinguish technical, managerial and financial independence as three separable properties of an independent verification activity, and an assessor may hold one without the others.

**P12-3.81 (MUST NOT) No independence claimed where any form is absent.** An implementation must not describe an assessment as independent where any of the three forms is other than independent, and must state which forms hold.

**P12-3.82 (MUST) Competence basis recorded.** An implementation must record the basis on which an assessor's competence rests, including where it is merely declared.

**P12-3.83 (MUST NOT) No assessment outside the registered scope.** An implementation must not accept a finding from an assessor for a criterion outside that assessor's registered scope.

**P12-3.84 (MUST NOT) No advisor as assessor.** An implementation must not accept a finding from an assessor that advised on, designed or configured the object of the finding, and must record any such case as a conflict.

**P12-3.85 (MUST) Funded by the object owner recorded as a conflict.** An implementation must record financial dependence on the owner of the object as a declared conflict rather than as an ordinary arrangement.

### 3.14 Nonconformities and their disposition

| Field | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `nonconformity_id` | identifier | yes | 1 | Not possible |
| `finding_id` | identifier | yes | 1 | Not possible |
| `severity_basis` | enum(`modality`,`declared_by_part`,`assessor_judgement`) | yes | 1 | Not possible |
| `owner` | pin to party | yes | 1 | Not possible; a party outside this component |
| `state` | enum, section 5.5 | yes | 1 | Not possible |
| `accepted_until` | instant | no | 0..1 | The nonconformity is not accepted |
| `acceptance_authorisation_ref` | pin to `Part 7` | no | 0..1 | The nonconformity is not accepted |
| `acceptance_reason` | text | no | 0..1 | The nonconformity is not accepted |
| `remediation_work_ref` | pin to `Part 8` | no | 0..1 | No remediation work is tracked |
| `closed_at` | instant | no | 0..1 | The nonconformity is open |
| `closing_finding_id` | identifier | no | 0..1 | The nonconformity was not closed by a reassessment |

**P12-3.86 (MUST) Owner outside this component.** An implementation must record the owner of every nonconformity as a party other than itself and must refuse to record itself as owner.

**P12-3.87 (MUST) Acceptance bounded and authorised.** An implementation must require an acceptance of a nonconformity to carry an expiry, an authorisation reference and a reason, and must not accept one without all three.

**P12-3.88 (MUST NOT) No closure without a reassessment.** An implementation must not close a nonconformity other than on a finding from a reassessment of the same determination statement, and must not close one on an assertion that it was remediated.

**P12-3.89 (MUST) Expired acceptance reopens.** An implementation must return a nonconformity to open when its acceptance expires and must emit an event.

**P12-3.90 (MUST) Accepted population exposed.** An implementation must expose every accepted nonconformity with its expiry and its owner, since an acceptance that nobody revisits is a nonconformity that has been made invisible by being acknowledged.

### 3.15 Surveillance

**P12-3.91 (MUST) Surveillance schedule per statement class.** An implementation must declare a surveillance cadence for every class of assurance statement and must record the cadence in force at each iteration. **Source.** The conformity assessment vocabulary defines surveillance as the systematic iteration of conformity assessment activities as a basis for maintaining the validity of a statement, which is the mechanism by which an attestation about a moment is kept meaningful over an interval.

**P12-3.92 (MUST) Iterations recorded, including those that found nothing.** An implementation must record every surveillance iteration and its outcome, including iterations in which no change was found.

**P12-3.93 (MUST) Lapse recorded, not silent.** An implementation must record the lapse of an assurance statement whose surveillance was not performed, and must not extend the validity interval in its absence.

**P12-3.94 (MUST) Overdue surveillance population exposed.** An implementation must expose every assurance statement whose surveillance is overdue.

### 3.16 Projections

**P12-3.95 (MUST) Projections marked as such.** An implementation must mark every projection it exposes as a projection and must not permit a projection to be cited as a finding or an assurance statement.

**P12-3.96 (MUST) Aggregate carries its denominator.** An implementation must state, with every aggregate over findings, the assessability classes included, the frame, the coverage achieved and the count of findings resting on self report alone.

**P12-3.97 (MUST NOT) No single figure for a part.** An implementation must not expose a single scalar summarising a component's conformance to a part, since no such figure can carry the qualifications section 3.2 requires.

**P12-3.98 (MUST NOT) No colour or grade as a projection.** An implementation must not expose a status colour, grade or score in place of an outcome from section 7, and may expose one only alongside the outcome and its qualifications.

### 3.17 Worked demonstration

The demonstration is narrative and binds nothing.

`Part 11` clause P11-3.48 requires a store to record, for every retrieval that returned octets, whether they were fully verified, partially verified or returned unverified. The claim under assessment is universal: every retrieval carries a verification declaration.

The criterion is resolved from `Part 11` version 1.0.0 and classified. It is not `externally_observable`, because a caller sees a declaration and cannot tell whether the declaration is truthful. It is not `record_derivable` alone, because the record is written by the party whose truthfulness is in question. It is classified `elicitation_required`, and `Part 11` clause P11-12.35 supplies the permission: that component must support the retrieval of content and the independent recomputation of its address by this component without relying on the store's own verification result.

Two determination statements are derived. That every retrieval record carries one of the four declaration values, which is `record_derivable`. And that a retrieval reported as `verified_full` did in fact verify, which is `elicitation_required`.

The plan is declared before evidence is gathered. The frame for the first statement is the retrieval records over a stated interval, declared by the store and therefore examined independently under clause P12-3.51 by reconciling the record count against an independent count of requests observed at the boundary. The frame is enumerable, so a probability sample is drawn and every member recorded.

For the second statement a probe is used: content of known octets is ingested, its address computed independently, and a retrieval performed. The store returns octets and reports `verified_full`. The assessor recomputes the address itself, without relying on the store, per clause P12-3.45, and the evidence is recorded as `independently_reconstructed`. A second probe substitutes altered octets at the storage layer, where the elicitation permission and an authorisation reference allow it, and the store reports `verified_full` again. That is a counterexample. Under clause P12-3.9 the universal claim is falsified on the single instance, and under clause P12-3.10 the result must not be reported as a pass rate.

The assurance statement is issued with outcome `falsified`, with the two determination statements, the frame, the coverage, the depth, the probes and the instance class. The nonconformity is recorded with an owner outside this component and cannot be closed except by a reassessment of the same determination statement.

Had the second probe not produced a counterexample, the honest outcome would have been `not_falsified` over a coverage of two probes at basic depth on a production instance, which is a weak statement and says so. It is not a statement that the store verifies its retrievals.

## 4. Interfaces

### 4.1 Interface principles

The interface of this component is unusual in one respect that governs the whole section: almost everything it does is a read of something else and a write to itself. It has one operation that touches an assessed component, being the introduction of a probe, and that operation is fenced by a permission the assessed part must itself grant. Everything else is examination, and the records it writes are its own. A harness whose interface list is longer than this in the direction of the assessed components has acquired a capability it should not have.

**P12-4.1 (MUST) Operations defined over the entities of section 3.** An implementation must define every operation it exposes in terms of the entities of section 3 and must state which records each creates and which events it emits.

**P12-4.2 (MUST) Idempotency key accepted.** An implementation must accept a caller supplied idempotency key on every state changing operation and must return the original result when invoked again with the same key and arguments.

**P12-4.3 (MUST) Authorisation obtained per operation.** An implementation must obtain an authorisation decision from `Part 7` before declaring a plan, introducing a probe, issuing an assurance statement, accepting a nonconformity or registering an assessor, and must record the reference.

**P12-4.4 (MUST) One outcome per operation.** An implementation must return exactly one outcome from section 7 for every operation.

**P12-4.5 (MUST) Refusals recorded.** An implementation must record every refused operation with the requesting party, the instant and the refusal code.

**P12-4.6 (MUST NOT) No operation that alters a finding or an evidence item.** An implementation must not expose an operation that changes a recorded finding or evidence item.

**P12-4.7 (MUST NOT) No write to an assessed component outside a probe.** An implementation must not expose an operation that writes to an assessed component other than the introduction and withdrawal of a probe under section 6.7.

### 4.2 Registration and planning operations

| Operation | Effect |
|---|---|
| `register_criteria` | Resolves the clauses of a part version and registers them |
| `classify_criterion` | Assigns or revises an assessability class with a reason |
| `derive_determination_statement` | Records a statement derived from a criterion |
| `register_claim` | Records a proposition to be assessed |
| `declare_frame` | Records a frame declaration with its enumerability |
| `examine_frame_declaration` | Records an independent examination of a frame declared by an assessed component |
| `declare_plan` | Records an assessment plan before evidence is gathered |
| `register_assessor` | Registers an assessor with a competence basis and scope |
| `declare_independence` | Records the three independence forms for an assessment |
| `register_probe_definition` | Registers a probe with its expected outcome and side effects |
| `declare_trust_base_item` | Records an assumed proposition and its consequence |

**P12-4.8 (MUST) Registration refused without a part version.** An implementation must refuse `register_criteria` for a part whose version is not named.

**P12-4.9 (MUST) Classification refused without a reason where not externally observable.** An implementation must refuse a classification other than `externally_observable` that carries no reason.

**P12-4.10 (MUST) Plan refused without a frame.** An implementation must refuse `declare_plan` where no frame declaration is named.

**P12-4.11 (MUST) Plan refused without an independence declaration.** An implementation must refuse `declare_plan` where the three independence forms are not declared.

**P12-4.12 (MUST) Plan refused where the assessor is out of scope.** An implementation must refuse `declare_plan` naming an assessor whose registered scope does not include every criterion in the plan.

**P12-4.13 (MUST) Probe registration refused without an expected outcome.** An implementation must refuse `register_probe_definition` that declares no expected outcome.

**P12-4.14 (MUST) Trust base item refused without a consequence.** An implementation must refuse `declare_trust_base_item` that does not state what becomes unassessable if the proposition is false.

### 4.3 Assessment operations

| Operation | Effect |
|---|---|
| `open_run` | Opens an assessment run against a declared plan |
| `record_evidence` | Records an evidence item with its provenance |
| `introduce_probe` | Introduces a probe under a cited permission and authorisation |
| `withdraw_probe` | Withdraws a reversible probe and records the withdrawal |
| `record_finding` | Records a finding against a determination statement |
| `close_run` | Closes a run and records the achieved depth and coverage |
| `issue_assurance_statement` | Issues a statement over the findings of one or more runs |
| `record_nonconformity` | Records a nonconformity with an owner outside this component |
| `accept_nonconformity` | Records a bounded, authorised acceptance |
| `perform_surveillance` | Records a surveillance iteration and its outcome |
| `supersede_statement` | Marks a statement superseded on an object version change |
| `record_dispute` | Records a dispute of a finding |
| `record_external_assessment` | Records an assessment of this component performed by another party |

**P12-4.15 (MUST) Evidence refused without provenance.** An implementation must refuse `record_evidence` that declares no provenance.

**P12-4.16 (MUST) Probe refused without a permission citation.** An implementation must refuse `introduce_probe` that cites no clause of the assessed part permitting elicitation.

**P12-4.17 (MUST) Finding refused without evidence.** An implementation must refuse `record_finding` that cites no evidence item.

**P12-4.18 (MUST) Satisfied finding refused on self report alone.** An implementation must refuse a finding of satisfied whose every supporting item is self reported or influenceable, and must require the outcome that names the reliance.

**P12-4.19 (MUST) Statement refused without method, depth, coverage and frame.** An implementation must refuse `issue_assurance_statement` lacking any of the four.

**P12-4.20 (MUST) Statement refused without a validity interval and decay basis.** An implementation must refuse an assurance statement lacking either.

**P12-4.21 (MUST) Nonconformity refused with this component as owner.** An implementation must refuse `record_nonconformity` naming itself as owner.

**P12-4.22 (MUST) Acceptance refused without expiry, authorisation and reason.** An implementation must refuse `accept_nonconformity` lacking any of the three.

**P12-4.23 (MUST) Closure refused without a reassessment finding.** An implementation must refuse the closure of a nonconformity that cites no finding from a reassessment of the same determination statement.

**P12-4.24 (MUST) Run closure records the shortfall.** An implementation must require `close_run` to record achieved depth and coverage and any shortfall against the plan.

### 4.4 Reading operations

**P12-4.25 (MUST) Findings retrievable by criterion and by object.** An implementation must expose retrieval of findings by criterion reference and by object.

**P12-4.26 (MUST) Point in time query supported.** An implementation must answer, for any stated past instant, the assurance statements then valid, the nonconformities then open and the assessability classification then in force.

**P12-4.27 (MUST) Assessability classification published.** An implementation must expose, per part and part version, the classification of every criterion and the counts by class.

**P12-4.28 (MUST) Trust base published.** An implementation must expose the trust base in full.

**P12-4.29 (MUST NOT) No state change from a read.** An implementation must not change any state other than a read record in response to a reading operation.

**P12-4.30 (MUST) Expired statements returned as expired.** An implementation must return an expired assurance statement marked expired rather than omitting it, so that a caller learns that assurance once existed and lapsed.

**P12-4.31 (MUST) Qualifications returned with every statement.** An implementation must return the method, depth, coverage, frame, not established set and party class with every assurance statement it returns, and must not expose an operation that returns the outcome alone.

### 4.5 What a caller may and may not assume

**P12-4.32 (MUST NOT) No assumption of conformance.** A caller must not read an outcome of not falsified as establishing that the object conforms.

**P12-4.33 (MUST NOT) No assumption that an unassessed criterion is satisfied.** A caller must not read the absence of a nonconformity against a criterion as evidence that the criterion is satisfied, and must read the assessability classification and the coverage.

**P12-4.34 (MUST NOT) No assumption of currency.** A caller must not treat an assurance statement as current without reading its validity interval and the state of its surveillance.

**P12-4.35 (MUST NOT) No assumption of independence.** A caller must not assume an assessment was independent and must read the three declared forms.

**P12-4.36 (MUST NOT) No assumption that this component was itself assessed.** A caller must not assume that an external assessment of this component exists, and must read the record or its declared absence.

**P12-4.37 (MUST) Coverage bounds every inference.** A caller may rely on a finding only over the coverage the finding records.

### 4.6 Reads from other components

| Read | Component | Pinning | On failure |
|---|---|---|---|
| Clause text and version of a part | `Part 1` | pinned per part version | refuse registration; do not register a criterion whose text cannot be resolved |
| Clause octets by address | `Part 11` | content address | refuse registration |
| Authorisation decision | `Part 7` | policy version pinned per decision | deny the operation; never permit on failure |
| Verdict for a declarative determination statement | `Part 2` | rule version pinned per evaluation | record the non verdict; do not record a finding |
| Party identity for assessor, owner and interviewee | `Part 10` | snapshot pinned per record | refuse the operation |
| Remediation work item | `Part 8` | work item reference | leave the nonconformity open |
| Schema of an assessment record payload | `Part 9` | schema version pinned | refuse to emit |
| The assessed component's own exposed state | the part assessed | pinned at the instant read | record the read failure as evidence of unavailability, not as a finding |

**P12-4.38 (MUST) Reads treated as fallible.** An implementation must treat every read in the table in section 4.6 as fallible and must apply the stated failure behaviour rather than a default.

**P12-4.39 (MUST NOT) No proceeding on an authorisation failure.** An implementation must not proceed with an operation when the authorisation read fails, and must deny.

**P12-4.40 (MUST) Unavailability recorded as unavailability.** An implementation must record a failure to read an assessed component's state as evidence that the state was unavailable and must not record it as a finding that the criterion was not satisfied.

### 4.7 Events emitted

**P12-4.41 (MUST) Event per finding and per statement.** An implementation must emit an event for every finding recorded, every assurance statement issued, superseded or expired, and every nonconformity recorded, accepted, reopened or closed.

**P12-4.42 (MUST) Event carries the qualifications.** An implementation must carry the criterion reference, the outcome, the strongest provenance and the coverage on every finding event.

**P12-4.43 (MUST) Events delivered to the ledger.** An implementation must deliver every event to `Part 3` at least once and must retain the event until delivery is acknowledged.

**P12-4.44 (MUST) Falsification event distinct.** An implementation must emit a distinct event class for a falsified claim, naming the counterexample.

**P12-4.45 (MUST) Reclassification event.** An implementation must emit an event on a change of a criterion's assessability class, naming the prior class.

**P12-4.46 (MUST) Trust base change event.** An implementation must emit an event on the addition, removal or reclassification of a trust base item.

**P12-4.47 (MUST) Acceptance expiry event.** An implementation must emit an event at a declared interval before an acceptance of a nonconformity expires.

**P12-4.48 (MUST) Probe detection event.** An implementation must emit an event where there is evidence that an assessed component detected a probe.

**P12-4.49 (SHOULD) Self report reliance signal.** An implementation should emit an event where the proportion of findings in a run resting on self report alone exceeds a declared threshold.

## 5. State model

### 5.1 Six state models

The six answer different questions and collapsing any two loses the answer to one. The assessability class answers whether a criterion can be assessed at all. The run state answers whether an assessment is in progress, complete or abandoned. The assurance statement state answers whether a conclusion is still to be relied on. The nonconformity state answers whether a failure is open, accepted or closed. The probe state answers whether an introduced probe is still in the assessed component. And the trust base item state answers whether an assumption is still being made.

The commonest collapse is to fold the assurance statement state into the nonconformity state, so that a statement with no open nonconformities is reported as valid regardless of whether its surveillance lapsed two years ago.

**P12-5.1 (MUST) States held as transitions.** An implementation must hold every state as a sequence of recorded transitions and must not hold it as a mutable field.

**P12-5.2 (MUST) One state per axis per instant.** An implementation must not represent two states of one entity on one axis as simultaneously current.

**P12-5.3 (MUST NOT) No derivation of one axis from another.** An implementation must not derive an assurance statement's state from the state of the nonconformities within its scope.

**P12-5.4 (MUST) Transitions carry authorisation where required.** An implementation must record the authorising decision reference on every transition that requires one under section 4.

**P12-5.5 (MUST) Illegal transitions recorded.** An implementation must record every refused transition and must not discard the attempt.

**P12-5.6 (MUST NOT) No unlisted transition.** An implementation must not admit a transition this section does not list.

### 5.2 Assessability class as a state

The seven classes of section 3.6 are the values; this subsection governs movement between them.

Legal transitions: any class to any other class, on a recorded reclassification carrying a reason and the prior class.

**P12-5.7 (MUST) Reclassification always permitted and always recorded.** An implementation must permit a criterion to be reclassified on a recorded reason and must retain every prior classification.

**P12-5.8 (MUST) Findings tied to the class in force.** An implementation must record, on every finding, the assessability class in force when the finding was made, so that a finding made when a criterion was thought unassessable is distinguishable from one made after it was reclassified.

**P12-5.9 (MUST) Reclassification to assessable reopens the population.** An implementation must expose, on reclassification of a criterion from `not_assessable` to any other class, every object for which the criterion was previously reported as unassessable.

### 5.3 Assessment run state

| State | Meaning | Terminal |
|---|---|---|
| `planned` | A plan is declared and no evidence has been gathered | no |
| `gathering` | Evidence gathering is under way | no |
| `complete` | Evidence gathering ended and findings were recorded | yes |
| `abandoned` | The run ended without findings, for a recorded reason | yes |
| `invalidated` | The run's evidence was found unsound after closure | yes |

Legal transitions: to `planned` on plan declaration; `planned` to `gathering` on the first evidence item; `planned` to `abandoned`; `gathering` to `complete` on closure; `gathering` to `abandoned`; `complete` to `invalidated` on a recorded finding that the evidence was unsound.

**P12-5.10 (MUST) Abandonment reasoned.** An implementation must record a reason for every abandoned run and must not delete the evidence already gathered.

**P12-5.11 (MUST) Invalidation propagates to statements.** An implementation must mark every assurance statement resting on an invalidated run as withdrawn and must record the invalidation as the cause.

**P12-5.12 (MUST NOT) No reopening of a closed run.** An implementation must not reopen a closed run and must express further assessment as a new run.

### 5.4 Assurance statement state

| State | Meaning | Terminal |
|---|---|---|
| `valid` | Within its validity interval, surveillance current | no |
| `surveillance_overdue` | Within its validity interval, surveillance not performed on cadence | no |
| `expired` | The validity interval has ended | yes |
| `superseded` | The object version it names has changed in a covered respect | yes |
| `withdrawn` | The statement was withdrawn, for a recorded reason | yes |
| `falsified` | A later finding falsified the claim the statement concerned | yes |

Legal transitions: to `valid` on issue; `valid` to `surveillance_overdue` on cadence elapse; `surveillance_overdue` to `valid` on a surveillance iteration; either to `expired` on interval end; either to `superseded` on an object version change; either to `withdrawn`; either to `falsified` on a later counterexample.

**P12-5.13 (MUST) Overdue surveillance visible in the state.** An implementation must move an assurance statement to `surveillance_overdue` on the elapse of its cadence and must not leave it in `valid`.

**P12-5.14 (MUST) Falsified is terminal and retained.** An implementation must treat `falsified` as terminal, must retain the statement, and must not delete or amend it.

**P12-5.15 (MUST NOT) No reinstatement.** An implementation must not return a statement from a terminal state to `valid`, and must express renewed assurance as a new statement over a new run.

**P12-5.16 (MUST) Superseded distinguished from expired.** An implementation must distinguish a statement invalidated by a change to its object from one invalidated by the passage of time.

### 5.5 Nonconformity state

| State | Meaning | Terminal |
|---|---|---|
| `open` | Recorded and not accepted or closed | no |
| `accepted` | Accepted for a bounded interval by an authorised party | no |
| `remediation_in_progress` | Remediation work is tracked | no |
| `closed_verified` | Closed on a finding from a reassessment | yes |
| `closed_criterion_withdrawn` | Closed because the criterion no longer exists in a later part version | yes |
| `disputed` | The finding it rests on is disputed and unresolved | no |

Legal transitions: to `open` on recording; `open` to `accepted` on an authorised acceptance; `accepted` to `open` on expiry; `open` or `accepted` to `remediation_in_progress`; `remediation_in_progress` to `open` on abandonment of the work; any non terminal to `closed_verified` on a reassessment finding; any non terminal to `closed_criterion_withdrawn`; `open` to `disputed` and back on resolution.

**P12-5.17 (MUST) Criterion withdrawal closes without a claim of remediation.** An implementation must record a nonconformity closed because a later part version withdrew the criterion as closed on that ground and must not record it as remediated.

**P12-5.18 (MUST) Dispute does not close.** An implementation must not treat a dispute as closing a nonconformity.

**P12-5.19 (MUST) Acceptance expiry automatic.** An implementation must return an accepted nonconformity to `open` at its expiry without any act.

### 5.6 Probe state

| State | Meaning | Terminal |
|---|---|---|
| `defined` | Registered and not introduced | no |
| `introduced` | Present in an assessed component | no |
| `withdrawn` | Removed and the removal recorded | yes |
| `abandoned_in_place` | Introduced, irreversible or unremovable, and recorded as remaining | yes |
| `compromised` | Known to have been detected as a probe | yes |

**P12-5.20 (MUST) Abandoned in place recorded, never silent.** An implementation must record every probe it introduced and did not withdraw, with the reason, and must expose the population.

**P12-5.21 (MUST) Compromised probes retired.** An implementation must retire a probe definition known to have been detected and must not reuse it.

**P12-5.22 (MUST NOT) No probe deleted from the record.** An implementation must retain the definition and every elicitation record of a retired probe.

### 5.7 Trust base item state

| State | Meaning | Terminal |
|---|---|---|
| `assumed` | The proposition is relied upon and not assessed | no |
| `under_assessment` | An assessment of the proposition is in progress | no |
| `assessed` | The proposition is now assessed and is no longer a trust base item | yes |
| `falsified` | The proposition was found false | yes |
| `withdrawn` | The system no longer relies on the proposition | yes |

**P12-5.23 (MUST) Falsified assumption escalated.** An implementation must, on a trust base item being falsified, mark every assurance statement whose assessment relied on it as withdrawn and record the item as the cause.

**P12-5.24 (MUST) Assumption removal recorded.** An implementation must record the withdrawal of a trust base item with the reason the reliance ceased.

## 6. Execution semantics

### 6.1 The functional sequence

The sequence is taken from the conformity assessment standards, whose functional approach comprises selection, including sampling, then determination, then review, then decision, then attestation, then surveillance. This part adopts it because it separates the gathering of information from the judgement made on it and the statement issued from the judgement, and every failure mode in section 11 is a collapse of one of those separations.

**P12-6.1 (MUST) Six functions distinguished.** An implementation must distinguish selection, determination, review, decision, attestation and surveillance as six activities and must record each separately. **Source.** The conformity assessment vocabulary describes conformity assessment through a functional approach comprising selection, determination, review, decision, attestation and surveillance, and states that the approach describes functions rather than prescribing organisational models.

**P12-6.2 (MUST) Determination separated from decision.** An implementation must record what the evidence showed separately from the judgement reached on it, and must not conflate a determination with a finding.

**P12-6.3 (MUST) Review recorded.** An implementation must record the review of the determination before the decision, naming the reviewing party.

**P12-6.4 (MUST NOT) No attestation without a decision.** An implementation must not issue an assurance statement that does not cite the decision it rests on.

**P12-6.5 (MUST) Reviewer distinct from determiner where depth is comprehensive.** An implementation must require, for an assessment at comprehensive depth, that the reviewing party be a party other than the one that gathered the evidence, and must record where it was not.

### 6.2 Determinism and reproducibility of an assessment

**P12-6.6 (MUST) Finding reproducible from its evidence.** An implementation must reach the same finding from the same evidence items, determination statement and criterion version, and must record a case in which it did not.

**P12-6.7 (MUST) Re-performance supported.** An implementation must be able to re-perform a recorded assessment from its plan, and must report `not_reproducible` where a plan input cannot be resolved.

**P12-6.8 (MUST NOT) No finding dependent on the assessor's identity.** An implementation must not permit a finding to differ by assessor for the same evidence and criterion, and must record any such divergence as a defect of the determination statement rather than of either assessor.

**P12-6.9 (MUST) Divergence between assessors exposed.** An implementation must expose every determination statement on which two registered assessors reached different findings from the same evidence, since such a statement is ambiguous and the ambiguity is in the statement.

**P12-6.10 (MUST NOT) No clock in a finding.** An implementation must not make a finding depend on the instant of assessment other than through the interval the plan declares.

### 6.3 Criterion resolution

**P12-6.11 (MUST) Criteria extracted by a declared method.** An implementation must declare the method by which it extracts clauses from a part and must apply it uniformly.

**P12-6.12 (MUST) Extraction count reconciled against the part.** An implementation must reconcile the count of criteria it extracted from a part against the derived count that part publishes, and must record any discrepancy.

**P12-6.13 (MUST) Discrepancy reported to the part's author.** An implementation must report a discrepancy between its extraction and a part's published clause count as a defect requiring resolution and must not proceed on its own count.

**P12-6.14 (MUST NOT) No assessment against an unresolved criterion.** An implementation must not assess against a criterion whose clause text could not be resolved.

**P12-6.15 (MUST) Version change triggers reclassification review.** An implementation must review the assessability classification of every criterion whose clause text changed between part versions.

### 6.4 Method selection

**P12-6.16 (MUST) Method appropriate to the class.** An implementation must select a method consistent with the criterion's assessability class and must record the selection.

**P12-6.17 (MUST) Depth and coverage declared per method application.** An implementation must declare depth and coverage for every application of a method and must record both as achieved. **Source.** The security control assessment guidance attaches depth and coverage attributes to assessment methods, with values basic, focused and comprehensive, defining depth as the rigour and level of detail and coverage as the scope and breadth including the number and type of objects examined or tested and of individuals interviewed.

**P12-6.18 (MUST NOT) No interview as sole evidence for a mechanism.** An implementation must not record a finding about a mechanism whose only evidence is an interview.

**P12-6.19 (MUST NOT) No examination of documentation as sole evidence for a behaviour.** An implementation must not record a finding about a behaviour whose only evidence is an examination of a specification.

**P12-6.20 (MUST) Elicitation required where the class requires it.** An implementation must not record a satisfied finding for a criterion classed `elicitation_required` without an elicitation record, and must record the outcome that names the missing elicitation.

**P12-6.21 (MUST) Construction only findings marked as inspection.** An implementation must record a finding for a criterion classed `construction_only` as resting on inspection and must record that no behaviour was observed.

### 6.5 The evidence weight rules

**P12-6.22 (MUST) Weight ordered and declared.** An implementation must treat evidence provenance as ordered, with independently reconstructed and elicited above observed, and observed above self reported, and must apply the ordering uniformly.

**P12-6.23 (MUST NOT) No satisfied finding at self reported provenance.** An implementation must not record a satisfied finding whose strongest provenance is self reported.

**P12-6.24 (MUST) Reliance proportion computed.** An implementation must compute and expose, per assessment run and per part, the proportion of findings whose strongest provenance is self reported.

**P12-6.25 (MUST) Contradicting evidence resolved explicitly.** An implementation must record, where evidence contradicts, either the finding that resolves it with the reason or the outcome that names the conflict, and must not silently prefer the supporting item.

**P12-6.26 (MUST NOT) No preference for the assessed component's account.** An implementation must not resolve a conflict between an independently reconstructed item and a self reported item in favour of the self reported item.

**P12-6.27 (MUST) Absence of evidence distinguished from evidence of absence.** An implementation must record a failure to find evidence of a behaviour as not assessed rather than as evidence that the behaviour does not occur, unless the plan declared a method capable of establishing absence and the method was applied.

### 6.6 Frames, sampling and the three unenumerable populations

Three parts handed this component the same problem and this subsection is the discharge of it. `Part 7` cannot compel an enforcement point to report; `Part 10` cannot compel a consumer to report what it holds; `Part 11` cannot compel a referrer to register. Each counted the population it could not see, exposed it as a signal, concluded that the remedy lay outside itself, and named this component.

The mechanism this part supplies is attested sampling, and it works only where the frame can be enumerated. Where the frame is enumerable, a probability sample is drawn, and for each member an attestation is obtained by a channel the assessed component does not control, so that the assessed component's own figure is tested against evidence it did not produce. Where the frame is not enumerable, no sample can be drawn, and this part refuses to approximate: the population is recorded as unassessed and the assessed component's figure is reported as unverified.

That is a partial discharge and it is the honest extent of one. The reason the three populations are hard is precisely that they are not enumerable from inside the estate: an enforcement point that never contacts the decision point, a consumer that fetched once and cached, and a component that holds an address in a record nobody registered are all invisible by construction. Making them enumerable requires a composition level obligation that every component be registered and that every pin be declared, which is `Part 0`'s and which section 13.9 hands to it. This component can then sample the register. Until then, what this part supplies is a sound method over the enumerable part and an honest refusal over the rest.

**P12-6.28 (MUST) Enumerability determined before sampling.** An implementation must determine and record the enumerability of a frame before drawing any sample from it.

**P12-6.29 (MUST NOT) No sample from a non enumerable frame.** An implementation must not draw a sample from a non enumerable frame and must not report a coverage proportion over one.

**P12-6.30 (MUST) Attestation obtained by an independent channel.** An implementation must obtain, for each sampled member of a population the assessed component reports on, an attestation by a channel the assessed component does not control, and must record where it could not.

**P12-6.31 (MUST) Assessed component's figure tested, not accepted.** An implementation must compare the assessed component's reported figure with the attestations it obtained and must record the discrepancy.

**P12-6.32 (MUST NOT) No acceptance of a reported population figure as a finding.** An implementation must not record a satisfied finding about a population figure whose only evidence is the assessed component's report of it.

**P12-6.33 (MUST) Unenumerable residue reported with every coverage figure.** An implementation must report, with every coverage figure over a partially enumerable frame, the description and, where estimable, the size of the residue it did not assess.

**P12-6.34 (MUST NOT) No estimate of a residue presented as measured.** An implementation must not present an estimate of an unenumerable residue as a measurement.

**P12-6.35 (MUST) Second enumeration used where one exists.** An implementation must, where a second independent enumeration of a frame exists, compare the two and record the discrepancy as a bound on the completeness of both.

**P12-6.36 (MUST) Non response recorded as non response.** An implementation must record a sampled member that did not respond to an attestation request as a non response and must not exclude it from the sample or impute a response.

**P12-6.37 (MUST) Non response rate published.** An implementation must publish the non response rate of every attested sample, since a sample with a high non response rate is a sample of the responsive.

### 6.7 Elicitation

**P12-6.38 (MUST) Permission required per part.** An implementation must not introduce a probe into an implementation of a part whose clauses do not permit elicitation, and must record the criterion as unassessable by elicitation where permission is absent.

**P12-6.39 (MUST) Coverage gap declared where permission is absent.** An implementation must declare, for every criterion classed `elicitation_required` in a part that does not permit elicitation, that the criterion cannot be assessed and that the gap follows from the part's own requirement.

**P12-6.40 (MUST) Conformance instance used where production is forbidden.** An implementation must, where a part forbids writes during assessment, perform elicitation against a separate conformance instance where one exists, and must record the instance class and the limits of the inference.

**P12-6.41 (MUST) Expected outcome fixed before introduction.** An implementation must fix and record the expected outcome before introducing a probe.

**P12-6.42 (MUST) Probe selection unpredictable.** An implementation must select probe instances by a means the assessed component cannot anticipate.

**P12-6.43 (MUST) Method class published, instances withheld.** An implementation must publish the class of probes it uses and must not publish the instances it will use in advance.

**P12-6.44 (MUST) Indistinguishability tested, not assumed.** An implementation must test whether an assessed component can distinguish a probe and must record the test rather than asserting indistinguishability.

**P12-6.45 (MUST) Detection invalidates the ordinary inference.** An implementation must record a finding resting on a detected probe as evidence about the component's treatment of probes and must not express it as a finding about ordinary behaviour.

**P12-6.46 (MUST) Side effects bounded and reversed.** An implementation must bound the side effects of every probe, must reverse every reversible probe, and must record every probe left in place.

**P12-6.47 (MUST NOT) No probe that could cause a nonconformity.** An implementation must not introduce a probe whose effect would itself cause the assessed component to breach a clause of its own part, and must record the refusal of such a probe.

### 6.8 Review, decision and attestation

**P12-6.48 (MUST) Decision cites the findings.** An implementation must cite every finding a decision rests on.

**P12-6.49 (MUST NOT) No decision beyond the findings.** An implementation must not reach a decision that the findings do not support, and must record the reasoning where a decision rests on findings that are not unanimous.

**P12-6.50 (MUST) Attestation party class determined by independence.** An implementation must determine the party class of an attestation from the declared independence and must not assign third party where any independence form is absent.

**P12-6.51 (MUST NOT) No attestation of an object the attesting party provided.** An implementation must not issue a third party attestation about an object the attesting party provides.

**P12-6.52 (MUST) Scope of attestation recorded.** An implementation must record the range of objects an attestation covers and must not permit it to be read as covering objects outside that range. **Source.** The conformity assessment vocabulary defines the scope of attestation as the range or characteristics of objects covered by the attestation, which exists because an attestation read outside its scope is the commonest misuse of one.

### 6.9 Surveillance and decay

**P12-6.53 (MUST) Cadence applied per statement class.** An implementation must perform surveillance at the declared cadence for the class of the statement and must record every iteration.

**P12-6.54 (MUST) Object change detected, not awaited.** An implementation must monitor for changes to the object version an assurance statement names and must supersede the statement on a change in a covered respect.

**P12-6.55 (MUST) Frame change treated as an object change.** An implementation must supersede an assurance statement whose frame has changed materially, since a conclusion over a population is not a conclusion over a different population.

**P12-6.56 (MUST NOT) No extension of a validity interval.** An implementation must not extend the validity interval of an issued statement, and must express continued assurance as a new statement.

**P12-6.57 (MUST) Lapse exposed.** An implementation must expose every statement whose surveillance lapsed and the interval since the last iteration.

### 6.10 Concurrency, idempotence and bounds

**P12-6.58 (MUST) Concurrent findings on one statement serialised.** An implementation must serialise concurrent findings against one determination statement for one object and must record the losing attempt.

**P12-6.59 (MUST) Repeated evidence recording idempotent.** An implementation must treat a repeated recording of an identical evidence item under the same idempotency key as idempotent.

**P12-6.60 (MUST) Assessment effort bound declared.** An implementation must declare a bound on the effort of a single assessment run, must record the bound, and must report a run that reached it as incomplete rather than as complete. The value is an implementation decision because the useful bound depends on the number of criteria and the depth declared, neither of which this part constrains.

**P12-6.61 (MUST) Bound reached recorded in coverage.** An implementation must record a bound reached as a shortfall in achieved coverage.

### 6.11 The assessment of this component

**P12-6.62 (MUST) Own criteria registered.** An implementation must register the criteria of this part alongside those of every other part.

**P12-6.63 (MUST) Own classification performed by the external assessor.** An implementation must obtain the assessability classification of this part's own criteria from the external assessor and must not classify its own criteria.

**P12-6.64 (MUST) Own findings recorded as received, not made.** An implementation must record every finding about itself as received from the external assessor, with that assessor's identity and independence declaration.

**P12-6.65 (MUST NOT) No amendment of a received finding.** An implementation must not amend, requalify or aggregate a finding it received about itself, and may only record a dispute.

**P12-6.66 (MUST) Own nonconformities exposed identically.** An implementation must expose nonconformities against itself on the same terms and in the same projections as nonconformities against any other component.

**P12-6.67 (MUST) Absence of external assessment exposed as a nonconformity.** An implementation must record the absence of a current external assessment of itself as an open nonconformity against clause P12-3.13 and must expose it.

Clause P12-6.67 is the clause a reviewer should test first in any implementation of this part. A harness with no external assessment of itself and no nonconformity recording that fact has failed at the only point where its own standard applies to it, and it will be reporting on twelve other components while carrying an undeclared exemption for itself.

### 6.12 What this component may compute and what it may not

**P12-6.68 (MUST NOT) No remediation.** An implementation must not alter any assessed component in order to resolve a nonconformity it recorded.

**P12-6.69 (MUST NOT) No criterion interpretation binding on the part.** An implementation must not represent its determination statements as the meaning of a clause and must attribute them to itself.

**P12-6.70 (MUST NOT) No risk judgement.** An implementation must not compute a risk rating, a materiality judgement or a business consequence from a finding, and must confine itself to the finding and its qualifications.

**P12-6.71 (MUST NOT) No prioritisation of nonconformities.** An implementation must not rank nonconformities for remediation, which is a decision for their owners.

**P12-6.72 (MUST) Severity derived from modality only where derived at all.** An implementation must derive any severity it records from the modality of the criterion or from a severity the part itself declares, and must record an assessor judgement of severity as such.

## 7. Outcome and failure taxonomy

### 7.1 Why the taxonomy is the specification

Every other part of this standard has a taxonomy whose purpose is to prevent a non result being reported as a negative. This part's taxonomy prevents the opposite: a non result reported as a positive.

A conventional harness has two outcomes, pass and fail, and a third it uses without admitting it, which is blank. Everything that is not a demonstrated failure becomes a pass, and blank becomes a pass at the next aggregation. Eight distinct conditions arrive at the reader as pass: a criterion satisfied on independently reconstructed evidence, a criterion satisfied on the component's own word, a criterion in scope and never reached, a criterion excluded from scope, a criterion that states no checkable property, a criterion that could not be assessed because access was refused, a criterion whose evidence conflicted, and a criterion whose assessment was prevented by the assessed part's own prohibition on elicitation. Seven of the eight are not evidence of anything and one of them is evidence that the standard cannot be assessed at that point.

This is also the section that makes the standard honest about itself. A harness conforming to this part will publish, per part, how many of that part's clauses state properties nobody can check. That number has never to my knowledge been published for any enterprise standard, and it is the number a reader should want first.

**P12-7.1 (MUST) One enumeration per value.** An implementation must draw every value it returns from exactly one enumeration in this section.

**P12-7.2 (MUST NOT) No value outside the enumerations.** An implementation must not return a value outside these enumerations and must not extend one marked closed.

**P12-7.3 (MUST) Properties of an outcome exposed.** An implementation must expose, for every finding outcome, the three properties in the table in section 7.6.

### 7.2 Finding outcomes

Closed enumeration.

| Value | Meaning |
|---|---|
| `satisfied` | The determination statement was established on evidence whose strongest provenance is observed, independently reconstructed or elicited |
| `satisfied_self_reported_only` | The statement appears satisfied and every supporting item is self reported or was influenceable by the assessed component |
| `not_satisfied` | A sound counterexample or contradicting evidence establishes that the statement is false |
| `not_satisfied_partially` | The statement holds over part of the coverage achieved and fails over another part, both stated |
| `not_assessed_in_scope` | The statement was in the plan's scope and was not reached |
| `not_assessed_bound_reached` | The declared effort bound was reached before the statement was assessed |
| `out_of_scope` | The statement was deliberately excluded by the plan, with the exclusion recorded |
| `not_assessable_construction` | The criterion states no property any method of this part can determine |
| `not_assessable_access_refused` | Assessment required access that was not granted |
| `not_assessable_elicitation_forbidden` | The criterion requires elicitation and the assessed part forbids it |
| `not_assessable_frame_unenumerable` | The statement is about a population that cannot be enumerated |
| `indeterminate_evidence_conflict` | Evidence supports and contradicts, and the conflict was not resolved |
| `indeterminate_evidence_insufficient` | The evidence gathered does not decide the statement either way |
| `indeterminate_not_reproducible` | The assessment could not be re-performed from its recorded inputs |
| `superseded_criterion_changed` | The criterion's text changed in a later part version and the finding was not carried forward |

**P12-7.4 (MUST) Satisfied requires provenance above self report.** An implementation must return `satisfied` only where the strongest provenance among the supporting items is observed, independently reconstructed or elicited.

**P12-7.5 (MUST NOT) No collapse to satisfied.** An implementation must not return `satisfied` in place of any other value in section 7.2.

**P12-7.6 (MUST NOT) No collapse to not satisfied.** An implementation must not return `not_satisfied` in place of any indeterminate or not assessable value, since a failure to assess is not a failure to conform.

**P12-7.7 (MUST) Five unassessable causes distinguished.** An implementation must distinguish the four `not_assessable` values and `not_assessed_in_scope` and must not report them as one.

**P12-7.8 (MUST) Out of scope distinguished from not reached.** An implementation must distinguish a statement deliberately excluded from one in scope and not reached, since the first is a decision and the second is a shortfall.

**P12-7.9 (MUST) Access refused attributed.** An implementation must record, with `not_assessable_access_refused`, the party that refused and the access requested.

**P12-7.10 (MUST) Elicitation forbidden attributed to the part.** An implementation must record, with `not_assessable_elicitation_forbidden`, the clause of the assessed part that forbids the write, so that the coverage gap is attributable to the standard rather than to the assessor.

**P12-7.11 (MUST) Conflict retained, not resolved by preference.** An implementation must return `indeterminate_evidence_conflict` where contradicting evidence was not resolved on stated grounds, and must not resolve it by preferring one provenance without recording the reason.

### 7.3 There is no conformant outcome

**P12-7.12 (MUST NOT) No conformance outcome.** An implementation must not provide, return or record any outcome value meaning that a component conforms to a part.

**P12-7.13 (MUST NOT) No aggregate outcome over a part.** An implementation must not provide an outcome value whose object is a part rather than a determination statement.

**P12-7.14 (MUST NOT) No pass or fail vocabulary.** An implementation must not label an outcome pass, fail, compliant or certified in any interface or projection.

**P12-7.15 (MUST) Satisfied bounded to the statement.** An implementation must express `satisfied` as concerning one determination statement over one stated coverage and must not permit it to be read as concerning the criterion universally.

### 7.4 Assurance statement outcomes

Closed enumeration.

| Value | Meaning |
|---|---|
| `not_falsified` | Every declared falsification attempt failed, at the declared depth over the declared coverage of the declared frame |
| `falsified` | At least one claim within scope was established false |
| `partially_falsified` | Some claims within scope were falsified and others were not, both enumerated |
| `inconclusive` | The attempts did not decide the claim, for a recorded reason |
| `not_attempted` | The claim was registered and no falsification attempt was made |
| `unfalsifiable` | No evidence could contradict the claim as stated |
| `withdrawn` | The statement was withdrawn, for a recorded reason |

**P12-7.16 (MUST) Not falsified is the strongest outcome.** An implementation must treat `not_falsified` as the strongest positive outcome available and must not provide a stronger one.

**P12-7.17 (MUST NOT) No not falsified without an attempt.** An implementation must not return `not_falsified` where no falsification attempt was made, and must return `not_attempted`.

**P12-7.18 (MUST) Unfalsifiable claims reported to their author.** An implementation must report a claim it classifies as unfalsifiable to the party that made it, since a claim no evidence could contradict is a claim that conveys nothing.

**P12-7.19 (MUST) Partial falsification enumerated on both sides.** An implementation must enumerate both the falsified and the not falsified claims when returning `partially_falsified` and must not report the aggregate alone.

**P12-7.20 (MUST) Inconclusive reasoned.** An implementation must record the reason an assurance statement is inconclusive from the values of section 7.2 that produced it.

### 7.5 Operation outcomes

Open enumeration, extended under section 9.

| Value | Meaning |
|---|---|
| `applied` | The change was made |
| `applied_idempotent` | Already applied under the same key |
| `idempotency_conflict` | The key was seen with different arguments |
| `refused_plan_after_evidence` | A plan amendment was attempted after evidence gathering began |
| `refused_no_frame` | A plan or statement was attempted with no frame declaration |
| `refused_no_independence_declaration` | A plan was attempted without the three independence forms |
| `refused_assessor_out_of_scope` | The named assessor's registration does not cover a criterion in the plan |
| `refused_no_evidence` | A finding was attempted with no evidence item |
| `refused_self_report_only` | A satisfied finding was attempted on self reported evidence alone |
| `refused_no_permission_for_elicitation` | A probe was attempted without a cited permission |
| `refused_probe_would_cause_nonconformity` | A probe was refused because its effect would breach the assessed part |
| `refused_own_ownership` | This component was named as the owner of a nonconformity |
| `refused_acceptance_incomplete` | An acceptance lacked an expiry, an authorisation or a reason |
| `refused_closure_without_reassessment` | A closure was attempted without a reassessment finding |
| `refused_statement_incomplete` | A statement lacked method, depth, coverage, frame, interval or decay basis |
| `refused_self_assessment` | This component attempted to record an assessment of itself |
| `refused_criterion_unresolved` | The clause text of a criterion could not be resolved |
| `refused_extraction_discrepancy` | The extracted clause count disagrees with the part's published count |
| `not_authorised` | `Part 7` denied the operation |
| `authorisation_unavailable` | `Part 7` could not be reached, and the operation was denied |
| `malformed` | The request could not be interpreted |
| `system_fault` | A value from section 7.7 |

**P12-7.21 (MUST) Refusal reasons distinguished.** An implementation must return the specific refusal reason and must not return one refusal for another.

**P12-7.22 (MUST) Self assessment refusal explicit.** An implementation must return `refused_self_assessment` where it is asked to assess itself and must not silently record the attempt as an assessment.

### 7.6 What distinguishes each outcome from a positive

**P12-7.23 (MUST) Three properties exposed.** An implementation must expose the three properties in the following table with every finding outcome it returns.

| Outcome | Evidence exists | Independent of the assessed party | Reader may rely on the statement holding |
|---|---|---|---|
| `satisfied` | yes | yes | over the recorded coverage only |
| `satisfied_self_reported_only` | yes | no | no |
| `not_satisfied` | yes | as recorded | the statement is false |
| `not_satisfied_partially` | yes | as recorded | over the stated parts only |
| `not_assessed_in_scope` | no | not applicable | no |
| `not_assessed_bound_reached` | no | not applicable | no |
| `out_of_scope` | no | not applicable | no |
| `not_assessable_construction` | no | not applicable | no, and no method would help |
| `not_assessable_access_refused` | no | not applicable | no |
| `not_assessable_elicitation_forbidden` | no | not applicable | no, and the standard prevents it |
| `not_assessable_frame_unenumerable` | partial | as recorded | no |
| `indeterminate_evidence_conflict` | yes, contradictory | as recorded | no |
| `indeterminate_evidence_insufficient` | yes, insufficient | as recorded | no |
| `indeterminate_not_reproducible` | yes, unrepeatable | as recorded | no |
| `superseded_criterion_changed` | yes, about a prior version | as recorded | no |

One of the fifteen permits reliance, and it permits it only over the coverage the finding records. A harness reporting pass and fail has told the reader that fourteen of the fifteen are the one that permits reliance.

### 7.7 System fault outcomes

Closed enumeration.

| Value | Meaning |
|---|---|
| `record_store_unavailable` | The assessment record store could not be read or written |
| `dependency_unavailable` | A required component could not be reached |
| `criterion_source_unavailable` | The part or its clause octets could not be resolved |
| `internal_invariant_violated` | The harness detected a violation of its own invariants |

**P12-7.24 (MUST NOT) No fault reported as a finding.** An implementation must not report a system fault as a finding or an assurance statement outcome.

**P12-7.25 (MUST) Invariant violation halts issuance.** An implementation must stop issuing assurance statements on detecting `internal_invariant_violated` and must raise the fault.

### 7.8 Propagation

**P12-7.26 (MUST) Outcome carried with its qualifications.** An implementation must return every outcome together with its provenance, depth, coverage and frame and must not return the outcome value alone.

**P12-7.27 (MUST NOT) No aggregation losing the distinctions.** An implementation must not aggregate outcomes into a summary that loses the distinction between satisfied, satisfied on self report, not assessed and not assessable.

**P12-7.28 (MUST) Counts report each outcome as its own category.** An implementation must report every outcome value as its own category in any count it publishes.

**P12-7.29 (MUST) Non results retained where unconsumed.** An implementation must retain a non result in the record of the affected finding where no consumer subscribes to it.

## 8. Observability and the audit record

### 8.1 The harness's own asymmetry

Three parts before this one recorded that they can prove what they did and not what happened. This component has the same shape and a sharper form of it: it can prove what it assessed and it cannot prove that what it assessed was representative.

Its own record is complete. Every plan, evidence item, finding and statement is written by it. What it cannot see is the population its samples came from, wherever that population was declared by the party under assessment, and whether the behaviour it elicited was the behaviour that occurs when it is not looking. Those two are the whole of the harness's epistemic exposure and both are countable.

**P12-8.1 (MUST) Completeness of each record declared.** An implementation must declare, for every figure it publishes, whether the underlying record is complete by construction or incomplete by construction.

**P12-8.2 (MUST NOT) No coverage figure without its frame provenance.** An implementation must not publish a coverage figure without stating who declared the frame and whether the declaration was independently examined.

### 8.2 Grain

**P12-8.3 (MUST) Grain stated with every count.** An implementation must state the grain and the instant of computation with every count it reports.

**P12-8.4 (MUST) Criterion counts state their assessability classes.** An implementation must state which assessability classes a count of criteria includes.

**P12-8.5 (MUST) Finding counts state their provenance distribution.** An implementation must state, with every count of satisfied findings, how many rest on each provenance.

**P12-8.6 (MUST NOT) No count spanning part versions.** An implementation must not report one count of criteria or findings spanning two versions of a part without stating the split.

**P12-8.7 (MUST) Object grain stated.** An implementation must state whether a count of findings counts determination statements, criteria, objects or runs.

### 8.3 What must be recorded

**P12-8.8 (MUST) Every plan recorded before its evidence.** An implementation must record every assessment plan with the instant of declaration, before any evidence attributed to it.

**P12-8.9 (MUST) Every evidence item recorded with provenance.** An implementation must record every evidence item it gathered, including items that contradicted the eventual finding.

**P12-8.10 (MUST) Every finding recorded with its qualifications.** An implementation must record every finding with its outcome, evidence, strongest provenance, achieved depth and achieved coverage.

**P12-8.11 (MUST) Every elicitation recorded.** An implementation must record every probe introduction, withdrawal, detection and abandonment in place.

**P12-8.12 (MUST) Every sample recorded in full.** An implementation must record every sample drawn, its scheme, its members and its non responses.

**P12-8.13 (MUST) Every frame examination recorded.** An implementation must record every independent examination of a frame declaration and its outcome.

**P12-8.14 (MUST) Every reclassification recorded.** An implementation must record every change of assessability class with its prior value and reason.

**P12-8.15 (MUST) Every acceptance and expiry recorded.** An implementation must record every acceptance of a nonconformity, its expiry and its reopening.

**P12-8.16 (MUST) Every dispute recorded.** An implementation must record every dispute of a finding and its resolution.

**P12-8.17 (MUST) Every trust base change recorded.** An implementation must record every addition, removal, reclassification and falsification of a trust base item.

**P12-8.18 (MUST) Every external assessment of itself recorded.** An implementation must record every assessment of itself received from another party, unaltered.

### 8.4 What must be reconstructable

**P12-8.19 (MUST) The plan behind any finding.** A reader must be able to reconstruct the plan a finding was made under, including the depth and coverage planned and the frame declared.

**P12-8.20 (MUST) The evidence behind any finding.** A reader must be able to reconstruct every evidence item a finding rests on, with its provenance, and every item that contradicted it.

**P12-8.21 (MUST) The clause text a finding was made against.** A reader must be able to reconstruct the exact clause text, at the part version, that a finding was made against.

**P12-8.22 (MUST) The independence of any assessment.** A reader must be able to reconstruct the three declared independence forms of any assessment and any conflicts declared.

**P12-8.23 (MUST) The frame and the sample.** A reader must be able to reconstruct the frame of any coverage figure, its enumerability, the sample drawn and the non response.

**P12-8.24 (MUST) The assessability history of any criterion.** A reader must be able to reconstruct the assessability class of any criterion at any past instant and every reclassification.

**P12-8.25 (MUST) The trust base at any instant.** A reader must be able to reconstruct the trust base as it stood at any past instant.

**P12-8.26 (MUST) Whether this component was itself assessed at any instant.** A reader must be able to establish, for any past instant, whether a current external assessment of this component existed.

**P12-8.27 (MUST NOT) No reconstruction dependent on this component running.** An implementation must not require its own runtime to be available for any reconstruction in section 8.4.

### 8.5 Signals

Each signal names a population this component can count and, in most cases, cannot remedy.

**P12-8.28 (MUST) Unassessable criterion population per part.** An implementation must expose, per part and part version, the count and identifiers of criteria classified `not_assessable`.

**P12-8.29 (MUST) Elicitation forbidden population.** An implementation must expose every criterion that requires elicitation and belongs to a part that forbids it, since that population is a coverage gap the standard creates.

**P12-8.30 (MUST) Self report reliance proportion.** An implementation must expose, per part and per run, the proportion of findings whose strongest provenance is self reported.

**P12-8.31 (MUST) Never assessed criterion population.** An implementation must expose every registered criterion never assessed for any object.

**P12-8.32 (MUST) Coverage over unenumerable frames.** An implementation must expose every determination statement whose frame is not enumerable, with the assessed component's own figure marked unverified.

**P12-8.33 (MUST) Non response rate per attested sample.** An implementation must expose the non response rate of every attested sample.

**P12-8.34 (MUST) Overdue surveillance population.** An implementation must expose every assurance statement whose surveillance is overdue and the interval since its last iteration.

**P12-8.35 (MUST) Expired and superseded statement population.** An implementation must expose every statement that lapsed or was superseded without replacement.

**P12-8.36 (MUST) Accepted nonconformity population.** An implementation must expose every accepted nonconformity with its expiry, its owner and the number of times it has been accepted.

**P12-8.37 (MUST) Repeatedly accepted population.** An implementation must expose every nonconformity accepted more than once, since a nonconformity re-accepted at each expiry has been converted into a permanent exemption by increments.

**P12-8.38 (MUST) Disputed finding population.** An implementation must expose every disputed finding and the age of the dispute.

**P12-8.39 (MUST) Probes in place population.** An implementation must expose every probe introduced and not withdrawn.

**P12-8.40 (MUST) Compromised probe population.** An implementation must expose every probe known to have been detected.

**P12-8.41 (MUST) Assessor divergence population.** An implementation must expose every determination statement on which registered assessors reached different findings from the same evidence.

**P12-8.42 (MUST) Its own nonconformity population.** An implementation must expose nonconformities against itself in the same projection as those against every other component and must not place them in a separate view.

**P12-8.43 (SHOULD) Trust base growth signal.** An implementation should expose the rate at which trust base items are added, since a growing trust base is a shrinking assessment.

### 8.6 The evidence package

**P12-8.44 (MUST) Package assemblable for a finding.** An implementation must be able to assemble, for any finding, a package containing the criterion text, the determination statement, the plan, every evidence item with its provenance, the elicitation records, the sample, the frame examination, the independence declaration and the finding itself.

**P12-8.45 (MUST) Package assemblable for a statement.** An implementation must be able to assemble, for any assurance statement, a package containing every finding it rests on, the falsification attempts, the coverage, the not established set and the surveillance history.

**P12-8.46 (MUST) Package states what it omits.** An implementation must state, in every package, every element it could not include and why.

**P12-8.47 (MUST) Package integrity protected.** An implementation must integrity protect every package by a means governed by `Part 3`.

### 8.7 Retention and what cannot be changed

**P12-8.48 (MUST) Records outlive the object.** An implementation must retain findings, evidence, plans and statements for at least as long as the longest retention obligation attaching to any determination the assessed component made in reliance on them.

**P12-8.49 (MUST NOT) No alteration of a finding, evidence item, plan or issued statement.** An implementation must not alter any of those once written.

**P12-8.50 (MUST NOT) No deletion of contradicting evidence.** An implementation must not delete an evidence item that contradicted a determination statement.

**P12-8.51 (MUST NOT) No removal of a nonconformity.** An implementation must not delete a nonconformity record, including one closed because a criterion was withdrawn.

**P12-8.52 (MUST) Retention notified to the components relied upon.** An implementation must notify `Part 10` and `Part 11` of the retention obligation its own records create over the versions and addresses they hold, per those parts' retention floor requirements.

## 9. Extension model

### 9.1 Closed sets and open sets

The extension model of this part is the most restrictive in the standard, and deliberately. Nine other parts open their kind registries wide, because the content they govern is heterogeneous and unpredictable. This component governs no content: it governs a vocabulary in which conclusions about other components are expressed, and a vocabulary that an implementation may extend is a vocabulary in which two implementations reach conclusions that cannot be compared. What is open here is the machinery of gathering evidence and what is closed is everything that appears in a conclusion.

**P12-9.1 (MUST) Closed sets not extended.** An implementation must not extend the following: assessability classes, finding outcomes, assurance statement outcomes, system fault outcomes, evidence provenance kinds, assessment methods, assessment object kinds, depth values, coverage values, independence forms, attestation party classes, frame enumerability values, run states, statement states, nonconformity states, probe states and trust base item states.

**P12-9.2 (MUST) Open sets extended only through a registry.** An implementation must extend the following only through the registries of section 9.2: probe kinds, sampling schemes, assessors, part registrations, refusal codes and surveillance cadence classes.

**P12-9.3 (MUST NOT) No new outcome for a new subject.** An implementation must not introduce a finding outcome to accommodate a new kind of criterion, and must classify the criterion under an existing assessability class or report it as `not_assessable_construction`.

The outcomes and classes are closed because they are the vocabulary in which this component's record speaks and because section 7.6 classifies exactly the members listed. The four methods are closed for a stronger reason: a fifth method would be a new way of obtaining evidence, and the weight ordering of section 6.5 would have no place for it, so a new method must be raised against this part rather than registered.

### 9.2 Registry mechanics

**P12-9.4 (MUST) Registration before use.** An implementation must require every open set member to be registered before an assessment uses it.

**P12-9.5 (MUST) Definition mandatory at registration.** An implementation must require a definition of every registered member's meaning.

**P12-9.6 (MUST) Registration attributable.** An implementation must record the registering party, the instant and the authorising decision for every registration.

**P12-9.7 (MUST NOT) No meaning change under a registered identifier.** An implementation must not alter the meaning of a registered member and must express a change as a new member.

**P12-9.8 (MUST) Retirement recorded, findings retained.** An implementation must retain every finding produced using a retired member and must not remove the member from the register.

### 9.3 The probe kind registry

**P12-9.9 (MUST) Probe kind semantics registered.** An implementation must register, for every probe kind, what it introduces, what behaviour it elicits, its side effects and its reversibility.

**P12-9.10 (MUST) Indistinguishability method registered.** An implementation must register the means by which a probe kind is made indistinguishable from ordinary input, or must record that it is not.

**P12-9.11 (MUST) Applicability recorded per part.** An implementation must record, for every probe kind, the parts whose clauses permit its use.

### 9.4 The sampling scheme registry

**P12-9.12 (MUST) Selection method registered.** An implementation must register the selection method of every sampling scheme and whether it is probabilistic.

**P12-9.13 (MUST) Enumerability requirement recorded.** An implementation must record, for every sampling scheme, that it requires an enumerable frame.

**P12-9.14 (MUST NOT) No scheme registered that operates on a non enumerable frame.** An implementation must not register a sampling scheme that purports to sample a frame that cannot be enumerated.

### 9.5 The assessor registry

**P12-9.15 (MUST) Scope recorded per assessor.** An implementation must record the criteria each registered assessor may assess.

**P12-9.16 (MUST) Competence basis recorded.** An implementation must record the basis of each assessor's competence, including where it is merely declared.

**P12-9.17 (MUST) Mutual assessment recorded.** An implementation must record, for every pair of registered assessors, whether either has assessed the other and when.

**P12-9.18 (MUST NOT) No assessor registered as its own peer.** An implementation must not record an assessor as having peer assessed itself.

### 9.6 Part registration

**P12-9.19 (MUST) Parts registered with their versions.** An implementation must register every part and part version it assesses against.

**P12-9.20 (MUST) Elicitation permission recorded per part.** An implementation must record, per part version, whether and under what conditions that part permits elicitation.

**P12-9.21 (MUST) Read only requirement recorded per part.** An implementation must record, per part version, whether that part requires assessment to be performed without writes.

**P12-9.22 (MUST) Conflicting requirements recorded.** An implementation must record, where two parts impose conflicting requirements on this component, the conflict and the resolution it applied, per section 10.7.

## 10. Standards and specifications

### 10.1 How the citations in this part are to be read

Each entry states what the source supplies, the edition established as current at the date of this part, and whether this part's account rests on specification text or on secondary sources. Section 13.1 lists the sources not obtained in full text.

This part has more usable normative material than most in this standard, because conformity assessment is itself a standardised field with a vocabulary, a functional model, a body of requirements for assessing bodies and a mechanism for terminating its own regress. What none of it supplies is the reflexive case: a harness assessing components of the system it is part of, against a standard whose clauses it must first classify by whether they can be assessed at all.

**P12-10.1 (MUST) Cited edition recorded.** An implementation must record the edition or version of every external standard it relies upon and must not cite a standard without its edition.

**P12-10.2 (MUST) Basis marked.** An implementation must record, for every control it adopts from a source named in this section, whether the basis is specification text or practice.

### 10.2 The conformity assessment vocabulary and functional model

**Supplies.** The definitions this part adopts unchanged: attestation as the issue of a statement, based on a decision following review, that fulfilment of specified requirements has been demonstrated; declaration as first party attestation; certification as third party attestation about an object; accreditation as third party attestation about a conformity assessment body, conveying formal demonstration of competence, impartiality and consistent operation; third party as independent of the provider of the object and of user interests in it; the absence of a special term for second party attestation; scope of attestation as the range of objects covered; peer assessment as assessment of a body by representatives of other bodies in an agreement group; and surveillance as systematic iteration to maintain the validity of a statement. It supplies the functional approach of selection, determination, review, decision, attestation and surveillance. ISO/IEC 17000:2020, corrected version 2020-12, with the 2004 first edition consulted for the text of several definitions.

**Does not supply.** Any treatment of a harness inside the system it assesses, of the assessability of a requirement, or of a reflexive assessment.

**Basis.** Specification text for the definitions and the functional model, read in the vocabulary's own words or in an authoritative quotation of them.

### 10.3 Guidance on writing assessable requirements

**Supplies.** The principle that a normative document should be written so that fulfilment of its requirements can be determined, and the framing of first, second and third party activity by worked example. ISO/IEC 17007, in its current form.

**Does not supply.** A classification of unassessable requirements, or any obligation on a drafter to publish which of its requirements cannot be assessed. Section 3.6 is this part's own.

**Basis.** Secondary. Obtained from a catalogue summary and a quoted extract; the standard itself was not read.

### 10.4 Assessment method, depth and coverage

**Supplies.** The methods examine, interview and test; the object kinds specification, mechanism, activity and individual; the depth and coverage attributes with values basic, focused and comprehensive; the construction of an assessment objective from determination statements linked to the content of the requirement so that results are traceable to it; and the resulting notion of an assessment finding. NIST Special Publication 800-53A, whose revision current at the date of this part was not established.

**Does not supply.** Elicitation as a method, evidence provenance as an ordered property, or any refusal to sample a non enumerable frame.

**Basis.** Specification text for depth and coverage and for the determination statement construction, quoted from the publication; the revision history was not established and section 13.1 records it.

### 10.5 Evaluation assurance and its meaning

**Supplies.** The principle that an assurance level grades the rigour of an evaluation and not the security of the object, which is the strongest available precedent for section 3.2. The security evaluation criteria and their evaluation methodology.

**Does not supply.** Anything about reflexive assessment. Its assurance levels are also the origin of the practice section 11.16 names as an anti pattern, being the reading of an evaluation grade as a property of the product.

**Basis.** Secondary. Neither the criteria nor the methodology was obtained in this session.

### 10.6 Independence, point in time attestation and the carve out

**Supplies.** Three constructions this part adopts. The separation of technical, managerial and financial independence, from the software verification and validation standards. The distinction between an attestation about the design of controls at a point in time and one about their operating effectiveness over a period, from the service organisation assurance standards. And the carve out, being the express exclusion of a subservice organisation from the scope of an attestation, which is the closest existing analogue to this part's requirement that what was not established be enumerated.

**Basis.** Secondary throughout. None of the three was obtained in this session and section 13.1 records it.

### 10.7 Named conflicts

| Conflict | Position A | Position B | Resolution | Reason |
|---|---|---|---|---|
| Whether assessment may write | `Part 7` clause P7-12.32 requires everything it exposes to be assessable through read operations and requires that no write be needed to assess it | `Part 11` clause P11-12.35 requires this component to plant known content and elicit each of sixteen retrieval outcomes, which are writes | Both, by part. Section 6.38 forbids elicitation where the part does not permit it; section 6.39 requires the resulting coverage gap to be declared and attributed to the part; section 6.40 permits a conformance instance where one exists | The two parts are not wrong about themselves. An authorisation decision point can be assessed by replaying recorded requests, and a store cannot be assessed for integrity reporting without corrupting something. The gap that follows for `Part 7`'s elicitation dependent clauses is real and is now visible rather than silently unassessed |
| Whether assurance may be expressed positively | Practice, and every certification scheme, issues a statement that an object conforms | This part, clauses P12-3.4 and P12-7.12: no outcome means conformant | This part | A finite assessment cannot establish a universal. Section 13.2 records that this position may be unusable by the parties who need assurance and that the pressure to abandon it will be constant |
| Whether an evaluation grade describes the object | Practice reads an assurance level as a property of the evaluated product | The evaluation criteria themselves grade the rigour of the evaluation | The standards, against practice | Section 11.16 names the misreading and clause P12-1.29 refuses to define a grade at all |
| Whether the assessed party may declare the population | Practice accepts the assessed party's declaration of its own population, because only it knows | `Part 7` clause P7-12.34 requires the declared request space to be exposed so that this component can assess whether a coverage figure means anything, and clause P12-3.51 requires every such declaration to be examined | This part and `Part 7` together | A coverage figure over a self declared frame measures the declaration. This is the same structure as clause P12-6.32's refusal to accept a reported population figure as a finding |
| Whether a method may be published | Reproducibility requires the method to be published; publication makes the method satisfiable without the property | This part, clauses P12-6.43 and P12-6.42: the class is published and the instances are unpredictable | This part, partially | Section 13.6 records that this is a mitigation and not a solution, and that a determined party can satisfy a published method class |

### 10.8 What none of the standards supplies

**P12-10.3 (MUST) Requirements of this part alone identified.** An implementation must treat the following as requirements of this part alone, no consulted source supplying them: the assessability classification and the obligation to publish the unassessable population per part; the refusal of any outcome meaning conformant; evidence provenance as an ordered closed set with a satisfied finding forbidden at self reported provenance; elicitation as a fourth method with a permission regime and an indistinguishability requirement; the refusal to sample a non enumerable frame; the enumerated trust base with per item consequence; the requirement that this component be assessed externally and record the absence of such an assessment as a nonconformity against itself; and the mutual assessment record among registered assessors.

## 11. Anti patterns

### 11.1 The green dashboard

**Mechanism.** Findings are aggregated to a colour or a percentage per component, and the aggregate is what anyone looks at.

**Evidence.** Section 7.6 shows that one of fifteen finding outcomes permits reliance. Any aggregate that assigns a single value to a component has mapped the other fourteen onto that one or discarded them.

**Consequence.** The figure moves when the assessment scope changes and does not move when the component changes, which is the opposite of what its readers believe. Nobody asks which criteria are in the denominator, because the figure has already answered the question.

**P12-11.1 (MUST NOT) No single figure per component.** An implementation must not expose a scalar or a colour summarising a component's conformance to a part.

### 11.2 The satisfied finding on the component's own word

**Mechanism.** The assessor asks the component whether it does what a clause requires, records the answer, and marks the clause satisfied.

**Evidence.** Nine parts of this standard forbid a component from presenting its own analysis as assurance. An assessor accepting that analysis has changed who wrote it down and nothing else.

**Consequence.** The assessment measures the component's willingness to report accurately, which is the property least in doubt in the cases where it matters least and most in doubt in the cases where it matters most.

**P12-11.2 (MUST NOT) No satisfied finding at self reported provenance.** An implementation must not record a satisfied finding whose strongest provenance is self reported.

### 11.3 The unassessed criterion counted as satisfied

**Mechanism.** A criterion in scope is not reached, no nonconformity is recorded against it, and the absence of a nonconformity is read as conformance.

**Evidence.** Section 7.2 separates five conditions that produce no nonconformity and none of which is evidence of conformance.

**Consequence.** Coverage becomes invisible. An assessment that reached a tenth of its scope and found nothing wrong reports identically to one that reached all of it.

**P12-11.3 (MUST) Not assessed reported as its own outcome.** An implementation must report a criterion in scope and not reached as `not_assessed_in_scope` and must not omit it.

### 11.4 The unassessable clause counted in the denominator

**Mechanism.** A part's clauses are counted, the assessable ones are assessed, and the proportion satisfied is computed over the whole set or over the assessable subset, without saying which.

**Evidence.** Clause P12-3.32.

**Consequence.** Two figures differ by the size of the unassessable population and both are presented as the conformance of the component. Neither reader knows which they have.

**P12-11.4 (MUST) Denominator declared.** An implementation must state which assessability classes are in the denominator of every proportion.

### 11.5 The scope amended after the failure

**Mechanism.** A check fails, the plan is revised so that the check falls outside scope, and the assessment completes cleanly.

**Evidence.** Clause P12-3.42. Nothing in a conventional output records that the scope moved.

**Consequence.** The assessment is an exercise in confirmation and looks exactly like one that was not. This is the failure that makes an entire assurance function worthless, because it is invisible in every artefact the function produces.

**P12-11.5 (MUST NOT) No plan amended after evidence.** An implementation must not amend a declared plan after evidence gathering has begun.

### 11.6 The convenience sample

**Mechanism.** The objects examined are the ones that were available, or the ones the assessed party offered, and the result is expressed as a proportion of the population.

**Evidence.** Clauses P12-3.56 and P12-3.57.

**Consequence.** The sample is biased in the direction of the assessed party's interest, and the coverage figure carries the bias into every aggregate above it. A sample the assessed party selected measures what the assessed party wanted measured.

**P12-11.6 (MUST NOT) No convenience sample described as probabilistic.** An implementation must not describe a non probabilistic sample as a probability sample.

### 11.7 The sample from a population nobody can list

**Mechanism.** A population that cannot be enumerated is sampled anyway, because a figure is needed, and the sample is drawn from whatever part of it is visible.

**Evidence.** Clause P12-6.29. The visible part of an unenumerable population is visible for a reason, and the reason is usually correlated with the property under assessment.

**Consequence.** The enforcement points that report are sampled, the consumers that refresh are sampled, and the referrers that registered are sampled, so the assessment covers exactly the members that were never the concern.

**P12-11.7 (MUST NOT) No sample from a non enumerable frame.** An implementation must not sample a frame it recorded as not enumerable.

### 11.8 The point in time attestation read as current

**Mechanism.** An assessment made eighteen months ago is cited as the assurance position, because it was the last one and nothing has been reported since.

**Evidence.** Clause P12-3.65 and the surveillance concept: an attestation is about a moment unless iterated.

**Consequence.** Confidence has a half life that nobody computes. The statement is not wrong, and reliance on it is.

**P12-11.8 (MUST NOT) No expired statement presented as current.** An implementation must not present an expired statement as current.

### 11.9 The carve out nobody reads

**Mechanism.** The assessment excludes a dependency, records the exclusion in a place the summary does not reach, and the summary is what circulates.

**Evidence.** The service organisation assurance standards name the construction and require the exclusion to be disclosed, and practice discloses it in a section readers skip.

**Consequence.** The assurance covers a system with a hole in the middle, and the hole is where the risk was. Clause P12-3.6 requires the not established set on every statement for exactly this reason.

**P12-11.9 (MUST) Not established set carried with the statement.** An implementation must carry the not established set on every assurance statement rather than in a separate document.

### 11.10 The probe the component recognised

**Mechanism.** Probes are drawn from a fixed set, or are distinguishable by a marker, and the assessed component handles them correctly and nothing else correctly.

**Evidence.** Clause P12-6.44 requires indistinguishability to be tested. A component that can identify a probe is being assessed on its probe handling path.

**Consequence.** The assessment is systematically wrong in the direction of favourable, and repeats cleanly for years. It is the closest thing in this part to an assessment that is worse than none, because it produces confidence with no relationship to the property.

**P12-11.10 (MUST) Indistinguishability tested.** An implementation must test whether a probe is distinguishable and must record the result.

### 11.11 The method published so precisely that it was engineered to

**Mechanism.** The assessment method, including the specific checks, is published so that components can prepare, and components prepare for the checks.

**Evidence.** Section 13.6. A published check is a specification for the minimum behaviour that satisfies it.

**Consequence.** The measure and the property separate, and the measure keeps improving. Clause P12-6.43 publishes the class and withholds the instances, which mitigates and does not solve it.

**P12-11.11 (MUST NOT) No advance publication of probe instances.** An implementation must not publish in advance the probe instances it will use.

### 11.12 The assessor who advised

**Mechanism.** The party that designed or configured the component assesses it, because it understands it best, which is true.

**Evidence.** Clause P12-3.84 and the independence definitions.

**Consequence.** The assessment cannot find a defect in the design, because a finding of nonconformity is a finding against the assessor's own prior work, and the incentive operates without anyone deciding to be dishonest.

**P12-11.12 (MUST NOT) No advisor as assessor.** An implementation must not accept a finding from an assessor that advised on, designed or configured the object.

### 11.13 The harness that remediated

**Mechanism.** The harness finds a misconfiguration and corrects it, because it is there and the fix is trivial.

**Evidence.** Clause P12-1.16.

**Consequence.** The next assessment finds the component conforming, and it conforms because the assessor made it conform. The record shows a component that met its requirements and does not show that it did so because the party checking supplied the compliance.

**P12-11.13 (MUST NOT) No remediation by the harness.** An implementation must not correct any assessed component.

### 11.14 The harness that assessed itself

**Mechanism.** The harness runs its own clauses against itself and reports the result, because no external assessor exists and something is better than nothing.

**Evidence.** Clause P12-1.30 and clause P12-3.14.

**Consequence.** The one component whose failure would invalidate every other assessment is the one component nobody checked. Clause P12-6.67 converts the absence into a visible nonconformity, which is the most this part can do about it.

**P12-11.14 (MUST) Absence of external assessment recorded as a nonconformity.** An implementation must record the absence of a current external assessment of itself as an open nonconformity.

### 11.15 The regress hidden by one more layer

**Mechanism.** Asked who verifies the verifier, the answer is a further body, and asked who verifies that, the question stops being asked.

**Evidence.** Section 3.4. The conformity assessment world terminates horizontally in peer assessment and states an uncertainty; it does not claim a top.

**Consequence.** Confidence is presented as grounded when it is suspended. The trust base is the thing that would make it honest, and it is precisely the thing that is never written down.

**P12-11.15 (MUST) Trust base enumerated and published.** An implementation must publish the trust base as an enumerated set.

### 11.16 The assurance grade read as a property

**Mechanism.** An evaluation grade is treated as a measure of the object rather than of the evaluation.

**Evidence.** The evaluation criteria themselves define their levels as grades of the rigour of the evaluation.

**Consequence.** Two objects with the same grade are treated as equivalent when one was examined comprehensively against a narrow claim and the other superficially against a broad one.

**P12-11.16 (MUST NOT) No conformance grade defined.** An implementation must not define or assign a graded conformance level.

### 11.17 Mechanism coverage read as requirement coverage

**Mechanism.** Coverage is measured over the mechanisms examined and reported as coverage of the requirements.

**Evidence.** Coverage in the assessment guidance is an attribute of a method's application to objects, not a proportion of requirements met.

**Consequence.** A component with one mechanism serving twenty criteria reports high coverage from one examination. The figure describes the assessor's effort and is read as describing the component.

**P12-11.17 (MUST) Coverage expressed over a declared frame.** An implementation must express coverage over the frame the plan declared and must state what the frame's members are.

### 11.18 The nonconformity accepted at every expiry

**Mechanism.** A nonconformity is accepted for ninety days, and re-accepted at each expiry, indefinitely.

**Evidence.** Clause P12-8.37.

**Consequence.** A permanent exemption is created without anyone ever granting one, and the record shows a series of reasonable short term decisions. The count of times a nonconformity has been accepted is the only thing that reveals it.

**P12-11.18 (MUST) Repeated acceptance exposed.** An implementation must expose every nonconformity accepted more than once with the count.

### 11.19 The nonconformity closed on an assurance that it was fixed

**Mechanism.** The owner reports the remediation complete and the nonconformity is closed.

**Evidence.** Clause P12-3.88. The report is self reported evidence about the very statement that failed.

**Consequence.** The population of closed nonconformities includes an unknown number that were never remediated, and the closure rate becomes the metric the remediation function is managed by.

**P12-11.19 (MUST NOT) No closure without a reassessment.** An implementation must not close a nonconformity other than on a finding from a reassessment.

### 11.20 The finding that outlived its object

**Mechanism.** A component is redeployed at a new version and the findings from the prior version continue to be cited.

**Evidence.** Clauses P12-3.69 and P12-3.70.

**Consequence.** Assurance attaches to a thing that no longer exists. The most recent change is the one least covered, and it is covered on paper by a statement about its predecessor.

**P12-11.20 (MUST) Statement superseded on object change.** An implementation must supersede a statement whose object version changed in a covered respect.

### 11.21 The interview recorded as a test

**Mechanism.** A practitioner describes what the system does, the description is recorded, and the record is cited as evidence of behaviour.

**Evidence.** Clause P12-6.18. Interview evidence is evidence about what an individual said.

**Consequence.** The assessment reports on the organisation's understanding of itself, which is worth knowing and is not what the finding claims.

**P12-11.21 (MUST NOT) No interview as sole evidence for a mechanism.** An implementation must not record a finding about a mechanism on interview evidence alone.

### 11.22 Absence of evidence reported as evidence of absence

**Mechanism.** The assessor looked for a behaviour, did not find it, and recorded that the behaviour does not occur.

**Evidence.** Clause P12-6.27. Whether the method could have found the behaviour is a separate question from whether it did.

**Consequence.** A negative claim is established by a method incapable of establishing it, and the claims most likely to be assessed this way are the ones about behaviour that occurs rarely, which is where it matters.

**P12-11.22 (MUST) Absence distinguished from not found.** An implementation must record a failure to find evidence as not assessed unless the method was capable of establishing absence.

### 11.23 The assessment nobody could repeat

**Mechanism.** A finding is recorded with a narrative justification and without the evidence, the plan or the coverage, so that no one can determine what was done.

**Evidence.** Clauses P12-3.58 and P12-6.7.

**Consequence.** The finding cannot be disputed, reviewed or superseded on evidence, so it becomes permanent by being unexaminable. This applies equally to favourable and unfavourable findings.

**P12-11.23 (MUST) Finding re-performable from its record.** An implementation must record enough for a finding to be re-performed and must report a finding it cannot re-perform as `indeterminate_not_reproducible`.

### 11.24 The trust base that grew

**Mechanism.** Each time something proves hard to assess, it is moved into the assumptions, and the assumptions are never revisited.

**Evidence.** Clauses P12-3.19 and P12-8.43.

**Consequence.** The assessment shrinks while its output looks constant. The coverage figures are unchanged because the denominator moved, and the growth is visible only in the rate at which trust base items are added.

**P12-11.24 (MUST) Trust base reviewed on a cadence.** An implementation must review the trust base at a declared cadence and record each review.

## 12. Boundaries with other parts

Every subsection states what this component delegates, what it must not absorb, the naive conflation, and the reciprocal this part requires of the other. Subsection numbers correspond to part numbers; there is no 12.12 because this is Part 12.

### 12.1 Boundary with Part 1, controlled documents and records

**Delegated.** The identity, version, approval and retention of every part of this standard as a document, and the point in time resolution of a citation to a clause.

**Must not absorb.** The clause text. This component holds a content address and a version reference and never a copy it maintains.

**Naive conflation.** The harness transcribes the clauses into its own store so that it can index them, and the transcription drifts from the part, so assessments are made against a text nobody approved.

**Reciprocal.** `Part 1` must declare that it owns the identity and version of every part, that it resolves a citation to a clause to the text in force at the cited instant rather than the current text, that this component's findings, evidence items and assurance statements are records in its sense and not revisable, and that it retains a part version for as long as any finding cites it.

**P12-12.1 (MUST) Clause text resolved, not held.** An implementation must resolve clause text through `Part 1` and must hold only a version reference and a content address.

**P12-12.2 (MUST) Point in time resolution required.** An implementation must resolve every criterion citation to the clause text in force at the instant the finding was made.

**P12-12.3 (MUST) Records treated as records.** An implementation must treat its findings, evidence items, plans and issued statements as records in the `Part 1` sense and must not revise one.

**P12-12.4 (MUST) Retention obligation notified.** An implementation must notify `Part 1` of the retention obligation its findings create over the part versions they cite.

### 12.2 Boundary with Part 2, business rules and constraint evaluation

**Delegated.** The evaluation of any determination statement expressible as a declarative rule over stated facts.

**Must not absorb.** Rule evaluation. A determination statement that can be evaluated mechanically is a rule, and the harness's job is to derive it, obtain the verdict and record the finding.

**Naive conflation.** The harness implements its own expression evaluator for determination statements, acquiring a second rule engine with no verdict vocabulary and no non result, so an unevaluable statement becomes a failed one.

**Reciprocal.** `Part 2` must declare that it owns rule identity, evaluation and verdicts, that it accepts a determination statement as a rule for evaluation, and that it returns its full verdict vocabulary including non verdicts.

**P12-12.5 (MUST) Declarative statements evaluated by Part 2.** An implementation must obtain the verdict for any determination statement expressible as a declarative rule from `Part 2` and must not evaluate it itself.

**P12-12.6 (MUST NOT) No non verdict recorded as a finding.** An implementation must not convert a `Part 2` non verdict into a finding of satisfied or not satisfied, and must record the outcome that names the indeterminacy.

### 12.3 Boundary with Part 3, provenance and audit ledger

**Delegated.** The evidentiary chain in which this component's findings participate, and the reconstruction of determinations spanning components.

**Must not absorb.** The chain. This component's findings are evidence about components; they are not the provenance of anything those components determined.

**Naive conflation.** The harness's records are treated as the audit trail of the system, so an auditor finds assessments of components and nothing about what the components decided.

**Reciprocal.** `Part 3` must declare that it owns the evidentiary chain, that a finding of this component is one input to it and not the chain itself, that it accepts this component's events, and that it does not assess conformance.

**P12-12.7 (MUST) Events emitted to the ledger.** An implementation must emit every event of section 4.7 to `Part 3`.

**P12-12.8 (MUST NOT) No chain asserted.** An implementation must not represent its findings as the provenance of any determination another component made.

**P12-12.9 (MUST) Ledger assessed like any other component.** An implementation must assess `Part 3` against its own clauses on the same terms as every other part and must not exempt the component it emits to.

Clause P12-12.9 names a circularity worth stating. This component emits its records to the ledger and also assesses the ledger. Neither can be avoided, and the mitigation is that the assessment of the ledger must not rest on evidence the ledger supplied, which clause P12-3.45 already requires.

### 12.4 Boundary with Part 4, metadata and model repository

**Delegated.** The governed definitions of terms this standard uses, and the lineage and impact analysis of a change to one.

**Must not absorb.** Definitions. Where a criterion turns on a defined term, the definition is resolved and not interpreted here.

**Naive conflation.** The harness records its reading of a term as the term's meaning, so a determination statement encodes an interpretation that the standard never made and that nobody can dispute.

**Reciprocal.** `Part 4` must declare that it owns governed definitions and their lineage, and that it exposes the set of criteria and determination statements citing each definition so that a definition change surfaces the assessments it affects.

**P12-12.10 (MUST) Definitions resolved, not interpreted.** An implementation must resolve a defined term from `Part 4` where a criterion turns on one and must record any interpretation as its own.

**P12-12.11 (MUST) Definition change triggers a reclassification review.** An implementation must review every determination statement citing a definition that changed.

### 12.5 Boundary with Part 5, decision engine

**Delegated.** Any governed selection among alternatives that is a business outcome, including the selection of a remediation priority or a risk rating.

**Must not absorb.** Business selection, risk rating and prioritisation.

**Naive conflation.** The harness computes a risk score from its findings, because a finding without a priority is hard to act on, so the assessor becomes the party deciding what matters.

**Reciprocal.** `Part 5` must declare that it owns business outcome selection, that it obtains findings from this component as inputs rather than computing them, and that it does not assess conformance.

**P12-12.12 (MUST NOT) No risk or priority computed.** An implementation must not compute a risk rating, materiality judgement or remediation priority from a finding.

**P12-12.13 (MUST) Findings supplied as inputs.** An implementation must supply findings with their full qualifications to `Part 5` where a decision consumes them, and must not supply an outcome value alone.

### 12.6 Boundary with Part 6, workflow and process orchestration

**Delegated.** The sequencing of an assessment programme where that sequencing is a defined process.

**Must not absorb.** Control flow. A run state is a fact about an assessment and not a process instance's position.

**Naive conflation.** The assessment lifecycle is implemented as a workflow, so a finding cannot be read without the process engine and a stalled process suppresses a nonconformity.

**Reciprocal.** `Part 6` must declare that it owns control flow, that a run state and a finding are facts held here, and that it does not gate the visibility of a finding.

**P12-12.14 (MUST) Run state is a fact.** An implementation must hold every state of section 5 as its own fact and must not derive it from a process instance's position.

**P12-12.15 (MUST NOT) No finding gated by a process.** An implementation must not make the visibility of a finding or a nonconformity conditional on the state of any process instance.

### 12.7 Boundary with Part 7, policy decision point and authorisation

**Delegated.** Every decision on whether a party may declare a plan, introduce a probe, issue a statement, accept a nonconformity, or read a finding.

**Must not absorb.** Authorisation, and in particular the temptation to decide who may see an unfavourable finding.

**Reciprocal, and its discharge.** `Part 7` section 12.12 requires this part to declare four things. That it obtains the clause set from that part by resolution: clauses P12-3.22 and P12-12.1. That it records the version of that part an assessment was made against: clauses P12-3.2 and P12-3.24. That it does not write there while assessing: clauses P12-4.7 and P12-6.38, which forbid elicitation absent a permission that part does not give, with the resulting coverage gap declared under clause P12-6.39. And that it examines the declared request space and the enforcement point capability declarations independently rather than accepting the figures computed from them: clauses P12-3.51 and P12-6.31. That part's clause P7-12.32 further requires that everything it exposes be assessable by reads alone, which section 10.7 records as a conflict with `Part 11`'s requirement and resolves per part.

**P12-12.16 (MUST) Authorisation obtained per operation.** An implementation must obtain an authorisation decision at the instant of every operation section 4.1 requires one for and must record the reference.

**P12-12.17 (MUST NOT) No authorisation decision rendered.** An implementation must not decide who may read a finding.

**P12-12.18 (MUST) Read only assessment where the part requires it.** An implementation must assess a part that requires read only assessment without writing to it, and must declare every criterion of that part it could not assess in consequence.

**P12-12.19 (MUST) Declared spaces examined, not accepted.** An implementation must independently examine every population, request space or capability declaration an assessed component makes and must not accept a figure computed from one as evidence of the figure's soundness.

### 12.8 Boundary with Part 8, human task and case management

**Delegated.** The work by which a nonconformity is remediated, a finding is disputed, an interview is conducted and an acceptance is reviewed: the queue, the assignment and the case.

**Must not absorb.** Task management, and remediation.

**Reciprocal, and its discharge.** `Part 8` clauses P8-12-31 and P8-12-32 require that component to expose the state needed to verify every externally observable clause of its part and not to report its own conformance as assurance. This part discharges the corresponding obligation by assessing that part's clauses on the same terms as every other and by clause P12-12.20, which requires the remediation work to be obtained rather than performed. `Part 8` must further declare that completing a work item does not close a nonconformity, which clause P12-3.88 requires from this side.

**P12-12.20 (MUST) Remediation work obtained, not performed.** An implementation must obtain the work by which a nonconformity is remediated from `Part 8` and must not perform it.

**P12-12.21 (MUST NOT) No closure from task completion.** An implementation must not treat the completion of a `Part 8` work item as closing a nonconformity.

**P12-12.22 (MUST) Interview conducted as work, recorded as evidence.** An implementation must obtain any interview as work from `Part 8` and must record its output as evidence of provenance self reported.

### 12.9 Boundary with Part 9, schema and contract registry

**Delegated.** Schema identity, versioning, compatibility and validation, including of this component's own record payloads.

**Must not absorb.** Validation and schema versioning.

**Reciprocal, and its discharge.** `Part 9` clauses P9-12-34 and P9-12-35 require that component to expose the state needed to verify every externally observable clause and not to report its own conformance as assurance, and its section 12.10 identifies its evaluated extent computation as the claim most needing independent verification. This part discharges that by treating the evaluated extent as a claim requiring elicitation: instances of known coverage are submitted and the reported extent is compared with the extent independently computed, per clause P12-3.45.

**P12-12.23 (MUST NOT) No validation performed.** An implementation must not validate a payload against a schema and must obtain the validation from `Part 9`.

**P12-12.24 (MUST) Evaluated extent assessed by elicitation.** An implementation must assess a claim about a validation's evaluated extent by submitting instances of known coverage and comparing the reported extent with the extent it computed independently.

**P12-12.25 (MUST NOT) No acceptance of a reported coverage figure.** An implementation must not record a satisfied finding about an evaluated extent whose only evidence is the registry's own report of it.

### 12.10 Boundary with Part 10, reference and master data management

**Delegated.** Party identity for assessors, owners and interviewees, and every code system and value set this component references.

**Must not absorb.** Reference content.

**Reciprocal, and its discharge.** `Part 10` section 12.12 requires this part to declare that it verifies that component's claims, that it may obtain a consumption report by independent observation or attestation rather than from the consumer, and that it treats an unreported population figure as a claim requiring sampling rather than as a fact. Section 6.6 discharges all three, and adds the limit: clauses P12-6.30 and P12-6.31 require attestation by an independent channel and comparison against the component's figure; clause P12-6.32 forbids accepting the figure as a finding; and clause P12-6.29 refuses to sample where the consumer population is not enumerable, which is the honest extent of the discharge and is recorded in section 13.4.

**P12-12.26 (MUST) Attestation obtained independently of the reporting component.** An implementation must obtain a consumption report by observation or by attestation from the consumer through a channel `Part 10` does not control, and must record where it could not.

**P12-12.27 (MUST) Unreported population treated as a claim.** An implementation must treat an unreported population figure as a claim requiring sampling and must not record it as a fact.

**P12-12.28 (MUST) Party identities obtained.** An implementation must obtain assessor, owner and interviewee identities from `Part 10` and must pin the snapshot used.

### 12.11 Boundary with Part 11, content addressed artifact store

**Delegated.** The custody of the octets of every evidence item, clause text and evidence package.

**Must not absorb.** The octets.

**Reciprocal, and its discharge.** `Part 11` section 12.12 requires this part to declare that it verifies that component's claims, that it may perform an independent verification by retrieving content and recomputing its address without relying on the store's own verification, that it may plant known content to test the outcome taxonomy, and that it treats a durability or independence claim as a claim requiring evidence. Clause P12-3.45 discharges the independent recomputation, section 3.12 and section 6.7 discharge the planting under a permission regime that part supplies at its clause P11-12.35, clause P12-12.31 discharges the elicitation of the sixteen outcomes required by its clause P11-12.36, and clauses P12-6.30 and P12-6.32 discharge the treatment of a durability claim.

**P12-12.29 (MUST NOT) No evidence octets held.** An implementation must not store the octets of an evidence item, clause text or package, and must hold the content address.

**P12-12.30 (MUST) Address recomputed independently.** An implementation must recompute the address of any content it retrieves for assessment purposes without relying on the store's verification result.

**P12-12.31 (MUST) Outcome taxonomy elicited.** An implementation must elicit each outcome of an assessed part's outcome taxonomy under controlled conditions where that part requires it, and must record every outcome it could not elicit as an unassessed determination statement.

**P12-12.32 (MUST) Durability and independence treated as claims.** An implementation must treat a durability figure and a replica independence claim as claims requiring evidence and must not record either as a fact on the store's report.

### 12.13 Boundary with Part 13, model invocation and agent execution

**Delegated.** The invocation record of any model used in the course of an assessment, and the properties of any model an assessed component invokes.

**Must not absorb.** Any assessment conclusion produced by a model without a recorded human decision.

**Naive conflation.** A model reads records and produces findings, and the findings are recorded as the harness's own, so the determination, the review and the decision are one act performed by a mechanism whose non determinism is unrecorded.

**Reciprocal.** `Part 13` must declare that it owns the invocation record and its non determinism, that a produced value is not a checked value, and that it does not issue assurance statements.

**P12-12.33 (MUST) Model produced determination recorded as evidence, not as a finding.** An implementation must record a determination produced by a model invocation as an evidence item with its invocation reference and must not record it as a finding.

**P12-12.34 (MUST) Human decision required for a finding.** An implementation must require a recorded decision by an accountable party for every finding and must not attribute a finding to a model.

**P12-12.35 (MUST) Non determinism recorded.** An implementation must record the non determinism of any model invocation an assessment relied upon, and must treat a determination that does not reproduce as `indeterminate_not_reproducible`.

**P12-12.36 (MUST) Model use in an assessment declared.** An implementation must declare, on every assurance statement, whether a model invocation contributed to any finding it rests on.

### 12.14 Boundary with Part 0, system composition

**Delegated.** What happens when the components run at once: authority over facts more than one component touches, the seams at which values cross boundaries, and the pinning of versions across a unit of work.

**Must not absorb.** Composition. This part assesses components against clauses and does not assess the composition, which is `Part 0`'s subject and which section 13.9 hands to it as a question rather than an answer.

**Reciprocal.** `Part 0` must declare that this component holds authority over criteria registrations, assessability classifications, plans, evidence, findings, assurance statements, nonconformities, probes, frames, the trust base and assessor registrations, and over nothing else. It must state, for every seam, what must hold and how a violation appears here. It must in particular resolve the eight questions section 13.9 hands it, of which the first is the one three other parts also handed it.

**P12-12.37 (MUST) Authority declared, not assumed.** An implementation must not accept an assertion about a finding, an assurance statement, an assessability classification or a trust base item from another component, and must require every such fact to be established by its own operations.

**P12-12.38 (MUST) Composition clauses assessed as clauses.** An implementation must register and assess the clauses of `Part 0` on the same terms as those of every other part, and must record where a composition clause is classified `not_assessable`.

**P12-12.39 (MUST) Cross part conflicts reported to composition.** An implementation must report every case in which two parts impose conflicting requirements on it to `Part 0` and must record the resolution it applied in the interim.

**P12-12.40 (MUST) Assessment gap exposed to composition.** An implementation must make the unassessable criterion population, the elicitation forbidden population and the self report reliance proportion available as signals, since none can be remedied within this component.

## 13. What could not be established

### 13.1 Sources not obtained in full text

**ISO/IEC 17000.** Obtained in relevant part. The definitions of attestation, declaration, certification, accreditation, scope of attestation and peer assessment, and the description of third party as independent of the provider and of user interests, were read in the standard's own words or in an authoritative quotation of them, as was the enumeration of the functional approach. The 2020 edition's scope statement and the list of terms new in that edition were obtained; several definition texts were read from the 2004 first edition and may have been revised. A reviewer should confirm the 2020 wording of attestation and of the party classes before approval.

**ISO/IEC 17007.** Not obtained. The principle that a normative document should be drafted so that fulfilment can be determined, and the first, second and third party worked examples, were read from a catalogue summary and a quoted extract. This is the standard most directly on the subject of section 3.6 and its absence is the most significant gap in this part's source base.

**NIST SP 800-53A.** Obtained in relevant part. The methods, object kinds, depth and coverage attributes with their three values, and the determination statement construction were read in quotations of the publication's text. The revision current at the date of this part was not established: revision 1 was withdrawn in 2015 and superseded, and this part did not determine which revision is current or whether the depth and coverage attributes survive unchanged in it. No clause depends on a revision.

**The security evaluation criteria and methodology.** Not obtained. The principle that an assurance level grades the evaluation rather than the object is cited from general knowledge and is the strongest precedent for section 3.2, so a reviewer should verify it.

**The software verification and validation standards.** Not obtained. The separation of technical, managerial and financial independence is cited from general knowledge and clause P12-3.80 rests on it.

**The service organisation assurance standards.** Not obtained. The point in time against period distinction and the carve out construction are cited from general knowledge and inform section 3.11 and section 11.9.

**Metrological traceability and uncertainty.** Not obtained. The analogy in section 3.4, that a traceability chain terminates at a primary standard maintained outside the measuring system and states an uncertainty, is offered as an analogy and no clause depends on it.

**Prior parts of this standard.** `Part 7`, `Part 8`, `Part 9`, `Part 10` and `Part 11` were available and their reciprocals are discharged at sections 12.7, 12.8, 12.9, 12.10 and 12.11 with the discharging clauses named. `Part 1` through `Part 6` were not available, and sections 12.1 through 12.6 are written from this part's own analysis.

**P12-13.1 (MUST) Unverified reciprocals declared.** An implementation must not represent sections 12.1 through 12.6 as discharging a reciprocal statement of `Part 1` through `Part 6`, since the text of those parts was not read.

### 13.2 Whether not falsified is usable

This is the position most likely to be overturned and the one this part would least like to lose.

The parties who need assurance need to make a decision, and a decision needs a proposition. A board asked whether the estate conforms cannot act on the statement that four hundred and thirty determination statements were not falsified at focused depth over a coverage of sixty per cent of an enumerable frame with eleven per cent of findings resting on self report. It will ask for a summary, and clause P12-3.97 forbids one, and someone will produce one anyway outside the harness where none of the qualifications travel.

Two mitigations are available and neither is adopted. A structured summary whose form is fixed by this part, so that the qualifications travel with the headline, which risks becoming the grade clause P12-1.29 refuses. Or a declared decision rule, owned by the consumer of the assurance, mapping the qualified outcome onto that consumer's own threshold, which puts the judgement where the consequence sits and requires a mechanism this part does not specify. The second is probably right and section 13.9 hands the question forward, because the rule belongs to the party bearing the risk rather than to the party assessing.

### 13.3 The cost of the model

One evidence item per determination statement per object, with provenance and a content address, is the largest volume commitment in this part. For twelve parts carrying some five thousand clauses, with determination statements at better than one per clause and objects numbering in the tens, the evidence population is in the millions before any surveillance iteration.

The plan declaration requirement compounds it. Clause P12-3.36 requires a plan before evidence and clause P12-3.42 forbids amendment, so an assessment programme that learns as it goes must issue a new plan each time, and each supersession carries the evidence attribution. Nothing here is costed, no sampling of criteria is specified, and clause P12-6.60 admits an effort bound without saying how a bound should be chosen. A reviewer should expect the practical response to be an assessment that covers a small fraction of the clauses, which is legitimate under this part provided the coverage is declared, and should treat clause P12-8.31, the never assessed criterion population, as the figure that will reveal how small.

### 13.4 What was and was not discharged of the three handed forward problems

`Part 7`, `Part 10` and `Part 11` each concluded that a population it could not enumerate was the limit of its own assurance, and each named this component. Section 6.6 is the discharge and it is partial in a way worth stating precisely.

What is discharged: where a population can be enumerated, this part supplies a sound method. A probability sample is drawn from a declared frame, the frame declaration is examined independently rather than accepted, an attestation is obtained for each sampled member through a channel the assessed component does not control, the assessed component's own figure is compared against those attestations, and the non response rate is published. That is materially stronger than any of the three components could achieve alone, and it converts the reported figure from a fact into a claim with evidence against it.

What is not discharged: the three populations are hard because they are not enumerable, and section 6.6 refuses to sample a frame it cannot enumerate rather than approximating. An enforcement point that never contacts the decision point, a consumer that fetched once and cached, and a component holding an address in a record nobody registered are invisible by construction, and no method available to this component makes them visible. The residual is therefore recorded as unassessed with the component's own figure marked unverified, which is honest and is not a solution.

What would discharge it: a composition level obligation that every component be registered and every pin declared, which makes the frame enumerable by construction and lets this component sample the register. That is `Part 0`'s and is the first question of section 13.9. Four parts have now arrived at the same place, and the fourth arrival is this one, which is the component the other three nominated. A reviewer should read that as evidence that the problem is structural rather than as evidence that four authors were insufficiently ingenious.

### 13.5 Whether a harness can be independent inside one organisation

Clause P12-3.80 requires technical, managerial and financial independence to be declared separately, and clause P12-3.81 forbids describing an assessment as independent where any form is absent. In a single organisation operating a single estate, financial independence is absent by construction: the harness is funded by the same budget as the components it assesses, and often by the same owner.

The honest consequence is that a harness of this kind can issue second party attestations and not third party ones, and clause P12-6.50 enforces that by deriving the party class from the independence. What this part does not resolve is whether that is sufficient for the purposes an estate puts assurance to, or whether the conclusion is that some assessments must be procured externally. The conformity assessment standards answer it for their own domain by requiring accreditation of the body, which is a third party attestation about the assessor, and no mechanism in this standard produces one.

### 13.6 Gaming, and why the mitigation is not a solution

Clause P12-6.43 publishes the class of probes and withholds the instances, and clause P12-6.42 requires the instances to be unpredictable. Both are mitigations of a problem this part does not solve.

A published method class is a specification of the property that will be measured, and a component optimised against it will satisfy the class without necessarily holding the property. Unpredictable instances raise the cost of doing so and do not remove the possibility, because the class itself tells a component which of its behaviours are examined. The only construction that removes it is an assessment method the assessed party does not know exists, which is incompatible with clause P12-3.36's requirement that plans be declared and with any account of assessment that a reviewer could audit.

This part therefore accepts a known weakness in exchange for auditability, and states the trade rather than concealing it. A reviewer who prefers the other side of the trade should note that an undeclared method cannot be reviewed, and that an assessment nobody can review is the failure section 11.23 names.

### 13.7 Repeated structure across the standard, now twelve parts

`Part 4` recorded three repeated structures, `Part 5` five, `Part 6` six, `Part 7` eight with one divergence, `Part 10` eleven with two, `Part 11` twelve. This part carries the register forward, adds one, and resolves nothing, which is itself now the finding.

**The authority that can prove what it did and not what happened.** Four components. `Part 7` cannot see enforcement, `Part 10` cannot see consumption, `Part 11` cannot see citation, and this component cannot see whether what it sampled was representative or whether the behaviour it elicited is the behaviour that occurs unobserved. The first three nominated this one as the remedy; this one has now discharged the enumerable case and refused the rest, and handed the structural fix to `Part 0`. **Four independent arrivals and a nomination that could only be partly honoured. This is no longer a candidate for being specified once; it is a demonstration that it must be, and the specification has to be at composition level because every component level attempt has now been made.**

**The retention obligation a component cannot discover.** Third appearance. `Part 7` imposed it on `Part 10`, six parts imposed it on `Part 11`, and this part's clause P12-8.52 imposes it on `Part 10` and `Part 11` in turn while clause P12-12.4 imposes it on `Part 1`. Three implementations, three vocabularies, one device.

**The refusal to return a wrong value for a non result.** Fourth instance, and the first in the positive direction. `Part 7` refuses not applicable as deny, `Part 10` refuses unknown as non membership, `Part 11` refuses integrity failure as absence, and this part refuses not assessed as satisfied. The first three protect against a false negative and this one against a false positive, and it is the same principle.

**The declared completeness of a set.** Now ten parts, and in this part it is the primary claim rather than a qualifier: an assurance statement is a statement about a coverage and nothing else.

**The honest undeclared or unreported value.** Now twelve parts. This part contributes `satisfied_self_reported_only`, the four `not_assessable` values, `not_attempted` and `indeterminate_not_reproducible`.

**The immutable record with stateful assertions about it.** Now twelve parts. Here the immutable finding carries an assurance statement whose state decays.

**The refusal to arbitrate.** Now seven. This part refuses to resolve a divergence between two assessors and records it as a defect of the determination statement.

**The refusal of order dependent resolution.** Unchanged at seven parts.

**The residue model.** Still two, `Part 6` and `Part 7`.

**The extended third value.** Still an inconsistency between `Part 5` and `Part 7`, still unresolved, and this part does not adopt an extended form.

**The asymmetric bridge that disproves and cannot prove.** Resolved in principle, here. Two parts had one, four recorded that they should and did not, and `Part 11` made five. This part is the bridge: section 3.2 makes the asymmetry the governing principle of the whole component, section 3.12 supplies the device as the probe, and clause P12-3.9 makes a single counterexample decisive. What remains unresolved is whether the five parts that wanted one should each build their own or delegate to this one, and section 13.9 hands that forward.

**The marking vocabulary for restricted content.** Now six parts and unchanged.

**The divergence in clause convention.** `Part 8` and `Part 9` remain outside the convention the other ten parts share. Neither exposes a section 12.12, so this part derived both boundaries from their content, as `Part 10` and `Part 11` did before it. **Third consecutive part affected.** It is also now an assessment problem rather than only a drafting one: clause P12-6.11 requires a declared extraction method applied uniformly, and two parts require a different extraction, so a harness conforming to this part must register two methods and declare which applies to which part.

**Open.** All of it. This is the seventh consecutive part to record the register and the sixth to recommend acting before the next part. Thirteen items across twelve parts, two of them inconsistencies. One item is now demonstrated rather than merely repeated, and one is resolved in principle by this part and not in allocation.

**P12-13.2 (SHOULD) Register maintained.** An author of a subsequent part should carry this register forward, add to it, and state whether each entry is a repetition, an inconsistency or a demonstration.

### 13.8 What this part deliberately did not attempt

No conformance assessment of any system was performed or anticipated, per clause P12-1.27.

No certification scheme, accreditation scheme, mark, badge or grade is defined, per clauses P12-1.21, P12-1.22 and P12-1.29.

No assessor competence framework is specified. Clause P12-3.82 requires the basis of competence to be recorded and says nothing about what competence consists of.

No sampling mathematics is specified. Clause P12-3.54 requires the scheme and the intended confidence to be declared and specifies neither an estimator nor a sample size calculation.

No probe construction is specified for any part. Section 3.12 requires an expected outcome, indistinguishability and bounded side effects, and supplies no probes.

No assessability classification of any actual clause of any actual part is performed. Section 3.6 supplies the classes and the obligation to classify; the classification of the standard's own five thousand clauses is an exercise this part requires and does not carry out.

No treatment is given of assessment across an organisational boundary, where the assessor and the assessed are operated by different parties and the assessed party controls the evidence.

No performance or scale requirement is stated, and section 13.3 records the volume concern without a threshold.

**P12-13.3 (MUST) Gaps declared, not filled.** An implementation must not represent a matter listed in section 13.8 as specified by this part.

**P12-13.4 (SHOULD) Open questions carried forward.** A reviewer of this part should record a position on each open question in section 13, and where a position is adopted it should be recorded in the review outcome rather than by silent amendment of the clause it affects.

### 13.9 Questions handed to Part 0 rather than answered here

Whether every component must be registered and every pin declared at composition level, so that the frames of section 6.6 become enumerable. Four parts have now reached this question from four directions and it is the only one of the thirteen register items that is demonstrated rather than repeated. It is the first question `Part 0` should answer.

Whether the asymmetric bridge should be built once, here, or five times in the parts that each recorded wanting one. This part supplies the device and does not claim the allocation.

Who consumes a not falsified statement and by what declared rule, per section 13.2. The rule belongs to the party bearing the risk and this part specifies no mechanism for it.

Whether a harness funded by the owner of the objects it assesses can issue anything but a second party attestation, per section 13.5, and if not, which assessments of this estate must be procured externally.

Whether the conflict between `Part 7`'s read only requirement and `Part 11`'s elicitation requirement should be resolved at composition level, or whether the per part resolution of section 10.7 is the right answer permanently. The coverage gap it leaves in `Part 7`'s elicitation dependent clauses is now declared and is not closed.

Whether the retention obligation a component cannot discover should be a composition level device, which is the third part to ask and the second to ask it of the same structure.

Whether this component's own external assessment is a composition obligation, since clause P12-6.67 requires the absence to be recorded as a nonconformity and nothing in this standard requires anyone to remedy it.

Whether the thirteen repeated structures should each be specified once, and in particular whether the divergence in clause convention between `Part 8`, `Part 9` and the other ten parts should be remedied before `Part 13` is authored, since it has now cost three consecutive parts and has become an assessment problem as well as a drafting one.
