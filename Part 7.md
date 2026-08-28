# KAIROS STD 003 Part 7: Policy Decision Point and Authorisation

**Standard.** KAIROS STD 003, the enterprise architecture standard.
**Part.** Part 7 of 14 (Part 0 and Parts 1 through 13). Cited as `KAIROS STD 003 Part 7`.
**Title.** Policy decision point and authorisation.
**Version.** 1.0.0.
**Status.** Proposed. This part has not been approved and is not effective. It is issued for review against the authoring brief of 2026-08-17.
**Date of issue.** 2026-08-18.
**Supersedes.** Nothing. This is the first version.

## Binding of requirement language

The key words MUST, MUST NOT, SHOULD, SHOULD NOT and MAY in this part are to be interpreted as described in RFC 2119 and RFC 8174, and only in the upper case forms. This part does not use SHALL, SHALL NOT, REQUIRED, RECOMMENDED, NOT RECOMMENDED or OPTIONAL as requirement keywords.

Every requirement in this part is a numbered clause. A clause identifier has the form `P7-S.N`, where `S` is the section number and `N` is the ordinal of the clause within that section. Clause identifiers are permanent. A clause that is later removed has its identifier retired and never reissued. A clause that is later added to a section takes the next unused ordinal in that section, so ordinals are stable but not contiguous over the life of the part.

Text that is not a numbered clause is not binding. Narrative, tables, algorithms, examples and the discussion of standards are provided to make the clauses intelligible and testable, and where a table carries normative content a clause says so explicitly and names the table.

## Conformance

An implementation conforms to this part if it satisfies every MUST and MUST NOT clause and records, for each SHOULD and SHOULD NOT clause it does not satisfy, the reason. This part does not define conformance levels, profiles or a certification scheme, and it does not define the method of assessment. Assessment method is the subject of `KAIROS STD 003 Part 12` and is out of scope here.

Where a clause states that a value is an implementation decision, conformance requires that the implementation declare the value, not that it adopt a particular one. An undeclared implementation decision is a nonconformity.

## Clause index

The index below is generated from the clause text of this document. It lists every clause identifier, its modality and its subject label. The counts that follow the index are derived by the same extraction and are stated with the grain at which they were counted.

| Clause | Modality | Subject |
| --- | --- | --- |
| **Section 1** | | **Scope and responsibilities** |
| `P7-1.1` | MUST | Purpose satisfaction |
| `P7-1.2` | MUST | Decision and enforcement recorded separately |
| `P7-1.3` | MUST | Unreported enforcement countable |
| `P7-1.4` | MUST NOT | No enforcement |
| `P7-1.5` | MUST NOT | No business rule evaluation |
| `P7-1.6` | MUST NOT | No business selection |
| `P7-1.7` | MUST NOT | No authentication |
| `P7-1.8` | MUST | Four decision values at minimum |
| `P7-1.9` | MUST NOT | No default deny in the decision |
| `P7-1.10` | MUST | Obligations distinguished from advice |
| `P7-1.11` | MUST | Withholding marked, never silent |
| `P7-1.12` | MUST | Reproducibility |
| `P7-1.13` | MUST | Every attribute pinned |
| `P7-1.14` | MUST NOT | No update in place |
| `P7-1.15` | MUST NOT | No absorption of neighbouring responsibilities |
| `P7-1.16` | SHOULD | Declared exclusions |
| `P7-1.17` | MUST NOT | No conformance self assertion |
| `P7-1.18` | MUST | Time horizon declaration |
| **Section 2** | | **Terminology** |
| `P7-2.1` | MUST | Single meaning per term |
| `P7-2.2` | MUST NOT | No redefinition |
| `P7-2.3` | MUST NOT | No collapsing of decision and enforcement |
| `P7-2.4` | MUST NOT | No collapsing of obligation and advice |
| `P7-2.5` | MUST NOT | No collapsing of not applicable and deny |
| `P7-2.6` | MUST NOT | No collapsing of the three indeterminate values |
| `P7-2.7` | MUST NOT | No collapsing of a scope and a decision |
| `P7-2.8` | MUST NOT | No collapsing of the three clocks |
| `P7-2.9` | SHOULD | Term registry |
| **Section 3** | | **Data model** |
| `P7-3.1` | MUST | Declared types |
| `P7-3.2` | MUST NOT | No semantic identifiers |
| `P7-3.3` | MUST | Language tag present |
| `P7-3.4` | MUST NOT | No caller supplied knowledge time |
| `P7-3.5` | MUST | Authentication reference recorded, not verified |
| `P7-3.6` | MUST | Three valued condition domain used unchanged |
| `P7-3.7` | MUST | Two records, never merged |
| `P7-3.8` | MUST | Report receivable |
| `P7-3.9` | MUST | Unreported population counted |
| `P7-3.10` | MUST NOT | No inference of enforcement |
| `P7-3.11` | MUST NOT | No absence of report as a fault |
| `P7-3.12` | MUST | Enforcement point identified |
| `P7-3.13` | MUST | Entity coverage |
| `P7-3.14` | MUST NOT | No update in place |
| `P7-3.15` | MUST NOT | No decision amendment |
| `P7-3.16` | MUST | Policy carried by a document |
| `P7-3.17` | MUST | Statement present and authoritative language designated |
| `P7-3.18` | MUST | Combining algorithm on every element |
| `P7-3.19` | MUST | Authority per policy version |
| `P7-3.20` | MUST | Membership by pinned version only |
| `P7-3.21` | MUST NOT | No cyclic membership |
| `P7-3.22` | MUST | Approval obtained, not asserted |
| `P7-3.23` | MUST NOT | No policy amendment |
| `P7-3.24` | MUST | Authority drift observed |
| `P7-3.25` | MUST | Target on every element |
| `P7-3.26` | MUST | Effect from a closed pair |
| `P7-3.27` | MUST NOT | No effect from rule ordinal |
| `P7-3.28` | MUST | Conditions read attributes only |
| `P7-3.29` | MUST NOT | No duplicated business rule |
| `P7-3.30` | MUST | Conditions bounded |
| `P7-3.31` | MUST | Conditions pure |
| `P7-3.32` | MUST | Condition result recorded three valued |
| `P7-3.33` | MUST | Every attribute pinned |
| `P7-3.34` | MUST | Maximum staleness declared per attribute |
| `P7-3.35` | MUST | Stale attribute refuses the decision |
| `P7-3.36` | MUST | Absence declared, not assumed |
| `P7-3.37` | MUST | Absence yields indeterminate by default |
| `P7-3.38` | MUST | Declared default authorised |
| `P7-3.39` | MUST | Default reliance recorded on the decision |
| `P7-3.40` | MUST | Source reference recorded |
| `P7-3.41` | MUST | Concept binding reportable |
| `P7-3.42` | MUST | Attributes registered as dependencies |
| `P7-3.43` | MUST NOT | No attribute derivation |
| `P7-3.44` | MUST | Principal and authentication reference required |
| `P7-3.45` | MUST | Decision instant supplied |
| `P7-3.46` | MUST | Operation from a registered vocabulary |
| `P7-3.47` | MUST | Purpose recorded |
| `P7-3.48` | MUST | Enforcement point identified and registered |
| `P7-3.49` | MUST NOT | No clock read for the decision instant |
| `P7-3.50` | MUST | Closed algorithm set |
| `P7-3.51` | MUST NOT | No first applicable |
| `P7-3.52` | MUST | Ordered variants order obligations only |
| `P7-3.53` | MUST | Only one applicable returns indeterminate on multiplicity |
| `P7-3.54` | MUST | Collapsing algorithms fenced |
| `P7-3.55` | MUST | Algebraic properties declared |
| `P7-3.56` | MUST | Combination steps recorded |
| `P7-3.57` | MUST | Algorithm choice authorised where it embodies policy |
| `P7-3.58` | MUST | Obligations and advice held separately |
| `P7-3.59` | MUST | Obligation kind registered with an authority |
| `P7-3.60` | MUST | Fulfilment condition recorded |
| `P7-3.61` | MUST | Verifiability declared and counted |
| `P7-3.62` | MUST | Undischargeable obligation yields deny |
| `P7-3.63` | MUST | Capability mismatch detectable statically |
| `P7-3.64` | MUST | Parameters resolved from recorded attributes |
| `P7-3.65` | MUST | Advice ignorable in fact |
| `P7-3.66` | MUST NOT | No obligation without an authority |
| `P7-3.67` | MUST | Closed outcome set |
| `P7-3.68` | MUST | Not reported is the default |
| `P7-3.69` | MUST | Failed fulfilment leaves the position unknown |
| `P7-3.70` | MUST | Residue enumerated where required |
| `P7-3.71` | MUST | Unfulfilled obligation on a permit raises a review obligation |
| `P7-3.72` | MUST | Unfulfilled permits countable |
| `P7-3.73` | MUST | Residue assigned |
| `P7-3.74` | MUST | Unassigned residue countable |
| `P7-3.75` | MUST NOT | No outcome inference |
| `P7-3.76` | MUST | Obligation outcomes recorded with Part 3 |
| `P7-3.77` | MUST | Restriction expressed as an obligation |
| `P7-3.78` | MUST NOT | No silent removal |
| `P7-3.79` | MUST | Withheld distinguished from absent in the marking |
| `P7-3.80` | MUST | What was restricted recorded |
| `P7-3.81` | MUST | Reason and appeal path where declared |
| `P7-3.82` | MUST | Silent restriction reportable |
| `P7-3.83` | MUST NOT | No restriction outside an obligation |
| `P7-3.84` | MUST | Validity declared on every decision |
| `P7-3.85` | MUST | Validity declared per policy version |
| `P7-3.86` | MUST | Expired reliance reportable |
| `P7-3.87` | MUST | Revocation reach stated |
| `P7-3.88` | MUST | Exposure window computable |
| `P7-3.89` | MUST NOT | No indefinite validity |
| `P7-3.90` | MUST NOT | No revocation claim |
| `P7-3.91` | MUST | Delegation assessed under a policy version |
| `P7-3.92` | MUST | Chain obtained, not constructed |
| `P7-3.93` | MUST | Assessment recorded on the decision |
| `P7-3.94` | MUST | Unassessable delegation yields indeterminate |
| `P7-3.95` | MUST | Scope of delegation recorded |
| `P7-3.96` | MUST NOT | No delegation assessment held by another component |
| `P7-3.97` | MUST | Emergency access is a declared policy |
| `P7-3.98` | MUST | Three mandatory obligations |
| `P7-3.99` | MUST | Justification recorded, not assessed |
| `P7-3.100` | MUST | Capability required for emergency grant |
| `P7-3.101` | MUST | Undischarged reviews countable |
| `P7-3.102` | MUST | Emergency population reportable |
| `P7-3.103` | MUST NOT | No emergency access without a review obligation |
| `P7-3.104` | MUST | Outcome from the closed set with extended information |
| `P7-3.105` | MUST | Counts derived with grain |
| `P7-3.106` | MUST | Concealed outcome recorded |
| `P7-3.107` | MUST | Report distinguishes over and under application |
| `P7-3.108` | MUST | Under application countable |
| `P7-3.109` | MUST | Statuses carried with every decision |
| `P7-3.110` | MUST | Decision recorded as a determination |
| `P7-3.111` | MUST NOT | No report amendment |
| `P7-3.112` | MUST | Projections are pure |
| `P7-3.113` | MUST | Projection recomputable |
| `P7-3.114` | MUST | Named projections available |
| `P7-3.115` | MUST | Not applicable population available |
| `P7-3.116` | MUST | Explanation available for every decision |
| `P7-3.117` | MUST NOT | No writes through a projection |
| `P7-3.118` | MUST | Demonstration satisfiable |
| **Section 4** | | **Interfaces** |
| `P7-4.1` | MUST | Operation classes separated |
| `P7-4.2` | MUST | Refusal is an outcome |
| `P7-4.3` | MUST | Idempotence key accepted |
| `P7-4.4` | MUST NOT | No partial policy recording |
| `P7-4.5` | MUST | Preconditions checked at recording |
| `P7-4.6` | MUST | Whole policy version in one operation |
| `P7-4.7` | MUST | Approval recorded, never granted |
| `P7-4.8` | MUST | Withdrawal produces an exposure report |
| `P7-4.9` | MUST | Analysis performed before evaluation |
| `P7-4.10` | MUST | Refused versions retained |
| `P7-4.11` | MUST | Pins recorded before returning |
| `P7-4.12` | MUST | Reproduction available |
| `P7-4.13` | MUST | Reproduction failure recorded, not hidden |
| `P7-4.14` | MUST | Simulation over recorded requests available |
| `P7-4.15` | MUST NOT | No action on a non authoritative run |
| `P7-4.16` | MUST | Batch decides per request |
| `P7-4.17` | MUST | Explanation assembled, not recomputed |
| `P7-4.18` | MUST | Report accepted only from the recipient |
| `P7-4.19` | MUST | Reporting unobstructed |
| `P7-4.20` | MUST | Residue required with the outcome |
| `P7-4.21` | MUST | Late reports accepted and marked |
| `P7-4.22` | MUST NOT | No report as a decision amendment |
| `P7-4.23` | MUST | Times required on temporal resolution |
| `P7-4.24` | MUST NOT | No partial decision record |
| `P7-4.25` | MUST | Enforcement state returned with every decision |
| `P7-4.26` | MUST | Caller obligations declared |
| `P7-4.27` | MUST NOT | No permit as permission to proceed |
| `P7-4.28` | MUST NOT | No deny without its provenance |
| `P7-4.29` | MUST | Declared unavailability behaviour |
| `P7-4.30` | MUST NOT | No substitution on unavailability |
| `P7-4.31` | MUST | Attribute unavailability yields indeterminate, not deny |
| `P7-4.32` | MUST | Ledger recording failure does not lose the decision |
| `P7-4.33` | MUST | Minimum event set |
| `P7-4.34` | MUST | Envelope minimum |
| `P7-4.35` | MUST NOT | No event in place of a record |
| `P7-4.36` | MUST | Not applicable emitted individually |
| `P7-4.37` | MUST | Unfulfilled permits emitted individually |
| `P7-4.38` | MUST NOT | No suppression of adverse events |
| **Section 5** | | **State model** |
| `P7-5.1` | MUST | Four models separate |
| `P7-5.2` | MUST | States are projections |
| `P7-5.3` | MUST NOT | No force state held |
| `P7-5.4` | MUST | Unknown enforcement state representable |
| `P7-5.5` | MUST | Enumerated states only |
| `P7-5.6` | MUST | Enumerated transitions only |
| `P7-5.7` | MUST | State is a projection |
| `P7-5.8` | MUST | Suspension emitted and reported with its consequence |
| `P7-5.9` | MUST | Refused versions retained and countable |
| `P7-5.10` | MUST | Withdrawal authorised, reasoned and exposure reported |
| `P7-5.11` | MUST | Superseded versions remain evaluable |
| `P7-5.12` | MUST NOT | No evaluation outside evaluable states |
| `P7-5.13` | MUST NOT | No state change from the passage of time |
| `P7-5.14` | MUST | Enumerated run states |
| `P7-5.15` | MUST | Attributes gathered before evaluation |
| `P7-5.16` | MUST | Absence does not refuse the run |
| `P7-5.17` | MUST | Policy decision and obligation forced decision both recorded |
| `P7-5.18` | MUST | Abandonment detected and recorded |
| `P7-5.19` | MUST | Terminal states are terminal |
| `P7-5.20` | MUST | Enumerated enforcement states |
| `P7-5.21` | MUST | Expiry without report is a state, not a fault |
| `P7-5.22` | MUST | Unreported population standing |
| `P7-5.23` | MUST | Late reports transition the state |
| `P7-5.24` | MUST | Reports recorded as claims |
| `P7-5.25` | MUST NOT | No enforcement state inferred |
| `P7-5.26` | MUST | States held independently |
| `P7-5.27` | MUST | Unreported obligation is a state |
| `P7-5.28` | MUST | Review raised on the enumerated conditions |
| `P7-5.29` | MUST | Every step a recorded act |
| `P7-5.30` | MUST NOT | No discharge without an act |
| **Section 6** | | **Execution semantics** |
| `P7-6.1` | MUST | Identical inputs yield identical decisions |
| `P7-6.2` | MUST | Reproduction reads recorded values |
| `P7-6.3` | MUST | Condition semantics from Part 2 |
| `P7-6.4` | MUST | Attributes recorded as read, not as required |
| `P7-6.5` | MUST | Bag order total and declared |
| `P7-6.6` | MUST | Exact arithmetic for comparison |
| `P7-6.7` | MUST | Collation pinned |
| `P7-6.8` | MUST | Algorithm order |
| `P7-6.9` | MUST | Non matching elements recorded |
| `P7-6.10` | MUST | Staleness refuses, absence continues |
| `P7-6.11` | MUST | Element results recorded individually |
| `P7-6.12` | MUST | Combination steps recorded with inputs |
| `P7-6.13` | MUST | Order independence demonstrable |
| `P7-6.14` | MUST | Delegation assessed after policy and before obligations |
| `P7-6.15` | MUST | Both decisions recorded where obligations forced a change |
| `P7-6.16` | MUST | Extended value on every indeterminate |
| `P7-6.17` | MUST | Extended value computed |
| `P7-6.18` | MUST NOT | No defaulting to the widest value |
| `P7-6.19` | MUST | Cause recorded with the extended value |
| `P7-6.20` | MUST NOT | No indeterminate as a deny |
| `P7-6.21` | MUST | Obligations from contributing elements only |
| `P7-6.22` | MUST | Parameters resolved from recorded values |
| `P7-6.23` | MUST | Capability checked before returning |
| `P7-6.24` | MUST | Undischargeable obligation on a deny raises a review |
| `P7-6.25` | MUST | Obligation order declared |
| `P7-6.26` | MUST | Knowledge time assigned by this component |
| `P7-6.27` | MUST NOT | No occurrence time assignment |
| `P7-6.28` | MUST NOT | No ambient clock in a condition |
| `P7-6.29` | MUST | Instants in a declared scale |
| `P7-6.30` | MUST | Staleness computed from recorded instants |
| `P7-6.31` | MUST | Validity computed from the decision instant |
| `P7-6.32` | MUST | Idempotence by key |
| `P7-6.33` | MUST | Deduplication window declared |
| `P7-6.34` | MUST NOT | No idempotence across differing payloads |
| `P7-6.35` | MUST | Repeated decisions recorded separately |
| `P7-6.36` | MUST | Three bounds declared |
| `P7-6.37` | MUST | Primary budget deterministic |
| `P7-6.38` | MUST | Truncation yields the widest indeterminate |
| `P7-6.39` | MUST NOT | No silent bound |
| `P7-6.40` | MUST | Five analyses performed where decidable |
| `P7-6.41` | MUST | Request space declared for coverage |
| `P7-6.42` | MUST | Coverage reported as a proportion with its complement |
| `P7-6.43` | MUST | Shadowed rules reported |
| `P7-6.44` | MUST | Algebraic properties verified |
| `P7-6.45` | MUST | Unreachable obligations reported |
| `P7-6.46` | MUST | Analyses not performed recorded with the reason |
| `P7-6.47` | MUST NOT | No absence of finding as absence of fault |
| `P7-6.48` | MUST NOT | No analysis at evaluation time |
| `P7-6.49` | MUST | Permitted computations only |
| `P7-6.50` | MUST NOT | No inference of an attribute |
| `P7-6.51` | MUST NOT | No learning from decisions |
| `P7-6.52` | MUST NOT | No assessment of policy fitness |
| **Section 7** | | **Outcome and failure taxonomy** |
| `P7-7.1` | MUST | Closed decision set |
| `P7-7.2` | MUST NOT | No additional members |
| `P7-7.3` | MUST | Extended value on every indeterminate |
| `P7-7.4` | MUST | Not applicable returned as not applicable |
| `P7-7.5` | MUST | Obligation forced deny distinguished |
| `P7-7.6` | MUST NOT | No mapping onto a permit and deny pair |
| `P7-7.7` | MUST NOT | No caller selected collapse |
| `P7-7.8` | MUST | Fail safe response is the enforcement point's |
| `P7-7.9` | MUST | Envelope completeness |
| `P7-7.10` | MUST NOT | No envelope reduction |
| `P7-7.11` | MUST | Absent attributes in the envelope |
| `P7-7.12` | MUST | Verifiability in the envelope |
| `P7-7.13` | MUST | Closed enforcement outcome set |
| `P7-7.14` | MUST | Under application countable |
| `P7-7.15` | MUST | Over application countable |
| `P7-7.16` | MUST | Unknown action recorded as reported |
| `P7-7.17` | MUST NOT | No enforcement outcome inferred |
| `P7-7.18` | MUST | One outcome per obligation instance |
| `P7-7.19` | MUST | Not reported is not fulfilled |
| `P7-7.20` | MUST | Permit with an unfulfilled obligation reported as such |
| `P7-7.21` | MUST | Residue accompanies the outcome |
| `P7-7.22` | MUST | Refusal codes |
| `P7-7.23` | MUST | Refusal states what must change |
| `P7-7.24` | MUST | Meta policy declared |
| `P7-7.25` | MUST NOT | No unbounded meta recursion |
| `P7-7.26` | MUST NOT | No refusal as a deny |
| `P7-7.27` | MUST | Recording obligations honoured |
| `P7-7.28` | MUST | Emission obligations honoured |
| `P7-7.29` | MUST | Review obligations raised on the enumerated conditions |
| `P7-7.30` | MUST | Obligation distinguished from task |
| `P7-7.31` | MUST | Open obligations countable |
| `P7-7.32` | MUST NOT | No authorisation language for a not applicable |
| `P7-7.33` | MUST | An absence of policy is never a refusal by policy |
| `P7-7.34` | MUST | An inability to evaluate is never a decision |
| `P7-7.35` | MUST | A decision returned is never an operation authorised |
| **Section 8** | | **Observability and the audit record** |
| `P7-8.1` | MUST | Decision side complete |
| `P7-8.2` | MUST | Enforcement incompleteness measured, not hidden |
| `P7-8.3` | MUST | Determinations recorded with Part 3 |
| `P7-8.4` | MUST NOT | No second citation structure |
| `P7-8.5` | MUST | Own operations recorded |
| `P7-8.6` | MUST | Declared grain |
| `P7-8.7` | MUST | Attribute values recorded per use |
| `P7-8.8` | MUST | Condition results recorded individually |
| `P7-8.9` | MUST | Counting grain stated with every count |
| `P7-8.10` | MUST | Reproduction sufficiency |
| `P7-8.11` | MUST | Request recorded as received |
| `P7-8.12` | MUST | Conventions recorded |
| `P7-8.13` | MUST | Precondition outcomes recorded, including passes |
| `P7-8.14` | MUST | Periodic reproduction |
| `P7-8.15` | MUST | Divergence recorded, not corrected |
| `P7-8.16` | MUST | Reads recorded |
| `P7-8.17` | MUST | Withholding recorded |
| `P7-8.18` | MUST | Simulations recorded with their requester |
| `P7-8.19` | MUST | Explanation reads recorded |
| `P7-8.20` | MUST | Signals produced |
| `P7-8.21` | MUST | Signals derived from entries |
| `P7-8.22` | MUST NOT | No suppression of a signal |
| `P7-8.23` | MUST | Coverage reported continuously |
| `P7-8.24` | MUST | Unreported population standing and attributable |
| `P7-8.25` | MUST | Emergency use trended |
| `P7-8.26` | SHOULD | Signal thresholds declared |
| `P7-8.27` | MUST | Package sufficiency |
| `P7-8.28` | MUST | Policy content included or its absence stated |
| `P7-8.29` | MUST | Attribute values and absences included |
| `P7-8.30` | MUST | Enforcement state included |
| `P7-8.31` | MUST | Withholding record included |
| `P7-8.32` | MUST | Limit statements included |
| `P7-8.33` | MUST | Absence stated, not omitted |
| `P7-8.34` | MUST | Package digest |
| `P7-8.35` | MUST NOT | No package for a simulation |
| `P7-8.36` | MUST | Self description |
| `P7-8.37` | MUST | Retention obtained, not assigned |
| `P7-8.38` | MUST | Decisions retained with the operations they authorised |
| `P7-8.39` | MUST | Policies outlive their decisions |
| `P7-8.40` | MUST | Attribute values retained with the decision |
| `P7-8.41` | MUST | Obligation records outlive the decision |
| `P7-8.42` | MUST | Separate retention per structure |
| `P7-8.43` | MUST NOT | No disposal under an open review obligation |
| `P7-8.44` | MUST | Disposal recorded and citable |
| `P7-8.45` | MUST NOT | No amendment of a decision |
| `P7-8.46` | MUST NOT | No amendment of an enforcement report |
| `P7-8.47` | MUST NOT | No retrospective re evaluation |
| `P7-8.48` | MUST | Migration preserves identity and digests |
| `P7-8.49` | MUST NOT | No bulk assignment on import |
| **Section 9** | | **Extension model** |
| `P7-9.1` | MUST | Closed sets not extended |
| `P7-9.2` | MUST | Unknown member is a defect, not a default |
| `P7-9.3` | MUST | Open sets registered |
| `P7-9.4` | MUST NOT | No combining behaviour by registration |
| `P7-9.5` | MUST | Registry as controlled document |
| `P7-9.6` | MUST NOT | No key reuse |
| `P7-9.7` | MUST | Deprecation rather than removal |
| `P7-9.8` | MUST | Registry version pinned to the decision |
| `P7-9.9` | MUST | Semantics in the entry |
| `P7-9.10` | MUST | Obligation semantics stated in full |
| `P7-9.11` | MUST | Verifiability and its method declared |
| `P7-9.12` | MUST | Residue kinds declared per obligation kind |
| `P7-9.13` | MUST | Advice admissibility declared |
| `P7-9.14` | MUST NOT | No obligation kind by bilateral understanding |
| `P7-9.15` | MUST | Category semantics declared |
| `P7-9.16` | MUST | Requester supplied attributes marked |
| `P7-9.17` | MUST | Requester influenced decisions reportable |
| `P7-9.18` | MUST | Residue kind semantics declared |
| `P7-9.19` | MUST | External notification raised with the residue |
| `P7-9.20` | MUST | Capability set declared |
| `P7-9.21` | MUST | Not applicable response declared |
| `P7-9.22` | MUST | Extended indeterminate responses declared |
| `P7-9.23` | MUST | Reporting undertaking declared |
| `P7-9.24` | MUST | Non reporting points distinguished |
| `P7-9.25` | MUST | Maximum honoured validity declared |
| `P7-9.26` | MUST | Operation meanings declared |
| `P7-9.27` | MUST | Purposes registered and recorded |
| `P7-9.28` | MUST | Minimum purpose distinctions |
| `P7-9.29` | MUST | Administrative queries excluded from the unreported population |
| `P7-9.30` | MUST NOT | No default purpose |
| `P7-9.31` | MUST | Both registered and both recorded |
| `P7-9.32` | MUST | Deprecation without invalidation |
| `P7-9.33` | MUST | Refusal codes registered with remedy |
| `P7-9.34` | MUST | Event types registered |
| `P7-9.35` | MUST | Membership by pinned version only |
| `P7-9.36` | MUST NOT | No condition reading another policy's decision |
| `P7-9.37` | MUST NOT | No conditional combining algorithm |
| `P7-9.38` | MUST | Nesting depth declared and enforced |
| `P7-9.39` | MUST NOT | No cyclic membership |
| `P7-9.40` | MUST | Attribute composition recorded as attributes |
| **Section 10** | | **Standards and specifications** |
| `P7-10.1` | MUST | Cited edition recorded |
| `P7-10.2` | MUST | Basis marked |
| `P7-10.3` | MUST | Unsourced requirements identified |
| `P7-10.4` | MUST | Practice basis recorded |
| **Section 11** | | **Anti patterns** |
| `P7-11.1` | MUST | Not applicable returned as not applicable |
| `P7-11.2` | MUST NOT | No indeterminate as a deny |
| `P7-11.3` | MUST NOT | No two valued interface |
| `P7-11.4` | MUST NOT | No order dependent resolution |
| `P7-11.5` | MUST | Collapsing algorithms fenced to the outermost set |
| `P7-11.6` | MUST | Unfulfilled obligation on a permit reported |
| `P7-11.7` | MUST | Capability declared and mismatch detected |
| `P7-11.8` | MUST | Obligation kinds registered |
| `P7-11.9` | MUST NOT | No silent restriction |
| `P7-11.10` | MUST | Staleness bounded per attribute and enforced |
| `P7-11.11` | MUST | Absent attribute yields indeterminate |
| `P7-11.12` | MUST | Declared default authorised and recorded |
| `P7-11.13` | MUST | Validity declared and expired reliance reported |
| `P7-11.14` | MUST | Revocation reach stated and exposure computable |
| `P7-11.15` | MUST NOT | No enforcement inferred from silence |
| `P7-11.16` | MUST | Reporting unobstructed |
| `P7-11.17` | MUST NOT | No duplicated business rule |
| `P7-11.18` | MUST | A role is an attribute |
| `P7-11.19` | MUST | Ownership is an attribute |
| `P7-11.20` | MUST | Emergency access is a declared policy |
| `P7-11.21` | MUST | Overdue reviews countable and trended |
| `P7-11.22` | MUST | Meta policy declared and depth bounded |
| `P7-11.23` | MUST | Coverage measured against a declared space |
| `P7-11.24` | MUST | Shadowing analysed and reported |
| `P7-11.25` | MUST NOT | No enforcement |
| `P7-11.26` | MUST NOT | No authentication |
| **Section 12** | | **Boundaries with other parts** |
| `P7-12.1` | MUST | Declared allocation |
| `P7-12.2` | MUST | Refusal or absence rather than substitution |
| `P7-12.3` | MUST NOT | No reaching past a neighbour |
| `P7-12.4` | MUST NOT | No document state held |
| `P7-12.5` | MUST NOT | No marking interpreted as a rule |
| `P7-12.6` | MUST | Decision reference supplied for recording |
| `P7-12.7` | MUST | Verdicts read as attributes |
| `P7-12.8` | MUST | Withheld paths identified as withheld |
| `P7-12.9` | MUST | Indeterminate verdict carried as indeterminate |
| `P7-12.10` | MUST | Delegation validity owned here |
| `P7-12.11` | MUST | Withheld scope identified as withheld |
| `P7-12.12` | MUST | Determinations recorded there, not here |
| `P7-12.13` | MUST | Concepts resolved, not defined |
| `P7-12.14` | MUST | Attributes registered as dependencies |
| `P7-12.15` | MUST NOT | No stewardship as entitlement |
| `P7-12.16` | MUST NOT | No business selection |
| `P7-12.17` | MUST | Business outcomes read as attributes by pin |
| `P7-12.18` | MUST | Determinations recorded with Part 3, not Part 5 |
| `P7-12.19` | MUST NOT | No orchestration |
| `P7-12.20` | MUST NOT | No process state held |
| `P7-12.21` | MUST | Intervention decisions supplied |
| `P7-12.22` | MUST | Review obligations recorded, not managed |
| `P7-12.23` | MUST NOT | No task driven discharge |
| `P7-12.24` | MUST | Human decisions authorised, not performed |
| `P7-12.25` | MUST NOT | No schema validation or versioning |
| `P7-12.26` | MUST | Structural refusal distinguished from denial |
| `P7-12.27` | MUST | Value sets read by pin |
| `P7-12.28` | MUST | Target completeness checked against the set |
| `P7-12.29` | MUST | Set change surfaces as a policy change |
| `P7-12.30` | MUST | Digest is the interface |
| `P7-12.31` | MUST NOT | No decision state in the store |
| `P7-12.32` | MUST | Read only assessment |
| `P7-12.33` | MUST NOT | No self assessment as assessment |
| `P7-12.34` | MUST | Declared request space exposed |
| `P7-12.35` | MUST NOT | No invocation during an evaluation |
| `P7-12.36` | MUST | Model outputs marked as attributes |
| `P7-12.37` | MUST | Reproduction limit recorded |
| `P7-12.38` | MUST | Agent requests assessed for delegation |
| `P7-12.39` | MUST | Authority declared, not assumed |
| `P7-12.40` | MUST | Non results returned unmodified |
| `P7-12.41` | MUST | Enforcement gap exposed to composition |
| **Section 13** | | **What could not be established** |
| `P7-13.1` | MUST | Verification before approval |
| `P7-13.2` | MUST | Gaps declared, not filled |
| `P7-13.3` | SHOULD | Open questions carried forward |

### Derived counts

Every figure below is derived by extraction from the clause text of this document and not asserted independently. The grain of counting is stated for each figure. A clause is one line of the document matching the clause heading form given under Binding of requirement language, that is, an identifier of the form `P7-S.N`, a modality in parentheses, and a subject label. Narrative sentences containing a requirement keyword are not clauses and are not counted; per that same section they are not binding.

**Total clauses.** 463. Grain: one clause heading.

**By modality.** Grain: one clause heading, counted once against its single declared modality.

| Modality | Clauses | Share |
| --- | --- | --- |
| MUST | 353 | 76.2% |
| MUST NOT | 106 | 22.9% |
| SHOULD | 4 | 0.9% |
| SHOULD NOT | 0 | 0.0% |
| MAY | 0 | 0.0% |
| **All** | **463** | **100.0%** |

**Absolute requirements.** 459 clauses carry MUST or MUST NOT and are therefore conditions of conformance. 4 carry SHOULD or SHOULD NOT and require a recorded reason where not satisfied. 0 carry MAY and constrain nothing. Grain: one clause heading. These three figures sum to the total.

**By section.** Grain: one clause heading, attributed to the numbered section in which its heading appears.

