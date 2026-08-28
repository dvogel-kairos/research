# KAIROS STD 003 Part 13: Model Invocation and Agent Execution Layer

**Standard.** KAIROS STD 003, the enterprise architecture standard.
**Part.** Part 13 of 14 (Part 0 and Parts 1 through 13). Cited as `KAIROS STD 003 Part 13`.
**Title.** Model invocation and agent execution layer.
**Version.** 1.0.0.
**Status.** Proposed. This part has not been approved and is not effective. It is issued for review against the authoring brief of 2026-08-17.
**Date of issue.** 2026-08-18.
**Supersedes.** Nothing. This is the first version.

## Binding of requirement language

The key words MUST, MUST NOT, SHOULD, SHOULD NOT and MAY in this part are to be interpreted as described in RFC 2119 and RFC 8174, and only in the upper case forms. This part does not use SHALL, SHALL NOT, REQUIRED, RECOMMENDED, NOT RECOMMENDED or OPTIONAL as requirement keywords.

Every requirement in this part is a numbered clause. A clause identifier has the form `P13-S.N`, where `S` is the section number and `N` is the ordinal of the clause within that section. Clause identifiers are permanent. A clause that is later removed has its identifier retired and never reissued. A clause that is later added to a section takes the next unused ordinal in that section, so ordinals are stable but not contiguous over the life of the part.

Text that is not a numbered clause is not binding. Narrative, tables, algorithms, examples and the discussion of standards are provided to make the clauses intelligible and testable, and where a table carries normative content a clause says so explicitly and names the table.

Where a clause carries a **Source.** note, the note states the specification or published work on which the clause's subject rests and whether this part adopts that treatment or departs from it. The note is narrative and not binding; the clause governs.

## Conformance

An implementation conforms to this part if it satisfies every MUST and MUST NOT clause and records, for each SHOULD and SHOULD NOT clause it does not satisfy, the reason. This part does not define conformance levels, profiles or a certification scheme, and it does not define the method of assessment, which is the subject of `KAIROS STD 003 Part 12`.

The authoring brief for this standard states that this part has the least standards support of the thirteen and that the author should expect to report much of it as unestablished rather than manufacture a specification. That instruction has been followed and it is visible in the shape of the document. Section 3 and section 6 specify records, boundaries and refusals, because those are specifiable. Section 13 is longer in proportion than in any other part of this standard, because the subjects a reader might most want specified, being what makes a model output correct, what an agent may be trusted to decide, and how either should be evaluated, are not specified here and are reported as absent.

## Clause index

The index below is generated from the clause text of this document. It lists every clause identifier, its modality and its subject label. The counts that follow the index are derived by the same extraction and are stated with the grain at which they were counted.

| Clause | Modality | Subject |
| --- | --- | --- |
| P13-1.1 | MUST | Invocations owned |
| P13-1.2 | MUST | Model identity owned |
| P13-1.3 | MUST | Context assembly owned |
| P13-1.4 | MUST | Produced values owned |
| P13-1.5 | MUST | Attempts and selections owned |
| P13-1.6 | MUST | Reproducibility declarations owned |
| P13-1.7 | MUST | Cost records owned |
| P13-1.8 | MUST | Effect declarations owned |
| P13-1.9 | MUST | Agent runs owned |
| P13-1.10 | MUST | Tool call records owned |
| P13-1.11 | MUST | Defect notifications owned |
| P13-1.12 | MUST | Provider and serving configuration records owned |
| P13-1.13 | MUST NOT | Not the checker of anything it produced |
| P13-1.14 | MUST NOT | Not an authority on correctness |
| P13-1.15 | MUST NOT | Not a policy evaluator |
| P13-1.16 | MUST NOT | Not a rules engine or a decision engine |
| P13-1.17 | MUST NOT | Not a work manager |
| P13-1.18 | MUST NOT | Not a schema authority |
| P13-1.19 | MUST NOT | Not a reference authority |
| P13-1.20 | MUST NOT | Not an artifact store |
| P13-1.21 | MUST NOT | Not the audit ledger |
| P13-1.22 | MUST NOT | Not an assurance authority |
| P13-1.23 | MUST NOT | Not the document authority |
| P13-1.24 | MUST NOT | Not an evaluator of models |
| P13-1.25 | MUST NOT | Not a holder of authority an agent was not granted |
| P13-1.26 | MUST NOT | No conformance assessment anticipated |
| P13-1.27 | MUST | Model behaviour out of scope |
| P13-1.28 | MUST NOT | No claim of coverage over the subject |
| P13-2.1 | MUST NOT | No redefinition of another part's terms |
| P13-2.2 | MUST NOT | Produced not equated with checked |
| P13-2.3 | MUST NOT | Refusal not equated with error |
| P13-2.4 | MUST NOT | Provider filter not equated with refusal |
| P13-2.5 | MUST NOT | Cache hit not equated with invocation |
| P13-2.6 | MUST NOT | Attempt not equated with result |
| P13-2.7 | MUST NOT | Model name not equated with model identity |
| P13-2.8 | MUST NOT | Termination not equated with achievement |
| P13-2.9 | MUST NOT | Token count not equated with a measure of value |
| P13-2.10 | MUST | Kinds registered before use |
| P13-3.1 | MUST | Types declared |
| P13-3.2 | MUST NOT | No representation dependent identity |
| P13-3.3 | MUST | Material held by address |
| P13-3.4 | MUST | Produced status recorded on every output |
| P13-3.5 | MUST NOT | No produced value recorded as checked |
| P13-3.6 | MUST NOT | No self check |
| P13-3.7 | MUST NOT | No chain of models constitutes a check |
| P13-3.8 | MUST | Check requires an accountable actor |
| P13-3.9 | MUST NOT | No confidence score recorded as a check |
| P13-3.10 | MUST | Unchecked population exposed |
| P13-3.11 | MUST | Inventory normative |
| P13-3.12 | MUST | Immutability observed |
| P13-3.13 | MUST | Received determinations recorded unaltered |
| P13-3.14 | MUST | Identity class recorded |
| P13-3.15 | MUST | Verifiability derived and recorded |
| P13-3.16 | MUST | Requested and responding model both recorded |
| P13-3.17 | MUST | Alias invocation marked as unverifiable |
| P13-3.18 | MUST NOT | No reproducibility claim over an unverifiable identity |
| P13-3.19 | MUST | Silent identity change detectable |
| P13-3.20 | MUST NOT | No model card treated as a specification |
| P13-3.21 | MUST | One record per attempt |
| P13-3.22 | MUST | Provider defaults recorded as unknown |
| P13-3.23 | MUST NOT | No invocation record without a cost record |
| P13-3.24 | MUST | Attribution mandatory |
| P13-3.25 | MUST | Content recording level declared |
| P13-3.26 | MUST | Constrained generation recorded |
| P13-3.27 | MUST | Cache hit recorded and attributed |
| P13-3.28 | MUST NOT | No invocation record deletion |
| P13-3.29 | MUST | Vacuity classified and recorded |
| P13-3.30 | MUST NOT | No vacuous check counted as a check |
| P13-3.31 | MUST | Vacuity notified to the relying component |
| P13-3.32 | MUST NOT | No constrained output presented as validated |
| P13-3.33 | MUST | Same model review recorded |
| P13-3.34 | MUST | Vacuous check population exposed |
| P13-3.35 | MUST | Class defaults to unknown |
| P13-3.36 | MUST NOT | No determinism inferred from a temperature setting |
| P13-3.37 | MUST | Variance sources enumerated per invocation |
| P13-3.38 | MUST | Replay requirements stated |
| P13-3.39 | MUST | Observed variance recorded where measured |
| P13-3.40 | MUST | Batch invariance recorded as an assertion by the provider |
| P13-3.41 | MUST | Cost recorded per attempt |
| P13-3.42 | MUST | Cost of discarded attempts summed and exposed |
| P13-3.43 | MUST | Unit definition version recorded |
| P13-3.44 | MUST NOT | No cross provider cost comparison |
| P13-3.45 | MUST | Cost attributed to the work |
| P13-3.46 | MUST | Pricing basis recorded |
| P13-3.47 | MUST NOT | No cost figure presented as a measure of value |
| P13-3.48 | MUST | Discarded attempts retained |
| P13-3.49 | MUST | Selection recorded with a registered basis |
| P13-3.50 | MUST NOT | No selection by attempt order |
| P13-3.51 | MUST | Variance across attempts exposed |
| P13-3.52 | MUST | Objective recorded before the run |
| P13-3.53 | MUST | Four budgets declared and finite |
| P13-3.54 | MUST | Budget exhaustion is a termination reason, not a failure |
| P13-3.55 | MUST NOT | No agent assertion recorded as an outcome |
| P13-3.56 | MUST | Objective determination obtained, not made |
| P13-3.57 | MUST | Authority envelope declared and bounded by the initiating party |
| P13-3.58 | MUST | Authority exceeded refused and recorded |
| P13-3.59 | MUST NOT | No irreversible effect without a declared effect budget |
| P13-3.60 | MUST | Effects enumerated per run |
| P13-3.61 | MUST | Repetition detected and bounded |
| P13-3.62 | MUST NOT | No termination reason recorded as achievement |
| P13-3.63 | MUST | Tools registered before use |
| P13-3.64 | MUST | Effect class declared per tool |
| P13-3.65 | MUST | Argument origin recorded |
| P13-3.66 | MUST | Arguments validated against the registered schema |
| P13-3.67 | MUST NOT | No validation of arguments treated as a check of their content |
| P13-3.68 | MUST | Authorisation per call |
| P13-3.69 | MUST | Effects recorded per call |
| P13-3.70 | MUST NOT | No retry of a call that is not retry safe |
| P13-3.71 | MUST | Defect notification raised and propagated |
| P13-3.72 | MUST | Affected invocations enumerated |
| P13-3.73 | MUST NOT | No partial enumeration presented as complete |
| P13-3.74 | MUST | Notification to the ledger as a basis defect |
| P13-3.75 | MUST | Consumers identified by their own registration |
| P13-3.76 | MUST | Unidentifiable consumer population exposed |
| P13-3.77 | MUST | Instruction material versioned as a document |
| P13-3.78 | MUST | Instruction version pinned per invocation |
| P13-3.79 | MUST NOT | No instruction material held inline |
| P13-3.80 | MUST | Assembly order recorded |
| P13-3.81 | MUST | Retrieved material pinned |
| P13-3.82 | MUST | Truncation recorded |
| P13-3.83 | MUST | Projections marked as such |
| P13-3.84 | MUST | Produced status carried into every projection |
| P13-3.85 | MUST NOT | No aggregate that loses the produced and checked distinction |
| P13-3.86 | MUST NOT | No quality or accuracy figure exposed |
| P13-4.1 | MUST | Operations defined over the entities of section 3 |
| P13-4.2 | MUST | Idempotency key accepted |
| P13-4.3 | MUST NOT | No idempotency claim over the output |
| P13-4.4 | MUST | Authorisation obtained per invocation and per tool call |
| P13-4.5 | MUST | One outcome per operation |
| P13-4.6 | MUST | Refusals recorded |
| P13-4.7 | MUST NOT | No operation that alters an invocation record or a produced value |
| P13-4.8 | MUST NOT | No operation returning a value marked checked |
| P13-4.9 | MUST | Invocation refused without attribution |
| P13-4.10 | MUST | Invocation refused without a registered model |
| P13-4.11 | MUST | Invocation refused where the model status forbids it |
| P13-4.12 | MUST | Attempt set refused without a budget |
| P13-4.13 | MUST | Selection refused without a registered basis |
| P13-4.14 | MUST | Cache hit refused without the source or its declared absence |
| P13-4.15 | MUST NOT | No invocation without a context assembly record |
| P13-4.16 | MUST | Run refused without four budgets |
| P13-4.17 | MUST | Run refused without an authority envelope |
| P13-4.18 | MUST | Run refused where the envelope exceeds the initiating party's authority |
| P13-4.19 | MUST | Step refused outside the envelope |
| P13-4.20 | MUST | Halt available to a party at any step |
| P13-4.21 | MUST | Close refused without a termination reason |
| P13-4.22 | MUST NOT | No objective determination accepted from the run |
| P13-4.23 | MUST | Tool call refused where the tool is unregistered |
| P13-4.24 | MUST | Tool call refused where arguments do not validate |
| P13-4.25 | MUST | Invocation retrievable with its full record |
| P13-4.26 | MUST | Point in time query supported |
| P13-4.27 | MUST | Attempt set retrievable in full |
| P13-4.28 | MUST | Produced value carries its status on every read |
| P13-4.29 | MUST | Run retrievable with every step and effect |
| P13-4.30 | MUST NOT | No state change from a read |
| P13-4.31 | MUST | Affected invocation query supported |
| P13-4.32 | MUST NOT | No assumption of reproducibility |
| P13-4.33 | MUST NOT | No assumption that a validated output is a correct one |
| P13-4.34 | MUST NOT | No assumption that a produced value was checked |
| P13-4.35 | MUST NOT | No assumption that a named model is the model that answered |
| P13-4.36 | MUST NOT | No assumption that an agent's termination means success |
| P13-4.37 | MUST NOT | No assumption that an operation is free of external effect |
| P13-4.38 | MUST | Cost visible before commitment where a budget applies |
| P13-4.39 | MUST | Reads treated as fallible |
| P13-4.40 | MUST NOT | No proceeding on an authorisation failure |
| P13-4.41 | MUST NOT | No invocation on unresolvable material |
| P13-4.42 | MUST | Event per invocation and per tool call |
| P13-4.43 | MUST | Events delivered to the ledger |
| P13-4.44 | MUST | Distinct event class for a refusal by the model |
| P13-4.45 | MUST | Distinct event class for a provider filter |
| P13-4.46 | MUST | Distinct event class for an irreversible effect |
| P13-4.47 | MUST | Distinct event class for authority exceeded |
| P13-4.48 | MUST | Defect notification event names the affected interval |
| P13-4.49 | MUST | Responding model change event |
| P13-4.50 | MUST | Budget exhaustion event |
| P13-4.51 | SHOULD | Attempt divergence signal |
| P13-5.1 | MUST | States held as transitions |
| P13-5.2 | MUST | One state per axis per instant |
| P13-5.3 | MUST NOT | No derivation of one axis from another |
| P13-5.4 | MUST | Transitions carry authorisation where required |
| P13-5.5 | MUST | Illegal transitions recorded |
| P13-5.6 | MUST NOT | No unlisted transition |
| P13-5.7 | MUST | Investigation suspends invocation |
| P13-5.8 | MUST | Defect state triggers enumeration |
| P13-5.9 | MUST | Remediation recorded as a new configuration |
| P13-5.10 | MUST | Withdrawn models still resolvable |
| P13-5.11 | MUST | Abandonment does not cancel cost |
| P13-5.12 | MUST | Unresolved distinguished from failed |
| P13-5.13 | MUST NOT | No invocation state reopened |
| P13-5.14 | MUST | Termination is not settlement |
| P13-5.15 | MUST | Unsettled run population exposed |
| P13-5.16 | MUST | Resumption authorised afresh |
| P13-5.17 | MUST NOT | No settlement without effect resolution |
| P13-5.18 | MUST | Consumed unchecked recorded as a state, not inferred |
| P13-5.19 | MUST | Vacuous check does not reach checked |
| P13-5.20 | MUST | Defect affected applies retrospectively |
| P13-5.21 | MUST NOT | No defect affected value silently superseded |
| P13-5.22 | MUST | Irreversible effects exposed until accepted |
| P13-5.23 | MUST | Reversal failure recorded, not retried silently |
| P13-5.24 | MUST NOT | No effect state terminal without an accountable act |
| P13-6.1 | MUST | Record fidelity guaranteed |
| P13-6.2 | MUST NOT | No guarantee offered over outputs |
| P13-6.3 | MUST | Input digest recorded |
| P13-6.4 | MUST NOT | No clock or environment in a recorded input |
| P13-6.5 | MUST | Assembly composed from addressed material |
| P13-6.6 | MUST | Order recorded as part of the assembly |
| P13-6.7 | MUST | Assembly digest recorded |
| P13-6.8 | MUST | Truncation recorded with what was removed |
| P13-6.9 | MUST NOT | No silent context substitution |
| P13-6.10 | MUST | Retrieved material attributed to its source component |
| P13-6.11 | MUST | Variance sources enumerated |
| P13-6.12 | MUST | Batch composition recorded as present unless invariance is asserted |
| P13-6.13 | MUST NOT | No determinism from temperature or seed |
| P13-6.14 | MUST | Batch invariance recorded as an assertion with a version |
| P13-6.15 | MUST | Distribution reproducibility distinguished from bit reproducibility |
| P13-6.16 | MUST | Observed variance measured before a reproducibility claim |
| P13-6.17 | MUST | Cost of determinism recorded where claimed |
| P13-6.18 | MUST NOT | No replay presented as reproduction |
| P13-6.19 | MUST | Every retry recorded as a new invocation |
| P13-6.20 | MUST NOT | No retry represented as re attempting one invocation |
| P13-6.21 | MUST | Attempt set bounded |
| P13-6.22 | MUST | Exhaustion is an outcome |
| P13-6.23 | MUST | Retry on failure distinguished from search for a usable output |
| P13-6.24 | MUST NOT | No retry of an invocation with an unreversed irreversible effect |
| P13-6.25 | MUST | Effect class checked before retry |
| P13-6.26 | MUST | Selection basis registered and recorded |
| P13-6.27 | MUST | Discarded outputs retained and countable |
| P13-6.28 | MUST | Cost recorded in provider units and not normalised |
| P13-6.29 | MUST | Budget checked before invocation |
| P13-6.30 | MUST NOT | No budget decision made here |
| P13-6.31 | MUST | Cost attributed at the grain of the work |
| P13-6.32 | MUST | Cache hit cost recorded distinctly |
| P13-6.33 | MUST NOT | No cost figure aggregated across unit definitions |
| P13-6.34 | MUST | Unit definition change surfaces the affected population |
| P13-6.35 | MUST | Steps counted against the budget |
| P13-6.36 | MUST | Cost accumulated across the run |
| P13-6.37 | MUST | Authority checked per step, not per run |
| P13-6.38 | MUST NOT | No authority accretion |
| P13-6.39 | MUST | Repetition bound declared |
| P13-6.40 | MUST | Nested runs bounded and attributed |
| P13-6.41 | MUST | Nesting depth bounded |
| P13-6.42 | MUST NOT | No objective amendment during a run |
| P13-6.43 | MUST | Every step attributable to the run and the initiating party |
| P13-6.44 | MUST NOT | No effect outside the envelope |
| P13-6.45 | MUST | Halt honoured between steps |
| P13-6.46 | MUST | Concurrent invocations independent |
| P13-6.47 | MUST | Idempotency key prevents a second charge |
| P13-6.48 | MUST | Concurrent steps in one run serialised |
| P13-6.49 | MUST | Timeout recorded as an outcome with cost |
| P13-6.50 | MUST | All bounds declared and finite |
| P13-6.51 | MUST NOT | No judgement of an output's content |
| P13-6.52 | MUST NOT | No aggregate quality measure |
| P13-6.53 | MAY | Structural and variance measures permitted |
| P13-6.54 | MUST NOT | No inference from a refusal |
| P13-6.55 | MUST NOT | No model selection by governed algorithm |
| P13-6.56 | MAY | Operational routing permitted |
| P13-7.1 | MUST | One enumeration per value |
| P13-7.2 | MUST NOT | No value outside the enumerations |
| P13-7.3 | MUST | Properties of an outcome exposed |
| P13-7.4 | MUST NOT | No refusal recorded as an error |
| P13-7.5 | MUST | Refusal, filter and empty distinguished |
| P13-7.6 | MUST | Truncation distinguished from completion |
| P13-7.7 | MUST | Constrained production distinguished |
| P13-7.8 | MUST | Cache hit distinguished from production |
| P13-7.9 | MUST | Identity unverifiable recorded as an outcome, not a caveat |
| P13-7.10 | MUST | Budget and rate limit distinguished |
| P13-7.11 | MUST NOT | No outcome collapsed to a failure |
| P13-7.12 | MUST NOT | No correctness outcome |
| P13-7.13 | MUST NOT | No confidence outcome |
| P13-7.14 | MUST NOT | No success vocabulary over content |
| P13-7.15 | MUST | Produced is the strongest outcome |
| P13-7.16 | MUST | Effect uncertainty recorded as its own outcome |
| P13-7.17 | MUST NOT | No assumption of no effect on failure |
| P13-7.18 | MUST | Uncertain effect exposed |
| P13-7.19 | MUST | Refusal reasons distinguished |
| P13-7.20 | MUST | Refused operations carry no cost claim |
| P13-7.21 | MUST | Three properties exposed |
| P13-7.22 | MUST NOT | No invocation without a writable record store |
| P13-7.23 | MUST | Invariant violation halts invocation |
| P13-7.24 | MUST | Outcome carried with its qualifications |
| P13-7.25 | MUST NOT | No aggregation losing the distinctions |
| P13-7.26 | MUST | Counts report each outcome as its own category |
| P13-7.27 | MUST | Non results retained where unconsumed |
| P13-8.1 | MUST | Completeness of each record declared |
| P13-8.2 | MUST NOT | No figure about consequences presented as complete |
| P13-8.3 | MUST | Grain stated with every count |
| P13-8.4 | MUST | Invocation counts state whether attempts are counted individually |
| P13-8.5 | MUST | Cost figures state their unit definition version |
| P13-8.6 | MUST NOT | No count spanning model identities without the split |
| P13-8.7 | MUST | Agent figures state the grain |
| P13-8.8 | MUST | Every invocation recorded |
| P13-8.9 | MUST | Every context assembly recorded |
| P13-8.10 | MUST | Every produced value recorded with its status |
| P13-8.11 | MUST | Every cost recorded |
| P13-8.12 | MUST | Every tool call and effect recorded |
| P13-8.13 | MUST | Every reversal and acceptance recorded |
| P13-8.14 | MUST | Every run recorded with its budgets and termination |
| P13-8.15 | MUST | Every checking determination recorded as received |
| P13-8.16 | MUST | Every defect notification and enumeration recorded |
| P13-8.17 | MUST | Every responding model discrepancy recorded |
| P13-8.18 | MUST | The exact input of any invocation |
| P13-8.19 | MUST | The model and configuration that served it |
| P13-8.20 | MUST | Every attempt behind any result |
| P13-8.21 | MUST | The full cost of any unit of work |
| P13-8.22 | MUST | Whether any produced value was checked |
| P13-8.23 | MUST | Every step and effect of any run |
| P13-8.24 | MUST | What an agent was asked and what it asserted |
| P13-8.25 | MUST | Everything a defect affected |
| P13-8.26 | MUST NOT | No reconstruction dependent on this component running |
| P13-8.27 | MUST | Unchecked consumed population |
| P13-8.28 | MUST | Vacuous check proportion |
| P13-8.29 | MUST | Unverifiable identity proportion |
| P13-8.30 | MUST | Reproducibility class distribution |
| P13-8.31 | MUST | Discarded attempt cost and count |
| P13-8.32 | MUST | Attempt divergence population |
| P13-8.33 | MUST | Irreversible unaccepted effect population |
| P13-8.34 | MUST | Uncertain effect population |
| P13-8.35 | MUST | Unsettled run population |
| P13-8.36 | MUST | Agent asserted completion without determination population |
| P13-8.37 | MUST | Authority exceeded population |
| P13-8.38 | MUST | Unidentifiable consumer population |
| P13-8.39 | MUST | Responding model discrepancy population |
| P13-8.40 | MUST | Content not retained proportion |
| P13-8.41 | SHOULD | Refusal and filter rate by model |
| P13-8.42 | MUST | Package assemblable for an invocation |
| P13-8.43 | MUST | Package assemblable for a run |
| P13-8.44 | MUST | Package states what it omits |
| P13-8.45 | MUST | Package integrity protected |
| P13-8.46 | MUST | Records outlive the value |
| P13-8.47 | MUST | Retention obligation notified |
| P13-8.48 | MUST NOT | No alteration of an invocation record, produced value, cost record or tool call record |
| P13-8.49 | MUST NOT | No deletion of a discarded attempt |
| P13-8.50 | MUST NOT | No deletion of an effect record |
| P13-9.1 | MUST | Closed sets not extended |
| P13-9.2 | MUST | Open sets extended only through a registry |
| P13-9.3 | MUST NOT | No new outcome for a new model capability |
| P13-9.4 | MUST | Registration before use |
| P13-9.5 | MUST | Definition mandatory at registration |
| P13-9.6 | MUST | Registration attributable |
| P13-9.7 | MUST NOT | No meaning change under a registered identifier |
| P13-9.8 | MUST | Retirement recorded, records retained |
| P13-9.9 | MUST | Identity class recorded per registration |
| P13-9.10 | MUST | Serving configuration versioned |
| P13-9.11 | MUST | Provider assertions recorded as assertions |
| P13-9.12 | MUST NOT | No inherited registration across identity change |
| P13-9.13 | MUST | Effect class and retry safety recorded |
| P13-9.14 | MUST | Reversal procedure required for a reversible class |
| P13-9.15 | MUST | Required authority recorded |
| P13-9.16 | MUST | Argument schema required |
| P13-9.17 | MUST | Unit definitions versioned |
| P13-9.18 | MUST | Provider ownership of the definition recorded |
| P13-9.19 | MUST NOT | No cross provider unit equivalence registered |
| P13-9.20 | MUST | Basis semantics recorded |
| P13-9.21 | MUST | Order based bases marked |
| P13-9.22 | MUST NOT | No basis registered that selects on a model's self assessment |
| P13-10.1 | MUST | Cited edition recorded |
| P13-10.2 | MUST | Basis marked |
| P13-10.3 | MUST | Pre stable sources marked as such |
| P13-10.4 | MUST | Requirements of this part alone identified |
| P13-11.1 | MUST | Produced status carried into every projection |
| P13-11.2 | MUST NOT | No self check |
| P13-11.3 | MUST | Vacuity classified and not counted |
| P13-11.4 | MUST | Producer authored criteria recorded as vacuous |
| P13-11.5 | MUST NOT | No determinism from temperature or seed |
| P13-11.6 | MUST | Identity class recorded and alias marked unverifiable |
| P13-11.7 | MUST | Attempt divergence exposed |
| P13-11.8 | MUST | Cost recorded per attempt |
| P13-11.9 | MUST NOT | No cost figure as a measure of value |
| P13-11.10 | MUST NOT | No aggregation across unit definitions |
| P13-11.11 | MUST | Cache hit recorded distinctly |
| P13-11.12 | MUST NOT | No refusal as an error |
| P13-11.13 | MUST | Filter distinguished from refusal |
| P13-11.14 | MUST | Truncation recorded as its own outcome |
| P13-11.15 | MUST NOT | No assertion recorded as achievement |
| P13-11.16 | MUST | Four budgets declared and finite |
| P13-11.17 | MUST NOT | No authority accretion |
| P13-11.18 | MUST NOT | No retry of a call that is not retry safe |
| P13-11.19 | MUST | Uncertain effect recorded as uncertain |
| P13-11.20 | MUST | Instruction material versioned and addressed |
| P13-11.21 | MUST | Choice breadth of a presented proposal recorded |
| P13-11.22 | MUST | Provider declaration recorded as a declaration |
| P13-11.23 | MUST NOT | No invocation without a writable record |
| P13-11.24 | MUST | Unidentifiable consumer population exposed |
| P13-11.25 | MUST NOT | No invocation inside another component's evaluation |
| P13-11.26 | MUST NOT | No agent run substituted for a declared process |
| P13-12.1 | MUST | Instruction material governed as a document |
| P13-12.2 | MUST | Instruction version pinned per invocation |
| P13-12.3 | MUST | Records treated as records |
| P13-12.4 | MUST NOT | No rule evaluated by invocation |
| P13-12.5 | MUST | Produced values supplied pinned and marked |
| P13-12.6 | MUST NOT | No invocation during a rule evaluation |
| P13-12.7 | MUST | Events emitted to the ledger |
| P13-12.8 | MUST | Defect notified as a basis defect |
| P13-12.9 | MUST NOT | No chain asserted |
| P13-12.10 | MUST | Delegation chain supplied where an agent requests |
| P13-12.11 | MUST | Definitions cited, not restated |
| P13-12.12 | MUST | Definition change surfaces affected instructions |
| P13-12.13 | MUST NOT | No business decision produced as an outcome |
| P13-12.14 | MUST | Model selection obtained where it is a decision |
| P13-12.15 | MAY | Operational routing retained |
| P13-12.16 | MUST NOT | No agent run as a process instance |
| P13-12.17 | MUST | Invocation reference supplied to a process step |
| P13-12.18 | MUST | Run attributable to the initiating process instance |
| P13-12.19 | MUST NOT | No policy evaluated |
| P13-12.20 | MUST | Authorisation obtained per invocation and per call |
| P13-12.21 | MUST | Produced value pinnable |
| P13-12.22 | MUST | Reproduction limit supplied |
| P13-12.23 | MUST | Produced value supplied as a proposal |
| P13-12.24 | MUST | Invocation reference supplied for the completion record |
| P13-12.25 | MUST | Checking determination received, not made |
| P13-12.26 | MUST NOT | No completion of a work item |
| P13-12.27 | MUST | Constraint disclosed to the validating component |
| P13-12.28 | MUST NOT | No validation performed |
| P13-12.29 | MUST NOT | No validation treated as a check |
| P13-12.30 | MUST | Reference proposals supplied as proposals |
| P13-12.31 | MUST NOT | No assertion into reference content |
| P13-12.32 | MUST | Bound values drawn from pinned versions |
| P13-12.33 | MUST | Material held by address |
| P13-12.34 | MUST | Provenance retained here |
| P13-12.35 | MUST NOT | No correctness from addressability |
| P13-12.36 | MUST | Reproducibility declaration supplied for assessment use |
| P13-12.37 | MUST NOT | No finding or assurance statement produced |
| P13-12.38 | MUST | Elicitation supported |
| P13-12.39 | MUST | State exposed for verification |
| P13-12.40 | MUST NOT | No self assurance |
| P13-12.41 | MUST | Authority declared, not assumed |
| P13-12.42 | MUST | Non results returned unmodified |
| P13-12.43 | MUST | Unchecked consumption exposed to composition |
| P13-12.44 | MUST | Produced status preserved across every boundary |
| P13-13.1 | MUST | Unverified reciprocals declared |
| P13-13.2 | MUST | Register handed forward complete |
| P13-13.3 | MUST | Gaps declared, not filled |
| P13-13.4 | SHOULD | Open questions carried forward |

