# KAIROS STD 003 Part 6: Workflow and Process Orchestration

**Standard.** KAIROS STD 003, the enterprise architecture standard.
**Part.** Part 6 of 14 (Part 0 and Parts 1 through 13). Cited as `KAIROS STD 003 Part 6`.
**Title.** Workflow and process orchestration.
**Version.** 1.0.0.
**Status.** Proposed. This part has not been approved and is not effective. It is issued for review against the authoring brief of 2026-08-17.
**Date of issue.** 2026-08-18.
**Supersedes.** Nothing. This is the first version.

## Binding of requirement language

The key words MUST, MUST NOT, SHOULD, SHOULD NOT and MAY in this part are to be interpreted as described in RFC 2119 and RFC 8174, and only in the upper case forms. This part does not use SHALL, SHALL NOT, REQUIRED, RECOMMENDED, NOT RECOMMENDED or OPTIONAL as requirement keywords.

Every requirement in this part is a numbered clause. A clause identifier has the form `P6-S.N`, where `S` is the section number and `N` is the ordinal of the clause within that section. Clause identifiers are permanent. A clause that is later removed has its identifier retired and never reissued. A clause that is later added to a section takes the next unused ordinal in that section, so ordinals are stable but not contiguous over the life of the part.

Text that is not a numbered clause is not binding. Narrative, tables, algorithms, examples and the discussion of standards are provided to make the clauses intelligible and testable, and where a table carries normative content a clause says so explicitly and names the table.

## Conformance

An implementation conforms to this part if it satisfies every MUST and MUST NOT clause and records, for each SHOULD and SHOULD NOT clause it does not satisfy, the reason. This part does not define conformance levels, profiles or a certification scheme, and it does not define the method of assessment. Assessment method is the subject of `KAIROS STD 003 Part 12` and is out of scope here.

Where a clause states that a value is an implementation decision, conformance requires that the implementation declare the value, not that it adopt a particular one. An undeclared implementation decision is a nonconformity.

## Clause index

The index below is generated from the clause text of this document. It lists every clause identifier, its modality and its subject label. The counts that follow the index are derived by the same extraction and are stated with the grain at which they were counted.

| Clause | Modality | Subject |
| --- | --- | --- |
| **Section 1** | | **Scope and responsibilities** |
| `P6-1.1` | MUST | Purpose satisfaction |
| `P6-1.2` | MUST | Path only |
| `P6-1.3` | MUST | Disposability demonstrable |
| `P6-1.4` | MUST NOT | No condition evaluation |
| `P6-1.5` | MUST NOT | No selection among branches |
| `P6-1.6` | MUST | Joins declare their dispositions |
| `P6-1.7` | MUST | Loops bounded |
| `P6-1.8` | MUST | Compensation outcomes distinguished |
| `P6-1.9` | MUST | State is a projection |
| `P6-1.10` | MUST | Instance pinned to its definition version |
| `P6-1.11` | MUST NOT | No update in place |
| `P6-1.12` | MUST NOT | No retention authority over what it routed |
| `P6-1.13` | MUST NOT | No absorption of neighbouring responsibilities |
| `P6-1.14` | SHOULD | Declared exclusions |
| `P6-1.15` | MUST NOT | No conformance self assertion |
| `P6-1.16` | MUST | Time horizon declaration |
| **Section 2** | | **Terminology** |
| `P6-2.1` | MUST | Single meaning per term |
| `P6-2.2` | MUST NOT | No redefinition |
| `P6-2.3` | MUST NOT | No collapsing of structural and conditional constructs |
| `P6-2.4` | MUST NOT | No collapsing of compensation, rollback and retry |
| `P6-2.5` | MUST NOT | No collapsing of an activity and an invocation attempt |
| `P6-2.6` | MUST NOT | No collapsing of completion and stall |
| `P6-2.7` | MUST NOT | No collapsing of the three clocks |
| `P6-2.8` | SHOULD | Term registry |
| **Section 3** | | **Data model** |
| `P6-3.1` | MUST | Declared types |
| `P6-3.2` | MUST NOT | No semantic identifiers |
| `P6-3.3` | MUST | Language tag present |
| `P6-3.4` | MUST NOT | No caller supplied knowledge time |
| `P6-3.5` | MUST | Determination reference, not its value |
| `P6-3.6` | MUST | Three valued domain used unchanged |
| `P6-3.7` | MUST | Control and fact distinguished |
| `P6-3.8` | MUST NOT | No fact as a variable |
| `P6-3.9` | MUST | Periodic disposal demonstration |
| `P6-3.10` | MUST | Exceptions countable |
| `P6-3.11` | MUST | Entity coverage |
| `P6-3.12` | MUST NOT | No update in place |
| `P6-3.13` | MUST NOT | No state editing |
| `P6-3.14` | MUST | Administrative intervention is an event |
| `P6-3.15` | MUST | Definition carried by a document |
| `P6-3.16` | MUST | Process class registered |
| `P6-3.17` | MUST | Addressing scheme pinned |
| `P6-3.18` | MUST | Explicit termination |
| `P6-3.19` | MUST | Stall detection interval declared |
| `P6-3.20` | MUST NOT | No definition amendment |
| `P6-3.21` | MUST | Instance bound reportable |
| `P6-3.22` | MUST | Kind registered |
| `P6-3.23` | MUST | Compensability declared |
| `P6-3.24` | MUST | Handler required where compensable |
| `P6-3.25` | MUST | Residue kinds declared where not fully compensable |
| `P6-3.26` | MUST | Idempotence declared |
| `P6-3.27` | MUST | Undeclared compensability countable |
| `P6-3.28` | MUST | Timeout absence reportable |
| `P6-3.29` | MUST NOT | No work in the activity definition |
| `P6-3.30` | MUST | Closed split and join kind sets |
| `P6-3.31` | MUST | Structural constructs require no determination |
| `P6-3.32` | MUST | Exclusive split conditions mutually exclusive |
| `P6-3.33` | MUST | Non exclusive branch selection is a decision |
| `P6-3.34` | MUST | Default flow is a declared artifact |
| `P6-3.35` | MUST | Inclusive split determination per flow |
| `P6-3.36` | MUST | Second arrival at a simple merge is a defect |
| `P6-3.37` | MUST | Disposition declared on every partial join |
| `P6-3.38` | MUST | Unwaited work recorded |
| `P6-3.39` | MUST | Join resolution recorded |
| `P6-3.40` | MUST | Discard obligation reportable |
| `P6-3.41` | MUST | Structured region required |
| `P6-3.42` | MUST | Activated flow set recorded at the split |
| `P6-3.43` | MUST NOT | No inclusive join outside a structured region |
| `P6-3.44` | MUST | Matching split identified |
| `P6-3.45` | MUST NOT | No approximation |
| `P6-3.46` | MUST | Bound declared on every repetition |
| `P6-3.47` | MUST | Bound authorised and justified |
| `P6-3.48` | MUST | Instance count provenance recorded |
| `P6-3.49` | MUST NOT | No unbounded dynamic instantiation |
| `P6-3.50` | MUST | Exhaustion behaviour declared |
| `P6-3.51` | MUST | Per iteration compensation |
| `P6-3.52` | MUST | Iteration compensation order |
| `P6-3.53` | MUST | Arbitrary cycles identified |
| `P6-3.54` | MUST | Synchronisation declared on multiple instances |
| `P6-3.55` | MUST | Handlers attached to scopes |
| `P6-3.56` | MUST | Handler authority where it embodies policy |
| `P6-3.57` | MUST NOT | No compensation of a faulted scope |
| `P6-3.58` | MUST | Compensation order declared |
| `P6-3.59` | MAY | Compensation from normal flow |
| `P6-3.60` | MUST | Concurrent completion order recorded |
| `P6-3.61` | MUST | Elapsed interval recorded on compensation |
| `P6-3.62` | MUST NOT | No compensation of a compensation |
| `P6-3.63` | MUST | Compensation is not rollback |
| `P6-3.64` | MUST | Closed outcome set |
| `P6-3.65` | MUST | Residue enumerated where required |
| `P6-3.66` | MUST | Residue kind registered |
| `P6-3.67` | MUST | Failed compensation leaves the position unknown |
| `P6-3.68` | MUST | Full compensation is an assertion |
| `P6-3.69` | MUST | Residue assigned |
| `P6-3.70` | MUST | Unassigned residue countable |
| `P6-3.71` | MUST | Compensation recorded as a determination |
| `P6-3.72` | MUST NOT | No compensation outcome inference |
| `P6-3.73` | MUST | Timer declared as a duration or an instant |
| `P6-3.74` | MUST | Observed time recorded, not recomputed |
| `P6-3.75` | MUST | Lateness recorded |
| `P6-3.76` | MUST | Clock source recorded |
| `P6-3.77` | MUST | Unmatched events recorded |
| `P6-3.78` | MUST NOT | No ambiguous correlation |
| `P6-3.79` | MUST | Correlation scheme registered |
| `P6-3.80` | MUST NOT | No business identifier as a stored key |
| `P6-3.81` | MUST | Closed value kind set |
| `P6-3.82` | MUST NOT | No business fact as a value |
| `P6-3.83` | MUST | Control flags derived from engine events |
| `P6-3.84` | MUST | Opaque transit constrained |
| `P6-3.85` | MUST NOT | No value beyond the instance |
| `P6-3.86` | MUST | Value kind checked at recording |
| `P6-3.87` | MUST | Attribution on every conditional branch |
| `P6-3.88` | MUST | Flows not taken recorded |
| `P6-3.89` | MUST | Suspend and refer is the default |
| `P6-3.90` | MUST | Declared handling authorised |
| `P6-3.91` | MUST | Outcome recorded before referral |
| `P6-3.92` | MUST NOT | No branch on a vacuous satisfaction unmarked |
| `P6-3.93` | MUST NOT | No structural attribution for a conditional split |
| `P6-3.94` | MUST | Event log is append only and totally ordered |
| `P6-3.95` | MUST | Payload restricted to declared value kinds |
| `P6-3.96` | MUST | State derived from the log |
| `P6-3.97` | MUST | State recomputable and agreement demonstrable |
| `P6-3.98` | MUST | Gaps detected |
| `P6-3.99` | MUST | Parent and child linked in both directions |
| `P6-3.100` | MUST NOT | No cross instance state |
| `P6-3.101` | MUST | Attempts recorded separately |
| `P6-3.102` | MUST | Attempt outcome per attempt |
| `P6-3.103` | MUST | Idempotence key per activity instance |
| `P6-3.104` | MUST | Response recorded by reference |
| `P6-3.105` | MUST NOT | No exactly once claim |
| `P6-3.106` | MUST | Unknown outcome distinguished from failure |
| `P6-3.107` | MUST | Retry count reportable |
| `P6-3.108` | MUST | Instance pinned to its start version |
| `P6-3.109` | MUST | Migration only under a governed mapping |
| `P6-3.110` | MUST | Mapping exhaustive over occupiable positions |
| `P6-3.111` | MUST | Post migration soundness assessed |
| `P6-3.112` | MUST | Migration recorded on the instance |
| `P6-3.113` | MUST NOT | No rewriting of earlier events |
| `P6-3.114` | MUST | Migrated instances reportable |
| `P6-3.115` | MUST NOT | No silent migration |
| `P6-3.116` | MUST | Projections are pure |
| `P6-3.117` | MUST | Projection recomputable |
| `P6-3.118` | MUST | Named projections available |
| `P6-3.119` | MUST | Waiting on states what would release |
| `P6-3.120` | MUST | Version population available |
| `P6-3.121` | MUST NOT | No writes through a projection |
| `P6-3.122` | MUST | Demonstration satisfiable |
| **Section 4** | | **Interfaces** |
| `P6-4.1` | MUST | Operation classes separated |
| `P6-4.2` | MUST | Refusal is an outcome |
| `P6-4.3` | MUST | Idempotence key accepted |
| `P6-4.4` | MUST | Every operation appends an event |
| `P6-4.5` | MUST | Preconditions checked at recording |
| `P6-4.6` | MUST | Whole definition version in one operation |
| `P6-4.7` | MUST | Analysis performed before starting |
| `P6-4.8` | MUST NOT | No execution of an unanalysed definition where analysable |
| `P6-4.9` | MUST | Withdrawal reports its population |
| `P6-4.10` | MUST | Refused versions retained |
| `P6-4.11` | MUST | Start pins the version |
| `P6-4.12` | MUST | Advance is driven by events, not by polling state |
| `P6-4.13` | MUST | Determination required before a conditional advance |
| `P6-4.14` | MUST | Compensation outcome reported, not inferred |
| `P6-4.15` | MUST | Residue supplied with the outcome |
| `P6-4.16` | MUST | Completion requires an end position |
| `P6-4.17` | MUST NOT | No advance past an unresolved wait |
| `P6-4.18` | MUST | Interventions enumerated |
| `P6-4.19` | MUST | Authorisation and reason on every intervention |
| `P6-4.20` | MUST | Token move assessed |
| `P6-4.21` | MUST | Forced outcomes marked permanently |
| `P6-4.22` | MUST | Cancellation treatment declared |
| `P6-4.23` | MUST | Interventions countable by operator |
| `P6-4.24` | MUST | Replay available |
| `P6-4.25` | MUST | Replay divergence recorded |
| `P6-4.26` | MUST NOT | No partial instance record |
| `P6-4.27` | MUST | Forced and intervened events distinguishable in every read |
| `P6-4.28` | MUST | Caller obligations declared |
| `P6-4.29` | MUST NOT | No implied progress |
| `P6-4.30` | MUST NOT | No implied restoration |
| `P6-4.31` | MUST | Declared unavailability behaviour |
| `P6-4.32` | MUST NOT | No substitution on unavailability |
| `P6-4.33` | MUST | Pinned definition survives resolution failure |
| `P6-4.34` | MUST | Ledger recording failure does not lose the event |
| `P6-4.35` | MUST | Minimum event set |
| `P6-4.36` | MUST | Envelope minimum |
| `P6-4.37` | MUST NOT | No event in place of a record |
| `P6-4.38` | MUST | Stall emitted per instance |
| `P6-4.39` | MUST | Compensation members emitted distinctly |
| `P6-4.40` | MUST NOT | No suppression of adverse events |
| **Section 5** | | **State model** |
| `P6-5.1` | MUST | Four models separate |
| `P6-5.2` | MUST | States are projections |
| `P6-5.3` | MUST NOT | No state required of another component |
| `P6-5.4` | MUST | Enumerated states only |
| `P6-5.5` | MUST | Enumerated transitions only |
| `P6-5.6` | MUST | Waiting distinguished from running |
| `P6-5.7` | MUST | Stall detected and recorded |
| `P6-5.8` | MUST NOT | No implicit termination |
| `P6-5.9` | MUST | Stall exit is an intervention |
| `P6-5.10` | MUST | Terminal states are terminal |
| `P6-5.11` | MUST | Suspension does not advance |
| `P6-5.12` | MUST | Migration recorded as a state fact |
| `P6-5.13` | MUST | Enumerated activity states |
| `P6-5.14` | MUST | Waiting states distinguished by what is awaited |
| `P6-5.15` | MUST NOT | No resolution of an unknown outcome |
| `P6-5.16` | MUST | Forced outcome is its own state |
| `P6-5.17` | MUST | Cancelled activity effects recorded |
| `P6-5.18` | MUST | Skipped activities recorded |
| `P6-5.19` | MUST NOT | No human work item state |
| `P6-5.20` | MUST | Enumerated scope states |
| `P6-5.21` | MUST | Compensation enabled only on successful completion |
| `P6-5.22` | MUST | Unavailability recorded and refusals reasoned |
| `P6-5.23` | MUST | Compensation availability window declared |
| `P6-5.24` | MUST NOT | No re enabling |
| `P6-5.25` | MUST | Enumerated compensation states |
| `P6-5.26` | MUST | Outcome recorded on termination |
| `P6-5.27` | MUST | Decline reasoned |
| `P6-5.28` | MUST | Abandoned compensation leaves the position unknown |
| `P6-5.29` | MUST | Abandonment detected within a declared interval |
| `P6-5.30` | MUST NOT | No compensation reopening |
| **Section 6** | | **Execution semantics** |
| `P6-6.1` | MUST | Derivation deterministic |
| `P6-6.2` | MUST | Non deterministic inputs recorded as events |
| `P6-6.3` | MUST | Replay reads the record |
| `P6-6.4` | MUST NOT | No reproducibility claim |
| `P6-6.5` | MUST | Derivation order total and declared |
| `P6-6.6` | MUST | Algorithm order |
| `P6-6.7` | MUST | Pinned definition never re resolved during advance |
| `P6-6.8` | MUST | Three empty cases distinguished |
| `P6-6.9` | MUST | Attempt recorded before outcome |
| `P6-6.10` | MUST | Suspension rather than assumption at a split |
| `P6-6.11` | MUST | Join resolution recorded before disposition |
| `P6-6.12` | MUST | Determination from a declared source |
| `P6-6.13` | MUST | Whole envelope pinned |
| `P6-6.14` | MUST | Control tests enumerated |
| `P6-6.15` | MUST NOT | No comparison of instance values |
| `P6-6.16` | MUST NOT | No threshold on an observed time |
| `P6-6.17` | MUST | Compensation algorithm order |
| `P6-6.18` | MUST | Impossible elements do not halt the sequence |
| `P6-6.19` | MUST | Scope outcome derived from element outcomes |
| `P6-6.20` | MUST | Concurrent completion tie rule declared |
| `P6-6.21` | MUST | Compensation effort bounded |
| `P6-6.22` | MUST | State as at completion |
| `P6-6.23` | MUST | Knowledge time assigned by this component |
| `P6-6.24` | MUST NOT | No actor occurrence time assignment |
| `P6-6.25` | MUST | Observation distinguished from expiry |
| `P6-6.26` | MUST | Clock source recorded per observation |
| `P6-6.27` | MUST | Application time cited, not determined |
| `P6-6.28` | MUST | Instants in a declared scale |
| `P6-6.29` | MUST | Monotonic knowledge time within an instance |
| `P6-6.30` | MUST | Calendar convention declared |
| `P6-6.31` | MUST | Idempotence by key |
| `P6-6.32` | MUST | Deduplication window declared |
| `P6-6.33` | MUST NOT | No idempotence across differing payloads |
| `P6-6.34` | MUST | Duplicate instance starts detectable |
| `P6-6.35` | MUST | Soundness analysed where decidable |
| `P6-6.36` | MUST | Class recorded |
| `P6-6.37` | MUST | Analyses not performed recorded with the reason |
| `P6-6.38` | MUST | Cancellation undecidability declared |
| `P6-6.39` | MUST | Exclusivity analysed or its impossibility recorded |
| `P6-6.40` | MUST NOT | No absence of finding as absence of fault |
| `P6-6.41` | MUST | Dead activities reported |
| `P6-6.42` | MUST NOT | No analysis at execution time |
| `P6-6.43` | MUST | Analysis pinned to a version |
| `P6-6.44` | MUST | Every bound has a declared exhaustion behaviour |
| `P6-6.45` | MUST | Exhaustion is an outcome, not an error |
| `P6-6.46` | MUST | Instance bound refuses the start |
| `P6-6.47` | MUST NOT | No silent bound |
| `P6-6.48` | MUST | Permitted computations only |
| `P6-6.49` | MUST NOT | No inference of a determination |
| `P6-6.50` | MUST NOT | No learning from executions |
| `P6-6.51` | MUST NOT | No assessment of process fitness |
| **Section 7** | | **Outcome and failure taxonomy** |
| `P6-7.1` | MUST | Closed instance outcome set |
| `P6-7.2` | MUST | Unwaited work distinguished at the instance level |
| `P6-7.3` | MUST | Stall is not completion |
| `P6-7.4` | MUST | Bound termination distinguished from fault |
| `P6-7.5` | MUST NOT | No mapping onto a success and failure pair |
| `P6-7.6` | MUST | Closed activity outcome set |
| `P6-7.7` | MUST | Unknown outcome distinguished from fault |
| `P6-7.8` | MUST | Forced outcome permanently marked |
| `P6-7.9` | MUST | Bound exhaustion members distinguished |
| `P6-7.10` | MUST | Work left undone raises a review obligation |
| `P6-7.11` | MUST | Defects reported as defects |
| `P6-7.12` | MUST | Second arrival not absorbed |
| `P6-7.13` | MUST | Gap suspends the instance |
| `P6-7.14` | MUST NOT | No defect as a fault |
| `P6-7.15` | MUST | Envelope completeness |
| `P6-7.16` | MUST NOT | No envelope reduction |
| `P6-7.17` | MUST | Review obligations raised on the enumerated conditions |
| `P6-7.18` | MUST | Obligation distinguished from task |
| `P6-7.19` | MUST | Open obligations countable |
| `P6-7.20` | MUST | Refusal codes |
| `P6-7.21` | MUST | Refusal states what must change |
| `P6-7.22` | MUST | Refusals recorded |
| `P6-7.23` | MUST NOT | No refusal as an outcome |
| `P6-7.24` | MUST | Recording obligations honoured |
| `P6-7.25` | MUST | Emission obligations honoured |
| `P6-7.26` | MUST | Caller obligations documented |
| `P6-7.27` | MUST NOT | No completion language for a stall |
| `P6-7.28` | MUST | A stopped execution is never a finished one |
| `P6-7.29` | MUST | An operator's assertion is never a component's result |
| `P6-7.30` | MUST | A completed handler is never a restored position |
| **Section 8** | | **Observability and the audit record** |
| `P6-8.1` | MUST | Log is the audit record of the engine |
| `P6-8.2` | MUST | Steps registered as trail acts |
| `P6-8.3` | MUST NOT | No log as trail |
| `P6-8.4` | MUST NOT | No separate mutable log |
| `P6-8.5` | MUST | Own operations recorded |
| `P6-8.6` | MUST | Declared grain |
| `P6-8.7` | MUST | Attempts and iterations recorded individually |
| `P6-8.8` | MUST | Skipped activities recorded |
| `P6-8.9` | MUST | Counting grain stated with every count |
| `P6-8.10` | MUST | Derivation sufficiency |
| `P6-8.11` | MUST | Unknown outcomes recorded as unknown |
| `P6-8.12` | MUST | Conventions recorded |
| `P6-8.13` | MUST | Precondition outcomes recorded, including passes |
| `P6-8.14` | MUST | Periodic replay sampling |
| `P6-8.15` | MUST | Divergence recorded, not corrected |
| `P6-8.16` | MUST | Reads recorded |
| `P6-8.17` | MUST | Withholding recorded |
| `P6-8.18` | MUST | Interventions recorded with the operator |
| `P6-8.19` | SHOULD | Read records retained with the instance |
| `P6-8.20` | MUST | Signals produced |
| `P6-8.21` | MUST | Signals derived from events |
| `P6-8.22` | MUST NOT | No suppression of a signal |
| `P6-8.23` | MUST | Stall signal standing |
| `P6-8.24` | MUST | Waiting signal states the releaser |
| `P6-8.25` | MUST | Disposal exception trend available |
| `P6-8.26` | SHOULD | Signal thresholds declared |
| `P6-8.27` | MUST | Package sufficiency |
| `P6-8.28` | MUST | Definition content included or its absence stated |
| `P6-8.29` | MUST | Analyses included, including those not performed |
| `P6-8.30` | MUST | Interventions and forced outcomes included |
| `P6-8.31` | MUST | Limit statements included |
| `P6-8.32` | MUST | Absence stated, not omitted |
| `P6-8.33` | MUST | Package digest |
| `P6-8.34` | MUST | Self description |
| `P6-8.35` | MUST | Retention obtained, not assigned |
| `P6-8.36` | MUST NOT | No retention authority over routed artifacts |
| `P6-8.37` | MUST | Definitions outlive their instances |
| `P6-8.38` | MUST | Compensation records outlive the instance |
| `P6-8.39` | MUST | Separate retention per structure |
| `P6-8.40` | MUST NOT | No disposal under an open review obligation |
| `P6-8.41` | MUST | Disposal recorded and citable |
| `P6-8.42` | MUST NOT | No amendment of an event |
| `P6-8.43` | MUST NOT | No state setting |
| `P6-8.44` | MUST NOT | No removal of a forced marking |
| `P6-8.45` | MUST | Migration preserves the source segment |
| `P6-8.46` | MUST | Migration preserves identity and digests |
| `P6-8.47` | MUST NOT | No bulk assignment on import |
| **Section 9** | | **Extension model** |
| `P6-9.1` | MUST | Closed sets not extended |
| `P6-9.2` | MUST | Unknown member is a defect, not a default |
| `P6-9.3` | MUST | Open sets registered |
| `P6-9.4` | MUST NOT | No control flow construct by registration |
| `P6-9.5` | MUST | Registry as controlled document |
| `P6-9.6` | MUST NOT | No key reuse |
| `P6-9.7` | MUST | Deprecation rather than removal |
| `P6-9.8` | MUST | Registry version pinned to the instance |
| `P6-9.9` | MUST | Semantics in the entry |
| `P6-9.10` | MUST | Invocation target declared per kind |
| `P6-9.11` | MUST NOT | No determination from an unregistered source |
| `P6-9.12` | MUST | Compensability admissibility declared |
| `P6-9.13` | MUST | Wait semantics declared |
| `P6-9.14` | MUST | Stability declared |
| `P6-9.15` | MUST | Stable schemes required for migration mappings |
| `P6-9.16` | MUST NOT | No cross scheme comparison |
| `P6-9.17` | MUST | Class requirements declared and enforced |
| `P6-9.18` | MUST | Maximum lifetime declared per class |
| `P6-9.19` | MUST | Owning component per class |
| `P6-9.20` | MUST | Correlation uniqueness semantics declared |
| `P6-9.21` | MUST | Rebinding after termination declared |
| `P6-9.22` | MUST | Quantifiability and units declared |
| `P6-9.23` | MUST | Later reversibility declared |
| `P6-9.24` | MUST | Expected owner declared |
| `P6-9.25` | MUST | External notification obligation declared |
| `P6-9.26` | MUST | Both registered and both recorded |
| `P6-9.27` | MUST | Deprecation without invalidation |
| `P6-9.28` | MUST | Refusal codes registered with remedy |
| `P6-9.29` | MUST | Event types registered |
| `P6-9.30` | MUST | Intervention kinds registered |
| `P6-9.31` | MUST | Subprocess as a separate instance |
| `P6-9.32` | MUST | Synchronisation declared on subprocess activities |
| `P6-9.33` | MUST | Definition inclusion by pinned version only |
| `P6-9.34` | MUST NOT | No cyclic inclusion or instantiation |
| `P6-9.35` | MUST NOT | No cross instance state read |
| `P6-9.36` | MUST | Child compensation requested, not performed |
| `P6-9.37` | MUST | Composition depth declared |
| **Section 10** | | **Standards and specifications** |
| `P6-10.1` | MUST | Cited edition recorded |
| `P6-10.2` | MUST | Basis marked |
| `P6-10.3` | MUST | BPMN document identified precisely |
| `P6-10.4` | MUST | Practice basis recorded |
| `P6-10.5` | MUST | Unsourced requirements identified |
| **Section 11** | | **Anti patterns** |
| `P6-11.1` | MUST NOT | No business fact as a variable |
| `P6-11.2` | MUST NOT | No implicit termination |
| `P6-11.3` | MUST NOT | No condition evaluation |
| `P6-11.4` | MUST | Exclusivity or a decision |
| `P6-11.5` | MUST NOT | No approximated inclusive join |
| `P6-11.6` | MUST | Disposition declared and unwaited work recorded |
| `P6-11.7` | MUST NOT | No unbounded dynamic instantiation |
| `P6-11.8` | MUST | Per iteration compensation in reverse order |
| `P6-11.9` | MUST | Compensation outcome recorded, not inferred |
| `P6-11.10` | MUST | Compensability declared and the condition reported |
| `P6-11.11` | MUST | Residue enumerated and assigned |
| `P6-11.12` | MUST | Attempts recorded separately, unknown outcomes preserved |
| `P6-11.13` | MUST NOT | No exactly once claim |
| `P6-11.14` | MUST | Intervention is an authorised event |
| `P6-11.15` | MUST | Forced outcomes marked permanently |
| `P6-11.16` | MUST | Token move assessed for soundness |
| `P6-11.17` | MUST | Instances pinned; migration governed |
| `P6-11.18` | MUST | Withdrawal reports its population and definitions outlive instances |
| `P6-11.19` | MUST | Steps are trail acts, not citations |
| `P6-11.20` | MUST | Outcome recorded before referral |
| `P6-11.21` | MUST | Observed time recorded and read |
| `P6-11.22` | MUST | Unmatched events recorded and retained |
| `P6-11.23` | MUST NOT | No work item state |
| `P6-11.24` | MUST | Undecidability declared, not reported as soundness |
| `P6-11.25` | MUST NOT | No retention authority over routed artifacts |
| `P6-11.26` | MUST NOT | No transformation, enrichment or content routing |
| **Section 12** | | **Boundaries with other parts** |
| `P6-12.1` | MUST | Declared allocation |
| `P6-12.2` | MUST | Refusal rather than substitution |
| `P6-12.3` | MUST NOT | No reaching past a neighbour |
| `P6-12.4` | MUST NOT | No document state held |
| `P6-12.5` | MUST | Status changed by invocation, not by advance |
| `P6-12.6` | MUST NOT | No process identity required of Part 1 |
| `P6-12.7` | MUST | Report referenced, not the branch |
| `P6-12.8` | MUST NOT | No condition evaluation |
| `P6-12.9` | MUST | Indeterminate verdict handled by declaration |
| `P6-12.10` | MUST | Steps registered as acts |
| `P6-12.11` | MUST NOT | No basis held |
| `P6-12.12` | MUST | Compensation recorded as an act with its residue |
| `P6-12.13` | MUST NOT | No registration state held |
| `P6-12.14` | MUST NOT | No transformation |
| `P6-12.15` | MUST | Concepts resolved where referenced |
| `P6-12.16` | MUST | Decision referenced, not the branch |
| `P6-12.17` | MUST NOT | No selection by branch order |
| `P6-12.18` | MUST | Undecidable outcome recorded before referral |
| `P6-12.19` | MUST | Default is a declared artifact, not a diagram property |
| `P6-12.20` | MUST | Decisions consumed, not made |
| `P6-12.21` | MUST | Interventions authorised |
| `P6-12.22` | MUST NOT | No authorisation as a branch |
| `P6-12.23` | MUST NOT | No work item lifecycle |
| `P6-12.24` | MUST | Completion received as an activity outcome |
| `P6-12.25` | MUST | Escalation does not advance |
| `P6-12.26` | MUST | Review obligations passed, not managed |
| `P6-12.27` | MUST NOT | No schema validation or versioning |
| `P6-12.28` | MUST | Schema reference recorded |
| `P6-12.29` | MUST | Collections enumerated by pin |
| `P6-12.30` | MUST | Enumeration pin recorded with the instance count |
| `P6-12.31` | MUST | Digest is the interface |
| `P6-12.32` | MUST NOT | No process state in the store |
| `P6-12.33` | MUST | Read only assessment |
| `P6-12.34` | MUST NOT | No self assessment as assessment |
| `P6-12.35` | MUST | Instance values exposed for independent demonstration |
| `P6-12.36` | MUST NOT | No routing on a model output |
| `P6-12.37` | MUST | Model retries governed by the declared policy |
| `P6-12.38` | MUST | Agent attribution supplied |
| `P6-12.39` | MUST | Authority declared, not assumed |
| `P6-12.40` | MUST | Non results propagated unmodified |
| `P6-12.41` | MUST | Disposability exposed to composition |
| **Section 13** | | **What could not be established** |
| `P6-13.1` | MUST | Verification before approval |
| `P6-13.2` | MUST | Gaps declared, not filled |
| `P6-13.3` | SHOULD | Open questions carried forward |

### Derived counts

Every figure below is derived by extraction from the clause text of this document and not asserted independently. The grain of counting is stated for each figure. A clause is one line of the document matching the clause heading form given under Binding of requirement language, that is, an identifier of the form `P6-S.N`, a modality in parentheses, and a subject label. Narrative sentences containing a requirement keyword are not clauses and are not counted; per that same section they are not binding.

**Total clauses.** 456. Grain: one clause heading.

**By modality.** Grain: one clause heading, counted once against its single declared modality.

| Modality | Clauses | Share |
| --- | --- | --- |
| MUST | 346 | 75.9% |
| MUST NOT | 104 | 22.8% |
| SHOULD | 5 | 1.1% |
| SHOULD NOT | 0 | 0.0% |
| MAY | 1 | 0.2% |
| **All** | **456** | **100.0%** |

**Absolute requirements.** 450 clauses carry MUST or MUST NOT and are therefore conditions of conformance. 5 carry SHOULD or SHOULD NOT and require a recorded reason where not satisfied. 1 carry MAY and constrain nothing. Grain: one clause heading. These three figures sum to the total.

**By section.** Grain: one clause heading, attributed to the numbered section in which its heading appears.

| Section | Title | Clauses | MUST | MUST NOT | SHOULD | SHOULD NOT | MAY |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Scope and responsibilities | 16 | 9 | 6 | 1 | 0 | 0 |
| 2 | Terminology | 8 | 1 | 6 | 1 | 0 | 0 |
| 3 | Data model | 122 | 97 | 24 | 0 | 0 | 1 |
| 4 | Interfaces | 40 | 32 | 8 | 0 | 0 | 0 |
| 5 | State model | 30 | 24 | 6 | 0 | 0 | 0 |
| 6 | Execution semantics | 51 | 40 | 11 | 0 | 0 | 0 |
| 7 | Outcome and failure taxonomy | 30 | 25 | 5 | 0 | 0 | 0 |
| 8 | Observability and the audit record | 47 | 36 | 9 | 2 | 0 | 0 |
| 9 | Extension model | 37 | 31 | 6 | 0 | 0 | 0 |
| 10 | Standards and specifications | 5 | 5 | 0 | 0 | 0 | 0 |
| 11 | Anti patterns | 26 | 17 | 9 | 0 | 0 | 0 |
| 12 | Boundaries with other parts | 41 | 27 | 14 | 0 | 0 | 0 |
| 13 | What could not be established | 3 | 2 | 0 | 1 | 0 | 0 |
| **All** | | **456** | **346** | **104** | **5** | **0** | **1** |

