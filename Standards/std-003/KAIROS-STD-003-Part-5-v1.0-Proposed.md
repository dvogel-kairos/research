# KAIROS STD 003 Part 5: Decision Engine

**Standard.** KAIROS STD 003, the enterprise architecture standard.
**Part.** Part 5 of 14 (Part 0 and Parts 1 through 13). Cited as `KAIROS STD 003 Part 5`.
**Title.** Decision engine.
**Version.** 1.0.0.
**Status.** Proposed. This part has not been approved and is not effective. It is issued for review against the authoring brief of 2026-08-17.
**Date of issue.** 2026-08-18.
**Supersedes.** Nothing. This is the first version.

## Binding of requirement language

The key words MUST, MUST NOT, SHOULD, SHOULD NOT and MAY in this part are to be interpreted as described in RFC 2119 and RFC 8174, and only in the upper case forms. This part does not use SHALL, SHALL NOT, REQUIRED, RECOMMENDED, NOT RECOMMENDED or OPTIONAL as requirement keywords.

Every requirement in this part is a numbered clause. A clause identifier has the form `P5-S.N`, where `S` is the section number and `N` is the ordinal of the clause within that section. Clause identifiers are permanent. A clause that is later removed has its identifier retired and never reissued. A clause that is later added to a section takes the next unused ordinal in that section, so ordinals are stable but not contiguous over the life of the part.

Text that is not a numbered clause is not binding. Narrative, tables, algorithms, examples and the discussion of standards are provided to make the clauses intelligible and testable, and where a table carries normative content a clause says so explicitly and names the table.

## Conformance

An implementation conforms to this part if it satisfies every MUST and MUST NOT clause and records, for each SHOULD and SHOULD NOT clause it does not satisfy, the reason. This part does not define conformance levels, profiles or a certification scheme, and it does not define the method of assessment. Assessment method is the subject of `KAIROS STD 003 Part 12` and is out of scope here.

Where a clause states that a value is an implementation decision, conformance requires that the implementation declare the value, not that it adopt a particular one. An undeclared implementation decision is a nonconformity.

## Clause index

The index below is generated from the clause text of this document. It lists every clause identifier, its modality and its subject label. The counts that follow the index are derived by the same extraction and are stated with the grain at which they were counted.

| Clause | Modality | Subject |
| --- | --- | --- |
| **Section 1** | | **Scope and responsibilities** |
| `P5-1.1` | MUST | Purpose satisfaction |
| `P5-1.2` | MUST | Criterion as a governed artifact |
| `P5-1.3` | MUST NOT | No undeclared resolution |
| `P5-1.4` | MUST NOT | No constraint evaluation |
| `P5-1.5` | MUST | Indeterminate eligibility surfaced |
| `P5-1.6` | MUST | Reproducibility |
| `P5-1.7` | MUST | Every candidate recorded |
| `P5-1.8` | MUST | Margin recorded |
| `P5-1.9` | MUST NOT | No candidate invention |
| `P5-1.10` | MUST NOT | No action |
| `P5-1.11` | MUST NOT | No update in place |
| `P5-1.12` | MUST NOT | No absorption of neighbouring responsibilities |
| `P5-1.13` | SHOULD | Declared exclusions |
| `P5-1.14` | MUST NOT | No conformance self assertion |
| `P5-1.15` | MUST | Time horizon declaration |
| **Section 2** | | **Terminology** |
| `P5-2.1` | MUST | Single meaning per term |
| `P5-2.2` | MUST NOT | No redefinition |
| `P5-2.3` | MUST NOT | No collapsing of eligibility and preference |
| `P5-2.4` | MUST NOT | No collapsing of the bases of selection |
| `P5-2.5` | MUST NOT | No collapsing of precedence over outcomes and order over rules |
| `P5-2.6` | MUST NOT | No collapsing of the three failures to determine |
| `P5-2.7` | MUST NOT | No collapsing of human involvement and decisive automation |
| `P5-2.8` | MUST NOT | No collapsing of the three clocks |
| `P5-2.9` | SHOULD | Term registry |
| **Section 3** | | **Data model** |
| `P5-3.1` | MUST | Declared types |
| `P5-3.2` | MUST NOT | No semantic identifiers |
| `P5-3.3` | MUST | Language tag present |
| `P5-3.4` | MUST NOT | No caller supplied knowledge time |
| `P5-3.5` | MUST | Scale declared with every score |
| `P5-3.6` | MUST | Three valued domain used unchanged |
| `P5-3.7` | MUST | Four parts separately recorded |
| `P5-3.8` | MUST NOT | No eligibility by score threshold |
| `P5-3.9` | MUST | Eligibility obtained before preference |
| `P5-3.10` | MUST | Completeness of the candidate set declared |
| `P5-3.11` | MUST NOT | No merged exclusion ground |
| `P5-3.12` | MUST | Entity coverage |
| `P5-3.13` | MUST NOT | No update in place |
| `P5-3.14` | MUST NOT | No decision amendment |
| `P5-3.15` | MUST | Definition carried by a document |
| `P5-3.16` | MUST | Absent tiebreak and default are claims |
| `P5-3.17` | MUST | Indeterminate treatment required where eligibility applies |
| `P5-3.18` | MUST | Outcome concept bound |
| `P5-3.19` | MUST | Natural person subject declared |
| `P5-3.20` | MUST NOT | No implicit definition |
| `P5-3.21` | MUST NOT | No definition amendment |
| `P5-3.22` | MUST | Source kind declared |
| `P5-3.23` | MUST | Source pinned where the kind requires it |
| `P5-3.24` | MUST | Completeness recorded with its basis |
| `P5-3.25` | MUST | External solicitation never complete |
| `P5-3.26` | MUST NOT | No effect from source ordinal |
| `P5-3.27` | MUST | Outcome value digested |
| `P5-3.28` | MUST NOT | No candidate deduplication without a declared rule |
| `P5-3.29` | MUST | Eligibility obtained as a whole report |
| `P5-3.30` | MUST | Declining to decide is the default |
| `P5-3.31` | MUST | Treatment authorised and justified |
| `P5-3.32` | MUST | Treatment recorded on the decision |
| `P5-3.33` | MUST | Subclass treatments distinguishable |
| `P5-3.34` | MUST NOT | No treatment of a component defect as data |
| `P5-3.35` | MUST | Natural person applicability enforced |
| `P5-3.36` | MUST NOT | No silent exclusion |
| `P5-3.37` | MUST | Vacuous satisfaction carried through |
| `P5-3.38` | MUST | Exactly one kind |
| `P5-3.39` | MUST | Statement present and authoritative language designated |
| `P5-3.40` | MUST | Kind required fields enforced |
| `P5-3.41` | MUST | Scale and direction recorded together |
| `P5-3.42` | MUST | Attributes considered enumerated |
| `P5-3.43` | MUST | Sub criterion order declared for lexicographic criteria |
| `P5-3.44` | MUST | Random generator pinned and seed recorded |
| `P5-3.45` | MUST NOT | No hidden comparability |
| `P5-3.46` | MUST | Dominance only never resolves |
| `P5-3.47` | MUST | Authority per criterion version |
| `P5-3.48` | MUST | Locator to a clause |
| `P5-3.49` | MUST | Every parameter justified |
| `P5-3.50` | MUST | Justification citation where the basis requires it |
| `P5-3.51` | MUST | Interpretation note where a parameter is not in the clause |
| `P5-3.52` | MUST | Unjustified parameters countable |
| `P5-3.53` | MUST | Authority drift observed |
| `P5-3.54` | MUST NOT | No silent disable on authority drift |
| `P5-3.55` | MUST | Approval obtained, not asserted |
| `P5-3.56` | MUST | Hit policies expressed as criteria |
| `P5-3.57` | MUST | Unique and Any are constraints |
| `P5-3.58` | MUST | Constraint violation is a defect |
| `P5-3.59` | MUST NOT | No selection by rule sequence |
| `P5-3.60` | MUST | Precedence over outcomes recorded as an artifact |
| `P5-3.61` | MUST | Enumerated outcomes required for a precedence criterion |
| `P5-3.62` | MUST NOT | No else rule as a criterion |
| `P5-3.63` | MUST | Collection mode declared |
| `P5-3.64` | MUST | Aggregate recorded as derived |
| `P5-3.65` | MUST NOT | No collection as selection |
| `P5-3.66` | MUST | Aggregator registered |
| `P5-3.67` | MUST | Aggregation over a declared scale |
| `P5-3.68` | MUST | Tiebreak is a criterion version |
| `P5-3.69` | MUST | Tiebreak applicability declared |
| `P5-3.70` | MUST NOT | No tiebreak beyond its declared applicability |
| `P5-3.71` | MUST | Default authorised and justified |
| `P5-3.72` | MUST | Default applicability declared |
| `P5-3.73` | MUST | Basis of selection recorded |
| `P5-3.74` | MUST NOT | No default as a candidate |
| `P5-3.75` | MUST | Pin set complete |
| `P5-3.76` | MUST | Decision instant supplied |
| `P5-3.77` | MUST | Knowledge instant behaviour declared |
| `P5-3.78` | MUST | Purpose recorded |
| `P5-3.79` | MUST NOT | No unpinned dependency |
| `P5-3.80` | MUST NOT | No pin substitution |
| `P5-3.81` | MUST | Eligibility report pinned whole |
| `P5-3.82` | MUST | Outcome from the closed set |
| `P5-3.83` | MUST | Basis recorded and never collapsed |
| `P5-3.84` | MUST | Criterion recorded regardless of basis |
| `P5-3.85` | MUST | Counts derived with grain |
| `P5-3.86` | MUST | Approval and authority status carried |
| `P5-3.87` | MUST | Set completeness carried |
| `P5-3.88` | MUST NOT | No selection without a candidate |
| `P5-3.89` | MUST | Margin computed per kind |
| `P5-3.90` | MUST | Margin scale recorded |
| `P5-3.91` | MUST | Weight sensitivity recorded or its absence stated |
| `P5-3.92` | MUST | No margin definable is recorded as such |
| `P5-3.93` | MUST | Marginality derived from the declared threshold |
| `P5-3.94` | MUST | Marginal decisions countable |
| `P5-3.95` | MUST NOT | No marginality as a defect |
| `P5-3.96` | MUST | Ground on every unselected candidate |
| `P5-3.97` | MUST | Eliminating artifact linked |
| `P5-3.98` | MUST | Indeterminate exclusion distinguished |
| `P5-3.99` | MUST | Mapping to Part 3 recorded |
| `P5-3.100` | MUST | Out of scope candidates reported as a criterion defect |
| `P5-3.101` | MUST NOT | No unrecorded elimination |
| `P5-3.102` | MUST | Involvement recorded per person |
| `P5-3.103` | MUST | Recorded only distinguished from making |
| `P5-3.104` | MUST | Solely automated derived |
| `P5-3.105` | MUST | Decisive automation assessed separately |
| `P5-3.106` | MUST | Rate inference marked as inference |
| `P5-3.107` | MUST | Override rate computable per reviewer and class |
| `P5-3.108` | MUST | Unassessed decisions about persons countable |
| `P5-3.109` | MUST | Override recorded with its own basis |
| `P5-3.110` | MUST NOT | No override without the original |
| `P5-3.111` | MUST NOT | No inference of meaningful review |
| `P5-3.112` | MUST | Projections are pure |
| `P5-3.113` | MUST | Projection recomputable |
| `P5-3.114` | MUST | Named projections available |
| `P5-3.115` | MUST | Basis distribution available |
| `P5-3.116` | MUST | Divergence projection |
| `P5-3.117` | MUST NOT | No writes through a projection |
| `P5-3.118` | MUST | Demonstration satisfiable |
| **Section 4** | | **Interfaces** |
| `P5-4.1` | MUST | Operation classes separated |
| `P5-4.2` | MUST | Refusal is an outcome |
| `P5-4.3` | MUST | Idempotence key accepted |
| `P5-4.4` | MUST NOT | No partial recording |
| `P5-4.5` | MUST | Preconditions checked at recording |
| `P5-4.6` | MUST | Whole criterion version in one operation |
| `P5-4.7` | MUST | Approval recorded, never granted |
| `P5-4.8` | MUST NOT | No retirement of a bound criterion |
| `P5-4.9` | MUST | Scale semantics required at registration |
| `P5-4.10` | MUST | Pins recorded before returning |
| `P5-4.11` | MUST | Reproduction available |
| `P5-4.12` | MUST | Reproduction failure recorded, not hidden |
| `P5-4.13` | MUST | Simulation over historical candidate sets available |
| `P5-4.14` | MUST NOT | No citation of a non authoritative run |
| `P5-4.15` | MUST | Batch decides per subject |
| `P5-4.16` | MUST | Explanation available for every decision |
| `P5-4.17` | MUST NOT | No explanation by recomputation |
| `P5-4.18` | MUST | Override retains the original |
| `P5-4.19` | MUST | Times required on temporal resolution |
| `P5-4.20` | MUST NOT | No partial decision record |
| `P5-4.21` | MUST | Statuses returned with every criterion |
| `P5-4.22` | MUST | Caller obligations declared |
| `P5-4.23` | MUST NOT | No implied determinacy |
| `P5-4.24` | MUST NOT | No implied robustness |
| `P5-4.25` | MUST | Declared unavailability behaviour |
| `P5-4.26` | MUST NOT | No substitution on unavailability |
| `P5-4.27` | MUST | Eligibility unavailability refuses the decision |
| `P5-4.28` | MUST | Ledger recording failure does not lose the decision |
| `P5-4.29` | MUST NOT | No decision invoked during an evaluation |
| `P5-4.30` | MUST | Minimum event set |
| `P5-4.31` | MUST | Envelope minimum |
| `P5-4.32` | MUST NOT | No event in place of a record |
| `P5-4.33` | MUST | Undecidable outcomes emitted individually |
| `P5-4.34` | MUST | Indeterminate exclusion emitted per candidate |
| `P5-4.35` | MUST NOT | No suppression of adverse events |
| **Section 5** | | **State model** |
| `P5-5.1` | MUST | Four models separate |
| `P5-5.2` | MUST | Registered but unapproved reportable |
| `P5-5.3` | MUST NOT | No force state held |
| `P5-5.4` | MUST | Enumerated states only |
| `P5-5.5` | MUST | Enumerated transitions only |
| `P5-5.6` | MUST | State is a projection |
| `P5-5.7` | MUST NOT | No application outside applicable states |
| `P5-5.8` | MUST | Suspension reported, not silent |
| `P5-5.9` | MUST | Refused versions retained and countable |
| `P5-5.10` | MUST | Withdrawal authorised and reasoned |
| `P5-5.11` | MUST | Superseded versions remain applicable |
| `P5-5.12` | MUST NOT | No state change from the passage of time |
| `P5-5.13` | MUST | Enumerated run states |
| `P5-5.14` | MUST | Undecided distinguished from refused |
| `P5-5.15` | MUST | Undecided is terminal and complete as a record |
| `P5-5.16` | MUST | Pins before enumeration |
| `P5-5.17` | MUST | Eligibility before comparison |
| `P5-5.18` | MUST | Abandonment detected and recorded |
| `P5-5.19` | MUST NOT | No resumption of an abandoned run |
| `P5-5.20` | MUST | Terminal states are terminal |
| `P5-5.21` | MUST | Assessments held independently |
| `P5-5.22` | MUST NOT | No decision transition |
| `P5-5.23` | MUST | Supersession is a relation with a kind |
| `P5-5.24` | MUST | Correction implies dependents reported |
| `P5-5.25` | MUST | Superseded decisions remain readable |
| `P5-5.26` | MUST NOT | No assessment as amendment |
| **Section 6** | | **Execution semantics** |
| `P5-6.1` | MUST | Identical pins yield identical outcomes |
| `P5-6.2` | MUST | Scale comparison pinned |
| `P5-6.3` | MUST | Traversal order total and declared |
| `P5-6.4` | MUST | Exact arithmetic for comparison |
| `P5-6.5` | MUST | Order independence demonstrable |
| `P5-6.6` | MUST | Tie detection at declared precision |
| `P5-6.7` | MUST | Algorithm order |
| `P5-6.8` | MUST | Maximal set computed |
| `P5-6.9` | MUST NOT | No short circuit on eligibility |
| `P5-6.10` | MUST NOT | No short circuit on comparison |
| `P5-6.11` | MUST | Empty cases distinguished |
| `P5-6.12` | MUST | Tiebreak before default |
| `P5-6.13` | MUST NOT | No residual fallback |
| `P5-6.14` | MUST | Every comparison recorded |
| `P5-6.15` | MUST | Order totality declared |
| `P5-6.16` | MUST | Incomparability detected |
| `P5-6.17` | MUST | Intransitivity detected |
| `P5-6.18` | MUST | Cycle reported with its members |
| `P5-6.19` | MUST NOT | No resolution by traversal |
| `P5-6.20` | MUST NOT | No implicit rate of exchange |
| `P5-6.21` | MUST | Tie and incomparability distinguished in the record |
| `P5-6.22` | MUST | Four analyses performed where decidable |
| `P5-6.23` | MUST | Analysis read against the kind |
| `P5-6.24` | MUST | Masked rules reported |
| `P5-6.25` | MUST | Incompleteness reported with its consequence |
| `P5-6.26` | MUST | Undecidability declared |
| `P5-6.27` | MUST NOT | No absence of finding as absence of fault |
| `P5-6.28` | MUST NOT | No analysis at decision time |
| `P5-6.29` | MUST | Idempotence by key |
| `P5-6.30` | MUST | Deduplication window declared |
| `P5-6.31` | MUST NOT | No idempotence across differing payloads |
| `P5-6.32` | MUST | Repeated decisions recorded separately |
| `P5-6.33` | MUST | Knowledge time assigned by this component |
| `P5-6.34` | MUST NOT | No occurrence time assignment |
| `P5-6.35` | MUST NOT | No ambient clock in a criterion |
| `P5-6.36` | MUST | Instants in a declared scale |
| `P5-6.37` | MUST | Calendar convention declared |
| `P5-6.38` | MUST | Monotonic knowledge time within a stream |
| `P5-6.39` | MUST | Three bounds declared |
| `P5-6.40` | MUST | Primary budget deterministic |
| `P5-6.41` | MUST NOT | No selection from a truncated comparison set |
| `P5-6.42` | MUST | Truncation point recorded |
| `P5-6.43` | MUST NOT | No silent bound |
| `P5-6.44` | MUST | Permitted computations only |
| `P5-6.45` | MUST NOT | No inference of a criterion |
| `P5-6.46` | MUST NOT | No learning from outcomes |
| `P5-6.47` | MUST NOT | No assessment of criterion fitness |
| **Section 7** | | **Outcome and failure taxonomy** |
| `P5-7.1` | MUST | Closed outcome set |
| `P5-7.2` | MUST NOT | No additional members |
| `P5-7.3` | MUST | Three decided members distinguished |
| `P5-7.4` | MUST | Three undecidable failures distinguished |
| `P5-7.5` | MUST | Eligibility indeterminacy distinguished from criterion failure |
| `P5-7.6` | MUST | Empty cases distinguished |
| `P5-7.7` | MUST NOT | No mapping onto a decided or not decided pair |
| `P5-7.8` | MUST NOT | No caller selected collapse |
| `P5-7.9` | MUST | Envelope completeness |
| `P5-7.10` | MUST NOT | No envelope reduction |
| `P5-7.11` | MUST | Envelope is what is recorded |
| `P5-7.12` | MUST | Vacuous eligibility carried |
| `P5-7.13` | MUST | Refusal codes |
| `P5-7.14` | MUST | Refusal states what must change |
| `P5-7.15` | MUST | Refusals recorded |
| `P5-7.16` | MUST NOT | No refusal as an outcome |
| `P5-7.17` | MUST NOT | No silent retry |
| `P5-7.18` | MUST | Recording obligations honoured |
| `P5-7.19` | MUST | Emission obligations honoured |
| `P5-7.20` | MUST | Caller obligations documented |
| `P5-7.21` | MUST NOT | No determinacy language for a non criterion basis |
| `P5-7.22` | MUST NOT | No inference of policy from a default |
| `P5-7.23` | MUST | An arbitrary choice is never a determined one |
| `P5-7.24` | MUST | A failure to determine is never a determination |
| `P5-7.25` | MUST | An unassessable candidate is never an unqualified one |
| **Section 8** | | **Observability and the audit record** |
| `P5-8.1` | MUST | Determinations recorded in Part 3 |
| `P5-8.2` | MUST | Division of authority declared |
| `P5-8.3` | MUST NOT | No provenance for other subjects |
| `P5-8.4` | MUST | Own operations recorded |
| `P5-8.5` | MUST | Declared grain |
| `P5-8.6` | MUST | Comparisons recorded or derivable |
| `P5-8.7` | MUST | Authority and approval attempts recorded individually |
| `P5-8.8` | MUST | Counting grain stated with every count |
| `P5-8.9` | MUST | Reproduction sufficiency |
| `P5-8.10` | MUST | Request recorded as received |
| `P5-8.11` | MUST | Conventions recorded |
| `P5-8.12` | MUST | Precondition outcomes recorded, including passes |
| `P5-8.13` | MUST | Periodic reproduction |
| `P5-8.14` | MUST | Divergence recorded, not corrected |
| `P5-8.15` | MUST | Reads recorded |
| `P5-8.16` | MUST | Withholding recorded |
| `P5-8.17` | MUST | Simulations recorded with their requester |
| `P5-8.18` | SHOULD | Read records retained with the decision |
| `P5-8.19` | MUST | Signals produced |
| `P5-8.20` | MUST | Signals derived from entries |
| `P5-8.21` | MUST NOT | No suppression of a signal |
| `P5-8.22` | MUST | Basis distribution produced per definition |
| `P5-8.23` | MUST | Override rate reported in both directions |
| `P5-8.24` | MUST | Automation exposure standing |
| `P5-8.25` | SHOULD | Signal thresholds declared |
| `P5-8.26` | MUST | Package sufficiency |
| `P5-8.27` | MUST | Criterion content included or its absence stated |
| `P5-8.28` | MUST | Eligibility reports included |
| `P5-8.29` | MUST | Parameter justifications included |
| `P5-8.30` | MUST | Limit statements included |
| `P5-8.31` | MUST | Absence stated, not omitted |
| `P5-8.32` | MUST | Package digest |
| `P5-8.33` | MUST NOT | No package for a non authoritative run |
| `P5-8.34` | MUST | Self description |
| `P5-8.35` | MUST | Retention obtained, not assigned |
| `P5-8.36` | MUST | Decisions retained with their consequences |
| `P5-8.37` | MUST | Criteria outlive their decisions |
| `P5-8.38` | MUST | Eligibility reports retained with the decision |
| `P5-8.39` | MUST | Separate retention per structure |
| `P5-8.40` | MUST | Disposal recorded and citable |
| `P5-8.41` | MUST NOT | No disposal of a criterion under an open drift observation |
| `P5-8.42` | MUST NOT | No amendment of a decision |
| `P5-8.43` | MUST NOT | No amendment of a criterion version |
| `P5-8.44` | MUST NOT | No retrospective re basing |
| `P5-8.45` | MUST | Migration preserves identity and digests |
| `P5-8.46` | MUST NOT | No bulk assignment on import |
| **Section 9** | | **Extension model** |
| `P5-9.1` | MUST | Closed sets not extended |
| `P5-9.2` | MUST | Unknown member is a defect, not a default |
| `P5-9.3` | MUST | Open sets registered |
| `P5-9.4` | MUST NOT | No criterion kind by composition |
| `P5-9.5` | MUST | Registry as controlled document |
| `P5-9.6` | MUST NOT | No key reuse |
| `P5-9.7` | MUST | Deprecation rather than removal |
| `P5-9.8` | MUST | Registry version pinned in every run |
| `P5-9.9` | MUST | Semantics in the entry |
| `P5-9.10` | MUST | Scale semantics stated in full |
| `P5-9.11` | MUST | Precision declared |
| `P5-9.12` | MUST | Measurement level declared |
| `P5-9.13` | MUST | Cross scale conversion declared and attributed |
| `P5-9.14` | MUST NOT | No implicit scale |
| `P5-9.15` | MUST | Completeness semantics declared per kind |
| `P5-9.16` | MUST | Pin requirement declared per kind |
| `P5-9.17` | MUST NOT | No caller supply under a non caller kind |
| `P5-9.18` | MUST | Class requirements declared and enforced |
| `P5-9.19` | MUST | Natural person subject declared per class |
| `P5-9.20` | MUST | Owning component per class |
| `P5-9.21` | MUST | Retention basis per class |
| `P5-9.22` | MUST | Aggregator definedness declared |
| `P5-9.23` | MUST | Purposes registered and recorded |
| `P5-9.24` | MUST | Minimum purpose distinctions |
| `P5-9.25` | MUST NOT | No default purpose |
| `P5-9.26` | MUST | Both registered and both recorded |
| `P5-9.27` | MUST | Deprecation without invalidation |
| `P5-9.28` | MUST NOT | No digest without a profile |
| `P5-9.29` | MUST | Refusal codes registered with remedy |
| `P5-9.30` | MUST | Event types registered |
| `P5-9.31` | MUST | Lexicographic composition only |
| `P5-9.32` | MUST | Prior decision outcomes pinned and cited |
| `P5-9.33` | MUST NOT | No criterion reading a concurrent decision |
| `P5-9.34` | MUST NOT | No cyclic decision dependency |
| `P5-9.35` | MUST | Derived parameters recorded as versions |
| `P5-9.36` | MUST | Composition depth bounded and declared |
| **Section 10** | | **Standards and specifications** |
| `P5-10.1` | MUST | Cited edition recorded |
| `P5-10.2` | MUST | Basis marked |
| `P5-10.3` | MUST | Regulatory position established independently |
| `P5-10.4` | MUST | Practice basis recorded |
| `P5-10.5` | MUST | Unsourced requirements identified |
| **Section 11** | | **Anti patterns** |
| `P5-11.1` | MUST NOT | No criterion outside the model |
| `P5-11.2` | MUST NOT | No undeclared tiebreak |
| `P5-11.3` | MUST | Basis recorded on every outcome |
| `P5-11.4` | MUST NOT | No selection by rule sequence |
| `P5-11.5` | MUST | Weights justified and sensitivity recorded |
| `P5-11.6` | MUST NOT | No cycle resolution by traversal |
| `P5-11.7` | MUST | Empty cases distinguished and defaults scoped |
| `P5-11.8` | MUST NOT | No indeterminate as ineligible |
| `P5-11.9` | MUST NOT | No enforcement level as precedence |
| `P5-11.10` | MUST NOT | No eligibility by score threshold |
| `P5-11.11` | MUST | Out of scope candidates reported |
| `P5-11.12` | MUST | Masking analysed and reported |
| `P5-11.13` | MUST | Automation assessed separately from involvement |
| `P5-11.14` | MUST NOT | No override without the original |
| `P5-11.15` | MUST NOT | No tuning on outcomes |
| `P5-11.16` | MUST | Solicitation sets recorded incomplete |
| `P5-11.17` | MUST | Measurement level enforced |
| `P5-11.18` | MUST | Exact arithmetic and declared precision |
| `P5-11.19` | MUST NOT | No selection from a truncated set |
| `P5-11.20` | MUST NOT | No authorisation decisions |
| `P5-11.21` | MUST NOT | No inline eligibility |
| `P5-11.22` | MUST | Model output pinned as an input, not used as a criterion |
| `P5-11.23` | SHOULD | Compound outcomes declared as such |
| `P5-11.24` | MUST | Statement present and not derived |
| `P5-11.25` | MUST | Undecidable distinguished from refused |
| `P5-11.26` | MUST NOT | No action on a non authoritative run |
| **Section 12** | | **Boundaries with other parts** |
| `P5-12.1` | MUST | Declared allocation |
| `P5-12.2` | MUST | Refusal rather than substitution |
| `P5-12.3` | MUST NOT | No reaching past a neighbour |
| `P5-12.4` | MUST | Status and effectivity obtained, never determined |
| `P5-12.5` | MUST NOT | No activation outside the document |
| `P5-12.6` | MUST | Ambiguity returned, not resolved |
| `P5-12.7` | MUST | Whole report obtained and pinned |
| `P5-12.8` | MUST NOT | No constraint evaluation |
| `P5-12.9` | MUST | Indeterminate treatment recorded |
| `P5-12.10` | MUST | Criteria are artifacts, not rule properties |
| `P5-12.11` | MUST | Contradiction arbitrated only by a declared authority order |
| `P5-12.12` | MUST NOT | No decision during an evaluation |
| `P5-12.13` | MUST | Every candidate reported with its ground |
| `P5-12.14` | MUST | Criteria obtainable by pin |
| `P5-12.15` | MUST NOT | No second citation structure |
| `P5-12.16` | MUST | Concepts resolved, not defined |
| `P5-12.17` | MUST | Criteria registered as dependencies |
| `P5-12.18` | MUST | Definition change reaches the criterion |
| `P5-12.19` | MUST | Outcomes independent of process |
| `P5-12.20` | MUST NOT | No process identity required |
| `P5-12.21` | MUST | Undecidable outcomes recorded before routing |
| `P5-12.22` | MUST NOT | No authorisation outcome |
| `P5-12.23` | MUST | Own operations authorised elsewhere |
| `P5-12.24` | MUST | Business outcomes supplied as attributes |
| `P5-12.25` | MUST | Involvements independent of tasks |
| `P5-12.26` | MUST NOT | No task driven recording |
| `P5-12.27` | MUST NOT | No schema validation or versioning |
| `P5-12.28` | MUST | Outcome domain checked against Part 4, not a schema |
| `P5-12.29` | MUST | Value sets bound by pin only |
| `P5-12.30` | MUST | Order completeness checked against the set |
| `P5-12.31` | MUST | Set change surfaces as a criterion change |
| `P5-12.32` | MUST | Digest is the interface |
| `P5-12.33` | MUST NOT | No decision state in the store |
| `P5-12.34` | MUST | Read only assessment |
| `P5-12.35` | MUST NOT | No self assessment as assessment |
| `P5-12.36` | MUST | Basis distribution exposed for assessment |
| `P5-12.37` | MUST NOT | No invocation during a decision |
| `P5-12.38` | MUST | Model outputs pinned and marked |
| `P5-12.39` | MUST | Reproduction limit recorded |
| `P5-12.40` | MUST | Agent attribution supplied |
| `P5-12.41` | MUST | Authority declared, not assumed |
| `P5-12.42` | MUST | Undecidable outcomes returned unmodified |
| **Section 13** | | **What could not be established** |
| `P5-13.1` | MUST | Verification before approval |
| `P5-13.2` | MUST | Gaps declared, not filled |
| `P5-13.3` | SHOULD | Open questions carried forward |

### Derived counts

Every figure below is derived by extraction from the clause text of this document and not asserted independently. The grain of counting is stated for each figure. A clause is one line of the document matching the clause heading form given under Binding of requirement language, that is, an identifier of the form `P5-S.N`, a modality in parentheses, and a subject label. Narrative sentences containing a requirement keyword are not clauses and are not counted; per that same section they are not binding.

**Total clauses.** 433. Grain: one clause heading.

**By modality.** Grain: one clause heading, counted once against its single declared modality.

| Modality | Clauses | Share |
| --- | --- | --- |
| MUST | 305 | 70.4% |
| MUST NOT | 122 | 28.2% |
| SHOULD | 6 | 1.4% |
| SHOULD NOT | 0 | 0.0% |
| MAY | 0 | 0.0% |
| **All** | **433** | **100.0%** |

**Absolute requirements.** 427 clauses carry MUST or MUST NOT and are therefore conditions of conformance. 6 carry SHOULD or SHOULD NOT and require a recorded reason where not satisfied. 0 carry MAY and constrain nothing. Grain: one clause heading. These three figures sum to the total.

**By section.** Grain: one clause heading, attributed to the numbered section in which its heading appears.

| Section | Title | Clauses | MUST | MUST NOT | SHOULD | SHOULD NOT | MAY |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Scope and responsibilities | 15 | 7 | 7 | 1 | 0 | 0 |
| 2 | Terminology | 9 | 1 | 7 | 1 | 0 | 0 |
| 3 | Data model | 118 | 91 | 27 | 0 | 0 | 0 |
| 4 | Interfaces | 35 | 24 | 11 | 0 | 0 | 0 |
| 5 | State model | 26 | 20 | 6 | 0 | 0 | 0 |
| 6 | Execution semantics | 47 | 32 | 15 | 0 | 0 | 0 |
| 7 | Outcome and failure taxonomy | 25 | 17 | 8 | 0 | 0 | 0 |
| 8 | Observability and the audit record | 46 | 36 | 8 | 2 | 0 | 0 |
| 9 | Extension model | 36 | 28 | 8 | 0 | 0 | 0 |
| 10 | Standards and specifications | 5 | 5 | 0 | 0 | 0 | 0 |
| 11 | Anti patterns | 26 | 12 | 13 | 1 | 0 | 0 |
| 12 | Boundaries with other parts | 42 | 30 | 12 | 0 | 0 | 0 |
| 13 | What could not be established | 3 | 2 | 0 | 1 | 0 | 0 |
| **All** | | **433** | **305** | **122** | **6** | **0** | **0** |

**Ordinal integrity.** In this version, the highest ordinal in each section equals the number of clauses in that section, so no identifier has yet been retired. This will cease to be true at the first clause removal, and the count rather than the highest ordinal is then the figure to rely on.

## 1. Scope and responsibilities

### 1.1 What this component is

This part specifies a component that selects one outcome from candidates, using a criterion that is a governed artifact rather than a property of the code or of the order of rows in a table, and that refuses to select where the criterion does not determine an answer.

The component exists to answer one question reliably: **which outcome was chosen, on what criterion, from what candidates, and was the choice determined by the criterion or made by something nobody wrote down.** Every other responsibility in this part is subordinate to that question.

Three properties distinguish this component from the conditional logic it replaces, and each is a reason it exists at all.

