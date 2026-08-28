# KAIROS STD 003 Part 2: Business Rules and Constraint Evaluation

**Standard.** KAIROS STD 003, the enterprise architecture standard.
**Part.** Part 2 of 14 (Part 0 and Parts 1 through 13). Cited as `KAIROS STD 003 Part 2`.
**Title.** Business rules and constraint evaluation.
**Version.** 1.0.0.
**Status.** Proposed. This part has not been approved and is not effective. It is issued for review against the authoring brief of 2026-08-17.
**Date of issue.** 2026-08-17.
**Supersedes.** Nothing. This is the first version.

## Binding of requirement language

The key words MUST, MUST NOT, SHOULD, SHOULD NOT and MAY in this part are to be interpreted as described in RFC 2119 and RFC 8174, and only in the upper case forms. This part does not use SHALL, SHALL NOT, REQUIRED, RECOMMENDED, NOT RECOMMENDED or OPTIONAL as requirement keywords.

Every requirement in this part is a numbered clause. A clause identifier has the form `P2-S.N`, where `S` is the section number and `N` is the ordinal of the clause within that section. Clause identifiers are permanent. A clause that is later removed has its identifier retired and never reissued. A clause that is later added to a section takes the next unused ordinal in that section, so ordinals are stable but not contiguous over the life of the part.

Text that is not a numbered clause is not binding. Narrative, tables, truth tables, examples and the discussion of standards are provided to make the clauses intelligible and testable, and where a table carries normative content a clause says so explicitly and names the table.

A terminological warning applies to this part more than to most. The word "rule" is used by three current standards to mean three incompatible things: a proposition that claims an obligation or a necessity, a production that fires and changes state, and a row in a decision table that yields an output value. Section 10.8 names the conflict and section 2 states which of the three this part means. A reader who assumes one of the other two will misread every clause in section 6.

## Conformance

An implementation conforms to this part if it satisfies every MUST and MUST NOT clause and records, for each SHOULD and SHOULD NOT clause it does not satisfy, the reason. This part does not define conformance levels, profiles or a certification scheme, and it does not define the method of assessment. Assessment method is the subject of `KAIROS STD 003 Part 12` and is out of scope here.

Where a clause states that a value is an implementation decision, conformance requires that the implementation declare the value, not that it adopt a particular one. An undeclared implementation decision is a nonconformity.

## Clause index

The index below is generated from the clause text of this document. It lists every clause identifier, its modality and its subject label. The counts that follow the index are derived by the same extraction and are stated with the grain at which they were counted.

| Clause | Modality | Subject |
| --- | --- | --- |
| **Section 1** | | **Scope and responsibilities** |
| `P2-1.1` | MUST | Purpose satisfaction |
| `P2-1.2` | MUST NOT | No action |
| `P2-1.3` | MUST NOT | No enforcement |
| `P2-1.4` | MUST | Reproducibility |
| `P2-1.5` | MUST | Three outcomes at minimum |
| `P2-1.6` | MUST NOT | No collapse of the indeterminate |
| `P2-1.7` | MUST | Declaration, statement and authority all present |
| `P2-1.8` | MUST NOT | No rule lifecycle |
| `P2-1.9` | MUST | Termination |
| `P2-1.10` | MUST NOT | No absorption of neighbouring responsibilities |
| `P2-1.11` | SHOULD | Declared exclusions |
| `P2-1.12` | MUST NOT | No conformance self assertion |
| `P2-1.13` | MUST | Evaluation is total |
| `P2-1.14` | MUST | Budget declaration |
| **Section 2** | | **Terminology** |
| `P2-2.1` | MUST | Single meaning per term |
| `P2-2.2` | MUST NOT | No redefinition |
| `P2-2.3` | MUST | Rule sense declared |
| `P2-2.4` | MUST NOT | No collapsing of verdict and enforcement |
| `P2-2.5` | MUST NOT | No collapsing of declaration and statement |
| `P2-2.6` | MUST NOT | No collapsing of inapplicability and satisfaction |
| `P2-2.7` | MUST NOT | No collapsing of the three clocks |
| `P2-2.8` | SHOULD | Term registry |
| **Section 3** | | **Data model** |
| `P2-3.1` | MUST | Declared types |
| `P2-3.2` | MUST NOT | No semantic identifiers |
| `P2-3.3` | MUST | Language tag present |
| `P2-3.4` | MUST NOT | No caller supplied knowledge time |
| `P2-3.5` | MUST | Path scheme named |
| `P2-3.6` | MUST | Three artifacts, separately stored |
| `P2-3.7` | MUST NOT | No derivation between them |
| `P2-3.8` | MUST | Bound at approval |
| `P2-3.9` | MUST | Drift detectable |
| `P2-3.10` | MUST NOT | No silent disable on drift |
| `P2-3.11` | MUST | Correspondence claim recorded |
| `P2-3.12` | MUST | Entity coverage |
| `P2-3.13` | MUST NOT | No update in place |
| `P2-3.14` | MUST NOT | No verdict amendment |
| `P2-3.15` | MUST | Version identity obtained, not assigned |
| `P2-3.16` | MUST NOT | No approval state held |
| `P2-3.17` | MUST | Locator to a clause |
| `P2-3.18` | MUST | Absent guard is a claim |
| `P2-3.19` | MUST | Subject kind declared |
| `P2-3.20` | MUST NOT | No implicit versioning |
| `P2-3.21` | MUST | Pure expressions |
| `P2-3.22` | MUST NOT | No unbounded computation |
| `P2-3.23` | MUST NOT | No ambient time |
| `P2-3.24` | MUST | Binding digest over the whole |
| `P2-3.25` | MUST NOT | No embedded action |
| `P2-3.26` | MUST NOT | No embedded message |
| `P2-3.27` | MUST NOT | No embedded severity |
| `P2-3.28` | MUST | External randomness excluded |
| `P2-3.29` | MUST | Statement in at least one language |
| `P2-3.30` | MUST NOT | No translated statement as authoritative |
| `P2-3.31` | MUST | Message from the statement |
| `P2-3.32` | MUST | Modality recorded |
| `P2-3.33` | MUST NOT | No modality inference |
| `P2-3.34` | MUST | Authority per rule version |
| `P2-3.35` | MUST | Locator, not document |
| `P2-3.36` | MUST | Undeclared authority is declared as such |
| `P2-3.37` | MUST | Interpretation recorded where present |
| `P2-3.38` | MUST | Drift checked on a declared cycle |
| `P2-3.39` | MUST | Drift reported with the verdict |
| `P2-3.40` | MUST NOT | No drift suppression |
| `P2-3.41` | MUST NOT | No inference from silence |
| `P2-3.42` | MUST | Minimum example set |
| `P2-3.43` | MUST | Inapplicability exemplified where a guard exists |
| `P2-3.44` | SHOULD | Indeterminacy exemplified |
| `P2-3.45` | MUST | Examples executed on admission |
| `P2-3.46` | MUST NOT | No admission on disagreement |
| `P2-3.47` | MUST | Examples re executed on dependency change |
| `P2-3.48` | MUST NOT | No generated examples as the bridge |
| `P2-3.49` | MUST | Examples in the binding digest |
| `P2-3.50` | MUST NOT | No correspondence claim from agreement |
| `P2-3.51` | MUST | Guard evaluated separately |
| `P2-3.52` | MUST | Guard false yields inapplicability |
| `P2-3.53` | MUST | Guard indeterminate yields a non result |
| `P2-3.54` | MUST NOT | No implication as a guard |
| `P2-3.55` | MUST | Guard recorded in the verdict |
| `P2-3.56` | MUST NOT | No guard side effects |
| `P2-3.57` | MUST | Classification present |
| `P2-3.58` | MUST | Enforcement level only where behavioural |
| `P2-3.59` | MUST | Enforcement scheme pinned |
| `P2-3.60` | MUST NOT | No action on the level |
| `P2-3.61` | MUST | Distinct verdicts by classification |
| `P2-3.62` | MUST | Level change is a version change |
| `P2-3.63` | MUST NOT | No severity in the message |
| `P2-3.64` | MUST | Membership declared as content |
| `P2-3.65` | MUST | Binding mode per member |
| `P2-3.66` | MUST | Member count derived |
| `P2-3.67` | MUST NOT | No implicit membership |
| `P2-3.68` | MUST NOT | No ordinal as semantics |
| `P2-3.69` | MUST | Set version recorded with every report |
| `P2-3.70` | MUST | Subject state pinned |
| `P2-3.71` | MUST NOT | No unpinned fetch |
| `P2-3.72` | MUST | Withheld distinguished from absent |
| `P2-3.73` | MUST | Completeness declared |
| `P2-3.74` | MUST | Undeclared absence is indeterminate |
| `P2-3.75` | MUST NOT | No subject mutation |
| `P2-3.76` | MUST | As of semantics declared |
| `P2-3.77` | MUST | Terms enumerated |
| `P2-3.78` | MUST | Definition pinned |
| `P2-3.79` | MUST | Ungoverned terms reportable |
| `P2-3.80` | MUST | Definition change observed |
| `P2-3.81` | MUST NOT | No local definition |
| `P2-3.82` | MUST | Pin set complete |
| `P2-3.83` | MUST | Evaluation instant supplied |
| `P2-3.84` | MUST | Knowledge instant defaults declared |
| `P2-3.85` | MUST | Purpose recorded |
| `P2-3.86` | MUST NOT | No unpinned dependency |
| `P2-3.87` | MUST | Digest absence reportable |
| `P2-3.88` | MUST NOT | No pin substitution |
| `P2-3.89` | MUST | One verdict per rule per subject per run |
| `P2-3.90` | MUST | Vacuity reported |
| `P2-3.91` | MUST NOT | No vacuous satisfaction as satisfaction |
| `P2-3.92` | MUST | Witness count derived |
| `P2-3.93` | MUST | Authority status carried |
| `P2-3.94` | MUST | Statement reference carried |
| `P2-3.95` | MUST | Budget consumption recorded |
| `P2-3.96` | MUST NOT | No verdict without a rule version |
| `P2-3.97` | MUST | Finding per violation |
| `P2-3.98` | MUST | Witness path in every finding |
| `P2-3.99` | MUST | Value condition recorded |
| `P2-3.100` | MUST | Truncation declared |
| `P2-3.101` | MUST | Conforming witnesses counted |
| `P2-3.102` | MUST | Finding order declared |
| `P2-3.103` | MUST NOT | No finding without a verdict |
| `P2-3.104` | SHOULD | Sub expression addressing |
| `P2-3.105` | MUST | Report is the result |
| `P2-3.106` | MUST | Counts derived with grain |
| `P2-3.107` | MUST | Unevaluated rules counted |
| `P2-3.108` | MUST NOT | No boolean reduction |
| `P2-3.109` | MUST | Report digest |
| `P2-3.110` | MUST NOT | No summary in place of the report |
| `P2-3.111` | MAY | Derivation supported |
| `P2-3.112` | MUST | Phases separated |
| `P2-3.113` | MUST | Stratum declared |
| `P2-3.114` | MUST NOT | No same or higher stratum reads |
| `P2-3.115` | MUST | Monotonic derivation |
| `P2-3.116` | MUST | Conflicting derivation is a non result |
| `P2-3.117` | MUST NOT | No conflict resolution strategy |
| `P2-3.118` | MUST | Derived values pinned and attributed |
| `P2-3.119` | MUST | Derived values distinguishable |
| `P2-3.120` | MUST NOT | No derivation into the subject |
| `P2-3.121` | MUST | Reference set pinned |
| `P2-3.122` | MUST | Reference set resolved as of the evaluation instant |
| `P2-3.123` | MUST | Unavailable reference set is a non result |
| `P2-3.124` | MUST | Member removal observed |
| `P2-3.125` | MUST NOT | No local reference data |
| `P2-3.126` | MUST | Projections are pure |
| `P2-3.127` | MUST | Projection recomputable |
| `P2-3.128` | MUST | Named projections available |
| `P2-3.129` | MUST NOT | No writes through a projection |
| `P2-3.130` | MUST | Divergence projection |
| `P2-3.131` | MUST | Demonstration satisfiable |
| **Section 4** | | **Interfaces** |
| `P2-4.1` | MUST | Operation classes separated |
| `P2-4.2` | MUST | Refusal is an outcome |
| `P2-4.3` | MUST | Idempotence key accepted |
| `P2-4.4` | MUST NOT | No partial recording |
| `P2-4.5` | MUST | Admission is explicit |
| `P2-4.6` | MUST | Admission preconditions checked at admission |
| `P2-4.7` | MUST | Admission is not approval |
| `P2-4.8` | MUST NOT | No retirement of a rule in use |
| `P2-4.9` | MUST | Approval verified at admission |
| `P2-4.10` | MUST NOT | No admission on unresolvable authority |
| `P2-4.11` | MUST | Evaluation records its pins before returning |
| `P2-4.12` | MUST | Reproduction available |
| `P2-4.13` | MUST | Reproduction failure recorded, not hidden |
| `P2-4.14` | MUST NOT | No citation of a non authoritative run |
| `P2-4.15` | MUST | Batch evaluation reports per subject |
| `P2-4.16` | MUST | Explanation available for every verdict |
| `P2-4.17` | MUST NOT | No explanation reconstruction |
| `P2-4.18` | MUST | Reads do not evaluate |
| `P2-4.19` | MUST | Times required on temporal projections |
| `P2-4.20` | MUST NOT | No partial report |
| `P2-4.21` | MUST | Caller obligations declared |
| `P2-4.22` | MUST NOT | No implied completeness |
| `P2-4.23` | MUST | Non result surfaced unmodified |
| `P2-4.24` | MUST | Declared unavailability behaviour |
| `P2-4.25` | MUST NOT | No substitution on unavailability |
| `P2-4.26` | MUST | Authority unavailability does not gate evaluation |
| `P2-4.27` | MUST | Minimum event set |
| `P2-4.28` | MUST | Envelope minimum |
| `P2-4.29` | MUST NOT | No event in place of a record |
| `P2-4.30` | MUST | Vacuity and indeterminacy are separately eventful |
| `P2-4.31` | MUST NOT | No suppression of adverse events |
| **Section 5** | | **State model** |
| `P2-5.1` | MUST | Three models separate |
| `P2-5.2` | MUST | Unadmissible but in force is reportable |
| `P2-5.3` | MUST NOT | No force state held |
| `P2-5.4` | MUST | Enumerated states only |
| `P2-5.5` | MUST | Enumerated transitions only |
| `P2-5.6` | MUST | State is a projection |
| `P2-5.7` | MUST | No evaluation outside admitted states |
| `P2-5.8` | MUST | Suspension is reported, not silent |
| `P2-5.9` | MUST NOT | No suspension as refusal |
| `P2-5.10` | MUST | Revocation authorised and reasoned |
| `P2-5.11` | MUST | Reinstatement re executes examples |
| `P2-5.12` | MUST NOT | No state change from the passage of time |
| `P2-5.13` | MUST | Superseded versions remain evaluable |
| `P2-5.14` | MUST | Enumerated run states |
| `P2-5.15` | MUST | Pins before evaluation |
| `P2-5.16` | MUST | Derivation before evaluation |
| `P2-5.17` | MUST | Budget termination yields a report |
| `P2-5.18` | MUST NOT | No budget termination as failure |
| `P2-5.19` | MUST | Abandonment detected and recorded |
| `P2-5.20` | MUST NOT | No resumption of an abandoned run |
| `P2-5.21` | MUST | Terminal states are terminal |
| `P2-5.22` | MUST | Enumerated drift states |
| `P2-5.23` | MUST NOT | No dismissal |
| `P2-5.24` | MUST | Retention decision is authorised |
| `P2-5.25` | MUST NOT | No automatic resolution |
| `P2-5.26` | MUST | Open drift is visible in the verdict |
| **Section 6** | | **Execution semantics** |
| `P2-6.1` | MUST | Identical pins yield identical verdicts |
| `P2-6.2` | MUST | Expression language version pinned |
| `P2-6.3` | MUST | Collation pinned |
| `P2-6.4` | MUST | Arithmetic declared |
| `P2-6.5` | MUST | Iteration order total and declared |
| `P2-6.6` | MUST | Kleene strong connectives |
| `P2-6.7` | MUST | Quantifier semantics |
| `P2-6.8` | MUST | Vacuous universal flagged |
| `P2-6.9` | MUST NOT | No boundary collapse |
| `P2-6.10` | MUST | Withheld yields indeterminate |
| `P2-6.11` | MUST | Absent yields per declared semantics |
| `P2-6.12` | MUST NOT | No absence as a value |
| `P2-6.13` | MUST | Type mismatch yields indeterminate |
| `P2-6.14` | MUST NOT | No four valued extension without declaration |
| `P2-6.15` | MUST | Idempotence by key |
| `P2-6.16` | MUST | Deduplication window declared |
| `P2-6.17` | MUST NOT | No idempotence across differing payloads |
| `P2-6.18` | MUST | Evaluation is naturally idempotent |
| `P2-6.19` | MUST | Algorithm order |
| `P2-6.20` | MUST | Not admitted and not in force distinguished |
| `P2-6.21` | MUST | Absent guard yields true |
| `P2-6.22` | MUST | Every member reaches step 11 |
| `P2-6.23` | MUST NOT | No early return on the first violation |
| `P2-6.24` | MUST NOT | No ambient clock |
| `P2-6.25` | MUST | Instants in a declared scale |
| `P2-6.26` | MUST | Calendar convention declared |
| `P2-6.27` | MUST | Leap second behaviour declared |
| `P2-6.28` | MUST NOT | No occurrence time assignment |
| `P2-6.29` | MUST NOT | No knowledge time from a caller |
| `P2-6.30` | MUST | Closure in declared strata |
| `P2-6.31` | MUST | Stratum isolation |
| `P2-6.32` | MUST | Indeterminate derivation asserts nothing |
| `P2-6.33` | MUST | Conflict halts derivation |
| `P2-6.34` | MUST NOT | No fixpoint iteration |
| `P2-6.35` | MUST | Primary budget deterministic |
| `P2-6.36` | MAY | Secondary non deterministic guard |
| `P2-6.37` | MUST | Non deterministic termination marked |
| `P2-6.38` | MUST | Exhaustion yields a non result |
| `P2-6.39` | MUST | Partial results retained |
| `P2-6.40` | MUST | Budget consumption recorded per verdict |
| `P2-6.41` | MUST | Order independent verdicts |
| `P2-6.42` | MUST | Order independence checkable |
| `P2-6.43` | MUST NOT | No verdict as an input |
| `P2-6.44` | MUST | Short circuit disclosed |
| `P2-6.45` | MUST NOT | No short circuit that changes the truth value |
| `P2-6.46` | MUST | Analysis performed where decidable |
| `P2-6.47` | MUST | Undecidability declared |
| `P2-6.48` | MUST NOT | No absence of finding as absence of fault |
| `P2-6.49` | MUST | Detected contradiction reported, not resolved |
| `P2-6.50` | MUST NOT | No analysis at evaluation time |
| `P2-6.51` | MUST | Analysis pinned to a set version |
| **Section 7** | | **Verdict and failure taxonomy** |
| `P2-7.1` | MUST | Closed verdict set |
| `P2-7.2` | MUST NOT | No additional members |
| `P2-7.3` | MUST | Vacuity flag on every satisfaction |
| `P2-7.4` | MUST | Classification determines which conformance member |
| `P2-7.5` | MUST NOT | No mapping onto two values |
| `P2-7.6` | MUST NOT | No caller selected collapse |
| `P2-7.7` | MUST | Subclass on every indeterminacy |
| `P2-7.8` | MUST | Allocation honoured |
| `P2-7.9` | MUST | Defect distinguished from input deficiency |
| `P2-7.10` | MUST NOT | No generic indeterminacy |
| `P2-7.11` | MUST | Withheld and undeclared separated |
| `P2-7.12` | MUST | Cause path recorded |
| `P2-7.13` | MUST | Dependency identified |
| `P2-7.14` | MUST | Envelope completeness |
| `P2-7.15` | MUST NOT | No envelope reduction |
| `P2-7.16` | MUST | Envelope is what is recorded |
| `P2-7.17` | MUST | Two kinds distinguished |
| `P2-7.18` | MUST | Force resolved before the guard |
| `P2-7.19` | MUST | Non applicability is not conformance |
| `P2-7.20` | MUST NOT | No omission of non applicable members |
| `P2-7.21` | MUST | Refusal codes |
| `P2-7.22` | MUST | Refusal recorded |
| `P2-7.23` | MUST NOT | No refusal as a verdict |
| `P2-7.24` | MUST | Retryability stated |
| `P2-7.25` | MUST NOT | No silent retry |
| `P2-7.26` | MUST | Run outcome recorded |
| `P2-7.27` | MUST | Partial is not complete |
| `P2-7.28` | MUST | Non reproducible partials marked |
| `P2-7.29` | MUST | Abandoned runs are not results |
| `P2-7.30` | MUST | Recording obligations honoured |
| `P2-7.31` | MUST | Emission obligations honoured |
| `P2-7.32` | MUST | Caller obligations documented |
| `P2-7.33` | MUST NOT | No inference of conformity from the absence of violation |
| `P2-7.34` | MUST | Unevaluable is never conforming |
| **Section 8** | | **Observability and the audit record** |
| `P2-8.1` | MUST | Rows are the audit record |
| `P2-8.2` | MUST | No separate mutable log |
| `P2-8.3` | MUST | Negative assurance recorded |
| `P2-8.4` | MUST NOT | No inference from an unrecorded check |
| `P2-8.5` | MUST | Declared grain |
| `P2-8.6` | MUST | Witness grain declared |
| `P2-8.7` | MUST | Counting grain stated with every count |
| `P2-8.8` | MUST | Reproduction sufficiency |
| `P2-8.9` | MUST | Request recorded as received |
| `P2-8.10` | MUST | Resolution mode recorded |
| `P2-8.11` | MUST | Periodic reproduction |
| `P2-8.12` | MUST | Divergence recorded, not corrected |
| `P2-8.13` | MUST | Reads recorded |
| `P2-8.14` | MUST | Withholding recorded |
| `P2-8.15` | MUST NOT | No unrecorded export |
| `P2-8.16` | SHOULD | Read records retained with the verdict |
| `P2-8.17` | MUST | Signals produced |
| `P2-8.18` | MUST | Signals derived from rows |
| `P2-8.19` | MUST NOT | No suppression of a signal |
| `P2-8.20` | MUST | Vacuity trend available |
| `P2-8.21` | SHOULD | Signal thresholds declared |
| `P2-8.22` | MUST | Package sufficiency |
| `P2-8.23` | MUST | Authority content included or its absence stated |
| `P2-8.24` | MUST | Conventions included |
| `P2-8.25` | MUST | Absence stated, not omitted |
| `P2-8.26` | MUST | Package digest |
| `P2-8.27` | MUST NOT | No package for a non authoritative run |
| `P2-8.28` | MUST | Self description |
| `P2-8.29` | MUST | Retention obtained, not assigned |
| `P2-8.30` | MUST | Verdict retained at least as long as its subject's obligation |
| `P2-8.31` | MUST | Rule artifacts outlive their verdicts |
| `P2-8.32` | MUST | Disposal recorded |
| `P2-8.33` | MUST NOT | No disposal of a rule version under an open drift observation |
| `P2-8.34` | MUST NOT | No amendment of a recorded verdict |
| `P2-8.35` | MUST NOT | No amendment of a rule version's artifacts |
| `P2-8.36` | MUST | Migration preserves digests |
| `P2-8.37` | SHOULD | Independent anchoring |
| **Section 9** | | **Extension model** |
| `P2-9.1` | MUST | Closed sets not extended |
| `P2-9.2` | MUST | Unknown member is a defect, not a default |
| `P2-9.3` | MUST | Open sets registered |
| `P2-9.4` | MUST | Registry as controlled document |
| `P2-9.5` | MUST NOT | No key reuse |
| `P2-9.6` | MUST | Deprecation rather than removal |
| `P2-9.7` | MUST | Registry version pinned in every run |
| `P2-9.8` | MUST | Semantics in the entry |
| `P2-9.9` | MUST | Language constraints satisfied |
| `P2-9.10` | MUST | Language semantics stated in full |
| `P2-9.11` | MUST | Kleene semantics required of the language |
| `P2-9.12` | MUST | Implementation version registered separately |
| `P2-9.13` | MUST | Language change is a rule dependency change |
| `P2-9.14` | MUST | Stability declared |
| `P2-9.15` | SHOULD | Stable schemes preferred for findings |
| `P2-9.16` | MUST NOT | No cross scheme comparison |
| `P2-9.17` | MUST | Ordering declared |
| `P2-9.18` | MUST | Meaning declared per member |
| `P2-9.19` | MUST NOT | No behaviour from the level |
| `P2-9.20` | MUST | Guideline level admissible |
| `P2-9.21` | MUST | Purpose registered and recorded |
| `P2-9.22` | MUST | Minimum purpose distinctions |
| `P2-9.23` | MUST NOT | No default purpose |
| `P2-9.24` | MUST | Both registered and both recorded |
| `P2-9.25` | MUST | Deprecation without invalidation |
| `P2-9.26` | MUST NOT | No digest without a profile |
| `P2-9.27` | MUST | Subclass allocated at registration |
| `P2-9.28` | MUST | Remedy owner stated |
| `P2-9.29` | MUST | Retryability stated |
| `P2-9.30` | MUST | Event types registered |
| `P2-9.31` | MUST | Drift kinds registered |
| `P2-9.32` | MUST | Inclusion by pinned version only |
| `P2-9.33` | MUST | Effective membership derivable |
| `P2-9.34` | MUST NOT | No cyclic inclusion |
| `P2-9.35` | MUST | Shared sub expressions versioned |
| `P2-9.36` | MUST NOT | No verdict composition |
| **Section 10** | | **Standards and specifications** |
| `P2-10.1` | MUST | Cited edition recorded |
| `P2-10.2` | MUST | Basis marked |
| `P2-10.3` | MUST | Practice basis recorded |
| `P2-10.4` | MUST | Unsourced requirements identified |
| **Section 11** | | **Anti patterns** |
| `P2-11.1` | MUST NOT | No boolean edge |
| `P2-11.2` | MUST NOT | No collapse at a reduction |
| `P2-11.3` | MUST NOT | No salience |
| `P2-11.4` | MUST NOT | No embedded action |
| `P2-11.5` | MUST NOT | No unversioned statement |
| `P2-11.6` | MUST NOT | No admission without an authority reference |
| `P2-11.7` | MUST NOT | No actor as authority |
| `P2-11.8` | MUST NOT | No disable on drift |
| `P2-11.9` | MUST NOT | No applicability in the body |
| `P2-11.10` | MUST NOT | No vacuous satisfaction without its flag |
| `P2-11.11` | MUST NOT | No rule outside the model |
| `P2-11.12` | MUST NOT | No unpinned reference read |
| `P2-11.13` | MUST NOT | No ambient clock in a declaration |
| `P2-11.14` | MUST NOT | No severity in prose only |
| `P2-11.15` | MUST NOT | No fail open configuration |
| `P2-11.16` | MUST NOT | No fail closed configuration |
| `P2-11.17` | SHOULD NOT | No undecomposed conjunction |
| `P2-11.18` | SHOULD NOT | No mechanical granularity |
| `P2-11.19` | MUST NOT | No verdict suppression |
| `P2-11.20` | SHOULD | Unaddressed finding age reported |
| `P2-11.21` | MUST NOT | No generated examples |
| `P2-11.22` | MUST NOT | No computed membership |
| `P2-11.23` | MUST NOT | No comparison across differing pins |
| `P2-11.24` | MUST NOT | No verdict as an operand |
| `P2-11.25` | MUST NOT | No binary floating point at a threshold |
| `P2-11.26` | MUST NOT | No gating |
| **Section 12** | | **Boundaries with other parts** |
| `P2-12.1` | MUST | Declared allocation |
| `P2-12.2` | MUST | Refusal rather than substitution |
| `P2-12.3` | MUST NOT | No reaching past a neighbour |
| `P2-12.4` | MUST | Rule lifecycle obtained from Part 1 |
| `P2-12.5` | MUST NOT | No local lifecycle |
| `P2-12.6` | MUST | The report is the citable artifact |
| `P2-12.7` | MUST NOT | No provenance of other subjects |
| `P2-12.8` | MUST | Terms referenced and pinned |
| `P2-12.9` | MUST NOT | No local definition |
| `P2-12.10` | MUST NOT | No selection |
| `P2-12.11` | MUST NOT | No hit policy |
| `P2-12.12` | MUST NOT | No default or fallback rule |
| `P2-12.13` | MUST | Conflict reported, never arbitrated |
| `P2-12.14` | MUST | Decision outputs pinned as inputs |
| `P2-12.15` | MUST | Verdicts independent of process |
| `P2-12.16` | MUST NOT | No process identity required |
| `P2-12.17` | MUST | Attributes supplied, decisions consumed |
| `P2-12.18` | MUST | Withheld paths identified as withheld |
| `P2-12.19` | MUST | Findings immutable and independent |
| `P2-12.20` | MUST NOT | No schema validation here |
| `P2-12.21` | MUST | Structural defect is indeterminacy |
| `P2-12.22` | MUST | Reference sets read, not held |
| `P2-12.23` | MUST NOT | No enumerated membership in a declaration |
| `P2-12.24` | MUST | Digest is the interface |
| `P2-12.25` | MUST | Read only assessment |
| `P2-12.26` | MUST NOT | No self assessment as assessment |
| `P2-12.27` | MUST NOT | No invocation during evaluation |
| `P2-12.28` | MUST | Model outputs pinned and marked |
| `P2-12.29` | MUST | Authority declared, not assumed |
| `P2-12.30` | MUST | Non result propagation is a composition concern |
| **Section 13** | | **What could not be established** |
| `P2-13.1` | MUST | Verification before approval |
| `P2-13.2` | MUST | Practice basis recorded |
| `P2-13.3` | MUST | Gaps declared, not filled |
| `P2-13.4` | SHOULD | Open questions carried forward |

### Derived counts

Every figure below is derived by extraction from the clause text of this document and not asserted independently. The grain of counting is stated for each figure. A clause is one line of the document matching the clause heading form given under Binding of requirement language, that is, an identifier of the form `P2-S.N`, a modality in parentheses, and a subject label. Narrative sentences containing a requirement keyword are not clauses and are not counted; per that same section they are not binding.

**Total clauses.** 432. Grain: one clause heading.

**By modality.** Grain: one clause heading, counted once against its single declared modality.

| Modality | Clauses | Share |
| --- | --- | --- |
| MUST | 278 | 64.4% |
| MUST NOT | 140 | 32.4% |
| SHOULD | 10 | 2.3% |
| SHOULD NOT | 2 | 0.5% |
| MAY | 2 | 0.5% |
| **All** | **432** | **100.0%** |

**Absolute requirements.** 418 clauses carry MUST or MUST NOT and are therefore conditions of conformance. 12 carry SHOULD or SHOULD NOT and require a recorded reason where not satisfied. 2 carry MAY and constrain nothing. Grain: one clause heading. These three figures sum to the total.

**By section.** Grain: one clause heading, attributed to the numbered section in which its heading appears.