**Ordinal integrity.** In this version, the highest ordinal in each section equals the number of clauses in that section, so no identifier has yet been retired. This will cease to be true at the first clause removal, and the count rather than the highest ordinal is then the figure to rely on.

## 1. Scope and responsibilities

### 1.1 What this component is

This part specifies a component that sequences work: it determines what runs next, waits for what must be waited for, repeats what must be repeated, undoes what can be undone, and holds the state of an execution in progress.

The component exists to answer one question reliably: **what ran, in what order, why did the execution take this path, and would every business fact survive the disposal of every process instance.** The second half of that question is not an afterthought. It is the constraint under which the whole part is written.

Five prior parts have each required, in the same terms, that their own state be correct without reference to any process instance and that they remain correct where the orchestrator is replaced or its instances are disposed of. `Part 1` clauses P1-12.11 and P1-12.12 say it for document status. `Part 2` clauses P2-12.15 and P2-12.16 say it for verdicts. `Part 3` clauses P3-12.14 and P3-12.15 say it for provenance. `Part 4` clauses P4-12.15 and P4-12.16 say it for definitions. `Part 5` clauses P5-12.19 and P5-12.20 say it for decisions.

Taken together they amount to one requirement, and it is the spine of this part.

**The process instance is disposable.** It holds the path and nothing else. Every fact it touches is owned elsewhere, recorded elsewhere and answerable elsewhere. An organisation that deleted every process instance in this component would lose the ability to say in what order things happened and would lose nothing else.

That requirement is unusual among the parts of this standard because it is a requirement that this component be **less** than implementations of it habitually are. A workflow engine accretes: a variable here to avoid a lookup, a status there to avoid a call, a copy of a value because the owning system is slow. Each accretion is individually reasonable and the aggregate is a shadow system of record with no versioning, no approval, no effectivity and no retention, whose contents diverge from their owners silently. Section 3.12 and section 11.1 are written against that accretion and clause P6-1.3 states the test.

Three further properties distinguish the component and each is a subject the authoring brief named.

**It joins honestly.** A join that proceeds without waiting for every incoming branch must declare what became of the branches it did not wait for, and the work those branches performed must be recorded whether or not anything used it. Section 3.6 gives the join taxonomy and section 3.7 restricts the one join whose semantics no standard has ever pinned down.

**It bounds its loops.** Every repetition declares a bound, exhausting the bound is an outcome rather than a failure, and the provenance of an instance count is recorded. Section 3.8 specifies it.

**It compensates without pretending.** Compensation is not rollback and it does not always work. A compensating act can fail, can be impossible because the money has moved or the notice has been sent, or can leave a residue that somebody must own. Sections 3.9 and 3.10 give compensation its own outcome taxonomy, and the taxonomy is the contribution: no reviewed standard admits that a compensation might not have restored anything.

The component is accountable for the following.

Process definitions and their versions, as governed artifacts, and the pinning of a running instance to the version under which it started.

Activity definitions, their kinds, and the declaration of whether each is compensable and what residue it leaves if it is not.

Control flow: sequences, splits, joins, conditional routing, and the requirement that every conditional branch be attributable to an external determination rather than to a condition this component evaluated.

The join taxonomy, including the restriction of the inclusive join to forms in which its semantics are decidable, and the declared disposition of branches a partial join did not wait for.

Loops and multiple instance activities, their declared bounds, the provenance of an instance count, and the outcome of exhausting a bound.

Scopes, compensation handlers, fault handlers and termination handlers, the order in which compensation is performed, and the requirement that the order be declared.

Compensation outcomes, including partial compensation and impossible compensation, and the enumeration and assignment of residue.

Events, timers and correlation, and the recording of an observed time as a fact rather than a re evaluation of a clock.

Process state as a projection of an append only event log, and the disposability of the instance.

Invocation attempts, separately from activity outcomes, so that a retry is visible.

Version pinning and the migration of a running instance, only under a declared and governed mapping.

Static analysis: the soundness of a process definition where its form admits the analysis, and the honest reporting of the forms where it does not.

The audit record of all of the above, at a grain sufficient to replay any execution.

### 1.2 What this component is not

This is the longest exclusion list in the standard, and the length is the point. Everything is tempted to live in the process, because the process is where the work happens and because a process instance is the one place a developer can put something without asking anybody.

The component is not a data store. It holds no business fact. A process variable carrying a customer's address, a claim amount or an approval status is a copy of a fact whose owner is elsewhere, and it will diverge. Section 3.12 restricts what a variable may contain and clause P6-1.3 makes the restriction testable.

The component does not own document status, version identity or effectivity. Those are `Part 1`'s and section 12.1 is the reciprocal that part requires.

The component does not own verdicts. It does not evaluate a condition. A gateway condition is a `Part 2` evaluation report obtained beforehand and cited, and section 12.2 is the reciprocal.

The component does not own bases. A process step is not a reason. `Part 3` clause P3-12.14 requires a step to be registered as an act in a trail rather than as a citation in a basis, and section 12.3 is the reciprocal.

The component does not own definitions, registration state or lineage. Those are `Part 4`'s.

The component does not own decisions, criteria or outcomes. Where an execution branches on a choice among alternatives, the choice is a `Part 5` decision obtained beforehand and cited, and section 12.5 is the reciprocal.

The component is not a policy decision point. Whether a principal may start, cancel, retry or migrate an instance is an authorisation belonging to `Part 7`.

The component is not a human task manager. It owns the fact that a human activity exists at a position in the flow. The offering, allocation, escalation, delegation, queue and case belong to `Part 8`, and section 12.8 draws the line, which is the most delicate boundary in the part.

The component is not a schema registry, a reference data master, an artifact store, a conformance assessor or a model runtime.

The component is not an integration platform. It invokes; it does not transform, route by content, enrich or mediate. Content based routing is a decision, transformation is a derivation whose lineage belongs to `Part 4` and `Part 3`, and an engine that acquires either has acquired business logic with no artifact.

**P6-1.1 (MUST) Purpose satisfaction.** An implementation must be able to state, for any process instance within its retained history, which activities ran, in what order, what each returned by reference, and the external determination to which each conditional branch is attributable, by the mechanism specified in section 6.

**P6-1.2 (MUST) Path only.** An implementation must record the path of an execution and must not record, as its own authoritative content, any fact owned by another component.

**P6-1.3 (MUST) Disposability demonstrable.** An implementation must be able to demonstrate that the disposal of every process instance it holds would leave every business fact recorded by another component intact and answerable, and must record the demonstration.

**P6-1.4 (MUST NOT) No condition evaluation.** An implementation must not evaluate a condition in order to route an execution, and must obtain every conditional branch from a `Part 2` evaluation report or a `Part 5` decision, per section 3.13.

**P6-1.5 (MUST NOT) No selection among branches.** An implementation must not select among candidate branches by any criterion of its own, including the order in which branches are declared, and must obtain every such selection from `Part 5`.

**P6-1.6 (MUST) Joins declare their dispositions.** An implementation must declare, for every join that may proceed without every incoming branch, what becomes of the branches it did not wait for, and must record the work those branches performed.

**P6-1.7 (MUST) Loops bounded.** An implementation must declare a bound on every repetition and every multiple instance activity, and must return the corresponding outcome of section 7.3 where a bound is exhausted.

**P6-1.8 (MUST) Compensation outcomes distinguished.** An implementation must record whether a compensation restored the position fully, partially, or not at all, and must enumerate the residue where it did not, per section 3.10.

**P6-1.9 (MUST) State is a projection.** An implementation must compute the state of every process instance from an append only event log and must not hold it as mutable state, per section 3.14.

**P6-1.10 (MUST) Instance pinned to its definition version.** An implementation must pin every running instance to the process definition version under which it started and must migrate it only under a declared mapping, per section 3.16.

**P6-1.11 (MUST NOT) No update in place.** An implementation must not represent any state change specified by this part as a modification or deletion of a previously written event.

**P6-1.12 (MUST NOT) No retention authority over what it routed.** An implementation must not govern the retention of any document, verdict, determination, definition or decision it routed, and must not permit the disposal of a process instance to cause the disposal of any of them.

**P6-1.13 (MUST NOT) No absorption of neighbouring responsibilities.** An implementation must not hold business facts, evaluate constraints, make decisions, decide authorisation, assign human work, validate against schemas, master reference data or invoke models, as those responsibilities are allocated in section 12.

**P6-1.14 (SHOULD) Declared exclusions.** An implementation should publish, as a controlled document under `Part 1`, the list of section 1.2 exclusions that it in fact provides by other means, so that a reader can tell what the implementation does not guarantee.

**P6-1.15 (MUST NOT) No conformance self assertion.** An implementation must not assert conformance to this part on the basis of its own internal checks alone, and must not represent such an assertion as an assessment.

**P6-1.16 (MUST) Time horizon declaration.** An implementation must declare the period for which it undertakes to answer the purpose question, as a duration or an absolute date rather than as an indefinite commitment.

### 1.3 Why the disposability requirement is the hard one

Every other requirement in this part is a matter of getting a well studied mechanism right. Control flow patterns have been catalogued for a quarter of a century, compensation has a normative specification, and soundness has a formal definition and a decision procedure. The engineering is understood.

Disposability is different, because it is not a mechanism but a discipline, and it fails gradually.

The sequence is always the same. An activity needs a value that another component owns. Fetching it is a call, the call is slow or the component is unavailable, and the value is already in the message that started the process. So the value is put in a process variable. It is used by three subsequent activities and by a gateway condition. Six months later the owning component's copy is corrected and the process instance's copy is not, because nothing knows the copy exists. A year later somebody writes a report from the process instances, because that is where the data is convenient, and the report disagrees with the system of record. Two years later the process definition is the only place that records what the value meant, because the variable's name is the only documentation.

At no point in that sequence did anybody decide to build a second system of record. Each step was a reasonable local optimisation, and the aggregate is exactly what `Part 1` section 11.15, `Part 2` section 12.6 and `Part 4` section 11.1 each describe from their own side.

The requirement in clause P6-1.3 is therefore stated as a demonstration rather than a prohibition. A prohibition on holding business data is unenforceable, because whether a value is a business fact or a control value is a judgement. A periodic demonstration that the instances could be deleted without loss is enforceable, is cheap, and fails visibly as soon as the accretion begins.

### 1.4 The reader this part is written for

Two readers, and unusually they want the same thing for different reasons.

The first is an operator, at three in the morning, asked why forty thousand instances are stuck. That reader needs to know what each instance is waiting for, whether it can proceed, and whether anything will ever cause it to.

The second is an investigator, years later, asked why a particular case took the path it took. That reader needs the order, the branch attributions, and the external determinations by reference.

Both are served by the same discipline: an append only event log from which state is derived, explicit termination so that a stalled instance is distinguishable from a running one, and branch attribution so that a path is explicable. Section 5.2 and section 7.2 are written for the first reader, and everything else serves both.
## 2. Terminology

Terms are defined here only if this component owns them. A term owned by another part is cited to that part and is not redefined. Where a term is taken from an external standard, the standard is named. Where this part narrows or diverges from the external definition, the divergence is stated.

### 2.1 Terms owned by this part

**Process definition.** The governed artifact specifying a flow: its activities, its control flow, its scopes, its handlers and its bounds.

**Process instance.** One execution of a process definition version, consisting of an event log and the state derived from it. Disposable, per clause P6-1.3.

**Activity.** A unit of work in a process definition. An activity is a position in the flow and an instruction to invoke something; it is not the work itself.

**Activity instance.** One execution of an activity within one process instance.

**Invocation attempt.** One attempt to invoke the thing an activity instance names. Recorded separately from the activity instance's outcome, so that a retry is visible.

**Flow token.** A unit of control located at a position in a process instance. The term follows BPMN 2.0.2, which describes execution semantics in terms of tokens; this part uses it for the same purpose and requires the token multiset to be derived rather than stored.

**Split.** A construct from which more than one outgoing flow may proceed.

**Join.** A construct at which more than one incoming flow converges.

**Structural construct.** A split or join whose behaviour is determined by the topology of the definition alone: a parallel split, a synchronising join, a sequence. Distinguished throughout from a conditional construct.

**Conditional construct.** A split whose outgoing flow depends on something other than topology. Every conditional construct requires an external determination, per section 3.13.

**Branch attribution.** The recorded reference to the external determination to which a conditional branch is attributable.

**Scope.** A nested region of a process definition to which handlers may be attached and which is the unit of compensation. Term and sense follow WS-BPEL 2.0, which attaches compensation, fault, termination and event handlers to scopes.

**Compensation.** The performance of a semantically inverse act to undo the effect of a completed activity or scope. Distinguished from rollback, which restores a prior state, and from retry, which attempts the same act again.

**Compensable.** The declared property of an activity that a compensating act exists for it.

**Residue.** The part of an effect that a compensation did not undo, enumerated and assigned to an owner.

**Compensation order.** The declared order in which the compensation handlers of completed scopes are performed. WS-BPEL 2.0 makes reverse order of completion the default; section 3.9 adopts that default and requires any other order to be declared and justified.

**Fault.** A condition arising within a scope that prevents its normal completion.

**Fault handler.** A declared response to a fault within a scope.

**Termination handler.** A declared response to the forced termination of a scope from outside it.

**Cancellation region.** A declared set of activities whose running instances are terminated together. The term is used because the presence of one moves a process definition into a class for which soundness is undecidable; see section 6.7.

**Multiple instance activity.** An activity executed once per member of a collection. The provenance of the instance count is recorded, per section 3.8.

**Repetition.** A structured loop with a declared bound and a declared exit.

**Arbitrary cycle.** A cycle in the control flow that is not a structured repetition. Admitted only under a declared bound, per section 3.8.

**Bound.** A declared limit on iterations, instances, elapsed logical time or a declared resource, whose exhaustion is an outcome rather than a failure.

**Correlation key.** A value by which an inbound event is matched to a process instance.

**Stall.** The condition in which a process instance has no runnable work and has not terminated explicitly. A distinct state, per section 5.2, because implicit termination makes a deadlocked instance indistinguishable from a completed one.

**Soundness.** The property of a process definition that from every reachable state it is possible to reach proper completion, that proper completion leaves no work outstanding, and that no activity is unreachable. The three conditions follow the workflow net literature and section 6.7 states them.

**Migration.** The rebinding of a running instance from the definition version it was pinned to onto a later version, under a declared mapping.

**Application time.** The time dimension in which a process definition is in force. Used unchanged from `Part 1` section 2.1.

**Knowledge time.** The instant at which this component durably recorded an event, assigned by this component. Used unchanged from `Part 1`.

**Occurrence time.** The instant at which a recorded act happened in the world, as asserted by an actor or observed by this component. Used unchanged from `Part 1`, with the extension that this component observes elapsed time and section 6.5 states the consequence.

**Pin.** A recorded identity and version of something an execution depended on. Used unchanged from `Part 2` section 2.1.

### 2.2 Clauses governing terminology

**P6-2.1 (MUST) Single meaning per term.** An implementation must use each term defined in section 2.1 with the meaning given there in all of its interfaces, records, reports and documentation.

**P6-2.2 (MUST NOT) No redefinition.** An implementation must not use a term defined in section 2.1 for a different concept, and must not use a different term for a concept defined in section 2.1 in any interface specified by this part.

**P6-2.3 (MUST NOT) No collapsing of structural and conditional constructs.** An implementation must not use one term or one construct for a split whose behaviour follows from topology and one whose behaviour depends on a determination.

**P6-2.4 (MUST NOT) No collapsing of compensation, rollback and retry.** An implementation must not use one term for a semantically inverse act, a restoration of prior state and a repeated attempt.

**P6-2.5 (MUST NOT) No collapsing of an activity and an invocation attempt.** An implementation must not use one record for the position in the flow and for each attempt to invoke what it names.

**P6-2.6 (MUST NOT) No collapsing of completion and stall.** An implementation must not use one state for an instance that terminated and one that has no runnable work and did not terminate.

**P6-2.7 (MUST NOT) No collapsing of the three clocks.** An implementation must not use one term or one field for more than one of application time, knowledge time and occurrence time.

**P6-2.8 (SHOULD) Term registry.** An implementation should publish the terms it adds beyond section 2.1, with definitions, as a controlled document under `Part 1`.
## 3. Data model

The model is stated as entities with typed fields. For each field the model gives its type, whether it is required, its cardinality, and what its absence means. Absence semantics are stated because in this component the commonest wrong inference from a missing field is that a branch was taken for a reason nobody recorded.

### 3.1 Type vocabulary

| Type | Value space | Notes |
| --- | --- | --- |
| `ID` | An opaque, globally unique, immutable identifier | Never reused. Never parsed for meaning. |
| `URN` | A persistent name in a declared namespace | Resolvable by the component owning the namespace. |
| `ATIME` | An instant in application time | The dimension in which definitions are in force. |
| `KTIME` | An instant in knowledge time, assigned by this component | Never accepted from a caller. |
| `OTIME` | An instant asserted by an actor or observed by this component | Section 6.5 states the observation case. |
| `SEQ` | A monotonically increasing ordinal within a named stream | The event log's order. Total within the instance. |
| `DIGEST` | An algorithm identifier and a value | Algorithm from the registry of section 9.7. |
| `ENUM` | A member of a named closed or registered set | The set is named at every point of use. |
| `TEXT` | A sequence of characters intended for a person | Carries a `LANG`. |
| `LANG` | A language tag per BCP 47 | Required wherever `TEXT` appears. |
| `PIN` | An identity, a version and where available a digest | Sufficient to obtain the identical artifact again. |
| `CITEREF` | A citation resolvable under `Part 1`, carrying its mode | Used for definition and handler authority. |
| `DETREF` | A reference to a `Part 2` evaluation report or a `Part 5` decision | Carries which, and the whole envelope by pin. |
| `ACTOR` | An opaque reference to a person, organisation or automated agent | Carries its kind. Resolved elsewhere. |
| `AUTHREF` | A reference to an authorisation decision made by `Part 7` | Recorded, never evaluated here. |
| `NODEREF` | A position within a process definition version | In a declared addressing scheme. |
| `CORRKEY` | A correlation key value and the scheme it is drawn from | Section 3.11. |
| `DURATION` | A length of time, independent of any instant | |
| `COUNT` | A non negative integer | Grain stated wherever reported. |
| `TRUTH` | One of `TRUE`, `FALSE`, `INDETERMINATE` | The three valued domain, used unchanged from `Part 2` section 6.2. |

The `DETREF` type exists so that a branch attribution cannot be recorded as a bare boolean. A gateway that took the left branch because a condition was true records the report that established the truth, not the truth, and the type makes the requirement structural rather than a matter of discipline.

**P6-3.1 (MUST) Declared types.** An implementation must be able to state, for every field it holds that corresponds to a field in this section, which type of the table above it carries.

**P6-3.2 (MUST NOT) No semantic identifiers.** An implementation must not derive the routing, ordering, compensability or state of anything from the characters of its `ID` or `URN`.

**P6-3.3 (MUST) Language tag present.** An implementation must record a `LANG` with every `TEXT` value and must not default it silently.

**P6-3.4 (MUST NOT) No caller supplied knowledge time.** An implementation must assign every `KTIME` itself and must reject an event supplying one.

**P6-3.5 (MUST) Determination reference, not its value.** An implementation must record a `DETREF` for every branch attribution and must not record only the truth value or the outcome value the determination produced.

**P6-3.6 (MUST) Three valued domain used unchanged.** An implementation must use the truth domain of `Part 2` section 6.2 wherever it holds or reports a truth value and must not introduce a two valued reduction.

### 3.2 The engine owns the path, not the facts

This section states the spine and the two tests by which it is enforced.

**What the engine owns.** The topology of the definition. Which activity instances were created and in what order. Which flow tokens exist and where. Which scopes are open and which have completed. Which handlers ran. Which bounds were exhausted. Which invocation attempts were made and what each returned by reference. Which external determination each conditional branch is attributable to. Which correlation keys the instance responds to. The time it observed for each timer.

**What the engine does not own.** Anything in the preceding list is control. Anything not in it is a fact, and every fact has an owner in another part.

The distinction is not always obvious and two cases require care.

**A counter is control.** The number of iterations a loop has performed is a property of the execution and is the engine's own. A count of the items in a collection the loop is iterating over is a fact about the collection, whose owner is elsewhere, and recording it as a variable is recording a fact.

**A flag is usually a fact.** A boolean recording that approval was obtained looks like control and is a fact: the approval is a `Part 1` act with a signature, and the flag is a copy of it. The engine records that the activity which obtained the approval completed, and the approval itself is resolved from `Part 1` when needed. The distinction matters because the flag will be true in the instance after the approval has been withdrawn.

Two tests are specified and both are required, because neither alone is sufficient.

**The disposal test**, clause P6-1.3 and clause P6-3.9: could every instance be deleted without loss. This is the definitive test and it is expensive to perform honestly.

**The variable test**, section 3.12: every value held in an instance is of a declared kind from a closed set, and no kind admits a business fact. This is cheap, is checkable continuously, and is a proxy: it catches the accretion at the moment it happens rather than after a year.

**P6-3.7 (MUST) Control and fact distinguished.** An implementation must be able to state, for every value it holds in a process instance, which of the control kinds of section 3.12 it is, and must not hold a value of no such kind.

**P6-3.8 (MUST NOT) No fact as a variable.** An implementation must not hold, as an instance value, a copy of a value whose authoritative owner is another component, and must record a reference to it instead.

**P6-3.9 (MUST) Periodic disposal demonstration.** An implementation must perform, on a declared cycle, a demonstration that disposal of its instances would leave every business fact answerable, must record the demonstration and every exception it found, and must declare the cycle.

**P6-3.10 (MUST) Exceptions countable.** An implementation must be able to report every instance value that failed the disposal demonstration, by process definition version and by value kind, and must include the count in the signals of section 8.5.

### 3.3 Entity inventory

Every entity is immutable once written. A change is a new event; nothing specified in this part is ever updated in place. The reason is stronger here than elsewhere: a process instance's state is the thing operators most want to edit, because editing it is the fastest way to unstick a stuck instance, and an editable instance state makes the execution record worthless as an account of what happened.

| Group | Entity | Purpose |
| --- | --- | --- |
| Definition | `process_definition` | The persistent identity of a process. |
| Definition | `process_definition_version` | One immutable state of a process definition. |
| Definition | `activity_definition` | One activity in a definition version, with its kind and compensability. |
| Definition | `flow_definition` | One directed connection between positions. |
| Definition | `split_definition` | A split, with its kind and its determination requirement. |
| Definition | `join_definition` | A join, with its kind and its branch disposition. |
| Definition | `scope_definition` | A scope and its handler attachments. |
| Definition | `handler_definition` | A compensation, fault, termination or event handler. |
| Definition | `bound_declaration` | A declared bound on a repetition, multiple instance activity or cycle. |
| Definition | `cancellation_region` | A declared set of activities cancelled together. |
| Definition | `correlation_scheme` | How inbound events are matched to instances. |
| Definition | `definition_analysis` | A recorded static analysis over a definition version. |
| Definition | `migration_mapping` | A governed mapping from one definition version to another. |
| Instance | `process_instance` | The identity of one execution and its pinned definition version. |
| Instance | `instance_event` | One appended event in the instance's log. |
| Instance | `activity_instance` | One execution of an activity. |
| Instance | `invocation_attempt` | One attempt to invoke what an activity names. |
| Instance | `branch_attribution` | The determination to which a conditional branch is attributable. |
| Instance | `join_resolution` | How a join was satisfied and what became of unwaited branches. |
| Instance | `iteration` | One pass of a repetition or one member instance of a multiple instance activity. |
| Instance | `scope_instance` | One execution of a scope. |
| Instance | `instance_value` | One control value held by an instance, of a declared kind. |
| Instance | `timer_observation` | An observed elapse of time, recorded as a fact. |
| Instance | `correlation_binding` | A correlation key bound to an instance. |
| Instance | `instance_pin` | One artifact the execution depended on. |
| Compensation | `compensation_request` | A request to compensate a scope or activity. |
| Compensation | `compensation_execution` | One performance of a compensating act. |
| Compensation | `compensation_outcome` | The enumerated result of a compensation. |
| Compensation | `residue` | The part of an effect a compensation did not undo. |
| Compensation | `residue_assignment` | The owner to whom a residue was assigned. |
| Migration | `migration_execution` | One migration of a running instance. |
| Registry | `activity_kind_registration` | A registered activity kind. |
| Registry | `join_kind_registration` | Reserved. Join kinds are closed; see section 9.1. |
| Registry | `addressing_scheme_registration` | A registered position addressing scheme. |
| Registry | `correlation_scheme_registration` | A registered correlation scheme. |
| Registry | `process_class_registration` | A registered class of process. |
| Registry | `residue_kind_registration` | A registered residue kind. |

**P6-3.11 (MUST) Entity coverage.** An implementation must be able to state, for every entity in the table above, where the information it carries is held, or that the entity is not applicable because the corresponding optional capability is not provided.

**P6-3.12 (MUST NOT) No update in place.** An implementation must not represent any state change specified by this part as a modification or deletion of a previously written event.

**P6-3.13 (MUST NOT) No state editing.** An implementation must not provide a means of setting the state of a process instance, the position of a flow token, the value of an instance value or the outcome of an activity instance other than by appending an event that a declared operation of section 4 produces.

**P6-3.14 (MUST) Administrative intervention is an event.** An implementation must record every administrative intervention in an instance as an appended event of a declared kind, with the actor, the authorisation and the reason, and must not permit an intervention that leaves no event.

### 3.4 Process definitions and versions

`process_definition_version` fields:

| Field | Type | Required | Cardinality | Absence means |
| --- | --- | --- | --- | --- |
| `definition_version_id` | `ID` | yes | 1 | n/a |
| `definition_id` | `ID` | yes | 1 | n/a |
| `process_class` | `ENUM` | yes | 1 | n/a. Registered under section 9.5. |
| `document_citation` | `CITEREF` | yes | 1 | n/a. The `Part 1` version carrying the definition. |
| `addressing_scheme` | `PIN` | yes | 1 | n/a |
| `start_positions` | `NODEREF` | yes | 1..n | n/a |
| `end_positions` | `NODEREF` | yes | 1..n | n/a. Explicit; see clause P6-3.18. |
| `termination_is_explicit` | `TRUTH` | yes | 1 | n/a. Must be true; see clause P6-3.18. |
| `stall_detection_interval` | `DURATION` | yes | 1 | n/a |
| `instance_bound` | `COUNT` | no | 0..1 | No bound on concurrent instances. Reportable. |
| `analysis_reference` | `PIN` | no | 0..n | No static analysis has been recorded for this version. |
| `created_ktime` | `KTIME` | yes | 1 | n/a |
| `authored_by` | `ACTOR` | yes | 1..n | n/a |

The `termination_is_explicit` field exists in order to be required to be true, and the requirement is a divergence from ordinary practice worth stating plainly.

BPMN and most engines permit implicit termination: a process instance ends when no tokens remain. That rule makes a completed instance and a deadlocked instance indistinguishable, because both have no runnable work. In an estate of any size the consequence is a population of instances that stopped for unknown reasons and are reported as finished. Requiring an explicit end position, and treating an instance with no runnable work that has not reached one as **stalled**, is what makes the distinction visible. Section 5.2 gives the state and clause P6-3.19 requires the detection.

**P6-3.15 (MUST) Definition carried by a document.** An implementation must record the `Part 1` citation of the document version that carries every process definition version and must not execute a definition that has none.

**P6-3.16 (MUST) Process class registered.** An implementation must record a registered process class on every definition version and must not default it.

**P6-3.17 (MUST) Addressing scheme pinned.** An implementation must pin the addressing scheme by which positions in the definition are named and must record it with every position reference.

**P6-3.18 (MUST) Explicit termination.** An implementation must require every definition version to declare at least one end position and must not treat the absence of runnable work as termination.

**P6-3.19 (MUST) Stall detection interval declared.** An implementation must declare, per definition version, the interval after which an instance with no runnable work that has not reached an end position is recorded as stalled, and must detect the condition within it.

**P6-3.20 (MUST NOT) No definition amendment.** An implementation must not alter a recorded definition version and must record every change as a new version.

**P6-3.21 (MUST) Instance bound reportable.** An implementation must be able to report every definition version with no declared bound on concurrent instances, since an unbounded process is the mechanism by which one upstream defect consumes an estate.
### 3.5 Activity definitions and compensability

`activity_definition` fields:

| Field | Type | Required | Cardinality | Absence means |
| --- | --- | --- | --- | --- |
| `activity_id` | `ID` | yes | 1 | n/a |
| `definition_version_id` | `ID` | yes | 1 | n/a |
| `position` | `NODEREF` | yes | 1 | n/a |
| `kind` | `ENUM` | yes | 1 | n/a. Registered under section 9.3, with the minimum set below. |
| `invokes` | `URN` | no | 0..1 | The activity performs no invocation. Required for every invoking kind. |
| `compensability` | `ENUM` | yes | 1 | n/a. One of `COMPENSABLE`, `IRREVERSIBLE`, `PARTIALLY_COMPENSABLE`, `COMPENSABILITY_UNDECLARED`. |
| `compensation_handler_id` | `ID` | no | 0..1 | Required where `compensability` is `COMPENSABLE` or `PARTIALLY_COMPENSABLE`. |
| `residue_kinds` | `ENUM` | no | 0..n | Required where `compensability` is `IRREVERSIBLE` or `PARTIALLY_COMPENSABLE`. |
| `idempotent` | `TRUTH` | yes | 1 | n/a. Whether repeating the invocation is safe. |
| `retry_policy` | `PIN` | no | 0..1 | No retry. Required where `idempotent` is not `TRUE` and retry is permitted. |
| `bound_declaration_id` | `ID` | no | 0..1 | Required for a multiple instance activity. |
| `timeout` | `DURATION` | no | 0..1 | No timeout. Reportable for every invoking kind. |

The minimum registered activity kinds:

| Kind | Means | Invokes |
| --- | --- | --- |
| `EVALUATE` | Obtain a `Part 2` evaluation. | `Part 2` |
| `DECIDE` | Obtain a `Part 5` decision. | `Part 5` |
| `RECORD` | Effect a recording operation in an owning component. | The owning component |
| `RESOLVE` | Obtain a resolution, such as a `Part 1` citation resolution or a `Part 4` definition. | The owning component |
| `HUMAN` | Require a person to do something. | `Part 8` |
| `INVOKE_MODEL` | Obtain a model output through `Part 13`. | `Part 13` |
| `EXTERNAL` | Invoke something outside the standard. | Declared |
| `SIGNAL` | Emit an event for another instance or component to correlate. | n/a |
| `WAIT` | Wait for a timer or an inbound event. | n/a |
| `COMPENSATE` | Request compensation of a scope or activity. | n/a |
| `SUBPROCESS` | Execute another definition version as a child instance. | This component |
| `NO_OP` | Occupy a position with no work. | n/a |

The `compensability` field is the field this section exists for, and `IRREVERSIBLE` is the member that matters. Almost every real process contains acts that cannot be undone: a payment has cleared, a notice has been posted, a submission has been filed with a regulator, a message has been delivered to a counterparty. Engines model compensation as though every activity has an inverse, and the ones that do not are simply omitted from the compensation handler, so a compensated scope is reported as compensated while the irreversible act inside it stands.

Requiring the declaration turns that into a static property. An `IRREVERSIBLE` activity inside a scope that has a compensation handler is a design condition that can be detected before the process runs, and clause P6-6.32 requires the detection. It is not necessarily a defect: a scope may legitimately contain an irreversible act whose residue is accepted. What is a defect is not knowing.

`COMPENSABILITY_UNDECLARED` is admissible and countable, on the same basis every prior part admits an honest undeclared value. A process definition every one of whose activities is undeclared has no compensation model, and the count is the only way anyone finds out.

**P6-3.22 (MUST) Kind registered.** An implementation must record a registered activity kind on every activity definition and must not default it.

**P6-3.23 (MUST) Compensability declared.** An implementation must record a compensability value on every activity definition and must not default it to compensable.

**P6-3.24 (MUST) Handler required where compensable.** An implementation must require a compensation handler on every activity declared `COMPENSABLE` or `PARTIALLY_COMPENSABLE` and must refuse a definition version lacking one.

**P6-3.25 (MUST) Residue kinds declared where not fully compensable.** An implementation must require at least one registered residue kind on every activity declared `IRREVERSIBLE` or `PARTIALLY_COMPENSABLE`.

**P6-3.26 (MUST) Idempotence declared.** An implementation must record whether repeating an activity's invocation is safe and must not retry an invocation of an activity whose idempotence is not `TRUE` except under a declared retry policy.

**P6-3.27 (MUST) Undeclared compensability countable.** An implementation must be able to report every activity of compensability `COMPENSABILITY_UNDECLARED` by definition version and must include the count in the signals of section 8.5.

**P6-3.28 (MUST) Timeout absence reportable.** An implementation must be able to report every invoking activity with no declared timeout, since an invocation with no timeout is the mechanism by which an instance stalls indefinitely.

**P6-3.29 (MUST NOT) No work in the activity definition.** An implementation must not hold the logic an activity performs, and must hold only the reference to what it invokes.

### 3.6 Control flow: splits and the join taxonomy

Control flow is where this part is most constrained by prior parts and where its own subject matter is densest.

**Splits.** Three kinds and the division is by whether topology determines the behaviour.

| Split kind | Behaviour | Determination required |
| --- | --- | --- |
| `PARALLEL_SPLIT` | Every outgoing flow proceeds. | None. Structural. |
| `EXCLUSIVE_SPLIT` | Exactly one outgoing flow proceeds. | Required. |
| `INCLUSIVE_SPLIT` | One or more outgoing flows proceed. | Required, per outgoing flow. |