### Derived counts

Every figure below is derived by extraction from the clause text of this document and not asserted independently. The grain of counting is stated for each figure. A clause is one line of the document matching the clause heading form given under Binding of requirement language, that is, an identifier of the form `P13-S.N`, a modality in parentheses, and a subject label. Narrative sentences containing a requirement keyword are not clauses and are not counted; per that same section they are not binding. No clause of this part states a requirement keyword in its prose, so the modality of a clause is unambiguous.

**Total clauses.** 432. Grain: one clause heading.

**By modality.** Grain: one clause heading, counted once against its single declared modality.

| Modality | Clauses | Share |
| --- | --- | --- |
| MUST | 298 | 69.0% |
| MUST NOT | 128 | 29.6% |
| SHOULD | 3 | 0.7% |
| SHOULD NOT | 0 | 0.0% |
| MAY | 3 | 0.7% |
| **All** | **432** | **100.0%** |

**Absolute requirements.** 426 clauses carry MUST or MUST NOT and are therefore conditions of conformance. 3 carry SHOULD or SHOULD NOT and require a recorded reason where not satisfied. 3 carry MAY and constrain nothing. Grain: one clause heading. These three figures sum to the total.

**By section.** Grain: one clause heading, attributed to the numbered section in which its heading appears.

| Section | Title | Clauses | MUST | MUST NOT | SHOULD | SHOULD NOT | MAY |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Scope and responsibilities | 28 | 13 | 15 | 0 | 0 | 0 |
| 2 | Terminology | 10 | 1 | 9 | 0 | 0 | 0 |
| 3 | Data model | 86 | 62 | 24 | 0 | 0 | 0 |
| 4 | Interfaces | 51 | 36 | 14 | 1 | 0 | 0 |
| 5 | State model | 24 | 18 | 6 | 0 | 0 | 0 |
| 6 | Execution semantics | 56 | 38 | 16 | 0 | 0 | 2 |
| 7 | Outcome and failure taxonomy | 27 | 18 | 9 | 0 | 0 | 0 |
| 8 | Observability and the audit record | 50 | 43 | 6 | 1 | 0 | 0 |
| 9 | Extension model | 22 | 17 | 5 | 0 | 0 | 0 |
| 10 | Standards and specifications | 4 | 4 | 0 | 0 | 0 | 0 |
| 11 | Anti patterns | 26 | 15 | 11 | 0 | 0 | 0 |
| 12 | Boundaries with other parts | 44 | 30 | 13 | 0 | 0 | 1 |
| 13 | What could not be established | 4 | 3 | 0 | 1 | 0 | 0 |
| **All** | | **432** | **298** | **128** | **3** | **0** | **3** |

**Ordinal integrity.** In this version, the highest ordinal in each section equals the number of clauses in that section, so no identifier has yet been retired. This will cease to be true at the first clause removal, and the count rather than the highest ordinal is then the figure to rely on.

**Sourced clauses.** 11 clauses carry a **Source.** note naming the specification, published work or reciprocal requirement their subject rests on. Grain: one clause heading carrying at least one Source note. Section 10.1 states how the notes are to be read and section 13.1 lists the sources not obtained.

**Cross part citations.** This part cites fourteen clauses of other parts: P7-12.35, P7-12.38, P8-3-31, P8-3-32, P8-12-34, P8-12-36, P9-12-37, P9-12-38, P10-12.39, P10-12.42, P11-12.37, P11-12.39, P12-12.33 and P12-12.36. Every one was verified against the delivered text of the part concerned. Grain: one distinct clause identifier cited.

## 1. Scope and responsibilities

### 1.1 What this component is

This component invokes models, runs agents and records what happened. It is the newest subject in this standard and the only one where the thing being specified changes faster than a standard can be written about it, which is why almost everything in this part is about the record rather than about the model.

Every other part of this standard has now told this one what it must not be allowed to do. `Part 7` forbids an invocation during a policy evaluation and requires a model output to reach a decision only as a pinned attribute obtained beforehand. `Part 8` places the boundary at the point where responsibility transfers and holds that it transfers only through a completion record written by a human performer. `Part 9` holds that a validation of a constrained generation carries no information. `Part 10` requires a model proposal to be a proposal until an accountable party accepts it. `Part 11` holds that an address establishes what octets are and nothing about whether they are correct. `Part 12` requires a human decision for every finding and forbids attributing one to a model. Six components, six vocabularies, one boundary, and this part's principal job is to hold it from this side.

**P13-1.1 (MUST) Invocations owned.** An implementation must own the invocation, being one request to a model and the record of what was asked, what was returned and under what conditions.

**P13-1.2 (MUST) Model identity owned.** An implementation must own the identity of every model it invokes, together with the class of that identity and its verifiability.

**P13-1.3 (MUST) Context assembly owned.** An implementation must own the record of everything that composed an invocation's input, including instructions, retrieved material, tool results and prior turns.

**P13-1.4 (MUST) Produced values owned.** An implementation must own the produced value, being an output of an invocation, and its status as produced rather than checked.

**P13-1.5 (MUST) Attempts and selections owned.** An implementation must own every attempt made in the course of obtaining a result, including discarded attempts, and the record of which was selected and why.

**P13-1.6 (MUST) Reproducibility declarations owned.** An implementation must own the declaration of what would be required to reproduce an invocation and whether reproduction is achievable.

**P13-1.7 (MUST) Cost records owned.** An implementation must own the record of what an invocation consumed, in the units the provider defines, attributed to the work that caused it.

**P13-1.8 (MUST) Effect declarations owned.** An implementation must own the declaration of what effects an invocation or a tool call has outside itself, and their reversibility.

**P13-1.9 (MUST) Agent runs owned.** An implementation must own the agent run, being a bounded sequence of invocations and tool calls under a declared objective, with its budgets and its termination.

**P13-1.10 (MUST) Tool call records owned.** An implementation must own the record of every tool call an agent made, its arguments, its result and its effects.

**P13-1.11 (MUST) Defect notifications owned.** An implementation must own the notification that a model, a model version or a serving configuration was found defective, so that everything produced by it can be enumerated. **Source.** Required of this component by `Part 7` section 12.13, whose reciprocal requires this part to treat a model found defective as a basis defect to `Part 3` so that decisions relying on it can be enumerated.

**P13-1.12 (MUST) Provider and serving configuration records owned.** An implementation must own the record of the provider, the serving configuration and the parameters in force for every invocation.

### 1.2 What this component is not

**P13-1.13 (MUST NOT) Not the checker of anything it produced.** An implementation must not represent any output of an invocation as checked, and must not perform a check on a value it produced.

**P13-1.14 (MUST NOT) Not an authority on correctness.** An implementation must not record, expose or return any value meaning that a produced value is correct, true, accurate or fit for a purpose.

**P13-1.15 (MUST NOT) Not a policy evaluator.** An implementation must not evaluate a policy, render an authorisation decision or determine an entitlement, which are `Part 7`'s.

**P13-1.16 (MUST NOT) Not a rules engine or a decision engine.** An implementation must not evaluate a business constraint or select a business outcome, which are `Part 2`'s and `Part 5`'s.

**P13-1.17 (MUST NOT) Not a work manager.** An implementation must not assign, offer, escalate or complete a work item, which are `Part 8`'s.

**P13-1.18 (MUST NOT) Not a schema authority.** An implementation must not version a schema or validate an instance, which are `Part 9`'s.

**P13-1.19 (MUST NOT) Not a reference authority.** An implementation must not assert a concept, a value set member, a map entry or a master record, which are `Part 10`'s.

**P13-1.20 (MUST NOT) Not an artifact store.** An implementation must not hold the octets of a prompt, a retrieved document, a tool result or an output, and must hold the content address held by `Part 11`.

**P13-1.21 (MUST NOT) Not the audit ledger.** An implementation must not represent its invocation records as the evidentiary chain of any determination, which is `Part 3`'s.

**P13-1.22 (MUST NOT) Not an assurance authority.** An implementation must not issue an assurance statement or record a finding, which are `Part 12`'s.

**P13-1.23 (MUST NOT) Not the document authority.** An implementation must not govern the approval, effective date or retention schedule of a prompt, a model card or an evaluation report as a document, which are `Part 1`'s.

**P13-1.24 (MUST NOT) Not an evaluator of models.** An implementation must not represent any measurement it makes of a model as an evaluation of that model's fitness, and section 13.6 records that this part specifies no evaluation at all.

**P13-1.25 (MUST NOT) Not a holder of authority an agent was not granted.** An implementation must not permit an agent run to exercise an authority the initiating party did not hold.

### 1.3 The three failures this part exists to prevent

*The produced value that became a checked one by being handled.* A model produces a value. The value is well formed, so it validates. It is stored, so it has an address. It is read by three components, each of which records it. At no point did anyone check whether it was right, and at every point the record grew more solid. Section 3.2 states the boundary and section 3.6 supplies the concept the boundary needs, being the vacuous check: a check whose failure was impossible given how the value was produced. Constrained decoding is the clearest case and it is not the only one, and this part requires every vacuous check to be recorded as vacuous rather than counted.

*The invocation treated as a function of its inputs.* Everything a system does with a model output assumes that the same request would produce the same output, or at least that the output is a function of what was sent. It is not. At temperature zero, with a fixed seed, on a fixed model, the output depends on the batch the serving stack happened to place the request in, which depends on the load the provider was under, which is a property of other parties' traffic. Section 6.3 states this with its evidence and section 3.7 requires every invocation record to declare its reproducibility class rather than assume one. Every retry, every cache, every replay and every audit in this subject rests on an assumption that is false by default.

*The agent that reported its own success.* An agent is given an objective, runs, and stops. Whether it achieved the objective is a question about the world, and the only party that answered it was the agent. Section 3.9 makes the termination reason a record of why the run stopped and not a claim that it succeeded, and clause P13-3.62 forbids an agent's assertion of completion from being recorded as a checked outcome. This is the same boundary as the first failure and it is where the consequences are largest, because an agent's effects are already in the world by the time anyone looks.

### 1.4 The reader this part is written for

A reviewer should read section 3.2, then section 6.3, then section 13. Section 3.2 is the boundary six other parts require this one to hold. Section 6.3 is the finding that determines how much of the rest is achievable. Section 13 is longer than in any other part of this standard and is where the honest answer to most questions about this subject is recorded.

Three things in this part are most likely to be wrong. Section 13.3 records that cost is measured in units no two providers define the same way and that this part therefore requires a figure it cannot make comparable. Section 13.4 records that the reproducibility this part requires to be declared is, for hosted models, usually unachievable, so the declaration will almost always say so and a reader may conclude the requirement is empty. And section 13.5 records that this part specifies almost nothing about what an agent may be permitted to do, which is the question most people asking about this subject actually want answered.

**P13-1.26 (MUST NOT) No conformance assessment anticipated.** An implementation must not read this part as assessing any system, and must treat assessment as the subject of `Part 12`.

**P13-1.27 (MUST) Model behaviour out of scope.** An implementation must not read this part as constraining what a model outputs, and must treat this part as constraining what is recorded about an invocation and what may be concluded from it.

**P13-1.28 (MUST NOT) No claim of coverage over the subject.** An implementation must not represent this part as a complete specification of model invocation or agent execution, and must read section 13.8 as the statement of what it does not cover.

## 2. Terminology

### 2.1 Terms owned by this part

**Model.** A function from an input to an output whose parameters were fitted rather than authored, invoked as a service or executed locally. This part takes no position on what kinds of model exist and requires only that one be identified.

**Model identity.** The identification of the model that served an invocation, together with the class of that identity per section 3.4.

**Invocation.** One request to a model and the record of it. The unit of everything in this part.

**Attempt.** One invocation made in the course of obtaining a result. Where a result was obtained after several attempts, each attempt is an invocation with its own record and its own produced value.

**Produced value.** An output of an invocation. It is produced by construction and it is not checked, whatever is subsequently done with it.

**Checked value.** A value about which an accountable party outside this component has recorded a determination that it is fit for the use to which it is put. This component never produces one, and section 3.2 states why.

**Check.** An act by an accountable party that could have failed and did not. A check that could not have failed is a vacuous check.

**Vacuous check.** A check whose failure was impossible given how the value was produced. Introduced by this part; section 3.6 gives the classes and the reason.

**Context assembly.** The complete record of what composed an invocation's input: the instruction material, the prior turns, the retrieved material, the tool results and the order in which they were arranged.

**Sampling parameters.** The declared parameters governing how an output was selected from the model's distribution, such as temperature, nucleus threshold and seed.

**Serving configuration.** The declared state of the system that served an invocation, including the provider, the deployment, the quantisation and, where the provider asserts it, batch invariance.

**Reproducibility class.** The declared class of an invocation's reproducibility, from the closed set in section 3.7. The default is unknown.

**Batch invariance.** The property that a kernel produces the same numerical result for one request irrespective of the size and composition of the batch the request was served in. Its absence is the principal source of non determinism in hosted inference and section 6.3 gives the evidence.

**Effect class.** The declared class of what an invocation or tool call changes outside itself: none, reversible, idempotent, or irreversible.

**Tool call.** An invocation by a model, mediated by this component, of a capability outside the model, with recorded arguments, result and effects.

**Agent run.** A bounded sequence of invocations and tool calls under a declared objective, with a step budget, a cost budget, an effect class and a recorded termination.

**Objective.** The declared statement of what an agent run was initiated to achieve. This part requires it to be recorded and takes no position on what makes one well formed.

**Termination reason.** The recorded reason an agent run stopped, from the closed set in section 3.9. It is never a claim that the objective was achieved.

**Step.** One invocation or one tool call within an agent run.

**Budget.** A declared, finite bound on steps, cost, elapsed time or effects, whose exhaustion is an outcome and not a failure.

**Selection.** The recorded act of choosing one produced value from several attempts. This part requires it to be recorded as a selection with a basis.

**Cost unit.** A unit in which a provider meters consumption, defined by that provider and not comparable across providers or across versions of one provider's definition.

**Cache hit.** The return of a value that was produced by an earlier invocation, so that the parameters, the model identity and the instant of the current request did not determine it.

**Refusal.** A produced value in which the model declines to produce what was asked. It is content and it is not an error.

**Provider filter.** An intervention by the serving party that suppressed or altered an output, which is neither a refusal by the model nor a failure of this component.

**Defect notification.** The record that a model, version or serving configuration was found defective, together with the enumeration of everything produced by it.

**Attribution.** The recorded link from an invocation to the unit of work, the initiating party and the authorising decision that caused it.