| Section | Title | Clauses | MUST | MUST NOT | SHOULD | SHOULD NOT | MAY |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Scope and responsibilities | 14 | 7 | 6 | 1 | 0 | 0 |
| 2 | Terminology | 8 | 2 | 5 | 1 | 0 | 0 |
| 3 | Data model | 131 | 87 | 41 | 2 | 0 | 1 |
| 4 | Interfaces | 31 | 21 | 10 | 0 | 0 | 0 |
| 5 | State model | 26 | 19 | 7 | 0 | 0 | 0 |
| 6 | Execution semantics | 51 | 37 | 13 | 0 | 0 | 1 |
| 7 | Verdict and failure taxonomy | 34 | 25 | 9 | 0 | 0 | 0 |
| 8 | Observability and the audit record | 37 | 27 | 7 | 3 | 0 | 0 |
| 9 | Extension model | 36 | 28 | 7 | 1 | 0 | 0 |
| 10 | Standards and specifications | 4 | 4 | 0 | 0 | 0 | 0 |
| 11 | Anti patterns | 26 | 0 | 23 | 1 | 2 | 0 |
| 12 | Boundaries with other parts | 30 | 18 | 12 | 0 | 0 | 0 |
| 13 | What could not be established | 4 | 3 | 0 | 1 | 0 | 0 |
| **All** | | **432** | **278** | **140** | **10** | **2** | **2** |

**Ordinal integrity.** In this version, the highest ordinal in each section equals the number of clauses in that section, so no identifier has yet been retired. This will cease to be true at the first clause removal, and the count rather than the highest ordinal is then the figure to rely on.

## 1. Scope and responsibilities

### 1.1 What this component is

This part specifies a component that evaluates declared constraints against subjects and returns verdicts, and that holds the declaration of every constraint separately from the prose that states it and from the authority that legitimises it.

The component exists to answer one question reliably: **given this subject and this set of rules as they stood at a stated time, which rules were satisfied, which were violated by what, which did not apply, and which could not be evaluated and why.** Every other responsibility in this part is subordinate to that question. A component that evaluates quickly and correctly but cannot say which of the four happened, or cannot reproduce the answer later, has failed at its purpose.

Three properties distinguish this component from a general expression evaluator, and each of them is a reason it exists at all.

**It never acts.** It returns a verdict. It does not block, reject, correct, notify, escalate or write to the subject. The most common defect in rule systems is that the rule and the action it triggers are one artifact, after which nobody can say what the organisation believes without also deploying what the organisation does.

**It never guesses.** A constraint that cannot be evaluated because an input is absent yields a distinct verdict that is neither satisfaction nor violation. Collapsing that third outcome into either of the other two is the single most dangerous defect available in this component, and section 7 is written mainly to prevent it.

**It keeps three artifacts bound and distinct.** A rule has a machine evaluable declaration, a human readable statement, and a recorded authority. The declaration is what runs. The statement is what a reviewer approved. The authority is what makes the rule legitimate. These drift apart in every real system, and the component's job is to make the drift visible rather than to prevent it, which it cannot.

The component is accountable for the following.

The identity and addressing of rules, rule sets and the positions within a rule that a finding can point at.

The binding between a rule's declaration, its statement in prose, its worked examples, and its authority reference.

The detection and reporting of drift between those bound artifacts, including drift caused by the authority changing under a rule that did not change.

The classification of a rule as definitional or behavioural, and the consequences of that classification for what a violation means.

The declared enforcement level of a behavioural rule, carried with the verdict and never applied by this component.

The evaluation of a constraint against a subject, deterministically and reproducibly.

The truth semantics of the evaluation, including the treatment of absent, withheld and unrepresentable inputs, and the propagation of the indeterminate value through logical connectives.

The verdict taxonomy, including the separation of not applicable from satisfied and of indeterminate from violated.

Witnesses: for a violation, what violated the rule and where; for a satisfaction, how many instances were examined and whether the satisfaction was vacuous.

The evaluation report as a whole, and its reproducibility from its recorded pins.

Termination: a declared evaluation budget and the verdict returned when it is exhausted.

Derivation, where an implementation supports it, under constraints that keep it terminating and confluent.

The pinning of everything an evaluation depended on: rule set version, subject state, reference data version, vocabulary version, and the three clocks.

The audit record of every evaluation, at a grain sufficient to reproduce any verdict.

### 1.2 What this component is not

Each exclusion below names something a rules engine absorbs if nobody stops it, and each absorption destroys a property that some other component was supposed to guarantee.

The component is not the owner of rule identity, version, approval, effectivity or retention. A rule is content of a controlled document version, and its lifecycle belongs to `Part 1`. This is the reciprocal declaration required by clause P1-12.4 and it is restated as a clause in section 12.

The component is not a decision engine. It does not select among candidate outcomes, rank alternatives, resolve conflicts between competing recommendations, or produce a chosen value. It reports what holds. Selection belongs to `Part 5`, and section 12.5 states the boundary in detail because it is the boundary most often erased.

The component is not an enforcement point. It does not permit or deny an operation. Authorisation belongs to `Part 7`, which may consume verdicts as inputs to a policy decision.

The component is not a workflow engine. It does not sequence evaluations, retry them on a schedule, chase a violation to closure or own the state of a remediation. Orchestration belongs to `Part 6`.

The component is not a schema validator. Structural and type validity of a document or message against its schema belongs to `Part 9`. The distinction is not one of technique, since both are constraint checking, but one of authority: a schema states what a well formed instance is, and a rule states what a permissible instance is. Section 12.9 draws the line and admits that it is contestable.

The component is not the vocabulary. The terms a rule uses are governed definitions belonging to `Part 4`, and the code lists and reference sets it reads belong to `Part 10`. A rule that defines its own terms has no reviewable meaning.

The component is not the store of the subject. It reads a subject state supplied to it or fetched under a pin, and it never writes to the subject.

The component is not the provenance ledger. It emits evaluation records and holds its own audit record; the chain of reasoning of a determination that consumed a verdict belongs to `Part 3`.

The component is not a model invoker. Where a rule's meaning depends on the output of a model, that output is an input to the rule, obtained from `Part 13` and pinned, and never computed inside the evaluation. Section 12.13 states why a non deterministic evaluand cannot be inside a deterministic evaluator.

The component is not an authoring environment. It does not specify how a rule is written, tested interactively, or migrated from a legacy expression.

The component is not a conformance assessor of itself. Assessment belongs to `Part 12`.

**P2-1.1 (MUST) Purpose satisfaction.** An implementation must be able to answer, for any subject and any rule set version within its retained history, which rules were satisfied, which were violated, which did not apply and which could not be evaluated, and must do so by the mechanism specified in section 6.

**P2-1.2 (MUST NOT) No action.** An implementation must not perform, request or schedule any action as a consequence of a verdict, and must not modify the subject of an evaluation.

**P2-1.3 (MUST NOT) No enforcement.** An implementation must not permit, deny, block or reject any operation, and must not represent a verdict as a permission or a denial.

**P2-1.4 (MUST) Reproducibility.** An implementation must be able to reproduce any verdict it has issued from the pins recorded with it, and must return the same verdict on re evaluation with the same pins, per section 6.1.

**P2-1.5 (MUST) Three outcomes at minimum.** An implementation must distinguish satisfaction, violation and inability to evaluate as separate verdicts, and must additionally distinguish inapplicability, per section 7.

**P2-1.6 (MUST NOT) No collapse of the indeterminate.** An implementation must not report a constraint it could not evaluate as satisfied or as violated, under any configuration, including a configuration selected by the caller.

**P2-1.7 (MUST) Declaration, statement and authority all present.** An implementation must not admit a rule for evaluation unless it carries a declaration, a statement in prose and an authority reference, per section 3.2.

**P2-1.8 (MUST NOT) No rule lifecycle.** An implementation must not assign a version identifier, approval, effective date or retention period to a rule, and must obtain all four from `Part 1`.

**P2-1.9 (MUST) Termination.** An implementation must terminate every evaluation within a declared budget and must return the appropriate non result of section 7.2 where the budget is exhausted.

**P2-1.10 (MUST NOT) No absorption of neighbouring responsibilities.** An implementation must not select among outcomes, decide authorisation, orchestrate activities, validate against schemas, define vocabulary terms or invoke models, as those responsibilities are allocated in section 12.

**P2-1.11 (SHOULD) Declared exclusions.** An implementation should publish, as a controlled document under `Part 1`, the list of section 1.2 exclusions that it in fact provides by other means, so that a reader can tell what the implementation does not guarantee.

**P2-1.12 (MUST NOT) No conformance self assertion.** An implementation must not assert conformance to this part on the basis of its own internal checks alone, and must not represent such an assertion as an assessment.

**P2-1.13 (MUST) Evaluation is total.** An implementation must return a verdict of some class in section 7 for every rule it was asked to evaluate, and must not omit a rule from a report without a verdict.

**P2-1.14 (MUST) Budget declaration.** An implementation must declare its evaluation budget as a bound on a stated resource, and must declare the resource, per section 6.7.

### 1.3 The reader this part is written for

Two readers are assumed, and their needs conflict in a way that shapes the whole part.

The first reads a verdict at the moment it is issued and needs to know what to do. That reader wants a short answer and a message that names the problem.

The second reads a verdict years later, in an investigation, and needs to know why it said what it said: which rule, in which version, on whose authority, over what subject state, against what reference data, and whether anyone would get the same answer today. That reader is served only if the first reader's convenience was never allowed to reduce what was recorded.

Where the two conflict, this part serves the second. That is a decision, and it has costs: the evaluation report specified in section 3.16 is substantially larger than the boolean most callers want, and section 8 requires records that no caller will read. The alternative is a system that produces confident verdicts nobody can account for.

## 2. Terminology

Terms are defined here only if this component owns them. A term owned by another part is cited to that part and is not redefined. Where a term is taken from an external standard, the standard is named. Where this part narrows or diverges from the external definition, the divergence is stated, because a silent narrowing is the mechanism by which two components come to use one word for two things.

Definitions are given in the singular. A definition is not a clause and is not binding on its own; clauses that depend on a definition cite the term.

### 2.1 Terms owned by this part

**Rule.** A proposition that claims an obligation or a necessity, together with the artifacts that make it evaluable, reviewable and attributable: a declaration, a statement, examples, an authority reference and metadata. The core sense follows SBVR 1.5, which defines a rule as a proposition that is a claim of obligation or of necessity. This part does not adopt the production sense of PRR 1.0 and RIF-PRD, in which a rule is a construct that fires and changes state, and it does not adopt the decision table sense of DMN 1.5, in which a rule is a row yielding an output. Section 10.8 states the conflict.

**Declaration.** The machine evaluable expression of a rule, in a declared expression language, over declared terms. The declaration is what an evaluation evaluates. This part does not specify the expression language; section 9.2 requires that it be registered and constrained.

**Statement.** The expression of a rule in natural language, intended to be read and approved by a person. A statement is not documentation of the declaration and is not derived from it. Where SBVR distinguishes the meaning of a rule from its expression, the statement is an expression; where Schematron places assertion text inside the schema, that text is a statement in this sense.

**Authority reference.** A citation, resolvable under `Part 1`, to the position in a controlled document version from which the rule derives its legitimacy. An authority reference identifies a clause, not a document.

**Example.** A subject state supplied with a rule, together with the verdict the rule's author asserts the rule yields for it. An example is executable and is the only mechanically checkable link between a statement and a declaration; see section 3.8.

**Guard.** The part of a rule that determines whether the rule applies to a subject at all. A guard that is false yields inapplicability, never satisfaction.

**Body.** The part of a rule that is evaluated where the guard holds, and whose truth value determines satisfaction or violation.

**Definitional rule.** A rule that is true by definition, so that a subject appearing to contradict it indicates defective data rather than a violated obligation. Term and sense follow SBVR 1.5, which also calls these structural rules and treats them as claims of necessity.

**Behavioural rule.** A rule that governs conduct and that can be violated by a person or an organisation. Term and sense follow SBVR 1.5, which also calls these operative rules and treats them as claims of obligation.

**Enforcement level.** A declared position on a graded scale stating how strictly a behavioural rule is to be enforced when a violation is detected. SBVR 1.5 defines the concept, states that it is independent of the guidance the rule gives and may change without the rule changing, and does not standardise the values. This part follows SBVR in all three respects and additionally forbids this component from acting on the level.

**Subject.** The thing an evaluation is about, identified by reference and accompanied by a state.

**Subject state.** The values of the subject that the evaluation read, pinned so that the evaluation can be reproduced.

**Verdict.** The outcome of evaluating one rule against one subject, drawn from the closed set of section 7.1.

**Finding.** A record of one thing that violated a rule, identifying what and where.

**Witness.** A subject position that a finding points at, or, for a satisfaction, an instance that was examined and found conforming.

**Vacuous satisfaction.** Satisfaction of a rule whose guard was true but which examined no instances, so that nothing was actually checked.

**Evaluation report.** The complete result of evaluating a rule set against a subject: every verdict, every finding, every pin, and the outcome of the evaluation as a whole.

**Rule set.** A named collection of rules evaluated together, whose membership is itself declared and versioned.

**Pin.** A recorded identifier and version of something an evaluation depended on, sufficient to obtain the same thing again.

**Evaluation instant.** The application time as of which the rule set and the reference data are resolved. Distinct from the time of evaluation.

**Knowledge time.** The time at which this component durably recorded a fact, assigned by the component. The term and its separation from application time follow `Part 1` section 2.1 and are used here unchanged.

**Occurrence time.** The time at which an act being described happened in the world, as asserted by an actor. Used here unchanged from `Part 1`.

**Indeterminate.** The third truth value: the value of a proposition that could not be evaluated. Distinct from false and from unknown in the sense of an open world assumption; section 6.2 states the semantics precisely.

**Derivation rule.** A rule that produces asserted values from other values rather than yielding a verdict. Corresponds in purpose to SHACL Rules, which the SHACL 1.2 family separates from constraint validation, and to the production sense of rule excluded from the definition above. Section 3.18 constrains derivation severely and section 6.6 states why.

**Drift.** A recorded condition in which two artifacts that were bound at approval are no longer consistent, most importantly where a rule's authority has been superseded or withdrawn while the rule has not changed.

**Budget.** The declared bound on the resource an evaluation may consume before it must stop and return a non result.

### 2.2 Clauses governing terminology

**P2-2.1 (MUST) Single meaning per term.** An implementation must use each term defined in section 2.1 with the meaning given there in all of its interfaces, records, reports and documentation.

**P2-2.2 (MUST NOT) No redefinition.** An implementation must not use a term defined in section 2.1 for a different concept, and must not use a different term for a concept defined in section 2.1 in any interface specified by this part.

**P2-2.3 (MUST) Rule sense declared.** An implementation must declare, in documentation exposed to any author of a rule, that "rule" carries the sense of section 2.1 and not the production or decision table senses, and must not accept an artifact in either of the other senses as a rule under this part.

**P2-2.4 (MUST NOT) No collapsing of verdict and enforcement.** An implementation must not use one term or one field for a verdict and for an enforcement level, a severity, or an action.

**P2-2.5 (MUST NOT) No collapsing of declaration and statement.** An implementation must not use one field for both, must not derive either from the other, and must not present a rendering of the declaration as the statement.

**P2-2.6 (MUST NOT) No collapsing of inapplicability and satisfaction.** An implementation must not use one term or one value for both.

**P2-2.7 (MUST NOT) No collapsing of the three clocks.** An implementation must not use one term or one field for more than one of evaluation instant, knowledge time and occurrence time.

**P2-2.8 (SHOULD) Term registry.** An implementation should publish the terms it adds beyond section 2.1, with definitions, as a controlled document under `Part 1`.
## 3. Data model

The model is stated as entities with typed fields. For each field the model gives its type, whether it is required, its cardinality, and what its absence means. Absence semantics are stated because a field that is optional without a stated meaning for absence is a field whose readers will each invent a different meaning, and in this component the commonest such invention is that a missing input is a false input.

### 3.1 Type vocabulary

The types below are used throughout the model. Each is a constraint on a value space, not a serialisation. Serialisation is out of scope.

| Type | Value space | Notes |
| --- | --- | --- |
| `ID` | An opaque, globally unique, immutable identifier | Never reused. Never parsed for meaning. |
| `URN` | A persistent name in a declared namespace | Resolvable by the component that owns the namespace. |
| `ATIME` | An instant in application time | The time dimension in which rules are in force. Corresponds to application time in `Part 1`. |
| `KTIME` | An instant in knowledge time, assigned by this component | Never accepted from a caller. |
| `OTIME` | An instant asserted by an actor as when an act occurred | Never assigned by this component. |
| `SEQ` | A monotonically increasing ordinal within a named stream | Total order within the stream only. |
| `DIGEST` | An algorithm identifier and a value | Algorithm from the registry of section 9.7. |
| `ENUM` | A member of a named closed or registered set | The set is named at every point of use. |
| `TEXT` | A sequence of characters intended for a person | Carries a `LANG`. |
| `LANG` | A language tag per BCP 47 | Required wherever `TEXT` appears. |
| `EXPR` | An expression in a named, versioned expression language | Opaque to this model. The language is registered under section 9.2. |
| `TRUTH` | One of `TRUE`, `FALSE`, `INDETERMINATE` | The three valued domain of section 6.2. |
| `PATH` | A locator into a subject state, in a named path scheme | Registered under section 9.4. Identifies a witness. |
| `CITEREF` | A citation resolvable under `Part 1`, carrying its mode | Pinned or as of, per `Part 1` section 2.1. |
| `PIN` | An identity and a version of a depended upon artifact | Sufficient to obtain the identical artifact again. |
| `ACTOR` | An opaque reference to a person, organisation or automated agent | Resolved elsewhere. Carries its kind. |
| `AUTHREF` | A reference to an authorisation decision made by `Part 7` | Recorded, never evaluated here. |
| `COUNT` | A non negative integer | Where a count is reported, its grain is stated. |
| `BUDGET` | A resource kind and a bound | Section 6.7. |
| `DURATION` | A length of time, independent of any instant | |

**P2-3.1 (MUST) Declared types.** An implementation must be able to state, for every field it holds that corresponds to a field in this section, which type of the table above it carries.

**P2-3.2 (MUST NOT) No semantic identifiers.** An implementation must not derive the meaning, classification, severity, version or applicability of a rule from the characters of its `ID` or `URN`.

**P2-3.3 (MUST) Language tag present.** An implementation must record a `LANG` with every `TEXT` value, and must not default it silently.

**P2-3.4 (MUST NOT) No caller supplied knowledge time.** An implementation must assign every `KTIME` itself and must reject a request that supplies one.

**P2-3.5 (MUST) Path scheme named.** An implementation must record the path scheme with every `PATH`, and must not rely on a single implicit scheme.

### 3.2 The triad: declaration, statement, authority

This section is the reason the part exists in the form it does, and every later section depends on it.

A rule is three things at once, and they are three artifacts rather than one artifact with three views.

The **declaration** is the expression that runs. It is precise, it is checkable, and it is unreadable to most of the people the rule governs.

The **statement** is the sentence a person approves. It is readable, it is what appears in a procedure, and it is not a rendering of the declaration. It cannot be, because a rendering of the declaration would be readable only in the sense that a decompilation is readable, and because the statement is frequently the older artifact: someone wrote the sentence, and someone else later wrote an expression they believed captured it.

The **authority reference** is the citation to the clause of a controlled document from which the rule derives its legitimacy. Without it a rule is an assertion by whoever typed it. With it, and only with it, the question "who says so" has an answer that survives the departure of the person who typed it.

The three are bound at approval and drift afterwards. All three kinds of drift occur, and each is invisible without a mechanism designed to see it.

**Declaration drifts from statement.** Someone corrects the expression to handle a case, and does not update the sentence. The organisation now believes one thing and enforces another. This is undetectable in general, because establishing that an expression means what a sentence says is not mechanically decidable. What is mechanically checkable is agreement on worked examples, which is why section 3.8 requires them and treats them as the bridge rather than as tests.

**Statement drifts from declaration.** Someone rewrites the sentence for clarity, changing its meaning, and does not touch the expression. Detectable only by requiring that any change to either produce a new version of the rule requiring fresh approval, which section 3.4 does.

**Authority drifts from both.** The clause the rule cites is superseded or withdrawn, and the rule does not change. This is the most dangerous of the three, because nothing about the rule changed, no deployment occurred, and no one was notified. The rule continues to be enforced on the authority of a clause that no longer exists. It is also the only one of the three that can be detected mechanically and completely, because `Part 1` can report the status of the cited version at any time. Section 3.7 requires that detection and requires that the response be a signal rather than a silent disable, on the ground that silently disabling a rule changes what the organisation permits without anyone deciding to change it.

**P2-3.6 (MUST) Three artifacts, separately stored.** An implementation must hold the declaration, the statement and the authority reference of a rule as three distinct fields, each independently readable.

**P2-3.7 (MUST NOT) No derivation between them.** An implementation must not generate the statement from the declaration, must not generate the declaration from the statement, and must not present either as evidence of the content of the other.

**P2-3.8 (MUST) Bound at approval.** An implementation must record, for each approved rule version, a digest computed over the declaration, the statement, the example set and the authority reference together, per clause P2-3.24.

**P2-3.9 (MUST) Drift detectable.** An implementation must be able to report, for every rule admitted for evaluation, whether the version of the authority it cites is currently in force, per section 3.7.

**P2-3.10 (MUST NOT) No silent disable on drift.** An implementation must not cease evaluating a rule, and must not alter its verdict, because the rule's authority has been superseded or withdrawn.

**P2-3.11 (MUST) Correspondence claim recorded.** An implementation must record, with each rule version, the identity of the actor who asserted that the declaration expresses the statement, and must record that assertion as an assertion rather than as a verified fact.

### 3.3 Entity inventory

The model has the following entities. Fields are given in the sections that follow. Every entity is immutable once written: a change is a new row, and nothing specified in this part is ever updated in place, for the reasons `Part 1` section 3.2 gives and for the additional reason that a verdict is a historical fact about what a system concluded at a time, and a historical fact that can be edited is not evidence.

| Group | Entity | Purpose |
| --- | --- | --- |
| Rule | `rule_lineage` | The persistent identity of a rule across its versions. |
| Rule | `rule_version` | One immutable state of a rule: declaration, statement, classification, metadata. |
| Rule | `rule_statement` | The prose statement of a rule version, per language. |
| Rule | `rule_authority` | The authority reference of a rule version. |
| Rule | `rule_example` | One worked example bound to a rule version. |
| Rule | `rule_binding_digest` | The digest binding the artifacts of a rule version. |
| Rule | `rule_classification` | Definitional or behavioural, and the enforcement level where behavioural. |
| Rule | `rule_term_reference` | A term the declaration uses, and the definition it refers to. |
| Rule | `rule_drift_observation` | An observed inconsistency between bound artifacts. |
| Set | `rule_set_lineage` | The persistent identity of a rule set. |
| Set | `rule_set_version` | One immutable membership of a rule set. |
| Set | `rule_set_member` | One rule lineage or version in a rule set version. |
| Set | `rule_set_analysis` | A recorded static analysis result over a rule set version. |
| Evaluation | `evaluation_request` | What was asked, including the pins the caller supplied. |
| Evaluation | `evaluation_pin` | One artifact an evaluation depended on, with its version. |
| Evaluation | `subject_state` | The subject values the evaluation read. |
| Evaluation | `evaluation_run` | One execution: its budget, its clocks, its outcome. |
| Evaluation | `verdict` | The outcome for one rule in one run. |
| Evaluation | `finding` | One thing that violated a rule, with its witness. |
| Evaluation | `witness` | A subject position examined, whether conforming or not. |
| Evaluation | `evaluation_report` | The assembled result of a run. |
| Evaluation | `evaluation_signal` | A condition observed during a run that is not a verdict. |
| Derivation | `derivation_rule_version` | A rule that asserts values rather than yielding verdicts. |
| Derivation | `derived_assertion` | A value produced by a derivation rule in a run. |
| Derivation | `derivation_stratum` | The declared stratum of a derivation rule, per section 6.6. |
| Registry | `expression_language_registration` | A registered expression language and its constraints. |
| Registry | `path_scheme_registration` | A registered path scheme. |
| Registry | `enforcement_level_registration` | A registered enforcement level. |
| Registry | `verdict_code_registration` | A registered code within a closed verdict class. |

**P2-3.12 (MUST) Entity coverage.** An implementation must be able to state, for every entity in the table above, where the information it carries is held, or that the entity is not applicable because the corresponding optional capability is not provided.

**P2-3.13 (MUST NOT) No update in place.** An implementation must not represent any state change specified by this part as a modification or deletion of a previously written row, tuple, object or event.

**P2-3.14 (MUST NOT) No verdict amendment.** An implementation must not modify a recorded verdict, and must record a corrected conclusion as a further evaluation run whose relation to the earlier run is recorded.

### 3.4 Rule identity and version

Rule identity is split between this component and `Part 1`, and the split is the single most important boundary in the part.

`Part 1` owns the version identity, the approval, the effectivity, the supersession and the retention of the artifact that carries the rule. This component owns the addressable identity of the rule as an evaluable thing, its classification, the bindings among its artifacts, and everything about its evaluation.

The reason for the split is that a rule must be reviewable and datable, and neither property is achievable by a component whose job is evaluation. The reason for not delegating the whole of identity is that a rule needs an identifier that a verdict can point at and that survives a rule moving from one document to another.

`rule_lineage` fields:

| Field | Type | Required | Cardinality | Absence means |
| --- | --- | --- | --- | --- |
| `lineage_id` | `ID` | yes | 1 | n/a |
| `lineage_urn` | `URN` | yes | 1 | n/a |
| `created_ktime` | `KTIME` | yes | 1 | n/a |
| `label` | `TEXT` | yes | 1..n | n/a. One per `LANG`. |
| `retired_ktime` | `KTIME` | no | 0..1 | The lineage has not been retired. Absence is not a claim that it is in use. |

`rule_version` fields:

| Field | Type | Required | Cardinality | Absence means |
| --- | --- | --- | --- | --- |
| `version_id` | `ID` | yes | 1 | n/a |
| `lineage_id` | `ID` | yes | 1 | n/a |
| `document_citation` | `CITEREF` | yes | 1 | n/a. The `Part 1` version that carries this rule, pinned. |
| `document_locator` | `PATH` | yes | 1 | n/a. The position within that version. |
| `declaration` | `EXPR` | yes | 1 | n/a |
| `expression_language` | `PIN` | yes | 1 | n/a. Language identity and version. |
| `guard` | `EXPR` | no | 0..1 | The rule applies to every subject of its declared kind. Absence is a positive claim of universal applicability, not an omission. |
| `subject_kind` | `URN` | yes | 1..n | n/a |
| `created_ktime` | `KTIME` | yes | 1 | n/a |
| `authored_by` | `ACTOR` | yes | 1..n | n/a |
| `derived_from_version_id` | `ID` | no | 0..1 | This is the first version of the lineage, or the derivation was not recorded. The two cases are distinguished by `first_version`. |
| `first_version` | `TRUTH` | yes | 1 | n/a |
| `superseded_note` | `TEXT` | no | 0..1 | No note was recorded. Supersession itself is not recorded here; it is a `Part 1` fact. |

**P2-3.15 (MUST) Version identity obtained, not assigned.** An implementation must record the `Part 1` citation and locator of every rule version and must not treat its own `version_id` as the authoritative version identity of the rule.

**P2-3.16 (MUST NOT) No approval state held.** An implementation must not hold a status, approval record, signature or effective date for a rule version, and must obtain all of them by resolution against `Part 1`.

**P2-3.17 (MUST) Locator to a clause.** An implementation must record a `document_locator` that identifies the position of the rule within the cited version, and must not cite the version alone.

**P2-3.18 (MUST) Absent guard is a claim.** An implementation must treat an absent `guard` as an assertion that the rule applies to every subject of its declared kinds, and must record that assertion, per section 3.9.

**P2-3.19 (MUST) Subject kind declared.** An implementation must record at least one `subject_kind` for every rule version and must not evaluate a rule against a subject of an undeclared kind.

**P2-3.20 (MUST NOT) No implicit versioning.** An implementation must not create a new `rule_version` by editing an existing one, and must record every change to a declaration, guard, statement, example set or authority reference as a new version.

### 3.5 The declaration

The declaration is opaque to this model. What the model requires is not a syntax but a set of properties, because the properties are what make an evaluation reproducible and the syntax is what makes it convenient.

`rule_version.declaration` carries an `EXPR` whose language is pinned. The language must be registered under section 9.2, and registration requires that the language satisfy the constraints below. The constraints are stated as clauses because each of them, if violated, makes some requirement elsewhere in this part unachievable.

**P2-3.21 (MUST) Pure expressions.** An implementation must not admit a declaration that reads any state other than the subject state, the pinned reference data and the pinned derived assertions, and must not admit a declaration that writes anything.

**P2-3.22 (MUST NOT) No unbounded computation.** An implementation must not admit a declaration in a language that permits unbounded recursion or unbounded iteration without a bound the implementation can enforce, per section 6.7.

**P2-3.23 (MUST NOT) No ambient time.** An implementation must not admit a declaration that reads a clock, and must require that every temporal comparison be against a value supplied in the evaluation request, per section 6.5.

**P2-3.24 (MUST) Binding digest over the whole.** An implementation must compute the binding digest of clause P2-3.8 over a declared canonical form of the concatenation of declaration, guard, every statement, every example and the authority reference, and must record the canonical form profile used.

**P2-3.25 (MUST NOT) No embedded action.** An implementation must not admit a declaration containing an action, an effect, a notification, a message dispatch or an assignment to the subject.

**P2-3.26 (MUST NOT) No embedded message.** An implementation must not admit a declaration that constructs the text a person will read, and must obtain that text from the statement, per clause P2-3.31.

**P2-3.27 (MUST NOT) No embedded severity.** An implementation must not admit a declaration whose value or branch determines an enforcement level or a severity.

**P2-3.28 (MUST) External randomness excluded.** An implementation must not admit a declaration that reads a random source, a generated identifier or any other value that varies between evaluations with identical pins.

### 3.6 The statement

`rule_statement` fields:

| Field | Type | Required | Cardinality | Absence means |
| --- | --- | --- | --- | --- |
| `statement_id` | `ID` | yes | 1 | n/a |
| `version_id` | `ID` | yes | 1 | n/a |
| `lang` | `LANG` | yes | 1 | n/a |
| `text` | `TEXT` | yes | 1 | n/a |
| `is_authoritative_language` | `TRUTH` | yes | 1 | n/a |
| `modality` | `ENUM` | yes | 1 | n/a. One of `OBLIGATION`, `PROHIBITION`, `NECESSITY`, `IMPOSSIBILITY`, `PERMISSION`, `GUIDANCE`. |
| `guidance_text` | `TEXT` | no | 0..1 | The statement itself is the guidance message. |
| `created_ktime` | `KTIME` | yes | 1 | n/a |

The `modality` enumeration follows SBVR 1.5, which grounds rules in claims of obligation and of necessity and which treats an alethic claim and a deontic claim as different kinds of proposition. The distinction matters here operationally rather than philosophically: a claim of necessity that appears to be contradicted by a subject means the subject is wrong, and a claim of obligation that is contradicted means somebody did something they should not have. Those are different findings requiring different responses, and a component that returns the same verdict for both has discarded the difference.

The `guidance_text` field exists because the message a person reads when a rule is violated is part of the rule and not part of the code that reports it. This follows the treatment in SBVR commentary, where the rule statement is the guidance message, and in Schematron, where the natural language assertion text sits inside the assertion. Where the message is separated from the rule, it is maintained by different people on a different schedule, and the drift between them is the drift of section 3.2 in its most visible form.

**P2-3.29 (MUST) Statement in at least one language.** An implementation must hold at least one `rule_statement` for every rule version, and must designate exactly one language as authoritative.

**P2-3.30 (MUST NOT) No translated statement as authoritative.** An implementation must not designate more than one language authoritative and must not treat a translation as independently governing, consistently with `Part 1` clause P1-3.31.