**The criterion is an artifact.** It has an identity, a version, an authority, an effective date and an approval. It is not a priority number on a rule, not the sequence of rows in a spreadsheet, not the order in which a loop happened to iterate, and not a weight compiled into a scoring routine. Where the criterion is any of those, the organisation's real policy is not any document it holds, and section 11.1 names the mechanism.

**It does not evaluate.** Whether a candidate is admissible is a constraint question, answered by `Part 2` and obtained as a verdict. This is the reciprocal `Part 2` section 12.5 requires, and it is not a division of labour but a division of kind: that component returns truth, this one returns a choice.

**It declines to choose where the criterion does not choose.** A criterion that leaves two candidates tied, or that yields a cycle, or that compares candidates on incommensurable attributes, has not determined an answer. Every decision engine in ordinary use resolves the first by row order, the second by iteration order and the third by an implicit weighting, and all three resolutions are arbitrary and none is recorded. Section 7.2 makes each a first class outcome so that the arbitrariness cannot be concealed.

The component is accountable for the following.

The candidate set: its source, its members, and the declared completeness of the enumeration.

Eligibility: the obtaining of constraint verdicts from `Part 2` for each candidate, and the treatment of a candidate whose eligibility could not be established.

The criterion: its identity, version, kind, authority, parameters and approval, and the requirement that every parameter of it be justified rather than merely present.

The closed taxonomy of criterion kinds, and the properties each guarantees.

Hit policies, precedence orders, tiebreaks and defaults, all of which `Part 2` section 12.5 allocates here, and each of which is specified as a declared artifact rather than a behaviour.

Comparability and transitivity: the detection of ties, cycles and incomparable candidates, and the refusal to resolve any of the three by an undeclared rule.

The selection act: which candidate was chosen, on what basis, and by what margin.

Margin and marginality: how close the decision was, in the criterion's own terms, and the flagging of decisions decided within a declared margin.

Elimination grounds for every candidate not selected, in the form `Part 3` requires.

The distinction between a decision made by a mechanism, a decision made by a person, and a decision nominally made by a person that was decisively based on a mechanism.

The pinning of everything a decision depended on, and the reproducibility of the decision from those pins.

The audit record of all of the above, at a grain sufficient to reconstruct any decision.

### 1.2 What this component is not

Each exclusion names something a decision engine absorbs if nobody stops it, and each absorption destroys a property some other component was supposed to guarantee.

The component is not a constraint evaluator. It does not determine whether a candidate satisfies a rule, and it obtains verdicts from `Part 2`. This is the reciprocal that part requires, and clause P5-1.4 makes it binding.

The component is not the policy decision point. An authorisation decision, being whether a principal may perform an operation, belongs to `Part 7`, which has its own combining algorithms and its own obligations model. The boundary is stated in section 12.7 and it is contestable, since an authorisation is plainly a selection from two candidates; the test offered is whether the outcome is an entitlement to act.

The component is not the ledger. A decision is a determination in the sense of `Part 3` and is recorded there. This component holds its own operational record and does not hold provenance for anything else.

The component is not the definition repository. The concepts a criterion is expressed over are governed by `Part 4`, and clause P4-12.14 requires this component's criteria to be registered there as dependencies.

The component is not a workflow engine. When a decision is invoked, what happens to its outcome, how a referral to a person is routed and how an overturned decision is remediated are orchestration and belong to `Part 6`.

The component is not a task manager. The queue of decisions awaiting human determination belongs to `Part 8`.

The component is not a model runtime. Where a score produced by an inferential model is an input to a criterion, the score is a pinned input obtained beforehand, and the model is never invoked during a decision. `Part 13` owns invocation and section 12.13 states why a non deterministic evaluand cannot sit inside a reproducible selection.

The component is not the candidate generator of last resort. It never invents a candidate. Candidates are supplied or obtained from a declared source, per section 3.5.

The component is not an optimiser. It selects from an enumerated candidate set by a declared criterion. Searching a space for an optimum, solving a program, or fitting a policy is out of scope, and section 13.5 records that the boundary between a large candidate set and a search space is not sharp.

The component is not a conformance assessor, of itself or of anything else.

**P5-1.1 (MUST) Purpose satisfaction.** An implementation must be able to state, for any decision within its retained history, the candidate set, the eligibility verdict for each candidate, the criterion version applied, the outcome, the basis on which the outcome was reached and the margin by which it was reached, by the mechanism specified in section 6.

**P5-1.2 (MUST) Criterion as a governed artifact.** An implementation must obtain every criterion as a versioned artifact resolvable under `Part 1`, with an authority, and must not apply a criterion expressed as code, configuration, row order or an undeclared parameter.

**P5-1.3 (MUST NOT) No undeclared resolution.** An implementation must not resolve a tie, a cycle or an incomparability by any means not declared in the criterion, and must return the corresponding outcome of section 7.2 instead.

**P5-1.4 (MUST NOT) No constraint evaluation.** An implementation must not evaluate a constraint, must obtain eligibility verdicts from `Part 2`, and must record the whole evaluation report per clause P2-12.6.

**P5-1.5 (MUST) Indeterminate eligibility surfaced.** An implementation must not treat a candidate whose eligibility verdict is indeterminate as eligible or as ineligible without a criterion that declares the treatment, and must record that it did so, per section 3.6.

**P5-1.6 (MUST) Reproducibility.** An implementation must be able to reproduce any decision it has issued from the pins recorded with it, and must return the same outcome on re decision with the same pins, per section 6.1.

**P5-1.7 (MUST) Every candidate recorded.** An implementation must record every candidate it considered, with its elimination ground where it was not selected, and must not record the selected outcome alone.

**P5-1.8 (MUST) Margin recorded.** An implementation must record the margin by which the selected candidate was preferred to the next, in the criterion's own terms, or record that no margin is definable for the criterion kind.

**P5-1.9 (MUST NOT) No candidate invention.** An implementation must not add a candidate to a decision that was not supplied or obtained from a declared candidate source.

**P5-1.10 (MUST NOT) No action.** An implementation must not perform, request or schedule any action as a consequence of a decision, and must not modify any subject of a decision.

**P5-1.11 (MUST NOT) No update in place.** An implementation must not represent any state change specified by this part as a modification or deletion of a previously written row, tuple, object or event.

**P5-1.12 (MUST NOT) No absorption of neighbouring responsibilities.** An implementation must not evaluate constraints, decide authorisation, orchestrate activities, define concepts, invoke models or record provenance for other components, as those responsibilities are allocated in section 12.

**P5-1.13 (SHOULD) Declared exclusions.** An implementation should publish, as a controlled document under `Part 1`, the list of section 1.2 exclusions that it in fact provides by other means, so that a reader can tell what the implementation does not guarantee.

**P5-1.14 (MUST NOT) No conformance self assertion.** An implementation must not assert conformance to this part on the basis of its own internal checks alone, and must not represent such an assertion as an assessment.

**P5-1.15 (MUST) Time horizon declaration.** An implementation must declare the period for which it undertakes to answer the purpose question, as a duration or an absolute date rather than as an indefinite commitment.

### 1.3 What makes a decision a decision

The distinction between this component and `Part 2` was stated in that part's section 12.5 and is restated here because it is the boundary the whole design turns on.

**A determinate function of the inputs is not a decision.** Computing whether an interval exceeds a threshold, whether a value is in a set, whether a document was in force on a date, is evaluation. There is one right answer and no criterion is required beyond the definitions.

**A function that requires a criterion not derivable from the inputs is a decision.** Selecting which of two applicable retention schedules governs requires a rule of precedence. Choosing which of three eligible suppliers to use requires a preference. Deciding which of two conflicting authorities prevails requires a hierarchy among authorities. In each case the inputs do not contain the answer, and something must be supplied that is not a fact about the inputs.

The test is whether the component would have to choose. If it would, the thing it chooses by is policy, and policy that is not an artifact is policy nobody can review, date, approve or change deliberately.

Two consequences are worth drawing out because they are counterintuitive.

**A lookup can be a decision.** A table mapping a condition to an outcome looks like a function and is one, but where two rows both match and the table's hit policy picks between them, the hit policy is the criterion and it is policy. This is why `Part 2` section 12.5 allocates every hit policy here, and why section 3.9 specifies them as artifacts rather than as behaviours.

**A decision can have exactly one candidate and still be a decision.** Where the criterion is what admitted the single candidate, the decision is real and the outcome is the candidate. Where the single candidate was the only thing supplied, the decision is a formality and section 7.2 distinguishes the two, because a decision with one candidate that nobody chose among is a record of an absence of choice rather than a choice.

### 1.4 The reader this part is written for

Two readers are assumed and their needs diverge sharply.

The first invokes a decision and needs the outcome. That reader wants one value.

The second is asked, years later, why a particular applicant was declined, why a particular supplier was chosen, or why a particular retention period was applied. That reader needs the candidates, the eligibility verdicts, the criterion as it stood, the margin, and whether anybody exercised judgement. In some jurisdictions that reader is a regulator with a statutory basis for the question, and section 10.5 records the provisions.

Where the two conflict this part serves the second, and the cost is real: the decision record specified in section 3.13 is substantially larger than the value the first reader wanted, and section 13.6 records that nothing here is costed.
## 2. Terminology

Terms are defined here only if this component owns them. A term owned by another part is cited to that part and is not redefined. Where a term is taken from an external standard, the standard is named. Where this part narrows or diverges from the external definition, the divergence is stated.

### 2.1 Terms owned by this part

**Decision.** The selection of one outcome from a candidate set by a criterion, or the recorded refusal to select. A decision is a determination in the sense of `Part 3` section 2.1 and is recorded there; this part specifies how it is reached.

**Decision definition.** The governed artifact specifying, for a class of decision, the candidate source, the eligibility rule set, the criterion, the tiebreak, the default, and the treatment of an indeterminate eligibility verdict.

**Candidate.** One outcome that was available to be selected, whether or not it was eligible and whether or not it was selected.

**Candidate set.** The candidates considered in one decision, with the declared completeness of the enumeration.

**Candidate source.** The declared origin of a candidate set: supplied by the caller, enumerated from a reference set, or produced by a governed generator.

**Eligibility.** The admissibility of a candidate, established by constraint verdicts obtained from `Part 2` and never determined here.

**Criterion.** The governed artifact by which a selection is made among eligible candidates. A criterion is of exactly one kind from the closed set of section 3.7.

**Criterion parameter.** A value the criterion requires that is not derived from the candidates: a weight, a threshold, a precedence order, a seed. Every parameter requires a justification, per section 3.8.

**Precedence order.** A declared total or partial order over outcome values, used as a criterion or as a tiebreak. Distinguished throughout from an order over rules or rows, which this part refuses.

**Hit policy.** A criterion applied where more than one rule of a decision table matches. Term follows DMN 1.5, which defines seven; section 3.9 states which this part admits and which it refuses, and why.

**Tiebreak.** A declared criterion applied where the primary criterion leaves two or more candidates equally preferred. A tiebreak is a criterion in its own right and is subject to every requirement a criterion is.

**Default.** A declared outcome applied where the criterion selects no candidate. A default is an artifact with an authority and is not a fallback in code.

**Selection.** The act of identifying one candidate as the outcome, with the basis on which it was identified.

**Basis of selection.** Which of criterion, tiebreak or default produced the outcome. Recorded on every decision and never collapsed.

**Margin.** The extent by which the selected candidate was preferred to the next best, expressed in the terms of the criterion that selected it.

**Marginal decision.** A decision whose margin falls within a declared threshold, recorded so that a decision that nearly went the other way is distinguishable from one that did not.

**Dominance.** The relation in which one candidate is at least as good as another on every attribute the criterion considers and better on at least one.

**Incomparability.** The condition in which neither of two candidates dominates the other and the criterion supplies no rate of exchange between the attributes on which they differ.

**Intransitivity.** The condition in which the criterion's pairwise preferences contain a cycle, so that no candidate is maximal.

**Elimination ground.** The recorded reason a candidate was not selected, drawn from the closed set of section 3.15 and aligned with the enumeration `Part 3` section 3.10 requires.

**Solely automated decision.** A decision in which no natural person exercised judgement on the outcome.

**Decisive automation.** The condition in which a natural person nominally made the decision and the outcome was decisively based on a mechanism's output. The concept follows the criterion the Court of Justice of the European Union applied in Case C-634/21, and section 3.16 states why it is recorded separately from human involvement.

**Application time.** The time dimension in which a criterion is in force. Used unchanged from `Part 1` section 2.1.

**Knowledge time.** The instant at which this component durably recorded a fact, assigned by this component. Used unchanged from `Part 1`.

**Occurrence time.** The instant at which a recorded act happened in the world, as asserted by an actor. Used unchanged from `Part 1`.

**Pin.** A recorded identity and version of something a decision depended on, sufficient to obtain the same thing again. Used unchanged from `Part 2` section 2.1.

### 2.2 Clauses governing terminology

**P5-2.1 (MUST) Single meaning per term.** An implementation must use each term defined in section 2.1 with the meaning given there in all of its interfaces, records, reports and documentation.

**P5-2.2 (MUST NOT) No redefinition.** An implementation must not use a term defined in section 2.1 for a different concept, and must not use a different term for a concept defined in section 2.1 in any interface specified by this part.

**P5-2.3 (MUST NOT) No collapsing of eligibility and preference.** An implementation must not use one term or one field for whether a candidate was admissible and whether it was preferred.

**P5-2.4 (MUST NOT) No collapsing of the bases of selection.** An implementation must not use one term or one field for a criterion, a tiebreak and a default.

**P5-2.5 (MUST NOT) No collapsing of precedence over outcomes and order over rules.** An implementation must not use one term for a declared order over outcome values and a sequence of rules or rows.

**P5-2.6 (MUST NOT) No collapsing of the three failures to determine.** An implementation must not use one term or one value for a tie, an intransitivity and an incomparability.

**P5-2.7 (MUST NOT) No collapsing of human involvement and decisive automation.** An implementation must not treat a recorded human involvement as establishing that a decision was not decisively based on a mechanism.

**P5-2.8 (MUST NOT) No collapsing of the three clocks.** An implementation must not use one term or one field for more than one of application time, knowledge time and occurrence time.

**P5-2.9 (SHOULD) Term registry.** An implementation should publish the terms it adds beyond section 2.1, with definitions, as a controlled document under `Part 1`.
## 3. Data model

The model is stated as entities with typed fields. For each field the model gives its type, whether it is required, its cardinality, and what its absence means. Absence semantics are stated because in this component the commonest wrong inference from a missing field is that an outcome was determined by the criterion when it was in fact produced by a tiebreak or a default.

### 3.1 Type vocabulary

| Type | Value space | Notes |
| --- | --- | --- |
| `ID` | An opaque, globally unique, immutable identifier | Never reused. Never parsed for meaning. |
| `URN` | A persistent name in a declared namespace | Resolvable by the component owning the namespace. |
| `ATIME` | An instant in application time | The dimension in which criteria are in force. |
| `KTIME` | An instant in knowledge time, assigned by this component | Never accepted from a caller. |
| `OTIME` | An instant asserted by an actor as when an act occurred | Never assigned by this component. |
| `SEQ` | A monotonically increasing ordinal within a named stream | Total order within the stream only. |
| `DIGEST` | An algorithm identifier and a value | Algorithm from the registry of section 9.7. |
| `ENUM` | A member of a named closed or registered set | The set is named at every point of use. |
| `TEXT` | A sequence of characters intended for a person | Carries a `LANG`. |
| `LANG` | A language tag per BCP 47 | Required wherever `TEXT` appears. |
| `PIN` | An identity, a version and where available a digest | Sufficient to obtain the identical artifact again. |
| `CITEREF` | A citation resolvable under `Part 1`, carrying its mode | Used for criterion authority and approval. |
| `ACTOR` | An opaque reference to a person, organisation or automated agent | Carries its kind. Resolved elsewhere. |
| `AUTHREF` | A reference to an authorisation decision made by `Part 7` | Recorded, never evaluated here. |
| `VERDICT` | A `Part 2` verdict envelope | Recorded whole, never reduced. |
| `SCALE` | A named ordered value space with a declared comparison | Required wherever a score or a margin is expressed. |
| `TRUTH` | One of `TRUE`, `FALSE`, `INDETERMINATE` | The three valued domain, used unchanged from `Part 2` section 6.2. |
| `COUNT` | A non negative integer | Grain stated wherever reported. |
| `DURATION` | A length of time, independent of any instant | |

The `SCALE` type is the one worth noting. A score without a declared scale is a number whose comparison semantics are unknown, and a margin expressed without one cannot be compared with a marginality threshold. Section 3.14 requires the scale on every score and every margin.

**P5-3.1 (MUST) Declared types.** An implementation must be able to state, for every field it holds that corresponds to a field in this section, which type of the table above it carries.

**P5-3.2 (MUST NOT) No semantic identifiers.** An implementation must not derive the meaning, precedence, eligibility or preference of anything from the characters of its `ID` or `URN`.

**P5-3.3 (MUST) Language tag present.** An implementation must record a `LANG` with every `TEXT` value and must not default it silently.

**P5-3.4 (MUST NOT) No caller supplied knowledge time.** An implementation must assign every `KTIME` itself and must reject a request supplying one.

**P5-3.5 (MUST) Scale declared with every score.** An implementation must record the scale and its comparison semantics with every score and every margin it holds.

**P5-3.6 (MUST) Three valued domain used unchanged.** An implementation must use the truth domain of `Part 2` section 6.2 wherever it holds or reports a truth value and must not introduce a two valued reduction.

### 3.2 The four parts of a decision

A decision is four things and they are conflated in almost every implementation, with the conflation of the second and third being the one that does the damage.

**Candidate set generation.** What was available. This is a factual question about the world and about the enumeration performed, and its answer has a completeness property: the set is either every candidate there was, or the candidates that were found. A decision over an incomplete set chose the best of what it saw, which is a weaker claim than choosing the best.

**Eligibility.** Which candidates were admissible. This is a constraint question and is entirely `Part 2`'s. Its answers are three valued, and the third value is the hardest thing in this part, because a candidate whose eligibility could not be established is neither in nor out and the decision must do something.

**The criterion.** How to choose among the admissible. This is policy. It is not derivable from the candidates and it is the artifact this part exists to govern.

**The selection.** Which candidate the criterion identified, on what basis, and by what margin.

The conflation that matters is between eligibility and preference. An implementation that scores candidates and takes the highest has merged the two: an ineligible candidate with a high score is excluded by a threshold on the score, and the threshold is now doing two jobs at once. When the eligibility rule changes, the score distribution shifts and the selection changes for reasons nobody intended. When the preference changes, candidates that should have been excluded become admissible. Neither change is visible as what it was.

Separating them costs an extra call to `Part 2` and buys three things. Eligibility becomes reviewable as a rule with an authority and a statement. Preference becomes reviewable as a criterion with a justification. And the record distinguishes a candidate that was not permitted from one that was permitted and not preferred, which are entirely different facts to the person the decision was about.

**P5-3.7 (MUST) Four parts separately recorded.** An implementation must record the candidate set with its completeness, the eligibility verdict per candidate, the criterion applied, and the selection with its basis and margin, as separate elements of every decision.

**P5-3.8 (MUST NOT) No eligibility by score threshold.** An implementation must not exclude a candidate from selection by a threshold on a score produced by the criterion, and must obtain every exclusion for inadmissibility from an eligibility verdict.

**P5-3.9 (MUST) Eligibility obtained before preference.** An implementation must obtain every eligibility verdict before applying the criterion and must not apply the criterion to a candidate whose eligibility is not `TRUE`, except under the declared indeterminate treatment of section 3.6.

**P5-3.10 (MUST) Completeness of the candidate set declared.** An implementation must record whether the candidate set is a complete enumeration and must not default the value.

**P5-3.11 (MUST NOT) No merged exclusion ground.** An implementation must record whether a candidate was excluded for inadmissibility or not selected for want of preference, and must not use one ground for both.

### 3.3 Entity inventory

Every entity is immutable once written. A change is a new row; nothing specified in this part is ever updated in place, for the reason `Part 3` section 3.3 gives: a decision is a historical fact about what a system concluded, and a historical fact that can be edited is not evidence.

| Group | Entity | Purpose |
| --- | --- | --- |
| Definition | `decision_definition` | The persistent identity of a class of decision. |
| Definition | `decision_definition_version` | One immutable state of a decision definition. |
| Definition | `candidate_source_declaration` | The declared origin of candidate sets for the definition. |
| Definition | `eligibility_rule_set_binding` | The `Part 2` rule set version that establishes eligibility. |
| Definition | `indeterminate_treatment` | The declared treatment of an indeterminate eligibility verdict. |
| Criterion | `criterion` | The persistent identity of a criterion. |
| Criterion | `criterion_version` | One immutable state of a criterion, of exactly one kind. |
| Criterion | `criterion_parameter` | One parameter of a criterion version, with its justification. |
| Criterion | `precedence_order` | A declared order over outcome values. |
| Criterion | `criterion_authority` | The clause from which the criterion derives its legitimacy. |
| Criterion | `criterion_approval` | The `Part 1` resolution establishing approval. |
| Criterion | `tiebreak_declaration` | The declared tiebreak, itself a criterion version. |
| Criterion | `default_declaration` | The declared default outcome and its authority. |
| Criterion | `criterion_analysis` | A recorded static analysis over a criterion version. |
| Decision | `decision_request` | What was asked, with the instants and pins supplied. |
| Decision | `decision_run` | One execution: its bounds, clocks and outcome. |
| Decision | `candidate` | One candidate considered in a run. |
| Decision | `candidate_eligibility` | The `Part 2` verdict envelope for one candidate. |
| Decision | `comparison` | One pairwise or scored comparison performed. |
| Decision | `selection` | The outcome, its basis and its margin. |
| Decision | `elimination` | The ground on which a candidate was not selected. |
| Decision | `decision_pin` | One artifact the run depended on. |
| Decision | `decision_signal` | A condition observed during a run that is not an outcome. |
| Human | `human_involvement` | A natural person's participation in a decision. |
| Human | `decisive_automation_assessment` | Whether a nominally human decision was decisively based on a mechanism. |
| Human | `override` | A recorded departure from the outcome the criterion produced. |
| Registry | `criterion_kind_registration` | Reserved. Criterion kinds are closed; see section 9.1. |
| Registry | `scale_registration` | A registered scale and its comparison semantics. |
| Registry | `candidate_source_kind_registration` | A registered candidate source kind. |
| Registry | `decision_class_registration` | A registered class of decision. |
| Registry | `aggregator_registration` | A registered aggregation function for a collecting criterion. |

**P5-3.12 (MUST) Entity coverage.** An implementation must be able to state, for every entity in the table above, where the information it carries is held, or that the entity is not applicable because the corresponding optional capability is not provided.

**P5-3.13 (MUST NOT) No update in place.** An implementation must not represent any state change specified by this part as a modification or deletion of a previously written row.

**P5-3.14 (MUST NOT) No decision amendment.** An implementation must not modify a recorded decision, its candidates, its eligibility verdicts, its comparisons, its selection or its pins, and must record a corrected conclusion as a further decision whose relation to the earlier one is recorded.

### 3.4 The decision definition

A decision definition is the governed artifact specifying how a class of decision is made. It exists so that the answer to "how do we decide this" is a document rather than a deployment.

`decision_definition_version` fields:

| Field | Type | Required | Cardinality | Absence means |
| --- | --- | --- | --- | --- |
| `definition_version_id` | `ID` | yes | 1 | n/a |
| `definition_id` | `ID` | yes | 1 | n/a |
| `decision_class` | `ENUM` | yes | 1 | n/a. Registered under section 9.8. |
| `document_citation` | `CITEREF` | yes | 1 | n/a. The `Part 1` version that carries the definition. |
| `candidate_source_id` | `ID` | yes | 1 | n/a |
| `eligibility_binding_id` | `ID` | no | 0..1 | No eligibility rule set applies, which is a positive claim that every candidate is admissible. |
| `indeterminate_treatment_id` | `ID` | no | 0..1 | Required wherever an eligibility binding is present. |
| `criterion_version_id` | `ID` | yes | 1 | n/a |
| `tiebreak_id` | `ID` | no | 0..1 | No tiebreak is declared, so a tie yields the undecidable outcome of section 7.2. |
| `default_id` | `ID` | no | 0..1 | No default is declared, so an empty selection yields the outcome of section 7.2. |
| `outcome_concept` | `URN` | yes | 1 | n/a. The `Part 4` concept the outcome values realise. |
| `subject_is_natural_person` | `TRUTH` | yes | 1 | n/a. Whether decisions of this class concern natural persons. |
| `marginality_threshold` | `TEXT` | no | 0..1 | No marginality threshold is declared, so no decision of this class is flagged marginal. |
| `created_ktime` | `KTIME` | yes | 1 | n/a |
| `authored_by` | `ACTOR` | yes | 1..n | n/a |

Three fields carry more weight than their size suggests.

The absence of a `tiebreak_id` is a positive claim, not an omission. It says that where the criterion leaves candidates equally preferred, the organisation would rather be told than have the component pick. That is the correct default and section 7.2 provides the outcome. An implementation that supplies an implicit tiebreak when none is declared has taken a policy decision on the organisation's behalf, and section 11.2 names the mechanism.

The absence of a `default_id` is the same claim about the empty case.

`subject_is_natural_person` exists because the obligations that attach to a decision about a person are different in kind, and section 3.16 and section 10.5 state them. It is recorded on the definition rather than derived per decision, because deriving it per decision means it will be wrong in the cases where the subject is unusual.

**P5-3.15 (MUST) Definition carried by a document.** An implementation must record the `Part 1` citation of the document version that carries every decision definition version and must not apply a definition that has none.

**P5-3.16 (MUST) Absent tiebreak and default are claims.** An implementation must treat an absent tiebreak or default declaration as an assertion that the corresponding outcome of section 7.2 is to be returned, and must not supply either implicitly.

**P5-3.17 (MUST) Indeterminate treatment required where eligibility applies.** An implementation must refuse a definition version carrying an eligibility binding and no indeterminate treatment.

**P5-3.18 (MUST) Outcome concept bound.** An implementation must record the `Part 4` concept the outcome values realise, so that a change to the concept reaches the decision definition through impact analysis.

**P5-3.19 (MUST) Natural person subject declared.** An implementation must record whether decisions of a class concern natural persons and must not default the value.

**P5-3.20 (MUST NOT) No implicit definition.** An implementation must not perform a decision that is not governed by a recorded decision definition version.

**P5-3.21 (MUST NOT) No definition amendment.** An implementation must not alter a recorded definition version and must record every change as a new version.

### 3.5 Candidate sets and their sources

A decision engine that generates its own candidates has business logic in it that nobody reviewed. A decision engine that accepts whatever it is given has no record of whether the set was complete. This section requires the source to be declared and the completeness to be stated.

`candidate_source_declaration` fields carry a registered `kind`, a `pin` to the source artifact where the kind requires one, an `enumeration_basis`, and a `completeness_basis`. The minimum registered kinds:

| Kind | Means | Completeness |
| --- | --- | --- |
| `SUPPLIED_BY_CALLER` | The caller enumerated the candidates. | The caller declares it; this component records the declaration and does not verify it. |
| `REFERENCE_SET_ENUMERATION` | Every member of a pinned `Part 10` set. | Complete with respect to the pinned set version. |
| `GOVERNED_GENERATOR` | Produced by a generator that is itself a governed artifact under `Part 1`. | Declared by the generator. |
| `PRIOR_DECISION_OUTCOMES` | The outcomes of a set of earlier decisions. | Complete with respect to the enumerated decisions. |
| `EXTERNAL_SOLICITATION` | Responses to a request made outside the organisation, such as tenders or quotations. | Never complete: candidates that did not respond are not in the set and are not knowable. |

`EXTERNAL_SOLICITATION` is worth its own member because its incompleteness is structural rather than accidental. A supplier who did not bid is not a candidate and is not recorded as one, so a decision among three bids is not a decision among the market. That is obvious when stated and invisible in a record that says three candidates were considered.

`candidate` fields:

| Field | Type | Required | Cardinality | Absence means |
| --- | --- | --- | --- | --- |
| `candidate_id` | `ID` | yes | 1 | n/a |
| `run_id` | `ID` | yes | 1 | n/a |
| `outcome_value` | `TEXT` | yes | 1 | n/a. The value that would be the outcome if this candidate were selected. |
| `outcome_value_digest` | `DIGEST` | yes | 1 | n/a |
| `candidate_reference` | `URN` | no | 0..1 | The candidate is a bare value rather than a referenced thing. |
| `attributes_pin` | `PIN` | no | 0..1 | The candidate carries no attributes beyond its outcome value. |
| `source_ordinal` | `SEQ` | yes | 1 | n/a. Position as supplied. Never used as a criterion; see section 3.9. |
| `received_ktime` | `KTIME` | yes | 1 | n/a |

The `source_ordinal` field is recorded and is prohibited from affecting any outcome. It is recorded so that a reader can see the order in which candidates arrived, which is diagnostically useful, and it is prohibited from mattering because an order of arrival is not a criterion. Clause P5-3.26 states the prohibition and clause P5-6.5 makes it checkable.

**P5-3.22 (MUST) Source kind declared.** An implementation must record a registered candidate source kind for every candidate set and must not default it.

**P5-3.23 (MUST) Source pinned where the kind requires it.** An implementation must record a pin to the reference set version, the generator version or the enumerated decisions, as the source kind requires.

**P5-3.24 (MUST) Completeness recorded with its basis.** An implementation must record the completeness of every candidate set together with the basis on which the completeness is claimed, and must record a caller's declaration as the caller's.

**P5-3.25 (MUST) External solicitation never complete.** An implementation must record a candidate set of kind `EXTERNAL_SOLICITATION` as incomplete and must not accept a claim that it is complete.

**P5-3.26 (MUST NOT) No effect from source ordinal.** An implementation must not permit the order in which candidates were supplied or enumerated to affect any eligibility verdict, comparison, selection, tiebreak or margin.

**P5-3.27 (MUST) Outcome value digested.** An implementation must record a digest over each candidate's outcome value under a declared canonical form profile.

**P5-3.28 (MUST NOT) No candidate deduplication without a declared rule.** An implementation must not merge two candidates on the ground that their outcome values appear equal, unless the scale registration declares the equality, and must record every merge it performs.

### 3.6 Eligibility, and the indeterminate candidate

This is the hardest requirement in the part and it follows directly from `Part 2` returning three valued verdicts.

`Part 2` evaluates the eligibility rule set against a candidate and returns an evaluation report. The report may say the candidate satisfies every rule, violates one, or that one or more rules could not be evaluated. The third case is not rare; it is the ordinary consequence of a withheld attribute, an unavailable reference set or an absent value, all of which `Part 2` sections 7.2 and 3.12 specify in detail precisely so that they reach the caller intact.

The caller is this component, and it must do something. Three things are possible and each is wrong in a different way.

**Exclude the candidate.** The decision then chooses among a subset and may select a worse outcome than was available. Where the candidate was the best and was excluded for want of information, the organisation has taken a worse decision and nothing records that it did.

**Include the candidate.** The decision may select a candidate that was in fact inadmissible. Where the decision is about a person, the person may receive an outcome they were not entitled to, or be exposed to one they should have been protected from.

**Decline to decide.** The decision returns an indeterminate outcome, the caller is told, and somebody obtains the missing information or exercises judgement. This is correct and it is expensive, and an organisation that adopts it for every case will abandon it.

This part requires the third by default and permits the first two only where the decision definition declares the treatment, with an authority, and where the treatment is recorded on every decision that used it.

`indeterminate_treatment` fields:

| Field | Type | Required | Cardinality | Absence means |
| --- | --- | --- | --- | --- |
| `treatment_id` | `ID` | yes | 1 | n/a |
| `treatment` | `ENUM` | yes | 1 | n/a. One of `DECLINE_TO_DECIDE`, `EXCLUDE_CANDIDATE`, `INCLUDE_CANDIDATE`, `TREAT_BY_SUBCLASS`. |
| `subclass_treatment` | `ENUM` | no | 0..n | Required where `treatment` is `TREAT_BY_SUBCLASS`. One treatment per `Part 2` indeterminacy subclass. |
| `authority` | `CITEREF` | yes | 1 | n/a |
| `justification` | `TEXT` | yes | 1 | n/a |
| `declared_by` | `ACTOR` | yes | 1 | n/a |
| `applies_to_natural_person_subject` | `TRUTH` | yes | 1 | n/a. Whether the treatment is permitted where the subject is a natural person. |

`TREAT_BY_SUBCLASS` is the member that makes the field useful rather than a blunt switch. `Part 2` section 7.2 divides indeterminacy into five subclasses each with a named remedy owner, and they warrant different treatments. An indeterminacy of subclass `DEPENDENCY_INDETERMINACY`, where a reference set was unavailable, is transient and declining to decide is reasonable. One of subclass `SUBJECT_INDETERMINACY`, where an attribute was withheld, may be permanent for this candidate and excluding it may be the only workable answer. One of subclass `COMPONENT_DEFECT` should never lead to a decision at all. A single treatment for all five is a policy nobody would write if they had to write it out.

`applies_to_natural_person_subject` exists because a treatment that excludes a candidate for want of information is a materially different act when the candidate is a person's application, and section 10.5 records the regimes that bear on it.

**P5-3.29 (MUST) Eligibility obtained as a whole report.** An implementation must obtain the eligibility of every candidate as a `Part 2` evaluation report and must record the whole report and its pin set, not a pass indicator or a count, per clause P2-12.6.

**P5-3.30 (MUST) Declining to decide is the default.** An implementation must return the indeterminate outcome of section 7.2 where any candidate's eligibility is indeterminate and the decision definition declares no treatment.

**P5-3.31 (MUST) Treatment authorised and justified.** An implementation must require an authority and a justification on every indeterminate treatment declaration.

**P5-3.32 (MUST) Treatment recorded on the decision.** An implementation must record, on every decision in which an indeterminate eligibility verdict was treated, the treatment applied, the candidate affected and the `Part 2` subclass and code, per clause P5-1.5.