### 2.2 Clauses governing terminology

**P13-2.1 (MUST NOT) No redefinition of another part's terms.** An implementation must not redefine a term this standard allocates to another part, and must use it with the meaning that part gives it.

**P13-2.2 (MUST NOT) Produced not equated with checked.** An implementation must not describe a produced value as checked, verified, validated, confirmed or correct.

**P13-2.3 (MUST NOT) Refusal not equated with error.** An implementation must not record a refusal as a failure of the invocation or of this component.

**P13-2.4 (MUST NOT) Provider filter not equated with refusal.** An implementation must not record an intervention by the serving party as a refusal by the model.

**P13-2.5 (MUST NOT) Cache hit not equated with invocation.** An implementation must not record a cache hit as an invocation that produced the value at that instant.

**P13-2.6 (MUST NOT) Attempt not equated with result.** An implementation must not describe the selected attempt as the only attempt, and must not discard the others.

**P13-2.7 (MUST NOT) Model name not equated with model identity.** An implementation must not treat a provider's model name as an identity, and must record its identity class per section 3.4.

**P13-2.8 (MUST NOT) Termination not equated with achievement.** An implementation must not describe an agent run's termination as the achievement of its objective.

**P13-2.9 (MUST NOT) Token count not equated with a measure of value.** An implementation must not present a count of cost units as a measure of productivity, quality, effort or output.

**P13-2.10 (MUST) Kinds registered before use.** An implementation must register every model, provider, serving configuration, tool, effect class, cost unit definition and selection basis before an invocation uses it, per section 9.

## 3. Data model

### 3.1 Type vocabulary

Types in this section are abstract and impose no representation. `identifier` is an opaque immutable string unique within its declared scope. `instant` is a point in time with an offset from UTC and at least millisecond resolution. `address` is a content address held by `Part 11`. `pin` is a reference resolving to a stated version of a stated object as it stood at a stated instant. `digest` is a hash together with the identifier of the algorithm that produced it. `enum(...)` is a closed set unless the field description states otherwise.

**P13-3.1 (MUST) Types declared.** An implementation must declare the concrete representation it adopts for every abstract type in section 3.1 and must not vary it between records of one class.

**P13-3.2 (MUST NOT) No representation dependent identity.** An implementation must not derive the identity of any record from its representation.

**P13-3.3 (MUST) Material held by address.** An implementation must hold every prompt, retrieved document, tool argument, tool result and output by content address in `Part 11` and must not hold the octets itself.

### 3.2 The boundary between a produced value and a checked one

This is the position on which the part turns, and it is the only position in this standard that six other parts independently demanded before it was written.

A produced value is the output of a fitted function. It has a shape, a provenance and an address. It has no truth value that anything in this component established, and nothing this component can do to it changes that. Storing it does not check it. Validating its structure does not check it. Addressing it does not check it. Passing it to three other components does not check it, and each of those components recording it makes the absence of a check harder to see rather than less real.

A checked value is one about which an accountable party has recorded a determination that it is fit for the use to which it is put. Two properties are essential and both are absent from a produced value. There must be an actor who can be held to the determination, which under this standard means a party resolvable in `Part 10`, acting in a work item in `Part 8`, under an authorisation in `Part 7`. And the determination must have been capable of coming out the other way, which is what section 3.6 is about.

Three corollaries follow and each is a clause below. A model must not check its own output, because a second invocation is a second produced value and not a check. A chain of models checking one another never terminates in a check, however long it is, because at no point does an accountable actor appear. And a check that could not have failed is not a check, which is where constrained decoding and self written rubrics fall.

**P13-3.4 (MUST) Produced status recorded on every output.** An implementation must record every output of an invocation as a produced value and must record its status as produced.

**P13-3.5 (MUST NOT) No produced value recorded as checked.** An implementation must not record, expose or return a produced value as checked, verified or correct.

**P13-3.6 (MUST NOT) No self check.** An implementation must not record an invocation whose input includes an output of a prior invocation as a check of that output, and must record it as a further produced value.

**P13-3.7 (MUST NOT) No chain of models constitutes a check.** An implementation must not record a sequence of invocations, however long, as establishing that any value in it is checked.

**P13-3.8 (MUST) Check requires an accountable actor.** An implementation must record a value as checked only on receipt of a determination from an accountable party outside this component, and must record the party, the work item and the authorisation reference.

**P13-3.9 (MUST NOT) No confidence score recorded as a check.** An implementation must not record a score, probability, likelihood or self assessed confidence produced by a model as a check or as a substitute for one.

**P13-3.10 (MUST) Unchecked population exposed.** An implementation must expose the count of produced values consumed by another component for which no checking determination has been received.

Clause P13-3.10 is the figure that makes this section operative rather than rhetorical. Every other requirement here can be satisfied by careful labelling. The count of produced values that were used and never checked is the measure of how much of the estate's behaviour rests on outputs nobody examined, and it is a number that only this component can compute.

### 3.3 Entity inventory

The table is normative as to which entities exist and which component owns each.

| Entity | Immutable once written | Owned here |
|---|---|---|
| Model registration | no, its status changes | yes |
| Serving configuration record | no, versions are | yes |
| Invocation record | yes | yes |
| Context assembly record | yes | yes |
| Produced value record | yes | yes |
| Attempt set and selection record | yes | yes |
| Reproducibility declaration | yes | yes |
| Cost record | yes | yes |
| Effect declaration | no, per tool registration | yes |
| Tool registration | no | yes |
| Tool call record | yes | yes |
| Agent run record | no, its state changes | yes |
| Objective record | yes | yes |
| Budget declaration | yes, per run | yes |
| Defect notification | yes | yes |
| Checking determination received | yes | yes, as received |
| Prompt, document, tool result, output octets | — | no, `Part 11` |
| Authorisation decision | — | no, `Part 7` |
| Work item and human completion | — | no, `Part 8` |
| Schema and validation | — | no, `Part 9` |
| Party identity | — | no, `Part 10` |
| Evidentiary chain | — | no, `Part 3` |
| Finding and assurance statement | — | no, `Part 12` |

**P13-3.11 (MUST) Inventory normative.** An implementation must hold every entity the table in section 3.3 marks as owned here and must not hold as its own any entity the table allocates to another part.

**P13-3.12 (MUST) Immutability observed.** An implementation must not modify any record the table in section 3.3 marks immutable once written, and must express a correction as a new record superseding it.

**P13-3.13 (MUST) Received determinations recorded unaltered.** An implementation must record a checking determination received from another component unaltered and must not requalify, aggregate or summarise it.

### 3.4 Model identity and its verifiability

A provider's model name is a mutable pointer. The content behind it changes without notice, the same name serves different weights in different regions, and a request naming one model may be answered by another. The nearest thing to a standard for invocation telemetry recognises this by carrying the requested model and the responding model as two separate attributes.

| Field | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `model_registration_id` | identifier | yes | 1 | Not possible |
| `identity_class` | enum(`content_addressed_weights`,`provider_version_string`,`provider_alias`) | yes | 1 | Not possible; see P13-3.15 |
| `weights_address` | address | no | 0..1 | The identity class is not content addressed |
| `provider` | identifier | yes | 1 | Not possible |
| `provider_model_name` | string | yes | 1 | Not possible |
| `provider_version_string` | string | no | 0..1 | The provider supplies no version string, which forces the identity class to alias |
| `verifiability` | enum(`verifiable`,`attestable`,`unverifiable`) | yes | 1 | Not possible |
| `declared_card_ref` | pin to `Part 1` | no | 0..1 | No model card or provider documentation is registered for this model |
| `status` | enum, section 5.2 | yes | 1 | Not possible |
| `first_registered_at` | instant | yes | 1 | Not possible |

**P13-3.14 (MUST) Identity class recorded.** An implementation must record the identity class of every model it registers from the closed set of three.

**P13-3.15 (MUST) Verifiability derived and recorded.** An implementation must record content addressed weights as verifiable, a provider version string as attestable, and a provider alias as unverifiable, and must not record a stronger verifiability than the identity class supports.

**P13-3.16 (MUST) Requested and responding model both recorded.** An implementation must record both the model identity requested and the model identity the provider reports as having responded, and must record a discrepancy between them. **Source.** The OpenTelemetry generative AI semantic conventions carry `gen_ai.request.model` and `gen_ai.response.model` as separate attributes, which exists because the model that answers is not necessarily the model that was asked for.

**P13-3.17 (MUST) Alias invocation marked as unverifiable.** An implementation must mark every invocation against a provider alias as having an unverifiable model identity, and must carry that mark on every produced value derived from it.

**P13-3.18 (MUST NOT) No reproducibility claim over an unverifiable identity.** An implementation must not record a reproducibility class stronger than unknown for an invocation whose model identity is unverifiable.

**P13-3.19 (MUST) Silent identity change detectable.** An implementation must record enough of the responding model identity on every invocation for a change in the content behind a provider alias to be detectable after the fact, and must expose every detected change.

**P13-3.20 (MUST NOT) No model card treated as a specification.** An implementation must record a provider's model card or documentation as a declaration by that provider and must not treat it as a specification of behaviour.

### 3.5 The invocation record

| Field | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `invocation_id` | identifier | yes | 1 | Not possible |
| `model_registration_id` | identifier | yes | 1 | Not possible |
| `responding_model_identity` | string | no | 0..1 | The provider reported none, which weakens every claim about which model answered |
| `serving_configuration_id` | identifier | yes | 1 | Not possible |
| `context_assembly_id` | identifier | yes | 1 | Not possible |
| `sampling_parameters` | structure: parameter, value | yes | 0..n | An empty set means the provider accepted none and the parameters are the provider's defaults, which must be recorded as unknown rather than as absent |
| `requested_at` | instant | yes | 1 | Not possible |
| `completed_at` | instant | no | 0..1 | The invocation did not complete |
| `outcome` | enum, section 7.2 | yes | 1 | Not possible |
| `produced_value_id` | identifier | no | 0..1 | No value was produced |
| `cost_record_id` | identifier | yes | 1 | Not possible; an invocation that produced nothing may still have incurred cost |
| `reproducibility_declaration_id` | identifier | yes | 1 | Not possible |
| `effect_class` | enum(`none`,`reversible`,`idempotent`,`irreversible`) | yes | 1 | Not possible |
| `attempt_ordinal` | integer, one or greater | yes | 1 | Not possible |
| `attempt_set_id` | identifier | no | 0..1 | The invocation was not one of several attempts |
| `agent_run_id` | identifier | no | 0..1 | The invocation was not within an agent run |
| `attribution` | structure: work item ref, initiating party, authorisation ref | yes | 1 | Not possible; see P13-3.24 |
| `cache_hit` | boolean | yes | 1 | Not possible |
| `cached_from_invocation_id` | identifier | no | 0..1 | Not a cache hit; required where `cache_hit` is true and the source is known |
| `constrained_generation` | enum(`none`,`schema`,`grammar`,`choice_set`,`unknown`) | yes | 1 | Not possible; see P13-3.26 |
| `content_recorded` | enum(`full`,`redacted`,`digest_only`,`none`) | yes | 1 | Not possible; see P13-3.25 |

**P13-3.21 (MUST) One record per attempt.** An implementation must write one invocation record for every attempt, including attempts that failed, were discarded or produced a refusal.

**P13-3.22 (MUST) Provider defaults recorded as unknown.** An implementation must record a sampling parameter the provider applied and did not disclose as unknown rather than as absent or as a default value it assumed.

**P13-3.23 (MUST NOT) No invocation record without a cost record.** An implementation must write a cost record for every invocation, including one that produced nothing.

**P13-3.24 (MUST) Attribution mandatory.** An implementation must attribute every invocation to a unit of work, an initiating party and an authorising decision, and must refuse an invocation it cannot attribute.

**P13-3.25 (MUST) Content recording level declared.** An implementation must record whether the prompt and output octets were retained in full, redacted, retained as a digest only, or not retained, and must not leave the level unstated. **Source.** The OpenTelemetry generative AI conventions permit instrumentations to capture prompts and completions and require that instrumentations supporting capture offer the ability to turn it off, for reasons of privacy and data volume. The consequence is that a conforming record under that convention may contain nothing of what was asked or returned, and §10.7 records the conflict with this part's requirement.

**P13-3.26 (MUST) Constrained generation recorded.** An implementation must record whether the output was produced under a structural constraint and of what kind, or that the fact is unknown. **Source.** Required of this component by `Part 9` clause P9-12-37, which requires that component to record on every validation record whether the instance was produced under schema constrained generation, or that the fact is unknown, which it can only do if this component supplies it.

**P13-3.27 (MUST) Cache hit recorded and attributed.** An implementation must record a cache hit as such, must name the invocation whose output was returned where it is known, and must not record the current instant's parameters as having determined the value.

**P13-3.28 (MUST NOT) No invocation record deletion.** An implementation must not delete an invocation record when the produced value is discarded, superseded or redacted.

### 3.6 Vacuous checks

A check that could not have failed conveys nothing, and this subject generates them abundantly because the mechanisms that make outputs usable are the same mechanisms that make checks on them empty.

The classes are a closed set.

| Class | Meaning |
|---|---|
| `structural_by_construction` | The output was produced under a structural constraint, so a structural check could not have failed |
| `producer_authored_criterion` | The criterion the check applied was produced by the same model, or in the same run, as the value checked |
| `producer_authored_test` | The test the value was checked against was produced by the model that produced the value |
| `self_assessment` | The check was an invocation asking the model whether its own output was correct |
| `same_model_review` | The check was an invocation of the same model registration as the producer |
| `tautological_criterion` | The criterion is satisfied by any output of the form the producer emits |
| `unfalsifiable_criterion` | No output would have failed the criterion |

**P13-3.29 (MUST) Vacuity classified and recorded.** An implementation must classify every check applied to a produced value against the closed set in section 3.6 and must record the class where any applies.

**P13-3.30 (MUST NOT) No vacuous check counted as a check.** An implementation must not count a check carrying a vacuity class towards any figure of checked values.

**P13-3.31 (MUST) Vacuity notified to the relying component.** An implementation must notify the component that consumed a produced value of the vacuity class of any check applied to it, so that the consumer can record that its own check established nothing.

**P13-3.32 (MUST NOT) No constrained output presented as validated.** An implementation must not present the structural conformance of an output produced under a structural constraint as evidence of anything, and must record the conformance as vacuous. **Source.** `Part 9` clause P9-12-38 forbids that component from reporting a validation of an instance produced under schema constrained generation as independent evidence of conformance; this clause is the same requirement stated from the producing side.

**P13-3.33 (MUST) Same model review recorded.** An implementation must record where a check invocation used the same model registration as the invocation that produced the value.

**P13-3.34 (MUST) Vacuous check population exposed.** An implementation must expose the proportion of checks applied to produced values that carry a vacuity class.

### 3.7 The reproducibility declaration

| Field | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `reproducibility_declaration_id` | identifier | yes | 1 | Not possible |
| `invocation_id` | identifier | yes | 1 | Not possible |
| `class` | enum(`bit_reproducible`,`distribution_reproducible`,`not_reproducible`,`unknown`) | yes | 1 | Not possible; the default is `unknown` |
| `basis` | enum(`provider_asserted_batch_invariance`,`local_deterministic_execution`,`inferred_from_parameters`,`none`) | yes | 1 | Not possible |
| `known_variance_sources` | enum, section 6.3 | yes | 1..n | Not possible; at least one source is always present |
| `replay_requirements` | text | yes | 1 | Not possible; what would be needed to attempt reproduction |
| `replay_achievable` | enum(`yes`,`no`,`unknown`) | yes | 1 | Not possible |
| `observed_variance` | structure: attempts, distinct outputs | no | 0..1 | No repeated invocation was performed |

**P13-3.35 (MUST) Class defaults to unknown.** An implementation must record a reproducibility class of unknown unless it holds a basis for a stronger class, and must not infer a stronger class from the parameters alone.

**P13-3.36 (MUST NOT) No determinism inferred from a temperature setting.** An implementation must not record an invocation as bit reproducible on the ground that its temperature was zero or that a seed was supplied. **Source.** Section 6.3 gives the evidence; a published experiment produced eighty distinct completions from one thousand invocations of one prompt at temperature zero.

**P13-3.37 (MUST) Variance sources enumerated per invocation.** An implementation must record which of the variance sources of section 6.3 were present for every invocation and must not record an empty set.

**P13-3.38 (MUST) Replay requirements stated.** An implementation must state what would be required to attempt reproduction of an invocation and whether it is achievable.

**P13-3.39 (MUST) Observed variance recorded where measured.** An implementation must record the number of attempts and the number of distinct outputs where it repeated an invocation, and must not report reproducibility from a single attempt.

**P13-3.40 (MUST) Batch invariance recorded as an assertion by the provider.** An implementation must record a claim of batch invariance as an assertion by the serving party, with its version, and must not record it as a verified property.

### 3.8 Cost, attempts and selection

| Field, cost record | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `cost_record_id` | identifier | yes | 1 | Not possible |
| `invocation_id` | identifier | yes | 1 | Not possible |
| `units` | structure: unit name, quantity | yes | 1..n | Not possible |
| `unit_definition_id` | identifier | yes | 1 | Not possible; the registered definition of the units, with its version |
| `monetary_amount` | structure: amount, currency | no | 0..1 | No monetary amount was resolved, which must not be read as no cost |
| `pricing_basis` | enum(`list`,`contracted`,`cached_discount`,`unknown`) | yes | 1 | Not possible |
| `incurred_despite_discard` | boolean | yes | 1 | Not possible |
| `attributed_to` | structure: work item ref, process instance ref, party | yes | 1 | Not possible |

| Field, attempt set | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `attempt_set_id` | identifier | yes | 1 | Not possible |
| `attempts` | identifier | yes | 1..n | Not possible |
| `selected_attempt_id` | identifier | no | 0..1 | No attempt was selected, which requires the outcome to name the exhaustion |
| `selection_basis` | identifier | no | 0..1 | No selection was made; required where one was |
| `discarded_retained` | boolean | yes | 1 | Not possible |
| `total_cost_units` | structure: unit name, quantity | yes | 1..n | Not possible; the sum across all attempts |

**P13-3.41 (MUST) Cost recorded per attempt.** An implementation must record cost against every attempt and must not record cost only against the attempt whose output was used.

**P13-3.42 (MUST) Cost of discarded attempts summed and exposed.** An implementation must record and expose the cost incurred by attempts whose outputs were discarded.

**P13-3.43 (MUST) Unit definition version recorded.** An implementation must record the registered definition and version of every cost unit it reports, since a provider may redefine what a unit counts.

**P13-3.44 (MUST NOT) No cross provider cost comparison.** An implementation must not present cost figures from two providers as comparable and must not aggregate them into one figure without recording that the units differ.

**P13-3.45 (MUST) Cost attributed to the work.** An implementation must attribute every cost to the unit of work, process instance and party that caused it, and must not aggregate cost only at the platform level.

**P13-3.46 (MUST) Pricing basis recorded.** An implementation must record whether a monetary amount rests on list pricing, contracted pricing, a cached discount or an unknown basis.

**P13-3.47 (MUST NOT) No cost figure presented as a measure of value.** An implementation must not present a cost or unit figure as a measure of productivity, quality or output.

**P13-3.48 (MUST) Discarded attempts retained.** An implementation must retain the produced value of every discarded attempt and must record where it did not.

**P13-3.49 (MUST) Selection recorded with a registered basis.** An implementation must record the basis on which an attempt was selected from a set, from a registered set of bases, and must not leave a selection unattributed.

**P13-3.50 (MUST NOT) No selection by attempt order.** An implementation must not select an attempt on the ground that it was the first to satisfy a condition, and must record a first satisfying selection as a selection by order with that basis named. **Source.** This is the sixth part of this standard to constrain resolution by declaration order, after `Part 2`'s salience, `Part 5`'s first match, `Part 6`'s branch order, `Part 7`'s first applicable and `Part 10`'s source precedence; section 13.7 records the repetition.

Clause P13-3.50 is not a prohibition on the practice, which is ubiquitous and often reasonable. It is a prohibition on the practice being invisible. Retrying until an output parses and taking the first that does is a selection whose basis is the order of attempts, and the discarded attempts are the variance the selection concealed. A system that records the surviving attempt and nothing else has hidden the distribution and reports the mode as the value.

**P13-3.51 (MUST) Variance across attempts exposed.** An implementation must expose, for every attempt set with more than one attempt, whether the attempts produced materially different outputs, so that a selection which concealed a disagreement is visible.

### 3.9 Agent runs, objectives, budgets and termination

| Field | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `agent_run_id` | identifier | yes | 1 | Not possible |
| `objective_id` | identifier | yes | 1 | Not possible |
| `initiating_party` | pin to party | yes | 1 | Not possible |
| `authorisation_ref` | pin to `Part 7` | yes | 1 | Not possible |
| `authority_envelope` | structure: permitted tools, permitted effect classes, permitted data scopes | yes | 1 | Not possible; see P13-3.57 |
| `step_budget` | integer | yes | 1 | Not possible |
| `cost_budget` | structure: unit, quantity | yes | 1..n | Not possible |
| `elapsed_budget` | duration | yes | 1 | Not possible |
| `effect_budget` | structure: effect class, maximum count | no | 0..n | No effect budget is declared, which forbids irreversible effects under P13-3.59 |
| `state` | enum, section 5.4 | yes | 1 | Not possible |
| `steps` | identifier | yes | 1..n | Not possible |
| `termination_reason` | enum, below | no | 0..1 | The run has not terminated |
| `objective_assertion` | enum(`asserted_achieved`,`asserted_not_achieved`,`no_assertion`) | no | 0..1 | The run has not terminated |
| `checking_determination_id` | identifier | no | 0..1 | No accountable party has determined whether the objective was achieved |
| `effects_recorded` | identifier | no | 0..n | The run caused no recorded effect outside itself |

Termination reasons, closed enumeration: `step_budget_exhausted`, `cost_budget_exhausted`, `elapsed_budget_exhausted`, `effect_budget_exhausted`, `agent_asserted_completion`, `halted_by_party`, `halted_by_guard`, `repetition_detected`, `tool_unavailable`, `authority_exceeded_refused`, `provider_error`, `unrecoverable`.

**P13-3.52 (MUST) Objective recorded before the run.** An implementation must record the objective before the first step and must not amend it during the run.

**P13-3.53 (MUST) Four budgets declared and finite.** An implementation must declare a finite step budget, cost budget and elapsed budget for every agent run, and must refuse to start a run lacking any of them. The values are implementation decisions because the useful bounds depend on the objective, which this part does not constrain.