| Section | Title | Clauses | MUST | MUST NOT | SHOULD | SHOULD NOT | MAY |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Scope and responsibilities | 18 | 9 | 8 | 1 | 0 | 0 |
| 2 | Terminology | 9 | 1 | 7 | 1 | 0 | 0 |
| 3 | Data model | 118 | 95 | 23 | 0 | 0 | 0 |
| 4 | Interfaces | 38 | 29 | 9 | 0 | 0 | 0 |
| 5 | State model | 30 | 25 | 5 | 0 | 0 | 0 |
| 6 | Execution semantics | 52 | 41 | 11 | 0 | 0 | 0 |
| 7 | Outcome and failure taxonomy | 35 | 27 | 8 | 0 | 0 | 0 |
| 8 | Observability and the audit record | 49 | 40 | 8 | 1 | 0 | 0 |
| 9 | Extension model | 40 | 33 | 7 | 0 | 0 | 0 |
| 10 | Standards and specifications | 4 | 4 | 0 | 0 | 0 | 0 |
| 11 | Anti patterns | 26 | 18 | 8 | 0 | 0 | 0 |
| 12 | Boundaries with other parts | 41 | 29 | 12 | 0 | 0 | 0 |
| 13 | What could not be established | 3 | 2 | 0 | 1 | 0 | 0 |
| **All** | | **463** | **353** | **106** | **4** | **0** | **0** |

**Ordinal integrity.** In this version, the highest ordinal in each section equals the number of clauses in that section, so no identifier has yet been retired. This will cease to be true at the first clause removal, and the count rather than the highest ordinal is then the figure to rely on.

## 1. Scope and responsibilities

### 1.1 What this component is

This part specifies a component that decides whether a principal may perform an operation, on what policy, over what attributes, and with what obligations attached, and that records the decision in a form from which it can later be accounted for.

It is a **policy decision point**. It is not a policy enforcement point, and the separation is the whole design.

The component exists to answer one question reliably: **who was permitted to do what, on which policy version, over which attributes, with which obligations, and was the decision enforced as decided.** The last clause of that question is the one this component cannot answer by itself, and admitting that is the spine of the part.

**The decision is advice until it is enforced.** This component evaluates policy and returns a decision with obligations. Something else applies it. Between the two there is a gap: the enforcement point may not receive the decision, may misapply it, may act on it after it has expired, may be unable to discharge an obligation and proceed anyway, or may simply not report back. Every authorisation failure of consequence lives in that gap, and a component that records only what it decided has recorded the half of the story it controls.

The consequence for the model is stated in section 3.2 and repeated as clauses throughout: **what was decided and what was enforced are two facts, recorded separately, and the second is frequently unknown.** The honest count of decisions whose enforcement was never reported is the measure of how much of an organisation's access control is unverified, and section 8.5 requires it.

Three further properties distinguish the component and each is a subject the authoring brief named.

**It evaluates policy and nothing else.** A verdict about a rule is `Part 2`'s and arrives here as an attribute. A business selection is `Part 5`'s and arrives here as an attribute. Whether a document is in force is `Part 1`'s. This component combines attributes under policy to produce an entitlement, and it produces nothing else.

**It attaches obligations and cannot discharge them.** An obligation is a directive returned with a decision that the enforcement point must fulfil. The reviewed standard is unambiguous that an enforcement point which cannot understand or discharge an obligation must deny. What no standard says is what happens when the enforcement point discharges an obligation partially, cannot discharge it, or does not report. Sections 3.9 and 3.10 give obligations their own outcome taxonomy and their own residue model, on the same pattern `Part 6` applies to compensation and for the same reason.

**It combines by declared algorithm, never by declaration order.** A combining algorithm is a named, versioned, authorised artifact. Where several policies apply and disagree, the algorithm resolves it, and the algorithm is policy. This part refuses the algorithms whose resolution is the order in which policies were written, which is the fourth consecutive part to refuse selection by declaration order and section 13.7 records that the refusal has become a standard wide principle.

There is one further property that belongs in this list because five prior parts depend on it.

**This component is the origin of every withheld value in the estate.** `Part 1` distinguishes a withheld record from an absent one. `Part 2` returns `SUBJECT_PATH_WITHHELD` as a distinct indeterminacy code. `Part 3` records a negative citation as `PARTIAL_WITHHELD`. `Part 4` requires null semantics to distinguish withheld from absent. All four distinctions exist because of a decision made here, and clauses P2-12.18 and P3-12.18 require this component to identify what it restricted as withheld rather than silently removing it. Section 3.11 specifies the obligation and it is the single most consequential requirement this part owes to the rest of the standard.

The component is accountable for the following.

Policy definitions, policy sets and rules as governed artifacts, with their versions, authorities and approvals.

Targets and conditions, and the requirement that a condition read only attributes and never evaluate a business rule.

Attributes: their identity, their source, their pinning, their as of instant, their declared maximum staleness, and the treatment of an attribute that is absent.

The request, the decision instant, and the pinning of everything the decision depended on.

Combining algorithms: the closed set, their declared algebraic properties, and the ones this part refuses.

Obligations and advice, held separately, with obligations declared fulfillable or not and advice declared ignorable.

Obligation outcomes, including partial and impossible fulfilment, and the enumeration and assignment of residue.

The withholding obligation: the requirement that a restriction be marked rather than silent, and the record of what was restricted.

Decision validity, caching bounds, and the enumerated limits of what a revocation can reach.

Delegation validity, which `Part 3` and `Part 4` both allocate here.

Emergency access, declared as policy rather than existing outside it.

The decision record, the enforcement report, and the separation of the two.

The audit record of all of the above, at a grain sufficient to reproduce any decision.

### 1.2 What this component is not

The component is not an enforcement point. It decides; it does not intercept, block, redact, filter or permit. Clause P7-1.4 states it and section 3.2 explains why the separation cannot be relaxed.

The component is not an authenticator. It receives an authenticated principal with an authentication reference and it never establishes identity. A component that authenticates and authorises has one failure that produces both a wrong identity and a wrong entitlement, and neither is separately detectable.

The component is not a token issuer, and a token scope is not a decision. A scope granted at issuance is a coarse pre authorisation made without the resource, the action or the environment in view. It is an input attribute here and section 12.14 hands `Part 0` the question of how the two relate.

The component is not a rules engine. A condition here reads attributes; it does not evaluate a business constraint. `Part 2` section 12.7 names the conflation from the other side and clause P7-1.5 forbids it.

The component is not a decision engine in `Part 5`'s sense. It does not select among candidate business outcomes. The boundary is contestable and `Part 5` section 12.7 says so; section 12.5 restates the test and its limits.

The component is not a workflow engine. It does not sequence, retry, escalate or chase. An authorisation is not a step.

The component is not the ledger. Every decision is a determination recorded with `Part 3`, per the reciprocal `Part 5` requires of this part.

The component does not hold document status, definition state, process state or reference data membership. It reads them as attributes.

The component is not a data filter. It may attach an obligation to redact and it must not perform the redaction, and the redaction must be marked rather than silent per section 3.11.

The component is not a conformance assessor, of itself or of anything else.

**P7-1.1 (MUST) Purpose satisfaction.** An implementation must be able to state, for any decision within its retained history, the principal, the operation, the resource, the policy version applied, every attribute read with its source and as of instant, the combining algorithms applied, the decision, every obligation attached, and whether enforcement was reported, by the mechanism specified in section 6.

**P7-1.2 (MUST) Decision and enforcement recorded separately.** An implementation must record what it decided and what an enforcement point reported having done as two facts and must not represent the first as evidence of the second.

**P7-1.3 (MUST) Unreported enforcement countable.** An implementation must be able to report every decision for which no enforcement report was received, and must include the count in the signals of section 8.5.

**P7-1.4 (MUST NOT) No enforcement.** An implementation must not intercept an operation, block it, permit it, redact a value, filter a result or take any action upon a resource, and must return a decision with obligations for an enforcement point to apply.

**P7-1.5 (MUST NOT) No business rule evaluation.** An implementation must not evaluate a business constraint, must obtain every verdict as an attribute from `Part 2`, and must not admit a condition that duplicates a rule governed there.

**P7-1.6 (MUST NOT) No business selection.** An implementation must not select among candidate business outcomes and must obtain every such outcome as an attribute from `Part 5`.

**P7-1.7 (MUST NOT) No authentication.** An implementation must not establish the identity of a principal, must require an authentication reference with every request, and must record it.

**P7-1.8 (MUST) Four decision values at minimum.** An implementation must distinguish permit, deny, not applicable and indeterminate, and must carry the extended indeterminate information of section 7.2.

**P7-1.9 (MUST NOT) No default deny in the decision.** An implementation must return not applicable where no policy addressed the request and must not substitute a deny, per section 3.8.

**P7-1.10 (MUST) Obligations distinguished from advice.** An implementation must hold obligations and advice as separate sets and must not represent one as the other.

**P7-1.11 (MUST) Withholding marked, never silent.** An implementation must require every restriction it imposes on what a requester may see to be marked as withheld rather than silently removed, per section 3.11.

**P7-1.12 (MUST) Reproducibility.** An implementation must be able to reproduce any decision it has issued from the attributes and policy versions pinned with it, and must return the same decision on re evaluation with the same pins.

**P7-1.13 (MUST) Every attribute pinned.** An implementation must record the identity, source, value digest and as of instant of every attribute a decision read.

**P7-1.14 (MUST NOT) No update in place.** An implementation must not represent any state change specified by this part as a modification or deletion of a previously written row.

**P7-1.15 (MUST NOT) No absorption of neighbouring responsibilities.** An implementation must not enforce, authenticate, issue tokens, evaluate business rules, select business outcomes, orchestrate, hold document, definition or process state, or master reference data, as those responsibilities are allocated in section 12.

**P7-1.16 (SHOULD) Declared exclusions.** An implementation should publish, as a controlled document under `Part 1`, the list of section 1.2 exclusions that it in fact provides by other means, so that a reader can tell what the implementation does not guarantee.

**P7-1.17 (MUST NOT) No conformance self assertion.** An implementation must not assert conformance to this part on the basis of its own internal checks alone, and must not represent such an assertion as an assessment.

**P7-1.18 (MUST) Time horizon declaration.** An implementation must declare the period for which it undertakes to answer the purpose question, as a duration or an absolute date rather than as an indefinite commitment.

### 1.3 Why the separation of decision from enforcement cannot be relaxed

The separation is old. The access control framework of the reference model literature distinguished an access control decision function from an access control enforcement function decades before any of the current standards, and every subsequent standard has preserved it. It is preserved because collapsing it produces a specific and unrecoverable failure.

A component that both decides and enforces has one record, and the record says that access was granted. It cannot distinguish four situations that require four different responses.

The policy permitted the operation and it happened as permitted.

The policy permitted the operation with an obligation to log the access, the log write failed, and the operation happened anyway. Under the reviewed standard's own rule the operation should have been denied.

The policy did not address the operation at all, the enforcement point applied a local default, and the operation happened on the strength of a configuration rather than a policy.

The policy denied the operation, the enforcement point had a cached permit from forty minutes earlier, and the operation happened on a revoked entitlement.

In a combined component all four are one row saying granted. In a separated component the first is a decision and a matching enforcement report; the second is a permit with an unfulfilled obligation, which section 3.10 makes visible; the third is a not applicable that the enforcement point turned into a permit, which section 7.4 makes visible; and the fourth is an expired decision acted upon, which section 3.12 makes visible.

None of the three failures is exotic. Each is the ordinary behaviour of an ordinary estate, and each is invisible in every access log that records only the outcome.

### 1.4 The reader this part is written for

Three readers, and the third is the one this part is unusual in serving.

The first is an application, asking whether to proceed. That reader wants one value and will take a boolean if offered one.

The second is an investigator, asked why a particular person saw a particular record in a particular year. That reader needs the policy version, the attributes as they stood, the combining algorithms and the obligations.

The third is an assurance function, asked whether the organisation's access control works. That reader needs neither individual decision but the distributions: how many requests no policy addressed, how many obligations were never reported fulfilled, how many decisions were acted on after expiry, how many emergency accesses were granted and reviewed. Sections 6.8 and 8.5 exist for that reader, and no component that returns a boolean can serve them.

Where the first reader's convenience conflicts with the other two, this part serves the other two, and section 13.2 records that the cost is a decision response substantially larger than an application wants.
## 2. Terminology

Terms are defined here only if this component owns them. A term owned by another part is cited to that part and is not redefined. Where a term is taken from an external standard, the standard is named. Where this part narrows or diverges from the external definition, the divergence is stated.

The vocabulary of this subject is unusually settled. The decision point, enforcement point, information point and administration point terminology is common to the reviewed standards and follows RFC 2904 in all but the administration point. This part adopts it and states where it narrows.

### 2.1 Terms owned by this part

**Principal.** The authenticated actor on whose behalf a request is made. Authenticated elsewhere and received here with an authentication reference.

**Operation.** The action a principal seeks to perform, named in a registered vocabulary.

**Resource.** The thing upon which the operation is sought.

**Environment.** The attributes relevant to a decision that are properties of neither the principal, the operation nor the resource. Sense follows XACML 3.0.

**Request.** The tuple of principal, operation, resource and environment, with the decision instant and the purpose, presented for a decision.

**Attribute.** A named value a policy may read, with a declared source, a value digest, an as of instant and a declared maximum staleness.

**Policy.** A governed artifact containing rules, a target, a combining algorithm for its rules, and obligations and advice.

**Policy set.** A governed artifact containing policies or further policy sets, a target, a combining algorithm for its members, and obligations and advice.

**Rule.** The smallest governed unit of policy: a target, a condition and an effect of permit or deny.

**Target.** The declaration of which requests a rule, policy or policy set addresses. A target that does not match yields not applicable.

**Condition.** A predicate over attributes evaluating to true, false or indeterminate. Three valued, matching `Part 2` section 6.2, and constrained by section 3.5 to read attributes only.

**Effect.** The decision a rule yields where its target matches and its condition is true: permit or deny.

**Combining algorithm.** The governed artifact by which the decisions of the members of a policy or policy set are combined into one. Drawn from the closed set of section 3.8.

**Decision.** One of the members of the closed set of section 7.2: permit, deny, not applicable, or one of the three extended indeterminate values.

**Extended indeterminate.** An indeterminate decision carrying the set of decisions the evaluation could have produced had the indeterminacy not arisen. Term and sense follow XACML 3.0, which distinguishes an indeterminate that could only have been deny, one that could only have been permit, and one that could have been either.

**Obligation.** A directive returned with a decision that the enforcement point is required to fulfil. Sense follows XACML 3.0, in which an enforcement point must deny access unless it understands and can discharge every obligation associated with the applicable policy.

**Advice.** A directive returned with a decision that the enforcement point may ignore. Sense follows XACML 3.0.

**Fulfilment condition.** The decision upon which an obligation is triggered: permit, deny, or both. Corresponds to XACML's fulfilment attribute.

**Obligation outcome.** The enumerated result of an enforcement point's attempt to fulfil an obligation, drawn from the closed set of section 3.10.

**Obligation residue.** The part of an obligation's intended effect that was not achieved, enumerated and assigned to an owner. The concept is taken deliberately from `Part 6` section 3.10 and the parallel is noted in section 13.7.

**Withholding obligation.** An obligation requiring the enforcement point to restrict what a requester sees and to mark the restriction as withheld rather than removing it silently. Section 3.11.

**Enforcement point.** The component that requests a decision and applies it. Not specified by this part and not this component.

**Enforcement report.** The enforcement point's account of what it did with a decision, including the outcome of every obligation.

**Decision validity.** The declared interval for which a decision may be relied upon, after which it must not be acted on.

**Delegation.** The relation by which one principal acts on behalf of another. `Part 3` records the chain as asserted; this component decides whether it is valid, per section 3.13.

**Emergency access.** A decision reached under a declared policy that admits an operation the ordinary policy would refuse, with heightened obligations. Section 3.14.

**Coverage.** The proportion of a declared request space that some policy addresses. Its complement is the population for which the decision is not applicable, per section 6.8.

**Application time.** The time dimension in which a policy version is in force. Used unchanged from `Part 1` section 2.1.

**Knowledge time.** The instant at which this component durably recorded a fact, assigned by this component. Used unchanged from `Part 1`.

**Occurrence time.** The instant at which a recorded act happened in the world, as asserted by an actor. Used unchanged from `Part 1`.

**Pin.** A recorded identity and version of something a decision depended on. Used unchanged from `Part 2` section 2.1.

### 2.2 Clauses governing terminology

**P7-2.1 (MUST) Single meaning per term.** An implementation must use each term defined in section 2.1 with the meaning given there in all of its interfaces, records, reports and documentation.

**P7-2.2 (MUST NOT) No redefinition.** An implementation must not use a term defined in section 2.1 for a different concept, and must not use a different term for a concept defined in section 2.1 in any interface specified by this part.

**P7-2.3 (MUST NOT) No collapsing of decision and enforcement.** An implementation must not use one term or one record for what was decided and what was done.

**P7-2.4 (MUST NOT) No collapsing of obligation and advice.** An implementation must not use one term or one set for a directive the enforcement point must fulfil and one it may ignore.

**P7-2.5 (MUST NOT) No collapsing of not applicable and deny.** An implementation must not use one term or one value for the absence of an applicable policy and a policy that refused.

**P7-2.6 (MUST NOT) No collapsing of the three indeterminate values.** An implementation must not use one term or one value for an indeterminate that could only have been permit, one that could only have been deny, and one that could have been either.

**P7-2.7 (MUST NOT) No collapsing of a scope and a decision.** An implementation must not treat a token scope, a role assignment or a group membership as a decision, and must treat each as an attribute.

**P7-2.8 (MUST NOT) No collapsing of the three clocks.** An implementation must not use one term or one field for more than one of application time, knowledge time and occurrence time.

**P7-2.9 (SHOULD) Term registry.** An implementation should publish the terms it adds beyond section 2.1, with definitions, as a controlled document under `Part 1`.
## 3. Data model

The model is stated as entities with typed fields. For each field the model gives its type, whether it is required, its cardinality, and what its absence means. Absence semantics are stated because in this component the commonest wrong inference from a missing field is that an obligation was fulfilled.

### 3.1 Type vocabulary

| Type | Value space | Notes |
| --- | --- | --- |
| `ID` | An opaque, globally unique, immutable identifier | Never reused. Never parsed for meaning. |
| `URN` | A persistent name in a declared namespace | Resolvable by the component owning the namespace. |
| `ATIME` | An instant in application time | The dimension in which policy versions are in force. |
| `KTIME` | An instant in knowledge time, assigned by this component | Never accepted from a caller. |
| `OTIME` | An instant asserted by an actor as when an act occurred | Never assigned by this component. |
| `SEQ` | A monotonically increasing ordinal within a named stream | Total order within the stream only. |
| `DIGEST` | An algorithm identifier and a value | Algorithm from the registry of section 9.7. |
| `ENUM` | A member of a named closed or registered set | The set is named at every point of use. |
| `TEXT` | A sequence of characters intended for a person | Carries a `LANG`. |
| `LANG` | A language tag per BCP 47 | Required wherever `TEXT` appears. |
| `PIN` | An identity, a version and where available a digest | Sufficient to obtain the identical artifact again. |
| `CITEREF` | A citation resolvable under `Part 1`, carrying its mode | Used for policy authority and approval. |
| `ATTRREF` | An attribute identity, its category and its source | Section 3.6. |
| `TRUTH3` | One of `TRUE`, `FALSE`, `INDETERMINATE` | The condition domain, used unchanged from `Part 2` section 6.2. |
| `PRINCIPAL` | An opaque reference to an authenticated actor | Carries its kind and its authentication reference. |
| `AUTHNREF` | A reference to the authentication that established a principal | Recorded, never verified here. |
| `DETREF` | A reference to a `Part 2` report or a `Part 5` outcome consumed as an attribute | Carries which, and the whole envelope by pin. |
| `DURATION` | A length of time, independent of any instant | |
| `COUNT` | A non negative integer | Grain stated wherever reported. |

The `AUTHNREF` type is recorded and never verified, and the distinction is the substance of clause P7-1.7. This component knows that something authenticated the principal and records what; it does not establish that the authentication was sound.

**P7-3.1 (MUST) Declared types.** An implementation must be able to state, for every field it holds that corresponds to a field in this section, which type of the table above it carries.

**P7-3.2 (MUST NOT) No semantic identifiers.** An implementation must not derive an entitlement, a policy's applicability or an attribute's trustworthiness from the characters of its `ID` or `URN`.

**P7-3.3 (MUST) Language tag present.** An implementation must record a `LANG` with every `TEXT` value and must not default it silently.

**P7-3.4 (MUST NOT) No caller supplied knowledge time.** An implementation must assign every `KTIME` itself and must reject a request supplying one.

**P7-3.5 (MUST) Authentication reference recorded, not verified.** An implementation must record an `AUTHNREF` with every request, must refuse a request lacking one, and must not represent its presence as evidence that the authentication was sound.

**P7-3.6 (MUST) Three valued condition domain used unchanged.** An implementation must use the truth domain of `Part 2` section 6.2 for every condition and must not introduce a two valued reduction.

### 3.2 The decision is not the enforcement

This section states the spine and the two records by which it is kept.

**What this component knows.** The request it received. The policy versions it resolved. The attributes it read, with their sources and as of instants. The conditions it evaluated and their truth values. The combining algorithms it applied. The decision it produced. The obligations and advice it attached. The validity it declared. It knows all of this with certainty because it did all of it.

**What this component does not know.** Whether the enforcement point received the decision. Whether it understood every obligation. Whether it discharged them. Whether it applied the decision at all. Whether it applied it within the declared validity. Whether the operation happened. It knows none of this, and it can only know what an enforcement point reports.

The model therefore holds two records and never merges them.

A `decision` is what this component produced. It is immutable, complete and certain.

An `enforcement_report` is what an enforcement point says it did. It is a claim by another party, it may be absent, and its absence is the ordinary case.

The distinction has one consequence that is worth stating in advance of the field tables, because it is counterintuitive. **The absence of an enforcement report is not an error.** An enforcement point that does not report is behaving as most do. What the absence means is that the decision's effect is unverified, and the honest response is to count the population rather than to treat each instance as a fault. Clause P7-3.9 requires the count and clause P7-3.10 forbids the inference that goes the other way.

The reciprocal obligation on the enforcement point is not specified by this part, because the enforcement point is not specified by this part. What this part specifies is that the report be receivable, that its absence be visible, and that no projection present a decision as an account of what happened.

**P7-3.7 (MUST) Two records, never merged.** An implementation must hold the decision and any enforcement report as separate records and must not represent the decision as an account of what occurred.

**P7-3.8 (MUST) Report receivable.** An implementation must provide an operation by which an enforcement point reports what it did with a decision, including the outcome of every obligation.

**P7-3.9 (MUST) Unreported population counted.** An implementation must be able to report every decision for which no enforcement report was received, by policy version, by enforcement point and by age, and must include the count in the signals of section 8.5.

**P7-3.10 (MUST NOT) No inference of enforcement.** An implementation must not infer that a decision was enforced, that an obligation was fulfilled, or that an operation occurred, from the fact that a decision was returned.

**P7-3.11 (MUST NOT) No absence of report as a fault.** An implementation must not record the absence of an enforcement report as an error, a failure or a defect, and must record it as an unverified decision.

**P7-3.12 (MUST) Enforcement point identified.** An implementation must record the identity of the enforcement point to which every decision was returned, so that an unreporting population is attributable.

### 3.3 Entity inventory

Every entity is immutable once written. A change is a new row; nothing specified in this part is ever updated in place. The reason is the one every prior part gives and one specific to this component: a decision record is the evidence that an access was or was not authorised, and an editable authorisation record is not evidence.

| Group | Entity | Purpose |
| --- | --- | --- |
| Policy | `policy_definition` | The persistent identity of a policy or policy set. |
| Policy | `policy_version` | One immutable state of a policy or policy set. |
| Policy | `rule_definition` | One rule within a policy version: target, condition, effect. |
| Policy | `target_declaration` | Which requests an element addresses. |
| Policy | `combining_algorithm_binding` | The algorithm binding of a policy or policy set version. |
| Policy | `policy_authority` | The clause from which a policy derives its legitimacy. |
| Policy | `policy_approval` | The `Part 1` resolution establishing approval. |
| Policy | `policy_membership` | A member of a policy set version, by pinned version. |
| Policy | `policy_analysis` | A recorded static analysis over a policy version. |
| Attribute | `attribute_declaration` | A declared attribute: its identity, category, source and staleness bound. |
| Attribute | `attribute_value` | One attribute value read in one evaluation. |
| Attribute | `attribute_absence` | A declared absence of an attribute in one evaluation. |
| Request | `decision_request` | What was asked, with the instants and the purpose. |
| Request | `evaluation_run` | One evaluation: its bounds, clocks and result. |
| Request | `condition_evaluation` | One condition and its three valued result. |
| Request | `element_result` | The result of one rule, policy or policy set within an evaluation. |
| Request | `combination_step` | One application of a combining algorithm and its inputs. |
| Request | `decision` | The decision produced, with its validity. |
| Request | `decision_pin` | One artifact the evaluation depended on. |
| Obligation | `obligation_declaration` | An obligation declared on a policy element. |
| Obligation | `obligation_instance` | An obligation attached to one decision, with its resolved parameters. |
| Obligation | `advice_instance` | An advice attached to one decision. |
| Obligation | `obligation_outcome` | The reported result of an attempt to fulfil an obligation. |
| Obligation | `obligation_residue` | The part of an obligation's effect not achieved. |
| Obligation | `residue_assignment` | The owner to whom a residue was assigned. |
| Withholding | `withholding_obligation` | An obligation restricting what a requester sees. |
| Withholding | `withholding_record` | What was restricted, by whom and how marked. |
| Enforcement | `enforcement_report` | An enforcement point's account of what it did. |
| Enforcement | `enforcement_point_registration` | A registered enforcement point and its declared capabilities. |
| Delegation | `delegation_assessment` | The validity of an asserted delegation chain. |
| Emergency | `emergency_access_policy` | A declared policy admitting emergency access. |
| Emergency | `emergency_access_record` | One emergency access granted, with its review obligation. |
| Registry | `combining_algorithm_registration` | Reserved. Combining algorithms are closed; see section 9.1. |
| Registry | `obligation_kind_registration` | A registered obligation kind and its fulfilment semantics. |
| Registry | `attribute_category_registration` | A registered attribute category. |
| Registry | `operation_vocabulary_registration` | A registered operation vocabulary. |
| Registry | `residue_kind_registration` | A registered residue kind. |
| Registry | `purpose_registration` | A registered decision purpose. |

**P7-3.13 (MUST) Entity coverage.** An implementation must be able to state, for every entity in the table above, where the information it carries is held, or that the entity is not applicable because the corresponding optional capability is not provided.

**P7-3.14 (MUST NOT) No update in place.** An implementation must not represent any state change specified by this part as a modification or deletion of a previously written row.

**P7-3.15 (MUST NOT) No decision amendment.** An implementation must not modify a recorded decision, its attributes, its condition evaluations, its combination steps or its obligations, and must record a corrected conclusion as a further decision whose relation to the earlier one is recorded.

### 3.4 Policies, policy sets and versions

`policy_version` fields:

| Field | Type | Required | Cardinality | Absence means |
| --- | --- | --- | --- | --- |
| `policy_version_id` | `ID` | yes | 1 | n/a |
| `policy_id` | `ID` | yes | 1 | n/a |
| `element_kind` | `ENUM` | yes | 1 | n/a. `POLICY` or `POLICY_SET`. |
| `document_citation` | `CITEREF` | yes | 1 | n/a. The `Part 1` version carrying the policy. |
| `document_locator` | `PATH` | yes | 1 | n/a |
| `statement` | `TEXT` | yes | 1..n | n/a. The policy in natural language, one per language, one authoritative. |
| `target_id` | `ID` | yes | 1 | n/a |
| `combining_algorithm` | `ENUM` | yes | 1 | n/a. A member of the closed set of section 3.8. |
| `obligation_ids` | `ID` | no | 0..n | The element attaches no obligations. |
| `advice_ids` | `ID` | no | 0..n | The element attaches no advice. |
| `created_ktime` | `KTIME` | yes | 1 | n/a |
| `authored_by` | `PRINCIPAL` | yes | 1..n | n/a |
| `analysis_reference` | `PIN` | no | 0..n | No static analysis has been recorded for this version. |

The `statement` field is required for the same reason `Part 2` section 3.6 requires one on a rule and `Part 5` clause P5-3.39 requires one on a criterion: a policy governs people and a policy expressed only as a computation is a policy nobody can read. The correspondence between the statement and the rules is not mechanically checkable, and section 13.2 records that this is the fourth appearance of that limitation in the standard.

`policy_membership` binds a member into a policy set version, **by pinned version only**. Membership by lineage would make the including set's content change without the set changing, which is the position `Part 2` clause P2-9.32, `Part 4` clause P4-9.33 and `Part 6` clause P6-9.33 all take for the same reason. Clause P7-3.20 states it.

**P7-3.16 (MUST) Policy carried by a document.** An implementation must record the `Part 1` citation and locator of every policy version and must not evaluate a policy that has none.

**P7-3.17 (MUST) Statement present and authoritative language designated.** An implementation must hold at least one statement for every policy version and must designate exactly one language authoritative.

**P7-3.18 (MUST) Combining algorithm on every element.** An implementation must record a combining algorithm from the closed set of section 3.8 on every policy and policy set version and must not default it.

**P7-3.19 (MUST) Authority per policy version.** An implementation must record an authority for every policy version, must record `UNDECLARED` where none can be identified rather than recording a plausible one, and must be able to report every policy of undeclared authority.

**P7-3.20 (MUST) Membership by pinned version only.** An implementation must bind every member of a policy set version by pinned version and must not permit membership by lineage.

**P7-3.21 (MUST NOT) No cyclic membership.** An implementation must refuse a policy set version whose membership graph contains a cycle and must declare and enforce a maximum nesting depth.

**P7-3.22 (MUST) Approval obtained, not asserted.** An implementation must obtain the approval of every policy version by resolution against `Part 1`, must record the whole resolution outcome envelope, and must return the approval status with every decision that applied it.

**P7-3.23 (MUST NOT) No policy amendment.** An implementation must not alter a recorded policy version and must record every change as a new version.

**P7-3.24 (MUST) Authority drift observed.** An implementation must check the resolvability and status of every policy authority on a declared cycle, must record an observation where the cited version has been superseded or withdrawn, must continue to evaluate the policy, and must report the condition with every decision that applied it, on the same basis as `Part 2` clause P2-3.10.

### 3.5 Rules, targets and conditions

`rule_definition` fields carry the `policy_version_id`, a `rule_ordinal` recorded and prohibited from affecting any decision, the `target_id`, the `condition`, the `effect` of `PERMIT` or `DENY`, and the obligation and advice identities attached to the rule.

The `rule_ordinal` is recorded because a reader tracing a policy needs to see the order in which rules were written, and it is prohibited from mattering because a written order is not a governed criterion. Clause P7-3.27 states the prohibition and it is the same prohibition `Part 2` clause P2-3.68, `Part 5` clause P5-3.26 and `Part 6` clause P6-3.26 each state for their own ordinals.

A **target** declares which requests an element addresses, as a conjunction of disjunctions over attribute matches. A target that does not match yields not applicable, which is the mechanism by which coverage is measurable at all.

A **condition** is a predicate over attributes, evaluating in the three valued domain. Four constraints apply and each closes a route by which policy evaluation becomes something else.

**A condition reads attributes only.** It does not invoke, compute a business quantity, read a clock or consult a store. Every value it reads is an attribute with a declared source, per section 3.6.

**A condition does not duplicate a business rule.** Where the predicate the policy needs is a constraint governed under `Part 2`, the policy reads the verdict as an attribute rather than restating the constraint. Clause P7-3.29 states it and section 12.2 explains why the temptation is acute: a constraint and an authorisation condition are both predicates over a subject, and the same expression language would serve for both.

**A condition is bounded.** No unbounded recursion, no unbounded iteration, and a declared bound the implementation can enforce, on the same basis as `Part 2` clause P2-3.22.

**A condition is pure.** No effects, no writes, no randomness, and nothing that varies between evaluations with identical attributes.

**P7-3.25 (MUST) Target on every element.** An implementation must record a target on every rule, policy and policy set version and must treat a non matching target as yielding not applicable.

**P7-3.26 (MUST) Effect from a closed pair.** An implementation must record an effect of exactly `PERMIT` or `DENY` on every rule.

**P7-3.27 (MUST NOT) No effect from rule ordinal.** An implementation must not permit the order in which rules, policies or policy sets were declared to affect any decision, except through a combining algorithm the closed set of section 3.8 admits for that purpose.

**P7-3.28 (MUST) Conditions read attributes only.** An implementation must not admit a condition that reads any value other than an attribute declared under section 3.6, and must not admit one that invokes a component, reads a clock or consults a store.

**P7-3.29 (MUST NOT) No duplicated business rule.** An implementation must not admit a condition that restates a constraint governed under `Part 2` and must require the policy to read the verdict as an attribute.

**P7-3.30 (MUST) Conditions bounded.** An implementation must not admit a condition in a language permitting unbounded computation without a bound the implementation can enforce.

**P7-3.31 (MUST) Conditions pure.** An implementation must not admit a condition with an effect, a write, a random source or any value that varies between evaluations with identical attributes.

**P7-3.32 (MUST) Condition result recorded three valued.** An implementation must record the three valued result of every condition it evaluated and must not record only whether the rule fired.
### 3.6 Attributes, their pinning, staleness and absence

An attribute is the only thing a policy reads, so everything about a decision's soundness reduces to properties of its attributes. Three of those properties are routinely unrecorded and each produces a specific wrong decision.

`attribute_declaration` fields:

| Field | Type | Required | Cardinality | Absence means |
| --- | --- | --- | --- | --- |
| `attribute_id` | `ID` | yes | 1 | n/a |
| `attribute_urn` | `URN` | yes | 1 | n/a |
| `category` | `ENUM` | yes | 1 | n/a. Registered. `PRINCIPAL`, `OPERATION`, `RESOURCE`, `ENVIRONMENT` at minimum. |
| `source_component` | `URN` | yes | 1 | n/a. The component that owns the value. |
| `concept_reference` | `PIN` | no | 0..1 | The attribute is not bound to a governed concept. Reportable. |
| `datatype` | `URN` | yes | 1 | n/a |
| `maximum_staleness` | `DURATION` | yes | 1 | n/a. The interval beyond which a value must not be relied upon. |
| `absence_semantics` | `ENUM` | yes | 1 | n/a. One of `INDETERMINATE`, `TREAT_AS_EMPTY_BAG`, `DECLARED_DEFAULT`. |
| `default_value` | `TEXT` | no | 0..1 | Required where `absence_semantics` is `DECLARED_DEFAULT`. |
| `default_authority` | `CITEREF` | no | 0..1 | Required wherever a default value is present. |