The `EXCLUSIVE_SPLIT` carries a requirement that diverges from ordinary practice and follows directly from `Part 5`.

BPMN's exclusive gateway evaluates the conditions on its outgoing flows in a defined order and takes the first that is true. Where the conditions are not mutually exclusive, that is a selection among candidate branches by the order in which the branches are declared. `Part 5` clause P5-3.59 refuses exactly that: selection by the sequence of rules or rows, because a sequence is not a governed artifact and inserting a branch for readability changes the organisation's behaviour with no record that a policy changed.

This part therefore requires the conditions on an exclusive split to be **mutually exclusive**, which is an integrity constraint on the definition rather than a resolution rule, checkable statically. Where they are not mutually exclusive, the split is not an exclusive split: it is a selection among branches, and clause P6-3.33 requires it to be expressed as a `Part 5` decision whose outcome names the branch. That is more work and it produces a criterion somebody can approve.

A default flow, taken where no condition holds, is a default in `Part 5`'s sense and clause P6-3.34 requires it to be a declared artifact with an authority rather than a property of the diagram.

**Joins.** Six kinds. The table is normative and the set is closed.

| Join kind | Proceeds when | Unwaited branches | Semantics |
| --- | --- | --- | --- |
| `SYNCHRONISING_JOIN` | Every incoming flow has arrived. | None. | Local and total. |
| `SIMPLE_MERGE` | Any incoming flow arrives, and exactly one is expected. | n/a. Two arrivals is a defect. | Local. |
| `MULTI_MERGE` | Each incoming flow arrives, firing once per arrival. | None. | Local. Produces multiple downstream tokens. |
| `INCLUSIVE_JOIN` | Every incoming flow that will arrive has arrived. | None. | **Non local.** Restricted by section 3.7. |
| `PARTIAL_JOIN` | A declared number of incoming flows have arrived. | Declared disposition required. | Local. |
| `DISCRIMINATOR` | The first incoming flow arrives. | Declared disposition required. | Local. A partial join with a count of one. |

Three of the six require comment.

**`SIMPLE_MERGE` treats a second arrival as a defect rather than as a merge.** A merge that silently absorbs a second token has hidden a control flow error, and the downstream effect is that one activity ran once where the definition implied it would run once per arrival. The alternative behaviour is `MULTI_MERGE`, which fires per arrival and is explicit about doing so. Clause P6-3.36 requires the defect outcome.

**`PARTIAL_JOIN` and `DISCRIMINATOR` require a declared disposition for the branches they did not wait for**, and this is the requirement in this section most often absent from implementations. Those branches are still running. They will complete. They will have invoked things, recorded things and had effects, and the join has already proceeded. What becomes of them is a policy question with three answers and clause P6-3.37 requires one to be declared.

| Disposition | Means |
| --- | --- |
| `CANCEL_UNWAITED` | The unwaited branches are terminated. Their termination handlers run. Their completed work may require compensation. |
| `COMPLETE_AND_DISCARD` | They are allowed to complete and their outcomes are not consumed. The work is recorded and unused. |
| `COMPLETE_AND_RECORD_FOR_REVIEW` | They are allowed to complete, their outcomes are recorded, and a review obligation is raised. |

`COMPLETE_AND_DISCARD` is the behaviour most engines have by default and never state. Its consequence is that a process which asked three suppliers for a quote and proceeded on the first has two quotes it paid for and did not use, and no record connects them to the decision that ignored them. Recording the work is what clause P6-3.38 requires, and it is cheap.

**P6-3.30 (MUST) Closed split and join kind sets.** An implementation must record exactly one split kind and exactly one join kind from the tables above on every split and join and must not accept a kind outside the sets.

**P6-3.31 (MUST) Structural constructs require no determination.** An implementation must not require or accept a determination reference on a `PARALLEL_SPLIT`, a `SYNCHRONISING_JOIN`, a `SIMPLE_MERGE` or a `MULTI_MERGE`.

**P6-3.32 (MUST) Exclusive split conditions mutually exclusive.** An implementation must require the conditions on the outgoing flows of an `EXCLUSIVE_SPLIT` to be mutually exclusive, must verify the requirement by the analysis of section 6.7 where the form admits it, and must refuse a definition version in which they are not and the analysis established it.

**P6-3.33 (MUST) Non exclusive branch selection is a decision.** An implementation must express a split whose outgoing flows are not mutually exclusive and from which exactly one must proceed as an activity of kind `DECIDE` whose outcome names the branch, and must not select by branch order.

**P6-3.34 (MUST) Default flow is a declared artifact.** An implementation must record a default flow as a declared default with an authority under `Part 5` and must not treat it as a property of the definition's layout.

**P6-3.35 (MUST) Inclusive split determination per flow.** An implementation must record a separate determination reference for each outgoing flow of an `INCLUSIVE_SPLIT` and must not record one determination for the set.

**P6-3.36 (MUST) Second arrival at a simple merge is a defect.** An implementation must return the defect outcome of section 7.4 where a second flow arrives at a `SIMPLE_MERGE` within one instance and must not absorb it.

**P6-3.37 (MUST) Disposition declared on every partial join.** An implementation must require a declared disposition from the table above on every `PARTIAL_JOIN` and `DISCRIMINATOR` and must not default it.

**P6-3.38 (MUST) Unwaited work recorded.** An implementation must record the activity instances, invocation attempts and outcomes of every branch a join did not wait for, whether the disposition was to cancel, discard or review, and must be able to report them against the join resolution.

**P6-3.39 (MUST) Join resolution recorded.** An implementation must record, for every join, which incoming flows had arrived when it proceeded, which had not, and the disposition applied to those that had not.

**P6-3.40 (MUST) Discard obligation reportable.** An implementation must be able to report every join resolution of disposition `COMPLETE_AND_DISCARD` together with the work discarded, by definition version.

### 3.7 The inclusive join, and where it is admitted

The inclusive join is the one construct in this part whose semantics no standard has satisfactorily pinned down, and it is worth being explicit about why rather than adopting a behaviour and moving on.

An inclusive join must wait for every incoming flow that **will** arrive, and not for those that will not. Determining which flows will arrive requires knowing the future state of the execution. The BPMN specification's own account of the inclusive gateway requires global information about the state of the whole model, which the literature has repeatedly noted is a non local semantics that natural language description does not settle; multiple formalisations of it have been published and they do not agree in every case.

In the presence of arbitrary cycles the determination is not merely awkward. Whether a token can still reach a given incoming flow is a reachability question over the process graph, and reachability with cancellation is undecidable, per section 6.7. So an inclusive join in an unstructured cyclic process has no computable semantics at all, and every implementation that offers one has adopted an approximation.

This part therefore admits the inclusive join only where its semantics are decidable, and the condition is structural.

An inclusive join is **admissible** where the region between its matching inclusive split and itself is **block structured**: every flow leaving the split reaches the join, no flow enters the region other than through the split, no flow leaves the region other than through the join, and the region contains no cancellation region and no arbitrary cycle. Under those conditions the set of flows that will arrive is exactly the set the split activated, which the split recorded, so the join waits for a set it can read rather than a set it must predict.

An inclusive join is **inadmissible** otherwise, and clause P6-3.43 refuses the definition version. The remedy is one of three, and all three are more work and all three are explicit: use a synchronising join and have the split activate every flow with a declared no operation on the flows that would not have been taken; use a partial join with a declared count and disposition; or make the convergence a decision.

This is a restriction on expressiveness and it will be resisted. The justification is that the alternative is a construct whose behaviour differs between engines, cannot be statically analysed, and cannot be explained to the operator of section 1.4 who is asking why an instance is waiting. Section 13.3 records the cost and the argument against.

**P6-3.41 (MUST) Structured region required.** An implementation must admit an `INCLUSIVE_JOIN` only where the region between its matching `INCLUSIVE_SPLIT` and itself satisfies every condition of this section, and must record the verification.

**P6-3.42 (MUST) Activated flow set recorded at the split.** An implementation must record, at every `INCLUSIVE_SPLIT`, the exact set of outgoing flows it activated, and must satisfy the matching join against that recorded set rather than by predicting arrivals.

**P6-3.43 (MUST NOT) No inclusive join outside a structured region.** An implementation must refuse a definition version containing an `INCLUSIVE_JOIN` whose region is not block structured, contains a cancellation region, or contains an arbitrary cycle, and must state which condition failed.

**P6-3.44 (MUST) Matching split identified.** An implementation must record the matching `INCLUSIVE_SPLIT` of every `INCLUSIVE_JOIN` and must refuse a join for which no matching split can be identified.

**P6-3.45 (MUST NOT) No approximation.** An implementation must not implement an `INCLUSIVE_JOIN` by a timeout, a heuristic, an iteration limit or an assumption about which flows will arrive.

### 3.8 Loops, cycles and multiple instances

Three forms of repetition and each needs a bound.

**`REPETITION`.** A structured loop with a declared entry, a declared exit and a declared bound. The exit condition is a determination, per section 3.13, so a loop does not terminate because this component evaluated something.

**`ARBITRARY_CYCLE`.** A cycle in the control flow that is not a structured repetition: a flow returning to an earlier position without a single entry and exit. Admitted, because real processes contain them and refusing them pushes the work into a subprocess with worse visibility, and admitted only with a declared bound on traversals of the cycle's back edge and a declared exit.

**`MULTIPLE_INSTANCE`.** An activity executed once per member of a collection, with or without synchronisation.

`bound_declaration` fields carry a `kind` of `ITERATION_COUNT`, `INSTANCE_COUNT`, `ELAPSED_LOGICAL_TIME` or `DECLARED_RESOURCE`, the bound value, an `authority`, a `justification`, and an `on_exhaustion` of `TERMINATE_WITH_OUTCOME`, `EXIT_LOOP_AND_CONTINUE` or `RAISE_FAULT`.

The instance count of a multiple instance activity requires a recorded provenance, and the enumeration matters because the three cases have different risks.

| Provenance | Means | Risk |
| --- | --- | --- |
| `DESIGN_TIME_CONSTANT` | The count is fixed in the definition. | None. |
| `RUNTIME_VALUE_PINNED` | The count is read from a pinned collection whose version is recorded. | Bounded by the pin. |
| `RUNTIME_DYNAMIC` | Instances are created as members arrive, with no count known in advance. | Unbounded unless a bound is declared. |

`RUNTIME_DYNAMIC` without a declared bound is the single most effective mechanism available for one upstream defect to consume an estate: a collection that should contain three members contains three hundred thousand, and the engine faithfully creates three hundred thousand activity instances, each invoking something. Clause P6-3.49 refuses it.

Repetition and compensation interact in a way that is easy to get wrong. Compensating a scope that contains a completed repetition requires compensating each completed iteration, and the order is the reverse of the order of completion of the iterations. The alternative behaviour, compensating the loop body once, is what an implementation does if nobody specifies otherwise, and it leaves the effects of every iteration but the last standing. Clause P6-3.51 requires per iteration compensation and clause P6-3.52 requires the order.

**P6-3.46 (MUST) Bound declared on every repetition.** An implementation must require a declared bound on every `REPETITION`, `ARBITRARY_CYCLE` and `MULTIPLE_INSTANCE` activity and must refuse a definition version lacking one.

**P6-3.47 (MUST) Bound authorised and justified.** An implementation must record an authority and a justification for every declared bound, since a bound is a limit on what the organisation will do and the number is policy.

**P6-3.48 (MUST) Instance count provenance recorded.** An implementation must record the provenance of every multiple instance activity's instance count from the enumeration above.

**P6-3.49 (MUST NOT) No unbounded dynamic instantiation.** An implementation must refuse a multiple instance activity of provenance `RUNTIME_DYNAMIC` with no declared instance count bound.

**P6-3.50 (MUST) Exhaustion behaviour declared.** An implementation must record what happens when each bound is exhausted and must return the corresponding outcome of section 7.3 rather than a failure.

**P6-3.51 (MUST) Per iteration compensation.** An implementation must compensate each completed iteration of a repetition and each completed instance of a multiple instance activity separately, and must not compensate the body once.

**P6-3.52 (MUST) Iteration compensation order.** An implementation must compensate completed iterations in the reverse of their order of completion unless a different order is declared and justified, per section 3.9.

**P6-3.53 (MUST) Arbitrary cycles identified.** An implementation must identify and record every arbitrary cycle in a definition version, must record its declared bound and exit, and must include the count of definitions containing one in the signals of section 8.5.

**P6-3.54 (MUST) Synchronisation declared on multiple instances.** An implementation must record whether a multiple instance activity synchronises on completion of every instance, and where it does not must record the disposition of unsynchronised instances per section 3.6.
### 3.9 Scopes, handlers and compensation order

A scope is a nested region to which handlers attach and is the unit of compensation. The model follows WS-BPEL 2.0, which attaches compensation, fault, termination and event handlers to scopes, and diverges from it in three places that section 10.3 names.

`scope_definition` fields carry the enclosing scope, the positions it spans, and the identities of its handlers. `handler_definition` fields carry a `handler_kind` of `COMPENSATION`, `FAULT`, `TERMINATION` or `EVENT`, the fault or event it catches where applicable, the activities it performs, and an `authority` where the handler embodies a policy rather than a mechanism.

Four rules of the model are adopted from WS-BPEL and stated as clauses because each is subtle and each is commonly implemented differently.

**Compensation is available only for a scope that completed successfully.** A scope whose fault handler ran did not complete successfully, and compensation is therefore not enabled for it. WS-BPEL states this and the reasoning is sound: a scope whose fault handler ran has already had a declared response, and compensating it as well would perform two responses to one fault. Clause P6-3.57 adopts it.

**Default compensation order is the reverse of the order of completion.** WS-BPEL makes this the default for the compensation of enclosed scopes. Clause P6-3.58 adopts it as the default and requires any other order to be declared and justified.

**Compensation may be initiated only from a handler.** WS-BPEL permits its compensate activities only within a fault handler, a compensation handler or a termination handler, so compensation is reachable only from an error path. This part **diverges**: a business initiated reversal, where nothing failed and somebody has decided to undo, is a real and common case, and BPEL's own scope statement contemplates a partner requesting reversal. Clause P6-3.59 admits an activity of kind `COMPENSATE` in normal flow, on condition that the request records the determination that authorised it. Section 10.5 records the divergence.

**A compensation handler sees the state as at the completion of its scope.** WS-BPEL's snapshot semantics. This part adopts it and states the consequence: a compensation performed years after the scope completed compensates against what was true then, and where the world has since changed the compensation may be wrong. Clause P6-3.61 requires the elapsed interval to be recorded so that a stale compensation is visible.

The compensation order question is the one where the reviewed standard is known to be defective, and the defect is worth naming rather than inheriting. The literature has established that WS-BPEL's default order can violate control dependencies where control links cross scope boundaries, and the specification's own issue resolution settled on the weaker rule that the default order need only respect explicitly modelled control dependencies. So there are two accounts in circulation, reverse order of completion and dependency respecting order, and they differ exactly in the cases that matter.

This part requires the order to be one of three declared kinds and requires the declaration, so that no implementation has to guess.

| Order kind | Means |
| --- | --- |
| `REVERSE_COMPLETION` | Reverse of the order in which the scopes completed. The default. |
| `REVERSE_DEPENDENCY` | Reverse of the declared control dependencies among the scopes, which may differ from completion order where scopes completed concurrently. |
| `DECLARED_SEQUENCE` | An explicitly declared sequence, with a justification. |

**P6-3.55 (MUST) Handlers attached to scopes.** An implementation must attach every compensation, fault, termination and event handler to a declared scope and must not attach one to a position that is not a scope.

**P6-3.56 (MUST) Handler authority where it embodies policy.** An implementation must record an authority for every handler whose action is a policy rather than a mechanism, including every handler that performs a business act.

**P6-3.57 (MUST NOT) No compensation of a faulted scope.** An implementation must not enable compensation for a scope whose fault handler was invoked, and must record the reason where a compensation request names such a scope.

**P6-3.58 (MUST) Compensation order declared.** An implementation must record a compensation order kind from the table above for every scope with enclosed compensable scopes, must default it to `REVERSE_COMPLETION`, and must require a justification for any other kind.

**P6-3.59 (MAY) Compensation from normal flow.** An implementation may admit an activity of kind `COMPENSATE` in normal flow, and where it does must require the request to record the determination that authorised it.

**P6-3.60 (MUST) Concurrent completion order recorded.** An implementation must record, where two scopes completed concurrently within the precision of its clock, that their relative order of completion is not established, and must not impose one.

**P6-3.61 (MUST) Elapsed interval recorded on compensation.** An implementation must record the interval between the completion of a scope and the performance of its compensation, and must be able to report every compensation performed beyond a declared staleness threshold.

**P6-3.62 (MUST NOT) No compensation of a compensation.** An implementation must not compensate a compensation handler's own effects and must record the residue of a failed compensation per section 3.10.

**P6-3.63 (MUST) Compensation is not rollback.** An implementation must not represent a compensation as a restoration of prior state, and must record it as the performance of the declared compensating acts and their outcomes.

### 3.10 Compensation outcomes and residue

This section is the part's principal contribution and it exists because no reviewed standard admits that a compensation might not work.

WS-BPEL specifies when compensation handlers run and in what order. It does not specify what it means for a compensation to have failed to restore the position, because in its model a compensation handler either completes or faults, and a fault is handled by the enclosing scope. The distinction between a compensation that completed and a compensation that restored the position is not expressible.

That distinction is the whole of the practical difficulty. A compensating act can complete perfectly and restore nothing: the reversal transaction was submitted and the counterparty rejected it; the correction notice was sent and the original had already been acted upon; the record was updated and the report built from it had already been filed. In each case the compensation handler completed successfully and the effect stands.

`compensation_outcome` is therefore a closed set of six members. The table is normative.

| Member | Means | Residue |
| --- | --- | --- |
| `COMPENSATED_FULLY` | Every declared compensating act completed and the position is asserted restored. | None. |
| `COMPENSATED_PARTIALLY` | Some acts completed and some effect stands. | Required, enumerated. |
| `COMPENSATION_IMPOSSIBLE` | The activity was declared irreversible, or the compensating act cannot be performed in the present state. | Required, enumerated. |
| `COMPENSATION_FAILED` | A compensating act was attempted and did not complete. | Required, enumerated, and the position is unknown rather than unchanged. |
| `COMPENSATION_NOT_ATTEMPTED` | Compensation was requested and not performed, because a bound was exhausted, an authorisation was refused, or the request was superseded. | Required where the scope had effects. |
| `NO_COMPENSATION_DEFINED` | The scope or activity has no compensation handler. | Required, being the whole effect. |

Two members carry the weight.

**`COMPENSATION_FAILED` leaves the position unknown, not unchanged.** This is the state everybody models worst. A compensating act that was attempted and did not complete may have partially succeeded, may have succeeded and failed to report, or may have done nothing. The record must say that the position is unknown, and clause P6-3.67 forbids recording it as though the effect stands unaltered, because acting on that assumption is how a double reversal happens.

**`COMPENSATED_FULLY` is an assertion, not a finding.** This component performed the declared acts and they completed. Whether the position is in fact restored is a question about the world that this component cannot answer, and clause P6-3.68 requires the member to be recorded as an assertion attributable to the declaration of the compensation handler rather than as an established fact.

`residue` fields carry the `compensation_outcome_id`, a registered `residue_kind`, a `description`, an `extent` where quantifiable, a `reversible_later` truth value, and the `observed_ktime`. The minimum registered residue kinds:

| Kind | Means |
| --- | --- |
| `VALUE_TRANSFERRED` | Money or another fungible value moved and has not returned. |
| `COMMUNICATION_SENT` | A communication reached a recipient and cannot be unsent. |
| `EXTERNAL_FILING` | Something was filed with an external body and stands on their record. |
| `THIRD_PARTY_RELIANCE` | A third party has acted on the effect. |
| `TIME_ELAPSED` | A period passed that cannot be recovered, such as a missed deadline. |
| `PHYSICAL_ACT` | Something was physically done or moved. |
| `DATA_DISCLOSED` | Information reached a party who should not have had it. |
| `RESIDUE_UNCLASSIFIED` | The residue is known and its kind is not. |

`residue_assignment` records the owner to whom a residue was assigned, the assignment act, the actor and the authorisation. A residue with no assigned owner is a consequence nobody is answerable for, and clause P6-3.70 requires the count to be a standing signal.

**P6-3.64 (MUST) Closed outcome set.** An implementation must record exactly one member of the compensation outcome table above for every compensation performed or declined and must not accept a value outside the set.

**P6-3.65 (MUST) Residue enumerated where required.** An implementation must enumerate the residue for every outcome the table above requires it for and must refuse to record such an outcome without at least one residue record.

**P6-3.66 (MUST) Residue kind registered.** An implementation must record a registered residue kind on every residue and must permit `RESIDUE_UNCLASSIFIED` where the kind is not known.

**P6-3.67 (MUST) Failed compensation leaves the position unknown.** An implementation must record a `COMPENSATION_FAILED` outcome as leaving the position unknown, must not record it as leaving the effect unaltered, and must raise the review obligation of section 7.5.

**P6-3.68 (MUST) Full compensation is an assertion.** An implementation must record `COMPENSATED_FULLY` as an assertion attributable to the compensation handler's declaration and must not represent it as an established restoration of the position.

**P6-3.69 (MUST) Residue assigned.** An implementation must record an assignment of every residue to an owner, with the assigning actor and the authorisation, or must record that no assignment has been made.

**P6-3.70 (MUST) Unassigned residue countable.** An implementation must be able to report every residue with no recorded assignment, by kind and by definition version, and must include the count in the signals of section 8.5.

**P6-3.71 (MUST) Compensation recorded as a determination.** An implementation must record every compensation execution as an act with `Part 3`, citing the determination that authorised it where one exists and the residue it produced, and must not record it only as a process event.

**P6-3.72 (MUST NOT) No compensation outcome inference.** An implementation must not infer a compensation outcome from the completion of the handler's activities, and must require the outcome to be reported by the component that performed the compensating act or asserted by a named actor.

### 3.11 Events, timers and correlation

A process waits. It waits for a timer, for an inbound message, for a signal from another instance, or for a person. Waiting is where a process spends nearly all of its existence and where nearly all of its operational trouble lives.

`timer_observation` fields carry the `activity_instance_id`, the `declared_duration` or `declared_instant`, the `observed_otime` at which the elapse was observed, the `observed_ktime` at which it was recorded, the `clock_source`, and a `lateness` where the observation was later than the declared instant.

The requirement that matters is that **an observed time is a recorded fact and not a re evaluation of a clock**. A process that computes whether a deadline has passed by reading the clock during replay will replay differently on every replay, so the timer's firing must be an appended event that the replay reads. This component is the one component in the standard that must observe real elapsed time, and clause P6-3.74 states the discipline that makes the observation reproducible: observe once, record, and thereafter read the record.

The `lateness` field exists because timers fire late. An engine under load fires a deadline timer hours after the deadline, and the process behaves as though the deadline had just passed. Recording the lateness makes the difference between a deadline that expired and a deadline whose expiry was noticed visible, and clause P6-3.75 requires it.

`correlation_binding` records a correlation key, the scheme it is drawn from, the instance it identifies, and when it was bound. Three requirements follow and each addresses a specific failure.

**A correlation key must be bound before the event that uses it can arrive**, or the arrival is unmatched. An unmatched inbound event is not an error to be discarded: it is a message that arrived for an instance that is not ready or does not exist, and discarding it loses work. Clause P6-3.77 requires unmatched events to be recorded and reportable.

**A correlation key must identify at most one instance.** Two instances bound to one key is a defect that produces a message delivered to an arbitrary one of them, and clause P6-3.78 refuses the second binding.

**A correlation key is not a business identifier**, or if it is, it is a reference to one rather than a copy. A correlation key holding a claim number is holding a business fact, and section 3.12 governs it.

**P6-3.73 (MUST) Timer declared as a duration or an instant.** An implementation must record whether a timer is declared as an elapsed duration or an absolute instant and must not convert one to the other without recording both.

**P6-3.74 (MUST) Observed time recorded, not recomputed.** An implementation must record the observation of every timer elapse as an appended event and must read the recorded observation on every replay rather than evaluating a clock.

**P6-3.75 (MUST) Lateness recorded.** An implementation must record the interval between a timer's declared instant and the instant its elapse was observed, and must be able to report every observation beyond a declared lateness threshold.

**P6-3.76 (MUST) Clock source recorded.** An implementation must record the source of the clock from which every observation was made.

**P6-3.77 (MUST) Unmatched events recorded.** An implementation must record every inbound event it could not correlate to an instance, with the key it carried and the reason, must retain it for a declared period, and must be able to report the population.

**P6-3.78 (MUST NOT) No ambiguous correlation.** An implementation must refuse to bind a correlation key already bound to a live instance and must record the refusal with both instances.

**P6-3.79 (MUST) Correlation scheme registered.** An implementation must record a registered correlation scheme with every key and must not rely on a single implicit scheme.

**P6-3.80 (MUST NOT) No business identifier as a stored key.** An implementation must record a correlation key derived from a business identifier as a reference to the owning component's identifier rather than as a copy of a business value, per section 3.12.

### 3.12 Instance values and the prohibition on business data

This section is the cheap enforcement of the spine, and its whole content is a closed set.

An `instance_value` is one value held by a process instance. Every value is of exactly one kind from the set below, and no kind admits a business fact. The table is normative and the set is closed.

| Kind | Means | Example |
| --- | --- | --- |
| `REFERENCE` | An identifier by which an owning component's fact can be obtained. | A document lineage identifier, a subject reference. |
| `PIN` | An identity and version of a depended upon artifact. | The evaluation report version consumed at a gateway. |
| `DETERMINATION_REFERENCE` | A reference to a `Part 2` report or `Part 5` decision. | The report that attributed a branch. |
| `CONTROL_COUNTER` | A count of executions the engine itself performed. | Iterations completed, retries attempted. |
| `CONTROL_FLAG` | A boolean derived solely from recorded engine events. | Whether a scope completed, whether a bound was exhausted. |
| `CORRELATION_KEY` | A key by which inbound events are matched. | As constrained by clause P6-3.80. |
| `POSITION` | A position in the definition. | The activity a compensation targets. |
| `INSTANT` | An observed or declared time. | A timer's declared instant, an observation. |
| `AUTHORISATION_REFERENCE` | A `Part 7` decision reference. | The authorisation that permitted a cancellation. |
| `OPAQUE_TRANSIT` | A value the engine received and must pass on unread, whose content it does not interpret. | A signed token being carried between two activities. |

`OPAQUE_TRANSIT` is the member that will be abused and it is included because the alternative is worse. Real processes carry values between activities that the engine must not read and cannot avoid holding: a signed assertion, an encrypted payload, an opaque continuation. Admitting the kind and constraining it is better than pretending it does not occur. The constraints in clause P6-3.84 are that the value must be declared opaque, must not be read by any condition, gateway, correlation or handler, must carry a declared maximum lifetime, and must be separately countable, because a rising volume of opaque transit is the accretion of section 1.3 wearing a disguise.

**P6-3.81 (MUST) Closed value kind set.** An implementation must record exactly one kind from the table above on every instance value and must not hold a value of no such kind.

**P6-3.82 (MUST NOT) No business fact as a value.** An implementation must not hold a value that is a copy of a fact whose authoritative owner is another component, in any kind, and must hold a `REFERENCE` instead.

**P6-3.83 (MUST) Control flags derived from engine events.** An implementation must derive every `CONTROL_FLAG` from its own recorded events and must not accept one as an input or set one from an external value.

**P6-3.84 (MUST) Opaque transit constrained.** An implementation must not read, evaluate, correlate on or route by an `OPAQUE_TRANSIT` value, must record a declared maximum lifetime for it, and must be able to report the count and volume of opaque transit values by definition version.

**P6-3.85 (MUST NOT) No value beyond the instance.** An implementation must not expose an instance value to any consumer other than the activities of the instance holding it and the reading operations of section 4.5, and must not permit a report to be built over instance values.

**P6-3.86 (MUST) Value kind checked at recording.** An implementation must check the kind of every value at the moment it is recorded and must refuse a value whose kind is not declared or whose content is inconsistent with its declared kind so far as the kind admits a check.

### 3.13 Branch attribution

Every conditional branch must be attributable to something outside this component. This section states what and how.

`branch_attribution` fields:

| Field | Type | Required | Cardinality | Absence means |
| --- | --- | --- | --- | --- |
| `attribution_id` | `ID` | yes | 1 | n/a |
| `instance_id` | `ID` | yes | 1 | n/a |
| `split_position` | `NODEREF` | yes | 1 | n/a |
| `flow_taken` | `NODEREF` | yes | 1..n | n/a. More than one for an inclusive split. |
| `flows_not_taken` | `NODEREF` | yes | 0..n | Every outgoing flow was taken. |
| `determination` | `DETREF` | yes | 1..n | n/a. One per flow whose activation depended on a determination. |
| `determination_kind` | `ENUM` | yes | 1..n | n/a. `EVALUATION_REPORT`, `DECISION`, `STRUCTURAL` or `DEFAULT`. |
| `obtained_ktime` | `KTIME` | yes | 1 | n/a |
| `indeterminate_handling` | `ENUM` | no | 0..1 | Required where a determination was indeterminate; see below. |

The `indeterminate_handling` field is where this part meets the third value for the first time and it is the hardest requirement in the section.

`Part 2` may return an indeterminate verdict for the condition on a flow, and `Part 5` may return one of four undecidable outcomes for a branch decision. Both parts go to considerable lengths to ensure the third value reaches the caller intact, and this component is the caller. It must do something with a branch whose condition could not be established.

Four things are possible and the enumeration is closed.

| Handling | Means |
| --- | --- |
| `SUSPEND_AND_REFER` | The instance suspends at the split and a referral is raised. The default. |
| `TAKE_DECLARED_BRANCH` | A declared branch is taken, with an authority and a justification recorded on the definition. |
| `TAKE_NO_BRANCH_AND_STALL` | No flow is activated; the instance records the condition and stalls, per section 5.2. |
| `RAISE_FAULT` | A fault is raised in the enclosing scope. |

`SUSPEND_AND_REFER` is the default, per clause P6-3.89, on the same basis `Part 5` clause P5-3.30 makes declining to decide the default for an indeterminate eligibility. `TAKE_DECLARED_BRANCH` is admissible and requires an authority, because taking a branch on an unestablished condition is a policy act.

`Part 5` clause P5-12.21 requires an undecidable outcome to be recorded as an outcome before any referral is raised. Clause P6-3.91 is the reciprocal: this component must not raise the referral until it has confirmed that the outcome was recorded, so that the organisation has a count of undecidable decisions rather than a queue of referrals.

**P6-3.87 (MUST) Attribution on every conditional branch.** An implementation must record a branch attribution for every activation of a flow from an `EXCLUSIVE_SPLIT` or an `INCLUSIVE_SPLIT` and must refuse to activate one without it.

**P6-3.88 (MUST) Flows not taken recorded.** An implementation must record which outgoing flows were not activated, so that a path is explicable by what was excluded as well as by what was taken.

**P6-3.89 (MUST) Suspend and refer is the default.** An implementation must suspend the instance and raise a referral where a determination for a branch is indeterminate and the definition declares no handling.

**P6-3.90 (MUST) Declared handling authorised.** An implementation must require an authority and a justification on every declaration of `TAKE_DECLARED_BRANCH` and must record on every affected instance that the branch was taken on an unestablished condition.

**P6-3.91 (MUST) Outcome recorded before referral.** An implementation must confirm that an indeterminate verdict or undecidable decision was recorded by its owning component before raising a referral, and must record the confirmation, per clause P5-12.21.

**P6-3.92 (MUST NOT) No branch on a vacuous satisfaction unmarked.** An implementation must record where a branch was activated on a `Part 2` satisfaction marked vacuous and must be able to report the population.

**P6-3.93 (MUST NOT) No structural attribution for a conditional split.** An implementation must not record a determination kind of `STRUCTURAL` for a flow from a conditional split.
### 3.14 The process instance and its event log

`process_instance` fields:

| Field | Type | Required | Cardinality | Absence means |
| --- | --- | --- | --- | --- |
| `instance_id` | `ID` | yes | 1 | n/a |
| `definition_version_id` | `ID` | yes | 1 | n/a. Pinned; see section 3.16. |
| `parent_instance_id` | `ID` | no | 0..1 | The instance is not a child of a subprocess activity. |
| `started_ktime` | `KTIME` | yes | 1 | n/a |
| `started_by` | `ACTOR` | yes | 1 | n/a |
| `start_authorisation` | `AUTHREF` | no | 0..1 | Starting the instance was not the subject of an authorisation decision. |
| `subject_reference` | `URN` | no | 0..n | The instance concerns no identified subject. |
| `last_event_sequence` | `SEQ` | yes | 1 | n/a. Derived. |
| `terminated_ktime` | `KTIME` | no | 0..1 | The instance has not terminated. |

`instance_event` is the only entity in this part whose grain is prescribed exactly, because everything else is derived from it. Fields: `event_id`, `instance_id`, `sequence`, `event_kind`, the position or entity it concerns, the payload restricted to instance values of the kinds in section 3.12, the `actor` where an actor caused it, the `authorisation` where one applied, and the `recorded_ktime`.

**Every state is derived.** The set of activity instances and their states, the multiset of flow tokens and their positions, the set of open scopes, the values held, the bindings, and the instance's own state, are all projections of the event log. Nothing is stored as mutable state and clause P6-3.96 states the requirement.

The reason is the reason every prior part gives for the same discipline, and one more that is specific here. A workflow engine's state is the single most tempting thing in an estate to edit, because editing it is the fastest way to release a stuck instance and because the edit is invisible ten minutes later. An estate in which instance states have been edited has an execution record that is not an account of what happened, and the edits are precisely concentrated in the instances an investigation will ask about. Clause P6-3.13 forbids the edit and clause P6-3.14 requires an intervention to be an event, so that an unsticking is a recorded act rather than a silent correction.