**P13-3.54 (MUST) Budget exhaustion is a termination reason, not a failure.** An implementation must record the exhaustion of a budget as a termination reason and must not record it as an error of the agent or of this component.

**P13-3.55 (MUST NOT) No agent assertion recorded as an outcome.** An implementation must record an agent's assertion that it completed its objective as an assertion by the agent and must not record it as a determination that the objective was achieved.

**P13-3.56 (MUST) Objective determination obtained, not made.** An implementation must obtain any determination that an objective was achieved from an accountable party outside this component and must record it as received.

**P13-3.57 (MUST) Authority envelope declared and bounded by the initiating party.** An implementation must declare the tools, effect classes and data scopes an agent run may use, and must not declare an envelope exceeding the authority the initiating party holds.

**P13-3.58 (MUST) Authority exceeded refused and recorded.** An implementation must refuse a step outside the declared authority envelope, must record the refusal, and must terminate the run with the reason naming it.

**P13-3.59 (MUST NOT) No irreversible effect without a declared effect budget.** An implementation must not permit a step with an irreversible effect class in a run that declares no effect budget.

**P13-3.60 (MUST) Effects enumerated per run.** An implementation must record every effect a run caused outside itself, so that the consequences of a run are enumerable without inspecting the systems it touched.

**P13-3.61 (MUST) Repetition detected and bounded.** An implementation must detect repetition of a step pattern within a run, must declare the bound at which it terminates, and must record the detection.

**P13-3.62 (MUST NOT) No termination reason recorded as achievement.** An implementation must not record any termination reason as establishing that the objective was achieved, including `agent_asserted_completion`.

### 3.10 Tools and their effects

| Field, tool registration | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `tool_registration_id` | identifier | yes | 1 | Not possible |
| `tool_name` | string | yes | 1 | Not possible |
| `effect_class` | enum(`none`,`reversible`,`idempotent`,`irreversible`) | yes | 1 | Not possible |
| `reversal_procedure_ref` | pin | no | 0..1 | No reversal procedure exists, which forbids the class `reversible` |
| `authority_required` | structure: permissions | yes | 1..n | Not possible |
| `argument_schema_ref` | pin to `Part 9` | yes | 1 | Not possible |
| `result_schema_ref` | pin to `Part 9` | no | 0..1 | The tool returns nothing structured |
| `retry_safe` | boolean | yes | 1 | Not possible |

| Field, tool call record | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `tool_call_id` | identifier | yes | 1 | Not possible |
| `tool_registration_id` | identifier | yes | 1 | Not possible |
| `agent_run_id` | identifier | yes | 1 | Not possible |
| `arguments_address` | address | yes | 1 | Not possible |
| `arguments_origin` | enum(`model_produced`,`template_fixed`,`party_supplied`) | yes | 1 | Not possible; see P13-3.65 |
| `result_address` | address | no | 0..1 | The call returned nothing or failed |
| `outcome` | enum, section 7.4 | yes | 1 | Not possible |
| `effects_caused` | text | no | 0..n | The call caused no effect outside itself |
| `reversed_at` | instant | no | 0..1 | The effect was not reversed |
| `authorisation_ref` | pin to `Part 7` | yes | 1 | Not possible |

**P13-3.63 (MUST) Tools registered before use.** An implementation must register every tool with its effect class, its required authority and its argument schema before an agent may call it.

**P13-3.64 (MUST) Effect class declared per tool.** An implementation must declare the effect class of every tool and must not admit a tool whose effect class is undeclared.

**P13-3.65 (MUST) Argument origin recorded.** An implementation must record whether a tool call's arguments were produced by the model, fixed by a template or supplied by a party, since arguments a model produced are a produced value and carry that status.

**P13-3.66 (MUST) Arguments validated against the registered schema.** An implementation must obtain validation of tool call arguments against the registered schema from `Part 9` before the call and must refuse a call whose arguments do not validate.

**P13-3.67 (MUST NOT) No validation of arguments treated as a check of their content.** An implementation must not record the structural validation of model produced arguments as establishing that the arguments are correct.

**P13-3.68 (MUST) Authorisation per call.** An implementation must obtain an authorisation decision for every tool call and must not rely on a decision obtained for the run.

**P13-3.69 (MUST) Effects recorded per call.** An implementation must record what every tool call changed outside itself.

**P13-3.70 (MUST NOT) No retry of a call that is not retry safe.** An implementation must not retry a tool call whose registration records it as not retry safe, and must record the refusal.

### 3.11 Defect notification and enumeration

`Part 7` requires this component to treat a model found defective as a basis defect so that the decisions relying on it can be enumerated. The requirement generalises: every component that consumed a produced value needs to be able to find what it consumed when the producer turns out to have been faulty.

| Field | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `defect_notification_id` | identifier | yes | 1 | Not possible |
| `subject` | enum(`model`,`model_version`,`serving_configuration`,`prompt_version`,`tool`) | yes | 1 | Not possible |
| `subject_ref` | identifier | yes | 1 | Not possible |
| `defect_description` | text | yes | 1 | Not possible |
| `discovered_at` | instant | yes | 1 | Not possible |
| `affected_interval` | interval | yes | 1 | Not possible |
| `raised_by` | pin to party | yes | 1 | Not possible |
| `affected_invocations` | identifier | no | 0..n | The enumeration has not been performed or could not be completed |
| `enumeration_completeness` | enum(`complete`,`partial`,`not_performed`) | yes | 1 | Not possible |
| `notified_components` | identifier | no | 0..n | No consuming component was notified |

**P13-3.71 (MUST) Defect notification raised and propagated.** An implementation must raise a defect notification on being informed that a model, version, serving configuration, prompt version or tool was defective, and must notify every component that consumed a value produced by it in the affected interval.

**P13-3.72 (MUST) Affected invocations enumerated.** An implementation must enumerate the invocations falling within the affected interval and must record whether the enumeration is complete.

**P13-3.73 (MUST NOT) No partial enumeration presented as complete.** An implementation must not present a partial enumeration as complete and must state what it could not reach.

**P13-3.74 (MUST) Notification to the ledger as a basis defect.** An implementation must notify `Part 3` of a defect notification as a defect in the basis of every determination that consumed an affected value.

**P13-3.75 (MUST) Consumers identified by their own registration.** An implementation must maintain a register of components that consume produced values and must record where a consumer of an affected value could not be identified.

**P13-3.76 (MUST) Unidentifiable consumer population exposed.** An implementation must expose the count of produced values whose consumers it cannot identify, since those are the values a defect notification cannot reach.

### 3.12 Prompts and instruction material

**P13-3.77 (MUST) Instruction material versioned as a document.** An implementation must hold every instruction material used in an invocation as a version governed by `Part 1` and referenced by address in `Part 11`.

**P13-3.78 (MUST) Instruction version pinned per invocation.** An implementation must pin the version of every instruction material an invocation used and must not resolve it to the current version.

**P13-3.79 (MUST NOT) No instruction material held inline.** An implementation must not hold instruction material as an attribute of a configuration and must hold it as an addressed, versioned artifact.

**P13-3.80 (MUST) Assembly order recorded.** An implementation must record the order in which the components of a context assembly were arranged, since the order affects the output and is not recoverable from the parts.

**P13-3.81 (MUST) Retrieved material pinned.** An implementation must record every retrieved item that entered a context assembly by address and, where the item came from another component, by that component's own pin.

**P13-3.82 (MUST) Truncation recorded.** An implementation must record where any part of a context assembly was truncated, elided or summarised before the invocation, and must record what was removed.

### 3.13 Projections

**P13-3.83 (MUST) Projections marked as such.** An implementation must mark every projection it exposes as a projection and must not permit a projection to be cited as a record.

**P13-3.84 (MUST) Produced status carried into every projection.** An implementation must carry the produced status and the checking status of a value into every projection that exposes it.

**P13-3.85 (MUST NOT) No aggregate that loses the produced and checked distinction.** An implementation must not expose an aggregate over values that does not separate produced from checked.

**P13-3.86 (MUST NOT) No quality or accuracy figure exposed.** An implementation must not expose a figure purporting to measure the accuracy, quality or correctness of the values it produced, and section 13.6 states why.

### 3.14 Worked demonstration

The demonstration is narrative and binds nothing.

A case worker's work item in `Part 8` requires a document to be classified. The classification is obtained from a model. Under `Part 7` clause P7-12.35 the invocation must not occur during a policy evaluation, so it occurs beforehand and its output is pinned.

The invocation names a provider alias. Under clause P13-3.15 its identity class is `provider_alias` and its verifiability is `unverifiable`, and under clause P13-3.18 the reproducibility class is therefore `unknown` whatever the parameters were. The temperature was zero and a seed was supplied; under clause P13-3.36 neither may be recorded as establishing bit reproducibility, and the variance sources recorded include batch composition, which is outside anyone's control.

The output is required as one of four labels, so it is produced under a choice set constraint. Under clause P13-3.26 the invocation records `constrained_generation` of `choice_set`. `Part 9` validates the output against the schema and, under its own clause P9-12-38 and this part's clause P13-3.32, that validation establishes nothing: the output could not have been anything else. The vacuity class `structural_by_construction` is recorded and under clause P13-3.31 `Part 9` is notified, so its own validation record carries the fact that its check was vacuous.

Three attempts were made because the first two returned nothing parseable. All three are invocation records, all three have cost records, and under clause P13-3.42 the cost of the two discarded attempts is exposed. The third was selected. Under clause P13-3.50 the selection basis is recorded as selection by order, because it was the first that parsed, and under clause P13-3.51 the fact that the three attempts disagreed is exposed rather than concealed by the survivor.

The produced value reaches the work item as a proposal. Under `Part 8` clause P8-12-36 that component records whether the performer accepted it unchanged, and under `Part 8` clause P8-3-31 the performer's presentation pin records how many outcomes were available to them. If the interface offered only the model's label and an accept button, `Part 8`'s choice breadth is one and its own clause P8-3-32 records the presentation as constrained. So the estate can now distinguish a classification a person examined from one a person clicked past, which is the distinction that determines whether the value is checked.

Eleven months later the provider discloses that the alias served a different model for a fortnight. Under clause P13-3.71 a defect notification is raised, under clause P13-3.72 the invocations in the interval are enumerated, and under clause P13-3.74 `Part 3` is notified that the basis of every determination consuming those values is defective. Under clause P13-3.76 the values whose consumers cannot be identified are counted separately, and that count is the part of the exposure nobody can remediate.

## 4. Interfaces

### 4.1 Interface principles

Almost every operation of this component either invokes something outside it or writes a record about having done so. That shape has one consequence worth stating before the operations: this component is the only one in the standard whose ordinary functioning causes an external party to be paid and an external system to change. Every other component's interface can be exercised in a test without consequence. This one cannot, and section 4.5 is written accordingly.

**P13-4.1 (MUST) Operations defined over the entities of section 3.** An implementation must define every operation it exposes in terms of the entities of section 3 and must state which records each creates and which events it emits.

**P13-4.2 (MUST) Idempotency key accepted.** An implementation must accept a caller supplied idempotency key on every operation and must return the original result when invoked again with the same key and arguments.

**P13-4.3 (MUST NOT) No idempotency claim over the output.** An implementation must not represent an idempotent operation as producing the same output on repetition, and must confine idempotence to the effect on its own records and on external effects.

Clause P13-4.3 is the distinction that ordinary idempotency conventions do not make. A repeated request with the same key must not cause a second invocation and a second charge; it must not be represented as establishing that a second invocation would have returned the same value.

**P13-4.4 (MUST) Authorisation obtained per invocation and per tool call.** An implementation must obtain an authorisation decision from `Part 7` before every invocation and every tool call, and must record the reference.

**P13-4.5 (MUST) One outcome per operation.** An implementation must return exactly one outcome from section 7 for every operation.

**P13-4.6 (MUST) Refusals recorded.** An implementation must record every refused operation with the requesting party, the instant and the refusal code.

**P13-4.7 (MUST NOT) No operation that alters an invocation record or a produced value.** An implementation must not expose an operation that changes either.

**P13-4.8 (MUST NOT) No operation returning a value marked checked.** An implementation must not expose an operation whose result is a value marked as checked.

### 4.2 Invocation operations

| Operation | Effect |
|---|---|
| `assemble_context` | Records a context assembly from addressed material with its order |
| `invoke` | Performs one invocation, creating an invocation record, a produced value, a cost record and a reproducibility declaration |
| `invoke_attempt_set` | Performs several attempts under a declared budget, creating an attempt set |
| `select_attempt` | Records the selection of an attempt with a registered basis |
| `repeat_for_variance` | Performs repeated invocations to measure observed variance and records it |
| `record_cache_hit` | Records that a value was returned from an earlier invocation |
| `register_model` | Registers a model with its identity class and verifiability |
| `register_serving_configuration` | Registers a serving configuration with any batch invariance assertion |
| `register_cost_unit_definition` | Registers a cost unit definition with its version |

**P13-4.9 (MUST) Invocation refused without attribution.** An implementation must refuse an invocation that names no unit of work, initiating party and authorising decision.

**P13-4.10 (MUST) Invocation refused without a registered model.** An implementation must refuse an invocation naming a model that is not registered.

**P13-4.11 (MUST) Invocation refused where the model status forbids it.** An implementation must refuse an invocation against a model whose status is withdrawn or under defect investigation, and must record the refusal.

**P13-4.12 (MUST) Attempt set refused without a budget.** An implementation must refuse `invoke_attempt_set` that declares no maximum attempt count and no cost budget.

**P13-4.13 (MUST) Selection refused without a registered basis.** An implementation must refuse `select_attempt` that names no registered selection basis.

**P13-4.14 (MUST) Cache hit refused without the source or its declared absence.** An implementation must refuse `record_cache_hit` that neither names the source invocation nor records that the source is unknown.

**P13-4.15 (MUST NOT) No invocation without a context assembly record.** An implementation must not perform an invocation for which no context assembly has been recorded.

### 4.3 Agent operations

| Operation | Effect |
|---|---|
| `declare_objective` | Records an objective before a run |
| `open_run` | Opens an agent run with its authority envelope and four budgets |
| `step` | Records one invocation or tool call within a run |
| `call_tool` | Performs a tool call with recorded arguments, result and effects |
| `reverse_effect` | Records the reversal of a reversible effect |
| `halt_run` | Halts a run at the request of a party |
| `close_run` | Closes a run with a termination reason |
| `record_objective_determination` | Records a determination received from an accountable party |
| `register_tool` | Registers a tool with its effect class and schemas |

**P13-4.16 (MUST) Run refused without four budgets.** An implementation must refuse `open_run` lacking a finite step budget, cost budget or elapsed budget.

**P13-4.17 (MUST) Run refused without an authority envelope.** An implementation must refuse `open_run` lacking a declared authority envelope.

**P13-4.18 (MUST) Run refused where the envelope exceeds the initiating party's authority.** An implementation must refuse `open_run` whose envelope exceeds the authority the initiating party holds, as determined by `Part 7`.

**P13-4.19 (MUST) Step refused outside the envelope.** An implementation must refuse a step outside the declared envelope and must terminate the run with the reason naming it.

**P13-4.20 (MUST) Halt available to a party at any step.** An implementation must permit an authorised party to halt a run between steps and must record the halt as a termination reason.

**P13-4.21 (MUST) Close refused without a termination reason.** An implementation must refuse `close_run` that names no termination reason from the closed set.

**P13-4.22 (MUST NOT) No objective determination accepted from the run.** An implementation must not accept a determination that an objective was achieved from the agent, the run or any invocation within it.

**P13-4.23 (MUST) Tool call refused where the tool is unregistered.** An implementation must refuse a tool call naming an unregistered tool.

**P13-4.24 (MUST) Tool call refused where arguments do not validate.** An implementation must refuse a tool call whose arguments do not validate against the registered schema.

### 4.4 Reading operations

**P13-4.25 (MUST) Invocation retrievable with its full record.** An implementation must expose retrieval of an invocation with its context assembly, produced value, cost record, reproducibility declaration and attribution.

**P13-4.26 (MUST) Point in time query supported.** An implementation must answer, for any stated past instant, the registered model identity, serving configuration and instruction version then in force.

**P13-4.27 (MUST) Attempt set retrievable in full.** An implementation must expose every attempt of an attempt set, including discarded attempts, and must not expose only the selected one.

**P13-4.28 (MUST) Produced value carries its status on every read.** An implementation must return the produced status, the checking status and any vacuity class with every produced value it returns.

**P13-4.29 (MUST) Run retrievable with every step and effect.** An implementation must expose an agent run with every step, every tool call and every recorded effect.

**P13-4.30 (MUST NOT) No state change from a read.** An implementation must not change any state other than a read record in response to a reading operation.

**P13-4.31 (MUST) Affected invocation query supported.** An implementation must answer, for any stated model, version, serving configuration, instruction version or tool and any interval, the invocations affected.

### 4.5 What a caller may and may not assume

**P13-4.32 (MUST NOT) No assumption of reproducibility.** A caller must not assume that repeating an invocation will yield the same output, and must read the reproducibility declaration.

**P13-4.33 (MUST NOT) No assumption that a validated output is a correct one.** A caller must not read the structural validity of a produced value as evidence about its content.

**P13-4.34 (MUST NOT) No assumption that a produced value was checked.** A caller must not treat a produced value as checked in the absence of a checking determination, and must read the status.

**P13-4.35 (MUST NOT) No assumption that a named model is the model that answered.** A caller must not assume the responding model was the requested model, and must read both.

**P13-4.36 (MUST NOT) No assumption that an agent's termination means success.** A caller must not read a termination reason as a determination that the objective was achieved.

**P13-4.37 (MUST NOT) No assumption that an operation is free of external effect.** A caller must not assume that invoking any operation of this component is without cost or external effect, and this component must not expose an operation that gives that impression.

**P13-4.38 (MUST) Cost visible before commitment where a budget applies.** A caller may rely on this component refusing an invocation that would exceed a declared cost budget, per clause P13-6.29.

### 4.6 Reads from other components

| Read | Component | Pinning | On failure |
|---|---|---|---|
| Authorisation decision | `Part 7` | policy version pinned per decision | deny the invocation or tool call; never proceed on failure |
| Instruction material and model card versions | `Part 1` | pinned per invocation | refuse the invocation |
| Prompt, document, tool result and output octets | `Part 11` | content address | refuse the invocation; report the material unresolvable |
| Argument and result schema validation | `Part 9` | schema version pinned | refuse the tool call |
| Party identity for initiating and accountable parties | `Part 10` | snapshot pinned per record | refuse the operation |
| Work item context for a proposal or an adjudication | `Part 8` | work item reference | do not produce a proposal into an unidentified work item |
| Checking determination | `Part 8` or `Part 12` | received and recorded unaltered | record the value as unchecked |

**P13-4.39 (MUST) Reads treated as fallible.** An implementation must treat every read in the table in section 4.6 as fallible and must apply the stated failure behaviour rather than a default.

**P13-4.40 (MUST NOT) No proceeding on an authorisation failure.** An implementation must not proceed with an invocation or a tool call when the authorisation read fails.

**P13-4.41 (MUST NOT) No invocation on unresolvable material.** An implementation must not invoke a model on a context assembly any part of which could not be resolved, and must record the refusal.

### 4.7 Events emitted

**P13-4.42 (MUST) Event per invocation and per tool call.** An implementation must emit an event for every invocation and every tool call, carrying the outcome, the cost, the produced status and the attribution.

**P13-4.43 (MUST) Events delivered to the ledger.** An implementation must deliver every event to `Part 3` at least once and must retain the event until delivery is acknowledged.

**P13-4.44 (MUST) Distinct event class for a refusal by the model.** An implementation must emit a distinct event class for a refusal and must not emit it as an error.

**P13-4.45 (MUST) Distinct event class for a provider filter.** An implementation must emit a distinct event class for an intervention by the serving party.

**P13-4.46 (MUST) Distinct event class for an irreversible effect.** An implementation must emit a distinct event class for every step that caused an irreversible effect.

**P13-4.47 (MUST) Distinct event class for authority exceeded.** An implementation must emit a distinct event class where a step was refused for exceeding the authority envelope.

**P13-4.48 (MUST) Defect notification event names the affected interval.** An implementation must emit an event on raising a defect notification, naming the subject, the interval and the enumeration completeness.

**P13-4.49 (MUST) Responding model change event.** An implementation must emit an event on detecting that the content behind a provider alias changed.

**P13-4.50 (MUST) Budget exhaustion event.** An implementation must emit an event on the exhaustion of any budget, naming which.

**P13-4.51 (SHOULD) Attempt divergence signal.** An implementation should emit an event where the attempts in an attempt set produced materially different outputs and a selection was made among them.

## 5. State model

### 5.1 Five state models

The five answer different questions. The model registration state answers whether a model may be invoked. The invocation state answers whether one request completed and how. The produced value state answers what has since been determined about an output. The agent run state answers whether a run is proceeding, halted or terminated and why. And the effect state answers whether something a run did to the world has been reversed.

The effect state is the one no other part of this standard has an analogue for, and it exists because this is the only component that acts outside the system on its own initiative between one authorisation and the next.

**P13-5.1 (MUST) States held as transitions.** An implementation must hold every state as a sequence of recorded transitions and must not hold it as a mutable field.

**P13-5.2 (MUST) One state per axis per instant.** An implementation must not represent two states of one entity on one axis as simultaneously current.

**P13-5.3 (MUST NOT) No derivation of one axis from another.** An implementation must not derive a produced value's checking status from the state of the invocation that produced it.

**P13-5.4 (MUST) Transitions carry authorisation where required.** An implementation must record the authorising decision reference on every transition that requires one under section 4.

**P13-5.5 (MUST) Illegal transitions recorded.** An implementation must record every refused transition and must not discard the attempt.

**P13-5.6 (MUST NOT) No unlisted transition.** An implementation must not admit a transition this section does not list.

### 5.2 Model registration state

| State | Meaning | Terminal |
|---|---|---|
| `registered` | Registered and invocable | no |
| `under_defect_investigation` | A defect is suspected; not invocable, records retained | no |
| `defective` | A defect is established; not invocable, affected invocations enumerated | no |
| `deprecated` | Not to be used for new work; remains invocable for declared continuity | no |
| `withdrawn` | Not invocable | yes |

Legal transitions: to `registered` on registration; `registered` to `under_defect_investigation` on a suspicion recorded; `under_defect_investigation` to `registered` on the suspicion being cleared, with the clearance recorded; `under_defect_investigation` to `defective` on the defect being established; `defective` to `registered` on remediation by the provider, recorded as a new serving configuration; `registered` or `deprecated` to `withdrawn`; `registered` to `deprecated`; `deprecated` to `registered` on reinstatement with a reason.