`attribute_value` fields carry the `evaluation_run_id`, the `attribute_id`, a `value_digest`, the `as_of_otime` at which the value was true according to its source, the `obtained_ktime`, the `source_reference` by which the source's own record can be obtained, and a `staleness` derived from the two instants.

Three requirements carry this section.

**Every attribute is pinned.** Without the identity, the source, the digest and the as of instant, the decision is not reproducible, and a decision that cannot be reproduced cannot be defended. Clause P7-3.33 requires it and clause P7-1.12 makes reproducibility the property it serves.

**Staleness is bounded and declared per attribute.** An attribute fetched forty minutes ago and cached is a decision made on facts that may have changed. Different attributes tolerate different staleness: a resource's classification changes rarely, a principal's employment status changes at a moment and matters immediately. Declaring the bound per attribute rather than globally is what makes a cache defensible, and clause P7-3.35 requires a decision resting on an attribute beyond its bound to be refused rather than made.

**An absent attribute is not a false attribute.** This is the third value again and it reaches this component from four directions at once. `Part 2` may return an indeterminate verdict. `Part 4` may declare a representation's null semantics undeclared. `Part 3` may report a search as partially withheld. And an attribute source may simply be unavailable. In every case the condition that reads the attribute cannot be evaluated, so it is indeterminate, so the rule is indeterminate, and section 3.8's combining algorithms carry the indeterminacy into the extended indeterminate decision of section 7.2.

The `absence_semantics` enumeration admits two alternatives to indeterminacy and both are fenced. `TREAT_AS_EMPTY_BAG` is admissible where the attribute is genuinely multi valued and its emptiness is meaningful. `DECLARED_DEFAULT` is admissible with an authority, because supplying a value the source did not supply is a policy act. Clause P7-3.38 requires the authority and clause P7-3.39 requires every decision that relied on a default to record that it did.

**P7-3.33 (MUST) Every attribute pinned.** An implementation must record the identity, category, source, value digest, as of instant and obtained instant of every attribute value a decision read.

**P7-3.34 (MUST) Maximum staleness declared per attribute.** An implementation must record a maximum staleness on every attribute declaration and must not default it globally.

**P7-3.35 (MUST) Stale attribute refuses the decision.** An implementation must refuse a decision that would rest on an attribute value older than its declared maximum staleness, must return the refusal code of section 7.6, and must not make the decision on the stale value.

**P7-3.36 (MUST) Absence declared, not assumed.** An implementation must record an `attribute_absence` for every attribute a condition required and could not obtain, with the reason, and must not omit the record.

**P7-3.37 (MUST) Absence yields indeterminate by default.** An implementation must treat an absent attribute as making every condition that reads it indeterminate, unless the attribute declaration declares another semantics.

**P7-3.38 (MUST) Declared default authorised.** An implementation must record an authority for every attribute declaration whose absence semantics is `DECLARED_DEFAULT`, since supplying a value the source did not supply is a policy act.

**P7-3.39 (MUST) Default reliance recorded on the decision.** An implementation must record, on every decision that relied on a declared default for an absent attribute, which attribute and which default, and must be able to report the population.

**P7-3.40 (MUST) Source reference recorded.** An implementation must record the reference by which the source component's own record of an attribute value can be obtained, and must not record the value as its own content.

**P7-3.41 (MUST) Concept binding reportable.** An implementation must be able to report every attribute declaration not bound to a `Part 4` concept, since an attribute whose meaning is not governed is a policy term nobody can review.

**P7-3.42 (MUST) Attributes registered as dependencies.** An implementation must register every attribute declaration bound to a concept with `Part 4` as a dependent registration of kind `POLICY_ATTRIBUTE`, per clause P4-12.19.

**P7-3.43 (MUST NOT) No attribute derivation.** An implementation must not compute, transform or derive an attribute value from other attributes and must read every value from its declared source.

### 3.7 The request and the decision instant

`decision_request` fields:

| Field | Type | Required | Cardinality | Absence means |
| --- | --- | --- | --- | --- |
| `request_id` | `ID` | yes | 1 | n/a |
| `principal` | `PRINCIPAL` | yes | 1 | n/a |
| `authentication_reference` | `AUTHNREF` | yes | 1 | n/a. Recorded, never verified. |
| `operation` | `URN` | yes | 1 | n/a. From a registered operation vocabulary. |
| `resource` | `URN` | yes | 1..n | n/a |
| `environment_attributes` | `ID` | no | 0..n | No environment attribute was supplied. |
| `decision_instant` | `ATIME` | yes | 1 | n/a. Never defaulted; see clause P7-3.45. |
| `knowledge_instant` | `KTIME` | no | 0..1 | Resolve policy against present belief. |
| `purpose` | `ENUM` | yes | 1 | n/a. Registered under section 9.6. |
| `requesting_enforcement_point` | `URN` | yes | 1 | n/a. Registered under section 9.5. |
| `delegation_assertion` | `PIN` | no | 0..1 | The principal acts on their own behalf. |
| `received_ktime` | `KTIME` | yes | 1 | n/a |

The `decision_instant` is required rather than defaulted, on the same ground `Part 2` clause P2-3.83, `Part 5` clause P5-3.76 and `Part 6` require their own instants. A policy resolved as of the present, in a request that did not say so, produces a decision indistinguishable from a decision about a past state, and the distinction matters most where somebody is asking years later.

The `requesting_enforcement_point` is required so that the unreported population of clause P7-3.9 is attributable, and so that an enforcement point's declared capabilities can be checked against the obligations a decision would attach, per section 3.9.

**P7-3.44 (MUST) Principal and authentication reference required.** An implementation must refuse a request lacking a principal or an authentication reference.

**P7-3.45 (MUST) Decision instant supplied.** An implementation must require a `decision_instant` in every request and must not default it to the time of the request.

**P7-3.46 (MUST) Operation from a registered vocabulary.** An implementation must refuse a request whose operation is not a member of a registered operation vocabulary.

**P7-3.47 (MUST) Purpose recorded.** An implementation must record the declared purpose of every request and must not permit an unregistered purpose.

**P7-3.48 (MUST) Enforcement point identified and registered.** An implementation must refuse a request from an unregistered enforcement point and must record the identity with the decision.

**P7-3.49 (MUST NOT) No clock read for the decision instant.** An implementation must not read a clock to supply a decision instant and must record the instant the request supplied.

### 3.8 Combining algorithms

Where several elements apply and disagree, something must resolve it. That something is a combining algorithm, it is policy, and it is a governed artifact rather than a behaviour of the engine.

The set is **closed**. Eight members. The table is normative.

| Algorithm | Resolves to | Order dependent | Associative and commutative |
| --- | --- | --- | --- |
| `DENY_OVERRIDES` | Deny if any member denies; otherwise permit if any permits; otherwise the indeterminate or not applicable that remains. | No | Yes |
| `PERMIT_OVERRIDES` | Permit if any member permits; otherwise deny if any denies; otherwise as above. | No | Yes |
| `DENY_UNLESS_PERMIT` | Permit if any member permits; deny in every other case. Never returns not applicable or indeterminate. | No | Yes |
| `PERMIT_UNLESS_DENY` | Deny if any member denies; permit in every other case. Never returns not applicable or indeterminate. | No | Yes |
| `ONLY_ONE_APPLICABLE` | The decision of the single applicable member; not applicable if none applies; **indeterminate if more than one applies**. | No | Yes |
| `UNANIMOUS_PERMIT` | Permit only if every applicable member permits; deny if any denies; indeterminate if any is indeterminate. | No | Yes |
| `DENY_OVERRIDES_ORDERED_OBLIGATIONS` | The decision of `DENY_OVERRIDES`, with obligations returned in declared member order. | For obligations only | Yes for the decision |
| `PERMIT_OVERRIDES_ORDERED_OBLIGATIONS` | The decision of `PERMIT_OVERRIDES`, with obligations returned in declared member order. | For obligations only | Yes for the decision |

Five properties of the set are decisions and each is worth stating.

**Order dependent decision resolution is refused.** The reviewed standard provides a first applicable algorithm, which returns the decision of the first member whose target matches. Its resolution is the order in which the members were written, and a written order is not a governed criterion: inserting a policy above another for readability changes what the organisation permits with no record that a policy changed. `Part 2` refused salience, `Part 5` refused first match, `Part 6` refused branch order, and this part refuses first applicable. Clause P7-3.51 states it and section 13.3 records the cost.

**Ordered variants are admitted for obligation sequencing only.** The reviewed standard's ordered deny overrides and ordered permit overrides produce the same decision as their unordered counterparts and differ only in the order in which obligations are evaluated and returned. That is a real and legitimate need, since two obligations may need to be discharged in sequence. Admitting them as obligation orderings rather than as decision rules preserves the decision's order independence and gives authors the sequencing they need, and clause P7-3.52 requires the distinction to be explicit.

**`ONLY_ONE_APPLICABLE` refuses to arbitrate.** Where more than one member applies it returns indeterminate rather than choosing. This is the reviewed standard's own behaviour and it is the same refusal to arbitrate that `Part 2` clause P2-6.49 makes for a rule contradiction and `Part 5` section 7.2 makes for an undecidable selection. Three parts refuse to arbitrate in three vocabularies, and section 13.7 records it as a repeated pattern.

**`DENY_UNLESS_PERMIT` and `PERMIT_UNLESS_DENY` collapse the four values to two**, and the collapse is the boundary collapse this standard refuses everywhere else. They are admitted, because a fail safe outermost boundary is a real requirement, and they are fenced by three clauses. They may appear only at the outermost policy set of an evaluation, never nested. Their use must be authorised and recorded. And the decision the collapse concealed, being the not applicable or the indeterminate that would otherwise have been returned, must be recorded alongside the collapsed decision, so that the coverage gap remains visible. Clause P7-3.54 states the fence.

**Algebraic properties are declared and verified.** Associativity and commutativity of the decision are what make a nested policy set's result independent of how the nesting was drawn, and they are what make the static analysis of section 6.8 tractable. Clause P7-3.55 requires the property to be recorded per algorithm and clause P7-6.44 requires it to be verified.

`combining_algorithm_binding` records the algorithm on a policy or policy set version, its authority where the choice embodies a policy rather than a mechanism, and the obligation ordering where an ordered variant is used.

**P7-3.50 (MUST) Closed algorithm set.** An implementation must record exactly one member of the table above on every policy and policy set version and must not accept an algorithm outside the set.

**P7-3.51 (MUST NOT) No first applicable.** An implementation must not admit a combining algorithm whose decision resolution is determined by the order in which members were declared.

**P7-3.52 (MUST) Ordered variants order obligations only.** An implementation must produce, for an ordered variant, the same decision its unordered counterpart produces, must apply the declared order only to the sequence in which obligations are returned, and must record that the ordering applied to obligations.

**P7-3.53 (MUST) Only one applicable returns indeterminate on multiplicity.** An implementation must return indeterminate where a `ONLY_ONE_APPLICABLE` element has more than one applicable member, must record every applicable member, and must not select among them.

**P7-3.54 (MUST) Collapsing algorithms fenced.** An implementation must admit `DENY_UNLESS_PERMIT` and `PERMIT_UNLESS_DENY` only at the outermost policy set of an evaluation, must require the use to be authorised and recorded, and must record the not applicable or indeterminate decision the collapse concealed.

**P7-3.55 (MUST) Algebraic properties declared.** An implementation must record, for every combining algorithm, whether its decision resolution is associative and commutative, and must not nest a policy set under an algorithm whose declared properties the nesting would violate.

**P7-3.56 (MUST) Combination steps recorded.** An implementation must record every application of a combining algorithm in an evaluation, with the algorithm, the member results it combined and the result it produced.

**P7-3.57 (MUST) Algorithm choice authorised where it embodies policy.** An implementation must record an authority for the choice of combining algorithm on every policy set version whose members disagree in any evaluation, since the algorithm then determines the outcome.

### 3.9 Obligations and advice

An obligation is a directive the enforcement point must fulfil. Advice is a directive it may ignore. Holding them separately is the whole of clause P7-1.10, and the reason is that merging them makes an optional thing mandatory or, far worse, a mandatory thing optional.

The reviewed standard is unambiguous on the central rule and this part adopts it verbatim in effect: **an enforcement point must deny access unless it understands and can discharge every obligation associated with the applicable policy.** Two conditions, not one. An obligation the enforcement point does not recognise produces a deny just as surely as one it recognises and cannot perform. That is a strong rule and it is the right one, because an unrecognised obligation is an instruction that was not carried out and nobody knows what it was.

What the reviewed standard does not supply is a **vocabulary**. Its own text states that there are no standard definitions for these actions and that bilateral agreement between the policy administration point and the enforcement point is required for correct interpretation. So the mechanism is standardised and the meaning of every obligation is private. That is a substantial gap and it is why section 9.3 requires a registry: an obligation kind whose meaning is a bilateral understanding is an obligation no third party can audit.

`obligation_declaration` fields:

| Field | Type | Required | Cardinality | Absence means |
| --- | --- | --- | --- | --- |
| `declaration_id` | `ID` | yes | 1 | n/a |
| `element_id` | `ID` | yes | 1 | n/a. The rule, policy or policy set it attaches to. |
| `obligation_kind` | `ENUM` | yes | 1 | n/a. Registered under section 9.3. |
| `fulfilment_condition` | `ENUM` | yes | 1 | n/a. `ON_PERMIT`, `ON_DENY` or `ON_BOTH`. |
| `parameters` | `ATTRREF` | no | 0..n | The obligation takes no parameters. |
| `fulfilment_verifiable` | `TRUTH3` | yes | 1 | n/a. Whether this component can ever learn the outcome. |
| `authority` | `CITEREF` | yes | 1 | n/a |
| `residue_kinds` | `ENUM` | no | 0..n | Required where `fulfilment_verifiable` is not `TRUE`. |

`obligation_instance` records an obligation attached to one decision, with its parameters resolved from the attributes read.

The `fulfilment_verifiable` field is the field this section adds to the reviewed standard and it earns its place. An obligation to write an access log entry to a system this component can query is verifiable. An obligation to notify a data subject within seventy two hours is not: the notification happens elsewhere, on a schedule this component does not observe, and no report will come. An obligation to redact a field before display is verifiable only if the enforcement point reports it.

Declaring the property means the population of unverifiable obligations is countable, and that count is the honest measure of how much of an organisation's access policy consists of instructions nobody will ever confirm were followed. Clause P7-3.61 requires the count.

**Capability checking.** An enforcement point registration declares which obligation kinds it can discharge, per section 9.5. Where a decision would attach an obligation the requesting enforcement point has not declared, the decision is a deny, because the standard's rule makes it one and because attaching an obligation the recipient cannot perform and permitting anyway is the failure the rule exists to prevent. Clause P7-3.62 states it, and clause P7-3.63 requires the condition to be detectable statically so that an unfulfillable policy is found before it runs.

**P7-3.58 (MUST) Obligations and advice held separately.** An implementation must return obligations and advice as two distinct sets and must not represent an advice as an obligation or the reverse.

**P7-3.59 (MUST) Obligation kind registered with an authority.** An implementation must record a registered obligation kind and an authority on every obligation declaration.

**P7-3.60 (MUST) Fulfilment condition recorded.** An implementation must record whether an obligation is triggered on permit, on deny or on both, and must attach it only where the condition matches the decision.

**P7-3.61 (MUST) Verifiability declared and counted.** An implementation must record whether the fulfilment of every obligation kind is verifiable by this component and must be able to report the population of unverifiable obligations by kind and by policy version.

**P7-3.62 (MUST) Undischargeable obligation yields deny.** An implementation must return deny where a decision would attach an obligation of a kind the requesting enforcement point has not declared it can discharge, and must record the obligation and the enforcement point in the decision.

**P7-3.63 (MUST) Capability mismatch detectable statically.** An implementation must be able to report every combination of policy version and registered enforcement point in which the policy could attach an obligation the enforcement point cannot discharge, and must include the count in the signals of section 8.5.

**P7-3.64 (MUST) Parameters resolved from recorded attributes.** An implementation must resolve every obligation parameter from attributes it recorded in the evaluation and must not compute a parameter value.

**P7-3.65 (MUST) Advice ignorable in fact.** An implementation must not attach as advice any directive whose non performance would make a permit unsafe, and must attach such a directive as an obligation.

**P7-3.66 (MUST NOT) No obligation without an authority.** An implementation must refuse an obligation declaration lacking an authority, since an obligation is an instruction imposed on another component and imposing one is a policy act.
### 3.10 Obligation outcomes and residue

An obligation is returned. Whether it was fulfilled is a separate fact, reported by somebody else, and frequently unknown. This section gives the fact a taxonomy, on the same pattern `Part 6` section 3.10 applies to compensation and for the same reason: the reviewed standard specifies when an obligation is attached and says nothing about what it means for one to have failed.

`obligation_outcome` is a closed set of six members. The table is normative.

| Member | Means | Residue |
| --- | --- | --- |
| `FULFILLED` | The enforcement point reported performing every part of the obligation. | None. |
| `FULFILLED_PARTIALLY` | Some part was performed and some was not. | Required, enumerated. |
| `FULFILMENT_IMPOSSIBLE` | The obligation could not be performed in the state that obtained. | Required, enumerated. |
| `FULFILMENT_FAILED` | Performance was attempted and did not complete. The position is **unknown**, not unchanged. | Required, enumerated. |
| `FULFILMENT_NOT_REPORTED` | No report was received. The ordinary case for an unverifiable obligation. | Required where the obligation had an intended effect. |
| `NOT_APPLICABLE_TO_DECISION` | The obligation's fulfilment condition did not match the decision. | None. |

Two members carry the weight and both are absent from every implementation this part is written against.

**`FULFILMENT_NOT_REPORTED` is the default and the most common.** It is not a failure. It records that the obligation was attached, the decision was returned, and nothing came back. For an obligation declared unverifiable it is the expected terminal state, and the honest response is to count the population rather than to treat each instance as an incident. The count is the measure of how much of the estate's access policy is an instruction nobody confirmed.

**`FULFILMENT_FAILED` leaves the position unknown.** An obligation to redact that was attempted and did not complete may have redacted some fields; an obligation to log that failed may have written a partial entry. The record must say that the position is unknown, and clause P7-3.69 forbids recording it as though nothing happened, because acting on that assumption is how a second redaction attempt produces a doubly redacted record or a second log entry produces a duplicate.

And one member carries a consequence that follows from the standard's own rule. Where an obligation attached to a **permit** was not fulfilled, the reviewed standard's rule means the operation should have been denied. So a permit with an unfulfilled obligation is not merely a permit with a loose end: **it is an operation that should not have proceeded.** Clause P7-3.71 requires the condition to raise the review obligation of section 7.7 and clause P7-3.72 requires it to be separately countable, because it is the most consequential single population this component can report.

`obligation_residue` fields carry the `obligation_outcome_id`, a registered `residue_kind`, a `description`, an `extent` where quantifiable, a `remediable_later` truth value and the `observed_ktime`. The minimum registered residue kinds:

| Kind | Means |
| --- | --- |
| `ACCESS_UNLOGGED` | An access occurred and the record of it was not written. |
| `NOTIFICATION_UNSENT` | A party who should have been told was not. |
| `REDACTION_UNAPPLIED` | Information reached a requester who should not have seen it. |
| `MARKING_UNAPPLIED` | Information was disclosed without the marking that governs its onward handling. |
| `CONSENT_UNRECORDED` | An access requiring a recorded consent proceeded without the record. |
| `REVIEW_UNRAISED` | An access requiring subsequent review will not be reviewed. |
| `RETENTION_UNSET` | A derived copy was created and its retention was not established. |
| `RESIDUE_UNCLASSIFIED` | The residue is known and its kind is not. |

`REDACTION_UNAPPLIED` and `MARKING_UNAPPLIED` are the two whose consequences reach outside the organisation, and section 9.4 requires a residue kind registration to declare whether it carries an external notification obligation, on the same basis `Part 6` clause P6-9.25 requires.

`residue_assignment` records the owner, the assigning actor and the authorisation. A residue with no assigned owner is a consequence nobody is answerable for, and clause P7-3.74 requires the count to be a standing signal.

**P7-3.67 (MUST) Closed outcome set.** An implementation must record exactly one member of the table above for every obligation instance and must not accept a value outside the set.

**P7-3.68 (MUST) Not reported is the default.** An implementation must record `FULFILMENT_NOT_REPORTED` for every obligation instance for which no report has been received and must not record it as fulfilled or as failed.

**P7-3.69 (MUST) Failed fulfilment leaves the position unknown.** An implementation must record a `FULFILMENT_FAILED` outcome as leaving the position unknown, must not record it as leaving the intended effect unachieved in a determinate way, and must raise the review obligation of section 7.7.

**P7-3.70 (MUST) Residue enumerated where required.** An implementation must enumerate the residue for every outcome the table above requires it for and must refuse to record such an outcome without at least one residue record.

**P7-3.71 (MUST) Unfulfilled obligation on a permit raises a review obligation.** An implementation must raise a review obligation for every obligation attached to a permit whose outcome is other than `FULFILLED`, since under the rule of section 3.9 the operation should not have proceeded.

**P7-3.72 (MUST) Unfulfilled permits countable.** An implementation must be able to report every permit with an obligation whose outcome is other than `FULFILLED`, by policy version, obligation kind and enforcement point, and must include the count in the signals of section 8.5.

**P7-3.73 (MUST) Residue assigned.** An implementation must record an assignment of every residue to an owner, with the assigning actor and the authorisation, or must record that no assignment has been made.

**P7-3.74 (MUST) Unassigned residue countable.** An implementation must be able to report every residue with no recorded assignment, by kind and by age, and must include the count in the signals of section 8.5.

**P7-3.75 (MUST NOT) No outcome inference.** An implementation must not infer an obligation outcome from the receipt of an enforcement report that does not mention it, and must record `FULFILMENT_NOT_REPORTED` for every obligation the report did not address.

**P7-3.76 (MUST) Obligation outcomes recorded with Part 3.** An implementation must record every obligation outcome other than `FULFILLED` and `NOT_APPLICABLE_TO_DECISION` as an act with `Part 3`, with its residue, so that a determination relying on the access can reach it.

### 3.11 The withholding obligation

This section discharges the obligations `Part 2` clause P2-12.18 and `Part 3` clause P3-12.18 impose on this part, and it is the requirement this part owes most heavily to the rest of the standard.

Four prior parts maintain a distinction between a value that is absent and a value that is withheld. `Part 1` distinguishes a withheld record from an absent one. `Part 2` returns `SUBJECT_PATH_WITHHELD` as an indeterminacy code distinct from `SUBJECT_PATH_UNDECLARED`, and yields indeterminate rather than false for a condition depending on a withheld path. `Part 3` records a negative citation's completeness as `PARTIAL_WITHHELD` where scope was not visible to the searcher, and refuses to treat it as `COMPLETE_OVER_SCOPE`. `Part 4` requires every representation to declare whether an empty value means absent, withheld, unknown or not applicable.

All four distinctions exist because of a decision made here. **This component is where withholding originates**, and if it removes silently, the distinction is destroyed at its source and the four parts downstream are maintaining a difference that no longer has a referent.

The mechanism is a withholding obligation.

`withholding_obligation` fields carry the `obligation_declaration_id`, the `scope_expression` describing what is restricted, a `marking_requirement` of `MARK_AS_WITHHELD`, `MARK_AS_WITHHELD_WITH_REASON` or `MARK_AS_WITHHELD_WITH_APPEAL_PATH`, and the `authority`.

`withholding_record` records what was in fact restricted in one decision: the paths, fields, rows or scope, the marking applied, and the enforcement point that applied it.

The requirement is stated in three clauses and the middle one is the load bearing one.

**P7-3.77 (MUST) Restriction expressed as an obligation.** An implementation must express every restriction on what a requester may see as a withholding obligation attached to a decision and must not perform the restriction itself.

**P7-3.78 (MUST NOT) No silent removal.** An implementation must not attach an obligation whose effect is to remove information without marking the removal, and every withholding obligation must carry a marking requirement.

**P7-3.79 (MUST) Withheld distinguished from absent in the marking.** An implementation must require the marking to distinguish a value withheld from a value absent, so that a consumer applying `Part 2` clause P2-3.72, `Part 3` clause P3-3.40 or `Part 4` clause P4-3.42 can do so correctly.

**P7-3.80 (MUST) What was restricted recorded.** An implementation must record, for every decision carrying a withholding obligation, the scope the obligation restricted, so that a later reader can establish what a requester did not see.

**P7-3.81 (MUST) Reason and appeal path where declared.** An implementation must record the reason and, where the marking requirement demands it, the appeal path, and must not attach a marking requirement demanding either without supplying it.

**P7-3.82 (MUST) Silent restriction reportable.** An implementation must be able to report every enforcement report indicating that a restriction was applied without the required marking, and must include the count in the signals of section 8.5.

**P7-3.83 (MUST NOT) No restriction outside an obligation.** An implementation must not permit a policy to restrict visibility by any means other than a withholding obligation, and in particular must not do so by narrowing the resource in the decision.

### 3.12 Decision validity, caching and the reach of revocation

A decision is a statement about a moment. It is relied upon later, and the interval between is where two failures live.

`decision` carries a `validity_duration` and a `not_valid_after` instant. The enforcement point must not act on a decision after the instant, and `Part 1` clause P1-12.14 already forbids a consumer from caching a decision beyond a declared validity period, which is the reciprocal of this requirement seen from that side.

**What validity achieves.** It bounds the interval during which a stale entitlement can be exercised. A permit with a five minute validity, acted upon four minutes later, may be acting on an entitlement revoked three minutes ago, and the bound is what makes the exposure calculable.

**What validity cannot achieve.** It cannot make a revocation take effect immediately. Between the revocation and the expiry of every outstanding decision, the revoked entitlement remains exercisable. This component cannot push a revocation to an enforcement point holding a decision, because it does not know which enforcement points hold which decisions once returned, and even a notification mechanism cannot guarantee delivery before use.

That limit is structural rather than a defect, and clause P7-3.87 requires it to be stated rather than left to a reader's assumption. The mitigations are three and none is a solution: bound the validity, declare it per policy so that high consequence operations carry a shorter one, and record the exposure window so that a revocation's effective reach is a known quantity rather than a hope.

**P7-3.84 (MUST) Validity declared on every decision.** An implementation must record a validity duration and a not valid after instant on every decision and must not return one without them.

**P7-3.85 (MUST) Validity declared per policy version.** An implementation must record the validity duration on the policy version rather than globally, so that a high consequence operation can carry a shorter one.

**P7-3.86 (MUST) Expired reliance reportable.** An implementation must be able to report every enforcement report indicating that a decision was acted upon after its not valid after instant, and must include the count in the signals of section 8.5.

**P7-3.87 (MUST) Revocation reach stated.** An implementation must state, in the documentation of every reading interface and in every evidence package, that a revocation does not reach a decision already returned and that the exposure window is bounded only by the declared validity.

**P7-3.88 (MUST) Exposure window computable.** An implementation must be able to report, for any revocation of an entitlement, the interval during which outstanding decisions granting it remained valid, and the count of such decisions.

**P7-3.89 (MUST NOT) No indefinite validity.** An implementation must not admit a policy version declaring an unbounded decision validity and must declare a maximum validity it will admit.

**P7-3.90 (MUST NOT) No revocation claim.** An implementation must not represent a revocation as having taken effect at the instant it was recorded and must represent it as taking effect for decisions made after that instant.

### 3.13 Delegation validity

`Part 3` clause P3-12.17 forbids that component from assessing whether a delegation was valid, and `Part 4` section 12.7 allocates delegation validity here. So this component owns the question and `Part 3` owns the record of the chain as asserted.

The division is precise. `Part 3` records that A acted on behalf of B, that B acted on behalf of C, and the instrument cited at each step. This component decides whether that chain entitled A to perform the operation, which is a policy question with an effective date, a scope and an authority.

`delegation_assessment` fields carry the `request_id`, the `chain_reference` to the `Part 3` attribution, an `assessment` of `VALID`, `INVALID_INSTRUMENT_ABSENT`, `INVALID_OUT_OF_SCOPE`, `INVALID_EXPIRED`, `INVALID_CHAIN_INCOMPLETE`, `INVALID_TERMINUS_NOT_ACCOUNTABLE` or `UNASSESSABLE`, the `policy_version` under which it was assessed, and the `assessed_ktime`.

Two members warrant note.

`INVALID_TERMINUS_NOT_ACCOUNTABLE` records a chain terminating in something that cannot bear accountability, which `Part 3` clause P3-3.75 refuses to record at all. So the two parts interact: `Part 3` will not record such a chain, and this component's assessment exists for the case where a chain is asserted to this component directly, in a request, without having been recorded there.

`UNASSESSABLE` records that the chain could not be evaluated, most often because an instrument was not obtainable. It yields indeterminate rather than invalid, because a delegation whose instrument cannot be fetched is not a delegation that was refused. Clause P7-3.94 states it.

**P7-3.91 (MUST) Delegation assessed under a policy version.** An implementation must assess every asserted delegation under a recorded policy version and must record the assessment with the decision.

**P7-3.92 (MUST) Chain obtained, not constructed.** An implementation must obtain an asserted delegation chain from the request or from `Part 3` and must not construct or infer one from a role, a hierarchy or an access grant.

**P7-3.93 (MUST) Assessment recorded on the decision.** An implementation must record the delegation assessment on every decision made on behalf of a delegating principal.

**P7-3.94 (MUST) Unassessable delegation yields indeterminate.** An implementation must return an indeterminate decision where a delegation could not be assessed and must not return deny, since an unobtainable instrument is not a refused delegation.

**P7-3.95 (MUST) Scope of delegation recorded.** An implementation must record the scope within which a delegation was assessed valid and must not treat a valid delegation as unbounded.

**P7-3.96 (MUST NOT) No delegation assessment held by another component.** An implementation must be the only component that assesses delegation validity, per clause P3-12.17, and must expose its assessments so that `Part 3` can cite them.

### 3.14 Emergency access

Every real estate has a mechanism by which somebody obtains access the ordinary policy would refuse: the clinician who needs the record of a patient they have no relationship with, the engineer who needs production data at three in the morning, the investigator who needs an account nobody has granted them. The reviewed literature names the case explicitly as a canonical use of obligations.

The position this part takes is that the mechanism exists and must therefore be **inside** the model. An emergency access path implemented outside policy is an access nobody governs, and its use is invisible.

`emergency_access_policy` is a policy version like any other, with an authority and an approval, whose distinguishing property is that it is declared as an emergency policy and therefore carries three mandatory obligations: an obligation to record the access, an obligation to notify a declared party, and an obligation to raise a review. All three are mandatory rather than advisory, so the standard's rule applies: an enforcement point that cannot discharge them must deny, which means an enforcement point without the capability cannot grant emergency access at all.

`emergency_access_record` records each grant, its justification as asserted by the principal, the review obligation and its discharge.

Two requirements make the mechanism honest rather than decorative.

**The justification is recorded and is not assessed.** The principal asserts why. This component records the assertion and does not evaluate it, because evaluating an emergency justification in the moment is not possible and pretending to do so converts a recorded assertion into a validated one. Clause P7-3.99 states it.

**Review is an obligation, not an intention.** The review obligation is discharged by a recorded act, and the population of undischarged reviews is a standing signal. An emergency access mechanism whose reviews are never performed is an unaudited permanent bypass, and the count is how anybody finds out. Clause P7-3.101 requires it.

**P7-3.97 (MUST) Emergency access is a declared policy.** An implementation must express every emergency access path as a policy version with an authority and an approval and must not admit an access path outside policy.

**P7-3.98 (MUST) Three mandatory obligations.** An implementation must require every emergency access policy version to attach obligations to record the access, to notify a declared party and to raise a review, all as obligations rather than advice.

**P7-3.99 (MUST) Justification recorded, not assessed.** An implementation must record the principal's asserted justification for an emergency access as an assertion and must not evaluate it or represent it as validated.

**P7-3.100 (MUST) Capability required for emergency grant.** An implementation must return deny where an enforcement point requesting an emergency access has not declared the capability to discharge the three mandatory obligations, per clause P7-3.62.

**P7-3.101 (MUST) Undischarged reviews countable.** An implementation must be able to report every emergency access whose review obligation has not been discharged, by policy version, principal and age, and must include the count in the signals of section 8.5.

**P7-3.102 (MUST) Emergency population reportable.** An implementation must be able to report emergency accesses by principal, resource and policy version over time, so that a mechanism intended for exceptions and used routinely is visible.

**P7-3.103 (MUST NOT) No emergency access without a review obligation.** An implementation must not return a permit under an emergency access policy without attaching the review obligation, under any configuration.
### 3.15 The decision record and the enforcement report

`decision` fields:

| Field | Type | Required | Cardinality | Absence means |
| --- | --- | --- | --- | --- |
| `decision_id` | `ID` | yes | 1 | n/a |
| `request_id` | `ID` | yes | 1 | n/a |
| `outcome` | `ENUM` | yes | 1 | n/a. A member of the closed set of section 7.2. |
| `extended_indeterminate` | `ENUM` | no | 0..1 | Required for every indeterminate outcome. |
| `root_policy_version_id` | `ID` | yes | 1 | n/a |
| `policy_versions_evaluated` | `ID` | yes | 1..n | n/a. Every version whose target matched. |
| `policy_versions_not_applicable` | `COUNT` | yes | 1 | n/a. Grain: one policy version whose target did not match. |
| `approval_status` | `ENUM` | yes | 1 | n/a. From the `Part 1` resolution. |
| `authority_status` | `ENUM` | yes | 1 | n/a. One of `IN_FORCE`, `SUPERSEDED`, `WITHDRAWN`, `UNRESOLVABLE`, `NOT_CHECKED`. |
| `attributes_read` | `COUNT` | yes | 1 | n/a. Grain: one attribute value. |
| `attributes_absent` | `COUNT` | yes | 1 | n/a. Grain: one declared absence. |
| `attributes_defaulted` | `COUNT` | yes | 1 | n/a. Grain: one absence resolved by a declared default. |
| `conditions_indeterminate` | `COUNT` | yes | 1 | n/a. Grain: one condition evaluation. |
| `obligation_instance_ids` | `ID` | no | 0..n | The decision attaches no obligation. |
| `advice_instance_ids` | `ID` | no | 0..n | The decision attaches no advice. |
| `collapse_concealed_outcome` | `ENUM` | no | 0..1 | No collapsing algorithm applied. Required where one did. |
| `delegation_assessment_id` | `ID` | no | 0..1 | The principal acted on their own behalf. |
| `emergency_record_id` | `ID` | no | 0..1 | The decision was not under an emergency access policy. |
| `validity_duration` | `DURATION` | yes | 1 | n/a |
| `not_valid_after` | `ATIME` | yes | 1 | n/a |
| `enforcement_point` | `URN` | yes | 1 | n/a |
| `decided_ktime` | `KTIME` | yes | 1 | n/a |