**P6-3.94 (MUST) Event log is append only and totally ordered.** An implementation must assign a contiguous sequence to every event within an instance and must never reuse or reassign a sequence value.

**P6-3.95 (MUST) Payload restricted to declared value kinds.** An implementation must restrict the payload of every event to instance values of the kinds in section 3.12.

**P6-3.96 (MUST) State derived from the log.** An implementation must compute the state of every instance, including every activity instance state, token position, open scope and held value, as a function of its event log alone.

**P6-3.97 (MUST) State recomputable and agreement demonstrable.** An implementation must be able to recompute the state of any instance from its log and to demonstrate agreement between a served state and a recomputation.

**P6-3.98 (MUST) Gaps detected.** An implementation must detect any gap in an instance's event sequence, must record the observation, and must treat the instance's state as unestablished until the gap is resolved.

**P6-3.99 (MUST) Parent and child linked in both directions.** An implementation must record the parent instance on every child instance and must be able to enumerate the children of any instance.

**P6-3.100 (MUST NOT) No cross instance state.** An implementation must not hold state shared between instances other than the correlation bindings of section 3.11, and must not permit one instance to read another's values.

### 3.15 Activity instances and invocation attempts

The separation of these two entities is the requirement of this section and it is absent from most implementations.

An `activity_instance` is the execution of an activity: created, started, and reaching one outcome. An `invocation_attempt` is one attempt to invoke what the activity names, and there may be several. Merging them makes a retried invocation invisible, which matters for three reasons: a non idempotent activity invoked three times may have had three effects; the latency an activity took includes the retries and reporting only the last understates it; and an activity that succeeded on the fourth attempt is a different operational fact from one that succeeded on the first.

`invocation_attempt` fields carry the `activity_instance_id`, the `attempt_ordinal`, the `idempotence_key` supplied, the `invoked_target`, the `started_ktime`, the `completed_ktime`, the `attempt_outcome`, and the `response_reference` by which the invoked component's own record can be obtained.

The idempotence key is derived from the activity instance identity and the attempt is not part of it, so every attempt of one activity instance carries the same key. That is what makes the receiving component able to deduplicate, and it is the only mechanism by which repeated delivery is made safe. Clause P6-3.103 requires it.

**At least once is the achievable semantics.** An engine that invokes something across a boundary and records the outcome cannot guarantee that the invocation happened exactly once, because the failure between the invocation and the recording of its outcome is indistinguishable from the failure before the invocation. What is achievable is at least once delivery with an idempotence key, and an implementation claiming exactly once semantics has made a claim it cannot keep. Clause P6-3.105 forbids the claim.

**P6-3.101 (MUST) Attempts recorded separately.** An implementation must record every invocation attempt as its own entity and must not record only the attempt that produced the activity's outcome.

**P6-3.102 (MUST) Attempt outcome per attempt.** An implementation must record the outcome of every attempt, including attempts whose outcome was unknown because no response was received.

**P6-3.103 (MUST) Idempotence key per activity instance.** An implementation must derive the idempotence key it supplies from the activity instance identity, must supply the same key on every attempt of one activity instance, and must record the key.

**P6-3.104 (MUST) Response recorded by reference.** An implementation must record the reference by which the invoked component's own record of the invocation can be obtained and must not record the invoked component's result as its own content, per clause P6-1.2.

**P6-3.105 (MUST NOT) No exactly once claim.** An implementation must not represent its invocation semantics as exactly once and must declare the semantics it provides and the deduplication the receiver is required to perform.

**P6-3.106 (MUST) Unknown outcome distinguished from failure.** An implementation must record an attempt for which no response was received as having an unknown outcome, must not record it as a failure, and must not retry a non idempotent activity on an unknown outcome without a declared policy.

**P6-3.107 (MUST) Retry count reportable.** An implementation must be able to report the distribution of attempts per activity instance by activity definition, since a rising retry rate is a dependency failing rather than a process changing.

### 3.16 Version pinning and migration

A process instance may live for years and its definition will change under it. This is the hardest operational problem in workflow and it is where every implementation cheats.

**The rule is that an instance is pinned.** It runs, for its whole life, under the definition version it started with. Clause P6-3.108 states it. The consequence is that an organisation with long lived instances is running several definition versions concurrently, which is correct and which is unpopular, because it means a defect corrected in version four is still present in the instances running under version three.

**Migration is admitted only under a declared mapping.** A `migration_mapping` is a governed artifact under `Part 1` mapping positions in a source definition version to positions in a target version, with a declared treatment for every position in the source that has no target, every scope whose handlers differ, every open activity instance, and every held value. It carries an authority, a justification and an approval, exactly as a criterion does in `Part 5`.

`migration_mapping` fields carry the source and target version identities, a `position_mapping` of source to target for every position that may be occupied, a `disposition` for every unmapped source position from `TERMINATE_INSTANCE`, `MOVE_TO_DECLARED_POSITION`, `COMPENSATE_AND_TERMINATE` or `SUSPEND_FOR_REFERRAL`, a `value_mapping`, a `soundness_assessment`, an `authority`, a `justification` and an `approval_citation`.

Three requirements make the mapping honest.

**Every occupiable position must be mapped or dispositioned.** A mapping that covers the positions the author expected instances to be at, and leaves the rest, will encounter an instance at an unexpected position, and the engine's behaviour is then undefined at exactly the moment least amenable to investigation. Clause P6-3.110 requires exhaustive coverage.

**The mapping must be assessed for soundness.** A migration can move a token into a position from which the target definition cannot complete, producing an instance that is stalled by construction. The soundness analysis of section 6.7 applies to the post migration state and clause P6-3.111 requires it.

**Every migrated instance records the mapping.** So that the instance's history is readable as two segments under two definitions with a recorded join between them, rather than as a single history under a definition that half of it never ran. Clause P6-3.112 requires it and clause P6-3.113 forbids rewriting the earlier events into the target's vocabulary.

**P6-3.108 (MUST) Instance pinned to its start version.** An implementation must execute every instance under the definition version recorded at its start and must not apply a later version to a running instance except by a recorded migration.

**P6-3.109 (MUST) Migration only under a governed mapping.** An implementation must migrate a running instance only under a migration mapping that is a `Part 1` document version with an authority, a justification and a resolved approval.

**P6-3.110 (MUST) Mapping exhaustive over occupiable positions.** An implementation must require a migration mapping to map or disposition every position a running instance may occupy in the source version and must refuse a mapping that does not.

**P6-3.111 (MUST) Post migration soundness assessed.** An implementation must assess, and record, whether the migrated state can reach proper completion in the target version, and must refuse a migration whose assessment established that it cannot.

**P6-3.112 (MUST) Migration recorded on the instance.** An implementation must record the migration as an event on the instance, with the mapping identity, the source and target versions, the position before and after, and the disposition applied.

**P6-3.113 (MUST NOT) No rewriting of earlier events.** An implementation must not alter, reinterpret or renumber the events recorded before a migration, and must retain them addressed in the source version's addressing scheme.

**P6-3.114 (MUST) Migrated instances reportable.** An implementation must be able to report every migrated instance by mapping and by source and target version, and must include the count in the signals of section 8.5.

**P6-3.115 (MUST NOT) No silent migration.** An implementation must not migrate an instance as a side effect of deploying a definition version, and must require every migration to be a recorded, authorised operation.

### 3.17 Projections

Every read is a projection: a pure function of the recorded events, holding no state of its own, recomputable at any time.

| Projection | Yields |
| --- | --- |
| `instance_state` | The derived state of an instance: activity instances and their states, token positions, open scopes, held values, bindings. |
| `instance_history` | The event log in sequence order, with gaps marked. |
| `path_of` | The ordered sequence of activity instances an instance executed, with each conditional branch's attribution. |
| `waiting_on` | For every non terminal instance, precisely what it is waiting for, and whether anything will cause it to proceed. |
| `stalled_instances` | Every instance with no runnable work that has not reached an end position, by definition version and position. |
| `join_resolutions` | Every join resolution, with arrived and unarrived branches and the disposition applied. |
| `discarded_work` | Activity instances performed on branches a join did not wait for, by definition version. |
| `bound_exhaustions` | Every bound exhausted, by kind and definition version. |
| `attempt_distribution` | Invocation attempts per activity instance, by activity definition. |
| `unknown_outcome_attempts` | Attempts for which no response was received. |
| `compensation_outcomes` | Compensations by outcome member, by scope and definition version. |
| `residues` | Every residue with its kind, extent and assignment, and those unassigned. |
| `stale_compensations` | Compensations performed beyond the declared staleness threshold. |
| `indeterminate_branches` | Branches where a determination was indeterminate, with the handling applied. |
| `unmatched_events` | Inbound events that could not be correlated, with their keys. |
| `timer_lateness` | Timer observations beyond the declared lateness threshold. |
| `instance_values_by_kind` | Held values by kind and definition version, including opaque transit volume. |
| `disposal_exceptions` | Values that failed the disposal demonstration of clause P6-3.9. |
| `version_population` | Running instances by pinned definition version, and their ages. |
| `migrations` | Migrated instances by mapping, with the disposition applied. |
| `definition_analysis_state` | Static analysis results per definition version, with those not analysed and why. |
| `replay_divergence` | Where replay of a recorded instance from its log yields a different derived state. |

`waiting_on` is the projection the operator of section 1.4 needs and the one most implementations do not have. Its requirement is not merely to say that an instance is at a wait activity but to say what would release it: a timer at a stated instant, an inbound event on a stated correlation key, a human task with a stated identity in `Part 8`, an invocation attempt in flight, or nothing, which is the stall.

`version_population` is the projection that makes the pinning of section 3.16 governable. An organisation that cannot see how many instances are running under a definition version from two years ago cannot decide whether to migrate them, and will discover the population when the version is withdrawn.

**P6-3.116 (MUST) Projections are pure.** An implementation must compute every projection as a function of recorded events alone, holding no state not derivable from them.

**P6-3.117 (MUST) Projection recomputable.** An implementation must be able to recompute every projection from the recorded events and to demonstrate agreement between a served projection and a recomputation.

**P6-3.118 (MUST) Named projections available.** An implementation must provide every projection in the table above and must name each as named there in any interface it exposes.

**P6-3.119 (MUST) Waiting on states what would release.** An implementation must return, for every non terminal instance, what would cause it to proceed, and must return that nothing would where that is the case.

**P6-3.120 (MUST) Version population available.** An implementation must provide `version_population` and must report the age distribution of running instances per pinned definition version.

**P6-3.121 (MUST NOT) No writes through a projection.** An implementation must not permit any state change to be effected by writing to a projection.

### 3.18 Worked demonstration

The demonstration follows one process across five years. It is not normative. It exists because the field tables do not show whether the model catches the failures it was built for.

**2027, the definition.** Process definition `P`, version `PV1`, governs the settlement of a claim. Its class is registered, its document citation resolves, termination is explicit with two end positions, and its stall detection interval is four hours.

The flow: an `EVALUATE` activity obtains a `Part 2` eligibility report; an `EXCLUSIVE_SPLIT` whose two conditions are mutually exclusive and verified so by analysis; on the eligible branch a scope `S1` containing three activities, being a `RECORD` reserving funds, an `EXTERNAL` activity instructing a payment, and a `RECORD` closing the claim; on the ineligible branch a `HUMAN` activity and an end position.

Compensability is declared. The reservation is `COMPENSABLE`, with a handler that releases the reservation. **The payment instruction is `IRREVERSIBLE`, with residue kind `VALUE_TRANSFERRED`.** The closure is `COMPENSABLE`. Scope `S1` has a compensation handler with order `REVERSE_COMPLETION`.

The static analysis records: sound, exclusive split conditions mutually exclusive, no arbitrary cycle, no cancellation region, and **one condition flagged: an `IRREVERSIBLE` activity within a scope that has a compensation handler.** That is not a refusal. It is the finding that the scope cannot be fully compensated once the payment has been instructed, and it is recorded on the definition version so that nobody discovers it during an incident.

**2028, an ordinary instance.** Instance `I1` starts. The evaluation returns a report; the branch attribution records the report by pin and the determination kind `EVALUATION_REPORT`. The eligible branch is taken, the flow not taken is recorded. `S1` runs. The reservation records; the payment instruction is invoked; the closure records. The instance reaches an end position and terminates explicitly.

The instance holds four values: a `REFERENCE` to the claim, a `PIN` to the evaluation report, a `DETERMINATION_REFERENCE`, and a `CONTROL_COUNTER` of zero retries. It holds no claim amount, no claimant name and no approval flag. The disposal demonstration passes.

**2029, the failure that compensation cannot fix.** Instance `I2` reaches the closure activity, which faults: the claim record is under a legal hold and cannot be closed. `S1`'s fault handler runs and requests compensation of the completed activities.

Compensation proceeds in reverse order of completion. The payment instruction is compensated first. Its compensability is `IRREVERSIBLE`.

| Scope element | Compensation outcome | Residue |
| --- | --- | --- |
| Payment instruction | `COMPENSATION_IMPOSSIBLE` | `VALUE_TRANSFERRED`, extent recorded, `reversible_later` true |
| Fund reservation | `COMPENSATED_FULLY` | None |
| Scope `S1` overall | `COMPENSATED_PARTIALLY` | One residue, unassigned at first |

The scope's outcome is `COMPENSATED_PARTIALLY`, not `COMPENSATED_FULLY`, and that single distinction is what the section exists for. An engine without the taxonomy records that the compensation handler completed, which it did, and the payment stands with nothing pointing at it.

The residue is unassigned for eleven days and appears in the unassigned residue signal throughout. It is then assigned to a recoveries function with an authorisation, and the assignment is a recorded act.

**2030, the timer that fired late.** A `WAIT` activity with a fourteen day deadline. The engine is under load and observes the elapse thirty one hours after the declared instant. The observation records the declared instant, the observed instant, the lateness of thirty one hours and the clock source. The instance proceeds as though the deadline had passed, which it had, and the lateness projection shows that the organisation learned of it a day and a half late. On replay, the recorded observation is read and the replay is identical.

**2031, the definition change and the population nobody had counted.** Version `PV2` corrects a defect and inserts an activity inside `S1`. The `version_population` projection reports 214 instances still running under `PV1`, the oldest 700 days old.

A migration mapping is authored. It maps every occupiable `PV1` position to a `PV2` position except one: instances waiting at the `HUMAN` activity on the ineligible branch, which `PV2` restructured. Their disposition is declared `SUSPEND_FOR_REFERRAL`. The post migration soundness assessment passes for the mapped positions. The mapping is approved and executed; each migrated instance records the mapping, the positions before and after, and the disposition. The nineteen instances at the human activity are suspended and referred rather than moved, and nobody has to guess what happened to them.

**2032, the question.** An investigation asks the following.

| Question | Projection | Result |
| --- | --- | --- |
| What ran in `I2`, in what order? | `path_of` | The ordered activity instances, with the branch attribution and the report by pin |
| Why did it take the eligible branch? | `path_of` | The `Part 2` evaluation report, cited, obtainable |
| Did the compensation work? | `compensation_outcomes` | Partially. The payment could not be reversed. |
| Who owns the money that moved? | `residues` | Assigned to recoveries on day eleven, with the authorisation. Unassigned for eleven days before that. |
| Was the deadline missed or noticed late? | `timer_lateness` | Both. Declared instant, observed instant, thirty one hours. |
| Which definition version did it run under? | `version_population`, `migrations` | `PV1` throughout; `I2` terminated before the migration. |
| Would deleting every instance lose anything? | `disposal_exceptions` | No exceptions in this definition. Four value kinds, all references, pins and counters. |
| Was the definition ever known to be uncompensable? | `definition_analysis_state` | Yes, from 2027. The irreversible activity in a compensable scope was recorded at design time. |

The last two rows are the ones the part exists for. The seventh establishes that the process instances are not a shadow system of record. The eighth establishes that the organisation knew, four years before the incident, that this scope could not be fully undone.

**P6-3.122 (MUST) Demonstration satisfiable.** An implementation must be able to answer every question in the table above for any instance within its retained history, using only the projections of section 3.17.
## 4. Interfaces

### 4.1 Interface principles

Operations are specified by their obligations rather than their signatures. No transport, encoding or naming convention is specified.

Operations divide into four groups: those that record definitions, those that drive instances, those that intervene in instances, and those that read. The intervening group is separated from the driving group because an intervention is an administrative act with an authorisation and a reason, and merging the two makes an unsticking indistinguishable from a normal advance.

**P6-4.1 (MUST) Operation classes separated.** An implementation must not provide an operation that both records a definition version and drives an instance.

**P6-4.2 (MUST) Refusal is an outcome.** An implementation must return a refusal outcome of section 7.6 for any operation it declines and must not return an outcome of another class in its place.

**P6-4.3 (MUST) Idempotence key accepted.** An implementation must accept a caller supplied idempotence key on every recording, driving and intervening operation and must honour it per section 6.6.

**P6-4.4 (MUST) Every operation appends an event.** An implementation must record the effect of every driving and intervening operation as one or more appended events and must not effect a change by any other means.

### 4.2 Recording operations

| # | Operation | Records | Principal refusals |
| --- | --- | --- | --- |
| 1 | Register a process definition | `process_definition` | Duplicate identity; unregistered class |
| 2 | Record a definition version | `process_definition_version`, activities, flows, splits, joins, scopes, handlers, bounds | No document citation; no end position; termination not explicit; an activity with no compensability; a compensable activity with no handler; an irreversible activity with no residue kind; a repetition, cycle or multiple instance activity with no bound; an unbounded dynamic instantiation; an inclusive join outside a structured region; a conditional split whose conditions the analysis established are not mutually exclusive; a partial join with no disposition; no stall detection interval |
| 3 | Record a definition analysis | `definition_analysis` | Analysis referencing a different version |
| 4 | Record a migration mapping | `migration_mapping` | Occupiable positions unmapped and undispositioned; no post migration soundness assessment; no authority |
| 5 | Withdraw a definition version from starting | withdrawal | Running instances exist and no disposition is declared |
| 6 | Register an activity kind | registration | Duplicate key; no invocation target semantics |
| 7 | Register an addressing scheme | registration | No stability declaration |
| 8 | Register a correlation scheme | registration | No uniqueness semantics |
| 9 | Register a process class | registration | Duplicate key; no owning component |
| 10 | Register a residue kind | registration | Duplicate key; no assignment expectation |

Operation 2's refusal list is the design in compressed form and two of its refusals will be resisted.

The refusal of an inclusive join outside a structured region, per clause P6-3.43, removes a construct modellers use freely. Section 13.3 records the cost.

The refusal of an activity with no declared compensability requires somebody to say, for every activity in every process, whether it can be undone. That is a substantial authoring burden and it is the burden the whole of section 3.10 depends on. The escape is `COMPENSABILITY_UNDECLARED`, which is admissible and countable, so the requirement is not that every activity be classified correctly but that an unclassified one be visible as one.

Operation 5 is worth noting. Withdrawing a definition version from starting new instances is not the same as retiring it, because instances are pinned and will continue running under it for as long as they live. An implementation that treats withdrawal as deletion orphans a population, and clause P6-4.9 requires the population to be reported and a disposition declared.

**P6-4.5 (MUST) Preconditions checked at recording.** An implementation must check every precondition in the table above at the moment of recording, must record the outcome of each check, and must not defer a check to execution.

**P6-4.6 (MUST) Whole definition version in one operation.** An implementation must accept the whole structure of a definition version in a single operation and must record it atomically.

**P6-4.7 (MUST) Analysis performed before starting.** An implementation must perform the analyses of section 6.7 that the definition's form admits before permitting an instance to start under it, and must record the results including those that could not be performed.

**P6-4.8 (MUST NOT) No execution of an unanalysed definition where analysable.** An implementation must refuse to start an instance under a definition version whose form admits the soundness analysis and for which the analysis was not performed.

**P6-4.9 (MUST) Withdrawal reports its population.** An implementation must report every running instance pinned to a definition version at the moment the version is withdrawn from starting, and must require a declared disposition for the population.

**P6-4.10 (MUST) Refused versions retained.** An implementation must retain every refused definition version with its per check outcomes and must be able to report refusals by author and by failed precondition.

### 4.3 Driving operations

| # | Operation | Records | Principal refusals |
| --- | --- | --- | --- |
| 11 | Start an instance | `process_instance`, start events, pins | Definition version withdrawn from starting; instance bound exceeded; not authorised; correlation key already bound |
| 12 | Advance an instance | events for the activities and flows that became runnable | Instance terminated; a required determination absent; a pin unobtainable |
| 13 | Record an activity outcome | activity instance and attempt events | Activity instance unknown or already terminal |
| 14 | Deliver a correlated event | correlation and instance events | Key unbound; key ambiguous; instance terminated |
| 15 | Observe a timer elapse | `timer_observation` and instance events | Timer unknown; already observed |
| 16 | Request compensation | `compensation_request` | Scope not completed successfully; compensation requested from normal flow with no determination |
| 17 | Record a compensation outcome | `compensation_execution`, `compensation_outcome`, `residue` | Outcome requiring residue with none supplied; outcome inferred rather than reported |
| 18 | Assign a residue | `residue_assignment` | No authorisation; no owner |
| 19 | Complete an instance | terminal events | No end position reached |

Operation 12 is where the execution algorithm of section 6.2 runs, and its most important refusal is the third: a determination absent. The engine does not proceed past a conditional split without the report or decision that attributes the branch. It suspends and refers, per clause P6-3.89, or applies the declared handling.

Operation 17 is where clause P6-3.72 bites. The engine does not infer that a compensation succeeded from the completion of the handler's activities. The outcome is reported by the component that performed the compensating act, or asserted by a named actor, and an implementation that cannot obtain either records `COMPENSATION_NOT_ATTEMPTED` or leaves the outcome unrecorded rather than assuming.

**P6-4.11 (MUST) Start pins the version.** An implementation must record the definition version pin at the start of every instance and must not resolve the version again during the instance's life.

**P6-4.12 (MUST) Advance is driven by events, not by polling state.** An implementation must determine what became runnable from the appended events and must not compute runnability from a stored state it also maintains.

**P6-4.13 (MUST) Determination required before a conditional advance.** An implementation must refuse to activate a flow from a conditional split without the determination reference the attribution requires.

**P6-4.14 (MUST) Compensation outcome reported, not inferred.** An implementation must obtain every compensation outcome from the component that performed the compensating act or from a named actor's assertion, per clause P6-3.72.

**P6-4.15 (MUST) Residue supplied with the outcome.** An implementation must refuse to record a compensation outcome that requires residue without at least one residue record.

**P6-4.16 (MUST) Completion requires an end position.** An implementation must refuse to record an instance as completed where no end position has been reached, and must record it as stalled instead.

**P6-4.17 (MUST NOT) No advance past an unresolved wait.** An implementation must not advance an instance past a `WAIT` activity other than by a recorded timer observation, a correlated event or an intervention.

### 4.4 Intervening operations

| # | Operation | Records | Requires |
| --- | --- | --- | --- |
| 20 | Suspend an instance | suspension event | Authorisation, reason |
| 21 | Resume an instance | resumption event | Authorisation, reason |
| 22 | Cancel an instance | cancellation events, compensation requests where declared | Authorisation, reason, declared compensation treatment |
| 23 | Retry an activity instance | a further invocation attempt | Authorisation where the activity is not idempotent, reason |
| 24 | Move a flow token | intervention event with source and target positions | Authorisation, reason, and a recorded soundness assessment of the resulting state |
| 25 | Force an activity outcome | intervention event recording the forced outcome and the actual one where known | Authorisation, reason, and marking of the outcome as forced |
| 26 | Migrate an instance | `migration_execution` and events | An approved mapping, authorisation |
| 27 | Terminate an instance without completion | termination events, handlers | Authorisation, reason, declared handler treatment |

Operations 24 and 25 are the operations every engine provides and no engine records properly. Moving a token and forcing an outcome are how a stuck instance is released, they are performed under pressure, and they are the acts an investigation most needs to see.

Three requirements make them honest. Each is an event, per clause P6-3.14. Each requires an authorisation and a reason, per clause P6-4.19. And a forced outcome is **marked as forced for the life of the record**, per clause P6-4.21, so that an activity whose outcome was supplied by an operator under pressure is never read as an activity that completed.

Operation 24 additionally requires a soundness assessment of the state it produces, because moving a token to an arbitrary position is the most reliable way to produce an instance that can never complete.

**P6-4.18 (MUST) Interventions enumerated.** An implementation must provide no intervening operation beyond those in the table above and must register any additional operation as an extension under section 9.9.

**P6-4.19 (MUST) Authorisation and reason on every intervention.** An implementation must record an `AUTHREF` and a reason on every intervening operation and must refuse one lacking either.

**P6-4.20 (MUST) Token move assessed.** An implementation must record a soundness assessment of the state a token move produces and must refuse a move whose assessment established that the instance cannot then complete.

**P6-4.21 (MUST) Forced outcomes marked permanently.** An implementation must mark an activity outcome supplied by an intervention as forced, must record the actual outcome where it is known, must not permit the marking to be removed, and must carry the marking into every projection and export.

**P6-4.22 (MUST) Cancellation treatment declared.** An implementation must require a declared treatment of completed compensable scopes on every cancellation and must not cancel an instance leaving completed effects with no recorded decision about them.

**P6-4.23 (MUST) Interventions countable by operator.** An implementation must be able to report interventions by operator, by kind and by definition version, and must include the counts in the signals of section 8.5.

### 4.5 Reading operations

| # | Operation | Returns |
| --- | --- | --- |
| 28 | Read a named projection | The projection of section 3.17 |
| 29 | Get an instance | The instance with its derived state and its event log |
| 30 | Get an instance path | The ordered activity instances with branch attributions |
| 31 | Replay an instance | The state derived by replay, and a divergence record where it differs |
| 32 | Get a definition version | The whole structure with its analysis results |
| 33 | Export an evidence package | The package of section 8.6 |

**P6-4.24 (MUST) Replay available.** An implementation must provide operation 31 and must be able to replay any instance within its retained history from its event log.

**P6-4.25 (MUST) Replay divergence recorded.** An implementation must record every divergence between a served state and a replayed state as a finding about the record and must not amend either.

**P6-4.26 (MUST NOT) No partial instance record.** An implementation must return a complete event log from operation 29 or refuse, and must not return a subset without stating what was omitted and why.

**P6-4.27 (MUST) Forced and intervened events distinguishable in every read.** An implementation must return, with every instance and every path, which events were interventions and which outcomes were forced.

### 4.6 What a caller may and may not assume

**P6-4.28 (MUST) Caller obligations declared.** An implementation must document, for every operation, which of the assumptions below the caller may make.

A caller may assume that every conditional branch is attributable to a recorded determination, that every activity's invocation attempts are recorded, that the derived state is a function of the event log, that an instance recorded as completed reached an end position, and that a compensation outcome was reported rather than inferred.

A caller may not assume that an instance recorded as running is making progress, since it may be stalled and the stall interval may not have elapsed. A caller may not assume that a scope recorded as compensated was fully compensated, since the outcome member distinguishes the cases. A caller may not assume that an activity that completed was invoked once, since attempts are recorded separately. A caller may not assume that an activity outcome was produced by the invoked component, since it may have been forced by an intervention and the marking says so. A caller may not assume that an instance is running under the current definition version, since instances are pinned. And a caller may not assume that any business fact is available from this component, since clause P6-1.2 forbids it holding one.

**P6-4.29 (MUST NOT) No implied progress.** An implementation must not describe an instance as running, in progress or active without stating what it is waiting for and whether anything would release it.

**P6-4.30 (MUST NOT) No implied restoration.** An implementation must not describe a scope as compensated, reversed or unwound without the compensation outcome member and any residue.

### 4.7 Reads from other components

| Read | From | On unavailability |
| --- | --- | --- |
| Resolve a definition or mapping document version | `Part 1` | Refuse the start or the migration; do not refuse an advance of a running instance, whose version is pinned |
| Obtain an evaluation report | `Part 2` | Suspend the instance at the split; do not guess the branch |
| Register a step as a trail act | `Part 3` | Record the failure and retry; do not lose the event |
| Resolve a concept or definition | `Part 4` | Refuse the activity; do not proceed on an unresolved meaning |
| Obtain a decision | `Part 5` | Suspend the instance at the split |
| Obtain an authorisation decision | `Part 7` | Refuse the operation |
| Create or read a human task | `Part 8` | Suspend the activity and record the unavailability; do not complete the activity |
| Obtain a model output | `Part 13` | Refuse the activity |

The pattern differs from every prior part in one respect worth noting. A running instance whose definition version cannot be resolved **continues**, because the version is pinned and the definition was read at start; the resolution is needed to start a new instance, not to advance an existing one. That is a direct consequence of section 3.16 and it is the property that makes long lived instances survivable.

**P6-4.31 (MUST) Declared unavailability behaviour.** An implementation must implement the unavailability behaviour of the table above for every read and must record which behaviour it took.

**P6-4.32 (MUST NOT) No substitution on unavailability.** An implementation must not substitute a cached, default, current or successor version of any artifact in the table above, and must not proceed on an assumed determination.

**P6-4.33 (MUST) Pinned definition survives resolution failure.** An implementation must continue to advance a running instance under its pinned definition version where the carrying document version cannot be resolved, and must record the resolution failure.

**P6-4.34 (MUST) Ledger recording failure does not lose the event.** An implementation must retain its own event where registering a step as a `Part 3` trail act failed, must record the failure, and must be able to report every event not yet registered.

### 4.8 Events emitted

The envelope carries at minimum an event identity, a type from the registered set, the knowledge time assigned by this component, the instance and position concerned, the actor, a correlation reference, a schema reference and a digest over the event body.

The minimum event set. An implementation may emit more.

Definition version recorded. Definition version refused. Definition analysis recorded. Definition analysis not performed. Definition version withdrawn from starting. Migration mapping recorded. Instance started. Instance completed. Instance terminated without completion. Instance suspended. Instance resumed. Instance cancelled. Instance stalled. Activity instance created. Activity instance completed. Activity instance faulted. Invocation attempted. Invocation outcome unknown. Invocation retried. Branch attributed. Branch determination indeterminate. Branch taken on an unestablished condition. Join resolved. Join proceeded without every branch. Unwaited branch cancelled. Unwaited work discarded. Simple merge second arrival. Bound exhausted. Multiple instance count from a dynamic source. Timer observed. Timer observed late. Event unmatched. Correlation key ambiguous. Scope completed. Scope faulted. Fault handler invoked. Termination handler invoked. Compensation requested. Compensation outcome recorded. Compensation partial. Compensation impossible. Compensation failed. Residue recorded. Residue assigned. Residue unassigned beyond an age. Instance value of an undeclared kind refused. Disposal demonstration performed. Disposal exception found. Intervention performed. Outcome forced. Token moved. Instance migrated. Replay diverged. Evidence package exported.

Five of these are the operationally decisive ones and are the least likely to exist in an implementation that has not read this part.

**Instance stalled** must be emitted per instance, because it is the event that distinguishes a stopped instance from a finished one and nothing else produces it.

**Compensation partial**, **compensation impossible** and **compensation failed** must each be emitted distinctly, because the three have different owners and the aggregate is meaningless.

**Outcome forced** must be emitted per occurrence, because a forced outcome is an operator's assertion standing in for a component's result and every consumer downstream is treating it as the latter.

**P6-4.35 (MUST) Minimum event set.** An implementation must emit an event for every member of the set above and must register any additional type under section 9.9.

**P6-4.36 (MUST) Envelope minimum.** An implementation must include every envelope element named above in every event it emits.

**P6-4.37 (MUST NOT) No event in place of a record.** An implementation must not rely on event emission to satisfy any recording obligation of section 3 or section 8.

**P6-4.38 (MUST) Stall emitted per instance.** An implementation must emit a distinct event for every instance entering the stalled state and must not emit stalls only as counts.

**P6-4.39 (MUST) Compensation members emitted distinctly.** An implementation must emit a distinct event for each of partial, impossible and failed compensation.

**P6-4.40 (MUST NOT) No suppression of adverse events.** An implementation must not provide a configuration that suppresses the emission of a refusal, a stall, a bound exhaustion, a discarded work record, an indeterminate branch, an unmatched event, a late timer, a compensation that was not full, an unassigned residue, an intervention, a forced outcome, a migration or a replay divergence.
## 5. State model

### 5.1 Four state models, and the one this component genuinely owns

This part specifies four state machines. Unlike the five prior parts, one of them is genuinely this component's own business, and the distinction is worth stating because it is the only place in the standard where a component owns a lifecycle over something no other component holds.

The **process instance state** is this component's own. No other part holds it, no other part may require it, and every prior part has required its own state to be independent of it.

The **activity instance state** is also this component's own, with one exception: where the activity is of kind `HUMAN`, the work item's own lifecycle belongs to `Part 8` and this component holds only the activity's state in the flow. Section 12.8 draws the line.

The **scope state** governs when compensation becomes available and when it ceases to be.

The **compensation state** governs the progress of a compensation and terminates in one of the six outcomes of section 3.10.

All four are projections of the event log, per clause P6-3.96. None is stored.

**P6-5.1 (MUST) Four models separate.** An implementation must not represent instance state, activity instance state, scope state and compensation state in one field and must not derive any of them from a stored value.

**P6-5.2 (MUST) States are projections.** An implementation must compute every state in this section from the instance's event log alone.

**P6-5.3 (MUST NOT) No state required of another component.** An implementation must not require any other component to hold, read or reason about a state specified in this section.

### 5.2 Process instance state

States:

`RUNNING`. At least one flow token exists at a position from which work is runnable or a wait is outstanding.

`WAITING`. Every token is at a wait: a timer, an inbound event, a human activity or an invocation in flight. Distinguished from `RUNNING` because the operator's question is different, and distinguished from `STALLED` because something will release it.

`SUSPENDED`. An intervention suspended the instance. No token advances. The suspension carries an authorisation and a reason.