**P5-3.33 (MUST) Subclass treatments distinguishable.** An implementation must permit a treatment to be declared per `Part 2` indeterminacy subclass and must record which subclass triggered the treatment applied.

**P5-3.34 (MUST NOT) No treatment of a component defect as data.** An implementation must not apply a treatment of `EXCLUDE_CANDIDATE` or `INCLUDE_CANDIDATE` to an indeterminacy of `Part 2` subclass `COMPONENT_DEFECT` and must decline to decide.

**P5-3.35 (MUST) Natural person applicability enforced.** An implementation must refuse to apply a treatment whose `applies_to_natural_person_subject` is false in a decision whose definition declares the subject a natural person.

**P5-3.36 (MUST NOT) No silent exclusion.** An implementation must not exclude a candidate for an indeterminate eligibility verdict without recording the exclusion as an elimination of the corresponding ground in section 3.15.

**P5-3.37 (MUST) Vacuous satisfaction carried through.** An implementation must record where a candidate's eligibility rested on a `Part 2` satisfaction verdict marked vacuous, and must not treat a vacuous satisfaction as an established eligibility without recording that it did so.
### 3.7 The criterion, and the closed taxonomy of kinds

A criterion is of exactly one kind. The set is closed, because a consumer of a decision must know what guarantees the criterion offers, and a kind it does not recognise is a criterion whose properties it cannot assume.

Nine kinds. The table is normative.

| Kind | Selects by | Ties possible | Cycles possible | Incomparability possible |
| --- | --- | --- | --- | --- |
| `PRECEDENCE_OVER_OUTCOMES` | A declared total or partial order over outcome values. | Yes, where the order is partial or two candidates share an outcome value. | No. | Yes, where the order is partial. |
| `SCORE_FUNCTION` | A score computed per candidate on a declared scale; the extreme wins. | Yes. | No. | No. |
| `LEXICOGRAPHIC` | An ordered list of sub criteria, each resolving ties left by the previous. | Yes, only if every sub criterion ties. | No. | Yes, if a sub criterion is a partial order and no later one separates. |
| `WEIGHTED_AGGREGATE` | A weighted combination of attribute values on a declared scale. | Yes. | No. | No, and see the discussion below. |
| `DOMINANCE_ONLY` | Selects only where one candidate dominates every other. | No. | No. | Yes, and reporting it is the point of the kind. |
| `PAIRWISE_PREFERENCE` | A declared pairwise preference relation, which need not be a total order. | Yes. | **Yes.** | Yes. |
| `AUTHORITY_PRECEDENCE` | A declared order over the authorities from which candidate outcomes derive. | Yes, where two candidates derive from one authority. | No. | Yes, where two authorities are unranked relative to each other. |
| `EXTERNAL_DETERMINATION` | A choice made outside this component, recorded rather than computed. | n/a | n/a | n/a |
| `DECLARED_RANDOM` | A seeded pseudorandom selection over the eligible candidates. | No. | No. | No. |

Six of the nine warrant comment.

**`PRECEDENCE_OVER_OUTCOMES`** is the kind that DMN's priority and output order hit policies express, and section 3.9 explains why this part accepts those two and refuses the two that order rules instead. The order is over outcome values and is therefore a governable artifact: it can be written down, approved, dated and reviewed. Where the order is partial, two candidates may be unranked relative to each other, and the kind then yields incomparability rather than picking.

**`WEIGHTED_AGGREGATE`** is the kind that deserves the most suspicion and receives the most use. Combining attribute values on different scales into one number requires a rate of exchange between them, and a rate of exchange between incommensurable attributes is a value judgement, not a fact. A weight of 0.3 on price against 0.7 on delivery time is a statement that a certain amount of money is worth a certain amount of time, and that statement is policy of the most consequential kind. The kind is admitted because organisations need it; section 3.8 requires every weight to carry a justification, on the same basis `Part 2` requires an interpretation note wherever a threshold does not appear in the cited clause.

The table records that incomparability is not possible under this kind, and that is a statement about the arithmetic rather than about the world: once the weights are fixed, every pair of candidates is comparable, because the weights have supplied the rate of exchange. What has happened is that the incomparability was resolved by the weights rather than reported. That is legitimate where the weights are governed and it is the mechanism by which a genuine incommensurability is made invisible, which is why section 11.5 names it and why `DOMINANCE_ONLY` exists as the honest alternative.

**`DOMINANCE_ONLY`** selects only where one candidate is at least as good as every other on every attribute and better on one. It is the only kind that never resolves an incomparability, and it therefore fails to decide far more often than the others. It is specified because it is the correct kind for decisions where an arbitrary resolution is unacceptable, and because almost no engine offers it.

**`PAIRWISE_PREFERENCE`** is the only kind under which a cycle is possible, and the possibility is not hypothetical. A preference relation assembled from several attributes by majority comparison can be intransitive, so that candidate A is preferred to B, B to C and C to A, and no candidate is maximal. The condition is the Condorcet paradox, it is a known result rather than an implementation defect, and section 6.4 requires it to be detected and section 7.2 provides the outcome. Every engine that iterates a preference relation to find a winner resolves a cycle by whichever candidate it happened to start from.

**`AUTHORITY_PRECEDENCE`** is the kind that discharges the obligation `Part 2` clause P2-6.49 creates. That component detects that two rules contradict, reports both with their authorities, and refuses to arbitrate. Something must arbitrate, and the arbitration requires a declared order over authorities: a regulation outranks an internal policy, a contract outranks a guideline, a jurisdiction's law outranks a group standard. Where two authorities are unranked relative to each other, the kind yields incomparability, which is the honest answer and the prompt to rank them.

**`DECLARED_RANDOM`** is admitted deliberately and is better than several alternatives. Where a selection must be made among equally preferred candidates and no principled basis exists, a seeded pseudorandom choice is honest about being arbitrary, is reproducible from the recorded seed, and is defensible in a way that "the first row" is not. It is used for lotteries, sampling and load allocation. Clause P5-3.44 requires the seed to be recorded and the generator to be pinned, without which it is neither reproducible nor auditable.

`criterion_version` fields:

| Field | Type | Required | Cardinality | Absence means |
| --- | --- | --- | --- | --- |
| `criterion_version_id` | `ID` | yes | 1 | n/a |
| `criterion_id` | `ID` | yes | 1 | n/a |
| `kind` | `ENUM` | yes | 1 | n/a. Exactly one member of the table above. |
| `document_citation` | `CITEREF` | yes | 1 | n/a. The `Part 1` version carrying the criterion. |
| `document_locator` | `PATH` | yes | 1 | n/a |
| `statement` | `TEXT` | yes | 1..n | n/a. The criterion in natural language, one per language, one authoritative. |
| `attributes_considered` | `URN` | no | 0..n | The criterion considers only the outcome value. |
| `scale` | `PIN` | no | 0..1 | Required for `SCORE_FUNCTION` and `WEIGHTED_AGGREGATE`. |
| `direction` | `ENUM` | no | 0..1 | Required wherever a scale is present. `MAXIMISE` or `MINIMISE`. |
| `sub_criterion_order` | `ID` | no | 0..n | Required for `LEXICOGRAPHIC`, in declared order. |
| `precedence_order_id` | `ID` | no | 0..1 | Required for `PRECEDENCE_OVER_OUTCOMES` and `AUTHORITY_PRECEDENCE`. |
| `generator_pin` | `PIN` | no | 0..1 | Required for `DECLARED_RANDOM`. |
| `created_ktime` | `KTIME` | yes | 1 | n/a |

The `statement` field is required for the same reason `Part 2` section 3.6 requires one on a rule: the criterion is a policy that people are governed by, and a policy expressed only as a computation is a policy nobody can read. The correspondence between the statement and the computation is not mechanically checkable, and section 13.2 records that this is the third appearance of that limitation in the standard.

**P5-3.38 (MUST) Exactly one kind.** An implementation must record exactly one criterion kind from the table above on every criterion version and must not accept a kind outside the set.

**P5-3.39 (MUST) Statement present and authoritative language designated.** An implementation must hold at least one statement for every criterion version and must designate exactly one language authoritative.

**P5-3.40 (MUST) Kind required fields enforced.** An implementation must refuse a criterion version lacking a field the table above requires for its kind.

**P5-3.41 (MUST) Scale and direction recorded together.** An implementation must record a direction wherever a scale is present and must not default it.

**P5-3.42 (MUST) Attributes considered enumerated.** An implementation must record every candidate attribute the criterion considers and must not read an attribute it has not recorded.

**P5-3.43 (MUST) Sub criterion order declared for lexicographic criteria.** An implementation must record the order of sub criteria for a `LEXICOGRAPHIC` criterion and must apply them in that order.

**P5-3.44 (MUST) Random generator pinned and seed recorded.** An implementation must pin the pseudorandom generator and its version for a `DECLARED_RANDOM` criterion and must record the seed used on every decision, so that the selection is reproducible.

**P5-3.45 (MUST NOT) No hidden comparability.** An implementation must not compare two candidates on an attribute the criterion does not record as considered, and must not supply a rate of exchange between attributes that the criterion does not declare.

**P5-3.46 (MUST) Dominance only never resolves.** An implementation must return the incomparability outcome of section 7.2 for a `DOMINANCE_ONLY` criterion wherever no candidate dominates, and must not fall through to any other basis.

### 3.8 Criterion authority and the justification of parameters

A criterion without an authority is a preference somebody typed. A criterion parameter without a justification is a number of unknown origin, and the number is the policy.

`criterion_authority` fields carry the `criterion_version_id`, a `CITEREF` and a `PATH` locator to the clause relied upon, a `basis` of `REGULATION`, `CONTRACT`, `INTERNAL_POLICY`, `STANDARD`, `MANAGEMENT_DECISION`, `COMMERCIAL_JUDGEMENT` or `UNDECLARED`, an `asserted_by`, and an `interpretation_note`.

`criterion_parameter` fields:

| Field | Type | Required | Cardinality | Absence means |
| --- | --- | --- | --- | --- |
| `parameter_id` | `ID` | yes | 1 | n/a |
| `criterion_version_id` | `ID` | yes | 1 | n/a |
| `name` | `TEXT` | yes | 1 | n/a |
| `value` | `TEXT` | yes | 1 | n/a |
| `scale` | `PIN` | no | 0..1 | The parameter is not on a numeric scale. |
| `role` | `ENUM` | yes | 1 | n/a. One of `WEIGHT`, `THRESHOLD`, `SEED`, `PRECEDENCE_POSITION`, `TOLERANCE`, `AGGREGATOR`, `OTHER`. |
| `justification` | `TEXT` | yes | 1 | n/a |
| `justification_basis` | `ENUM` | yes | 1 | n/a. One of `IN_CITED_CLAUSE`, `DERIVED_FROM_CLAUSE`, `MANAGEMENT_DECISION_CITED`, `EMPIRICAL_STUDY_CITED`, `CONVENTION`, `UNJUSTIFIED`. |
| `justification_citation` | `CITEREF` | no | 0..1 | Required for every basis except `CONVENTION` and `UNJUSTIFIED`. |
| `declared_by` | `ACTOR` | yes | 1 | n/a |

`UNJUSTIFIED` is admissible and countable, on the same basis `Part 2` admits an undeclared rule authority and `Part 3` admits an undeclared method. The alternative to permitting the honest answer is a system in which every weight claims a provenance it does not have. Section 8.5 requires the count, because a criterion whose weights are all unjustified is a criterion nobody can review and the number is the only way anyone finds out.

`CONVENTION` records a parameter set by practice rather than by reasoning, which is extremely common and is different from unjustified: somebody knows why it is what it is, and the reason is that it has always been that.

The `interpretation_note` on the authority carries the same obligation `Part 2` section 3.7 imposes: where a parameter does not appear in the cited clause, the record must say where it came from. A regulation requiring that price be given due weight, implemented as a weight of 0.4, has a 0.4 that is not in the regulation, and recording where the 0.4 came from is the difference between a defensible criterion and a number of unknown origin.

**P5-3.47 (MUST) Authority per criterion version.** An implementation must hold exactly one authority record for every criterion version and must record `UNDECLARED` where none can be identified rather than recording a plausible one.

**P5-3.48 (MUST) Locator to a clause.** An implementation must record a locator identifying the clause relied upon and must not record a citation to a whole document as the authority for a criterion.

**P5-3.49 (MUST) Every parameter justified.** An implementation must record a justification and a justification basis for every criterion parameter and must refuse a criterion version with a parameter lacking either.

**P5-3.50 (MUST) Justification citation where the basis requires it.** An implementation must record a citation for every justification basis other than `CONVENTION` and `UNJUSTIFIED`.

**P5-3.51 (MUST) Interpretation note where a parameter is not in the clause.** An implementation must record an interpretation note wherever a parameter value does not appear in the cited authority clause.

**P5-3.52 (MUST) Unjustified parameters countable.** An implementation must be able to report every parameter of basis `UNJUSTIFIED` or `CONVENTION` by criterion and by decision class, and must include the counts in the signals of section 8.5.

**P5-3.53 (MUST) Authority drift observed.** An implementation must check the resolvability and status of every criterion authority on a declared cycle, must record an observation where the cited version has been superseded, withdrawn or made unresolvable, and must declare the cycle.

**P5-3.54 (MUST NOT) No silent disable on authority drift.** An implementation must continue to apply a criterion whose authority has been superseded or withdrawn, must report the condition with every decision that used it, and must not cease deciding, on the same basis as `Part 2` clause P2-3.10.

**P5-3.55 (MUST) Approval obtained, not asserted.** An implementation must obtain the approval of every criterion version by resolution against `Part 1`, must record the whole resolution outcome envelope, and must return the approval status with every decision that applied it.

### 3.9 Hit policies, and which this part refuses

`Part 2` section 12.5 allocates every hit policy here, on the ground that a hit policy is a conflict resolution criterion. This section specifies them and refuses two of the seven.

DMN 1.5 defines seven hit policies for a decision table, in two groups. The single hit policies are Unique, Any, Priority and First. The multiple hit policies are Collect, with optional aggregators for sum, count, minimum and maximum, Rule order and Output order.

Analysed by what they actually do, the seven are not one kind of thing but three.

**Two are integrity constraints, not criteria.** Unique asserts that at most one rule matches. Any asserts that all matching rules produce the same output. Neither resolves anything: each is a claim about the table that can be checked statically and whose violation is an error. This part treats both as constraints on a decision table rather than as criteria, and clause P5-3.58 requires a violation to be reported as a defect rather than resolved.

**Two are criteria over outcome values, and are admitted.** Priority returns the matching output that comes first in a declared list of output values. Output order returns the matching outputs ordered by that list. In both, the ordering is over **output values**, which DMN itself constrains by requiring that priority tables use enumerated output values. An order over enumerated outcome values is exactly the `PRECEDENCE_OVER_OUTCOMES` criterion of section 3.7: it is writable, approvable, datable and reviewable, and it is independent of the sequence of rules.

**Two are criteria over rule sequence, and are refused.** First returns the first match in rule order. Rule order returns the matching outputs in rule order. In both, the criterion is the physical sequence of rows in a table. That sequence is not a governed artifact: it has no authority, no statement, no justification and no version independent of the table's layout, it changes when somebody inserts a row for readability, and the change alters the decisions the organisation makes with no record that a policy changed. Clause P5-3.59 refuses both.

**One is not a selection at all.** Collect returns every matching output, optionally aggregated. Returning a set is not choosing from it, and aggregating is computing a value from the set rather than selecting a member of it. This part treats Collect as an aggregation and specifies it in section 3.10, separately from selection, because a decision that returns three outcomes has not decided and a decision that returns their sum has produced a new outcome that was not a candidate.

The refusal of First and Rule order is a divergence from DMN and it will be resisted, because First is the most used hit policy in practice and because a table with an ordered fall through is genuinely easy to read. The remedy this part offers is that the same table be expressed with an explicit precedence over its outcome values, which is very nearly as easy to read and is a policy somebody can approve. Section 13.3 records the divergence, its cost and the argument against it.

`hit policy` is recorded on a decision table as a criterion of the corresponding kind, not as a hit policy. Clause P5-3.60 requires the mapping.

**P5-3.56 (MUST) Hit policies expressed as criteria.** An implementation must express every hit policy as a criterion of a kind in section 3.7 and must not hold a hit policy as a property of a table that is not a criterion version.

**P5-3.57 (MUST) Unique and Any are constraints.** An implementation must treat a Unique or Any hit policy as a constraint on the decision table, must check it, and must not treat it as a means of selecting among matching rules.

**P5-3.58 (MUST) Constraint violation is a defect.** An implementation must return the defect outcome of section 7.5 where more than one rule matches under Unique, or where matching rules produce different outputs under Any, and must not select among them.

**P5-3.59 (MUST NOT) No selection by rule sequence.** An implementation must not admit a criterion whose effect is to select by the sequence of rules or rows in a table, and must not implement a First or Rule order hit policy.

**P5-3.60 (MUST) Precedence over outcomes recorded as an artifact.** An implementation must record the precedence order used by a Priority or Output order policy as a `precedence_order` artifact with its own authority and approval, and must not derive it from the layout of a table.

**P5-3.61 (MUST) Enumerated outcomes required for a precedence criterion.** An implementation must require the outcome values of a `PRECEDENCE_OVER_OUTCOMES` criterion to be an enumerated set bound to a `Part 10` value set version, so that the order is over a governed domain.

**P5-3.62 (MUST NOT) No else rule as a criterion.** An implementation must record a table's fall through outcome as a `default_declaration` under section 3.11, with its own authority, and must not treat it as a rule or as a position in a precedence order.

### 3.10 Collection and aggregation

A collecting policy returns every eligible candidate rather than one, optionally aggregated. Both are legitimate and neither is a selection, and the distinction matters because a caller that receives an aggregate has received a computed value that was not among the candidates.

`decision_definition_version` may declare a `collection_mode` of `SELECT_ONE`, `RETURN_ALL` or `AGGREGATE`, with a registered aggregator where the mode is `AGGREGATE`. Where the mode is not `SELECT_ONE`, the criterion is used to order rather than to choose, and the outcome is a list or a value rather than a candidate.

Two requirements follow and both are about honesty of the record.

An aggregate outcome is **not a candidate** and must not be recorded as one. A sum of three candidates' values is a fourth value that nobody offered, and recording it as the selected candidate makes the decision record false. Clause P5-3.64 requires it to be recorded as a derived outcome with the contributing candidates enumerated.

A `RETURN_ALL` outcome is **not a decision** in the sense of section 1.3, because nothing was chosen. It is recorded as an outcome of its own class in section 7.2 and clause P5-3.65 forbids presenting it as a selection.

**P5-3.63 (MUST) Collection mode declared.** An implementation must record a collection mode on every decision definition version and must not default it to anything other than `SELECT_ONE`.

**P5-3.64 (MUST) Aggregate recorded as derived.** An implementation must record an aggregate outcome as a derived value with its aggregator, its scale and every contributing candidate enumerated, and must not record it as a selected candidate.

**P5-3.65 (MUST NOT) No collection as selection.** An implementation must not present a `RETURN_ALL` or `AGGREGATE` outcome as a selection and must return the corresponding outcome member of section 7.2.

**P5-3.66 (MUST) Aggregator registered.** An implementation must record a registered aggregator for every `AGGREGATE` mode and must not accept an unregistered one.

**P5-3.67 (MUST) Aggregation over a declared scale.** An implementation must refuse an aggregation over values whose scale does not declare the aggregation to be defined, so that a sum over an ordinal scale is refused rather than computed.

### 3.11 Tiebreaks and defaults

A tiebreak and a default are the two artifacts that turn a criterion that did not determine an answer into an answer. Both are policy, both are optional, and both must be as governed as the criterion they supplement.

`tiebreak_declaration` carries a `criterion_version_id` for the tiebreak itself, which is a criterion version subject to every requirement of sections 3.7 and 3.8, together with the `applies_to` condition stating which of the three failures to determine it applies to: `TIE`, `INCOMPARABILITY`, `INTRANSITIVITY`, or a combination.

That last field is the point of the entity. A tiebreak declared for ties does not resolve an incomparability, and an implementation that applies it to one has silently supplied a rate of exchange the criterion refused to supply. Clause P5-3.70 forbids it.

A tiebreak of kind `DECLARED_RANDOM` is admissible and is often the right answer for a genuine tie. A tiebreak of kind `PRECEDENCE_OVER_OUTCOMES` is admissible. A tiebreak that selects by source ordinal is refused by clause P5-3.26.

`default_declaration` carries the default `outcome_value`, its `authority`, its `justification`, a `declared_by`, and an `applies_to` condition of `NO_CANDIDATE`, `NO_ELIGIBLE_CANDIDATE`, `NO_CANDIDATE_SELECTED`, or a combination.

The `applies_to` field on a default matters as much as on a tiebreak, and for the same reason. A default declared for the case where no candidate was eligible is a different policy from one declared for the case where no candidate was supplied at all. The first says what to do when nobody qualified; the second says what to do when the enumeration returned nothing, which is frequently a defect rather than a state of the world. Applying one default to both conceals the defect.

**P5-3.68 (MUST) Tiebreak is a criterion version.** An implementation must record a tiebreak as a criterion version subject to every requirement of sections 3.7 and 3.8.

**P5-3.69 (MUST) Tiebreak applicability declared.** An implementation must record which of tie, incomparability and intransitivity a tiebreak applies to and must not default the value.

**P5-3.70 (MUST NOT) No tiebreak beyond its declared applicability.** An implementation must not apply a tiebreak to a failure to determine that its declaration does not name, and must return the corresponding outcome of section 7.2.

**P5-3.71 (MUST) Default authorised and justified.** An implementation must record an authority, a justification and a declaring actor for every default declaration.

**P5-3.72 (MUST) Default applicability declared.** An implementation must record which of the empty cases a default applies to and must not apply it to a case its declaration does not name.

**P5-3.73 (MUST) Basis of selection recorded.** An implementation must record whether an outcome was produced by the criterion, by a tiebreak or by a default, and must not present a defaulted or tiebroken outcome as one the criterion determined.

**P5-3.74 (MUST NOT) No default as a candidate.** An implementation must record a defaulted outcome as a default rather than as a selected candidate, and must record that no candidate was selected.
### 3.12 The decision request and pins

A decision is reproducible only if everything it depended on is recorded with enough precision to obtain it again. The pin set is part of the result rather than diagnostic metadata, on the same basis as `Part 2` section 3.14.

`decision_request` fields:

| Field | Type | Required | Cardinality | Absence means |
| --- | --- | --- | --- | --- |
| `request_id` | `ID` | yes | 1 | n/a |
| `definition_reference` | `ID` | yes | 1 | n/a. A definition version or lineage. |
| `definition_binding_mode` | `ENUM` | yes | 1 | n/a. `PINNED_VERSION` or `AS_OF_LINEAGE`. |
| `decision_instant` | `ATIME` | yes | 1 | n/a. Never defaulted; see clause P5-3.76. |
| `knowledge_instant` | `KTIME` | no | 0..1 | Resolve against present belief. Where present, resolve against belief as at that instant. |
| `subject_reference` | `URN` | no | 0..1 | The decision is not about an identified subject. |
| `candidates_supplied` | `ID` | no | 0..n | Candidates are to be obtained from the declared source. |
| `attributes_pin` | `PIN` | no | 0..1 | Candidate attributes are carried on the candidates. |
| `requested_by` | `ACTOR` | yes | 1 | n/a |
| `authorisation` | `AUTHREF` | no | 0..1 | The decision was not the subject of an authorisation decision. |
| `purpose` | `ENUM` | yes | 1 | n/a. Registered under section 9.6. |
| `received_ktime` | `KTIME` | yes | 1 | n/a |

`decision_pin` records one artifact the run depended on, with a `kind` from the enumeration `DEFINITION_VERSION`, `CRITERION_VERSION`, `PRECEDENCE_ORDER`, `TIEBREAK_VERSION`, `DEFAULT_DECLARATION`, `ELIGIBILITY_RULE_SET_VERSION`, `ELIGIBILITY_REPORT`, `CANDIDATE_SOURCE`, `REFERENCE_SET`, `CONCEPT_DEFINITION`, `SCALE`, `MODEL_OUTPUT`, `RANDOM_SEED` and `AGGREGATOR`.

The `decision_instant` is required rather than defaulted, on the same ground `Part 2` clause P2-3.83 gives. A criterion resolved as of the present, in a request that did not say so, produces a decision that cannot be distinguished from a decision about a past state, and the distinction matters most in exactly the cases where somebody is asking years later.

`ELIGIBILITY_REPORT` is a pin kind of its own because the report is large and the temptation to record a summary is strong. `Part 2` clause P2-12.6 requires the whole report, and pinning it as an artifact rather than embedding a reduced form is how that requirement is met without making every decision record unmanageable.

**P5-3.75 (MUST) Pin set complete.** An implementation must record a pin for every artifact its decision read and must record a pin of every kind in the enumeration above that applied.

**P5-3.76 (MUST) Decision instant supplied.** An implementation must require a `decision_instant` in every request and must not default it to the time of the request.

**P5-3.77 (MUST) Knowledge instant behaviour declared.** An implementation must declare its behaviour where `knowledge_instant` is absent and must record the instant it used.

**P5-3.78 (MUST) Purpose recorded.** An implementation must record the declared purpose of every decision and must not permit an unregistered purpose.

**P5-3.79 (MUST NOT) No unpinned dependency.** An implementation must not complete a decision that read an artifact for which it could not record a pin, and must return the appropriate outcome of section 7.4 instead.

**P5-3.80 (MUST NOT) No pin substitution.** An implementation must not substitute a later version of a pinned artifact and must not treat a compatible successor as the pinned artifact.

**P5-3.81 (MUST) Eligibility report pinned whole.** An implementation must pin the whole `Part 2` evaluation report for every candidate and must not record a reduced form in its place.

### 3.13 The decision record

`selection` fields:

| Field | Type | Required | Cardinality | Absence means |
| --- | --- | --- | --- | --- |
| `selection_id` | `ID` | yes | 1 | n/a |
| `run_id` | `ID` | yes | 1 | n/a |
| `outcome` | `ENUM` | yes | 1 | n/a. A member of the closed set of section 7.2. |
| `selected_candidate_id` | `ID` | no | 0..1 | No candidate was selected. Required for every deciding outcome. |
| `outcome_value` | `TEXT` | no | 0..1 | No outcome value. Required for every deciding and defaulted outcome. |
| `basis` | `ENUM` | yes | 1 | n/a. One of `CRITERION`, `TIEBREAK`, `DEFAULT`, `EXTERNAL`, `NONE`. |
| `criterion_version_id` | `ID` | yes | 1 | n/a. Recorded even where the basis was a default. |
| `tiebreak_id` | `ID` | no | 0..1 | No tiebreak was applied. |
| `default_id` | `ID` | no | 0..1 | No default was applied. |
| `candidates_considered` | `COUNT` | yes | 1 | n/a. Grain: one `candidate`. |
| `candidates_eligible` | `COUNT` | yes | 1 | n/a. Grain: one candidate with an eligibility verdict of satisfied. |
| `candidates_indeterminate` | `COUNT` | yes | 1 | n/a. Grain: one candidate whose eligibility was indeterminate. |
| `margin` | `TEXT` | no | 0..1 | No margin is definable for the criterion kind, or the outcome was not a selection. |
| `margin_scale` | `PIN` | no | 0..1 | Required wherever a margin is present. |
| `marginal` | `TRUTH` | yes | 1 | n/a |
| `criterion_approval_status` | `ENUM` | yes | 1 | n/a. From the `Part 1` resolution. |
| `authority_status` | `ENUM` | yes | 1 | n/a. One of `IN_FORCE`, `SUPERSEDED`, `WITHDRAWN`, `UNRESOLVABLE`, `NOT_CHECKED`. |
| `solely_automated` | `TRUTH` | yes | 1 | n/a |
| `set_completeness` | `ENUM` | yes | 1 | n/a. Copied from the candidate set. |
| `decided_ktime` | `KTIME` | yes | 1 | n/a |

The `criterion_version_id` is recorded even where the basis was a default, because knowing which criterion failed to select is as informative as knowing which one selected. A decision record that omits the criterion when a default fired conceals whether the criterion was inapplicable or whether nothing was eligible.

The three counts are recorded separately and derived rather than accepted, and the third is the one nobody records. A decision among five candidates of which three were eligible and two were indeterminate is a materially different decision from one among five of which three were eligible and two were ineligible, and the counts are the only place the difference is visible at a glance.

**P5-3.82 (MUST) Outcome from the closed set.** An implementation must record exactly one outcome member from section 7.2 on every selection.

**P5-3.83 (MUST) Basis recorded and never collapsed.** An implementation must record the basis of every selection and must not present a tiebroken or defaulted outcome as one the criterion determined.

**P5-3.84 (MUST) Criterion recorded regardless of basis.** An implementation must record the criterion version applied even where the outcome was produced by a tiebreak or a default.

**P5-3.85 (MUST) Counts derived with grain.** An implementation must derive the candidate counts from the candidates recorded, must state the grain of each, and must record the indeterminate count separately.

**P5-3.86 (MUST) Approval and authority status carried.** An implementation must record the criterion's approval status and authority status with every selection and must record `NOT_CHECKED` where the drift check of clause P5-3.53 was not current rather than recording `IN_FORCE`.

**P5-3.87 (MUST) Set completeness carried.** An implementation must copy the candidate set's completeness onto the selection, so that a reader of the outcome is told whether the enumeration was complete.

**P5-3.88 (MUST NOT) No selection without a candidate.** An implementation must not record a `selected_candidate_id` for an outcome that was defaulted, and must not record a defaulted outcome without a `default_id`.

### 3.14 Margin and marginality

A decision decided by a hundredth of a point on a weighted score and a decision decided by dominance are recorded identically in every system in ordinary use, and they are entirely different facts. The first would have gone the other way had any weight been slightly different, any input slightly different, or any rounding rule slightly different. The second would not.

The margin is the extent by which the selected candidate was preferred to the next best, in the terms of the criterion that selected it. Its form differs by criterion kind and the table is normative.

| Criterion kind | Margin |
| --- | --- |
| `PRECEDENCE_OVER_OUTCOMES` | The number of positions in the precedence order between the selected outcome value and the next best present. |
| `SCORE_FUNCTION` | The difference in score, on the criterion's scale. |
| `LEXICOGRAPHIC` | The ordinal of the sub criterion that separated the candidates, and the margin at that sub criterion. |
| `WEIGHTED_AGGREGATE` | The difference in aggregate, on the criterion's scale, together with the smallest single weight perturbation that would reverse the outcome where the implementation can compute it. |
| `DOMINANCE_ONLY` | The number of attributes on which the selected candidate strictly dominated, of those considered. |
| `PAIRWISE_PREFERENCE` | The number of pairwise comparisons the selected candidate won, of those in which it participated. |
| `AUTHORITY_PRECEDENCE` | The number of positions in the authority order between the selected candidate's authority and the next. |
| `EXTERNAL_DETERMINATION` | No margin is definable. |
| `DECLARED_RANDOM` | No margin is definable. |

The weight perturbation for `WEIGHTED_AGGREGATE` is the most useful single figure this part specifies and is the one implementations will most want to omit. It answers the question a reviewer of a weighted decision actually has: how sensitive was this to the weights nobody can justify. Clause P5-3.91 requires it where computable and requires the incapacity to be recorded where not.

A decision is **marginal** where the margin falls within the threshold declared on the decision definition. Marginality is recorded on the decision, is separately countable, and is not a defect: a close decision correctly taken is still correct. What it is, is a decision whose review is worth more than the review of a decisive one, and an organisation that cannot enumerate its marginal decisions cannot direct review anywhere useful.

**P5-3.89 (MUST) Margin computed per kind.** An implementation must compute the margin of every selection in the form the table above specifies for the criterion kind that produced it.

**P5-3.90 (MUST) Margin scale recorded.** An implementation must record the scale of every margin and must not record a margin without one.

**P5-3.91 (MUST) Weight sensitivity recorded or its absence stated.** An implementation must record, for every selection by a `WEIGHTED_AGGREGATE` criterion, the smallest single weight perturbation that would reverse the outcome, or must record that it could not compute it and why.

**P5-3.92 (MUST) No margin definable is recorded as such.** An implementation must record that no margin is definable where the criterion kind admits none, and must not record a margin of zero in its place.

**P5-3.93 (MUST) Marginality derived from the declared threshold.** An implementation must derive the marginality flag from the recorded margin and the threshold declared on the decision definition, and must not accept the flag as an input.

**P5-3.94 (MUST) Marginal decisions countable.** An implementation must be able to report every marginal decision by definition, criterion and outcome, and must include the count in the signals of section 8.5.

**P5-3.95 (MUST NOT) No marginality as a defect.** An implementation must not represent a marginal decision as erroneous, invalid or requiring reversal, and must represent it as a decision whose margin fell within the declared threshold.

### 3.15 Elimination grounds

`Part 3` clause P3-3.63 refuses a determination that reports a selection with no alternatives, and `Part 3` section 3.10 enumerates the grounds on which an alternative may have been eliminated. This section supplies them.

`elimination` fields carry the `candidate_id`, the `run_id`, a `ground` from the closed set below, the identity of the eligibility verdict or comparison that eliminated the candidate where one did, and the `eliminated_ktime`.

Eight grounds. The table is normative and maps onto the enumeration `Part 3` requires.

| Ground | Means | Maps to Part 3 ground |
| --- | --- | --- |
| `INELIGIBLE` | An eligibility verdict of violated or contradicted. | `CONSTRAINT_VIOLATION` |
| `ELIGIBILITY_INDETERMINATE_EXCLUDED` | Eligibility could not be established and the declared treatment excluded the candidate. | `NOT_EVALUABLE` |
| `NOT_PREFERRED` | Eligible, and the criterion preferred another candidate. | `CRITERION` |
| `NOT_PREFERRED_BY_TIEBREAK` | Eligible and tied, and the tiebreak preferred another. | `CRITERION` |
| `DOMINATED` | Eligible, and another candidate dominated it on every attribute considered. | `CRITERION` |
| `OUT_OF_SCOPE_OF_CRITERION` | The criterion does not consider the candidate, for example an outcome value absent from the precedence order. | `INELIGIBILITY` |
| `WITHDRAWN` | The candidate was withdrawn by its proposer before selection. | `WITHDRAWN_BY_PROPOSER` |
| `NOT_COMPARED` | The candidate was never compared, because a bound was reached or the run terminated. | `UNRECORDED` |