**P2-3.31 (MUST) Message from the statement.** An implementation must derive any text presented to a person on violation from the statement or its `guidance_text`, and must not construct it in the evaluator.

**P2-3.32 (MUST) Modality recorded.** An implementation must record a `modality` for every statement, and must not default it.

**P2-3.33 (MUST NOT) No modality inference.** An implementation must not infer modality from the declaration, from the classification, or from the words of the statement.
### 3.7 Authority binding and drift

`rule_authority` fields:

| Field | Type | Required | Cardinality | Absence means |
| --- | --- | --- | --- | --- |
| `authority_id` | `ID` | yes | 1 | n/a |
| `version_id` | `ID` | yes | 1 | n/a |
| `citation` | `CITEREF` | yes | 1 | n/a |
| `locator` | `PATH` | yes | 1 | n/a. The clause within the cited version. |
| `basis` | `ENUM` | yes | 1 | n/a. One of `REGULATION`, `CONTRACT`, `INTERNAL_POLICY`, `STANDARD`, `MANAGEMENT_DECISION`, `UNDECLARED`. |
| `asserted_by` | `ACTOR` | yes | 1 | n/a |
| `asserted_ktime` | `KTIME` | yes | 1 | n/a |
| `interpretation_note` | `TEXT` | no | 0..1 | The rule is asserted to follow from the cited clause without interpretation. Absence is a stronger claim than presence, not a weaker one. |

The `UNDECLARED` member of `basis` exists because the alternative to admitting that a rule has no traceable authority is a system in which every rule claims one falsely. A rule whose basis is `UNDECLARED` is admissible and evaluable; it is simply reportable as such, and section 8.5 requires that the count of such rules be a standing signal. A rule set in which most rules have no declared authority is a rule set nobody can review, and the number is the only way anyone finds out.

The `interpretation_note` field carries the reasoning where the rule does not follow from the clause mechanically. Most rules of any consequence require interpretation: a clause says records must be retained for an appropriate period and someone decided that appropriate means seven years. The seven is not in the clause. Recording where the seven came from is the difference between a defensible rule and a number of unknown origin, and the absence of the note asserts that no such step was taken.

Drift observation. Because `Part 1` can report the status of a cited version at any knowledge time, the component can compare the status at approval with the status now. `rule_drift_observation` records the comparison.

| Field | Type | Required | Cardinality | Absence means |
| --- | --- | --- | --- | --- |
| `observation_id` | `ID` | yes | 1 | n/a |
| `version_id` | `ID` | yes | 1 | n/a |
| `kind` | `ENUM` | yes | 1 | n/a. One of `AUTHORITY_SUPERSEDED`, `AUTHORITY_WITHDRAWN`, `AUTHORITY_UNRESOLVABLE`, `AUTHORITY_LOCATOR_RETIRED`, `EXAMPLE_DISAGREES`, `BINDING_DIGEST_MISMATCH`, `TERM_DEFINITION_CHANGED`, `REFERENCE_SET_MEMBER_REMOVED`. |
| `observed_ktime` | `KTIME` | yes | 1 | n/a |
| `detail` | `TEXT` | yes | 1 | n/a |
| `resolution_outcome` | `PIN` | no | 0..1 | The observation has not been addressed. Never means it was found not to matter. |

**P2-3.34 (MUST) Authority per rule version.** An implementation must hold exactly one `rule_authority` for every rule version.

**P2-3.35 (MUST) Locator, not document.** An implementation must record a `locator` identifying the clause relied upon, and must not record a citation to a whole document as the authority for a rule.

**P2-3.36 (MUST) Undeclared authority is declared as such.** An implementation must record `basis` as `UNDECLARED` where no authority can be identified, and must not record a plausible authority in its place.

**P2-3.37 (MUST) Interpretation recorded where present.** An implementation must record an `interpretation_note` wherever a value, threshold, period or enumeration in the declaration does not appear in the cited clause.

**P2-3.38 (MUST) Drift checked on a declared cycle.** An implementation must check the resolvability and status of every rule authority on a declared cycle, must record a `rule_drift_observation` for every adverse finding, and must declare the cycle length.

**P2-3.39 (MUST) Drift reported with the verdict.** An implementation must include, with every verdict, whether an unresolved drift observation exists for the rule version evaluated, per section 3.15.

**P2-3.40 (MUST NOT) No drift suppression.** An implementation must not permit a drift observation to be closed other than by recording a resolution outcome referencing a new rule version, a new authority assertion, or a recorded decision that the rule is to continue unchanged.

**P2-3.41 (MUST NOT) No inference from silence.** An implementation must not treat the absence of a drift observation as evidence that the authority is in force, where the check of clause P2-3.38 has not been performed within its declared cycle.

### 3.8 Examples as the bridge

A statement and a declaration cannot be mechanically shown to agree. Establishing that an arbitrary expression means what an arbitrary sentence says is not a decidable problem, and no standard reviewed for this part claims otherwise.

What can be done is narrower and useful. If the author of the rule supplies subject states together with the verdict they assert the rule yields, then the declaration can be run against them. Agreement does not prove correspondence. Disagreement proves the absence of it. That asymmetry is the whole value: the examples cannot confirm that the declaration expresses the statement, but they can and do catch the case where it demonstrably does not.

This is why examples are specified here as part of the rule rather than in section 12 as a testing concern delegated to `Part 12`. They are not tests of the implementation. They are a component of the rule's meaning, they are approved with it, they are included in its binding digest, and a rule whose examples disagree with its declaration is a defective artifact rather than a passing rule with a failing test.

`rule_example` fields:

| Field | Type | Required | Cardinality | Absence means |
| --- | --- | --- | --- | --- |
| `example_id` | `ID` | yes | 1 | n/a |
| `version_id` | `ID` | yes | 1 | n/a |
| `subject_state` | `PIN` | yes | 1 | n/a. A pinned subject state, held as an artifact. |
| `asserted_verdict` | `ENUM` | yes | 1 | n/a. A member of the verdict set of section 7.1. |
| `asserted_finding_paths` | `PATH` | no | 0..n | For a violation, no witness position is asserted. Permitted but weaker. |
| `rationale` | `TEXT` | yes | 1 | n/a. Why this example is included. |
| `kind` | `ENUM` | yes | 1 | n/a. One of `SATISFYING`, `VIOLATING`, `INAPPLICABLE`, `INDETERMINATE`, `BOUNDARY`. |
| `authored_by` | `ACTOR` | yes | 1 | n/a |
| `created_ktime` | `KTIME` | yes | 1 | n/a |

**P2-3.42 (MUST) Minimum example set.** An implementation must not admit a rule version for evaluation unless its example set contains at least one example of kind `SATISFYING` and at least one of kind `VIOLATING`.

**P2-3.43 (MUST) Inapplicability exemplified where a guard exists.** An implementation must not admit a rule version carrying a guard unless its example set contains at least one example of kind `INAPPLICABLE`.

**P2-3.44 (SHOULD) Indeterminacy exemplified.** An implementation should require at least one example of kind `INDETERMINATE` for every rule version whose declaration reads a field that may be absent or withheld.

**P2-3.45 (MUST) Examples executed on admission.** An implementation must evaluate every example of a rule version before admitting the version for evaluation, and must record the outcome.

**P2-3.46 (MUST NOT) No admission on disagreement.** An implementation must not admit a rule version for evaluation where any example yields a verdict other than its `asserted_verdict`.

**P2-3.47 (MUST) Examples re executed on dependency change.** An implementation must re execute the example set of every rule version affected by a change to a pinned expression language version, reference data version or term definition, and must record a `rule_drift_observation` of kind `EXAMPLE_DISAGREES` on any disagreement.

**P2-3.48 (MUST NOT) No generated examples as the bridge.** An implementation must not satisfy clause P2-3.42 with examples produced by executing the declaration, and must record the provenance of every example.

**P2-3.49 (MUST) Examples in the binding digest.** An implementation must include the example set in the binding digest of clause P2-3.24, so that adding or removing an example produces a new rule version.

**P2-3.50 (MUST NOT) No correspondence claim from agreement.** An implementation must not report, present or record that a declaration has been shown to express its statement on the basis of example agreement.

### 3.9 Guard and body

A rule has two evaluable parts and they mean different things. The guard asks whether the rule is about this subject. The body asks whether this subject conforms.

The distinction is load bearing because folding the guard into the body converts inapplicability into satisfaction, and the two are not the same fact. A report saying that a rule was satisfied asserts that the rule was checked and held. A report saying it did not apply asserts that the rule was never in question. An auditor reading a hundred satisfied verdicts, ninety of which are actually inapplicability, has been told that ninety checks were performed that were not.

The mechanism of the conflation is simple and almost always accidental. An author writes the whole rule as one implication: if the subject is a controlled document then its review date must be set. Evaluated as a material implication, that expression is true for every subject that is not a controlled document. Every uncontrolled document in the estate now reports as satisfying the review date rule. Nothing was checked. The verdict is not false, in the logical sense, and it is useless.

**P2-3.51 (MUST) Guard evaluated separately.** An implementation must evaluate the guard of a rule before its body and must not evaluate the body where the guard did not yield `TRUE`.

**P2-3.52 (MUST) Guard false yields inapplicability.** An implementation must return `NOT_APPLICABLE` where the guard yielded `FALSE`, and must not return a satisfaction verdict.

**P2-3.53 (MUST) Guard indeterminate yields a non result.** An implementation must return the appropriate `INDETERMINATE` subclass of section 7.2 where the guard yielded `INDETERMINATE`, and must not return `NOT_APPLICABLE`.

**P2-3.54 (MUST NOT) No implication as a guard.** An implementation must not admit a declaration in which the applicability condition appears as the antecedent of an implication in the body, where the expression language permits the condition to be expressed as a guard.

**P2-3.55 (MUST) Guard recorded in the verdict.** An implementation must record with every verdict the truth value the guard yielded.

**P2-3.56 (MUST NOT) No guard side effects.** An implementation must not admit a guard that derives, asserts or caches any value used by the body other than the binding of the instances the body will examine.

### 3.10 Classification and enforcement level

`rule_classification` fields:

| Field | Type | Required | Cardinality | Absence means |
| --- | --- | --- | --- | --- |
| `classification_id` | `ID` | yes | 1 | n/a |
| `version_id` | `ID` | yes | 1 | n/a |
| `kind` | `ENUM` | yes | 1 | n/a. `DEFINITIONAL` or `BEHAVIOURAL`. |
| `enforcement_level` | `ENUM` | no | 0..1 | Required where `kind` is `BEHAVIOURAL`; must be absent where `DEFINITIONAL`. |
| `enforcement_level_scheme` | `PIN` | no | 0..1 | Required wherever `enforcement_level` is present. |
| `violation_response_reference` | `URN` | no | 0..n | No response procedure has been associated. Never means no response is required. |
| `asserted_by` | `ACTOR` | yes | 1 | n/a |
| `asserted_ktime` | `KTIME` | yes | 1 | n/a |

The classification is the SBVR distinction between definitional and behavioural rules, and this part adopts it because the two have different failure meanings. A definitional rule is a claim of necessity: if the subject appears to contradict it, the subject is defective, or the definition is wrong, or the rule is wrong, and in no case has anyone violated an obligation. A behavioural rule is a claim of obligation: it can be violated, and a violation is a fact about conduct.

The consequence for this part is that the two produce different verdicts. Section 7.1 provides `VIOLATED` for a behavioural rule and `CONTRADICTED` for a definitional one, and the separation exists so that a report can distinguish a data quality defect from a compliance failure without a reader having to look up which kind of rule it was.

Enforcement level follows SBVR 1.5, which defines it as a position on a graded scale specifying the severity of action imposed to keep a behavioural rule in force, states explicitly that it is a separate question from the guidance the rule gives, states that it can change independently of the rule, and does not standardise the values. SBVR's commentary offers a set including strict enforcement, deferred enforcement, override by a pre authorised actor, post justified override, override with explanation, and guideline.

This part takes three positions on enforcement level and each of them is a position rather than a finding.

It is declared on the rule, per SBVR, and pinned to a registered scheme, because a level whose scale is not named is a word.

It is returned with the verdict and never applied. This component reports that a strictly enforced rule was violated. Whether the operation proceeds is not its business, and a component that both determines truth and applies consequence cannot be asked what is true without also being asked to act.

A change of enforcement level produces a new rule version. This diverges from SBVR's observation that the level can change independently of the rule, and the divergence is deliberate: independent change is correct as a statement about the business, and unworkable as a statement about a record, because a verdict issued last year must be interpretable against the level that applied last year. Section 13.5 records the divergence.

**P2-3.57 (MUST) Classification present.** An implementation must record a classification for every rule version and must not default it.

**P2-3.58 (MUST) Enforcement level only where behavioural.** An implementation must record an enforcement level for every behavioural rule version, and must not record one for a definitional rule version.

**P2-3.59 (MUST) Enforcement scheme pinned.** An implementation must pin the scheme and version from which an enforcement level is drawn, per section 9.5.

**P2-3.60 (MUST NOT) No action on the level.** An implementation must not vary its evaluation, its verdict, its report or its behaviour in any way on the basis of an enforcement level, and must return the level unaltered with the verdict.

**P2-3.61 (MUST) Distinct verdicts by classification.** An implementation must return `VIOLATED` for a failing behavioural rule and `CONTRADICTED` for a failing definitional rule, per section 7.1.

**P2-3.62 (MUST) Level change is a version change.** An implementation must treat a change of enforcement level or classification as producing a new rule version.

**P2-3.63 (MUST NOT) No severity in the message.** An implementation must not encode an enforcement level, a severity or a priority in the text of a statement or a guidance message as its only representation.
### 3.11 Rule set and membership

A rule set is what a caller evaluates. Its membership is declared and versioned, because the set of rules in force is itself a governed fact: a report saying that a subject satisfied every applicable rule is worthless unless someone can say which rules were in the set, and a set whose membership is computed at evaluation time from a query cannot answer that question about last year.

`rule_set_version` fields:

| Field | Type | Required | Cardinality | Absence means |
| --- | --- | --- | --- | --- |
| `set_version_id` | `ID` | yes | 1 | n/a |
| `set_lineage_id` | `ID` | yes | 1 | n/a |
| `document_citation` | `CITEREF` | yes | 1 | n/a. The `Part 1` version carrying the membership declaration. |
| `member_count` | `COUNT` | yes | 1 | n/a. Grain: one `rule_set_member`. |
| `created_ktime` | `KTIME` | yes | 1 | n/a |
| `analysis_reference` | `PIN` | no | 0..n | No static analysis has been recorded for this set version. |

`rule_set_member` fields:

| Field | Type | Required | Cardinality | Absence means |
| --- | --- | --- | --- | --- |
| `member_id` | `ID` | yes | 1 | n/a |
| `set_version_id` | `ID` | yes | 1 | n/a |
| `binding_mode` | `ENUM` | yes | 1 | n/a. `PINNED_VERSION` or `AS_OF_LINEAGE`. |
| `rule_version_id` | `ID` | no | 0..1 | Required where `binding_mode` is `PINNED_VERSION`. |
| `rule_lineage_id` | `ID` | no | 0..1 | Required where `binding_mode` is `AS_OF_LINEAGE`. |
| `member_ordinal` | `SEQ` | no | 0..1 | The set is unordered. Presence does not imply evaluation order; see clause P2-3.68. |

The two binding modes exist because both are needed and confusing them is a common defect. A set that pins rule versions is reproducible and stale: it evaluates the rules as they were when the set was assembled, and a corrected rule does not reach it. A set that binds lineages resolves each member as of the evaluation instant, so it is current and its membership is only reproducible if the evaluation instant is recorded. Both are legitimate. Neither is safe if the caller does not know which they have.

**P2-3.64 (MUST) Membership declared as content.** An implementation must express the membership of a rule set version as content of a `Part 1` document version, and must not compute membership from a query at evaluation time.

**P2-3.65 (MUST) Binding mode per member.** An implementation must record a binding mode for every member and must record the resolved rule version for every `AS_OF_LINEAGE` member in every evaluation that used it.

**P2-3.66 (MUST) Member count derived.** An implementation must derive `member_count` from the members recorded and must not accept it as an input.

**P2-3.67 (MUST NOT) No implicit membership.** An implementation must not evaluate a rule that is not a recorded member of the rule set version named in the request, and must not add a rule to an evaluation because it appeared applicable.

**P2-3.68 (MUST NOT) No ordinal as semantics.** An implementation must not vary any verdict on the basis of `member_ordinal`, and must not use it to resolve a conflict, establish a precedence or short circuit an evaluation.

**P2-3.69 (MUST) Set version recorded with every report.** An implementation must record the rule set version identity in every evaluation report.

### 3.12 Subject and subject state

The subject is what the rules are about. This component does not own it, does not store it as a system of record, and does not fetch it without a pin.

`subject_state` fields:

| Field | Type | Required | Cardinality | Absence means |
| --- | --- | --- | --- | --- |
| `state_id` | `ID` | yes | 1 | n/a |
| `subject_reference` | `URN` | yes | 1 | n/a |
| `subject_kind` | `URN` | yes | 1 | n/a |
| `state_digest` | `DIGEST` | yes | 1 | n/a |
| `canonical_form_profile` | `PIN` | yes | 1 | n/a |
| `source` | `ENUM` | yes | 1 | n/a. `SUPPLIED_BY_CALLER`, `FETCHED_UNDER_PIN` or `EXAMPLE_ARTIFACT`. |
| `source_pin` | `PIN` | no | 0..1 | Required where `source` is `FETCHED_UNDER_PIN`. |
| `as_of_atime` | `ATIME` | no | 0..1 | The state is not a temporal snapshot of the subject and no as of semantics are claimed. |
| `withheld_paths` | `PATH` | no | 0..n | No path was withheld. Distinct from a path being absent. |
| `absent_paths` | `PATH` | no | 0..n | No path was declared absent. Distinct from a path whose absence was not declared. |
| `received_ktime` | `KTIME` | yes | 1 | n/a |

Three states of a field must be distinguished and are the most frequent source of wrong verdicts in constraint systems.

A field can be **present with a value**. A field can be **absent**, meaning the subject has no value for it. A field can be **withheld**, meaning the subject has a value that this evaluation was not permitted to see.

Absent and withheld are different facts with different consequences. A rule requiring an approver name is violated by a subject with no approver, and cannot be evaluated on a subject whose approver is withheld. A component that receives a withheld field as an absence will report a violation of something that may well be conforming, and will do so in a way indistinguishable from a real violation. This is the mechanism by which access control silently manufactures compliance findings, and clause P2-3.72 exists to prevent it.

Undeclared absence is a fourth condition and it must not be silently merged with declared absence. If the subject state simply does not carry a path, the component cannot tell whether the subject has no value or whether the supplier omitted it. That is an indeterminate condition, not an absence, and clause P2-3.74 requires it to be treated as one unless the state declares completeness.

**P2-3.70 (MUST) Subject state pinned.** An implementation must record a digest and canonical form profile for every subject state it evaluated.

**P2-3.71 (MUST NOT) No unpinned fetch.** An implementation must not read subject values from any source without recording a pin sufficient to obtain the same values again, or recording that no such pin was obtainable.

**P2-3.72 (MUST) Withheld distinguished from absent.** An implementation must distinguish a withheld path from an absent path, must not treat a withheld path as absent, and must yield `INDETERMINATE` for any expression whose value depends on a withheld path.

**P2-3.73 (MUST) Completeness declared.** An implementation must record whether a subject state is declared complete for the subject kind, and must declare the meaning it assigns to an undeclared path in each case.

**P2-3.74 (MUST) Undeclared absence is indeterminate.** An implementation must treat a path that is neither present, nor declared absent, nor declared withheld as `INDETERMINATE` where the subject state is not declared complete.

**P2-3.75 (MUST NOT) No subject mutation.** An implementation must not write to the subject, must not request that it be written to, and must not return a modified subject state.

**P2-3.76 (MUST) As of semantics declared.** An implementation must record `as_of_atime` where the subject state was obtained as of an application time, and must not present a state without it as a temporal snapshot.

### 3.13 Term binding

A rule's declaration uses terms. The terms are governed definitions held in `Part 4`, and the code lists and reference sets whose members the rule tests against are held in `Part 10`. A rule that uses a term without recording which definition it means has no reviewable meaning, because the reviewer cannot tell whether the author meant the same thing the reader does.

`rule_term_reference` fields:

| Field | Type | Required | Cardinality | Absence means |
| --- | --- | --- | --- | --- |
| `reference_id` | `ID` | yes | 1 | n/a |
| `version_id` | `ID` | yes | 1 | n/a |
| `term_token` | `TEXT` | yes | 1 | n/a. The token as it appears in the declaration. |
| `definition_pin` | `PIN` | no | 0..1 | The term is a primitive of the expression language, or no definition was identified; the two are distinguished by `kind`. |
| `kind` | `ENUM` | yes | 1 | n/a. `GOVERNED_DEFINITION`, `REFERENCE_SET`, `LANGUAGE_PRIMITIVE` or `UNGOVERNED`. |
| `resolved_ktime` | `KTIME` | no | 0..1 | The reference has never been resolved. |

**P2-3.77 (MUST) Terms enumerated.** An implementation must record a term reference for every non primitive token in a declaration and must record its kind.

**P2-3.78 (MUST) Definition pinned.** An implementation must pin the definition version of every `GOVERNED_DEFINITION` term reference and must record the pin with every evaluation that used the rule.

**P2-3.79 (MUST) Ungoverned terms reportable.** An implementation must be able to report every term reference of kind `UNGOVERNED` across a rule set version, and must include the count in the signals of section 8.5.

**P2-3.80 (MUST) Definition change observed.** An implementation must record a `rule_drift_observation` of kind `TERM_DEFINITION_CHANGED` where a pinned definition has been superseded, and must not silently rebind to the successor.

**P2-3.81 (MUST NOT) No local definition.** An implementation must not hold a definition of a governed term, and must not permit a rule to define a term for its own use.

### 3.14 Evaluation request and pins

An evaluation is reproducible only if everything it depended on is recorded with enough precision to obtain it again. The pin set is therefore not diagnostic metadata; it is part of the result.

`evaluation_request` fields:

| Field | Type | Required | Cardinality | Absence means |
| --- | --- | --- | --- | --- |
| `request_id` | `ID` | yes | 1 | n/a |
| `set_reference` | `ID` | yes | 1 | n/a. A rule set version or lineage. |
| `set_binding_mode` | `ENUM` | yes | 1 | n/a. `PINNED_VERSION` or `AS_OF_LINEAGE`. |
| `evaluation_instant` | `ATIME` | yes | 1 | n/a. Never defaulted; see clause P2-3.83. |
| `knowledge_instant` | `KTIME` | no | 0..1 | Resolve rule versions against present belief. Where present, resolve against belief as at that instant. |
| `subject_reference` | `URN` | yes | 1..n | n/a |
| `subject_state_id` | `ID` | no | 0..n | The state is to be fetched under a pin rather than supplied. |
| `requested_by` | `ACTOR` | yes | 1 | n/a |
| `authorisation` | `AUTHREF` | no | 0..1 | The evaluation was not the subject of an authorisation decision. |
| `purpose` | `ENUM` | yes | 1 | n/a. Registered under section 9.6. |
| `budget_override` | `BUDGET` | no | 0..1 | The declared default budget applies. |
| `received_ktime` | `KTIME` | yes | 1 | n/a |

`evaluation_pin` fields:

| Field | Type | Required | Cardinality | Absence means |
| --- | --- | --- | --- | --- |
| `pin_id` | `ID` | yes | 1 | n/a |
| `run_id` | `ID` | yes | 1 | n/a |
| `kind` | `ENUM` | yes | 1 | n/a. One of `RULE_SET_VERSION`, `RULE_VERSION`, `EXPRESSION_LANGUAGE`, `TERM_DEFINITION`, `REFERENCE_SET`, `SUBJECT_STATE`, `DERIVED_ASSERTION_SET`, `PATH_SCHEME`, `ENFORCEMENT_SCHEME`, `MODEL_OUTPUT`. |
| `identity` | `URN` | yes | 1 | n/a |
| `version` | `TEXT` | yes | 1 | n/a |
| `digest` | `DIGEST` | no | 0..1 | The pinned artifact does not carry a digest. Reduces reproducibility and is reportable. |
| `obtained_ktime` | `KTIME` | yes | 1 | n/a |

The `evaluation_instant` is required rather than defaulted, and this is the clause most likely to be resisted, because defaulting it to the present is convenient and almost always what the caller wants. It is refused because a rule set resolved as of the present, in a request that did not say so, produces a verdict that cannot be distinguished from a verdict about a past state, and the distinction matters most in exactly the cases where someone is asking questions years later.

**P2-3.82 (MUST) Pin set complete.** An implementation must record a pin for every artifact its evaluation read, and must record a pin of every kind in the enumeration above that applied.

**P2-3.83 (MUST) Evaluation instant supplied.** An implementation must require an `evaluation_instant` in every request and must not default it to the time of the request.

**P2-3.84 (MUST) Knowledge instant defaults declared.** An implementation must declare its behaviour where `knowledge_instant` is absent, and must record the instant it used.

**P2-3.85 (MUST) Purpose recorded.** An implementation must record the declared purpose of every evaluation and must not permit an unregistered purpose.

**P2-3.86 (MUST NOT) No unpinned dependency.** An implementation must not complete an evaluation that read an artifact for which it could not record a pin, and must return the appropriate non result of section 7.2 instead.

**P2-3.87 (MUST) Digest absence reportable.** An implementation must be able to report every pin recorded without a digest, and must include the count in the signals of section 8.5.

**P2-3.88 (MUST NOT) No pin substitution.** An implementation must not substitute a later version of a pinned artifact, and must not treat a compatible successor as the pinned artifact.

### 3.15 The verdict

`verdict` fields:

| Field | Type | Required | Cardinality | Absence means |
| --- | --- | --- | --- | --- |
| `verdict_id` | `ID` | yes | 1 | n/a |
| `run_id` | `ID` | yes | 1 | n/a |
| `rule_version_id` | `ID` | yes | 1 | n/a |
| `subject_reference` | `URN` | yes | 1 | n/a |
| `outcome` | `ENUM` | yes | 1 | n/a. A member of the closed set of section 7.1. |
| `outcome_code` | `ENUM` | no | 0..1 | Required for `INDETERMINATE` and refusal outcomes; registered under section 9.8. |
| `guard_truth` | `TRUTH` | yes | 1 | n/a |
| `body_truth` | `TRUTH` | no | 0..1 | The body was not evaluated. |
| `witnesses_examined` | `COUNT` | yes | 1 | n/a. Grain: one instance bound by the guard and examined by the body. |
| `findings_count` | `COUNT` | yes | 1 | n/a. Grain: one `finding`. |
| `vacuous` | `TRUTH` | yes | 1 | n/a |
| `classification_kind` | `ENUM` | yes | 1 | n/a. Copied from the rule version, not re derived. |
| `enforcement_level` | `ENUM` | no | 0..1 | The rule is definitional. |
| `statement_reference` | `ID` | yes | 1 | n/a. The statement whose text a reader should be shown. |
| `authority_status` | `ENUM` | yes | 1 | n/a. One of `IN_FORCE`, `SUPERSEDED`, `WITHDRAWN`, `UNRESOLVABLE`, `NOT_CHECKED`. |
| `drift_open` | `TRUTH` | yes | 1 | n/a |
| `budget_consumed` | `TEXT` | yes | 1 | n/a. The resource and the amount. |
| `evaluated_ktime` | `KTIME` | yes | 1 | n/a |

The `vacuous` field records whether a satisfaction was reached without examining anything. A rule stating that every attachment of a submission must be signed is satisfied by a submission with no attachments, and the satisfaction is true and empty. Vacuous satisfaction is the quietest failure mode available to a constraint system, because it produces a green result on a subject that was never checked, and it is most likely to occur precisely where the data is most defective, since a missing collection is both the cause of the vacuity and the defect that ought to have been reported.

**P2-3.89 (MUST) One verdict per rule per subject per run.** An implementation must record exactly one verdict for each pair of rule version and subject in a run.

**P2-3.90 (MUST) Vacuity reported.** An implementation must record whether every satisfaction verdict was vacuous, and must derive the value from the count of witnesses examined rather than accepting it as an input.

**P2-3.91 (MUST NOT) No vacuous satisfaction as satisfaction.** An implementation must not present a vacuous satisfaction as a satisfaction without the vacuity, in any report, projection or interface.

**P2-3.92 (MUST) Witness count derived.** An implementation must derive `witnesses_examined` from the witnesses recorded and must state its grain.

**P2-3.93 (MUST) Authority status carried.** An implementation must record the authority status with every verdict, and must record `NOT_CHECKED` where the check of clause P2-3.38 was not current, rather than recording `IN_FORCE`.

**P2-3.94 (MUST) Statement reference carried.** An implementation must record with every verdict the identity of the statement a reader should be shown, and must not carry the message text in the verdict in place of the reference.

**P2-3.95 (MUST) Budget consumption recorded.** An implementation must record the budget consumed by every verdict.

**P2-3.96 (MUST NOT) No verdict without a rule version.** An implementation must not record a verdict against a rule lineage, and must record the resolved version.
### 3.16 Findings and witnesses

A verdict says that a rule was violated. A finding says what violated it. The difference is the difference between a report somebody can act on and a report somebody must investigate before acting.

SHACL 1.0 is the strongest specification anchor for this requirement. Its validation report is a first class artifact rather than a return code, and each result identifies the focus node, the path, the offending value, the source shape and a severity. Schematron in ISO/IEC 19757-3:2025 does the same in its own idiom, associating each assertion with the context node it fired against and with natural language text. Both standards treat the location of the failure as part of the result rather than as diagnostic output, and this part follows them.

`finding` fields:

| Field | Type | Required | Cardinality | Absence means |
| --- | --- | --- | --- | --- |
| `finding_id` | `ID` | yes | 1 | n/a |
| `verdict_id` | `ID` | yes | 1 | n/a |
| `witness_path` | `PATH` | yes | 1 | n/a |
| `path_scheme` | `PIN` | yes | 1 | n/a |
| `offending_value_digest` | `DIGEST` | no | 0..1 | The value was withheld, absent or not representable; `value_condition` states which. |
| `value_condition` | `ENUM` | yes | 1 | n/a. One of `PRESENT`, `ABSENT`, `WITHHELD`, `NOT_REPRESENTABLE`. |
| `sub_expression_reference` | `PATH` | no | 0..1 | The declaration was not decomposed, or the language does not support addressing sub expressions. |
| `finding_ordinal` | `SEQ` | yes | 1 | n/a. Position within the findings of this verdict, in a declared order. |
| `truncated_after` | `COUNT` | no | 0..1 | The finding set is complete. |

`witness` fields:

| Field | Type | Required | Cardinality | Absence means |
| --- | --- | --- | --- | --- |
| `witness_id` | `ID` | yes | 1 | n/a |
| `verdict_id` | `ID` | yes | 1 | n/a |
| `path` | `PATH` | yes | 1 | n/a |
| `conforming` | `TRUTH` | yes | 1 | n/a |
| `examined_ktime` | `KTIME` | yes | 1 | n/a |

Recording conforming witnesses as well as failing ones is more expensive and is required for one reason: it is the only way to distinguish a rule that examined ten thousand instances and found none failing from a rule that examined none. Both produce satisfaction. Only one of them checked anything, and section 3.15 requires the vacuity flag whose value can only be derived from this count.