Four fields are worth noting because they exist in no ordinary decision response.

`policy_versions_not_applicable` records how many policies did not address the request. It is the raw material of the coverage measure of section 6.8, and without it a not applicable decision cannot be distinguished from one where forty policies were consulted and none matched.

`attributes_absent`, `attributes_defaulted` and `conditions_indeterminate` are the three counts that say how much of the decision rested on facts the component did not have. A permit reached with four absent attributes and two indeterminate conditions is a materially weaker permit than one reached with none, and no ordinary response says so.

`collapse_concealed_outcome` records what a collapsing combining algorithm hid, per clause P7-3.54. A deny produced by `DENY_UNLESS_PERMIT` where the underlying evaluation was not applicable is a coverage gap wearing the clothes of a policy refusal, and this field is where the gap remains visible.

`enforcement_report` fields carry the `decision_id`, the reporting `enforcement_point`, an `action_taken` of `APPLIED_AS_DECIDED`, `APPLIED_MORE_RESTRICTIVELY`, `APPLIED_LESS_RESTRICTIVELY`, `NOT_APPLIED`, `APPLIED_AFTER_EXPIRY` or `ACTION_UNKNOWN`, the outcome of every obligation, the `operation_occurred` truth value, the `occurred_otime`, and the `reported_ktime`.

`APPLIED_LESS_RESTRICTIVELY` is the member that matters and it is the one an enforcement point will be reluctant to report. It records that the enforcement point permitted more than the decision permitted: it ignored an obligation, it applied a local default over a not applicable, or it proceeded on an expired decision. Providing the member is what makes the honest report possible, and clause P7-3.108 requires the population to be a standing signal, because an estate in which enforcement points systematically under apply decisions has an authorisation system that does not authorise.

**P7-3.104 (MUST) Outcome from the closed set with extended information.** An implementation must record exactly one outcome member from section 7.2 on every decision and must record the extended indeterminate value on every indeterminate outcome.

**P7-3.105 (MUST) Counts derived with grain.** An implementation must derive every count in the decision record from the records of the evaluation, must state the grain of each, and must not accept any as an input.

**P7-3.106 (MUST) Concealed outcome recorded.** An implementation must record the outcome a collapsing combining algorithm concealed, per clause P7-3.54.

**P7-3.107 (MUST) Report distinguishes over and under application.** An implementation must provide the enumeration above for an enforcement report and must distinguish an application more restrictive than the decision from one less restrictive.

**P7-3.108 (MUST) Under application countable.** An implementation must be able to report every enforcement report of `APPLIED_LESS_RESTRICTIVELY` or `APPLIED_AFTER_EXPIRY` by enforcement point and policy version, and must include the counts in the signals of section 8.5.

**P7-3.109 (MUST) Statuses carried with every decision.** An implementation must record the policy approval status and authority status with every decision and must record `NOT_CHECKED` where the drift check of clause P7-3.24 was not current rather than recording `IN_FORCE`.

**P7-3.110 (MUST) Decision recorded as a determination.** An implementation must record every decision as a determination with `Part 3`, citing the policy version as its authority, the attributes as premises, the combining algorithm as its method and the obligations as its outcome, and must not record determinations of its own elsewhere.

**P7-3.111 (MUST NOT) No report amendment.** An implementation must not modify a recorded enforcement report and must record a corrected report as a further report citing the earlier one.

### 3.16 Projections

Every read is a projection: a pure function of the recorded rows, holding no state of its own, recomputable at any time.

| Projection | Yields |
| --- | --- |
| `decision_of` | One decision with its request, policy versions, attributes, condition results, combination steps, obligations and validity. |
| `explanation_of` | The decision assembled for a reader: which rules matched, which conditions held, which algorithm resolved the disagreement, and why. |
| `policy_at` | The policy version in force at an application time and a knowledge time, with its approval and authority status. |
| `decisions_by_outcome` | Decisions by outcome member, by policy version and by enforcement point. |
| `not_applicable_population` | Requests for which no policy applied, by operation, resource kind and enforcement point. The coverage gap. |
| `indeterminate_population` | Indeterminate decisions by extended value and by cause, being absent attribute, unavailable source, unassessable delegation or condition error. |
| `attributes_absent_population` | Decisions resting on absent attributes, by attribute and policy version. |
| `defaulted_attribute_population` | Decisions that relied on a declared default for an absent attribute. |
| `stale_refusals` | Decisions refused because an attribute exceeded its declared staleness, by attribute. |
| `unreported_decisions` | Decisions for which no enforcement report was received, by enforcement point and age. |
| `under_applied_decisions` | Enforcement reports of less restrictive application or application after expiry. |
| `unfulfilled_obligations` | Obligation instances by outcome member, by kind and by enforcement point. |
| `unfulfilled_permits` | Permits carrying an obligation whose outcome is other than fulfilled. |
| `obligation_residues` | Every residue with its kind, extent and assignment, and those unassigned. |
| `unverifiable_obligations` | Obligation kinds declared unverifiable, with the volume attached. |
| `capability_mismatches` | Policy version and enforcement point pairs where an obligation could not be discharged. |
| `withholding_records` | What was restricted, by decision, with the marking applied. |
| `unmarked_restrictions` | Enforcement reports indicating a restriction applied without the required marking. |
| `collapsed_decisions` | Decisions produced by a collapsing algorithm, with the concealed outcome. |
| `emergency_accesses` | Emergency accesses by principal, resource and policy, with review discharge state. |
| `delegation_assessments` | Assessments by member, by policy version and by delegating principal. |
| `revocation_exposure` | For a revocation, the outstanding valid decisions and the exposure window. |
| `policy_analysis_state` | Static analysis results per policy version, with those not performed and why. |
| `decision_divergence` | Where re evaluation of a recorded decision under present pins yields a different outcome. |

`not_applicable_population` is the projection that most distinguishes an implementation of this part. An estate in which a third of requests are not applicable has policy coverage of two thirds, and if the component returns deny in those cases the figure is unknowable. Section 6.8 makes coverage measurable and this projection is where it is read.

`unfulfilled_permits` is the projection an assurance function should read first, for the reason clause P7-3.71 gives: under the reviewed standard's own rule, every member of that population is an operation that should not have proceeded.

**P7-3.112 (MUST) Projections are pure.** An implementation must compute every projection as a function of recorded rows alone, holding no state not derivable from them.

**P7-3.113 (MUST) Projection recomputable.** An implementation must be able to recompute every projection from the recorded rows and to demonstrate agreement between a served projection and a recomputation.

**P7-3.114 (MUST) Named projections available.** An implementation must provide every projection in the table above and must name each as named there in any interface it exposes.

**P7-3.115 (MUST) Not applicable population available.** An implementation must provide `not_applicable_population` and must report it by operation, resource kind and enforcement point.

**P7-3.116 (MUST) Explanation available for every decision.** An implementation must provide `explanation_of` for every recorded decision, assembled from the records of the evaluation, and must not recompute a decision in order to explain it.

**P7-3.117 (MUST NOT) No writes through a projection.** An implementation must not permit any state change to be effected by writing to a projection.

### 3.17 Worked demonstration

The demonstration follows one policy across six years. It is not normative. It exists because the field tables do not show whether the model catches the failures it was built for.

**2027, the policy.** Policy set `PS1` governs access to patient records. Its combining algorithm is `DENY_OVERRIDES`, declared associative and commutative. Its members, by pinned version, are three policies.

`P_relationship` permits where an attribute asserting a care relationship between the principal and the patient is true. The attribute's source is a clinical system, its maximum staleness is four hours, and its absence semantics are `INDETERMINATE`.

`P_consent` denies where a `Part 2` verdict attribute reports that the patient has withheld consent for the principal's role. The verdict is obtained as an attribute, not evaluated here.

`P_emergency` is declared an emergency access policy. It permits where the principal asserts an emergency, and it attaches three mandatory obligations: record the access, notify the patient's care team, and raise a review within twenty four hours.

The root set carries a withholding obligation on every permit: fields marked as restricted by the record's classification must be redacted **and the redaction marked as withheld with an appeal path**. Decision validity is five minutes.

Static analysis records: coverage over the declared request space is 94 per cent, so six per cent of requests will be not applicable; no rule can never fire; the collapsing algorithms are not used; and the emergency policy's three obligations are dischargeable by two of the three registered enforcement points and **not by the third**. That last finding is recorded on the policy version, so it is known from the day the policy is approved that one enforcement point cannot grant emergency access.

**2028, an ordinary decision.** A clinician requests a record. `P_relationship` matches and its condition is true. `P_consent` matches and the `Part 2` verdict attribute reports satisfied. `P_emergency` does not match. `DENY_OVERRIDES` yields permit.

The decision records: outcome permit; three policy versions evaluated, of which one matched not applicable; eleven attributes read, none absent, none defaulted, no condition indeterminate; one obligation attached, being the withholding obligation; validity five minutes; enforcement point recorded.

The enforcement report arrives: applied as decided; the withholding obligation fulfilled with the redaction marked and the appeal path shown; the operation occurred. This is what a complete record looks like and it is the case nobody has trouble with.

**2029, the absent attribute.** The clinical system is unavailable. The care relationship attribute cannot be obtained. `P_relationship`'s condition is indeterminate. `P_consent` still evaluates and returns satisfied, so no deny. `DENY_OVERRIDES` over an indeterminate permit branch and a satisfied non deny yields **indeterminate, extended value `INDETERMINATE_PERMIT`**: had the attribute been obtainable, the decision could only have been permit or not applicable, never deny.

That extended value is what makes the enforcement point's fail safe response principled. It knows the decision could not have been a deny, so a policy of proceeding on `INDETERMINATE_PERMIT` for read operations, declared in advance, is defensible. Under a plain indeterminate it would be a guess.

The decision records one absent attribute and one indeterminate condition. The absent attribute population reports it, and the aggregate over a week reveals that the clinical system was unavailable for nineteen hours, which no individual decision showed.

**2030, the obligation that failed.** An emergency access is granted. The record obligation is fulfilled. The notification obligation fails: the care team's messaging service rejects it.

| Obligation | Outcome | Residue |
| --- | --- | --- |
| Record the access | `FULFILLED` | None |
| Notify the care team | `FULFILMENT_FAILED` | `NOTIFICATION_UNSENT`, position unknown |
| Raise a review | `FULFILLED` | None |

Under the rule of section 3.9 this permit should not have proceeded, because the enforcement point could not discharge every obligation. It proceeded. Clause P7-3.71 raises a review obligation, the decision appears in `unfulfilled_permits`, and the residue is unassigned for four days before being assigned to a clinical governance function with an authorisation.

An implementation without the obligation outcome taxonomy records that the emergency access was granted and the obligations were attached. The failed notification is a line in a messaging service's log with nothing connecting it to the access.

**2031, the enforcement point that under applied.** A quarterly review of `under_applied_decisions` shows one enforcement point reporting `APPLIED_LESS_RESTRICTIVELY` on 212 decisions. Investigation establishes that it was ignoring the withholding obligation for one field type it did not recognise, and therefore displaying unredacted values.

Three things made this findable. The obligation was mandatory, so the standard's rule says the enforcement point should have denied. The enforcement point reported honestly, which the enumeration made possible. And the capability registration of section 9.5 had **not** declared that field type, which clause P7-3.63's static check would have reported as a capability mismatch had anybody read it. The finding was available before the policy ran and was read two years later.

**2032, the revocation.** A principal's access is revoked at 14:02. `revocation_exposure` reports that seven decisions granting the revoked entitlement were outstanding and valid until 14:07, of which two were acted upon at 14:03 and 14:05. Neither was a defect: both acted on valid decisions. The exposure window was five minutes because the policy declared it, and clause P7-3.87's statement is what prevents anybody from believing the revocation was instantaneous.

**2033, the question.** An investigation asks the following.

| Question | Projection | Result |
| --- | --- | --- |
| Why did this clinician see this record in 2028? | `explanation_of` | Three policies, which matched, which conditions held, the algorithm, the obligation |
| What did they not see? | `withholding_records` | The restricted fields, the marking applied, the appeal path |
| Was the decision enforced as decided? | `decision_of` and the report | Yes, applied as decided, obligation fulfilled |
| How much of the estate's policy has coverage? | `not_applicable_population` | Six per cent of requests matched no policy, by operation |
| Did any permit proceed on an unfulfilled obligation? | `unfulfilled_permits` | Yes. The 2030 emergency access and 212 decisions at one enforcement point. |
| Who owns the unsent notification? | `obligation_residues` | Clinical governance, from day four. Unassigned for the first four days. |
| Was the emergency mechanism used routinely? | `emergency_accesses` | The population by principal over time, and the review discharge state |
| How far did the 2032 revocation reach? | `revocation_exposure` | Seven outstanding decisions, five minute window, two exercised |
| Was any of this knowable in advance? | `policy_analysis_state` | Yes. The capability mismatch was recorded in 2027. |

The fifth and ninth rows are the ones the part exists for. The fifth is the population of operations that should not have proceeded, which no access log can produce. The ninth establishes that the most serious finding in six years was available on the day the policy was approved.

**P7-3.118 (MUST) Demonstration satisfiable.** An implementation must be able to answer every question in the table above for any decision within its retained history, using only the projections of section 3.16.
## 4. Interfaces

### 4.1 Interface principles

Operations are specified by their obligations rather than their signatures. No transport, encoding or naming convention is specified.

Operations divide into four groups: those that record policy, those that decide, those that report enforcement, and those that read. The third is separated from the second because an enforcement report is a claim by another party about a decision already made, and merging the two would let a decision be amended by the account of its own application.

**P7-4.1 (MUST) Operation classes separated.** An implementation must not provide an operation that both records a policy version and produces a decision, and must not provide one that both produces a decision and records its enforcement.

**P7-4.2 (MUST) Refusal is an outcome.** An implementation must return a refusal outcome of section 7.6 for any operation it declines and must not return a decision in its place.

**P7-4.3 (MUST) Idempotence key accepted.** An implementation must accept a caller supplied idempotence key on every recording and reporting operation and must honour it per section 6.6.

**P7-4.4 (MUST NOT) No partial policy recording.** An implementation must record a policy version together with its rules, targets, combining algorithm binding, obligations, advice and authority, or record none of them.

### 4.2 Recording operations

| # | Operation | Records | Principal refusals |
| --- | --- | --- | --- |
| 1 | Register a policy | `policy_definition` | Duplicate identity |
| 2 | Record a policy version | `policy_version`, rules, targets, combining algorithm binding, obligations, advice, authority | No document citation; no statement; two authoritative languages; no combining algorithm; a first applicable algorithm; a collapsing algorithm not at the outermost set; a condition reading a non attribute; a condition restating a `Part 2` constraint; an unbounded condition; an obligation with no authority; a rule with no target; no declared validity duration; a validity exceeding the declared maximum |
| 3 | Record policy set membership | `policy_membership` | Membership by lineage; a cycle; nesting beyond the declared depth |
| 4 | Record a policy approval | `policy_approval` | Resolution outcome envelope not supplied in full |
| 5 | Record a policy analysis | `policy_analysis` | Analysis referencing a different version |
| 6 | Record an authority drift observation | drift observation | Unknown policy version |
| 7 | Withdraw a policy version from evaluation | withdrawal | Outstanding valid decisions exist and no exposure report is produced |
| 8 | Declare an attribute | `attribute_declaration` | No source component; no maximum staleness; no absence semantics; a declared default with no authority |
| 9 | Register an enforcement point | registration | No declared obligation capability set |
| 10 | Register an obligation kind | registration | No fulfilment semantics; no verifiability declaration |
| 11 | Register an operation vocabulary | registration | Duplicate key |
| 12 | Register an attribute category | registration | Duplicate key |
| 13 | Register a residue kind | registration | No assignment expectation; no external notification declaration |
| 14 | Register a decision purpose | registration | Duplicate key |
| 15 | Declare an emergency access policy | `emergency_access_policy` | Fewer than the three mandatory obligations; any of them declared as advice |

Operation 2's refusal list is the design in compressed form. Three of its refusals will be resisted.

The refusal of a first applicable combining algorithm removes the construct most used for expressing a policy with an ordered fall through, and section 13.3 records the cost.

The refusal of a condition restating a `Part 2` constraint requires a policy author to obtain a verdict as an attribute rather than writing the predicate, which is more work and produces a constraint with an authority, a statement and a verdict record.

The refusal of an obligation with no authority requires somebody to say on what basis an instruction is imposed on another component. That is the right question and it is one nobody currently asks.

Operation 7 is worth noting. Withdrawing a policy version does not reach decisions already returned under it, per section 3.12, so the withdrawal must produce an exposure report enumerating the outstanding valid decisions. An implementation that treats withdrawal as immediately effective has misdescribed what it did.

**P7-4.5 (MUST) Preconditions checked at recording.** An implementation must check every precondition in the table above at the moment of recording, must record the outcome of each check, and must not defer a check to evaluation.

**P7-4.6 (MUST) Whole policy version in one operation.** An implementation must accept the whole structure of a policy version in a single operation and must record it atomically.

**P7-4.7 (MUST) Approval recorded, never granted.** An implementation must not provide an operation that approves a policy version and must provide only the recording of an approval obtained from `Part 1`.

**P7-4.8 (MUST) Withdrawal produces an exposure report.** An implementation must enumerate every outstanding valid decision at the moment a policy version is withdrawn from evaluation and must record the enumeration with the withdrawal.

**P7-4.9 (MUST) Analysis performed before evaluation.** An implementation must perform the analyses of section 6.8 that the policy's form admits before evaluating any request against it, and must record the results including those that could not be performed.

**P7-4.10 (MUST) Refused versions retained.** An implementation must retain every refused policy version with its per check outcomes and must be able to report refusals by author and by failed precondition.

### 4.3 Deciding operations

| # | Operation | Records | Principal refusals |
| --- | --- | --- | --- |
| 16 | Decide | `decision_request`, `evaluation_run`, attribute values and absences, condition evaluations, element results, combination steps, `decision`, obligations, advice, pins | No decision instant; no authentication reference; unregistered operation or purpose; unregistered enforcement point; an attribute beyond its declared staleness; a required pin unobtainable |
| 17 | Decide as a batch | as above per request, plus a batch record | As above |
| 18 | Reproduce a recorded decision | a new run linked to the original, and a divergence record | Original unknown; a pinned attribute value no longer obtainable |
| 19 | Explain a decision | an access record | Decision unknown |
| 20 | Simulate under a proposed policy version | a run marked non authoritative | Caller not authorised for the purpose |
| 21 | Assess a delegation | `delegation_assessment` | No chain supplied or obtainable |
| 22 | Record an emergency justification | `emergency_access_record` | No justification; not under an emergency policy |

Operation 20 exists for the reason `Part 2` operation 25 and `Part 5` operation 21 exist: policy authors need to try a policy before it is approved, and the alternative to providing it is that they will do so in a copy of the engine with none of the recording. The run is marked non authoritative, the marking is not removable, and clause P7-4.15 forbids acting on the result.

Operation 20 is also the operation that would have found the 2031 finding in the worked demonstration before it happened: running a proposed policy over recorded requests and reporting the coverage, the not applicable population and the capability mismatches it would produce. That is the most useful thing a policy decision point can do before a policy is adopted and very little offers it.

**P7-4.11 (MUST) Pins recorded before returning.** An implementation must durably record the pin set and every attribute value of an evaluation before returning any decision from it.

**P7-4.12 (MUST) Reproduction available.** An implementation must provide operation 18 and must be able to attempt reproduction of any decision within its retained history.

**P7-4.13 (MUST) Reproduction failure recorded, not hidden.** An implementation must record a non result where a pinned attribute value cannot be obtained during reproduction and must not substitute a current value.

**P7-4.14 (MUST) Simulation over recorded requests available.** An implementation must permit operation 20 to be run over the recorded requests of past decisions, and must report the coverage, the not applicable population, the indeterminate population and the capability mismatches the proposed policy would produce.

**P7-4.15 (MUST NOT) No action on a non authoritative run.** An implementation must mark every simulation non authoritative irremovably, must refuse to include it in an evidence package as a decision, and must declare that its outcome must not be acted upon.

**P7-4.16 (MUST) Batch decides per request.** An implementation must produce a separate decision for each request in a batch, must record each with its own attributes and pins, and must not share an attribute value across requests without recording that it did.

**P7-4.17 (MUST) Explanation assembled, not recomputed.** An implementation must assemble every explanation from the records of the evaluation and must not recompute a decision in order to explain it.

### 4.4 Enforcement reporting operations

| # | Operation | Records | Principal refusals |
| --- | --- | --- | --- |
| 23 | Report enforcement | `enforcement_report`, obligation outcomes, withholding records | Decision unknown; reporting point not the point the decision was returned to; an obligation outcome requiring residue with none supplied |
| 24 | Report an obligation outcome | `obligation_outcome`, `obligation_residue` | As above |
| 25 | Assign a residue | `residue_assignment` | No owner; no authorisation |
| 26 | Discharge a review obligation | discharge record | No discharging act; no actor |

Operation 23 is the operation this component cannot compel and cannot do without. Its provision is what makes the enforcement side of the record possible at all, and clause P7-4.19 requires it to be available to every registered enforcement point without a further authorisation barrier, on the ground that a barrier to reporting is a barrier to the record.

**P7-4.18 (MUST) Report accepted only from the recipient.** An implementation must accept an enforcement report only from the enforcement point to which the decision was returned and must record a refusal where another point reports.

**P7-4.19 (MUST) Reporting unobstructed.** An implementation must make the reporting operation available to every registered enforcement point without requiring a further authorisation for the report itself, and must record the report even where it discloses an under application.

**P7-4.20 (MUST) Residue required with the outcome.** An implementation must refuse an obligation outcome requiring residue without at least one residue record.

**P7-4.21 (MUST) Late reports accepted and marked.** An implementation must accept an enforcement report received after a declared interval, must mark it late, and must not discard it.

**P7-4.22 (MUST NOT) No report as a decision amendment.** An implementation must not alter a recorded decision on receipt of an enforcement report.

### 4.5 Reading operations

| # | Operation | Returns |
| --- | --- | --- |
| 27 | Read a named projection | The projection of section 3.16 |
| 28 | Get a decision | The decision with its request, attributes, condition results, combination steps and obligations |
| 29 | Get an explanation | The assembled explanation of a decision |
| 30 | Get a policy version | The whole structure with its analysis results |
| 31 | Resolve a policy as of a time | The version in force, with its approval and authority status |
| 32 | Export an evidence package | The package of section 8.6 |

**P7-4.23 (MUST) Times required on temporal resolution.** An implementation must require both an application time and a knowledge time for operation 31 and must not default either.

**P7-4.24 (MUST NOT) No partial decision record.** An implementation must return a complete decision record from operation 28 or refuse, and must not return a subset without stating what was omitted and why.

**P7-4.25 (MUST) Enforcement state returned with every decision.** An implementation must return, with every decision, whether an enforcement report was received and what it said, or that none was.

### 4.6 What a caller may and may not assume

**P7-4.26 (MUST) Caller obligations declared.** An implementation must document, for every operation, which of the assumptions below the caller may make.

A caller may assume that a returned decision was produced by the recorded policy versions over the recorded attributes, that every obligation attached is one the requesting enforcement point declared it can discharge, that a not applicable decision means no policy addressed the request, that an indeterminate decision carries the set of decisions it could have been, and that the decision is reproducible from its pins.

A caller may not assume that a permit means the operation may proceed, since the obligations must be discharged first and the reviewed standard's rule makes an undischargeable obligation a deny. A caller may not assume that a decision remains valid, since it carries a not valid after instant. A caller may not assume that a deny reflects a policy, since a collapsing algorithm may have produced it from a not applicable and the concealed outcome says so. A caller may not assume that an attribute was current, since staleness is bounded per attribute and the bound may be hours. A caller may not assume that an absent attribute was treated as false, since it makes the condition indeterminate. And a caller may not assume that this component knows whether any earlier decision was enforced.

**P7-4.27 (MUST NOT) No permit as permission to proceed.** An implementation must not describe a permit as authorising an operation without stating that every obligation must be discharged first.

**P7-4.28 (MUST NOT) No deny without its provenance.** An implementation must return, with every deny produced by a collapsing algorithm, the outcome the collapse concealed.

### 4.7 Reads from other components

| Read | From | On unavailability |
| --- | --- | --- |
| Resolve a policy document version and its status | `Part 1` | Refuse the decision; do not evaluate an unresolvable policy version |
| Resolve a policy authority citation and its status | `Part 1` | Record `authority_status` as `UNRESOLVABLE`; do not refuse the decision |
| Obtain a classification, marking or distribution attribute | `Part 1` | Record the attribute absent; apply the declared absence semantics |
| Obtain a verdict attribute | `Part 2` | As above |
| Obtain a delegation chain | `Part 3` | Record the delegation `UNASSESSABLE`; return indeterminate |
| Obtain a concept definition for an attribute | `Part 4` | Refuse the decision where the attribute's meaning cannot be resolved |
| Obtain a business outcome attribute | `Part 5` | Record the attribute absent; apply the declared absence semantics |
| Obtain a process fact attribute | `Part 6` | As above |
| Record the decision as a determination | `Part 3` | Record the failure and retry; do not discard the decision |
| Obtain a reference set version for an attribute domain | `Part 10` | Record the attribute absent |

The pattern is deliberate and differs from `Part 5`'s. There, an unavailable eligibility report refused the decision, because without it the component did not know which candidates were admissible. Here, an unavailable attribute source does **not** refuse the decision: it makes the attribute absent, the condition indeterminate, and the decision extended indeterminate. That is the whole point of the three valued condition domain and the extended indeterminate value, and refusing instead would discard the information the extended value carries.

Two exceptions are stated. An unresolvable policy document version refuses, because evaluating a policy whose text cannot be obtained is evaluating nothing. And an unresolvable concept definition for an attribute refuses, because an attribute whose meaning cannot be established is not an attribute, on the same basis `Part 2` clause P2-4.24 refuses an unresolvable term.

**P7-4.29 (MUST) Declared unavailability behaviour.** An implementation must implement the unavailability behaviour of the table above for every read and must record which behaviour it took.

**P7-4.30 (MUST NOT) No substitution on unavailability.** An implementation must not substitute a cached, default, current or successor version of any artifact in the table above, other than by the declared absence semantics of the attribute.

**P7-4.31 (MUST) Attribute unavailability yields indeterminate, not deny.** An implementation must treat an unavailable attribute source as making the attribute absent and must not return deny on that ground.

**P7-4.32 (MUST) Ledger recording failure does not lose the decision.** An implementation must retain its own decision where recording the determination with `Part 3` failed, must record the failure, and must be able to report every decision not yet recorded there.

### 4.8 Events emitted

The envelope carries at minimum an event identity, a type from the registered set, the knowledge time assigned by this component, the decision or policy concerned, the actor, a correlation reference, a schema reference and a digest over the event body.

The minimum event set. An implementation may emit more.

Policy version recorded. Policy version refused. Policy analysis recorded. Policy analysis not performed. Policy version withdrawn from evaluation. Policy authority drift observed. Policy approval unresolvable. Attribute declared. Enforcement point registered. Enforcement point capability mismatch detected. Obligation kind registered. Decision requested. Decision produced. Permit produced. Deny produced. Not applicable produced. Indeterminate produced. Extended indeterminate recorded. Decision refused for stale attribute. Attribute absent in an evaluation. Declared default applied for an absent attribute. Condition indeterminate. Collapsing algorithm applied. Only one applicable returned indeterminate on multiplicity. Undischargeable obligation produced a deny. Obligation attached. Withholding obligation attached. Delegation assessed. Delegation unassessable. Emergency access granted. Emergency review discharged. Emergency review overdue. Enforcement report received. Enforcement report late. Enforcement applied less restrictively. Enforcement applied after expiry. Obligation outcome recorded. Obligation fulfilment failed. Obligation fulfilment not reported beyond an age. Permit with an unfulfilled obligation. Residue recorded. Residue assigned. Residue unassigned beyond an age. Restriction applied without marking. Revocation exposure computed. Decision reproduced. Decision diverged. Simulation performed. Evidence package exported.

Five of these are the operationally decisive ones and are the least likely to exist in an implementation that has not read this part.

**Not applicable produced** must be emitted per decision, because it is the raw material of the coverage measure and because an implementation returning deny in its place emits nothing.

**Permit with an unfulfilled obligation** must be emitted per decision, because it is the population of operations that under the reviewed standard's own rule should not have proceeded.

**Enforcement applied less restrictively** must be emitted per report, because it is the only signal that an enforcement point is not doing what it was told.

**Restriction applied without marking** must be emitted per report, because it is the failure that destroys the withheld distinction four other parts depend on.

**Obligation fulfilment not reported beyond an age** must be emitted, because the ordinary case for an unverifiable obligation is silence and silence produces no event otherwise.

**P7-4.33 (MUST) Minimum event set.** An implementation must emit an event for every member of the set above and must register any additional type under section 9.9.

**P7-4.34 (MUST) Envelope minimum.** An implementation must include every envelope element named above in every event it emits.

**P7-4.35 (MUST NOT) No event in place of a record.** An implementation must not rely on event emission to satisfy any recording obligation of section 3 or section 8.

**P7-4.36 (MUST) Not applicable emitted individually.** An implementation must emit a distinct event for every not applicable decision and must not emit them only as counts.

**P7-4.37 (MUST) Unfulfilled permits emitted individually.** An implementation must emit a distinct event for every permit carrying an obligation whose outcome is other than fulfilled.

**P7-4.38 (MUST NOT) No suppression of adverse events.** An implementation must not provide a configuration that suppresses the emission of a refusal, a not applicable, an indeterminate, a collapsing algorithm application, an undischargeable obligation deny, an absent attribute, a declared default application, an under application, an application after expiry, an unfulfilled obligation, an unassigned residue, an unmarked restriction, an overdue emergency review or a decision divergence.
## 5. State model

### 5.1 Four state models, and one that belongs to somebody else

This part specifies four state machines, following the pattern the six prior parts establish. One property distinguishes this part: the most consequential state in the model is not this component's to hold.

The **registration state** of a policy version is owned here and describes whether this component will evaluate it.

The **force state** of a policy is not owned here. Whether a policy version is approved is a `Part 1` fact obtained by resolution, and whether it is in force at an application time follows from that approval and the effectivity of the document carrying it.

The **enforcement state** of a decision is owned by nobody in this standard. This component holds what it was told about it, and the default is that it was told nothing. Section 5.4 specifies it as a state whose value is frequently unknown, which is unusual and honest.

The **obligation fulfilment state** of an obligation instance has the same character and terminates in one of the six outcomes of section 3.10.

**P7-5.1 (MUST) Four models separate.** An implementation must not represent registration state, force state, enforcement state and obligation fulfilment state in one field and must not derive any of them from a stored value.

**P7-5.2 (MUST) States are projections.** An implementation must compute every state in this section from recorded rows alone.

**P7-5.3 (MUST NOT) No force state held.** An implementation must not hold, cache beyond a declared validity period, or assert the approval or force state of a policy version.

**P7-5.4 (MUST) Unknown enforcement state representable.** An implementation must represent the enforcement state of a decision for which no report was received as unknown and must not represent it as any other value.

### 5.2 Registration state of a policy version

States:

`DRAFT`. The structure exists and is incomplete. Readable, marked, and never evaluated.

`CHECKING`. The preconditions of operation 2 are being applied.

`REGISTERED`. Every precondition passed. The version is evaluable subject to approval and effectivity.

`REFUSED`. A precondition failed. Retained, never evaluable.

`SUSPENDED`. Registered and a pinned dependency has since become unobtainable: an attribute declaration, a concept definition, a registered obligation kind or a member policy version. Not evaluable. A statement about the component rather than about the policy.

`SUPERSEDED`. A later version exists. Remains evaluable for a request whose instants resolve to it.

`WITHDRAWN`. Registration revoked deliberately, with an authorisation and a reason, on the ground that the version should not have been registered.

Transitions:

| From | To | Trigger | Requires |
| --- | --- | --- | --- |
| `DRAFT` | `CHECKING` | Registration requested | Complete structure |
| `CHECKING` | `REGISTERED` | All checks passed | Analyses recorded where the form admits them |
| `CHECKING` | `REFUSED` | Any check failed | Recorded reason per failed check |
| `REFUSED` | `CHECKING` | Registration requested again | A new structure, that is, a new version |
| `REGISTERED` | `SUSPENDED` | A pinned dependency became unobtainable | Recorded dependency |
| `SUSPENDED` | `REGISTERED` | The dependency became obtainable | Analyses re run |
| `REGISTERED` | `SUPERSEDED` | A later version registered | Identity of the successor |
| `REGISTERED`, `SUPERSEDED` | `WITHDRAWN` | Deliberate revocation | Authorisation, reason, exposure report |
| `WITHDRAWN` | `REGISTERED` | Reinstatement | Authorisation, reason, analyses re run |

`SUSPENDED` matters more here than in the prior parts because of what happens next. A suspended policy version is not evaluated, so requests it would have addressed now match no policy, so they return **not applicable**, so an enforcement point applying a fail closed default denies them. A suspension therefore presents to users as a widespread denial with no policy change, and clause P7-5.8 requires the condition to be emitted and reported so that the cause is findable in minutes rather than hours.