Two of the eight carry the weight.

`ELIGIBILITY_INDETERMINATE_EXCLUDED` is the ground that makes the treatment of section 3.6 visible in the record. Without it, a candidate excluded for want of information is indistinguishable from one excluded for failing a rule, and the person the decision was about is told they did not qualify when in fact nobody could tell.

`OUT_OF_SCOPE_OF_CRITERION` records the case where an eligible candidate simply is not addressed by the criterion: its outcome value is not in the precedence order, or it lacks an attribute the score function requires. That is a defect in the criterion rather than a fact about the candidate, and clause P5-3.100 requires it to be reported as such and counted, because a criterion that silently cannot see a class of candidate will exclude that class forever.

**P5-3.96 (MUST) Ground on every unselected candidate.** An implementation must record exactly one elimination ground for every candidate not selected.

**P5-3.97 (MUST) Eliminating artifact linked.** An implementation must link the eligibility verdict or the comparison that eliminated a candidate wherever one did.

**P5-3.98 (MUST) Indeterminate exclusion distinguished.** An implementation must record `ELIGIBILITY_INDETERMINATE_EXCLUDED` where a candidate was excluded for an indeterminate verdict and must not record `INELIGIBLE`.

**P5-3.99 (MUST) Mapping to Part 3 recorded.** An implementation must supply, with every decision reported to `Part 3`, the ground of each eliminated candidate in the enumeration `Part 3` section 3.10 requires, per the mapping above.

**P5-3.100 (MUST) Out of scope candidates reported as a criterion defect.** An implementation must record a candidate eliminated as `OUT_OF_SCOPE_OF_CRITERION`, must emit the corresponding event, and must include the count in the signals of section 8.5.

**P5-3.101 (MUST NOT) No unrecorded elimination.** An implementation must not omit an elimination record for a candidate on the ground that it was obviously worse, and must record `NOT_COMPARED` where no comparison was performed.

### 3.16 Human decisions, and decisive automation

A component that records only mechanised decisions covers a fraction of the decisions an organisation makes and misses every one that matters most. This section brings human and hybrid decisions into the model, and it draws one distinction that no engine in ordinary use draws.

`human_involvement` fields carry the `run_id`, the `actor`, an `involvement` from `MADE_THE_DECISION`, `REVIEWED_AND_ACCEPTED`, `REVIEWED_AND_OVERRODE`, `CONSULTED`, `RECORDED_ONLY`, a `basis_narrative`, the `authorisation`, and the `occurred_otime`.

`RECORDED_ONLY` is the honest member for the person who pressed the button. It records participation without asserting judgement, and it exists because recording that person as having made the decision is a false statement that will be relied upon.

**Decisive automation.** Where a natural person nominally made a decision and the outcome was decisively based on a mechanism's output, the decision is in substance automated even though a person was in the loop. The test is not whether a person participated but whether the outcome would have differed had the mechanism said something else. The Court of Justice of the European Union applied this criterion in Case C-634/21, holding that the question is whether the final decision was decisively based on the preceding automated determination, even where the person had formal and substantive decision making power.

The consequence for this part is that `solely_automated` on a selection is not sufficient. A separate assessment is required, and it is an assessment rather than a computation, because whether a reviewer's acceptance was meaningful is a judgement.

`decisive_automation_assessment` fields:

| Field | Type | Required | Cardinality | Absence means |
| --- | --- | --- | --- | --- |
| `assessment_id` | `ID` | yes | 1 | n/a |
| `run_id` | `ID` | yes | 1 | n/a |
| `assessment` | `ENUM` | yes | 1 | n/a. One of `NOT_AUTOMATED`, `AUTOMATED_WITH_MEANINGFUL_REVIEW`, `DECISIVELY_AUTOMATED`, `SOLELY_AUTOMATED`, `UNASSESSED`. |
| `basis` | `ENUM` | yes | 1 | n/a. One of `DERIVED_FROM_INVOLVEMENT`, `ASSESSED_BY_ACTOR`, `SAMPLED_REVIEW`, `RATE_INFERRED`. |
| `override_rate` | `TEXT` | no | 0..1 | No override rate was computed for the reviewer or the class. |
| `assessed_by` | `ACTOR` | no | 0..1 | The assessment is `UNASSESSED` or was derived. |
| `assessed_ktime` | `KTIME` | no | 0..1 | As above. |

`RATE_INFERRED` is the basis worth noting. A reviewer who has accepted the mechanism's output on every one of four hundred consecutive decisions is providing formal rather than meaningful review, and the override rate is the only evidence available at scale. It is not proof, and clause P5-3.106 requires it to be recorded as an inference rather than a finding.

`UNASSESSED` is the default and is honest. Nothing in this component can establish whether a reviewer's acceptance was meaningful, and section 8.5 requires the count of unassessed decisions about natural persons, because that count is the measure of the organisation's exposure under the regimes section 10.5 records.

**P5-3.102 (MUST) Involvement recorded per person.** An implementation must record every natural person's involvement in a decision with its kind and the occurrence time.

**P5-3.103 (MUST) Recorded only distinguished from making.** An implementation must record `RECORDED_ONLY` where a person effected a decision without exercising judgement on the outcome and must not record them as having made it.

**P5-3.104 (MUST) Solely automated derived.** An implementation must derive `solely_automated` from the recorded involvements and must not accept it as an input.

**P5-3.105 (MUST) Decisive automation assessed separately.** An implementation must hold a decisive automation assessment separate from the record of human involvement, must default it to `UNASSESSED`, and must not derive `AUTOMATED_WITH_MEANINGFUL_REVIEW` from the presence of a review.

**P5-3.106 (MUST) Rate inference marked as inference.** An implementation must record an assessment of basis `RATE_INFERRED` as an inference and must record the rate and the population from which it was computed.

**P5-3.107 (MUST) Override rate computable per reviewer and class.** An implementation must be able to report the proportion of decisions in which a reviewer overrode the mechanism's outcome, by reviewer and by decision class.

**P5-3.108 (MUST) Unassessed decisions about persons countable.** An implementation must be able to report every decision whose definition declares a natural person subject and whose decisive automation assessment is `UNASSESSED`, and must include the count in the signals of section 8.5.

**P5-3.109 (MUST) Override recorded with its own basis.** An implementation must record an override as a departure from the outcome the criterion produced, with the overriding actor, the authorisation, the reason, and both the criterion's outcome and the outcome recorded.

**P5-3.110 (MUST NOT) No override without the original.** An implementation must retain the outcome the criterion produced alongside any override and must not replace it.

**P5-3.111 (MUST NOT) No inference of meaningful review.** An implementation must not assert that a review was meaningful, and must record such an assessment only where a named actor made it.
### 3.17 Projections

Every read is a projection: a pure function of the recorded rows, holding no state of its own, recomputable at any time.

| Projection | Yields |
| --- | --- |
| `decision_of` | One decision with its candidates, eligibility verdicts, comparisons, selection, basis, margin and pins. |
| `criterion_at` | The criterion version in force for a definition at an application time and a knowledge time, with its approval and authority status. |
| `definition_at` | The decision definition version in force at an application time and a knowledge time. |
| `candidates_of` | Every candidate of a decision with its eligibility verdict and elimination ground. |
| `eliminations_by_ground` | Eliminations grouped by ground, so that exclusions for want of information are separable from exclusions for failing a rule. |
| `basis_distribution` | Decisions by basis of selection, by definition and by criterion version. |
| `marginal_decisions` | Every decision whose margin fell within the declared threshold. |
| `weight_sensitivity` | For weighted criteria, the perturbation that would reverse each decision, and those with none computed. |
| `undecidable_decisions` | Every decision returning a tie, intransitivity or incomparability outcome, by kind. |
| `indeterminate_eligibility_handling` | Decisions in which an indeterminate eligibility verdict was treated, by treatment and by `Part 2` subclass. |
| `unjustified_parameters` | Every criterion parameter of basis `UNJUSTIFIED` or `CONVENTION`. |
| `unapproved_criteria` | Every criterion version whose approval status is not approved. |
| `criterion_authority_drift` | Every criterion whose cited authority has been superseded, withdrawn or made unresolvable. |
| `out_of_scope_candidates` | Candidates eliminated as outside the criterion's scope, by criterion. |
| `incomplete_candidate_sets` | Decisions over candidate sets declared incomplete, by source kind. |
| `override_history` | Every override, with the criterion outcome, the recorded outcome, the actor and the reason. |
| `override_rate` | The proportion of decisions overridden, by reviewer, by definition and over time. |
| `automation_assessment` | Decisions by decisive automation assessment, restricted to natural person subjects. |
| `decision_divergence` | Where re decision of a recorded run under present pins yields a different outcome. |
| `criterion_analysis_state` | Static analysis results per criterion version, with those not analysed. |

`eliminations_by_ground` and `basis_distribution` are the two projections an organisation should read regularly and almost never has. The first separates the candidates that failed a rule from those nobody could assess, which is the difference between a policy working and a data supply failing. The second shows how often the criterion actually determined an answer, and a definition whose decisions are mostly defaulted has a criterion that does not fit the candidates it receives.

`decision_divergence` is specified for the same reason `Part 2` specifies `verdict_divergence`: a decision that would come out differently today, from the same pins, indicates that a pin has decayed or that the implementation has changed under the record.

**P5-3.112 (MUST) Projections are pure.** An implementation must compute every projection as a function of recorded rows alone, holding no state not derivable from them.

**P5-3.113 (MUST) Projection recomputable.** An implementation must be able to recompute every projection from the recorded rows and to demonstrate agreement between a served projection and a recomputation.

**P5-3.114 (MUST) Named projections available.** An implementation must provide every projection in the table above and must name each as named there in any interface it exposes.

**P5-3.115 (MUST) Basis distribution available.** An implementation must provide `basis_distribution`, since the proportion of decisions determined by the criterion rather than by a default or a tiebreak is the measure of whether the criterion fits.

**P5-3.116 (MUST) Divergence projection.** An implementation must provide `decision_divergence` and must be able to report, for any recorded run, whether re decision under present pins yields the same outcome.

**P5-3.117 (MUST NOT) No writes through a projection.** An implementation must not permit any state change to be effected by writing to a projection.

### 3.18 Worked demonstration

The demonstration follows one decision definition across seven years. It is not normative. It exists because the field tables do not show whether the model catches the failures it was built for.

**2027, the definition.** A decision definition `D` governs the selection of a servicing supplier for a claim. Its class is registered, its subject is not a natural person, its candidate source is `EXTERNAL_SOLICITATION` and is therefore recorded as never complete. Its eligibility binding is a `Part 2` rule set version `RSV7` with eleven rules. Its indeterminate treatment is `TREAT_BY_SUBCLASS`: decline to decide on `COMPONENT_DEFECT` and `DEPENDENCY_INDETERMINACY`, exclude on `SUBJECT_INDETERMINACY`, decline on the remaining two, with an authority and a justification recorded. Its criterion is version `CV1` of kind `WEIGHTED_AGGREGATE` over three attributes, with weights 0.5 on price, 0.3 on turnaround and 0.2 on quality score, on a declared scale, direction `MINIMISE` for price and `MAXIMISE` for the others. A tiebreak of kind `DECLARED_RANDOM` applies to `TIE` only. No default is declared. The marginality threshold is 2 per cent of the aggregate scale.

Each weight carries a justification. The 0.5 on price cites a management decision of 2026 recorded as a document version; the 0.3 and 0.2 carry basis `CONVENTION`, with the note that they were carried over from a predecessor process. Two of three weights are therefore, honestly, conventional, and the projection `unjustified_parameters` reports them from the day the criterion is recorded.

**2028, an ordinary decision.** Four bids arrive. `Part 2` returns four evaluation reports: two satisfied, one violated on a rule about insurance cover, and one indeterminate with subclass `SUBJECT_INDETERMINACY` and code `SUBJECT_PATH_WITHHELD`, because the bidder's financial disclosure was withheld.

| Candidate | Eligibility | Ground | Aggregate |
| --- | --- | --- | --- |
| B1 | satisfied | `NOT_PREFERRED` | 0.71 |
| B2 | satisfied | selected | 0.74 |
| B3 | violated | `INELIGIBLE` | not computed |
| B4 | indeterminate, `SUBJECT_INDETERMINACY` | `ELIGIBILITY_INDETERMINATE_EXCLUDED` | not computed |

The outcome is a selection of B2, basis `CRITERION`, margin 0.03 on the aggregate scale, marginality false since 0.03 exceeds the 2 per cent threshold. The weight sensitivity is computed: a reduction of the price weight from 0.5 to 0.46 would reverse the outcome in favour of B1. Candidates considered 4, eligible 2, indeterminate 1. Set completeness `INCOMPLETE`, basis `EXTERNAL_SOLICITATION`.

Four facts in that record are absent from every equivalent record in ordinary use. That B4 was excluded because nobody could assess it rather than because it failed. That the decision turned on a weight two thirds of which is conventional. That a four per cent shift in one weight reverses it. And that the candidate set was never the market.

**2029, the tie.** Two bids produce identical aggregates to the scale's declared precision. The criterion does not determine an answer. The tiebreak applies, because its declaration names `TIE`, and it is `DECLARED_RANDOM` with the generator pinned and the seed recorded. The outcome is a selection with basis `TIEBREAK`, and it is reproducible: re running the decision from the recorded seed selects the same bid. Had no tiebreak been declared, clause P5-3.16 would have required the undecidable outcome of section 7.2 and the decision would have gone to a person.

**2030, the incomparability that was not reported.** A revised criterion `CV2` is proposed, of kind `DOMINANCE_ONLY`, on the ground that the weights cannot be justified. Under it, the 2028 decision would have returned an incomparability: B1 was better on price, B2 better on turnaround, neither dominated. The proposal is rejected on the ground that too many decisions would fail to determine, and `CV1` is retained with a recorded decision to that effect.

This is worth recording because it is the trade the part exists to make visible. `DOMINANCE_ONLY` is more honest and decides less often. The organisation chose the weights over the honesty, deliberately, with a record. That is a legitimate choice and it is a different thing from never having been offered it.

**2031, the authority drift.** The management decision document that justified the 0.5 price weight is superseded by a version that states a different intent. The drift check of clause P5-3.53 resolves the citation, finds the cited version superseded, and appends an observation. Every decision from that date carries `authority_status` of `SUPERSEDED`. Decisions continue, per clause P5-3.54, because ceasing to decide would change what the organisation does on the strength of a lookup failure. The observation stands open and is countable.

**2032, the review that was not a review.** A control is added requiring a person to approve every supplier selection. Over eleven months the reviewer accepts the criterion's outcome on 380 of 381 decisions. The override rate projection reports 0.26 per cent. A decisive automation assessment of basis `RATE_INFERRED` records `DECISIVELY_AUTOMATED` for the class, marked as an inference. The control exists, the record does not pretend it is meaningful review, and section 10.5 records why that distinction has consequences where the subject is a natural person, which here it is not.

**2034, the question.** An investigation asks the following.

| Question | Projection | Result |
| --- | --- | --- |
| Why was B2 chosen in 2028? | `decision_of` | Four candidates, two eligible, `CV1`, aggregate 0.74 against 0.71, basis `CRITERION`, margin 0.03 |
| Would it have gone the other way easily? | `weight_sensitivity` | Yes. A shift of 0.04 in the price weight reverses it. |
| Was B4 rejected or unassessable? | `eliminations_by_ground` | Unassessable. Financial disclosure withheld, subclass recorded. |
| Was the criterion approved and its authority in force? | `decision_of` | Approved. Authority in force at the decision instant, superseded from 2031. |
| How often did the criterion actually decide? | `basis_distribution` | Criterion in most cases, tiebreak in a recorded minority, default never, since none was declared. |
| Was the market considered? | `incomplete_candidate_sets` | No. Every set of this class is `EXTERNAL_SOLICITATION` and recorded incomplete. |
| Was the 2032 control meaningful? | `override_rate`, `automation_assessment` | 0.26 per cent override. Assessed `DECISIVELY_AUTOMATED` on an inferred basis. |
| Which weights can be justified? | `unjustified_parameters` | One of three. The other two are conventional, and have been since 2027. |
| Would the same decision be reached today? | `decision_divergence` | The pins resolve and the outcome reproduces. The current criterion is `CV1` still, so the question and the answer coincide. |

The last three rows are the ones no ordinary decision record can produce, and the eighth is the one an organisation would least like to be asked and most needs to know.

**P5-3.118 (MUST) Demonstration satisfiable.** An implementation must be able to answer every question in the table above for any decision within its retained history, using only the projections of section 3.17.
## 4. Interfaces

### 4.1 Interface principles

Operations are specified by their obligations rather than their signatures. No transport, encoding or naming convention is specified.

Operations divide into three groups and the division is enforced: those that record definitions and criteria, those that decide, and those that read. The deciding group never records a criterion, because a decision that can change the criterion it is applying has no criterion.

**P5-4.1 (MUST) Operation classes separated.** An implementation must not provide an operation that both records a criterion version and performs a decision.

**P5-4.2 (MUST) Refusal is an outcome.** An implementation must return a refusal outcome of section 7.5 for any operation it declines and must not return an outcome of another class in its place.

**P5-4.3 (MUST) Idempotence key accepted.** An implementation must accept a caller supplied idempotence key on every recording and deciding operation and must honour it per section 6.5.

**P5-4.4 (MUST NOT) No partial recording.** An implementation must record a criterion version together with its statements, parameters, authority and required kind fields, or record none of them.

### 4.2 Recording operations

| # | Operation | Records | Principal refusals |
| --- | --- | --- | --- |
| 1 | Register a decision definition | `decision_definition` | Duplicate identity; unregistered class |
| 2 | Record a decision definition version | `decision_definition_version`, `candidate_source_declaration`, `eligibility_rule_set_binding`, `indeterminate_treatment` | No document citation; eligibility binding with no indeterminate treatment; unregistered candidate source kind; no outcome concept; natural person subject undeclared; collection mode undeclared |
| 3 | Register a criterion | `criterion` | Duplicate identity |
| 4 | Record a criterion version | `criterion_version`, `criterion_parameter`, `criterion_authority` | Kind outside the closed set; a field the kind requires absent; a parameter with no justification or basis; a justification basis requiring a citation with none; no statement; two authoritative languages; a criterion whose effect is selection by rule sequence; a precedence criterion over non enumerated outcomes |
| 5 | Record a precedence order | `precedence_order` | Order over rules rather than outcome values; unbound to a `Part 10` value set version where the kind requires it |
| 6 | Declare a tiebreak | `tiebreak_declaration` | Tiebreak that is not a criterion version; applicability undeclared; a tiebreak selecting by source ordinal |
| 7 | Declare a default | `default_declaration` | No authority; no justification; applicability undeclared |
| 8 | Record a criterion approval | `criterion_approval` | Resolution outcome envelope not supplied in full |
| 9 | Record a criterion analysis | `criterion_analysis` | Analysis referencing a different criterion version |
| 10 | Record an authority drift observation | drift observation | Unknown criterion version |
| 11 | Retire a criterion | retirement | Criterion is bound by an active definition version |
| 12 | Register a scale | registration | No declared comparison semantics; no declared aggregation definedness |
| 13 | Register a candidate source kind | registration | Duplicate key; no completeness semantics |
| 14 | Register a decision class | registration | Duplicate key; no owning component |
| 15 | Register an aggregator | registration | No declared scale requirement |
| 16 | Register a decision purpose | registration | Duplicate key |

Operation 4 is the operation the part is built around and its refusal list is the design in compressed form. Two of its refusals will be resisted.

The refusal of a criterion whose effect is selection by rule sequence, per clause P5-3.59, removes the most used hit policy in practice. The remedy is a precedence over outcome values, which is a policy somebody can approve.

The refusal of a parameter with no justification, per clause P5-3.49, means a criterion cannot be recorded until somebody says where its weights came from. The escape is the `UNJUSTIFIED` basis, which is admissible and countable. That is deliberate: the requirement is not that every weight be defensible, but that an indefensible weight be visible as one.

**P5-4.5 (MUST) Preconditions checked at recording.** An implementation must check every precondition in the table above at the moment of recording, must record the outcome of each check, and must not defer a check.

**P5-4.6 (MUST) Whole criterion version in one operation.** An implementation must accept the whole artifact set of a criterion version in a single operation and must record it atomically.

**P5-4.7 (MUST) Approval recorded, never granted.** An implementation must not provide an operation that approves a criterion version and must provide only the recording of an approval obtained from `Part 1`.

**P5-4.8 (MUST NOT) No retirement of a bound criterion.** An implementation must refuse to retire a criterion bound by an active decision definition version and must state the definition in the refusal.

**P5-4.9 (MUST) Scale semantics required at registration.** An implementation must require a scale registration to declare its comparison semantics and whether aggregation over it is defined, and must refuse one that does not.

### 4.3 Deciding operations

| # | Operation | Records | Principal refusals |
| --- | --- | --- | --- |
| 17 | Decide | `decision_request`, `decision_run`, `candidate`, `candidate_eligibility`, `comparison`, `selection`, `elimination`, `decision_pin` | No decision instant; unknown or unapproved definition; a pin unobtainable; candidates supplied for a definition whose source is not `SUPPLIED_BY_CALLER`; a candidate whose outcome value is outside the outcome concept's value set |
| 18 | Decide as a batch | as above per subject, plus a batch record | As above |
| 19 | Reproduce a recorded decision | a new run linked to the original, and a divergence record | Original unknown; a pin no longer obtainable |
| 20 | Explain a decision | an access record | Decision unknown |
| 21 | Simulate a decision under a proposed criterion | a run marked non authoritative | Caller not authorised for the purpose |
| 22 | Record a human involvement | `human_involvement` | Run unknown; actor kind not a natural person |
| 23 | Record an override | `override` | No authorisation; no reason; original outcome not retained |
| 24 | Record a decisive automation assessment | `decisive_automation_assessment` | Assessment other than `UNASSESSED` with no named assessor, except where the basis is derived or inferred |

Operation 21 exists for the reason `Part 2` operation 25 exists: criterion authors need to try a criterion before it is approved, and the alternative to providing it is that they will do so in a copy of the engine with none of the recording. It is fenced identically: the run is marked non authoritative, the marking is not removable, and clause P5-4.14 forbids a non authoritative outcome from being cited or acted upon.

Operation 21 is also the operation that would have produced the 2030 comparison in the worked demonstration: running the historical candidate sets under a proposed criterion to see how often it would fail to determine. That is the most useful thing a decision engine can do before a criterion is adopted and almost nothing offers it.

**P5-4.10 (MUST) Pins recorded before returning.** An implementation must durably record the pin set of a run before returning any outcome from it.

**P5-4.11 (MUST) Reproduction available.** An implementation must provide operation 19 and must be able to attempt reproduction of any decision within its retained history.

**P5-4.12 (MUST) Reproduction failure recorded, not hidden.** An implementation must record a non result where a pinned artifact cannot be obtained during reproduction and must not substitute the current version.

**P5-4.13 (MUST) Simulation over historical candidate sets available.** An implementation must permit operation 21 to be run over the recorded candidate sets of past decisions, and must report the outcome distribution of the proposed criterion including the outcomes on which it would fail to determine.

**P5-4.14 (MUST NOT) No citation of a non authoritative run.** An implementation must mark every run produced by operation 21 as non authoritative, must not permit the marking to be removed, and must refuse to include such a run in an evidence package as evidence of a decision.

**P5-4.15 (MUST) Batch decides per subject.** An implementation must produce a separate decision record for each subject in a batch and must not merge candidates or selections across subjects.

**P5-4.16 (MUST) Explanation available for every decision.** An implementation must be able to return, for every recorded decision, the candidate set with its completeness, every eligibility verdict, the criterion version with its statement and authority status, every comparison, the selection with its basis and margin, every elimination with its ground, the pins, and every human involvement.

**P5-4.17 (MUST NOT) No explanation by recomputation.** An implementation must assemble every explanation from the records of the run and must not recompute a decision in order to explain it.

**P5-4.18 (MUST) Override retains the original.** An implementation must retain the outcome the criterion produced when recording an override, per clause P5-3.110.

### 4.4 Reading operations

| # | Operation | Returns |
| --- | --- | --- |
| 25 | Read a named projection | The projection of section 3.17, at the times supplied |
| 26 | Resolve a criterion as of a time | The criterion version in force, with its approval and authority status |
| 27 | Get a decision | The decision record, complete |
| 28 | Get a criterion version | The whole artifact set of the version |
| 29 | Export an evidence package | The package of section 8.6 |

**P5-4.19 (MUST) Times required on temporal resolution.** An implementation must require both an application time and a knowledge time for operation 26 and must not default either.

**P5-4.20 (MUST NOT) No partial decision record.** An implementation must return a complete decision record from operation 27 or refuse, and must not return a subset without stating what was omitted and why.

**P5-4.21 (MUST) Statuses returned with every criterion.** An implementation must return the approval status and the authority status with every criterion version returned from any operation.

### 4.5 What a caller may and may not assume

**P5-4.22 (MUST) Caller obligations declared.** An implementation must document, for every operation, which of the assumptions below the caller may make.

A caller may assume that a returned outcome was produced by the recorded basis, that every candidate considered is recorded with an elimination ground, that no candidate was excluded for inadmissibility other than on a `Part 2` verdict, that the outcome is reproducible from the recorded pins, and that no undeclared rule resolved a tie, a cycle or an incomparability.

A caller may not assume that the candidate set was complete, since completeness is declared and for some source kinds is never claimed. A caller may not assume that a decided outcome was determined by the criterion, since the basis may be a tiebreak or a default. A caller may not assume that an outcome was robust, since the margin may be within the marginality threshold. A caller may not assume that a candidate recorded as ineligible failed a rule, since it may have been excluded for want of information under a declared treatment. A caller may not assume that a recorded human involvement makes a decision non automated, since the decisive automation assessment is separate and defaults to unassessed. And a caller may not assume that the criterion is approved or that its authority is in force, since both statuses are returned.

**P5-4.23 (MUST NOT) No implied determinacy.** An implementation must not describe an outcome as determined, computed or required where the basis was a tiebreak, a default or an external determination.

**P5-4.24 (MUST NOT) No implied robustness.** An implementation must not describe an outcome as clear, decisive or unambiguous, and must return the margin and the marginality flag.

### 4.6 Reads from other components

| Read | From | On unavailability |
| --- | --- | --- |
| Resolve a definition or criterion document version and its status | `Part 1` | Refuse the decision where the binding mode is `AS_OF_LINEAGE`; record `APPROVAL_UNRESOLVABLE` otherwise |
| Resolve a criterion authority citation and its status | `Part 1` | Record `authority_status` as `UNRESOLVABLE`; do not refuse the decision |
| Obtain an eligibility evaluation report | `Part 2` | Refuse the decision; return the outcome of section 7.4 |
| Obtain a concept definition version | `Part 4` | Refuse the decision where the outcome concept or a considered attribute cannot be resolved |
| Obtain an authorisation decision | `Part 7` | Refuse the operation |
| Obtain a permissible value set version | `Part 10` | Refuse the decision where a precedence criterion is bound to it |
| Obtain a pinned model output | `Part 13` | Refuse the decision |
| Record the decision as a determination | `Part 3` | Record the failure and retry; do not discard the decision record |

The asymmetry in the second row is the same one `Part 2` draws for its own authority reads and `Part 3` draws for its citations. An unresolvable authority does not stop the decision, because stopping would change what the organisation does on the strength of a lookup failure. An unavailable eligibility report does stop it, because without it the component does not know which candidates are admissible and every treatment of that gap is a policy nobody declared.

The last row is not a read but is included because it is an obligation. A decision is a determination and `Part 3` records it; a failure to record must not cause the decision to be lost here, and clause P5-4.28 states the requirement.

**P5-4.25 (MUST) Declared unavailability behaviour.** An implementation must implement the unavailability behaviour of the table above for every read and must record which behaviour it took.

**P5-4.26 (MUST NOT) No substitution on unavailability.** An implementation must not substitute a cached, default, current or successor version of any artifact in the table above.

**P5-4.27 (MUST) Eligibility unavailability refuses the decision.** An implementation must refuse a decision for which it could not obtain an eligibility report and must not proceed on an assumption about admissibility.

**P5-4.28 (MUST) Ledger recording failure does not lose the decision.** An implementation must retain its own decision record where recording the determination with `Part 3` failed, must record the failure, and must be able to report every decision not yet recorded there.

**P5-4.29 (MUST NOT) No decision invoked during an evaluation.** An implementation must not accept a decision request originating from a `Part 2` evaluation in progress, consistently with `Part 2` clause P2-12.14, and must declare the mechanism by which the dependency is kept in one direction.

### 4.7 Events emitted

The envelope carries at minimum an event identity, a type from the registered set, the knowledge time assigned by this component, the subject, the actor, a correlation reference, a schema reference and a digest over the event body.

The minimum event set. An implementation may emit more.

Decision definition version recorded. Criterion version recorded. Criterion version refused. Criterion parameter recorded unjustified. Precedence order recorded. Tiebreak declared. Default declared. Criterion approval recorded. Criterion approval unresolvable. Criterion authority drift observed. Criterion analysis recorded. Criterion retired. Scale registered. Decision requested. Decision run started. Decision completed. Decision decided by criterion. Decision decided by tiebreak. Decision decided by default. Decision undecidable by tie. Decision undecidable by intransitivity. Decision undecidable by incomparability. Decision refused for indeterminate eligibility. Indeterminate eligibility treated. Candidate excluded for indeterminate eligibility. Candidate out of scope of criterion. Candidate set incomplete. Marginal decision. Weight sensitivity computed. Weight sensitivity not computable. Human involvement recorded. Override recorded. Decisive automation assessed. Decision reproduced. Decision diverged. Simulation performed. Evidence package exported.

Four of these are the operationally important ones and are the least likely to be emitted by an implementation that has not read this part.

The three undecidable events must be emitted per decision rather than aggregated, because they are the events an organisation needs in order to discover that its criterion does not fit its candidates.

**Candidate excluded for indeterminate eligibility** must be emitted per candidate, because it is the event by which a data supply failure becomes visible as one rather than as a run of unsuccessful applicants.

**Marginal decision** must be emitted per decision, because a marginal decision is where review is worth directing and nothing else identifies it.

**Weight sensitivity not computable** must be emitted, because an implementation that cannot compute the perturbation for a weighted criterion has a criterion whose robustness nobody can assess.

**P5-4.30 (MUST) Minimum event set.** An implementation must emit an event for every member of the set above and must register any additional type under section 9.9.

**P5-4.31 (MUST) Envelope minimum.** An implementation must include every envelope element named above in every event it emits.

**P5-4.32 (MUST NOT) No event in place of a record.** An implementation must not rely on event emission to satisfy any recording obligation of section 3 or section 8.

**P5-4.33 (MUST) Undecidable outcomes emitted individually.** An implementation must emit a distinct event for each decision returning a tie, intransitivity or incomparability outcome and must not emit them only as counts.

**P5-4.34 (MUST) Indeterminate exclusion emitted per candidate.** An implementation must emit a distinct event for each candidate excluded for an indeterminate eligibility verdict.

**P5-4.35 (MUST NOT) No suppression of adverse events.** An implementation must not provide a configuration that suppresses the emission of a refusal, an undecidable outcome, a defaulted outcome, a tiebroken outcome, an indeterminate exclusion, a marginal decision, an unjustified parameter, an authority drift, an override or a divergence.
## 5. State model

### 5.1 Four state models, deliberately separated

This part specifies four state machines and keeps them apart, following the pattern the four prior parts establish. Section 13.7 restates the question `Part 4` section 13.7 hands `Part 0`: whether the pattern should be stated once for the whole standard.

The **registration state** of a criterion version is owned here and describes whether this component will apply it.

The **force state** of a criterion is not owned here. Whether a criterion is approved is a `Part 1` fact obtained by resolution, and whether it is in force at an application time follows from that approval and the effectivity of the document carrying it. This part holds no field carrying it.

The **decision run state** describes the progress of one execution.

The **assessment state** of a decision describes what has been established about it after the fact: its decisive automation assessment, its override, and any recorded review.

The separation of registration from force matters for the reason it matters in `Part 2` and `Part 4`. A criterion can be fully registered here, with a statement, justified parameters and a passing analysis, and approved by nobody. A single status field must then report either that it does not exist, which conceals the criterion the organisation is actually using, or that it is available, which conceals that nobody accepted responsibility for the weights.

**P5-5.1 (MUST) Four models separate.** An implementation must not represent registration state and force state in one field and must not derive either from the other.

**P5-5.2 (MUST) Registered but unapproved reportable.** An implementation must be able to report every criterion version whose registration state is complete and whose approval status is not approved, and must include the count in the signals of section 8.5.

**P5-5.3 (MUST NOT) No force state held.** An implementation must not hold, cache beyond a declared validity period, or assert the approval or force state of a criterion version.

### 5.2 Registration state of a criterion version

States:

`DRAFT`. The artifact set is incomplete. The version is readable, is marked, and must not be applied by any decision.

`CHECKING`. The preconditions of operation 4 are being applied.

`REGISTERED`. Every precondition passed. The version is applicable subject to approval and effectivity.

`REFUSED`. A precondition failed. The reason is recorded per check. The version is retained and is never applicable.

`SUSPENDED`. The version was registered and a pinned dependency has since become unobtainable: a scale registration, a `Part 10` value set version bound by a precedence order, or a sub criterion. The version is not applicable. This is a statement about the component rather than about the criterion.