Truncation is permitted because a rule violated by every row of a large collection produces a finding set nobody will read and a report that may not be transmissible. Truncation is required to be declared, because a truncated finding set that does not say it was truncated understates the problem and does so silently.

**P2-3.97 (MUST) Finding per violation.** An implementation must record at least one finding for every verdict of outcome `VIOLATED` or `CONTRADICTED`.

**P2-3.98 (MUST) Witness path in every finding.** An implementation must record a witness path and its scheme in every finding.

**P2-3.99 (MUST) Value condition recorded.** An implementation must record the value condition of every finding, and must not record a withheld or absent value as a present value with an empty digest.

**P2-3.100 (MUST) Truncation declared.** An implementation must record `truncated_after` where it did not record every finding, and must not present a truncated set as complete.

**P2-3.101 (MUST) Conforming witnesses counted.** An implementation must record or count every instance examined and found conforming, at a grain sufficient to derive `witnesses_examined`.

**P2-3.102 (MUST) Finding order declared.** An implementation must declare the order in which findings are ordinalled, and must not vary that order between evaluations with identical pins.

**P2-3.103 (MUST NOT) No finding without a verdict.** An implementation must not emit a finding that is not attached to a recorded verdict.

**P2-3.104 (SHOULD) Sub expression addressing.** An implementation should record which sub expression of the declaration produced each finding, where the expression language permits sub expressions to be addressed.

### 3.17 The evaluation report

`evaluation_report` fields:

| Field | Type | Required | Cardinality | Absence means |
| --- | --- | --- | --- | --- |
| `report_id` | `ID` | yes | 1 | n/a |
| `run_id` | `ID` | yes | 1 | n/a |
| `request_id` | `ID` | yes | 1 | n/a |
| `run_outcome` | `ENUM` | yes | 1 | n/a. Per section 7.6. |
| `verdict_count` | `COUNT` | yes | 1 | n/a. Grain: one `verdict`. |
| `counts_by_outcome` | `COUNT` | yes | 1..n | n/a. One per member of the section 7.1 set present. |
| `rules_not_evaluated` | `COUNT` | yes | 1 | n/a. Grain: one member of the rule set version. |
| `report_digest` | `DIGEST` | yes | 1 | n/a |
| `assembled_ktime` | `KTIME` | yes | 1 | n/a |

The report is the unit that is recorded, transmitted and cited. A caller may read one verdict from it, and a later reader needs the whole, which is why section 12.3 requires that the report rather than a summary be what `Part 3` records, and why clause P2-3.108 forbids reducing it to an aggregate on the way out.

The single most common defect in this area is a report reduced to a boolean at its edge. A caller asks whether the subject is compliant, and receives true or false. Everything specified in this part is then discarded at the last step: the vacuity, the indeterminacy, the drift, the pins. The boolean is also wrong, because there is no defensible way to fold indeterminacy into it, and every implementation that tries picks one of the two wrong answers and does not say which.

**P2-3.105 (MUST) Report is the result.** An implementation must return an evaluation report for every evaluation and must not return a verdict set without the report fields above.

**P2-3.106 (MUST) Counts derived with grain.** An implementation must derive every count in the report from the records it holds and must state the grain of each count.

**P2-3.107 (MUST) Unevaluated rules counted.** An implementation must record the number of rule set members for which no verdict was produced, and must record a verdict of an `INDETERMINATE` or refusal class for each rather than omitting it, per clause P2-1.13.

**P2-3.108 (MUST NOT) No boolean reduction.** An implementation must not expose an interface whose result for an evaluation is a single truth value, a pass indicator or a count of violations without the report.

**P2-3.109 (MUST) Report digest.** An implementation must record a digest over a declared canonical form of the report.

**P2-3.110 (MUST NOT) No summary in place of the report.** An implementation must not supply a summary to a component that will record the evaluation as evidence, per clause P2-12.6.

### 3.18 Derivation, and why it is fenced

A derivation rule produces asserted values. It is the production rule of PRR 1.0 and RIF-PRD, and the inferencing of the SHACL Rules specification, and it is a different thing from a constraint. This part permits derivation, treats it as an optional capability, and fences it, because the properties this part guarantees for constraint evaluation are properties that unrestricted derivation destroys.

RIF-PRD specifies the operational semantics of a production rule system as a loop: match the rules against the state, apply a conflict resolution strategy to choose which instance fires, act by changing the state, and repeat until a terminal state. Every one of those four steps is incompatible with something required here. Matching against mutable state means the verdict depends on evaluation order. Conflict resolution means the outcome depends on a strategy that is not itself a rule. Acting means the evaluation changes what it is evaluating. Looping means termination is a property of the rule set rather than of the engine.

The fence has four parts.

Derivation is separated from constraint evaluation into two phases, and the phases do not interleave. All derivation completes, then all constraints evaluate against the closure. A constraint never sees a partially derived state.

Derivation rules are stratified, and the stratum is declared rather than inferred. A rule in stratum n may read the output of strata below n and may not read its own stratum or above. This makes the closure computable in a declared number of passes and makes termination a property the component can check at admission rather than discover at run time.

Derivation is monotonic. A derivation rule may assert a value; it may not retract, overwrite or contradict one. Where two derivation rules assert different values for the same path, the result is a recorded conflict and a non result, not a resolution.

Conflict resolution by priority, salience, specificity or order is prohibited outright. Section 11.3 states the mechanism by which salience destroys reviewability: the rule set's behaviour is then determined by a set of integers that no author wrote down as a rule, that no authority document contains, and that nobody reviews.

`derived_assertion` fields:

| Field | Type | Required | Cardinality | Absence means |
| --- | --- | --- | --- | --- |
| `assertion_id` | `ID` | yes | 1 | n/a |
| `run_id` | `ID` | yes | 1 | n/a |
| `derivation_rule_version_id` | `ID` | yes | 1 | n/a |
| `path` | `PATH` | yes | 1 | n/a |
| `value_digest` | `DIGEST` | yes | 1 | n/a |
| `stratum` | `COUNT` | yes | 1 | n/a |
| `input_paths` | `PATH` | yes | 1..n | n/a. The paths read to produce this value. |
| `asserted_ktime` | `KTIME` | yes | 1 | n/a |

**P2-3.111 (MAY) Derivation supported.** An implementation may support derivation rules, and where it does not it must reject a rule set version containing one rather than ignoring the member.

**P2-3.112 (MUST) Phases separated.** An implementation that supports derivation must complete all derivation before evaluating any constraint, and must not evaluate a constraint against a partially derived state.

**P2-3.113 (MUST) Stratum declared.** An implementation must require a declared stratum on every derivation rule version and must not infer it from the dependency graph.

**P2-3.114 (MUST NOT) No same or higher stratum reads.** An implementation must not admit a derivation rule that reads a path asserted by its own stratum or a higher one.

**P2-3.115 (MUST) Monotonic derivation.** An implementation must not permit a derivation rule to retract or overwrite an asserted value.

**P2-3.116 (MUST) Conflicting derivation is a non result.** An implementation must return the appropriate non result of section 7.2 where two derivation rules assert different values for one path, and must record both assertions.

**P2-3.117 (MUST NOT) No conflict resolution strategy.** An implementation must not resolve a derivation conflict by priority, salience, specificity, recency, rule order or member ordinal.

**P2-3.118 (MUST) Derived values pinned and attributed.** An implementation must record, for every derived assertion, the rule version that produced it and the paths it read, and must include the derived assertion set in the pin set of the run.

**P2-3.119 (MUST) Derived values distinguishable.** An implementation must mark every derived value as derived in the state a constraint reads, and must not present a derived value as a subject value.

**P2-3.120 (MUST NOT) No derivation into the subject.** An implementation must not write a derived value to the subject or to any store outside the evaluation run.

### 3.19 Reference data

A rule that tests membership in a code list depends on the code list. A code list is a governed artifact in `Part 10` with its own versions, and a rule evaluated today against a list that gained a member last month may yield a different verdict from the same rule evaluated last year. That is correct behaviour and it is only correct if the list version is pinned, because otherwise the change is invisible and the two verdicts are irreconcilable.

The failure mode worth naming is removal. A code list member removed in a later version makes a historical subject that used it now unrecognised. A rule reading the current list reports a violation of a rule the subject satisfied when it was created. Pinning the list as of the evaluation instant is the correct behaviour and requires the reference component to retain superseded versions, which is the reciprocal obligation `Part 1` clause P1-12.18 and section 12.10 here both require of `Part 10`.

**P2-3.121 (MUST) Reference set pinned.** An implementation must pin the identity and version of every reference set an evaluation read.

**P2-3.122 (MUST) Reference set resolved as of the evaluation instant.** An implementation must resolve a reference set as of the `evaluation_instant` of the request, and must not read the current version where the instant is earlier.

**P2-3.123 (MUST) Unavailable reference set is a non result.** An implementation must return the appropriate non result of section 7.2 where a pinned reference set version cannot be obtained, and must not fall back to a later version or a cached copy of unknown version.

**P2-3.124 (MUST) Member removal observed.** An implementation must record a `rule_drift_observation` of kind `REFERENCE_SET_MEMBER_REMOVED` where a member relied upon by a rule's examples is absent from a later version of a pinned set.

**P2-3.125 (MUST NOT) No local reference data.** An implementation must not hold a reference set as its own data, and must not extend, correct or supplement one it obtained.

### 3.20 Projections

Nothing in this part is read by querying the stored rows directly. Every read is a projection: a pure function of the recorded facts, holding no state of its own, recomputable from the rows at any time. The reason is the reason `Part 1` gives for the same requirement, and one more specific to this component: a cached view of rule state that drifts from the rows will cause a rule set to be evaluated that nobody approved, and the drift will be invisible because the cache is what everybody reads.

The projections required are the following. Each is named because a name is what a clause elsewhere can refer to.

| Projection | Yields |
| --- | --- |
| `admitted_rules_at` | The rule versions admissible for evaluation at an application time and a knowledge time. |
| `rule_set_membership_at` | The resolved membership of a rule set at an application time and a knowledge time. |
| `rule_current_artifacts` | The declaration, statements, examples, authority and classification of a rule version as one assembled artifact. |
| `binding_integrity` | Whether the recorded binding digest of a rule version matches its current artifacts. |
| `authority_status_at` | The status of every rule's authority as at a knowledge time. |
| `open_drift` | Every drift observation without a resolution outcome. |
| `ungoverned_terms` | Every term reference of kind `UNGOVERNED`, by rule set version. |
| `unauthorised_rules` | Every rule version whose authority basis is `UNDECLARED`. |
| `example_agreement` | The most recent example execution outcome per rule version. |
| `verdict_history` | Every verdict for a subject, ordered by knowledge time, with its pins. |
| `verdict_divergence` | Where re evaluation of a recorded run under present pins yields a different outcome. |
| `vacuity_report` | Every satisfaction verdict that was vacuous, by rule and rule set version. |
| `indeterminacy_report` | Every indeterminate verdict by outcome code and by cause. |
| `budget_exhaustion_report` | Every run and verdict terminated by budget exhaustion. |

**P2-3.126 (MUST) Projections are pure.** An implementation must compute every projection above as a function of recorded rows alone, holding no state not derivable from them.

**P2-3.127 (MUST) Projection recomputable.** An implementation must be able to recompute every projection from the recorded rows and must be able to demonstrate agreement between a served projection and a recomputation.

**P2-3.128 (MUST) Named projections available.** An implementation must provide every projection in the table above, and must name each of them as named there in any interface it exposes.

**P2-3.129 (MUST NOT) No writes through a projection.** An implementation must not permit any state change to be effected by writing to a projection.

**P2-3.130 (MUST) Divergence projection.** An implementation must provide `verdict_divergence` and must be able to report, for any recorded run, whether re evaluation under present pins yields the same outcome for every verdict.

### 3.21 Worked demonstration

The demonstration shows the three drifts of section 3.2 occurring over seven years and shows what each read returns. It is not normative. It exists because a reader who has followed the field tables still cannot tell whether the model does the work claimed for it, and the only way to show that is to run it.

**2027.** A rule is authored. Its lineage is `L`, its version `V1`. Its statement, in English and authoritative, says that a controlled document must be reviewed at least every twenty four months. Its declaration compares an interval. Its authority cites clause `C-7.2` of policy document `D`, version `D2`, whose text says documents must be reviewed periodically; the interpretation note records that twenty four months was set by a management decision of 2026 and names it. Its classification is behavioural, enforcement level strict. Its example set has one satisfying, one violating, one boundary case at exactly twenty four months. Binding digest `H1` is computed. All rows are appended.

| row | relation | subject | detail |
| --- | --- | --- | --- |
| RV1 | rule_version | L, V1 | declaration `E1`, authority `D` `D2` `C-7.2`, digest `H1` |
| EX1 | rule_example | V1 | satisfying |
| EX2 | rule_example | V1 | violating |
| EX3 | rule_example | V1 | boundary |

**2028.** A subject `S` is evaluated. The request carries evaluation instant 2028-06-01 and no knowledge instant. The rule set version resolves to `RSV3` whose member binds `L` as of lineage; `L` resolves to `V1`. `S` has a review date twenty nine months old. The verdict is `VIOLATED`, one finding at path `/review/last_completed`, witnesses examined 1, vacuous false, authority status `IN_FORCE`, drift open false. The report is recorded with nine pins.

**2029.** Someone corrects the declaration to exclude documents whose lineage is retired, because the old expression flagged retired documents. A new version `V2` is created: new declaration, same statement, one new inapplicable example, new digest `H2`. The statement was not changed, and it does not mention retired documents. This is declaration drift from statement, and the model does not detect it: the examples pass, the digest is fresh, and nothing is wrong from the component's point of view. What the model does provide is that the change produced a version, that the version records who asserted that the declaration expresses the statement, and that the two artifacts sit side by side for a reviewer who reads both. Clause P2-3.11 and section 13.2 are the whole of what this part can offer here, and section 13.2 says so.

**2031.** Policy document `D` is revised. Version `D3` renumbers nothing but rewrites `C-7.2` to require review every twelve months. `L` still resolves to `V2`, whose declaration says twenty four. The drift check of clause P2-3.38 runs, resolves the authority citation, and finds that `D2` is superseded. It appends a drift observation.

| row | relation | subject | detail |
| --- | --- | --- | --- |
| DO1 | rule_drift_observation | V2 | `AUTHORITY_SUPERSEDED`, observed 2031-02-14, no resolution |

The rule continues to be evaluated, per clause P2-3.10, and every verdict issued from 2031-02-14 onward carries `authority_status` of `SUPERSEDED` and `drift_open` true. This is the case the part exists to catch. Nothing about the rule changed, no deployment happened, and the organisation is now enforcing twenty four months on the authority of a clause that says twelve. The verdict is still `VIOLATED` or `SATISFIED` as the case may be, because the component does not know which of the two numbers is right, and it says loudly that somebody needs to.

**2032.** A new version `V3` is authored with the twelve month interval, a rewritten statement, a fresh authority citation to `D3` `C-7.2`, and a resolution outcome appended to `DO1` naming `V3`.

**2034.** An investigation asks what governed subject `S` in 2028 and whether the answer would be the same today.

| question | parameters | result |
| --- | --- | --- |
| What was evaluated in 2028? | run of 2028-06-01 | `V1`, resolved from `L` under `RSV3`, nine pins, verdict `VIOLATED` |
| Would the same request return the same answer now? | `verdict_divergence` on that run | Yes for the verdict. The pins resolve, `V1` is obtainable, the subject state digest matches. |
| Does the current rule set give the same answer for `S`? | evaluation instant 2034, current set | Different rule version `V3`, different interval, possibly a different outcome. Not a divergence: a different question. |
| On whose authority was the 2028 verdict issued? | `authority_status_at` for `V1` as at 2028 | `D` `D2` `C-7.2`, in force at that time. |
| Was the rule ever enforced on a superseded authority? | `open_drift` history for `L` | Yes, `V2` from 2031-02-14 to 2032, with the observation and its resolution. |

The last row is the one that matters, and no component that stores a rule as code can produce it.

**P2-3.131 (MUST) Demonstration satisfiable.** An implementation must be able to answer every question in the table above for any rule lineage and subject within its retained history, using only the projections of section 3.20.
## 4. Interfaces

### 4.1 Interface principles

This section specifies operations by their obligations rather than by their signatures. No transport, encoding or naming convention is specified. What is specified is what each operation must accept, what it must record, what it must return, what it must refuse, and what a caller may and may not assume.

Operations divide into three groups: those that record rule artifacts, those that evaluate, and those that read. The division is not cosmetic. Recording operations write rows and never evaluate against a subject. Evaluating operations write rows describing what they did and never write rule artifacts. Reading operations write nothing except the access records of section 8.4.

**P2-4.1 (MUST) Operation classes separated.** An implementation must not provide an operation that both records a rule artifact and evaluates against a subject.

**P2-4.2 (MUST) Refusal is an outcome.** An implementation must return a refusal outcome of section 7.5 for any operation it declines, and must not return an outcome of another class in its place.

**P2-4.3 (MUST) Idempotence key accepted.** An implementation must accept a caller supplied idempotence key on every recording and evaluating operation and must honour it per section 6.3.

**P2-4.4 (MUST NOT) No partial recording.** An implementation must not record part of the artifact set of a rule version, and must record a rule version together with its statements, examples, authority, classification and term references or record none of them.

### 4.2 Recording operations

Each row states what the operation records, whether it is synchronous, and its principal refusals. The table is normative for the set of operations that must exist; it is not normative for their names.

| # | Operation | Records | Sync | Principal refusals |
| --- | --- | --- | --- | --- |
| 1 | Register rule lineage | `rule_lineage` | yes | Duplicate `lineage_urn` |
| 2 | Record rule version | `rule_version` | yes | Unregistered expression language; unresolvable document citation; declaration violating section 3.5 |
| 3 | Record statement | `rule_statement` | yes | No authoritative language; second authoritative language; absent modality |
| 4 | Record authority | `rule_authority` | yes | Citation to a document without a locator; unresolvable citation |
| 5 | Record example | `rule_example` | yes | Subject state not pinnable; asserted verdict not in the section 7.1 set |
| 6 | Record classification | `rule_classification` | yes | Enforcement level on a definitional rule; unpinned enforcement scheme |
| 7 | Record term references | `rule_term_reference` | yes | Unresolvable definition pin for a governed term |
| 8 | Compute and record binding digest | `rule_binding_digest` | yes | Incomplete artifact set |
| 9 | Admit rule version | example execution outcomes, admission record | yes | Example disagreement; missing satisfying or violating example; absent authority |
| 10 | Record rule set version | `rule_set_version` | yes | Member referencing an unadmitted rule version |
| 11 | Record rule set member | `rule_set_member` | yes | Binding mode without its corresponding identifier |
| 12 | Record rule set analysis | `rule_set_analysis` | either | Analysis referencing a different set version |
| 13 | Record derivation rule version | `derivation_rule_version`, `derivation_stratum` | yes | Same or higher stratum read; non monotonic assertion; derivation unsupported |
| 14 | Record drift observation | `rule_drift_observation` | yes | Unknown rule version |
| 15 | Record drift resolution | resolution outcome on an observation | yes | Resolution not referencing a version, authority or decision |
| 16 | Retire rule lineage | `retired_ktime` on the lineage | yes | Lineage is a member of an admitted rule set version |
| 17 | Register expression language | registration row | yes | Language admitting unbounded computation or effects |
| 18 | Register path scheme | registration row | yes | Duplicate scheme name |
| 19 | Register enforcement level scheme | registration row | yes | Scheme without a declared ordering |
| 20 | Register verdict code | registration row | yes | Code in a closed class; duplicate code |
| 21 | Register evaluation purpose | registration row | yes | Duplicate purpose |

**P2-4.5 (MUST) Admission is explicit.** An implementation must require an explicit admission operation before a rule version may be evaluated, and must not admit a version as a side effect of recording it.

**P2-4.6 (MUST) Admission preconditions checked at admission.** An implementation must check every admission precondition at the moment of admission, must record the outcome of each check, and must not defer a check to the first evaluation.

**P2-4.7 (MUST) Admission is not approval.** An implementation must not represent admission as approval of a rule and must record that approval was obtained from `Part 1`, per clause P2-4.9.

**P2-4.8 (MUST NOT) No retirement of a rule in use.** An implementation must refuse to retire a lineage that is a member of an admitted rule set version and must state the set version in the refusal.

**P2-4.9 (MUST) Approval verified at admission.** An implementation must resolve the document citation of a rule version at admission, must record the status the resolution returned, and must refuse admission where the resolution did not establish that the carrying version was approved.

**P2-4.10 (MUST NOT) No admission on unresolvable authority.** An implementation must refuse admission of a rule version whose authority citation does not resolve, and must not admit it with a note.

### 4.3 Evaluating operations

| # | Operation | Records | Sync | Principal refusals |
| --- | --- | --- | --- | --- |
| 22 | Evaluate | `evaluation_request`, `evaluation_run`, pins, verdicts, findings, witnesses, report | yes | Absent evaluation instant; unadmitted rule set version; subject kind not declared by any member |
| 23 | Evaluate as a batch | as above per subject, plus a batch record | no | As above |
| 24 | Reproduce a recorded run | a new run linked to the original, and a divergence record | either | Original run unknown; a pin no longer obtainable |
| 25 | Evaluate unadmitted rule version | a run marked non authoritative | yes | Caller not authorised for the purpose |
| 26 | Explain a verdict | an access record | yes | Verdict unknown |

Operation 24 is the operation that makes reproducibility real rather than claimed. It takes a recorded run, obtains every pinned artifact at its recorded version, re executes, and records whether every verdict came out the same. Its most useful outcome is failure: a pin that can no longer be obtained is the discovery that the evidence for a past verdict has decayed, and it is far better to discover that during a periodic reproduction than during an investigation.

Operation 25 exists because rule authors need to try a rule before it is approved, and the alternative to providing it is that they will do it in a copy of the engine with none of the recording. It is fenced: the run is marked non authoritative, the marking is not removable, and clause P2-4.14 forbids a non authoritative verdict from being cited.

**P2-4.11 (MUST) Evaluation records its pins before returning.** An implementation must durably record the pin set of a run before returning any verdict from it.

**P2-4.12 (MUST) Reproduction available.** An implementation must provide operation 24 and must be able to attempt reproduction of any run within its retained history.

**P2-4.13 (MUST) Reproduction failure recorded, not hidden.** An implementation must record a non result where a pinned artifact cannot be obtained during reproduction, and must not substitute the current version.

**P2-4.14 (MUST NOT) No citation of a non authoritative run.** An implementation must mark every run produced by operation 25 as non authoritative, must not permit the marking to be removed, and must refuse to include such a run in an evidence package as evidence of a verdict.

**P2-4.15 (MUST) Batch evaluation reports per subject.** An implementation must produce a separate evaluation report for each subject in a batch and must not merge verdicts across subjects into one report.

**P2-4.16 (MUST) Explanation available for every verdict.** An implementation must be able to return, for every recorded verdict, the rule version, the statement, the authority reference and status, the pins, the guard truth value, the findings and witnesses, and the budget consumed.

**P2-4.17 (MUST NOT) No explanation reconstruction.** An implementation must return an explanation assembled from the records of the run and must not recompute a verdict in order to explain it.

### 4.4 Reading operations

| # | Operation | Returns |
| --- | --- | --- |
| 27 | Read a named projection | The projection of section 3.20 named in the request, at the times supplied |
| 28 | Get rule artifacts | The assembled artifacts of a rule version, per `rule_current_artifacts` |
| 29 | Get evaluation report | The report of a run, complete |
| 30 | Get verdict | One verdict with its findings and witnesses |
| 31 | Export evidence package | The package of section 8.6 |

**P2-4.18 (MUST) Reads do not evaluate.** An implementation must not evaluate any rule in the course of a reading operation.

**P2-4.19 (MUST) Times required on temporal projections.** An implementation must require both an application time and a knowledge time for every projection whose name ends in `_at`, and must not default either.

**P2-4.20 (MUST NOT) No partial report.** An implementation must return a complete evaluation report from operation 29 or refuse, and must not return a subset without stating what was omitted and why.

### 4.5 What a caller may and may not assume

**P2-4.21 (MUST) Caller obligations declared.** An implementation must document, for every operation, which of the assumptions below the caller may make.

A caller may assume that a returned verdict is reproducible from its recorded pins, that a satisfaction verdict marked non vacuous examined at least one instance, that a violation verdict carries at least one finding, and that no verdict was produced by evaluating a rule version that was not admitted at the evaluation instant.

A caller may not assume that a satisfaction verdict means the rule was checked, unless the vacuity flag is false. A caller may not assume that the absence of a violation means conformity, since indeterminacy and inapplicability are not conformity. A caller may not assume that a rule's authority is in force, since the verdict carries the status. A caller may not assume that a rule set version contains every rule that ought to apply, since membership is declared and this component cannot know what was omitted.

**P2-4.22 (MUST NOT) No implied completeness.** An implementation must not represent an evaluation report as an assessment of the subject's compliance, and must represent it as the outcome of evaluating the named rule set version.

**P2-4.23 (MUST) Non result surfaced unmodified.** An implementation must return every non result of section 7.2 to the caller unmodified, and must not degrade one to a violation, a satisfaction or an error to fit a caller's model.

### 4.6 Reads from other components

| Read | From | On unavailability |
| --- | --- | --- |
| Resolve a rule document version and its status | `Part 1` | Refuse admission; refuse evaluation of an `AS_OF_LINEAGE` member |
| Resolve an authority citation and its status | `Part 1` | Record `authority_status` as `UNRESOLVABLE`; do not refuse the evaluation |
| Obtain a term definition version | `Part 4` | Non result `TERM_UNRESOLVABLE` for any rule using the term |
| Obtain a reference set version | `Part 10` | Non result `REFERENCE_SET_UNAVAILABLE` for any rule reading it |
| Obtain an authorisation decision | `Part 7` | Refuse the operation |
| Obtain a pinned model output | `Part 13` | Non result `MODEL_OUTPUT_UNAVAILABLE` |
| Obtain a subject state under a pin | The subject's owning component | Non result `SUBJECT_STATE_UNAVAILABLE` |

The asymmetry in the second row is deliberate and is the most consequential design decision in this section. An unresolvable authority does not stop the rule from being evaluated, because stopping it would change what the organisation permits on the basis of a lookup failure. An unresolvable term does stop the rule from being evaluated, because without the definition the component does not know what the rule means. The first is a governance problem to be reported; the second is an inability to compute.

**P2-4.24 (MUST) Declared unavailability behaviour.** An implementation must implement the unavailability behaviour of the table above for every read, and must record which behaviour it took.

**P2-4.25 (MUST NOT) No substitution on unavailability.** An implementation must not substitute a cached, default or later version of any artifact in the table above, and must not proceed as though the read succeeded.

**P2-4.26 (MUST) Authority unavailability does not gate evaluation.** An implementation must continue to evaluate a rule whose authority citation could not be resolved, and must record `authority_status` as `UNRESOLVABLE`.

### 4.7 Events emitted

An implementation emits events so that other components can react without polling and so that `Part 3` can hold provenance. The event envelope carries at minimum: an event identity, a type from the registered set, the knowledge time assigned by this component, the subject or artifact the event concerns, the actor, a correlation reference to the run or operation, a schema reference, and a digest over the event body.

The minimum event set is the following. An implementation may emit more.

Rule lineage registered. Rule version recorded. Statement recorded. Authority recorded. Example recorded. Classification recorded. Binding digest recorded. Rule version admitted. Rule version admission refused. Rule lineage retired. Rule set version recorded. Rule set analysis recorded. Drift observed. Drift resolved. Expression language registered. Path scheme registered. Enforcement scheme registered. Verdict code registered. Evaluation purpose registered. Evaluation requested. Evaluation run started. Evaluation run completed. Evaluation run terminated by budget. Verdict issued. Violation verdict issued. Contradiction verdict issued. Indeterminate verdict issued. Vacuous satisfaction issued. Finding recorded. Derivation conflict observed. Reproduction attempted. Reproduction diverged. Reproduction pin unobtainable. Evidence package exported. Non authoritative run performed.

**P2-4.27 (MUST) Minimum event set.** An implementation must emit an event for every member of the set above, and must register any additional event type under section 9.9.

**P2-4.28 (MUST) Envelope minimum.** An implementation must include every envelope element named above in every event it emits.

**P2-4.29 (MUST NOT) No event in place of a record.** An implementation must not rely on event emission to satisfy any recording obligation of section 3 or section 8.

**P2-4.30 (MUST) Vacuity and indeterminacy are separately eventful.** An implementation must emit a distinct event for a vacuous satisfaction and for an indeterminate verdict, and must not emit them as a verdict issued event alone.

**P2-4.31 (MUST NOT) No suppression of adverse events.** An implementation must not provide a configuration that suppresses the emission of a violation, contradiction, indeterminacy, vacuity, drift or divergence event.
## 5. State model

### 5.1 Three state models, deliberately separated

This part specifies three state models and keeps them apart. Fusing any two of them is an anti pattern named in section 11.

The **admission state** of a rule version is a transition machine owned by this component. It describes whether the component will evaluate the rule and why not, where it will not.

The **force state** of a rule is not owned by this component at all. Whether a rule is in force at an application time is a `Part 1` fact, obtained by resolution. This part specifies no transitions for it and holds no field carrying it.

The **run state** of an evaluation is a transition machine describing the progress of one execution.

The reason for keeping admission and force apart is that they answer different questions with different owners. Force asks whether the organisation has decided that the rule governs. Admission asks whether this component is technically able and permitted to evaluate it. A rule can be in force and unadmissible, which is a serious condition the organisation needs to know about, and a system with one status field cannot express it: a fused field must report either that the rule is not in force, which is false and dangerous, or that it is in force, which conceals that nothing is checking it.

**P2-5.1 (MUST) Three models separate.** An implementation must not represent admission state and force state in one field, and must not derive either from the other.

**P2-5.2 (MUST) Unadmissible but in force is reportable.** An implementation must be able to report every rule that is in force at a stated application time and is not admitted, and must include the count in the signals of section 8.5.

**P2-5.3 (MUST NOT) No force state held.** An implementation must not hold, cache beyond a declared validity period, or assert the force state of a rule.

### 5.2 Admission state of a rule version

States:

`RECORDED`. The version and its artifacts exist. No admission check has been performed. The component will not evaluate it.

`ADMISSION_PENDING`. An admission operation is in progress.

`ADMITTED`. Every admission precondition was satisfied. The component will evaluate it, subject to force resolution at evaluation time.

`ADMISSION_REFUSED`. An admission precondition failed. The reason is recorded per check. The component will not evaluate it.

`SUSPENDED`. The version was admitted and a precondition has since ceased to hold, specifically a pinned expression language version, path scheme or term definition that is no longer obtainable. The component will not evaluate it. This is not a decision about the rule; it is a report that the component can no longer run it.

`SUPERSEDED_LOCALLY`. A later version of the same lineage has been admitted. The version remains evaluable for a request whose evaluation instant or pinned member resolves to it.

`WITHDRAWN_FROM_ADMISSION`. Admission was revoked deliberately, with an authorisation reference and a reason. The component will not evaluate it.

Transitions:

| From | To | Trigger | Requires |
| --- | --- | --- | --- |
| `RECORDED` | `ADMISSION_PENDING` | Admission requested | Complete artifact set |
| `ADMISSION_PENDING` | `ADMITTED` | All checks passed | Approval resolved, examples agreed, authority resolved |
| `ADMISSION_PENDING` | `ADMISSION_REFUSED` | Any check failed | Recorded reason per failed check |
| `ADMISSION_REFUSED` | `ADMISSION_PENDING` | Admission requested again | A new artifact set, that is, a new version |
| `ADMITTED` | `SUSPENDED` | A pinned dependency became unobtainable | Recorded dependency and observation |
| `SUSPENDED` | `ADMITTED` | The dependency became obtainable again | Example set re executed and agreed |
| `ADMITTED` | `SUPERSEDED_LOCALLY` | A later version of the lineage admitted | Identity of the successor |
| `ADMITTED` | `WITHDRAWN_FROM_ADMISSION` | Deliberate revocation | `AUTHREF` and reason |
| `SUPERSEDED_LOCALLY` | `WITHDRAWN_FROM_ADMISSION` | Deliberate revocation | `AUTHREF` and reason |
| `WITHDRAWN_FROM_ADMISSION` | `ADMITTED` | Reinstatement | `AUTHREF`, reason, and example set re executed |

`ADMISSION_REFUSED` does not transition to `ADMITTED` without a new version, because the refusal was a finding about the artifacts and the artifacts are immutable. `SUPERSEDED_LOCALLY` and `WITHDRAWN_FROM_ADMISSION` are not terminal, because both reinstatement and the discovery that a supersession was wrong occur, and a terminal state forces the record to be falsified in order to represent them.

**P2-5.4 (MUST) Enumerated states only.** An implementation must represent the admission state of a rule version as exactly one member of the set above.

**P2-5.5 (MUST) Enumerated transitions only.** An implementation must not effect a transition absent from the table above.

**P2-5.6 (MUST) State is a projection.** An implementation must compute admission state from recorded rows and must not hold it as an updatable field, per clause P2-3.13.

**P2-5.7 (MUST) No evaluation outside admitted states.** An implementation must not evaluate a rule version whose admission state is not `ADMITTED` or `SUPERSEDED_LOCALLY`, except under operation 25 of section 4.3.

**P2-5.8 (MUST) Suspension is reported, not silent.** An implementation must emit an event and record a signal when a version enters `SUSPENDED`, and must report every rule set version containing a suspended member.

**P2-5.9 (MUST NOT) No suspension as refusal.** An implementation must not record a suspension as an admission refusal, since the first is a statement about the component and the second about the rule.

**P2-5.10 (MUST) Revocation authorised and reasoned.** An implementation must record an `AUTHREF` and a reason for every transition to `WITHDRAWN_FROM_ADMISSION`.

**P2-5.11 (MUST) Reinstatement re executes examples.** An implementation must re execute the example set before any transition into `ADMITTED`.

**P2-5.12 (MUST NOT) No state change from the passage of time.** An implementation must not transition admission state as a consequence of a date passing, and must effect every transition by a recorded act.

**P2-5.13 (MUST) Superseded versions remain evaluable.** An implementation must continue to evaluate a version in `SUPERSEDED_LOCALLY` for a request that resolves to it, and must not substitute the successor.

### 5.3 Run state of an evaluation

States: `REQUESTED`, `PINNING`, `DERIVING`, `EVALUATING`, `ASSEMBLING`, `COMPLETED`, `TERMINATED_BY_BUDGET`, `REFUSED`, `ABANDONED`.

| From | To | Trigger |
| --- | --- | --- |
| `REQUESTED` | `PINNING` | Request accepted |
| `REQUESTED` | `REFUSED` | Request invalid or unauthorised |
| `PINNING` | `DERIVING` | Pins recorded and derivation supported and present |
| `PINNING` | `EVALUATING` | Pins recorded and no derivation |
| `PINNING` | `REFUSED` | A required pin unobtainable |
| `DERIVING` | `EVALUATING` | Closure reached |
| `DERIVING` | `TERMINATED_BY_BUDGET` | Budget exhausted |
| `DERIVING` | `REFUSED` | Derivation conflict |
| `EVALUATING` | `ASSEMBLING` | Every member has a verdict |
| `EVALUATING` | `TERMINATED_BY_BUDGET` | Budget exhausted |
| `ASSEMBLING` | `COMPLETED` | Report recorded |
| any | `ABANDONED` | Loss of the executing process |

`TERMINATED_BY_BUDGET` is not a refusal and not a failure. It is a run that produced verdicts for some members and a non result for the rest, and the distinction matters because a caller that treats it as a failure discards the verdicts that were produced and a caller that treats it as a success reads a partial report as complete.

`ABANDONED` exists because a run whose process is lost leaves rows behind, and the alternative to a state for it is rows that look like an incomplete run in progress forever.

**P2-5.14 (MUST) Enumerated run states.** An implementation must represent the state of every run as exactly one member of the set above.

**P2-5.15 (MUST) Pins before evaluation.** An implementation must not enter `EVALUATING` or `DERIVING` before recording the pin set.

**P2-5.16 (MUST) Derivation before evaluation.** An implementation must not enter `EVALUATING` from `DERIVING` before the derivation closure is complete, per clause P2-3.112.

**P2-5.17 (MUST) Budget termination yields a report.** An implementation must assemble and record a report for a run in `TERMINATED_BY_BUDGET`, containing the verdicts produced and a non result for every member not evaluated.

**P2-5.18 (MUST NOT) No budget termination as failure.** An implementation must not represent a run terminated by budget as a refusal, and must not discard the verdicts it produced.

**P2-5.19 (MUST) Abandonment detected and recorded.** An implementation must transition a run whose executing process is lost to `ABANDONED` within a declared interval and must declare the interval.

**P2-5.20 (MUST NOT) No resumption of an abandoned run.** An implementation must not resume an abandoned run and must record a new run where the evaluation is retried.

**P2-5.21 (MUST) Terminal states are terminal.** An implementation must not transition out of `COMPLETED`, `TERMINATED_BY_BUDGET`, `REFUSED` or `ABANDONED`.

### 5.4 Drift observation state

States: `OPEN`, `RESOLVED_BY_NEW_VERSION`, `RESOLVED_BY_REASSERTION`, `RESOLVED_BY_DECISION_TO_RETAIN`, `SUPERSEDED_BY_OBSERVATION`.

An observation is never closed as invalid, and there is no `DISMISSED` state. The three resolutions are all positive acts: a new rule version, a fresh authority assertion, or a recorded decision that the rule stands unchanged despite the drift. The absence of a dismissal state is deliberate: dismissal is how a drift register becomes empty without anything having been fixed, and the decision to retain is exactly as reviewable as the other two while being honest about what happened.

`SUPERSEDED_BY_OBSERVATION` exists for the case where a later observation about the same rule version subsumes an earlier one, so that the earlier is not left open forever.

**P2-5.22 (MUST) Enumerated drift states.** An implementation must represent the state of every drift observation as exactly one member of the set above.

**P2-5.23 (MUST NOT) No dismissal.** An implementation must not provide a means of closing a drift observation without recording one of the three resolutions or a subsuming observation.

**P2-5.24 (MUST) Retention decision is authorised.** An implementation must record an `ACTOR` and an `AUTHREF` for every transition to `RESOLVED_BY_DECISION_TO_RETAIN`, together with a reason.

**P2-5.25 (MUST NOT) No automatic resolution.** An implementation must not resolve a drift observation as a consequence of a later rule version being recorded, and must require the resolution to be recorded as an act naming the observation.

**P2-5.26 (MUST) Open drift is visible in the verdict.** An implementation must set `drift_open` true in every verdict for a rule version with an observation in `OPEN`.
## 6. Execution semantics

### 6.1 Determinism and reproducibility

Two properties are required and they are not the same. **Determinism** means that one evaluation, run twice in the same conditions, yields the same result. **Reproducibility** means that an evaluation run today can be run again in five years, from its recorded pins, and yield the same result. Determinism is easy and nearly free. Reproducibility is expensive, is what section 3.14 exists for, and is the property that makes a verdict evidence rather than an opinion.

Reproducibility fails in four ways, and only the first is usually anticipated. The rule changed, which pinning prevents. The reference data changed, which pinning prevents. The subject changed, which pinning prevents. And the evaluator changed: a new version of the expression language, a different collation, a different arithmetic, a different calendar convention, a different iteration order. The fourth is the one that defeats systems which pinned everything else, and clauses P2-6.2 through P2-6.5 exist for it.

**P2-6.1 (MUST) Identical pins yield identical verdicts.** An implementation must return the same outcome, guard truth value, body truth value, vacuity flag, witness count and finding set for two evaluations whose pin sets are identical.

**P2-6.2 (MUST) Expression language version pinned.** An implementation must pin the version of the expression language implementation, not only of the language specification, and must record both.

**P2-6.3 (MUST) Collation pinned.** An implementation must pin the collation and the Unicode version used for every string comparison, and must not rely on a locale, an environment setting or a platform default.

**P2-6.4 (MUST) Arithmetic declared.** An implementation must declare the arithmetic model used for every numeric comparison, must use an exact decimal arithmetic for any comparison of a monetary or quantity value, and must not use binary floating point for an equality or threshold comparison.

**P2-6.5 (MUST) Iteration order total and declared.** An implementation must impose a declared total order on the traversal of any unordered collection and must not permit the order to vary between evaluations with identical pins.

### 6.2 Three valued semantics

The truth domain is `TRUE`, `FALSE`, `INDETERMINATE`. `INDETERMINATE` means the component could not establish the value. It does not mean half true, unknown in the sense of an open world, or false by default.

There is a specification anchor for requiring a third value rather than two. ISO/IEC 19757-3:2025 defines a Schematron validator as a function returning valid, invalid or error, and the third member of that triple is not an exception mechanism but a return value of the function. This part takes the same position and makes it structural.

The connectives are those of Kleene's strong three valued system.

Negation:

| p | ¬p |
| --- | --- |
| `TRUE` | `FALSE` |
| `FALSE` | `TRUE` |
| `INDETERMINATE` | `INDETERMINATE` |

Conjunction:

| p ∧ q | q = `TRUE` | q = `FALSE` | q = `INDETERMINATE` |
| --- | --- | --- | --- |
| p = `TRUE` | `TRUE` | `FALSE` | `INDETERMINATE` |
| p = `FALSE` | `FALSE` | `FALSE` | `FALSE` |
| p = `INDETERMINATE` | `INDETERMINATE` | `FALSE` | `INDETERMINATE` |

Disjunction:

| p ∨ q | q = `TRUE` | q = `FALSE` | q = `INDETERMINATE` |
| --- | --- | --- | --- |
| p = `TRUE` | `TRUE` | `TRUE` | `TRUE` |
| p = `FALSE` | `TRUE` | `FALSE` | `INDETERMINATE` |
| p = `INDETERMINATE` | `TRUE` | `INDETERMINATE` | `INDETERMINATE` |

Implication, defined as ¬p ∨ q:

| p → q | q = `TRUE` | q = `FALSE` | q = `INDETERMINATE` |
| --- | --- | --- | --- |
| p = `TRUE` | `TRUE` | `FALSE` | `INDETERMINATE` |
| p = `FALSE` | `TRUE` | `TRUE` | `TRUE` |
| p = `INDETERMINATE` | `TRUE` | `INDETERMINATE` | `INDETERMINATE` |

The four tables above are normative.

The literature disagrees about the last cell of the implication table, and the disagreement is worth stating rather than hiding. Łukasiewicz's three valued system assigns `TRUE` to an implication whose antecedent and consequent are both indeterminate, which preserves the law of identity: p → p is a theorem. Kleene's strong system assigns `INDETERMINATE`. This part requires Kleene, for a reason specific to what the third value means here. If `INDETERMINATE` meant a degree of truth, Łukasiewicz would be defensible. It means that the component could not establish a value, and an implication that becomes true because neither of its sides could be evaluated is a rule reporting satisfaction on the strength of two failures. That is the exact outcome this part is written to prevent, and the cost is the loss of a logical law that nothing here needs.

A second disagreement concerns contradictory evidence. Belnap's four valued system adds a value for propositions supported as both true and false, which arises where two sources disagree. This part does not adopt it: contradictory input is treated as an inability to evaluate and returns a non result whose code records the contradiction, per section 7.2. Section 13.4 records this as an open question, because the four valued treatment is arguably more truthful and the three valued treatment is arguably more useful.

A third point is not a disagreement but a trap. SQL's `NULL` semantics implement Kleene's strong system for the connectives, and then collapse to two values at the boundary of a filter, where `UNKNOWN` is treated as not satisfying the predicate and the row is excluded. The internal logic is right and the boundary discards it. A rule engine built on a query language will inherit both halves of that behaviour, and the collapse is invisible because it happens in the language rather than in the rule. Clause P2-6.9 forbids it and section 11.2 names the mechanism.

Quantification:

| Quantifier | Empty range | Any `FALSE` | No `FALSE`, some `INDETERMINATE` | All `TRUE` |
| --- | --- | --- | --- | --- |
| Universal | `TRUE`, vacuous | `FALSE` | `INDETERMINATE` | `TRUE` |
| Existential | `FALSE` | see next column | `INDETERMINATE` unless some `TRUE` | `TRUE` |

An existential quantifier yields `TRUE` if any instance is `TRUE`, `FALSE` if the range is empty or every instance is `FALSE`, and `INDETERMINATE` otherwise.

**P2-6.6 (MUST) Kleene strong connectives.** An implementation must implement negation, conjunction, disjunction and implication exactly as the four tables of this section specify.

**P2-6.7 (MUST) Quantifier semantics.** An implementation must implement universal and existential quantification exactly as the table of this section specifies.

**P2-6.8 (MUST) Vacuous universal flagged.** An implementation must mark a universal quantification over an empty range as vacuous and must propagate the vacuity to the verdict, per clause P2-3.90.

**P2-6.9 (MUST NOT) No boundary collapse.** An implementation must not treat `INDETERMINATE` as `FALSE` or as `TRUE` at the boundary of a filter, a selection, a join, a projection or any other operation that reduces a collection.

**P2-6.10 (MUST) Withheld yields indeterminate.** An implementation must yield `INDETERMINATE` for any expression whose value depends on a withheld path, per clause P2-3.72.

**P2-6.11 (MUST) Absent yields per declared semantics.** An implementation must declare, for each operator of its expression language, the value yielded where an operand is a declared absence, and must not yield `TRUE` or `FALSE` from an absence without a declared rule.

**P2-6.12 (MUST NOT) No absence as a value.** An implementation must not compare a declared absence for equality with a value and yield `FALSE`, unless the expression language declares an explicit absence test operator and the rule used it.

**P2-6.13 (MUST) Type mismatch yields indeterminate.** An implementation must yield `INDETERMINATE` where an operand is not of the type an operator requires, and must not coerce silently.

**P2-6.14 (MUST NOT) No four valued extension without declaration.** An implementation must not introduce a fourth truth value, and must return a non result of section 7.2 where inputs are contradictory.

### 6.3 Idempotence

**P2-6.15 (MUST) Idempotence by key.** An implementation must return the originally recorded outcome for a repeated recording or evaluating operation bearing an idempotence key already seen within its declared deduplication window, and must not perform the operation again.

**P2-6.16 (MUST) Deduplication window declared.** An implementation must declare its deduplication window as a duration and must state what happens to a key repeated after it.

**P2-6.17 (MUST NOT) No idempotence across differing payloads.** An implementation must refuse an operation bearing a seen idempotence key with a different payload, and must not return the earlier outcome.

**P2-6.18 (MUST) Evaluation is naturally idempotent.** An implementation must not vary the verdicts of a repeated evaluation with identical pins, whether or not an idempotence key was supplied, and must record each execution as a separate run.

### 6.4 The evaluation algorithm

The algorithm below is normative in its ordering and in its outcomes. It is not normative in its structure as code.

```
evaluate(request):
  1  if request.evaluation_instant is absent: return REFUSED(EVALUATION_INSTANT_REQUIRED)
  2  authorisation = obtain decision from Part 7 for request.purpose and subject
     if not permitted: return REFUSED(NOT_AUTHORISED)
  3  set_version = resolve(request.set_reference, request.set_binding_mode,
                           request.evaluation_instant, request.knowledge_instant)
     if unresolved: return REFUSED(RULE_SET_UNRESOLVABLE)
  4  members = rule_set_membership_at(set_version)
  5  for each member:
        rule_version = resolve member per binding_mode
        record pin(RULE_VERSION, rule_version)
        if admission_state(rule_version) not in {ADMITTED, SUPERSEDED_LOCALLY}:
            verdict(member) = INDETERMINATE(RULE_NOT_ADMITTED); continue
        if force_state(rule_version, evaluation_instant) is not in force:
            verdict(member) = NOT_IN_FORCE_AT_INSTANT; continue
  6  pin every expression language, term definition, reference set, path scheme,
     enforcement scheme and model output required by the surviving members
     if any pin unobtainable: return REFUSED(PIN_UNOBTAINABLE) with the pin identified
  7  subject_state = supplied, or fetched under pin
     if unavailable: return REFUSED(SUBJECT_STATE_UNAVAILABLE)
  8  if derivation members present:
        derived = derive_closure(derivation members, subject_state, budget)
        if conflict: return REFUSED(DERIVATION_CONFLICT) with both assertions recorded
        if budget exhausted: state = TERMINATED_BY_BUDGET; skip to 11
  9  for each constraint member, in any order:
        g = eval(rule.guard, subject_state, derived)     // absent guard yields TRUE
        record guard_truth = g
        if g == FALSE:          verdict = NOT_APPLICABLE; continue
        if g == INDETERMINATE:  verdict = INDETERMINATE(GUARD_INDETERMINATE); continue
        witnesses = bind(rule, subject_state, derived)
        b = eval(rule.body, witnesses)
        record body_truth = b, witnesses_examined = |witnesses|
        if b == TRUE:           verdict = SATISFIED
                                vacuous = (|witnesses| == 0)
        if b == FALSE:          verdict = VIOLATED if behavioural else CONTRADICTED
                                record a finding per failing witness
        if b == INDETERMINATE:  verdict = INDETERMINATE(code from the cause)
        if budget exhausted:    state = TERMINATED_BY_BUDGET; break
 10  for each member without a verdict: verdict = INDETERMINATE(BUDGET_EXHAUSTED)
 11  assemble report: verdicts, findings, witnesses, pins, counts, run outcome
 12  record report digest; emit events; return report
```

Step 5 is where two facts that look alike are kept apart. A rule that is not admitted yields an indeterminate verdict, because the component cannot evaluate it. A rule that is not in force at the evaluation instant yields a distinct outcome, because the component can evaluate it and the organisation has said it does not govern. Both are non violations and neither is a satisfaction.

Step 9 evaluates members in any order, which is the point of section 6.8: if the order could matter, the algorithm would have to specify it, and specifying it would make the rule set's behaviour depend on something no author wrote.

**P2-6.19 (MUST) Algorithm order.** An implementation must perform the steps of the algorithm above in the order given, and must not evaluate any constraint before recording the pin set.

**P2-6.20 (MUST) Not admitted and not in force distinguished.** An implementation must return distinct outcomes for a rule that is not admitted and a rule that is not in force at the evaluation instant.

**P2-6.21 (MUST) Absent guard yields true.** An implementation must treat an absent guard as yielding `TRUE`.

**P2-6.22 (MUST) Every member reaches step 11.** An implementation must ensure that every member of the resolved rule set has a verdict recorded in the report, per clause P2-1.13.

**P2-6.23 (MUST NOT) No early return on the first violation.** An implementation must evaluate every member of the rule set unless the budget is exhausted, and must not stop at the first violation.

### 6.5 Clocks and temporal comparison

Three clocks are kept separate, on the same basis and with the same names as `Part 1` section 3.1: the evaluation instant, which is application time and is supplied; the knowledge time, which this component assigns; and the occurrence time, which an actor asserts and this component never assigns.

The rule against reading a clock inside a declaration is the most operationally significant clause in this section. A declaration that computes the interval between a stored date and now is not reproducible: run it again next year and it yields a different verdict from identical pins. The remedy is that every temporal comparison is against a value in the request, so that reproduction supplies the same value and obtains the same verdict.

Calendar arithmetic requires a declared convention, because the obvious operations are not well defined. Adding twenty four months to 31 January is unambiguous; adding one month to 31 January is not, and implementations variously yield 28 February, 2 March or an error. A review interval rule is exactly this computation, and two engines will disagree about whether a document is overdue unless the convention is pinned.

**P2-6.24 (MUST NOT) No ambient clock.** An implementation must not permit a declaration to read a clock, and must require every temporal comparison to be against a value supplied in the evaluation request or held in the subject state.

**P2-6.25 (MUST) Instants in a declared scale.** An implementation must record every `ATIME`, `KTIME` and `OTIME` in a declared time scale with a declared offset, and must not record a local time without its offset.

**P2-6.26 (MUST) Calendar convention declared.** An implementation must declare the convention by which it adds and subtracts months and years, must state its behaviour where the result would fall on a date that does not exist, and must pin the convention in the run.

**P2-6.27 (MUST) Leap second behaviour declared.** An implementation must declare its treatment of a leap second in a duration computation.

**P2-6.28 (MUST NOT) No occurrence time assignment.** An implementation must not assign an occurrence time, and must record every occurrence time as asserted by a named actor.

**P2-6.29 (MUST NOT) No knowledge time from a caller.** An implementation must assign every knowledge time from its own clock and must refuse a request supplying one, per clause P2-3.4.

### 6.6 Derivation closure

```
derive_closure(rules, subject_state, budget):
  strata = distinct declared strata of rules, ascending
  state = subject_state
  for s in strata:
      assertions = {}
      for each rule r in stratum s:            // any order
          for each binding b of r over state:  // state excludes stratum s and above
              v = eval(r.expression, b)
              if v is INDETERMINATE: record a signal; do not assert
              else if assertions has r.path with a different value:
                  return CONFLICT(both assertions)
              else assertions[r.path] = v
          if budget exhausted: return EXHAUSTED
      state = state ∪ assertions               // monotonic
  return state
```

The closure terminates in a number of passes equal to the number of strata, which is known before execution. That is the whole reason for requiring a declared stratum rather than inferring one: inference makes termination a property discovered at run time, and a rule set that fails to terminate has already consumed the budget of every caller before anyone notices.

**P2-6.30 (MUST) Closure in declared strata.** An implementation must compute the derivation closure in ascending stratum order and must complete each stratum before beginning the next.

**P2-6.31 (MUST) Stratum isolation.** An implementation must not permit a derivation rule to read an assertion made by its own stratum or a higher one, and must enforce this at admission rather than at run time.

**P2-6.32 (MUST) Indeterminate derivation asserts nothing.** An implementation must not assert a derived value where the derivation expression yielded `INDETERMINATE`, and must record a signal.

**P2-6.33 (MUST) Conflict halts derivation.** An implementation must halt the closure on a conflict, must record both conflicting assertions, and must return the non result of section 7.2.

**P2-6.34 (MUST NOT) No fixpoint iteration.** An implementation must not iterate a stratum to a fixpoint, and must not re evaluate a stratum after completing it.

### 6.7 Budget and termination

A budget is a bound on a resource. Which resource matters, because the choice determines whether the verdict is reproducible.

A **deterministic** resource is one whose consumption is identical for identical pins: expression evaluation steps, witnesses bound, witnesses examined, derived assertions, findings recorded. A budget on a deterministic resource preserves reproducibility, because a run that exhausted it will exhaust it again at the same point.

A **non deterministic** resource is one whose consumption varies with conditions the pins do not capture: wall clock time, memory, network calls. A budget on a non deterministic resource destroys reproducibility, because the same request can complete on one day and be truncated on another, yielding different verdicts from identical pins.

The requirement follows. A primary budget must be on a deterministic resource. A non deterministic guard may also exist, because a runaway evaluation has to be stoppable, but exhausting it must be recorded as a non deterministic termination and marked so that nobody treats the resulting report as reproducible.

**P2-6.35 (MUST) Primary budget deterministic.** An implementation must enforce a primary budget on a deterministic resource and must declare the resource and the bound.

**P2-6.36 (MAY) Secondary non deterministic guard.** An implementation may enforce an additional bound on a non deterministic resource.

**P2-6.37 (MUST) Non deterministic termination marked.** An implementation must mark every run terminated by a non deterministic bound as not reproducible, and must not present its report as reproducible.

**P2-6.38 (MUST) Exhaustion yields a non result.** An implementation must return an `INDETERMINATE` verdict for every member not evaluated because a budget was exhausted, and must not return a satisfaction or omit the member.

**P2-6.39 (MUST) Partial results retained.** An implementation must retain and report every verdict produced before exhaustion, per clause P2-5.17.

**P2-6.40 (MUST) Budget consumption recorded per verdict.** An implementation must record the budget consumed by each verdict and by the run as a whole.

### 6.8 Order independence

A set of constraints is order independent: each is a proposition about the subject, and the truth of one does not depend on when another was evaluated. This is a property the component must preserve, and the ways it is lost are specific.

A constraint reads a value another constraint wrote. Prevented by clause P2-3.21, which admits no writes.

A constraint reads the verdict of another constraint. This is the common case and it is prohibited outright by clause P2-6.43. A rule saying that where rule X is violated some further condition applies is not a constraint; it is a composition of constraints, and composing them is `Part 5`'s work. Admitting it here makes the rule set a program with an execution order, and the order is then determined by dependency analysis nobody wrote down as a rule.

A constraint reads a partially derived state. Prevented by the phase separation of clause P2-3.112.

Evaluation order affects the finding set through short circuiting. Not prevented, because short circuiting is sound for the truth value and valuable in practice, but constrained: a short circuited evaluation examined fewer witnesses than a complete one, so its finding set is not complete and must not be presented as complete.

**P2-6.41 (MUST) Order independent verdicts.** An implementation must produce the same verdict for each constraint regardless of the order in which the constraints of a rule set were evaluated.

**P2-6.42 (MUST) Order independence checkable.** An implementation must be able to demonstrate order independence for a rule set version by evaluating it in at least two different orders and comparing the verdicts, and must record the result as a `rule_set_analysis`.

**P2-6.43 (MUST NOT) No verdict as an input.** An implementation must not admit a rule whose declaration or guard reads the verdict, finding set or witness count of another rule.

**P2-6.44 (MUST) Short circuit disclosed.** An implementation must record whether an evaluation short circuited, and must not present the finding set of a short circuited evaluation as complete.

**P2-6.45 (MUST NOT) No short circuit that changes the truth value.** An implementation must not short circuit where the tables of section 6.2 do not determine the result from the operands already evaluated.

### 6.9 Static analysis and what is undecidable

Three properties of a rule set are worth knowing and none of them is decidable in general.

**Unsatisfiability.** A rule set no subject can satisfy. This is the most valuable property to know and the least likely to be discovered by testing, because the symptom is that every subject is non conformant, which looks like a data problem.

**Subsumption.** One rule implies another, so the weaker is redundant. Redundancy is harmless to correctness and expensive to governance: a rule that can never produce a finding of its own still appears in reports, still requires review, and still has an authority nobody can retire.

**Contradiction.** Two rules that cannot both be satisfied by any subject to which both apply. A special case of unsatisfiability, and the one with a governance answer rather than a technical one, since the resolution is to establish which authority prevails.

All three are decidable for restricted expression languages and undecidable for expressive ones. The SHACL literature has established decision procedures for satisfiability and containment over restricted fragments, and DMN provides completeness and consistency checking over decision tables, which are a restricted form by construction. This part therefore requires analysis where the language permits it, requires the result to be recorded, and forbids the absence of a detected problem from being reported as the absence of the problem.

**P2-6.46 (MUST) Analysis performed where decidable.** An implementation must perform unsatisfiability and subsumption analysis over every rule set version where its registered expression language admits a decision procedure, and must record the result as a `rule_set_analysis`.

**P2-6.47 (MUST) Undecidability declared.** An implementation must record, for every rule set version it did not analyse, that the analysis was not performed and why.

**P2-6.48 (MUST NOT) No absence of finding as absence of fault.** An implementation must not report a rule set as consistent, satisfiable or non redundant on the basis of an analysis that did not complete or was not performed.

**P2-6.49 (MUST) Detected contradiction reported, not resolved.** An implementation must report a detected contradiction between rules together with both rules and both authorities, and must not select between them, disable either, or alter a verdict.

**P2-6.50 (MUST NOT) No analysis at evaluation time.** An implementation must not perform static analysis during an evaluation and must not vary a verdict on the basis of an analysis result.

**P2-6.51 (MUST) Analysis pinned to a set version.** An implementation must record every analysis result against the rule set version analysed and must not carry a result forward to a later version.
## 7. Verdict and failure taxonomy

### 7.1 Why the taxonomy is the specification

For this component more than for most, the taxonomy is not a list of error codes appended to a design. It is the design. Everything else in this part exists to make the distinctions in this section true and knowable.

The reason is that a constraint evaluator has exactly one output, and every defect in it manifests as a wrong or under specified value of that output. A rule engine that evaluates the wrong expression is a bug someone will find. A rule engine that returns satisfaction where it should have returned indeterminacy is a bug nobody will ever find, because the output is well formed, plausible, and reported as green. Systems fail this way for years.

The verdict set is closed. Members may be added only by a revision of this part, per section 9.1. Codes within the `INDETERMINATE` and `REFUSAL` classes are registered and open. The reason for the asymmetry is that a new class requires every consumer to grow a new branch, while a new code within a class is handled by the branch that already exists.

The set has four classes and seven members.

| Class | Member | Means |
| --- | --- | --- |
| Conformance | `SATISFIED` | The rule applied, the body was evaluated, and it held. Carries a vacuity flag. |
| Conformance | `VIOLATED` | The rule applied and a behavioural obligation was not met. |
| Conformance | `CONTRADICTED` | The rule applied and a definitional necessity was contradicted. |
| Non applicability | `NOT_APPLICABLE` | The guard was evaluated and yielded `FALSE`. The rule was never in question. |
| Non applicability | `NOT_IN_FORCE_AT_INSTANT` | The rule exists and was not in force at the evaluation instant. |
| Non result | `INDETERMINATE` | The rule could not be evaluated. Carries a subclass and a code. |
| Refusal | `REFUSED` | The component declined to evaluate the rule. Carries a code. |

The table above is normative.

Five distinctions in it are load bearing and each is commonly erased.

**`SATISFIED` against `NOT_APPLICABLE`.** The first asserts a check was performed and passed. The second asserts no check was owed. A report that merges them overstates how much checking occurred, and the overstatement is largest in exactly the rule sets that are broadest, because a broad set applied to a narrow subject is mostly inapplicable.

**`SATISFIED` against vacuous `SATISFIED`.** The vacuity flag is inside the member rather than a separate member, because a vacuous satisfaction is still a satisfaction and promoting it to its own class would force every consumer to handle it or fall through. It is required to be present in every report because a vacuous satisfaction is a check that examined nothing.

**`VIOLATED` against `CONTRADICTED`.** A violated behavioural rule is a fact about conduct: somebody did something they were obliged not to do. A contradicted definitional rule is a fact about data: the subject asserts something that cannot be true, so the subject is wrong, or the definition is, or the rule is. The remedies have different owners and the reports go to different people. SBVR 1.5 draws the underlying distinction; this part gives it two verdicts so that a report can carry it without a reader having to look up the rule's classification.

**`VIOLATED` against `INDETERMINATE`.** The most dangerous confusion available. A violation asserts non conformity. An indeterminacy asserts nothing about conformity at all. Reporting the second as the first manufactures findings against conforming subjects, and reporting the first as the second conceals real non conformity. Neither direction is safe and neither is detectable downstream.

**`INDETERMINATE` against `REFUSED`.** An indeterminacy is a statement about the rule and the subject: the question could not be answered. A refusal is a statement about the request: the component did not attempt it. Merging them means a caller cannot tell whether to fix its request or fix its data.