`WITHDRAWN` requires an exposure report, per clause P7-4.8, because withdrawal does not reach decisions already returned.

**P7-5.5 (MUST) Enumerated states only.** An implementation must represent the registration state of a policy version as exactly one member of the set above.

**P7-5.6 (MUST) Enumerated transitions only.** An implementation must not effect a transition absent from the table above.

**P7-5.7 (MUST) State is a projection.** An implementation must compute registration state from recorded rows and must not hold it as an updatable field.

**P7-5.8 (MUST) Suspension emitted and reported with its consequence.** An implementation must emit an event and record a signal when a policy version enters `SUSPENDED`, and must report the request classes that will consequently return not applicable.

**P7-5.9 (MUST) Refused versions retained and countable.** An implementation must retain every refused version with its per check outcomes and must be able to report refusals by author and by failed precondition.

**P7-5.10 (MUST) Withdrawal authorised, reasoned and exposure reported.** An implementation must record an authorisation, a reason and an exposure report for every transition to `WITHDRAWN`.

**P7-5.11 (MUST) Superseded versions remain evaluable.** An implementation must continue to evaluate a version in `SUPERSEDED` for a request whose instants resolve to it and must not substitute the successor.

**P7-5.12 (MUST NOT) No evaluation outside evaluable states.** An implementation must not evaluate a policy version whose registration state is not `REGISTERED` or `SUPERSEDED`, except under operation 20 of section 4.3.

**P7-5.13 (MUST NOT) No state change from the passage of time.** An implementation must not transition registration state as a consequence of a date passing and must effect every transition by a recorded act.

### 5.3 Evaluation run state

States: `REQUESTED`, `RESOLVING_POLICY`, `GATHERING_ATTRIBUTES`, `EVALUATING`, `COMBINING`, `ATTACHING_OBLIGATIONS`, `COMPLETED`, `REFUSED`, `ABANDONED`.

| From | To | Trigger |
| --- | --- | --- |
| `REQUESTED` | `RESOLVING_POLICY` | Request accepted and well formed |
| `REQUESTED` | `REFUSED` | Request malformed, unregistered operation, purpose, or enforcement point, or no decision instant |
| `RESOLVING_POLICY` | `GATHERING_ATTRIBUTES` | Root policy version resolved and evaluable |
| `RESOLVING_POLICY` | `REFUSED` | Policy document version unresolvable |
| `GATHERING_ATTRIBUTES` | `EVALUATING` | Every attribute a matched target requires attempted |
| `GATHERING_ATTRIBUTES` | `REFUSED` | An attribute beyond its declared staleness, or a concept definition unresolvable |
| `EVALUATING` | `COMBINING` | Every applicable element evaluated |
| `COMBINING` | `ATTACHING_OBLIGATIONS` | The root decision produced |
| `ATTACHING_OBLIGATIONS` | `COMPLETED` | Obligations and advice attached, or a deny produced by an undischargeable obligation |
| any | `ABANDONED` | Loss of the executing process |

Two properties of the machine are worth noting.

**Attribute gathering precedes evaluation and does not refuse on absence.** An unobtainable attribute makes the attribute absent and the run continues, per clause P7-4.31. The two refusals in that state are staleness, which is a positive finding that a value must not be relied upon, and an unresolvable concept, which means the attribute has no established meaning.

**Obligation attachment can change the decision.** A permit that would attach an obligation the enforcement point cannot discharge becomes a deny, per clause P7-3.62, and the transition occurs in `ATTACHING_OBLIGATIONS` rather than in `COMBINING`. Placing it there is deliberate: the decision the policy produced and the decision the obligations forced are two facts and clause P7-5.17 requires both to be recorded.

**P7-5.14 (MUST) Enumerated run states.** An implementation must represent every evaluation run as exactly one member of the set above.

**P7-5.15 (MUST) Attributes gathered before evaluation.** An implementation must attempt every attribute a matched target requires before evaluating any condition that reads it.

**P7-5.16 (MUST) Absence does not refuse the run.** An implementation must continue an evaluation where an attribute could not be obtained and must apply the declared absence semantics.

**P7-5.17 (MUST) Policy decision and obligation forced decision both recorded.** An implementation must record the decision the combining algorithms produced and, where an undischargeable obligation changed it, the decision returned, as two values.

**P7-5.18 (MUST) Abandonment detected and recorded.** An implementation must transition a run whose executing process is lost to `ABANDONED` within a declared interval, must declare the interval, and must not return a decision from an abandoned run.

**P7-5.19 (MUST) Terminal states are terminal.** An implementation must not transition out of `COMPLETED`, `REFUSED` or `ABANDONED`.

### 5.4 Enforcement state of a decision

This is the machine whose value this component does not control, and specifying it as a state rather than as an absence is the substance of section 3.2.

States: `RETURNED`, `EXPIRED_UNREPORTED`, `REPORTED_APPLIED`, `REPORTED_MORE_RESTRICTIVE`, `REPORTED_LESS_RESTRICTIVE`, `REPORTED_NOT_APPLIED`, `REPORTED_AFTER_EXPIRY`, `REPORTED_UNKNOWN`.

| From | To | Trigger |
| --- | --- | --- |
| decision produced | `RETURNED` | The decision was returned to the enforcement point |
| `RETURNED` | any `REPORTED_*` | An enforcement report received |
| `RETURNED` | `EXPIRED_UNREPORTED` | The not valid after instant passed with no report |
| `EXPIRED_UNREPORTED` | any `REPORTED_*` | A late report received |

`EXPIRED_UNREPORTED` is the state most decisions in most estates will occupy, and it is not a failure. It records that the decision's validity elapsed and nothing came back. Its population is the honest measure of how much of an organisation's access control is unverified, and clause P7-5.22 requires the count to be a standing signal rather than an on demand query, because a value that depends on absence is a value nobody requests.

`REPORTED_UNKNOWN` is the state where an enforcement point reported and could not say what it did, which happens where it crashed between deciding and acting. It is distinguished from `EXPIRED_UNREPORTED` because a report of ignorance is a different fact from silence: somebody looked and could not tell.

There is no transition to a state meaning the decision was not enforced and definitely not acted upon, because no report can establish that. `REPORTED_NOT_APPLIED` is an enforcement point's claim, and clause P7-5.24 requires it to be recorded as a claim.

**P7-5.20 (MUST) Enumerated enforcement states.** An implementation must represent the enforcement state of every decision as exactly one member of the set above.

**P7-5.21 (MUST) Expiry without report is a state, not a fault.** An implementation must transition a decision to `EXPIRED_UNREPORTED` on the passing of its not valid after instant with no report and must not record it as an error.

**P7-5.22 (MUST) Unreported population standing.** An implementation must produce the unreported population continuously rather than on demand and must report it by enforcement point.

**P7-5.23 (MUST) Late reports transition the state.** An implementation must accept a report received after expiry, must transition the state, and must mark the report late.

**P7-5.24 (MUST) Reports recorded as claims.** An implementation must record every enforcement state derived from a report as derived from that party's claim and must not represent it as established.

**P7-5.25 (MUST NOT) No enforcement state inferred.** An implementation must not transition an enforcement state on any basis other than a received report or the passing of the validity instant.

### 5.5 Obligation fulfilment state

States: `ATTACHED`, `REPORTED`, `EXPIRED_UNREPORTED`, `RESIDUE_RECORDED`, `RESIDUE_ASSIGNED`, `REVIEW_RAISED`, `REVIEW_DISCHARGED`.

These are not mutually exclusive in the way the other machines' states are, and clause P7-5.26 requires them to be held as independent appended facts, on the pattern `Part 3` section 5.1 and `Part 5` section 5.4 establish.

The sequence that matters is `ATTACHED` to `EXPIRED_UNREPORTED` to nothing further, which is what happens to an unverifiable obligation and is the ordinary case. The sequence `REPORTED` with an outcome other than fulfilled, then `RESIDUE_RECORDED`, then `RESIDUE_ASSIGNED`, then `REVIEW_RAISED`, then `REVIEW_DISCHARGED` is the complete path and clause P7-5.29 requires every step to be a recorded act.

**P7-5.26 (MUST) States held independently.** An implementation must hold each obligation fulfilment state as an independent appended fact and must not represent them as one status field.

**P7-5.27 (MUST) Unreported obligation is a state.** An implementation must transition an obligation instance to `EXPIRED_UNREPORTED` where no outcome was reported by the decision's expiry and must record the outcome as `FULFILMENT_NOT_REPORTED`.

**P7-5.28 (MUST) Review raised on the enumerated conditions.** An implementation must raise a review for every obligation outcome other than fulfilled and not applicable, per clause P7-3.71.

**P7-5.29 (MUST) Every step a recorded act.** An implementation must record each transition as an act with an actor and, where the transition is an assignment or a discharge, an authorisation.

**P7-5.30 (MUST NOT) No discharge without an act.** An implementation must not treat the closure of a task in another component as discharging a review and must require a recorded discharging act naming an actor.
## 6. Execution semantics

### 6.1 Determinism and reproducibility

Two properties, distinguished as in `Part 2` section 6.1.

**Determinism.** One evaluation, run twice over the same policy versions and the same attribute values, yields the same decision, the same obligations and the same validity.

**Reproducibility.** A decision made in 2028 can be evaluated again in 2035, from its recorded policy versions and attribute values, and yield the same decision.

Both are achievable here, unlike in `Part 6`, because this component's inputs are attributes and attributes are pinnable. What is not achievable is that the attribute values would be the same if fetched again, and that is precisely why they are recorded rather than re fetched. A reproduction that re read the attributes would be a different decision about a different state of the world.

Four sources of non determinism must be controlled and the last two are specific to policy evaluation.

The policy changed, which pinning prevents. The attribute values changed, which recording prevents.

**Condition evaluation order.** Where a condition is a conjunction and one operand is indeterminate, the result depends on the tables of `Part 2` section 6.2 and not on the order of evaluation, because those tables are order independent. Short circuiting is therefore sound for the truth value and changes which attributes were read, so clause P7-6.4 requires the read set to be recorded as read rather than as required.

**Attribute bag ordering.** Where an attribute is multi valued, a function over the bag may depend on its order. Clause P7-6.5 requires a declared total order.

**P7-6.1 (MUST) Identical inputs yield identical decisions.** An implementation must return the same decision, obligations, advice and validity for two evaluations over the same policy versions and attribute values.

**P7-6.2 (MUST) Reproduction reads recorded values.** An implementation must, during a reproduction, read every recorded attribute value rather than re fetching it, and must record a non result where a recorded value cannot be obtained.

**P7-6.3 (MUST) Condition semantics from Part 2.** An implementation must evaluate every condition under the three valued connective semantics of `Part 2` section 6.2 and must not adopt a different treatment of the indeterminate value.

**P7-6.4 (MUST) Attributes recorded as read, not as required.** An implementation must record which attributes it in fact read and must distinguish them from those a matched target could have required but which short circuiting made unnecessary.

**P7-6.5 (MUST) Bag order total and declared.** An implementation must impose a declared total order on every multi valued attribute and must not permit a function over a bag to depend on an undeclared order.

**P7-6.6 (MUST) Exact arithmetic for comparison.** An implementation must use an exact decimal arithmetic for every numeric comparison in a condition and must not use binary floating point, on the same basis as `Part 2` clause P2-6.4.

**P7-6.7 (MUST) Collation pinned.** An implementation must pin the collation and the Unicode version used for every string comparison in a condition.

### 6.2 The evaluation algorithm

Normative in its ordering and in its outcomes; not normative in its structure as code.

```
decide(request):
  1  if request malformed, or operation, purpose or enforcement point unregistered,
     or no decision instant, or no authentication reference:
                                              return REFUSED(with the code)
  2  root = resolve(request.root_policy_reference, decision_instant, knowledge_instant)
     if unresolvable:                          return REFUSED(POLICY_UNRESOLVABLE)
     if registration_state(root) not in {REGISTERED, SUPERSEDED}:
                                              return REFUSED(POLICY_NOT_EVALUABLE)
     record approval status and authority status
  3  pin root, every member version, every attribute declaration, every registered
     obligation kind, the operation vocabulary and the collation
  4  matched = elements whose target matches the request      // targets read attributes
     record every element whose target did not match as not applicable
  5  for each attribute a matched target or condition requires:
        attempt to obtain from its declared source
        if obtained:
             if staleness(value) > declared maximum:  return REFUSED(ATTRIBUTE_STALE)
             record attribute_value with source, digest, as_of, obtained
        else:
             record attribute_absence with the reason
             apply declared absence semantics:
                INDETERMINATE      -> conditions reading it are indeterminate
                TREAT_AS_EMPTY_BAG -> the bag is empty
                DECLARED_DEFAULT   -> the default value, recorded as defaulted
  6  for each matched rule, in any order:
        t = evaluate(condition) in the three valued domain of Part 2 section 6.2
        record condition_evaluation
        if t == TRUE:            element_result = effect          // PERMIT or DENY
        if t == FALSE:           element_result = NOT_APPLICABLE
        if t == INDETERMINATE:   element_result = INDETERMINATE{effect}
  7  for each policy and policy set, innermost first:
        result = apply(combining_algorithm, member results)
        record combination_step with the algorithm, the inputs and the result
        if the algorithm is collapsing:
             record the concealed outcome                        // per clause P7-3.54
  8  policy_decision = the root result
  9  if request carries a delegation assertion:
        assessment = assess_delegation(request, policy_version)
        if assessment is UNASSESSABLE:  policy_decision = INDETERMINATE{DP}
        if assessment is any INVALID:   policy_decision = DENY
        record delegation_assessment
 10  obligations = obligation declarations of every element that contributed,
        whose fulfilment_condition matches policy_decision
     resolve every parameter from recorded attribute values
     if any obligation kind is not in the declared capability set of the
        requesting enforcement point:
             returned_decision = DENY                            // per clause P7-3.62
             record the undischargeable obligation and both decisions
     else: returned_decision = policy_decision
 11  advice = advice declarations similarly matched
 12  validity = declared validity of the root policy version
     not_valid_after = decision_instant + validity
 13  record decision, obligation instances, advice instances, pins, counts
     record the determination with Part 3; emit events
 14  return returned_decision, obligations, advice, validity, extended value
```

Five properties of the algorithm are decisions rather than derivations.

**Step 4 records the elements that did not match.** Without that record, a not applicable decision cannot be distinguished from an evaluation in which forty policies were consulted and none addressed the request, and the coverage measure of section 6.8 has no denominator.

**Step 5 refuses on staleness and continues on absence.** These are the two different responses to two different conditions, and section 4.7 states why: a stale value is a positive finding that a fact must not be relied upon; an absent value is an absence the three valued domain exists to carry.

**Step 6 evaluates rules in any order.** No combining algorithm in the closed set of section 3.8 makes the decision depend on order, so the order cannot matter, and clause P7-6.13 requires the property to be demonstrable.

**Step 9 places delegation assessment after policy evaluation and before obligations.** An invalid delegation produces a deny regardless of what the policy said, because a principal not entitled to act on another's behalf is not the principal the policy addressed. An unassessable delegation produces the fully extended indeterminate, because the decision could have been either.

**Step 10 can change the decision the policy produced**, and both are recorded, per clause P7-5.17. This is the reviewed standard's rule applied structurally: the obligations are computed from the policy decision and may then force a deny.

**P7-6.8 (MUST) Algorithm order.** An implementation must perform the steps above in the order given and must not attach an obligation before the policy decision is produced.

**P7-6.9 (MUST) Non matching elements recorded.** An implementation must record every policy version whose target did not match a request.

**P7-6.10 (MUST) Staleness refuses, absence continues.** An implementation must refuse a decision resting on a stale attribute and must continue an evaluation where an attribute is absent.

**P7-6.11 (MUST) Element results recorded individually.** An implementation must record the result of every matched rule, policy and policy set, with the three valued condition result that produced it.

**P7-6.12 (MUST) Combination steps recorded with inputs.** An implementation must record every application of a combining algorithm with the member results it combined.

**P7-6.13 (MUST) Order independence demonstrable.** An implementation must be able to demonstrate, for a policy version, that its decision is unaffected by the order in which members were evaluated, by evaluating a recorded request in at least two orders and comparing, and must record the result as a `policy_analysis`.

**P7-6.14 (MUST) Delegation assessed after policy and before obligations.** An implementation must perform the delegation assessment at step 9 and must record its effect on the decision.

**P7-6.15 (MUST) Both decisions recorded where obligations forced a change.** An implementation must record the policy decision and the returned decision as two values wherever an undischargeable obligation changed the outcome.

### 6.3 The extended indeterminate

An indeterminate decision says the evaluation could not be completed. The extended value says what it could have been, and the difference is what makes a fail safe response principled rather than arbitrary.

Three values. The table is normative.

| Value | Means | The enforcement point knows |
| --- | --- | --- |
| `INDETERMINATE_DENY` | Had the indeterminacy not arisen, the decision could only have been deny or not applicable. | Proceeding is not defensible. |
| `INDETERMINATE_PERMIT` | It could only have been permit or not applicable. | Denying is safe; proceeding on a declared policy is defensible. |
| `INDETERMINATE_DENY_PERMIT` | It could have been either. | Nothing. Only a declared default response applies. |

The values are computed rather than asserted, and the computation follows from the algorithms. A rule whose effect is deny and whose condition is indeterminate yields `INDETERMINATE_DENY`; one whose effect is permit yields `INDETERMINATE_PERMIT`; a combining algorithm over both yields `INDETERMINATE_DENY_PERMIT`. Clause P7-6.17 requires the computation and clause P7-6.18 forbids defaulting to the fully extended value, which is the tempting simplification and which discards the information.

`Part 5` section 13.6 records that this part's predecessor considered adopting extended indeterminacy for eligibility and did not, and that the omission may have been a mistake. This part adopts it, and section 13.7 notes the inconsistency between two adjacent parts on the same question.

**P7-6.16 (MUST) Extended value on every indeterminate.** An implementation must record one of the three values above on every indeterminate decision and must not return an indeterminate without one.

**P7-6.17 (MUST) Extended value computed.** An implementation must compute the extended value from the effects of the elements whose evaluation was indeterminate and must not accept it as an input.

**P7-6.18 (MUST NOT) No defaulting to the widest value.** An implementation must not record `INDETERMINATE_DENY_PERMIT` where the computation establishes a narrower value.

**P7-6.19 (MUST) Cause recorded with the extended value.** An implementation must record, with every indeterminate decision, which attribute absences, unavailable sources, unassessable delegations or condition faults produced the indeterminacy.

**P7-6.20 (MUST NOT) No indeterminate as a deny.** An implementation must not return deny in place of an indeterminate and must not offer a configuration by which it does.

### 6.4 Obligation resolution

```
resolve_obligations(contributing_elements, decision, enforcement_point):
  1  candidates = obligation declarations of every element that contributed
        to the decision, whose fulfilment_condition matches the decision
  2  for each candidate:
        resolve every parameter from recorded attribute values
        if a parameter cannot be resolved:
             the obligation is unresolvable; record it; treat as undischargeable
  3  capability = declared obligation capability set of enforcement_point
  4  undischargeable = candidates whose kind is not in capability,
        plus the unresolvable ones
  5  if undischargeable is not empty and decision is PERMIT:
        return DENY, with undischargeable recorded          // per clause P7-3.62
  6  if undischargeable is not empty and decision is DENY:
        return DENY, with undischargeable recorded and a review raised
  7  order = declared obligation order where an ordered combining algorithm applies,
        else the declared canonical order of the implementation
  8  return decision, obligations in order, advice
```

Two properties are decisions.

**Step 5 turns a permit into a deny and step 6 does not turn a deny into anything.** A deny with an undischargeable obligation is still a deny, and the operation does not proceed, so the safety property holds. What is lost is the obligation, which may have been a notification or a log entry attached to the refusal, so clause P7-6.24 requires a review to be raised rather than the condition to be silently tolerated.

**Step 2 treats an unresolvable parameter as making the obligation undischargeable.** An obligation to notify a party whose address could not be resolved is an obligation that cannot be performed, and treating it as dischargeable because its kind is supported is how a permit proceeds on an obligation that was never going to work.

**P7-6.21 (MUST) Obligations from contributing elements only.** An implementation must attach obligations only from elements that contributed to the decision and must record which elements contributed.

**P7-6.22 (MUST) Parameters resolved from recorded values.** An implementation must resolve every obligation parameter from recorded attribute values and must treat an unresolvable parameter as making the obligation undischargeable.

**P7-6.23 (MUST) Capability checked before returning.** An implementation must check every obligation kind against the requesting enforcement point's declared capability set before returning a decision.

**P7-6.24 (MUST) Undischargeable obligation on a deny raises a review.** An implementation must raise a review where a deny carried an undischargeable obligation and must not silently discard the obligation.

**P7-6.25 (MUST) Obligation order declared.** An implementation must declare the order in which it returns obligations where no ordered combining algorithm applies and must not vary it between evaluations.

### 6.5 Clocks

Three clocks, on the same basis as `Part 1` section 3.1.

**P7-6.26 (MUST) Knowledge time assigned by this component.** An implementation must assign every knowledge time from its own clock and must refuse a request supplying one.

**P7-6.27 (MUST NOT) No occurrence time assignment.** An implementation must not assign an occurrence time and must record every one as asserted by an actor or reported by an enforcement point.

**P7-6.28 (MUST NOT) No ambient clock in a condition.** An implementation must not admit a condition that reads a clock and must require every temporal comparison to be against the decision instant or an environment attribute supplied in the request.

**P7-6.29 (MUST) Instants in a declared scale.** An implementation must record every instant in a declared time scale with a declared offset.

**P7-6.30 (MUST) Staleness computed from recorded instants.** An implementation must compute an attribute's staleness from its recorded as of instant and the decision instant and must not compute it from a clock read at evaluation.

**P7-6.31 (MUST) Validity computed from the decision instant.** An implementation must compute the not valid after instant from the decision instant and the declared validity duration and must not compute it from a clock read at evaluation.

### 6.6 Idempotence

**P7-6.32 (MUST) Idempotence by key.** An implementation must return the originally recorded outcome for a repeated recording or reporting operation bearing an idempotence key already seen within its declared deduplication window.

**P7-6.33 (MUST) Deduplication window declared.** An implementation must declare its deduplication window as a duration and must state what happens to a key repeated after it.

**P7-6.34 (MUST NOT) No idempotence across differing payloads.** An implementation must refuse an operation bearing a seen key with a different payload.

**P7-6.35 (MUST) Repeated decisions recorded separately.** An implementation must record each evaluation of a request as a separate decision, whether or not an idempotence key was supplied, and must not return a cached decision as a new one without recording that it did.

### 6.7 Bounds

Three bounds are required: a **depth** bound on policy set nesting, a **breadth** bound on the elements evaluated in one request, and a **budget** on a declared resource. As in the five prior parts, the primary budget must be on a deterministic resource, because a budget on wall clock time makes the same request decidable on one day and not on another.

The consequence of exhausting a bound here is more serious than in most parts, because a truncated evaluation may not have reached the policy that would have denied. Clause P7-6.38 therefore requires a truncated evaluation to return indeterminate rather than a decision, with the fully extended value, since what it would have decided is unknown.

**P7-6.36 (MUST) Three bounds declared.** An implementation must declare a nesting depth bound, an element breadth bound and a budget, and must state the resource the budget bounds.

**P7-6.37 (MUST) Primary budget deterministic.** An implementation must make its primary budget a bound on a deterministic resource.

**P7-6.38 (MUST) Truncation yields the widest indeterminate.** An implementation must return `INDETERMINATE_DENY_PERMIT` where a bound was reached before every matched element was evaluated, must record the bound and the point of truncation, and must not return a decision.

**P7-6.39 (MUST NOT) No silent bound.** An implementation must not apply an undeclared bound and must not return a result without stating the bound that truncated it.

### 6.8 Static analysis: coverage, conflict and shadowing

Five properties of a policy version are worth knowing before it evaluates anything, and the first is the one that distinguishes an implementation of this part.

**Coverage.** The proportion of a declared request space for which some element's target matches. Its complement is the population that will return not applicable. Coverage is decidable over a finite declared request space and undecidable over an unbounded attribute domain, so the analysis requires the space to be declared, and clause P7-6.41 requires the declaration.

**Conflict.** Whether some request can produce both a permit and a deny from different elements. Conflict is not a defect: it is the ordinary condition that combining algorithms exist to resolve. What is worth reporting is a conflict resolved by a **collapsing** algorithm, where the resolution discards information, and a conflict resolved differently under two nestings, which the associativity requirement of clause P7-3.55 exists to prevent.

**Shadowing.** Whether some rule can never contribute to a decision, because every request matching its target is resolved by another element the algorithm prefers. A shadowed rule is dead policy that reviewers read as live, which is the same failure `Part 5` section 6.4 names as masking and `Part 6` reports for unreachable activities.

**Capability satisfiability.** Whether, for each registered enforcement point, every obligation the policy could attach is in that point's declared capability set. Where it is not, the policy will produce denies at that point which the policy author did not intend, per clause P7-3.63.

**Obligation reachability.** Whether every declared obligation can be attached by some request. An unreachable obligation is a control the organisation believes it has and does not.

`policy_analysis` records all five, the procedure version, the declared request space, the analyses not performed and why, and the knowledge time.

**P7-6.40 (MUST) Five analyses performed where decidable.** An implementation must perform coverage, conflict, shadowing, capability satisfiability and obligation reachability analysis over every policy version whose form admits each, and must record the results separately.

**P7-6.41 (MUST) Request space declared for coverage.** An implementation must require a declared request space for a coverage analysis, must record it with the result, and must record that coverage could not be computed where none is declared.

**P7-6.42 (MUST) Coverage reported as a proportion with its complement.** An implementation must report coverage as a proportion of the declared request space together with the request classes that fall outside it.

**P7-6.43 (MUST) Shadowed rules reported.** An implementation must report every rule that can never contribute to a decision and must include the count in the signals of section 8.5.

**P7-6.44 (MUST) Algebraic properties verified.** An implementation must verify that every combining algorithm it applies has the associativity and commutativity properties clause P7-3.55 records for it, and must record the verification.

**P7-6.45 (MUST) Unreachable obligations reported.** An implementation must report every declared obligation that no request could cause to be attached.

**P7-6.46 (MUST) Analyses not performed recorded with the reason.** An implementation must record, for every analysis it did not perform, that it was not performed and why.

**P7-6.47 (MUST NOT) No absence of finding as absence of fault.** An implementation must not report a policy version as complete in coverage, free of shadowing or capability satisfiable on the basis of an analysis that did not complete or was not performed.

**P7-6.48 (MUST NOT) No analysis at evaluation time.** An implementation must not perform a static analysis during an evaluation and must not vary a decision on the basis of an analysis result.

### 6.9 What this component may compute, and what it may not

It may compute: whether a target matches; the three valued value of a condition over recorded attributes; the result of a combining algorithm over member results; the extended indeterminate value; the obligation set and its parameters; the validity instant; the delegation assessment under a policy version; the five analyses of section 6.8; and every projection of section 3.16.

It may not compute: whether a business constraint holds, which is `Part 2`'s; which of several business outcomes to select, which is `Part 5`'s; what was in force at an application time, which is `Part 1`'s; the meaning of an attribute, which is `Part 4`'s; whether an operation occurred, which only an enforcement point can report; whether an obligation was fulfilled, likewise; whether an emergency justification was genuine, which clause P7-3.99 reserves; and whether the policy is the right policy, which is nobody's in this standard.

**P7-6.49 (MUST) Permitted computations only.** An implementation must not compute any determination allocated to another component by section 12 and must return the recorded value that component supplied.

**P7-6.50 (MUST NOT) No inference of an attribute.** An implementation must not compute, derive or assume an attribute value and must read every value from its declared source or record its absence.

**P7-6.51 (MUST NOT) No learning from decisions.** An implementation must not adjust a policy version, a target, a condition, a combining algorithm or a validity duration on the basis of observed decisions or enforcement reports, and must require every change to be a recorded policy version.

**P7-6.52 (MUST NOT) No assessment of policy fitness.** An implementation must not assert that a policy is appropriate, sufficient or well designed, and must report only the analyses of section 6.8 and the distributions of section 8.5.
## 7. Outcome and failure taxonomy

### 7.1 Why the taxonomy is the specification

This component produces four kinds of output and each has a characteristic way of being wrong that the output conceals.

A **decision** says whether an operation is authorised. It is wrong invisibly when a not applicable is returned as a deny, because the coverage gap then looks like a policy, and when an indeterminate is returned as a deny, because an inability to evaluate then looks like a refusal.

An **obligation set** says what must accompany the operation. It is wrong invisibly when it is attached to a permit an enforcement point cannot discharge, because the reviewed standard's rule then makes the permit a deny and the enforcement point may not have applied the rule.

An **obligation outcome** says whether the accompaniment happened. It is wrong invisibly whenever it is unrecorded, which is the ordinary case.

An **enforcement report** says what was done. It is wrong invisibly when its absence is read as compliance.

In all four the plausible, well formed output is the failure mode, and the taxonomy exists so that the qualification travels with the output.

### 7.2 The decision set

Seven members in five classes. The table is normative.

| Class | Member | Means |
| --- | --- | --- |
| Permit | `PERMIT` | Some element permitted and the combining algorithms resolved to permit. Obligations must be discharged first. |
| Deny | `DENY` | Some element denied and the algorithms resolved to deny. |
| Deny | `DENY_UNDISCHARGEABLE_OBLIGATION` | The policy resolved to permit and an obligation could not be discharged by the requesting enforcement point. |
| Not applicable | `NOT_APPLICABLE` | No element's target matched the request. **No policy addressed it.** |
| Indeterminate | `INDETERMINATE_DENY` | The evaluation could not complete and could only have resolved to deny or not applicable. |
| Indeterminate | `INDETERMINATE_PERMIT` | It could only have resolved to permit or not applicable. |
| Indeterminate | `INDETERMINATE_DENY_PERMIT` | It could have resolved either way. |
| Refusal | `REFUSED` | The component declined to evaluate the request. Carries a code. |

Five distinctions are load bearing.

**`NOT_APPLICABLE` against `DENY`.** This is the most important distinction in the part. A not applicable says nobody has said anything about this request; a deny says somebody has said no. Collapsing them is default deny, which is a correct and necessary **enforcement point** behaviour and a catastrophic **decision point** behaviour, because it makes the coverage gap invisible. An estate where a third of requests match no policy has policy coverage of two thirds, and if the decision point returns deny nobody can ever discover it. Clause P7-7.4 states it and clause P7-1.9 forbids the substitution.

**`DENY` against `DENY_UNDISCHARGEABLE_OBLIGATION`.** Both are denies and the operation does not proceed. The first is policy working. The second is a capability mismatch between a policy and an enforcement point, which is fixable and which section 6.8's analysis would have found in advance. Merging them means an estate accumulates denials attributed to policy that are in fact integration defects.

**The three indeterminate members against each other.** Section 6.3 states the value: they tell the enforcement point what the decision could have been, so a fail safe response can be principled. Merging them discards the only information that distinguishes a defensible fail open from a guess.

**Any indeterminate against `DENY`.** An indeterminate is a statement about the evaluation; a deny is a statement about the request. Returning the first as the second is the same collapse `Part 2` clause P2-1.6 forbids for verdicts and `Part 5` clause P5-7.24 forbids for selections, and it is forbidden here for the same reason: an inability becomes a finding.

**Any decision against `REFUSED`.** A refusal means the component did not evaluate. A caller that treats it as a deny will not correct the request.

**P7-7.1 (MUST) Closed decision set.** An implementation must return exactly one member of the table above from every request and must not return a value outside the set.

**P7-7.2 (MUST NOT) No additional members.** An implementation must not add a member and must express any additional distinction as a registered code within the `REFUSED` class.

**P7-7.3 (MUST) Extended value on every indeterminate.** An implementation must return one of the three indeterminate members and must not return an undifferentiated indeterminate.

**P7-7.4 (MUST) Not applicable returned as not applicable.** An implementation must return `NOT_APPLICABLE` where no element's target matched and must not substitute a deny under any configuration.

**P7-7.5 (MUST) Obligation forced deny distinguished.** An implementation must return `DENY_UNDISCHARGEABLE_OBLIGATION` where the policy resolved to permit and an obligation could not be discharged, and must record both decisions.

**P7-7.6 (MUST NOT) No mapping onto a permit and deny pair.** An implementation must not provide an interface that maps the seven members onto two values and must not document such a mapping as canonical.

**P7-7.7 (MUST NOT) No caller selected collapse.** An implementation must not offer a configuration by which a not applicable or an indeterminate is returned as a permit or a deny.

**P7-7.8 (MUST) Fail safe response is the enforcement point's.** An implementation must document that the response to a not applicable or an indeterminate is the enforcement point's declared policy and must not implement that response itself.

### 7.3 The decision envelope

Normative in content; serialisation unspecified.

The decision member and, for an indeterminate, the extended value with its cause. The policy decision where an obligation forced a different returned decision. The root policy version and every version evaluated, with the count of those that did not match. The approval status and the authority status. Every attribute read, with its source, digest and as of instant, and every attribute absent with its reason and the semantics applied. Every condition evaluated with its three valued result. Every combination step with its algorithm, inputs and result. The outcome a collapsing algorithm concealed. Every obligation with its kind, parameters, fulfilment condition and verifiability. Every advice. The delegation assessment where one was made. The emergency record where the decision was under an emergency policy. The validity duration and the not valid after instant. The enforcement point identity. The three clocks. Whether the run was a non authoritative simulation. The bound that truncated the evaluation where one did.

**P7-7.9 (MUST) Envelope completeness.** An implementation must include every element named above in every decision envelope it returns and records.

**P7-7.10 (MUST NOT) No envelope reduction.** An implementation must not omit an envelope element on the ground that a caller does not use it.

**P7-7.11 (MUST) Absent attributes in the envelope.** An implementation must include every absent attribute with its reason and the absence semantics applied, so that a caller can see how much of the decision rested on facts the component did not have.

**P7-7.12 (MUST) Verifiability in the envelope.** An implementation must state, for every obligation attached, whether its fulfilment is verifiable by this component.

### 7.4 Enforcement outcomes