**P13-5.7 (MUST) Investigation suspends invocation.** An implementation must refuse new invocations against a model under defect investigation and must record the refusals.

**P13-5.8 (MUST) Defect state triggers enumeration.** An implementation must perform the enumeration of section 3.11 on a model entering the defective state.

**P13-5.9 (MUST) Remediation recorded as a new configuration.** An implementation must record a provider's remediation of a defect as a new serving configuration and must not return the prior configuration to the registered state.

**P13-5.10 (MUST) Withdrawn models still resolvable.** An implementation must continue to resolve a withdrawn model registration, since invocation records cite it.

### 5.3 Invocation state

| State | Meaning | Terminal |
|---|---|---|
| `requested` | Sent and not yet resolved | no |
| `completed` | Resolved with an outcome from section 7.2 | yes |
| `abandoned` | The caller ceased to await a result; cost may still have been incurred | yes |
| `unresolved` | No outcome was ever determined, for a recorded reason | yes |

**P13-5.11 (MUST) Abandonment does not cancel cost.** An implementation must record cost against an abandoned invocation where cost was incurred and must not record an abandoned invocation as free.

**P13-5.12 (MUST) Unresolved distinguished from failed.** An implementation must distinguish an invocation whose outcome was never determined from one that completed with a failure outcome.

**P13-5.13 (MUST NOT) No invocation state reopened.** An implementation must not return a terminal invocation to `requested` and must express a further attempt as a new invocation.

### 5.4 Agent run state

| State | Meaning | Terminal |
|---|---|---|
| `declared` | Objective and budgets recorded, no step taken | no |
| `running` | At least one step taken, no termination | no |
| `paused` | Halted between steps, resumable | no |
| `terminated` | Stopped with a recorded termination reason | no |
| `settled` | Terminated, every reversible effect reversed or accepted, and the objective determination received or its absence recorded | yes |

Legal transitions: to `declared` on declaration; `declared` to `running` on the first step; `declared` to `terminated` without a step; `running` to `paused` on a halt; `paused` to `running` on resumption with an authorisation; `paused` to `terminated`; `running` to `terminated`; `terminated` to `settled`.

**P13-5.14 (MUST) Termination is not settlement.** An implementation must distinguish a run that stopped from one whose effects and objective determination have been resolved, and must not treat termination as the end of the record.

**P13-5.15 (MUST) Unsettled run population exposed.** An implementation must expose every terminated run that has not settled, with the effects outstanding and whether an objective determination is awaited.

**P13-5.16 (MUST) Resumption authorised afresh.** An implementation must obtain a new authorisation decision to resume a paused run and must not rely on the decision that opened it.

**P13-5.17 (MUST NOT) No settlement without effect resolution.** An implementation must not record a run as settled while any reversible effect it caused is neither reversed nor recorded as accepted by an accountable party.

### 5.5 Produced value state

| State | Meaning | Terminal |
|---|---|---|
| `produced` | Produced and no determination received | no |
| `consumed_unchecked` | Consumed by another component with no checking determination | no |
| `checked` | A checking determination was received from an accountable party | no |
| `checked_vacuously` | A check was applied and carries a vacuity class | no |
| `rejected` | An accountable party determined the value unfit | yes |
| `defect_affected` | The producing model, version or configuration was found defective | no |
| `superseded` | Replaced by a later produced value for the same purpose | no |

**P13-5.18 (MUST) Consumed unchecked recorded as a state, not inferred.** An implementation must record that a produced value was consumed without a checking determination and must not leave the condition to be inferred from the absence of a record.

**P13-5.19 (MUST) Vacuous check does not reach checked.** An implementation must not transition a produced value to `checked` on a check carrying a vacuity class.

**P13-5.20 (MUST) Defect affected applies retrospectively.** An implementation must transition every produced value in a defect's affected interval to `defect_affected`, including values already checked, and must notify the consuming component.

**P13-5.21 (MUST NOT) No defect affected value silently superseded.** An implementation must not resolve a defect by producing a replacement value and superseding the affected one without recording the defect and notifying the consumer.

### 5.6 Effect state

| State | Meaning | Terminal |
|---|---|---|
| `caused` | An effect occurred outside this component | no |
| `reversed` | The effect was reversed and the reversal recorded | yes |
| `accepted` | An accountable party accepted the effect as it stands | yes |
| `irreversible` | The effect cannot be reversed and was not accepted | no |
| `reversal_failed` | Reversal was attempted and did not succeed | no |

**P13-5.22 (MUST) Irreversible effects exposed until accepted.** An implementation must expose every effect in the `irreversible` state until an accountable party accepts it.

**P13-5.23 (MUST) Reversal failure recorded, not retried silently.** An implementation must record a failed reversal, must not retry it without an authorisation, and must expose it.

**P13-5.24 (MUST NOT) No effect state terminal without an accountable act.** An implementation must not treat an effect as resolved other than by a recorded reversal or a recorded acceptance.

## 6. Execution semantics

### 6.1 What is determinate and what is not

Two things in this component are determinate and everything else is not. The record of what was sent is determinate, because this component composed it. The record of what came back is determinate, because this component received it. Everything about the relationship between the two is not, and section 6.3 states why with its evidence.

The design consequence runs through the whole part: this component's guarantees are about its records and never about its outputs. It can guarantee that the context assembly recorded is the context assembly sent, that the produced value recorded is the value received, that the cost recorded was incurred and that the attribution recorded is the work that caused it. It can guarantee nothing about what a second invocation would return.

**P13-6.1 (MUST) Record fidelity guaranteed.** An implementation must guarantee that the context assembly it records is the input it sent and that the produced value it records is the output it received, and must record any case in which it cannot.

**P13-6.2 (MUST NOT) No guarantee offered over outputs.** An implementation must not offer, publish or imply a guarantee about what an invocation will return.

**P13-6.3 (MUST) Input digest recorded.** An implementation must record a digest over the exact input sent, so that a claim that a given input produced a given output is testable as to the input.

**P13-6.4 (MUST NOT) No clock or environment in a recorded input.** An implementation must record any value in a context assembly that varied with the instant or the environment, so that an input that cannot be reconstituted is visible as such.

### 6.2 Context assembly

**P13-6.5 (MUST) Assembly composed from addressed material.** An implementation must compose every context assembly from material held by address and must record the address of each part.

**P13-6.6 (MUST) Order recorded as part of the assembly.** An implementation must record the order of the parts and must treat a change of order as a different assembly.

**P13-6.7 (MUST) Assembly digest recorded.** An implementation must record a digest over the assembled input and must record the digest with the invocation.

**P13-6.8 (MUST) Truncation recorded with what was removed.** An implementation must record every truncation, elision or summarisation applied during assembly, together with the address of the material removed.

**P13-6.9 (MUST NOT) No silent context substitution.** An implementation must not substitute, reorder or summarise material after recording an assembly and before sending it.

**P13-6.10 (MUST) Retrieved material attributed to its source component.** An implementation must record, for every retrieved item, the component that supplied it and that component's own pin, so that a produced value resting on stale reference content is traceable.

### 6.3 Non determinism, and why reproducibility is the exception

This subsection is the finding on which the achievable scope of this part depends, and it is the one place where recent published work settles a question that practice still gets wrong.

The common account of why model outputs vary is that floating point arithmetic is not associative and that parallel hardware completes work in an unpredictable order. That account is largely wrong for inference. Most kernels in a transformer forward pass avoid atomic accumulation and use fixed reduction trees, so for a fixed input shape and schedule they are bitwise repeatable. The variance comes from somewhere else: serving systems batch concurrent requests, several kernels are not invariant to the size and composition of the batch, and the batch a request lands in depends on the load the server is under at that instant. So the numerical path taken by one request depends on other parties' traffic.

The measured consequence is severe. In the published experiment, one thousand completions of a single prompt at temperature zero on one model produced eighty distinct completions, the most frequent occurring seventy eight times. Deterministic execution is achievable, by replacing the non invariant kernels with batch invariant implementations, at a throughput cost reported in the original work at around sixty per cent and reduced by later integration work to around a third. It is achievable and it is not what a hosted endpoint does by default.

Three conclusions follow and each is a clause. An invocation is not a function of its inputs, because it is also a function of the concurrent load. A temperature of zero and a supplied seed establish nothing about reproducibility, because the seed governs sampling and not the forward pass numerics. And a claim of determinism can only rest on an assertion by the party operating the serving stack, which is an assertion and not a verified property.

**P13-6.11 (MUST) Variance sources enumerated.** An implementation must draw the recorded variance sources of every invocation from the following closed set: `sampling_parameters`, `seed_absent`, `batch_composition`, `serving_stack_version`, `model_identity_unverifiable`, `quantisation`, `hardware_class`, `routing_variability`, `prefix_or_cache_reuse`, `context_assembly_variability`, `tool_result_variability`, `retrieved_material_variability`, `provider_filter`, `clock_or_randomness_in_input`.

**P13-6.12 (MUST) Batch composition recorded as present unless invariance is asserted.** An implementation must record `batch_composition` as a variance source for every invocation served by a system that does not assert batch invariance. **Source.** Published work of September 2025 attributes the non determinism of temperature zero inference principally to the absence of batch invariance in reduction kernels, notes that the batch a request is served in depends on concurrent load, and records that the effect is not specific to any one class of accelerator.

**P13-6.13 (MUST NOT) No determinism from temperature or seed.** An implementation must not record a reproducibility class stronger than unknown on the basis of a temperature setting or a supplied seed. **Source.** The same work reports one thousand temperature zero completions of a single prompt yielding eighty distinct outputs, and the seed governs sampling rather than the numerics of the forward pass.

**P13-6.14 (MUST) Batch invariance recorded as an assertion with a version.** An implementation must record a claim of batch invariance as an assertion by the serving party, with the version of the serving configuration to which it applies, and must not record it as verified.

**P13-6.15 (MUST) Distribution reproducibility distinguished from bit reproducibility.** An implementation must distinguish a claim that repeated invocation yields the same output from a claim that it yields outputs from the same distribution, and must not report the second as the first.

**P13-6.16 (MUST) Observed variance measured before a reproducibility claim.** An implementation must not record a reproducibility class of bit reproducible without having measured repeated invocations and recorded the count of distinct outputs.

**P13-6.17 (MUST) Cost of determinism recorded where claimed.** An implementation must record, where it operates a deterministic serving configuration, the throughput or latency cost of doing so, since the cost is what determines whether the configuration will survive.

**P13-6.18 (MUST NOT) No replay presented as reproduction.** An implementation must not present the replay of a recorded produced value as the reproduction of an invocation, and must record a replay as the reuse of a record.

### 6.4 Retry and attempt sets

A retry in this subject is not a retry. In ordinary systems a retry is a second attempt at the same operation, justified by the assumption that the operation is a function of its inputs and that the first attempt failed for an incidental reason. Here the second attempt is a different draw, and the practice called retry is usually a search: attempt until an output is usable, then take it.

**P13-6.19 (MUST) Every retry recorded as a new invocation.** An implementation must record every retry as a new invocation with its own record, produced value, cost and reproducibility declaration.

**P13-6.20 (MUST NOT) No retry represented as re attempting one invocation.** An implementation must not represent a set of attempts as one invocation that eventually succeeded.

**P13-6.21 (MUST) Attempt set bounded.** An implementation must declare a maximum attempt count and a cost bound for every attempt set and must record the bound reached.

**P13-6.22 (MUST) Exhaustion is an outcome.** An implementation must record the exhaustion of an attempt bound as the outcome `retry_exhausted` and must not record it as a failure of the last attempt.

**P13-6.23 (MUST) Retry on failure distinguished from search for a usable output.** An implementation must record whether an attempt set was made because prior attempts failed to complete or because prior outputs were judged unusable, since the two justify different conclusions about the result.

**P13-6.24 (MUST NOT) No retry of an invocation with an unreversed irreversible effect.** An implementation must not retry an invocation or tool call that caused an unreversed irreversible effect.

**P13-6.25 (MUST) Effect class checked before retry.** An implementation must check the effect class of an operation before retrying it and must refuse to retry one recorded as not retry safe.

**P13-6.26 (MUST) Selection basis registered and recorded.** An implementation must record the basis of every selection among attempts from a registered set and must not perform a selection with no recorded basis.

**P13-6.27 (MUST) Discarded outputs retained and countable.** An implementation must retain every discarded output and must expose the count and cost of discarded attempts per unit of work.

### 6.5 Cost

**P13-6.28 (MUST) Cost recorded in provider units and not normalised.** An implementation must record cost in the units the provider meters and must not convert them to a common unit without recording the conversion and its basis.

**P13-6.29 (MUST) Budget checked before invocation.** An implementation must refuse an invocation that would exceed a declared cost budget and must record the refusal as `budget_exhausted`.

**P13-6.30 (MUST NOT) No budget decision made here.** An implementation must not determine whether a budget should be raised, and must obtain that decision from the party that owns the budget.

**P13-6.31 (MUST) Cost attributed at the grain of the work.** An implementation must attribute cost to the work item, process instance or agent run that caused it, and must expose cost at that grain rather than only in aggregate.

**P13-6.32 (MUST) Cache hit cost recorded distinctly.** An implementation must record the cost of a cache hit distinctly from the cost of an invocation, since the two are not comparable measures of the same thing.

**P13-6.33 (MUST NOT) No cost figure aggregated across unit definitions.** An implementation must not aggregate cost figures across differing unit definitions or unit definition versions into one total.

**P13-6.34 (MUST) Unit definition change surfaces the affected population.** An implementation must expose the invocations recorded under a superseded cost unit definition when the definition changes, since their figures are not comparable with later ones.

### 6.6 Agent execution

This subsection is deliberately thin, and section 13.5 states why. What is specified here is the bounding, the recording and the refusals. What is not specified is anything about how an agent should decide what to do, which this part does not attempt.

**P13-6.35 (MUST) Steps counted against the budget.** An implementation must count every invocation and every tool call against the step budget and must terminate on exhaustion.

**P13-6.36 (MUST) Cost accumulated across the run.** An implementation must accumulate cost across every step of a run against the run's cost budget.

**P13-6.37 (MUST) Authority checked per step, not per run.** An implementation must check every step against the authority envelope and must obtain an authorisation decision for every tool call.

**P13-6.38 (MUST NOT) No authority accretion.** An implementation must not permit a run to acquire an authority during the run that it did not hold at its opening.

**P13-6.39 (MUST) Repetition bound declared.** An implementation must declare the bound at which a repeated step pattern terminates a run and must record the pattern detected.

**P13-6.40 (MUST) Nested runs bounded and attributed.** An implementation must count the steps and cost of a run initiated by another run against both runs' budgets and must record the initiating run.

**P13-6.41 (MUST) Nesting depth bounded.** An implementation must declare a maximum nesting depth for runs and must refuse a run exceeding it. The value is an implementation decision because the useful depth depends on the objectives admitted.

**P13-6.42 (MUST NOT) No objective amendment during a run.** An implementation must not permit the objective of a running agent to be amended, and must require a new run.

**P13-6.43 (MUST) Every step attributable to the run and the initiating party.** An implementation must attribute every step to its run, its initiating party and the authorising decision.

**P13-6.44 (MUST NOT) No effect outside the envelope.** An implementation must not permit a step to cause an effect of a class the envelope does not permit.

**P13-6.45 (MUST) Halt honoured between steps.** An implementation must honour a halt request at the next step boundary and must record the step at which it took effect.

### 6.7 Concurrency, idempotence and bounds

**P13-6.46 (MUST) Concurrent invocations independent.** An implementation must treat concurrent invocations as independent and must not represent one's output as bearing on another's.

**P13-6.47 (MUST) Idempotency key prevents a second charge.** An implementation must ensure that a repeated request under the same idempotency key does not cause a second invocation or a second charge.

**P13-6.48 (MUST) Concurrent steps in one run serialised.** An implementation must serialise steps within one agent run unless the run declares parallel steps, and must record the concurrency where it does.

**P13-6.49 (MUST) Timeout recorded as an outcome with cost.** An implementation must record a timeout as an outcome and must record any cost incurred before it.

**P13-6.50 (MUST) All bounds declared and finite.** An implementation must declare every bound it applies, must make each finite, and must record the bound on the operation it constrained.

### 6.8 What this component may compute and what it may not

**P13-6.51 (MUST NOT) No judgement of an output's content.** An implementation must not compute, record or expose any judgement of whether a produced value is correct, accurate, appropriate or fit for use.

**P13-6.52 (MUST NOT) No aggregate quality measure.** An implementation must not compute a quality, accuracy or performance measure over the outputs it produced.

**P13-6.53 (MAY) Structural and variance measures permitted.** An implementation may compute measures of structure, length, latency, cost and observed variance, which are properties of the invocation and not judgements of the output.

**P13-6.54 (MUST NOT) No inference from a refusal.** An implementation must not infer from a refusal that the request was improper, and must record the refusal as content.

**P13-6.55 (MUST NOT) No model selection by governed algorithm.** An implementation must not select which model to invoke by a governed algorithm where the selection is a business decision, and must obtain such a selection from `Part 5`.

**P13-6.56 (MAY) Operational routing permitted.** An implementation may route an invocation among deployments of one registered model identity for availability or latency, which is an operational choice, and must record the deployment that served it.

## 7. Outcome and failure taxonomy

### 7.1 Why the taxonomy is the specification

This component's outputs arrive at every other component in the estate, and a conventional client reduces them to two conditions: a string, or an exception. Everything that is not an exception becomes the string, and the string is used.

Eight conditions arrive as a usable string that is not one: a produced value; a value produced under a constraint so that its shape carries no information; a refusal, which is content and is not the answer to the question asked; a value returned from a cache, produced at some earlier instant by some earlier configuration; an output truncated at a limit so that it is the beginning of an answer; an empty output; an output the serving party altered or suppressed; and an output whose model identity cannot be established. Each requires a different response and none is distinguishable from the others once it has been assigned to a variable.

This section also states the boundary in the only way that makes it enforceable, by not providing the vocabulary in which it could be crossed. There is no outcome in this part meaning that a value is correct, and clause P13-7.12 forbids one being added.

**P13-7.1 (MUST) One enumeration per value.** An implementation must draw every value it returns from exactly one enumeration in this section.

**P13-7.2 (MUST NOT) No value outside the enumerations.** An implementation must not return a value outside these enumerations and must not extend one marked closed.

**P13-7.3 (MUST) Properties of an outcome exposed.** An implementation must expose, for every invocation outcome, the three properties in the table in section 7.6.

### 7.2 Invocation outcomes

Closed enumeration.

| Value | Meaning |
|---|---|
| `produced` | An output was produced under no structural constraint |
| `produced_constrained` | An output was produced under a structural constraint, so its conformance to that structure carries no information |
| `produced_truncated` | An output was produced and terminated at a length or token limit before completion |
| `refused_by_model` | The model produced content declining to produce what was asked |
| `filtered_by_provider` | The serving party suppressed or altered the output |
| `empty` | The model produced no content and did not refuse |
| `cache_hit` | A value produced by an earlier invocation was returned |
| `identity_unverifiable` | An output was produced and the responding model identity could not be established |
| `tool_error` | An invocation within an agent run failed at a tool call rather than at the model |
| `timeout` | No output was received within the declared bound |
| `rate_limited` | The serving party declined to serve the request for capacity reasons |
| `budget_exhausted` | A declared cost, step, elapsed or effect budget prevented the invocation |
| `retry_exhausted` | An attempt bound was reached without a usable output being selected |
| `provider_error` | The serving party reported a failure |
| `material_unresolvable` | A part of the context assembly could not be resolved |
| `not_authorised` | `Part 7` denied the invocation |
| `authorisation_unavailable` | `Part 7` could not be reached, and the invocation was denied |
| `not_attempted` | The invocation was requested and not attempted |

**P13-7.4 (MUST NOT) No refusal recorded as an error.** An implementation must record a refusal as `refused_by_model` and must not record it as `provider_error`, `empty` or a failure of this component.

**P13-7.5 (MUST) Refusal, filter and empty distinguished.** An implementation must distinguish content declining the request, an intervention by the serving party, and the absence of content, and must not report any of the three as another.

**P13-7.6 (MUST) Truncation distinguished from completion.** An implementation must record `produced_truncated` where an output terminated at a limit and must not record it as `produced`.

**P13-7.7 (MUST) Constrained production distinguished.** An implementation must record `produced_constrained` where a structural constraint applied and must not record it as `produced`.

**P13-7.8 (MUST) Cache hit distinguished from production.** An implementation must record `cache_hit` where a value was returned from an earlier invocation and must not record it as an outcome of the current request's parameters.

**P13-7.9 (MUST) Identity unverifiable recorded as an outcome, not a caveat.** An implementation must record `identity_unverifiable` as the outcome where an output was produced and the responding model could not be established.

**P13-7.10 (MUST) Budget and rate limit distinguished.** An implementation must distinguish an invocation this component declined for budget from one the serving party declined for capacity.

**P13-7.11 (MUST NOT) No outcome collapsed to a failure.** An implementation must not map `refused_by_model`, `filtered_by_provider`, `empty`, `cache_hit`, `identity_unverifiable`, `produced_truncated` or `budget_exhausted` to a general failure outcome.

### 7.3 There is no correct outcome

**P13-7.12 (MUST NOT) No correctness outcome.** An implementation must not provide, return or record any outcome value meaning that a produced value is correct, accurate, true or fit for use.

**P13-7.13 (MUST NOT) No confidence outcome.** An implementation must not provide an outcome value expressing a degree of confidence in a produced value's content.

**P13-7.14 (MUST NOT) No success vocabulary over content.** An implementation must not label an outcome success, valid, verified or passed in respect of a produced value's content.

**P13-7.15 (MUST) Produced is the strongest outcome.** An implementation must treat `produced` as the strongest available outcome and must not provide a stronger one.

### 7.4 Tool call outcomes

Closed enumeration.

| Value | Meaning |
|---|---|
| `called_with_result` | The tool executed and returned a result |
| `called_no_result` | The tool executed and returned nothing |
| `refused_unregistered` | The named tool is not registered |
| `refused_arguments_invalid` | The arguments did not validate against the registered schema |
| `refused_outside_envelope` | The call is outside the run's authority envelope |
| `refused_not_authorised` | `Part 7` denied the call |
| `refused_not_retry_safe` | A retry was attempted of a call recorded as not retry safe |
| `failed_effect_uncertain` | The call failed and whether an effect occurred is unknown |
| `failed_no_effect` | The call failed and no effect occurred |
| `timeout_effect_uncertain` | The call did not return and whether an effect occurred is unknown |