**P2-7.1 (MUST) Closed verdict set.** An implementation must return exactly one member of the table above for every rule evaluated and must not return a value outside the set.

**P2-7.2 (MUST NOT) No additional members.** An implementation must not add a member to the verdict set and must express any additional distinction as a registered code within the `INDETERMINATE` or `REFUSAL` class.

**P2-7.3 (MUST) Vacuity flag on every satisfaction.** An implementation must carry a vacuity flag on every `SATISFIED` verdict and must not omit it in any interface, report or projection.

**P2-7.4 (MUST) Classification determines which conformance member.** An implementation must return `VIOLATED` for a behavioural rule and `CONTRADICTED` for a definitional rule, and must not return either for the other.

**P2-7.5 (MUST NOT) No mapping onto two values.** An implementation must not provide an interface that maps the seven members onto two values, and must not document such a mapping as canonical.

**P2-7.6 (MUST NOT) No caller selected collapse.** An implementation must not offer a configuration, parameter or header by which a caller may request that `INDETERMINATE` be returned as `SATISFIED` or `VIOLATED`.

### 7.2 Indeterminacy subclasses

An `INDETERMINATE` verdict carries a subclass and a code. The subclass identifies where the inability lies, and it exists because the five subclasses have five different remedies with five different owners. A single undifferentiated indeterminacy routes all of them to nobody.

| Subclass | The inability lies in | Remedy owner | Registered codes |
| --- | --- | --- | --- |
| `SUBJECT_INDETERMINACY` | The subject state | The subject's custodian | `SUBJECT_PATH_WITHHELD`, `SUBJECT_PATH_UNDECLARED`, `TYPE_MISMATCH`, `CONTRADICTORY_INPUT` |
| `RULE_INDETERMINACY` | The rule | The rule's author | `GUARD_INDETERMINATE`, `RULE_NOT_ADMITTED`, `RULE_SUSPENDED`, `DERIVED_VALUE_INDETERMINATE` |
| `DEPENDENCY_INDETERMINACY` | Another component | That component's owner | `TERM_UNRESOLVABLE`, `REFERENCE_SET_UNAVAILABLE`, `MODEL_OUTPUT_UNAVAILABLE`, `EXPRESSION_LANGUAGE_UNAVAILABLE`, `PATH_SCHEME_UNAVAILABLE` |
| `RESOURCE_INDETERMINACY` | The resources available | The operator | `BUDGET_EXHAUSTED`, `BUDGET_EXHAUSTED_NON_DETERMINISTIC` |
| `COMPONENT_DEFECT` | This component | The implementer | `EVALUATION_FAULT`, `INVARIANT_BROKEN` |

The table above is normative for the subclasses and for the allocation of the listed codes. The code sets are open under section 9.8.

`COMPONENT_DEFECT` is separated from the other four because a defect in the evaluator is not a fact about the rule or the subject, and reporting it as one sends people to investigate data that is fine. A component that cannot distinguish its own faults from its inputs' deficiencies will have its users debugging the wrong thing indefinitely.

`SUBJECT_PATH_WITHHELD` and `SUBJECT_PATH_UNDECLARED` are separate codes because the first is an access decision and the second is a data supply gap, and conflating them makes an authorisation problem look like a data quality problem.

**P2-7.7 (MUST) Subclass on every indeterminacy.** An implementation must carry a subclass and a code on every `INDETERMINATE` verdict.

**P2-7.8 (MUST) Allocation honoured.** An implementation must allocate every code to the subclass the table above assigns it, and must allocate a newly registered code to exactly one subclass.

**P2-7.9 (MUST) Defect distinguished from input deficiency.** An implementation must return `COMPONENT_DEFECT` where the inability arose from its own fault, and must not return a subject or dependency subclass in its place.

**P2-7.10 (MUST NOT) No generic indeterminacy.** An implementation must not return an `INDETERMINATE` verdict without a code, and must not use a catch all code where a specific one in the table applies.

**P2-7.11 (MUST) Withheld and undeclared separated.** An implementation must return `SUBJECT_PATH_WITHHELD` where a path was withheld and `SUBJECT_PATH_UNDECLARED` where it was not supplied, and must not use one for the other.

**P2-7.12 (MUST) Cause path recorded.** An implementation must record, with every `SUBJECT_INDETERMINACY` verdict, the path whose condition caused the indeterminacy.

**P2-7.13 (MUST) Dependency identified.** An implementation must record, with every `DEPENDENCY_INDETERMINACY` verdict, the identity and version of the artifact it could not obtain.

### 7.3 The verdict envelope

Every verdict is returned in an envelope carrying the following. The envelope is normative in its content; its serialisation is not specified.

The verdict member and, where applicable, the subclass and code. The rule version identity and its lineage. The rule set version identity. The statement reference and its language. The classification kind, and the enforcement level where behavioural. The guard truth value and the body truth value. The witness count and its grain, and the vacuity flag. The finding count and whether the finding set was truncated. The authority status and the drift flag. The evaluation instant, the knowledge instant used, and the knowledge time assigned. The pin set reference. The budget consumed and whether the run was terminated. Whether the run was non authoritative. Whether the evaluation short circuited.

**P2-7.14 (MUST) Envelope completeness.** An implementation must include every element named above in every verdict it returns and records.

**P2-7.15 (MUST NOT) No envelope reduction.** An implementation must not omit an envelope element on the ground that a caller does not use it.

**P2-7.16 (MUST) Envelope is what is recorded.** An implementation must record the whole envelope, and must not record a reduced form while returning the full one or the reverse.

### 7.4 Non applicability, and the two kinds

`NOT_APPLICABLE` and `NOT_IN_FORCE_AT_INSTANT` are both non applicability and they are not interchangeable.

`NOT_APPLICABLE` says the rule is in force and is not about this subject. The rule set was correctly assembled and this member simply has nothing to say here.

`NOT_IN_FORCE_AT_INSTANT` says the rule is about this subject and the organisation had not brought it into force at the evaluation instant, or had ceased to. This is a temporal fact obtained from `Part 1` and it is the mechanism by which an evaluation of a past state uses the rules of that past state.

The distinction matters most in a retrospective evaluation. Asking what a subject's compliance position was in 2028 means evaluating the rules in force in 2028. A rule introduced in 2030 must return `NOT_IN_FORCE_AT_INSTANT` and must not return `NOT_APPLICABLE`, because the second would report that the rule had nothing to say about that subject, which is false: it has plenty to say and was not yet law.

**P2-7.17 (MUST) Two kinds distinguished.** An implementation must return `NOT_IN_FORCE_AT_INSTANT` where the rule was not in force at the evaluation instant and `NOT_APPLICABLE` where the guard yielded false, and must not use one for the other.

**P2-7.18 (MUST) Force resolved before the guard.** An implementation must resolve force state before evaluating a guard, per section 6.4, and must not evaluate the guard of a rule not in force.

**P2-7.19 (MUST) Non applicability is not conformance.** An implementation must not include either non applicability member in any count, projection or report presented as a count of conforming rules.

**P2-7.20 (MUST NOT) No omission of non applicable members.** An implementation must record a verdict for every member of the rule set including those not applicable and those not in force, per clause P2-1.13.

### 7.5 Refusals

A refusal is the outcome of an operation the component declined to attempt. Refusals are recorded, are not verdicts about rules, and are not retried by the component.

| Code | Cause | Retryable |
| --- | --- | --- |
| `EVALUATION_INSTANT_REQUIRED` | The request omitted the evaluation instant | Yes, with the instant |
| `MALFORMED_REQUEST` | The request was not well formed | Yes, corrected |
| `NOT_AUTHORISED` | `Part 7` did not permit the operation for the purpose | No, without a changed decision |
| `RULE_SET_UNRESOLVABLE` | The rule set reference did not resolve at the instants supplied | No |
| `PIN_UNOBTAINABLE` | A required pinned artifact could not be obtained | Possibly, if availability is restored |
| `SUBJECT_STATE_UNAVAILABLE` | The subject state was neither supplied nor obtainable | Possibly |
| `SUBJECT_KIND_NOT_DECLARED` | No member of the set declares the subject's kind | No |
| `DERIVATION_CONFLICT` | Two derivation rules asserted different values for one path | No, without a rule change |
| `DERIVATION_UNSUPPORTED` | The set contains a derivation rule and the implementation does not support derivation | No |
| `IDEMPOTENCE_KEY_CONFLICT` | A seen key was presented with a different payload | Yes, with a new key |

The table above is normative for the codes and their allocation. The set is open under section 9.8.

**P2-7.21 (MUST) Refusal codes.** An implementation must return one of the codes above, or a registered code, for every refused operation.

**P2-7.22 (MUST) Refusal recorded.** An implementation must record every refusal with its code, the request, and the knowledge time.

**P2-7.23 (MUST NOT) No refusal as a verdict.** An implementation must not return a refusal in the position of a verdict for a rule, and must not record a refusal as an `INDETERMINATE` verdict.

**P2-7.24 (MUST) Retryability stated.** An implementation must state, with every refusal it returns, whether the operation may be retried and what must change.

**P2-7.25 (MUST NOT) No silent retry.** An implementation must not retry a refused operation on its own initiative.

### 7.6 Run outcomes

| Outcome | Means | Report contains |
| --- | --- | --- |
| `COMPLETE` | Every member was evaluated within budget | A verdict for every member |
| `PARTIAL_BUDGET` | A deterministic budget was exhausted | Verdicts produced, plus `BUDGET_EXHAUSTED` for the rest |
| `PARTIAL_NON_DETERMINISTIC` | A non deterministic bound was exhausted | As above, and the report is marked not reproducible |
| `REFUSED` | The run did not begin | No verdicts, one refusal code |
| `ABANDONED` | The executing process was lost | Whatever was durably recorded, marked incomplete |

**P2-7.26 (MUST) Run outcome recorded.** An implementation must record exactly one run outcome for every run.

**P2-7.27 (MUST) Partial is not complete.** An implementation must not record a run outcome of `COMPLETE` where any member lacks a verdict of a conformance or non applicability class.

**P2-7.28 (MUST) Non reproducible partials marked.** An implementation must mark a report of outcome `PARTIAL_NON_DETERMINISTIC` as not reproducible and must not include it in an evidence package as evidence of a verdict without the marking.

**P2-7.29 (MUST) Abandoned runs are not results.** An implementation must not return the report of an abandoned run as the result of an evaluation and must not permit it to be cited.

### 7.7 Outcome obligations

The table below states, for each class, what the component must record, what it must emit, and what the caller must do. It is normative.

| Class | Component records | Component emits | Caller must |
| --- | --- | --- | --- |
| `SATISFIED`, not vacuous | Verdict, witnesses, pins | Verdict issued | Nothing |
| `SATISFIED`, vacuous | As above, with vacuity | Verdict issued and vacuous satisfaction | Not treat the rule as checked |
| `VIOLATED` | Verdict, findings, pins | Verdict issued and violation | Apply its own enforcement, not this component's |
| `CONTRADICTED` | As above | Verdict issued and contradiction | Treat as a data or definition defect, not misconduct |
| `NOT_APPLICABLE` | Verdict, guard truth | Verdict issued | Not count as conformance |
| `NOT_IN_FORCE_AT_INSTANT` | Verdict, force resolution outcome | Verdict issued | Not count as conformance and not conclude the rule is irrelevant |
| `INDETERMINATE` | Verdict, subclass, code, cause | Verdict issued and indeterminate verdict | Route to the remedy owner of section 7.2 and not conclude conformity |
| `REFUSED` | Refusal, code, request | Nothing beyond the refusal | Correct the request or escalate |

**P2-7.30 (MUST) Recording obligations honoured.** An implementation must record everything the table above requires for the class of every outcome it produces.

**P2-7.31 (MUST) Emission obligations honoured.** An implementation must emit every event the table above requires.

**P2-7.32 (MUST) Caller obligations documented.** An implementation must document the caller obligations of the table above and must state that it does not enforce them.

**P2-7.33 (MUST NOT) No inference of conformity from the absence of violation.** An implementation must not describe a subject as conforming, compliant or passing in any report, projection or interface where the report contains an `INDETERMINATE` verdict or a vacuous satisfaction.

### 7.8 The one thing this section is for

If a single requirement of this part is to be preserved when the rest is compromised by schedule, it is this one.

**P2-7.34 (MUST) Unevaluable is never conforming.** An implementation must not, by any mechanism, configuration, default, aggregation, projection, interface, export or summary, represent a rule it could not evaluate as one that was satisfied.
## 8. Observability and the audit record

### 8.1 What the audit record is, in this model

The rows are the audit record. Because nothing specified in this part is ever updated in place, the sequence of appended rows is already a complete history of what the component was told, what it concluded, and when. There is no separate audit log recording changes to a mutable store, because there is no mutable store and no changes to record.

This is not a saving. It shifts the obligation from recording changes to recording enough at the time, and it makes one failure mode impossible while making another more likely. Impossible: an audit trail that disagrees with the data, or that was switched off. More likely: an evaluation that recorded a verdict without the pins needed to account for it, which cannot be repaired afterwards because the state that produced it is gone.

Two things must additionally be recorded because they are not state changes and therefore leave no row of their own.

**Reads.** A verdict read is a disclosure. Who asked what a rule concluded about a subject, and when, is frequently the question in an investigation.

**Non events.** A drift check that ran and found nothing, an example set re executed and agreed, an analysis that completed and found no contradiction. Each is a positive fact about assurance and each is invisible in a record that only holds changes. The absence of a drift observation is worthless as evidence unless the check that produced the absence was itself recorded, which is the substance of clause P2-3.41.

**P2-8.1 (MUST) Rows are the audit record.** An implementation must be able to produce, for any rule version, rule set version, run or verdict within its retained history, the complete sequence of rows concerning it in knowledge time order.

**P2-8.2 (MUST) No separate mutable log.** An implementation must not maintain an audit log whose contents can diverge from the rows, and must not provide a means of disabling the recording of any row this part requires.

**P2-8.3 (MUST) Negative assurance recorded.** An implementation must record every drift check, example re execution and static analysis that completed, including those that found nothing, with the identity of what was checked and the knowledge time.

**P2-8.4 (MUST NOT) No inference from an unrecorded check.** An implementation must not present the absence of an adverse finding as assurance where the check that would have produced it is not recorded.

### 8.2 Grain

The grain of the record is stated because a record whose grain is not stated cannot be relied upon and cannot be counted.

| Subject | Grain |
| --- | --- |
| Rule artifacts | One row per artifact per version. A version's artifact set is never amended. |
| Admission | One row per check per admission attempt. |
| Drift | One row per observation and one per resolution. |
| Drift check | One row per rule version per check cycle. |
| Rule set analysis | One row per analysis per set version. |
| Evaluation run | One row per run. |
| Pin | One row per artifact per run. |
| Verdict | One row per rule version per subject per run. |
| Finding | One row per violating witness, subject to declared truncation. |
| Witness | One row per instance examined, or a count where the implementation declares the count grain. |
| Derived assertion | One row per path per run. |
| Read | One row per verdict, report or rule artifact returned to a principal. |
| Signal | One row per signal per observation interval. |

**P2-8.5 (MUST) Declared grain.** An implementation must record at the grain of the table above, or declare a finer grain, and must not record at a coarser one.

**P2-8.6 (MUST) Witness grain declared.** An implementation must declare whether it records witnesses individually or as a count, and must record individually for any rule whose verdicts are cited as evidence.

**P2-8.7 (MUST) Counting grain stated with every count.** An implementation must state the grain of every count it reports.

### 8.3 What must be recorded with every evaluation

An evaluation's record must be sufficient to reproduce it. That is a strong requirement and it is testable: operation 24 of section 4.3 tests it directly, and clause P2-8.11 requires that the test be run on a cycle rather than only when someone asks.

Required: the request as received, including the idempotence key; the resolved rule set version; the resolved rule version for every member and the mode by which it was resolved; every pin with its identity, version and digest; the subject state digest and canonical form profile; the declared absences and withheld paths; the derivation closure, its strata and every derived assertion; every verdict envelope; every finding and witness; the budget declared, the budget consumed, and the point of exhaustion where applicable; the run outcome; the report digest; the identity of the principal and the authorisation reference; and the three clocks.

**P2-8.8 (MUST) Reproduction sufficiency.** An implementation must record enough with every run to reproduce every verdict in it, and must treat a run it cannot reproduce as a defect against clause P2-1.4.

**P2-8.9 (MUST) Request recorded as received.** An implementation must record the request as it was received, and must not record a normalised form in its place.

**P2-8.10 (MUST) Resolution mode recorded.** An implementation must record, for every member resolved by lineage, that the resolution was by lineage and the version it resolved to.

**P2-8.11 (MUST) Periodic reproduction.** An implementation must attempt reproduction of a declared sample of retained runs on a declared cycle, must record every divergence and every unobtainable pin, and must declare the sample and the cycle.

**P2-8.12 (MUST) Divergence recorded, not corrected.** An implementation must record a reproduction divergence as a finding about the record and must not amend the original verdict.

### 8.4 Access records

**P2-8.13 (MUST) Reads recorded.** An implementation must record every return of a verdict, an evaluation report, a rule artifact set or an evidence package to a principal, with the principal, the subject, the purpose and the knowledge time.

**P2-8.14 (MUST) Withholding recorded.** An implementation must record a read that was refused or reduced by an authorisation decision, with the decision reference, and must record it whether or not the requester was told.

**P2-8.15 (MUST NOT) No unrecorded export.** An implementation must not export an evidence package without recording the export, its recipient and its scope.

**P2-8.16 (SHOULD) Read records retained with the verdict.** An implementation should retain the read records of a verdict for as long as the verdict itself.

### 8.5 Signals

A signal is a standing measurement whose value tells someone whether the component is being used in a way that preserves what it guarantees. The signals below are required because each of them measures a specific way in which this part's guarantees are hollowed out in practice while every individual operation continues to succeed.

| Signal | Grain | Why it matters |
| --- | --- | --- |
| Vacuous satisfactions, by rule and set version | One verdict | A rule producing only vacuous satisfactions is checking nothing. Rising vacuity means the data stopped arriving, not that conformance improved. |
| Indeterminate verdicts by subclass and code | One verdict | Rising subject indeterminacy is a data supply failure presenting as a rules problem. |
| Rules with `UNDECLARED` authority | One rule version | The count of rules nobody can justify. |
| Rules with open drift, by kind | One rule version | The count of rules enforced on a superseded, withdrawn or unresolvable authority. |
| Rule versions in `SUSPENDED` | One rule version | Rules the organisation believes are being enforced and which are not being evaluated. |
| Rules in force and not admitted | One rule version | The same failure from the other direction. |
| Ungoverned term references | One term reference | Rules whose meaning is not anchored to a definition. |
| Pins recorded without a digest | One pin | The erosion of reproducibility. |
| Reproduction divergences and unobtainable pins | One run | Decay of the evidence base. |
| Runs terminated by budget, by resource kind | One run | Reports being read as complete that are not. |
| Short circuited evaluations reported as complete finding sets | One verdict | Understated finding counts. |
| Truncated finding sets | One verdict | The same. |
| Rule sets not statically analysed | One set version | Unknown consistency presented as consistency. |
| Non authoritative runs performed, by principal | One run | Use of the unadmitted evaluation path in place of the governed one. |
| Example sets not re executed within the declared cycle | One rule version | The bridge between statement and declaration going stale. |
| Verdict reads with no recorded purpose | One read | Erosion of the access record. |

**P2-8.17 (MUST) Signals produced.** An implementation must produce every signal in the table above at a declared interval and must declare the interval.

**P2-8.18 (MUST) Signals derived from rows.** An implementation must derive every signal from recorded rows and must be able to enumerate the rows behind any signal value.

**P2-8.19 (MUST NOT) No suppression of a signal.** An implementation must not provide a means of disabling, filtering or thresholding a signal in the table above such that a non zero value is reported as zero.

**P2-8.20 (MUST) Vacuity trend available.** An implementation must be able to report the vacuous satisfaction count for a rule over time, so that a rule which has stopped checking anything is distinguishable from one that always was vacuous.

**P2-8.21 (SHOULD) Signal thresholds declared.** An implementation should declare, for each signal, the value at which it is treated as requiring attention, and should record the declaration as a controlled document under `Part 1`.

### 8.6 The evidence package

An evidence package is a self describing export sufficient to account for a verdict without this component running. It exists because the second reader of section 1.3 will arrive after the implementation has been replaced.

Contents, all required:

The verdict envelope in full, and the whole report it belonged to.

The rule version's complete artifact set: declaration, every statement with its language and modality, every example with its asserted verdict, the authority reference with its basis and interpretation note, the classification and enforcement level, the term references, and the binding digest with its canonical form profile.

The authority itself: the content of the cited document version at the cited locator, obtained from `Part 1`, or a statement that it could not be obtained and why.

The rule set version's membership as declared.

Every pin, with the content of the pinned artifact where obtainable, or a statement that it was not.

The subject state as evaluated, or its digest and a statement of why the state itself is not included.

Every finding and witness, or the count and the declared truncation.

The derivation closure where derivation occurred.

The three clocks and the calendar, collation and arithmetic conventions in force for the run.

Every drift observation open against the rule version at the time of the run.

The reproduction history of the run, where any reproduction was attempted.

A statement of the version of this part the package claims to conform to.

**P2-8.22 (MUST) Package sufficiency.** An implementation must produce a package sufficient to account for the verdict without the implementation running and without access to any component of this standard other than the package.

**P2-8.23 (MUST) Authority content included or its absence stated.** An implementation must include the content of the cited authority clause in the package, or must state that it could not be obtained together with the reason.

**P2-8.24 (MUST) Conventions included.** An implementation must include the calendar, collation and arithmetic conventions in force for the run, since a verdict cannot be checked without them.

**P2-8.25 (MUST) Absence stated, not omitted.** An implementation must state, for every required element it could not include, that it could not be included and why, and must not omit the element silently.

**P2-8.26 (MUST) Package digest.** An implementation must record a digest over a declared canonical form of the package and must include the profile identity.

**P2-8.27 (MUST NOT) No package for a non authoritative run.** An implementation must not export a package presenting the verdicts of a non authoritative run as verdicts, per clause P2-4.14.

**P2-8.28 (MUST) Self description.** An implementation must include in the package a description of its own structure sufficient for a reader with no knowledge of the implementation to locate each required element.

### 8.7 Retention

**P2-8.29 (MUST) Retention obtained, not assigned.** An implementation must obtain the retention period of every record it holds from a retention rule expressed under `Part 1`, and must not assign a retention period of its own.

**P2-8.30 (MUST) Verdict retained at least as long as its subject's obligation.** An implementation must retain a verdict, its findings, its pins and its report for at least as long as the record of the act the verdict informed, where that period is known to it.

**P2-8.31 (MUST) Rule artifacts outlive their verdicts.** An implementation must retain the artifact set of a rule version for at least as long as the longest retained verdict issued from it, since a verdict whose rule has been disposed of cannot be accounted for.

**P2-8.32 (MUST) Disposal recorded.** An implementation must record the disposal of any record it holds, with the authorisation reference, and must retain the identity of what was disposed of.

**P2-8.33 (MUST NOT) No disposal of a rule version under an open drift observation.** An implementation must not dispose of a rule version's artifacts while a drift observation against it is `OPEN`.

### 8.8 What cannot be changed

**P2-8.34 (MUST NOT) No amendment of a recorded verdict.** An implementation must not modify a recorded verdict, its findings, its witnesses or its pin set by any mechanism, including administrative, migration, correction and support mechanisms.

**P2-8.35 (MUST NOT) No amendment of a rule version's artifacts.** An implementation must not modify the declaration, statement, example set, authority reference or classification of a recorded rule version.

**P2-8.36 (MUST) Migration preserves digests.** An implementation that migrates its records to another store or format must preserve every recorded digest unchanged and must record the migration as an event, and must not recompute a digest under a different canonical form profile without recording both.

**P2-8.37 (SHOULD) Independent anchoring.** An implementation should periodically publish a digest over its appended rows to a store it does not control, so that a later reader can establish that the record was not rewritten.
## 9. Extension model

### 9.1 Closed sets, open sets, and why

Three sets in this part are closed. Every other extensible set is open and governed by a registry.

**The verdict set of section 7.1 is closed.** A new member requires a revision of this part. The reason is that each member obliges every consumer to have a branch for it, and a consumer that meets an unknown member either crashes or falls through to a default. The default will be satisfaction or violation, and both are wrong. A closed set makes the exhaustiveness of a consumer's handling a checkable property.

**The indeterminacy subclasses of section 7.2 are closed.** A new subclass is a new remedy owner, and inventing one in a registry means routing findings to a party nobody agreed would receive them. Codes within a subclass are open, because a new code is handled by the branch the subclass already has.

**The truth domain of section 6.2 is closed at three values.** A fourth value changes every table in that section and every consumer's arithmetic. Section 13.4 records the argument for a fourth.

Everything else is open: expression languages, path schemes, enforcement level schemes, evaluation purposes, digest algorithms, verdict codes within their classes, refusal codes, event types, drift observation kinds, and canonical form profiles.

**P2-9.1 (MUST) Closed sets not extended.** An implementation must not add a member to the verdict set, the indeterminacy subclass set or the truth domain.

**P2-9.2 (MUST) Unknown member is a defect, not a default.** An implementation must treat receipt of a verdict member, subclass or truth value outside the closed sets as a `COMPONENT_DEFECT` and must not map it to a member it does recognise.

**P2-9.3 (MUST) Open sets registered.** An implementation must admit a member of an open set only through the registry mechanics of section 9.2, and must not accept an unregistered member at any interface.

### 9.2 Registry mechanics

Every registry in this part obeys the same rules, stated once.

A registry is content of a controlled document version under `Part 1`, so that a registration has an effective date, an approval and an author. A registry that is configuration rather than a controlled document has none of those, and the question of when a member was admitted becomes unanswerable.

Keys are permanent and are never reused. A member is deprecated rather than removed, because a record that referenced it must remain interpretable. Deprecation carries an effective date and a reason. A superseded member's entry is retained and marked.

Every registration states what it means, not only what it is called. A registered expression language whose entry does not state its evaluation semantics, its type system and its bounds is a name.

**P2-9.4 (MUST) Registry as controlled document.** An implementation must express every registry as content of a document version under `Part 1` and must resolve the registry version in force at the evaluation instant of any operation that reads it.

**P2-9.5 (MUST NOT) No key reuse.** An implementation must not reuse a registry key and must not remove a member that any retained record references.

**P2-9.6 (MUST) Deprecation rather than removal.** An implementation must deprecate a member with an effective date and a reason, and must continue to interpret records referencing it.

**P2-9.7 (MUST) Registry version pinned in every run.** An implementation must pin the version of every registry an evaluation read.

**P2-9.8 (MUST) Semantics in the entry.** An implementation must not admit a registry entry that does not state the meaning of the member in terms a consumer can act on.

### 9.3 Expression language registry

The most consequential registry in the part. Registering a language is admitting a semantics into the component, and the constraints below are the conditions under which the guarantees of sections 6 and 7 remain true.

A registration must state: the language identity and version; the version of the implementation, per clause P2-6.2; the type system and its coercion rules, if any; the truth domain and the connective semantics, which must be those of section 6.2; the treatment of an absent operand for every operator; the bound on computation and how it is enforced; whether sub expressions are addressable and in what path scheme; whether a decision procedure exists for satisfiability and containment; the collation and Unicode version for string comparison; the arithmetic model; and the calendar convention.

Initial members are an implementation decision. This part registers none, because registering one would make this part depend on the currency of a language specification it does not control.

**P2-9.9 (MUST) Language constraints satisfied.** An implementation must not register an expression language that permits effects, ambient clock reads, randomness, unbounded computation without an enforceable bound, or silent type coercion.

**P2-9.10 (MUST) Language semantics stated in full.** An implementation must state every element listed above in every expression language registration.

**P2-9.11 (MUST) Kleene semantics required of the language.** An implementation must not register a language whose connective semantics differ from the tables of section 6.2, and must not adapt a two valued language by mapping its result onto three values.

**P2-9.12 (MUST) Implementation version registered separately.** An implementation must register and pin the version of the language implementation separately from the version of the language specification.

**P2-9.13 (MUST) Language change is a rule dependency change.** An implementation must re execute the example set of every rule version pinned to a language whose registration changes, per clause P2-3.47.

### 9.4 Path scheme registry

A path scheme is how a finding says where. A registration states the syntax, what a path denotes, whether a path is stable across changes to the subject, and whether the scheme addresses sub expressions of a declaration as well as positions in a subject.

Stability is the property worth registering and the one most often absent. A path expressed as an ordinal position in a collection denotes a different thing after an insertion, so a finding recorded against it becomes false without anything having changed. A path expressed against a stable key does not.

**P2-9.14 (MUST) Stability declared.** An implementation must declare, for every registered path scheme, whether a path in it remains valid across changes to the subject, and must record the scheme with every path.

**P2-9.15 (SHOULD) Stable schemes preferred for findings.** An implementation should record findings in a path scheme declared stable, and should record both a stable and a positional path where only the positional one is available.

**P2-9.16 (MUST NOT) No cross scheme comparison.** An implementation must not compare, deduplicate or match paths recorded in different schemes.

### 9.5 Enforcement level scheme registry

SBVR 1.5 defines enforcement level as a position on a graded scale and does not standardise the values. Registering the scheme is how this part makes an unstandardised concept usable without inventing a standard for it.

A registration must state: the members; their order, since a graded scale without an order is a set of labels; for each member, what is expected of an actor who encounters a violation at that level; and whether the level admits an override and by whom.

An implementation must register at least one scheme. A scheme comprising a single member is admissible and is a truthful statement that the organisation does not grade enforcement, which is preferable to a scheme of six members used as two.

**P2-9.17 (MUST) Ordering declared.** An implementation must declare a total or partial order over the members of every enforcement level scheme.

**P2-9.18 (MUST) Meaning declared per member.** An implementation must state, for every member, what is expected of an actor on encountering a violation at that level.

**P2-9.19 (MUST NOT) No behaviour from the level.** An implementation must not vary its own behaviour on the level, per clause P2-3.60, and must not admit a registration that requires it to.

**P2-9.20 (MUST) Guideline level admissible.** An implementation must permit a scheme member denoting a rule that is evaluated and not enforced, and must evaluate rules at that level identically to any other, consistently with SBVR's treatment of guidelines as rules.

### 9.6 Evaluation purpose registry

A purpose is why an evaluation was requested. It is registered because it appears in the access record, because `Part 7` may condition an authorisation on it, and because the mix of purposes over time is the clearest signal of how a rule set is actually used.

Purposes that must be distinguished, at minimum: evaluation informing an act about to be taken; retrospective evaluation of a past state; evaluation for the purpose of testing a rule; evaluation for the purpose of reproducing a recorded run; and evaluation in the course of an assessment by `Part 12`.

**P2-9.21 (MUST) Purpose registered and recorded.** An implementation must register every purpose and must record the purpose of every evaluation.

**P2-9.22 (MUST) Minimum purpose distinctions.** An implementation must register at least the five purposes named above as distinct members.

**P2-9.23 (MUST NOT) No default purpose.** An implementation must not default the purpose of an evaluation and must refuse a request that omits it.

### 9.7 Digest algorithm and canonical form registries

Digests appear in this part over subject states, reports, packages, rule binding sets and derived values. Both the algorithm and the canonical form must be registered, because a digest without its canonical form profile is uncheckable: a later reader recomputing it will serialise differently and conclude that the record was altered.

**P2-9.24 (MUST) Both registered and both recorded.** An implementation must register digest algorithms and canonical form profiles separately and must record both with every digest.