`STALLED`. No token is at a runnable position, no wait is outstanding, and no end position has been reached. **Nothing will release it.**

`COMPENSATING`. A compensation is in progress at the instance level.

`COMPLETED`. An end position was reached and every token is accounted for.

`TERMINATED`. The instance ended without reaching an end position, by cancellation or by forced termination, with handlers run as declared.

`MIGRATED_OUT`. The instance was migrated and continues under the target version as the same instance; recorded so that the pinned version change is a state fact and not only an event.

Transitions:

| From | To | Trigger | Requires |
| --- | --- | --- | --- |
| start | `RUNNING` | Instance started | Definition version pinned, authorisation |
| `RUNNING` | `WAITING` | Every token reached a wait | The wait recorded with what would release it |
| `WAITING` | `RUNNING` | A timer observed, an event correlated, a human activity completed, an invocation returned | The releasing event appended |
| `RUNNING`, `WAITING` | `STALLED` | No runnable work, no outstanding wait, no end position, stall interval elapsed | Detection recorded |
| `STALLED` | `RUNNING` | An intervention | Authorisation, reason, soundness assessment where a token was moved |
| `RUNNING`, `WAITING`, `STALLED` | `SUSPENDED` | Suspension | Authorisation, reason |
| `SUSPENDED` | `RUNNING`, `WAITING` | Resumption | Authorisation, reason |
| `RUNNING` | `COMPENSATING` | Instance level compensation requested | The determination or the fault that requested it |
| `COMPENSATING` | `TERMINATED` | Compensation reached an outcome | Every compensation outcome recorded |
| `RUNNING` | `COMPLETED` | An end position reached and tokens accounted for | Explicit end |
| any non terminal | `TERMINATED` | Cancellation or forced termination | Authorisation, reason, handler treatment |
| any non terminal | `MIGRATED_OUT` | Migration executed | Approved mapping, authorisation |

`STALLED` is the state this section exists for and it is absent from BPMN and from most engines, because both permit implicit termination: an instance with no tokens is finished. Under that rule an instance that deadlocked, an instance whose only token was consumed by a defect, and an instance that ran to completion are the same state, and the first two are reported as the third.

Making the stall a state has three consequences and all three are wanted. It is detectable, within a declared interval per clause P6-3.19. It is countable, per section 8.5. And it is a legitimate terminal condition to be reported rather than an error to be retried, so the population of stalled instances is a governance measure of a process definition's fitness rather than an operational backlog.

There is no transition from `COMPLETED` or `TERMINATED` back to any other state. An instance that must run again is a new instance, because reviving a terminated instance makes the gap in its history indistinguishable from continuity, on the same basis `Part 4` clause P4-5.14 refuses concept revival.

**P6-5.4 (MUST) Enumerated states only.** An implementation must represent the state of every instance as exactly one member of the set above.

**P6-5.5 (MUST) Enumerated transitions only.** An implementation must not effect a transition absent from the table above.

**P6-5.6 (MUST) Waiting distinguished from running.** An implementation must record `WAITING` where every token is at a wait and must record what would release each wait, per clause P6-3.119.

**P6-5.7 (MUST) Stall detected and recorded.** An implementation must transition an instance to `STALLED` within the declared interval where it has no runnable work, no outstanding wait and no end position reached, and must not record it as completed.

**P6-5.8 (MUST NOT) No implicit termination.** An implementation must not transition an instance to `COMPLETED` on the exhaustion of its tokens and must require an end position.

**P6-5.9 (MUST) Stall exit is an intervention.** An implementation must treat every exit from `STALLED` as an intervention requiring an authorisation, a reason and, where a token was moved, a soundness assessment.

**P6-5.10 (MUST) Terminal states are terminal.** An implementation must not transition out of `COMPLETED` or `TERMINATED` and must record a repeated execution as a new instance.

**P6-5.11 (MUST) Suspension does not advance.** An implementation must not advance any token, observe any timer or correlate any event into an instance in `SUSPENDED`, and must record every inbound event arriving during suspension as pending or unmatched.

**P6-5.12 (MUST) Migration recorded as a state fact.** An implementation must record `MIGRATED_OUT` as a state of the instance under its source version and must retain the source version's events unaltered, per clause P6-3.113.

### 5.3 Activity instance state

States: `CREATED`, `READY`, `RUNNING`, `WAITING_ON_INVOCATION`, `WAITING_ON_HUMAN`, `WAITING_ON_EVENT`, `COMPLETED`, `FAULTED`, `CANCELLED`, `OUTCOME_UNKNOWN`, `OUTCOME_FORCED`, `SKIPPED`.

Four of these require comment.

`OUTCOME_UNKNOWN` is the state of an activity whose invocation was attempted and for which no response was received. It is neither completed nor faulted, and the distinction is load bearing: the invoked component may have performed the work. Clause P6-5.15 forbids resolving it to either without evidence, and clause P6-3.106 forbids retrying a non idempotent activity from it without a declared policy.

`OUTCOME_FORCED` is the state of an activity whose outcome was supplied by an intervention. It is permanent, per clause P6-4.21, and it is not `COMPLETED`, because the invoked component did not report completion.

`SKIPPED` is the state of an activity on a branch that was not taken, or within a multiple instance activity whose bound was exhausted before the instance was created. It is recorded rather than absent, because a reader tracing a path needs to see the activities that were reachable and not executed.

`CANCELLED` is the state of an activity terminated by a cancellation region, a join disposition of `CANCEL_UNWAITED`, or an instance cancellation. A cancelled activity that had begun may have had effects, and clause P6-5.17 requires the effects to be recorded and the compensation question to be raised.

**P6-5.13 (MUST) Enumerated activity states.** An implementation must represent every activity instance state as exactly one member of the set above.

**P6-5.14 (MUST) Waiting states distinguished by what is awaited.** An implementation must distinguish waiting on an invocation, on a human activity and on an event, since the three have different owners and different releases.

**P6-5.15 (MUST NOT) No resolution of an unknown outcome.** An implementation must not transition an activity from `OUTCOME_UNKNOWN` to `COMPLETED` or `FAULTED` without a recorded response from the invoked component or a recorded intervention, and must record which.

**P6-5.16 (MUST) Forced outcome is its own state.** An implementation must represent an outcome supplied by an intervention as `OUTCOME_FORCED` and must not represent it as `COMPLETED`.

**P6-5.17 (MUST) Cancelled activity effects recorded.** An implementation must record, for every activity cancelled after it began, the invocation attempts it had made and their outcomes, and must record whether compensation was requested.

**P6-5.18 (MUST) Skipped activities recorded.** An implementation must record an activity on an untaken branch as `SKIPPED` rather than omitting it, so that a path is readable as what was and was not executed.

**P6-5.19 (MUST NOT) No human work item state.** An implementation must not hold the offering, allocation, delegation or escalation state of a human activity's work item, and must hold only the activity's state in the flow, per section 12.8.

### 5.4 Scope state

States: `OPEN`, `COMPLETED_SUCCESSFULLY`, `FAULTED`, `FAULT_HANDLED`, `TERMINATED`, `COMPENSATION_ENABLED`, `COMPENSATING`, `COMPENSATED`, `COMPENSATION_UNAVAILABLE`.

The transitions that matter are the two that govern whether compensation is available.

A scope that reaches `COMPLETED_SUCCESSFULLY` transitions to `COMPENSATION_ENABLED`, and its compensation handler may be invoked thereafter for as long as the enclosing scope has not itself completed and been discarded.

A scope that faults and whose fault handler runs reaches `FAULT_HANDLED` and transitions to `COMPENSATION_UNAVAILABLE`, per clause P6-3.57 and following WS-BPEL. The reasoning is that the scope has already had a declared response to its failure, and compensating it as well performs two responses to one event.

`COMPENSATION_UNAVAILABLE` is a state rather than an absence, so that a compensation request naming such a scope is refused with a reason rather than silently doing nothing. Clause P6-5.22 requires the refusal to be recorded.

**P6-5.20 (MUST) Enumerated scope states.** An implementation must represent every scope instance state as exactly one member of the set above.

**P6-5.21 (MUST) Compensation enabled only on successful completion.** An implementation must transition a scope to `COMPENSATION_ENABLED` only from `COMPLETED_SUCCESSFULLY`.

**P6-5.22 (MUST) Unavailability recorded and refusals reasoned.** An implementation must record `COMPENSATION_UNAVAILABLE` for a scope whose fault handler was invoked and must refuse a compensation request naming it with the reason recorded.

**P6-5.23 (MUST) Compensation availability window declared.** An implementation must declare the period for which a completed scope's compensation remains available and must record the expiry as a state transition rather than as an absence.

**P6-5.24 (MUST NOT) No re enabling.** An implementation must not transition a scope from `COMPENSATED` or `COMPENSATION_UNAVAILABLE` to `COMPENSATION_ENABLED`.

### 5.5 Compensation state

States: `REQUESTED`, `AUTHORISED`, `EXECUTING`, `OUTCOME_RECORDED`, `DECLINED`, `ABANDONED`.

The machine is short because the interesting content is the outcome rather than the progress. `OUTCOME_RECORDED` is terminal and carries one of the six members of section 3.10, and the residue records hang off it.

`DECLINED` is the state of a compensation request refused: because the scope's compensation is unavailable, because a bound was exhausted, because an authorisation was refused, or because the request was superseded by a later one. It maps onto the outcome `COMPENSATION_NOT_ATTEMPTED` and clause P6-5.27 requires the reason.

`ABANDONED` exists for the same reason it exists in `Part 2` and `Part 3`: a compensation whose executing process is lost leaves rows behind, and the alternative to a state for it is a compensation that appears to be in progress indefinitely. An abandoned compensation is materially worse than an abandoned evaluation, because the compensating acts may have partially completed, so clause P6-5.28 requires the outcome to be recorded as `COMPENSATION_FAILED` with the position unknown rather than left open.

**P6-5.25 (MUST) Enumerated compensation states.** An implementation must represent every compensation as exactly one member of the set above.

**P6-5.26 (MUST) Outcome recorded on termination.** An implementation must record one of the six outcome members of section 3.10 on every compensation reaching a terminal state.

**P6-5.27 (MUST) Decline reasoned.** An implementation must record the reason for every `DECLINED` compensation and must map it to the outcome `COMPENSATION_NOT_ATTEMPTED`.

**P6-5.28 (MUST) Abandoned compensation leaves the position unknown.** An implementation must record an abandoned compensation as outcome `COMPENSATION_FAILED` with the position unknown, must enumerate the residue as unclassified where it cannot be determined, and must raise the review obligation of section 7.5.

**P6-5.29 (MUST) Abandonment detected within a declared interval.** An implementation must detect a compensation whose executing process is lost within a declared interval and must declare the interval.

**P6-5.30 (MUST NOT) No compensation reopening.** An implementation must not transition out of `OUTCOME_RECORDED` and must record a further attempt as a new compensation request citing the earlier one.
## 6. Execution semantics

### 6.1 Determinism, replay and the one non deterministic input

Two properties, and this component is the only one in the standard that cannot have the second in its full form.

**Determinism of derivation.** The state derived from an event log is a function of the log alone. Two derivations of the same log yield the same state. This is achievable, is required by clause P6-3.96, and is what makes the record an account of the execution.

**Reproducibility of execution.** Running the same instance again from the same inputs yields the same path. This is **not** achievable and this part does not require it, because the engine's inputs include real elapsed time, the arrival order of external events, and the availability of external components, none of which is under its control and none of which is a pin.

The distinction is the design. This component does not claim that an execution would happen the same way twice. It claims that what did happen is fully recoverable from the log, which is the weaker and achievable property, and it achieves it by making every non deterministic input an appended event: a timer elapse becomes a `timer_observation`, an event arrival becomes a correlation event, an invocation result becomes an attempt record. After that, replay reads the record rather than the world.

Section 13.2 records that this is a weaker guarantee than the four prior parts offer and that the weakening is forced rather than chosen.

**P6-6.1 (MUST) Derivation deterministic.** An implementation must derive the same state from the same event log on every derivation.

**P6-6.2 (MUST) Non deterministic inputs recorded as events.** An implementation must record every timer elapse, event arrival, invocation outcome and external availability condition as an appended event and must not consult the world during a replay.

**P6-6.3 (MUST) Replay reads the record.** An implementation must, during a replay, read every recorded observation rather than evaluating a clock, invoking a component or consulting external state.

**P6-6.4 (MUST NOT) No reproducibility claim.** An implementation must not represent an execution as reproducible in the sense of `Part 2` clause P2-1.4 and must declare that it guarantees recoverability of the recorded execution rather than repeatability of the execution.

**P6-6.5 (MUST) Derivation order total and declared.** An implementation must impose a declared total order on the derivation of state from concurrent events and must not permit the derived state to vary between derivations of one log.

### 6.2 The execution algorithm

Normative in its ordering and in its outcomes; not normative in its structure as code.

```
advance(instance):
  1  if state(instance) in {SUSPENDED, COMPLETED, TERMINATED, MIGRATED_OUT}:
                                             return REFUSED(INSTANCE_NOT_ADVANCEABLE)
  2  definition = pinned definition version of instance     // never re resolved
  3  runnable = {}
     for each flow token t in derived_state(instance):
        position = position(t)
        if position is an activity not yet instantiated:      runnable += t
        if position is a split:                               runnable += t
        if position is a join:
             if join_satisfied(position, derived_state):      runnable += t
        if position is an end position:                       runnable += t
  4  if runnable is empty:
        if an outstanding wait exists:        state = WAITING; record what releases each
        else if an end position was reached and tokens accounted: state = COMPLETED
        else if stall interval elapsed:       state = STALLED; emit; return
        else:                                 return                     // not yet stalled
  5  for each t in runnable, in the declared total order:
        case activity:
           create activity_instance; record CREATED
           if kind requires an invocation:
                attempt = invoke with the idempotence key of the activity instance
                record invocation_attempt; do not record an outcome not received
           if kind is WAIT:  record the wait and what would release it
           if kind is COMPENSATE:  raise a compensation_request per section 6.4
        case split:
           if kind is PARALLEL_SPLIT:
                activate every outgoing flow; record attribution kind STRUCTURAL
           else:
                determination = obtain per section 6.3
                if determination is absent:      suspend at the split; refer; return
                if determination is indeterminate:
                     apply the declared handling of section 3.13; record it
                else activate the flows the determination names
                record branch_attribution with flows taken and not taken
        case join:
           record join_resolution: arrived, not arrived, disposition applied
           apply the disposition to unwaited branches
           consume the arrived tokens per the join kind; produce the outgoing token
        case end position:
           consume the token; record the end reached
  6  if a bound was exhausted at any position:
        record the exhaustion; apply the declared on_exhaustion behaviour
  7  recompute derived state; if it differs from the served state, record a divergence
  8  emit events; register steps as Part 3 trail acts; return the derived state
```

Four properties of the algorithm are decisions rather than derivations.

**Step 2 never re resolves the definition.** The version was pinned at start and the resolution failing does not stop a running instance. Clause P6-4.33 states it and it is what makes long lived instances survivable.

**Step 4 distinguishes three empty cases.** No runnable work with an outstanding wait is `WAITING`. No runnable work with an end reached is `COMPLETED`. No runnable work with neither is a stall, and only after a declared interval, because a momentary absence of runnable work during concurrent advance is normal. Collapsing the three is the failure section 5.2 exists to prevent.

**Step 5 records the invocation attempt before the outcome.** An attempt with no recorded outcome is the `OUTCOME_UNKNOWN` state, and recording the attempt first is what makes the unknown case representable at all. An implementation that records only completed invocations cannot distinguish an invocation that was never made from one whose result was lost.

**Step 5 suspends rather than guessing at a conditional split with no determination.** There is no default branch unless one is declared as an artifact, and there is no evaluation performed here.

**P6-6.6 (MUST) Algorithm order.** An implementation must perform the steps above in the order given and must not activate a flow from a conditional split before recording the branch attribution.

**P6-6.7 (MUST) Pinned definition never re resolved during advance.** An implementation must use the pinned definition version throughout an instance's life and must not resolve the carrying document during an advance.

**P6-6.8 (MUST) Three empty cases distinguished.** An implementation must distinguish waiting, completion and stall per step 4 and must not treat an absence of runnable work as any one of them without the stated condition.

**P6-6.9 (MUST) Attempt recorded before outcome.** An implementation must record an invocation attempt before any outcome of it is known and must not record an attempt and its outcome as one indivisible event.

**P6-6.10 (MUST) Suspension rather than assumption at a split.** An implementation must suspend an instance at a conditional split for which no determination is available and must not activate a flow by any default not declared as an artifact.

**P6-6.11 (MUST) Join resolution recorded before disposition.** An implementation must record the join resolution, including which branches had not arrived, before applying any disposition to them.

### 6.3 Obtaining a determination

A conditional branch requires a determination and this section states where it comes from and what the engine may not do.

Three sources are admissible.

**A `Part 2` evaluation report**, obtained by an activity of kind `EVALUATE` earlier in the flow, whose whole report is pinned per clause P6-6.13. The split reads which rules were satisfied from the report; it does not evaluate anything.

**A `Part 5` decision**, obtained by an activity of kind `DECIDE`, whose whole outcome envelope is pinned. The decision's outcome value names the branch.

**A structural rule**, which is not a determination at all and applies only to the constructs clause P6-3.31 names.

The prohibition is that the engine may not obtain a determination by evaluating anything itself, and the prohibition covers three forms that look like exceptions and are not.

A comparison of two instance values is an evaluation. A test that a counter has reached its bound is admissible, because the counter is a `CONTROL_COUNTER` and the bound is a declared property of the definition, so the test is a structural property of the execution rather than a fact about the world. A test of any other value is not.

A test that an activity completed is admissible, because it is a `CONTROL_FLAG` derived from the engine's own events. A test of what the activity returned is not.

A test that a timer elapsed is admissible, because the elapse is a recorded observation. A test of whether the elapsed time exceeds a business threshold is not, because the threshold is a rule.

**P6-6.12 (MUST) Determination from a declared source.** An implementation must obtain every determination from a `Part 2` evaluation report, a `Part 5` decision or a structural rule and must record which.

**P6-6.13 (MUST) Whole envelope pinned.** An implementation must pin the whole `Part 2` evaluation report or `Part 5` outcome envelope on which a branch was attributed and must refuse a summary, a count or a bare value, per clause P2-12.6 and clause P6-3.5.

**P6-6.14 (MUST) Control tests enumerated.** An implementation must restrict the conditions it evaluates itself to the tests this section names as admissible and must not evaluate any other condition.

**P6-6.15 (MUST NOT) No comparison of instance values.** An implementation must not route by comparing two instance values, other than a `CONTROL_COUNTER` against a declared bound.

**P6-6.16 (MUST NOT) No threshold on an observed time.** An implementation must not compare an observed elapse against a threshold other than the declared duration or instant of the timer that produced it.

### 6.4 Compensation semantics

```
compensate(scope_instance, order_kind, request):
  1  if state(scope_instance) != COMPENSATION_ENABLED:
        record DECLINED with the reason; outcome = COMPENSATION_NOT_ATTEMPTED; return
  2  if request came from normal flow and carries no determination:
        record DECLINED; return                       // per clause P6-3.59
  3  enclosed = compensable elements of the scope, being
        completed enclosed scopes, completed compensable activities,
        and each completed iteration of each completed repetition
  4  order = sequence enclosed by order_kind:
        REVERSE_COMPLETION   -> reverse of recorded completion order
        REVERSE_DEPENDENCY   -> reverse of declared control dependencies
        DECLARED_SEQUENCE    -> the declared sequence
     where two elements completed within the clock's precision, record that
     their relative order is not established and use the declared tie rule
  5  for each element in order:
        if compensability is IRREVERSIBLE:
             outcome(element) = COMPENSATION_IMPOSSIBLE
             enumerate residue from the declared residue kinds
             continue                                  // do not stop the sequence
        if no handler:
             outcome(element) = NO_COMPENSATION_DEFINED
             enumerate residue as the whole effect
             continue
        execute the handler's activities against the state as at the element's completion
        obtain the outcome from the performing component or a named actor
        if not obtained: outcome(element) = COMPENSATION_FAILED, position unknown
        record outcome and any residue
        if a bound on compensation effort is exhausted:
             outcome(remaining) = COMPENSATION_NOT_ATTEMPTED; break
  6  scope outcome =
        COMPENSATED_FULLY      if every element is COMPENSATED_FULLY
        COMPENSATED_PARTIALLY  if some are and some are not
        COMPENSATION_IMPOSSIBLE if every element is impossible
        COMPENSATION_FAILED    if any element failed and none succeeded
  7  record the scope outcome, every residue, the elapsed interval since completion
  8  record the compensation as an act with Part 3; raise review obligations
```

Three properties are decisions.

**Step 5 continues past an impossible element.** An implementation that stops on encountering an irreversible activity leaves the compensable elements after it uncompensated, which is strictly worse: the position is then partly restored in an arbitrary way determined by the order. Continuing compensates everything that can be compensated and enumerates what cannot.

**Step 5 obtains the outcome rather than inferring it.** The handler's activities completing is not the compensation having worked, per clause P6-3.72.

**Step 6 derives the scope outcome from the element outcomes** rather than accepting it, so a scope containing one irreversible activity cannot be recorded as fully compensated however the handler behaved.

**P6-6.17 (MUST) Compensation algorithm order.** An implementation must perform the steps above in the order given.

**P6-6.18 (MUST) Impossible elements do not halt the sequence.** An implementation must continue compensating the remaining elements after recording an impossible or failed element and must not abandon the sequence.

**P6-6.19 (MUST) Scope outcome derived from element outcomes.** An implementation must derive the scope's compensation outcome from the outcomes of its elements as step 6 specifies and must not accept it as an input.

**P6-6.20 (MUST) Concurrent completion tie rule declared.** An implementation must declare the rule by which it orders elements whose completions were not distinguishable, and must record that their relative order was not established.

**P6-6.21 (MUST) Compensation effort bounded.** An implementation must declare a bound on compensation effort and must record the remaining elements as `COMPENSATION_NOT_ATTEMPTED` where it is exhausted.

**P6-6.22 (MUST) State as at completion.** An implementation must execute a compensation handler against the values as at the completion of the element being compensated and must record where a later value would have differed, per clause P6-3.61.

### 6.5 Clocks and observed time

Three clocks, with one extension particular to this component.

`Part 1` section 3.1 forbids a component from assigning an occurrence time. This component **observes** elapsed time, which is neither assigning an actor's assertion nor computing from a stored value, and the extension is stated here so that it is not read as a departure.

The discipline is: observe once, record the observation with its clock source and its lateness, and thereafter read the record. An observation is a fact about what this component saw, attributable to this component, and it is the one class of occurrence time this component may originate. Clause P6-6.25 states the constraint that keeps it honest: the observation is recorded as an observation rather than as the instant the declared duration expired, and the two are recorded separately.

**P6-6.23 (MUST) Knowledge time assigned by this component.** An implementation must assign every knowledge time from its own clock and must refuse an event supplying one.

**P6-6.24 (MUST NOT) No actor occurrence time assignment.** An implementation must not assign an occurrence time on behalf of an actor and must record every actor asserted occurrence time as asserted.

**P6-6.25 (MUST) Observation distinguished from expiry.** An implementation must record the instant a timer's declared duration expired and the instant it observed the expiry as two values and must not record one in place of the other.

**P6-6.26 (MUST) Clock source recorded per observation.** An implementation must record the clock source of every observation and must record where the source changed.

**P6-6.27 (MUST) Application time cited, not determined.** An implementation must record application times as supplied by the components that resolved against them and must not determine what was in force at one.

**P6-6.28 (MUST) Instants in a declared scale.** An implementation must record every instant in a declared time scale with a declared offset.

**P6-6.29 (MUST) Monotonic knowledge time within an instance.** An implementation must assign knowledge times that do not decrease within an instance's event sequence and must record any correction of its own clock as an event.

**P6-6.30 (MUST) Calendar convention declared.** An implementation must declare the convention by which it adds durations expressed in months or years to an instant and must pin the convention in the instance.

### 6.6 Idempotence

**P6-6.31 (MUST) Idempotence by key.** An implementation must return the originally recorded outcome for a repeated recording, driving or intervening operation bearing an idempotence key already seen within its declared deduplication window and must not append again.

**P6-6.32 (MUST) Deduplication window declared.** An implementation must declare its deduplication window as a duration and must state what happens to a key repeated after it.

**P6-6.33 (MUST NOT) No idempotence across differing payloads.** An implementation must refuse an operation bearing a seen key with a different payload.

**P6-6.34 (MUST) Duplicate instance starts detectable.** An implementation must be able to report instances of one definition version whose correlation keys and start payloads coincide, so that a duplicate start is discoverable.

### 6.7 Static analysis: soundness and the limits of it

Four properties of a process definition version are worth knowing before it runs. All four are established results and the fourth is a limitation rather than a property.

**Soundness.** A process definition is sound where three conditions hold: from every reachable state it is possible to reach the state in which the process has properly completed, which is the **option to complete**; the completed state leaves no work outstanding, which is **proper completion**; and every activity is reachable from the start, so there are **no dead activities**. The three conditions are those of the workflow net literature and the property guarantees the absence of deadlocks, livelocks and other anomalies detectable without domain knowledge. The classical result is that soundness of a workflow net corresponds to liveness and boundedness of the net obtained by connecting its sink back to its source.

**Decidability.** Soundness is decidable, and for the free choice class it is decidable in polynomial time. This is why the restriction of section 3.7 is worth its cost: a definition whose conditional constructs are free choice and whose inclusive joins are structured is in the class where the analysis is cheap.

**Undecidability under cancellation.** Soundness is **undecidable** for workflow nets with reset arcs, which is how cancellation is modelled, and it is undecidable for the weaker relaxed notions as well. This is the result that shapes the requirement: **declaring a cancellation region moves a definition out of the class in which its soundness can be established.** An implementation cannot analyse it and must say so rather than report that nothing was found. Clause P6-6.38 requires it.

**Exclusive split exclusivity.** Whether the conditions on an exclusive split are mutually exclusive is decidable where the conditions are `Part 2` rules over a bounded domain and undecidable in general. Clause P6-6.39 requires the analysis where it is possible and requires the honest report where it is not.

`definition_analysis` records the results of each analysis, the procedure version, the class the definition was found to be in, the analyses not performed and why, and the knowledge time.

**P6-6.35 (MUST) Soundness analysed where decidable.** An implementation must analyse soundness over every definition version whose form places it in a class where soundness is decidable, and must record the three conditions separately.

**P6-6.36 (MUST) Class recorded.** An implementation must record the class in which a definition version falls for the purpose of the analysis, and must record the structural features that placed it there.

**P6-6.37 (MUST) Analyses not performed recorded with the reason.** An implementation must record, for every analysis it did not perform, that it was not performed and why.

**P6-6.38 (MUST) Cancellation undecidability declared.** An implementation must record, for every definition version containing a cancellation region, that its soundness cannot be established, and must not report the absence of a finding as soundness.

**P6-6.39 (MUST) Exclusivity analysed or its impossibility recorded.** An implementation must analyse the mutual exclusivity of the conditions on every `EXCLUSIVE_SPLIT` where the form admits it and must record that it could not where it does not.

**P6-6.40 (MUST NOT) No absence of finding as absence of fault.** An implementation must not report a definition version as sound, deadlock free or free of dead activities on the basis of an analysis that did not complete or was not performed.

**P6-6.41 (MUST) Dead activities reported.** An implementation must report every activity unreachable from a start position and must include the count in the signals of section 8.5.

**P6-6.42 (MUST NOT) No analysis at execution time.** An implementation must not perform a soundness analysis during an advance and must not vary an execution on the basis of an analysis result.

**P6-6.43 (MUST) Analysis pinned to a version.** An implementation must record every analysis result against the definition version analysed and must not carry a result forward to a later version.

### 6.8 Bounds and resource limits

Bounds appear in four places in this part and each has a different exhaustion behaviour.

A **repetition or cycle bound** limits traversals. Exhaustion applies the declared `on_exhaustion` behaviour.

A **multiple instance bound** limits instances created. Exhaustion records the instances not created as `SKIPPED` and applies the declared behaviour.

A **compensation effort bound** limits the elements a compensation will attempt. Exhaustion records the remainder as `COMPENSATION_NOT_ATTEMPTED`, per clause P6-6.21.

An **instance bound** limits concurrent instances of a definition version. Exhaustion refuses the start, per section 7.6, and this is the bound that protects the estate from the failure of section 3.8.

**P6-6.44 (MUST) Every bound has a declared exhaustion behaviour.** An implementation must record the behaviour on exhaustion of every declared bound and must apply it rather than failing.

**P6-6.45 (MUST) Exhaustion is an outcome, not an error.** An implementation must record every bound exhaustion as an outcome of section 7.3 and must emit the corresponding event.

**P6-6.46 (MUST) Instance bound refuses the start.** An implementation must refuse to start an instance where the declared concurrent instance bound of its definition version is reached and must record the refusal.

**P6-6.47 (MUST NOT) No silent bound.** An implementation must not apply an undeclared bound and must not truncate an execution without recording the bound that truncated it.

### 6.9 What this component may compute, and what it may not

It may compute: which flow tokens exist and where; which activities are runnable; whether a join is satisfied under its declared kind; whether a declared bound is exhausted; the derived state of an instance from its log; the compensation order under a declared order kind; the scope compensation outcome from its element outcomes; the four analyses of section 6.7; and every projection of section 3.17.

It may not compute: whether a candidate satisfies a rule, which is `Part 2`'s; which of several branches should be taken where the choice requires a criterion, which is `Part 5`'s; what was in force at an application time, which is `Part 1`'s; the meaning of anything, which is `Part 4`'s; whether a person may perform an operation, which is `Part 7`'s; who should do a human activity, which is `Part 8`'s; whether a compensation restored the position, which is a fact about the world; and whether the process definition is the right process, which is nobody's in this standard.

**P6-6.48 (MUST) Permitted computations only.** An implementation must not compute any determination allocated to another component by section 12 and must return the recorded outcome that component supplied.

**P6-6.49 (MUST NOT) No inference of a determination.** An implementation must not generate, complete or assume a determination for a conditional branch.

**P6-6.50 (MUST NOT) No learning from executions.** An implementation must not adjust a definition version, a bound, a join kind or a disposition on the basis of observed executions, and must require every change to be a recorded definition version.

**P6-6.51 (MUST NOT) No assessment of process fitness.** An implementation must not assert that a process definition is appropriate, efficient or well designed, and must report only the analyses of section 6.7 and the distributions of section 8.5.
## 7. Outcome and failure taxonomy

### 7.1 Why the taxonomy is the specification

This component produces four kinds of output and each has a characteristic way of being wrong that the output itself conceals.

An **instance outcome** says how an execution ended. It is wrong invisibly when an instance that deadlocked is reported as finished, which is what implicit termination produces.

An **activity outcome** says what a step did. It is wrong invisibly when an outcome supplied by an operator under pressure is reported as an outcome the invoked component produced, and when an invocation whose result was never received is reported as a failure.

A **compensation outcome** says whether an undo worked. It is wrong invisibly whenever it is reported at all in most implementations, because the only distinction available is that the handler completed.

A **bound exhaustion** says the engine stopped early. It is wrong invisibly when it is reported as a failure, because a failure is retried and an exhausted bound will exhaust again.

In all four the well formed, plausible output is the failure mode, and the taxonomy exists so the qualification travels with the outcome.

### 7.2 Instance outcomes

Eight members in four classes. The table is normative.

| Class | Member | Means |
| --- | --- | --- |
| Completed | `COMPLETED_AT_END_POSITION` | An end position was reached and every token is accounted for. |
| Completed | `COMPLETED_WITH_UNWAITED_WORK` | As above, and a join proceeded without branches whose work was discarded or is still recorded. |
| Terminated | `TERMINATED_BY_CANCELLATION` | Cancelled by an authorised intervention, with the declared compensation treatment applied. |
| Terminated | `TERMINATED_BY_FAULT` | A fault propagated to the process level and no handler caught it. |
| Terminated | `TERMINATED_BY_BOUND` | A declared bound whose exhaustion behaviour is termination was exhausted. |
| Stalled | `STALLED` | No runnable work, no outstanding wait, no end position reached. Nothing will release it. |
| Migrated | `MIGRATED_OUT` | The instance continues under a target definition version. |
| Refusal | `REFUSED` | The instance was not started, or an operation upon it was declined. Carries a code. |

Four distinctions are load bearing.

**`COMPLETED_AT_END_POSITION` against `COMPLETED_WITH_UNWAITED_WORK`.** Both completed. In the second, work was performed that nothing consumed, and the organisation paid for it. Separating the two is what makes the discarded work of section 3.6 countable at the instance level rather than only per join.

**`STALLED` against every completed member.** The distinction the whole of section 5.2 exists for. An implementation with implicit termination cannot draw it, and its population of completed instances includes every instance that deadlocked.

**`TERMINATED_BY_BOUND` against `TERMINATED_BY_FAULT`.** A bound exhaustion is the engine doing what it was told. A fault is something going wrong. Reporting the first as the second sends it to whoever handles faults, who will retry it.

**`MIGRATED_OUT` against `TERMINATED`.** The instance did not end. Recording it as terminated loses the continuity and produces two histories for one execution with nothing joining them.

**P6-7.1 (MUST) Closed instance outcome set.** An implementation must record exactly one member of the table above for every instance reaching a terminal condition and must not record a value outside the set.

**P6-7.2 (MUST) Unwaited work distinguished at the instance level.** An implementation must record `COMPLETED_WITH_UNWAITED_WORK` where any join proceeded without every branch and must not record `COMPLETED_AT_END_POSITION`.

**P6-7.3 (MUST) Stall is not completion.** An implementation must not record a stalled instance under any completed member.

**P6-7.4 (MUST) Bound termination distinguished from fault.** An implementation must record `TERMINATED_BY_BOUND` where a bound's exhaustion behaviour terminated the instance and must not record it as a fault.