**P13-7.16 (MUST) Effect uncertainty recorded as its own outcome.** An implementation must distinguish a failed call that caused no effect from one where whether an effect occurred is unknown.

**P13-7.17 (MUST NOT) No assumption of no effect on failure.** An implementation must not record a failed or timed out call as having caused no effect unless it established that no effect occurred.

**P13-7.18 (MUST) Uncertain effect exposed.** An implementation must expose every call whose effect is uncertain, since it is the population where the state of the world is not known.

Clause P13-7.18 names the condition that makes agent execution qualitatively different from ordinary computation. A failed write in a transactional system is either committed or not. A failed tool call that sent an email, moved money or changed a record in a system without a transactional interface may have done so, and the agent's next step proceeds on an assumption about the world that nothing established.

### 7.5 Refusal codes for operations

Open enumeration, extended under section 9.

| Value | Meaning |
|---|---|
| `applied` | The operation was performed |
| `applied_idempotent` | Already performed under the same key |
| `idempotency_conflict` | The key was seen with different arguments |
| `refused_unattributed` | No unit of work, initiating party or authorising decision was supplied |
| `refused_model_unregistered` | The named model is not registered |
| `refused_model_status` | The model's status forbids invocation |
| `refused_no_context_assembly` | No context assembly was recorded |
| `refused_material_unresolvable` | Material in the assembly could not be resolved |
| `refused_no_budget` | A required budget was not declared |
| `refused_no_authority_envelope` | A run was opened with no envelope |
| `refused_envelope_exceeds_authority` | The envelope exceeds the initiating party's authority |
| `refused_no_termination_reason` | A run closure named no termination reason |
| `refused_objective_determination_from_run` | A determination of achievement was offered by the run |
| `refused_selection_basis_absent` | A selection was made with no registered basis |
| `refused_irreversible_without_effect_budget` | An irreversible step was attempted with no effect budget |
| `not_authorised` | `Part 7` denied the operation |
| `authorisation_unavailable` | `Part 7` could not be reached |
| `malformed` | The request could not be interpreted |
| `system_fault` | A value from section 7.7 |

**P13-7.19 (MUST) Refusal reasons distinguished.** An implementation must return the specific refusal reason and must not return one refusal for another.

**P13-7.20 (MUST) Refused operations carry no cost claim.** An implementation must record whether a refused operation incurred cost and must not assume it did not.

### 7.6 What distinguishes each outcome from a usable answer

**P13-7.21 (MUST) Three properties exposed.** An implementation must expose the three properties in the following table with every invocation outcome it returns.

| Outcome | Content present | Produced at this instant by the named model | Consumer may treat the content as an answer to what was asked |
|---|---|---|---|
| `produced` | yes | yes, subject to identity class | yes, and unchecked |
| `produced_constrained` | yes | yes | yes, and its shape carries no information |
| `produced_truncated` | partly | yes | no, it is incomplete |
| `refused_by_model` | yes | yes | no, it declines the question |
| `filtered_by_provider` | altered or absent | not as produced | no |
| `empty` | no | yes | no |
| `cache_hit` | yes | no, at an earlier instant | only under the earlier configuration |
| `identity_unverifiable` | yes | unknown | yes, and nothing rests on which model produced it |
| `tool_error` | no | not applicable | no |
| `timeout` | no | unknown | no |
| `rate_limited` | no | no | no |
| `budget_exhausted` | no | no | no |
| `retry_exhausted` | no | no | no |
| `provider_error` | no | no | no |
| `material_unresolvable` | no | no | no |
| `not_authorised` | no | no | no |
| `authorisation_unavailable` | no | no | no |
| `not_attempted` | no | no | no |

Three of the eighteen permit the content to be treated as an answer, and all three of those are unchecked. A client that reduces the eighteen to a string and an exception has told itself that all eighteen are the first.

### 7.7 System fault outcomes

Closed enumeration.

| Value | Meaning |
|---|---|
| `record_store_unavailable` | The invocation record store could not be written |
| `dependency_unavailable` | A required component could not be reached |
| `artifact_store_unavailable` | Material could not be read from or written to `Part 11` |
| `internal_invariant_violated` | The layer detected a violation of its own invariants |

**P13-7.22 (MUST NOT) No invocation without a writable record store.** An implementation must not perform an invocation it cannot record, and must return `record_store_unavailable`.

**P13-7.23 (MUST) Invariant violation halts invocation.** An implementation must stop invoking on detecting `internal_invariant_violated` and must raise the fault.

Clause P13-7.22 is the strongest ordering requirement in this part. An invocation that occurred and was not recorded has incurred cost, may have caused an effect and has produced a value that will circulate with no provenance. The record is not an account of the invocation; it is a precondition of it.

### 7.8 Propagation

**P13-7.24 (MUST) Outcome carried with its qualifications.** An implementation must return every outcome together with the produced status, the constraint, the identity class, the reproducibility class and the cost, and must not return the outcome value alone.

**P13-7.25 (MUST NOT) No aggregation losing the distinctions.** An implementation must not aggregate outcomes into a summary that loses the distinction between produced, constrained, refused, filtered, empty and cached.

**P13-7.26 (MUST) Counts report each outcome as its own category.** An implementation must report every outcome value as its own category in any count it publishes.

**P13-7.27 (MUST) Non results retained where unconsumed.** An implementation must retain a non result in the record of the affected invocation where no consumer subscribes to it.

## 8. Observability and the audit record

### 8.1 What this component can and cannot see

This component's records are complete about itself and about nothing else. It knows every request it sent, every value it received, every unit it was charged and every effect it initiated. It does not know whether any produced value was right, whether any output it recorded was the output the provider intended to send, or what any consumer did with what it returned.

That is the same asymmetry the four components before it recorded, and this one's form is the most consequential because the population it cannot see is the population of consequences. `Part 7` cannot see enforcement, `Part 10` cannot see consumption, `Part 11` cannot see citation, `Part 12` cannot see whether its samples were representative, and this component cannot see whether anything it produced was checked before it was acted upon.

**P13-8.1 (MUST) Completeness of each record declared.** An implementation must declare, for every figure it publishes, whether the underlying record is complete by construction or incomplete by construction.

**P13-8.2 (MUST NOT) No figure about consequences presented as complete.** An implementation must not publish a figure about what was done with its outputs without publishing the count of produced values for which no checking determination was received.

### 8.2 Grain

**P13-8.3 (MUST) Grain stated with every count.** An implementation must state the grain and the instant of computation with every count it reports.

**P13-8.4 (MUST) Invocation counts state whether attempts are counted individually.** An implementation must state whether a count of invocations counts every attempt or only selected attempts.

**P13-8.5 (MUST) Cost figures state their unit definition version.** An implementation must state the unit definition and version behind every cost figure.

**P13-8.6 (MUST NOT) No count spanning model identities without the split.** An implementation must not report one count across model registrations without stating the split.

**P13-8.7 (MUST) Agent figures state the grain.** An implementation must state whether a figure about agent activity counts runs, steps, invocations or tool calls.

### 8.3 What must be recorded

**P13-8.8 (MUST) Every invocation recorded.** An implementation must record every invocation, including refused, abandoned, cached and unresolved ones.

**P13-8.9 (MUST) Every context assembly recorded.** An implementation must record every context assembly with its parts, order and truncations.

**P13-8.10 (MUST) Every produced value recorded with its status.** An implementation must record every produced value with its produced status, constraint and any vacuity class.

**P13-8.11 (MUST) Every cost recorded.** An implementation must record cost against every attempt, including discarded and abandoned ones.

**P13-8.12 (MUST) Every tool call and effect recorded.** An implementation must record every tool call, its arguments origin, its result and every effect it caused.

**P13-8.13 (MUST) Every reversal and acceptance recorded.** An implementation must record every reversal of an effect, every failed reversal and every acceptance of an irreversible effect.

**P13-8.14 (MUST) Every run recorded with its budgets and termination.** An implementation must record every agent run with its objective, envelope, four budgets, steps and termination reason.

**P13-8.15 (MUST) Every checking determination recorded as received.** An implementation must record every checking determination it receives, unaltered, with the determining party.

**P13-8.16 (MUST) Every defect notification and enumeration recorded.** An implementation must record every defect notification with the affected interval and the enumeration completeness.

**P13-8.17 (MUST) Every responding model discrepancy recorded.** An implementation must record every case in which the responding model differed from the requested model.

### 8.4 What must be reconstructable

**P13-8.18 (MUST) The exact input of any invocation.** A reader must be able to reconstruct the exact input sent for any invocation, from addressed material and the recorded order, or must be able to establish that the content was not retained and at what level.

**P13-8.19 (MUST) The model and configuration that served it.** A reader must be able to reconstruct the model identity, its identity class, its verifiability and the serving configuration of any invocation.

**P13-8.20 (MUST) Every attempt behind any result.** A reader must be able to reconstruct every attempt made in obtaining a result, the outputs discarded and the basis of the selection.

**P13-8.21 (MUST) The full cost of any unit of work.** A reader must be able to reconstruct the total cost of a unit of work including discarded and abandoned attempts.

**P13-8.22 (MUST) Whether any produced value was checked.** A reader must be able to establish, for any produced value, whether a checking determination was received, from whom, and whether any check applied was vacuous.

**P13-8.23 (MUST) Every step and effect of any run.** A reader must be able to reconstruct every step of an agent run in order, every effect it caused and whether each was reversed or accepted.

**P13-8.24 (MUST) What an agent was asked and what it asserted.** A reader must be able to reconstruct the objective as declared and the assertion the agent made on termination, and to distinguish the second from a determination.

**P13-8.25 (MUST) Everything a defect affected.** A reader must be able to reconstruct which invocations fell in a defect's affected interval and which consumers were notified.

**P13-8.26 (MUST NOT) No reconstruction dependent on this component running.** An implementation must not require its own runtime to be available for any reconstruction in section 8.4.

### 8.5 Signals

**P13-8.27 (MUST) Unchecked consumed population.** An implementation must expose the count of produced values consumed by another component with no checking determination received.

**P13-8.28 (MUST) Vacuous check proportion.** An implementation must expose the proportion of checks applied to produced values that carry a vacuity class.

**P13-8.29 (MUST) Unverifiable identity proportion.** An implementation must expose the proportion of invocations whose model identity is unverifiable.

**P13-8.30 (MUST) Reproducibility class distribution.** An implementation must expose the distribution of invocations by reproducibility class, which for most estates will be overwhelmingly unknown and should be seen to be.

**P13-8.31 (MUST) Discarded attempt cost and count.** An implementation must expose the cost and count of discarded attempts, per unit of work and in total.

**P13-8.32 (MUST) Attempt divergence population.** An implementation must expose every attempt set whose attempts produced materially different outputs and from which a selection was made.

**P13-8.33 (MUST) Irreversible unaccepted effect population.** An implementation must expose every irreversible effect not yet accepted by an accountable party.

**P13-8.34 (MUST) Uncertain effect population.** An implementation must expose every tool call whose effect is uncertain.

**P13-8.35 (MUST) Unsettled run population.** An implementation must expose every terminated run that has not settled.

**P13-8.36 (MUST) Agent asserted completion without determination population.** An implementation must expose every run that asserted completion and for which no objective determination has been received.

**P13-8.37 (MUST) Authority exceeded population.** An implementation must expose every step refused for exceeding an authority envelope, by run and by party.

**P13-8.38 (MUST) Unidentifiable consumer population.** An implementation must expose the count of produced values whose consumers cannot be identified.

**P13-8.39 (MUST) Responding model discrepancy population.** An implementation must expose every invocation whose responding model differed from the requested model.

**P13-8.40 (MUST) Content not retained proportion.** An implementation must expose the proportion of invocations for which the prompt or output content was not retained, since those are the invocations no later question can be answered about.

**P13-8.41 (SHOULD) Refusal and filter rate by model.** An implementation should expose the rate of refusals and provider filters by model registration, since a change in either is a change in behaviour that no version string may reflect.

### 8.6 The evidence package

**P13-8.42 (MUST) Package assemblable for an invocation.** An implementation must be able to assemble, for any invocation, a package containing the context assembly and its material, the model identity and serving configuration, the sampling parameters, the produced value, the cost record, the reproducibility declaration, the attribution and every checking determination received.

**P13-8.43 (MUST) Package assemblable for a run.** An implementation must be able to assemble, for any agent run, a package containing the objective, the envelope, the budgets, every step in order, every tool call and effect, the termination reason and any objective determination.

**P13-8.44 (MUST) Package states what it omits.** An implementation must state, in every package, every element it could not include and why, including content not retained.

**P13-8.45 (MUST) Package integrity protected.** An implementation must integrity protect every package by a means governed by `Part 3`.

### 8.7 Retention and what cannot be changed

**P13-8.46 (MUST) Records outlive the value.** An implementation must retain an invocation record and its cost record for at least as long as the longest retention obligation attaching to any determination that consumed the produced value.

**P13-8.47 (MUST) Retention obligation notified.** An implementation must notify `Part 11` and `Part 1` of the retention obligation its records create over the addresses and versions they cite.

**P13-8.48 (MUST NOT) No alteration of an invocation record, produced value, cost record or tool call record.** An implementation must not alter any of those once written.

**P13-8.49 (MUST NOT) No deletion of a discarded attempt.** An implementation must not delete the record of a discarded attempt.

**P13-8.50 (MUST NOT) No deletion of an effect record.** An implementation must not delete the record of an effect caused outside this component.

## 9. Extension model

### 9.1 Closed sets and open sets

**P13-9.1 (MUST) Closed sets not extended.** An implementation must not extend the following: invocation outcomes, tool call outcomes, system fault outcomes, identity classes, verifiability values, reproducibility classes, variance sources, vacuity classes, effect classes, termination reasons, model registration states, invocation states, agent run states, produced value states and effect states.

**P13-9.2 (MUST) Open sets extended only through a registry.** An implementation must extend the following only through the registries of section 9.2: models, providers, serving configurations, tools, cost unit definitions, selection bases, instruction materials, sampling parameter names and refusal codes.

**P13-9.3 (MUST NOT) No new outcome for a new model capability.** An implementation must not introduce an invocation outcome to accommodate a new modality or capability, and must classify the result under an existing outcome.

The open sets are the ones that change with the technology and the closed sets are the ones that appear in a conclusion. Models, providers, tools and parameters will change faster than this part can be revised, and a component that cannot register a new one is obsolete on the day a provider ships. The outcomes and classes must not change, because they are what six other parts read.

### 9.2 Registry mechanics

**P13-9.4 (MUST) Registration before use.** An implementation must require every open set member to be registered before an invocation or a run uses it.

**P13-9.5 (MUST) Definition mandatory at registration.** An implementation must require a definition of every registered member's meaning.

**P13-9.6 (MUST) Registration attributable.** An implementation must record the registering party, the instant and the authorising decision for every registration.

**P13-9.7 (MUST NOT) No meaning change under a registered identifier.** An implementation must not alter the meaning of a registered member and must express a change as a new member or a new version.

**P13-9.8 (MUST) Retirement recorded, records retained.** An implementation must retain every invocation record referencing a retired member and must not remove the member from the register.

### 9.3 The model and serving configuration registries

**P13-9.9 (MUST) Identity class recorded per registration.** An implementation must record the identity class and verifiability of every registered model.

**P13-9.10 (MUST) Serving configuration versioned.** An implementation must version every serving configuration and must record which version served each invocation.

**P13-9.11 (MUST) Provider assertions recorded as assertions.** An implementation must record every property a provider asserts about a model or configuration as an assertion by that provider, with the instant and the source.

**P13-9.12 (MUST NOT) No inherited registration across identity change.** An implementation must not carry a registration forward across a detected change in the content behind a provider alias, and must register the changed content as a new configuration.

### 9.4 The tool registry

**P13-9.13 (MUST) Effect class and retry safety recorded.** An implementation must record the effect class and the retry safety of every registered tool.

**P13-9.14 (MUST) Reversal procedure required for a reversible class.** An implementation must not register a tool with the effect class reversible unless a reversal procedure is recorded.

**P13-9.15 (MUST) Required authority recorded.** An implementation must record the permissions a tool requires and must obtain them per call.

**P13-9.16 (MUST) Argument schema required.** An implementation must not register a tool with no argument schema.

### 9.5 The cost unit definition registry

**P13-9.17 (MUST) Unit definitions versioned.** An implementation must version every cost unit definition and must record which version applied to each cost record.

**P13-9.18 (MUST) Provider ownership of the definition recorded.** An implementation must record that a cost unit definition is the provider's and not this component's.

**P13-9.19 (MUST NOT) No cross provider unit equivalence registered.** An implementation must not register an equivalence between the cost units of two providers.

### 9.6 The selection basis registry

**P13-9.20 (MUST) Basis semantics recorded.** An implementation must record, for every selection basis, what property of an attempt it selects on.

**P13-9.21 (MUST) Order based bases marked.** An implementation must mark every selection basis that selects on the order of attempts as order based, so that clause P13-3.50's population is derivable.

**P13-9.22 (MUST NOT) No basis registered that selects on a model's self assessment.** An implementation must not register a selection basis whose input is a confidence or quality score the producing model generated.

## 10. Standards and specifications

### 10.1 How the citations in this part are to be read

Each entry states what the source supplies, its status at the date of this part, and whether this part's account rests on specification text, on published work or on general knowledge. Section 13.1 lists the sources not obtained.

The authoring brief for this standard predicted that this part would have the least standards support of the thirteen, and the prediction holds. There is no standard for an invocation record. There is one convention that is close, and it is explicitly pre stable. There are management system standards about governing artificial intelligence, which say nothing about invocation. There is a regulation with logging obligations, which is a legal instrument and not a technical specification. The two findings this part rests on most heavily come from a vendor neutral telemetry convention that is still marked as under development, and from a piece of published engineering work from a single laboratory.

**P13-10.1 (MUST) Cited edition recorded.** An implementation must record the edition or version of every external source it relies upon and must not cite one without it.

**P13-10.2 (MUST) Basis marked.** An implementation must record, for every control it adopts from a source named in this section, whether the basis is specification text, published work or practice.

**P13-10.3 (MUST) Pre stable sources marked as such.** An implementation must record, for every source it adopts that is marked pre stable or under development by its publisher, that the source may change and that its own record shape may therefore change.

### 10.2 The telemetry convention for generative artificial intelligence

**Supplies.** The nearest thing to a standard for an invocation record. Span shapes for model inference, embeddings, retrieval, memory operations, tool execution, agent invocation, workflow invocation and planning. Attribute names including the requested model, the responding model, the provider, the operation name, input and output token counts and the finish reason. Metrics for token usage, operation duration, streaming timing, agent invocation duration, per invocation call counts and tool execution duration. The separation of the requested model from the responding model, which clause P13-3.16 adopts.

**Status.** Pre stable. As of a release on 12 June 2026 the generative artificial intelligence attributes and spans were moved out of the main semantic conventions repository into a dedicated repository, which is an organisational change and not a graduation. Every document in that repository carries the status Development, formerly called experimental. There is no version one and attribute names can change between versions.

**Does not supply.** Any distinction between a produced and a checked value. Any reproducibility declaration. Any cost unit definition or cross provider comparability. Any treatment of retry as selection. Any agent authority envelope, effect class or termination reason. And it makes the capture of prompts and completions optional, which section 10.7 records as a conflict.

**Basis.** Convention text and project documentation, read at second hand through descriptions of the repository contents and the attribute registry. The registry and the moved repository were not read directly.

### 10.3 The non determinism finding

**Supplies.** The evidence for section 6.3. Published work of September 2025 attributing the non determinism of temperature zero inference principally to the absence of batch invariance in reduction kernels rather than to floating point non associativity combined with concurrency; the observation that the batch a request is served in depends on concurrent load and is therefore outside the requester's control; the measurement of eighty distinct completions from one thousand temperature zero invocations of one prompt; the demonstration that batch invariant kernels yield bitwise identical outputs; and the reported throughput cost of doing so, given as roughly sixty per cent in the original implementation and reduced to roughly a third by later integration work.

**Does not supply.** A standard. This is published engineering work from one laboratory with a reference implementation, corroborated in subsequent literature, and it is not a specification anyone conforms to.

**Basis.** Published work, read at second hand through the original blog post's own text as quoted and through corroborating academic literature. The reference implementation was not examined.

### 10.4 Management system and risk standards

**Supplies.** Governance apparatus. The artificial intelligence management system standard supplies a management system with roles, objectives and continual improvement. The risk management guidance supplies a risk process. The concepts and terminology standard supplies vocabulary. None of them constrains an invocation record.

**Does not supply.** Anything this part specifies. They govern how an organisation manages the use of these systems, not what the systems record.

**Basis.** General knowledge. None was obtained and section 13.1 records it.

### 10.5 Regulatory logging obligations

**Supplies.** An obligation, in a regulation applying in one jurisdiction, that certain systems keep automatically generated records over their lifetime sufficient to identify situations that may present a risk, together with transparency and human oversight obligations and technical documentation requirements. It establishes that a durable invocation record is a legal expectation and not only an engineering preference.

**Does not supply.** A record format, a field set or any of the distinctions this part turns on. It is a legal instrument, its obligations are phased, and its detail is being developed through standardisation and guidance that this part did not consult.

**Basis.** General knowledge, not obtained. Section 13.1 records that the current state of the obligations and of the standardisation supporting them was not established, and no clause of this part depends on them.

### 10.6 Declarative documentation practice

**Supplies.** The practice of publishing a document describing a model's intended use, evaluation and limitations, and the practice of describing a dataset similarly. Emerging bill of materials formats carry model and dataset profiles that make such declarations machine readable.

**Does not supply.** Any obligation on a provider to publish one, any assurance that a published one is accurate, and any relationship between a published document and the model actually served behind an alias. Clause P13-3.20 records such a document as a declaration by the provider and not as a specification.

**Basis.** Practice and general knowledge.

### 10.7 Named conflicts