`SUPERSEDED`. A later version of the same criterion has been registered. The version remains applicable for a decision whose instants resolve to it.

`WITHDRAWN`. Registration was revoked deliberately, with an authorisation reference and a reason, on the ground that the version should not have been registered.

Transitions:

| From | To | Trigger | Requires |
| --- | --- | --- | --- |
| `DRAFT` | `CHECKING` | Registration requested | Complete artifact set |
| `CHECKING` | `REGISTERED` | All checks passed | Analysis recorded where the kind admits one |
| `CHECKING` | `REFUSED` | Any check failed | Recorded reason per failed check |
| `REFUSED` | `CHECKING` | Registration requested again | A new artifact set, that is, a new version |
| `REGISTERED` | `SUSPENDED` | A pinned dependency became unobtainable | Recorded dependency |
| `SUSPENDED` | `REGISTERED` | The dependency became obtainable | Analysis re run |
| `REGISTERED` | `SUPERSEDED` | A later version registered | Identity of the successor |
| `REGISTERED`, `SUPERSEDED` | `WITHDRAWN` | Deliberate revocation | `AUTHREF` and reason |
| `WITHDRAWN` | `REGISTERED` | Reinstatement | `AUTHREF`, reason, and analysis re run |

`SUSPENDED` matters more here than the equivalent state in `Part 2`, because a suspended criterion means decisions of its class cannot be made. An organisation whose supplier selection criterion is suspended because a value set became unobtainable is not making a worse decision; it is not making one, and clause P5-5.8 requires the condition to be reported rather than silently causing refusals.

`REFUSED` versions are retained, as in `Part 4` section 5.2, and for the same reason: the record that somebody attempted to register a criterion selecting by rule order, or with three unjustified weights and a claim of authority it did not have, is the record an assurance function needs.

**P5-5.4 (MUST) Enumerated states only.** An implementation must represent the registration state of a criterion version as exactly one member of the set above.

**P5-5.5 (MUST) Enumerated transitions only.** An implementation must not effect a transition absent from the table above.

**P5-5.6 (MUST) State is a projection.** An implementation must compute registration state from recorded rows and must not hold it as an updatable field.

**P5-5.7 (MUST NOT) No application outside applicable states.** An implementation must not apply a criterion version whose registration state is not `REGISTERED` or `SUPERSEDED`, except under operation 21 of section 4.3.

**P5-5.8 (MUST) Suspension reported, not silent.** An implementation must emit an event and record a signal when a version enters `SUSPENDED`, and must report every decision definition version whose criterion is suspended.

**P5-5.9 (MUST) Refused versions retained and countable.** An implementation must retain every refused version with its per check outcomes and must be able to report refusals by author, by criterion and by failed precondition.

**P5-5.10 (MUST) Withdrawal authorised and reasoned.** An implementation must record an `AUTHREF` and a reason for every transition to `WITHDRAWN`, and must report the decisions taken under the version while it stood.

**P5-5.11 (MUST) Superseded versions remain applicable.** An implementation must continue to apply a version in `SUPERSEDED` for a decision whose instants resolve to it and must not substitute the successor.

**P5-5.12 (MUST NOT) No state change from the passage of time.** An implementation must not transition registration state as a consequence of a date passing and must effect every transition by a recorded act.

### 5.3 Decision run state

States: `REQUESTED`, `RESOLVING`, `ENUMERATING_CANDIDATES`, `ESTABLISHING_ELIGIBILITY`, `COMPARING`, `SELECTING`, `COMPLETED`, `UNDECIDED`, `REFUSED`, `ABANDONED`.

| From | To | Trigger |
| --- | --- | --- |
| `REQUESTED` | `RESOLVING` | Request accepted and authorised |
| `REQUESTED` | `REFUSED` | Request invalid, unauthorised, or no decision instant |
| `RESOLVING` | `ENUMERATING_CANDIDATES` | Definition, criterion and pins resolved |
| `RESOLVING` | `REFUSED` | A required pin unobtainable, or the criterion not applicable |
| `ENUMERATING_CANDIDATES` | `ESTABLISHING_ELIGIBILITY` | Candidate set assembled and its completeness recorded |
| `ENUMERATING_CANDIDATES` | `SELECTING` | No eligibility binding declared |
| `ESTABLISHING_ELIGIBILITY` | `COMPARING` | Every candidate has a verdict |
| `ESTABLISHING_ELIGIBILITY` | `REFUSED` | Eligibility unobtainable |
| `ESTABLISHING_ELIGIBILITY` | `UNDECIDED` | An indeterminate verdict and a treatment of decline to decide |
| `COMPARING` | `SELECTING` | Comparisons complete within bounds |
| `COMPARING` | `UNDECIDED` | A tie, intransitivity or incomparability with no applicable tiebreak |
| `SELECTING` | `COMPLETED` | An outcome recorded, whether by criterion, tiebreak or default |
| `SELECTING` | `UNDECIDED` | No candidate selected and no applicable default |
| any | `ABANDONED` | Loss of the executing process |

`UNDECIDED` is a terminal state distinct from `REFUSED` and from `COMPLETED`, and the distinction is the most consequential in this section.

`REFUSED` means the component did not attempt the decision: the request was bad, a pin was missing, the criterion was not applicable. It is a statement about the request.

`UNDECIDED` means the component attempted the decision, did the work, and the criterion did not determine an answer. It is a statement about the criterion and the candidates, it is a legitimate result, and it is the outcome the whole design exists to make possible. An implementation that maps it onto `REFUSED` has turned a substantive finding about policy into an error somebody will retry.

`COMPLETED` covers every outcome in which something was recorded as the outcome, including those produced by a tiebreak and a default, because in all those cases a decision was reached. The basis distinguishes them and clause P5-3.83 forbids collapsing it.

**P5-5.13 (MUST) Enumerated run states.** An implementation must represent every run as exactly one member of the set above.

**P5-5.14 (MUST) Undecided distinguished from refused.** An implementation must record `UNDECIDED` where the criterion did not determine an answer and `REFUSED` where it did not attempt the decision, and must not use one for the other.

**P5-5.15 (MUST) Undecided is terminal and complete as a record.** An implementation must record the whole candidate set, every eligibility verdict, every comparison performed and every elimination for a run in `UNDECIDED`, and must not discard the work.

**P5-5.16 (MUST) Pins before enumeration.** An implementation must resolve and record the pin set before enumerating candidates.

**P5-5.17 (MUST) Eligibility before comparison.** An implementation must not enter `COMPARING` before every candidate has an eligibility verdict, where an eligibility binding is declared.

**P5-5.18 (MUST) Abandonment detected and recorded.** An implementation must transition a run whose executing process is lost to `ABANDONED` within a declared interval and must declare the interval.

**P5-5.19 (MUST NOT) No resumption of an abandoned run.** An implementation must not resume an abandoned run and must record a new run where the decision is retried.

**P5-5.20 (MUST) Terminal states are terminal.** An implementation must not transition out of `COMPLETED`, `UNDECIDED`, `REFUSED` or `ABANDONED`.

### 5.4 Assessment state of a decision

The decision itself never transitions. What transitions is what has been established about it, on the pattern `Part 3` section 5.1 states.

States: `AS_DECIDED`, `HUMAN_REVIEWED`, `OVERRIDDEN`, `AUTOMATION_ASSESSED`, `SUPERSEDED_BY_DECISION`.

These are not mutually exclusive in the way the other machines' states are, and clause P5-5.21 requires them to be held as independent facts rather than as one field. A decision may be human reviewed, then assessed for decisive automation, then superseded by a later decision, and each is a separate appended assertion.

`SUPERSEDED_BY_DECISION` records that a later decision replaced this one, with a kind of `CORRECTION`, `REVISION`, `REAFFIRMATION` or `UNSPECIFIED`, on the pattern `Part 3` section 5.5 establishes. The distinction between correction and revision matters here for the same reason: a corrected decision asserts that the earlier outcome should not have been reached, which bears on everything that relied on it, and a revised decision asserts that circumstances changed.

**P5-5.21 (MUST) Assessments held independently.** An implementation must hold each assessment of a decision as an independent appended fact and must not represent them as one status field.

**P5-5.22 (MUST NOT) No decision transition.** An implementation must not assign a lifecycle state to a decision, a candidate, an eligibility verdict or a selection.

**P5-5.23 (MUST) Supersession is a relation with a kind.** An implementation must record supersession as a relation between two decisions with a recorded kind and must not represent it as a state change on either.

**P5-5.24 (MUST) Correction implies dependents reported.** An implementation must report, at the moment a decision is superseded by kind `CORRECTION`, every determination `Part 3` records as having relied upon it, or record that the report could not be obtained.

**P5-5.25 (MUST) Superseded decisions remain readable.** An implementation must return a superseded decision in full on request, with its supersession relation, and must not redirect a read to the superseding decision.

**P5-5.26 (MUST NOT) No assessment as amendment.** An implementation must not alter a recorded selection, basis, margin or outcome in the course of recording a review, an override or an automation assessment.
## 6. Execution semantics

### 6.1 Determinism and reproducibility

Two properties, distinguished as in `Part 2` section 6.1.

**Determinism.** One decision, run twice in the same conditions with the same candidates, yields the same outcome.

**Reproducibility.** A decision made in 2028 can be made again in 2035, from its recorded pins, and yield the same outcome.

Determinism fails in this component in ways it does not fail in `Part 2`, because a selection is sensitive to things an evaluation is not. Five sources must be controlled and the last two are specific to selection.

The criterion changed, which pinning prevents. The candidate attributes changed, which pinning prevents. The eligibility report changed, which pinning prevents.

**Candidate iteration order.** A comparison performed in a different order can yield a different winner where the comparison is not a total order, and can yield a different margin where floating point arithmetic is used. Clause P5-6.3 requires a declared total order on traversal, and clause P5-3.26 forbids that order from affecting the outcome, so the two together require that a differing traversal order produce an identical outcome and that the property be checkable.

**Numeric comparison.** A score comparison in binary floating point is wrong at the boundary, and the boundary is where ties and near ties live. A tie detected under one arithmetic is a margin of one machine epsilon under another, and the outcome differs. Clause P5-6.4 requires exact decimal arithmetic for score and aggregate comparison, on the same basis as `Part 2` clause P2-6.4 and for a sharper reason: in an evaluation a boundary error changes one verdict, and in a selection it changes which candidate wins.

**P5-6.1 (MUST) Identical pins yield identical outcomes.** An implementation must return the same outcome, basis, selected candidate, margin and elimination grounds for two decisions whose pin sets and candidate sets are identical.

**P5-6.2 (MUST) Scale comparison pinned.** An implementation must pin the scale registration used for every comparison and must not rely on a platform default for ordering, collation or precision.

**P5-6.3 (MUST) Traversal order total and declared.** An implementation must impose a declared total order on the traversal of a candidate set and must not permit the order to vary between runs with identical inputs.

**P5-6.4 (MUST) Exact arithmetic for comparison.** An implementation must use an exact decimal arithmetic for every score, aggregate and margin comparison and must not use binary floating point.

**P5-6.5 (MUST) Order independence demonstrable.** An implementation must be able to demonstrate, for a decision definition version, that decisions are unaffected by candidate traversal order, by deciding a recorded candidate set in at least two orders and comparing the outcomes, and must record the result as a `criterion_analysis`.

**P5-6.6 (MUST) Tie detection at declared precision.** An implementation must detect a tie at the precision the scale registration declares and must not treat a difference below the declared precision as a margin.

### 6.2 The decision algorithm

Normative in its ordering and in its outcomes; not normative in its structure as code.

```
decide(request):
  1  if request.decision_instant is absent:   return REFUSED(DECISION_INSTANT_REQUIRED)
  2  decision = obtain authorisation from Part 7 for purpose and subject
     if not permitted:                        return REFUSED(NOT_AUTHORISED)
  3  definition = resolve(request.definition_reference, binding_mode,
                          decision_instant, knowledge_instant)
     if unresolved:                           return REFUSED(DEFINITION_UNRESOLVABLE)
  4  criterion = criterion_version of definition
     if registration_state(criterion) not in {REGISTERED, SUPERSEDED}:
                                              return REFUSED(CRITERION_NOT_APPLICABLE)
     record criterion approval status and authority status
  5  pin definition, criterion, precedence order, tiebreak, default,
     eligibility rule set, scale, aggregator, value sets, model outputs, seed
     if any pin unobtainable:                 return REFUSED(PIN_UNOBTAINABLE)
  6  candidates = enumerate per the declared source
     record the set completeness and its basis
     if candidates is empty:
        if a default applies to NO_CANDIDATE: outcome = DECIDED_BY_DEFAULT; goto 12
        else:                                 outcome = NO_CANDIDATE; goto 12
  7  if an eligibility binding is declared:
        for each candidate, in the declared traversal order:
            report = obtain evaluation from Part 2 for the candidate
            if unobtainable:                  return REFUSED(ELIGIBILITY_UNAVAILABLE)
            pin the whole report
            eligible(candidate) = TRUE if every rule satisfied
                                  FALSE if any violated or contradicted
                                  INDETERMINATE otherwise
        for each candidate with INDETERMINATE eligibility:
            apply the declared treatment for its Part 2 subclass
            record the treatment applied
            if the treatment is DECLINE_TO_DECIDE:
                                              outcome = UNDECIDED_ELIGIBILITY_INDETERMINATE
                                              goto 12
     else: eligible(candidate) = TRUE for all
  8  admissible = candidates where eligible is TRUE, or included by treatment
     record an elimination for every candidate not admissible
     if admissible is empty:
        if a default applies to NO_ELIGIBLE_CANDIDATE:
                                              outcome = DECIDED_BY_DEFAULT; goto 12
        else:                                 outcome = NO_ELIGIBLE_CANDIDATE; goto 12
  9  if collection_mode is RETURN_ALL:         outcome = RETURNED_ALL; goto 12
     if collection_mode is AGGREGATE:          outcome = AGGREGATED; goto 12
 10  apply the criterion to admissible, recording every comparison
     maximal = the candidates no other candidate is preferred to
     if the pairwise relation contains a cycle:
                                              undetermined = INTRANSITIVE
     else if |maximal| > 1 and the members are equally preferred:
                                              undetermined = TIE
     else if |maximal| > 1 and the members are unranked relative to each other:
                                              undetermined = INCOMPARABLE
     else:                                    undetermined = none
 11  if undetermined is none:
            outcome = DECIDED; basis = CRITERION; selected = the single maximal
     else if a tiebreak applies to undetermined:
            apply the tiebreak to maximal, recording every comparison
            if it determines one:  outcome = DECIDED_BY_TIEBREAK; basis = TIEBREAK
            else:                  outcome = the undecidable member for undetermined
     else if a default applies to NO_CANDIDATE_SELECTED:
            outcome = DECIDED_BY_DEFAULT; basis = DEFAULT
     else:  outcome = the undecidable member for undetermined
 12  compute the margin per section 3.14 and the marginality flag
     record selection, eliminations, counts, statuses, pins, seed
     derive solely_automated; default the automation assessment to UNASSESSED
     emit events; record the determination with Part 3
     return the outcome envelope of section 7.3
```

Four properties of the algorithm are decisions rather than derivations.

**Step 7 obtains eligibility for every candidate before treating any.** An implementation that short circuits, treating the first indeterminate candidate before evaluating the rest, produces a different record depending on traversal order and may decline to decide on a candidate that would have been eliminated anyway. Clause P5-6.9 forbids the short circuit.

**Step 10 identifies the maximal set rather than a winner.** Finding a winner directly requires a total order and there is no guarantee of one. Computing the maximal set and then classifying why it has more than one member is what makes the three undecidable outcomes distinguishable, and every engine that does the former cannot produce them.

**Step 11 tries the tiebreak before the default.** A tiebreak resolves among candidates and a default replaces them, so a declared tiebreak that applies is always the better basis. The order is normative and clause P5-6.12 states it.

**Step 11 falls to the undecidable outcome rather than to any residual rule.** There is no final fallback. Where the criterion does not determine, no declared tiebreak applies and no declared default applies, the component returns the undecidable outcome and the decision goes to a person. That is the design and clause P5-6.13 forbids any other terminus.

**P5-6.7 (MUST) Algorithm order.** An implementation must perform the steps above in the order given and must not apply the criterion before recording the pin set and the candidate set completeness.

**P5-6.8 (MUST) Maximal set computed.** An implementation must compute the set of candidates to which no other admissible candidate is preferred, and must classify a set of more than one member as intransitive, tied or incomparable per step 10.

**P5-6.9 (MUST NOT) No short circuit on eligibility.** An implementation must obtain an eligibility verdict for every candidate before applying any indeterminate treatment and must not stop at the first indeterminate verdict.

**P5-6.10 (MUST NOT) No short circuit on comparison.** An implementation must record every comparison the criterion requires and must not stop comparing on finding a candidate that appears to win, since the remaining comparisons determine the margin and the maximal set.

**P5-6.11 (MUST) Empty cases distinguished.** An implementation must distinguish an empty candidate set from an empty admissible set and must return the corresponding outcome or apply the corresponding default.

**P5-6.12 (MUST) Tiebreak before default.** An implementation must apply an applicable tiebreak before an applicable default.

**P5-6.13 (MUST NOT) No residual fallback.** An implementation must return the undecidable outcome of section 7.2 where the criterion does not determine and no declared tiebreak or default applies, and must not select by any other means.

**P5-6.14 (MUST) Every comparison recorded.** An implementation must record every comparison it performed, with the candidates compared, the attribute or attributes considered, and the result.

### 6.3 Comparability and the resolution of incomparability

A criterion supplies an order over candidates. The order may be total, in which case one candidate is maximal unless two are equal, or partial, in which case candidates may be unranked relative to each other.

The condition to be careful about is the second and it is not a defect. Two suppliers, one cheaper and one faster, are genuinely unranked until somebody says how much money a day is worth. A criterion that produces a winner has been given that rate of exchange; a criterion that reports incomparability has not been given it and says so.

Arrow's impossibility theorem is the general result behind this. It establishes that no rule for aggregating individual orderings into a collective ordering can simultaneously satisfy a small set of conditions each of which appears reasonable, so that any aggregation rule sacrifices one of them. Applied here, the consequence is not that aggregation is impossible but that every aggregation rule embeds a choice that cannot be justified from the inputs, which is exactly the definition of a criterion in section 1.3 and exactly why sections 3.7 and 3.8 require the rule and its parameters to be governed artifacts with justifications.

The Condorcet paradox is the specific case that produces intransitivity: pairwise majority comparison over three or more attributes can yield a cycle. It is a mathematical fact rather than an implementation defect and it is why `PAIRWISE_PREFERENCE` is the only kind in section 3.7 under which a cycle is possible.

**P5-6.15 (MUST) Order totality declared.** An implementation must record, for every criterion version, whether the order it induces is total or partial, and must not treat a partial order as total.

**P5-6.16 (MUST) Incomparability detected.** An implementation must detect where two candidates in the maximal set are unranked relative to each other and must classify the outcome as incomparable rather than tied.

**P5-6.17 (MUST) Intransitivity detected.** An implementation must detect a cycle in the pairwise preference relation and must classify the outcome as intransitive.

**P5-6.18 (MUST) Cycle reported with its members.** An implementation must record the candidates forming the cycle and the comparisons constituting it.

**P5-6.19 (MUST NOT) No resolution by traversal.** An implementation must not resolve an intransitivity by the order in which it traversed the candidates, by the candidate it started from, or by an iteration limit.

**P5-6.20 (MUST NOT) No implicit rate of exchange.** An implementation must not compare two candidates on attributes for which the criterion declares no weight, ordering or rate of exchange, and must report incomparability instead.

**P5-6.21 (MUST) Tie and incomparability distinguished in the record.** An implementation must record which of the two occurred and must not use one outcome member for both.

### 6.4 Static analysis of criteria and decision tables

Four properties of a criterion or a decision table are worth knowing before it is used and each is decidable in the restricted forms this part admits.

**Completeness.** Whether every combination of input values the outcome concept admits is addressed. An incomplete table falls through to a default, or to the undecidable outcome where none is declared, and the gap is discoverable in advance. DMN treats completeness as a configurable requirement on a table and this part treats it as an analysis result recorded per criterion version.

**Overlap.** Whether more than one rule can match. Overlap is a defect under a Unique constraint and is the normal case under a precedence criterion, so the analysis must be read against the criterion kind rather than reported as an error.

**Subsumption.** Whether one rule is entirely contained in another, so that it can never be the sole match. A subsumed rule is redundant and, more usefully, is often a mistake: somebody added a specific case that a general case already covered, believing the specific one would win.

**Masking.** Whether a rule can never be selected under the criterion, because every case it matches is also matched by a rule the precedence prefers. A masked rule is dead policy that reviewers will read as live, which is worse than redundancy.

`criterion_analysis` records the four results, the analysis procedure version, and the knowledge time. An analysis that did not complete is recorded as not performed rather than as finding nothing, on the same basis as `Part 2` clause P2-6.48.

**P5-6.22 (MUST) Four analyses performed where decidable.** An implementation must analyse completeness, overlap, subsumption and masking over every criterion version whose form admits the analysis, and must record the results.

**P5-6.23 (MUST) Analysis read against the kind.** An implementation must record whether an overlap is a defect or the expected condition given the criterion kind and must not report an overlap under a precedence criterion as an error.

**P5-6.24 (MUST) Masked rules reported.** An implementation must report every rule of a decision table that can never be selected under the declared criterion and must include the count in the signals of section 8.5.

**P5-6.25 (MUST) Incompleteness reported with its consequence.** An implementation must report an incomplete criterion together with what will happen in the unaddressed cases, being a default or an undecidable outcome.

**P5-6.26 (MUST) Undecidability declared.** An implementation must record, for every criterion version it did not analyse, that the analysis was not performed and why.

**P5-6.27 (MUST NOT) No absence of finding as absence of fault.** An implementation must not report a criterion as complete, non overlapping, contracted or free of masking on the basis of an analysis that did not complete or was not performed.

**P5-6.28 (MUST NOT) No analysis at decision time.** An implementation must not perform static analysis during a decision and must not vary an outcome on the basis of an analysis result.

### 6.5 Idempotence

**P5-6.29 (MUST) Idempotence by key.** An implementation must return the originally recorded outcome for a repeated recording or deciding operation bearing an idempotence key already seen within its declared deduplication window and must not perform the operation again.

**P5-6.30 (MUST) Deduplication window declared.** An implementation must declare its deduplication window as a duration and must state what happens to a key repeated after it.

**P5-6.31 (MUST NOT) No idempotence across differing payloads.** An implementation must refuse an operation bearing a seen key with a different payload.

**P5-6.32 (MUST) Repeated decisions recorded separately.** An implementation must record each execution of a decision as a separate run, whether or not an idempotence key was supplied, and must not overwrite an earlier run.

### 6.6 Clocks

**P5-6.33 (MUST) Knowledge time assigned by this component.** An implementation must assign every knowledge time from its own clock and must refuse a request supplying one.

**P5-6.34 (MUST NOT) No occurrence time assignment.** An implementation must not assign an occurrence time and must record every one as asserted by a named actor.

**P5-6.35 (MUST NOT) No ambient clock in a criterion.** An implementation must not admit a criterion that reads a clock and must require every temporal comparison to be against a value supplied in the request or carried on a candidate, on the same basis as `Part 2` clause P2-6.24.

**P5-6.36 (MUST) Instants in a declared scale.** An implementation must record every instant in a declared time scale with a declared offset.

**P5-6.37 (MUST) Calendar convention declared.** An implementation must declare the convention by which it adds and subtracts months and years wherever a criterion compares durations, and must pin the convention in the run.

**P5-6.38 (MUST) Monotonic knowledge time within a stream.** An implementation must assign knowledge times that do not decrease within a stream and must record any correction of its own clock as an entry.

### 6.7 Bounds and budget

A decision over a large candidate set performs a number of comparisons that grows faster than the set for pairwise criteria, so the work must be bounded.

Three bounds: **candidate count**, **comparison count**, and a **budget** on a declared resource. As in the three prior parts, the primary budget must be on a deterministic resource, because a budget on wall clock time makes the same decision complete on one day and truncate on another, and a truncated decision is not a smaller decision but a decision over a subset.

The consequence of exhausting a bound here is more serious than in `Part 2`, where a budget exhaustion yields an indeterminate verdict for the unevaluated rules. Here it means candidates were not compared, so the selected candidate may not be the maximal one. Clause P5-6.41 therefore requires a truncated decision to return an outcome of its own rather than a selection.

**P5-6.39 (MUST) Three bounds declared.** An implementation must declare a candidate count bound, a comparison count bound and a budget, and must state the resource the budget bounds.

**P5-6.40 (MUST) Primary budget deterministic.** An implementation must make its primary budget a bound on a deterministic resource.

**P5-6.41 (MUST NOT) No selection from a truncated comparison set.** An implementation must return the truncation outcome of section 7.4 where a bound was reached before every required comparison was performed, and must not return a selection.

**P5-6.42 (MUST) Truncation point recorded.** An implementation must record the candidate and comparison at which truncation occurred and must record every elimination as `NOT_COMPARED` for candidates not reached.

**P5-6.43 (MUST NOT) No silent bound.** An implementation must not apply an undeclared bound and must not return a result without stating the bound that truncated it.

### 6.8 What this component may compute, and what it may not

It may compute: the maximal set under a criterion; the classification of a non singleton maximal set as tied, incomparable or intransitive; scores and aggregates on declared scales; margins and weight sensitivities; the four static analyses of section 6.4; and every count and projection of section 3.17.

It may not compute: whether a candidate is eligible, which is `Part 2`'s; whether a criterion is approved, which is `Part 1`'s; the meaning of a concept a criterion is expressed over, which is `Part 4`'s; whether a person's review was meaningful, which clause P5-3.111 reserves to a named actor; whether the criterion is the right criterion, which is nobody's in this standard; and whether an outcome was correct, which follows from the criterion and is not separately assessable.

**P5-6.44 (MUST) Permitted computations only.** An implementation must not compute any determination allocated to another component by section 12 and must return the recorded outcome that component supplied.

**P5-6.45 (MUST NOT) No inference of a criterion.** An implementation must not generate, complete, fit or suggest a criterion, a weight, a precedence order or a threshold and record it as a declared parameter.

**P5-6.46 (MUST NOT) No learning from outcomes.** An implementation must not adjust a criterion, a weight or a precedence order on the basis of recorded outcomes, overrides or observed results, and must require every change to be a recorded criterion version.

**P5-6.47 (MUST NOT) No assessment of criterion fitness.** An implementation must not assert that a criterion is appropriate, well calibrated or fit for its purpose, and must report only the analyses of section 6.4 and the distributions of section 8.5.
## 7. Outcome and failure taxonomy

### 7.1 Why the taxonomy is the specification

A decision engine has one output and every defect in it presents as a plausible value of that output.

An engine that resolves a tie by row order returns a well formed selection. An engine that resolves an intransitivity by whichever candidate it started from returns a well formed selection. An engine that excludes a candidate because its eligibility could not be established returns a well formed selection over a smaller set. An engine whose criterion did not determine anything and whose default fired returns a well formed selection. In every one of those four cases the output is indistinguishable from a decision the criterion determined, and in every one the organisation believes its policy chose when something else did.

The taxonomy exists so that the four are distinguishable, and every requirement in this section is written to make the distinction travel with the outcome rather than be available on request.

### 7.2 The outcome set

Thirteen members in five classes. The table is normative.

| Class | Member | Means |
| --- | --- | --- |
| Decided | `DECIDED` | The criterion determined a single candidate. |
| Decided | `DECIDED_BY_TIEBREAK` | The criterion did not determine; a declared tiebreak did. |
| Decided | `DECIDED_BY_DEFAULT` | No candidate was selected; a declared default supplied the outcome. |
| Decided | `DECIDED_EXTERNALLY` | The choice was made outside this component and is recorded. |
| Empty | `NO_CANDIDATE` | The candidate set was empty and no default applies. |
| Empty | `NO_ELIGIBLE_CANDIDATE` | Candidates existed, none was admissible, and no default applies. |
| Undecidable | `UNDECIDABLE_TIE` | Two or more candidates are equally preferred and no tiebreak applies. |
| Undecidable | `UNDECIDABLE_INCOMPARABLE` | Two or more candidates are unranked relative to each other and no tiebreak applies. |
| Undecidable | `UNDECIDABLE_INTRANSITIVE` | The pairwise preference relation contains a cycle and no tiebreak applies. |
| Undecidable | `UNDECIDED_ELIGIBILITY_INDETERMINATE` | A candidate's eligibility could not be established and the declared treatment is to decline. |
| Collected | `RETURNED_ALL` | The collection mode was to return every admissible candidate. Nothing was chosen. |
| Collected | `AGGREGATED` | The collection mode was to aggregate. The outcome is a computed value, not a candidate. |
| Refusal | `REFUSED` | The component did not attempt the decision. Carries a code. |

Six distinctions in the table are load bearing.

**`DECIDED` against `DECIDED_BY_TIEBREAK` and `DECIDED_BY_DEFAULT`.** All three produce an outcome value and only the first was determined by the criterion. A single member covering all three is the most common defect available in this component, because it makes a criterion that never determines anything indistinguishable from one that always does, and section 11.3 names the mechanism.

**The three `UNDECIDABLE` members against each other.** A tie, an incomparability and an intransitivity have three different remedies. A tie needs a tiebreak. An incomparability needs somebody to state a rate of exchange between the attributes on which the candidates differ, which is a policy act. An intransitivity needs the preference relation itself to be reconstructed, because the criterion is not an ordering. Merging them into one undecidable member sends all three to whoever handles the first.

**`UNDECIDED_ELIGIBILITY_INDETERMINATE` against every other undecidable member.** The others are statements about the criterion. This one is a statement about the inputs: the decision could not proceed because something was not known. Its remedy is to obtain the information, and it belongs to a different owner, on the same basis `Part 2` section 7.2 allocates its indeterminacy subclasses to five remedy owners.

**`NO_CANDIDATE` against `NO_ELIGIBLE_CANDIDATE`.** The first says nothing was offered, which is very often an upstream defect. The second says things were offered and none qualified, which is a policy working as intended. Reporting the first as the second conceals a broken enumeration behind a plausible policy outcome, and section 11.7 names it.

**The `Collected` class against the `Decided` class.** Returning every candidate is not choosing, and returning an aggregate produces a value that was not a candidate. Both are legitimate and neither is a selection, and clause P5-3.65 forbids presenting them as one.

**`Undecidable` against `REFUSED`.** An undecidable outcome is a substantive finding about the criterion, produced after the component did all the work. A refusal is a statement that the component did not attempt the decision. A caller that treats the first as the second will retry it, and it will fail identically forever.

**P5-7.1 (MUST) Closed outcome set.** An implementation must return exactly one member of the table above from every decision and must not return a value outside the set.

**P5-7.2 (MUST NOT) No additional members.** An implementation must not add a member and must express any additional distinction as a registered code within the `REFUSED` class.

**P5-7.3 (MUST) Three decided members distinguished.** An implementation must return `DECIDED` only where the criterion determined the outcome and must return the tiebreak or default member otherwise.

**P5-7.4 (MUST) Three undecidable failures distinguished.** An implementation must return the member corresponding to the specific failure to determine and must not use one member for a tie, an incomparability and an intransitivity.

**P5-7.5 (MUST) Eligibility indeterminacy distinguished from criterion failure.** An implementation must return `UNDECIDED_ELIGIBILITY_INDETERMINATE` where the decision could not proceed for want of an eligibility verdict, and must not return an undecidable member that attributes the failure to the criterion.

**P5-7.6 (MUST) Empty cases distinguished.** An implementation must return `NO_CANDIDATE` and `NO_ELIGIBLE_CANDIDATE` as distinct members and must not use one for the other.

**P5-7.7 (MUST NOT) No mapping onto a decided or not decided pair.** An implementation must not provide an interface that maps the thirteen members onto two values and must not document such a mapping as canonical.

**P5-7.8 (MUST NOT) No caller selected collapse.** An implementation must not offer a configuration by which an undecidable outcome is returned as a decided one, or by which a tiebroken or defaulted outcome is returned as `DECIDED`.

### 7.3 The outcome envelope

Normative in content; serialisation unspecified.

The outcome member. The basis of selection. The selected candidate identity and its outcome value, or the defaulted or aggregated value, or the statement that none was produced. The decision definition version and the criterion version, with the criterion's kind, its approval status and its authority status. The candidate set with its source kind, its completeness and the basis of that completeness. The three candidate counts, considered, eligible and indeterminate, each with its grain. Every elimination with its ground. The margin, its scale, and the marginality flag, or the statement that no margin is definable. The weight sensitivity for a weighted criterion, or the statement that it was not computable. Every indeterminate eligibility treatment applied, with the candidate and the `Part 2` subclass and code. Whether any candidate's eligibility rested on a vacuous satisfaction. The tiebreak and default identities where applied. The random seed where a random criterion or tiebreak was applied. The decision instant, the knowledge instant used and the knowledge time assigned. The pin set reference. Whether the outcome is solely automated, and the decisive automation assessment. Whether the run was non authoritative. The bound that truncated the run where one did.

**P5-7.9 (MUST) Envelope completeness.** An implementation must include every element named above in every outcome it returns and records.

**P5-7.10 (MUST NOT) No envelope reduction.** An implementation must not omit an envelope element on the ground that a caller does not use it.

**P5-7.11 (MUST) Envelope is what is recorded.** An implementation must record the whole envelope and must not record a reduced form while returning the full one or the reverse.

**P5-7.12 (MUST) Vacuous eligibility carried.** An implementation must include, in the envelope, whether any candidate's eligibility rested on a `Part 2` satisfaction marked vacuous, per clause P5-3.37.

### 7.4 Refusal codes