Reported by an enforcement point, recorded here, and never inferred. Six members plus the unreported state of section 5.4.

| Member | Means |
| --- | --- |
| `APPLIED_AS_DECIDED` | The decision was applied and every obligation discharged. |
| `APPLIED_MORE_RESTRICTIVELY` | The enforcement point permitted less than the decision permitted. |
| `APPLIED_LESS_RESTRICTIVELY` | It permitted more: an obligation ignored, a local default applied over a not applicable, or an expired decision acted upon. |
| `NOT_APPLIED` | The decision was not applied and the operation did not proceed. |
| `APPLIED_AFTER_EXPIRY` | The decision was applied after its not valid after instant. |
| `ACTION_UNKNOWN` | The enforcement point reported and could not establish what it did. |

`APPLIED_MORE_RESTRICTIVELY` is safe and is not therefore uninteresting. An enforcement point systematically applying more restriction than policy requires is a source of denials attributed to policy that policy did not impose, and users experience it as an incoherent system. Clause P7-7.15 requires the population to be reportable for that reason.

`APPLIED_LESS_RESTRICTIVELY` is the member no enforcement point wants to report and the one this taxonomy exists to make reportable. Clause P7-4.19 removes the authorisation barrier to reporting for exactly this reason: a component that makes honest self reporting difficult will receive no honest self reports.

**P7-7.13 (MUST) Closed enforcement outcome set.** An implementation must record exactly one member of the table above for every enforcement report and must not accept a value outside the set.

**P7-7.14 (MUST) Under application countable.** An implementation must be able to report every `APPLIED_LESS_RESTRICTIVELY` and `APPLIED_AFTER_EXPIRY` outcome by enforcement point and policy version.

**P7-7.15 (MUST) Over application countable.** An implementation must be able to report every `APPLIED_MORE_RESTRICTIVELY` outcome by enforcement point and policy version.

**P7-7.16 (MUST) Unknown action recorded as reported.** An implementation must record `ACTION_UNKNOWN` as a received report and must not treat it as an absence of report.

**P7-7.17 (MUST NOT) No enforcement outcome inferred.** An implementation must not record any enforcement outcome other than from a received report.

### 7.5 Obligation outcomes

The six members of section 3.10, and this section states their obligations rather than restating the members.

**P7-7.18 (MUST) One outcome per obligation instance.** An implementation must record exactly one member of the section 3.10 set for every obligation instance.

**P7-7.19 (MUST) Not reported is not fulfilled.** An implementation must not treat `FULFILMENT_NOT_REPORTED` as fulfilment in any projection, report, aggregate or export.

**P7-7.20 (MUST) Permit with an unfulfilled obligation reported as such.** An implementation must report every permit carrying an obligation whose outcome is other than fulfilled as an operation that under the applicable rule should not have proceeded.

**P7-7.21 (MUST) Residue accompanies the outcome.** An implementation must record the residue with every outcome the section 3.10 table requires it for.

### 7.6 Refusal codes

| Code | Cause | Retryable |
| --- | --- | --- |
| `DECISION_INSTANT_REQUIRED` | The request omitted the decision instant | Yes, with the instant |
| `AUTHENTICATION_REFERENCE_REQUIRED` | The request omitted the authentication reference | Yes |
| `OPERATION_UNREGISTERED` | The operation is not in a registered vocabulary | No, until registered |
| `PURPOSE_UNREGISTERED` | The purpose is not registered | No, until registered |
| `ENFORCEMENT_POINT_UNREGISTERED` | The requesting point is not registered | No, until registered |
| `POLICY_UNRESOLVABLE` | The policy document version could not be resolved | Possibly |
| `POLICY_NOT_EVALUABLE` | The policy version is draft, refused, suspended or withdrawn | No, until evaluable |
| `ATTRIBUTE_STALE` | An attribute value exceeded its declared maximum staleness | Yes, with a fresh value |
| `CONCEPT_UNRESOLVABLE` | An attribute's `Part 4` concept could not be resolved | Possibly |
| `PIN_UNOBTAINABLE` | A required pinned artifact could not be obtained | Possibly |
| `NOT_AUTHORISED_TO_ASK` | The requester is not permitted to request a decision for the purpose | No, without a changed decision |
| `DELEGATION_CHAIN_UNOBTAINABLE` | An asserted delegation chain could not be obtained | Possibly |
| `MALFORMED` | The request was not well formed | Yes, corrected |
| `IDEMPOTENCE_KEY_CONFLICT` | A seen key with a different payload | Yes, with a new key |

The set is open under section 9.9.

`NOT_AUTHORISED_TO_ASK` deserves note. Whether a requester may request a decision is itself an authorisation question, and answering it here is not circular provided the meta policy is a policy like any other, evaluable without recursion. Clause P7-7.24 requires the meta policy to be declared and clause P7-7.25 forbids recursion beyond a declared depth.

A refusal is distinguished from a deny throughout, and the newest reviewed standard makes the same distinction at the transport level: a policy based denial and a request level failure are different responses. Section 10.4 records it.

**P7-7.22 (MUST) Refusal codes.** An implementation must return one of the codes above, or a registered code, for every refused request.

**P7-7.23 (MUST) Refusal states what must change.** An implementation must state, with every refusal, whether the request may be retried and what must change.

**P7-7.24 (MUST) Meta policy declared.** An implementation must express the policy governing who may request a decision as a declared policy version and must not embed it in the component.

**P7-7.25 (MUST NOT) No unbounded meta recursion.** An implementation must declare and enforce a maximum depth of meta authorisation and must refuse beyond it rather than recursing.

**P7-7.26 (MUST NOT) No refusal as a deny.** An implementation must not return a refusal in the position of a decision and must not record a refused request as a denied one.

### 7.7 Outcome obligations and review obligations

Normative.

| Outcome | Component records | Component emits | Caller must |
| --- | --- | --- | --- |
| `PERMIT` | Envelope, obligations, validity | Permit produced | Discharge every obligation before proceeding, or deny |
| `DENY` | Envelope | Deny produced | Not proceed |
| `DENY_UNDISCHARGEABLE_OBLIGATION` | Envelope, the undischargeable obligation, both decisions | The corresponding event | Not proceed, and report the capability gap |
| `NOT_APPLICABLE` | Envelope, the count of non matching elements | Not applicable produced | Apply its own declared default and record that it did |
| Any indeterminate | Envelope, the extended value, the cause | Indeterminate produced | Apply its declared response for that extended value |
| `REFUSED` | Refusal, code | Nothing beyond the refusal | Correct the request |
| Enforcement report other than as decided | Report | The corresponding event | Nothing; the record is the point |
| Obligation outcome other than fulfilled | Outcome, residue, review | The corresponding event | Assign the residue |

A **review obligation** is raised where a decision or its enforcement left something requiring attention that nothing else will surface. The enumeration is closed: an obligation attached to a permit whose outcome is other than fulfilled; an obligation on a deny that could not be discharged; an unassigned residue; an emergency access whose review is overdue; an enforcement report of less restrictive application or application after expiry; a restriction applied without the required marking; and a decision produced by a collapsing algorithm that concealed a not applicable.

The last is the least obvious and belongs in the list. A deny that was in fact a coverage gap is a policy defect presenting as a policy decision, and it will never be found by anybody reading denials.

**P7-7.27 (MUST) Recording obligations honoured.** An implementation must record everything the table above requires for every outcome it produces.

**P7-7.28 (MUST) Emission obligations honoured.** An implementation must emit every event the table above requires.

**P7-7.29 (MUST) Review obligations raised on the enumerated conditions.** An implementation must raise a review obligation for every condition the enumeration above names and must record it against the decision.

**P7-7.30 (MUST) Obligation distinguished from task.** An implementation must record a review obligation as a fact and must obtain any task by which it is discharged from `Part 8`, and must not treat the closure of a task as the discharge unless a recorded act says so.

**P7-7.31 (MUST) Open obligations countable.** An implementation must be able to report every open review obligation by condition, policy version and age.

**P7-7.32 (MUST NOT) No authorisation language for a not applicable.** An implementation must not describe a not applicable decision as a denial, a refusal or a prohibition in any report, projection, interface or export.

### 7.8 The three things this section is for

**P7-7.33 (MUST) An absence of policy is never a refusal by policy.** An implementation must not, by any mechanism, configuration, default, aggregation, projection, interface, export or summary, represent a request that matched no policy as a request that policy denied.

**P7-7.34 (MUST) An inability to evaluate is never a decision.** An implementation must return an indeterminate with its extended value where the evaluation could not complete and must not return a permit or a deny in its place.

**P7-7.35 (MUST) A decision returned is never an operation authorised.** An implementation must not represent a permit as evidence that an operation was authorised to proceed, since every obligation must be discharged first and the discharge is reported by somebody else or not at all.
## 8. Observability and the audit record

### 8.1 Two records, one of them incomplete by construction

This component's audit record has an unusual shape. The decision side is complete and certain: it holds everything about every evaluation it performed. The enforcement side is a collection of other parties' claims, most of which never arrive.

That asymmetry is not a defect to be engineered away and it must not be presented as one. An implementation whose observability treats the enforcement side as a data quality problem to be improved to completeness has misunderstood the architecture: the enforcement point is not this component's to instrument, and its silence is a fact about the estate rather than a gap in the record.

What the observability requirements therefore do is different from the prior parts. They make the decision side reproducible, and they make the enforcement side's incompleteness **measurable and attributable**, so that the question "how much of our access control is verified" has a number.

Every decision is also a determination recorded with `Part 3`, per clause P7-3.110 and the reciprocal `Part 5` requires of this part. The division is that `Part 3` holds why the decision was legitimate and what it rested on, and this component holds the evaluation's internals: the condition results, the combination steps, the attribute values.

**P7-8.1 (MUST) Decision side complete.** An implementation must be able to produce, for any decision within its retained history, every attribute value read, every condition result, every combination step and every obligation attached.

**P7-8.2 (MUST) Enforcement incompleteness measured, not hidden.** An implementation must report the proportion of decisions for which no enforcement report was received, by enforcement point and by policy version, and must not present the population as a defect in its own record.

**P7-8.3 (MUST) Determinations recorded with Part 3.** An implementation must record every decision as a determination with `Part 3`, citing the policy version as authority, the attributes as premises, the combining algorithm as method and the obligations as outcome.

**P7-8.4 (MUST NOT) No second citation structure.** An implementation must not hold a citation structure for a decision beyond its pin set and must record the determination's basis with `Part 3`.

**P7-8.5 (MUST) Own operations recorded.** An implementation must record its own policy refusals, analyses, simulations, reproductions, exports and reads as entries.

### 8.2 Grain

| Subject | Grain |
| --- | --- |
| Policy version | One entry per version, plus one per rule, target, obligation and advice declaration. |
| Policy analysis | One entry per analysis per version, including analyses not performed. |
| Attribute declaration | One entry per declaration. |
| Decision request | One entry per request. |
| Attribute value | One entry per attribute per evaluation, not one per attribute. |
| Attribute absence | One entry per required attribute not obtained per evaluation. |
| Condition evaluation | One entry per condition per evaluation. |
| Element result | One entry per matched element per evaluation. |
| Combination step | One entry per application of a combining algorithm. |
| Decision | One entry per decision. |
| Obligation instance | One entry per obligation per decision. |
| Obligation outcome | One entry per obligation instance, updated only by appending a further outcome. |
| Residue | One entry per residue, one per assignment. |
| Withholding record | One entry per decision carrying a withholding obligation. |
| Enforcement report | One entry per report, including late and corrected reports. |
| Delegation assessment | One entry per assessment. |
| Emergency access | One entry per grant, one per review discharge. |
| Read | One entry per decision, explanation, projection or package returned to a principal. |
| Signal | One entry per signal per observation interval. |

Two grains will be resisted on volume grounds and both are required.

**One attribute value entry per attribute per evaluation.** A cached attribute read by four hundred decisions produces four hundred entries, each with its own as of instant and staleness. That is the point: staleness is a property of a use rather than of a value, and the four hundredth use may be beyond the bound when the first was not.

**One condition evaluation entry per condition per evaluation.** Without them, the count of indeterminate conditions in the decision record cannot be derived and the explanation of section 3.16 cannot be assembled without recomputing, which clause P7-4.17 forbids.

**P7-8.6 (MUST) Declared grain.** An implementation must record at the grain of the table above, or declare a finer grain, and must not record at a coarser one.

**P7-8.7 (MUST) Attribute values recorded per use.** An implementation must record an attribute value entry for every use in every evaluation, with the staleness computed for that use, and must not record one entry per cached value.

**P7-8.8 (MUST) Condition results recorded individually.** An implementation must record the three valued result of every condition it evaluated in every evaluation.

**P7-8.9 (MUST) Counting grain stated with every count.** An implementation must state the grain of every count it reports.

### 8.3 What must be recorded with every decision

Sufficient to reproduce the decision and to explain it, without this component running.

Required: the request as received; the resolved policy versions and the mode by which each resolved; every pin; every attribute value with its source, digest, as of instant, obtained instant and computed staleness; every attribute absence with its reason and the semantics applied; every condition evaluation; every element result; every combination step; the concealed outcome of any collapsing algorithm; every obligation and advice instance with its resolved parameters and verifiability; the delegation assessment; the emergency record; both decisions where an obligation forced a change; the validity and the not valid after instant; the enforcement point identity; the three clocks; the collation and arithmetic conventions; and the outcome of every precondition check applied at policy recording, including those that passed.

**P7-8.10 (MUST) Reproduction sufficiency.** An implementation must record enough with every decision to reproduce it from the recorded attribute values and must treat a decision it cannot reproduce as a defect against clause P7-1.12.

**P7-8.11 (MUST) Request recorded as received.** An implementation must record the request as received and must not record a normalised form in its place.

**P7-8.12 (MUST) Conventions recorded.** An implementation must record the collation, Unicode version and arithmetic conventions in force for every evaluation.

**P7-8.13 (MUST) Precondition outcomes recorded, including passes.** An implementation must record the outcome of every precondition check applied at policy recording and the version of the precondition set applied.

**P7-8.14 (MUST) Periodic reproduction.** An implementation must attempt reproduction of a declared sample of retained decisions on a declared cycle, must record every divergence and every unobtainable recorded value, and must declare the sample and the cycle.

**P7-8.15 (MUST) Divergence recorded, not corrected.** An implementation must record a reproduction divergence as a finding about the record and must not amend the original decision.

### 8.4 Access records

**P7-8.16 (MUST) Reads recorded.** An implementation must record every return of a decision, an explanation, a projection or an evidence package to a principal, with the principal, the subject, the purpose and the knowledge time.

**P7-8.17 (MUST) Withholding recorded.** An implementation must record a read of its own records that was refused or reduced by an authorisation decision, with the decision reference, whether or not the requester was told.

**P7-8.18 (MUST) Simulations recorded with their requester.** An implementation must record the requester and the proposed policy version of every simulation, since a simulation over recorded requests reveals how the estate would have decided differently.

**P7-8.19 (MUST) Explanation reads recorded.** An implementation must record every explanation returned, since an explanation of a decision about a person may itself be a disclosure.

### 8.5 Signals

Each signal measures a way in which this part's guarantees are hollowed out while every individual decision continues to look correct.

| Signal | Grain | Why it matters |
| --- | --- | --- |
| Coverage, and the not applicable population by operation and resource kind | One decision | The proportion of the estate's requests no policy addresses. The single most important signal in the part, and one that does not exist where a decision point returns deny. |
| Permits with an obligation whose outcome is other than fulfilled | One decision | Operations that under the applicable rule should not have proceeded. |
| Decisions with no enforcement report, by enforcement point and age | One decision | The proportion of access control that is unverified. |
| Enforcement reports of less restrictive application or application after expiry | One report | Enforcement points not doing what they were told. |
| Enforcement reports of more restrictive application | One report | Denials attributed to policy that policy did not impose. |
| Restrictions applied without the required marking | One report | The failure that destroys the withheld distinction four other parts depend on. |
| Obligation outcomes by member, by kind and by enforcement point | One outcome | Where fulfilment fails, and where it is never reported. |
| Unverifiable obligations by kind, with volume attached | One obligation kind | Instructions nobody will ever confirm were followed. |
| Unassigned residues by kind and age | One residue | Consequences nobody is answerable for. |
| Indeterminate decisions by extended value and by cause | One decision | Which attribute sources are failing, and whether the failures bias toward permit or deny. |
| Decisions resting on absent attributes, by attribute | One decision | Sources whose unavailability is shaping decisions. |
| Decisions relying on a declared default for an absent attribute | One decision | Values the policy supplied because the source did not. |
| Decisions refused for attribute staleness, by attribute | One refusal | Caches at their bounds, and sources too slow for their policies. |
| Collapsed decisions, with the concealed outcome | One decision | Coverage gaps and inabilities wearing the clothes of policy refusals. |
| Capability mismatches by policy version and enforcement point | One pair | Policies that will produce denials their authors did not intend. |
| Shadowed rules by policy version | One rule | Dead policy reviewers read as live. |
| Policy versions unanalysed, and unanalysable for want of a declared request space | One version | Unknown coverage, distinguished from coverage. |
| Policy versions suspended, with the request classes consequently not applicable | One version | The cause of a widespread denial with no policy change. |
| Policy versions of undeclared authority | One version | Policies nobody can justify. |
| Policies with authority drift open | One version | Policies applied on a superseded or withdrawn authority. |
| Emergency accesses by principal and resource, with review discharge state | One access | A mechanism for exceptions used routinely. |
| Overdue emergency reviews by age | One access | An unaudited permanent bypass. |
| Delegation assessments by member | One assessment | Where delegation is failing and where it cannot be assessed. |
| Revocation exposure windows and decisions exercised within them | One revocation | The reach a revocation actually had. |
| Reproduction divergences | One decision | Decay of the record. |
| Decisions not yet recorded with `Part 3` | One decision | The provenance record falling behind. |
| Reads and explanations with no recorded purpose | One read | Erosion of the access record. |

Three of these are the ones an organisation should read first.

**Coverage.** An access control system nobody can measure the coverage of is a system whose gaps are discovered by exploitation. This signal exists only because clause P7-7.4 forbids returning deny for a not applicable.

**Permits with an unfulfilled obligation.** Every member of that population is, under the reviewed standard's own rule, an operation that should have been denied.

**Decisions with no enforcement report.** The honest number for how much of the estate's access control has been verified, which in most organisations will be a small fraction and which nobody currently knows.

**P7-8.20 (MUST) Signals produced.** An implementation must produce every signal in the table above at a declared interval and must declare the interval.

**P7-8.21 (MUST) Signals derived from entries.** An implementation must derive every signal from recorded entries and must be able to enumerate the entries behind any signal value.

**P7-8.22 (MUST NOT) No suppression of a signal.** An implementation must not provide a means of disabling, filtering or thresholding a signal such that a non zero value is reported as zero.

**P7-8.23 (MUST) Coverage reported continuously.** An implementation must produce the coverage and not applicable signals continuously rather than on demand.

**P7-8.24 (MUST) Unreported population standing and attributable.** An implementation must produce the unreported decision signal continuously and must attribute it to enforcement points.

**P7-8.25 (MUST) Emergency use trended.** An implementation must be able to report emergency access counts by principal over time, so that routine use of an exceptional mechanism is visible.

**P7-8.26 (SHOULD) Signal thresholds declared.** An implementation should declare, for each signal, the value at which it requires attention, and should record the declaration as a controlled document under `Part 1`.

### 8.6 The evidence package

Self describing, sufficient to account for a decision without this component running. This is the package a person may be entitled to where a decision about them restricted what they could see, and its contents are specified with that in mind.

Contents, all required.

The decision envelope of section 7.3 in full.

Every policy version evaluated: its statement in every language, its rules with their targets, conditions and effects, its combining algorithm with its declared algebraic properties, its obligations and advice with their authorities and verifiability, its authority with its basis, and its approval resolution outcome envelope.

The content of the `Part 1` document versions carrying the policies and of the clauses cited as their authorities, or the statement that they could not be obtained and why.

Every attribute value with its source, digest, as of instant and computed staleness, and every absence with its reason and the semantics applied.

Every condition evaluation, element result and combination step, and the concealed outcome of any collapsing algorithm.

Every obligation instance with its parameters, its verifiability, its outcome and every residue with its assignment.

The withholding record: what was restricted and how it was marked.

The delegation assessment and the emergency record where either applies.

The enforcement report where one was received, or the statement that none was, with the elapsed interval.

The policy versions' static analysis results, including the analyses not performed and why.

The statement of the limits: that this component records what it decided and not what occurred; that the absence of an enforcement report is the ordinary case and not evidence of compliance; that an obligation declared unverifiable will never be confirmed; and that a revocation does not reach a decision already returned.

A statement of the version of this part the package claims to conform to.

**P7-8.27 (MUST) Package sufficiency.** An implementation must produce a package sufficient to account for the decision without the implementation running and without access to any component of this standard other than the package.

**P7-8.28 (MUST) Policy content included or its absence stated.** An implementation must include the content of the document versions carrying the policies and of the cited authority clauses, or must state that they could not be obtained with the reason and the knowledge time of the attempt.

**P7-8.29 (MUST) Attribute values and absences included.** An implementation must include every attribute value with its provenance and every absence with its reason, since a decision cannot be assessed without knowing what it rested on and what it did not.

**P7-8.30 (MUST) Enforcement state included.** An implementation must include the enforcement report or the statement that none was received, with the elapsed interval.

**P7-8.31 (MUST) Withholding record included.** An implementation must include what a withholding obligation restricted and how it was marked, since that is what the subject of the decision did not see.

**P7-8.32 (MUST) Limit statements included.** An implementation must include the four limit statements in every package.

**P7-8.33 (MUST) Absence stated, not omitted.** An implementation must state, for every required element it could not include, that it could not be included and why.

**P7-8.34 (MUST) Package digest.** An implementation must record a digest over a declared canonical form of the package and must include the profile identity.

**P7-8.35 (MUST NOT) No package for a simulation.** An implementation must not export a package presenting the outcome of a non authoritative simulation as a decision.

**P7-8.36 (MUST) Self description.** An implementation must include a description of the package's structure sufficient for a reader with no knowledge of the implementation to locate each required element.

### 8.7 Retention

**P7-8.37 (MUST) Retention obtained, not assigned.** An implementation must obtain the retention period of every record it holds from a retention rule expressed under `Part 1` and must not assign one of its own.

**P7-8.38 (MUST) Decisions retained with the operations they authorised.** An implementation must retain a decision, its attributes and its obligations for at least as long as the record of the operation it authorised, where that period is known to it, and must record where it is not known.

**P7-8.39 (MUST) Policies outlive their decisions.** An implementation must retain a policy version's whole structure for at least as long as the longest retained decision made under it, since a decision whose policy has been disposed of cannot be explained.

**P7-8.40 (MUST) Attribute values retained with the decision.** An implementation must retain every recorded attribute value for as long as the decision that read it, since reproduction depends on it and the source will not preserve a historical value for this purpose.

**P7-8.41 (MUST) Obligation records outlive the decision.** An implementation must retain every obligation outcome, residue and assignment for at least as long as the record of the operation the obligation accompanied.

**P7-8.42 (MUST) Separate retention per structure.** An implementation must permit the retention of policies, decisions, attribute values and condition evaluations to be set independently, since the last two exceed the first two by orders of magnitude.

**P7-8.43 (MUST NOT) No disposal under an open review obligation.** An implementation must not dispose of a decision carrying an open review obligation or an unassigned residue.

**P7-8.44 (MUST) Disposal recorded and citable.** An implementation must record the disposal of any record it holds with its authorisation reference and must make the disposal citable as a `Part 3` frontier of kind `RETENTION_EXPIRED`.

### 8.8 What cannot be changed

**P7-8.45 (MUST NOT) No amendment of a decision.** An implementation must not modify a recorded decision, its attribute values, its condition evaluations, its combination steps or its obligations by any mechanism, including administrative, migration, correction and support mechanisms.

**P7-8.46 (MUST NOT) No amendment of an enforcement report.** An implementation must not modify a recorded enforcement report and must record a correction as a further report citing the earlier one.

**P7-8.47 (MUST NOT) No retrospective re evaluation.** An implementation must not recompute a recorded decision under a later policy version, a later attribute value or a later combining algorithm and present the result as that decision.

**P7-8.48 (MUST) Migration preserves identity and digests.** An implementation that migrates its records must preserve every decision identity, every attribute value digest and every recorded digest unchanged and must record the migration as an entry.

**P7-8.49 (MUST NOT) No bulk assignment on import.** An implementation must not assign an absence semantics, a maximum staleness, an obligation verifiability, a capability set or an enforcement outcome in bulk during an import, and must record every imported artifact lacking one as carrying the undeclared or unreported value.
## 9. Extension model

### 9.1 Closed sets, open sets, and why

Six sets in this part are closed.

**The combining algorithm set of section 3.8 is closed.** This is the strongest closure in the part. A combining algorithm determines what happens when policies disagree, and a registered algorithm would be a resolution rule whose order dependence, associativity and treatment of the indeterminate no consumer or analyser could assume. The static analysis of section 6.8 depends on the set being enumerable, and the refusal of order dependent resolution in clause P7-3.51 would be defeated by a registry within a month.

**The decision set of section 7.2 is closed.** A new member obliges every enforcement point to grow a branch, and the default branch will be a deny or a permit.

**The three extended indeterminate values are closed.** They are the complete set of what an incomplete evaluation could have produced.

**The obligation outcome set of section 3.10 is closed.** Six things can have happened to an obligation.

**The enforcement outcome set of section 7.4 is closed.** Six things an enforcement point can report.

**The attribute absence semantics set of section 3.6 is closed.** Three things can be done with an absent attribute.

Everything else is open under a registry: obligation kinds, attribute categories, operation vocabularies, residue kinds, decision purposes, enforcement points, digest algorithms, canonical form profiles, refusal codes and event types.

**P7-9.1 (MUST) Closed sets not extended.** An implementation must not add a member to the combining algorithm, decision, extended indeterminate, obligation outcome, enforcement outcome or absence semantics sets.

**P7-9.2 (MUST) Unknown member is a defect, not a default.** An implementation must treat receipt of a member outside a closed set as a defect and must not map it to a member it does recognise.

**P7-9.3 (MUST) Open sets registered.** An implementation must admit a member of an open set only through the registry mechanics of section 9.2 and must not accept an unregistered member at any interface.

**P7-9.4 (MUST NOT) No combining behaviour by registration.** An implementation must not register an obligation kind, an attribute category or any other member whose effect is to resolve a disagreement between policies, since resolution is a combining algorithm and the set is closed.

### 9.2 Registry mechanics

A registry is content of a controlled document version under `Part 1`, so a registration has an effective date, an approval and an author. Keys are permanent and never reused. A member is deprecated rather than removed. Every registration states what the member means, not only what it is called.

**P7-9.5 (MUST) Registry as controlled document.** An implementation must express every registry as content of a document version under `Part 1` and must resolve the registry version in force at the decision instant of any evaluation that reads it.

**P7-9.6 (MUST NOT) No key reuse.** An implementation must not reuse a registry key and must not remove a member that any retained record references.

**P7-9.7 (MUST) Deprecation rather than removal.** An implementation must deprecate a member with an effective date and a reason and must continue to interpret records referencing it.

**P7-9.8 (MUST) Registry version pinned to the decision.** An implementation must pin the version of every registry an evaluation read and must retain that registry version for at least as long as the decision.

**P7-9.9 (MUST) Semantics in the entry.** An implementation must not admit a registry entry that does not state the meaning of the member in terms a consumer can act on.

### 9.3 Obligation kind registry

This is the most consequential registry in the part, and its necessity is a direct consequence of a gap in the reviewed standard.

That standard specifies the obligation mechanism normatively and states in its own text that there are no standard definitions for the actions an obligation may name, so that bilateral agreement between the policy administration point and the enforcement point is required for correct interpretation. The consequence is that an obligation is a string whose meaning lives in a private understanding between two parties, and a third party auditing the estate cannot establish what any obligation required.

A registration must state: the obligation's identity; what the enforcement point is required to do; the parameters it takes and their types; whether its fulfilment is verifiable by this component and, where it is, how; the residue kinds its non fulfilment produces; whether it carries an external notification obligation on non fulfilment; and whether it may be attached as advice, which for most kinds is false.

The last field closes a specific route. An obligation whose non performance makes a permit unsafe must never be attachable as advice, per clause P7-3.65, and declaring the property on the kind makes the constraint enforceable at recording rather than dependent on an author's judgement.

**P7-9.10 (MUST) Obligation semantics stated in full.** An implementation must state every element listed above in every obligation kind registration.

**P7-9.11 (MUST) Verifiability and its method declared.** An implementation must record whether an obligation kind's fulfilment is verifiable and, where it is, by what means, and must not declare a kind verifiable without a means.

**P7-9.12 (MUST) Residue kinds declared per obligation kind.** An implementation must record the residue kinds an obligation kind's non fulfilment produces and must refuse a residue of an undeclared kind against it.

**P7-9.13 (MUST) Advice admissibility declared.** An implementation must record whether each obligation kind may be attached as advice and must refuse an advice declaration of a kind whose registration forbids it.

**P7-9.14 (MUST NOT) No obligation kind by bilateral understanding.** An implementation must not accept an obligation of an unregistered kind and must not rely on an understanding between a policy author and an enforcement point that is not recorded in the registry.

### 9.4 Attribute category and residue kind registries

An attribute category registration states the category's identity, what it describes, whether an attribute of that category may be supplied in the request or must be obtained from a source, and whether values of that category may be cached and for how long by default.

The supply question matters. An attribute a requester may supply is an attribute a requester may choose, so a policy conditioned on a requester supplied attribute is a policy the requester influences. Declaring the property per category, and reporting the population of decisions turning on a requester supplied attribute, is how that influence becomes visible. Clause P7-9.17 requires the report.

A residue kind registration states, as in `Part 6` section 9.6, the kind's identity, whether it is quantifiable and in what units, whether it is remediable later and by what means, the expected assignment owner, and whether it carries an obligation to notify a party outside the organisation.

The external notification field is more consequential here than in `Part 6`. A residue of kind `REDACTION_UNAPPLIED` or `DATA_DISCLOSED` may carry a notification obligation to a supervisory authority or to the person whose information it was, and recording the obligation on the kind means it is raised by the residue rather than remembered.

**P7-9.15 (MUST) Category semantics declared.** An implementation must state, for every attribute category, whether an attribute of that category may be supplied in the request and its default cache lifetime.

**P7-9.16 (MUST) Requester supplied attributes marked.** An implementation must record, on every attribute value, whether it was supplied in the request or obtained from a source.

**P7-9.17 (MUST) Requester influenced decisions reportable.** An implementation must be able to report every decision whose outcome turned on a requester supplied attribute, and must include the count in the signals of section 8.5.

**P7-9.18 (MUST) Residue kind semantics declared.** An implementation must state, for every residue kind, its quantifiability, its later remediability, its expected assignment owner and any external notification obligation.

**P7-9.19 (MUST) External notification raised with the residue.** An implementation must raise the external notification obligation of a residue kind at the moment the residue is recorded and must not leave it to the assignee to discover.

### 9.5 Enforcement point registry

An enforcement point registration states: its identity; the resources and operations it protects; the set of obligation kinds it declares it can discharge; whether it reports enforcement, and within what interval; its declared response to a not applicable decision; its declared response to each of the three extended indeterminate values; and the maximum decision validity it will honour.

The declared responses are the fields that make this registry more than an inventory, and they are what allow the fail safe behaviour to be governed rather than assumed.

**The declared response to a not applicable** is where default deny lives. Clause P7-1.9 forbids this component from returning a deny for a not applicable, and something must decide what happens. Recording it here, per enforcement point, makes it a declared position rather than a property of some code, and makes an enforcement point that permits on not applicable visible as one.

**The declared responses to the three extended indeterminate values** are what make section 6.3's distinctions useful. An enforcement point may reasonably declare that it denies on `INDETERMINATE_DENY`, denies on `INDETERMINATE_DENY_PERMIT`, and permits read operations on `INDETERMINATE_PERMIT`. That is a defensible fail safe policy and it is defensible only because it is declared and because the extended value is computed rather than guessed.

**Whether it reports enforcement** is what makes the unreported population attributable. An enforcement point declaring that it does not report is honest, and the population of decisions returned to it is then known to be unverified by construction rather than by omission. Clause P7-9.24 requires the distinction.

**P7-9.20 (MUST) Capability set declared.** An implementation must record the obligation kinds every enforcement point declares it can discharge and must refuse a registration with no declared set.

**P7-9.21 (MUST) Not applicable response declared.** An implementation must record every enforcement point's declared response to a not applicable decision and must be able to report every point that permits on one.

**P7-9.22 (MUST) Extended indeterminate responses declared.** An implementation must record a declared response to each of the three extended indeterminate values for every enforcement point.

**P7-9.23 (MUST) Reporting undertaking declared.** An implementation must record whether each enforcement point reports enforcement and within what interval.

**P7-9.24 (MUST) Non reporting points distinguished.** An implementation must distinguish a decision returned to a point that does not report enforcement from one returned to a point that does and did not, and must report the two populations separately.

**P7-9.25 (MUST) Maximum honoured validity declared.** An implementation must record the maximum decision validity each enforcement point will honour and must report where a policy declares a longer one.

### 9.6 Operation vocabulary and purpose registries

An operation vocabulary registration states the operations it names, their meanings, the resource kinds each applies to, and the concept binding of each under `Part 4` where one exists.

A purpose registration states why a decision is requested. The purposes that must be distinguished, at minimum: a decision informing an operation about to be performed; a retrospective decision about a past state; a simulation under a proposed policy; a reproduction of a recorded decision; an administrative query about entitlement; and a decision made in the course of an assessment by `Part 12`.

The administrative query purpose is worth its own member. Asking whether a principal **would** be permitted, without any operation being attempted, is a legitimate and common request, and it must be distinguished from a decision informing an actual operation, because the second is followed by an enforcement report and the first never is. Without the distinction the unreported population of section 5.4 is polluted by queries nobody was ever going to enforce.

**P7-9.26 (MUST) Operation meanings declared.** An implementation must state, for every operation in a registered vocabulary, what it means and the resource kinds it applies to.