| Conflict | Position A | Position B | Resolution | Reason |
|---|---|---|---|---|
| Whether prompts and outputs are recorded | The telemetry convention makes capture optional and requires implementations that support it to offer the ability to turn it off, for privacy and data volume reasons | This part, clauses P13-3.3 and P13-3.25: material is held by address and the content recording level is declared | Both, partially. This part does not require full content retention; it requires the level to be declared and the level to be visible on every figure derived from those records, per clause P13-8.40 | The convention's reasons are sound and the consequence is that a conforming record may contain nothing of substance. What this part refuses is that the absence be invisible: an invocation whose content was not retained cannot answer any later question, and the proportion of such invocations is the ceiling on any subsequent enquiry |
| Whether temperature zero is deterministic | Widespread practice, and several provider interfaces, treat a temperature of zero with a seed as producing repeatable output | This part, clauses P13-3.36 and P13-6.13: neither establishes reproducibility | This part | The measurement is published and unambiguous. One provider describes its own interface as mostly deterministic, which is the honest form of the same position |
| Whether a retry is a retry | Ordinary idempotency and retry conventions assume the operation is a function of its inputs | This part, section 6.4: each attempt is a distinct invocation and taking the first usable output is a selection | This part | The assumption is false here. The consequence of not stating it is that the variance a search concealed is invisible and the discarded attempts are unrecorded |
| Whether structural validity is evidence | Practice treats a schema conformant output as validated | `Part 9` clause P9-12-38 and this part's clause P13-3.32: where the constraint produced the conformance, it establishes nothing | Both parts together | The check could not have failed. Section 3.6 generalises the case to every check whose failure was impossible |
| Whether cost is comparable | Practice reports token counts and monetary totals across providers as one figure | This part, clauses P13-3.44 and P13-6.33: units differ by provider and by definition version and must not be aggregated | This part, with the cost recorded in section 13.3 | The figures are the only hard numbers in this subject and the easiest to mislead with. A single total across providers is a number with no unit |

### 10.8 What none of the sources supplies

**P13-10.4 (MUST) Requirements of this part alone identified.** An implementation must treat the following as requirements of this part alone, no consulted source supplying them: the produced and checked distinction and the prohibition on self check; the vacuity classes and the prohibition on counting a vacuous check; the reproducibility declaration with a default of unknown; the identity class and verifiability model; the treatment of every attempt as an invocation with its own cost and the retention of discarded attempts; the selection basis with order based selection marked; the cost unit definition version and the refusal of cross provider aggregation; the authority envelope, the effect class and the four budgets of an agent run; the termination reason enumeration and the prohibition on reading any of it as achievement; the effect state model and the uncertain effect outcome; and the defect notification with enumeration of affected invocations.

## 11. Anti patterns

### 11.1 The produced value that became checked by circulating

**Mechanism.** A produced value is stored, addressed, validated, logged and read by several components. Each records it. None checked it.

**Evidence.** Six parts of this standard forbid their own component from treating a produced value as checked, and each forbids it in its own vocabulary because each found the same failure independently.

**Consequence.** The value's apparent standing rises with every handling and its actual standing never changes. By the time it is relied on, the record is thick and the check is absent, and nothing in the record says which.

**P13-11.1 (MUST) Produced status carried into every projection.** An implementation must carry the produced and checking status into every projection of a value.

### 11.2 The model that checked itself

**Mechanism.** A second invocation asks the model whether its first output was correct, and the answer is recorded as a check.

**Evidence.** Clause P13-3.6. The second invocation is a produced value with the same status as the first.

**Consequence.** A produced value is confirmed by a produced value, and the confidence rises with no accountable party anywhere in the chain. The failure is invisible because the output of a self check is almost always favourable.

**P13-11.2 (MUST NOT) No self check.** An implementation must not record an invocation as a check of a prior invocation's output.

### 11.3 The vacuous check

**Mechanism.** An output produced under a schema constraint is validated against that schema and the validation is cited as evidence.

**Evidence.** `Part 9` names it from the consuming side and this part names it from the producing side. The check could not have failed.

**Consequence.** The strongest available evidence turns out to be a tautology, and it is the evidence most often produced because it is the cheapest to automate.

**P13-11.3 (MUST) Vacuity classified and not counted.** An implementation must classify a vacuous check and must not count it towards any figure of checked values.

### 11.4 The rubric the producer wrote

**Mechanism.** A model generates the criteria against which its own output will be judged, or generates the tests a generated artefact must pass.

**Evidence.** Section 3.6, classes `producer_authored_criterion` and `producer_authored_test`.

**Consequence.** The criterion is fitted to the output rather than the output to the criterion, and the resulting pass rate measures internal consistency. This is the same failure as the vacuous check with a longer path and it is harder to see.

**P13-11.4 (MUST) Producer authored criteria recorded as vacuous.** An implementation must record a check against a criterion the producer authored as carrying a vacuity class.

### 11.5 Temperature zero read as determinism

**Mechanism.** A configuration sets temperature to zero and supplies a seed, and the system is treated as reproducible thereafter.

**Evidence.** One thousand temperature zero invocations of a single prompt produced eighty distinct completions in the published experiment, because the batch a request lands in depends on concurrent load.

**Consequence.** Every downstream mechanism that assumes reproducibility is wrong: caches return values that would not have been produced again, replays diverge and are treated as faults, and an audit that re invokes and gets a different answer concludes the record was falsified.

**P13-11.5 (MUST NOT) No determinism from temperature or seed.** An implementation must not record a reproducibility class stronger than unknown on the basis of either.

### 11.6 The alias treated as an identity

**Mechanism.** A provider's model name is recorded as the model, and the content behind the name changes without notice.

**Evidence.** The telemetry convention carries the requested model and the responding model separately, which exists because they differ.

**Consequence.** Every claim about which model produced a value is unfounded, and a change in behaviour cannot be attributed. The change is discovered when outputs shift and nobody can establish whether the model, the prompt or the data moved.

**P13-11.6 (MUST) Identity class recorded and alias marked unverifiable.** An implementation must record the identity class and mark an alias invocation as having an unverifiable identity.

### 11.7 The retry that hid the variance

**Mechanism.** The system retries until an output parses, takes it, and discards the rest.

**Evidence.** Section 6.4 and clause P13-3.51.

**Consequence.** The distribution is concealed and its mode is reported as the value. Where the attempts disagreed materially, a disagreement has been resolved by an accident of ordering and nothing records that there was one.

**P13-11.7 (MUST) Attempt divergence exposed.** An implementation must expose every attempt set whose attempts diverged materially and from which a selection was made.

### 11.8 The cost of the successful call

**Mechanism.** Cost is recorded against the invocation whose output was used.

**Evidence.** Clause P13-3.41. Discarded and abandoned attempts were charged.

**Consequence.** The reported unit cost of an operation understates the actual cost by the retry multiple, which is exactly the operations where retries are frequent, which is exactly where the reported figure is used to justify the approach.

**P13-11.8 (MUST) Cost recorded per attempt.** An implementation must record cost against every attempt.

### 11.9 The token count as a measure of value

**Mechanism.** Consumption figures are reported as a measure of productivity, adoption or output.

**Evidence.** Clause P13-2.9. A cost unit measures what a provider meters.

**Consequence.** The metric rises when prompts grow, when retries increase and when outputs become more verbose, all of which are costs. Managed against, it selects for the behaviours it should discourage.

**P13-11.9 (MUST NOT) No cost figure as a measure of value.** An implementation must not present a cost or unit figure as a measure of productivity, quality or output.

### 11.10 The single total across providers

**Mechanism.** Token counts or monetary amounts from several providers are added into one figure.

**Evidence.** Clauses P13-3.44 and P13-6.33. The units are each provider's own and are redefined without notice.

**Consequence.** A number with no unit is reported to people who make decisions with it, and a provider changing its definition changes the estate's reported consumption with no change in behaviour.

**P13-11.10 (MUST NOT) No aggregation across unit definitions.** An implementation must not aggregate cost across differing unit definitions.

### 11.11 The cache hit reported as an invocation

**Mechanism.** A cached value is returned and recorded as though the current request's model and parameters produced it.

**Evidence.** Clause P13-3.27.

**Consequence.** The record attributes a value to a configuration that did not produce it, so a defect enumeration over that configuration misses it and a reproducibility claim about it is a claim about a different invocation.

**P13-11.11 (MUST) Cache hit recorded distinctly.** An implementation must record a cache hit as such and must name the source invocation where known.

### 11.12 The refusal recorded as an error

**Mechanism.** The model declines to produce what was asked, and the client records an exception.

**Evidence.** Clause P13-7.4. A refusal is content.

**Consequence.** A meaningful signal about what was asked becomes an operational failure statistic, the request is retried, and the retry produces the same refusal at additional cost. Nobody learns what the refusal said.

**P13-11.12 (MUST NOT) No refusal as an error.** An implementation must record a refusal as its own outcome.

### 11.13 The provider filter recorded as a refusal

**Mechanism.** The serving party suppresses or alters an output and the client records it as the model having declined.

**Evidence.** Clause P13-2.4. The two have different causes and different remedies.

**Consequence.** Behaviour is attributed to the model that belongs to the serving infrastructure, and a change in a provider's filtering appears as a change in the model.

**P13-11.13 (MUST) Filter distinguished from refusal.** An implementation must record a provider filter as its own outcome.

### 11.14 The truncated output used as a complete one

**Mechanism.** An output stops at a token limit and is consumed as though it were finished.

**Evidence.** Clause P13-7.6.

**Consequence.** A partial answer is acted on as a whole one, and in structured output the truncation may still parse, so no downstream check detects it.

**P13-11.14 (MUST) Truncation recorded as its own outcome.** An implementation must record a truncated output distinctly.

### 11.15 The agent that reported its own success

**Mechanism.** An agent terminates, asserts that it completed the objective, and the assertion is recorded as the outcome.

**Evidence.** Clauses P13-3.55 and P13-3.62.

**Consequence.** The only party that determined whether the work was done is the party that did it, and its effects are already in the world. Where the assertion is wrong, the record shows a completed objective and the discovery comes from somewhere else entirely.

**P13-11.15 (MUST NOT) No assertion recorded as achievement.** An implementation must not record an agent's assertion of completion as a determination.

### 11.16 The unbounded run

**Mechanism.** An agent runs until it stops, with no step, cost, elapsed or effect budget.

**Evidence.** Clause P13-3.53.

**Consequence.** Cost is discovered from an invoice and effects are discovered from their consequences. A loop that neither terminates nor progresses is indistinguishable from work in progress.

**P13-11.16 (MUST) Four budgets declared and finite.** An implementation must declare a finite step, cost and elapsed budget for every run.

### 11.17 The authority the agent accreted

**Mechanism.** An agent acquires access during a run, because a step needed it and the credential was available.

**Evidence.** Clauses P13-3.57 and P13-6.38.

**Consequence.** The run exercises authority the initiating party never held, and the authorisation record for the run does not cover what the run did. Nobody granted the composite authority and nobody can be found who did.

**P13-11.17 (MUST NOT) No authority accretion.** An implementation must not permit a run to acquire authority it did not hold at opening.

### 11.18 The irreversible tool call retried

**Mechanism.** A tool call fails or times out, and the call is retried because retry is the default.

**Evidence.** Clauses P13-3.70, P13-6.24 and P13-7.17.

**Consequence.** The effect happens twice, or happens once when it was believed not to have happened at all. This is the failure in this part with the largest consequences outside the system and the least visibility inside it.

**P13-11.18 (MUST NOT) No retry of a call that is not retry safe.** An implementation must not retry a call whose registration records it as not retry safe.

### 11.19 The uncertain effect assumed absent

**Mechanism.** A tool call times out, and the system proceeds on the assumption that nothing happened.

**Evidence.** Clause P13-7.17.

**Consequence.** The agent's next step rests on a belief about the world that nothing established, and where the effect did occur the divergence compounds through the rest of the run.

**P13-11.19 (MUST) Uncertain effect recorded as uncertain.** An implementation must record an effect it did not establish as uncertain and must expose the population.

### 11.20 The prompt in the configuration file

**Mechanism.** Instruction material lives in a deployment configuration, is edited in place, and is not versioned as a document.

**Evidence.** Clauses P13-3.77 to P13-3.79.

**Consequence.** The single largest determinant of what the system produces is the one thing with no version history, no approval and no retention. A change in behaviour cannot be attributed and a past output cannot be explained.

**P13-11.20 (MUST) Instruction material versioned and addressed.** An implementation must hold instruction material as a versioned, addressed artifact.

### 11.21 The human in the loop with one button

**Mechanism.** A produced value is presented to a person with an accept action and no alternative, at a rate that permits no examination, and the acceptance is recorded as a human check.

**Evidence.** `Part 8` clause P8-3-31 requires the outcomes available to a performer to be recorded and clause P8-3-32 requires a presentation offering one outcome to be recorded as constrained. The mechanism is designed to satisfy the letter of a human check while removing its content.

**Consequence.** The record shows a human determination and the determination did not occur. Every regulatory position requiring a person to be accountable is satisfied on paper by a click, and the person is accountable for something they could not have examined.

**P13-11.21 (MUST) Choice breadth of a presented proposal recorded.** An implementation must record, for every produced value presented for a checking determination, that the recording of available outcomes is `Part 8`'s and must supply the value as a proposal rather than as a default.

### 11.22 The evaluation the vendor performed

**Mechanism.** A provider's published figures are recorded as the properties of the model.

**Evidence.** Clause P13-3.20.

**Consequence.** A first party declaration is treated as a measurement, and it concerns a model that may not be the model served behind the alias.

**P13-11.22 (MUST) Provider declaration recorded as a declaration.** An implementation must record a provider's published figures as assertions by that provider.

### 11.23 The invocation that was not recorded

**Mechanism.** An invocation proceeds when the record store is unavailable, because the work matters and the record can be written later.

**Evidence.** Clause P13-7.22.

**Consequence.** Cost was incurred, an effect may have occurred, and a value now circulates with no provenance, no attribution and no place in any defect enumeration. It is the one failure in this part that cannot be repaired afterwards.

**P13-11.23 (MUST NOT) No invocation without a writable record.** An implementation must not invoke a model it cannot record.

### 11.24 The defect nobody could trace

**Mechanism.** A model is found to have been faulty for a period, and the affected outputs cannot be enumerated because the invocations were not attributed or the consumers were not identified.

**Evidence.** Section 3.11 and clause P13-3.76.

**Consequence.** The estate knows it acted on faulty output and cannot say where. The remedy is either to do nothing or to invalidate everything from the period, and both are usually unacceptable.

**P13-11.24 (MUST) Unidentifiable consumer population exposed.** An implementation must expose the count of produced values whose consumers cannot be identified.

### 11.25 The model in the evaluation path

**Mechanism.** A model is invoked during a policy evaluation, a rule evaluation or a validation, so a governed determination depends on a non deterministic output obtained at that instant.

**Evidence.** `Part 7` clause P7-12.35 forbids the invocation of a model, an agent or any non deterministic service during an evaluation.

**Consequence.** The determination is not reproducible, its basis cannot be pinned, and re running it yields a different answer with no record of why. The governed decision has become a fitted function with no statement.

**P13-11.25 (MUST NOT) No invocation inside another component's evaluation.** An implementation must not offer, and must refuse, an invocation requested from within a policy evaluation, a rule evaluation or a validation.

### 11.26 The agent that became the process

**Mechanism.** A defined process is replaced by an agent given the process's objective, because the agent can handle the variation.

**Evidence.** `Part 6` owns control flow and `Part 8` owns work whose order is determined at runtime. An agent run is neither: it is a bounded sequence with no declared plan and no gates.

**Consequence.** The organisation loses the ability to say what the process is. Every instance is different, none is a deviation because there is no norm, and the coverage, conflict and completeness analyses the other parts require have nothing to analyse.

**P13-11.26 (MUST NOT) No agent run substituted for a declared process.** An implementation must not represent an agent run as a process instance or a case, and must record it as a run under an objective.

## 12. Boundaries with other parts

Every subsection states what this component delegates, what it must not absorb, the naive conflation, and the reciprocal this part requires of the other. Subsection numbers correspond to part numbers; there is no 12.13 because this is Part 13.

### 12.1 Boundary with Part 1, controlled documents and records

**Delegated.** The identity, version, approval, effective date and retention of every instruction material, model card and provider declaration.

**Must not absorb.** Document lifecycle. An instruction material is the largest single determinant of what this component produces and it is a controlled document.

**Naive conflation.** Prompts live in configuration and are edited in place, so the thing that determines the output has no version history.

**Reciprocal.** `Part 1` must declare that it owns the version and approval of instruction material and provider declarations, that it resolves a citation to the version in force at the cited instant, that this component's invocation and cost records are records in its sense and not revisable, and that it retains an instruction version for as long as any invocation cites it.

**P13-12.1 (MUST) Instruction material governed as a document.** An implementation must obtain the version identity and approval of every instruction material from `Part 1`.

**P13-12.2 (MUST) Instruction version pinned per invocation.** An implementation must pin the instruction version each invocation used and must not resolve it to the current version.

**P13-12.3 (MUST) Records treated as records.** An implementation must treat its invocation, cost, tool call and effect records as records in the `Part 1` sense and must not revise one.

### 12.2 Boundary with Part 2, business rules and constraint evaluation

**Delegated.** Every constraint whose evaluation is declarative, including any constraint applied to a produced value.

**Must not absorb.** Constraint evaluation, and in particular the temptation to have a model evaluate a rule.

**Naive conflation, two forms.** A rule is implemented as an invocation, so a governed constraint becomes a non deterministic output with no rule identity and no verdict vocabulary. Or a model output becomes a rule input evaluated at the same instant, which `Part 7` clause P7-12.35 forbids for its own subject and which is no better here.

**Reciprocal.** `Part 2` must declare that it owns rule identity, evaluation and verdicts, that it does not invoke a model during an evaluation, and that a model output reaches it only as a pinned value obtained beforehand and marked as produced.

**P13-12.4 (MUST NOT) No rule evaluated by invocation.** An implementation must not represent an invocation as the evaluation of a declarative rule.

**P13-12.5 (MUST) Produced values supplied pinned and marked.** An implementation must supply a produced value to `Part 2` as a pinned value marked produced, obtained before the evaluation.

**P13-12.6 (MUST NOT) No invocation during a rule evaluation.** An implementation must refuse an invocation requested during a rule evaluation.

### 12.3 Boundary with Part 3, provenance and audit ledger

**Delegated.** The evidentiary chain in which a produced value participates, and the enumeration of determinations affected by a defect.

**Must not absorb.** The chain. An invocation record is one input to the provenance of a determination and is not that provenance.

**Naive conflation.** The invocation log is treated as the audit trail, so a reader finds what was asked and returned and nothing about what was decided on it.

**Reciprocal.** `Part 3` must declare that it owns the evidentiary chain, that a produced value is one basis element within it, that it accepts a defect notification from this component as a defect in the basis of every determination that consumed an affected value, and that it can enumerate those determinations.

**P13-12.7 (MUST) Events emitted to the ledger.** An implementation must emit every event of section 4.7 to `Part 3`.

**P13-12.8 (MUST) Defect notified as a basis defect.** An implementation must notify `Part 3` of every defect notification as a defect in the basis of the determinations that consumed affected values. **Source.** Required of this component by `Part 7` section 12.13.

**P13-12.9 (MUST NOT) No chain asserted.** An implementation must not represent its invocation records as the provenance of any determination.

**P13-12.10 (MUST) Delegation chain supplied where an agent requests.** An implementation must supply the delegation chain from an agent run to an accountable party where a run requests a decision, so that `Part 3` and `Part 7` can assess its validity. **Source.** `Part 7` clause P7-12.38 requires that component to assess the delegation of every request an automated agent makes and to record the assessment on the decision.

### 12.4 Boundary with Part 4, metadata and model repository

**Delegated.** The governed definition of any term an instruction material or an output schema uses, and the lineage of a change to it.

**Must not absorb.** Meaning.

**Naive conflation.** The prompt becomes the place where business meaning is stated, so a definition lives in an unversioned instruction and cannot be cited by anything.

**Reciprocal.** `Part 4` must declare that it owns governed definitions and their lineage, and that it exposes the instruction materials and output schemas citing each definition so that a definition change surfaces the invocations affected.

**P13-12.11 (MUST) Definitions cited, not restated.** An implementation must cite a `Part 4` definition where an instruction material or output schema turns on a governed term and must not restate the definition in the instruction.

**P13-12.12 (MUST) Definition change surfaces affected instructions.** An implementation must expose every instruction material citing a definition that changed.

### 12.5 Boundary with Part 5, decision engine

**Delegated.** Every business outcome selection, including which model to use where that choice is a business decision and which of several produced values is authoritative.

**Must not absorb.** Business selection. Choosing among attempts on a registered basis is a recorded selection within this component; choosing which of two produced values a business relies on is a decision.

**Naive conflation.** The model is given the decision, so the outcome is a fitted function with no criterion, no statement and no explanation.

**Reciprocal.** `Part 5` must declare that it owns business outcome selection, that a model output reaches it only as a pinned produced value, and that it does not delegate a decision to an invocation.

**P13-12.13 (MUST NOT) No business decision produced as an outcome.** An implementation must not represent a produced value as a business decision and must supply it as a produced value for a decision to consume.

**P13-12.14 (MUST) Model selection obtained where it is a decision.** An implementation must obtain from `Part 5` any selection of which model to invoke that depends on a governed business rule.

**P13-12.15 (MAY) Operational routing retained.** An implementation may route among deployments of one model identity for availability or latency and must record the deployment that served.

### 12.6 Boundary with Part 6, workflow and process orchestration

**Delegated.** Predefined control flow, and the sequencing of work whose order is known in advance.

**Must not absorb.** Control flow. An agent run is a bounded sequence under an objective and is not a process.

**Naive conflation.** A process is replaced by an agent, so the organisation can no longer state what its process is, per section 11.26.

**Reciprocal.** `Part 6` must declare that it owns control flow, that an agent run is not a process instance, that it may invoke this component as a step and must record the invocation reference, and that it does not embed a produced value in place of a determination.

**P13-12.16 (MUST NOT) No agent run as a process instance.** An implementation must not represent an agent run as a process instance or a case.

**P13-12.17 (MUST) Invocation reference supplied to a process step.** An implementation must supply the invocation reference to any process step that invoked it, so that the step's record cites the invocation.

**P13-12.18 (MUST) Run attributable to the initiating process instance.** An implementation must record the process instance that initiated an agent run where one did.

### 12.7 Boundary with Part 7, policy decision point and authorisation

**Delegated.** Every decision on whether an invocation, a tool call, a run or a resumption may proceed, and the assessment of the delegation behind an agent's request.

**Must not absorb.** Authorisation, entitlement and policy evaluation.