**P6-7.5 (MUST NOT) No mapping onto a success and failure pair.** An implementation must not provide an interface that maps the eight members onto two values and must not document such a mapping as canonical.

### 7.3 Activity and bound outcomes

Activity instance outcomes, drawn from the states of section 5.3 that are terminal: `COMPLETED`, `FAULTED`, `CANCELLED`, `OUTCOME_UNKNOWN`, `OUTCOME_FORCED`, `SKIPPED`.

Two of the six are the ones that matter and both are commonly collapsed into their neighbours.

**`OUTCOME_UNKNOWN` is not `FAULTED`.** An invocation for which no response was received may have performed the work. Recording it as failed and retrying a non idempotent activity is the mechanism by which a payment is made twice. Clause P6-7.7 forbids the collapse and clause P6-3.106 forbids the retry.

**`OUTCOME_FORCED` is not `COMPLETED`.** The invoked component did not report completion; an operator asserted it. Every downstream consumer treating it as a completion is relying on an assertion made under pressure, and clause P6-7.8 requires the marking to be permanent and visible.

Bound exhaustion outcomes: `BOUND_EXHAUSTED_LOOP_EXITED`, `BOUND_EXHAUSTED_INSTANCE_TERMINATED`, `BOUND_EXHAUSTED_FAULT_RAISED`, `BOUND_EXHAUSTED_INSTANCES_NOT_CREATED`, `BOUND_EXHAUSTED_COMPENSATION_INCOMPLETE`.

The five are separate members rather than one with a parameter, because they have five different consequences: the loop stopped early and the process continued; the instance ended; a fault entered the scope's handler; some members of a collection were never processed; and some compensable elements were never compensated. The fourth and fifth are the ones that leave work undone in the world, and clause P6-7.10 requires both to raise the review obligation of section 7.5.

**P6-7.6 (MUST) Closed activity outcome set.** An implementation must record exactly one of the six terminal activity states as the outcome of every activity instance.

**P6-7.7 (MUST) Unknown outcome distinguished from fault.** An implementation must record `OUTCOME_UNKNOWN` where no response was received and must not record `FAULTED`.

**P6-7.8 (MUST) Forced outcome permanently marked.** An implementation must record `OUTCOME_FORCED` permanently, must carry it into every projection, report and export, and must not permit it to be presented as `COMPLETED`.

**P6-7.9 (MUST) Bound exhaustion members distinguished.** An implementation must record exactly one of the five bound exhaustion members and must not report them under one member with a parameter.

**P6-7.10 (MUST) Work left undone raises a review obligation.** An implementation must raise the review obligation of section 7.5 for every `BOUND_EXHAUSTED_INSTANCES_NOT_CREATED` and `BOUND_EXHAUSTED_COMPENSATION_INCOMPLETE` outcome.

### 7.4 Defect outcomes

Four conditions are defects in the record or the definition rather than outcomes of an execution, and they are separated because they escalate differently.

| Member | Means |
| --- | --- |
| `DEFECT_SECOND_ARRIVAL_AT_SIMPLE_MERGE` | Two flows arrived at a merge that expects one. |
| `DEFECT_EVENT_SEQUENCE_GAP` | A gap in an instance's event sequence. The instance's state is unestablished. |
| `DEFECT_REPLAY_DIVERGENCE` | Replay from the log yields a state differing from the state served. |
| `DEFECT_CORRELATION_AMBIGUOUS` | A correlation key resolved to more than one live instance. |

`DEFECT_EVENT_SEQUENCE_GAP` is the most serious, because it means the state of the instance is not established: the engine cannot say what the instance is doing, and any advance it performs may be against a state that never existed. Clause P6-7.13 requires the instance to be suspended rather than advanced.

**P6-7.11 (MUST) Defects reported as defects.** An implementation must record each condition above as a defect, must emit the corresponding event, and must escalate defects through a channel distinct from execution outcomes.

**P6-7.12 (MUST) Second arrival not absorbed.** An implementation must record `DEFECT_SECOND_ARRIVAL_AT_SIMPLE_MERGE` and must not consume the second token silently.

**P6-7.13 (MUST) Gap suspends the instance.** An implementation must suspend an instance in which an event sequence gap is detected, must not advance it, and must record the suspension as a defect rather than as an intervention.

**P6-7.14 (MUST NOT) No defect as a fault.** An implementation must not route a defect of this section into a fault handler, since a fault handler is a declared response to a business condition and a defect is a failure of the record.

### 7.5 The outcome envelope and review obligations

The outcome envelope of an instance is normative in content; serialisation unspecified.

The instance identity, its pinned definition version and whether it was migrated. The outcome member. The path, being the ordered activity instances with their outcomes. Every branch attribution with its determination reference and determination kind, and the handling applied where a determination was indeterminate. Every join resolution with arrived and unarrived branches and the disposition applied. Every bound exhaustion with its member. Every compensation outcome with its residue and assignment state. Every invocation attempt count by activity. Every intervention with its actor, authorisation, reason and whether an outcome was forced. Every timer observation with its lateness. Every instance value by kind. The three clocks. The stall detection interval and, where stalled, the position and what was awaited.

A **review obligation** is raised where the execution left something requiring a person's attention that no other mechanism will surface. The enumeration is closed: an unassigned residue; a compensation outcome other than full; a bound exhaustion leaving work undone; a branch taken on an unestablished condition; an outcome forced by intervention; a stall; and discarded work above a declared threshold.

A review obligation is not a task. It is a recorded fact that something needs review, and the task by which somebody reviews it belongs to `Part 8`. Clause P6-7.18 states the distinction, because an implementation that raises a task instead has put the obligation in a queue that can be cleared without the underlying record changing.

**P6-7.15 (MUST) Envelope completeness.** An implementation must include every element named above in every instance outcome envelope it returns and records.

**P6-7.16 (MUST NOT) No envelope reduction.** An implementation must not omit an envelope element on the ground that a caller does not use it.

**P6-7.17 (MUST) Review obligations raised on the enumerated conditions.** An implementation must raise a review obligation for every condition the enumeration above names and must record it against the instance.

**P6-7.18 (MUST) Obligation distinguished from task.** An implementation must record a review obligation as a fact about the instance, must obtain any task by which it is discharged from `Part 8`, and must not treat the closure of a task as the discharge of the obligation unless a recorded act says so.

**P6-7.19 (MUST) Open obligations countable.** An implementation must be able to report every open review obligation by condition, definition version and age, and must include the counts in the signals of section 8.5.

### 7.6 Refusal codes

| Code | Cause | Retryable |
| --- | --- | --- |
| `DEFINITION_UNRESOLVABLE` | The definition version could not be resolved at start | No |
| `DEFINITION_WITHDRAWN_FROM_STARTING` | The version no longer admits new instances | No |
| `DEFINITION_UNANALYSED` | The form admits the soundness analysis and it was not performed | No, until analysed |
| `INSTANCE_BOUND_REACHED` | The concurrent instance bound is reached | Yes, later |
| `CORRELATION_KEY_BOUND` | The key is already bound to a live instance | No |
| `INSTANCE_NOT_ADVANCEABLE` | The instance is suspended, terminated, completed or migrated out | No |
| `DETERMINATION_ABSENT` | A conditional split has no available determination | Yes, with the determination |
| `PIN_UNOBTAINABLE` | A required pinned artifact could not be obtained | Possibly |
| `ELIGIBILITY_OR_DECISION_UNAVAILABLE` | `Part 2` or `Part 5` could not be reached | Possibly |
| `HUMAN_TASK_UNAVAILABLE` | `Part 8` could not be reached to create a work item | Possibly |
| `SCOPE_COMPENSATION_UNAVAILABLE` | The named scope did not complete successfully | No |
| `RESIDUE_REQUIRED` | A compensation outcome requiring residue was submitted without one | Yes, corrected |
| `NOT_AUTHORISED` | `Part 7` did not permit the operation | No, without a changed decision |
| `MAPPING_INCOMPLETE` | A migration mapping does not cover every occupiable position | No |
| `MIGRATION_UNSOUND` | The post migration state cannot reach completion | No |
| `VALUE_KIND_UNDECLARED` | An instance value of no declared kind was submitted | Yes, corrected |
| `MALFORMED` | The submission was not well formed | Yes, corrected |
| `IDEMPOTENCE_KEY_CONFLICT` | A seen key with a different payload | Yes, with a new key |

The set is open under section 9.9.

**P6-7.20 (MUST) Refusal codes.** An implementation must return one of the codes above, or a registered code, for every refused operation.

**P6-7.21 (MUST) Refusal states what must change.** An implementation must state, with every refusal, whether the operation may be retried and what must change.

**P6-7.22 (MUST) Refusals recorded.** An implementation must record every refusal with its code, the request and the knowledge time, and must record a refusal to start against the definition version rather than against a non existent instance.

**P6-7.23 (MUST NOT) No refusal as an outcome.** An implementation must not record a refusal as an instance outcome and must not record a refused start as a terminated instance.

### 7.7 Outcome obligations

Normative.

| Outcome | Component records | Component emits | Caller must |
| --- | --- | --- | --- |
| `COMPLETED_AT_END_POSITION` | Envelope, path, attributions | Instance completed | Nothing |
| `COMPLETED_WITH_UNWAITED_WORK` | As above, with the discarded work | Instance completed and unwaited work discarded | Account for the work performed and not used |
| `STALLED` | Envelope, position, what was awaited | Instance stalled | Treat as requiring intervention, not retry |
| `TERMINATED_BY_BOUND` | As above, with the bound | Bound exhausted | Not retry; the bound will exhaust again |
| `TERMINATED_BY_FAULT` | As above, with the fault and handlers run | Instance terminated | Investigate the fault |
| `TERMINATED_BY_CANCELLATION` | As above, with the authorisation and compensation treatment | Instance cancelled | Account for residue |
| `OUTCOME_UNKNOWN` on an activity | Attempt with no outcome | Invocation outcome unknown | Establish what happened before retrying anything non idempotent |
| `OUTCOME_FORCED` on an activity | Intervention, actor, authorisation, reason | Outcome forced | Treat the outcome as an operator's assertion |
| Any compensation outcome other than full | Outcome, residue, review obligation | The corresponding compensation event | Assign the residue |
| Any defect member | Defect record | The corresponding defect event | Escalate as a record failure, not a business fault |
| `REFUSED` | Refusal, code | Nothing beyond the refusal | Correct the request or escalate |

**P6-7.24 (MUST) Recording obligations honoured.** An implementation must record everything the table above requires for every outcome it produces.

**P6-7.25 (MUST) Emission obligations honoured.** An implementation must emit every event the table above requires.

**P6-7.26 (MUST) Caller obligations documented.** An implementation must document the caller obligations above and must state that it does not enforce them.

**P6-7.27 (MUST NOT) No completion language for a stall.** An implementation must not describe a stalled instance as finished, ended, closed or complete in any report, projection, interface or export.

### 7.8 The three things this section is for

**P6-7.28 (MUST) A stopped execution is never a finished one.** An implementation must not, by any mechanism, configuration, default, aggregation, projection, interface, export or summary, represent an instance with no runnable work that did not reach an end position as an instance that completed.

**P6-7.29 (MUST) An operator's assertion is never a component's result.** An implementation must not represent an activity outcome supplied by an intervention as an outcome reported by the invoked component, and must carry the forced marking permanently.

**P6-7.30 (MUST) A completed handler is never a restored position.** An implementation must not represent a compensation as having restored the position on the strength of its handler having completed, and must record the outcome member and every residue.
## 8. Observability and the audit record

### 8.1 The event log is the audit record, and it is not the trail

This component's event log is its audit record. Because nothing is updated in place and every state is derived, the log is already a complete account of what the engine did.

It is not, however, the trail of `Part 3`. `Part 3` clause P3-12.14 requires a process step to be registered as a subject act in a trail rather than as a citation in a basis, and section 12.3 is the reciprocal. So a step appears in two places with two purposes: here as an event in the engine's log, from which the engine's state derives, and there as an act in the subject's trail, from which the subject's history reads.

The division is that this log answers what the engine did and the trail answers what happened to the subject. They overlap and they are not duplicates: the engine's log contains token movements, join resolutions and derived state transitions that are meaningless to a subject's history, and the trail contains acts by other components that this engine never saw.

Clause P6-8.2 states the resolution and clause P6-8.3 forbids the tempting alternative, which is to treat the engine's log as the trail and skip the registration. That alternative fails when the orchestrator is replaced, which is exactly the condition every prior part required its own records to survive.

**P6-8.1 (MUST) Log is the audit record of the engine.** An implementation must be able to produce, for any instance within its retained history, the complete event log in sequence order with any gap marked.

**P6-8.2 (MUST) Steps registered as trail acts.** An implementation must register every step that concerns an identified subject as a `Part 3` subject act, must record the registration, and must be able to report every step not yet registered.

**P6-8.3 (MUST NOT) No log as trail.** An implementation must not represent its own event log as the subject's trail and must not omit the `Part 3` registration on the ground that the log contains the information.

**P6-8.4 (MUST NOT) No separate mutable log.** An implementation must not maintain an execution log whose contents can diverge from the events and must not provide a means of disabling the recording of any event this part requires.

**P6-8.5 (MUST) Own operations recorded.** An implementation must record its own definition refusals, analyses, replays, interventions, exports and reads as entries.

### 8.2 Grain

| Subject | Grain |
| --- | --- |
| Definition version | One entry per version, plus one per activity, flow, split, join, scope, handler and bound. |
| Definition analysis | One entry per analysis per version, including analyses not performed. |
| Migration mapping | One entry per mapping, plus one per mapped position and per disposition. |
| Instance | One entry per instance. |
| Instance event | One entry per event. Contiguous within the instance. |
| Activity instance | One entry per activity instance, including those `SKIPPED`. |
| Invocation attempt | One entry per attempt, not one per activity instance. |
| Branch attribution | One entry per activation of a conditional split. |
| Join resolution | One entry per join firing, with arrived and unarrived branches enumerated. |
| Iteration | One entry per iteration of a repetition and per instance of a multiple instance activity. |
| Compensation | One entry per request, one per execution, one per outcome, one per residue, one per assignment. |
| Timer observation | One entry per observation. |
| Correlation | One entry per binding and one per unmatched event. |
| Instance value | One entry per value per set, since a value's history is part of the log. |
| Intervention | One entry per intervention, with the actor and authorisation. |
| Migration | One entry per migration execution. |
| Read | One entry per instance, path, projection or package returned to a principal. |
| Signal | One entry per signal per observation interval. |

Two grains will be resisted on volume grounds and both are required.

**One entry per invocation attempt.** An activity retried eleven times produces eleven entries. That is the point: the retry distribution of clause P6-3.107 is the earliest available signal that a dependency is failing, and it does not exist if only the successful attempt is recorded.

**One entry per iteration.** A repetition of four hundred iterations produces four hundred entries. Without them, per iteration compensation under clause P6-3.51 cannot be performed, because the engine does not know which iterations completed.

**P6-8.6 (MUST) Declared grain.** An implementation must record at the grain of the table above, or declare a finer grain, and must not record at a coarser one.

**P6-8.7 (MUST) Attempts and iterations recorded individually.** An implementation must record each invocation attempt and each iteration as its own entry and must not record aggregates in their place.

**P6-8.8 (MUST) Skipped activities recorded.** An implementation must record an activity instance for every activity on an untaken branch, per clause P6-5.18.

**P6-8.9 (MUST) Counting grain stated with every count.** An implementation must state the grain of every count it reports.

### 8.3 What must be recorded with every instance

Sufficient to derive the state, explain the path and account for what was left undone, without this component running.

Required: the definition version pin; the whole event log in sequence; every activity instance with its outcome; every invocation attempt with its idempotence key, target and outcome including unknown; every branch attribution with its determination reference, determination kind and indeterminate handling; every join resolution with arrived and unarrived branches and the disposition; every iteration; every bound exhaustion; every compensation request, execution, outcome, residue and assignment; every timer observation with its declared instant, observed instant, lateness and clock source; every correlation binding and unmatched event; every instance value with its kind; every intervention with actor, authorisation, reason and forced marking; every migration with its mapping and dispositions; the conventions in force; and the outcome of every precondition check applied at recording, including those that passed.

**P6-8.10 (MUST) Derivation sufficiency.** An implementation must record enough with every instance to derive its whole state and path from the log alone and must treat an instance whose state it cannot derive as a defect under section 7.4.

**P6-8.11 (MUST) Unknown outcomes recorded as unknown.** An implementation must record an invocation attempt with no received response as having an unknown outcome and must not omit it.

**P6-8.12 (MUST) Conventions recorded.** An implementation must record the time scale, calendar and clock source conventions in force for every instance.

**P6-8.13 (MUST) Precondition outcomes recorded, including passes.** An implementation must record the outcome of every precondition check applied at definition recording and the version of the precondition set applied.

**P6-8.14 (MUST) Periodic replay sampling.** An implementation must replay a declared sample of retained instances on a declared cycle, must record every divergence, and must declare the sample and the cycle.

**P6-8.15 (MUST) Divergence recorded, not corrected.** An implementation must record a replay divergence as a defect about the record and must not amend the log or the served state.

### 8.4 Access records

**P6-8.16 (MUST) Reads recorded.** An implementation must record every return of an instance, a path, a projection or an evidence package to a principal, with the principal, the subject, the purpose and the knowledge time.

**P6-8.17 (MUST) Withholding recorded.** An implementation must record a read that was refused or reduced by an authorisation decision, with the decision reference, whether or not the requester was told.

**P6-8.18 (MUST) Interventions recorded with the operator.** An implementation must record the operator of every intervention, since an intervention is an assertion standing in for a component's result.

**P6-8.19 (SHOULD) Read records retained with the instance.** An implementation should retain the read records of an instance for as long as the instance.

### 8.5 Signals

Each signal measures a way in which this part's guarantees are hollowed out while every individual instance continues to look healthy.

| Signal | Grain | Why it matters |
| --- | --- | --- |
| Stalled instances by definition version, position and age | One instance | The population that stopped and nobody noticed. The single most important signal in the part. |
| Instances by outcome member | One instance | Where completion, stalling, bound termination and cancellation concentrate. |
| Instances waiting, by what they are waiting for | One instance | The operator's view, and the population of waits whose releaser no longer exists. |
| Instances by pinned definition version, with age | One instance | The population that migration would have to address, or that is running old policy. |
| Disposal demonstration exceptions | One value | The accretion of section 1.3 caught in the act. |
| Instance values by kind and volume, especially opaque transit | One value | A rising opaque transit volume is business data wearing a disguise. |
| Discarded work by definition version | One activity instance | Work paid for and not used, per join disposition. |
| Join resolutions proceeding without every branch | One resolution | Where partial joins are firing and what became of the rest. |
| Bound exhaustions by member and definition version | One exhaustion | Loops and collections hitting their limits, and work not created. |
| Invocation attempts per activity instance, distribution | One activity instance | A rising retry rate is a dependency failing. |
| Attempts with unknown outcomes | One attempt | Invocations that may have happened. |
| Activities with `OUTCOME_FORCED` | One activity instance | Operator assertions standing in for component results. |
| Interventions by operator, kind and definition version | One intervention | Where the engine is being driven by hand. |
| Token moves, with the soundness assessment result | One intervention | The most dangerous intervention available. |
| Compensations by outcome member | One compensation | Partial, impossible and failed separately, since the owners differ. |
| Unassigned residue by kind and age | One residue | Consequences nobody is answerable for. |
| Compensations beyond the staleness threshold | One compensation | Compensation performed against a world that has moved. |
| Activities of compensability `COMPENSABILITY_UNDECLARED` | One activity definition | Process definitions with no compensation model. |
| Irreversible activities within compensable scopes | One activity definition | Scopes that cannot be fully undone, known at design time. |
| Indeterminate branches by handling applied | One attribution | Where the third value reached this component and what it did. |
| Branches taken on an unestablished condition | One attribution | Policy applied without the condition being established. |
| Unmatched inbound events by correlation key and age | One event | Work that arrived for nobody. |
| Timer observations beyond the lateness threshold | One observation | Deadlines noticed late. |
| Definition versions unanalysed, and unanalysable by class | One version | Unknown soundness, distinguished from soundness. |
| Dead activities detected | One activity definition | Positions no execution can reach. |
| Definition versions containing an arbitrary cycle or a cancellation region | One version | The forms in which soundness cannot be established. |
| Replay divergences and event sequence gaps | One instance | Decay of the record. |
| Open review obligations by condition and age | One obligation | Work the executions left behind. |
| Steps not yet registered as `Part 3` trail acts | One step | The trail falling behind the engine. |

Three of these are the ones an organisation should read first.

**Stalled instances** is the signal that most distinguishes an implementation of this part from an ordinary engine, because an ordinary engine does not have the state.

**Disposal demonstration exceptions** is the signal that protects the spine. It should be zero and it will not be, and the rate at which it rises is the rate at which the engine is becoming a system of record.

**Irreversible activities within compensable scopes** is a design time signal reported at run time, so that on the day a compensation fails to restore a position, the record shows that the condition was known for years.

**P6-8.20 (MUST) Signals produced.** An implementation must produce every signal in the table above at a declared interval and must declare the interval.

**P6-8.21 (MUST) Signals derived from events.** An implementation must derive every signal from recorded events and must be able to enumerate the events behind any signal value.

**P6-8.22 (MUST NOT) No suppression of a signal.** An implementation must not provide a means of disabling, filtering or thresholding a signal such that a non zero value is reported as zero.

**P6-8.23 (MUST) Stall signal standing.** An implementation must produce the stalled instance signal continuously rather than on demand, since its value depends on absence and nobody will request it.

**P6-8.24 (MUST) Waiting signal states the releaser.** An implementation must report, for every waiting instance, what would release it, and must separately report waits whose releaser cannot be identified.

**P6-8.25 (MUST) Disposal exception trend available.** An implementation must be able to report disposal demonstration exceptions over time, so that accretion is distinguishable from a stable position.

**P6-8.26 (SHOULD) Signal thresholds declared.** An implementation should declare, for each signal, the value at which it requires attention, and should record the declaration as a controlled document under `Part 1`.

### 8.6 The evidence package

Self describing, sufficient to account for an execution without this component running.

Contents, all required.

The instance outcome envelope of section 7.5 in full.

The pinned definition version in full: activities with their kinds, compensability and residue kinds; flows; splits and joins with their kinds and dispositions; scopes and their handlers; bounds with their authorities and justifications; cancellation regions; and the addressing scheme.

The content of the `Part 1` document version carrying the definition, or the statement that it could not be obtained and why.

The definition version's static analysis results, including the analyses not performed and the class that made them impossible.

The whole event log in sequence order, with any gap marked.

Every activity instance, invocation attempt, branch attribution, join resolution, iteration and bound exhaustion.

Every determination reference with the `Part 2` report or `Part 5` envelope obtained where obtainable, or the statement that it was not.

Every compensation request, execution, outcome, residue and assignment.

Every timer observation with declared instant, observed instant, lateness and clock source.

Every correlation binding and every unmatched event bearing the instance's keys.

Every instance value with its kind, and the disposal demonstration result for the definition version.

Every intervention with actor, authorisation, reason and forced marking.

Every migration with its mapping, dispositions and post migration soundness assessment.

Every open and discharged review obligation.

The statement of the limits: that the execution is recoverable from the log and was not reproducible in the sense of the four prior parts; that a compensation recorded as full is an assertion and not an established restoration; and that no business fact is held here.

A statement of the version of this part the package claims to conform to.

**P6-8.27 (MUST) Package sufficiency.** An implementation must produce a package sufficient to account for the execution without the implementation running and without access to any component of this standard other than the package.

**P6-8.28 (MUST) Definition content included or its absence stated.** An implementation must include the content of the document version carrying the definition, or must state that it could not be obtained with the reason and the knowledge time of the attempt.

**P6-8.29 (MUST) Analyses included, including those not performed.** An implementation must include the static analysis results and must state which analyses were not performed and why.

**P6-8.30 (MUST) Interventions and forced outcomes included.** An implementation must include every intervention with its actor, authorisation and reason, and must carry the forced marking of every affected activity.

**P6-8.31 (MUST) Limit statements included.** An implementation must include the limit statements in every package.

**P6-8.32 (MUST) Absence stated, not omitted.** An implementation must state, for every required element it could not include, that it could not be included and why.

**P6-8.33 (MUST) Package digest.** An implementation must record a digest over a declared canonical form of the package and must include the profile identity.

**P6-8.34 (MUST) Self description.** An implementation must include a description of the package's structure sufficient for a reader with no knowledge of the implementation to locate each required element.

### 8.7 Retention

Retention here carries an obligation no other part has: this component must not govern the retention of anything it routed. Five prior parts have required it in those terms and clause P6-1.12 makes it binding.

**P6-8.35 (MUST) Retention obtained, not assigned.** An implementation must obtain the retention period of every record it holds from a retention rule expressed under `Part 1` and must not assign one of its own.

**P6-8.36 (MUST NOT) No retention authority over routed artifacts.** An implementation must not govern the retention of any document, verdict, determination, definition, decision or human task it routed, and must not permit the disposal of an instance to cause the disposal of any of them.

**P6-8.37 (MUST) Definitions outlive their instances.** An implementation must retain a definition version's whole structure for at least as long as the longest retained instance pinned to it, since an instance whose definition has been disposed of cannot be derived.

**P6-8.38 (MUST) Compensation records outlive the instance.** An implementation must retain every compensation outcome, residue and assignment for at least as long as the record of the act the compensation reversed or failed to reverse, where that period is known to it.

**P6-8.39 (MUST) Separate retention per structure.** An implementation must permit the retention of definitions, instance logs, invocation attempts and iterations to be set independently, since the last two exceed the first two by orders of magnitude.

**P6-8.40 (MUST NOT) No disposal under an open review obligation.** An implementation must not dispose of an instance carrying an open review obligation or an unassigned residue.

**P6-8.41 (MUST) Disposal recorded and citable.** An implementation must record the disposal of any record it holds with its authorisation reference and must make the disposal citable as a `Part 3` frontier of kind `RETENTION_EXPIRED`.

### 8.8 What cannot be changed

**P6-8.42 (MUST NOT) No amendment of an event.** An implementation must not modify any recorded event by any mechanism, including administrative, migration, correction and support mechanisms.

**P6-8.43 (MUST NOT) No state setting.** An implementation must not provide a means of setting a derived state directly, and must effect every change by an appended event produced by a declared operation, per clause P6-3.13.

**P6-8.44 (MUST NOT) No removal of a forced marking.** An implementation must not remove or suppress the marking of a forced outcome under any circumstance.

**P6-8.45 (MUST) Migration preserves the source segment.** An implementation must retain the events recorded before a migration unaltered and addressed in the source version's scheme, per clause P6-3.113.

**P6-8.46 (MUST) Migration preserves identity and digests.** An implementation that migrates its records to another store must preserve every instance identity, every event sequence and every recorded digest unchanged and must record the migration as an entry.

**P6-8.47 (MUST NOT) No bulk assignment on import.** An implementation must not assign a compensability, a join disposition, a bound, a determination kind or an instance value kind in bulk during an import, and must record every imported artifact lacking one as carrying the undeclared value.
## 9. Extension model

### 9.1 Closed sets, open sets, and why

Six sets in this part are closed.

**The split kind and join kind sets of section 3.6 are closed.** This is the strongest closure in the part. A join kind determines whether the construct waits, whether it may proceed without every branch, and whether its semantics are local. A registered join kind would be a construct whose synchronisation behaviour no consumer, analyser or operator could assume, and the analysis of section 6.7 depends on the kinds being enumerable.

**The instance value kind set of section 3.12 is closed.** It is the cheap enforcement of the spine, and a registry over it would be a mechanism for admitting business data one kind at a time.

**The compensation outcome set of section 3.10 is closed.** Six members and no more, because a seventh would be a seventh thing that could have happened to an undo and there are only six.

**The join disposition set of section 3.6 is closed.** Three things can be done with an unwaited branch.

**The instance outcome set of section 7.2 is closed.**

**The indeterminate branch handling set of section 3.13 is closed.** Four things can be done with a branch whose condition is unestablished.

Everything else is open under a registry: activity kinds, residue kinds, addressing schemes, correlation schemes, process classes, event types, refusal codes, digest algorithms, canonical form profiles and intervention kinds beyond those of section 4.4.

**P6-9.1 (MUST) Closed sets not extended.** An implementation must not add a member to the split kind, join kind, join disposition, instance value kind, compensation outcome, instance outcome or indeterminate handling sets.

**P6-9.2 (MUST) Unknown member is a defect, not a default.** An implementation must treat receipt of a member outside a closed set as a defect and must not map it to a member it does recognise.

**P6-9.3 (MUST) Open sets registered.** An implementation must admit a member of an open set only through the registry mechanics of section 9.2 and must not accept an unregistered member at any interface.

**P6-9.4 (MUST NOT) No control flow construct by registration.** An implementation must not register an activity kind whose effect is to introduce a split, a join, a loop or a cancellation not expressible in the closed sets of section 3.6 and section 3.8.

### 9.2 Registry mechanics

A registry is content of a controlled document version under `Part 1`, so a registration has an effective date, an approval and an author. Keys are permanent and never reused. A member is deprecated rather than removed. Every registration states what the member means, not only what it is called.

The retention obligation on these registries is long, because an instance pinned to a definition version from years ago references the registry versions in force then, and interpreting its events requires them. Clause P6-9.8 states it.

**P6-9.5 (MUST) Registry as controlled document.** An implementation must express every registry as content of a document version under `Part 1` and must resolve the registry version in force at the start of any instance that references it.

**P6-9.6 (MUST NOT) No key reuse.** An implementation must not reuse a registry key and must not remove a member that any retained event references.

**P6-9.7 (MUST) Deprecation rather than removal.** An implementation must deprecate a member with an effective date and a reason and must continue to interpret events referencing it.

**P6-9.8 (MUST) Registry version pinned to the instance.** An implementation must pin the version of every registry a definition version references at the start of every instance and must retain that registry version for at least as long as the instance.

**P6-9.9 (MUST) Semantics in the entry.** An implementation must not admit a registry entry that does not state the meaning of the member in terms a consumer can act on.

### 9.3 Activity kind registry

A registration states: what the kind does; which component it invokes, or that it invokes none; whether it may wait and on what; whether it may be compensable; whether it may appear within a cancellation region; whether it produces a determination and of which kind; and what its idempotence expectation is.

The determination field is where the closure of the split kinds is protected. An activity kind that produces a determination is an `EVALUATE` or a `DECIDE`, whose determination comes from `Part 2` or `Part 5`. A registration claiming to produce a determination from anywhere else would be an evaluation performed here, and clause P6-9.11 refuses it.

**P6-9.10 (MUST) Invocation target declared per kind.** An implementation must record which component an activity kind invokes, or that it invokes none, and must refuse an activity of a kind whose target is not the component it in fact invoked.

**P6-9.11 (MUST NOT) No determination from an unregistered source.** An implementation must not register an activity kind that produces a determination from any source other than `Part 2` or `Part 5`.

**P6-9.12 (MUST) Compensability admissibility declared.** An implementation must record whether a kind may be declared compensable and must refuse a compensability declaration inconsistent with the registration.

**P6-9.13 (MUST) Wait semantics declared.** An implementation must record whether a kind may wait and on what, and must refuse a wait on a condition the registration does not admit.

### 9.4 Addressing scheme registry

A position in a definition version must be addressable, and the addressing survives for as long as the longest instance pinned to that version.

A registration states the syntax, what a position denotes, and whether an address remains valid across changes to the definition. The last is the field that matters, because a migration mapping is written in terms of addresses in two versions and an unstable address makes the mapping ambiguous.

**P6-9.14 (MUST) Stability declared.** An implementation must declare, for every registered addressing scheme, whether an address remains valid across changes to a definition, and must record the scheme with every position reference.

**P6-9.15 (MUST) Stable schemes required for migration mappings.** An implementation must require both versions referenced by a migration mapping to use an addressing scheme declared stable and must refuse a mapping in a scheme that is not.

**P6-9.16 (MUST NOT) No cross scheme comparison.** An implementation must not compare, deduplicate or match positions recorded in different schemes.

### 9.5 Process class and correlation scheme registries

A process class registration states: what kind of process the class covers; which component owns it; whether its instances concern natural persons; the retention basis; and any class level requirement beyond this part's universal ones, such as a mandatory compensation model, a prohibited join disposition, a mandatory human activity or a maximum instance lifetime.

The class level requirements are the useful part, on the same basis as `Part 4` section 9.6 and `Part 5` section 9.5. A class covering processes that move money may be registered as prohibiting a join disposition of `COMPLETE_AND_DISCARD` and requiring every activity's compensability to be declared, which turns a governance expectation into a precondition the component enforces at definition recording.

A correlation scheme registration states how a key is formed, its uniqueness semantics, whether a key may be rebound after an instance terminates, and the retention period for unmatched events bearing keys of that scheme.

**P6-9.17 (MUST) Class requirements declared and enforced.** An implementation must record any class level requirement beyond this part's universal ones and must refuse a definition version that does not satisfy it.

**P6-9.18 (MUST) Maximum lifetime declared per class.** An implementation must record a maximum instance lifetime per process class, must report every instance exceeding it, and must not terminate one automatically.

**P6-9.19 (MUST) Owning component per class.** An implementation must record which component owns each class and must refuse a definition of a class from a component that does not own it.

**P6-9.20 (MUST) Correlation uniqueness semantics declared.** An implementation must record the uniqueness semantics of every correlation scheme and must enforce clause P6-3.78 against them.

**P6-9.21 (MUST) Rebinding after termination declared.** An implementation must record whether a scheme permits a key to be rebound after the instance holding it terminated, and must refuse a rebinding the scheme does not admit.

### 9.6 Residue kind registry

A registration states: what the residue is; whether it is quantifiable and in what units; whether it is reversible later and by what means; the expected assignment owner or role; and whether it requires notification of a party outside the organisation.