**P2-9.25 (MUST) Deprecation without invalidation.** An implementation must be able to mark a digest algorithm deprecated without invalidating any recorded digest, and must record an additional digest under a current algorithm rather than replacing the original.

**P2-9.26 (MUST NOT) No digest without a profile.** An implementation must not record a digest whose canonical form profile is not recorded.

### 9.8 Verdict code and refusal code registries

Codes within the `INDETERMINATE` class are registered within a subclass. Refusal codes are registered without subclassing. Every registration states the cause, whether the operation is retryable, and which party owns the remedy.

**P2-9.27 (MUST) Subclass allocated at registration.** An implementation must allocate every registered indeterminacy code to exactly one subclass at registration and must not reallocate it.

**P2-9.28 (MUST) Remedy owner stated.** An implementation must state the remedy owner in every indeterminacy code registration, consistently with section 7.2.

**P2-9.29 (MUST) Retryability stated.** An implementation must state retryability in every refusal code registration.

### 9.9 Event type and drift kind registries

**P2-9.30 (MUST) Event types registered.** An implementation must register every event type it emits beyond the minimum set of section 4.7.

**P2-9.31 (MUST) Drift kinds registered.** An implementation must register every drift observation kind beyond those enumerated in section 3.7, and must state for each what condition it reports and how it is detected.

### 9.10 Composition of rules and rule sets

Three compositions are distinguished, and confusing them is a real defect rather than a modelling nicety.

**A rule set containing rules.** Membership. Every member is evaluated independently and produces its own verdict. Membership is the only composition this part specifies for evaluation.

**A rule set containing a rule set.** Inclusion. Permitted, provided the included set version is pinned, so that the effective membership of the including version is fixed. An inclusion by lineage would make the including set's membership change without the including set changing, which defeats the whole purpose of declaring membership.

**A rule whose declaration references another rule.** Prohibited by clause P2-6.43. A rule that reads another rule's verdict is a composition of propositions, and composing propositions into a conclusion is what `Part 5` does. The temptation is strong because the alternative is duplicating a condition, and the cost of yielding is that the rule set acquires an execution order.

There is a fourth thing that looks like composition and is not: a rule whose declaration shares a sub expression with another rule. Sharing is a factoring convenience, is permitted, and creates a dependency that must be pinned like any other, because a change to a shared sub expression changes both rules and must produce a new version of both.

**P2-9.32 (MUST) Inclusion by pinned version only.** An implementation must permit a rule set version to include another rule set only by pinned version, and must not permit inclusion by lineage.

**P2-9.33 (MUST) Effective membership derivable.** An implementation must be able to enumerate the effective membership of a rule set version including every transitively included member, and must record the count with its grain.

**P2-9.34 (MUST NOT) No cyclic inclusion.** An implementation must refuse a rule set version whose inclusion graph contains a cycle.

**P2-9.35 (MUST) Shared sub expressions versioned.** An implementation must treat a change to a shared sub expression as producing a new version of every rule version that references it, and must pin the sub expression version in each.

**P2-9.36 (MUST NOT) No verdict composition.** An implementation must not provide a means by which the verdicts of several rules are combined into a single conclusion about the subject, and must return the verdicts, per clause P2-3.108.
## 10. Standards and specifications

### 10.1 How the citations in this part are to be read

Every entry below states what the source supplies, the edition established as current at the date of this part, and whether this part's account of it rests on the specification text or on secondary sources. The distinction is recorded because a requirement said to follow from a standard the author did not read is a requirement resting on hearsay, and a reader is entitled to know which requirements those are. Section 13.1 lists the sources not obtained.

Where a clause of this part rests on practice rather than on specification text, section 10.7 and section 13.6 say so. A control adopted from practice is not weaker, but its basis must not be misrepresented as normative.

Currency was established from publisher catalogues and status pages rather than inferred. Three of the sources a reader would expect to be current are not, and two are moving.

**P2-10.1 (MUST) Cited edition recorded.** An implementation must record the edition or version of every external standard it relies upon, and must not cite a standard without its edition.

**P2-10.2 (MUST) Basis marked.** An implementation must record, for every control it adopts from a source named in this section, whether the basis is specification text or practice.

### 10.2 Business rule modelling: the OMG family

| Standard | Status established | Supplies | Basis of this part's account |
| --- | --- | --- | --- |
| SBVR 1.5 | Formal, published December 2019. A 1.5 beta exists for information only. | The rule as a proposition claiming obligation or necessity. The behavioural against definitional distinction. Enforcement level as a graded scale, explicitly independent of the rule's guidance and explicitly not standardised. The rule statement as the guidance message. Structured English. | Scope and the cited concepts from secondary sources including an extract of pages 118 to 119 reproduced in commentary. The clause text was not obtained. |
| DMN 1.5 | Current formal version, adopted August 2024. Versions 1.6 beta and 1.7 beta both dated September 2024 are in process; 1.7 is the latest inventory. Prior formals 1.4 (April 2023), 1.3 (February 2021), 1.2, 1.1, 1.0. | Decision requirements diagrams, decision tables with hit policies, and the FEEL expression language. Completeness and consistency checking over decision tables. | Scope statement obtained from the publisher. Internals from secondary sources. |
| PRR 1.0 | Adopted 2009. PRR Core is normative; the PRR OCL set is non normative. A 1.1 was announced as planned and no evidence of its publication was found. | A production rule metamodel at the platform independent level, and the match, conflict resolution, act summary that RIF-PRD later cites. | Scope and conformance points obtained from the publisher. |

Note on DMN's version state, because it affects how a citation should be written. The most recent formal version is 1.5 and two later betas exist, both published one month after it. A citation to "DMN" without a version therefore does not identify a document, and a citation to the latest DMN identifies a beta that the publisher marks as informational.

Note on the relationship among the three. SBVR and DMN and PRR are all OMG standards and they do not share a notion of what a rule is. Section 10.8 states the conflict.

### 10.3 Rule interchange: the W3C family

| Standard | Status established | Supplies |
| --- | --- | --- |
| RIF-PRD, Production Rule Dialect, Second Edition | W3C Recommendation, 5 February 2013. One of a set of thirteen RIF documents. The Working Group's work is complete; comments may be addressed in errata or future revisions. | An interchange serialisation for production rules, and a normative operational semantics: match, conflict resolution, act, loop until a terminal state. |

RIF-PRD is cited in this part chiefly for what it specifies that this part excludes. Its operational semantics is the clearest normative statement available of what a production rule system does, and section 3.18 uses it to say precisely which four properties this part cannot accept. That is a use of a standard, not a rejection of it: a specification that fences off a semantics should name the document that defines the semantics it is fencing off.

### 10.4 Constraint and validation languages

| Standard | Status established | Supplies | Basis |
| --- | --- | --- | --- |
| SHACL 1.0 | W3C Recommendation, 20 July 2017. Remains the Recommendation at the date of this part. | Shapes as constraints over graphs. The validation report as a first class artifact, with results carrying a focus node, a path, a value, a source shape and a severity. Severity as a property of the shape. Core and a SPARQL based extension mechanism. Recursion explicitly left undefined and delegated to implementations. | Specification text obtained. |
| SHACL 1.2 family | In the W3C technical report space through 2025 and 2026. Core and SPARQL editor's drafts were published for review in November 2025 targeting Candidate Recommendation in January 2026. A separate SHACL 1.2 Rules document exists. A First Public Working Draft of SHACL 1.2 User Interfaces was published in 2026. | The separation of Core from SPARQL extensions, and the separation of Rules, that is inferencing, from constraint validation. A security consideration naming rule sets that cause excessive computation. | Status pages and announcements obtained. The maturity level of each document at the date of this part could not be established; see section 13.1. |
| ISO/IEC 19757-3:2025, Schematron | Edition 4, published September 2025, 51 pages. Cancels and replaces ISO/IEC 19757-3:2020, which is withdrawn. Already at the stage indicating an International Standard to be revised, with a further edition in preparation. | Rule based validation with assert and report, natural language assertion text held inside the schema, patterns and contexts, role and flag attributes, and query language bindings. A validator defined as a function returning valid, invalid or error. | Foreword, scope, structure and the validator definition obtained. Full clause text not obtained. |
| JSON Schema | Current release 2020-12, which the publisher continues to label a draft. Previous release 2019-09. Not ratified as a standard by any standards development organisation. | Structural and value constraints over JSON, and by far the widest deployment of any constraint language reviewed. | Publisher status page obtained. |

Two observations from this table shape the part.

The first is the Schematron definition of a validator as returning valid, invalid or error. It is the only normative statement found in any current standard that a constraint checker's return type has three members rather than two, and section 6.2 rests on it.

The second is the state of JSON Schema. The most widely deployed constraint language in the world is on a release its own publisher calls a draft, from 2020, with no ratification. That is not a criticism of it; it is a caution against the assumption that wide deployment implies a stable normative reference, and it is the reason section 9.3 requires an implementation to register the semantics of its expression language itself rather than by citation.

### 10.5 Logical foundations

These are not standards and are cited as literature. Section 6.2 depends on them and the dependency should be visible.

| Source | Supplies |
| --- | --- |
| Kleene's strong three valued system | The connective semantics required by section 6.2, in which an indeterminate operand yields an indeterminate result except where the other operand determines it. |
| Łukasiewicz's three valued system | An alternative in which an implication with indeterminate antecedent and consequent is true. Rejected in section 6.2, with the reason stated. |
| Belnap's four valued system | A treatment of contradictory as distinct from unknown. Not adopted; recorded as open in section 13.4. |
| The temporal database literature on valid and transaction time | The two clock model this part inherits from `Part 1`. |

SQL is a partial specification anchor and a cautionary one. Its `NULL` handling implements a three valued logic for the connectives and then treats the third value as failure at the boundary of a filter. This part's clause P2-6.9 exists because of that pattern. The account here rests on secondary sources and general knowledge; the edition of ISO/IEC 9075 in force was not established, and section 13.1 records that.

### 10.6 Adjacent standards deliberately not used

| Standard | Why not used here |
| --- | --- |
| XACML and its successors | Policy evaluation for authorisation. Belongs to `Part 7`. A verdict is not a permit or a deny, and adopting an authorisation vocabulary here would invite exactly that conflation. |
| BPMN | Process orchestration. Belongs to `Part 6`. DMN is designed to be usable alongside BPMN, and this part uses neither for control flow. |
| Business Motivation Model | Motivation and the relation of rules to goals. Out of scope: this part specifies evaluation, not why an organisation holds a rule. |

### 10.7 Supporting specifications

| Specification | Used for |
| --- | --- |
| RFC 2119 and RFC 8174 | Requirement keywords and their upper case forms. |
| BCP 47 | Language tags on every statement and text value. |
| RFC 3339 and ISO 8601 | Instant representation for the three clocks. |
| The Unicode Collation Algorithm and the Unicode Standard | Collation and Unicode version pinning under clause P2-6.3. |
| RFC 8785, JSON Canonicalization Scheme | An example of a canonical form profile of the kind section 9.7 requires. Named as an example, not required. |
| RFC 9457 | A model for conveying a problem in a response, relevant to how refusals of section 7.5 may be expressed. |
| CloudEvents | A model for the event envelope of section 4.7. |

The following clauses of this part rest on practice rather than on specification text, and are collected here so that a reader can see the set: clause P2-3.38 on a declared drift check cycle; clause P2-3.42 on a minimum example set; clause P2-6.3 on collation pinning; clause P2-6.4 on decimal arithmetic for monetary comparison; clause P2-6.26 on a declared calendar convention; clause P2-8.11 on periodic reproduction; clause P2-8.13 on recording all reads; and clause P2-8.37 on independent anchoring.

**P2-10.3 (MUST) Practice basis recorded.** An implementation that adopts a clause listed in the paragraph above as a control must record that its basis is practice.

### 10.8 Named conflicts

Six conflicts among current standards bear directly on this part. None is resolved by averaging.

**What a rule is.** SBVR 1.5 says a proposition claiming obligation or necessity. PRR 1.0 and RIF-PRD say a construct that matches, is selected by conflict resolution, and acts. DMN 1.5 says, in its decision tables, a row that yields an output value. These are not three views of one thing. The first has a truth value and no behaviour; the second has behaviour and no truth value; the third has a value and neither. **Position taken.** This part adopts the SBVR sense for a rule, fences the PRR and RIF-PRD sense into derivation under section 3.18, and allocates the DMN sense to `Part 5`, which is what a decision table is for.

**Whether a validator returns two values or three.** ISO/IEC 19757-3:2025 says a validator returns valid, invalid or error. SHACL 1.0's validation report carries a conformance boolean alongside its results, with execution failures signalled separately from non conformance. JSON Schema is two valued. **Position taken.** Three, structurally, per section 7.1, and the third is a verdict rather than a signalling channel beside the verdict.

**Where enforcement lives, and whether it can move.** SBVR 1.5 places enforcement level on the rule and states that it may change independently of the rule. SHACL places severity on the shape. Neither says who acts on it or what acting means. **Position taken.** On the rule version, pinned to a registered scheme, never acted on here, and a change of level produces a new version. The last of those diverges from SBVR and section 13.5 records the divergence and its cost.

**Whether termination is the standard's problem.** SHACL 1.0 explicitly leaves validation with recursive shapes undefined and delegates it to implementations, so that two conforming processors may differ on whether a shapes graph can be evaluated at all. RIF-PRD's semantics is a loop with no termination guarantee. The SHACL 1.2 Rules document raises excessive computation as a security consideration rather than a semantic one. **Position taken.** Termination is an admission property, enforced by declared stratification and a deterministic budget, per sections 6.6 and 6.7.

**Whether inferencing belongs with constraint checking.** The SHACL 1.2 family separates Rules from Core, treating inferencing as a distinct specification. RIF-PRD makes acting intrinsic to what a rule is. DMN has no notion of asserting into the subject at all. **Position taken.** Separated, phased, stratified, monotonic and optional, per section 3.18.

**Whether the natural language statement is part of the rule.** Schematron places assertion text inside the assertion, so the message is in the schema. SBVR treats the statement as the guidance message. SHACL provides a message on the shape. DMN provides annotations that the specification states carry no semantics. So three of the four put the human readable text inside the artifact, and none of them makes it normative or requires it to be approved. **Position taken.** The statement is a required, approved, digest bound component of the rule, per section 3.2, and this is a strengthening of what the standards provide rather than an adoption of it.

### 10.9 What none of the standards supplies

Twelve requirements in this part have no source. They are listed so that a reader can see which parts of this specification are inventions and hold them to a higher standard of scrutiny than the parts with a citation.

Vacuous satisfaction is not addressed by any standard reviewed. None requires a validator to report that a constraint examined nothing, and the condition is therefore invisible in every conforming implementation.

The binding of a rule to the clause of a controlled document that authorises it. No reviewed standard has a place to put it.

Detection of authority drift, and the requirement that the response be a signal rather than a disable.

Reproducibility of a verdict from a recorded pin set. No reviewed standard requires a validator to record what it read.

Point in time evaluation against the rule set in force at a past instant. DMN, SHACL, Schematron and JSON Schema are all atemporal.

Worked examples as a required, approved component of a rule rather than as tests held elsewhere.

The distinction between a withheld input and an absent one.

Pinning of collation, Unicode version, arithmetic model and calendar convention, without which no verdict involving a string, a number or a date is reproducible across implementations.

The separation of the verdict from the enforcement action, as a prohibition on the evaluator rather than as advice.

Allocation of an inability to evaluate to a remedy owner.

The prohibition on reporting an unanalysed rule set as consistent.

Retention of a rule's artifacts for longer than the verdicts issued from it.

**P2-10.4 (MUST) Unsourced requirements identified.** An implementation must be able to state, for any control it implements under this part, whether the requirement has a cited source in this section or is listed in section 10.9 as unsourced.
## 11. Anti patterns

Each entry names the mechanism by which the failure occurs, states the consequence, and marks whether the prohibition rests on specification text or on practice. A design smell without a mechanism is not actionable, because two systems that look alike can differ in whether the mechanism is present.

### 11.1 The boolean at the edge

**Mechanism.** Every distinction in this part is produced correctly and then discarded at the outermost interface, which returns whether the subject passed. Indeterminacy must be folded into the boolean; whichever way it is folded is wrong, and the choice is made by a developer at a keyboard rather than by anyone accountable.

**Consequence.** The component's entire value is destroyed at the last step, and the destruction is invisible because everything upstream is correct.

**Basis.** Practice.

**P2-11.1 (MUST NOT) No boolean edge.** An implementation must not expose an interface whose result for an evaluation is a single truth value or pass indicator, per clause P2-3.108.

### 11.2 The filter that eats the third value

**Mechanism.** The expression language implements three valued logic correctly for its connectives and then reduces a collection with a filter whose semantics treat the third value as exclusion. The rule that should have been indeterminate becomes satisfied, because the rows it could not evaluate simply are not there.

**Consequence.** Indeterminacy is silently converted to satisfaction at a point no rule author can see, in a language construct that looks like it is doing nothing of the kind.

**Basis.** Specification text, in that SQL's treatment of the unknown value at a filter boundary is well attested, though the edition was not established.

**P2-11.2 (MUST NOT) No collapse at a reduction.** An implementation must not treat `INDETERMINATE` as `FALSE` at the boundary of any operation that reduces a collection, per clause P2-6.9.

### 11.3 Salience as semantics

**Mechanism.** Rules are given priority numbers, and the behaviour of the rule set is determined by their relative values. No author wrote the priorities down as a rule; no authority document contains them; nobody reviews them; and changing one changes the system's behaviour without changing any rule.

**Consequence.** The rule set becomes a program whose control flow is expressed as integers scattered across the rules, and the organisation's actual policy is not any document it holds.

**Basis.** Specification text, in that RIF-PRD makes conflict resolution intrinsic to production rule semantics and this part excludes it.

**P2-11.3 (MUST NOT) No salience.** An implementation must not admit a priority, salience, specificity or order value that affects any verdict or any derivation outcome, per clauses P2-3.68 and P2-3.117.

### 11.4 The rule that carries its action

**Mechanism.** The rule and the response to its violation are one artifact: the rule ends with a block, a rejection, an email or a status change. Asking the system what it believes requires deploying what it does.

**Consequence.** The rule cannot be evaluated in a report, a simulation, a retrospective or an assessment, because evaluating it does something. Nobody can ask what would happen, so nobody asks.

**Basis.** Practice, though SBVR's separation of enforcement level from the rule's guidance supports the underlying distinction.

**P2-11.4 (MUST NOT) No embedded action.** An implementation must not admit a declaration containing an action or effect, per clause P2-3.25, and must not act on a verdict, per clause P2-1.2.

### 11.5 Prose as a comment

**Mechanism.** The natural language statement is held as a comment in the declaration or as a description field beside it, and is not versioned, approved or bound. The declaration is the artifact under change control and the sentence is decoration.

**Consequence.** The sentence and the expression diverge, and every human reader of the rule reads the sentence. The organisation believes one thing and enforces another, and the divergence is discovered when somebody is asked to explain a verdict.

**Basis.** Practice, though Schematron's placement of assertion text inside the assertion shows the alternative is available.

**P2-11.5 (MUST NOT) No unversioned statement.** An implementation must hold the statement as an artifact of the rule version, bound by the binding digest, per clauses P2-3.6 and P2-3.49.

### 11.6 The rule with no authority

**Mechanism.** Rules accumulate over years, each added because somebody needed it, and none records the clause it implements. The rule set is a strata of decisions whose authors have left.

**Consequence.** No rule can be retired, because nobody can establish that it is no longer required. The rule set grows monotonically and its review becomes impossible in proportion to its size.

**Basis.** Practice.

**P2-11.6 (MUST NOT) No admission without an authority reference.** An implementation must not admit a rule version without a `rule_authority`, and must record `UNDECLARED` where none exists rather than omitting the reference, per clauses P2-1.7 and P2-3.36.

### 11.7 The authority that is a person

**Mechanism.** The authority field holds a name: a rule exists because a named individual asked for it. This is often true and is not an authority, because it is not resolvable, not dated, and not reviewable.

**Consequence.** When the person leaves, the rule's justification leaves with them, and the rule becomes unretirable for the reason given in section 11.6.

**Basis.** Practice.

**P2-11.7 (MUST NOT) No actor as authority.** An implementation must not accept an `ACTOR` as an authority reference, and must record a management decision as a citation to a document version recording that decision.

### 11.8 The silent disable

**Mechanism.** The component detects that a rule's authority has been withdrawn and stops evaluating the rule, on the reasonable ground that a rule without authority should not be enforced.

**Consequence.** What the organisation permits changes, with no decision, no record and no notification. This is worse than continuing to enforce a superseded rule, because the second is visible in the verdicts and the first is visible nowhere.

**Basis.** Practice.

**P2-11.8 (MUST NOT) No disable on drift.** An implementation must continue to evaluate a rule whose authority has been superseded, withdrawn or made unresolvable, and must report the condition, per clauses P2-3.10 and P2-4.26.

### 11.9 The guard folded into the body

**Mechanism.** The applicability condition is written as the antecedent of an implication inside the body. Every subject to which the rule does not apply satisfies the implication vacuously and is reported as satisfying the rule.

**Consequence.** A report of ten thousand satisfactions where nine thousand nine hundred were inapplicable. The number of checks performed is overstated by two orders of magnitude, and the overstatement grows as the rule set broadens.

**Basis.** Practice.

**P2-11.9 (MUST NOT) No applicability in the body.** An implementation must not admit a declaration expressing applicability as an antecedent in the body where the language permits a guard, per clause P2-3.54.

### 11.10 The vacuous green

**Mechanism.** A rule quantifies over a collection that is empty, yields true, and is reported as satisfied with no indication that nothing was examined. The collection is empty because the data stopped arriving.

**Consequence.** The rule most likely to be vacuous is the rule whose data is broken, so the mechanism converts the most serious data failures into the cleanest reports. Conformance appears to improve at the moment it stops being measured.

**Basis.** Practice. No reviewed standard addresses vacuity; see section 10.9.

**P2-11.10 (MUST NOT) No vacuous satisfaction without its flag.** An implementation must not present a vacuous satisfaction as a satisfaction, per clauses P2-3.91 and P2-7.3.

### 11.11 The rule in the application

**Mechanism.** The rule is a conditional in application code. It has no version separate from the release, no effective date, no approval, no statement, no authority and no verdict record.

**Consequence.** The organisation cannot enumerate the rules it enforces, cannot date a change to one, and cannot answer what governed a past act. This is the condition that `Part 1` clause P1-12.4 and this part exist to end.

**Basis.** Specification text, in that this is the naive conflation `Part 1` section 12.2 names.

**P2-11.11 (MUST NOT) No rule outside the model.** An implementation must not evaluate a condition as a rule under this part unless it is a recorded rule version with the artifact set of section 3.

### 11.12 Reference data read live

**Mechanism.** The rule tests membership in a code list read from the current version of the list at evaluation time, with no pin. Verdicts change when the list changes and nothing records that the list was what changed.

**Consequence.** Two evaluations of the same subject against the same rule disagree, and the disagreement is unattributable. A historical subject becomes non conformant because a code was retired years after it was used.

**Basis.** Practice.

**P2-11.12 (MUST NOT) No unpinned reference read.** An implementation must pin every reference set version it reads and must resolve it as of the evaluation instant, per clauses P2-3.121 and P2-3.122.

### 11.13 The clock in the expression

**Mechanism.** The declaration computes an interval against the current time. The rule is correct and the verdict is not reproducible: the same request yields a different answer tomorrow.

**Consequence.** Every verdict from every such rule is unreproducible, and the failure is discovered only when someone tries to account for one, which is years later and in an investigation.

**Basis.** Practice.

**P2-11.13 (MUST NOT) No ambient clock in a declaration.** An implementation must not admit a declaration that reads a clock, per clause P2-6.24.

### 11.14 Severity in the message

**Mechanism.** The only representation of how serious a violation is is the word CRITICAL at the start of the message text. Consumers parse the string; changing the wording changes the behaviour of downstream systems.

**Consequence.** The enforcement level cannot be queried, counted, reviewed or changed without editing prose, and a translation of the message changes the severity.

**Basis.** Practice.

**P2-11.14 (MUST NOT) No severity in prose only.** An implementation must record the enforcement level as a registered value and must not rely on the text of a statement or message to convey it, per clause P2-3.63.

### 11.15 The treat errors as pass switch

**Mechanism.** A configuration flag, usually introduced during an incident, causes rules that could not be evaluated to be reported as satisfied so that processing continues.

**Consequence.** The component now certifies as conforming exactly those subjects it knows least about. The flag is never removed, because removing it produces a flood of findings that looks like a regression.

**Basis.** Practice.

**P2-11.15 (MUST NOT) No fail open configuration.** An implementation must not provide a means by which an `INDETERMINATE` verdict is reported as `SATISFIED`, per clauses P2-1.6 and P2-7.34.

### 11.16 The treat errors as violations switch

**Mechanism.** The converse, and usually well intentioned: unevaluable rules are reported as violated so that nothing slips through.

**Consequence.** Findings are manufactured against conforming subjects. The finding queue fills with items nobody can close, because the subject is fine and the rule cannot be evaluated. Within a quarter, users learn that findings are unreliable, which is a worse outcome than the leak the switch was meant to prevent.

**Basis.** Practice.

**P2-11.16 (MUST NOT) No fail closed configuration.** An implementation must not provide a means by which an `INDETERMINATE` verdict is reported as `VIOLATED` or `CONTRADICTED`.

### 11.17 The mega rule

**Mechanism.** One rule with forty conjoined conditions, one statement, one authority and one message. It is a rule because it is one row in a table.

**Consequence.** A violation says only that one of forty conditions failed. The finding cannot identify which, because the rule's granularity is the granularity of its verdict. The rule cannot be partly superseded, its authority is necessarily a whole document, and its statement is necessarily vague.

**Basis.** Practice.

**P2-11.17 (SHOULD NOT) No undecomposed conjunction.** An implementation should not admit a rule whose body is a conjunction of independently authorised conditions, and should require each condition with a distinct authority to be a distinct rule.

### 11.18 One rule per sentence

**Mechanism.** The opposite failure, produced by mechanically converting a regulation into rules sentence by sentence. Definitions become rules, scoping paragraphs become rules, and cross references become rules.

**Consequence.** A rule set of thousands of members, most of which can never produce a finding, all of which require review and carry authority references. The review burden makes real review impossible, which is the same outcome as having no rules.

**Basis.** Practice.

**P2-11.18 (SHOULD NOT) No mechanical granularity.** An implementation should not admit a rule that cannot produce a finding against any subject, and should report such rules under the analysis of section 6.9.

### 11.19 The suppression list

**Mechanism.** A list of subject and rule pairs whose verdicts are hidden, added to whenever a finding is judged not to matter. The list is configuration, has no authority, no expiry and no approval.

**Consequence.** A parallel and unreviewable rule system that overrides the reviewable one. The real policy of the organisation is the rule set minus the suppression list, and only one of the two is under control.

**Basis.** Practice.

**P2-11.19 (MUST NOT) No verdict suppression.** An implementation must not provide a means of suppressing, hiding or filtering a recorded verdict, and must express any decision to tolerate a violation as a recorded act elsewhere rather than as an absence here.

### 11.20 The warning nobody clears

**Mechanism.** Rules at a low enforcement level produce findings that nothing obliges anyone to address. The count grows without bound. After two years it is a number in the hundreds of thousands that everyone has learned to ignore.

**Consequence.** The low level becomes indistinguishable from no rule, and worse, the high level findings are now hidden in the same queue.

**Basis.** Practice, and it is a consequence of correct behaviour rather than of a defect, which is why the remedy is a signal rather than a prohibition.

**P2-11.20 (SHOULD) Unaddressed finding age reported.** An implementation should report the age distribution of findings by enforcement level, so that a level that has ceased to mean anything is visible.

### 11.21 Examples generated from the declaration

**Mechanism.** The example set required by section 3.8 is produced by running the declaration and recording what it returns. Every example passes by construction.

**Consequence.** The only mechanically checkable bridge between the statement and the declaration is replaced by a tautology. The check still runs, still passes, and now proves nothing, which is worse than not having it because it produces assurance.

**Basis.** Practice.

**P2-11.21 (MUST NOT) No generated examples.** An implementation must not satisfy the example requirement with examples produced by executing the declaration, and must record the provenance of every example, per clause P2-3.48.

### 11.22 The rule set assembled by query

**Mechanism.** The rule set is defined as whatever rules match a query: all rules tagged retention, all rules for this jurisdiction. Membership is computed at evaluation time.

**Consequence.** Nobody can say what was evaluated last year, because the query would return something different now. A rule silently joins the set when someone adds a tag, and an evaluation report becomes uninterpretable as evidence.

**Basis.** Practice.

**P2-11.22 (MUST NOT) No computed membership.** An implementation must express rule set membership as declared content and must not compute it from a query at evaluation time, per clause P2-3.64.

### 11.23 Re evaluation without re pinning

**Mechanism.** A subject's compliance position is refreshed by evaluating it again against the current rule set and comparing with the previous verdict. Any difference is attributed to the subject.

**Consequence.** A rule change, a reference data change and a subject change are indistinguishable in the comparison, so the one thing the comparison is used for is the one thing it cannot establish. Trend reporting built on it is unfalsifiable.

**Basis.** Practice.

**P2-11.23 (MUST NOT) No comparison across differing pins.** An implementation must not present a comparison of two verdicts whose pin sets differ as a change in the subject, and must identify which pins differed.

### 11.24 The rule that reads another rule

**Mechanism.** A rule's condition refers to whether another rule was violated, in order to avoid restating a condition.

**Consequence.** The rule set acquires an evaluation order, determined by a dependency graph nobody wrote as a rule. Order independence is lost, and with it the ability to evaluate one rule without evaluating the set.

**Basis.** Practice, and it is the composition that `Part 5` exists to perform.

**P2-11.24 (MUST NOT) No verdict as an operand.** An implementation must not admit a rule whose declaration or guard reads another rule's verdict, per clause P2-6.43.

### 11.25 Floating point money

**Mechanism.** A threshold comparison over a monetary or quantity value is performed in binary floating point. The comparison is correct almost always and wrong at the boundary, and the boundary is exactly where thresholds are set.

**Consequence.** A verdict that differs between platforms, between library versions, and between the engine and the spreadsheet somebody used to check it. The disagreement is attributed to the rule for months.

**Basis.** Practice.

**P2-11.25 (MUST NOT) No binary floating point at a threshold.** An implementation must not use binary floating point for an equality or threshold comparison of a monetary or quantity value, per clause P2-6.4.

### 11.26 The evaluator that is also the gate

**Mechanism.** The component that evaluates the rules is the component that permits or denies the operation, because it already has the answer and adding the check saves a call.

**Consequence.** The rule set can no longer be evaluated for a report, a simulation or an assessment, since evaluation is now an authorisation event. Every consumer that wanted to ask a question is now taking an action, and the two cannot be separated afterwards without rewriting both components.

**Basis.** Specification text, in that `Part 1` section 12.7 and section 12.7 here allocate authorisation to `Part 7`.

**P2-11.26 (MUST NOT) No gating.** An implementation must not permit, deny or gate any operation, per clause P2-1.3.
## 12. Boundaries with other parts

Each subsection below states four things: what this component delegates, what it must not absorb, the naive design that conflates the two, and the reciprocal declaration the other part must make. Subsection numbers correspond to part numbers, so section 12.7 states the boundary with `Part 7` and section 12.14 states the boundary with `Part 0`. Section 12.2 is deliberately unused, since it would designate this part. Numbers are permanent.