**Reciprocal, and its discharge.** `Part 7` section 12.13 requires this part to declare four things. That it owns invocation and the model artifact: clauses P13-1.1 and P13-1.2. That it does not evaluate policy: clauses P13-1.15 and P13-12.19. That it exposes a model output as an artifact with an identity and a digest that component can pin: clauses P13-3.3, P13-6.3 and P13-12.21. And that it treats a model found defective as a basis defect to `Part 3` so that decisions relying on it can be enumerated: section 3.11 and clause P13-12.8. Its clause P7-12.35 further forbids invocation during an evaluation, which clause P13-12.6 and clause P13-11.25 discharge from this side, and its clause P7-12.38 requires the delegation of an agent's request to be assessed, which clause P13-12.10 supports.

**P13-12.19 (MUST NOT) No policy evaluated.** An implementation must not evaluate a policy, determine an entitlement or render an authorisation decision.

**P13-12.20 (MUST) Authorisation obtained per invocation and per call.** An implementation must obtain an authorisation decision before every invocation and every tool call and must record the reference.

**P13-12.21 (MUST) Produced value pinnable.** An implementation must expose every produced value with an identity, a digest and an as of instant that `Part 7` can pin, and must mark it as a produced value rather than as a fact.

**P13-12.22 (MUST) Reproduction limit supplied.** An implementation must supply, with every produced value, the reproducibility declaration, so that a component reproducing a determination from the recorded value can record that it has not reproduced the invocation.

### 12.8 Boundary with Part 8, human task and case management

**Delegated.** The work item in which a person examines a produced value and takes responsibility for it, the queue, the case, and the recording of what was presented and what alternatives existed.

**Must not absorb.** The human act, and any representation of an invocation as one.

**Reciprocal, and its discharge.** `Part 8` clauses P8-12-34 to P8-12-36 require that component not to record an invocation as a human act, to record an agent completion with an agent actor class and an invocation reference, and to record whether a performer accepted an agent proposal unchanged. This part discharges the corresponding obligations by clauses P13-12.23 to P13-12.25: a produced value is supplied as a proposal and never as a completion, the invocation reference is supplied for the record, and the checking determination is received from that component rather than made here.

**P13-12.23 (MUST) Produced value supplied as a proposal.** An implementation must supply a produced value to a work item as a proposal and must not supply it as a completion or a default outcome.

**P13-12.24 (MUST) Invocation reference supplied for the completion record.** An implementation must supply the invocation reference that `Part 8` records on an agent completion.

**P13-12.25 (MUST) Checking determination received, not made.** An implementation must receive a checking determination from `Part 8` where a person made one and must record it unaltered.

**P13-12.26 (MUST NOT) No completion of a work item.** An implementation must not complete, claim, release or dispose of a work item.

### 12.9 Boundary with Part 9, schema and contract registry

**Delegated.** Schema identity, versioning and validation, including of output shapes and tool argument schemas.

**Must not absorb.** Validation and schema versioning.

**Reciprocal, and its discharge.** `Part 9` clauses P9-12-37 and P9-12-38 require that component to record whether an instance was produced under schema constrained generation, or that the fact is unknown, and forbid it from reporting such a validation as independent evidence. This part discharges the obligation by clause P13-3.26, which records the constraint and its kind on every invocation, and by clause P13-3.31, which notifies the consuming component of the vacuity class so that its validation record can carry the fact.

**P13-12.27 (MUST) Constraint disclosed to the validating component.** An implementation must disclose to `Part 9` whether an output it supplies was produced under a structural constraint and of what kind, or that the fact is unknown.

**P13-12.28 (MUST NOT) No validation performed.** An implementation must not validate an instance against a schema and must obtain validation from `Part 9`.

**P13-12.29 (MUST NOT) No validation treated as a check.** An implementation must not record a validation obtained from `Part 9` as a check of a produced value's content.

### 12.10 Boundary with Part 10, reference and master data management

**Delegated.** Every code system, value set, master record and party identity a produced value refers to or is drawn from.

**Must not absorb.** Reference content, and any assertion into it.

**Reciprocal, and its discharge.** `Part 10` clauses P10-12.39 to P10-12.42 require that component to record a model produced match, map entry or designation as a proposal, to record this component's invocation reference, to refuse a model authored concept without a human accepting act, and to record the accepting party. This part discharges the corresponding obligations by clause P13-12.30, which supplies every such output as a proposal, and by clause P13-12.31, which refuses to assert into that component at all.

**P13-12.30 (MUST) Reference proposals supplied as proposals.** An implementation must supply a produced match, map entry, designation or concept to `Part 10` as a proposal with its invocation reference.

**P13-12.31 (MUST NOT) No assertion into reference content.** An implementation must not assert a concept, member, map entry or master record, and must not represent a produced value as an accepted one.

**P13-12.32 (MUST) Bound values drawn from pinned versions.** An implementation must record the pinned value set version where an output was constrained to a governed enumeration, so that the constraint's provenance is recoverable.

### 12.11 Boundary with Part 11, content addressed artifact store

**Delegated.** The octets of every prompt, retrieved document, tool argument, tool result and output.

**Must not absorb.** The octets, and any provenance claim held in that component.

**Reciprocal, and its discharge.** `Part 11` clauses P11-12.37 to P11-12.39 require that component not to hold as an artifact attribute the claim that a model produced it, to accept invocation material as addressed artifacts, and not to infer correctness from addressability. This part discharges the corresponding obligations by clause P13-3.3, which holds all material by address, and by clause P13-12.34, which retains the provenance claim here where it can be substantiated.

**P13-12.33 (MUST) Material held by address.** An implementation must hold every prompt, document, argument, result and output by content address in `Part 11`.

**P13-12.34 (MUST) Provenance retained here.** An implementation must hold the claim that a model produced a given artifact in its own invocation record and must not require `Part 11` to hold it.

**P13-12.35 (MUST NOT) No correctness from addressability.** An implementation must not represent the addressing or verification of a produced value as evidence about its content.

### 12.12 Boundary with Part 12, conformance and assurance harness

**Delegated.** The assessment of this component against this part, and the assessment of any claim about a model's properties.

**Must not absorb.** Any assurance conclusion, finding or assessment.

**Reciprocal, and its discharge.** `Part 12` clauses P12-12.33 to P12-12.36 require that component to record a model produced determination as evidence rather than a finding, to require a human decision for every finding, to record the non determinism of any invocation an assessment relied upon, and to declare model use on every assurance statement. This part discharges the corresponding obligations by clause P13-12.36, which supplies the reproducibility declaration with every produced value used in an assessment, and by clause P13-12.37, which refuses to produce a finding.

**P13-12.36 (MUST) Reproducibility declaration supplied for assessment use.** An implementation must supply the reproducibility declaration and the variance sources with every produced value an assessment consumes.

**P13-12.37 (MUST NOT) No finding or assurance statement produced.** An implementation must not produce a finding, an assurance statement or a conformance conclusion.

**P13-12.38 (MUST) Elicitation supported.** An implementation must support the repeated invocation of a recorded context assembly at the request of `Part 12`, so that observed variance can be measured independently, and must record every such invocation as an invocation with its own cost.

**P13-12.39 (MUST) State exposed for verification.** An implementation must expose the state required to verify every externally observable clause of this part.

**P13-12.40 (MUST NOT) No self assurance.** An implementation must not report its own conformance to this part as assurance.

### 12.14 Boundary with Part 0, system composition

**Delegated.** What happens when the components run at once: authority over facts more than one component touches, the seams at which values cross boundaries, the propagation of non results, and the pinning of versions across a unit of work.

**Must not absorb.** Composition. This part records invocations and refuses to conclude anything about their outputs, and does not state what the estate should do with a produced value nobody checked.

**Reciprocal.** `Part 0` must declare that this component holds authority over invocations, model registrations, serving configurations, context assemblies, produced values, attempt sets, cost records, reproducibility declarations, agent runs, tool calls, effects and defect notifications, and over nothing else. It must state, for every seam, what must hold and how a violation appears here. It must in particular resolve the eight questions section 13.9 hands it.

**P13-12.41 (MUST) Authority declared, not assumed.** An implementation must not accept an assertion about an invocation, a produced value, a cost, an effect or a run from another component, and must require every such fact to be established by its own operations.

**P13-12.42 (MUST) Non results returned unmodified.** An implementation must return every outcome of section 7 unmodified regardless of whether the caller can represent it, and must not degrade a refusal, a filter, a truncation or a cache hit into a produced value.

**P13-12.43 (MUST) Unchecked consumption exposed to composition.** An implementation must make the unchecked consumed population, the vacuous check proportion and the unidentifiable consumer population available as signals, since none can be remedied within this component.

**P13-12.44 (MUST) Produced status preserved across every boundary.** An implementation must ensure the produced status travels with every value it supplies to another component, and must record where a consumer accepted a value without recording the status.

## 13. What could not be established

The authoring brief for this standard states that this part has the least standards support of the thirteen and that the author should expect to report much of it as unestablished rather than manufacture a specification. This section is longer in proportion than in any other part of this standard for that reason, and a reader who wants to know what this part does not do should read it before section 3.

### 13.1 Sources not obtained in full text

**The telemetry convention for generative artificial intelligence.** Not obtained directly. The span shapes, the attribute names, the metric names and the status were read at second hand through descriptions of the repository contents, the attribute registry and release notes, several of which post date the author's general knowledge and were established by search. Two facts material to this part were established and should be reverified before approval: that the conventions were moved to a dedicated repository in a release of 12 June 2026 and that every document in that repository carries the status Development, and that the requested and responding model are carried as separate attributes. The registry itself and the conventions' own text were not read.

**The non determinism work.** Not obtained as a primary document. The finding, the experimental result of eighty distinct completions from one thousand temperature zero invocations, the attribution to batch invariance rather than to floating point non associativity, and the reported throughput costs of deterministic execution were read through the original text as quoted in several places and through corroborating academic literature. The reference implementation was not examined. This is a single laboratory's engineering result, widely corroborated and not a standard, and clauses P13-6.12 and P13-6.13 rest on it.

**The artificial intelligence management system standard, the risk management guidance and the concepts and terminology standard.** None obtained. Paywalled. Section 10.4 rests on general knowledge and no clause depends on any of them.

**The regulatory logging obligations.** Not obtained. Section 10.5 rests on general knowledge of a regulation whose obligations are phased and whose detail is being developed through standardisation this part did not consult. The current state of both was not established. No clause depends on them, and a reviewer in a regulated setting should treat section 10.5 as a pointer rather than as an account.

**Declarative documentation practice and bill of materials formats.** Not obtained. Section 10.6 rests on general knowledge. The specific profiles for models and datasets in the emerging formats were not read and no clause depends on them.

**Idempotency conventions.** Not obtained. Clause P13-4.3 departs from the ordinary convention on its own reasoning and does not cite it.

**Prior parts of this standard.** `Part 7`, `Part 8`, `Part 9`, `Part 10`, `Part 11` and `Part 12` were available and their reciprocals are discharged at sections 12.7 through 12.12 with the discharging clauses named. `Part 1` through `Part 6` were not available, and sections 12.1 through 12.6 are written from this part's own analysis.

**P13-13.1 (MUST) Unverified reciprocals declared.** An implementation must not represent sections 12.1 through 12.6 as discharging a reciprocal statement of `Part 1` through `Part 6`, since the text of those parts was not read.

### 13.2 What a produced value is worth

This part establishes what a produced value is not. It does not establish what one is worth, and that is the question every reader actually has.

The position taken is that a produced value carries no warrant until an accountable party checks it, and the position is defensible and incomplete. It is incomplete because the volume of produced values in any real deployment exceeds by orders of magnitude what accountable parties can examine, so an estate conforming to this part will have an unchecked consumed population that is nearly the whole of its output. Clause P13-3.10 makes that number visible, which is progress, and it does not make it smaller.

Three constructions might close the gap and none is specified here. Sampling with attested checking, which `Part 12` supplies the machinery for and which would give a bounded statement over an enumerable population of produced values. Consequence based triage, in which the checking obligation attaches to the effect a value may have rather than to the value, which requires a consequence model this standard does not have. Or an accepted risk position, declared by an accountable party, that a class of produced values may be consumed unchecked, which is honest and is a governance act rather than an engineering one. The third is probably what most estates will do and this part gives them no mechanism for recording it, which is a gap section 13.9 hands forward.

### 13.3 Cost, which is measured and not comparable

Cost is the only subject in this part with hard numbers and it is the one where the numbers mislead most.

The units are the provider's. What a unit counts is the provider's definition, the definition changes, and two providers' units are not commensurable in any respect that matters. This part therefore requires a figure recorded in units it forbids anyone to aggregate, which is an unsatisfying requirement and is the honest one. A reviewer may reasonably ask what a finance function is supposed to do with it, and the answer this part gives is that the monetary amount is comparable where the pricing basis is recorded and the unit counts are not, and that presenting the second as though it were the first is the failure section 11.10 names.

What is not established: whether any normalisation is sound. A unit that counts fragments of text is not a measure of work, of value or of difficulty, and two providers whose units differ by a factor of three in count may differ by nothing in what they did. This part records the unit definition version and refuses the conversion, and a reviewer who needs a comparable figure should expect to construct it outside this component and to state its basis.

### 13.4 Reproducibility, which is required to be declared and is usually absent

Section 6.3 requires a reproducibility declaration on every invocation and section 3.7 defaults it to unknown. For a hosted model behind a provider alias, which is the overwhelmingly common case, the declaration will say unknown every time, and a reviewer may conclude that the requirement is empty.

It is not empty and it is close to it. What it achieves is that the absence of reproducibility becomes a recorded property of the estate rather than an assumption nobody examined, and clause P13-8.30 makes the distribution visible, which will be almost entirely unknown and should be seen to be. What it does not achieve is any reproducibility. The remedy exists, being a serving stack that asserts batch invariance, and it costs throughput, and it is not available from a provider that does not offer it. An estate that needs a reproducible determination cannot obtain one from a hosted alias, and this part's contribution is to make that fact impossible to overlook rather than to change it.

Two things were not established. Whether any provider offers a batch invariance assertion at the date of this part, and if so on what terms. And whether distribution reproducibility, being a claim that repeated invocation samples from the same distribution, is verifiable in practice at any sample size an estate would pay for. Clause P13-6.15 requires the two claims to be distinguished and specifies no method for establishing either.

### 13.5 Agent autonomy, deliberately not specified

Section 6.6 is thin and this subsection says why.

What this part specifies about agents is bounding, recording and refusal: four budgets, an authority envelope, an effect class, a termination reason enumeration, a prohibition on authority accretion and a prohibition on an agent determining its own success. Every one of those is a constraint on the record and on the perimeter, and none of them says anything about what an agent should be permitted to do.

The questions not answered are the ones people ask. Which objectives may be given to an agent at all. When an agent must stop and ask rather than proceed. How much of a decision an agent may make before a person is required. What makes an objective well formed enough to be delegated. How to decompose a task, and whether an agent may decompose its own. None of these is specified here, and the reason is that this part found nothing to rest such a specification on and declined to invent one. A manufactured answer would have the form of a standard and the content of an opinion, and it would be adopted because it was written down.

What this part offers instead is that every one of those questions becomes a declaration: the envelope declares what may be done, the budgets declare how far, and the effect classes declare what may be changed irreversibly. Who sets the declarations, and on what basis, is not this component's and section 13.9 hands it forward.

### 13.6 Evaluation, deliberately not specified

This part specifies no evaluation of any model and clause P13-1.24 forbids representing any measurement it makes as one. Clause P13-3.86 forbids exposing an accuracy figure and clause P13-6.52 forbids computing one.

The reason is not that evaluation is unimportant. It is that a component that measures the outputs it produced is in the position section 11.2 and `Part 12` both name: the party producing the value is measuring it, the measurement is favourable, and the whole apparatus of `Part 12` exists because that arrangement establishes nothing. An evaluation of a model is an assessment, assessments belong to `Part 12`, and `Part 12` requires an accountable party, an independence declaration and a falsification attempt, none of which this component can supply about its own outputs.

What is therefore unspecified anywhere in this standard is how a model should be evaluated. `Part 12` supplies the machinery for assessing a claim and this part supplies the invocation records an assessment would need, and neither supplies a method, a benchmark, a metric or a threshold. That is a real gap in the standard as a whole and it is recorded here rather than filled.

### 13.7 Repeated structure across the standard, closing at thirteen parts

`Part 4` recorded three repeated structures, `Part 5` five, `Part 6` six, `Part 7` eight with one divergence, `Part 10` eleven with two, `Part 11` twelve, `Part 12` thirteen. This part is the last of the thirteen and closes the register rather than extending it. Every item below is now the responsibility of `Part 0`, which is the only part remaining and the only one whose subject is the composition in which these structures recur.

**The authority that can prove what it did and not what happened.** Five components. `Part 7` cannot see enforcement, `Part 10` cannot see consumption, `Part 11` cannot see citation, `Part 12` cannot see whether its samples were representative, and this component cannot see whether anything it produced was checked before being acted upon. Five independent arrivals at one structure, and the fifth is the one whose invisible population is the population of consequences. `Part 12` discharged the enumerable case and refused the rest. **This is the register's first item, it has been demonstrated five times, and it is the first thing `Part 0` should specify.**

**The refusal to return a wrong value for a non result.** Five instances. `Part 7` refuses not applicable as deny, `Part 10` refuses unknown as non membership, `Part 11` refuses integrity failure as absence, `Part 12` refuses not assessed as satisfied, and this part refuses a refusal, a filter, a truncation and a cache hit as a produced value. Five subjects, one principle, five vocabularies.

**The refusal of order dependent resolution.** Now eight parts, with this part's refusal of selection by attempt order. Eight refusals, eight vocabularies, one principle, and each with its own recorded cost.

**The declared completeness of a set.** Now eleven parts. This part contributes the content recording level and the enumeration completeness of a defect notification.

**The honest undeclared or unreported value.** All thirteen parts. This part contributes `identity_unverifiable`, `cache_hit`, `empty`, `unknown` as the default reproducibility class, and the uncertain effect outcome.

**The immutable record with stateful assertions about it.** All thirteen parts. Here the immutable invocation record carries a produced value whose checking state changes.

**The retention obligation a component cannot discover.** Four appearances. This part's clause P13-8.47 imposes it on `Part 1` and `Part 11` in turn.

**The refusal to arbitrate.** Now eight. This part returns every applicable attempt and requires the selection to be recorded rather than concealed.

**The asymmetric bridge that disproves and cannot prove.** Resolved in principle by `Part 12` and unresolved in allocation. This part supplies the material an elicitation needs, at clause P13-12.38, and does not build a bridge of its own.

**The marking vocabulary for restricted content.** Six parts and unchanged. This part does not withhold.

**The residue model.** Still two, `Part 6` and `Part 7`.

**The extended third value.** Still an inconsistency between `Part 5` and `Part 7`, unresolved through thirteen parts. This part does not adopt an extended form.

**The divergence in clause convention.** `Part 8` and `Part 9` remain outside the convention the other eleven parts share. Neither exposes a section 12.13, so this part derived both boundaries from their content, as `Part 10`, `Part 11` and `Part 12` did. **Fourth consecutive part affected, and now the last: every part that will ever need to read those two sections has now had to work around them.** `Part 12` recorded that it has also become an assessment problem, since a harness must register two extraction methods.

**Closing the register.** Thirteen items across thirteen parts, two of them inconsistencies rather than repetitions, one demonstrated five times and one resolved in principle. Six consecutive parts recorded the register and five recommended acting before the next part, and no part acted because no part could: every item spans components and no component may specify across a boundary. That is the correct outcome of the discipline and it is also its cost. The register is now handed in full to `Part 0`.

**P13-13.2 (MUST) Register handed forward complete.** An implementation must treat the thirteen items of section 13.7 as the standard's own record of its unresolved cross component structures and must not represent any of them as resolved by this part.

### 13.8 What this part deliberately did not attempt

No conformance assessment of any system was performed or anticipated, per clause P13-1.26.

No evaluation method, benchmark, metric or threshold for any model, per section 13.6.

No specification of what a model is, what kinds exist, or what any of them can do. Clause P13-1.27 confines this part to the record.

No specification of what an agent may be permitted to do, when it must stop and ask, or what makes an objective delegable, per section 13.5.

No prompt engineering, instruction design, context construction strategy or retrieval method. Section 3.12 requires instruction material to be versioned and addressed and says nothing about its content.

No safety, alignment, harm or content policy. This part records a refusal and a provider filter as outcomes and takes no position on either.

No specification of a normalisation across cost units, per section 13.3.

No specification of how to make inference reproducible, beyond requiring the declaration and recording the published remedy, per section 13.4.

No treatment of a model an organisation trains or fine tunes itself, and therefore no treatment of training data, provenance of weights, or the relationship between a fine tuned model and its base. Clause P13-3.14 admits content addressed weights as an identity class and this part says nothing else about them.

No treatment of a model invoked across an organisational boundary where the invoking party cannot record what the serving party did.

No performance or scale requirement, and section 13.3 records the volume concern without a threshold.

**P13-13.3 (MUST) Gaps declared, not filled.** An implementation must not represent a matter listed in section 13.8 as specified by this part.

**P13-13.4 (SHOULD) Open questions carried forward.** A reviewer of this part should record a position on each open question in section 13, and where a position is adopted it should be recorded in the review outcome rather than by silent amendment of the clause it affects.

### 13.9 Questions handed to Part 0 rather than answered here

Whether an estate may declare that a class of produced values may be consumed unchecked, and by what act. Section 13.2 records that this is what most estates will do and that this part supplies no mechanism for recording it. It is the most consequential omission in this part.

Who sets an agent's authority envelope, its budgets and its permitted effect classes, and on what basis. Section 13.5 records that this part specifies the declarations and not the declaring.

Whether the sampling and attestation machinery of `Part 12` should be applied to produced values, so that an estate can make a bounded statement about the proportion of its unchecked output that would have survived a check.

How a unit of work spanning this component, `Part 2`, `Part 5`, `Part 7`, `Part 9` and `Part 10` pins a produced value, a rule set version, a criterion version, a policy version, a schema version and a value set version together. `Part 7` handed forward four of these, `Part 10` added three, and this part adds the produced value, which is the only one of them that is not reproducible.

Whether the retention obligation a component cannot discover should be a composition level device. Fourth part to ask.

Who is accountable for a produced value that was consumed unchecked and turned out to be wrong, given that this component records the consumption, `Part 8` records that no person examined it, and neither has authority over the consumer.

Whether an agent run may initiate an agent run in another component's authority, and how the composite authority is established, since clause P13-6.40 bounds nesting and says nothing about whose authority the nested run exercises.

Whether the thirteen structures of section 13.7 should each be specified once. This is the last of the thirteen parts to ask, and no further part remains to ask it.