The last field is the one that earns the registry. A residue of kind `DATA_DISCLOSED` may carry a notification obligation to a supervisory authority or to the person whose data it was, and a residue of kind `EXTERNAL_FILING` may carry an obligation to correct a filing. Recording the obligation on the kind means it is raised by the residue rather than remembered by whoever handles it.

**P6-9.22 (MUST) Quantifiability and units declared.** An implementation must record whether a residue kind is quantifiable and in what units, and must record an extent on every residue of a quantifiable kind.

**P6-9.23 (MUST) Later reversibility declared.** An implementation must record whether a residue kind is reversible later and by what means, and must record the value on every residue.

**P6-9.24 (MUST) Expected owner declared.** An implementation must record the expected assignment owner or role for every residue kind and must report every residue assigned otherwise or unassigned.

**P6-9.25 (MUST) External notification obligation declared.** An implementation must record whether a residue kind carries an obligation to notify a party outside the organisation and must raise the obligation with the residue.

### 9.7 Digest, canonical form and code registries

**P6-9.26 (MUST) Both registered and both recorded.** An implementation must register digest algorithms and canonical form profiles separately and must record both with every digest.

**P6-9.27 (MUST) Deprecation without invalidation.** An implementation must be able to deprecate a digest algorithm without invalidating any recorded digest and must record an additional digest under a current algorithm rather than replacing the original.

**P6-9.28 (MUST) Refusal codes registered with remedy.** An implementation must state, in every refusal code registration, whether the operation may be retried and what must change.

**P6-9.29 (MUST) Event types registered.** An implementation must register every event type it emits beyond the minimum set of section 4.8.

**P6-9.30 (MUST) Intervention kinds registered.** An implementation must register every intervention kind beyond those of section 4.4 and must state its authorisation and reason requirements.

### 9.8 Composition of processes

Four compositions are distinguished and two are prohibited.

**A subprocess activity creating a child instance.** The only composition of processes this part provides. The child is a separate instance with its own log, its own pinned definition version and its own state, linked to the parent in both directions per clause P6-3.99. The parent's activity waits on the child's completion where declared synchronous, or does not where declared asynchronous.

**A signal correlated between instances.** Permitted. One instance emits a signal, another correlates it. This is the only cross instance communication and it is mediated entirely by correlation keys, so an instance never reads another's state.

**A process definition including another definition by reference.** Permitted only by pinned version, on the same basis `Part 2` clause P2-9.32 gives for rule sets and `Part 4` clause P4-9.33 gives for models: inclusion by lineage would make the including definition's content change without the including definition changing.

**An instance reading another instance's state.** Prohibited by clause P6-3.100. The remedy is the signal.

**A parent compensating a child's completed scopes directly.** Prohibited. A parent may request compensation of a child instance, which the child performs against its own scopes and reports; it may not reach into the child's scopes. The reason is that the child's compensation order, handlers and residue enumeration are properties of the child's definition, and a parent performing them applies the wrong ones.

**P6-9.31 (MUST) Subprocess as a separate instance.** An implementation must execute a subprocess activity as a separate instance with its own log and pinned definition version and must link it to the parent in both directions.

**P6-9.32 (MUST) Synchronisation declared on subprocess activities.** An implementation must record whether a subprocess activity waits on its child's completion and must record the disposition of an unfinished child where it does not.

**P6-9.33 (MUST) Definition inclusion by pinned version only.** An implementation must permit a definition version to include another only by pinned version and must not permit inclusion by lineage.

**P6-9.34 (MUST NOT) No cyclic inclusion or instantiation.** An implementation must refuse a definition version whose inclusion graph contains a cycle and must declare and enforce a maximum depth of subprocess instantiation.

**P6-9.35 (MUST NOT) No cross instance state read.** An implementation must not permit an instance to read another instance's values, state or events, and must mediate every cross instance interaction by a correlated signal.

**P6-9.36 (MUST) Child compensation requested, not performed.** An implementation must request compensation of a child instance from the child and must not compensate a child's scopes from the parent.

**P6-9.37 (MUST) Composition depth declared.** An implementation must declare the maximum depth of subprocess instantiation and definition inclusion it accepts and must refuse anything exceeding it.
## 10. Standards and specifications

### 10.1 How the citations in this part are to be read

Every entry states what the source supplies, the edition established as current at the date of this part, and whether this part's account rests on specification text or on secondary sources. Section 13.1 lists the sources not obtained.

This part is unusual in the standard so far. Its subject matter is the best studied in the whole of the standard: control flow patterns have been catalogued for a quarter of a century, compensation has a normative specification, and correctness has a formal definition with a decision procedure. The author's task here was less to invent and more to take precise positions among well specified alternatives and to name what the specifications get wrong.

Three findings shape the section. The de facto standard for process modelling has had no major revision in fifteen years and its hardest construct is acknowledged in its own text to require global information. The normative specification for compensation has a documented anomaly in its default ordering, and two accounts of that ordering are in circulation. And the formal correctness property most worth having becomes undecidable exactly when cancellation is modelled, which is to say in almost every real process.

**P6-10.1 (MUST) Cited edition recorded.** An implementation must record the edition or version of every external standard it relies upon and must not cite a standard without its edition.

**P6-10.2 (MUST) Basis marked.** An implementation must record, for every control it adopts from a source named in this section, whether the basis is specification text or practice.

### 10.2 Process modelling: BPMN

| Standard | Status established | Supplies |
| --- | --- | --- |
| BPMN 2.0.2 | The current OMG version. BPMN 2.0 was published January 2011; 2.0.2 is the maintenance release, the OMG formal document being dated December 2013. No major revision has been published since 2011. Issues continue to be reported against 2.0.2 in the OMG issue tracker as recently as 2024, so the specification is maintained without a new version. | A metamodel, an XML interchange format, diagram interchange, and an execution semantics expressed in terms of tokens. Gateways: exclusive, inclusive, parallel, complex and event based. Activities, subprocesses, events, boundary events. Section 13 of the specification is the execution semantics and contains a list of elements described as non operational. |
| ISO/IEC 19510:2013 | Published as an International Standard through the Publicly Available Specification route. | The same content as the OMG specification, with introductory material. |

**A discrepancy that could not be resolved.** The ISO/IEC 19510 introductory material states that the standard is identical with the OMG specification for BPMN **version 2.0.1**. The OMG's own specification page states that version **2.0.2** was formally published by ISO as the 2013 edition. The two statements cannot both be right, and the consequence for a reader is practical: a citation to ISO/IEC 19510 does not unambiguously identify which BPMN maintenance release is being cited. Section 13.1 records the discrepancy and clause P6-10.3 requires an implementation citing either to state which document it read.

Two properties of BPMN bear directly on this part's design and both are adopted as problems rather than as models.

**The inclusive gateway requires global information.** The specification's own account of the inclusive gateway's join behaviour requires knowledge of the state of the whole model, which is a non local semantics. The literature has repeatedly noted that the specification's execution semantics are given in natural language descriptions that in places contain misleading information, and multiple published formalisations of the inclusive gateway do not agree in every case. Section 3.7 restricts the construct on this basis and section 13.3 records the cost.

**The exclusive gateway is order dependent.** It evaluates the conditions on its outgoing flows in a defined order and takes the first that is true, with a default flow where none is. Where the conditions are not mutually exclusive, that is selection among branches by the order in which they are declared, which `Part 5` clause P5-3.59 refuses. Section 3.6 therefore requires mutual exclusivity as an integrity constraint and requires a non exclusive selection to be a `Part 5` decision. Section 10.5 records the divergence.

The account of BPMN in this part rests on the OMG version inventory and issue tracker, obtained directly, and on the ISO front matter and secondary literature for the semantics. The specification text was not obtained, and section 13.1 records that the claims about the two gateways are therefore unverified against the source.

**P6-10.3 (MUST) BPMN document identified precisely.** An implementation citing BPMN or ISO/IEC 19510 must state which document and which maintenance release it read, given the discrepancy this section records.

### 10.3 Compensation: WS-BPEL

| Standard | Status established | Supplies |
| --- | --- | --- |
| WS-BPEL 2.0 | OASIS Standard, 2007. | Scopes as the unit to which handlers attach. Section 12 of the specification covers scopes, with 12.4 compensation handlers, 12.5 fault handlers, 12.6 termination handlers, 12.7 event handlers and 12.8 isolated scopes. The `compensate` and `compensateScope` activities. Snapshot semantics, in which a compensation handler sees the state as at the completion of its scope. |

Four rules of the WS-BPEL model are adopted in section 3.9 and each is stated there as a clause.

Compensation is enabled only for a scope that completed successfully, and a scope whose fault handler was invoked is never considered to have completed successfully, so compensation is never enabled for it.

Default compensation executes the handlers of enclosed scopes in reverse order of completion.

The `compensate` and `compensateScope` activities may be used only within a fault handler, a compensation handler or a termination handler.

A compensation handler sees the state as at the completion of its scope.

**The ordering anomaly, named rather than inherited.** Two accounts of the default order are in circulation and they differ. The specification text describes reverse order of completion. The specification's own issue resolution settled on the weaker rule that the default order need only respect the control dependencies that are explicitly modelled. And the published literature has identified anomalies in the mechanism, in particular that the compensation order can violate control link dependencies where control links cross scope boundaries between nested non isolated scopes, with proposals to remove the anomalies by eliminating default and termination handlers altogether.

This part does not resolve the anomaly. It requires the order to be one of three declared kinds and requires the declaration, per clause P6-3.58, so that no implementation is left to choose between two accounts and no reader has to guess which was chosen.

**One divergence.** WS-BPEL confines compensation to error paths. This part admits an activity of kind `COMPENSATE` in normal flow, per clause P6-3.59, on condition that the request records the determination that authorised it. The reason is that a business initiated reversal, where nothing failed and somebody decided to undo, is real and common, and WS-BPEL's own scope statement contemplates a partner requesting reversal. Section 10.5 records it.

**What WS-BPEL does not supply, and this part's principal contribution.** Nothing in the specification distinguishes a compensation that completed from a compensation that restored the position. A compensation handler either completes or faults, and a fault is handled by the enclosing scope. So a compensating act that completed perfectly and restored nothing, because the payment had cleared or the notice had been read, is recorded as a successful compensation. Section 3.10's six member outcome taxonomy and its residue model have no source in this specification or in any other reviewed here, and section 10.9 records them as unsourced.

The account rests on the specification's table of contents and section headings, on its published issue list and on secondary literature. The clause text was not obtained.

### 10.4 Correctness: workflow nets and soundness

These are literature rather than standards and section 6.7 depends on them directly.

| Source | Supplies |
| --- | --- |
| The workflow net formalism | A Petri net with a distinguished source place and sink place, activities as transitions and their partial ordering as places. |
| The soundness property | Three conditions: **option to complete**, being that from every reachable state the state marking only the sink is reachable; **proper completion**, being that when the sink is marked every other place is empty; and **no dead transitions**, being that every activity can be enabled from some reachable state. The property guarantees the absence of deadlocks, livelocks and other anomalies detectable without domain knowledge. |
| The short circuit result | Classical soundness of a workflow net corresponds to liveness and boundedness of the net obtained by connecting the sink back to the source, which is what makes standard Petri net tooling applicable. |
| Decidability results | Soundness is decidable, and for free choice nets it is decidable in polynomial time; results extend to an almost free choice class. |
| Undecidability under reset arcs | Soundness is **undecidable** for workflow nets with reset arcs, which are how cancellation is modelled, and undecidable for the weaker relaxed notions as well. |
| The control flow pattern catalogue | The taxonomy of splits, joins, multiple instance behaviours, cancellation and arbitrary cycles from which section 3.6's join kinds and section 3.8's repetition forms are drawn. |

The undecidability result is the one that shapes the part. **Declaring a cancellation region moves a process definition out of the class in which its correctness can be established at all.** That is not a limitation of an implementation; it is a mathematical fact about the formalism, and an engine that reports a cancelling process as sound has reported a finding it cannot have made. Clause P6-6.38 requires the honest report and section 3.6's restriction of the inclusive join to structured regions exists partly to keep more definitions inside the decidable class.

The account of each rests on the published literature as generally understood. No primary source was obtained and no edition is cited, and section 13.1 records it.

### 10.5 Named conflicts

Five conflicts bear on this part. None is resolved by averaging.

**Whether termination may be implicit.** BPMN and most engines permit a process to end when no tokens remain. **Position taken.** Termination must be explicit, per clause P6-3.18, and an instance with no runnable work that reached no end position is `STALLED`, per section 5.2. The reason is that implicit termination makes a deadlock indistinguishable from a completion, and the population of instances that quietly stopped is then invisible. This is the largest divergence in the part.

**Whether the inclusive join is admissible in general.** BPMN provides it and acknowledges that its semantics require global information. **Position taken.** Admitted only within a block structured region with no cancellation and no arbitrary cycle, per section 3.7, so that the set of arriving flows is a recorded set rather than a predicted one. Section 13.3 records the cost.

**Whether branch order may select.** BPMN's exclusive gateway takes the first true condition in a defined order. **Position taken.** Conditions must be mutually exclusive, and a non exclusive selection is a `Part 5` decision, per clauses P6-3.32 and P6-3.33. This follows `Part 5` clause P5-3.59 rather than BPMN.

**Where compensation may be initiated.** WS-BPEL confines it to error paths. **Position taken.** Admitted in normal flow with a recorded determination, per clause P6-3.59, because a business initiated reversal is real and the specification's own scope contemplates it.

**What the default compensation order is.** Two accounts are in circulation, reverse order of completion and dependency respecting order, and the literature has identified anomalies where control links cross scope boundaries. **Position taken.** Neither is adopted as an implicit default. The order is one of three declared kinds and the declaration is required, per clause P6-3.58, with reverse completion as the default value where the author declares nothing.

### 10.6 Adjacent standards deliberately not used

| Standard | Why not used here |
| --- | --- |
| CMMN | Case management, with sentries, stages, milestones and discretionary items. The case is `Part 8`'s and adopting CMMN here would put case state in two components. Not obtained and not assessed. |
| SCXML | State chart notation. Relevant to the derived state machines of section 5 and not adopted, because this part specifies states and transitions rather than a notation for them. Not obtained. |
| XPDL | A process definition interchange format. Interchange is out of scope. |
| ISO/IEC 15909 | High level Petri nets. Relevant to the formalism of section 6.7 and cited only through the workflow net literature. Currency not established. |
| Distributed transaction standards for two phase commit | An alternative to compensation that requires resources to hold locks across a long running process, which a process spanning days or years cannot do. Cited as the reason compensation exists rather than as a mechanism used here. |

### 10.7 Supporting specifications

| Specification | Used for |
| --- | --- |
| RFC 2119 and RFC 8174 | Requirement keywords. |
| BCP 47 | Language tags. |
| RFC 3339 and ISO 8601 | Instant representation for the three clocks and for observed elapses. |
| RFC 8785 | An example of a canonical form profile of the kind section 9.7 requires. |
| RFC 9457 | A model for conveying a refusal of the kind section 7.6 specifies. |
| CloudEvents | A model for the event envelope of section 4.8. |

The following clauses rest on practice rather than specification text and are collected so a reader can see the set: clause P6-3.9 on the periodic disposal demonstration; clause P6-3.19 on a declared stall detection interval; clause P6-3.38 on recording unwaited work; clause P6-3.47 on authorising and justifying a bound; clause P6-3.75 on recording timer lateness; clause P6-3.103 on deriving the idempotence key from the activity instance; clause P6-4.21 on the permanence of a forced outcome marking; clause P6-8.14 on periodic replay sampling; and clause P6-9.25 on residue notification obligations.

**P6-10.4 (MUST) Practice basis recorded.** An implementation that adopts a clause listed in the paragraph above as a control must record that its basis is practice.

### 10.8 What none of the standards supplies

Twelve requirements in this part have no source in any reviewed standard.

The disposability requirement itself: that the process instance hold no business fact, and that the position be demonstrated periodically rather than asserted. No reviewed standard addresses what a process instance may contain.

The closed instance value kind set, and the treatment of an opaque transit value as a countable, lifetime bounded exception.

The requirement that every conditional branch be attributable to an external determination, and that the whole determination envelope be pinned rather than its result recorded.

The declared handling of a branch whose determination is indeterminate, with suspension as the default.

The stall as a distinct state, detected within a declared interval and reported.

The declared disposition of branches a partial join did not wait for, and the requirement that their work be recorded whether or not it was consumed.

The compensation outcome taxonomy of section 3.10, and in particular the members for partial, impossible and failed compensation, and the requirement that a full compensation be recorded as an assertion.

The residue model: its enumeration, its registered kinds, its assignment to an owner and the counting of unassigned residue.

The separation of an invocation attempt from an activity outcome, and the `OUTCOME_UNKNOWN` state.

The permanent marking of a forced outcome, and the prohibition on its removal.

Version pinning of a running instance with migration only under a governed, exhaustive, soundness assessed mapping.

The review obligation as a recorded fact distinct from a task.

**P6-10.5 (MUST) Unsourced requirements identified.** An implementation must be able to state, for any control it implements under this part, whether the requirement has a cited source in this section or is listed in section 10.8 as unsourced.
## 11. Anti patterns

Each entry names the mechanism by which the failure occurs, states the consequence, and marks whether the prohibition rests on specification text or on practice.

### 11.1 The process instance that became the database

**Mechanism.** An activity needs a value another component owns. Fetching it is a call; the call is slow or the component is unavailable; the value is already in the message that started the instance. So it goes in a variable. Three activities and a gateway then read the variable.

**Consequence.** The owning component's copy is corrected and the instance's is not, because nothing knows the copy exists. Reports get built from the instances because that is where the data is convenient. Within two years the process definition is the only documentation of what the value meant. Five prior parts each required their own state to survive the disposal of every instance, and this is the mechanism by which that requirement is quietly abandoned.

**Basis.** Specification text, in `Part 1` clause P1-12.11, `Part 2` clause P2-12.15, `Part 3` clause P3-12.15, `Part 4` clause P4-12.15 and `Part 5` clause P5-12.19.

**P6-11.1 (MUST NOT) No business fact as a variable.** An implementation must hold every instance value as one of the declared kinds of section 3.12, must hold references rather than copies, and must demonstrate disposability periodically, per clauses P6-3.8 and P6-3.9.

### 11.2 Implicit termination

**Mechanism.** The instance ends when no tokens remain. The rule is simple, it is what BPMN permits, and it is what almost every engine implements.

**Consequence.** A deadlocked instance, an instance whose only token was consumed by a defect, and an instance that ran to completion are the same state. The first two are reported as the third. In an estate of any size the population of instances that stopped for unknown reasons is invisible and grows monotonically, and it is discovered when somebody asks about a case from eighteen months ago and finds it marked complete with nothing having happened.

**Basis.** Practice, and a divergence from BPMN recorded in section 10.5.

**P6-11.2 (MUST NOT) No implicit termination.** An implementation must require an explicit end position and must record an instance with no runnable work that reached none as `STALLED`, per clauses P6-3.18 and P6-5.8.

### 11.3 The gateway that evaluates

**Mechanism.** A gateway carries an expression. The engine evaluates it and routes. It is the most natural thing in the world to write and it is how every engine is used.

**Consequence.** The condition is a rule with no identity, no statement, no authority, no enforcement level and no verdict record. Its three valued outcome is gone, so an unevaluable condition becomes a false one and the instance takes the other branch silently. `Part 2` exists to prevent exactly this and its section 12.6 names it from the other side.

**Basis.** Specification text, in `Part 2` section 12.6.

**P6-11.3 (MUST NOT) No condition evaluation.** An implementation must obtain every conditional branch from a `Part 2` report or a `Part 5` decision, must pin the whole envelope, and must not evaluate a condition itself, per clauses P6-1.4 and P6-6.13.

### 11.4 The first matching branch

**Mechanism.** A gateway has three outgoing flows with overlapping conditions and takes the first that is true, in the order the flows were drawn.

**Consequence.** Somebody adds a branch above another for readability and the organisation's routing changes. The change has no author, no approval and no record, because moving a connector is not a policy act in anybody's process. `Part 5` refused this construct in its own domain for precisely this reason and section 3.6 refuses it here.

**Basis.** Specification text, in `Part 5` clause P5-3.59, and a divergence from BPMN recorded in section 10.5.

**P6-11.4 (MUST) Exclusivity or a decision.** An implementation must require the conditions on an exclusive split to be mutually exclusive and must express a non exclusive selection as a `Part 5` decision, per clauses P6-3.32 and P6-3.33.

### 11.5 The inclusive join with a timeout

**Mechanism.** The inclusive join's semantics are hard, so the implementation waits for a configured interval and proceeds with whatever arrived.

**Consequence.** The construct's behaviour is a function of load. Under normal conditions every branch arrives and the join looks like a synchronising join; under load a branch is late and the join proceeds without it, silently. The instance then completes having skipped work, and nothing distinguishes that run from a correct one. The timeout is also invisible in the definition, so a reader cannot tell that the join is approximate.

**Basis.** Practice.

**P6-11.5 (MUST NOT) No approximated inclusive join.** An implementation must not implement an inclusive join by a timeout, a heuristic or an iteration limit, and must restrict the construct to structured regions, per clauses P6-3.45 and P6-3.41.

### 11.6 The discarded branch nobody counted

**Mechanism.** A discriminator proceeds on the first of three parallel branches. The other two complete in their own time and their outcomes are dropped, because nothing is waiting for them.

**Consequence.** Two of three suppliers were asked for a quote, produced one, and were charged for by nobody's reckoning; two of three services were invoked and their side effects stand. The work was performed and no record connects it to the join that ignored it. Where the branches were not idempotent, the effects may need compensating and nothing knows they exist.

**Basis.** Practice.

**P6-11.6 (MUST) Disposition declared and unwaited work recorded.** An implementation must declare a disposition on every partial join and discriminator and must record the activity instances and outcomes of every branch it did not wait for, per clauses P6-3.37 and P6-3.38.

### 11.7 The unbounded collection

**Mechanism.** A multiple instance activity iterates a collection whose size is read at run time. In testing the collection has three members.

**Consequence.** In production a defect upstream produces a collection of three hundred thousand, and the engine faithfully creates three hundred thousand activity instances, each invoking something. This is the most effective mechanism available for one upstream defect to consume an estate, and the engine is behaving exactly as specified.

**Basis.** Practice.

**P6-11.7 (MUST NOT) No unbounded dynamic instantiation.** An implementation must record the provenance of every instance count and must refuse a dynamic multiple instance activity with no declared bound, per clauses P6-3.48 and P6-3.49.

### 11.8 The loop compensated once

**Mechanism.** A scope contains a repetition that ran forty times. The scope is compensated. The compensation handler runs once.

**Consequence.** Thirty nine iterations' effects stand and the scope is recorded as compensated. Nobody notices, because the handler completed and the outcome taxonomy in an ordinary engine has no member for what actually happened.

**Basis.** Practice.

**P6-11.8 (MUST) Per iteration compensation in reverse order.** An implementation must compensate each completed iteration separately, in reverse order of completion unless another order is declared, per clauses P6-3.51 and P6-3.52.

### 11.9 The compensation that pretended

**Mechanism.** A scope's compensation handler runs. Its activities complete. The scope is recorded as compensated.

**Consequence.** The payment cleared before the reversal was submitted and the reversal was rejected. The notice was read before the correction was sent. The filing stands on the regulator's record. In every case the handler completed and the effect remains, and no field in the record can say so. This is the failure the whole of section 3.10 exists for and it is the one an organisation discovers during an incident, years after the process was signed off.

**Basis.** Practice. No reviewed standard distinguishes a compensation that completed from one that restored the position; see section 10.3.

**P6-11.9 (MUST) Compensation outcome recorded, not inferred.** An implementation must record one of the six outcome members, must obtain the outcome from the performing component or a named actor, and must enumerate residue where the outcome requires it, per clauses P6-3.64, P6-3.65 and P6-3.72.

### 11.10 The irreversible act in a compensable scope

**Mechanism.** A scope has a compensation handler. One activity inside it instructs a payment. Nobody records that the payment cannot be undone, because the field for recording it does not exist.

**Consequence.** The scope is designed as though it can be unwound and it cannot. The condition is discoverable at design time by inspection and is discovered at run time by an incident. This is the same class of failure as `Part 4`'s semantic drift: nothing fails, and the record asserts something that was never true.

**Basis.** Practice.

**P6-11.10 (MUST) Compensability declared and the condition reported.** An implementation must require a compensability declaration on every activity and must report every irreversible activity within a scope carrying a compensation handler, per clauses P6-3.23 and section 8.5.

### 11.11 The residue nobody owns

**Mechanism.** A compensation is partial. The residue is described in a comment on the incident ticket. The ticket is closed.

**Consequence.** Money that moved, a notice that was read, a filing that stands, and no record connects any of it to an owner. The organisation's exposure is the sum of every partial compensation it has ever performed and the sum is not computable.

**Basis.** Practice.

**P6-11.11 (MUST) Residue enumerated and assigned.** An implementation must enumerate every residue, record its kind and extent, assign it to an owner with an authorisation, and count the unassigned, per clauses P6-3.65, P6-3.69 and P6-3.70.

### 11.12 The retry that ran twice

**Mechanism.** An invocation times out. The engine retries. It does not record the first attempt, because the first attempt did not produce an outcome.

**Consequence.** The first invocation may have completed. Where the activity is not idempotent the effect happened twice, and the record shows one activity that completed on its first and only attempt. The reconciliation two weeks later finds a duplicate and nothing in the process record explains it.

**Basis.** Practice.

**P6-11.12 (MUST) Attempts recorded separately, unknown outcomes preserved.** An implementation must record every invocation attempt as its own entity, must record an attempt with no response as having an unknown outcome, and must not retry a non idempotent activity from that state without a declared policy, per clauses P6-3.101, P6-3.106 and P6-5.15.

### 11.13 Exactly once

**Mechanism.** The engine's documentation states that it invokes each activity exactly once.

**Consequence.** The claim cannot be kept, because the failure between an invocation and the recording of its outcome is indistinguishable from the failure before the invocation. Consumers build on the claim and omit their own deduplication, and the duplicate arrives during the incident when it is least welcome.

**Basis.** Practice.

**P6-11.13 (MUST NOT) No exactly once claim.** An implementation must declare the semantics it provides, must supply an idempotence key derived from the activity instance, and must state the deduplication the receiver is required to perform, per clauses P6-3.103 and P6-3.105.

### 11.14 The state edited to unstick the instance

**Mechanism.** An instance is stuck. An operator sets the state, moves the token or writes the outcome directly in the store. The instance proceeds. It takes ninety seconds and it works.

**Consequence.** The execution record is no longer an account of what happened, and the edits are concentrated precisely in the instances an investigation will ask about. There is no record of who did it, why, or what the state was before.

**Basis.** Practice.

**P6-11.14 (MUST) Intervention is an authorised event.** An implementation must effect every change by an appended event, must require an authorisation and a reason on every intervention, and must not provide a means of setting a derived state, per clauses P6-3.13, P6-3.14 and P6-4.19.

### 11.15 The forced outcome that looks like a result

**Mechanism.** An operator supplies an activity's outcome to release an instance. The outcome is recorded in the same field a real outcome would occupy.

**Consequence.** Every consumer downstream treats an operator's assertion as the invoked component's result. A report of completed activities includes activities nobody performed. The marking that would distinguish them either does not exist or is removed when the incident is closed.

**Basis.** Practice.

**P6-11.15 (MUST) Forced outcomes marked permanently.** An implementation must record a forced outcome as `OUTCOME_FORCED`, must carry the marking into every projection and export, and must not permit its removal, per clauses P6-4.21 and P6-8.44.

### 11.16 The token moved into a dead end

**Mechanism.** An operator moves a token past a problem to a position that looks right.

**Consequence.** The position is one from which the definition cannot complete. The instance runs a few activities and stalls, or completes having skipped a scope whose compensation is now unreachable. This is the most dangerous intervention available and it is the one performed under the most pressure.

**Basis.** Practice.

**P6-11.16 (MUST) Token move assessed for soundness.** An implementation must record a soundness assessment of the state a token move produces and must refuse a move whose assessment established the instance cannot then complete, per clause P6-4.20.

### 11.17 The definition redeployed under running instances

**Mechanism.** A defect is corrected and the definition is redeployed. Running instances pick up the new version at their next step, because that is the simplest deployment model.

**Consequence.** An instance runs half under one definition and half under another, with no record of the join. A token sits at a position the new version deleted and the engine's behaviour is undefined. The activities already executed were the old version's and the compensation handlers that would unwind them are the new version's, which may not correspond.

**Basis.** Practice.

**P6-11.17 (MUST) Instances pinned; migration governed.** An implementation must pin every instance to its start version, must migrate only under an approved, exhaustive, soundness assessed mapping, and must not migrate as a side effect of deployment, per clauses P6-3.108, P6-3.109 and P6-3.115.

### 11.18 The old version withdrawn under a population

**Mechanism.** A definition version is superseded and removed, because the new one is deployed and nobody starts instances on the old one.

**Consequence.** Two hundred instances are still running under it. Their pinned version is gone, so their state cannot be derived, their activities cannot be resolved and their compensation handlers cannot be found. They are unrecoverable and were healthy an hour earlier.

**Basis.** Practice.

**P6-11.18 (MUST) Withdrawal reports its population and definitions outlive instances.** An implementation must report every running instance at the moment a version is withdrawn from starting, must require a declared disposition, and must retain a definition version for at least as long as the longest instance pinned to it, per clauses P6-4.9 and P6-8.37.

### 11.19 The process history registered as a basis

**Mechanism.** A determination is made at the end of a nine step process. Its basis is registered with `Part 3` as the nine steps.

**Consequence.** None of the nine is an authority, a premise or a method. The basis is voluminous and reconstructs nothing, and the actual authority, the rule that was evaluated and the criterion that was applied are absent. `Part 3` section 12.6 names this from the other side.

**Basis.** Specification text, in `Part 3` clause P3-12.14.

**P6-11.19 (MUST) Steps are trail acts, not citations.** An implementation must register a process step as a `Part 3` subject act and must not register one as a citation in a basis, per section 12.3.

### 11.20 The undecidable outcome that became a branch

**Mechanism.** A `Part 5` decision returns an undecidable outcome. The gateway has a branch for it. The instance routes to manual review and proceeds.

**Consequence.** The organisation has process instances that went to manual review and no count of decisions its criterion could not determine, because the outcome was consumed as a branch rather than recorded as an outcome. `Part 5` section 12.6 names this and its clause P5-12.21 requires the outcome to be recorded before the referral.

**Basis.** Specification text, in `Part 5` clause P5-12.21.

**P6-11.20 (MUST) Outcome recorded before referral.** An implementation must confirm that an indeterminate verdict or undecidable decision was recorded by its owning component before raising a referral, per clause P6-3.91.

### 11.21 The timer read at replay

**Mechanism.** The process computes whether a deadline has passed by comparing a stored date with the current time. On replay it computes again.

**Consequence.** The replay takes a different path from the original execution, so the record cannot be used to explain what happened. The divergence is silent and grows with the age of the instance.

**Basis.** Practice.

**P6-11.21 (MUST) Observed time recorded and read.** An implementation must record every timer elapse as an appended observation and must read the recorded observation on replay rather than evaluating a clock, per clauses P6-3.74 and P6-6.3.

### 11.22 The unmatched event discarded

**Mechanism.** An inbound event arrives with a correlation key bound to no instance. There is nothing to deliver it to, so it is logged and dropped.

**Consequence.** A message arrived for an instance that had not started, had already terminated, or was suspended. The work it represented is lost and the sender believes it was delivered. The population of such events is the measure of a race condition nobody has diagnosed.

**Basis.** Practice.

**P6-11.22 (MUST) Unmatched events recorded and retained.** An implementation must record every uncorrelated inbound event with its key and the reason, must retain it for a declared period, and must report the population, per clause P6-3.77.

### 11.23 The human task owned twice

**Mechanism.** The engine needs to know whether a human activity is done, so it holds the work item's state: offered, allocated, in progress, complete. `Part 8` holds it too.

**Consequence.** Two components hold the same lifecycle and they diverge, most reliably when a task is reassigned or escalated, which is exactly when somebody is watching. The engine's copy is the one the process routes on, so the process proceeds on a state that is not the work item's state.

**Basis.** Specification text, in section 12.8.

**P6-11.23 (MUST NOT) No work item state.** An implementation must hold only the activity's state in the flow, must obtain the work item's lifecycle from `Part 8`, and must not hold offering, allocation, delegation or escalation state, per clause P6-5.19.

### 11.24 The cancellation region that made the process unanalysable

**Mechanism.** A cancellation region is added so that a cancel event can terminate a set of activities cleanly. It is the right modelling construct and it is used freely.

**Consequence.** The definition leaves the class in which soundness is decidable. The analysis reports nothing and the report is read as a clean bill. This is not a defect in the construct or the implementation; it is a mathematical consequence, and the only remedy is to say so.

**Basis.** Literature, in the undecidability of soundness for workflow nets with reset arcs.

**P6-11.24 (MUST) Undecidability declared, not reported as soundness.** An implementation must record, for every definition containing a cancellation region, that soundness cannot be established, and must not report the absence of a finding as soundness, per clauses P6-6.38 and P6-6.40.

### 11.25 The retention that took its neighbours with it

**Mechanism.** Process instances are purged after ninety days, which is a sensible operational retention. The purge cascades to the records the instances reference, because a foreign key relationship exists.

**Consequence.** Verdicts, determinations and approvals whose retention was governed by their own components are disposed of on the orchestrator's schedule. Five prior parts required that this not happen and this is the mechanism by which a well intentioned housekeeping job does it.

**Basis.** Specification text, in the reciprocal every prior part requires.

**P6-11.25 (MUST NOT) No retention authority over routed artifacts.** An implementation must not govern the retention of anything it routed and must not permit the disposal of an instance to cause the disposal of any of them, per clauses P6-1.12 and P6-8.36.