A boundary is reciprocal. If this part declares that it delegates something, the receiving part must declare that it owns it, in the same terms. A boundary declared on one side only is not a boundary; it is a hope.

**P2-12.1 (MUST) Declared allocation.** An implementation must be able to state, for every capability named in this section as delegated, which component provides it, and must not provide it within this component.

**P2-12.2 (MUST) Refusal rather than substitution.** Where a delegated capability is unavailable, an implementation must take the behaviour of section 4.6 and must not substitute a local implementation of it.

**P2-12.3 (MUST NOT) No reaching past a neighbour.** An implementation must not read or write the internal state of another component named in this section, and must interact with it only through that component's declared interface.

### 12.1 Boundary with Part 1, controlled documents and records

This is the boundary on which the whole part depends, and this subsection is the reciprocal declaration that `Part 1` clause P1-12.4 and section 12.2 of that part require.

**Delegated.** The identity, version, approval, signature, effectivity, supersession, withdrawal, retention and citability of the artifact that carries every rule and every rule set membership declaration, and of every registry this part requires. The resolution of what was in force at an application time. The resolution of a clause level locator, which is what a rule's authority reference is.

**Must not absorb.** Rule lifecycle. This component does not hold a status, an approval, a signature or an effective date for a rule, and does not decide whether a rule is in force. It obtains all of it by resolution.

**Naive conflation.** Two forms. This component grows a status field on the rule so that rules can be activated and deactivated without a document change, at which point the rule set in force is not any document the organisation holds and no rule change has an approval or a date. Or `Part 1` grows an evaluator, so that a retention predicate is executed by the document component, which is the conflation `Part 1` section 12.2 names.

**Reciprocal.** This part declares that it does not hold the versions, approvals or effectivity of the rules it evaluates, and that it obtains the rule text in force at an application time by resolution against `Part 1`. That is the declaration `Part 1` requires, and clauses P2-1.8, P2-3.16 and P2-5.3 make it binding.

**P2-12.4 (MUST) Rule lifecycle obtained from Part 1.** An implementation must obtain the version identity, approval, effectivity and retention of every rule and rule set membership declaration by resolution against `Part 1`, and must record the resolution outcome envelope rather than the resolved version identifier alone.

**P2-12.5 (MUST NOT) No local lifecycle.** An implementation must not hold, cache beyond a declared validity period, or assert the status or force state of a rule, and must not provide a means of activating or deactivating a rule other than by a change to the document that carries it or by the admission mechanism of section 5.2.

### 12.3 Boundary with Part 3, provenance and audit ledger

**Delegated.** The chain of reasoning of a determination that consumed a verdict, including everything the determination cited other than rules, and the reconstructability of the determination as a whole.

**Must not absorb.** The general ledger. This component's records concern rules, evaluations and verdicts only.

**Naive conflation.** `Part 3` records the outcome of an evaluation as a summary, typically a violation count or a pass indicator, because the report is large. The provenance of the determination is then unreconstructable in exactly the way `Part 3` exists to prevent, and the loss is silent because the summary looks like a record.

**Reciprocal.** `Part 3` must declare that it records the whole evaluation report and its pin set rather than a summary, that it does not re evaluate a rule in order to explain a determination, and that it obtains an explanation from operation 26 of section 4.3.

**P2-12.6 (MUST) The report is the citable artifact.** An implementation must return, and `Part 3` must record, the whole evaluation report of section 3.17 including the pin set, rather than a summary, a count or an aggregate.

**P2-12.7 (MUST NOT) No provenance of other subjects.** An implementation must not record provenance for subjects other than the rules, evaluations and registries it owns.

### 12.4 Boundary with Part 4, metadata and model repository

**Delegated.** The definition of every term a rule uses, its versioning, its lineage and the impact analysis of changing it.

**Must not absorb.** Definitions. A rule references a definition; it does not contain one.

**Naive conflation.** The rule defines its own terms inline, so that two rules using the same word mean different things and no reviewer can tell. The converse conflation is `Part 4` acquiring rule semantics, so that a definition carries a constraint and there are two places a constraint can live.

**Reciprocal.** `Part 4` must declare that it owns term identity and versioning, that it exposes a definition version obtainable by pin, and that it notifies or is queryable about supersession so that clause P2-3.80 can be satisfied.

**P2-12.8 (MUST) Terms referenced and pinned.** An implementation must record a term reference for every non primitive token in a declaration, must pin the definition version of every governed term, and must include the pins in the run.

**P2-12.9 (MUST NOT) No local definition.** An implementation must not hold a definition of a governed term and must not permit a rule to define one, per clause P2-3.81.

### 12.5 Boundary with Part 5, decision engine

This is the boundary the authoring brief flags as needing special care, and it needs it because the two components look alike from outside: both take inputs, apply declared logic and return something. The difference is what they return, and it is categorical rather than a matter of degree.

**This component returns truth.** For each rule, whether it held, did not hold, did not apply, or could not be evaluated. It never chooses among candidates. Where two rules conflict, it reports both, per clause P2-6.49. Where two derivation rules disagree, it returns a non result and both assertions, per clause P2-3.116.

**`Part 5` returns a choice.** One outcome selected from several that were possible. A selection requires a criterion, the criterion is policy, and the policy must be reviewable as itself rather than as a side effect of an evaluation order.

**Delegated.** Every selection. Which of several eligible options applies. Which of two conflicting authorities prevails. Which retention period governs where two schedules give different answers. Which approver is required. Any ranking, scoring or ordering of outcomes. Any decision table with a hit policy, since a hit policy is a conflict resolution criterion and DMN's decision tables are that construct.

**Must not absorb.** Selection, and specifically the four forms it arrives in. Priority values on rules, addressed in section 11.3. A first match or single hit semantics over a rule set, which is a hit policy under another name. A fallback or default rule, which selects an outcome where no rule matched. And an aggregation of verdicts into a conclusion, prohibited by clause P2-3.108 and clause P2-9.36.

**Naive conflation, first form.** This component acquires the ability to pick. It starts with something small: a default when no rule applies, or an ordering so that the most specific rule wins. Every property in sections 6 and 7 then degrades at once. Order independence is gone. Reproducibility survives only if the ordering is pinned, which nobody does because the ordering does not look like data. And the verdict set becomes useless, because the component now returns the chosen answer rather than what each rule concluded, so a caller can no longer tell that four rules were indeterminate.

**Naive conflation, second form.** `Part 5` acquires constraint evaluation, on the reasonable ground that a decision needs to know which options are permitted. It then evaluates conditions inline without a rule identity, an authority, a statement, a pin set or a verdict taxonomy. The decision is recorded, the conditions behind it are not, and the determination cannot be accounted for. This is the more common of the two and the harder to detect, because the decision engine's own records look complete.

**The seam, stated precisely.** A determinate function of the inputs is not a decision, even where it involves conditions: computing whether an interval exceeds a threshold is evaluation. A function that requires a criterion not derivable from the inputs is a decision, even where it looks like a lookup: selecting which of two applicable retention schedules governs requires a rule of precedence, and that rule is policy. The test is whether the component would have to choose. If it would, it is `Part 5`'s.

**Reciprocal.** `Part 5` must declare that it does not evaluate constraints, that it obtains verdicts from this component and records the whole report per clause P2-12.6, that it does not treat an `INDETERMINATE` verdict as an input from which a decision may be made without recording that it did so, and that its conflict resolution criteria are themselves declared and versioned artifacts rather than properties of the rules it consumes.

**P2-12.10 (MUST NOT) No selection.** An implementation must not select, rank, score, order or prefer among rules, verdicts, findings or candidate outcomes, and must return every verdict.

**P2-12.11 (MUST NOT) No hit policy.** An implementation must not implement a first match, single match, priority or output order semantics over a rule set, and must evaluate every member, per clause P2-6.23.

**P2-12.12 (MUST NOT) No default or fallback rule.** An implementation must not admit a rule whose function is to supply an outcome where no other rule produced one, and must report the absence of an applicable rule as the non applicability verdicts of section 7.4.

**P2-12.13 (MUST) Conflict reported, never arbitrated.** An implementation must report a detected contradiction between rules, or a conflict between derivation rules, together with every conflicting artifact and its authority, and must not select between them.

**P2-12.14 (MUST) Decision outputs pinned as inputs.** An implementation must treat any value produced by `Part 5` that a rule reads as a pinned input recorded as such, and must not invoke a decision in the course of an evaluation.

### 12.6 Boundary with Part 6, workflow and process orchestration

**Delegated.** Control flow: when an evaluation is triggered, in what order evaluations of different subjects occur, what happens after a violation, how a remediation is chased, and the state of that remediation.

**Must not absorb.** Process state. A verdict is a conclusion, not a step.

**Naive conflation.** The evaluation becomes a workflow step whose output drives a gateway, and the verdict is not recorded except as the branch that was taken. The organisation then has process instances rather than verdicts, and process instances are designed to be transient.

**Reciprocal.** `Part 6` must declare that it does not own verdicts, that it records the evaluation report reference rather than the branch taken, and that its own retention does not govern the retention of the verdicts it consumed.

**P2-12.15 (MUST) Verdicts independent of process.** An implementation must record and return every verdict without reference to any process instance, and must remain correct where the orchestrator is replaced.

**P2-12.16 (MUST NOT) No process identity required.** An implementation must not require a process instance identifier in order to evaluate, record or read anything specified in this part.

### 12.7 Boundary with Part 7, policy decision point and authorisation

**Delegated.** Every authorisation decision: whether a principal may request an evaluation for a purpose, may read a verdict, may read a rule's declaration, may admit a rule, may revoke admission, or may export an evidence package. The withholding of subject paths, which arrives here as the withheld condition of section 3.12.

**Must not absorb.** Policy. A verdict is not a permission. The temptation is acute because a constraint and an authorisation policy are both conditions evaluated against a subject, and because the same expression language would serve for both.

**Naive conflation.** This component becomes the authorisation point, per section 11.26. Or `Part 7` embeds constraints in policy, so that the conditions governing conduct are split between two components with two vocabularies and two review cycles, and no one can enumerate them.

**Reciprocal.** `Part 7` must declare that it owns policy evaluation, that it does not evaluate business rules under this part, that it obtains verdicts as attributes where a decision depends on one, and that it identifies withheld paths to this component as withheld rather than removing them.

**P2-12.17 (MUST) Attributes supplied, decisions consumed.** An implementation must supply verdicts as attributes for an authorisation decision where asked, must record the `AUTHREF` of a decision with the operation it permitted, and must not evaluate policy.

**P2-12.18 (MUST) Withheld paths identified as withheld.** An implementation must require that a path removed from a subject state by an authorisation decision be identified as withheld, must record it as such, and must yield `INDETERMINATE` rather than treating it as absent, per clause P2-3.72.

### 12.8 Boundary with Part 8, human task and case management

**Delegated.** The work a person does about a finding: the queue, the assignment, the investigation, the case, the justification of an override, and the closure.

**Must not absorb.** Finding management. A finding here is a record of what violated a rule. Its disposition is somebody's work and belongs elsewhere.

**Naive conflation.** The finding and the task are one entity, so closing the task closes the finding, and a finding disposed of with the task is a violation that has been erased rather than addressed.

**Reciprocal.** `Part 8` must declare that closing a task does not alter a verdict or a finding, and that an override or acceptance of a violation is recorded as its own act referencing the immutable finding.

**P2-12.19 (MUST) Findings immutable and independent.** An implementation must retain every finding unchanged after any task, case or override concerning it, and must not provide a means of closing, clearing or resolving a finding.

### 12.9 Boundary with Part 9, schema and contract registry

**Delegated.** Schema identity, schema versioning, compatibility between schema versions, and validation of an instance against its schema.

**Must not absorb.** Structural validation. The line is not one of technique, since both are constraint checking, and it must therefore be drawn by authority rather than by mechanism.

**Position taken.** A schema states what a well formed instance is: which fields exist, of what type, in what cardinality. A rule states what a permissible instance is: which combinations of values the organisation allows. The test is whether a violation is a defect in the message or a fact about the world. A missing required field is the first. A discount exceeding the authorised maximum is the second. The boundary is contestable, and section 13.3 records that a substantial class of constraints sits on it, since almost anything expressible as a rule can be expressed as a schema constraint in a sufficiently expressive schema language.

**Naive conflation.** Business rules migrate into schemas because the schema is enforced earlier and cheaply. They lose their statement, their authority, their enforcement level, their verdict taxonomy and their evaluation record, and a violation becomes a parse failure.

**Reciprocal.** `Part 9` must declare that it does not express business rules as schema constraints, that a schema violation is reported as a structural defect and not as a rule verdict, and that it exposes schema versions obtainable by pin.

**P2-12.20 (MUST NOT) No schema validation here.** An implementation must not validate a subject state against a schema and must not report a structural defect as a verdict.

**P2-12.21 (MUST) Structural defect is indeterminacy.** An implementation must return `INDETERMINATE` with a `SUBJECT_INDETERMINACY` subclass where a subject state is structurally unusable, and must not return a conformance verdict.

### 12.10 Boundary with Part 10, reference and master data management

**Delegated.** Code lists, reference sets, jurisdiction lists, classification schemes and their governance, versioning and retention.

**Must not absorb.** Vocabulary governance. This component reads reference sets under a pin and must not define, extend or correct one.

**Naive conflation.** The rule enumerates the members of a code list in its own declaration, because reading the list is inconvenient. The list then has two masters, and a member added in one place is missing in the other, with no signal.

**Reciprocal.** `Part 10` must declare that it retains every superseded reference set version for at least as long as the longest retained verdict of any rule that read it, that it does not remove or reuse member keys, and that it exposes a version resolvable as of an application time.

**P2-12.22 (MUST) Reference sets read, not held.** An implementation must read every reference set from `Part 10` under a pin resolved as of the evaluation instant, and must not hold, extend or correct one, per clause P2-3.125.

**P2-12.23 (MUST NOT) No enumerated membership in a declaration.** An implementation must not admit a declaration that enumerates the members of a governed reference set in place of testing membership in it.

### 12.11 Boundary with Part 11, content addressed artifact store

**Delegated.** The durable storage of the octets of anything this part digests: subject states held as example artifacts, evaluation reports, evidence packages, and the content of rule declarations where held separately.

**Must not absorb.** Storage semantics. This component owns the mapping from an artifact to a digest and a canonical form profile.

**Naive conflation.** The store holds verdicts because it holds reports, and a verdict acquires two homes.

**Reciprocal.** `Part 11` must declare that it holds no verdicts, no rule state and no admission state, and that it does not delete content on its own authority.

**P2-12.24 (MUST) Digest is the interface.** An implementation must address stored content by digest under a declared canonical form profile and must not rely on a location or path as identity.

### 12.12 Boundary with Part 12, conformance and assurance harness

**Delegated.** All assessment of whether an implementation satisfies this part. The verification of the properties this part requires an implementation to demonstrate: projection agreement, order independence, reproduction, and example agreement.

**Must not absorb.** Self assessment. This component performs the checks of clauses P2-6.42, P2-8.11 and P2-3.47 and records their results; it does not assess itself against this part.

**Naive conflation.** The component's own reproduction and analysis results are presented as conformance evidence, which is the condition in which nobody discovers that the reproduction sample was chosen to exclude the difficult runs.

**Reciprocal.** `Part 12` must declare that it obtains the clause set from this part by resolution, that it records the version of this part an assessment was made against, and that it does not modify any row of this component while assessing it.

**P2-12.25 (MUST) Read only assessment.** An implementation must expose everything `Part 12` requires through read operations and must not require a write in order to be assessed.

**P2-12.26 (MUST NOT) No self assessment as assessment.** An implementation must not present its own reproduction, analysis or example execution results as an assessment of conformance, per clause P2-1.12.

### 12.13 Boundary with Part 13, model invocation and agent execution

**Delegated.** The invocation of any model, its cost, its retries, its non determinism, and the record of what it was asked and what it returned.

**Must not absorb.** Invocation. A model output is an input to a rule, obtained beforehand and pinned, never computed during an evaluation.

**Naive conflation.** A rule calls a model in the course of its evaluation, because the rule needs a judgement the expression language cannot express: whether a description is adequate, whether two records refer to the same thing. Every guarantee in section 6.1 fails at once. The verdict is not reproducible, since the model is not a pinned artifact and may not be deterministic even pinned. The verdict is not explainable, since the finding points at a model's output rather than at a subject value. And the rule's statement cannot express what the rule does, since the criterion is inside the model.

**Position taken.** A model output may be an input to a rule if and only if it is obtained before the evaluation, recorded as an artifact with its own identity and digest, pinned in the run, and marked in the subject state as a model output rather than a subject value. Under those conditions the rule is reproducible in the only sense available: it will yield the same verdict from the same recorded output. It is not reproducible in the stronger sense that re invoking the model would yield the same output, and clause P2-12.28 requires that distinction to be recorded rather than glossed.

An automated agent may author a rule, and the authorship must be recorded as the agent's, per the same reasoning `Part 1` section 12.13 gives. An agent may not assert the correspondence claim of clause P2-3.11, because that assertion is the one a person is accountable for, and an actor that cannot bear accountability cannot make it. Section 13.7 records this as a position rather than a settled question.

**Reciprocal.** `Part 13` must declare that it owns the invocation record, that it does not evaluate rules, and that it returns an output as an artifact with an identity and a digest that this component can pin.

**P2-12.27 (MUST NOT) No invocation during evaluation.** An implementation must not invoke a model, an agent or any non deterministic service during an evaluation, per clause P2-3.28.

**P2-12.28 (MUST) Model outputs pinned and marked.** An implementation must record a model output used by a rule as a pinned artifact with its own identity and digest, must mark it in the subject state as a model output, and must record that reproduction of the verdict does not establish reproduction of the output.

### 12.14 Boundary with Part 0, system composition

**Delegated.** What happens when all the components run at once: authority over facts more than one component touches, the seams at which values cross boundaries, the propagation of non results, consistency and ordering across components, and version pinning across a unit of work spanning several components.

**Must not absorb.** Composition. This part states its own contract, including the caller obligations of section 4.5 and section 7.7, and does not state what a caller with no representation for indeterminacy must do.

**Reciprocal.** `Part 0` must declare that this component holds authority over rule admission state, verdicts, findings, evaluation reports and the pin sets of evaluations, and that `Part 1` holds authority over rule identity, version, approval and effectivity. It must state, for every seam at which one of those facts crosses into another component, what must hold and how a violation appears in the record. It must in particular state what a receiving component does with each indeterminacy subclass of section 7.2, since this part specifies only what this component returns, and it must state how a single unit of work spanning this component and `Part 5` pins one rule set version across both.

**P2-12.29 (MUST) Authority declared, not assumed.** An implementation must not accept an assertion about a verdict, a finding, an admission state or a pin set from another component, and must require that such facts be established by its own operations.

**P2-12.30 (MUST) Non result propagation is a composition concern.** An implementation must return the outcomes of section 7 unmodified regardless of whether the caller can represent them, and must not degrade an `INDETERMINATE` verdict to a conformance verdict in order to fit a caller's model.
## 13. What could not be established

This section is a deliverable rather than a disclaimer. A question recorded as open can be closed by someone with access to the source; a question closed by inference cannot be reopened, because nothing in the document reveals that an inference was made.

### 13.1 Sources not obtained in full text

The following were not available to the author in full text. This part's account of each rests on published scope statements, status pages, catalogue entries, forewords and secondary literature. No clause reproduces text from any of them, and no clause should be read as asserting that its requirement appears in them.

SBVR 1.5. The scope, the behavioural against definitional distinction, the definition of enforcement level and the treatment of the rule statement as the guidance message were obtained from secondary sources, including an extract of pages 118 to 119 reproduced in published commentary. The specification text was not obtained. Sections 2.1, 3.10 and 10.2 depend on this and should be checked before approval. In particular, the claim that SBVR does not standardise the enforcement level values is central to section 9.5 and rests on commentary.

DMN 1.5. The version state, the adoption dates and the scope statement were obtained from the publisher. The decision table semantics, the hit policies and the completeness and consistency checking referred to in sections 10.2 and 12.5 were not obtained from the specification.

PRR 1.0. Scope and conformance points obtained. The metamodel was not.

ISO/IEC 19757-3:2025. The edition, publication date, page count, revision stage and the definition of a validator as returning valid, invalid or error were obtained, the last from a secondary source quoting page 12. The clause text was not obtained. Section 6.2 leans on that definition and it should be verified against the standard, since it is the only normative anchor found for the three valued return type.

ISO/IEC 9075, on SQL. The edition in force was not established. Section 10.5 and section 11.2 rest on well attested behaviour rather than on the standard, and the account should not be cited as a statement about any particular edition.

OMG OCL. Not obtained and not assessed, although PRR 1.0 includes a non normative OCL set and OCL is the obvious candidate for the invariant expression of a constraint over a model. Its absence from section 10 is a gap rather than a judgement.

ISO/IEC 24707, Common Logic. Not obtained and not assessed. It is the most likely place to find a normative treatment of the logical foundations section 10.5 cites as literature.

The SHACL 1.2 family. Status pages, announcements and the technical report documents were obtained. The maturity level of each document as at the date of this part could not be established with confidence: the Core and SPARQL editor's drafts were published for review in November 2025 targeting Candidate Recommendation in January 2026, and whether that transition occurred was not determined. Section 10.4 states what was established and no more.

By contrast, SHACL 1.0 and the RIF-PRD Second Edition were obtained in full, and clauses resting on them are marked as resting on specification text.

**P2-13.1 (MUST) Verification before approval.** An implementation or reviewer must verify the claims listed in section 13.1 against the source standards before this part is approved, and must record the outcome of each verification against this section.

### 13.2 Whether declaration and statement can ever be shown to correspond

This part requires a declaration and a statement, requires them bound and separately approved, and requires examples as a partial bridge. It does not and cannot require that they be shown to agree, because establishing that an arbitrary expression means what an arbitrary sentence says is not decidable, and no reviewed source claims otherwise.

What this leaves is uncomfortable. The central artifact pair of the part is bound by a digest, approved together, exercised against examples, and still capable of meaning two different things without anything detecting it. The worked demonstration of section 3.21 shows exactly this case occurring in 2029 and the component failing to notice.

**Open.** Whether a stronger bridge exists. Three candidates were considered and none was pursued. A controlled natural language, in the manner of SBVR Structured English, from which the declaration is generated, which would make correspondence structural but would constrain what a statement can say to what the language can parse. A bidirectional generation with a round trip check. And a required review protocol in which two people independently produce the declaration from the statement and the products are compared, which is a governance mechanism rather than a specification one and is expensive. A reviewer who believes one of these should be required should say so, because section 3.2 is the whole basis of the part and this is its weakest point.

### 13.3 The boundary between a rule and a schema constraint

Section 12.9 draws a line between what a schema states and what a rule states, and offers a test: whether a violation is a defect in the message or a fact about the world. The test works at the extremes and not in the middle.

A large class of constraints sits in the middle. A conditional requirement, where field B is mandatory if field A has a particular value, is expressible in most current schema languages and is also plainly a business rule. A cross field consistency check is the same. A value range that derives from a regulation is a business rule expressed as a schema facet. The more expressive the schema language, the larger the middle becomes, and the current generation of schema languages is expressive enough to express nearly everything this part calls a rule.

**Open.** Whether a principled criterion exists, or whether the allocation is a governance decision to be made per organisation and recorded. This part behaves as though the second is true, since section 12.9 requires the boundary to be declared rather than derived, and that is an evasion of a question that ought to have an answer.

### 13.4 Three truth values or four

Section 6.2 requires three and rejects Belnap's four valued treatment, in which a proposition can be supported as both true and false. The rejection is defensible for cost and consumer complexity, and it is not obviously right.

The case for four is that contradictory input is a real and distinct condition. Two sources give different values for the same field; the rule can be evaluated against each and yields opposite results. This part returns an indeterminacy coded `CONTRADICTORY_INPUT`, which says the rule could not be evaluated. That is arguably false: the rule was evaluated twice and gave two answers, which is a different fact from being unable to evaluate it, and a system that reports the two as the same has lost information that a data steward needs.

**Open.** Whether the fourth value should be adopted, and if so whether it belongs in the truth domain or in the verdict set. The cost of adopting it is every table in section 6.2 and a branch in every consumer, and the cost of not adopting it is that a specific and important condition is reported as a generic one.

### 13.5 Enforcement level and version identity

SBVR 1.5 states that the enforcement level of a behavioural rule can change independently of the rule. Clause P2-3.62 requires that a change of level produce a new rule version, which contradicts that.

The reason for the divergence is recorded in section 3.10: a verdict issued three years ago must be interpretable against the level that applied three years ago, and a level that floats free of version identity is a level that cannot be resolved as of a past time. The cost is real. It means that a decision to relax enforcement of a rule from strict to guideline, which is a policy decision and not a change to what the rule says, produces a new version of the rule and requires the whole approval cycle. Organisations will resist this, and the resistance will take the form of holding the level outside the model, which is worse than either position.

**Open.** Whether the level should instead be a separately versioned assertion about a rule lineage, resolvable as of a time in the manner of a `Part 1` effectivity assertion, which would satisfy both requirements at the cost of a further entity and a further resolution. This is the most likely candidate for revision in a second version of this part.

### 13.6 Clauses resting on practice

The clauses whose basis is practice rather than specification text are enumerated in section 10.7 and are not repeated here. What could not be established is whether any of the eight has a normative source that was not found. The most likely candidates are clause P2-6.3 on collation pinning and clause P2-6.26 on calendar convention, both of which are the kind of requirement a conformance clause in an expression language specification might carry.

**P2-13.2 (MUST) Practice basis recorded.** An implementation that adopts a clause listed in section 10.7 as a control must record that its basis is practice, per clause P2-10.3.

### 13.7 Whether an automated agent may assert correspondence

Section 12.13 permits an agent to author a rule and forbids it from asserting the correspondence claim of clause P2-3.11, on the ground that the claim is what a person is accountable for. This is the same position `Part 1` takes on signature and it is open for the same reason: the argument rests on accountability rather than on any cited requirement, and it is not obvious that an agent operating under a recorded delegation, with an invocation record and an accountable owner, is worse at the task than a person who approves without reading.

The task is also unusually well suited to an agent. Comparing a sentence with an expression and reporting whether they agree is close to what current models do well, and a system that required an agent to make the comparison and a person to accept or reject the agent's finding might produce better correspondence than either alone.

**Open.** Whether the prohibition should instead be a requirement that an agent's correspondence finding be recorded as such and countersigned, which is a different design and probably a better one.

### 13.8 Vacuity: flag or verdict

Clause P2-7.3 puts vacuity in a flag inside `SATISFIED` rather than making it a verdict member, on the ground that a new member obliges every consumer to grow a branch. The consequence is that a consumer which ignores the flag reports a vacuous satisfaction as a satisfaction, which is the exact failure section 11.10 describes, and the flag does not prevent it.

**Open.** Whether vacuous satisfaction should be a member of the closed verdict set, so that a consumer cannot ignore it without failing an exhaustiveness check. The argument against is consumer burden. The argument for is that consumer burden is the mechanism by which the distinction survives.

### 13.9 Where non applicability by time belongs

`NOT_IN_FORCE_AT_INSTANT` is a verdict member here and the fact it reports is a `Part 1` fact. It may belong there, returned as a resolution outcome, with this part never seeing the rule at all.

**Open.** Which allocation is right. The argument for the present one is that a caller asking for an evaluation of a rule set wants a verdict for every member, and a member silently omitted because it was not yet in force is an omission the caller cannot detect. The argument against is that this part now holds a member whose truth it does not determine.

### 13.10 Whether stratification is workable

Section 6.6 requires declared strata and forbids fixpoint iteration. This is sound and it may be too restrictive for real derivation sets, which commonly contain a genuine mutual dependency that a human author resolves by iterating until stable.

**Open.** Whether a bounded fixpoint, that is a declared maximum number of passes with a non result on non convergence, would be a better rule than strict stratification. It would admit more rule sets and would keep termination checkable, at the cost that the number of passes becomes a parameter nobody can justify from a rule.

### 13.11 Rule granularity

Sections 11.17 and 11.18 name the two failures of granularity, the mega rule and the rule per sentence, and neither offers a criterion for the right answer. Clause P2-11.17 gestures at one, that each condition with a distinct authority should be a distinct rule, which is defensible and incomplete: it says nothing about several conditions sharing one authority, which is the common case.

**Open.** Whether a criterion exists. The candidate worth investigating is that a rule should be the smallest unit that can independently produce a finding a person could act on, which is a statement about the reader rather than about the authority and is therefore not mechanically checkable.

### 13.12 Long run reproducibility of an evaluator

Clause P2-6.2 requires pinning the version of the expression language implementation. Over a retention horizon of decades this is a pin to an artifact that will not run: the runtime, the platform and possibly the language will be gone.

The same problem is recorded in `Part 1` section 13.8 for signature validation, and it has the same shape. Beyond some horizon, reproducibility becomes the recorded assertion that a verdict was reproduced at a time when reproduction was possible, rather than the ability to reproduce it now. Clause P2-8.11 requires periodic reproduction, which is the only available mitigation and is a way of moving the assertion forward rather than of solving the problem.

**Open.** Whether an expression language can be specified so completely that a verdict is recomputable from the specification alone, without the implementation, and whether the cost of that specification is bearable.

### 13.13 What this part deliberately did not attempt

No conformance assessment of any system against this part was performed or anticipated, per section 1 and clause P2-1.12.

No expression language is specified, and none is registered. Section 9.3 states the conditions a language must satisfy and stops there. This is the largest single omission and it is deliberate: registering a language would bind this part to the currency of a specification it does not control, and the currency findings of section 10.4 show why that is a poor bet.

No performance, scale or concurrency requirement is stated. The pin recording of section 3.14 and the witness recording of section 3.16 have evident cost implications and nothing here addresses them, because a threshold stated without a workload is not a requirement.

No authoring, testing or migration tooling is specified, and no method is given for extracting rules from an existing codebase, which is the first thing any organisation adopting this part will need.

No treatment is given of rules over streams, over aggregates across many subjects, or over relationships between subjects. Every rule in this part is a proposition about one subject, and a rule saying that no more than three approvals may be granted per month is not expressible in the model as specified. This is a substantial gap and it is recorded here rather than concealed.

**P2-13.3 (MUST) Gaps declared, not filled.** An implementation must not represent a matter listed in section 13.13 as specified by this part.

**P2-13.4 (SHOULD) Open questions carried forward.** A reviewer of this part should record a position on each open question in section 13, and where a position is adopted it should be recorded in the review outcome rather than by silent amendment of the clause it affects.

### 13.14 Questions handed to Part 0 rather than answered here

Each was identified while authoring this part and is recorded so that `Part 0` inherits it rather than rediscovering it.

What a component receiving an `INDETERMINATE` verdict must record, and what it must not conclude, per subclass.

How one rule set version is pinned across a unit of work that touches this component and `Part 5`, so that a decision and the verdicts it consumed rest on the same rules.

What happens when `Part 3`'s record of a determination and this component's record of the verdict it consumed disagree.

Whether a retention obligation recorded in `Part 1` can bind the disposal of a verdict here and of the report copy held in `Part 11`, given clause P2-8.31 requires rule artifacts to outlive their verdicts.

How the drift signal of section 3.7 reaches the owner of a determination made years earlier on the strength of a verdict from a rule whose authority has since been withdrawn.

Which component holds authority over the identity of an actor, since this part treats it as opaque and needs it for authorship, correspondence claims and access records.

Whether an evaluation spanning subjects owned by several components can pin a consistent state across them, which the model of section 3.12 assumes and does not provide.