| Code | Cause | Retryable |
| --- | --- | --- |
| `DECISION_INSTANT_REQUIRED` | The request omitted the decision instant | Yes, with the instant |
| `MALFORMED_REQUEST` | The request was not well formed | Yes, corrected |
| `NOT_AUTHORISED` | `Part 7` did not permit the operation | No, without a changed decision |
| `DEFINITION_UNRESOLVABLE` | The definition reference did not resolve at the instants supplied | No |
| `CRITERION_NOT_APPLICABLE` | The criterion version is draft, refused, suspended or withdrawn | No, until the criterion is applicable |
| `PIN_UNOBTAINABLE` | A required pinned artifact could not be obtained | Possibly, if availability is restored |
| `ELIGIBILITY_UNAVAILABLE` | A `Part 2` evaluation report could not be obtained | Possibly |
| `CANDIDATES_SUPPLIED_UNEXPECTEDLY` | Candidates were supplied for a definition whose source is not the caller | Yes, without them |
| `CANDIDATE_OUTSIDE_OUTCOME_DOMAIN` | A candidate's outcome value is not in the outcome concept's value set | Yes, corrected |
| `TRUNCATED_BY_BOUND` | A bound was reached before every required comparison was performed | Possibly, with larger bounds |
| `CONSTRAINT_VIOLATED_UNIQUE` | More than one rule matched under a Unique constraint | No, until the table is corrected |
| `CONSTRAINT_VIOLATED_ANY` | Matching rules produced different outputs under an Any constraint | No, until the table is corrected |
| `IDEMPOTENCE_KEY_CONFLICT` | A seen key with a different payload | Yes, with a new key |

The set is open under section 9.9.

Two codes deserve note. `TRUNCATED_BY_BOUND` is a refusal rather than an outcome because a truncated comparison set may not contain the maximal candidate, so returning a selection would be a false claim; clause P5-6.41 states it. The two `CONSTRAINT_VIOLATED` codes are refusals rather than resolutions, per clause P5-3.58, because a Unique or Any constraint is an assertion about the table and its violation is a defect in the table rather than a case for the criterion to settle.

**P5-7.13 (MUST) Refusal codes.** An implementation must return one of the codes above, or a registered code, for every refused decision.

**P5-7.14 (MUST) Refusal states what must change.** An implementation must state, with every refusal, whether the operation may be retried and what must change.

**P5-7.15 (MUST) Refusals recorded.** An implementation must record every refusal with its code, the request and the knowledge time.

**P5-7.16 (MUST NOT) No refusal as an outcome.** An implementation must not return a refusal code in the position of a decision outcome and must not record a refused decision as undecidable.

**P5-7.17 (MUST NOT) No silent retry.** An implementation must not retry a refused decision on its own initiative.

### 7.5 Outcome obligations

Normative.

| Outcome | Component records | Component emits | Caller must |
| --- | --- | --- | --- |
| `DECIDED` | Envelope, candidates, eliminations, comparisons, pins | Decided by criterion | Read the margin before treating the outcome as robust |
| `DECIDED_BY_TIEBREAK` | As above, with the tiebreak and any seed | Decided by tiebreak | Not treat the outcome as determined by policy |
| `DECIDED_BY_DEFAULT` | As above, with the default | Decided by default | Treat the criterion as not having fitted the candidates |
| `DECIDED_EXTERNALLY` | As above, with the deciding actor | Decision completed | Not treat the outcome as produced by the criterion |
| `NO_CANDIDATE` | Envelope with the source and completeness | Decision completed | Investigate the enumeration before concluding anything about policy |
| `NO_ELIGIBLE_CANDIDATE` | As above, with every eligibility verdict | Decision completed | Distinguish candidates that failed from candidates nobody could assess |
| Any `UNDECIDABLE` member | Envelope, every comparison, the maximal set, the cycle where one | The corresponding undecidable event | Route to the remedy owner for that member; nothing will fail to prompt it |
| `UNDECIDED_ELIGIBILITY_INDETERMINATE` | As above, with the `Part 2` subclass and code | Refused for indeterminate eligibility | Obtain the missing information; do not retry unchanged |
| `RETURNED_ALL`, `AGGREGATED` | Envelope with every contributing candidate | Decision completed | Not treat the result as a selection |
| `REFUSED` | Refusal, code, request | Nothing beyond the refusal | Correct the request or escalate |

**P5-7.18 (MUST) Recording obligations honoured.** An implementation must record everything the table above requires for every outcome it produces.

**P5-7.19 (MUST) Emission obligations honoured.** An implementation must emit every event the table above requires.

**P5-7.20 (MUST) Caller obligations documented.** An implementation must document the caller obligations above and must state that it does not enforce them.

**P5-7.21 (MUST NOT) No determinacy language for a non criterion basis.** An implementation must not describe an outcome as determined, required, mandated or dictated by policy in any report, projection or interface where the basis was a tiebreak, a default or an external determination.

**P5-7.22 (MUST NOT) No inference of policy from a default.** An implementation must not describe a defaulted outcome as the outcome the criterion produces for those inputs.

### 7.6 The three things this section is for

Three requirements carry the part. If the rest is compromised by schedule, these survive.

**P5-7.23 (MUST) An arbitrary choice is never a determined one.** An implementation must not, by any mechanism, configuration, default, aggregation, projection, interface, export or summary, represent an outcome produced by a tiebreak, a default, a traversal order, a rule sequence or an undeclared rule as an outcome the criterion determined.

**P5-7.24 (MUST) A failure to determine is never a determination.** An implementation must return the corresponding undecidable member where the criterion did not determine and no declared tiebreak or default applies, and must not select by any other means.

**P5-7.25 (MUST) An unassessable candidate is never an unqualified one.** An implementation must not represent a candidate excluded for an indeterminate eligibility verdict as one that failed to qualify, in any record, report, projection, interface, export or communication to the subject of the decision.
## 8. Observability and the audit record

### 8.1 What the audit record is here

Every decision is a determination in the sense of `Part 3` and is recorded there, with the criterion as its `SELECTION_CRITERION` citation and every unselected candidate as an `ALTERNATIVE_REJECTED` citation. That is where a decision's provenance lives, and this component must not duplicate it.

What this component holds is its own operational record: the criterion artifacts, the run records, the comparisons, the analyses, the assessments and the signals. The division is that `Part 3` holds why a determination was legitimate and what it rested on, and this component holds how the selection was performed and what it would take to perform it again.

The two overlap at the decision record itself, and clause P5-8.2 states the resolution: this component's record is authoritative for the comparisons, the margin and the criterion internals, and `Part 3`'s is authoritative for the determination's citation structure. Section 12.3 states the reciprocal and section 13.4 records that the overlap is the least comfortable boundary in this part.

**P5-8.1 (MUST) Determinations recorded in Part 3.** An implementation must record every decision as a determination with `Part 3`, with the criterion as a selection criterion citation and every unselected candidate as a rejected alternative citation, per clause P3-12.12.

**P5-8.2 (MUST) Division of authority declared.** An implementation must declare that its own record is authoritative for comparisons, margins and criterion internals, and that `Part 3` is authoritative for the determination's citation structure, and must not hold a second citation structure.

**P5-8.3 (MUST NOT) No provenance for other subjects.** An implementation must not record provenance for anything other than its own criteria, decisions and analyses.

**P5-8.4 (MUST) Own operations recorded.** An implementation must record its own recording refusals, analyses, simulations, reproductions, exports and reads as entries.

### 8.2 Grain

| Subject | Grain |
| --- | --- |
| Criterion version | One entry per version. Never amended. |
| Criterion parameter | One entry per parameter per version. |
| Criterion authority | One entry per resolution attempt, not one per version. |
| Precedence order | One entry per version of the order. |
| Criterion approval | One entry per resolution attempt. |
| Criterion analysis | One entry per analysis per version. |
| Decision run | One entry per run. |
| Candidate | One entry per candidate per run. |
| Candidate eligibility | One entry per candidate per run, carrying the whole report by pin. |
| Comparison | One entry per comparison performed. |
| Selection | One entry per run. |
| Elimination | One entry per unselected candidate per run. |
| Pin | One entry per artifact per run. |
| Human involvement | One entry per person per run. |
| Automation assessment | One entry per assessment act. |
| Override | One entry per override. |
| Refusal | One entry per refusal, with one outcome per failed check. |
| Read | One entry per decision, criterion, projection or package returned to a principal. |
| Signal | One entry per signal per observation interval. |

One comparison per entry is the grain that will be resisted on volume grounds and it is required. A decision over twenty candidates under a pairwise criterion performs up to one hundred and ninety comparisons, and the comparison set is what establishes the maximal set, the margin and the presence or absence of a cycle. Recording the outcome without the comparisons makes all three unverifiable, and clause P5-8.6 admits a declared alternative only where the criterion kind makes the comparison set derivable from the scores.

**P5-8.5 (MUST) Declared grain.** An implementation must record at the grain of the table above, or declare a finer grain, and must not record at a coarser one.

**P5-8.6 (MUST) Comparisons recorded or derivable.** An implementation must record every comparison individually, or must declare that the criterion kind makes the comparison set derivable from the recorded scores and record the scores, and must not record neither.

**P5-8.7 (MUST) Authority and approval attempts recorded individually.** An implementation must record every authority and approval resolution attempt as its own entry and must not hold either as a single mutable status.

**P5-8.8 (MUST) Counting grain stated with every count.** An implementation must state the grain of every count it reports.

### 8.3 What must be recorded with every decision

Sufficient to reproduce the outcome and to account for it, without this component running.

Required: the request as received, including the idempotence key; the resolved definition and criterion versions and the mode by which each resolved; every pin with its identity, version and digest; the candidate set with its source, completeness and the basis of that completeness; every candidate with its outcome value digest and attributes pin; every eligibility report by pin; every indeterminate treatment applied with the `Part 2` subclass and code; every comparison; the selection with its basis, margin, scale and marginality; every elimination with its ground; the seed where a random criterion or tiebreak was applied; the calendar and arithmetic conventions in force; every human involvement; the three clocks; and the outcome of every precondition check, including the ones that passed.

**P5-8.9 (MUST) Reproduction sufficiency.** An implementation must record enough with every decision to reproduce it and must treat a decision it cannot reproduce as a defect against clause P5-1.6.

**P5-8.10 (MUST) Request recorded as received.** An implementation must record the request as received and must not record a normalised form in its place.

**P5-8.11 (MUST) Conventions recorded.** An implementation must record the arithmetic, scale and calendar conventions in force for every run, since a comparison cannot be checked without them.

**P5-8.12 (MUST) Precondition outcomes recorded, including passes.** An implementation must record the outcome of every precondition check applied and the version of the precondition set applied.

**P5-8.13 (MUST) Periodic reproduction.** An implementation must attempt reproduction of a declared sample of retained decisions on a declared cycle, must record every divergence and every unobtainable pin, and must declare the sample and the cycle.

**P5-8.14 (MUST) Divergence recorded, not corrected.** An implementation must record a reproduction divergence as a finding about the record and must not amend the original outcome.

### 8.4 Access records

**P5-8.15 (MUST) Reads recorded.** An implementation must record every return of a decision, a criterion version, a projection or an evidence package to a principal, with the principal, the subject, the purpose and the knowledge time.

**P5-8.16 (MUST) Withholding recorded.** An implementation must record a read that was refused or reduced by an authorisation decision, with the decision reference, whether or not the requester was told.

**P5-8.17 (MUST) Simulations recorded with their requester.** An implementation must record the requester and the proposed criterion of every simulation, since a simulation over historical candidate sets reveals how the estate would have decided differently.

**P5-8.18 (SHOULD) Read records retained with the decision.** An implementation should retain the read records of a decision for as long as the decision.

### 8.5 Signals

Each signal measures a way in which this part's guarantees are hollowed out while every individual decision continues to succeed.

| Signal | Grain | Why it matters |
| --- | --- | --- |
| Decisions by basis of selection, by definition | One decision | The proportion the criterion actually determined. A definition mostly defaulted has a criterion that does not fit. |
| Decisions by outcome member | One decision | Where the undecidable members are concentrated. |
| Undecidable outcomes by member and by definition | One decision | Ties, incomparabilities and intransitivities separately, since the remedies differ. |
| Marginal decisions, by definition and criterion | One decision | Where review is worth directing. |
| Weight sensitivities below a declared threshold | One decision | Decisions a small weight change would reverse. |
| Weight sensitivities not computable | One decision | Weighted criteria whose robustness nobody can assess. |
| Candidates excluded for indeterminate eligibility, by `Part 2` subclass | One candidate | A data supply failure presenting as unsuccessful applicants. |
| Decisions in which an indeterminate verdict was included rather than excluded | One decision | Candidates that may have been inadmissible and were selected among. |
| Eligibility resting on a vacuous satisfaction | One candidate | A candidate admitted by a rule that examined nothing. |
| Candidates eliminated as out of scope of the criterion | One candidate | A criterion that cannot see a class of candidate and never will. |
| Criterion parameters of basis `UNJUSTIFIED` or `CONVENTION` | One parameter | Weights nobody can defend, and the number is the only way anyone finds out. |
| Criterion versions unapproved | One version | Criteria in use that nobody accepted responsibility for. |
| Criteria with authority drift open | One version | Criteria applied on a superseded or withdrawn authority. |
| Criterion versions suspended | One version | Decision classes that cannot be decided. |
| Criterion versions refused, by failed precondition | One refusal | Attempts to register selection by rule order, unjustified weights, or an unapprovable criterion. |
| Criteria not statically analysed | One version | Unknown completeness, overlap, subsumption and masking presented as none. |
| Masked rules detected | One rule | Dead policy reviewers will read as live. |
| Incomplete candidate sets, by source kind | One decision | Decisions over a subset of what was available. |
| Empty candidate sets | One decision | Frequently an upstream defect rather than a policy outcome. |
| Overrides, by reviewer and definition | One override | Where the criterion and the people disagree. |
| Override rate by reviewer | One reviewer per interval | A rate near zero is formal review; a rate near one is a criterion nobody uses. |
| Decisions about natural persons with an unassessed automation assessment | One decision | The exposure under the regimes of section 10.5. |
| Decisions assessed `DECISIVELY_AUTOMATED` where a review control exists | One decision | Controls that exist and do not work. |
| Truncated decisions by bound | One decision | Selections that were not made over the whole candidate set. |
| Reproduction divergences and unobtainable pins | One decision | Decay of the evidence base. |
| Decisions not yet recorded with `Part 3` | One decision | The provenance record falling behind. |
| Reads and simulations with no recorded purpose | One read | Erosion of the access record. |

Two of these are the ones an organisation should read first and almost never has.

**Decisions by basis of selection** is the single most diagnostic figure in the part. A definition whose decisions are ninety per cent defaulted has a criterion that does not address its candidates, and nobody notices because every decision produced an outcome.

**Override rate by reviewer** is diagnostic in both directions and is usually read in only one. A rate near zero means the review is formal, which is the finding section 3.16 exists for. A rate near one means the criterion is not the organisation's actual policy and the reviewers are, which is a governance failure of the opposite kind and is equally invisible.

**P5-8.19 (MUST) Signals produced.** An implementation must produce every signal in the table above at a declared interval and must declare the interval.

**P5-8.20 (MUST) Signals derived from entries.** An implementation must derive every signal from recorded entries and must be able to enumerate the entries behind any signal value.

**P5-8.21 (MUST NOT) No suppression of a signal.** An implementation must not provide a means of disabling, filtering or thresholding a signal such that a non zero value is reported as zero.

**P5-8.22 (MUST) Basis distribution produced per definition.** An implementation must produce the basis of selection distribution per decision definition version rather than in aggregate only.

**P5-8.23 (MUST) Override rate reported in both directions.** An implementation must report an override rate below a declared floor and above a declared ceiling as distinct conditions and must declare both.

**P5-8.24 (MUST) Automation exposure standing.** An implementation must produce the unassessed automation signal for natural person subjects continuously rather than on demand.

**P5-8.25 (SHOULD) Signal thresholds declared.** An implementation should declare, for each signal, the value at which it requires attention, and should record the declaration as a controlled document under `Part 1`.

### 8.6 The evidence package

Self describing, sufficient to account for a decision without this component running. This is the package a person is entitled to in some jurisdictions, per section 10.5, and its contents are specified with that in mind.

Contents, all required.

The outcome envelope in full.

The decision definition version with its candidate source declaration, its eligibility binding, its indeterminate treatment with its authority and justification, its collection mode and its marginality threshold.

The criterion version in full: its kind, every statement with its language, every parameter with its value, role, justification and justification basis, its scale and direction, its precedence order or sub criterion order, its authority with its basis and interpretation note, and its approval resolution outcome envelope.

The content of the document version carrying the criterion, and of the clause cited as its authority, obtained from `Part 1`, or the statement that neither could be obtained and why.

Every candidate with its outcome value, its attributes and its elimination ground.

Every eligibility report in full, or the statement that it could not be obtained, with the `Part 2` verdict envelopes it contains.

Every comparison, or the scores from which the comparison set is derivable together with the derivation.

The margin, its scale, the marginality determination and the weight sensitivity or the statement that it was not computable.

The seed and generator where a random criterion or tiebreak was applied.

Every human involvement, the decisive automation assessment with its basis, and every override with its reason and authorisation.

Every pin, with the content of the pinned artifact where obtainable.

The conventions in force: arithmetic, scale comparison and calendar.

The static analysis results for the criterion version, or the statement that none were performed.

The statement of the limits: that the candidate set's completeness is declared rather than established, that the criterion's parameters are justified to the degree recorded and no further, and that no assessment of whether the criterion was the right criterion is made anywhere.

A statement of the version of this part the package claims to conform to.

**P5-8.26 (MUST) Package sufficiency.** An implementation must produce a package sufficient to account for the decision without the implementation running and without access to any component of this standard other than the package.

**P5-8.27 (MUST) Criterion content included or its absence stated.** An implementation must include the content of the criterion document version and of the cited authority clause, or must state that they could not be obtained with the reason and the knowledge time of the attempt.

**P5-8.28 (MUST) Eligibility reports included.** An implementation must include every eligibility report in full, since a candidate's exclusion cannot be accounted for without it.

**P5-8.29 (MUST) Parameter justifications included.** An implementation must include every criterion parameter with its justification and justification basis, so that a reader can see which of the criterion's numbers are defensible.

**P5-8.30 (MUST) Limit statements included.** An implementation must include the limit statements in every package.

**P5-8.31 (MUST) Absence stated, not omitted.** An implementation must state, for every required element it could not include, that it could not be included and why.

**P5-8.32 (MUST) Package digest.** An implementation must record a digest over a declared canonical form of the package and must include the profile identity.

**P5-8.33 (MUST NOT) No package for a non authoritative run.** An implementation must not export a package presenting the outcome of a simulation as a decision, per clause P5-4.14.

**P5-8.34 (MUST) Self description.** An implementation must include a description of the package's structure sufficient for a reader with no knowledge of the implementation to locate each required element.

### 8.7 Retention

**P5-8.35 (MUST) Retention obtained, not assigned.** An implementation must obtain the retention period of every record it holds from a retention rule expressed under `Part 1` and must not assign one of its own.

**P5-8.36 (MUST) Decisions retained with their consequences.** An implementation must retain a decision, its candidates, its comparisons and its pins for at least as long as the record of the act the decision informed, where that period is known to it, and must record where it is not known.

**P5-8.37 (MUST) Criteria outlive their decisions.** An implementation must retain a criterion version's whole artifact set for at least as long as the longest retained decision made under it, since a decision whose criterion has been disposed of cannot be accounted for.

**P5-8.38 (MUST) Eligibility reports retained with the decision.** An implementation must retain, or retain a resolvable pin to, every eligibility report for as long as the decision that consumed it.

**P5-8.39 (MUST) Separate retention per structure.** An implementation must permit the retention of criteria, decisions, comparisons and analyses to be set independently, since the comparison volume exceeds the rest by orders of magnitude.

**P5-8.40 (MUST) Disposal recorded and citable.** An implementation must record the disposal of any record it holds with its authorisation reference and must make the disposal citable as a `Part 3` frontier of kind `RETENTION_EXPIRED`.

**P5-8.41 (MUST NOT) No disposal of a criterion under an open drift observation.** An implementation must not dispose of a criterion version while an authority drift observation against it is open.

### 8.8 What cannot be changed

**P5-8.42 (MUST NOT) No amendment of a decision.** An implementation must not modify a recorded decision, its candidates, its eligibility verdicts, its comparisons, its selection, its margin or its pins by any mechanism, including administrative, migration, correction and support mechanisms.

**P5-8.43 (MUST NOT) No amendment of a criterion version.** An implementation must not modify the kind, statements, parameters, authority or required kind fields of a recorded criterion version.

**P5-8.44 (MUST NOT) No retrospective re basing.** An implementation must not recompute the basis, margin or marginality of a recorded decision under a later criterion version, a later scale registration or a later marginality threshold.

**P5-8.45 (MUST) Migration preserves identity and digests.** An implementation that migrates its records must preserve every criterion identity, every version identity and every recorded digest unchanged, must record the migration as an entry, and must not recompute a digest under a different canonical form profile without recording both.

**P5-8.46 (MUST NOT) No bulk assignment on import.** An implementation must not assign a justification basis, a completeness value, a basis of selection or an automation assessment in bulk during an import, and must record every imported artifact lacking one as carrying the undeclared or unassessed value.
## 9. Extension model

### 9.1 Closed sets, open sets, and why

Five sets in this part are closed.

**The criterion kind set of section 3.7 is closed.** This is the strongest closure in the part. A consumer of a decision must know what guarantees the criterion offers: whether ties are possible, whether cycles are possible, whether an incomparability will be reported or resolved. A kind admitted by registration would be a criterion whose properties no consumer can assume, and the properties are the whole reason the taxonomy exists.

**The outcome set of section 7.2 is closed.** A new member obliges every consumer to grow a branch and the default branch will treat it as decided.

**The elimination ground set of section 3.15 is closed**, because it maps onto an enumeration `Part 3` requires and an unmapped ground cannot be reported there.

**The basis of selection set is closed.** Four values and no more, because the whole point is that the four are distinguishable.

**The indeterminate treatment set of section 3.6 is closed.** A fifth treatment would be a fifth thing to do with a candidate nobody can assess, and there are only four things that can be done.

Everything else is open under a registry: scales, candidate source kinds, decision classes, aggregators, refusal codes, event types, decision purposes, digest algorithms and canonical form profiles.

**P5-9.1 (MUST) Closed sets not extended.** An implementation must not add a member to the criterion kind set, the outcome set, the elimination ground set, the basis of selection set or the indeterminate treatment set.

**P5-9.2 (MUST) Unknown member is a defect, not a default.** An implementation must treat receipt of a member outside a closed set as a defect and must not map it to a member it does recognise.

**P5-9.3 (MUST) Open sets registered.** An implementation must admit a member of an open set only through the registry mechanics of section 9.2 and must not accept an unregistered member at any interface.

**P5-9.4 (MUST NOT) No criterion kind by composition.** An implementation must not compose two criterion kinds into a third and must express a compound criterion as a `LEXICOGRAPHIC` criterion whose sub criteria are of declared kinds.

### 9.2 Registry mechanics

A registry is content of a controlled document version under `Part 1`, so a registration has an effective date, an approval and an author. Keys are permanent and never reused. A member is deprecated rather than removed. Every registration states what the member means, not only what it is called.

**P5-9.5 (MUST) Registry as controlled document.** An implementation must express every registry as content of a document version under `Part 1` and must resolve the registry version in force at the decision instant of any operation that reads it.

**P5-9.6 (MUST NOT) No key reuse.** An implementation must not reuse a registry key and must not remove a member that any retained entry references.

**P5-9.7 (MUST) Deprecation rather than removal.** An implementation must deprecate a member with an effective date and a reason and must continue to interpret entries referencing it.

**P5-9.8 (MUST) Registry version pinned in every run.** An implementation must pin the version of every registry a decision read.

**P5-9.9 (MUST) Semantics in the entry.** An implementation must not admit a registry entry that does not state the meaning of the member in terms a consumer can act on.

### 9.3 Scale registry

This is the most consequential registry in the part, because a scale is what makes a comparison meaningful and a margin interpretable.

A scale registration must state: its identity and version; its value space; its comparison semantics, being whether the ordering is total or partial and how equality is determined; its declared precision, so that a tie can be distinguished from a small margin; its measurement level, being nominal, ordinal, interval or ratio; whether aggregation over it is defined and which aggregators are admissible; and whether differences on it are comparable with differences on any other registered scale, and if so by what declared conversion.

The measurement level is the field that does the work and the one that will be omitted. An ordinal scale admits comparison and does not admit arithmetic: the difference between the third and fourth positions is not a quantity, so summing ordinal values or averaging them produces a number with no meaning. Almost every weighted criterion in ordinary use aggregates over at least one ordinal attribute dressed as a number, typically a quality rating or a risk band, and the aggregate is arithmetic on labels. Clause P5-9.12 requires the level to be declared and clause P5-3.67 requires an aggregation over a scale that does not admit it to be refused rather than computed.

**P5-9.10 (MUST) Scale semantics stated in full.** An implementation must state every element listed above in every scale registration.

**P5-9.11 (MUST) Precision declared.** An implementation must state the precision at which equality is determined on every scale and must use it for tie detection, per clause P5-6.6.

**P5-9.12 (MUST) Measurement level declared.** An implementation must state the measurement level of every scale and must refuse an aggregation or a difference computation over a scale whose level does not admit it.

**P5-9.13 (MUST) Cross scale conversion declared and attributed.** An implementation must record a declared conversion, with an asserting actor, wherever a criterion compares differences on two scales, and must not infer a conversion from the numeric ranges.

**P5-9.14 (MUST NOT) No implicit scale.** An implementation must not admit a score, aggregate or margin whose scale is not recorded, per clause P5-3.5.

### 9.4 Candidate source kind registry

A registration states what the kind is, whether it requires a pin and to what, the completeness semantics of the kind, and whether a caller may supply candidates under it.

The completeness semantics field is where clause P5-3.25 becomes enforceable. A registration for `EXTERNAL_SOLICITATION` declares that completeness is never claimable, and the component then refuses a claim rather than relying on a caller's honesty.

**P5-9.15 (MUST) Completeness semantics declared per kind.** An implementation must record the completeness semantics of every registered candidate source kind and must enforce them.

**P5-9.16 (MUST) Pin requirement declared per kind.** An implementation must record what a source of each kind must pin and must refuse a candidate set lacking it.

**P5-9.17 (MUST NOT) No caller supply under a non caller kind.** An implementation must refuse candidates supplied by a caller for a definition whose source kind does not admit them.

### 9.5 Decision class registry

A class is what makes a decision findable and is what a signal is reported over. A registration states: what kind of decision the class covers; which component owns it; whether its subjects are natural persons; the retention basis; and any class level requirement beyond this part's universal ones, such as a mandatory tiebreak, a prohibited indeterminate treatment or a mandatory human involvement.

The class level requirements are the useful part, on the same basis as `Part 4` section 9.6. A class of decision about a person's entitlement may be registered as prohibiting an `EXCLUDE_CANDIDATE` treatment and requiring a human involvement of at least `REVIEWED_AND_ACCEPTED`, which turns a governance expectation into a precondition the component enforces.

**P5-9.18 (MUST) Class requirements declared and enforced.** An implementation must record any class level requirement beyond this part's universal ones and must refuse a definition or a decision that does not satisfy it.

**P5-9.19 (MUST) Natural person subject declared per class.** An implementation must record whether the subjects of a class are natural persons and must refuse a definition of the class whose declaration disagrees.

**P5-9.20 (MUST) Owning component per class.** An implementation must record which component owns each class and must refuse a definition of a class from a component that does not own it.

**P5-9.21 (MUST) Retention basis per class.** An implementation must record the retention basis for each class, per section 8.7.

### 9.6 Aggregator and purpose registries

An aggregator registration states the function, the measurement levels of scale over which it is defined, its behaviour on an empty input, and its behaviour where a contributing value is absent. The last two are the fields that matter: a sum over an empty set is zero and a maximum over an empty set is undefined, and an aggregator whose empty behaviour is not declared will return one or the other silently.

A purpose registration states why a decision is requested. The purposes that must be distinguished, at minimum: a decision informing an act about to be taken; a retrospective decision about a past state; a simulation under a proposed criterion; a reproduction of a recorded decision; and a decision made in the course of an assessment by `Part 12`.

**P5-9.22 (MUST) Aggregator definedness declared.** An implementation must state, for every registered aggregator, the measurement levels over which it is defined and its behaviour on an empty input and on an absent contributing value.

**P5-9.23 (MUST) Purposes registered and recorded.** An implementation must register every purpose and must record the purpose of every decision.

**P5-9.24 (MUST) Minimum purpose distinctions.** An implementation must register at least the five purposes named above as distinct members.

**P5-9.25 (MUST NOT) No default purpose.** An implementation must not default the purpose of a decision and must refuse a request that omits it.

### 9.7 Digest and canonical form registries

**P5-9.26 (MUST) Both registered and both recorded.** An implementation must register digest algorithms and canonical form profiles separately and must record both with every digest.

**P5-9.27 (MUST) Deprecation without invalidation.** An implementation must be able to deprecate a digest algorithm without invalidating any recorded digest and must record an additional digest under a current algorithm rather than replacing the original.

**P5-9.28 (MUST NOT) No digest without a profile.** An implementation must not record a digest whose canonical form profile is not recorded.

### 9.8 Code and event registries

**P5-9.29 (MUST) Refusal codes registered with remedy.** An implementation must state, in every refusal code registration, whether the operation may be retried and what must change.

**P5-9.30 (MUST) Event types registered.** An implementation must register every event type it emits beyond the minimum set of section 4.7.

### 9.9 Composition of criteria and decisions

Four compositions are distinguished and one is prohibited.

**A lexicographic criterion over sub criteria.** The only composition of criteria this part provides. Each sub criterion is a criterion version in its own right, subject to every requirement of sections 3.7 and 3.8, and the order of application is declared. Order independence is preserved because the order is over criteria, which is a governable artifact, rather than over rules or candidates.

**A decision consuming the outcome of an earlier decision.** Permitted, as a pinned input recorded as such. The earlier decision is cited, its outcome is used, and the citation is what makes a correction to the earlier decision reach the later one through `Part 3`'s defect propagation.

**A decision whose candidate source is the outcomes of a set of earlier decisions.** Permitted, per section 3.5, and it is the composition by which a portfolio decision is made over individual ones. The completeness of the candidate set is the completeness of the enumeration of those decisions.

**A criterion whose parameters are derived from a pinned computation.** Permitted, provided the computation's output is a pinned artifact recorded as a parameter with its justification citing the computation. The distinction from clause P5-6.46 is that a parameter derived once and recorded as a version is governed, and a parameter recomputed per decision is not.

**A criterion that reads another decision's outcome as a term.** Prohibited. A criterion whose value depends on what a concurrent decision concluded creates an ordering between decisions that nothing declares, and the ordering then determines both outcomes. The remedy is the second composition above: obtain the earlier decision's outcome, pin it, and cite it, which makes the dependency explicit and acyclic.

**P5-9.31 (MUST) Lexicographic composition only.** An implementation must express a compound criterion as a `LEXICOGRAPHIC` criterion over declared sub criterion versions in a declared order.

**P5-9.32 (MUST) Prior decision outcomes pinned and cited.** An implementation must record a prior decision's outcome consumed by a later decision as a pinned input citing that decision, so that a correction propagates.

**P5-9.33 (MUST NOT) No criterion reading a concurrent decision.** An implementation must not admit a criterion whose evaluation requires the outcome of a decision not already recorded and pinned.

**P5-9.34 (MUST NOT) No cyclic decision dependency.** An implementation must refuse a decision whose pinned prior decision citations would create a cycle.

**P5-9.35 (MUST) Derived parameters recorded as versions.** An implementation must record a parameter derived from a computation as a recorded parameter of a criterion version with a justification citing the computation, and must not recompute it per decision.

**P5-9.36 (MUST) Composition depth bounded and declared.** An implementation must declare the maximum depth of sub criterion nesting and of prior decision chaining it accepts and must refuse anything exceeding it.
## 10. Standards and specifications

### 10.1 How the citations in this part are to be read

Every entry states what the source supplies, the edition established as current at the date of this part, and whether this part's account rests on specification text or on secondary sources. Section 13.1 lists the sources not obtained.

Three findings bear on how a reader should treat this section. The principal standard for decision logic has a formal version and two later betas, so a citation without a version does not identify a document. The best normative treatment of combining several verdicts into one outcome is in an authorisation standard this part deliberately does not adopt. And the regulatory position on automated decisions about persons was, at the date of this part, subject to a legislative proposal whose outcome could not be established.

**P5-10.1 (MUST) Cited edition recorded.** An implementation must record the edition or version of every external standard it relies upon and must not cite a standard without its edition.

**P5-10.2 (MUST) Basis marked.** An implementation must record, for every control it adopts from a source named in this section, whether the basis is specification text or practice.

### 10.2 Decision modelling: DMN

| Standard | Status established | Supplies |
| --- | --- | --- |
| DMN 1.5 | Current formal version, adopted August 2024. Betas 1.6 and 1.7, both dated September 2024, are in process; 1.7 is the latest inventory and is marked informational. Prior formals 1.4 (April 2023), 1.3, 1.2, 1.1, 1.0. | Decision requirements diagrams and the decision requirements graph. Decision tables with input and output expressions. The seven hit policies. The FEEL expression language. Completeness as a configurable requirement on a table. |

The seven hit policies, established from the specification clause on hit policy as reported in secondary sources and from multiple independent implementation accounts, are: Unique, Any, Priority and First as single hit policies, and Collect, Output order and Rule order as multiple hit policies, with Collect admitting aggregators for sum, count, minimum and maximum.

Four properties of the hit policies are established and are the basis of section 3.9.

**Priority returns the matching output that comes first in a supplied list of output values.** The priority is a property of the output value list and is therefore independent of rule sequence. The specification constrains priority tables to enumerated output values, and an else rule's output must be the lowest priority value.

**Output order returns the matching outputs ordered by the same output value list.** Also independent of rule sequence.