### 11.26 The process that is the integration layer

**Mechanism.** The engine already invokes things, so it acquires transformation, content based routing and enrichment. Each is a small step and each is convenient.

**Consequence.** Transformation is a derivation whose lineage belongs to `Part 4` and whose instances belong to `Part 3`, and it now happens in an engine that records neither. Content based routing is a decision with no criterion. Enrichment is a copy of a fact, which is section 11.1 again. The engine becomes the place where the estate's business logic lives with none of the artifacts that make logic reviewable.

**Basis.** Practice.

**P6-11.26 (MUST NOT) No transformation, enrichment or content routing.** An implementation must not transform, enrich or route by the content of anything it carries, must route only on determinations obtained from `Part 2` and `Part 5`, and must not read an `OPAQUE_TRANSIT` value, per clauses P6-1.4, P6-3.84 and P6-6.15.
## 12. Boundaries with other parts

Each subsection states four things: what this component delegates, what it must not absorb, the naive design that conflates the two, and the reciprocal declaration the other part must make. Subsection numbers correspond to part numbers, so section 12.7 states the boundary with `Part 7` and section 12.14 states the boundary with `Part 0`. Section 12.6 is deliberately unused, since it would designate this part. Numbers are permanent.

Five of this part's boundaries discharge reciprocal declarations already committed by the parts on the other side, and all five say substantially the same thing in five vocabularies: this component owns no state of theirs and their records survive its disposal. Sections 12.1 through 12.5 discharge them.

**P6-12.1 (MUST) Declared allocation.** An implementation must be able to state, for every capability named in this section as delegated, which component provides it, and must not provide it within this component.

**P6-12.2 (MUST) Refusal rather than substitution.** Where a delegated capability is unavailable, an implementation must take the behaviour of section 4.7 and must not substitute a local implementation of it.

**P6-12.3 (MUST NOT) No reaching past a neighbour.** An implementation must not read or write the internal state of another component named in this section and must interact with it only through that component's declared interface.

### 12.1 Boundary with Part 1, controlled documents and records

This subsection is the reciprocal declaration `Part 1` section 12.6 requires.

**Delegated.** Document and record identity, version identity, status, effectivity, supersession, approval, signature and retention. The controlled documents that carry every process definition version, every migration mapping and every registry of this part. The retention rules governing this component's own records.

**Must not absorb.** Document status. A document's status is not a position in a process and does not cease to exist when no process is running.

**Naive conflation.** The workflow instance owns document status, so a document's state exists only as a position in a flow, per `Part 1` section 11.15. The document then has no state between processes, and reconstructing its history means reading process instances designed to be transient.

**Reciprocal.** This part declares that it does not own document status, version identity or effectivity, that it invokes the recording operations of `Part 1` section 4.2, and that its own retention does not govern the retention of the documents it routed. Clauses P6-12.4 through P6-12.6 make it binding.

**P6-12.4 (MUST NOT) No document state held.** An implementation must not hold, cache beyond a declared validity period, or assert the status, version identity or effectivity of any document or record, and must obtain each by resolution against `Part 1`.

**P6-12.5 (MUST) Status changed by invocation, not by advance.** An implementation must effect every change to a document's status by invoking a `Part 1` recording operation and must not treat the advance of a token as effecting one.

**P6-12.6 (MUST NOT) No process identity required of Part 1.** An implementation must not require `Part 1` to record, read or reason about a process instance identifier, consistently with clause P1-12.12.

### 12.2 Boundary with Part 2, business rules and constraint evaluation

This subsection is the reciprocal declaration `Part 2` section 12.6 requires.

**Delegated.** Every constraint evaluation. Whether a condition holds, whether a rule applies, whether a rule could be evaluated, and the whole verdict taxonomy including the vacuity flag and the five indeterminacy subclasses.

**Must not absorb.** Evaluation. A gateway condition is a report obtained beforehand and cited.

**Naive conflation.** The evaluation becomes a workflow step whose output drives a gateway and the verdict is not recorded except as the branch taken. The organisation then has process instances rather than verdicts, per `Part 2` section 12.6.

**Reciprocal.** This part declares that it does not own verdicts, that it records the evaluation report reference rather than the branch taken, and that its own retention does not govern the retention of the verdicts it consumed. Clauses P6-12.7 through P6-12.9 make it binding.

**P6-12.7 (MUST) Report referenced, not the branch.** An implementation must record, for every branch attributed to an evaluation, the whole report by pin, and must not record only which branch was taken or the truth value that determined it.

**P6-12.8 (MUST NOT) No condition evaluation.** An implementation must not evaluate a constraint and must restrict the tests it performs itself to those clause P6-6.14 admits.

**P6-12.9 (MUST) Indeterminate verdict handled by declaration.** An implementation must apply the declared handling of section 3.13 to an indeterminate verdict on a branch condition, must default to suspension, and must not treat an indeterminate verdict as false.

### 12.3 Boundary with Part 3, provenance and audit ledger

This subsection is the reciprocal declaration `Part 3` section 12.6 requires.

**Delegated.** The basis of every determination made within a process. The subject's trail, into which process steps are registered as acts. The closure assessment, the frontier treatment and the propagation of a basis defect.

**Must not absorb.** Bases. A process step is not a reason.

**Naive conflation.** The process history is registered as the basis, per section 11.19. Or the engine's own event log is treated as the subject's trail and the registration is skipped, which fails when the orchestrator is replaced.

**Reciprocal.** This part declares that it does not own bases, that a process step is registered as a subject act rather than as a citation, and that its own retention does not govern the retention of the bases of determinations made within it. Clauses P6-12.10 through P6-12.12 make it binding.

**P6-12.10 (MUST) Steps registered as acts.** An implementation must register every step concerning an identified subject as a `Part 3` subject act and must not register one as a citation in a basis, per clause P3-12.14.

**P6-12.11 (MUST NOT) No basis held.** An implementation must not hold a citation structure for any determination and must not represent its own event log as a determination's basis.

**P6-12.12 (MUST) Compensation recorded as an act with its residue.** An implementation must record every compensation execution as an act with `Part 3`, citing the determination that authorised it and the residue it produced, per clause P6-3.71.

### 12.4 Boundary with Part 4, metadata and model repository

This subsection is the reciprocal declaration `Part 4` section 12.6 requires.

**Delegated.** The identity, version, meaning and representation of every concept a definition references. The design lineage of any transformation, which this component does not perform. Registration state of definitions, which is not a position in a process.

**Must not absorb.** Registration state, definition identity or effectivity. And not transformation: a derivation whose lineage `Part 4` records cannot be performed by a component that records no lineage.

**Naive conflation.** The registration state becomes a position in a change workflow, so a definition version has no state when no request is open, per `Part 4` section 12.6. Or the engine acquires transformation, per section 11.26.

**Reciprocal.** This part declares that it does not own registration state, definition identity or effectivity, that it invokes the recording operations of `Part 4`, and that its own retention does not govern the retention of the definitions it routed. Clauses P6-12.13 through P6-12.15 make it binding.

**P6-12.13 (MUST NOT) No registration state held.** An implementation must not hold, cache beyond a declared validity period, or assert the registration state or effectivity of any definition, and must obtain each by resolution.

**P6-12.14 (MUST NOT) No transformation.** An implementation must not transform, derive or enrich any value it carries, since the resulting lineage belongs to `Part 4` as a design fact and to `Part 3` as a historical one.

**P6-12.15 (MUST) Concepts resolved where referenced.** An implementation must obtain the definition version of every concept a definition version references by resolution against `Part 4` and must pin it at the start of every instance.

### 12.5 Boundary with Part 5, decision engine

This subsection is the reciprocal declaration `Part 5` section 12.6 requires.

**Delegated.** Every selection among candidate outcomes, including every selection among branches where the branches are not mutually exclusive. Criteria, tiebreaks, defaults and precedence orders. The four undecidable outcomes and their meaning.

**Must not absorb.** Selection. A branch is chosen by a decision or by mutual exclusivity, never by branch order.

**Naive conflation.** The undecidable outcome becomes a workflow branch and is not recorded as an outcome, so the organisation has referrals rather than a count of decisions its criterion could not determine, per `Part 5` section 12.6.

**Reciprocal.** This part declares that it does not own decisions, criteria or outcomes, that it records the decision reference rather than the branch taken, and that its own retention does not govern the retention of the decisions it routed. Clauses P6-12.16 through P6-12.19 make it binding.

**P6-12.16 (MUST) Decision referenced, not the branch.** An implementation must record, for every branch attributed to a decision, the whole outcome envelope by pin, and must not record only which branch was taken.

**P6-12.17 (MUST NOT) No selection by branch order.** An implementation must not select among branches by the order in which they are declared and must express a non exclusive selection as a `DECIDE` activity, per clause P6-3.33.

**P6-12.18 (MUST) Undecidable outcome recorded before referral.** An implementation must confirm that an undecidable decision outcome was recorded by `Part 5` before raising a referral, per clause P5-12.21.

**P6-12.19 (MUST) Default is a declared artifact, not a diagram property.** An implementation must record a default flow as a `Part 5` default declaration with an authority and must not treat it as a property of the definition, per clause P6-3.34.

### 12.7 Boundary with Part 7, policy decision point and authorisation

**Delegated.** Every authorisation decision: whether a principal may start, advance, suspend, resume, cancel, retry, intervene in, migrate or read an instance; whether a principal may record a definition version or a migration mapping; and whether a compensation may be performed.

**Must not absorb.** Policy. This component records decision references and supplies its own facts as attributes.

**Naive conflation.** The engine becomes the authorisation point, because a process is where operations happen and a gateway looks like a place to check permission. The authorisation then has no obligations model, no combining algorithm and no enforcement point, and it is expressed as a branch.

**Reciprocal.** `Part 7` must declare that it owns authorisation and its combining algorithms, that it does not orchestrate, that it obtains process facts as attributes by pin where a policy depends on one, and that it does not hold process state.

**P6-12.20 (MUST) Decisions consumed, not made.** An implementation must record the `AUTHREF` of every authorisation decision that permitted an operation and must not evaluate policy.

**P6-12.21 (MUST) Interventions authorised.** An implementation must obtain an authorisation for every intervening operation of section 4.4 and must refuse one lacking it.

**P6-12.22 (MUST NOT) No authorisation as a branch.** An implementation must not express an authorisation check as a conditional split and must obtain the decision from `Part 7` as an activity outcome.

### 12.8 Boundary with Part 8, human task and case management

This is the most delicate boundary in the part, because both components have a legitimate claim to the same thing and the line is fine.

**Delegated.** Everything about the work item: its offering, its allocation to a person or a group, its reallocation, its delegation, its escalation, its suspension by the performer, its queue, its priority, its due date as presented to the performer, and the case in which it sits. Also the review obligations of section 7.5, which are discharged by work `Part 8` manages.

**Must not absorb.** The work item lifecycle. This component holds the state of the **activity in the flow**: created, waiting on a human, completed, faulted, cancelled. It does not hold the state of the **work item**: offered, allocated, started, suspended, reallocated.

**Position taken, and the test.** The engine knows that a person must do something and knows when it is done. Everything between those two facts belongs to `Part 8`. The test is whether the fact would change if the work were reassigned to a different person: if it would, the fact is the work item's; if it would not, it is the activity's.

**Naive conflation, both directions.** The engine holds the work item state, per section 11.23, and the two copies diverge exactly when a task is escalated. Or `Part 8` holds the flow position, so completing a task advances the process directly and the process's state exists only in the task manager, which is section 11.1 again with a different owner.

**Reciprocal.** `Part 8` must declare that it owns the work item lifecycle, the queue and the case, that completing a work item does not itself advance a process, that it reports completion to this component as an activity outcome, and that its own retention does not govern the retention of the instances that created its work items.

**P6-12.23 (MUST NOT) No work item lifecycle.** An implementation must not hold the offering, allocation, reallocation, delegation, escalation or performer suspension state of a human activity's work item.

**P6-12.24 (MUST) Completion received as an activity outcome.** An implementation must receive the completion of a human activity as an activity outcome reported by `Part 8` and must not advance a token on a work item state change.

**P6-12.25 (MUST) Escalation does not advance.** An implementation must not advance a token, take a branch or fire a timer as a consequence of an escalation, a reallocation or a delegation within `Part 8`.

**P6-12.26 (MUST) Review obligations passed, not managed.** An implementation must record every review obligation of section 7.5 as a fact and must obtain any task by which it is discharged from `Part 8`, per clause P6-7.18.

### 12.9 Boundary with Part 9, schema and contract registry

**Delegated.** The identity, versioning and compatibility of the schemas of definition interchange, event payloads, invocation requests and outcome envelopes, and the validation of an instance against one.

**Must not absorb.** Schema validation. This component records the schema a payload claims and does not validate against it.

**Naive conflation.** The engine validates payloads against a cached schema, so two components disagree about whether a message was well formed, and a malformed payload is refused for a reason `Part 9` would not give.

**Reciprocal.** `Part 9` must declare that it owns schema identity and compatibility, that it does not express control flow, and that it exposes schema versions obtainable by pin.

**P6-12.27 (MUST NOT) No schema validation or versioning.** An implementation must not assign version identity to a schema and must not validate a payload against one, and must express a structural refusal as `MALFORMED` without asserting a schema outcome.

**P6-12.28 (MUST) Schema reference recorded.** An implementation must record the schema identity and version every event and invocation payload claims and must pin it in the instance.

### 12.10 Boundary with Part 10, reference and master data management

**Delegated.** The membership, versioning and retention of every value set, including any set from which a multiple instance activity enumerates its members and any set a correlation scheme draws upon.

**Must not absorb.** Value set membership. A collection enumerated by a multiple instance activity is read from a pinned `Part 10` version, not held.

**Naive conflation.** The collection is copied into an instance value so the iteration does not need a call, which is section 11.1 with a list instead of a scalar, and the copy's size is then the instance count of section 3.8.

**Reciprocal.** `Part 10` must declare that it owns value set membership and versioning, that it retains every superseded version for at least as long as the longest retained instance that enumerated it, and that it does not hold process state.

**P6-12.29 (MUST) Collections enumerated by pin.** An implementation must enumerate a multiple instance activity's members from a pinned `Part 10` value set version and must not hold the collection as an instance value.

**P6-12.30 (MUST) Enumeration pin recorded with the instance count.** An implementation must record the pinned set version alongside the recorded instance count and its provenance, per clause P6-3.48.

### 12.11 Boundary with Part 11, content addressed artifact store

**Delegated.** The durable storage and retrieval by digest of the octets of anything this component pins or exports: definition artifacts, evidence packages and opaque transit values whose size warrants it.

**Must not absorb.** Storage semantics. This component owns the mapping from a pin to a digest and a canonical form profile.

**Naive conflation.** The store holds instance event logs and becomes a second source for process state, with no derivation, no sequence guarantee and no gap detection.

**Reciprocal.** `Part 11` must declare that it holds no process state, no event sequence and no derived state, and that it does not delete content on its own authority.

**P6-12.31 (MUST) Digest is the interface.** An implementation must address stored content by digest under a declared canonical form profile and must not rely on a location or path as identity.

**P6-12.32 (MUST NOT) No process state in the store.** An implementation must not hold event sequences, derived states or token positions in the artifact store and must not accept them from it.

### 12.12 Boundary with Part 12, conformance and assurance harness

**Delegated.** All assessment of whether an implementation satisfies this part, including the verification of the properties this part requires an implementation to demonstrate: derivation determinism, replay agreement, the disposal demonstration and the four static analyses.

**Must not absorb.** Self assessment. This component performs the disposal demonstration of clause P6-3.9, the replay sampling of clause P6-8.14 and the analyses of section 6.7, and records their results; it does not assess itself against this part.

**Naive conflation.** The component's own disposal demonstration is presented as evidence that the instances hold no business data. A demonstration performed by the component that would have to admit the exception is the weakest possible assurance, and it is precisely the demonstration on which the spine of this part depends.

**Reciprocal.** `Part 12` must declare that it obtains the clause set from this part by resolution, that it records the version of this part an assessment was made against, that it does not write to any instance while assessing, and that it performs its own disposal demonstration independently rather than accepting this component's.

**P6-12.33 (MUST) Read only assessment.** An implementation must expose everything `Part 12` requires through read operations and must not require a write in order to be assessed.

**P6-12.34 (MUST NOT) No self assessment as assessment.** An implementation must not present its own disposal demonstrations, replay samples or analyses as an assessment of conformance, per clause P6-1.15.

**P6-12.35 (MUST) Instance values exposed for independent demonstration.** An implementation must expose every instance value with its declared kind so that `Part 12` can perform the disposal demonstration independently.

### 12.13 Boundary with Part 13, model invocation and agent execution

**Delegated.** The invocation of any model or agent, its cost, its retries, its non determinism, its behaviour and the record of what it was asked and returned.

**Must not absorb.** Invocation mechanics. An activity of kind `INVOKE_MODEL` names a `Part 13` operation and records its outcome by reference; the engine does not invoke a model directly.

**Naive conflation, two forms.** A gateway routes on a model's output directly, so the branch is attributed to a score rather than to a determination and the criterion that turned the score into a branch does not exist. Or the engine retries a model invocation on its own initiative, which for a non deterministic service produces a different output and an activity whose recorded outcome is one of several the model produced.

**Position taken.** A model output reaches a branch only through a `Part 2` evaluation or a `Part 5` decision that consumed it as a pinned input. The engine may not compare a score to a threshold, per clause P6-6.15, because the threshold is a rule.

An agent may perform an activity. Where it does, the attribution and the delegation chain to an accountable party are `Part 3`'s, and clause P6-12.38 requires this component to supply what that needs.

**Reciprocal.** `Part 13` must declare that it owns invocation and the model artifact, that it does not hold process state, that it exposes an invocation record obtainable by pin, and that it treats a repeated invocation bearing the same idempotence key as this component supplies it.

**P6-12.36 (MUST NOT) No routing on a model output.** An implementation must not attribute a branch to a model output and must require the attribution to be a `Part 2` report or a `Part 5` decision that consumed the output as a pinned input.

**P6-12.37 (MUST) Model retries governed by the declared policy.** An implementation must not retry a model invocation other than under the activity's declared retry policy, must record every attempt, and must record that the outcomes of separate attempts may differ.

**P6-12.38 (MUST) Agent attribution supplied.** An implementation must supply, for an activity performed by an automated agent, the agent identity, the `Part 13` invocation reference and whatever `Part 3` section 3.12 requires to establish a delegation chain to an accountable party.

### 12.14 Boundary with Part 0, system composition

**Delegated.** What happens when all the components run at once: authority over facts more than one component touches, the seams at which values cross boundaries, the propagation of non results, and pinning across a unit of work spanning several components.

**Must not absorb.** Composition. This part states what it orchestrates and what it refuses to hold, and does not state what the estate does when an orchestrator is replaced with running instances in flight.

**Reciprocal.** `Part 0` must declare that this component holds authority over process definitions, instances, event logs, derived states, join resolutions, compensation outcomes and residues, and that it holds authority over nothing else. It must state, for every seam, what must hold and how a violation appears here. It must in particular resolve eight questions this part hands it.

How the disposability requirement is enforced across the estate, given that this part can demonstrate its own compliance and cannot prevent a consumer from building a report over its instances.

What the estate does when an orchestrator is replaced with instances in flight, given that instances are pinned to definition versions the replacement may not hold and that clause P6-1.3 requires every business fact to survive the replacement.

Who owns a residue by default where no assignment is made, since clause P6-3.69 requires an assignment and cannot compel one.

How a unit of work spanning this component, `Part 2` and `Part 5` pins one rule set version, one criterion version and one definition version together, so that a path, the verdicts that attributed it and the decisions that routed it cannot be against different vintages of policy.

Whether a review obligation raised here, a `Part 8` task, and a `Part 3` determination of its discharge are one act or three, which is the same question `Part 5` section 13.9 hands forward about an override.

What a component must do when this component's activity outcome and the invoked component's own record of the invocation disagree, which is the concrete form of the question `Part 3` section 13.11 hands forward.

Whether the engine's observation of elapsed time, which is the one occurrence time a component may originate under section 6.5, should be permitted to any other component.

Whether the structural patterns this standard has now repeated six times should each be stated once for the whole standard, per section 13.7.

**P6-12.39 (MUST) Authority declared, not assumed.** An implementation must not accept an assertion about a definition, an instance, an event log, a derived state, a join resolution, a compensation outcome or a residue from another component, and must require every such fact to be established by its own operations.

**P6-12.40 (MUST) Non results propagated unmodified.** An implementation must pass every indeterminate verdict and undecidable decision to the declared handling of section 3.13 unmodified and must not degrade one to a determinate branch in order to keep an instance moving.

**P6-12.41 (MUST) Disposability exposed to composition.** An implementation must make its disposal demonstration results and its instance value kinds available as signals, since neither a consumer building reports over its instances nor an accreting variable can be remedied within this component.
## 13. What could not be established

A question recorded as open can be closed by someone with access to the source. A question closed by inference cannot be reopened, because nothing in the document reveals that an inference was made.

### 13.1 Sources not obtained in full text

The following were not available in full text. This part's account of each rests on publisher inventories, issue trackers, front matter, implementation documentation and secondary literature. No clause reproduces text from any of them.

**BPMN 2.0.2.** The version history, the December 2013 formal document date, the absence of a major revision since 2011 and the live issue tracker were obtained directly from the publisher. **The execution semantics were not.** Two claims on which this part's design turns rest on secondary sources.

That the inclusive gateway's join semantics require global information about the state of the whole model rests on a published formalisation paper which states that this is what the OMG standard requires, and on the surrounding literature's repeated observation that the specification's semantics are given in natural language that in places misleads. Section 3.7's restriction is built on it.

That the exclusive gateway evaluates its outgoing conditions in a defined order and takes the first true one rests on four independent implementation accounts and on published commentary. Section 3.6's mutual exclusivity requirement is built on it.

Both should be verified against the specification text before approval, and the second matters more, because clause P6-3.32 refuses a construct on its strength.

**The ISO/IEC 19510 discrepancy.** The ISO front matter states that the standard is identical with BPMN 2.0.1. The OMG's specification page states that 2.0.2 was published by ISO as the 2013 edition. Both statements were obtained and they cannot both be right. Which is correct **could not be established**, and clause P6-10.3 requires an implementation to state which document it read rather than citing the standard number alone.

**WS-BPEL 2.0.** The OASIS Standard status, the 2007 date and the section structure of section 12 were obtained from the specification's own table of contents. The clause text was not. Four rules this part adopts as clauses in section 3.9, being compensation availability only on successful completion, the disabling of compensation by fault handler invocation, reverse order of completion as the default, and the confinement of the compensate activities to handlers, rest on the table of contents, the published issue list and secondary sources including implementation documentation.

**The compensation ordering anomaly.** That the specification's issue resolution settled on respecting only explicitly modelled control dependencies, and that the published literature identifies anomalies where control links cross scope boundaries between nested non isolated scopes, rest on the OASIS issue list and on a published paper's abstract respectively. Neither the resolution text nor the paper was obtained. Section 10.3 names the conflict on that basis and section 3.9 requires the order to be declared rather than resolving it, which is the honest response to an unverified conflict.

**Workflow nets, soundness and its decidability.** The three soundness conditions, the short circuit correspondence to liveness and boundedness, polynomial decidability for the free choice class, and the undecidability of soundness for workflow nets with reset arcs, all rest on the published literature as generally understood. Multiple sources were obtained and they agree. No primary source was obtained and no edition is cited. Section 6.7 depends on all of it and clause P6-6.38's requirement rests on the undecidability result in particular, which is the single most consequential literature claim in the part.

**The control flow pattern catalogue.** The taxonomy from which section 3.6's join kinds and section 3.8's repetition forms are drawn was not obtained. The join kinds as stated here are this part's own naming and its own closed set, informed by the catalogue as generally understood rather than derived from it, and a reviewer with the catalogue should check the set against it for a pattern this part has no member for.

Not obtained and not assessed at all: CMMN, which bears on the `Part 8` boundary of section 12.8; SCXML, which bears on the derived state machines of section 5; ISO/IEC 15909 on high level Petri nets, whose currency was not established and which is the formal basis of section 6.7 at one remove; XPDL; and the exception handling pattern literature, which is the most likely source for anything in section 3.10 and which section 10.8 currently records as unsourced.

**P6-13.1 (MUST) Verification before approval.** An implementation or reviewer must verify the claims listed in section 13.1 against the source standards and literature before this part is approved and must record the outcome of each verification against this section.

### 13.2 The reproducibility this part cannot offer

`Part 2` requires a verdict to be reproducible from its pins. `Part 5` requires a decision to be. `Part 3` requires a chain to be reconstructable. This part requires only that an execution be **recoverable from its log**, which is weaker, and section 6.1 states why: the engine's inputs include real elapsed time, the arrival order of external events and the availability of external components, none of which is a pin.

The weakening is forced rather than chosen and it has a consequence worth stating plainly. Two instances of the same definition, started with the same inputs, may legitimately take different paths: one because a timer fired before a message arrived and the other because it did not; one because a component was available and the other because it was not. Neither is a defect. Both are correct executions of the same definition and their difference is not explicable from the definition.

**Open.** Whether more is achievable. Two directions were considered and neither pursued. Recording an arrival order as a pinned sequence and requiring replay to honour it, which is what section 6.1 already does for a replay and which does not make two live executions comparable. And declaring, per definition version, the classes of external timing on which the path may legitimately depend, so that a path difference attributable to an undeclared timing dependency becomes a finding. The second is a real idea, would make race conditions in process definitions discoverable, and was not designed.

### 13.3 The cost of restricting the inclusive join

Section 3.7 admits the inclusive join only within a block structured region with no cancellation and no arbitrary cycle. Clause P6-3.43 refuses the definition version otherwise.

The justification is that the construct's semantics are non local, that the specification's own account requires global state, that published formalisations disagree, and that in the presence of cancellation the underlying reachability question is undecidable. Those are good reasons and the restriction has a real cost.

Modellers use inclusive convergence freely and naturally, because it expresses something true: several things may or may not have happened and we proceed when all of those that were going to have. Expressing the same thing under this part requires either a parallel split with explicit no operation branches, which doubles the diagram's size, or a partial join with a count, which is wrong when the count varies, or a decision, which is heavier than the situation warrants.

There is a genuine possibility that the restriction pushes modellers toward the parallel split with no operation branches, which is expressible and unreadable, and that the net effect on reviewability is negative even though the net effect on analysability is positive. Section 11.5 refuses the timeout approximation and offers nothing as easy.

**Open.** Whether a middle position exists. The candidate is to admit the inclusive join in an unstructured region on condition that the definition declares, for every incoming flow, the positions from which a token could still reach it, and that the declaration be verified statically where the class permits. That makes the non local information an authored artifact rather than a computed one, which is the same move sections 3.6 and 3.13 make elsewhere in this part, and it was not designed.

### 13.4 Where the flow ends and the work item begins

Section 12.8 draws the `Part 8` boundary by a test: a fact belongs to the work item if it would change were the work reassigned to a different person. The test is serviceable and it does not settle everything.

Three cases sit on the line. A due date presented to a performer is the work item's; a deadline that causes a boundary timer to fire and take a branch is the flow's; and they are frequently the same date, held twice, with the second the one the process routes on. An escalation that reassigns work is the work item's; an escalation that changes the process path is the flow's; and the same operational event may do both. And a work item that a performer suspends is the work item's, while the activity waiting on it is the flow's, so an instance in `WAITING` may be waiting on a work item that nobody is working on and this component cannot tell.

The third case is the one clause P6-3.119 cannot fully satisfy. The `waiting_on` projection must say what would release a wait, and for a human activity the honest answer is that `Part 8` holds a work item whose state this component does not know.

**Open.** Whether this component should be permitted to read the work item's state for the purpose of reporting, without holding it. Reading without holding is a coherent position, it would let `waiting_on` say whether anybody is actually working on the thing, and it introduces a read dependency that makes the projection unavailable when `Part 8` is. Section 12.8's present position is stricter than may be useful.

### 13.5 Whether compensation availability should expire

Clause P6-5.23 requires a declared period for which a completed scope's compensation remains available, and clause P6-3.61 requires the elapsed interval since completion to be recorded on every compensation. Neither settles what the period should be or what happens at its end.

The tension is real. A compensation performed years after the scope completed compensates against a snapshot of a world that has moved, per the snapshot semantics of section 3.9, and may therefore do something wrong. But an instance that lives for years and needs unwinding in year three needs the compensation to still be available, and expiring it means the unwinding becomes a manual act with no handler.

**Open.** What the expiry should do. Three candidates. Expire the compensation and raise a review obligation, which is honest and leaves the work to a person. Retain availability indefinitely and rely on the staleness signal, which is the present position by default and which permits a stale compensation to run. Or require a re assessment before a stale compensation runs, so that a person confirms the handler is still appropriate, which is probably right and adds a step nobody will want.

### 13.6 The volume this part requires

Section 8.2 requires one entry per invocation attempt and one per iteration. A repetition of four hundred iterations, each invoking something with two retries, produces twelve hundred entries in one activity. Nothing here is costed.

The volume is required for two specific reasons, and neither is negotiable without losing a capability. Per attempt entries are the retry distribution, which is the earliest signal that a dependency is failing. Per iteration entries are what makes per iteration compensation possible at all, since compensating iteration two hundred and seventeen requires knowing it completed.

**Open.** Whether a declared coarser grain is admissible for definitions that declare no compensation and no retry policy, so that the volume is paid only where the capability is used. That is probably the right answer and it introduces a grain that varies by definition version, which every projection would then have to declare.

### 13.7 Repeated structure across the standard, now six times

`Part 4` section 13.7 recorded three repeated structures. `Part 5` section 13.7 recorded five. This part adds to the list and the drift is now observable rather than predicted.

**The immutable record with stateful assertions about it.** Six parts.

**The declared completeness of a set.** Five parts: `Part 3`'s basis and negative citation completeness, `Part 4`'s lineage completeness, `Part 5`'s candidate set completeness, and this part's declared enumeration of a candidate set for a multiple instance activity.

**The frontier as a declared terminus.** Two parts specify it, `Part 5` uses the concept without the name, and this part uses it a third way: a stall is a terminus with no declared reason, which is structurally the `FRONTIER_UNDECLARED` of `Part 3` section 3.11 applied to an execution. Three uses, two vocabularies, one unnamed.

**The asymmetric bridge that disproves and cannot prove.** Two parts have one, `Part 5` records that it should and does not, and this part has none. Its candidate would be a set of recorded executions with the paths their author asserts the definition produces, run at definition recording. That would catch a definition whose control flow does not do what its author believes, which is the commonest defect in process modelling, and it was not specified.

**The honest undeclared value.** Six parts. This part contributes `COMPENSABILITY_UNDECLARED`, `RESIDUE_UNCLASSIFIED` and `OUTCOME_UNKNOWN`.

**The prohibition on an undeclared arbitrary resolution.** Five parts, and this is the pattern this part shares most closely with `Part 5`: `Part 2` refuses to arbitrate a rule contradiction, `Part 5` refuses to resolve a tie, a cycle or an incomparability, and this part refuses to resolve a join, a branch or an inclusive convergence by an order nobody declared. Three refusals, three vocabularies, one principle.

**Open.** All of it, and now urgently. Six parts have independently specified the same six patterns, three vocabularies exist for the frontier concept, and the asymmetric bridge is missing from two parts that should have one. This is the third consecutive part to record the question and the second to recommend acting before the next part rather than at `Part 0`.

### 13.8 What this part deliberately did not attempt

No conformance assessment of any system was performed or anticipated, per clause P6-1.15.

No notation is specified. Whether a definition is expressed in BPMN, in a textual language or in a table is out of scope, and section 3.4 specifies only that positions be addressable in a registered scheme. This is deliberate and it means this part cannot check anything about a definition's readability.

No interchange format is specified, so a definition cannot be moved between conforming implementations on the strength of this part alone.

No treatment is given of processes spanning organisations. A choreography, in which no single component holds the flow, is a different problem and the reciprocals of section 12 assume a single orchestrator inside one organisation.

No treatment is given of a process whose definition is itself produced by a mechanism. A generated or fitted process definition would need the same triad `Part 2` requires of a rule, and this part requires only a document citation.

No treatment is given of ad hoc or unstructured work, where the order is chosen by the performer rather than declared. `Part 8`'s case management covers some of it and the boundary was not examined.

No performance, scale or latency requirement is stated, and section 13.6 records the volume concern without a threshold.

**P6-13.2 (MUST) Gaps declared, not filled.** An implementation must not represent a matter listed in section 13.8 as specified by this part.

**P6-13.3 (SHOULD) Open questions carried forward.** A reviewer of this part should record a position on each open question in section 13, and where a position is adopted it should be recorded in the review outcome rather than by silent amendment of the clause it affects.

### 13.9 Questions handed to Part 0 rather than answered here

Each was identified while authoring this part.

How the disposability requirement is enforced across the estate, given that this part can demonstrate its own compliance and cannot prevent a consumer from building a report over its instances.

What the estate does when an orchestrator is replaced with instances in flight, given that instances are pinned to definition versions the replacement may not hold.

Who owns a residue by default where no assignment is made, since clause P6-3.69 requires an assignment and cannot compel one.

How a unit of work spanning this component, `Part 2` and `Part 5` pins one rule set version, one criterion version and one definition version together.

Whether a review obligation raised here, a `Part 8` task and a `Part 3` determination of its discharge are one act or three, which is the same shape as the question `Part 5` section 13.9 hands forward about an override.

What a component must do when this component's activity outcome and the invoked component's own record of the invocation disagree, which is the concrete form of `Part 3` section 13.11's question.

Whether the engine's observation of elapsed time, which section 6.5 permits as the one occurrence time a component may originate, should be permitted to any other component or reserved to this one.

Whether the six repeated structures of section 13.7 should each be stated once for the whole standard, and whether the frontier concept's three vocabularies should be reconciled before `Part 7`.