**P7-9.27 (MUST) Purposes registered and recorded.** An implementation must register every purpose and must record the purpose of every request.

**P7-9.28 (MUST) Minimum purpose distinctions.** An implementation must register at least the six purposes named above as distinct members.

**P7-9.29 (MUST) Administrative queries excluded from the unreported population.** An implementation must exclude decisions of the administrative query purpose from the unreported enforcement population and must report them separately.

**P7-9.30 (MUST NOT) No default purpose.** An implementation must not default the purpose of a request and must refuse a request that omits it.

### 9.7 Digest, canonical form and code registries

**P7-9.31 (MUST) Both registered and both recorded.** An implementation must register digest algorithms and canonical form profiles separately and must record both with every digest.

**P7-9.32 (MUST) Deprecation without invalidation.** An implementation must be able to deprecate a digest algorithm without invalidating any recorded digest and must record an additional digest under a current algorithm rather than replacing the original.

**P7-9.33 (MUST) Refusal codes registered with remedy.** An implementation must state, in every refusal code registration, whether the request may be retried and what must change.

**P7-9.34 (MUST) Event types registered.** An implementation must register every event type it emits beyond the minimum set of section 4.8.

### 9.8 Composition of policy

Four compositions are distinguished and two are prohibited.

**A policy set containing policies and policy sets, by pinned version.** The only composition this part provides, and the combining algorithm of the containing set resolves its members' disagreements.

**A policy reading a verdict, a decision or a process fact as an attribute.** Permitted, and it is how this component composes with `Part 2`, `Part 5` and `Part 6`. The composed value is an attribute with a source, a digest and an as of instant like any other.

**A policy referencing another policy's decision.** Prohibited. A condition that reads whether another policy permitted creates an ordering between policies that nothing declares, and the ordering then determines both outcomes. The remedy is the policy set: put both policies under a combining algorithm, which is exactly what combining algorithms are for. Clause P7-9.36 states it.

**A policy set whose combining algorithm depends on which members applied.** Prohibited. A conditional choice of algorithm is a meta policy with no artifact, and its effect is indistinguishable from an order dependent resolution. Clause P7-9.37 states it.

**P7-9.35 (MUST) Membership by pinned version only.** An implementation must bind every policy set member by pinned version, per clause P7-3.20.

**P7-9.36 (MUST NOT) No condition reading another policy's decision.** An implementation must not admit a condition that reads the decision, element result or obligation set of another policy in the same evaluation.

**P7-9.37 (MUST NOT) No conditional combining algorithm.** An implementation must record exactly one combining algorithm per policy set version and must not admit one selected at evaluation time.

**P7-9.38 (MUST) Nesting depth declared and enforced.** An implementation must declare the maximum policy set nesting depth it accepts and must refuse a membership exceeding it.

**P7-9.39 (MUST NOT) No cyclic membership.** An implementation must refuse a policy set version whose membership graph contains a cycle.

**P7-9.40 (MUST) Attribute composition recorded as attributes.** An implementation must record a verdict, decision or process fact consumed from another component as an attribute value with that component as its source, and must not record it as a policy element result.
## 10. Standards and specifications

### 10.1 How the citations in this part are to be read

Every entry states what the source supplies, the edition established as current at the date of this part, and whether this part's account rests on specification text or on secondary sources. Section 13.1 lists the sources not obtained.

This part's subject has more usable normative material than any other in the standard so far, and two findings post date the author's general knowledge and were established by search. The long standing standard for policy evaluation acquired a draft successor six months before the date of this part. And a new standard for the interface between decision and enforcement was published five months before it, by a different body, with a decision model that conflicts directly with a requirement of this part.

**P7-10.1 (MUST) Cited edition recorded.** An implementation must record the edition or version of every external standard it relies upon and must not cite a standard without its edition.

**P7-10.2 (MUST) Basis marked.** An implementation must record, for every control it adopts from a source named in this section, whether the basis is specification text or practice.

### 10.2 Policy evaluation: XACML

| Standard | Status established | Supplies |
| --- | --- | --- |
| XACML 3.0 Plus Errata 01 | OASIS Standard incorporating Approved Errata, 12 July 2017. The stable release. Version history: first appeared April 2001; 1.0 ratified 2003; 2.0 ratified 1 February 2005; 3.0 ratified January 2013, updated July 2017. | The decision point, enforcement point, information point, retrieval point and administration point architecture, following RFC 2904 in all but the administration point. The four decision values: **permit, deny, indeterminate and not applicable**, with optionally a set of obligations and advice. Conditions evaluating to **true, false or indeterminate**. Policy sets, policies, rules, targets with `AllOf` and `AnyOf`, and conditions. Twelve combining algorithms in a normative appendix, of which four are legacy. Extended indeterminate values. Obligations and advice. |
| XACML 4.0 Committee Specification Draft 01 | Published by OASIS **18 February 2026**. A draft, not a standard. | JSON and YAML policy representations alongside XML; aggregate functions; emptiness tests over bags; lazy variable evaluation. A live discussion about renaming the language to be format agnostic, with candidates including an authorisation language name and its JSON and YAML variants, the XML form retaining the XACML name. |
| XACML profiles | XACML REST Profile 1.1 and JSON Profile of XACML 3.0 Version 1.1 are OASIS Standards. Dynamic Attribute Authority 1.0, Time Extensions 1.0 and Related and Nested Entities 1.0 are Committee Specifications. | Bindings and extensions not used by this part. |

Four properties of XACML bear directly on this part's design and three are adopted.

**The four decision values are adopted unchanged**, and the separation of not applicable from deny is clause P7-7.4, which is the most important requirement in the part.

**The three valued condition domain is adopted**, and it is the same domain `Part 2` section 6.2 specifies, which is what allows a verdict to be consumed as an attribute without a change of logic.

**Extended indeterminate values are adopted.** The distinction between an indeterminate that could only have been deny, one that could only have been permit, and one that could have been either is the most sophisticated treatment of a third value in any standard reviewed across the whole of this standard, and section 6.3 adopts it. `Part 5` section 13.6 records that the idea was considered there and not adopted, and section 13.7 here notes the inconsistency between two adjacent parts.

**The obligation rule is adopted and it is the strongest normative statement this part relies upon.** The specification's own text states that conforming enforcement points are required to deny access unless they **understand and can discharge** every obligation associated with the applicable policy, that obligations are returned to the enforcement point for enforcement, and that advice may be safely ignored. Sections 3.9 and 3.10 are built on it and clause P7-3.62 implements it structurally by turning a permit into a deny where the requesting enforcement point has not declared the capability.

**What XACML does not supply, and this part's principal contributions.** Three gaps, each named in the specification's own text or evident from it.

**No obligation vocabulary.** The specification states that there are no standard definitions for these actions and that bilateral agreement between the administration point and the enforcement point is required for correct interpretation. So the mechanism is standardised and the meaning of every obligation is private, which makes an obligation unauditable by a third party. Section 9.3 requires a registry for that reason.

**No obligation outcome.** The standard specifies when an obligation is attached and what an enforcement point must do if it cannot discharge one. It does not specify what it means for an obligation to have been partially discharged, to have failed, or never to have been reported on. Section 3.10's six member taxonomy and its residue model have no source here.

**No enforcement report.** There is no mechanism by which an enforcement point tells the decision point what it did. The decision point therefore has no basis for the population of section 5.4 and no way to know that an enforcement point has been ignoring an obligation for two years. Sections 3.2 and 3.15 supply it and section 10.6 records it as unsourced.

The account of XACML in this part rests on the specification's own definitions section and on the passage stating the obligation rule, both obtained, and on secondary description for the behaviour of individual combining algorithms. The normative appendix text was not obtained and section 13.1 records it.

### 10.3 The decision and enforcement separation

The separation this part treats as its spine predates every current standard. The access control framework of the open systems reference model literature distinguished an access control decision function from an access control enforcement function, and XACML's decision point and enforcement point are that distinction under later names.

That framework was not obtained and section 13.1 records it. It is cited here because the age of the distinction is part of the argument in section 1.3: this is not a novel architectural preference but a separation every standard in the field has preserved for decades, and the reason it has been preserved is the reason section 1.3 gives.

RFC 2904 supplies the authorisation framework terminology the reviewed standard follows for the decision, enforcement and information points, and was not obtained.

### 10.4 The interface between them: AuthZEN

| Standard | Status established | Supplies |
| --- | --- | --- |
| OpenID Authorization API 1.0 | **OpenID Final Specification, approved by the OpenID Foundation membership and published as Standards Track on 11 March 2026.** The membership vote was 81 approve, 1 object, 25 abstain. A Final Specification is not subject to further revision. Product of the OpenID AuthZEN Working Group. | A transport agnostic API published by the decision point, to which the enforcement point acts as a client. A four tuple information model of subject, action, resource and context. An access evaluation API, batch evaluation, search APIs and decision point metadata. A mandatory HTTPS binding. IANA registries for decision point metadata and capabilities, a well known configuration URI and a URN sub namespace. |

Three properties matter to this part and the third is a direct conflict.

**It does not define a policy language.** Existing decision points, including XACML implementations and the current generation of policy engines, are stated to work unchanged; only the interface is standardised. That is compatible with this part, which specifies a policy model and no wire format.

**It separates a policy denial from a request failure at the transport level.** A successful response carrying a negative decision is a policy based denial; an authentication failure is a different response. That is the same distinction section 7.6 draws between a deny and a refusal, and its presence in a new standard is a useful confirmation.

**Its decision model is boolean, and this part requires four values.** The API's core evaluation returns a decision that is true or false. This part requires permit, deny, not applicable and three extended indeterminate values, and clause P7-7.6 forbids mapping them onto two. The conflict is direct and section 10.5 states the position taken.

The account rests on the OpenID Foundation's approval announcement, on the specification's own IANA considerations section and on a published technical summary. The specification text was not obtained and section 13.1 records that the boolean decision claim in particular rests on secondary description.

### 10.5 Named conflicts

Five conflicts bear on this part. None is resolved by averaging.

**Whether a decision may be boolean.** The newest reviewed standard's evaluation API returns a boolean. XACML returns four values. **Position taken.** Four values plus three extended indeterminate values, per section 7.2, and clause P7-7.6 forbids a two valued interface. The reason is section 7.1: a boolean cannot distinguish a coverage gap from a refusal or an inability from a decision, and those distinctions are the substance of sections 6.8 and 8.5. An implementation exposing the newer API must do so as a projection over the fuller decision and must record the fuller decision, and section 13.4 records that this makes conformance to both standards awkward.

**Whether order dependent resolution is admissible.** XACML provides a first applicable combining algorithm whose resolution is the order in which members were declared. **Position taken.** Refused, per clause P7-3.51, because a declared order is not a governed criterion. This is the fourth consecutive part to refuse selection by declaration order, after `Part 2`'s salience, `Part 5`'s first match and `Part 6`'s branch order, and section 13.7 records that the refusal has become a standard wide principle.

**Whether an ordered variant is a decision rule.** XACML's ordered deny overrides and ordered permit overrides produce the same decision as their unordered counterparts and differ only in obligation evaluation order. **Position taken.** Admitted as obligation orderings and not as decision rules, per clause P7-3.52, which preserves order independence of the decision while supplying the sequencing authors need. This is a reading of the standard rather than a divergence from it.

**Whether a decision point may collapse the four values.** XACML provides deny unless permit and permit unless deny, which never return not applicable or indeterminate. **Position taken.** Admitted only at the outermost policy set, authorised, recorded, and with the concealed outcome recorded, per clause P7-3.54. The alternative of refusing them altogether was considered and rejected, because a fail safe outermost boundary is a real requirement and refusing it would push the collapse into the enforcement point where nothing records it.

**Whether the obligation vocabulary can remain private.** XACML states that bilateral agreement between administration point and enforcement point is required for correct interpretation of an obligation. **Position taken.** Refused. Section 9.3 requires every obligation kind to be registered as content of a controlled document, because an obligation whose meaning is a private understanding is a control no third party can audit and no assurance function can test.

### 10.6 What none of the standards supplies

Twelve requirements in this part have no source in any reviewed standard.

The enforcement report: a mechanism by which the enforcement point tells the decision point what it did, and the treatment of its absence as a measurable population rather than an error.

The obligation outcome taxonomy, and in particular the members for partial fulfilment, impossible fulfilment and unreported fulfilment.

The obligation residue model: its enumeration, its registered kinds, its assignment to an owner and the counting of unassigned residue.

The declaration that an obligation's fulfilment is unverifiable, and the counting of the population.

The requirement that a permit carrying an unfulfilled obligation be reported as an operation that should not have proceeded.

The withholding obligation and its marking requirement, which four prior parts depend upon and which no standard provides.

The requirement that an attribute carry a declared maximum staleness, and that a decision resting on a stale value be refused rather than made.

The requirement that an enforcement point declare its obligation capability set, and the static detection of a capability mismatch before a policy runs.

Coverage as a measured property of a policy set against a declared request space, and the not applicable population as its complement.

Decision validity as a mandatory declared property, and the requirement to state that a revocation does not reach a decision already returned.

Emergency access as a declared policy with three mandatory obligations and a countable review population.

Delegation validity as this component's determination, distinct from `Part 3`'s recording of the chain as asserted.

**P7-10.3 (MUST) Unsourced requirements identified.** An implementation must be able to state, for any control it implements under this part, whether the requirement has a cited source in this section or is listed in section 10.6 as unsourced.

### 10.7 Adjacent standards deliberately not used

| Standard | Why not used here |
| --- | --- |
| Role based access control standards | A role is an attribute, per clause P7-2.7. Adopting a role model as the policy model would put an entitlement structure in this component that `Part 4` governs as concepts and `Part 3` records as assertions. Not obtained. |
| Attribute based access control guidance | The attribute model here is XACML's. The guidance literature was not obtained and section 13.1 records it. |
| OAuth 2.0 and its rich authorisation request extension | A token scope is a coarse pre authorisation issued without the resource in view. It is an attribute here, per clause P7-2.7, and section 12.14 hands `Part 0` the question of how the two relate. |
| Zero trust architecture guidance | An architectural posture rather than a policy model. Its decision point is this component. Not obtained. |
| The general data protection regulation and the artificial intelligence act | Established in `Part 5` section 10.5 and relevant here where an authorisation decision about a natural person carries obligations of notification or explanation. This part does not restate them and section 12.14 hands forward the question of whether an authorisation is ever a decision within the meaning of those instruments. |

### 10.8 Supporting specifications

| Specification | Used for |
| --- | --- |
| RFC 2119 and RFC 8174 | Requirement keywords. |
| RFC 2904 | The decision, enforcement and information point terminology, at one remove. Not obtained. |
| BCP 47 | Language tags on every policy statement. |
| RFC 3339 and ISO 8601 | Instant representation for the three clocks and for attribute as of instants. |
| The Unicode Standard and the Unicode Collation Algorithm | Collation pinning for string comparison in conditions, per clause P7-6.7. |
| RFC 8785 | An example of a canonical form profile of the kind section 9.7 requires. |
| RFC 9457 | A model for conveying a refusal of the kind section 7.6 specifies. |
| CloudEvents | A model for the event envelope of section 4.8. |

The following clauses rest on practice rather than specification text and are collected so a reader can see the set: clause P7-3.34 on a declared maximum staleness per attribute; clause P7-3.61 on declaring an obligation's verifiability; clause P7-3.63 on the static detection of capability mismatch; clause P7-3.85 on declaring validity per policy version; clause P7-3.88 on computing a revocation exposure window; clause P7-4.19 on removing the authorisation barrier to enforcement reporting; clause P7-6.41 on requiring a declared request space for coverage; clause P7-8.14 on periodic reproduction sampling; and clause P7-9.17 on reporting decisions turning on a requester supplied attribute.

**P7-10.4 (MUST) Practice basis recorded.** An implementation that adopts a clause listed in the paragraph above as a control must record that its basis is practice.
## 11. Anti patterns

Each entry names the mechanism by which the failure occurs, states the consequence, and marks whether the prohibition rests on specification text or on practice.

### 11.1 Default deny in the decision point

**Mechanism.** No policy addresses a request. Returning not applicable requires the caller to decide what to do, which is awkward, so the decision point returns deny. It is safe, it is what everybody expects, and it is one line.

**Consequence.** The coverage gap becomes invisible. An estate where a third of requests match no policy has policy coverage of two thirds and nobody can ever discover it, because every uncovered request looks like a policy refusal. Users experience arbitrary denials and the policy authors cannot find the cause, since the policy they are reading is not the one producing the outcome.

**Basis.** Specification text, in that the reviewed standard provides not applicable as a decision value distinct from deny.

**P7-11.1 (MUST) Not applicable returned as not applicable.** An implementation must return `NOT_APPLICABLE` where no element's target matched and must record the enforcement point's declared response separately, per clauses P7-7.4 and P7-9.21.

### 11.2 Indeterminate returned as deny

**Mechanism.** An attribute source is unavailable. The condition cannot be evaluated. Denying is the safe response, so the decision point denies.

**Consequence.** An inability to evaluate becomes a policy finding. The population of decisions affected by a failing attribute source is indistinguishable from the population the policy refused, so an outage in an identity system presents as a policy change. And the extended indeterminate information, which would have told the enforcement point that the decision could only have been permit, is discarded before it reaches anyone.

**Basis.** Specification text, in the reviewed standard's four value decision set and its extended indeterminate values.

**P7-11.2 (MUST NOT) No indeterminate as a deny.** An implementation must return an indeterminate with its extended value and must not return deny on that ground, per clauses P7-6.20 and P7-7.34.

### 11.3 The boolean at the interface

**Mechanism.** The decision point evaluates four values correctly and its interface returns true or false, because that is what applications want and what the newest interface standard specifies.

**Consequence.** Every distinction the evaluation maintained is destroyed at the boundary. Coverage cannot be measured, the extended indeterminate cannot be acted upon, and an operation proceeding on an unfulfilled obligation is indistinguishable from one proceeding correctly. This is the same collapse `Part 2` section 11.1 names for verdicts and `Part 5` section 11.14 names for decisions, appearing a third time.

**Basis.** Practice, and a direct conflict with a current standard recorded in section 10.5.

**P7-11.3 (MUST NOT) No two valued interface.** An implementation must not provide an interface whose result is a single truth value and must expose any boolean form as a projection over a recorded fuller decision, per clause P7-7.6.

### 11.4 First applicable

**Mechanism.** Policies are combined by taking the decision of the first whose target matches, in the order the policies were listed. It is easy to read and it is a standard combining algorithm.

**Consequence.** Somebody inserts a policy above another and the organisation's entitlements change. The change has no author, no approval and no effective date, because listing order is not a policy artifact in anybody's process. `Part 2`, `Part 5` and `Part 6` each refused the same construct in their own domain.

**Basis.** Specification text, in that the reviewed standard provides algorithms whose decision is order independent, and a divergence from it recorded in section 10.5.

**P7-11.4 (MUST NOT) No order dependent resolution.** An implementation must not admit a combining algorithm whose decision is determined by declaration order, per clause P7-3.51.

### 11.5 The collapsing algorithm at every level

**Mechanism.** Deny unless permit is convenient: it always returns a decision and never returns anything the caller has to think about. So it is used on every policy set, not just the outermost.

**Consequence.** Every not applicable and every indeterminate at every level becomes a deny, and the concealment compounds. A coverage gap three sets deep is a deny at the root with nothing recording that no policy addressed the request. The measure of section 6.8 becomes uncomputable.

**Basis.** Practice.

**P7-11.5 (MUST) Collapsing algorithms fenced to the outermost set.** An implementation must admit a collapsing algorithm only at the outermost policy set, must require the use to be authorised, and must record the concealed outcome, per clause P7-3.54.

### 11.6 The permit that proceeded on an unfulfilled obligation

**Mechanism.** A permit carries an obligation to write an access log entry. The log write fails. The enforcement point permits the operation, because denying at that point means failing a user request for a logging problem.

**Consequence.** Under the reviewed standard's own rule the operation should have been denied. It proceeded, and the only record of the failure is in a logging system with nothing connecting it to the access. This is the single most consequential population this component can report and it is reportable only if the obligation outcome is recorded.

**Basis.** Specification text, in the rule that a conforming enforcement point must deny unless it can discharge every obligation.

**P7-11.6 (MUST) Unfulfilled obligation on a permit reported.** An implementation must record the obligation outcome, must raise a review obligation and must count the population, per clauses P7-3.71 and P7-3.72.

### 11.7 The obligation nobody can discharge

**Mechanism.** A policy attaches an obligation to a permit. The enforcement point receiving it has never implemented that obligation kind. Nobody checked.

**Consequence.** Either the enforcement point denies every affected request, producing an unexplained widespread denial, or it ignores the obligation and permits, producing section 11.6. Both outcomes were detectable before the policy ran, by comparing the policy's obligations against the enforcement point's declared capabilities, and neither was detected because the capabilities were never declared.

**Basis.** Practice, and enabled by the reviewed standard's absence of an obligation vocabulary.

**P7-11.7 (MUST) Capability declared and mismatch detected.** An implementation must record every enforcement point's obligation capability set, must return deny where an obligation is outside it, and must report the mismatch statically, per clauses P7-3.62 and P7-3.63.

### 11.8 The obligation whose meaning is a private understanding

**Mechanism.** An obligation is a string. The policy author and the enforcement point developer agreed what it means over a conversation. The reviewed standard explicitly contemplates this arrangement.

**Consequence.** No third party can establish what any obligation required, so no assurance function can test whether it was fulfilled and no auditor can say whether the control exists. The obligation is a control on paper whose content is unrecorded.

**Basis.** Specification text, in the standard's statement that bilateral agreement is required for correct interpretation, which this part refuses.

**P7-11.8 (MUST) Obligation kinds registered.** An implementation must register every obligation kind as content of a controlled document with its semantics, parameters, verifiability and residue kinds, and must refuse an unregistered kind, per clauses P7-3.59 and P7-9.14.

### 11.9 The silent redaction

**Mechanism.** A policy restricts what a requester may see. The enforcement point removes the fields. The requester sees a record with fewer fields and no indication that anything was removed.

**Consequence.** `Part 1`, `Part 2`, `Part 3` and `Part 4` all maintain a distinction between a value that is absent and one that is withheld, and every one of those distinctions originates in a decision made here. A silent removal destroys the distinction at its source: the consumer cannot tell whether the field is empty because the subject has no value or because policy hid it, and `Part 2` will treat the withheld path as undeclared, and `Part 3` will record a search as complete when it was not.

**Basis.** Specification text, in `Part 2` clause P2-12.18 and `Part 3` clause P3-12.18, both of which require this component to identify what it restricted as withheld.

**P7-11.9 (MUST NOT) No silent restriction.** An implementation must express every restriction as a withholding obligation carrying a marking requirement and must record what was restricted, per clauses P7-3.78 and P7-3.80.

### 11.10 The stale attribute

**Mechanism.** An attribute is expensive to fetch, so it is cached. The cache lifetime is a global setting chosen for performance.

**Consequence.** A principal's employment status changed at nine o'clock and the decision at nine forty is made on the eight o'clock value. Whether that matters depends entirely on the attribute, and a global cache lifetime cannot express the difference between a classification that changes yearly and an employment status that changes at a moment.

**Basis.** Practice.

**P7-11.10 (MUST) Staleness bounded per attribute and enforced.** An implementation must record a maximum staleness on every attribute declaration and must refuse a decision resting on a value beyond it, per clauses P7-3.34 and P7-3.35.

### 11.11 The absent attribute treated as false

**Mechanism.** A condition tests whether a principal holds a clearance. The clearance attribute cannot be obtained. The condition is false, so the rule does not fire.

**Consequence.** The rule was a permit rule, so the principal is denied for a reason nobody recorded: not that they lack the clearance but that the source was unavailable. Where the rule was a deny rule the consequence is worse, because the principal is permitted. In both cases a three valued condition was evaluated in two values, which is the collapse `Part 2` clause P2-6.9 forbids in its own domain.

**Basis.** Specification text, in the reviewed standard's three valued condition domain.

**P7-11.11 (MUST) Absent attribute yields indeterminate.** An implementation must record every absence with its reason, must apply the declared absence semantics, and must default to making every condition reading it indeterminate, per clauses P7-3.36 and P7-3.37.

### 11.12 The default that filled the gap

**Mechanism.** An attribute is frequently unavailable and the indeterminate decisions are inconvenient, so a default value is configured.

**Consequence.** The policy now evaluates on a value nobody supplied, and the default is a policy decision made in a configuration file with no authority, no approval and no effective date. Every decision it affected looks like a decision made on facts.

**Basis.** Practice.

**P7-11.12 (MUST) Declared default authorised and recorded.** An implementation must require an authority on every declared default and must record on every affected decision that a default was applied, per clauses P7-3.38 and P7-3.39.

### 11.13 The decision cached past its validity

**Mechanism.** The decision point is a network call, so decisions are cached at the enforcement point. The cache lifetime is chosen for performance and the decision's declared validity is ignored or not read.

**Consequence.** A revoked entitlement remains exercisable for the cache lifetime rather than the validity, and the exposure window is a property of a performance setting rather than of policy. `Part 1` clause P1-12.14 already forbids a consumer from caching beyond a declared validity, and this is that prohibition failing.

**Basis.** Specification text, in `Part 1` clause P1-12.14.

**P7-11.13 (MUST) Validity declared and expired reliance reported.** An implementation must declare a validity on every decision and must report every enforcement report indicating action after expiry, per clauses P7-3.84 and P7-3.86.

### 11.14 The revocation believed instantaneous

**Mechanism.** An entitlement is revoked. The revocation is recorded. Everybody proceeds on the belief that access has stopped.

**Consequence.** Every outstanding decision granting the entitlement remains valid until its expiry, so access continues for up to the validity interval. Where the validity is long or unbounded, it continues indefinitely. This is structural rather than a defect, and the failure is the belief rather than the behaviour.

**Basis.** Practice.

**P7-11.14 (MUST) Revocation reach stated and exposure computable.** An implementation must state that a revocation does not reach a returned decision and must be able to compute the exposure window and the decisions within it, per clauses P7-3.87 and P7-3.88.

### 11.15 The absence of a report read as compliance

**Mechanism.** Decisions are returned. No enforcement reports come back. The access logs show no violations. The quarterly report says access control is operating effectively.

**Consequence.** Nothing was verified. The absence of adverse reports is the absence of reports, and an enforcement point that has been ignoring an obligation for two years produces exactly the same silence as one operating perfectly. This is the failure clause P7-3.10 forbids and it is the reason the unreported population is the third signal an organisation should read.

**Basis.** Practice.

**P7-11.15 (MUST NOT) No enforcement inferred from silence.** An implementation must not infer enforcement, fulfilment or occurrence from the return of a decision, and must count and attribute the unreported population, per clauses P7-3.10 and P7-8.24.

### 11.16 The reporting barrier

**Mechanism.** Reporting enforcement requires an authorisation, or a schema the enforcement point does not implement, or a field it cannot populate. Honest reporting is harder than silence.

**Consequence.** The reports that do arrive are the easy ones, which are the ones where everything worked. An enforcement point that under applied a decision has every incentive not to report and a technical excuse for not doing so. The population of under application is then structurally undercounted.

**Basis.** Practice.

**P7-11.16 (MUST) Reporting unobstructed.** An implementation must make the reporting operation available without a further authorisation and must record a report even where it discloses an under application, per clause P7-4.19.

### 11.17 The condition that is a business rule

**Mechanism.** A policy needs to know whether a transaction exceeds a threshold. Writing the comparison in the condition is one line. Obtaining a `Part 2` verdict as an attribute is an integration.

**Consequence.** The threshold is now a rule with no identity, no statement, no authority, no enforcement level and no verdict record, and its three valued outcome is gone. `Part 2` section 12.7 names this from the other side, and the estate now has business constraints in two components with two vocabularies and two review cycles.

**Basis.** Specification text, in `Part 2` section 12.7.

**P7-11.17 (MUST NOT) No duplicated business rule.** An implementation must not admit a condition restating a constraint governed under `Part 2` and must require the verdict to be read as an attribute, per clause P7-3.29.

### 11.18 The role that became the policy

**Mechanism.** Entitlements are expressed as role assignments. The policy is the role model: holding a role is permission.

**Consequence.** There is no policy artifact. The organisation's access rules are the contents of a group directory, which has no statement, no authority, no combining algorithm and no version. A change to an entitlement is a membership change performed by an administrator, and nobody can say what the rule was on a past date.

**Basis.** Practice.

**P7-11.18 (MUST) A role is an attribute.** An implementation must treat a role, a group membership or a token scope as an attribute and must not treat it as a decision, per clause P7-2.7.

### 11.19 Stewardship as entitlement

**Mechanism.** The recorded steward of a concept, the custodian of a document or the owner of a resource is treated as entitled to change it, because ownership plainly implies authority.

**Consequence.** Two authorisation authorities exist: this component and whatever component records ownership. The second has no effective date, no scope and no approval, and its answers diverge from the first's. `Part 4` clause P4-12.18 forbids that component from deriving an entitlement from stewardship, and this is the same conflation approached from the other side.

**Basis.** Specification text, in `Part 4` clause P4-12.18.

**P7-11.19 (MUST) Ownership is an attribute.** An implementation must treat a stewardship, custodianship or ownership assertion as an attribute and must require every entitlement to be a decision under a policy version.

### 11.20 The emergency path outside policy

**Mechanism.** Emergency access is implemented as a separate mechanism: a break glass account, an administrative override, a support tool with elevated rights. It is faster than a policy and it works when the policy system is down.

**Consequence.** The access nobody governs is the access most worth governing. Its use is invisible, its justifications are unrecorded, and nothing reviews it. And the argument that it must work when the policy system is down is the argument that it must be the one access path with no controls at all.

**Basis.** Practice, and the reviewed literature names emergency access as a canonical use of obligations rather than as a bypass.

**P7-11.20 (MUST) Emergency access is a declared policy.** An implementation must express every emergency path as a policy version with three mandatory obligations and a countable review population, per clauses P7-3.97 and P7-3.98.

### 11.21 The emergency review nobody performs

**Mechanism.** Emergency access attaches a review obligation. The reviews accumulate. Nobody has time.

**Consequence.** The mechanism intended for exceptions becomes an unaudited permanent bypass, and its routine use is invisible because the only thing that would reveal it is the review nobody performs. The count of overdue reviews is the measure and it is the measure nobody requests.

**Basis.** Practice.

**P7-11.21 (MUST) Overdue reviews countable and trended.** An implementation must report every undischarged emergency review by age and must report emergency use by principal over time, per clauses P7-3.101 and P7-8.25.

### 11.22 The policy that authorises the policy

**Mechanism.** Deciding whether a requester may request a decision is itself an authorisation, so the component asks itself, which asks itself.

**Consequence.** Either the recursion is unbounded and a request never completes, or a base case is hard coded and the meta policy is a configuration nobody governs. Both failures are silent.

**Basis.** Practice.

**P7-11.22 (MUST) Meta policy declared and depth bounded.** An implementation must express the meta policy as a declared policy version and must declare and enforce a maximum recursion depth, per clauses P7-7.24 and P7-7.25.

### 11.23 Coverage never measured

**Mechanism.** Nobody asks what proportion of requests the policy set addresses, because the question requires a declared request space and nobody has declared one.

**Consequence.** The organisation cannot say whether its access control is complete. Gaps are discovered by exploitation or by a user complaint, and each is treated as an individual policy omission rather than as a symptom of an unmeasured property.

**Basis.** Practice.

**P7-11.23 (MUST) Coverage measured against a declared space.** An implementation must perform the coverage analysis where a request space is declared, must record that it could not where none is, and must report the not applicable population continuously, per clauses P7-6.41 and P7-8.23.

### 11.24 The shadowed rule

**Mechanism.** A rule is added for a specific case. A broader rule already covers it and the combining algorithm prefers the broader one. The specific rule can never contribute.

**Consequence.** Dead policy that reviewers read as live. A reviewer confirms that the policy handles a case; the case is handled by a different rule with a different effect. This is the same failure `Part 5` section 11.12 names as masking and `Part 6` reports for unreachable activities.

**Basis.** Practice.

**P7-11.24 (MUST) Shadowing analysed and reported.** An implementation must analyse shadowing over every policy version whose form admits it and must report every rule that can never contribute, per clauses P7-6.40 and P7-6.43.

### 11.25 The decision point that enforces

**Mechanism.** The decision point is already in the request path, so it blocks. Or it returns the resource with fields removed rather than an obligation to remove them.

**Consequence.** The four situations of section 1.3 collapse into one record saying access was granted. The obligation model becomes decorative, because there is nobody to return obligations to. And the component becomes unavailable in the request path, which is the architectural reason the separation exists as much as the audit reason.

**Basis.** Specification text, in the decision and enforcement separation every reviewed standard preserves.

**P7-11.25 (MUST NOT) No enforcement.** An implementation must not intercept, block, permit, redact or filter, and must return a decision with obligations, per clause P7-1.4.

### 11.26 The decision point that authenticates

**Mechanism.** The decision point receives a credential rather than an authenticated principal, because it is the natural place to check it and because the caller has one to hand.

**Consequence.** One component has one failure producing both a wrong identity and a wrong entitlement, and neither is separately detectable. Every decision then rests on an authentication this component performed and did not record as a separate fact, so an investigation cannot establish whether the identity or the policy was at fault.

**Basis.** Practice.

**P7-11.26 (MUST NOT) No authentication.** An implementation must require an authentication reference with every request, must record it without verifying it, and must not establish the identity of a principal, per clauses P7-1.7 and P7-3.5.
## 12. Boundaries with other parts

Each subsection states four things: what this component delegates, what it must not absorb, the naive design that conflates the two, and the reciprocal declaration the other part must make. Subsection numbers correspond to part numbers, so section 12.8 states the boundary with `Part 8` and section 12.14 states the boundary with `Part 0`. Section 12.7 is deliberately unused, since it would designate this part. Numbers are permanent.

Six of this part's boundaries discharge reciprocal declarations already committed by the parts on the other side. Sections 12.1 through 12.6 discharge them, and two of those obligations are concrete requirements rather than declarations: `Part 2` clause P2-12.18 and `Part 3` clause P3-12.18 both require this component to identify what it restricted as withheld rather than removing it, which section 3.11 specifies.