**First returns the first match in rule order.** The criterion is the sequence of rules.

**Rule order returns the matching outputs in rule order.** Also the sequence of rules.

That division is the whole of section 3.9's analysis. Two of the four selecting policies order outcome values, which is a governable artifact; two order rules, which is a physical property of a table's layout. This part admits the first two as instances of the `PRECEDENCE_OVER_OUTCOMES` criterion kind and refuses the second two, and section 13.3 records the divergence.

Also established, from implementation guidance and commentary rather than from the specification: overlapping rules under Unique is an error; a table with no overlap assigned to Any or Priority is a mistake though technically legal; incomplete tables with gaps, and subsumption where rules could be contracted, are recognised defects. Those four are the basis of section 6.4's analyses. The specification's own treatment of completeness as a configurable requirement rather than a mandatory property is noted and diverged from: this part treats completeness as an analysis result that must be recorded either way.

The account of DMN in this part rests on the publisher's version inventory, obtained directly, and on secondary sources for the hit policy semantics. The specification text was not obtained. Section 13.1 records this and it is the most load bearing unverified claim in the part.

### 10.3 Combining several results into one: XACML

| Standard | Status established | Supplies |
| --- | --- | --- |
| XACML 3.0 Plus Errata 01 | OASIS Standard incorporating Approved Errata, 12 July 2017. | Twelve standard combining algorithms in a normative appendix: deny overrides, ordered deny overrides, permit overrides, ordered permit overrides, deny unless permit, permit unless deny, first applicable, only one applicable, and four legacy variants retained for compatibility. Extended indeterminate values. |

XACML is an authorisation standard and section 12.7 allocates authorisation to `Part 7`. It is cited here because it contains the best normative treatment found anywhere of the problem this part exists for: given several results, produce one, by a named and specified rule.

Three features bear directly on this part's design.

**The combining algorithm is a named, identified artifact.** A policy declares which algorithm combines its rules, by identifier. That is precisely the position section 3.7 takes: the rule of combination is a thing with a name that can be pointed at, rather than a behaviour of the engine.

**Only one applicable returns indeterminate where more than one policy applies.** It does not choose. That is a normative precedent for the position section 7.2 takes with its undecidable members: an engine may be specified to refuse to arbitrate and to say so.

**Extended indeterminate values record what the result could have been.** Where a policy could not be evaluated, XACML distinguishes an indeterminate that could only have been deny, one that could only have been permit, and one that could have been either. That is a considerably more sophisticated treatment of the third value than merely reporting it, and it is the closest thing in any reviewed standard to an answer to the indeterminate candidate problem of section 3.6. This part does not adopt it, because a candidate's eligibility being indeterminate does not carry a comparable set of possible values, and section 13.6 records that the idea may transfer better than this part assumes.

The account rests on the standard's table of contents and normative appendix headings, obtained, and on secondary description of the algorithms' behaviour. The appendix text was not obtained.

### 10.4 Production rules and conflict resolution

| Specification | Status established | Relevance |
| --- | --- | --- |
| RIF-PRD Second Edition | W3C Recommendation, 5 February 2013. Established in `Part 2` section 10.3. | A normative operational semantics for production rules: match, conflict resolution, act, loop. The conflict resolution step is precisely what `Part 2` fenced out and this part owns. |
| PRR 1.0 | OMG, adopted 2009. Established in `Part 2` section 10.2. | A production rule metamodel, in which conflict resolution is intrinsic. |
| SBVR 1.5 | OMG, formal, December 2019. Established in `Part 2` section 10.2. | Enforcement level as a graded scale independent of the rule. Relevant here because an enforcement level is not a criterion and must not be used as one; see section 11.9. |

`Part 2` excluded conflict resolution from constraint evaluation and named RIF-PRD as the specification defining what it was excluding. This part takes the other side of that boundary: conflict resolution is a criterion, and the requirement this part adds to RIF-PRD's treatment is that the strategy be an artifact with an authority rather than a property of the engine or a salience integer on a rule.

### 10.5 Automated decisions about natural persons

This subsection is the reason section 3.16 exists and it is the part of section 10 most likely to be out of date by the time it is read.

| Instrument | Status established | Supplies |
| --- | --- | --- |
| GDPR, Regulation (EU) 2016/679, Article 22 | In force. | A right not to be subject to a decision based solely on automated processing, including profiling, producing legal effects or similarly significant effects, subject to exceptions for explicit consent, contractual necessity and explicit legal authorisation. Articles 13(2)(f) and 14(2)(g) require the existence of automated decision making to be disclosed. Recital 71 is the basis on which a right to explanation is generally argued. Article 15 gives a right of access, Article 21 a right to object, Article 35 a data protection impact assessment obligation. |
| Court of Justice of the European Union, Case C-634/21 | Decided December 2023. | The criterion that a decision is automated under Article 22 where the final decision was **decisively based** on a preceding automated determination, even where the person involved had formal and substantive decision making power. This is the test section 3.16 adopts for decisive automation. |
| EU AI Act, Regulation (EU) 2024/1689 | In force. Application phased. Article 12 requires automatic logging of system operation; Article 14 requires high risk systems to permit effective human oversight by natural persons; Article 26 imposes deployer obligations including, at Article 26(11), informing natural persons subject to a high risk system; Article 50 imposes transparency obligations. Article 2(7) provides that the Act applies alongside the GDPR without affecting its scope. | Human oversight as a design obligation on the system rather than a right of the subject, and logging as a system requirement. |

**A live uncertainty that could not be resolved.** The obligations for high risk systems, including the Article 14 human oversight requirement, were scheduled to apply from 2 August 2026. A European Commission Digital Omnibus package was, at the date of this part, under discussion, proposing to make the application of the high risk obligations conditional on the availability of harmonised technical standards, with deadlines no later than December 2027 or August 2028 depending on classification. Whether that proposal has been enacted, and therefore whether the Article 14 obligations are in application as at the date of this part, **could not be established**. Section 13.1 records this and clause P5-10.3 requires an implementation to establish the position for itself rather than relying on this section.

Three design consequences follow and each is a clause elsewhere in this part.

The distinction between human involvement and decisive automation, per section 3.16, follows from Case C-634/21. A record showing that a person approved the outcome does not establish that the decision was not automated, and an organisation relying on such a record has a control that does not do what it believes.

The requirement that the elimination ground distinguish a candidate that failed from one nobody could assess, per clause P5-7.25, follows from the disclosure obligations. Telling a person they did not qualify when in fact their eligibility could not be established is a false statement about a decision they have a right to be informed about.

The evidence package of section 8.6, containing the criterion, its parameters and their justifications, is specified with the explanation obligations in mind. Whether it satisfies them is a legal question this part does not answer.

Also reported and not assessed: three United States state instruments imposing automated decision obligations, being the Colorado AI Act, the California automated decision making technology regulations and the Texas Responsible AI Governance Act. Section 13.1 records that none was examined.

**P5-10.3 (MUST) Regulatory position established independently.** An implementation must establish, for each jurisdiction in which it operates, which obligations attach to a decision about a natural person, must record what it established and when, and must not rely on this section as a statement of the position in force.

### 10.6 Decision theory and social choice

These are not standards and are cited as literature. Sections 6.3 and 3.7 depend on them.

| Source | Supplies |
| --- | --- |
| Arrow's impossibility theorem | The result that no rule aggregating individual orderings into a collective ordering satisfies a small set of individually reasonable conditions simultaneously. The consequence adopted here is that every aggregation rule embeds a choice not derivable from the inputs, which is the definition of a criterion in section 1.3. |
| The Condorcet paradox | The specific result that pairwise majority comparison can produce a cycle, so that no candidate is maximal. The basis of the `UNDECIDABLE_INTRANSITIVE` outcome. |
| Pareto dominance | The relation underlying the `DOMINANCE_ONLY` criterion kind and the definition of incomparability in section 2.1. |
| The analytic hierarchy process and the rank reversal critique of it | Cited as the best known cautionary case for weighted aggregation: a method in wide use whose outcomes can reverse on the addition or removal of an irrelevant alternative. Relevant to the weight sensitivity requirement of clause P5-3.91 and not adopted as a method. |
| Measurement theory on levels of measurement | The basis of the requirement in clause P5-9.12 that a scale declare its measurement level and that arithmetic over an ordinal scale be refused. |

The account of each rests on general knowledge of settled results rather than on a cited edition, and section 13.1 records that no primary source was obtained for any of them.

### 10.7 Adjacent standards deliberately not used

| Standard | Why not used here |
| --- | --- |
| BPMN | Process orchestration. Belongs to `Part 6`. DMN is designed to be usable alongside it and this part uses neither for control flow. |
| ISO 31000 and IEC 31010 | Risk management and risk assessment techniques, the latter including decision analysis methods. Cited as containing techniques rather than requirements; adopting them would put method selection in scope, which section 1.2 excludes. |
| ISO/IEC 42001 and ISO/IEC 23894 | Artificial intelligence management and risk. Relevant to inferential models and allocated to `Part 13`, with the interface governed by `Part 4`. |
| Business Motivation Model | The relation of decisions to goals. Out of scope: this part specifies how a selection is made, not why the organisation wants that outcome. |

### 10.8 Supporting specifications

| Specification | Used for |
| --- | --- |
| RFC 2119 and RFC 8174 | Requirement keywords. |
| BCP 47 | Language tags on every criterion statement. |
| RFC 3339 and ISO 8601 | Instant representation for the three clocks. |
| RFC 8785 | An example of a canonical form profile of the kind section 9.7 requires. |
| RFC 9457 | A model for conveying a refusal of the kind section 7.4 specifies. |
| CloudEvents | A model for the event envelope of section 4.7. |

The following clauses rest on practice rather than specification text and are collected so a reader can see the set: clause P5-3.49 on requiring a justification for every parameter; clause P5-3.53 on a declared authority drift cycle; clause P5-3.91 on the weight perturbation; clause P5-3.93 on a declared marginality threshold; clause P5-3.106 on rate inferred automation assessment; clause P5-4.13 on simulation over historical candidate sets; clause P5-6.4 on exact decimal arithmetic for comparison; clause P5-8.13 on periodic reproduction; and clause P5-8.23 on reporting an override rate in both directions.

**P5-10.4 (MUST) Practice basis recorded.** An implementation that adopts a clause listed in the paragraph above as a control must record that its basis is practice.

### 10.9 Named conflicts

Five conflicts bear on this part. None is resolved by averaging.

**Whether rule order may be a criterion.** DMN provides First and Rule order, which select by the sequence of rules, and First is the most used hit policy in practice. **Position taken.** Refused, by clause P5-3.59, because a sequence of rows is not a governed artifact and a policy change effected by inserting a row is a policy change nobody approved. Section 13.3 records the cost.

**Whether completeness is optional.** DMN treats the completeness of a decision table as a configurable requirement, so an incomplete table is valid. **Position taken.** Completeness is an analysis result that must be recorded either way, per clause P5-6.25, together with what will happen in the unaddressed cases. This is a strengthening rather than a contradiction.

**Whether an engine may refuse to arbitrate.** XACML's only one applicable algorithm returns indeterminate where more than one policy applies, so a standard already contemplates refusal. Production rule semantics, in RIF-PRD and PRR, make conflict resolution intrinsic, so an engine always resolves. **Position taken.** Refusal is a first class outcome, per section 7.2, and there is no residual fallback, per clause P5-6.13. This follows XACML rather than the production rule tradition.

**Whether the third value carries information about what it could have been.** XACML's extended indeterminate values record the set of results that were possible. This part records the `Part 2` indeterminacy subclass and code and does not record a possible outcome set. **Position taken.** Not adopted, and recorded in section 13.6 as possibly a mistake, since the information is available for eligibility and would make an inclusion or exclusion treatment better founded.

**Whether human involvement establishes that a decision is not automated.** The GDPR's Article 22 is framed around decisions based solely on automated processing, which reads as satisfied by any human involvement. The Court of Justice applied a substantive test in Case C-634/21, holding that the question is whether the final decision was decisively based on the automated determination. **Position taken.** The substantive test, per section 3.16, with the assessment held separately from the record of involvement and defaulting to unassessed.

### 10.10 What none of the standards supplies

Eleven requirements in this part have no source in any reviewed standard.

The separation of eligibility from preference as two artifacts with two owners, per section 3.2.

The treatment of a candidate whose eligibility is indeterminate, and the requirement that the treatment be declared per `Part 2` indeterminacy subclass with an authority.

The closed criterion kind taxonomy, and in particular the `DOMINANCE_ONLY` kind, which is the only kind that never resolves an incomparability.

The requirement that every criterion parameter carry a justification and a justification basis, and that an unjustified weight be countable as one.

The three undecidable outcomes as distinct first class members, and the detection of intransitivity in particular.

The prohibition on selection by rule sequence.

Margin, as a per kind computation, and marginality against a declared threshold.

The weight perturbation that would reverse a weighted decision.

The distinction between human involvement and decisive automation as separately recorded facts, and the override rate as evidence bearing on the latter. The legal test exists; nothing in any technical standard records against it.

The declared completeness of the candidate set, and the treatment of a solicitation based source as never complete.

Simulation of a proposed criterion over historical candidate sets, reporting the outcomes on which it would fail to determine.

**P5-10.5 (MUST) Unsourced requirements identified.** An implementation must be able to state, for any control it implements under this part, whether the requirement has a cited source in this section or is listed in section 10.10 as unsourced.
## 11. Anti patterns

Each entry names the mechanism by which the failure occurs, states the consequence, and marks whether the prohibition rests on specification text or on practice.

### 11.1 The criterion that is the code

**Mechanism.** The selection logic is a function. It sorts, it compares, it returns the first element. There is no criterion artifact, no version, no authority and no statement, and the policy exists only as a release.

**Consequence.** The organisation cannot state its own selection policy, cannot date a change to it, and cannot answer why a past decision went as it did without reading source control. Every property this part specifies is unavailable at once.

**Basis.** Specification text, in that `Part 2` section 12.5 allocates selection here precisely so that the criterion can be an artifact.

**P5-11.1 (MUST NOT) No criterion outside the model.** An implementation must obtain every criterion as a versioned artifact with an authority and must not apply one expressed as code or configuration, per clause P5-1.2.

### 11.2 The implicit tiebreak

**Mechanism.** The criterion leaves two candidates equal. The implementation returns one of them, because it had to return something. Which one it returns is determined by the sort's stability, the collection's iteration order, or the row that happened to be read first.

**Consequence.** The organisation has a tiebreak policy and does not know what it is. The policy changes when the data store's ordering changes, when a query plan changes, or when a library is upgraded, and none of those is a policy change anybody approved. The decision remains reproducible only by accident.

**Basis.** Practice.

**P5-11.2 (MUST NOT) No undeclared tiebreak.** An implementation must return the undecidable tie outcome where no tiebreak is declared and must not select by any means the criterion or a declared tiebreak did not specify, per clauses P5-3.16 and P5-6.13.

### 11.3 The default that looks like a decision

**Mechanism.** The criterion addresses most cases. For the rest a fallback returns a sensible outcome. The record shows an outcome and does not show which produced it.

**Consequence.** A criterion that fits half its cases is indistinguishable from one that fits all of them, and nobody discovers that half the organisation's decisions of a class are made by a line of fallback logic. The signal that would reveal it, the distribution of decisions by basis, does not exist because the basis was never recorded.

**Basis.** Practice.

**P5-11.3 (MUST) Basis recorded on every outcome.** An implementation must record whether an outcome was produced by the criterion, a tiebreak or a default, and must produce the basis distribution per definition, per clauses P5-3.83 and P5-8.22.

### 11.4 Selection by row order

**Mechanism.** A decision table with overlapping rules and a first match policy. It is easy to read, it is the most used hit policy in practice, and the criterion is the order of the rows.

**Consequence.** Somebody inserts a row for readability and the organisation's decisions change. The change has no author, no approval, no effective date and no record, because moving a row is not a policy act in anybody's process. The table's behaviour is a property of its layout.

**Basis.** Specification text, in that DMN's own Priority policy orders output values rather than rules and thereby shows the alternative.

**P5-11.4 (MUST NOT) No selection by rule sequence.** An implementation must not implement a First or Rule order policy and must express the same table as a precedence over enumerated outcome values, per clauses P5-3.59 and P5-3.60.

### 11.5 The weights that resolve an incomparability silently

**Mechanism.** Two candidates differ on price and on delivery time, and neither dominates. A weighted aggregate returns a winner, because the weights supplied the rate of exchange between money and time.

**Consequence.** A genuine incommensurability was resolved by two numbers, and the numbers are frequently conventional. The decision looks determinate, the record shows a margin, and the margin is an artefact of the weights rather than a fact about the candidates. Nothing indicates that under a dominance criterion the decision would not have been made at all.

**Basis.** Literature, in Arrow's result that every aggregation rule embeds a choice not derivable from the inputs.

**P5-11.5 (MUST) Weights justified and sensitivity recorded.** An implementation must record a justification and basis for every weight and must record the perturbation that would reverse the outcome, per clauses P5-3.49 and P5-3.91.

### 11.6 The cycle resolved by iteration

**Mechanism.** A pairwise preference relation contains a cycle. The implementation iterates the candidates comparing each against the current best, and returns whatever it ends with, which depends on where it started.

**Consequence.** The criterion is not an ordering and the engine reports as though it were. The outcome depends on traversal, so it is not reproducible under a different traversal, and the condition is a known mathematical possibility rather than a defect that testing will find.

**Basis.** Literature, in the Condorcet paradox.

**P5-11.6 (MUST NOT) No cycle resolution by traversal.** An implementation must detect a cycle, must record its members, must return the intransitive outcome, and must not resolve it by traversal order or an iteration limit, per clauses P5-6.17 and P5-6.19.

### 11.7 The empty set reported as a policy outcome

**Mechanism.** The candidate enumeration returns nothing, because a query was wrong, a feed was late or a filter was too narrow. A default fires and an outcome is recorded.

**Consequence.** An upstream defect is recorded as a policy outcome. The default was written for the case where nobody qualified, and it is applied to the case where nobody was asked. The two are recorded identically and the defect is invisible for as long as the default is tolerable.

**Basis.** Practice.

**P5-11.7 (MUST) Empty cases distinguished and defaults scoped.** An implementation must distinguish an empty candidate set from an empty admissible set and must not apply a default to a case its declaration does not name, per clauses P5-6.11 and P5-3.72.

### 11.8 The unassessable candidate recorded as unqualified

**Mechanism.** A candidate's eligibility could not be established, because an attribute was withheld or a reference set was unavailable. The candidate is excluded and recorded as ineligible.

**Consequence.** The person or party the candidate represents is told they did not qualify, which is false: nobody could tell. Where the subject is a natural person this is a false statement about a decision they may have a right to be informed about, and section 10.5 records the obligations. It is also a data supply failure recorded as a policy result, so the failure is never fixed.

**Basis.** Specification text, in that `Part 2` sections 7.1 and 7.2 exist to keep the third value distinguishable to exactly this point.

**P5-11.8 (MUST NOT) No indeterminate as ineligible.** An implementation must record `ELIGIBILITY_INDETERMINATE_EXCLUDED` where a candidate was excluded for want of an eligibility verdict and must not represent it as a failure to qualify, per clauses P5-3.98 and P5-7.25.

### 11.9 Enforcement level used as a criterion

**Mechanism.** Rules carry an enforcement level, per SBVR. Where two rules conflict, the one with the stricter level wins.

**Consequence.** The enforcement level is a statement about what to do when a rule is breached, not a statement about which rule prevails. Using it as a precedence order means changing how strictly a rule is enforced changes which rules apply, so two unrelated policy dimensions are welded together and neither can be adjusted alone.

**Basis.** Specification text, in that SBVR treats enforcement level as independent of the guidance the rule gives, and `Part 2` clause P2-3.60 forbids acting on it.

**P5-11.9 (MUST NOT) No enforcement level as precedence.** An implementation must not use a `Part 2` enforcement level as a criterion, a precedence order or a tiebreak, and must require an authority precedence to be a declared order over authorities.

### 11.10 The score that is also the gate

**Mechanism.** Candidates are scored and any candidate below a threshold is excluded. The threshold does the work of an eligibility rule and the score does the work of a preference.

**Consequence.** Two policies are entangled in one number. Changing the eligibility threshold shifts the selection among the remaining candidates, because the same score orders them. Changing the preference changes who is admissible. Neither change is visible as what it was, and the eligibility rule has no statement, no authority and no verdict record.

**Basis.** Practice.

**P5-11.10 (MUST NOT) No eligibility by score threshold.** An implementation must obtain every exclusion for inadmissibility from a `Part 2` verdict and must not exclude a candidate by a threshold on a criterion score, per clause P5-3.8.

### 11.11 The criterion that cannot see a class of candidate

**Mechanism.** A precedence order over outcome values omits a value, or a score function requires an attribute some candidates lack. Those candidates are eligible and are never selected.

**Consequence.** A class of candidate is excluded permanently by an omission rather than by a policy, and the exclusion is invisible because the candidates appear in the set and simply never win. In a supplier selection this is a category of supplier that can never be chosen; in a decision about people it is a category of person.

**Basis.** Practice.

**P5-11.11 (MUST) Out of scope candidates reported.** An implementation must record a candidate the criterion cannot address as eliminated out of scope, must emit the event, and must count it, per clause P5-3.100.

### 11.12 The masked rule

**Mechanism.** A decision table contains a rule that can never be selected, because every case it matches is also matched by a rule the precedence prefers.

**Consequence.** Dead policy that reviewers read as live. A reviewer confirms that the table handles a case, the case is handled by a rule that never fires, and the actual outcome is something else. This is worse than a redundant rule, because a redundant rule produces the same answer and a masked one does not.

**Basis.** Specification text, in that masking is a recognised decision table defect.

**P5-11.12 (MUST) Masking analysed and reported.** An implementation must analyse masking over every criterion version whose form admits it and must report every rule that can never be selected, per clauses P5-6.22 and P5-6.24.

### 11.13 The review that never overrides

**Mechanism.** A control requires a person to approve every decision. The person approves every decision, because the mechanism is usually right and because overriding requires a justification and the approval does not.

**Consequence.** The control exists and does nothing. The organisation believes its decisions are human decisions and they are decisively automated in the sense Case C-634/21 describes. Where the subject is a natural person the belief may be legally consequential, and nothing in the record contradicts it because the record shows a human involvement on every decision.

**Basis.** Specification text, in the substantive test the Court of Justice applied, and practice for the mechanism.

**P5-11.13 (MUST) Automation assessed separately from involvement.** An implementation must hold a decisive automation assessment separate from the record of involvement, must default it to unassessed, and must be able to report an override rate by reviewer, per clauses P5-3.105 and P5-3.107.

### 11.14 The override that erases the criterion's outcome

**Mechanism.** A reviewer disagrees with the outcome and changes it. The record shows the outcome the reviewer chose.

**Consequence.** The criterion's outcome is gone, so nobody can measure how often the criterion and the reviewers disagree, and nobody can tell whether the criterion is wrong or the reviewers are. The override rate signal, which is the only evidence bearing on both, cannot be computed.

**Basis.** Practice.

**P5-11.14 (MUST NOT) No override without the original.** An implementation must retain the outcome the criterion produced alongside any override, per clauses P5-3.110 and P5-4.18.

### 11.15 The criterion tuned on outcomes

**Mechanism.** The weights are adjusted until the decisions come out as the people making them would have decided. Each adjustment is small and reasonable.

**Consequence.** The criterion is now a fitted approximation to a set of past judgements, its parameters have no authority beyond having produced agreeable results, and the justifications on them are false. The organisation has an unexaminable policy that looks like a governed one, and the tuning has no version history because it was configuration.

**Basis.** Practice.

**P5-11.15 (MUST NOT) No tuning on outcomes.** An implementation must not adjust a criterion, a weight or a precedence order on the basis of recorded outcomes or overrides and must require every change to be a recorded criterion version, per clause P5-6.46.

### 11.16 The candidate set that is the market

**Mechanism.** Three suppliers responded to a solicitation. The record says three candidates were considered and the best was chosen.

**Consequence.** The decision is presented as a choice among the available options when it was a choice among the responses. The suppliers who did not respond are not candidates, are not recorded, and are not knowable, and the completeness of the set is the single most important qualification on the outcome.

**Basis.** Practice.

**P5-11.16 (MUST) Solicitation sets recorded incomplete.** An implementation must record a candidate set of a solicitation based source kind as incomplete, must refuse a claim that it is complete, and must carry the completeness onto the selection, per clauses P5-3.25 and P5-3.87.

### 11.17 Arithmetic on labels

**Mechanism.** A quality rating on a five point scale is one of the attributes in a weighted aggregate. The rating is stored as an integer and is multiplied by a weight.

**Consequence.** The aggregate performs arithmetic on an ordinal scale, where the difference between three and four is not a quantity. The resulting number is not a measure of anything and the margins computed from it are meaningless, so the marginality flag is noise. This is present in a substantial proportion of weighted criteria in ordinary use.

**Basis.** Literature, in measurement theory on levels of measurement.

**P5-11.17 (MUST) Measurement level enforced.** An implementation must record the measurement level of every scale and must refuse an aggregation or difference computation over a scale whose level does not admit it, per clauses P5-9.12 and P5-3.67.

### 11.18 The tie resolved at the wrong precision

**Mechanism.** Two scores are compared in binary floating point. They differ in the fifteenth decimal place. The engine reports a margin and selects.

**Consequence.** A tie is reported as a decision, so the declared tiebreak never runs and the outcome is determined by rounding. On a different platform, a different library version or a different order of operations, the outcome differs. The decision is not reproducible and appears to be.

**Basis.** Practice.

**P5-11.18 (MUST) Exact arithmetic and declared precision.** An implementation must use exact decimal arithmetic for comparison and must detect a tie at the precision the scale declares, per clauses P5-6.4 and P5-6.6.

### 11.19 The truncated decision reported as a selection

**Mechanism.** The candidate set is large. A bound is reached. The best of those compared is returned.

**Consequence.** The selected candidate may not be the maximal one and the record does not say so. This is materially different from a truncated evaluation in `Part 2`, where the unevaluated rules yield indeterminate verdicts; here the unexamined candidates are simply absent from a result presented as a choice among all of them.

**Basis.** Practice.

**P5-11.19 (MUST NOT) No selection from a truncated set.** An implementation must return the truncation refusal where a bound was reached before every required comparison and must not return a selection, per clause P5-6.41.

### 11.20 The decision engine that became the policy decision point

**Mechanism.** The component decides business outcomes. Somebody notices it could also decide whether an operation is permitted, and it already has the criteria machinery.

**Consequence.** The two decision kinds have different requirements. An authorisation decision carries obligations, has a specified indeterminate treatment, has its own combining algorithms and must be enforceable at a policy enforcement point. Merging them means neither set of requirements is met, and an authorisation becomes a business selection with no obligations model.

**Basis.** Specification text, in that XACML specifies the authorisation model this component does not implement and section 12.7 allocates authorisation to `Part 7`.

**P5-11.20 (MUST NOT) No authorisation decisions.** An implementation must not produce an outcome that is an entitlement to perform an operation and must obtain every authorisation decision from `Part 7`.

### 11.21 The eligibility evaluated inline

**Mechanism.** The decision needs to know which candidates are admissible. Calling `Part 2` per candidate is a round trip per candidate, so the conditions are evaluated inline.

**Consequence.** This is the second naive conflation `Part 2` section 12.5 names. The conditions have no rule identity, no statement, no authority, no enforcement level and no verdict taxonomy. The three valued outcome is gone, so an unevaluable condition becomes a false one, and every candidate whose data was incomplete is silently ineligible.

**Basis.** Specification text, in `Part 2` section 12.5 and clause P2-12.9.

**P5-11.21 (MUST NOT) No inline eligibility.** An implementation must obtain every eligibility verdict from `Part 2` as a whole evaluation report and must not evaluate a condition itself, per clauses P5-1.4 and P5-3.29.

### 11.22 The model score as the criterion

**Mechanism.** An inferential model produces a score and the highest score wins. The criterion is the model.

**Consequence.** The criterion has no statement anybody can read, no parameters anybody can justify, and no authority, and its behaviour changes when the model is retrained. The decision is not reproducible unless the model version is pinned, and it is not explainable in the terms this part requires because the reason one candidate beat another is inside the model.

**Basis.** Practice, and specification text in that `Part 4` section 3.12 governs the model interface and `Part 13` owns its invocation.

**P5-11.22 (MUST) Model output pinned as an input, not used as a criterion.** An implementation must treat a model score as a pinned candidate attribute, must not invoke a model during a decision, and must require the criterion that reads the score to be an artifact with its own statement and parameters.

### 11.23 The single decision that is many

**Mechanism.** One decision returns a bundle: which supplier, at what price, on what terms. The criterion selects the bundle.

**Consequence.** Where the bundle's components were separably variable, the record cannot show which component the criterion actually turned on, and a change to any component's policy requires changing the bundle criterion. Where the bundle was genuinely atomic this is correct, and the distinction is not recorded.

**Basis.** Practice.

**P5-11.23 (SHOULD) Compound outcomes declared as such.** An implementation should record, for a decision whose outcome value has separable components, whether the components were selected together as one candidate or could have varied independently, and should express the latter as separate decisions.

### 11.24 The criterion nobody can read

**Mechanism.** The criterion is a formula. Its statement field contains the formula rendered in words, or is empty.

**Consequence.** The people governed by the criterion cannot read it, and the reviewers who approved it approved a formula. The correspondence between what the organisation meant and what the criterion computes is unexamined, which is the same unbridged correspondence `Part 2` section 13.2 records for rules and section 13.2 here records for criteria.

**Basis.** Practice.

**P5-11.24 (MUST) Statement present and not derived.** An implementation must hold a statement for every criterion version and must not present a rendering of the criterion's computation as its statement.

### 11.25 The undecidable outcome retried forever

**Mechanism.** The criterion returns an undecidable tie. The caller's error handling treats a non decision as a transient failure and retries. It retries on a schedule, indefinitely.

**Consequence.** A substantive finding about policy is consumed as an infrastructure error. Nobody is told the criterion does not fit, the queue of retrying decisions grows, and the eventual remedy is a change to the retry policy rather than to the criterion.

**Basis.** Practice.

**P5-11.25 (MUST) Undecidable distinguished from refused.** An implementation must return an undecidable outcome as an outcome rather than as a refusal, must emit the corresponding event per decision, and must document that the caller obligation is to route it to a remedy owner, per clauses P5-5.14 and P5-4.33.

### 11.26 The simulation that became the decision

**Mechanism.** A criterion author runs a proposed criterion over live candidate sets to see how it behaves. The outcomes are useful and somebody acts on one.

**Consequence.** A decision was taken under an unapproved criterion, with no authority and no approval, and the record marks it non authoritative in a field the acting system did not read. The mechanism is the same as `Part 2` section 4.3's non authoritative evaluation and the consequence here is larger, because a decision produces an act.

**Basis.** Practice.

**P5-11.26 (MUST NOT) No action on a non authoritative run.** An implementation must mark every simulation non authoritative irremovably, must refuse to include it in an evidence package as a decision, and must declare that its outcome must not be acted upon, per clause P5-4.14.
## 12. Boundaries with other parts

Each subsection states four things: what this component delegates, what it must not absorb, the naive design that conflates the two, and the reciprocal declaration the other part must make. Subsection numbers correspond to part numbers, so section 12.7 states the boundary with `Part 7` and section 12.14 states the boundary with `Part 0`. Section 12.5 is deliberately unused, since it would designate this part. Numbers are permanent.

Four of this part's boundaries discharge reciprocal declarations already committed by the parts on the other side: `Part 1` clause P1-12.10, `Part 2` clauses P2-12.10 through P2-12.14, `Part 3` clauses P3-12.12 and P3-12.13, and `Part 4` clauses P4-12.13 and P4-12.14.

**P5-12.1 (MUST) Declared allocation.** An implementation must be able to state, for every capability named in this section as delegated, which component provides it, and must not provide it within this component.

**P5-12.2 (MUST) Refusal rather than substitution.** Where a delegated capability is unavailable, an implementation must take the behaviour of section 4.6 and must not substitute a local implementation of it.

**P5-12.3 (MUST NOT) No reaching past a neighbour.** An implementation must not read or write the internal state of another component named in this section and must interact with it only through that component's declared interface.

### 12.1 Boundary with Part 1, controlled documents and records

This subsection is the reciprocal declaration `Part 1` section 12.5 requires.

**Delegated.** The identity, version, approval, signature, effectivity, supersession and retention of every document that carries a decision definition, a criterion, a precedence order, a tiebreak, a default or a registry. The determination of what was in force at an application time. The resolution of a clause level locator, which is what a criterion's authority reference is.

**Must not absorb.** Document status and effectivity. This component does not determine what governed at a time; it obtains it by citation resolution.

**Naive conflation.** This component acquires an active or inactive flag on a criterion, so criteria can be switched without a document change. The organisation's selection policy is then not any document it holds, and no change to it has an approval or a date. The converse conflation is `Part 1` selecting among candidate approvers or candidate versions, which clause P1-12.10 forbids.

**Reciprocal.** This part declares that it does not determine document status or effectivity, and that a decision requiring a governing document obtains it by citation resolution against `Part 1`. That is the declaration `Part 1` requires and clauses P5-12.4 and P5-12.5 make it binding.

**P5-12.4 (MUST) Status and effectivity obtained, never determined.** An implementation must obtain the approval and effectivity of every criterion and decision definition version by resolution against `Part 1`, must record the whole resolution outcome envelope, and must not hold or assert either.

**P5-12.5 (MUST NOT) No activation outside the document.** An implementation must not provide a means of activating or deactivating a criterion or a decision definition other than by a change to the document that carries it or by the registration mechanism of section 5.2.

**P5-12.6 (MUST) Ambiguity returned, not resolved.** An implementation must return the ambiguity outcomes `Part 1` supplies where a citation resolution is ambiguous and must not select among candidate versions, consistently with clause P1-12.10.