**P7-12.1 (MUST) Declared allocation.** An implementation must be able to state, for every capability named in this section as delegated, which component provides it, and must not provide it within this component.

**P7-12.2 (MUST) Refusal or absence rather than substitution.** Where a delegated capability is unavailable, an implementation must take the behaviour of section 4.7 and must not substitute a local implementation of it.

**P7-12.3 (MUST NOT) No reaching past a neighbour.** An implementation must not read or write the internal state of another component named in this section and must interact with it only through that component's declared interface.

### 12.1 Boundary with Part 1, controlled documents and records

This subsection is the reciprocal declaration `Part 1` section 12.7 requires.

**Delegated.** The identity, version, status, effectivity, approval, signature and retention of every document carrying a policy version, a migration of policy or a registry of this part. Classification, security marking, custodian, aggregation membership and distribution facts, which arrive here as attributes.

**Must not absorb.** Document status and document metadata. A classification value is an attribute read from that component and never a rule interpreted here.

**Naive conflation.** Access rules expressed as classification values interpreted locally, so the meaning of a marking is encoded in the document component and cannot be changed without changing it. The converse conflation is this component holding document metadata, which then diverges from that component's assertions.

**Reciprocal.** This part declares that it owns policy evaluation, that it obtains classification, marking and distribution facts as attributes from `Part 1`, and that it does not record document status. Clauses P7-12.4 through P7-12.6 make it binding.

**P7-12.4 (MUST NOT) No document state held.** An implementation must not hold, cache beyond the declared staleness of the attribute, or assert the status, version identity or effectivity of any document, and must read every such fact as an attribute.

**P7-12.5 (MUST NOT) No marking interpreted as a rule.** An implementation must treat a classification, marking or distribution value as an attribute and must express the entitlement it implies as a policy element with its own authority.

**P7-12.6 (MUST) Decision reference supplied for recording.** An implementation must return a decision reference that `Part 1` can record with the operation the decision permitted, per clause P1-12.13.

### 12.2 Boundary with Part 2, business rules and constraint evaluation

This subsection is the reciprocal declaration `Part 2` section 12.7 requires, and it carries the concrete obligation of clause P2-12.18.

**Delegated.** Every business constraint evaluation. Whether a rule is satisfied, violated, inapplicable or unevaluable, with the whole verdict envelope including the vacuity flag and the five indeterminacy subclasses.

**Must not absorb.** Constraint evaluation. A verdict arrives as an attribute and a condition never restates the constraint.

**Naive conflation.** That component becomes the authorisation point, per its section 11.26. Or this component embeds constraints in policy, so the conditions governing conduct are split across two components with two vocabularies and no one can enumerate them.

**Reciprocal.** This part declares that it owns policy evaluation, that it does not evaluate business rules under `Part 2`, that it obtains verdicts as attributes where a decision depends on one, and that it identifies withheld paths to that component as withheld rather than removing them. Clauses P7-12.7 through P7-12.9 make it binding.

**P7-12.7 (MUST) Verdicts read as attributes.** An implementation must obtain every verdict as an attribute with `Part 2` as its source, must pin the whole evaluation report, and must not evaluate the constraint itself, per clause P7-3.29.

**P7-12.8 (MUST) Withheld paths identified as withheld.** An implementation must express every restriction on the paths of a subject state as a withholding obligation carrying a marking requirement, must record what was restricted, and must not remove a path silently, per clause P2-12.18 and section 3.11.

**P7-12.9 (MUST) Indeterminate verdict carried as indeterminate.** An implementation must treat a verdict attribute of an indeterminate subclass as making every condition reading it indeterminate and must not treat it as a violation or a satisfaction.

### 12.3 Boundary with Part 3, provenance and audit ledger

This subsection is the reciprocal declaration `Part 3` section 12.7 requires and it carries two concrete obligations.

**Delegated.** The determination record of every decision this component makes, with its basis, its closure assessment and its frontiers. The recording of a delegation chain as asserted, with its instruments.

**Must not absorb.** Provenance. And not the recording of a delegation chain, which is that component's.

**Naive conflation.** That component assesses whether a delegation was valid, because it holds the chain and the instruments, which its clause P3-12.17 forbids. Or this component holds its own citation structure, so two accounts of a decision's basis exist and diverge.

**Reciprocal.** This part declares that it owns policy evaluation and delegation validity, that it identifies withheld scope to `Part 3` as withheld rather than removing it, and that it does not record determinations outside that component. Clauses P7-12.10 through P7-12.12 make it binding.

**P7-12.10 (MUST) Delegation validity owned here.** An implementation must assess the validity of every asserted delegation under a recorded policy version, must expose the assessment so that `Part 3` can cite it, and must be the only component that makes the assessment, per clauses P3-12.17 and P7-3.96.

**P7-12.11 (MUST) Withheld scope identified as withheld.** An implementation must express every restriction on the scope of a search as a withholding obligation carrying a marking requirement, so that `Part 3` can record `PARTIAL_WITHHELD` correctly, per clause P3-12.18.

**P7-12.12 (MUST) Determinations recorded there, not here.** An implementation must record every decision as a determination with `Part 3` and must not hold a citation structure of its own, per clauses P7-3.110 and P7-8.4.

### 12.4 Boundary with Part 4, metadata and model repository

This subsection is the reciprocal declaration `Part 4` section 12.7 requires and it carries the concrete obligation of clause P4-12.19.

**Delegated.** The identity, version, meaning and representation of every concept an attribute is bound to, and of the outcome vocabulary of every operation. The impact analysis of changing any of them.

**Must not absorb.** Definitions, and not stewardship as entitlement.

**Naive conflation.** Stewardship is treated as authorisation, so the recorded steward of a concept becomes the entitlement to change it, which that component's clause P4-12.18 forbids. Or this component defines its own attribute meanings, so two policies over the same word mean different things.

**Reciprocal.** This part declares that it owns policy evaluation, that it obtains governed definitions by resolution against `Part 4` where a policy reads one as an attribute, that a policy attribute expressed over a concept is registered there as a dependency, and that it does not hold definition state. Clauses P7-12.13 through P7-12.15 make it binding.

**P7-12.13 (MUST) Concepts resolved, not defined.** An implementation must obtain the definition version of every concept an attribute is bound to by resolution against `Part 4`, must pin it, and must not hold a definition of its own.

**P7-12.14 (MUST) Attributes registered as dependencies.** An implementation must register every attribute declaration bound to a concept with `Part 4` as a dependent registration of kind `POLICY_ATTRIBUTE`, per clause P4-12.19.

**P7-12.15 (MUST NOT) No stewardship as entitlement.** An implementation must treat a stewardship or ownership assertion as an attribute and must express the entitlement it implies as a policy element with its own authority.

### 12.5 Boundary with Part 5, decision engine

This subsection is the reciprocal declaration `Part 5` section 12.7 requires, and it is the boundary that part records as contestable.

**Delegated.** Every business selection: which of several candidate outcomes applies, on what criterion, with what margin. Criteria, tiebreaks, defaults and precedence orders over business outcomes.

**Must not absorb.** Business selection. A business outcome arrives here as an attribute.

**Naive conflation.** That component becomes the policy decision point, per its section 11.20, because it has criteria machinery and no obligations model. Or this component acquires business criteria, so a selection policy lives in an authorisation engine with no margin, no candidate record and no elimination grounds.

**The test and its limits.** `Part 5` offers the test that an authorisation is a decision whose outcome is an entitlement to act, and records that it works at the extremes and not in the middle. Two cases sit in the middle and both are worth naming. A decision determining which of three approvers is required is a business selection whose outcome this component reads as an attribute. A decision determining a credit limit is a business selection whose outcome constrains later authorisations, and the constraint is expressed here as a condition over the limit attribute. In both the allocation follows the test and in both a reasonable reader might allocate differently, and section 13.4 records it.

**Reciprocal.** This part declares that it owns authorisation and its combining algorithms, that it does not make business selections, that it obtains a business outcome by resolution from `Part 5` where a policy depends on one, and that it records its own decisions as determinations with `Part 3` rather than there. Clauses P7-12.16 through P7-12.18 make it binding.

**P7-12.16 (MUST NOT) No business selection.** An implementation must not select among candidate business outcomes and must obtain every such outcome as an attribute from `Part 5`, per clause P7-1.6.

**P7-12.17 (MUST) Business outcomes read as attributes by pin.** An implementation must obtain a `Part 5` outcome as an attribute with the whole outcome envelope pinned, per clause P5-12.24.

**P7-12.18 (MUST) Determinations recorded with Part 3, not Part 5.** An implementation must record its own decisions as determinations with `Part 3` and must not record them with `Part 5`.

### 12.6 Boundary with Part 6, workflow and process orchestration

This subsection is the reciprocal declaration `Part 6` section 12.7 requires.

**Delegated.** Control flow: when a decision is requested, what happens to it, how a denial is routed, how a review obligation is chased. Process state.

**Must not absorb.** Orchestration and process state. A process fact arrives here as an attribute.

**Naive conflation.** The orchestrator becomes the authorisation point, because a process is where operations happen and a gateway looks like a place to check permission, which its clause P6-12.22 forbids. Or this component acquires sequencing, so a policy expresses an order of operations rather than an entitlement.

**Reciprocal.** This part declares that it owns authorisation and its combining algorithms, that it does not orchestrate, that it obtains process facts as attributes by pin where a policy depends on one, and that it does not hold process state. Clauses P7-12.19 through P7-12.21 make it binding.

**P7-12.19 (MUST NOT) No orchestration.** An implementation must not sequence, retry, escalate or chase anything, and must return a decision.

**P7-12.20 (MUST NOT) No process state held.** An implementation must not hold the state of a process instance and must read every process fact as an attribute with `Part 6` as its source, pinned.

**P7-12.21 (MUST) Intervention decisions supplied.** An implementation must supply a decision for every intervening operation `Part 6` section 4.4 specifies and must record the decision reference, per clause P6-12.21.

### 12.8 Boundary with Part 8, human task and case management

**Delegated.** The work a person does about a decision: reviewing an emergency access, assessing an unfulfilled obligation, assigning a residue, investigating an under application, and the case in which that work sits. The queue and the assignment.

**Must not absorb.** Task management. This component records that a review obligation exists and that it was discharged by a named act; it does not manage the doing.

**Naive conflation.** The review obligation and the task are one entity, so closing the task discharges the obligation and an emergency access is reviewed by a work item being marked done. Or this component acquires the queue, so the population of undischarged reviews is a list nobody outside it can see.

**Reciprocal.** `Part 8` must declare that it owns the work item lifecycle, the queue and the case, that completing a work item does not itself discharge a review obligation, that every discharge is effected by a recording operation here whose outcome the task records, and that its own retention does not govern the retention of the decisions that raised its work items.

**P7-12.22 (MUST) Review obligations recorded, not managed.** An implementation must record every review obligation of section 7.7 as a fact and must obtain any task by which it is discharged from `Part 8`.

**P7-12.23 (MUST NOT) No task driven discharge.** An implementation must not treat the closure of a task as discharging a review obligation without a recorded discharging act naming an actor, per clause P7-5.30.

**P7-12.24 (MUST) Human decisions authorised, not performed.** An implementation must supply the decision authorising a person to perform a task and must not assign, offer or escalate the task.

### 12.9 Boundary with Part 9, schema and contract registry

**Delegated.** The identity, versioning and compatibility of the schemas of policy interchange, decision requests, decision responses, enforcement reports and event payloads, and the validation of an instance against one.

**Must not absorb.** Schema validation. This component records the schema a payload claims and does not validate against it.

**Naive conflation.** A schema constraint becomes an authorisation rule, because rejecting a malformed request looks like denying it. A structural refusal and a policy denial are different outcomes with different meanings, and section 7.6 keeps them apart.

**Reciprocal.** `Part 9` must declare that it owns schema identity and compatibility, that it does not express entitlement, and that it exposes schema versions obtainable by pin.

**P7-12.25 (MUST NOT) No schema validation or versioning.** An implementation must not assign version identity to a schema and must not validate a payload against one, and must express a structural refusal as `MALFORMED` without asserting a schema outcome.

**P7-12.26 (MUST) Structural refusal distinguished from denial.** An implementation must return a refusal for a malformed request and must not return a deny, per clause P7-7.26.

### 12.10 Boundary with Part 10, reference and master data management

**Delegated.** The membership, versioning and retention of every value set an attribute's domain draws upon, and of every operation vocabulary's underlying code list.

**Must not absorb.** Value set membership. An attribute's admissible values are read from a pinned version and never enumerated here.

**Naive conflation.** A policy enumerates a set of permitted values inside a condition, so the set has two masters and a member added in one is absent from the other. A new value then matches no target and every request carrying it returns not applicable, permanently and invisibly.

**Reciprocal.** `Part 10` must declare that it owns value set membership and versioning, that it retains every superseded version for at least as long as the longest retained decision that read it, that it does not remove or reuse member keys, and that it reports the addition or removal of a member to this component so that target completeness can be checked against it.

**P7-12.27 (MUST) Value sets read by pin.** An implementation must read every value set an attribute domain draws upon from a pinned `Part 10` version and must not enumerate the membership in a condition or a target.

**P7-12.28 (MUST) Target completeness checked against the set.** An implementation must be able to report every member of a pinned value set version that no target addresses, since such a member yields a not applicable for every request carrying it.

**P7-12.29 (MUST) Set change surfaces as a policy change.** An implementation must record a change to a pinned value set version as requiring a new policy version where target completeness against the set is affected.

### 12.11 Boundary with Part 11, content addressed artifact store

**Delegated.** The durable storage and retrieval by digest of the octets of anything this component pins or exports: policy artifacts, evidence packages and recorded attribute values whose size warrants it.

**Must not absorb.** Storage semantics. This component owns the mapping from a pin to a digest and a canonical form profile.

**Naive conflation.** The store holds decisions and becomes a second source for them, with no attributes, no condition results and no combination steps, so a reader finds an outcome without its provenance.

**Reciprocal.** `Part 11` must declare that it holds no decision, no attribute value provenance and no policy state, and that it does not delete content on its own authority.

**P7-12.30 (MUST) Digest is the interface.** An implementation must address stored content by digest under a declared canonical form profile and must not rely on a location or path as identity.

**P7-12.31 (MUST NOT) No decision state in the store.** An implementation must not hold decisions, attribute values or condition results in the artifact store as their authoritative record.

### 12.12 Boundary with Part 12, conformance and assurance harness

**Delegated.** All assessment of whether an implementation satisfies this part, including the verification of the properties this part requires an implementation to demonstrate: order independence, reproduction, algebraic property verification and the five analyses of section 6.8.

**Must not absorb.** Self assessment. This component performs the analyses of section 6.8 and the reproduction sampling of clause P7-8.14 and records their results; it does not assess itself against this part.

**Naive conflation.** The component's own coverage figure is presented as evidence that the policy set is complete. A coverage figure computed against a request space the same organisation declared is only as meaningful as the declaration, and clause P7-12.34 requires the declaration to be independently examinable.

**Reciprocal.** `Part 12` must declare that it obtains the clause set from this part by resolution, that it records the version of this part an assessment was made against, that it does not write here while assessing, and that it examines the declared request space and the enforcement point capability declarations independently rather than accepting the coverage and capability figures computed from them.

**P7-12.32 (MUST) Read only assessment.** An implementation must expose everything `Part 12` requires through read operations and must not require a write in order to be assessed.

**P7-12.33 (MUST NOT) No self assessment as assessment.** An implementation must not present its own analyses, coverage figures or reproduction samples as an assessment of conformance, per clause P7-1.17.

**P7-12.34 (MUST) Declared request space exposed.** An implementation must expose the declared request space against which every coverage figure was computed, so that `Part 12` can assess whether the figure means anything.

### 12.13 Boundary with Part 13, model invocation and agent execution

**Delegated.** The invocation of any model, its cost, its retries, its non determinism, its behaviour and the record of what it was asked and returned.

**Must not absorb.** Invocation. A model output reaches a policy only as a pinned attribute obtained beforehand.

**Naive conflation, two forms.** A condition invokes a model to classify a request, so the entitlement depends on a non deterministic output and the decision is not reproducible. Or a model is given the authorisation decision itself, so the policy is a fitted function with no statement, no authority and no combining algorithm, and no explanation of a decision is possible in the terms section 3.16 requires.

**Position taken.** A model output may be an attribute if and only if it was obtained before the evaluation, recorded with its own identity, digest and as of instant, pinned, and marked as a model output rather than a fact. Under those conditions the decision is reproducible in the only available sense: it will yield the same decision from the same recorded output. It is not reproducible in the stronger sense that re invoking the model would yield the same output, and clause P7-12.37 requires the distinction to be recorded.

An agent may request a decision. Where it does, the delegation chain to an accountable party is `Part 3`'s and this component assesses its validity per section 3.13, and clause P7-12.38 requires the assessment to be recorded on the decision.

**Reciprocal.** `Part 13` must declare that it owns invocation and the model artifact, that it does not evaluate policy, that it exposes a model output as an artifact with an identity and a digest that this component can pin, and that it treats a model found defective as a basis defect to `Part 3` so that decisions relying on it can be enumerated.

**P7-12.35 (MUST NOT) No invocation during an evaluation.** An implementation must not invoke a model, an agent or any non deterministic service during an evaluation.

**P7-12.36 (MUST) Model outputs marked as attributes.** An implementation must record a model output used as an attribute with its own identity, digest and as of instant, and must mark it as a model output rather than as a fact from its subject's owner.

**P7-12.37 (MUST) Reproduction limit recorded.** An implementation must record that reproduction of a decision reading a model output does not establish reproduction of the output.

**P7-12.38 (MUST) Agent requests assessed for delegation.** An implementation must assess the delegation of every request made by an automated agent and must record the assessment on the decision.

### 12.14 Boundary with Part 0, system composition

**Delegated.** What happens when all the components run at once: authority over facts more than one component touches, the seams at which values cross boundaries, the propagation of non results, and pinning across a unit of work spanning several components.

**Must not absorb.** Composition. This part states what it decides and what it refuses to hold, and does not state what the estate does with a not applicable or an extended indeterminate beyond requiring the enforcement point's response to be declared.

**Reciprocal.** `Part 0` must declare that this component holds authority over policy versions, decisions, obligations, attribute values as read, delegation validity and emergency access grants, and that it holds authority over nothing else. It must state, for every seam, what must hold and how a violation appears here. It must in particular resolve eight questions this part hands it.

How a token scope relates to a decision, given that a scope is a coarse pre authorisation issued without the resource in view and that this part treats it as an attribute. Whether an estate may rely on a scope in place of a decision, and if so under what declared conditions, is not settled here.

Who is accountable for an enforcement point that does not report, given that clause P7-8.24 makes the population attributable and that this component has no authority over the point.

Whether the response to a not applicable is a per enforcement point declaration, as section 9.5 requires, or an enterprise wide position, given that a heterogeneous set of responses means one request denied at one point and permitted at another.

How a unit of work spanning this component, `Part 2` and `Part 5` pins one policy version, one rule set version and one criterion version together, so that an entitlement, the constraints it rested on and the business outcomes it consumed cannot be against different vintages.

Whether an authorisation decision about a natural person falls within the automated decision provisions `Part 5` section 10.5 records, which would attach explanation and human intervention obligations this part does not specify.

Whether a review obligation raised here, a `Part 8` task and a `Part 3` determination of its discharge are one act or three, which is the third consecutive part to hand the same question forward.

Whether the withholding obligation's marking vocabulary should be specified once for the estate, since four parts consume the distinction and each names it differently.

Whether the six repeated structures now identified should each be specified once, per section 13.7.

**P7-12.39 (MUST) Authority declared, not assumed.** An implementation must not accept an assertion about a policy version, a decision, an obligation, an attribute value as read, a delegation validity or an emergency grant from another component, and must require every such fact to be established by its own operations.

**P7-12.40 (MUST) Non results returned unmodified.** An implementation must return every not applicable and every extended indeterminate unmodified regardless of whether the enforcement point can represent it, and must not degrade one to a permit or a deny in order to fit a caller's model.

**P7-12.41 (MUST) Enforcement gap exposed to composition.** An implementation must make the unreported population, the under application population and the capability mismatch population available as signals, since none can be remedied within this component.
## 13. What could not be established

A question recorded as open can be closed by someone with access to the source. A question closed by inference cannot be reopened, because nothing in the document reveals that an inference was made.

### 13.1 Sources not obtained in full text

The following were not available in full text. This part's account of each rests on specification definitions sections, approval announcements, IANA considerations, publisher status pages, issue trackers and secondary literature. No clause reproduces text from any of them.

**XACML 3.0 Plus Errata 01.** More of this specification was obtained than of any other source in this standard so far, and it is still not the whole. Obtained: the terminology section, including the four decision values, the definition of a condition as evaluating to true, false or indeterminate, and the descriptions of the decision point, enforcement point, information point and context handler. Obtained and load bearing: the passage stating that conforming enforcement points are required to deny access unless they understand and can discharge every obligation associated with the applicable policy, that obligations are returned for enforcement, that advice may be safely ignored, and that there are no standard definitions for obligation actions so that bilateral agreement is required.

**Not obtained: the normative appendix specifying the twelve combining algorithms.** Section 3.8's account of what each algorithm does, and in particular the claims that only one applicable returns indeterminate on multiplicity and that the ordered variants differ from their unordered counterparts only in obligation evaluation order, rest on the appendix headings and on secondary description. Since clause P7-3.52 admits the ordered variants on the strength of the second claim and clause P7-3.51 refuses first applicable on the strength of the first, both should be verified before approval and they are the most load bearing unverified claims in the part.

Also not obtained: the extended indeterminate section. Section 6.3's account of the three values rests on the appendix heading and on secondary description, and section 6.3 is where this part diverges from its own predecessor.

**XACML 4.0 Committee Specification Draft 01.** Established as published by OASIS on 18 February 2026, six months before the date of this part, from the publisher's version record. The draft itself was not obtained. Its content as described here, being JSON and YAML representations, aggregate functions, emptiness tests and lazy variable evaluation, and the live discussion about renaming the language, rests on a technical committee issue summary. Whether the draft changes anything this part relies upon **could not be established**, and a reviewer should read it: a draft successor to the part's principal source, published six months before the part was written, is the most likely thing to invalidate a position taken here.

One source described a JSON representation of XACML 4.0 under a name the technical committee's own naming discussion does not use. The discrepancy could not be resolved and this part does not name the format.

**OpenID Authorization API 1.0.** Established as an OpenID Final Specification approved by the foundation's membership and published as Standards Track on 11 March 2026, five months before the date of this part, with the vote counts, from the foundation's own announcement. The IANA considerations section was obtained. **The specification text was not.**

The claim on which section 10.5's named conflict rests, that the API's core evaluation returns a boolean decision, comes from a published technical summary rather than from the specification. It is a significant claim and it is the basis of clause P7-7.6's refusal to expose a two valued interface, so it should be verified. It is possible that the API carries additional decision context alongside the boolean and that the conflict is narrower than section 10.5 states.

**The access control framework distinguishing a decision function from an enforcement function.** Cited in section 10.3 as the origin of the separation that is this part's spine. Not obtained, not identified by edition, and cited from general knowledge of the reference model literature. The claim that every subsequent standard has preserved the distinction is an inference from the standards that were examined and is not established.

**RFC 2904.** Cited at one remove, as the terminology the reviewed standard follows. Not obtained.

Not obtained and not assessed at all: the role based access control standards; the attribute based access control guidance literature; the OAuth 2.0 family including the rich authorisation request extension, which bears on the scope question section 12.14 hands forward; zero trust architecture guidance; and the current generation of policy languages and engines that the newest reviewed standard states work unchanged beneath its API, none of which was examined for a construct this part's closed sets cannot express.

**P7-13.1 (MUST) Verification before approval.** An implementation or reviewer must verify the claims listed in section 13.1 against the source standards before this part is approved and must record the outcome of each verification against this section.

### 13.2 The size of the decision response

Section 1.4 records that this part serves the investigator and the assurance function over the application, and section 7.3 is the consequence: a decision envelope containing every attribute read with its provenance, every condition result, every combination step, every obligation with its verifiability, and the outcome any collapsing algorithm concealed.

An application wants a boolean. What it gets is a document. The cost is real and it falls in the place where it is least welcome, because an authorisation decision sits in the request path of every operation an estate performs, so the response size and the evaluation cost are multiplied by the estate's whole transaction volume.

Nothing here is costed and section 13.6 records that.

**Open.** Whether a declared reduced response is admissible for a declared class of low consequence operation, with the full envelope recorded and the reduced form returned. That is probably the right answer: the record is what the investigator and the assurance function need, and the response is what the application needs, and they need not be the same object. It was not specified because separating them introduces a second form whose correspondence to the first nothing checks, which is the unbridged correspondence problem this standard has now recorded four times.

### 13.3 The cost of refusing first applicable

Clause P7-3.51 refuses the first applicable combining algorithm. It is a standard algorithm, it is widely used, and it expresses something authors find natural: a list of cases in the order they should be considered, with a fall through.

The justification is the same one `Part 2`, `Part 5` and `Part 6` each gave for the same refusal in their own domains, and the accumulated weight of four refusals is now an argument in itself. The cost is also the same and it is worth restating rather than treating as settled.

An ordered list of cases is more readable than a set of mutually exclusive targets plus a precedence over outcome values. A reviewer can follow the first and must hold the second in mind. So the refusal may make policy more governable in principle and less reviewable in practice, and reviewability is what governability is for.

**Open.** Whether the middle position `Part 6` section 13.3 proposes for its own refusal transfers here: admit an ordered resolution on condition that the order is itself a declared, versioned, approved artifact separate from the listing of the members, so that inserting a policy does not change the order unless the order is also changed. That preserves the readability and removes the mechanism, at the cost of two artifacts whose consistency nothing checks. It was not adopted and the same proposal now stands unadopted in two parts, which suggests it deserves a decision rather than a third recording.

### 13.4 The boundary with the decision engine, and the boundary with everything

`Part 5` section 12.7 records the entitlement test as contestable and section 12.5 here restates it with two middle cases. Neither part resolves it and the position is worth stating plainly: **the boundary between an authorisation and a business decision is a governance allocation, not a derivable fact.**

Three considerations pull in different directions. An authorisation carries an obligations model, an enforcement point and a validity, which a business decision does not, so allocating a selection here gives it machinery it may not need. A business decision carries a margin, a candidate record and elimination grounds, which an authorisation does not, so allocating a selection there gives it machinery this part does not provide. And some selections plainly need both: choosing which of three approvers is required is a business selection whose outcome then constrains an authorisation, and the two components must compose.

**Open.** Whether the test should be replaced by a declaration. An organisation could declare, per operation, which component decides, recording the allocation as a governed artifact rather than deriving it from a test that works at the extremes. That is probably right, it makes the contestable boundary a recorded decision, and it was not specified.

### 13.5 Whether the enforcement report can be more than a hope

Sections 3.2 and 5.4 are honest that this component cannot compel an enforcement report and that its absence is the ordinary case. Clause P7-4.19 removes the barriers to reporting and section 8.5 counts the silence. That is the whole of what this part does about it, and it is not much.

The consequence is that the most important thing this component would like to know, whether its decisions were enforced, is the thing it knows least about, and no requirement in this part changes that.

**Open.** Whether a stronger construction exists. Three were considered and none pursued.

**Receipts as a precondition.** The enforcement point cannot obtain a decision without undertaking to report, and a decision is issued with a receipt the point must return. This is structurally the mechanism `Part 3` section 13.5 considered for registration and did not pursue, and it has the same cost: it makes every operation depend on this component's availability twice rather than once.

**Obligation self reporting.** Every obligation carries, as one of its parameters, the endpoint to which its fulfilment is reported, so the report is part of the obligation rather than a separate undertaking. This is elegant and it does not help for the obligations declared unverifiable, which are the ones that matter.

**Sampling with attestation.** The enforcement point is not required to report every decision and is required to attest periodically that it applied them, with a sample verified independently by `Part 12`. This is how the rest of the world assures controls it cannot instrument and it was not designed here.

The third is probably the right answer and its absence is the largest gap in this part.

### 13.6 The cost of the model

Section 8.2 requires one attribute value entry per use per evaluation and one condition evaluation entry per condition per evaluation. An estate performing a hundred million authorisation decisions a year, each reading eleven attributes and evaluating six conditions, produces about one and a half billion entries. Nothing here is costed.

Both grains are required and each for a specific reason. Per use attribute entries are what make staleness a property of a use rather than of a value, which is what clause P7-3.35 enforces. Per condition entries are what make the explanation of section 3.16 assemblable without recomputation, which clause P7-4.17 requires.

**Open.** Whether a declared coarser grain is admissible for a declared class of operation, so that the volume is paid where the capability is used. That is the same open question `Part 6` section 13.6 records for its own volume, in a domain where the transaction rate is higher by orders of magnitude, and the answer probably has to be the same for both.

### 13.7 Repeated structure across the standard, now seven parts

`Part 4` recorded three repeated structures, `Part 5` five, `Part 6` six. This part adds to the list, and one addition is a **divergence between two adjacent parts on the same question**, which is the first observed instance of the drift the three prior recordings predicted.

**The extended third value.** `Part 5` section 13.6 records that it considered adopting extended indeterminacy, so that an indeterminate outcome would carry the set of decisions it could have been, and did not, and that the omission may have been a mistake. This part adopts it, per section 6.3, because its principal source supplies it. So `Part 5`'s eligibility indeterminacy carries a subclass and a remedy owner, and this part's decision indeterminacy carries what it could have been, and the two are solving the same problem differently in adjacent components that exchange values. **This is not a repeated pattern. It is an inconsistency**, and it should be resolved before it is inherited.

**The refusal of order dependent resolution.** Four parts: `Part 2`'s salience, `Part 5`'s first match, `Part 6`'s branch order, and this part's first applicable. Four refusals, four vocabularies, one principle, and each with its own recorded cost.

**The refusal to arbitrate.** Four parts: `Part 2` reports a rule contradiction and refuses to resolve it, `Part 5` returns an undecidable outcome, `Part 6` refuses to resolve a join by an undeclared order, and this part's only one applicable returns indeterminate on multiplicity.

**The residue model.** `Part 6`'s compensation residue and this part's obligation residue are the same structure: an intended effect partially achieved, enumerated by registered kind, assigned to an owner, counted when unassigned, with an external notification obligation declared per kind. Two parts, two vocabularies, one model.

**The honest undeclared or unreported value.** Seven parts. This part contributes `FULFILMENT_NOT_REPORTED`, `ACTION_UNKNOWN`, `UNASSESSABLE` and `NOT_CHECKED`.

**The immutable record with stateful assertions about it.** Seven parts.

**The declared completeness of a set.** Six parts. This part's coverage against a declared request space is the same structure as `Part 3`'s basis completeness, `Part 4`'s lineage completeness, `Part 5`'s candidate set completeness and `Part 6`'s enumeration completeness: a set whose extent is not declared cannot be relied upon, and the declaration is the responsibility of whoever bounded it.

**The asymmetric bridge that disproves and cannot prove.** Two parts have one, `Part 5` records that it should and does not, `Part 6` records the same, and this part makes three without one. Its candidate is a set of recorded requests with the decisions the policy author asserts the policy produces, run at policy recording, which would catch a policy whose rules do not do what its statement says. Three consecutive parts have now identified the same missing device.

**Open.** All of it, and the first item is no longer a question about tidiness. Two adjacent parts now treat the third value differently, three consecutive parts lack a device each says it should have, and the residue model exists twice. This is the fourth consecutive part to record the question and the third to recommend acting before the next part.

### 13.8 What this part deliberately did not attempt

No conformance assessment of any system was performed or anticipated, per clause P7-1.17.

No policy language is specified. The conditions and targets are constrained by properties rather than by a syntax, on the same basis and for the same reason `Part 2` section 13.13 gives, and the newest reviewed standard's decision not to specify a policy language is a confirmation rather than a coincidence.

No wire format is specified. An implementation may expose the newest reviewed standard's API as a projection over the decision of section 7.3, and section 10.5 records that doing so makes conformance to both standards awkward.

No enforcement point is specified. This part specifies what an enforcement point must be told and what it must declare, and specifies nothing about how it works, which means the most consequential component in the authorisation path is outside this standard entirely. Section 12.14 hands `Part 0` the question of accountability for it.

No treatment is given of authorisation across an organisational boundary, where the decision point and the enforcement point are operated by different parties and neither can compel the other.

No treatment is given of delegation of policy administration: who may write which policies, over which resources. That is itself an authorisation question about this component's own operations, and section 7.6's meta policy addresses only who may request a decision.

No performance or scale requirement is stated, and section 13.6 records the volume concern without a threshold.

**P7-13.2 (MUST) Gaps declared, not filled.** An implementation must not represent a matter listed in section 13.8 as specified by this part.

**P7-13.3 (SHOULD) Open questions carried forward.** A reviewer of this part should record a position on each open question in section 13, and where a position is adopted it should be recorded in the review outcome rather than by silent amendment of the clause it affects.

### 13.9 Questions handed to Part 0 rather than answered here

Each was identified while authoring this part.

How a token scope relates to a decision, and whether an estate may rely on a scope in place of a decision under declared conditions.

Who is accountable for an enforcement point that does not report, given that this part makes the population attributable and has no authority over the point.

Whether the response to a not applicable is a per enforcement point declaration or an enterprise wide position, since a heterogeneous set of responses means one request denied at one point and permitted at another.

How a unit of work spanning this component, `Part 2` and `Part 5` pins one policy version, one rule set version and one criterion version together.

Whether an authorisation decision about a natural person falls within the automated decision provisions `Part 5` section 10.5 records, which would attach explanation and intervention obligations this part does not specify.

Whether a review obligation raised here, a `Part 8` task and a `Part 3` determination of its discharge are one act or three, which three consecutive parts have now handed forward.

Whether the withholding marking vocabulary should be specified once for the estate, since four parts consume the distinction and each names it differently.

Whether the divergence recorded in section 13.7, in which `Part 5` and this part treat the third value differently in adjacent components that exchange values, should be resolved before `Part 8`.