### 12.2 Boundary with Part 2, business rules and constraint evaluation

This subsection is the reciprocal declaration `Part 2` section 12.5 requires, and it is the most consequential boundary in the part.

**Delegated.** Every constraint evaluation. Whether a candidate satisfies a rule, whether a rule applies, whether a rule could be evaluated at all, and the whole verdict taxonomy including the vacuity flag and the five indeterminacy subclasses. The reporting of a contradiction between rules, which that component detects and refuses to arbitrate.

**Must not absorb.** Evaluation. Eligibility is obtained as a whole evaluation report and is never determined here.

**Naive conflation, and it runs both ways.** `Part 2` acquires the ability to pick, through a priority, a first match or a default, and every property of its sections 6 and 7 degrades. Or this component evaluates conditions inline, per section 11.21, and the eligibility rules lose their identity, authority, statement and three valued outcome.

**What this component owns that Part 2 handed it.** Every hit policy, since a hit policy is a conflict resolution criterion. Every default and fallback. Every precedence and priority. Every aggregation of verdicts into a conclusion. Section 3.9 specifies the hit policies and refuses two of them; section 3.10 specifies aggregation as not being a selection; section 3.11 specifies defaults and tiebreaks as artifacts.

**Reciprocal.** This part declares that it does not evaluate constraints, that it obtains verdicts from `Part 2` and records the whole report per clause P2-12.6, that it does not treat an indeterminate verdict as an input from which a decision may be made without recording that it did so, and that its conflict resolution criteria are declared and versioned artifacts rather than properties of the rules it consumes. That is the declaration `Part 2` requires and clauses P5-12.7 through P5-12.11 make it binding.

**P5-12.7 (MUST) Whole report obtained and pinned.** An implementation must obtain every eligibility verdict as a `Part 2` evaluation report, must pin the whole report including its pin set, and must refuse a summary, a count or a pass indicator, per clause P2-12.6.

**P5-12.8 (MUST NOT) No constraint evaluation.** An implementation must not evaluate a constraint, must not admit a criterion whose evaluation determines admissibility, and must not exclude a candidate for inadmissibility other than on a verdict.

**P5-12.9 (MUST) Indeterminate treatment recorded.** An implementation must record, on every decision in which an indeterminate verdict was treated, the treatment applied, the candidate affected, and the `Part 2` subclass and code, and must not treat an indeterminate verdict as eligible or ineligible without a declared treatment.

**P5-12.10 (MUST) Criteria are artifacts, not rule properties.** An implementation must hold every conflict resolution criterion as a versioned artifact with an authority and must not derive one from a priority, a salience, an enforcement level or an order recorded on the rules it consumes.

**P5-12.11 (MUST) Contradiction arbitrated only by a declared authority order.** An implementation must resolve a `Part 2` reported contradiction between rules only by an `AUTHORITY_PRECEDENCE` criterion over a declared order of authorities, and must return the incomparability outcome where the authorities are unranked relative to each other.

**P5-12.12 (MUST NOT) No decision during an evaluation.** An implementation must not accept a decision request originating from an evaluation in progress and must declare the mechanism by which the dependency between the two components is kept in one direction, consistently with clause P2-12.14.

### 12.3 Boundary with Part 3, provenance and audit ledger

This subsection is the reciprocal declaration `Part 3` section 12.5 requires.

**Delegated.** The determination record and its citation structure: the criterion as a selection criterion citation, every unselected candidate as a rejected alternative citation, the eligibility reports as constraint outcome citations, the delegation chain, the frontiers, the closure assessment and the basis defect propagation.

**Must not absorb.** Provenance. This component records how the selection was performed; `Part 3` records what the determination rested on and whether the chain closes.

**Naive conflation.** This component keeps its own citation structure, so there are two accounts of what the decision rested on and they diverge. Or `Part 3` acquires the ability to assess whether the right candidate was chosen, which clause P3-12.13 forbids and clause P3-1.3 forbids more generally.

**Position taken on the overlap.** The decision record exists in both components and section 8.1 states the division: this component is authoritative for the comparisons, the margin and the criterion internals, and `Part 3` is authoritative for the citation structure. Section 13.4 records that this is the least comfortable boundary in the part.

**Reciprocal.** This part declares that it reports every candidate it considered and the criterion it applied, that its criteria are declared and versioned artifacts obtainable by pin, and that it does not record determinations of its own outside `Part 3`. That is the declaration `Part 3` requires and clauses P5-12.13 through P5-12.15 make it binding.

**P5-12.13 (MUST) Every candidate reported with its ground.** An implementation must report, with every determination it records, every candidate considered and its elimination ground in the enumeration `Part 3` section 3.10 requires, and must not record a determination reporting a selection with no alternatives, per clause P3-12.12.

**P5-12.14 (MUST) Criteria obtainable by pin.** An implementation must expose every criterion version obtainable by pin, with its statement, parameters, justifications and authority, so that `Part 3` can cite it as a selection criterion.

**P5-12.15 (MUST NOT) No second citation structure.** An implementation must not hold a citation structure for a decision beyond the pin set of section 3.12, and must record the determination's basis with `Part 3`.

### 12.4 Boundary with Part 4, metadata and model repository

This subsection is the reciprocal declaration `Part 4` section 12.5 requires.

**Delegated.** The identity, version, meaning and representation of every concept a criterion is expressed over, of every candidate attribute it considers, and of the outcome concept. The impact analysis of changing any of them. The governance of the interface of any inferential model whose output is a candidate attribute.

**Must not absorb.** Definitions. A criterion references a concept; it does not define one.

**Naive conflation.** The criterion defines its own attributes inline, so two criteria over the same word mean different things. The converse conflation is `Part 4` producing a recommendation from an impact analysis, which clause P4-12.13 forbids.

**Reciprocal.** This part declares that it does not resolve definitions, that a decision requiring a governed meaning obtains it by resolution against `Part 4`, and that every selection criterion expressed over a concept is registered there as a dependency of kind `DECISION_CRITERION`. That is the declaration `Part 4` requires and clauses P5-12.16 through P5-12.18 make it binding.

**P5-12.16 (MUST) Concepts resolved, not defined.** An implementation must obtain the definition version of every concept a criterion considers by resolution against `Part 4`, must pin it, and must not hold a definition of its own.

**P5-12.17 (MUST) Criteria registered as dependencies.** An implementation must register every criterion version with `Part 4` as a dependent registration of kind `DECISION_CRITERION` against every concept it considers, per clause P4-12.14.

**P5-12.18 (MUST) Definition change reaches the criterion.** An implementation must record a pinned definition version's supersession as an observation against every criterion that considers it, and must not silently rebind to the successor.

### 12.6 Boundary with Part 6, workflow and process orchestration

**Delegated.** Control flow: when a decision is invoked, what happens to its outcome, how an undecidable outcome is routed to a person, how a referral is chased, and how an overturned decision is remediated.

**Must not absorb.** Process state. A decision is a conclusion, not a step, and the run states of section 5.3 describe an execution rather than a process.

**Naive conflation.** The undecidable outcome becomes a workflow branch and is not recorded as an outcome, so the organisation has process instances that went to manual review rather than a count of decisions its criterion could not determine. The signal that would reveal the criterion does not fit is then a property of a transient process instance.

**Reciprocal.** `Part 6` must declare that it does not own decisions, criteria or outcomes, that it records the decision reference rather than the branch taken, and that its own retention does not govern the retention of the decisions it routed.

**P5-12.19 (MUST) Outcomes independent of process.** An implementation must record and return every outcome without reference to any process instance and must remain correct where the orchestrator is replaced.

**P5-12.20 (MUST NOT) No process identity required.** An implementation must not require a process instance identifier in order to decide, record or read anything specified in this part.

**P5-12.21 (MUST) Undecidable outcomes recorded before routing.** An implementation must record an undecidable outcome as an outcome, with its whole envelope, before any referral is raised, and must not permit the referral to be the only record.

### 12.7 Boundary with Part 7, policy decision point and authorisation

This is the boundary most likely to be misread, because an authorisation is plainly a selection from two candidates and this component selects.

**Delegated.** Every authorisation decision, being whether a principal may perform an operation on a resource, together with its obligations, its advice, its combining algorithms and its enforcement at a policy enforcement point. Also every authorisation of this component's own operations: who may record a criterion, decide, simulate, override or export.

**Must not absorb.** Authorisation. The test offered is whether the outcome is an entitlement to act. Choosing which supplier to use is a business decision; determining whether this user may approve that payment is an authorisation. Both are selections and only one carries an obligations model and an enforcement point.

**Naive conflation.** This component becomes the policy decision point, per section 11.20, because it has criteria machinery. The authorisation then has no obligations model, no extended indeterminate treatment and no enforcement point. Or `Part 7` acquires business criteria, so a selection policy lives in an authorisation engine with no margin, no candidate record and no elimination grounds.

**Position taken, and its limits.** The entitlement test works at the extremes and not in the middle. A decision determining which of three approvers is required is a business decision whose outcome is consumed by an authorisation. A decision determining a credit limit is a business decision whose outcome constrains later authorisations. Section 13.3 records that the boundary is contestable and that a reasonable reader might allocate differently.

**Reciprocal.** `Part 7` must declare that it owns authorisation and its combining algorithms, that it does not make business selections, that it obtains a business outcome by resolution here where a policy depends on one, and that it records its own decisions as determinations with `Part 3` rather than here.

**P5-12.22 (MUST NOT) No authorisation outcome.** An implementation must not produce an outcome that is an entitlement to perform an operation and must obtain every authorisation from `Part 7`.

**P5-12.23 (MUST) Own operations authorised elsewhere.** An implementation must obtain the authorisation of its own recording, deciding, simulating, overriding and exporting operations from `Part 7` and must record the decision reference.

**P5-12.24 (MUST) Business outcomes supplied as attributes.** An implementation must supply a recorded decision outcome as an attribute for an authorisation decision where asked, by pin, and must not evaluate the authorisation policy.

### 12.8 Boundary with Part 8, human task and case management

**Delegated.** The work a person does: the queue of decisions awaiting determination, the referral of an undecidable outcome, the review of a marginal decision, the assessment of decisive automation, and the case in which that work sits.

**Must not absorb.** Task management. This component records that a person was involved, what they did and when; it does not manage the doing.

**Naive conflation.** The human involvement and the task are one entity, so completing the task records the involvement and disposing of the task disposes of the record that a person decided. An override then disappears with its work item.

**Reciprocal.** `Part 8` must declare that completing a task does not itself record an involvement, an override or an assessment, that each is effected by a recording operation of section 4.3 whose outcome the task records, and that disposing of a task does not alter any of them.

**P5-12.25 (MUST) Involvements independent of tasks.** An implementation must retain every human involvement, override and automation assessment unchanged after any task concerning it is disposed of.

**P5-12.26 (MUST NOT) No task driven recording.** An implementation must not provide a means by which a task completion records an involvement, an override or an assessment without a recorded act naming the actor.

### 12.9 Boundary with Part 9, schema and contract registry

**Delegated.** The identity, versioning and compatibility of the schemas of decision requests, candidate representations, outcome envelopes and event payloads, and the validation of an instance against one.

**Must not absorb.** Schema validation. This component records the schema a payload claims and does not validate against it.

**Naive conflation.** The candidate representation's schema becomes the definition of what a candidate is, so a candidate's admissible values are a schema facet rather than an eligibility rule, and a candidate outside the domain is a parse failure rather than a recorded ineligibility.

**Reciprocal.** `Part 9` must declare that it owns schema identity and compatibility, that it does not express eligibility or preference, and that it exposes schema versions obtainable by pin.

**P5-12.27 (MUST NOT) No schema validation or versioning.** An implementation must not assign version identity to a schema and must not validate an instance against one, and must express a structural refusal as `MALFORMED_REQUEST` without asserting a schema outcome.

**P5-12.28 (MUST) Outcome domain checked against Part 4, not a schema.** An implementation must check a candidate's outcome value against the outcome concept's value set obtained under `Part 4` and `Part 10`, and must refuse it with `CANDIDATE_OUTSIDE_OUTCOME_DOMAIN` rather than as a schema violation.

### 12.10 Boundary with Part 10, reference and master data management

**Delegated.** The membership, versioning, retention and governance of every value set: the enumerated outcome values a precedence order is over, the code lists a criterion tests against, and the authority identifiers an authority precedence orders.

**Must not absorb.** Value set membership. A precedence order names and orders members of a pinned set; it does not enumerate the set.

**Naive conflation.** The precedence order enumerates the outcome values inside itself, so the order and the value set have two masters and a member added in one is absent from the other. A new outcome value then falls outside the order and every candidate carrying it is eliminated out of scope, per section 11.11, permanently and invisibly.

**Reciprocal.** `Part 10` must declare that it owns value set membership and versioning, that it retains every superseded set version for at least as long as the longest retained decision citing it, that it does not remove or reuse member keys, and that it reports the addition or removal of a member to this component so that a precedence order can be checked for completeness against it.

**P5-12.29 (MUST) Value sets bound by pin only.** An implementation must bind a precedence order to a `Part 10` value set version by pin and must not enumerate the set's membership itself.

**P5-12.30 (MUST) Order completeness checked against the set.** An implementation must be able to report every member of a pinned value set version that a precedence order does not position, since such a member yields an out of scope elimination for every candidate carrying it.

**P5-12.31 (MUST) Set change surfaces as a criterion change.** An implementation must record a change to a pinned value set version as requiring a new criterion version where the order's completeness against the set is affected, and must not permit the binding to follow a set version silently.

### 12.11 Boundary with Part 11, content addressed artifact store

**Delegated.** The durable storage and retrieval by digest of the octets of anything this component pins or exports: candidate attribute sets, eligibility reports, evidence packages and comparison sets where held separately.

**Must not absorb.** Storage semantics. This component owns the mapping from a pin to a digest and a canonical form profile.

**Naive conflation.** The store holds decision records and becomes a second source for them, with no criterion, no basis and no margin, so a reader finds an outcome without its qualifications.

**Reciprocal.** `Part 11` must declare that it holds no criterion, no outcome, no basis and no margin, and that it does not delete content on its own authority.

**P5-12.32 (MUST) Digest is the interface.** An implementation must address stored content by digest under a declared canonical form profile and must not rely on a location or path as identity.

**P5-12.33 (MUST NOT) No decision state in the store.** An implementation must not hold criteria, outcomes, bases or margins in the artifact store and must not accept them from it.

### 12.12 Boundary with Part 12, conformance and assurance harness

**Delegated.** All assessment of whether an implementation satisfies this part, including the verification of the properties this part requires an implementation to demonstrate: order independence, reproduction, and the four static analyses.

**Must not absorb.** Self assessment. This component performs the analyses of section 6.4, the order independence demonstration of clause P5-6.5 and the reproduction sampling of clause P5-8.13, and records their results; it does not assess itself against this part.

**Naive conflation.** The component's own analysis results are presented as evidence that its criteria are sound. A criterion can pass every analysis in section 6.4 and be entirely inappropriate, since none of the four addresses whether the criterion is the right criterion, which clause P5-6.47 forbids this component from asserting.

**Reciprocal.** `Part 12` must declare that it obtains the clause set from this part by resolution, that it records the version of this part an assessment was made against, that it does not write here while assessing, and that it independently examines the distribution of decisions by basis rather than accepting an implementation's analysis results.

**P5-12.34 (MUST) Read only assessment.** An implementation must expose everything `Part 12` requires through read operations and must not require a write in order to be assessed.

**P5-12.35 (MUST NOT) No self assessment as assessment.** An implementation must not present its own analyses, order independence demonstrations or reproduction samples as an assessment of conformance, per clause P5-1.14.

**P5-12.36 (MUST) Basis distribution exposed for assessment.** An implementation must expose the distribution of decisions by basis of selection per definition version, since a criterion that passes every static analysis and determines nothing is visible only there.

### 12.13 Boundary with Part 13, model invocation and agent execution

**Delegated.** The invocation of any inferential model, its cost, its retries, its non determinism, its behaviour and its performance. The model artifact itself.

**Must not absorb.** Invocation. A model output is a pinned candidate attribute obtained before the decision, never computed during it.

**Naive conflation.** The criterion invokes a model, per section 11.22. Reproducibility fails, because the model may not be deterministic even pinned. Explainability fails, because the reason one candidate beat another is inside the model. And the criterion's statement cannot express what the criterion does, so the requirement of clause P5-3.39 becomes a formality.

**Position taken.** A model output may be a candidate attribute the criterion considers if and only if it was obtained before the decision, recorded as an artifact with its own identity and digest, pinned in the run, marked as a model output rather than a candidate property, and considered by a criterion that is itself an artifact with a statement and justified parameters. Under those conditions the decision is reproducible in the only available sense: it will yield the same outcome from the same recorded score. It is not reproducible in the stronger sense that re invoking the model would yield the same score, and clause P5-12.39 requires the distinction to be recorded.

An automated agent may perform a decision. The attribution of that decision, and the delegation chain to an accountable party, are `Part 3`'s under section 3.12 of that part, and clause P5-12.40 requires this component to supply what that requires.

**Reciprocal.** `Part 13` must declare that it owns the invocation record and the model artifact, that it does not hold criteria or outcomes, that it exposes a model output as an artifact with an identity and a digest that this component can pin, and that it reports a model found defective as a basis defect to `Part 3`.

**P5-12.37 (MUST NOT) No invocation during a decision.** An implementation must not invoke a model, an agent or any non deterministic service during a decision.

**P5-12.38 (MUST) Model outputs pinned and marked.** An implementation must record a model output used as a candidate attribute as a pinned artifact with its own identity and digest and must mark it as a model output rather than a candidate property.

**P5-12.39 (MUST) Reproduction limit recorded.** An implementation must record that reproduction of a decision reading a model output does not establish reproduction of the output.

**P5-12.40 (MUST) Agent attribution supplied.** An implementation must supply, for a decision performed by an automated agent, the agent identity, the invocation reference and whatever `Part 3` section 3.12 requires to establish a delegation chain to an accountable party, and must not record the decision as made by the person who requested it.

### 12.14 Boundary with Part 0, system composition

**Delegated.** What happens when all the components run at once: authority over facts more than one component touches, the seams at which values cross boundaries, the propagation of non results, ordering and acyclicity across components, and pinning across a unit of work spanning several.

**Must not absorb.** Composition. This part states what it decides and what it refuses, and does not state what a caller with no representation for an undecidable outcome must do.

**Reciprocal.** `Part 0` must declare that this component holds authority over criteria, candidate sets, eligibility treatments, selections, bases, margins and decision records, and that `Part 1` holds authority over the approval of criteria and `Part 2` over eligibility. It must state, for every seam, what must hold and how a violation appears here. It must in particular resolve seven questions this part hands it.

What a caller must do with each of the four undecidable outcomes, given that this part specifies only what it returns and that a caller with no representation for them will retry, default or fail.

How the acyclicity between this component and `Part 2` is enforced, given that clause P5-12.12 and clause P2-12.14 each forbid one direction and neither can observe the other.

How a unit of work spanning this component and `Part 2` pins one rule set version and one criterion version together, so that a decision and the eligibility it rested on cannot be evaluated against different vintages of policy.

Which component is authoritative where this component's decision record and `Part 3`'s determination record disagree, which is the overlap section 8.1 declares and section 13.4 records as uncomfortable.

Whether the treatment of an indeterminate input has one enterprise wide answer or one per decision class, since this part requires a declaration per definition and `Part 2` allocates its five subclasses to five remedy owners.

Whether an override recorded here, a `Part 8` case, and a `Part 3` determination of the override are one act or three, and which is authoritative for the outcome that was finally acted upon.

Whether the structural patterns this standard has now repeated five times, being the immutable record with stateful assertions about it, the declared completeness of a set, the frontier as a declared terminus, and the asymmetric bridge that disproves and cannot prove, should each be stated once for the whole standard rather than five times.

**P5-12.41 (MUST) Authority declared, not assumed.** An implementation must not accept an assertion about a criterion, a candidate set, an eligibility treatment, a selection, a basis or a margin from another component, and must require every such fact to be established by its own operations.

**P5-12.42 (MUST) Undecidable outcomes returned unmodified.** An implementation must return every outcome of section 7.2 unmodified regardless of whether the caller can represent it, and must not degrade an undecidable outcome to a decided one or to a refusal in order to fit a caller's model.
## 13. What could not be established

A question recorded as open can be closed by someone with access to the source. A question closed by inference cannot be reopened, because nothing in the document reveals that an inference was made.

### 13.1 Sources not obtained in full text

The following were not available in full text. This part's account of each rests on publisher inventories, status pages, implementation documentation, commentary and secondary literature. No clause reproduces text from any of them.

**DMN 1.5.** The version inventory and adoption dates were obtained directly from the publisher and are established. **The hit policy semantics were not.** Section 10.2's account of the seven policies, and in particular the two properties on which section 3.9 turns, being that Priority and Output order reference a list of output values while First and Rule order reference rule sequence, rest on implementation documentation from four independent vendors and on published commentary. Those sources agree with one another and none is the specification. Since clause P5-3.59 refuses two hit policies on the strength of that distinction, it is the most load bearing unverified claim in the part and should be checked first. The related claims, that a Priority table is constrained to enumerated output values and that an else rule's output must be the lowest priority value, rest on commentary alone.

The account of decision table defects, being overlap under Unique, subsumption, incomplete tables and misleading hit policies, rests on published best practice guidance rather than on the specification, and section 6.4's four analyses are built on it.

**XACML 3.0 Plus Errata 01.** The status, date, the twelve combining algorithm names and the existence of a normative appendix and of extended indeterminate values were obtained from the specification's own table of contents and section headings. The appendix text was not obtained, so section 10.3's account of what each algorithm does, and in particular the claim that only one applicable returns indeterminate where more than one policy applies, rests on secondary description. Given that section 10.9 cites that behaviour as the precedent for this part's undecidable outcomes, it warrants verification.

**GDPR Article 22 and the related articles.** The provisions and the exception grounds are established from secondary sources and from the general currency of the Regulation. No article text was obtained. Recital 71's status as the basis for a right to explanation is contested in the literature and this part states it as generally argued rather than as settled.

**Court of Justice of the European Union, Case C-634/21.** The decision date and the criterion this part adopts as the test for decisive automation rest entirely on secondary sources, including academic commentary that discusses the holding at length. The judgment was not obtained. Section 3.16 is built on it and it should be verified.

**EU AI Act, Regulation (EU) 2024/1689.** The article numbers and their subjects were obtained from secondary sources. No article text was obtained.

**The application status of the Act's high risk obligations could not be established, and this is the most consequential gap in the section.** The obligations, including the Article 14 human oversight requirement, were scheduled to apply from 2 August 2026, which is sixteen days before the date of this part. A European Commission Digital Omnibus package was reported as under discussion, proposing to condition the application of those obligations on the availability of harmonised technical standards, with deadlines no later than December 2027 or August 2028. Whether that proposal has been enacted, whether the 2 August 2026 date took effect, and therefore what is in application as at the date of this part, was not determined. Clause P5-10.3 requires an implementation to establish the position for itself and this section records why.

**United States state instruments.** The Colorado AI Act, the California automated decision making technology regulations and the Texas Responsible AI Governance Act were reported as imposing automated decision obligations with audit trail requirements. None was examined. Their obligations may bear on sections 3.16 and 8.6 and this part does not reflect them.

**Arrow's impossibility theorem, the Condorcet paradox, Pareto dominance, the analytic hierarchy process and its rank reversal critique, and measurement theory on levels of measurement.** All cited as settled results from general knowledge. No primary source was obtained for any of them, and no edition is cited. Sections 6.3, 3.7 and 9.3 depend on them. The account of each is standard and a reviewer should nonetheless be aware that no source was checked.

**RIF-PRD, PRR 1.0 and SBVR 1.5.** Carried forward from `Part 2` section 13.1 with the same limitations.

Not obtained and not assessed at all: ISO 31000 and IEC 31010, which contain decision analysis techniques and may bear on section 3.7's criterion kinds; and the OMG Business Motivation Model.

**P5-13.1 (MUST) Verification before approval.** An implementation or reviewer must verify the claims listed in section 13.1 against the source standards before this part is approved and must record the outcome of each verification against this section.

### 13.2 The correspondence between a criterion's statement and its computation

Clause P5-3.39 requires a statement on every criterion version and clause P5-11.24 forbids presenting a rendering of the computation as one. Nothing establishes that the two agree.

This is the third appearance of the same limitation in the standard. `Part 2` section 13.2 records it for a rule's statement against its declaration and offers worked examples as an asymmetric bridge. `Part 4` section 13.2 records it for a definition's text against its extension and offers a classification test set. Neither proves correspondence; both disprove it.

This part offers no bridge at all, and that is an omission rather than a considered position.

**Open.** Whether the same device would work here. The candidate is a set of recorded candidate sets with the outcome the criterion's author asserts the criterion produces for each, run against the criterion at registration, disproving a claim where they disagree. It would be structurally identical to `Part 2`'s worked examples and `Part 4`'s classification instances, it would be cheap to specify, and it was not specified because the part was already long. A reviewer who thinks the pattern should be completed across the three parts should say so, and section 13.7 is the related question.

### 13.3 The refusal of selection by rule sequence

Clause P5-3.59 refuses the First and Rule order hit policies. First is, on the evidence of every implementation account obtained, the most used hit policy in practice.

The reason for the refusal is stated in section 3.9 and is not restated here. What is worth recording is the cost, honestly.

An ordered fall through table is genuinely easier to read than a precedence over outcome values, because the reader sees the cases in the order they are considered and does not have to hold an output ordering in mind. A table of fifteen rows with a first match policy is comprehensible to a subject matter expert with no training; the same table expressed as a precedence over eight outcome values is not.

The remedy this part offers therefore has a real cost in reviewability, and reviewability is the property the part exists to protect. There is a genuine possibility that refusing First makes criteria less reviewable in practice while making them more governable in principle, and that the second is worth less than the first.

**Open.** Whether a middle position exists. The candidate is to admit rule order as a criterion on condition that the order is itself a declared, versioned, approved artifact separate from the table's layout, so that inserting a row does not change the order unless the order is also changed. That preserves the readability and removes the mechanism, at the cost of two artifacts that must be kept consistent and a consistency nobody will check. It was not adopted and it may be better than what was.

### 13.4 The overlap with Part 3

Section 8.1 declares a division: this component is authoritative for comparisons, margins and criterion internals, and `Part 3` is authoritative for the determination's citation structure. Both hold a record of the same decision.

The division is workable and it is not clean. The candidate set appears in both, as candidates here and as rejected alternative citations there. The eligibility reports appear in both, as pinned reports here and as constraint outcome citations there. The criterion appears in both. Clause P5-12.15 forbids a second citation structure and does not prevent the two records from diverging, since nothing compares them.

`Part 3` section 13.11 hands `Part 0` the question of what happens when its record and an owning component's record disagree, and this part is the first component for which that question is concrete rather than hypothetical.

**Open.** Whether the duplication should be removed, and in which direction. Two candidates. This component could hold only the criterion artifacts and the comparisons, recording the candidate set and its eliminations solely with `Part 3`, which removes the duplication and makes every read of a decision a cross component read. Or `Part 3` could cite this component's decision record as a single artifact rather than decomposing it into citations, which contradicts that part's clause P3-11.24 on summaries. Neither is obviously right and the present arrangement was chosen for readability of this part rather than for architectural cleanliness.

### 13.5 The boundary with optimisation

Section 1.2 excludes optimisation and section 3.5 requires candidates to be enumerated from a declared source. The boundary between a large enumerated candidate set and a search space is not sharp.

A decision among four suppliers is plainly within scope. A decision among ten thousand pricing combinations generated by a governed generator is formally within scope, since the candidates are enumerated and the source is declared, and is in substance an optimisation. The comparison count bound of section 6.7 will truncate it, and clause P5-6.41 will then refuse to return a selection, which is correct and unhelpful.

**Open.** What this part should say about a candidate set too large to compare exhaustively. Three positions were considered. Refuse, which is what the present text does and which pushes the work outside the standard with no governance at all. Admit a declared search strategy as a criterion kind, which would make the strategy an artifact and would import every property optimisation does not have, including reproducibility only under a pinned seed and no meaningful margin. Or require the candidate set to be reduced by a declared filter before decision, which moves the problem to the filter and at least makes the filter an artifact. The third is probably right and was not specified.

### 13.6 Whether the third value should carry its possibilities

Section 10.3 records that XACML's extended indeterminate values distinguish an indeterminate that could only have been deny, one that could only have been permit, and one that could have been either. Section 3.6 does not adopt anything comparable: an indeterminate eligibility verdict is treated by subclass and the treatment is declared, and nothing records what the verdict could have been.

The information is frequently available. A candidate whose eligibility is indeterminate because one rule of eleven could not be evaluated, where the other ten were satisfied, could only have been eligible or ineligible depending on that one rule, and where that rule is known to be satisfied by almost every candidate the possibilities are not symmetric. `Part 2` records enough to establish this, since it returns a verdict per rule.

**Open.** Whether an indeterminate eligibility should carry the set of possible eligibility values, so that an inclusion or exclusion treatment is better founded. The argument for is that a treatment applied without it is a policy applied blind, and that XACML shows the idea is specifiable. The argument against is that computing the possibilities requires reasoning about what the unevaluable rule could have returned, which is exactly the reasoning `Part 2` clause P2-7.34 refuses to do. That tension may be resolvable and was not resolved.

### 13.7 Repeated structure across the standard

`Part 4` section 13.7 recorded three structures appearing in more than one part and handed `Part 0` the question of whether each should be stated once. This part adds to the list and the question is now more pressing than it was.

**The immutable record with stateful assertions about it.** Five parts, five statements: `Part 1`'s status against force, `Part 2`'s admission against force, `Part 3`'s record with no lifecycle, `Part 4`'s registration against authority, and section 5.1 here.

**The declared completeness of a set.** Four parts: `Part 3`'s basis completeness, `Part 4`'s lineage completeness per node, `Part 3`'s negative citation completeness, and section 3.5's candidate set completeness. All four say the same thing: a set whose completeness is not declared cannot be relied upon, and the declaration is the responsibility of whoever enumerated it.

**The frontier as a declared terminus.** Two parts, `Part 3` for chains of reasoning and `Part 4` for lineage graphs. This part does not use it, and arguably should: a candidate source of kind `EXTERNAL_SOLICITATION` is a frontier in exactly that sense.

**The asymmetric bridge that disproves and cannot prove.** Two parts, `Part 2`'s worked examples and `Part 4`'s classification instances, and section 13.2 records that this part should have a third and does not.

**The honest undeclared value.** Five parts: `Part 2`'s undeclared rule authority, `Part 3`'s undeclared method and frontier, `Part 4`'s undeclared null semantics and unjustified nothing, and this part's `UNJUSTIFIED` parameter basis and `UNASSESSED` automation. In every case the reasoning is identical: the alternative to permitting the honest answer is a system in which every record claims a provenance it does not have, and the count of honest answers is the only available measure of the estate.

**Open.** All of it. Five parts have now independently specified the same five patterns and the drift between them has already begun: `Part 3`'s frontier kinds and `Part 4`'s are different sets for the same concept, and this part uses the concept without the name. A decision to factor them is cheap now and will not be after `Part 13`.

### 13.8 What this part deliberately did not attempt

No conformance assessment of any system was performed or anticipated, per clause P5-1.14.

No expression language is specified for a score function or a condition, on the same basis and for the same reason `Part 2` section 13.13 gives: registering one would bind this part to the currency of a specification it does not control.

No method for choosing a criterion is specified. Whether a weighted aggregate, a lexicographic order or a dominance test is the right instrument for a given decision is a question of judgement and this part specifies only what each guarantees. IEC 31010 contains techniques and was not obtained.

No guidance is given on what weights should be. The part requires them to be justified and says nothing about what a good justification is, which is the question a steward will actually ask.

No treatment is given of decisions taken under time pressure, where declining to decide is not available. A decision that must be made now, on incomplete eligibility, is common in operational settings and the part's answer is a declared treatment recorded in advance, which is correct and which will not have been declared for the case that arises.

No treatment is given of group decisions, where several people must agree. A decision requiring three of five approvals is a decision whose criterion is a voting rule, and voting rules are exactly where Arrow's result bites hardest. Section 3.7 has no criterion kind for it and one is probably needed.

No performance or scale requirement is stated. The comparison grain of section 8.2 is the largest volume this part requires and nothing is costed.

**P5-13.2 (MUST) Gaps declared, not filled.** An implementation must not represent a matter listed in section 13.8 as specified by this part.

**P5-13.3 (SHOULD) Open questions carried forward.** A reviewer of this part should record a position on each open question in section 13, and where a position is adopted it should be recorded in the review outcome rather than by silent amendment of the clause it affects.

### 13.9 Questions handed to Part 0 rather than answered here

Each was identified while authoring this part.

What a caller must do with each of the four undecidable outcomes, given that a caller with no representation for them will retry, default or fail.

How the acyclicity between this component and `Part 2` is enforced, given that clause P5-12.12 and clause P2-12.14 each forbid one direction and neither component can observe the other.

How a unit of work pins one rule set version and one criterion version together, so that a decision and the eligibility it rested on cannot be against different vintages of policy.

Which component is authoritative where this component's decision record and `Part 3`'s determination record disagree, which section 13.4 records as this part's least comfortable boundary.

Whether the treatment of an indeterminate input has one enterprise wide answer or one per decision class.

Whether an override recorded here, a `Part 8` case and a `Part 3` determination of the override are one act or three, and which is authoritative for what was finally acted upon.

Whether the five repeated structures of section 13.7 should each be stated once for the whole standard, which is now a decision worth taking before `Part 6` rather than after `Part 13`.

Which component holds authority over actor identity, since five parts now treat it as opaque and this one requires a named reviewer whose override rate is a governance measure.

Whether the entitlement test of section 12.7 is the right boundary between a business decision and an authorisation, given that a decision determining a credit limit constrains later authorisations and a decision determining which approver is required is consumed by one.
