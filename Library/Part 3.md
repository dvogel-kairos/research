# KAIROS STD 003 Part 3: Provenance and Audit Ledger

**Standard.** KAIROS STD 003, the enterprise architecture standard.
**Part.** Part 3 of 14 (Part 0 and Parts 1 through 13). Cited as `KAIROS STD 003 Part 3`.
**Title.** Provenance and audit ledger.
**Version.** 1.0.0.
**Status.** Proposed. This part has not been approved and is not effective. It is issued for review against the authoring brief of 2026-08-17.
**Date of issue.** 2026-08-17.
**Supersedes.** Nothing. This is the first version.

## Binding of requirement language

The key words MUST, MUST NOT, SHOULD, SHOULD NOT and MAY in this part are to be interpreted as described in RFC 2119 and RFC 8174, and only in the upper case forms. This part does not use SHALL, SHALL NOT, REQUIRED, RECOMMENDED, NOT RECOMMENDED or OPTIONAL as requirement keywords.

Every requirement in this part is a numbered clause. A clause identifier has the form `P3-S.N`, where `S` is the section number and `N` is the ordinal of the clause within that section. Clause identifiers are permanent. A clause that is later removed has its identifier retired and never reissued. A clause that is later added to a section takes the next unused ordinal in that section, so ordinals are stable but not contiguous over the life of the part.

Text that is not a numbered clause is not binding. Narrative, tables, graphs, examples and the discussion of standards are provided to make the clauses intelligible and testable, and where a table carries normative content a clause says so explicitly and names the table.

## Conformance

An implementation conforms to this part if it satisfies every MUST and MUST NOT clause and records, for each SHOULD and SHOULD NOT clause it does not satisfy, the reason. This part does not define conformance levels, profiles or a certification scheme, and it does not define the method of assessment. Assessment method is the subject of `KAIROS STD 003 Part 12` and is out of scope here.

Where a clause states that a value is an implementation decision, conformance requires that the implementation declare the value, not that it adopt a particular one. An undeclared implementation decision is a nonconformity.

## Clause index

The index below is generated from the clause text of this document. It lists every clause identifier, its modality and its subject label. The counts that follow the index are derived by the same extraction and are stated with the grain at which they were counted.

| Clause | Modality | Subject |
| --- | --- | --- |
| **Section 1** | | **Scope and responsibilities** |
| `P3-1.1` | MUST | Purpose satisfaction |
| `P3-1.2` | MUST | Three properties distinguished |
| `P3-1.3` | MUST NOT | No assessment of correctness |
| `P3-1.4` | MUST NOT | No determining |
| `P3-1.5` | MUST NOT | No re derivation to explain |
| `P3-1.6` | MUST | Reliance distinguished from availability |
| `P3-1.7` | MUST | Survivability |
| `P3-1.8` | MUST NOT | No update in place |
| `P3-1.9` | MUST NOT | No telemetry absorption |
| `P3-1.10` | MUST NOT | No absorption of neighbouring responsibilities |
| `P3-1.11` | MUST | Completeness limit declared |
| `P3-1.12` | SHOULD | Declared exclusions |
| `P3-1.13` | MUST NOT | No conformance self assertion |
| `P3-1.14` | MUST | Time horizon declaration |
| **Section 2** | | **Terminology** |
| `P3-2.1` | MUST | Single meaning per term |
| `P3-2.2` | MUST NOT | No redefinition |
| `P3-2.3` | MUST NOT | No collapsing of the three properties |
| `P3-2.4` | MUST NOT | No collapsing of reliance and availability |
| `P3-2.5` | MUST NOT | No collapsing of the three structures |
| `P3-2.6` | MUST NOT | No collapsing of the three clocks |
| `P3-2.7` | MUST NOT | No agent as accountable party |
| `P3-2.8` | SHOULD | Term registry |
| **Section 3** | | **Data model** |
| `P3-3.1` | MUST | Declared types |
| `P3-3.2` | MUST NOT | No semantic identifiers |
| `P3-3.3` | MUST | Language tag present |
| `P3-3.4` | MUST NOT | No caller supplied knowledge time |
| `P3-3.5` | MUST | Three valued domain used unchanged |
| `P3-3.6` | MUST | Three structures distinguishable |
| `P3-3.7` | MUST NOT | No merged structure |
| `P3-3.8` | MUST | Separate retention |
| `P3-3.9` | MUST | Cross structure traversal |
| `P3-3.10` | MUST | Entity coverage |
| `P3-3.11` | MUST NOT | No update in place |
| `P3-3.12` | MUST NOT | No basis amendment |
| `P3-3.13` | MUST | Determination classified |
| `P3-3.14` | MUST | Owning component recorded |
| `P3-3.15` | MUST | Conclusion cited, not copied |
| `P3-3.16` | MUST | Completeness claimed explicitly |
| `P3-3.17` | MUST NOT | No inferred completeness |
| `P3-3.18` | MUST | Occurrence and knowledge time both recorded |
| `P3-3.19` | MUST | Evaluation instant required where anything was resolved as of a time |
| `P3-3.20` | MUST | All five parts present |
| `P3-3.21` | MUST | Resolution outcome recorded in full |
| `P3-3.22` | MUST | Digest absence reasoned |
| `P3-3.23` | MUST | Indeterminate reliance permitted and reported |
| `P3-3.24` | MUST NOT | No omission of the reliance flag |
| `P3-3.25` | MUST | Citation order declared |
| `P3-3.26` | MUST | Locator where a position was relied upon |
| `P3-3.27` | MUST NOT | No citation without a determination |
| `P3-3.28` | MUST | Closed role set |
| `P3-3.29` | MUST NOT | No role extension |
| `P3-3.30` | MUST | Reliance constraints enforced |
| `P3-3.31` | MUST | Context recorded where supplied |
| `P3-3.32` | MUST NOT | No context as input |
| `P3-3.33` | MUST | Authority present on every determination |
| `P3-3.34` | MUST | Method present on every determination |
| `P3-3.35` | MUST | Selection criterion required where alternatives exist |
| `P3-3.36` | MUST | Delegation present where the actor is not the accountable party |
| `P3-3.37` | MUST | Scope declared |
| `P3-3.38` | MUST | Completeness declared |
| `P3-3.39` | MUST | Both instants recorded |
| `P3-3.40` | MUST | Withheld absence distinguished |
| `P3-3.41` | MUST NOT | No negative citation with results |
| `P3-3.42` | SHOULD | Query recorded |
| `P3-3.43` | MUST | Unknown completeness reportable |
| `P3-3.44` | MUST | Method kind registered |
| `P3-3.45` | MUST | Method pinned where pinnable |
| `P3-3.46` | MUST | Determinism declared |
| `P3-3.47` | MUST | Parameters recorded or their absence declared |
| `P3-3.48` | MUST | Judgement declared as judgement |
| `P3-3.49` | MUST | Judgement is a frontier |
| `P3-3.50` | MUST | Undeclared method reportable |
| `P3-3.51` | MUST NOT | No method inference |
| `P3-3.52` | MUST | Non result acceptance recorded |
| `P3-3.53` | MUST | Non result envelope pinned unaltered |
| `P3-3.54` | MUST | Disposition declared |
| `P3-3.55` | MUST | Supporting pin where the disposition requires one |
| `P3-3.56` | MUST | Rationale recorded |
| `P3-3.57` | MUST | Proceeding without basis countable |
| `P3-3.58` | MUST | Acceptance appears in the basis |
| `P3-3.59` | MUST | Alternatives recorded where a selection occurred |
| `P3-3.60` | MUST | Elimination ground recorded |
| `P3-3.61` | MUST | Eliminating citation linked |
| `P3-3.62` | MUST | Not evaluable distinguished |
| `P3-3.63` | MUST NOT | No winner only selection record |
| `P3-3.64` | MUST | Alternatives appear in the basis |
| `P3-3.65` | MUST | Every terminus is a declared frontier |
| `P3-3.66` | MUST | Justification recorded |
| `P3-3.67` | MUST | External reference where external |
| `P3-3.68` | MUST | Undeclared frontier is a defect |
| `P3-3.69` | MUST | Adoption boundary declared |
| `P3-3.70` | MUST | Disposition cited at a retention frontier |
| `P3-3.71` | MUST | Access frontiers belong to the reading |
| `P3-3.72` | MUST NOT | No frontier as closure |
| `P3-3.73` | MUST | Expected closability recorded |
| `P3-3.74` | MUST | Actor and accountable party both recorded |
| `P3-3.75` | MUST | Accountable party is a person or an organisation |
| `P3-3.76` | MUST | Delegation chain complete |
| `P3-3.77` | MUST | Agent attribution recorded as such |
| `P3-3.78` | MUST | Instrument recorded or its absence reasoned |
| `P3-3.79` | MUST NOT | No inferred delegation |
| `P3-3.80` | MUST | Attestation recorded where relied upon |
| `P3-3.81` | MUST | Five conditions assessed |
| `P3-3.82` | MUST | Chain assembled without the producer |
| `P3-3.83` | MUST | Cycle detection |
| `P3-3.84` | MUST | Depth and breadth bounds declared |
| `P3-3.85` | MUST | Pins dereferenceable independently |
| `P3-3.86` | MUST NOT | No partial chain as complete |
| `P3-3.87` | MUST | Defect accepted from the owning component |
| `P3-3.88` | MUST | Impact enumerated exhaustively |
| `P3-3.89` | MUST | Reliance value carried forward |
| `P3-3.90` | MUST | Materiality unassessed by default |
| `P3-3.91` | MUST | Assessment attributed |
| `P3-3.92` | MUST NOT | No determination amendment on defect |
| `P3-3.93` | MUST | Unsound determinations reportable |
| `P3-3.94` | MUST | Defect propagates through prior determinations |
| `P3-3.95` | MUST | Transitive depth declared |
| `P3-3.96` | MUST | Sequence carries order |
| `P3-3.97` | MUST | Contiguity required and gaps reported |
| `P3-3.98` | MUST | Determination linkage where present |
| `P3-3.99` | MUST | State digests where the state changed |
| `P3-3.100` | MUST NOT | No trail as basis |
| `P3-3.101` | MUST | Reads recorded in the trail where the subject is sensitive |
| `P3-3.102` | MUST | Values addressed, not copied |
| `P3-3.103` | MUST | Partiality declared |
| `P3-3.104` | MUST | Source nodes are frontiers |
| `P3-3.105` | MUST | Design lineage joined where available |
| `P3-3.106` | MUST NOT | No design lineage authority |
| `P3-3.107` | MUST | Divergence from design reportable |
| `P3-3.108` | MUST | Append only sequence |
| `P3-3.109` | MUST | Segments sealed and committed |
| `P3-3.110` | MUST | Commitment procedure pinned |
| `P3-3.111` | MUST | External anchoring |
| `P3-3.112` | MUST | Anchor cycle declared |
| `P3-3.113` | MUST | Receipts issued |
| `P3-3.114` | MUST | Gaps detected and recorded |
| `P3-3.115` | MUST | Reconciliation performed |
| `P3-3.116` | MUST | Completeness limit stated to every reader |
| `P3-3.117` | MUST NOT | No completeness claim |
| `P3-3.118` | MUST | Registering components enumerated |
| `P3-3.119` | MUST NOT | No deletion for integrity |
| `P3-3.120` | MUST | Projections are pure |
| `P3-3.121` | MUST | Projection recomputable |
| `P3-3.122` | MUST | Named projections available |
| `P3-3.123` | MUST | Reliance filtered projections separate |
| `P3-3.124` | MUST | Reverse index available |
| `P3-3.125` | MUST NOT | No writes through a projection |
| `P3-3.126` | MUST | Demonstration satisfiable |
| **Section 4** | | **Interfaces** |
| `P3-4.1` | MUST | Operation classes separated |
| `P3-4.2` | MUST | Refusal is an outcome |
| `P3-4.3` | MUST | Idempotence key accepted |
| `P3-4.4` | MUST | Refusal at registration, not repair later |
| `P3-4.5` | MUST NOT | No partial registration |
| `P3-4.6` | MUST | Preconditions checked at registration |
| `P3-4.7` | MUST | Whole basis in one operation |
| `P3-4.8` | MUST | Authority or a frontier |
| `P3-4.9` | MUST | Defect reported only by the owner |
| `P3-4.10` | MUST NOT | No caller supplied sequence |
| `P3-4.11` | MUST | Anchor store independence checked |
| `P3-4.12` | MUST | Registrant declares its classes |
| `P3-4.13` | MUST NOT | No self registration of determinations |
| `P3-4.14` | MUST | Reconstruction records its own run |
| `P3-4.15` | MUST | Five condition result returned |
| `P3-4.16` | MUST NOT | No recomputation during traversal |
| `P3-4.17` | MUST | Reverse index latency declared |
| `P3-4.18` | MUST | Truncation stated |
| `P3-4.19` | MUST | Verification results recorded |
| `P3-4.20` | MUST | Reads do not traverse implicitly |
| `P3-4.21` | MUST NOT | No partial basis |
| `P3-4.22` | MUST | Gaps marked in a trail |
| `P3-4.23` | MUST | Coverage readable |
| `P3-4.24` | MUST | Caller obligations declared |
| `P3-4.25` | MUST NOT | No implied completeness in a result |
| `P3-4.26` | MUST | Absence of defect not reported as soundness |
| `P3-4.27` | MUST | Unavailability recorded, not propagated as failure |
| `P3-4.28` | MUST NOT | No substitution on unavailability |
| `P3-4.29` | MUST | Unobtainability is timestamped, not permanent |
| `P3-4.30` | MUST | Minimum event set |
| `P3-4.31` | MUST | Envelope minimum |
| `P3-4.32` | MUST NOT | No event in place of an entry |
| `P3-4.33` | MUST | Cessation of registration detected |
| `P3-4.34` | MUST NOT | No suppression of adverse events |
| **Section 5** | | **State model** |
| `P3-5.1` | MUST | Determinations have no lifecycle |
| `P3-5.2` | MUST | Assertions carry the state |
| `P3-5.3` | MUST NOT | No status field on a determination |
| `P3-5.4` | MUST | Correction is a new determination |
| `P3-5.5` | MUST | Enumerated soundness states |
| `P3-5.6` | MUST | Enumerated transitions only |
| `P3-5.7` | MUST NOT | No return to sound as recorded |
| `P3-5.8` | MUST | Assessment attributed and reasoned |
| `P3-5.9` | MUST | Unassessable recorded rather than inferred |
| `P3-5.10` | MUST NOT | No automatic assessment |
| `P3-5.11` | MUST | Suspected unsoundness surfaced in every read |
| `P3-5.12` | MUST | Enumerated segment states |
| `P3-5.13` | MUST | Sealing on a declared boundary |
| `P3-5.14` | MUST | Commitments chained |
| `P3-5.15` | MUST | External verification distinguished from integrity failure |
| `P3-5.16` | MUST | Integrity failure terminal and reported |
| `P3-5.17` | MUST NOT | No commitment recomputation |
| `P3-5.18` | MUST | Unanchored interval bounded and declared |
| `P3-5.19` | MUST | Enumerated gap states |
| `P3-5.20` | MUST NOT | No dismissal |
| `P3-5.21` | MUST | Allocation cited where claimed |
| `P3-5.22` | MUST | Undetermined cause countable |
| `P3-5.23` | MUST | Supersession is a relation |
| `P3-5.24` | MUST | Supersession kind recorded |
| `P3-5.25` | MUST | Correction implies a defect |
| `P3-5.26` | MUST | Superseded determinations remain readable |
| `P3-5.27` | MUST | Enumerated run states |
| `P3-5.28` | MUST | Pins attempted before assessment |
| `P3-5.29` | MUST | Truncation recorded on the run |
| `P3-5.30` | MUST | Truncated runs still assessed |
| `P3-5.31` | MUST NOT | No truncated chain as closed |
| `P3-5.32` | MUST | Abandonment detected and recorded |
| `P3-5.33` | MUST | Terminal states are terminal |
| **Section 6** | | **Execution semantics** |
| `P3-6.1` | MUST | Traversal order total and declared |
| `P3-6.2` | MUST | Bounds applied deterministically |
| `P3-6.3` | MUST | Assessment deterministic given resolution results |
| `P3-6.4` | MUST | Resolution results recorded per attempt |
| `P3-6.5` | MUST NOT | No caching of resolution results as facts |
| `P3-6.6` | MUST | Three orderings distinguished |
| `P3-6.7` | MUST | Sequence is the integrity order |
| `P3-6.8` | MUST | Occurrence order not totalised |
| `P3-6.9` | MUST | Retrograde citation flagged |
| `P3-6.10` | MUST | Occurrence beyond knowledge time bounded |
| `P3-6.11` | MUST | Causal cycles reported |
| `P3-6.12` | MUST NOT | No reordering on read |
| `P3-6.13` | MUST | Knowledge time assigned by this component |
| `P3-6.14` | MUST NOT | No occurrence time assignment |
| `P3-6.15` | MUST | Application time cited, not determined |
| `P3-6.16` | MUST | Instants in a declared scale |
| `P3-6.17` | MUST | Monotonic knowledge time within a stream |
| `P3-6.18` | MUST | Idempotence by key |
| `P3-6.19` | MUST | Deduplication window declared |
| `P3-6.20` | MUST NOT | No idempotence across differing payloads |
| `P3-6.21` | MUST | Duplicate registration without a key detectable |
| `P3-6.22` | MUST | Algorithm order |
| `P3-6.23` | MUST | Access frontier against the run |
| `P3-6.24` | MUST | Unobtainable pin becomes an undeclared frontier |
| `P3-6.25` | MUST | Soundness returned with the chain |
| `P3-6.26` | MUST | Five assessments returned separately |
| `P3-6.27` | MUST NOT | No resolution of what was in force |
| `P3-6.28` | MUST | Three bounds declared |
| `P3-6.29` | MUST | Primary budget deterministic |
| `P3-6.30` | MAY | Secondary non deterministic guard |
| `P3-6.31` | MUST | Non deterministic truncation marked |
| `P3-6.32` | MUST | Truncation point recorded |
| `P3-6.33` | MUST NOT | No silent bound |
| `P3-6.34` | MUST | Propagation exhaustive at the first hop |
| `P3-6.35` | MUST | Transitive propagation through prior determinations |
| `P3-6.36` | MUST | Impact set orderable by reliance |
| `P3-6.37` | MUST NOT | No propagation through context only paths beyond the first hop |
| `P3-6.38` | MUST | Unbounded application time handled |
| `P3-6.39` | MUST | Recomputation by the pinned procedure |
| `P3-6.40` | MUST | Chain of commitments verified |
| `P3-6.41` | MUST | Verification recorded whether or not adverse |
| `P3-6.42` | MUST | Limit statement accompanies every result |
| `P3-6.43` | MUST NOT | No repair by verification |
| `P3-6.44` | MUST | Permitted computations only |
| `P3-6.45` | MUST NOT | No inference of a missing citation |
| `P3-6.46` | MUST NOT | No inference of reliance |
| `P3-6.47` | MUST NOT | No inference of a frontier kind |
| **Section 7** | | **Outcome and failure taxonomy** |
| `P3-7.1` | MUST | Closed outcome set |
| `P3-7.2` | MUST NOT | No additional members |
| `P3-7.3` | MUST | Frontier kinds enumerated with the outcome |
| `P3-7.4` | MUST | Complete and to frontier distinguished |
| `P3-7.5` | MUST | Withheld distinguished from incomplete |
| `P3-7.6` | MUST | Defective escalated separately |
| `P3-7.7` | MUST NOT | No mapping onto two values |
| `P3-7.8` | MUST NOT | No caller selected collapse |
| `P3-7.9` | MUST | Outcome derived by the table |
| `P3-7.10` | MUST | All assessments returned |
| `P3-7.11` | MUST | Precedence applied as stated |
| `P3-7.12` | MUST | Withheld overrides nothing |
| `P3-7.13` | MUST | Envelope completeness |
| `P3-7.14` | MUST NOT | No envelope reduction |
| `P3-7.15` | MUST | Counts by role and reliance included |
| `P3-7.16` | MUST | Integrity state included |
| `P3-7.17` | MUST | Refusal codes |
| `P3-7.18` | MUST | Refusal states what to supply |
| `P3-7.19` | MUST | Refusals recorded and counted |
| `P3-7.20` | MUST NOT | No refusal as an outcome of reconstruction |
| `P3-7.21` | MUST NOT | No silent acceptance on retry |
| `P3-7.22` | MUST | Read refusal codes |
| `P3-7.23` | MUST | Unknown determination distinguished from withheld |
| `P3-7.24` | MUST NOT | No not found for withheld |
| `P3-7.25` | MUST | Recording obligations honoured |
| `P3-7.26` | MUST | Emission obligations honoured |
| `P3-7.27` | MUST | Reader obligations documented |
| `P3-7.28` | MUST NOT | No adequacy language for an incomplete outcome |
| `P3-7.29` | MUST | Three properties reported separately |
| `P3-7.30` | MUST NOT | No correctness member |
| `P3-7.31` | MUST | Closed and unsound reportable together |
| `P3-7.32` | MUST | An account that stopped is never an account that closed |
| **Section 8** | | **Observability and the audit record** |
| `P3-8.1` | MUST | Own operations recorded |
| `P3-8.2` | MUST | Self recording depth declared |
| `P3-8.3` | MUST | Assurance from outside |
| `P3-8.4` | MUST NOT | No self exemption |
| `P3-8.5` | MUST | Declared grain |
| `P3-8.6` | MUST | Context citations recorded individually |
| `P3-8.7` | MUST | Impact at citation grain |
| `P3-8.8` | MUST | Counting grain stated with every count |
| `P3-8.9` | MUST | Reconstruction sufficiency |
| `P3-8.10` | MUST | Request recorded as received |
| `P3-8.11` | MUST | Precondition outcomes recorded, including passes |
| `P3-8.12` | MUST | Periodic reconstruction sampling |
| `P3-8.13` | MUST | Decay recorded, not corrected |
| `P3-8.14` | MUST | Reads recorded |
| `P3-8.15` | MUST | Withholding recorded |
| `P3-8.16` | MUST | Reverse index queries recorded |
| `P3-8.17` | MUST NOT | No unrecorded export |
| `P3-8.18` | SHOULD | Read records retained with the subject |
| `P3-8.19` | MUST | Signals produced |
| `P3-8.20` | MUST | Signals derived from entries |
| `P3-8.21` | MUST NOT | No suppression of a signal |
| `P3-8.22` | MUST | Refusal signal reaches the registrant's owner |
| `P3-8.23` | MUST | Cessation signal is a standing measure |
| `P3-8.24` | MUST | Decay trend available |
| `P3-8.25` | SHOULD | Signal thresholds declared |
| `P3-8.26` | MUST | Package sufficiency |
| `P3-8.27` | MUST | Verification procedure included |
| `P3-8.28` | MUST | Limit statements included |
| `P3-8.29` | MUST | Absence stated, not omitted |
| `P3-8.30` | MUST | Package digest |
| `P3-8.31` | MUST | Soundness included |
| `P3-8.32` | MUST | Self description |
| `P3-8.33` | MUST | Retention obtained, not assigned |
| `P3-8.34` | MUST | Basis outlives the determination's obligation |
| `P3-8.35` | MUST | Separate retention per structure |
| `P3-8.36` | MUST | Integrity material outlives the entries it covers |
| `P3-8.37` | MUST | Disposal recorded and cited |
| `P3-8.38` | MUST NOT | No disposal under an open impact record |
| `P3-8.39` | MUST NOT | No disposal of a cited basis |
| `P3-8.40` | MUST NOT | No amendment of an entry |
| `P3-8.41` | MUST NOT | No amendment of a reconstruction outcome |
| `P3-8.42` | MUST | Migration preserves sequence and digests |
| `P3-8.43` | MUST | Own assurance determinations recorded as determinations |
| **Section 9** | | **Extension model** |
| `P3-9.1` | MUST | Closed sets not extended |
| `P3-9.2` | MUST | Unknown member is a defect, not a default |
| `P3-9.3` | MUST | Open sets registered |
| `P3-9.4` | MUST | Additional distinction through cited kind |
| `P3-9.5` | MUST | Registry as controlled document |
| `P3-9.6` | MUST NOT | No key reuse |
| `P3-9.7` | MUST | Deprecation rather than removal |
| `P3-9.8` | MUST | Registry version recorded with the entry |
| `P3-9.9` | MUST | Semantics in the entry |
| `P3-9.10` | MUST | Legitimacy declared per kind |
| `P3-9.11` | MUST | Chain or reading declared |
| `P3-9.12` | MUST | Required evidence declared |
| `P3-9.13` | MUST NOT | No new kind to avoid a defect |
| `P3-9.14` | MUST | Stability declared |
| `P3-9.15` | SHOULD | Stable schemes preferred for citations |
| `P3-9.16` | MUST NOT | No cross scheme comparison |
| `P3-9.17` | MUST | Clause identifier scheme supported |
| `P3-9.18` | MUST | Pinnability declared |
| `P3-9.19` | MUST | Frontier status declared |
| `P3-9.20` | MUST | Owning component declared |
| `P3-9.21` | MUST NOT | No procedural kind for judgement |
| `P3-9.22` | MUST | Class mandates declared and enforced |
| `P3-9.23` | MUST | Owning component per class |
| `P3-9.24` | MUST | Expected method kinds declared |
| `P3-9.25` | MUST | Retention basis per class |
| `P3-9.26` | MUST | Three registries separate |
| `P3-9.27` | MUST | Commitment procedure fully specified |
| `P3-9.28` | MUST | Deprecation without invalidation |
| `P3-9.29` | MUST NOT | No digest without a profile |
| `P3-9.30` | MUST | Refusal codes registered with remedy |
| `P3-9.31` | MUST | Event types registered |
| `P3-9.32` | MUST | Cited kinds registered with their owner |
| `P3-9.33` | MUST | Prior determination cited by identity |
| `P3-9.34` | MUST | Composite cites its members |
| `P3-9.35` | MUST NOT | No basis borrowing |
| `P3-9.36` | MUST | Composite depth bounded and declared |
| `P3-9.37` | MUST NOT | No cyclic citation |
| **Section 10** | | **Standards and specifications** |
| `P3-10.1` | MUST | Cited edition recorded |
| `P3-10.2` | MUST | Basis marked |
| `P3-10.3` | MUST | Practice basis recorded |
| `P3-10.4` | MUST | Unsourced requirements identified |
| **Section 11** | | **Anti patterns** |
| `P3-11.1` | MUST NOT | No telemetry as a basis |
| `P3-11.2` | MUST NOT | No undifferentiated input list |
| `P3-11.3` | MUST NOT | No undeclared terminus |
| `P3-11.4` | MUST NOT | No completeness claim from integrity |
| `P3-11.5` | MUST NOT | No undetected cessation |
| `P3-11.6` | MUST NOT | No inferred completeness |
| `P3-11.7` | MUST NOT | No unrecorded proceeding |
| `P3-11.8` | MUST NOT | No withheld as complete |
| `P3-11.9` | MUST NOT | No judgement as procedure |
| `P3-11.10` | MUST NOT | No selection without alternatives |
| `P3-11.11` | MUST NOT | No producer dependent pin |
| `P3-11.12` | MUST NOT | No basis amendment |
| `P3-11.13` | MUST NOT | No replay as explanation |
| `P3-11.14` | MUST NOT | No combined indicator |
| `P3-11.15` | SHOULD | Impact queue aged and ordered |
| `P3-11.16` | MUST NOT | No computed materiality |
| `P3-11.17` | SHOULD | Reliance ratio monitored per registrant |
| `P3-11.18` | MUST NOT | No timestamp ordering |
| `P3-11.19` | MUST NOT | No gap dismissal |
| `P3-11.20` | MUST NOT | No self anchoring |
| `P3-11.21` | MUST NOT | No agent as accountable party |
| `P3-11.22` | MUST NOT | No inferred delegation |
| `P3-11.23` | MUST NOT | No basis borrowing |
| `P3-11.24` | MUST NOT | No summary as a citation |
| `P3-11.25` | MUST NOT | No forward only traversal |
| `P3-11.26` | MUST NOT | No authoritative copies |
| **Section 12** | | **Boundaries with other parts** |
| `P3-12.1` | MUST | Declared allocation |
| `P3-12.2` | MUST | Recording rather than substitution |
| `P3-12.3` | MUST NOT | No reaching past a neighbour |
| `P3-12.4` | MUST | Resolution outcome recorded, never re resolved |
| `P3-12.5` | MUST NOT | No force state held or asserted |
| `P3-12.6` | MUST | Retraction accepted as a basis defect |
| `P3-12.7` | MUST | Whole report recorded |
| `P3-12.8` | MUST NOT | No re evaluation |
| `P3-12.9` | MUST | Drift accepted as a basis defect |
| `P3-12.10` | MUST | Design lineage cited, not asserted |
| `P3-12.11` | MUST | Divergence reportable |
| `P3-12.12` | MUST | Alternatives and criterion recorded as reported |
| `P3-12.13` | MUST NOT | No assessment of the selection |
| `P3-12.14` | MUST | Process steps are acts, not citations |
| `P3-12.15` | MUST NOT | No process identity required |
| `P3-12.16` | MUST | Decisions consumed, not made |
| `P3-12.17` | MUST NOT | No delegation validation |
| `P3-12.18` | MUST | Withheld scope identified as withheld |
| `P3-12.19` | MUST | Assessments recorded independently of tasks |
| `P3-12.20` | MUST NOT | No task driven closure |
| `P3-12.21` | MUST | Schema reference recorded, not evaluated |
| `P3-12.22` | MUST | Reference sets cited, not held |
| `P3-12.23` | MUST | Reference correction accepted as a defect |
| `P3-12.24` | MUST | Digest is the interface |
| `P3-12.25` | MUST NOT | No ledger state in the store |
| `P3-12.26` | MUST | Read only assessment |
| `P3-12.27` | MUST NOT | No self assessment as assessment |
| `P3-12.28` | MUST | Independent verification supported |
| `P3-12.29` | MUST | Invocation record cited, not the value alone |
| `P3-12.30` | MUST | Non determinism recorded |
| `P3-12.31` | MUST | Model defect accepted as a basis defect |
| `P3-12.32` | MUST | Authority declared, not assumed |
| `P3-12.33` | MUST | Refusal is visible to composition |
| **Section 13** | | **What could not be established** |
| `P3-13.1` | MUST | Verification before approval |
| `P3-13.2` | MUST | Gaps declared, not filled |
| `P3-13.3` | SHOULD | Open questions carried forward |

### Derived counts

Every figure below is derived by extraction from the clause text of this document and not asserted independently. The grain of counting is stated for each figure. A clause is one line of the document matching the clause heading form given under Binding of requirement language, that is, an identifier of the form `P3-S.N`, a modality in parentheses, and a subject label. Narrative sentences containing a requirement keyword are not clauses and are not counted; per that same section they are not binding.

**Total clauses.** 440. Grain: one clause heading.

**By modality.** Grain: one clause heading, counted once against its single declared modality.

| Modality | Clauses | Share |
| --- | --- | --- |
| MUST | 313 | 71.1% |
| MUST NOT | 117 | 26.6% |
| SHOULD | 9 | 2.0% |
| SHOULD NOT | 0 | 0.0% |
| MAY | 1 | 0.2% |
| **All** | **440** | **100.0%** |

**Absolute requirements.** 430 clauses carry MUST or MUST NOT and are therefore conditions of conformance. 9 carry SHOULD or SHOULD NOT and require a recorded reason where not satisfied. 1 carry MAY and constrain nothing. Grain: one clause heading. These three figures sum to the total.

**By section.** Grain: one clause heading, attributed to the numbered section in which its heading appears.

| Section | Title | Clauses | MUST | MUST NOT | SHOULD | SHOULD NOT | MAY |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Scope and responsibilities | 14 | 6 | 7 | 1 | 0 | 0 |
| 2 | Terminology | 8 | 1 | 6 | 1 | 0 | 0 |
| 3 | Data model | 126 | 103 | 22 | 1 | 0 | 0 |
| 4 | Interfaces | 34 | 25 | 9 | 0 | 0 | 0 |
| 5 | State model | 33 | 27 | 6 | 0 | 0 | 0 |
| 6 | Execution semantics | 47 | 35 | 11 | 0 | 0 | 1 |
| 7 | Outcome and failure taxonomy | 32 | 23 | 9 | 0 | 0 | 0 |
| 8 | Observability and the audit record | 43 | 34 | 7 | 2 | 0 | 0 |
| 9 | Extension model | 37 | 29 | 7 | 1 | 0 | 0 |
| 10 | Standards and specifications | 4 | 4 | 0 | 0 | 0 | 0 |
| 11 | Anti patterns | 26 | 0 | 24 | 2 | 0 | 0 |
| 12 | Boundaries with other parts | 33 | 24 | 9 | 0 | 0 | 0 |
| 13 | What could not be established | 3 | 2 | 0 | 1 | 0 | 0 |
| **All** | | **440** | **313** | **117** | **9** | **0** | **1** |

**Ordinal integrity.** In this version, the highest ordinal in each section equals the number of clauses in that section, so no identifier has yet been retired. This will cease to be true at the first clause removal, and the count rather than the highest ordinal is then the figure to rely on.

## 1. Scope and responsibilities

### 1.1 What this component is

This part specifies a component that records what determinations rested on, so that the reasoning behind any determination can be reconstructed by someone who was not present, using no component that produced it, at a time when the systems involved may no longer exist.

The component exists to answer one question reliably: **on what did this determination rest, and can a person who was not there establish that it rested on those things and on nothing undisclosed.** Every other responsibility in this part is subordinate to that question.

Three properties must be distinguished at the outset, because the whole part turns on keeping them apart and because almost every discussion of audit trails collapses them.

**Reconstructable** means a reader can see what the determination rested on and obtain each of those things at the version relied upon. This component establishes reconstructability. It is the only one of the three it establishes.

**Sound** means that what the determination rested on was in fact true, valid and in force at the time. This component reports on soundness, because it can compare what was relied upon against what the owning components later say about those artifacts. It does not guarantee soundness and cannot, because an artifact can be wrong without anyone knowing.

**Correct** means the conclusion follows from the premises by the method. This component does not assess correctness, does not evaluate it, and must not be represented as doing so. A determination can be perfectly reconstructable, resting on perfectly sound premises, and wrong.

A component that conflates these three will claim to have validated determinations it has merely recorded, and the claim is the most damaging thing it can do, because it produces confidence in place of evidence.

The component is accountable for the following.

The determination record: the identity of a conclusion or act that had reasons, recorded by reference, immutable once written.

The citation: the typed, pinned, role bearing link from a determination to something it rested on, including the mode by which it was obtained and whether it was relied upon or merely available.

The closed taxonomy of citation roles, which is the substance of what a determination must cite.

Negative citations: reliance on the absence of something, recorded with the scope and completeness of the search that established the absence.

The method citation: the procedure, algorithm, expression, model version or human judgement that combined the premises into the conclusion.

The record of a non result accepted: where a determination proceeded despite an input it could not obtain or could not evaluate, and on what basis.

Alternatives considered and rejected, where the determination involved a selection.

Frontiers: the declared points at which a chain of reasoning stops, and the reason each stops there.

Attribution and delegation: the actor who made the determination, and the chain by which accountability reaches a person or an organisation.

The chain: the transitive closure of citations from a determination, its closure properties, and the enumerated ways in which it fails to close.

Basis defect and soundness assessment: the recorded finding that something a determination rested on has since been retracted, superseded, withdrawn or found defective, and the enumeration of every determination so affected.

The audit trail: the ordered history of what happened to a subject, as distinct from what a determination rested on.

Instance lineage: how a particular value came to have its value through actual transformations, as distinct from the design level lineage of `Part 4`.

The ledger itself: its append only structure, its sequence, its segmentation, its integrity anchoring, and the enumerated limits of what integrity anchoring can establish.

### 1.2 What this component is not

Each exclusion below names something a provenance ledger absorbs if nobody stops it. This component is more prone to absorption than any other in the standard, for a structural reason: everything cites it, so every component has a reason to push its own records here, and a ledger that accepts them acquires invariants it cannot hold and a retention obligation it cannot meet.

The component is not the determiner. It does not evaluate constraints, which is `Part 2`. It does not select among outcomes, which is `Part 5`. It does not authorise, which is `Part 7`. It records what those components determined and what they said they rested on.

The component is not the authority on what was in force. Which version of a document governed at an application time is a `Part 1` determination, obtained by resolution. This is the reciprocal declaration `Part 1` clause P1-12.6 requires and section 12.1 makes it binding.

The component is not the store of the artifacts it cites. It holds identities, versions and digests. Octets belong to `Part 11` and controlled content to `Part 1`.

The component is not the schema level lineage repository. That a field is derived from another field by a declared transformation is a design fact belonging to `Part 4`. That this value was derived from that value in this run is a historical fact belonging here. Section 12.4 states the split and section 13.4 records that it is contestable.

The component is not the workflow history. That a task was assigned, escalated and completed is process state belonging to `Part 6`. A process step is not a reason. A determination made at the end of a five step process cites what it rested on, not the five steps.

The component is not an operational telemetry or monitoring system. Application logs, traces, metrics and diagnostics are not provenance. They have a different grain, a different retention, a different reader and a volume three or more orders of magnitude larger. Merging them is the anti pattern of section 11.1 and it destroys the ledger by making its retention unaffordable.

The component is not a general event bus. Other components emit events; this one records determinations and their bases. Receiving every event any component emits is the absorption `Part 1` section 12.3 warns against.

The component is not an identity provider. Actors are opaque references resolvable elsewhere, and the delegation chains of section 3.12 are recorded rather than validated.

The component is not a model invocation record. What a model was asked, what it returned, what it cost and how it was retried belongs to `Part 13`. This component cites the invocation record.

The component is not a conformance assessor, of itself or of anything else. Assessment belongs to `Part 12`.

The component is not a search or analytics platform. It must make chains traversable and determinations findable by their citations; ranking, similarity and free text retrieval quality are out of scope.

**P3-1.1 (MUST) Purpose satisfaction.** An implementation must be able to produce, for any determination within its retained history, the complete set of things it rested on with their roles, versions and pins, and the enumerated closure outcome of the chain, by the mechanism specified in section 6.

**P3-1.2 (MUST) Three properties distinguished.** An implementation must distinguish reconstructability, soundness and correctness as specified in section 1.1, must report the first two separately, and must not report on the third.

**P3-1.3 (MUST NOT) No assessment of correctness.** An implementation must not evaluate, assert or represent that a determination's conclusion follows from its premises.

**P3-1.4 (MUST NOT) No determining.** An implementation must not evaluate a constraint, select among outcomes, authorise an operation or resolve what was in force, and must obtain each from the component to which section 12 allocates it.

**P3-1.5 (MUST NOT) No re derivation to explain.** An implementation must not recompute, re evaluate or re resolve anything in order to explain a determination, and must construct every explanation from the records it holds.

**P3-1.6 (MUST) Reliance distinguished from availability.** An implementation must record, for every citation, whether the cited thing was relied upon or was merely available, per section 3.6, and must not record availability as reliance.

**P3-1.7 (MUST) Survivability.** The evidence package specified in section 8.6 must be sufficient to establish what a determination rested on without the implementation running and without access to any component of this standard other than the package itself.

**P3-1.8 (MUST NOT) No update in place.** An implementation must not represent any state change specified by this part as a modification or deletion of a previously written row, tuple, object or event.

**P3-1.9 (MUST NOT) No telemetry absorption.** An implementation must not accept operational logs, traces, metrics or diagnostics into the ledger, and must declare the boundary between what it accepts and what it does not.

**P3-1.10 (MUST NOT) No absorption of neighbouring responsibilities.** An implementation must not hold document status, rule state, process state, schema level lineage, model invocation records or authorisation policy, as those responsibilities are allocated in section 12.

**P3-1.11 (MUST) Completeness limit declared.** An implementation must declare, in terms a reader can act on, that its integrity mechanisms establish that recorded entries were not altered and do not establish that every determination was recorded, per section 3.17.

**P3-1.12 (SHOULD) Declared exclusions.** An implementation should publish, as a controlled document under `Part 1`, the list of section 1.2 exclusions that it in fact provides by other means, so that a reader can tell what the implementation does not guarantee.

**P3-1.13 (MUST NOT) No conformance self assertion.** An implementation must not assert conformance to this part on the basis of its own internal checks alone, and must not represent such an assertion as an assessment.

**P3-1.14 (MUST) Time horizon declaration.** An implementation must declare the period for which it undertakes to answer the purpose question, as a duration or an absolute date rather than as an indefinite commitment.

### 1.3 Why reconstructability is the hard requirement

Recording what happened is easy and almost every system does it. Recording what a determination rested on is hard, and the difficulty is not volume. It is that the information is not available at the moment it must be captured unless the determining component was built to surrender it.

A component that reaches a conclusion knows what it read. It rarely knows, and almost never records, which of the things it read the conclusion actually depended on. It read a subject record with forty fields and used four. It resolved three documents and relied on one. It received an indeterminate verdict and proceeded on a default nobody wrote down. It considered two candidate outcomes and chose one. All four of those facts are the reasoning, and all four are absent from a record of what happened.

This is why section 3.6 makes the citation role a closed enumeration and why section 4.2 refuses a determination record that omits one. The component cannot infer a role, cannot infer reliance, and must not accept a bare list of everything in scope. A ledger that accepts an undifferentiated list of inputs has recorded that a determination occurred in the vicinity of some data.

The second difficulty is that reasoning does not terminate. A verdict rested on a rule, which rested on a policy clause, which rested on a regulation, which rested on a statute. A subject value came from a feed, which came from a system, which came from a keyboard. Every chain either terminates at a declared point or trails off. Section 3.11 makes the termination explicit, because an undeclared frontier is indistinguishable from a missing citation and the two require different responses.

## 2. Terminology

Terms are defined here only if this component owns them. A term owned by another part is cited to that part and is not redefined. Where a term is taken from an external standard, the standard is named. Where this part narrows or diverges from the external definition, the divergence is stated.

Definitions are given in the singular. A definition is not a clause and is not binding on its own; clauses that depend on a definition cite the term.

### 2.1 Terms owned by this part

**Determination.** A recorded conclusion or act that had reasons, and that some component other than this one is accountable for having made. A determination is not a computation, an event or a state change; it is a conclusion whose basis someone may later be required to account for. Whether a given act is a determination is declared by its owning component, not inferred here.

**Basis.** The whole set of things a determination rested on, as recorded. The basis is the thing this part exists to hold.

**Citation.** One recorded link from a determination to one thing in its basis, carrying a role, a pin, a mode of obtaining, and a reliance flag. A citation is a claim about the determination, not a reference in the bibliographic sense.

**Role.** The part a cited thing played in the determination, drawn from the closed set of section 3.6.

**Reliance.** The recorded claim that the determination would or might have concluded differently had the cited thing been different. Distinguished from availability throughout.

**Availability.** The recorded fact that a thing was in scope and could have been read, without the claim that the determination depended on it.

**Negative citation.** A citation whose subject is the absence of something, carrying the scope searched, the instant as of which it was searched, and whether the search was complete.

**Method.** The procedure, algorithm, expression, decision table, model version, or declared human judgement by which the basis produced the conclusion. Corresponds to the plan of a PROV Association, which W3C PROV-DM treats as the third term of the ternary relation between an activity and an agent.

**Frontier.** A declared point at which a chain of reasoning stops, together with the reason it stops there, drawn from the closed set of section 3.11.

**Chain.** The transitive closure of citations reachable from a determination, terminating at frontiers.

**Closure.** The property that every citation in a chain resolves, every cited artifact is obtainable at its pinned version, and every terminus is a declared frontier. Closure is enumerated rather than boolean; section 7.2 gives the outcomes.

**Reconstruction.** The operation of assembling a chain and reporting its closure outcome. Reconstruction never recomputes.

**Soundness assessment.** A recorded comparison between what a determination relied upon and what the owning components now say about those artifacts.

**Basis defect.** A recorded finding that something a determination relied upon has since been retracted, superseded, withdrawn, found defective, or shown to have been misresolved. A basis defect does not make the determination wrong; it makes it unsound.

**Determination supersession.** The relation in which a later determination replaces an earlier one on the same subject. The earlier determination remains a true record of what was concluded then.

**Audit trail.** The ordered history of acts concerning one subject. Distinct from a basis, which concerns one determination.

**Instance lineage.** The record of how a particular value came to have its value through actual transformations in actual runs. Distinct from the design level lineage of `Part 4`.

**Ledger.** The append only sequence of entries this component holds.

**Entry.** One appended row in the ledger, bearing a sequence number within a stream.

**Segment.** A bounded, sealed range of entries over which an integrity commitment is computed.

**Commitment.** A digest over a segment, computed by a declared procedure, from which alteration of any entry in the segment is detectable.

**Anchor.** A commitment published to a store the implementation does not control, so that a later reader can establish that the ledger was not rewritten wholesale.

**Receipt.** A returned proof that a given entry was included in the ledger at a stated position. Term and sense follow the SCITT architecture of RFC 9943, in which a transparency service issues a receipt on registering a signed statement.

**Attestation.** A signed statement by an identified actor that something is so, recorded as an entry and relied upon as a frontier where nothing further is available.

**Delegation.** The relation by which an actor acted on behalf of another, ultimately reaching an accountable person or organisation. Term and sense follow the `actedOnBehalfOf` relation of W3C PROV-DM.

**Accountable party.** The natural person or the organisation at the terminus of a delegation chain. An automated agent is never an accountable party.

**Knowledge time.** The instant at which this component durably recorded an entry, assigned by this component. Used unchanged from `Part 1` section 2.1.

**Occurrence time.** The instant at which a recorded act happened in the world, as asserted by an actor. Used unchanged from `Part 1`.

**Application time.** The time dimension in which artifacts are in force. Used unchanged from `Part 1`, and cited rather than resolved here.

### 2.2 Clauses governing terminology

**P3-2.1 (MUST) Single meaning per term.** An implementation must use each term defined in section 2.1 with the meaning given there in all of its interfaces, records, reports and documentation.

**P3-2.2 (MUST NOT) No redefinition.** An implementation must not use a term defined in section 2.1 for a different concept, and must not use a different term for a concept defined in section 2.1 in any interface specified by this part.

**P3-2.3 (MUST NOT) No collapsing of the three properties.** An implementation must not use one term or one field for reconstructability, soundness or correctness.

**P3-2.4 (MUST NOT) No collapsing of reliance and availability.** An implementation must not use one term or one field for both.

**P3-2.5 (MUST NOT) No collapsing of the three structures.** An implementation must not use one term for a basis, an audit trail and an instance lineage, per section 3.2.

**P3-2.6 (MUST NOT) No collapsing of the three clocks.** An implementation must not use one term or one field for more than one of application time, knowledge time and occurrence time.

**P3-2.7 (MUST NOT) No agent as accountable party.** An implementation must not record an automated agent as the terminus of a delegation chain, per section 3.12.

**P3-2.8 (SHOULD) Term registry.** An implementation should publish the terms it adds beyond section 2.1, with definitions, as a controlled document under `Part 1`.
## 3. Data model

The model is stated as entities with typed fields. For each field the model gives its type, whether it is required, its cardinality, and what its absence means. Absence semantics are stated because in this component the commonest wrong inference from a missing field is that the thing was not relied upon, and the second commonest is that it was.

### 3.1 Type vocabulary

| Type | Value space | Notes |
| --- | --- | --- |
| `ID` | An opaque, globally unique, immutable identifier | Never reused. Never parsed for meaning. |
| `URN` | A persistent name in a declared namespace | Resolvable by the component owning the namespace. |
| `ATIME` | An instant in application time | Cited, never resolved here. |
| `KTIME` | An instant in knowledge time, assigned by this component | Never accepted from a caller. |
| `OTIME` | An instant asserted by an actor as when an act occurred | Never assigned by this component. |
| `SEQ` | A monotonically increasing ordinal within a named stream | Total order within the stream only. Gaps are detectable and reportable. |
| `DIGEST` | An algorithm identifier and a value | Algorithm from the registry of section 9.7. |
| `ENUM` | A member of a named closed or registered set | The set is named at every point of use. |
| `TEXT` | A sequence of characters intended for a person | Carries a `LANG`. |
| `LANG` | A language tag per BCP 47 | Required wherever `TEXT` appears. |
| `PIN` | An identity, a version and where available a digest of a cited artifact | Sufficient to obtain the identical artifact again. |
| `ACTOR` | An opaque reference to a person, organisation or automated agent | Carries its kind. Resolved elsewhere. |
| `AUTHREF` | A reference to an authorisation decision made by `Part 7` | Recorded, never evaluated here. |
| `PATH` | A locator into an artifact, in a named path scheme | Registered under section 9.4. |
| `SCOPE` | A declared extent over which a search was performed | Required on every negative citation. |
| `COUNT` | A non negative integer | Grain stated wherever reported. |
| `TRUTH` | One of `TRUE`, `FALSE`, `INDETERMINATE` | The three valued domain, used unchanged from `Part 2` section 6.2. |
| `DURATION` | A length of time, independent of any instant | |

**P3-3.1 (MUST) Declared types.** An implementation must be able to state, for every field it holds that corresponds to a field in this section, which type of the table above it carries.

**P3-3.2 (MUST NOT) No semantic identifiers.** An implementation must not derive the meaning, role, reliance, soundness or class of any record from the characters of its `ID` or `URN`.

**P3-3.3 (MUST) Language tag present.** An implementation must record a `LANG` with every `TEXT` value and must not default it silently.

**P3-3.4 (MUST NOT) No caller supplied knowledge time.** An implementation must assign every `KTIME` itself and must reject an entry that supplies one.

**P3-3.5 (MUST) Three valued domain used unchanged.** An implementation must use the truth domain and connective semantics of `Part 2` section 6.2 wherever it holds or reports a truth value, and must not introduce a two valued reduction.

### 3.2 Three structures, deliberately separate

This component holds three structures. They are routinely built as one table called the audit log, and the result is none of the three.

**The basis** is a directed acyclic graph rooted at a determination, whose edges are citations and whose leaves are frontiers. It answers what a conclusion rested on. It is read backwards from a conclusion, once, usually years later, by an investigator.

**The audit trail** is a totally ordered sequence of acts concerning one subject. It answers what happened to this thing, in what order. It is read forwards, frequently, by anyone reviewing a subject's history.

**The instance lineage** is a directed acyclic graph over values, whose edges are actual transformations in actual runs. It answers where this number came from. It is read backwards from a value, by a data steward tracing an error.

The three differ in every dimension that matters to an implementation. Their grains differ: one determination, one subject act, one value transformation. Their graph shapes differ: rooted DAG, total order, DAG over a different node type. Their volumes differ by orders of magnitude, lineage being the largest and basis the smallest. Their retention differs, since a basis must outlive the determination's obligation while a lineage may be disposable once the value is superseded. And their readers differ, which means a single presentation serves none of them well.

They are held in one component rather than three because they share the citation and pin machinery of section 3.5, because they share the integrity machinery of section 3.17, and because a real chain crosses between them: a determination cites a value, the value's lineage reaches a source, and the source's audit trail shows when it was loaded. Splitting them across components would put a boundary in the middle of every real question.

**P3-3.6 (MUST) Three structures distinguishable.** An implementation must hold the basis, the audit trail and the instance lineage as distinguishable structures, and must be able to state for any entry which structure it belongs to.

**P3-3.7 (MUST NOT) No merged structure.** An implementation must not represent a basis edge, an audit trail act and a lineage transformation as instances of one undifferentiated entry type.

**P3-3.8 (MUST) Separate retention.** An implementation must permit the retention period of each structure to be set independently, per section 8.7.

**P3-3.9 (MUST) Cross structure traversal.** An implementation must permit a traversal that begins in one structure and continues in another, and must record at every crossing which structure it moved into.

### 3.3 Entity inventory

Every entity is immutable once written. A change is a new entry; nothing specified in this part is ever updated in place. The reason is stronger here than in `Part 1` or `Part 2`: this component's only product is testimony about what other components did, and testimony that can be edited is not testimony.

| Group | Entity | Purpose |
| --- | --- | --- |
| Determination | `determination` | The identity and classification of a recorded conclusion. |
| Determination | `determination_conclusion` | The conclusion reached, by reference. |
| Determination | `determination_supersession` | A later determination replacing an earlier. |
| Basis | `citation` | One typed, pinned, role bearing link to something in the basis. |
| Basis | `negative_citation` | Reliance on an absence, with the search that established it. |
| Basis | `method_citation` | The method by which the basis produced the conclusion. |
| Basis | `non_result_acceptance` | A determination proceeding despite an unobtainable or unevaluable input. |
| Basis | `alternative_considered` | A candidate outcome not selected, and the criterion. |
| Basis | `frontier` | A declared terminus of a chain. |
| Basis | `basis_digest` | A digest binding the whole basis of a determination. |
| Attribution | `attribution` | The actor who made the determination. |
| Attribution | `delegation_step` | One link in the chain from actor to accountable party. |
| Attribution | `attestation` | A signed statement relied upon as a frontier. |
| Soundness | `soundness_assessment` | A recorded comparison of relied upon artifacts against present belief. |
| Soundness | `basis_defect` | A finding that a relied upon artifact is now defective. |
| Soundness | `defect_impact` | The relation between a basis defect and an affected determination. |
| Trail | `subject_act` | One act concerning one subject, in trail order. |
| Trail | `trail_stream` | The named ordered stream for one subject. |
| Lineage | `value_node` | One value at one point in one run. |
| Lineage | `transformation` | One actual derivation of values from values. |
| Ledger | `ledger_entry` | The append only record of everything above. |
| Ledger | `ledger_segment` | A sealed range over which a commitment is computed. |
| Ledger | `commitment` | A digest over a segment. |
| Ledger | `anchor_publication` | A commitment published externally. |
| Ledger | `receipt` | A returned inclusion proof. |
| Ledger | `gap_observation` | A detected discontinuity in a sequence. |
| Ledger | `reconciliation` | A comparison of this ledger's counts against an emitting component's. |
| Reconstruction | `reconstruction_run` | One attempt to assemble and close a chain. |
| Reconstruction | `reconstruction_outcome` | The enumerated result of a run. |
| Access | `access_record` | One return of a record to a principal. |
| Registry | `role_registration` | Reserved. Roles are closed; see section 9.1. |
| Registry | `frontier_kind_registration` | A registered frontier kind. |
| Registry | `method_kind_registration` | A registered method kind. |
| Registry | `determination_class_registration` | A registered class of determination. |

**P3-3.10 (MUST) Entity coverage.** An implementation must be able to state, for every entity in the table above, where the information it carries is held, or that the entity is not applicable because the corresponding optional capability is not provided.

**P3-3.11 (MUST NOT) No update in place.** An implementation must not represent any state change specified by this part as a modification or deletion of a previously written entry.

**P3-3.12 (MUST NOT) No basis amendment.** An implementation must not add a citation to, remove a citation from, or alter a citation of a recorded determination, and must record any correction as a further determination whose relation to the earlier one is recorded.

### 3.4 The determination

`determination` fields:

| Field | Type | Required | Cardinality | Absence means |
| --- | --- | --- | --- | --- |
| `determination_id` | `ID` | yes | 1 | n/a |
| `class` | `ENUM` | yes | 1 | n/a. Registered under section 9.8. |
| `subject_reference` | `URN` | yes | 1..n | n/a. What the determination is about. |
| `owning_component` | `URN` | yes | 1 | n/a. The component accountable for having made it. |
| `conclusion_reference` | `URN` | yes | 1 | n/a. The conclusion, held by its owner, cited not copied. |
| `conclusion_digest` | `DIGEST` | no | 0..1 | The conclusion is not digestible or the owner supplied none. Reduces reconstructability and is reportable. |
| `occurred_otime` | `OTIME` | yes | 1 | n/a. Asserted by the owning component. |
| `recorded_ktime` | `KTIME` | yes | 1 | n/a |
| `evaluation_instant` | `ATIME` | no | 0..1 | The determination did not resolve anything as of an application time. Presence is required wherever any citation was resolved as of a time. |
| `basis_complete_declared` | `TRUTH` | yes | 1 | n/a. The owning component's claim that the basis as recorded is complete. |
| `basis_digest` | `DIGEST` | yes | 1 | n/a |
| `sequence` | `SEQ` | yes | 1 | n/a |

The `basis_complete_declared` field is the owning component's assertion, not this component's finding, and the distinction is the reason the field exists. This component can establish that every recorded citation resolves. It cannot establish that nothing was omitted, because an omission leaves no trace. What it can do is require the owning component to make the claim explicitly, so that a false claim is a false statement by an identified party rather than an absence of information. Section 3.17 states the general form of this limit and section 11.6 names the failure it prevents.

**P3-3.13 (MUST) Determination classified.** An implementation must record a registered class for every determination and must not default it.

**P3-3.14 (MUST) Owning component recorded.** An implementation must record the component accountable for each determination and must not record itself.

**P3-3.15 (MUST) Conclusion cited, not copied.** An implementation must record the conclusion by reference and digest, and must not hold the conclusion as its own authoritative copy.

**P3-3.16 (MUST) Completeness claimed explicitly.** An implementation must require the owning component to declare whether the basis it supplied is complete, must record the declaration as that component's claim, and must not infer it.

**P3-3.17 (MUST NOT) No inferred completeness.** An implementation must not represent a basis as complete on the basis of its own checks, and must report the declaration and the closure outcome separately.

**P3-3.18 (MUST) Occurrence and knowledge time both recorded.** An implementation must record both, must assign the second itself, and must record where the first exceeds the second by more than a declared tolerance.

**P3-3.19 (MUST) Evaluation instant required where anything was resolved as of a time.** An implementation must refuse a determination record carrying a citation resolved as of an application time where no `evaluation_instant` is recorded.

### 3.5 The citation and its five parts

A citation is not a link. A link says that two things are related. A citation says five things, and a record missing any of the five is not reconstructable.

**What.** The identity of the cited thing, its version, and where available its digest, together sufficient to obtain the identical artifact again.

**How obtained.** The mode of resolution and the whole outcome the resolving component returned. This is where `Part 1` clause P1-12.6 and `Part 2` clause P2-12.6 bind: the resolution outcome envelope, not the resolved identifier; the whole evaluation report, not a summary.

**What part it played.** The role, from the closed set of section 3.6.

**Whether it was relied upon.** The reliance flag, distinguishing dependence from availability.

**When.** The instants: as of what application time it was resolved, and at what knowledge time it was obtained.

`citation` fields:

| Field | Type | Required | Cardinality | Absence means |
| --- | --- | --- | --- | --- |
| `citation_id` | `ID` | yes | 1 | n/a |
| `determination_id` | `ID` | yes | 1 | n/a |
| `role` | `ENUM` | yes | 1 | n/a. Closed set of section 3.6. |
| `pin` | `PIN` | yes | 1 | n/a |
| `cited_kind` | `ENUM` | yes | 1 | n/a. Registered. The kind of artifact, for example document version, verdict, report, value, prior determination. |
| `locator` | `PATH` | no | 0..1 | The whole artifact was cited rather than a position within it. |
| `resolution_mode` | `ENUM` | yes | 1 | n/a. One of `PINNED`, `AS_OF`, `SUPPLIED_BY_CALLER`, `ATTESTED`. |
| `resolution_outcome` | `PIN` | no | 0..1 | Required where `resolution_mode` is `AS_OF`. Holds the whole outcome envelope the resolving component returned. |
| `relied_upon` | `TRUTH` | yes | 1 | n/a. `INDETERMINATE` is permitted and means the owning component could not establish whether the conclusion depended on it. |
| `resolved_as_of_atime` | `ATIME` | no | 0..1 | The citation was not resolved as of an application time. |
| `obtained_ktime` | `KTIME` | yes | 1 | n/a |
| `digest_absent_reason` | `ENUM` | no | 0..1 | Required where the pin carries no digest. |
| `citation_ordinal` | `SEQ` | yes | 1 | n/a. Position within the basis, in a declared order. |

The `relied_upon` field admits `INDETERMINATE`, and this is deliberate rather than a concession. A component often cannot say whether its conclusion depended on a particular input: the code read forty fields and the dependency structure is not recoverable. Requiring a binary answer would produce a guess, and a guess recorded as a fact is worse than a recorded uncertainty. What is not permitted is omitting the field, because then the uncertainty is invisible and a reader will assume reliance or assume availability according to temperament. Section 8.5 requires the count of indeterminate reliance to be a standing signal, because a component whose citations are all indeterminate has not recorded a basis.

**P3-3.20 (MUST) All five parts present.** An implementation must record the role, the pin, the resolution mode, the reliance flag and the obtaining instant for every citation, and must refuse a citation missing any of them.

**P3-3.21 (MUST) Resolution outcome recorded in full.** An implementation must record the whole outcome envelope a resolving component returned for every citation of mode `AS_OF`, and must not record the resolved identifier alone.

**P3-3.22 (MUST) Digest absence reasoned.** An implementation must record a reason wherever a pin carries no digest, and must be able to report every such citation.

**P3-3.23 (MUST) Indeterminate reliance permitted and reported.** An implementation must accept `INDETERMINATE` as a reliance value, must not convert it to `TRUE` or `FALSE`, and must include the count in the signals of section 8.5.

**P3-3.24 (MUST NOT) No omission of the reliance flag.** An implementation must refuse a citation without a reliance value.

**P3-3.25 (MUST) Citation order declared.** An implementation must declare the order in which citations are ordinalled and must not vary it between reads of the same basis.

**P3-3.26 (MUST) Locator where a position was relied upon.** An implementation must record a locator wherever the determination relied upon a position within an artifact rather than the whole of it.

**P3-3.27 (MUST NOT) No citation without a determination.** An implementation must not record a citation that is not attached to a recorded determination.
### 3.6 What a determination must cite: the closed role taxonomy

This is the answer to the first question the part was asked, and it is a closed enumeration because an open one would let a component invent a role that no consumer knows how to read.

Thirteen roles. The table is normative.

| Role | Means | Reliance |
| --- | --- | --- |
| `AUTHORITY` | What makes the determination legitimate: the rule, the policy clause, the delegated power, the contractual term. | Always `TRUE`. A determination does not have an authority it did not rely on. |
| `PREMISE` | A fact relied upon as true. | `TRUE` or `INDETERMINATE`. |
| `NEGATIVE_PREMISE` | An absence relied upon as true, recorded per section 3.7. | `TRUE` or `INDETERMINATE`. |
| `INPUT` | A value consumed by the method. | Any. |
| `CONSTRAINT_OUTCOME` | A verdict or evaluation report obtained from `Part 2`. | Any. |
| `SELECTION_CRITERION` | The rule of choice applied where the determination selected among alternatives, obtained from `Part 5`. | Always `TRUE` where any alternative was considered. |
| `ALTERNATIVE_REJECTED` | A candidate outcome that was available and not selected, recorded per section 3.10. | `FALSE` by construction: the determination did not rest on it, and the record exists to show that a choice occurred. |
| `DERIVED_INTERMEDIATE` | A value computed during the determination and used by it. | Any. |
| `PRIOR_DETERMINATION` | An earlier determination relied upon rather than re derived. | Any. |
| `DELEGATION` | The authority under which the acting actor acted, recorded per section 3.12. | Always `TRUE`. |
| `METHOD` | The procedure that combined the basis into the conclusion, recorded per section 3.8. | Always `TRUE`. |
| `CONTEXT` | Something available to the determination and not relied upon. | Always `FALSE`. |
| `NON_RESULT_ACCEPTED` | An input the determination could not obtain or could not evaluate, and proceeded despite, recorded per section 3.9. | Always `TRUE`, because proceeding despite it is a dependence on the decision to proceed. |

Four of the thirteen carry most of the weight and each is absent from every provenance model reviewed for this part.

**`CONTEXT` against everything else.** This is the distinction between what was in scope and what was relied upon. A component that records forty fields as inputs has told a reader nothing, because thirty six of them were noise. Recording the thirty six as `CONTEXT` and the four as `INPUT` is the difference between a basis and a data dump. W3C PROV-DM has `used`, which is undifferentiated, so the distinction is not expressible in PROV without an extension.

**`NEGATIVE_PREMISE`.** A determination that rests on nothing having been found rests on a search, and a search has a scope and a completeness property. Section 3.7 requires both.

**`NON_RESULT_ACCEPTED`.** This is the role that catches the hidden decision. `Part 1` returns non results and `Part 2` returns indeterminate verdicts, and both parts require the caller to be told rather than protected from the fact. What the caller then does is the most under recorded act in any system of this kind: it proceeds, on a default, a fallback, a cached value or an assumption that nobody wrote down. Recording it as a role makes the proceeding visible and makes it countable, and section 8.5 requires the count.

**`ALTERNATIVE_REJECTED`.** Without it a reader sees the chosen outcome and cannot tell that a choice was made. A determination that selected among three candidates and recorded only the winner is indistinguishable from a determination that computed one answer, and the two have entirely different review requirements.

**P3-3.28 (MUST) Closed role set.** An implementation must record exactly one role from the table above on every citation and must not accept a role outside the set.

**P3-3.29 (MUST NOT) No role extension.** An implementation must not add a role, and must express any additional distinction as a registered `cited_kind` or as an attribute of the citation.

**P3-3.30 (MUST) Reliance constraints enforced.** An implementation must enforce the reliance column of the table above, and must refuse a citation whose reliance value contradicts it.

**P3-3.31 (MUST) Context recorded where supplied.** An implementation must record as `CONTEXT` anything the owning component supplied as available and not relied upon, and must not discard it.

**P3-3.32 (MUST NOT) No context as input.** An implementation must not record a `CONTEXT` citation as an `INPUT`, a `PREMISE` or a `DERIVED_INTERMEDIATE`.

**P3-3.33 (MUST) Authority present on every determination.** An implementation must refuse a determination record carrying no `AUTHORITY` citation, and must require a declared frontier where no authority can be identified, per section 3.11.

**P3-3.34 (MUST) Method present on every determination.** An implementation must refuse a determination record carrying no `METHOD` citation.

**P3-3.35 (MUST) Selection criterion required where alternatives exist.** An implementation must refuse a determination record carrying an `ALTERNATIVE_REJECTED` citation and no `SELECTION_CRITERION` citation.

**P3-3.36 (MUST) Delegation present where the actor is not the accountable party.** An implementation must refuse a determination record whose acting actor is not itself the accountable party and which carries no `DELEGATION` citation.

### 3.7 Negative citations

An absence is the hardest thing to record honestly, because the record of a search that found nothing looks identical whether the search was thorough or was never run.

`negative_citation` fields:

| Field | Type | Required | Cardinality | Absence means |
| --- | --- | --- | --- | --- |
| `negative_citation_id` | `ID` | yes | 1 | n/a |
| `determination_id` | `ID` | yes | 1 | n/a |
| `asserted_absence` | `TEXT` | yes | 1 | n/a. What was found not to exist. |
| `search_scope` | `SCOPE` | yes | 1 | n/a. The declared extent searched. |
| `scope_authority` | `URN` | yes | 1 | n/a. The component whose data defines the scope. |
| `searched_as_of_atime` | `ATIME` | yes | 1 | n/a |
| `searched_ktime` | `KTIME` | yes | 1 | n/a |
| `completeness` | `ENUM` | yes | 1 | n/a. One of `COMPLETE_OVER_SCOPE`, `PARTIAL_TRUNCATED`, `PARTIAL_WITHHELD`, `PARTIAL_UNAVAILABLE`, `COMPLETENESS_UNKNOWN`. |
| `result_count` | `COUNT` | yes | 1 | n/a. Zero for a true absence. A non zero value with a negative citation is a defect. |
| `query_pin` | `PIN` | no | 0..1 | The search expression was not recorded. Reduces reconstructability materially and is reportable. |
| `withheld_count` | `COUNT` | no | 0..1 | Nothing was withheld, or withholding was not reported to the searcher. |

The `completeness` enumeration is the whole point. `COMPLETE_OVER_SCOPE` asserts that everything in the declared scope was examined. `PARTIAL_WITHHELD` asserts that some of the scope was not visible to the searcher, which means the absence is not established: something may exist that the search was not permitted to see, and a determination resting on that absence rests on an access decision rather than on a fact. `COMPLETENESS_UNKNOWN` is admissible and truthful, and section 8.5 requires the count, because a system whose negative premises are all of unknown completeness has no negative premises.

The distinction between `PARTIAL_WITHHELD` and `COMPLETE_OVER_SCOPE` is the same distinction `Part 1` draws between withheld and absent and `Part 2` draws between `SUBJECT_PATH_WITHHELD` and `SUBJECT_PATH_UNDECLARED`. It appears in all three parts because it is the mechanism by which access control silently manufactures facts.

**P3-3.37 (MUST) Scope declared.** An implementation must record a declared scope and the component whose data defines it for every negative citation, and must refuse one without both.

**P3-3.38 (MUST) Completeness declared.** An implementation must record a completeness value from the enumeration above and must not default it.

**P3-3.39 (MUST) Both instants recorded.** An implementation must record the application time as of which the search was performed and the knowledge time at which it was performed.

**P3-3.40 (MUST) Withheld absence distinguished.** An implementation must record `PARTIAL_WITHHELD` where any part of the scope was not visible to the searcher, and must not record `COMPLETE_OVER_SCOPE` in its place.

**P3-3.41 (MUST NOT) No negative citation with results.** An implementation must refuse a negative citation whose `result_count` is not zero.

**P3-3.42 (SHOULD) Query recorded.** An implementation should record a pin to the search expression used, so that the search can be repeated rather than described.

**P3-3.43 (MUST) Unknown completeness reportable.** An implementation must be able to report every negative citation of completeness `COMPLETENESS_UNKNOWN` or `PARTIAL_WITHHELD`, and must include the counts in the signals of section 8.5.

### 3.8 The method citation

A basis without a method is a list of ingredients. Every input can be present, pinned and obtainable, and a reader still cannot reconstruct the reasoning, because the step from premises to conclusion is missing.

This is the point at which the part diverges most sharply from the audit trail tradition, which records acts and their actors and treats the reasoning as implicit in the code. It aligns instead with W3C PROV-DM, whose Association is a ternary relation between an activity, an agent and a **plan**, so that what the agent was following is part of the record rather than outside it. It also aligns with ISO/IEC 27042, which requires an analysis process to be documented sufficiently that an independent analyst can reproduce it, and with ISO/IEC 27041's concern for the suitability of an investigative method.

`method_citation` fields:

| Field | Type | Required | Cardinality | Absence means |
| --- | --- | --- | --- | --- |
| `method_citation_id` | `ID` | yes | 1 | n/a |
| `determination_id` | `ID` | yes | 1 | n/a |
| `kind` | `ENUM` | yes | 1 | n/a. Registered under section 9.5. |
| `pin` | `PIN` | no | 0..1 | Required for every kind except `HUMAN_JUDGEMENT` and `UNDECLARED`. |
| `deterministic` | `TRUTH` | yes | 1 | n/a |
| `parameters_pin` | `PIN` | no | 0..1 | The method took no parameters, or they were not recorded. Distinguished by `parameters_declared_none`. |
| `parameters_declared_none` | `TRUTH` | yes | 1 | n/a |
| `narrative` | `TEXT` | no | 0..1 | Required where `kind` is `HUMAN_JUDGEMENT`. |
| `asserted_by` | `ACTOR` | yes | 1 | n/a |

The minimum registered method kinds are: `RULE_EVALUATION`, referencing a `Part 2` rule set version; `DECISION`, referencing a `Part 5` decision artifact; `ALGORITHM`, referencing a versioned procedure; `EXPRESSION`, referencing a versioned expression; `MODEL_INFERENCE`, referencing a `Part 13` invocation record; `PROCEDURE`, referencing a `Part 1` document version describing what a person was to do; `HUMAN_JUDGEMENT`, where a person reached a conclusion by means not reducible to a procedure; and `UNDECLARED`.

`HUMAN_JUDGEMENT` is admissible and is a frontier. A determination reached by a person exercising judgement is legitimate, common, and not reconstructable beyond the point at which the person's reasoning becomes unrecorded. What the model requires is that it be declared as such, with a narrative and a named actor, rather than dressed as a procedure. A determination recorded as `PROCEDURE` that was in fact judgement is a false record, and it is false in the specific way that makes an investigation reach a wrong conclusion about whether a process was followed.

`UNDECLARED` is admissible for the same reason `Part 2` admits an undeclared rule authority: the alternative to permitting the honest answer is a system in which every method claims to be something it is not. Section 8.5 requires the count.

**P3-3.44 (MUST) Method kind registered.** An implementation must record a registered method kind for every determination and must not default it.

**P3-3.45 (MUST) Method pinned where pinnable.** An implementation must record a pin for every method kind other than `HUMAN_JUDGEMENT` and `UNDECLARED`, and must refuse a determination record lacking one.

**P3-3.46 (MUST) Determinism declared.** An implementation must record whether the method is deterministic and must not default the value.

**P3-3.47 (MUST) Parameters recorded or their absence declared.** An implementation must record a pin to the method's parameters or an explicit declaration that it took none, and must not leave the two indistinguishable.

**P3-3.48 (MUST) Judgement declared as judgement.** An implementation must record `HUMAN_JUDGEMENT` with a narrative and a named actor wherever the conclusion was not produced by a pinnable method, and must not record another kind in its place.

**P3-3.49 (MUST) Judgement is a frontier.** An implementation must record a frontier of kind `HUMAN_JUDGEMENT` for every determination whose method is of that kind, per section 3.11.

**P3-3.50 (MUST) Undeclared method reportable.** An implementation must be able to report every determination whose method kind is `UNDECLARED` and must include the count in the signals of section 8.5.

**P3-3.51 (MUST NOT) No method inference.** An implementation must not infer a method kind from the class of the determination, the owning component or the citations present.

### 3.9 Non result acceptance

`Part 1` returns non results. `Part 2` returns indeterminate verdicts with five subclasses. Both parts require the caller to receive them unmodified, and neither specifies what the caller does next, because that is a composition question. This section is where the answer is recorded.

`non_result_acceptance` fields:

| Field | Type | Required | Cardinality | Absence means |
| --- | --- | --- | --- | --- |
| `acceptance_id` | `ID` | yes | 1 | n/a |
| `determination_id` | `ID` | yes | 1 | n/a |
| `non_result_pin` | `PIN` | yes | 1 | n/a. The non result envelope as returned. |
| `source_component` | `URN` | yes | 1 | n/a |
| `non_result_class` | `ENUM` | yes | 1 | n/a. As returned by the source, recorded unaltered. |
| `disposition` | `ENUM` | yes | 1 | n/a. One of `PROCEEDED_ON_DECLARED_DEFAULT`, `PROCEEDED_ON_PRIOR_VALUE`, `PROCEEDED_TREATING_AS_ABSENT`, `PROCEEDED_ON_HUMAN_OVERRIDE`, `PROCEEDED_WITHOUT_BASIS`, `DEFERRED`, `ABANDONED`. |
| `default_pin` | `PIN` | no | 0..1 | Required where `disposition` is `PROCEEDED_ON_DECLARED_DEFAULT`. |
| `prior_value_pin` | `PIN` | no | 0..1 | Required where `disposition` is `PROCEEDED_ON_PRIOR_VALUE`. |
| `override_actor` | `ACTOR` | no | 0..1 | Required where `disposition` is `PROCEEDED_ON_HUMAN_OVERRIDE`. |
| `override_authority` | `AUTHREF` | no | 0..1 | Required where `disposition` is `PROCEEDED_ON_HUMAN_OVERRIDE`. |
| `rationale` | `TEXT` | yes | 1 | n/a |

`PROCEEDED_WITHOUT_BASIS` is the member that matters. It records that a determination went ahead despite an input it could not obtain, with no declared default, no prior value, no override and no stated ground beyond the rationale text. It is admissible because it happens constantly and the alternative to recording it is not preventing it. It is separately countable because a system in which it is common is a system whose determinations do not rest on what they claim to rest on, and no other signal reveals that.

`PROCEEDED_TREATING_AS_ABSENT` is separated from the others because it is the specific mechanism by which the withheld against absent distinction, maintained carefully by `Part 1` and `Part 2`, is destroyed at the point of consumption. A caller that receives a withheld input and treats it as absent has undone the work of two components, and the record makes it visible.

**P3-3.52 (MUST) Non result acceptance recorded.** An implementation must record a `non_result_acceptance` for every non result or indeterminate outcome a determination received and did not treat as terminating.

**P3-3.53 (MUST) Non result envelope pinned unaltered.** An implementation must pin the non result as it was returned by its source and must not record a reclassified or simplified form.

**P3-3.54 (MUST) Disposition declared.** An implementation must record a disposition from the enumeration above and must not default it.

**P3-3.55 (MUST) Supporting pin where the disposition requires one.** An implementation must record the default, prior value, or override actor and authority required by the disposition recorded, and must refuse an acceptance lacking it.

**P3-3.56 (MUST) Rationale recorded.** An implementation must record a rationale for every non result acceptance.

**P3-3.57 (MUST) Proceeding without basis countable.** An implementation must be able to report every acceptance of disposition `PROCEEDED_WITHOUT_BASIS` and `PROCEEDED_TREATING_AS_ABSENT`, and must include both counts in the signals of section 8.5.

**P3-3.58 (MUST) Acceptance appears in the basis.** An implementation must record a citation of role `NON_RESULT_ACCEPTED` for every non result acceptance, so that the acceptance is reachable from the determination's basis and not only from a side table.

### 3.10 Alternatives and selection

`alternative_considered` fields:

| Field | Type | Required | Cardinality | Absence means |
| --- | --- | --- | --- | --- |
| `alternative_id` | `ID` | yes | 1 | n/a |
| `determination_id` | `ID` | yes | 1 | n/a |
| `candidate_reference` | `URN` | yes | 1 | n/a |
| `candidate_digest` | `DIGEST` | no | 0..1 | The candidate was not digestible. |
| `eliminated_by` | `ENUM` | yes | 1 | n/a. One of `CRITERION`, `CONSTRAINT_VIOLATION`, `INELIGIBILITY`, `WITHDRAWN_BY_PROPOSER`, `NOT_EVALUABLE`, `UNRECORDED`. |
| `eliminating_citation_id` | `ID` | no | 0..1 | Required where `eliminated_by` is `CRITERION` or `CONSTRAINT_VIOLATION`. |
| `candidate_ordinal` | `SEQ` | yes | 1 | n/a |

`NOT_EVALUABLE` records a candidate eliminated because it could not be assessed rather than because it was worse. This is a materially different fact and one that a selection record ordinarily hides: an option was discarded for want of information, and someone may wish to know that the option was never really considered.

`UNRECORDED` is admissible and countable, on the same basis as the other honest admissions in this part.

**P3-3.59 (MUST) Alternatives recorded where a selection occurred.** An implementation must record every candidate outcome the owning component reports as having been available and not selected.

**P3-3.60 (MUST) Elimination ground recorded.** An implementation must record a ground of elimination for every alternative and must not default it.

**P3-3.61 (MUST) Eliminating citation linked.** An implementation must link the citation that eliminated a candidate wherever the ground is `CRITERION` or `CONSTRAINT_VIOLATION`.

**P3-3.62 (MUST) Not evaluable distinguished.** An implementation must record `NOT_EVALUABLE` where a candidate was discarded for want of information and must not record `CRITERION` in its place.

**P3-3.63 (MUST NOT) No winner only selection record.** An implementation must refuse a determination record whose owning component reports that a selection occurred and which supplies no alternatives.

**P3-3.64 (MUST) Alternatives appear in the basis.** An implementation must record a citation of role `ALTERNATIVE_REJECTED` for every alternative considered.
### 3.11 Frontiers

A chain of reasoning does not terminate on its own. Followed far enough, every determination rests on a statute, a physical measurement, a keystroke or somebody's word. The chain must stop, and the only question is whether it stops at a declared point or trails off.

An undeclared terminus and a missing citation are indistinguishable in the record and require opposite responses. The first is correct and complete; the second is a defect. Making the distinction is the purpose of this section, and no provenance standard reviewed for this part provides it.

`frontier` fields:

| Field | Type | Required | Cardinality | Absence means |
| --- | --- | --- | --- | --- |
| `frontier_id` | `ID` | yes | 1 | n/a |
| `at_citation_id` | `ID` | no | 0..1 | The frontier is at the determination itself rather than at a cited artifact. |
| `determination_id` | `ID` | yes | 1 | n/a |
| `kind` | `ENUM` | yes | 1 | n/a. Registered under section 9.3, with the minimum set below. |
| `declared_by` | `ACTOR` | yes | 1 | n/a |
| `declared_ktime` | `KTIME` | yes | 1 | n/a |
| `justification` | `TEXT` | yes | 1 | n/a |
| `external_reference` | `URN` | no | 0..1 | Required where `kind` is `EXTERNAL_AUTHORITY`. |
| `expected_to_close` | `TRUTH` | yes | 1 | n/a. Whether the frontier is expected to be closable in future. |

The minimum frontier kinds. The set is normative as a minimum and is open under section 9.3.

| Kind | Means | Legitimate |
| --- | --- | --- |
| `EXTERNAL_AUTHORITY` | The chain reaches something outside the organisation's control: a statute, a regulation, a standard, a counterparty's contract. | Yes, permanently. |
| `AXIOM` | A proposition accepted without justification by declared policy. | Yes, and it should be rare enough to enumerate. |
| `ATTESTED` | A named actor asserts the fact and nothing further is recorded, per section 3.12. | Yes, and the attestation is the record. |
| `HUMAN_JUDGEMENT` | The step was a person's judgement, not reducible further, per section 3.8. | Yes. |
| `PHYSICAL_OBSERVATION` | The chain reaches a measurement, a sample, an instrument reading or a physical inspection. | Yes, and the instrument and its calibration should be cited where available. |
| `OPAQUE_COMPONENT` | A component supplied a value and does not expose its own basis. | Yes as a statement of fact, and it is a defect in the estate rather than in this record. |
| `PRIOR_TO_ADOPTION` | The chain reaches a period before this component was recording. | Yes, and it should have a declared end date. |
| `RETENTION_EXPIRED` | The chain reaches something lawfully disposed of under a retention rule. | Yes, and the disposition authorisation should be cited. |
| `ACCESS_WITHHELD` | The reader is not permitted to traverse further. | Yes as a statement to that reader, and it is not a property of the chain. |
| `FRONTIER_UNDECLARED` | The chain stops and no reason is recorded. | No. This is the defect the section exists to name. |

`ACCESS_WITHHELD` is a frontier of the reading rather than of the chain, and the distinction must be preserved: the same chain reconstructed by a differently authorised reader closes differently. Clause P3-3.71 requires that a withheld frontier be recorded against the reconstruction run rather than against the determination, because recording it against the determination would make an access decision look like a property of the reasoning.

`OPAQUE_COMPONENT` is the honest name for the most common real situation: a value arrives from a system that has no provenance to give. Declaring it is worth doing because the count of opaque frontiers is the measure of how far the estate is from being accountable, and it is the only measure available.

**P3-3.65 (MUST) Every terminus is a declared frontier.** An implementation must record a frontier at every point at which a chain terminates, and must record `FRONTIER_UNDECLARED` where no reason was supplied rather than recording nothing.

**P3-3.66 (MUST) Justification recorded.** An implementation must record a justification for every frontier of a kind other than `FRONTIER_UNDECLARED`.

**P3-3.67 (MUST) External reference where external.** An implementation must record an external reference for every frontier of kind `EXTERNAL_AUTHORITY`.

**P3-3.68 (MUST) Undeclared frontier is a defect.** An implementation must treat a frontier of kind `FRONTIER_UNDECLARED` as a reconstruction defect, must report it as such in the closure outcome of section 7.2, and must include the count in the signals of section 8.5.

**P3-3.69 (MUST) Adoption boundary declared.** An implementation must declare the instant before which it holds no records, and must record frontiers of kind `PRIOR_TO_ADOPTION` against chains reaching it rather than reporting a missing citation.

**P3-3.70 (MUST) Disposition cited at a retention frontier.** An implementation must cite the disposition authorisation at every frontier of kind `RETENTION_EXPIRED` where one is obtainable, per `Part 1` section 12.1.

**P3-3.71 (MUST) Access frontiers belong to the reading.** An implementation must record a frontier of kind `ACCESS_WITHHELD` against the reconstruction run and the principal, and must not record it against the determination.

**P3-3.72 (MUST NOT) No frontier as closure.** An implementation must not report a chain terminating at a frontier as fully closed, and must report the outcome `RECONSTRUCTED_TO_FRONTIER` of section 7.2 with the frontier kinds enumerated.

**P3-3.73 (MUST) Expected closability recorded.** An implementation must record whether each frontier is expected to be closable, so that a permanent boundary is distinguishable from a gap awaiting work.

### 3.12 Attribution and delegation

Every determination has an actor and an accountable party, and in an estate with automated agents they are frequently not the same.

`attribution` fields:

| Field | Type | Required | Cardinality | Absence means |
| --- | --- | --- | --- | --- |
| `attribution_id` | `ID` | yes | 1 | n/a |
| `determination_id` | `ID` | yes | 1 | n/a |
| `acting_actor` | `ACTOR` | yes | 1 | n/a |
| `acting_actor_kind` | `ENUM` | yes | 1 | n/a. One of `NATURAL_PERSON`, `ORGANISATION`, `AUTOMATED_AGENT`, `SYSTEM_PROCESS`. |
| `accountable_party` | `ACTOR` | yes | 1 | n/a |
| `accountable_party_kind` | `ENUM` | yes | 1 | n/a. `NATURAL_PERSON` or `ORGANISATION` only. |
| `delegation_depth` | `COUNT` | yes | 1 | n/a. Zero where the actor is the accountable party. |
| `invocation_reference` | `URN` | no | 0..1 | The actor was not an automated agent, or `Part 13` held no invocation record. |

`delegation_step` fields:

| Field | Type | Required | Cardinality | Absence means |
| --- | --- | --- | --- | --- |
| `step_id` | `ID` | yes | 1 | n/a |
| `attribution_id` | `ID` | yes | 1 | n/a |
| `step_ordinal` | `SEQ` | yes | 1 | n/a. One is the acting actor's immediate principal. |
| `from_actor` | `ACTOR` | yes | 1 | n/a |
| `to_actor` | `ACTOR` | yes | 1 | n/a |
| `delegation_instrument` | `PIN` | no | 0..1 | The delegation is asserted without a resolvable instrument. Reportable. |
| `instrument_absent_reason` | `ENUM` | no | 0..1 | Required where `delegation_instrument` is absent. |

The delegation chain must terminate in a natural person or an organisation. A chain terminating in an automated agent is refused, on the same ground `Part 1` gives for refusing an agent signature and `Part 2` gives for refusing an agent correspondence claim: accountability is a relation to a party that can bear it, and a record whose accountability terminates in software records that nobody is answerable.

This is a position rather than a finding. W3C PROV-DM's `actedOnBehalfOf` supplies the relation and imposes no such constraint, and nothing in the reviewed standards requires the terminus to be a person or an organisation. Section 13.6 records the position and the argument against it.

The delegation instrument is the artifact conferring the authority: a delegation of authority document, a role assignment, a power of attorney, a contractual term. It is separated from the delegation assertion because the two differ in strength, and a delegation asserted without an instrument is a claim rather than a demonstrable fact. Section 8.5 requires the count.

**P3-3.74 (MUST) Actor and accountable party both recorded.** An implementation must record both for every determination, must record the kind of each, and must not omit either where they coincide.

**P3-3.75 (MUST) Accountable party is a person or an organisation.** An implementation must refuse an attribution whose accountable party is of kind `AUTOMATED_AGENT` or `SYSTEM_PROCESS`.

**P3-3.76 (MUST) Delegation chain complete.** An implementation must record a delegation step for every link between the acting actor and the accountable party, and must record a depth consistent with the steps held.

**P3-3.77 (MUST) Agent attribution recorded as such.** An implementation must record an automated agent as the acting actor where it performed the determination, must not attribute the act to the person who requested it, and must record the `Part 13` invocation reference where one exists.

**P3-3.78 (MUST) Instrument recorded or its absence reasoned.** An implementation must record a pin to the delegation instrument for every step, or a reason it is absent, and must be able to report every step lacking one.

**P3-3.79 (MUST NOT) No inferred delegation.** An implementation must not infer a delegation step from a role, an organisational hierarchy or an access grant, and must record every step as asserted by an identified party.

**P3-3.80 (MUST) Attestation recorded where relied upon.** An implementation must record an attestation entry, with its signer and its signature, for every frontier of kind `ATTESTED`.

### 3.13 The chain, and the conditions of reconstructability

Reconstructability is a property with a definition, and the definition is testable. A chain rooted at a determination is **reconstructable** if and only if all five conditions hold.

**One, resolution.** Every citation in the chain resolves: the cited artifact is identified, its version is recorded, and the artifact is obtainable at that version, or the point at which it is not obtainable is a declared frontier.

**Two, role completeness.** Every citation carries a role from the closed set, and the mandatory roles are present: an authority and a method on every determination, a selection criterion wherever an alternative is recorded, a delegation wherever the actor is not the accountable party.

**Three, closure to frontiers.** Every terminus of the chain is a declared frontier of a kind other than `FRONTIER_UNDECLARED`.

**Four, method presence.** The method by which the basis produced the conclusion is recorded and, where pinnable, obtainable.

**Five, independence.** The chain can be assembled and read using only the records of this component and the artifacts its pins identify, without the participation of any component that produced the determination.

The fifth is the one that most implementations fail, and it fails quietly. A ledger that stores references which only the originating component can dereference has recorded a chain that is reconstructable exactly as long as that component exists, which is not the period over which the question will be asked. Clause P3-3.85 states the requirement and section 8.6 makes it testable through the evidence package.

The five conditions map onto the four principles ISO/IEC 27037 states for digital evidence handling, and the mapping is worth stating because the divergence is instructive. That standard's **auditability** corresponds to conditions one and two. Its **repeatability**, being the same result under the same conditions, corresponds to the reproduction requirement of `Part 2` rather than to anything here. Its **reproducibility**, being the same result under different conditions by a different party, corresponds to condition five. Its **justifiability**, being the demonstrable appropriateness of the method chosen, corresponds to condition four and is the principle this part strengthens most, since a recorded method pin is a stronger artifact than a documented rationale.

`reconstruction_run` and `reconstruction_outcome` record the assembly and its result; their fields are given in section 7.

**P3-3.81 (MUST) Five conditions assessed.** An implementation must assess all five conditions above for every reconstruction run and must report the result of each separately.

**P3-3.82 (MUST) Chain assembled without the producer.** An implementation must be able to assemble any chain within its retained history without invoking the component that produced the determination.

**P3-3.83 (MUST) Cycle detection.** An implementation must detect a cycle in a chain, must report it as a defect, and must not traverse indefinitely.

**P3-3.84 (MUST) Depth and breadth bounds declared.** An implementation must declare the maximum depth and breadth to which it will traverse a chain and must report a traversal truncated by either as truncated rather than as closed.

**P3-3.85 (MUST) Pins dereferenceable independently.** An implementation must record pins that identify artifacts in terms the owning component's successor could resolve, and must not record a reference resolvable only through a running instance of the producing component.

**P3-3.86 (MUST NOT) No partial chain as complete.** An implementation must not report a chain as reconstructable where any of the five conditions failed, and must report the enumerated outcome of section 7.2.

### 3.14 Soundness assessment and basis defect

A determination is a true record of what was concluded, and it stays true. What changes is what we now believe about the things it rested on.

`Part 1` retracts an effectivity assertion and records a divergence between belief then and belief now. `Part 2` observes that a rule's authority has been superseded and records a drift observation. Both leave a question neither can answer: which determinations rested on the thing that turned out to be wrong. This section answers it, and it is the strongest argument for the component's existence.

`basis_defect` fields:

| Field | Type | Required | Cardinality | Absence means |
| --- | --- | --- | --- | --- |
| `defect_id` | `ID` | yes | 1 | n/a |
| `defective_pin` | `PIN` | yes | 1 | n/a. The artifact and version now believed defective. |
| `kind` | `ENUM` | yes | 1 | n/a. One of `RETRACTED`, `SUPERSEDED_WITH_CORRECTION`, `WITHDRAWN`, `INTEGRITY_FAILED`, `MISRESOLVED`, `RULE_DEFECTIVE`, `MODEL_DEFECTIVE`, `SOURCE_DATA_CORRECTED`, `AUTHORITY_LAPSED`. |
| `reported_by_component` | `URN` | yes | 1 | n/a |
| `reported_ktime` | `KTIME` | yes | 1 | n/a |
| `effective_from_atime` | `ATIME` | no | 0..1 | The defect is not bounded in application time and affects every reliance on the artifact. |
| `detail` | `TEXT` | yes | 1 | n/a |
| `originating_observation` | `PIN` | no | 0..1 | No originating observation was supplied. |

`defect_impact` fields:

| Field | Type | Required | Cardinality | Absence means |
| --- | --- | --- | --- | --- |
| `impact_id` | `ID` | yes | 1 | n/a |
| `defect_id` | `ID` | yes | 1 | n/a |
| `determination_id` | `ID` | yes | 1 | n/a |
| `citation_id` | `ID` | yes | 1 | n/a. The specific reliance affected. |
| `reliance_at_time` | `TRUTH` | yes | 1 | n/a. Copied from the citation, not re derived. |
| `assessed_ktime` | `KTIME` | yes | 1 | n/a |
| `assessment` | `ENUM` | yes | 1 | n/a. One of `UNSOUND`, `UNSOUND_IMMATERIAL`, `SOUND_DESPITE_DEFECT`, `MATERIALITY_UNASSESSED`. |
| `assessed_by` | `ACTOR` | no | 0..1 | The assessment is `MATERIALITY_UNASSESSED`. |

`MISRESOLVED` deserves note. It records that the artifact was not defective but that the determination cited the wrong version of it, which is a different failure with a different remedy and which `Part 1`'s divergence flag exposes directly.

`MATERIALITY_UNASSESSED` is the default and is honest. This component can enumerate every determination that relied on a defective artifact. It cannot say whether the defect changed the answer, because that would require re deriving the conclusion, which clause P3-1.5 forbids and which would in any case be a new determination rather than an assessment of the old one. Whether the defect mattered is a judgement for the owning component or a person, recorded here as their assessment.

`SOUND_DESPITE_DEFECT` records the case where someone examined the impact and concluded the determination stands. It is a positive act with a named assessor, not a silence.

**P3-3.87 (MUST) Defect accepted from the owning component.** An implementation must accept a basis defect report from the component that owns the defective artifact and must record it without alteration.

**P3-3.88 (MUST) Impact enumerated exhaustively.** An implementation must enumerate every determination and every citation that relied upon a defective artifact at a version and within an application time range the defect covers.

**P3-3.89 (MUST) Reliance value carried forward.** An implementation must copy the reliance value recorded on the affected citation into the impact record and must not re derive it.

**P3-3.90 (MUST) Materiality unassessed by default.** An implementation must record `MATERIALITY_UNASSESSED` on creating an impact record and must not assess materiality itself.

**P3-3.91 (MUST) Assessment attributed.** An implementation must record a named assessor for every impact record whose assessment is not `MATERIALITY_UNASSESSED`.

**P3-3.92 (MUST NOT) No determination amendment on defect.** An implementation must not alter, annotate in place, or withdraw a determination because a basis defect was found, and must record the defect and its impact as further entries.

**P3-3.93 (MUST) Unsound determinations reportable.** An implementation must be able to report every determination with an open impact record, by defect and by assessment, and must include the counts in the signals of section 8.5.

**P3-3.94 (MUST) Defect propagates through prior determinations.** An implementation must include, in the impact enumeration, every determination that relied upon an affected determination through a citation of role `PRIOR_DETERMINATION`, transitively, to a declared depth.

**P3-3.95 (MUST) Transitive depth declared.** An implementation must declare the depth to which it propagates a defect through prior determination citations and must report a propagation truncated by it.
### 3.15 The audit trail

The audit trail answers a different question from the basis, and it is the question most people mean when they say audit log: what happened to this thing, in what order, and who did each of it.

`trail_stream` fields:

| Field | Type | Required | Cardinality | Absence means |
| --- | --- | --- | --- | --- |
| `stream_id` | `ID` | yes | 1 | n/a |
| `subject_reference` | `URN` | yes | 1 | n/a |
| `opened_ktime` | `KTIME` | yes | 1 | n/a |
| `closed_ktime` | `KTIME` | no | 0..1 | The stream remains open. Never means the subject is still in use. |

`subject_act` fields:

| Field | Type | Required | Cardinality | Absence means |
| --- | --- | --- | --- | --- |
| `act_id` | `ID` | yes | 1 | n/a |
| `stream_id` | `ID` | yes | 1 | n/a |
| `stream_sequence` | `SEQ` | yes | 1 | n/a. Contiguous within the stream; a gap is a defect. |
| `act_kind` | `ENUM` | yes | 1 | n/a. Registered. |
| `acting_actor` | `ACTOR` | yes | 1 | n/a |
| `occurred_otime` | `OTIME` | yes | 1 | n/a |
| `recorded_ktime` | `KTIME` | yes | 1 | n/a |
| `determination_id` | `ID` | no | 0..1 | The act was not a determination. Presence links the trail to the basis. |
| `before_digest` | `DIGEST` | no | 0..1 | The act did not change the subject's state, or the prior state was not digestible. |
| `after_digest` | `DIGEST` | no | 0..1 | As above. |
| `authorisation` | `AUTHREF` | no | 0..1 | The act was not the subject of an authorisation decision. |

Two properties of the trail differ from the basis and drive its clauses.

**Order is normative.** The trail's value is that it is ordered, so a gap in the sequence is a defect rather than a curiosity, and the ordering must be a property of the record rather than of a timestamp. Timestamps from distributed sources do not totally order, and a trail ordered by timestamp will silently reorder itself when clocks disagree. Section 6.2 requires the sequence to carry the order.

**Not every act is a determination.** Most are not. A subject is created, read, corrected, classified, transferred and disposed of, and only some of those had reasons anyone will ask about. The `determination_id` field links the two structures where an act was a determination, and its absence is a positive statement that no basis was recorded, which is different from a basis having been lost.

**P3-3.96 (MUST) Sequence carries order.** An implementation must order every trail by a sequence assigned by itself and must not order a trail by any timestamp.

**P3-3.97 (MUST) Contiguity required and gaps reported.** An implementation must assign contiguous sequence values within a stream, must detect any gap, and must record a `gap_observation` per section 3.17.

**P3-3.98 (MUST) Determination linkage where present.** An implementation must record the determination identity on every act that was a determination and must not record one on an act that was not.

**P3-3.99 (MUST) State digests where the state changed.** An implementation must record before and after digests for every act that changed the subject's state, or record why it could not.

**P3-3.100 (MUST NOT) No trail as basis.** An implementation must not present a trail as the basis of a determination, and must not construct a basis by selecting acts from a trail.

**P3-3.101 (MUST) Reads recorded in the trail where the subject is sensitive.** An implementation must record a read as an act in the trail wherever the subject's owning component declares that reads are to be trailed, and must declare which subjects those are.

### 3.16 Instance lineage

`value_node` fields:

| Field | Type | Required | Cardinality | Absence means |
| --- | --- | --- | --- | --- |
| `node_id` | `ID` | yes | 1 | n/a |
| `value_reference` | `URN` | yes | 1 | n/a. The addressed position, not the value. |
| `value_digest` | `DIGEST` | yes | 1 | n/a |
| `observed_ktime` | `KTIME` | yes | 1 | n/a |
| `run_reference` | `URN` | no | 0..1 | The value was not produced by a recorded run. |
| `is_source` | `TRUTH` | yes | 1 | n/a. A source node is a lineage frontier. |

`transformation` fields:

| Field | Type | Required | Cardinality | Absence means |
| --- | --- | --- | --- | --- |
| `transformation_id` | `ID` | yes | 1 | n/a |
| `output_node_id` | `ID` | yes | 1 | n/a |
| `input_node_id` | `ID` | yes | 1..n | n/a |
| `method_pin` | `PIN` | no | 0..1 | The transformation's method was not recorded. Reportable and materially weakening. |
| `design_lineage_pin` | `PIN` | no | 0..1 | No `Part 4` design level lineage assertion corresponds to this transformation. |
| `applied_ktime` | `KTIME` | yes | 1 | n/a |
| `partial` | `TRUTH` | yes | 1 | n/a. Whether the recorded inputs are the complete set. |

The `design_lineage_pin` field is the join between this structure and `Part 4`. `Part 4` asserts that a field derives from other fields by a declared transformation; that is a statement about the design. This structure records that this value derived from those values on this occasion; that is a statement about history. The two disagree more often than anyone expects, and the disagreement is the most useful thing either structure produces: a value produced by a path the design does not contain is either an undocumented process or a defect, and neither is visible from one structure alone.

The `partial` field exists because lineage is frequently recorded incompletely by instrumentation that sees some inputs and not others. Recording partiality is the difference between an incomplete lineage and a wrong one.

**P3-3.102 (MUST) Values addressed, not copied.** An implementation must record a value by its addressed position and its digest and must not hold the value as its own authoritative copy, except where the owning component requires it and the requirement is recorded.

**P3-3.103 (MUST) Partiality declared.** An implementation must record whether the inputs of a transformation are the complete set and must not default the value.

**P3-3.104 (MUST) Source nodes are frontiers.** An implementation must treat a source node as a lineage frontier and must record a frontier kind for it.

**P3-3.105 (MUST) Design lineage joined where available.** An implementation must record the corresponding `Part 4` lineage assertion where one exists, and must be able to report every transformation for which none does.

**P3-3.106 (MUST NOT) No design lineage authority.** An implementation must not assert, correct or version a design level lineage relation, per section 12.4.

**P3-3.107 (MUST) Divergence from design reportable.** An implementation must be able to report every transformation whose input and output positions are not related by any `Part 4` lineage assertion.

### 3.17 The ledger, its integrity, and the limits of integrity

The ledger is an append only sequence of entries. Its integrity machinery establishes one thing and does not establish another, and confusing the two is the most consequential misunderstanding available about a component of this kind.

**What it establishes.** That an entry recorded at position n has not been altered since, and that no entry has been removed from or inserted into the sequence, to the strength of the digest algorithm and the independence of the anchor.

**What it does not establish.** That anything which should have been recorded was recorded. A determination made and never registered leaves no trace, and no cryptographic construction can reveal the absence of something that was never present. A hash chain over an incomplete record is a perfectly verifiable incomplete record.

This limit is not a weakness of a particular design. It is intrinsic, it is stated in the reviewed literature on transparency logs, and the SCITT architecture of RFC 9943 addresses authenticity and transparency of registered statements without claiming completeness of registration. An individual Internet Draft in the same working group's space, cited here as an observation rather than as a normative source, states the point directly in the context of logged refusals: what such a mechanism provides is auditability of what was logged, not proof that nothing unlogged occurred.

Three mitigations are available and none is a solution. Each is required because the combination is materially better than any one.

**Sequence contiguity.** Within a stream, entries are contiguous, so a removed entry is detectable as a gap even though a never written entry is not.

**Reconciliation.** The emitting component counts what it emitted; this component counts what it recorded; the two are compared on a cycle. This detects loss in transit and detects an emitter that stopped emitting, which is the most common real failure. It does not detect an emitter that never emitted for a class of determination.

**Declared completeness.** The owning component declares whether the basis it supplied was complete, per section 3.4, and declares which classes of determination it registers at all. A false declaration is then a false statement by an identified party, which is a governance fact rather than a technical one, and governance is the only register in which completeness can be addressed.

`ledger_segment`, `commitment`, `anchor_publication`, `receipt` and `gap_observation` fields are summarised below.

| Entity | Required fields |
| --- | --- |
| `ledger_segment` | `segment_id`, `stream`, `from_sequence`, `to_sequence`, `sealed_ktime`, `entry_count` |
| `commitment` | `commitment_id`, `segment_id`, `procedure_pin`, `digest`, `prior_commitment_digest`, `computed_ktime` |
| `anchor_publication` | `publication_id`, `commitment_id`, `external_store`, `external_reference`, `published_ktime`, `verification_procedure_pin` |
| `receipt` | `receipt_id`, `entry_id`, `commitment_id`, `inclusion_proof`, `issued_ktime` |
| `gap_observation` | `observation_id`, `stream`, `expected_sequence`, `observed_ktime`, `resolution` |
| `reconciliation` | `reconciliation_id`, `emitting_component`, `period`, `emitted_count`, `recorded_count`, `discrepancy`, `performed_ktime` |

**P3-3.108 (MUST) Append only sequence.** An implementation must assign a contiguous sequence to every entry within a declared stream and must never reuse or reassign a sequence value.

**P3-3.109 (MUST) Segments sealed and committed.** An implementation must seal segments on a declared boundary, must compute a commitment over each, and must chain each commitment to its predecessor's digest.

**P3-3.110 (MUST) Commitment procedure pinned.** An implementation must pin the procedure by which a commitment is computed, so that a later reader can recompute it, and must not rely on an undocumented construction.

**P3-3.111 (MUST) External anchoring.** An implementation must publish commitments to at least one store it does not control, on a declared cycle, and must record the publication and the procedure by which a reader verifies it.

**P3-3.112 (MUST) Anchor cycle declared.** An implementation must declare its anchoring cycle, and must state that alteration within the interval since the last anchor is detectable only by parties holding an earlier commitment.

**P3-3.113 (MUST) Receipts issued.** An implementation must be able to issue, for any entry, a proof of its inclusion at its recorded position, verifiable against a published anchor.

**P3-3.114 (MUST) Gaps detected and recorded.** An implementation must detect every sequence gap, must record a `gap_observation`, and must not close one other than by recording a resolution.

**P3-3.115 (MUST) Reconciliation performed.** An implementation must reconcile its recorded counts against the emitted counts of every registering component on a declared cycle and must record every discrepancy.

**P3-3.116 (MUST) Completeness limit stated to every reader.** An implementation must state, in every evidence package and in the documentation of every reading interface, that its integrity mechanisms do not establish that every determination was recorded.

**P3-3.117 (MUST NOT) No completeness claim.** An implementation must not assert, imply or permit an interface to imply that the ledger is a complete record of determinations.

**P3-3.118 (MUST) Registering components enumerated.** An implementation must maintain and expose the list of components that register determinations with it and the classes each registers, so that a reader can see what is not covered.

**P3-3.119 (MUST NOT) No deletion for integrity.** An implementation must not remove an entry in order to repair an integrity failure and must record the failure as a further entry.

### 3.18 Projections

Every read is a projection: a pure function of the recorded entries, holding no state of its own, recomputable at any time.

| Projection | Yields |
| --- | --- |
| `basis_of` | Every citation of a determination with its role, pin, reliance and instants. |
| `chain_of` | The transitive closure from a determination, with frontiers, to declared bounds. |
| `closure_outcome_of` | The five condition assessment and the enumerated outcome for a chain. |
| `relied_upon_only` | The chain restricted to citations whose reliance is `TRUE`. |
| `context_only` | The citations whose reliance is `FALSE`, so that a reader can see what was available and unused. |
| `indeterminate_reliance` | Citations whose reliance could not be established. |
| `frontiers_of` | Every frontier in a chain, by kind. |
| `undeclared_frontiers` | Every terminus with no declared reason, by determination and owning component. |
| `negative_premises_of` | Every negative citation with its scope and completeness. |
| `non_results_accepted_by` | Every non result a determination proceeded despite, with its disposition. |
| `alternatives_of` | Every candidate not selected and its elimination ground. |
| `method_of` | The method citation of a determination with its pin and determinism. |
| `attribution_of` | The actor, the delegation chain and the accountable party. |
| `determinations_relying_on` | Every determination that relied upon a stated artifact at a stated version. |
| `impact_of_defect` | Every determination and citation affected by a basis defect, transitively to the declared depth. |
| `unsound_determinations` | Every determination with an open impact record. |
| `trail_of` | The ordered acts concerning a subject. |
| `lineage_of` | The transformation graph reaching a value. |
| `lineage_design_divergence` | Transformations unmatched by any `Part 4` assertion. |
| `integrity_state` | Segments, commitments, anchors, receipts and open gaps. |
| `coverage` | Registering components, classes registered, and reconciliation discrepancies. |

`determinations_relying_on` is the projection the component exists for. Everything else supports it. It is the query an organisation runs on the morning it discovers that a document was wrong, a rule was defective or a feed was corrupted, and no other component in the standard can answer it.

**P3-3.120 (MUST) Projections are pure.** An implementation must compute every projection as a function of recorded entries alone, holding no state not derivable from them.

**P3-3.121 (MUST) Projection recomputable.** An implementation must be able to recompute every projection from the recorded entries and to demonstrate agreement between a served projection and a recomputation.

**P3-3.122 (MUST) Named projections available.** An implementation must provide every projection in the table above and must name each of them as named there in any interface it exposes.

**P3-3.123 (MUST) Reliance filtered projections separate.** An implementation must provide `relied_upon_only` and `context_only` as separate projections and must not merge them.

**P3-3.124 (MUST) Reverse index available.** An implementation must provide `determinations_relying_on` over any artifact identity and version it holds a citation to, and must declare the latency with which a newly recorded citation becomes visible in it.

**P3-3.125 (MUST NOT) No writes through a projection.** An implementation must not permit any state change to be effected by writing to a projection.

### 3.19 Worked demonstration

The demonstration follows one determination across seven years and shows what each read returns. It is not normative. It exists because the field tables do not show whether the model does the work claimed for it.

**2028.** A determination `D1` is recorded. Its class is a disposition authorisation. Its owning component is a records component. Its basis is recorded as follows.

| Citation | Role | Cited | Reliance |
| --- | --- | --- | --- |
| C1 | `AUTHORITY` | Retention policy `POL` version `V4`, clause `7.2`, resolved as of 2028-06-01, outcome envelope recorded | `TRUE` |
| C2 | `CONSTRAINT_OUTCOME` | Evaluation report `ER9` from a rules component, whole report with its pin set | `TRUE` |
| C3 | `PREMISE` | Record `R` closed date, pinned with digest | `TRUE` |
| C4 | `NEGATIVE_PREMISE` | No legal hold in scope `holds/all`, searched as of 2028-06-01, `COMPLETE_OVER_SCOPE`, result count 0, query pinned | `TRUE` |
| C5 | `CONTEXT` | Record `R` classification history, thirty one entries | `FALSE` |
| C6 | `METHOD` | Procedure document `PROC` version `V2` | `TRUE` |
| C7 | `DELEGATION` | Role assignment instrument `DEL7` | `TRUE` |
| C8 | `NON_RESULT_ACCEPTED` | Verdict `INDETERMINATE`, subclass `DEPENDENCY_INDETERMINACY`, code `REFERENCE_SET_UNAVAILABLE`; disposition `PROCEEDED_ON_DECLARED_DEFAULT`, default pinned | `TRUE` |

The attribution records an automated agent as the acting actor, one delegation step to a named person, and that person as the accountable party. One frontier is recorded at C1, kind `EXTERNAL_AUTHORITY`, external reference to a statutory retention period, expected to close false.

**2029.** A reconstruction is run for routine assurance. All five conditions hold. The outcome is `RECONSTRUCTED_TO_FRONTIER` with one frontier of kind `EXTERNAL_AUTHORITY`. Note what this outcome is not: it is not `RECONSTRUCTED_COMPLETE`, because the chain stopped, and the distinction is recorded rather than rounded.

**2031.** The records component retracts the effectivity assertion under which `POL` `V4` was in force on 2028-06-01, having found an approval defect. It reports a basis defect of kind `RETRACTED` against `POL` `V4` over an application time range covering 2028.

The ledger enumerates impact. `determinations_relying_on` over `POL` `V4` returns `D1` and four thousand and six others. An impact record is created for each, carrying the reliance value from the affected citation and an assessment of `MATERIALITY_UNASSESSED`. Nothing about `D1` is altered.

| row | relation | detail |
| --- | --- | --- |
| BD1 | basis_defect | `RETRACTED`, `POL` `V4`, reported 2031-04-02 by the records component |
| IM1 | defect_impact | BD1, `D1`, citation C1, reliance `TRUE`, `MATERIALITY_UNASSESSED` |

**2032.** A person assesses IM1 and concludes that the successor policy version imposed the same period, so the disposition would have been authorised either way. The assessment is recorded as `SOUND_DESPITE_DEFECT` with the assessor named. `D1` still stands and now carries a closed impact record rather than an open one.

**2034.** The procedure document `PROC` `V2` is disposed of under its own retention rule. A reconstruction of `D1` now returns `RECONSTRUCTED_TO_FRONTIER` with two frontiers: the original external authority, and a new frontier of kind `RETENTION_EXPIRED` at C6, citing the disposition authorisation. The chain is still closed and it is closed less far than it was.

**2035.** An investigation asks the following.

| Question | Projection | Result |
| --- | --- | --- |
| What did `D1` rest on? | `basis_of` | Eight citations with roles, pins, reliance and instants |
| What did it actually depend on? | `relied_upon_only` | Seven. C5 was available and unused, and the record says so. |
| Was anything not obtainable? | `closure_outcome_of` | `PROC` `V2` no longer obtainable, at a declared `RETENTION_EXPIRED` frontier, not a gap |
| Did it proceed despite anything? | `non_results_accepted_by` | Yes, C8, on a pinned declared default, with rationale |
| Was the absence of a hold established? | `negative_premises_of` | Yes, scope declared, `COMPLETE_OVER_SCOPE`, query pinned and repeatable |
| Who is answerable? | `attribution_of` | Agent acted, one delegation step, named person accountable |
| Was it ever unsound? | `impact_of_defect` | Yes, from 2031-04-02, assessed 2032 as sound despite the defect, assessor named |
| How many other determinations were exposed? | `determinations_relying_on` | Four thousand and seven, with per determination assessments |
| Has the record been altered? | `integrity_state` | Segments sealed, commitments chained, anchors published, receipt for `D1` verifiable |
| Is this every determination of that class? | `coverage` | Registering components and classes listed; the completeness limit stated |

The last two rows are the honest pair. The ledger can prove that what it holds was not altered. It cannot prove that it holds everything, and it says so in the same breath rather than letting the first claim be read as the second.

**P3-3.126 (MUST) Demonstration satisfiable.** An implementation must be able to answer every question in the table above for any determination within its retained history, using only the projections of section 3.18.
## 4. Interfaces

### 4.1 Interface principles

Operations are specified by their obligations rather than their signatures. No transport, encoding or naming convention is specified.

Operations divide into three groups and the division is enforced. Registering operations append entries and never traverse. Traversing operations assemble chains and never append except for the access record and the reconstruction run. Reading operations append nothing except the access record.

One principle governs the whole section and it is unusual. **This component refuses more than it accepts.** A ledger that accepts whatever it is given will hold an unusable record, because the omissions it tolerates are precisely the ones that make a chain unreconstructable, and they cannot be repaired later: the information was available only at the moment of registration. Every refusal in section 4.2 is therefore a refusal at the only time the defect is fixable.

**P3-4.1 (MUST) Operation classes separated.** An implementation must not provide an operation that both registers a determination and traverses a chain.

**P3-4.2 (MUST) Refusal is an outcome.** An implementation must return a refusal outcome of section 7.5 for any operation it declines and must not return an outcome of another class in its place.

**P3-4.3 (MUST) Idempotence key accepted.** An implementation must accept a caller supplied idempotence key on every registering operation and must honour it per section 6.4.

**P3-4.4 (MUST) Refusal at registration, not repair later.** An implementation must refuse a registration that fails a completeness precondition of section 4.2 rather than accepting it for later correction.

**P3-4.5 (MUST NOT) No partial registration.** An implementation must register a determination together with its whole basis, or register neither, and must not accept a determination whose citations are to be supplied by later operations.

### 4.2 Registering operations

| # | Operation | Appends | Principal refusals |
| --- | --- | --- | --- |
| 1 | Register a determination with its basis | `determination`, every `citation`, `negative_citation`, `method_citation`, `non_result_acceptance`, `alternative_considered`, `frontier`, `attribution`, `delegation_step`, `basis_digest` | No `AUTHORITY` citation and no declared frontier for it; no `METHOD` citation; a citation missing a role, pin, resolution mode or reliance flag; an `ALTERNATIVE_REJECTED` with no `SELECTION_CRITERION`; an accountable party of agent kind; a delegation chain not terminating in a person or organisation; an `AS_OF` citation without an outcome envelope; a negative citation without scope or completeness; a determination with no `basis_complete_declared` value |
| 2 | Register a determination supersession | `determination_supersession` | Either determination unknown; the two concern no common subject |
| 3 | Register a basis defect | `basis_defect` | Reporting component does not own the defective artifact |
| 4 | Enumerate and record defect impact | `defect_impact` per affected citation | Defect unknown; propagation depth undeclared |
| 5 | Record an impact assessment | assessment fields on an impact record | No named assessor for an assessment other than unassessed |
| 6 | Register a subject act | `subject_act`, and `trail_stream` where new | Sequence supplied by the caller; act kind unregistered |
| 7 | Register a value node | `value_node` | No digest |
| 8 | Register a transformation | `transformation` | Output node unknown; partiality undeclared |
| 9 | Register an attestation | `attestation` | Signer not a natural person or organisation; signature absent |
| 10 | Seal a segment and compute a commitment | `ledger_segment`, `commitment` | Segment overlaps a sealed segment |
| 11 | Publish an anchor | `anchor_publication` | External store is one the implementation controls |
| 12 | Record a reconciliation | `reconciliation` | Emitting component not a registered registrant |
| 13 | Record a gap resolution | resolution on a `gap_observation` | Resolution does not identify the cause or state that it could not be identified |
| 14 | Register a frontier kind | registration entry | Duplicate key |
| 15 | Register a method kind | registration entry | Kind admits no determinism declaration |
| 16 | Register a determination class | registration entry | Duplicate key; no owning component |
| 17 | Register a registrant | registration entry | Classes registered not declared |

Operation 1 is the whole component. Its refusal list is long because each item is a specific way in which a basis becomes unreconstructable and each is detectable only at registration.

The refusal a caller will resent most is the requirement of an `AUTHORITY` citation or an explicit frontier standing in for one. It is retained because a determination with no recorded authority is the condition `Part 2` section 11.6 describes for rules and it has the same consequence here: nobody can later establish whether the determination should have been made, and the number of such determinations is the measure of how much of the estate is unaccountable. Declaring a frontier of kind `AXIOM`, `UNDECLARED` or `OPAQUE_COMPONENT` satisfies the requirement and records the truth.

**P3-4.6 (MUST) Preconditions checked at registration.** An implementation must check every precondition in the table above at the moment of registration, must record the outcome of each check, and must not defer a check.

**P3-4.7 (MUST) Whole basis in one operation.** An implementation must accept the whole basis of a determination in a single registering operation and must record it atomically.

**P3-4.8 (MUST) Authority or a frontier.** An implementation must refuse a determination registration that carries neither an `AUTHORITY` citation nor a frontier declared in its place.

**P3-4.9 (MUST) Defect reported only by the owner.** An implementation must refuse a basis defect report from a component that does not own the artifact reported defective.

**P3-4.10 (MUST NOT) No caller supplied sequence.** An implementation must assign every sequence value itself and must refuse an entry supplying one.

**P3-4.11 (MUST) Anchor store independence checked.** An implementation must refuse to record an anchor publication to a store under its own control and must record the basis on which independence was established.

**P3-4.12 (MUST) Registrant declares its classes.** An implementation must require every registering component to declare which determination classes it registers, and must refuse a determination of an undeclared class.

**P3-4.13 (MUST NOT) No self registration of determinations.** An implementation must not register a determination whose owning component is itself, other than the reconstruction and assurance determinations of section 8.8.

### 4.3 Traversing operations

| # | Operation | Appends | Returns |
| --- | --- | --- | --- |
| 18 | Reconstruct a chain | `reconstruction_run`, `reconstruction_outcome`, access record | The chain, the five condition assessment, the enumerated outcome |
| 19 | Reconstruct restricted to reliance | as above | The chain restricted to relied upon citations |
| 20 | Enumerate determinations relying on an artifact | access record | The reverse index result with its declared latency |
| 21 | Propagate a defect | `defect_impact` per affected citation | The impact set and the truncation state |
| 22 | Verify integrity over a range | a verification entry | Segment, commitment and anchor verification results |
| 23 | Issue a receipt | access record | An inclusion proof |

**P3-4.14 (MUST) Reconstruction records its own run.** An implementation must record a reconstruction run and its outcome as entries, so that the fact that a chain was examined is itself part of the record.

**P3-4.15 (MUST) Five condition result returned.** An implementation must return the assessment of each of the five conditions of section 3.13 separately, and must not return the enumerated outcome alone.

**P3-4.16 (MUST NOT) No recomputation during traversal.** An implementation must not invoke any component to recompute, re evaluate or re resolve anything in the course of a traversal, and must report an unobtainable artifact rather than obtaining a current equivalent.

**P3-4.17 (MUST) Reverse index latency declared.** An implementation must declare the latency with which a newly registered citation becomes visible to operation 20 and must state it with every result.

**P3-4.18 (MUST) Truncation stated.** An implementation must state, with every traversal result, whether it was truncated by a declared depth, breadth or budget bound.

**P3-4.19 (MUST) Verification results recorded.** An implementation must record the outcome of every integrity verification, including a successful one, per clause P3-8.3.

### 4.4 Reading operations

| # | Operation | Returns |
| --- | --- | --- |
| 24 | Read a named projection | The projection of section 3.18 named, at the times supplied |
| 25 | Get a determination with its basis | The determination and every citation, complete |
| 26 | Get a trail | The ordered acts of a stream, with gaps marked |
| 27 | Get a lineage | The transformation graph reaching a value |
| 28 | Get coverage | Registrants, classes and reconciliation state |
| 29 | Export an evidence package | The package of section 8.6 |

**P3-4.20 (MUST) Reads do not traverse implicitly.** An implementation must not assemble a chain in the course of a reading operation without recording a reconstruction run.

**P3-4.21 (MUST NOT) No partial basis.** An implementation must return the complete basis of a determination from operation 25 or refuse, and must not return a subset without stating what was omitted and why.

**P3-4.22 (MUST) Gaps marked in a trail.** An implementation must mark every detected sequence gap in a returned trail and must not return a trail with gaps silently elided.

**P3-4.23 (MUST) Coverage readable.** An implementation must make the coverage projection readable by any principal permitted to read any determination, so that a reader can always establish what the record does not cover.

### 4.5 What a caller may and may not assume

**P3-4.24 (MUST) Caller obligations declared.** An implementation must document, for every operation, which of the assumptions below the caller may make.

A caller may assume that every citation returned was recorded at registration and has not been altered, that a reliance value of `TRUE` was asserted by the owning component, that every terminus carries a declared frontier kind, and that a determination returned was registered by the component named as its owner.

A caller may not assume that the basis is complete, since completeness is the owning component's declaration and this component cannot verify it. A caller may not assume that a reliance value of `TRUE` means the conclusion would have differed, since it means the owning component asserted dependence. A caller may not assume that a determination is sound, since soundness is assessed separately and may be assessed later. A caller may not assume that the absence of a basis defect means the basis was sound, since a defect is recorded only when someone reports it. A caller may not assume that the ledger contains every determination of a class, and the coverage projection exists so that the caller can find out what it does contain.

**P3-4.25 (MUST NOT) No implied completeness in a result.** An implementation must not describe a returned chain as the complete reasoning behind a determination, and must describe it as the basis as registered.

**P3-4.26 (MUST) Absence of defect not reported as soundness.** An implementation must not report a determination as sound on the ground that no basis defect has been recorded against it.

### 4.6 Reads from other components

| Read | From | On unavailability |
| --- | --- | --- |
| Resolve a cited document version and its status | `Part 1` | Record the pin as unresolved at this knowledge time; do not alter the citation |
| Obtain an evaluation report or verdict envelope | `Part 2` | As above |
| Obtain a term or definition version | `Part 4` | As above |
| Obtain a decision artifact or selection criterion | `Part 5` | As above |
| Obtain an authorisation decision | `Part 7` | Refuse the operation |
| Obtain a reference set version | `Part 10` | Record the pin as unresolved |
| Obtain cited content octets | `Part 11` | Record the pin as unresolved |
| Obtain a model invocation record | `Part 13` | Record the pin as unresolved |

The pattern differs from `Part 2`'s deliberately. There, an unobtainable dependency prevented an evaluation, because without it the component did not know what the rule meant. Here, an unobtainable dependency does not prevent anything, because this component is not computing: it records that the artifact could not be obtained at this knowledge time and reports it in the closure outcome. The distinction matters because a ledger that refused to answer whenever a cited artifact was unavailable would be useless in exactly the circumstances it exists for.

**P3-4.27 (MUST) Unavailability recorded, not propagated as failure.** An implementation must record a cited artifact as unobtainable at a knowledge time and must continue to return the chain, per section 7.2.

**P3-4.28 (MUST NOT) No substitution on unavailability.** An implementation must not substitute a current, cached, successor or equivalent version of any cited artifact, and must not represent a substitution as the cited artifact.

**P3-4.29 (MUST) Unobtainability is timestamped, not permanent.** An implementation must record unobtainability against a knowledge time rather than as a property of the citation, since an artifact unobtainable today may be obtainable tomorrow.

### 4.7 Events emitted

The envelope carries at minimum: an event identity, a type from the registered set, the knowledge time assigned by this component, the entry or determination concerned, the actor, a correlation reference, a schema reference, and a digest over the event body.

The minimum event set. An implementation may emit more.

Determination registered. Determination registration refused. Basis digest recorded. Determination superseded. Citation with indeterminate reliance recorded. Negative citation with unknown or partial completeness recorded. Non result acceptance recorded. Proceeding without basis recorded. Undeclared frontier recorded. Undeclared method recorded. Delegation without an instrument recorded. Attestation registered. Basis defect registered. Defect impact enumerated. Impact assessed. Determination became unsound. Subject act registered. Trail gap observed. Trail gap resolved. Value node registered. Transformation registered. Lineage divergence from design observed. Segment sealed. Commitment computed. Anchor published. Anchor verification failed. Receipt issued. Reconciliation discrepancy observed. Reconstruction run performed. Reconstruction closure failed. Reverse index enumeration performed. Evidence package exported. Registrant registered. Registrant ceased registering.

The last of these is the most important operational event in the part and the least obvious. A component that stops registering determinations produces no events, no errors and no findings; the ledger simply stops receiving from it, and every report about the remaining determinations continues to look healthy. Clause P3-4.33 requires the cessation to be detected and emitted, which is the only way anyone learns.

**P3-4.30 (MUST) Minimum event set.** An implementation must emit an event for every member of the set above and must register any additional type under section 9.9.

**P3-4.31 (MUST) Envelope minimum.** An implementation must include every envelope element named above in every event it emits.

**P3-4.32 (MUST NOT) No event in place of an entry.** An implementation must not rely on event emission to satisfy any recording obligation of section 3 or section 8.

**P3-4.33 (MUST) Cessation of registration detected.** An implementation must detect, within a declared interval, that a registrant which previously registered determinations of a class has ceased to do so, must emit the event, and must declare the interval.

**P3-4.34 (MUST NOT) No suppression of adverse events.** An implementation must not provide a configuration that suppresses the emission of a refusal, an undeclared frontier, an undeclared method, a proceeding without basis, a defect, an unsoundness, a gap, a reconciliation discrepancy, a closure failure or an anchor verification failure.
## 5. State model

### 5.1 Nothing recorded ever changes state

The organising principle of this section is a negative one, and it distinguishes this part from the two before it.

`Part 1` gives a document version a lifecycle: it is drafted, approved, becomes effective, is superseded. `Part 2` gives a rule version an admission lifecycle. In both, the governed thing itself transitions.

Here, the governed thing never transitions. A determination is recorded and is thereafter a fixed historical fact: at this instant, this component concluded this, on this basis. There is no state in which a determination is pending, approved, active or retired, because none of those is a property of a past conclusion.

What does have state is **assertions about** the record, and there are four such machines.

The **soundness overlay** on a determination, which changes as defects are found and assessed. The determination does not change; what we believe about its basis does.

The **segment lifecycle**, which is a property of the ledger's integrity machinery rather than of anything recorded in it.

The **gap observation lifecycle**, which tracks the investigation of a detected discontinuity.

The **reconstruction run lifecycle**, which tracks one attempt at assembly.

This separation is the same pattern the two prior parts use, applied more strictly: `Part 1` separates lifecycle status from derived force state, `Part 2` separates admission state from force state, and this part separates the immutable record from every assertion about it. A reviewer should read the pattern as deliberate rather than coincidental, and section 12.14 hands `Part 0` the question of whether it should be stated once for the whole standard.

**P3-5.1 (MUST) Determinations have no lifecycle.** An implementation must not assign a lifecycle state to a determination, a citation, a subject act, a value node or a transformation.

**P3-5.2 (MUST) Assertions carry the state.** An implementation must represent every state in this section as a property of an assertion about a record, computed from appended entries, and must not hold it as an updatable field on the record.

**P3-5.3 (MUST NOT) No status field on a determination.** An implementation must not provide a field on a determination whose value can be changed to indicate that the determination is inactive, void, cancelled, withdrawn or corrected.

**P3-5.4 (MUST) Correction is a new determination.** An implementation must record a corrected conclusion as a new determination with its own basis and a recorded supersession relation, per section 5.5.

### 5.2 Soundness overlay of a determination

States, computed from defect and impact entries:

`SOUND_AS_RECORDED`. No basis defect has been reported against any artifact the determination relied upon. This is not a positive finding of soundness. It is the absence of a report, and clause P3-4.26 forbids presenting it as more.

`UNSOUNDNESS_SUSPECTED`. A basis defect has been reported against a relied upon artifact and the impact has not been assessed.

`UNSOUND_MATERIAL`. An assessment found the defect material to the determination.

`UNSOUND_IMMATERIAL`. An assessment found the defect real and not material.

`SOUND_DESPITE_DEFECT`. An assessment found that the determination stands notwithstanding the defect, for reasons recorded.

`SOUNDNESS_UNASSESSABLE`. The artifact needed to assess the impact is no longer obtainable, so the question cannot be settled either way.

Transitions:

| From | To | Trigger | Requires |
| --- | --- | --- | --- |
| `SOUND_AS_RECORDED` | `UNSOUNDNESS_SUSPECTED` | A defect reported against a relied upon artifact | Defect entry and impact entry |
| `UNSOUNDNESS_SUSPECTED` | `UNSOUND_MATERIAL` | Assessment | Named assessor and reason |
| `UNSOUNDNESS_SUSPECTED` | `UNSOUND_IMMATERIAL` | Assessment | Named assessor and reason |
| `UNSOUNDNESS_SUSPECTED` | `SOUND_DESPITE_DEFECT` | Assessment | Named assessor and reason |
| `UNSOUNDNESS_SUSPECTED` | `SOUNDNESS_UNASSESSABLE` | The artifact required is unobtainable | Recorded unobtainability |
| any of the four assessed states | `UNSOUNDNESS_SUSPECTED` | A further defect reported | A new defect entry |
| `SOUNDNESS_UNASSESSABLE` | any assessed state | The artifact became obtainable | Named assessor and reason |

There is no transition back to `SOUND_AS_RECORDED`. Once a defect has been reported, the determination's history contains that report permanently, and a state meaning no defect was ever reported would be false. This is the same reasoning `Part 2` applies in refusing a dismissal state for a drift observation: a register that can be emptied is a register that tells you nothing.

`SOUNDNESS_UNASSESSABLE` is a real and uncomfortable state. It arises when the retracted document, the corrected feed or the defective model output has itself been disposed of, so that nobody can now determine whether the determination would have differed. It is recorded rather than resolved because the alternative is to record a guess.

**P3-5.5 (MUST) Enumerated soundness states.** An implementation must represent the soundness overlay of every determination as exactly one member of the set above, computed from entries.

**P3-5.6 (MUST) Enumerated transitions only.** An implementation must not effect a transition absent from the table above.

**P3-5.7 (MUST NOT) No return to sound as recorded.** An implementation must not transition a determination back to `SOUND_AS_RECORDED` once a defect has been reported against it.

**P3-5.8 (MUST) Assessment attributed and reasoned.** An implementation must record a named assessor and a reason for every transition into an assessed state.

**P3-5.9 (MUST) Unassessable recorded rather than inferred.** An implementation must record `SOUNDNESS_UNASSESSABLE` where the artifact required to assess an impact is unobtainable, and must not record an assessed state in its place.

**P3-5.10 (MUST NOT) No automatic assessment.** An implementation must not assess materiality itself, and must not transition out of `UNSOUNDNESS_SUSPECTED` without a recorded act by a named actor.

**P3-5.11 (MUST) Suspected unsoundness surfaced in every read.** An implementation must return the soundness state with every determination it returns, and must not omit it in any interface, projection or export.

### 5.3 Segment lifecycle

States: `OPEN`, `SEALED`, `COMMITTED`, `ANCHORED`, `ANCHOR_VERIFIED`, `ANCHOR_VERIFICATION_FAILED`, `INTEGRITY_FAILED`.

| From | To | Trigger |
| --- | --- | --- |
| `OPEN` | `SEALED` | The declared segment boundary reached |
| `SEALED` | `COMMITTED` | Commitment computed and chained to its predecessor |
| `COMMITTED` | `ANCHORED` | Commitment published to an independent store |
| `ANCHORED` | `ANCHOR_VERIFIED` | Verification against the external store succeeded |
| `ANCHORED` | `ANCHOR_VERIFICATION_FAILED` | Verification failed or the external record is absent |
| `ANCHOR_VERIFICATION_FAILED` | `ANCHOR_VERIFIED` | Re verification succeeded |
| `COMMITTED`, `ANCHORED`, `ANCHOR_VERIFIED` | `INTEGRITY_FAILED` | Recomputation over the segment does not match its commitment |

`INTEGRITY_FAILED` is terminal and is not repairable within the model. A segment whose recomputed digest does not match its commitment has either been altered or the commitment procedure has changed unrecorded, and both are findings rather than faults to be cleared. Clause P3-3.119 forbids removing entries to repair it and clause P3-5.17 forbids recomputing a replacement commitment.

The separation of `ANCHOR_VERIFICATION_FAILED` from `INTEGRITY_FAILED` matters. The first says the external record could not be checked, which is frequently a fault in the external store or in connectivity. The second says the ledger's own content does not match what was committed. Reporting the first as the second produces false alarms that train people to ignore both.

**P3-5.12 (MUST) Enumerated segment states.** An implementation must represent every segment as exactly one member of the set above.

**P3-5.13 (MUST) Sealing on a declared boundary.** An implementation must declare its segment boundary, by entry count, time interval or both, and must seal on it.

**P3-5.14 (MUST) Commitments chained.** An implementation must include the prior segment's commitment digest in each commitment.

**P3-5.15 (MUST) External verification distinguished from integrity failure.** An implementation must distinguish an inability to verify against the external store from a mismatch between the ledger content and its commitment.

**P3-5.16 (MUST) Integrity failure terminal and reported.** An implementation must treat `INTEGRITY_FAILED` as terminal, must emit the event, and must report every determination whose entries fall within the affected segment.

**P3-5.17 (MUST NOT) No commitment recomputation.** An implementation must not replace, recompute or reissue the commitment of a sealed segment.

**P3-5.18 (MUST) Unanchored interval bounded and declared.** An implementation must declare the maximum interval for which entries may remain unanchored and must report an interval exceeding it.

### 5.4 Gap observation lifecycle

States: `OPEN`, `RESOLVED_LOSS_IN_TRANSIT`, `RESOLVED_EMITTER_FAULT`, `RESOLVED_SEQUENCE_ALLOCATION`, `RESOLVED_CAUSE_UNDETERMINED`, `SUPERSEDED_BY_OBSERVATION`.

There is no dismissal state, for the reason `Part 2` gives in its section 5.4. `RESOLVED_CAUSE_UNDETERMINED` is the honest terminus of an investigation that could not establish what happened, and it is separately countable, because a system in which most gaps resolve that way has a systemic problem that no individual gap reveals.

`RESOLVED_SEQUENCE_ALLOCATION` covers the benign case where a sequence value was allocated and the entry was never written, for example a transaction that rolled back. It is benign only if it is demonstrable, which is why it requires the allocation record to be cited.

**P3-5.19 (MUST) Enumerated gap states.** An implementation must represent every gap observation as exactly one member of the set above.

**P3-5.20 (MUST NOT) No dismissal.** An implementation must not provide a means of closing a gap observation without recording one of the four resolutions or a subsuming observation.

**P3-5.21 (MUST) Allocation cited where claimed.** An implementation must cite the sequence allocation record for every resolution of `RESOLVED_SEQUENCE_ALLOCATION`.

**P3-5.22 (MUST) Undetermined cause countable.** An implementation must be able to report every gap resolved as `RESOLVED_CAUSE_UNDETERMINED` and must include the count in the signals of section 8.5.

### 5.5 Determination supersession

Supersession is a relation, not a state. A later determination may supersede an earlier one, and both remain true records of what was concluded at their respective instants.

The relation carries a kind: `CORRECTION`, where the earlier determination is now held to have been wrong; `REVISION`, where circumstances changed and a new conclusion was reached on a new basis; `REAFFIRMATION`, where the question was reconsidered and the same conclusion reached; and `SUPERSESSION_UNSPECIFIED`.

The distinction between `CORRECTION` and `REVISION` is load bearing and is routinely lost. A correction asserts that the earlier determination should not have been made as it was; a revision asserts that it was right then and is not right now. They have different consequences for everything that relied on the earlier determination, and an organisation that records only that a later determination exists cannot tell which happened.

**P3-5.23 (MUST) Supersession is a relation.** An implementation must record supersession as a relation between two determinations and must not represent it as a state change on either.

**P3-5.24 (MUST) Supersession kind recorded.** An implementation must record a kind from the set above and must not default it.

**P3-5.25 (MUST) Correction implies a defect.** An implementation must record a basis defect, or a declared reason why none applies, for every supersession of kind `CORRECTION`.

**P3-5.26 (MUST) Superseded determinations remain readable.** An implementation must return a superseded determination in full on request, with its supersession relation, and must not redirect a read to the superseding determination.

### 5.6 Reconstruction run lifecycle

States: `REQUESTED`, `ASSEMBLING`, `RESOLVING_PINS`, `ASSESSING`, `COMPLETED`, `TRUNCATED`, `REFUSED`, `ABANDONED`.

| From | To | Trigger |
| --- | --- | --- |
| `REQUESTED` | `ASSEMBLING` | Request accepted and authorised |
| `REQUESTED` | `REFUSED` | Determination unknown, or not authorised |
| `ASSEMBLING` | `RESOLVING_PINS` | The citation graph assembled to its bounds |
| `RESOLVING_PINS` | `ASSESSING` | Every pin attempted |
| `ASSESSING` | `COMPLETED` | Five conditions assessed and outcome recorded |
| `ASSEMBLING`, `RESOLVING_PINS` | `TRUNCATED` | A declared depth, breadth or budget bound reached |
| `TRUNCATED` | `ASSESSING` | Assessment proceeds on the truncated chain |
| any | `ABANDONED` | Loss of the executing process |

`TRUNCATED` transitions into `ASSESSING` rather than terminating, because a truncated chain still yields a useful assessment provided the truncation is reported. What must never happen is a truncated chain assessed as closed, which clause P3-5.31 forbids.

**P3-5.27 (MUST) Enumerated run states.** An implementation must represent every reconstruction run as exactly one member of the set above.

**P3-5.28 (MUST) Pins attempted before assessment.** An implementation must attempt to resolve every pin in the assembled chain before assessing the five conditions.

**P3-5.29 (MUST) Truncation recorded on the run.** An implementation must record the bound that truncated a run and the point at which truncation occurred.

**P3-5.30 (MUST) Truncated runs still assessed.** An implementation must assess and record an outcome for a truncated run rather than returning no outcome.

**P3-5.31 (MUST NOT) No truncated chain as closed.** An implementation must not record a closure outcome of `RECONSTRUCTED_COMPLETE` or `RECONSTRUCTED_TO_FRONTIER` for a truncated run.

**P3-5.32 (MUST) Abandonment detected and recorded.** An implementation must transition a run whose executing process is lost to `ABANDONED` within a declared interval and must declare the interval.

**P3-5.33 (MUST) Terminal states are terminal.** An implementation must not transition out of `COMPLETED`, `REFUSED` or `ABANDONED`.
## 6. Execution semantics

### 6.1 Determinism of reading

This component computes almost nothing, and the little it computes must be deterministic in a specific sense: two readers assembling the same chain from the same entries, at the same knowledge time, must obtain the same chain, the same five condition assessment and the same closure outcome.

That is weaker than the reproducibility `Part 2` requires of an evaluation and it is achieved differently. `Part 2` must pin what it read because it computed a result. This component must pin nothing new, because the pins are already in the record; what it must control is traversal order, bound application and the resolution attempt, all three of which vary between readings unless constrained.

**P3-6.1 (MUST) Traversal order total and declared.** An implementation must impose a declared total order on the traversal of a chain and must not permit the order to vary between readings of the same entries.

**P3-6.2 (MUST) Bounds applied deterministically.** An implementation must apply depth, breadth and budget bounds in a declared order and must truncate at the same point on repeated readings of the same entries.

**P3-6.3 (MUST) Assessment deterministic given resolution results.** An implementation must produce the same five condition assessment and the same closure outcome from the same entries and the same set of pin resolution results.

**P3-6.4 (MUST) Resolution results recorded per attempt.** An implementation must record, for each pin resolution attempt, whether the artifact was obtained, at what knowledge time, and the outcome the resolving component returned, so that a differing assessment on a later reading is attributable to a differing resolution rather than to the traversal.

**P3-6.5 (MUST NOT) No caching of resolution results as facts.** An implementation must not treat a prior successful resolution as establishing present obtainability, and must record obtainability against the knowledge time of each attempt, per clause P3-4.29.

### 6.2 Ordering, sequence and causality

Three orderings exist in this component and they are not the same order.

**Sequence order.** The order in which this component appended entries, carried by `SEQ` within a declared stream. This is the only total order the component owns, and it is the order over which integrity commitments are computed.

**Occurrence order.** The order in which acts happened in the world, as asserted by actors. Partial at best, since two actors' assertions cannot be compared without a shared clock.

**Causal order.** The order imposed by the citation graph: a determination that cites another occurred after it. Partial, and the only one of the three that is semantically meaningful for reasoning.

The three disagree routinely and each disagreement is a fact worth recording rather than a problem to be smoothed. An entry appended before another may describe a later occurrence. A determination may cite one whose entry has a higher sequence number, because the cited determination was registered late.

That last case must be handled and must not be prohibited. Prohibiting it would require the component to reject a late registration, which would lose the record entirely. Permitting it silently would let a chain contain a citation to something that, on the sequence order, did not yet exist. The resolution is clause P3-6.9: a citation whose target has a later sequence than the citing determination is recorded, is flagged, and is reported, because it is either a late registration or a defect and the distinction requires investigation.

**P3-6.6 (MUST) Three orderings distinguished.** An implementation must not use one field or one order for sequence, occurrence and causal order.

**P3-6.7 (MUST) Sequence is the integrity order.** An implementation must compute every commitment over sequence order and must not compute one over occurrence order.

**P3-6.8 (MUST) Occurrence order not totalised.** An implementation must not impose a total order on occurrence times from different actors and must not present one as authoritative.

**P3-6.9 (MUST) Retrograde citation flagged.** An implementation must record and report every citation whose target entry has a later sequence than the citing determination's entry, and must not refuse the registration.

**P3-6.10 (MUST) Occurrence beyond knowledge time bounded.** An implementation must record where an asserted occurrence time exceeds the knowledge time assigned by more than a declared tolerance, must declare the tolerance, and must not adjust either value.

**P3-6.11 (MUST) Causal cycles reported.** An implementation must detect a cycle in the citation graph and must report it as a defect of the record rather than traversing it.

**P3-6.12 (MUST NOT) No reordering on read.** An implementation must not reorder entries within a stream on read and must return them in sequence order with any gap marked.

### 6.3 Clocks

Three clocks, on the same basis and with the same names as `Part 1` section 3.1 and `Part 2` section 6.5.

**P3-6.13 (MUST) Knowledge time assigned by this component.** An implementation must assign every knowledge time from its own clock and must refuse an entry supplying one.

**P3-6.14 (MUST NOT) No occurrence time assignment.** An implementation must not assign an occurrence time and must record every one as asserted by a named actor.

**P3-6.15 (MUST) Application time cited, not determined.** An implementation must record application times as supplied by the components that resolved against them and must not itself determine what was in force at one.

**P3-6.16 (MUST) Instants in a declared scale.** An implementation must record every instant in a declared time scale with a declared offset and must not record a local time without its offset.

**P3-6.17 (MUST) Monotonic knowledge time within a stream.** An implementation must assign knowledge times that do not decrease within a stream, and must record any correction of its own clock as an entry.

### 6.4 Idempotence

**P3-6.18 (MUST) Idempotence by key.** An implementation must return the originally recorded outcome for a repeated registering operation bearing an idempotence key already seen within its declared deduplication window and must not append again.

**P3-6.19 (MUST) Deduplication window declared.** An implementation must declare its deduplication window as a duration and must state what happens to a key repeated after it.

**P3-6.20 (MUST NOT) No idempotence across differing payloads.** An implementation must refuse an operation bearing a seen key with a different payload and must not return the earlier outcome.

**P3-6.21 (MUST) Duplicate registration without a key detectable.** An implementation must be able to report determinations whose owning component, conclusion reference and basis digest coincide, so that a duplicate registered without a key is discoverable.

### 6.5 The reconstruction algorithm

Normative in its ordering and in its outcomes; not normative in its structure as code.

```
reconstruct(determination_id, principal, bounds):
  1  d = determination(determination_id)
     if unknown:                  return REFUSED(DETERMINATION_UNKNOWN)
  2  decision = obtain authorisation from Part 7 for principal and purpose
     if not permitted:            return REFUSED(NOT_AUTHORISED)
  3  frontier_set = {}; nodes = {d}; edges = {}; open = {d}
  4  while open not empty and bounds not exceeded:
        n = next(open) in declared traversal order
        for each citation c of n in declared citation order:
            edges += c
            if principal not permitted to traverse c:
                frontier_set += ACCESS_WITHHELD at c, against this run
                continue
            if c has a declared frontier:
                frontier_set += that frontier
                continue
            t = target(c)
            if t is a determination held here:  nodes += t; open += t
            else:                               nodes += t   // a leaf artifact
  5  if bounds exceeded:          state = TRUNCATED
  6  for each pin in edges:
        attempt resolution; record obtained or unobtainable with this knowledge time
        if unobtainable and no declared frontier:
            frontier_set += FRONTIER_UNDECLARED at that citation
  7  assess condition 1, resolution:      every pin obtained or at a declared frontier
     assess condition 2, role completeness: mandatory roles present at every determination
     assess condition 3, closure:          every terminus a declared frontier, none undeclared
     assess condition 4, method:           method citation present and, where pinnable, obtained
     assess condition 5, independence:     no pin required a producing component to dereference
  8  soundness = soundness overlay of every determination in nodes
  9  outcome = enumerate per section 7.2 from the five assessments, the truncation
     state and the soundness overlay
 10  record reconstruction_run and reconstruction_outcome; record the access
 11  return chain, five assessments, frontier set, soundness overlay, outcome
```

Three properties of the algorithm are worth stating because each is a decision.

Step 4 records the access frontier against the run rather than the chain, per clause P3-3.71, so that two principals reconstructing the same determination get different frontier sets and the same chain.

Step 6 converts an unobtainable pin with no declared frontier into `FRONTIER_UNDECLARED` rather than into an error. The chain is still returned; what changes is the closure outcome. This is the behaviour that makes the component useful in the circumstances it exists for, when things have already gone missing.

Step 8 attaches the soundness overlay to the result rather than leaving it to a second query, because a reader who obtains a beautifully closed chain and does not know that its authority was retracted has been misled by a true answer.

**P3-6.22 (MUST) Algorithm order.** An implementation must perform the steps above in the order given and must not assess any condition before attempting every pin in the assembled chain.

**P3-6.23 (MUST) Access frontier against the run.** An implementation must record a frontier arising from an access decision against the reconstruction run and the principal and must not record it against the determination.

**P3-6.24 (MUST) Unobtainable pin becomes an undeclared frontier.** An implementation must record `FRONTIER_UNDECLARED` where a pin cannot be resolved and no frontier was declared at that citation, and must continue rather than failing the run.

**P3-6.25 (MUST) Soundness returned with the chain.** An implementation must return the soundness overlay of every determination in the chain together with the chain and must not require a separate request for it.

**P3-6.26 (MUST) Five assessments returned separately.** An implementation must return the assessment of each condition separately in addition to the enumerated outcome.

**P3-6.27 (MUST NOT) No resolution of what was in force.** An implementation must not resolve an `AS_OF` citation itself and must return the outcome envelope recorded at registration.

### 6.6 Bounds and budget

Traversal must terminate. A chain over a real estate is not large in the number of determinations and can be very large in the number of leaf artifacts, and a defect in the record can make it unbounded.

Three bounds are required. **Depth**, the number of determination to determination hops. **Breadth**, the number of citations traversed from any one node. **Budget**, a bound on a declared resource.

As in `Part 2` section 6.7, the resource matters. A budget on a deterministic resource, such as citations traversed or pins attempted, truncates at the same point on repeated readings. A budget on wall clock time does not, so the same reconstruction can close on one day and truncate on another, and the two readings then disagree about the closure outcome for reasons the record does not contain. The primary bound must therefore be deterministic.

**P3-6.28 (MUST) Three bounds declared.** An implementation must declare a depth bound, a breadth bound and a budget, and must state the resource the budget bounds.

**P3-6.29 (MUST) Primary budget deterministic.** An implementation must make its primary budget a bound on a deterministic resource.

**P3-6.30 (MAY) Secondary non deterministic guard.** An implementation may enforce an additional bound on a non deterministic resource.

**P3-6.31 (MUST) Non deterministic truncation marked.** An implementation must mark a run truncated by a non deterministic bound as not repeatable and must not present its outcome as a stable property of the chain.

**P3-6.32 (MUST) Truncation point recorded.** An implementation must record the node and citation at which truncation occurred, so that a later run with larger bounds can be compared with the earlier one.

**P3-6.33 (MUST NOT) No silent bound.** An implementation must not apply an undeclared bound and must not return a truncated result without stating the bound that truncated it.

### 6.7 Defect propagation

```
propagate(defect, depth_bound):
  1  affected = citations whose pin matches defect.defective_pin
       and whose determination's evaluation_instant falls within
       defect.effective_from_atime range, where that range is bounded
  2  for each c in affected:
        append defect_impact(defect, c.determination, c, c.relied_upon,
                             MATERIALITY_UNASSESSED)
  3  frontier = determinations in affected
  4  for hop in 1..depth_bound:
        next = citations of role PRIOR_DETERMINATION whose target is in frontier
        for each c in next:
            append defect_impact(defect, c.determination, c, c.relied_upon,
                                 MATERIALITY_UNASSESSED)
        frontier = determinations in next
        if frontier empty: break
  5  if hop reached depth_bound and frontier not empty:
        record truncation with the frontier size
  6  return impact set, truncation state
```

Step 2 propagates to every matching citation regardless of its reliance value, including citations whose reliance is `FALSE`. That is deliberate. A `CONTEXT` citation to a defective artifact is almost certainly immaterial, and almost certainly is not a basis for omitting it, because the owning component's reliance assertion may itself have been wrong and the enumeration is the only chance to notice. What the reliance value does is order the work: clause P3-6.36 requires the impact set to be reportable by reliance so that an assessor starts with the citations asserted to have been relied upon.

**P3-6.34 (MUST) Propagation exhaustive at the first hop.** An implementation must create an impact record for every citation whose pin matches the defective artifact within the defect's application time range, regardless of reliance value.

**P3-6.35 (MUST) Transitive propagation through prior determinations.** An implementation must propagate through citations of role `PRIOR_DETERMINATION` to the declared depth and must record truncation where the frontier is not empty at the bound.

**P3-6.36 (MUST) Impact set orderable by reliance.** An implementation must be able to report an impact set partitioned by the reliance value recorded on the affected citation.

**P3-6.37 (MUST NOT) No propagation through context only paths beyond the first hop.** An implementation must not traverse a citation of reliance `FALSE` in order to reach a further determination, and must declare this bound where it affects a result.

**P3-6.38 (MUST) Unbounded application time handled.** An implementation must treat a defect with no application time range as affecting every reliance on the artifact at the affected version and must record the resulting impact set size.

### 6.8 Integrity verification

```
verify(range):
  1  for each segment in range, in sequence order:
       recompute the commitment over its entries using the pinned procedure
       compare with the recorded commitment
       compare the recorded prior commitment digest with its predecessor's
  2  for each anchored commitment:
       obtain the external record; compare
       record ANCHOR_VERIFIED or ANCHOR_VERIFICATION_FAILED
  3  detect and report every sequence gap in the range
  4  compare recorded counts against reconciliation records for the period
  5  record the verification as an entry, whether or not it found anything
  6  return per segment results, gaps, reconciliation discrepancies, and the
     statement of what verification does not establish
```

Step 6 is a requirement rather than a courtesy. Every verification result must carry the statement that verification establishes non alteration of what is present and does not establish that everything was recorded, because a verification result reported without it will be read as a certificate of completeness by the next person who quotes it.

**P3-6.39 (MUST) Recomputation by the pinned procedure.** An implementation must recompute each commitment using the procedure pinned with it and must not use a current procedure where it differs.

**P3-6.40 (MUST) Chain of commitments verified.** An implementation must verify that each commitment records its predecessor's digest.

**P3-6.41 (MUST) Verification recorded whether or not adverse.** An implementation must record every verification as an entry, including one that found nothing.

**P3-6.42 (MUST) Limit statement accompanies every result.** An implementation must include the statement of clause P3-3.116 with every verification result it returns or records.

**P3-6.43 (MUST NOT) No repair by verification.** An implementation must not alter, remove or rewrite any entry, commitment or segment in the course of verification.

### 6.9 What this component may compute, and what it may not

The line is worth stating explicitly because every capability on the wrong side of it is one somebody will ask for.

It may compute: the transitive closure of a citation graph; the five condition assessment; the closure outcome; the soundness overlay from defect and impact entries; digests and commitments; sequence gaps; counts and their grains; the reverse index; and the divergence between an instance lineage and a design lineage assertion.

It may not compute: what was in force at a time, which is `Part 1`; whether a rule was satisfied, which is `Part 2`; whether a determination's conclusion follows from its basis, which is nobody's in this standard; whether a defect was material, which is a named person's or the owning component's; which of several candidate outcomes should have been selected, which is `Part 5`; or whether a delegation was valid, which is `Part 7`.

**P3-6.44 (MUST) Permitted computations only.** An implementation must not compute any determination allocated to another component by section 12 and must return the recorded outcome that component supplied.

**P3-6.45 (MUST NOT) No inference of a missing citation.** An implementation must not infer, reconstruct or supply a citation that was not registered, including where the omission is obvious from the pattern of other determinations of the same class.

**P3-6.46 (MUST NOT) No inference of reliance.** An implementation must not infer a reliance value from the method, the role, the artifact kind or the behaviour of other determinations.

**P3-6.47 (MUST NOT) No inference of a frontier kind.** An implementation must not infer a frontier kind from the reason a pin could not be resolved, and must record `FRONTIER_UNDECLARED` where no kind was declared.
## 7. Outcome and failure taxonomy

### 7.1 Why the taxonomy is the specification

In this component the taxonomy carries a burden it does not carry elsewhere in the standard, because this component's entire output is a statement about the quality of a record. Every other part produces a result whose correctness can eventually be checked against the world. This part produces an assessment of whether an account is adequate, and an assessment that is not finely enough divided will be read as approval.

The specific danger is a two valued reading. A reconstruction that returns anything other than a plain failure will be reported upward as evidence that the determination was properly made. Section 7.2 therefore separates the outcomes that mean the account is adequate from those that mean the account stopped, and separates both from those that mean the account is defective, and requires that the three never be presented under one heading.

Four classes and thirteen members.

| Class | Member | Means |
| --- | --- | --- |
| Closed | `RECONSTRUCTED_COMPLETE` | Every citation resolved, every role present, no frontier reached, method obtained, independence satisfied. |
| Closed | `RECONSTRUCTED_TO_FRONTIER` | As above, and the chain terminated at one or more declared frontiers. |
| Incomplete | `INCOMPLETE_ARTIFACT_UNOBTAINABLE` | A cited artifact could not be obtained and no frontier was declared for it. |
| Incomplete | `INCOMPLETE_UNDECLARED_FRONTIER` | The chain stopped with no reason recorded. |
| Incomplete | `INCOMPLETE_ROLE_MISSING` | A mandatory role is absent from a determination in the chain. |
| Incomplete | `INCOMPLETE_METHOD_UNRECORDED` | A method citation is absent or its pin is unobtainable and undeclared. |
| Incomplete | `INCOMPLETE_TRUNCATED` | A declared depth, breadth or budget bound was reached. |
| Incomplete | `INCOMPLETE_DEPENDENT_ON_PRODUCER` | A pin could not be dereferenced without the producing component. |
| Defective | `DEFECTIVE_CYCLE` | The citation graph contains a cycle. |
| Defective | `DEFECTIVE_LEDGER_INTEGRITY` | A segment containing entries in the chain failed integrity verification. |
| Defective | `DEFECTIVE_RETROGRADE_CITATION` | A citation targets an entry appended after the citing determination and the discrepancy is unexplained. |
| Withheld | `WITHHELD_IN_PART` | The reader was not permitted to traverse part of the chain. |
| Refusal | `REFUSED` | The component declined the request. Carries a code. |

The table is normative.

Five distinctions in it are load bearing.

**`RECONSTRUCTED_COMPLETE` against `RECONSTRUCTED_TO_FRONTIER`.** The first is rare and in a real estate almost non existent, because nearly every chain reaches a statute, a person's judgement or a physical observation. The second is the normal good outcome. They are separated so that the frontier kinds must be enumerated with the result, which is how a reader learns that the chain closed at `OPAQUE_COMPONENT` eleven times rather than at an external statute once.

**`RECONSTRUCTED_TO_FRONTIER` against `INCOMPLETE_UNDECLARED_FRONTIER`.** Identical in shape and opposite in meaning. Both are chains that stopped. In one the stopping was declared and justified; in the other nobody said why. The whole of section 3.11 exists to make this distinction expressible, and a component that cannot draw it cannot tell a complete account from an abandoned one.

**`INCOMPLETE_ARTIFACT_UNOBTAINABLE` against `INCOMPLETE_DEPENDENT_ON_PRODUCER`.** The first says the artifact is gone. The second says it is probably there and this record cannot reach it without a component that may not outlive the question. The second is a design defect in how the citation was recorded and is fixable for future determinations; the first is not.

**Incomplete against defective.** An incomplete chain is an inadequate account. A defective chain is evidence that the record itself is wrong: a cycle, an integrity failure, an unexplained retrograde citation. The first is a finding about a determination; the second is a finding about this component and must be escalated differently.

**`WITHHELD_IN_PART` against everything.** A withheld outcome is a property of the reading, not of the chain. The same determination reconstructed by an authorised reader may return `RECONSTRUCTED_TO_FRONTIER`. Recording it as an incompleteness of the chain would make an access decision look like a defect in the record, and would let a poorly authorised reader conclude that a well documented determination was undocumented.

**P3-7.1 (MUST) Closed outcome set.** An implementation must return exactly one member of the table above for every reconstruction run and must not return a value outside the set.

**P3-7.2 (MUST NOT) No additional members.** An implementation must not add a member and must express any further distinction as a registered code within the `REFUSED` class or as a frontier kind.

**P3-7.3 (MUST) Frontier kinds enumerated with the outcome.** An implementation must return the kind and count of every frontier reached with every outcome of `RECONSTRUCTED_TO_FRONTIER`.

**P3-7.4 (MUST) Complete and to frontier distinguished.** An implementation must not return `RECONSTRUCTED_COMPLETE` for a chain that reached any frontier.

**P3-7.5 (MUST) Withheld distinguished from incomplete.** An implementation must return `WITHHELD_IN_PART` where the reader was not permitted to traverse, must record the principal, and must not return an incomplete or defective member in its place.

**P3-7.6 (MUST) Defective escalated separately.** An implementation must report every outcome of the defective class through a channel distinct from the reporting of incomplete outcomes and must emit the corresponding event.

**P3-7.7 (MUST NOT) No mapping onto two values.** An implementation must not provide an interface that maps the thirteen members onto two values and must not document such a mapping as canonical.

**P3-7.8 (MUST NOT) No caller selected collapse.** An implementation must not offer a configuration by which an incomplete or defective outcome is returned as a closed outcome.

### 7.2 Composition of the outcome from the five assessments

The outcome is derived, not asserted. The derivation is normative.

| Condition failing | Resulting member |
| --- | --- |
| None, and no frontier reached | `RECONSTRUCTED_COMPLETE` |
| None, and a frontier reached | `RECONSTRUCTED_TO_FRONTIER` |
| Condition 1, a pin unobtainable with no frontier | `INCOMPLETE_ARTIFACT_UNOBTAINABLE` |
| Condition 2, a mandatory role absent | `INCOMPLETE_ROLE_MISSING` |
| Condition 3, an undeclared terminus | `INCOMPLETE_UNDECLARED_FRONTIER` |
| Condition 4, method absent or unobtainable and undeclared | `INCOMPLETE_METHOD_UNRECORDED` |
| Condition 5, a pin requiring the producer | `INCOMPLETE_DEPENDENT_ON_PRODUCER` |
| A bound reached | `INCOMPLETE_TRUNCATED` |

Where more than one condition fails, the member reported is the first in the following precedence: defective members in the order given in section 7.1; then `INCOMPLETE_ROLE_MISSING`; then `INCOMPLETE_METHOD_UNRECORDED`; then `INCOMPLETE_UNDECLARED_FRONTIER`; then `INCOMPLETE_DEPENDENT_ON_PRODUCER`; then `INCOMPLETE_ARTIFACT_UNOBTAINABLE`; then `INCOMPLETE_TRUNCATED`.

The precedence puts role and method failures above artifact unobtainability, because a missing role or method is a defect in how the determination was registered, which is actionable and preventable, while an unobtainable artifact is often simply the passage of time. Reporting the recoverable defect first sends the finding to someone who can act on it.

Precedence never suppresses the other failures: clause P3-7.10 requires all five assessments to be returned alongside the single member, so the precedence orders the headline and hides nothing.

**P3-7.9 (MUST) Outcome derived by the table.** An implementation must derive the outcome member from the five assessments, the frontier set and the truncation state exactly as this section specifies.

**P3-7.10 (MUST) All assessments returned.** An implementation must return every condition assessment alongside the outcome member and must not return the member alone.

**P3-7.11 (MUST) Precedence applied as stated.** An implementation must apply the precedence of this section where more than one condition fails.

**P3-7.12 (MUST) Withheld overrides nothing.** An implementation must return `WITHHELD_IN_PART` in addition to, not instead of, the assessment results for the portion of the chain the reader could traverse.

### 7.3 The reconstruction outcome envelope

Normative in content; serialisation unspecified.

The determination identity and its class. The owning component. The outcome member. The five condition assessments, each with the citations that caused a failure. The frontier set, by kind, with the citation at which each was reached. The truncation state and the bound and point where applicable. The soundness overlay of every determination in the chain, with any open impact records. The count of citations traversed, of pins attempted, of pins obtained, and of pins unobtainable, each with its grain. The count of citations by role and by reliance value. The principal, the purpose and the authorisation reference. The knowledge time of the run. The integrity state of every segment containing an entry in the chain. The statement of the completeness limit required by clause P3-3.116. Whether the run was itself recorded as an entry.

**P3-7.13 (MUST) Envelope completeness.** An implementation must include every element named above in every reconstruction outcome it returns and records.

**P3-7.14 (MUST NOT) No envelope reduction.** An implementation must not omit an envelope element on the ground that a caller does not use it.

**P3-7.15 (MUST) Counts by role and reliance included.** An implementation must include the citation counts by role and by reliance value, so that a reader can see how much of the basis was asserted to have been relied upon.

**P3-7.16 (MUST) Integrity state included.** An implementation must include the integrity state of every segment containing an entry in the chain, so that a reader is not required to make a second request to learn that the record is unverified.

### 7.4 Registration refusals

Refusals of a registering operation are the component's most consequential output, because a refused registration means a determination exists with no record of its basis. They are therefore recorded, counted and reported, not merely returned.

| Code | Cause |
| --- | --- |
| `AUTHORITY_ABSENT` | No `AUTHORITY` citation and no frontier declared in its place |
| `METHOD_ABSENT` | No `METHOD` citation |
| `ROLE_ABSENT` | A citation with no role |
| `RELIANCE_ABSENT` | A citation with no reliance value |
| `PIN_ABSENT` | A citation with no pin |
| `RESOLUTION_OUTCOME_ABSENT` | An `AS_OF` citation with no recorded outcome envelope |
| `SCOPE_ABSENT` | A negative citation with no declared scope |
| `COMPLETENESS_ABSENT` | A negative citation with no completeness value |
| `SELECTION_CRITERION_ABSENT` | An alternative recorded with no criterion |
| `ACCOUNTABLE_PARTY_INVALID` | An accountable party of agent or process kind |
| `DELEGATION_INCOMPLETE` | A delegation chain not terminating in a person or organisation |
| `COMPLETENESS_DECLARATION_ABSENT` | No `basis_complete_declared` value |
| `CLASS_UNREGISTERED` | A determination class not registered by the registrant |
| `REGISTRANT_UNKNOWN` | The registering component is not a registered registrant |
| `SEQUENCE_SUPPLIED` | The caller supplied a sequence value |
| `IDEMPOTENCE_KEY_CONFLICT` | A seen key presented with a different payload |
| `NOT_AUTHORISED` | `Part 7` did not permit the operation |
| `MALFORMED` | The registration was not well formed |

The set is open under section 9.8. Every code is retryable by definition, since the caller can supply what was missing, and the component must say what to supply.

The counting requirement in clause P3-7.19 is the important one. A refusal returns to a caller that may discard it, and the determination then exists with no basis recorded and no trace anywhere that it should have been. Counting refusals by registrant and code is the only signal that a component is making determinations the ledger is rejecting.

**P3-7.17 (MUST) Refusal codes.** An implementation must return one of the codes above, or a registered code, for every refused registration.

**P3-7.18 (MUST) Refusal states what to supply.** An implementation must state, with every refusal, what must be added or corrected for the registration to be accepted.

**P3-7.19 (MUST) Refusals recorded and counted.** An implementation must record every refusal with its code, its registrant and the knowledge time, and must include the counts by registrant and code in the signals of section 8.5.

**P3-7.20 (MUST NOT) No refusal as an outcome of reconstruction.** An implementation must not return a registration refusal code from a reconstruction and must not record a refused registration as a determination.

**P3-7.21 (MUST NOT) No silent acceptance on retry.** An implementation must not accept on a later attempt a registration it refused, unless the later attempt supplies what was missing, and must not accept a registration whose missing element was supplied as a placeholder value.

### 7.5 Reconstruction and read refusals

| Code | Cause | Retryable |
| --- | --- | --- |
| `DETERMINATION_UNKNOWN` | No determination of that identity is held | No |
| `NOT_AUTHORISED` | `Part 7` did not permit the operation | No, without a changed decision |
| `BOUNDS_INVALID` | Requested bounds exceed declared maxima | Yes, within the maxima |
| `PROJECTION_UNKNOWN` | The named projection is not one of section 3.18 | Yes |
| `TIMES_ABSENT` | A temporal projection was requested without both instants | Yes |
| `LEDGER_UNAVAILABLE` | The ledger could not be read | Possibly |

**P3-7.22 (MUST) Read refusal codes.** An implementation must return one of the codes above, or a registered code, for every refused read or traversal.

**P3-7.23 (MUST) Unknown determination distinguished from withheld.** An implementation must return `DETERMINATION_UNKNOWN` only where it holds no such determination, and must return `NOT_AUTHORISED` where it holds one the principal may not see, consistently with `Part 1`'s separation of an absence from a withholding.

**P3-7.24 (MUST NOT) No not found for withheld.** An implementation must not return `DETERMINATION_UNKNOWN` for a determination it holds and is not permitted to disclose.

### 7.6 Outcome obligations

Normative.

| Outcome | Component records | Component emits | Reader must |
| --- | --- | --- | --- |
| `RECONSTRUCTED_COMPLETE` | Run, outcome, access | Reconstruction performed | Not read it as a finding of soundness or correctness |
| `RECONSTRUCTED_TO_FRONTIER` | As above, with frontier kinds | As above | Read the frontier kinds before relying on the result |
| Any incomplete member | As above, with the failing citations | Reconstruction closure failed | Treat the determination as inadequately accounted for |
| Any defective member | As above | The corresponding defect event | Escalate as a defect of the record, not of the determination |
| `WITHHELD_IN_PART` | Run, outcome, principal, decision reference | Reconstruction performed | Not conclude anything about the chain beyond what was traversed |
| Registration `REFUSED` | Refusal, code, registrant | Registration refused | Supply what is missing and re register |
| Read `REFUSED` | Refusal, code, principal | Nothing beyond the refusal | Correct the request or escalate |

**P3-7.25 (MUST) Recording obligations honoured.** An implementation must record everything the table above requires for every outcome it produces.

**P3-7.26 (MUST) Emission obligations honoured.** An implementation must emit every event the table above requires.

**P3-7.27 (MUST) Reader obligations documented.** An implementation must document the reader obligations above and must state that it does not enforce them.

**P3-7.28 (MUST NOT) No adequacy language for an incomplete outcome.** An implementation must not describe a determination as documented, accounted for, evidenced or traceable in any report, projection or interface where the outcome is of the incomplete or defective class.

### 7.7 The three properties, restated as outcomes

The distinction of section 1.1 appears in the taxonomy as follows, and this is the reading a consumer must be given.

An outcome of the closed class establishes **reconstructability** and nothing else. It says the account is adequate. It says nothing about whether what the determination rested on was true.

The **soundness overlay**, returned alongside, addresses whether what it rested on is still believed. It is separate from the outcome because a perfectly closed chain resting on a retracted document is the most dangerous single result this component can produce, and a single combined value would let it be reported as good.

**Correctness** has no outcome, no field and no member, because this component does not assess it. A closed chain, a sound basis and a wrong conclusion are entirely compatible.

**P3-7.29 (MUST) Three properties reported separately.** An implementation must return the closure outcome and the soundness overlay as separate values and must not combine them into a single quality indicator.

**P3-7.30 (MUST NOT) No correctness member.** An implementation must not add an outcome member, field or flag asserting or denying that a conclusion follows from its basis.

**P3-7.31 (MUST) Closed and unsound reportable together.** An implementation must be able to report every determination whose closure outcome is of the closed class and whose soundness overlay is not `SOUND_AS_RECORDED`, and must include the count in the signals of section 8.5.

### 7.8 The one thing this section is for

If a single requirement of this part is to be preserved when the rest is compromised by schedule, it is this one.

**P3-7.32 (MUST) An account that stopped is never an account that closed.** An implementation must not, by any mechanism, configuration, default, aggregation, projection, interface, export or summary, represent a chain that terminated for an undeclared reason, that was truncated, or that reached an artifact it could not obtain, as a chain that was reconstructed.
## 8. Observability and the audit record

### 8.1 The recursion, and where it stops

This component is the audit record of other components. The question of what audits it cannot be answered by another ledger, because that ledger would raise the same question, and a chain of ledgers each auditing the last terminates in an unaudited one or in a cycle.

The recursion is stopped in three places and the stopping is declared rather than hidden.

**Self inclusion at declared depth.** This component's own operations are recorded in its own ledger: registrations, refusals, reconstruction runs, verifications, exports and reads. Those entries are entries like any other and are covered by the integrity machinery. But a read of a read record is not itself recorded, and a reconstruction of a reconstruction run is not itself a reconstruction run. The depth is one, it is declared, and clause P3-8.2 requires the declaration.

**External anchoring for integrity.** The assurance that this component's own entries were not rewritten does not come from within it. It comes from commitments published to a store the implementation does not control, per section 3.17. This is the only assurance in the standard that does not rest on a component of the standard.

**External assessment for conformance.** Whether this component satisfies this part is assessed by `Part 12`, which does not write here, per section 12.12.

An implementation that recorded its own reads recursively would fill its ledger with records of records. An implementation that recorded none of its own operations would be the one component in the estate with no accountability. Depth one with external anchoring is the compromise, and it is worth stating as a compromise rather than as a design.

**P3-8.1 (MUST) Own operations recorded.** An implementation must record its own registrations, refusals, reconstruction runs, integrity verifications, exports and reads as entries in its own ledger.

**P3-8.2 (MUST) Self recording depth declared.** An implementation must declare the depth to which it records operations upon its own records, must not record recursively beyond that depth, and must state the depth in every evidence package.

**P3-8.3 (MUST) Assurance from outside.** An implementation must obtain the assurance that its own entries were not altered from commitments published outside its control and must not present internal recomputation alone as that assurance.

**P3-8.4 (MUST NOT) No self exemption.** An implementation must not exclude its own operations from the integrity machinery of section 3.17.

### 8.2 Grain

| Subject | Grain |
| --- | --- |
| Determination | One entry per determination. Never amended. |
| Citation | One entry per citation, including every `CONTEXT` citation. |
| Negative citation | One entry per asserted absence. |
| Non result acceptance | One entry per non result accepted. |
| Alternative | One entry per candidate not selected. |
| Frontier | One entry per terminus. |
| Attribution | One entry per determination, plus one per delegation step. |
| Basis defect | One entry per defect. |
| Defect impact | One entry per affected citation, not per affected determination. |
| Impact assessment | One entry per assessment act. |
| Subject act | One entry per act, contiguous within the stream. |
| Value node and transformation | One entry each. |
| Registration refusal | One entry per refusal. |
| Reconstruction run | One entry per run, plus one outcome. |
| Integrity verification | One entry per verification, per segment result. |
| Read | One entry per determination, chain, trail, lineage or package returned to a principal. |
| Signal | One entry per signal per observation interval. |

The impact grain is worth stating explicitly. One entry per affected **citation**, not per affected determination, because a determination may rely on a defective artifact more than once in different roles, and the assessments may differ: the same retracted document may have been an authority in one citation and context in another.

**P3-8.5 (MUST) Declared grain.** An implementation must record at the grain of the table above, or declare a finer grain, and must not record at a coarser one.

**P3-8.6 (MUST) Context citations recorded individually.** An implementation must record each `CONTEXT` citation as its own entry and must not record them as a count or a summary.

**P3-8.7 (MUST) Impact at citation grain.** An implementation must record one impact entry per affected citation.

**P3-8.8 (MUST) Counting grain stated with every count.** An implementation must state the grain of every count it reports.

### 8.3 What must be recorded with every registration

Sufficient to reconstruct without the producer. That is the requirement and clause P3-8.11 makes it testable.

Required: the registration request as received, including the idempotence key; the determination and every element of its basis; the resolution outcome envelope for every `AS_OF` citation; the completeness declaration; the registrant identity and the authorisation reference; the basis digest and its canonical form profile; the assigned sequence and knowledge time; and the outcome of every precondition check, including the ones that passed.

Recording the checks that passed is unusual and is required for a specific reason. A registration accepted in 2028 under a set of preconditions, read in 2035 after the preconditions have been strengthened, will look deficient. The record of which checks were applied at the time distinguishes a determination registered under a weaker regime from one that evaded a check.

**P3-8.9 (MUST) Reconstruction sufficiency.** An implementation must record enough with every registration to reconstruct the chain without the producing component, and must treat a determination it cannot so reconstruct as a defect against clause P3-3.82.

**P3-8.10 (MUST) Request recorded as received.** An implementation must record the registration request as received and must not record a normalised form in its place.

**P3-8.11 (MUST) Precondition outcomes recorded, including passes.** An implementation must record the outcome of every precondition check applied at registration, and must record the version of the precondition set applied.

**P3-8.12 (MUST) Periodic reconstruction sampling.** An implementation must reconstruct a declared sample of retained determinations on a declared cycle, must record every outcome that is not of the closed class, and must declare the sample and the cycle.

**P3-8.13 (MUST) Decay recorded, not corrected.** An implementation must record a reconstruction that closed on an earlier run and does not close now as a finding about the record, and must not amend the earlier outcome.

### 8.4 Access records

**P3-8.14 (MUST) Reads recorded.** An implementation must record every return of a determination, a chain, a trail, a lineage, a projection or an evidence package to a principal, with the principal, the subject, the purpose and the knowledge time.

**P3-8.15 (MUST) Withholding recorded.** An implementation must record a read that was refused or reduced by an authorisation decision, with the decision reference, whether or not the requester was told.

**P3-8.16 (MUST) Reverse index queries recorded.** An implementation must record every enumeration of determinations relying on a stated artifact, with the artifact and the principal, since that query reveals more about the estate than any single determination read.

**P3-8.17 (MUST NOT) No unrecorded export.** An implementation must not export an evidence package without recording the export, its recipient and its scope.

**P3-8.18 (SHOULD) Read records retained with the subject.** An implementation should retain the read records of a determination for as long as the determination itself.

### 8.5 Signals

Each signal measures a specific way in which this part's guarantees are hollowed out while every individual operation continues to succeed. That is the criterion for inclusion, and it is why the list is long: this component fails quietly by construction.

| Signal | Grain | Why it matters |
| --- | --- | --- |
| Registration refusals by registrant and code | One refusal | The count of determinations whose basis was never recorded. The single most important signal in the part. |
| Registrants that have ceased registering, by class | One registrant and class | A component that stops registering produces silence, and silence looks like health. |
| Determinations with `basis_complete_declared` false | One determination | The owning component's own admission that it did not supply the whole basis. |
| Citations with `INDETERMINATE` reliance | One citation | A component that cannot say what it relied on has not recorded a basis. |
| Ratio of `CONTEXT` to relied upon citations, by registrant | One citation | A registrant recording everything as context, or nothing as context, is not distinguishing. |
| Frontiers of kind `FRONTIER_UNDECLARED` | One frontier | Chains that stopped for no recorded reason. |
| Frontiers of kind `OPAQUE_COMPONENT` | One frontier | The measure of how much of the estate has no provenance to give. |
| Methods of kind `UNDECLARED` | One determination | Determinations whose reasoning step is unrecorded. |
| Methods of kind `HUMAN_JUDGEMENT`, by class and actor | One determination | Legitimate, and a rising proportion in a class expected to be procedural is a finding. |
| Non result acceptances by disposition | One acceptance | Concentrations of `PROCEEDED_WITHOUT_BASIS` and `PROCEEDED_TREATING_AS_ABSENT`. |
| Negative citations by completeness value | One citation | Absences of unknown or partial completeness relied upon as facts. |
| Negative citations without a pinned query | One citation | Absences that cannot be re established. |
| Delegation steps without an instrument | One step | Authority asserted and not demonstrable. |
| Determinations closed and unsound | One determination | Well documented determinations resting on retracted bases. |
| Impact records in `MATERIALITY_UNASSESSED` beyond a declared age | One impact | Known exposure nobody has looked at. |
| Soundness states of `SOUNDNESS_UNASSESSABLE` | One determination | Exposure that can no longer be settled. |
| Reconstruction outcomes by member, by registrant and class | One run | Where the record is failing and whose it is. |
| Reconstruction decay, being determinations that closed and no longer do | One determination | The evidence base eroding. |
| Truncated reconstructions by bound | One run | Chains too large to assess, which may be the interesting ones. |
| Retrograde citations unexplained | One citation | Either late registration or a defect. |
| Sequence gaps open, and resolved as cause undetermined | One observation | Loss, and unexplained loss. |
| Reconciliation discrepancies by registrant | One reconciliation | Emission not arriving. |
| Segments unanchored beyond the declared interval | One segment | The window in which alteration is undetectable. |
| Anchor verification failures | One segment | Either connectivity or something worse. |
| Pins recorded without a digest, by cited kind | One citation | Erosion of the ability to establish that the obtained artifact is the cited one. |
| Reads with no recorded purpose | One read | Erosion of the access record. |

**P3-8.19 (MUST) Signals produced.** An implementation must produce every signal in the table above at a declared interval and must declare the interval.

**P3-8.20 (MUST) Signals derived from entries.** An implementation must derive every signal from recorded entries and must be able to enumerate the entries behind any signal value.

**P3-8.21 (MUST NOT) No suppression of a signal.** An implementation must not provide a means of disabling, filtering or thresholding a signal in the table above such that a non zero value is reported as zero.

**P3-8.22 (MUST) Refusal signal reaches the registrant's owner.** An implementation must make the registration refusal signal available to the owner of each registrant, since the refusal was returned to a system rather than to a person.

**P3-8.23 (MUST) Cessation signal is a standing measure.** An implementation must produce the cessation signal continuously rather than on demand, since its value depends on absence and nobody will request it.

**P3-8.24 (MUST) Decay trend available.** An implementation must be able to report reconstruction outcomes for the same determination over time, so that erosion is distinguishable from a determination that never closed.

**P3-8.25 (SHOULD) Signal thresholds declared.** An implementation should declare, for each signal, the value at which it requires attention, and should record the declaration as a controlled document under `Part 1`.

### 8.6 The evidence package

Self describing, sufficient to establish what a determination rested on without this component running.

Contents, all required.

The determination in full, with its class, owning component, conclusion reference and digest, clocks, completeness declaration and basis digest.

Every citation with its role, pin, resolution mode, resolution outcome envelope, reliance value and instants. Every `CONTEXT` citation, individually.

Every negative citation with its scope, completeness, result count and pinned query.

The method citation, and the method artifact itself where obtainable, or the statement that it was not.

Every non result acceptance with its envelope, disposition, supporting pin and rationale.

Every alternative considered with its elimination ground.

Every frontier with its kind, justification and external reference.

The attribution, the delegation chain, every instrument or the reason for its absence, and the accountable party.

The content of every cited artifact where obtainable, or the statement that it was not and why, with the knowledge time of the attempt.

The soundness overlay, every basis defect and every impact record with its assessment and assessor.

The reconstruction history of the determination, being every run and its outcome.

The integrity material: the entries' sequence positions, the segments containing them, the commitments, the anchor publications, the receipts, and the procedure by which a reader verifies them.

The coverage statement: which components register determinations of this class, and since when.

The statement of the completeness limit required by clause P3-3.116, and the self recording depth required by clause P3-8.2.

A statement of the version of this part the package claims to conform to.

**P3-8.26 (MUST) Package sufficiency.** An implementation must produce a package sufficient to establish what a determination rested on without the implementation running and without access to any component of this standard other than the package.

**P3-8.27 (MUST) Verification procedure included.** An implementation must include the procedure by which a reader independently verifies the commitments and anchors in the package, in terms that do not require this implementation.

**P3-8.28 (MUST) Limit statements included.** An implementation must include the completeness limit statement and the self recording depth in every package.

**P3-8.29 (MUST) Absence stated, not omitted.** An implementation must state, for every required element it could not include, that it could not be included and why, with the knowledge time of the attempt.

**P3-8.30 (MUST) Package digest.** An implementation must record a digest over a declared canonical form of the package and must include the profile identity.

**P3-8.31 (MUST) Soundness included.** An implementation must include the soundness overlay and every impact record in the package, and must not export a package presenting a closed chain without them.

**P3-8.32 (MUST) Self description.** An implementation must include a description of the package's structure sufficient for a reader with no knowledge of the implementation to locate each required element.

### 8.7 Retention

Retention in this component is harder than in the two before it, because a basis must outlive the obligation of the determination it explains, and this component does not know what that obligation is.

**P3-8.33 (MUST) Retention obtained, not assigned.** An implementation must obtain the retention period of every record it holds from a retention rule expressed under `Part 1` and must not assign one of its own.

**P3-8.34 (MUST) Basis outlives the determination's obligation.** An implementation must retain a determination and its whole basis for at least as long as the record of the act the determination authorised or informed, where that period is known to it, and must record where it is not known.

**P3-8.35 (MUST) Separate retention per structure.** An implementation must permit the retention of a basis, an audit trail and an instance lineage to be set independently, per clause P3-3.8.

**P3-8.36 (MUST) Integrity material outlives the entries it covers.** An implementation must retain the segments, commitments, anchors and verification procedures covering an entry for at least as long as the entry, since an entry whose commitment has been disposed of is unverifiable.

**P3-8.37 (MUST) Disposal recorded and cited.** An implementation must record the disposal of any record it holds with its authorisation reference, must retain the identity of what was disposed of, and must make the disposal citable as a `RETENTION_EXPIRED` frontier.

**P3-8.38 (MUST NOT) No disposal under an open impact record.** An implementation must not dispose of a determination or its basis while an impact record against it is in `MATERIALITY_UNASSESSED`.

**P3-8.39 (MUST NOT) No disposal of a cited basis.** An implementation must not dispose of a determination that is the target of a `PRIOR_DETERMINATION` citation from a retained determination, and must record the citing determination in the refusal.

### 8.8 What cannot be changed

**P3-8.40 (MUST NOT) No amendment of an entry.** An implementation must not modify any recorded entry by any mechanism, including administrative, migration, correction and support mechanisms.

**P3-8.41 (MUST NOT) No amendment of a reconstruction outcome.** An implementation must not modify a recorded reconstruction outcome and must record a differing later result as a further run.

**P3-8.42 (MUST) Migration preserves sequence and digests.** An implementation that migrates its records must preserve every sequence value and every recorded digest unchanged, must record the migration as an entry, and must not recompute a commitment under a different procedure without recording both.

**P3-8.43 (MUST) Own assurance determinations recorded as determinations.** An implementation must record its own reconstruction sampling and integrity verification conclusions as determinations under this part, with their own bases, so that its assurance activity is accountable on the same terms as everything else.
## 9. Extension model

### 9.1 Closed sets, open sets, and why

Four sets in this part are closed.

**The citation role set of section 3.6 is closed.** This is the strongest closure in the part and the one most likely to be resisted, because every registrant will eventually want a role of its own. It is closed because the role is what a consumer branches on: a reader assembling a chain must know, for every edge, whether it was an authority, a premise, an alternative or noise. A registrant that invents a role has produced an edge no reader can classify, and the reader will classify it as an input or discard it. Additional distinction is available through the registered `cited_kind` and through attributes, neither of which changes how an edge is read.

**The closure outcome set of section 7.1 is closed.** A new member obliges every consumer to grow a branch, and the default branch will treat it as adequate.

**The five reconstructability conditions of section 3.13 are closed.** They are the definition of the property. A sixth would change what reconstructable means, and a fifth removed would change it more.

**The three structures of section 3.2 are closed.** A fourth structure is a new component.

Everything else is open under a registry: frontier kinds, method kinds, determination classes, cited kinds, subject act kinds, refusal codes, digest algorithms, canonical form profiles, path schemes, commitment procedures, event types and evaluation purposes.

**P3-9.1 (MUST) Closed sets not extended.** An implementation must not add a member to the citation role set, the closure outcome set, the reconstructability condition set or the structure set.

**P3-9.2 (MUST) Unknown member is a defect, not a default.** An implementation must treat receipt of a role or outcome member outside the closed sets as a defect and must not map it to a member it does recognise.

**P3-9.3 (MUST) Open sets registered.** An implementation must admit a member of an open set only through the registry mechanics of section 9.2 and must not accept an unregistered member at any interface.

**P3-9.4 (MUST) Additional distinction through cited kind.** An implementation must express a registrant's need for a finer distinction than the role set provides through a registered `cited_kind` or a citation attribute, and must not overload a role.

### 9.2 Registry mechanics

Every registry obeys the same rules, stated once.

A registry is content of a controlled document version under `Part 1`, so a registration has an effective date, an approval and an author. Keys are permanent and never reused. A member is deprecated rather than removed, because entries referencing it must remain interpretable, and in this component that period is the longest in the standard. Every registration states what the member means, not only what it is called.

**P3-9.5 (MUST) Registry as controlled document.** An implementation must express every registry as content of a document version under `Part 1` and must resolve the registry version in force at the knowledge time of any entry that references it.

**P3-9.6 (MUST NOT) No key reuse.** An implementation must not reuse a registry key and must not remove a member that any retained entry references.

**P3-9.7 (MUST) Deprecation rather than removal.** An implementation must deprecate a member with an effective date and a reason and must continue to interpret entries referencing it.

**P3-9.8 (MUST) Registry version recorded with the entry.** An implementation must record the registry version in force when an entry referencing a registered member was appended, so that the member's meaning at that time is recoverable.

**P3-9.9 (MUST) Semantics in the entry.** An implementation must not admit a registry entry that does not state the meaning of the member in terms a consumer can act on.

### 9.3 Frontier kind registry

The minimum set of section 3.11 is normative. A registration must state: what condition the kind reports; whether it is legitimate as a permanent terminus or is a defect; whether it is a property of the chain or of the reading; whether it is expected to be closable; and what evidence must accompany a frontier of that kind.

`FRONTIER_UNDECLARED` is registered as a defect and must not be re registered as legitimate. A registry that permits an implementation to declare undeclared frontiers acceptable has removed the only distinction section 3.11 exists to draw.

**P3-9.10 (MUST) Legitimacy declared per kind.** An implementation must record, for every registered frontier kind, whether it is a legitimate permanent terminus, and must not register `FRONTIER_UNDECLARED` as legitimate.

**P3-9.11 (MUST) Chain or reading declared.** An implementation must record whether each frontier kind is a property of the chain or of the reading, and must record a reading frontier against the run, per clause P3-3.71.

**P3-9.12 (MUST) Required evidence declared.** An implementation must state, for every frontier kind, what evidence must accompany it, and must refuse a frontier lacking it.

**P3-9.13 (MUST NOT) No new kind to avoid a defect.** An implementation must not register a frontier kind whose effect is to reclassify an undeclared terminus, an unobtainable artifact or a truncation as a legitimate frontier.

### 9.4 Path scheme registry

A path scheme addresses a position within a cited artifact. A registration states the syntax, what a path denotes, and whether a path remains valid across changes to the artifact.

Stability matters more here than in `Part 2`, because a citation's locator must still denote the same position decades later. A positional path into a document that has been reflowed denotes different text, and a citation whose locator has drifted is worse than one with no locator, because it points confidently at the wrong thing.

**P3-9.14 (MUST) Stability declared.** An implementation must declare, for every registered path scheme, whether a path in it remains valid across changes to the artifact, and must record the scheme with every path.

**P3-9.15 (SHOULD) Stable schemes preferred for citations.** An implementation should record citation locators in a scheme declared stable, and should record both a stable and a positional path where only the positional one is available.

**P3-9.16 (MUST NOT) No cross scheme comparison.** An implementation must not compare, deduplicate or match paths recorded in different schemes.

**P3-9.17 (MUST) Clause identifier scheme supported.** An implementation must support the clause identifier scheme of `Part 1`, since an authority citation must address a clause rather than a document.

### 9.5 Method kind registry

The minimum kinds of section 3.8 are normative. A registration must state: whether a method of the kind is pinnable; whether it is deterministic, or that determinism is declared per instance; what the pin must identify; whether the kind constitutes a frontier; and which component owns the artifact the pin identifies.

**P3-9.18 (MUST) Pinnability declared.** An implementation must record whether each method kind is pinnable and must refuse a method citation of a pinnable kind without a pin.

**P3-9.19 (MUST) Frontier status declared.** An implementation must record whether each method kind constitutes a frontier and must record the corresponding frontier where it does.

**P3-9.20 (MUST) Owning component declared.** An implementation must record which component owns the artifact a method pin of each kind identifies.

**P3-9.21 (MUST NOT) No procedural kind for judgement.** An implementation must not register a method kind that permits a conclusion reached by human judgement to be recorded as a pinnable procedure.

### 9.6 Determination class registry

A class is what makes a determination findable and is what a coverage statement is expressed over. A registration must state: what kind of conclusion the class covers; which component owns it; which citation roles are mandatory for the class beyond the universal mandates of section 3.6; what the expected method kinds are; and the retention basis.

Per class mandatory roles are the useful part. A disposition authorisation must cite a negative premise about holds. A price determination must cite the reference data version. Encoding those as class level mandates turns a governance expectation into a registration precondition, which is the only place it will be enforced.

**P3-9.22 (MUST) Class mandates declared and enforced.** An implementation must record the citation roles mandatory for each determination class beyond the universal mandates and must refuse a registration of that class lacking one.

**P3-9.23 (MUST) Owning component per class.** An implementation must record which component owns each class and must refuse a registration of a class from a component that does not own it.

**P3-9.24 (MUST) Expected method kinds declared.** An implementation must record the expected method kinds for each class and must be able to report determinations whose method kind is outside the expected set.

**P3-9.25 (MUST) Retention basis per class.** An implementation must record the retention basis for each class, per section 8.7.

### 9.7 Digest, canonical form and commitment procedure registries

Digests appear over conclusions, subject states, bases, values, packages and segments. Three things must be registered separately: the algorithm, the canonical form profile, and the commitment procedure by which a segment digest is computed from entry digests.

The commitment procedure is registered separately because it is the one a reader must reproduce decades later without the implementation. A commitment computed by an undocumented construction is unverifiable, which makes the integrity machinery decorative.

**P3-9.26 (MUST) Three registries separate.** An implementation must register digest algorithms, canonical form profiles and commitment procedures separately and must record all three where all three apply.

**P3-9.27 (MUST) Commitment procedure fully specified.** An implementation must record, for every registered commitment procedure, a specification sufficient for an independent party to recompute a commitment from the entries and their digests.

**P3-9.28 (MUST) Deprecation without invalidation.** An implementation must be able to deprecate a digest algorithm or commitment procedure without invalidating any recorded commitment, and must record an additional commitment under a current procedure rather than replacing the original.

**P3-9.29 (MUST NOT) No digest without a profile.** An implementation must not record a digest whose canonical form profile is not recorded.

### 9.8 Code and event registries

**P3-9.30 (MUST) Refusal codes registered with remedy.** An implementation must state, in every refusal code registration, what must be supplied or corrected.

**P3-9.31 (MUST) Event types registered.** An implementation must register every event type it emits beyond the minimum set of section 4.7.

**P3-9.32 (MUST) Cited kinds registered with their owner.** An implementation must register every `cited_kind` together with the component that owns artifacts of that kind and the pin form required.

### 9.9 Composition of determinations

Three compositions are distinguished and confusing them produces specific defects.

**A determination citing a prior determination.** Reliance rather than re derivation. Permitted, pinned, and the mechanism by which a defect propagates transitively under section 6.7. This is the only composition the model provides for reasoning.

**A determination bundling several determinations.** A composite determination whose conclusion is that a set of sub determinations were made, for example a batch authorisation. Permitted, and it must cite each member as a `PRIOR_DETERMINATION` rather than summarising them, because a composite that records only a count cannot be traversed to the members.

**A determination whose basis is another determination's basis.** Prohibited. A determination that cites the basis of another determination without citing the determination itself has copied a reasoning chain without recording that it did so, and the two then diverge silently when a defect is found against one.

There is a fourth thing that resembles composition and is not: two determinations citing the same artifact. That is not composition and requires nothing beyond both citations existing, and it is the ordinary case that makes the reverse index of section 3.18 valuable.

**P3-9.33 (MUST) Prior determination cited by identity.** An implementation must record reliance on an earlier determination as a citation of role `PRIOR_DETERMINATION` to that determination's identity.

**P3-9.34 (MUST) Composite cites its members.** An implementation must require a composite determination to cite each member determination individually and must refuse one that records a count or a range in place of the members.

**P3-9.35 (MUST NOT) No basis borrowing.** An implementation must refuse a determination that cites the citations of another determination without citing that determination.

**P3-9.36 (MUST) Composite depth bounded and declared.** An implementation must declare the maximum nesting depth of composite determinations it accepts and must refuse a registration exceeding it.

**P3-9.37 (MUST NOT) No cyclic citation.** An implementation must refuse a registration whose `PRIOR_DETERMINATION` citations would create a cycle in the determination graph.
## 10. Standards and specifications

### 10.1 How the citations in this part are to be read

Every entry states what the source supplies, the edition established as current at the date of this part, and whether this part's account rests on specification text or on secondary sources. Section 13.1 lists the sources not obtained.

Currency was established from publisher status pages rather than inferred. Two findings bear directly on how a reader should treat this section. The most relevant recent development, the publication of the SCITT architecture as an RFC, post dates the author's general knowledge and was established by search. And the most widely cited national guidance on log management is nineteen years old with a revision that has been in draft for nearly three years.

**P3-10.1 (MUST) Cited edition recorded.** An implementation must record the edition or version of every external standard it relies upon and must not cite a standard without its edition.

**P3-10.2 (MUST) Basis marked.** An implementation must record, for every control it adopts from a source named in this section, whether the basis is specification text or practice.

### 10.2 Provenance modelling: the W3C PROV family

| Document | Status established | Supplies |
| --- | --- | --- |
| PROV-DM, the PROV Data Model | W3C Recommendation, 30 April 2013. No successor found. | Entity, Activity and Agent as the three node types. The relations `used`, `wasGeneratedBy`, `wasDerivedFrom`, `wasInformedBy`, `wasAttributedTo`, `wasAssociatedWith` and `actedOnBehalfOf`. Association as a ternary relation between an activity, an agent and a **plan**. Bundles, being named sets of provenance descriptions which are themselves entities, so that provenance of provenance is expressible. |
| PROV-O, the PROV Ontology | W3C Recommendation, 30 April 2013. | An OWL 2 mapping of PROV-DM to RDF. |
| PROV-N | W3C Recommendation, 30 April 2013. | A notation for provenance aimed at human readers. |
| PROV-CONSTRAINTS | W3C Recommendation, 30 April 2013. | Constraints defining a valid PROV instance. |
| PROV-SEM, PROV-OVERVIEW, PROV-PRIMER, PROV-AQ, PROV-XML, PROV-DICTIONARY, PROV-LINKS | W3C Notes, 2013. | Model theoretic semantics, guidance, access and query, serialisations, and extensions. PROV-SEM establishes that valid instances correspond to satisfiable first order theories. |

The PROV Working Group's work is complete. The family remains the only broadly adopted general model of provenance and this part borrows from it deliberately in three places: the delegation relation of section 3.12 is `actedOnBehalfOf`; the method citation of section 3.8 is the plan of an Association; and the recursion treatment of section 8.1 is the bundle idea used at depth one rather than indefinitely.

Where this part departs from PROV, it departs on purpose, and the departures are enumerated in section 10.7 rather than glossed. The account above rests on specification text for PROV-DM and on the family overview for the remainder.

### 10.3 Transparency and integrity of append only records

| Specification | Status established | Supplies |
| --- | --- | --- |
| RFC 9943, An Architecture for Trustworthy and Transparent Digital Supply Chains | RFC, June 2026, from the IETF SCITT working group. The document passed through at least twenty two working group draft revisions. | Issuer, Signed Statement, Transparency Service, append only ledger, Receipt and Auditor. Registration as a notarisation, in which a service confirms a policy is met before recording. The ledger as a linear and irrevocable history of statements. A generic, content agnostic paradigm, contrasted in the document with the artifact specific approach of Certificate Transparency. Cryptographic agility through COSE. A threat model in which issuers and transparency services may both be compromised and which does not require trust in a single centralised service. |
| RFC 9162, Certificate Transparency version 2.0 | RFC, 2021. | Merkle tree logs with inclusion and consistency proofs, for one artifact class. |
| RFC 4998 and RFC 6283 | RFCs. | Evidence record syntax for long term integrity, cited in `Part 1` section 10 and applicable unchanged here. |
| RFC 3161 | RFC. | Trusted timestamping of a digest. |

The receipt of section 2.1 and the anchoring of section 3.17 both follow RFC 9943's shape. This part diverges in one respect worth naming: SCITT's transparency service confirms a registration policy before recording, whereas this component's registration preconditions in section 4.2 are about the completeness of a basis rather than about the authority of an issuer. Both are registration policies; they police different things.

An individual Internet Draft in the SCITT space, cited here as an observation and not as a normative source, states the completeness limit of section 3.17 explicitly in the context of logged refusals: such a mechanism provides auditability of what was logged and not proof that nothing unlogged occurred. The observation is independently derivable from RFC 9943's threat model, and the draft is cited because it states it in one sentence.

### 10.4 Digital evidence and investigation

| Standard | Status established | Supplies |
| --- | --- | --- |
| ISO/IEC 27037:2012 | Current edition. Reviewed and confirmed in 2018 and under review again. Adopted in Europe as EN ISO/IEC 27037:2017. | Identification, collection, acquisition and preservation of digital evidence. The Digital Evidence First Responder and Digital Evidence Specialist roles. Four quality principles: **auditability, repeatability, reproducibility and justifiability**. |
| ISO/IEC 27041 | Published. | Assurance that an investigative method is suitable and adequate, through validation and verification. |
| ISO/IEC 27042:2015 | Published. | Analysis and interpretation of digital evidence. Static, dynamic and real time analysis, each required to be documented so that an independent analyst can reproduce it. |
| ISO/IEC 27043 | Published. Due for periodic review in 2025 and reported as likely to be confirmed unchanged. | Incident investigation principles and processes, framing the other three. |
| ISO 21043 series | Published. | The forensic process generally, drawing an explicit boundary with ISO/IEC 27037 for data held on storage media. |

The four principles of ISO/IEC 27037 are the closest thing in any reviewed standard to a definition of what this part calls reconstructability, and section 3.13 states the mapping and the divergence explicitly. The distinction that standard draws between repeatability, being the same result under the same conditions, and reproducibility, being the same result by a different party under different conditions, is the distinction this standard draws between `Part 2`'s reproduction of a verdict and this part's condition five. It is a better vocabulary than the one in common use and it is adopted here.

The account of the four principles and of ISO/IEC 27042's reproduction requirement rests on secondary sources. None of the four standards was obtained in full text.

### 10.5 Records, preservation and regulated audit trails

| Standard | Status | Relevance here |
| --- | --- | --- |
| ISO 14721:2025, the OAIS reference model | Third edition. Cancels the 2012 edition. Established in `Part 1`. | Preservation Description Information includes Provenance Information as one of its categories, which makes a basis a preservation concern rather than only an operational one. |
| PREMIS 3.0 | 2015. Established in `Part 1`. | Events, agents and their linkage, and fixity as a property with verification as an event. |
| ISO 15489-1:2016 | Current, confirmed 2021. Established in `Part 1`. | The record as evidence, which is the property this component holds about determinations. |
| 21 CFR Part 11, clause 11.10(e) | Substantially unchanged since 1997. Established in `Part 1`. | The computer generated, time stamped audit trail requirement, and the prohibition on obscuring previously recorded information. |
| EU GMP Annex 11 | Revision draft published 7 July 2025; consultation closed 7 October 2025; not finalised as at the date of this part. Established in `Part 1`. | Audit trail expectations, and a draft Annex 22 on artificial intelligence in the same package that may bear on the agent attribution position of section 3.12. |

The regulated audit trail requirements are cited because they are the reason many organisations will read this part, and because they specify considerably less than this part does. They require that changes be recorded and not obscured. They do not require that a determination record what it rested on, and none of them contains anything resembling the role taxonomy of section 3.6.

### 10.6 Log management, and a caution

| Publication | Status established | Note |
| --- | --- | --- |
| NIST SP 800-92, Guide to Computer Security Log Management | Final, September 2006. Still the current final publication. | The most widely cited guidance on log management. |
| NIST SP 800-92 Revision 1, Cybersecurity Log Management Planning Guide | Initial public draft, 11 October 2023. Comment period closed 29 November 2023. Still a draft as at the project page's November 2025 update. | Narrower than what it replaces: its scope is planning only, and it explicitly excludes implementing log management technology and making use of log data. |
| RFC 5424 | RFC. | The syslog protocol, cited only to be excluded. |

Two cautions follow, and both matter to how this part should be read.

The generally cited guidance is nineteen years old and its replacement has been in draft for nearly three years and is narrower in scope. An organisation citing NIST log management guidance in an architecture document is citing either a 2006 publication or a draft, and should say which.

More importantly, log management and provenance are different problems that share a vocabulary. Everything in SP 800-92 concerns the generation, transmission, storage, access and disposal of records of events. None of it concerns what a determination rested on. A programme that implements log management well has not thereby implemented this part, and the belief that it has is the most common reason a component like this one is never built. Section 11.1 names the mechanism.

### 10.7 Supporting specifications

| Specification | Used for |
| --- | --- |
| RFC 2119 and RFC 8174 | Requirement keywords. |
| BCP 47 | Language tags. |
| RFC 3339 and ISO 8601 | Instant representation for the three clocks. |
| RFC 8785 | An example of a canonical form profile of the kind section 9.7 requires. |
| RFC 9457 | A model for conveying a refusal of the kind section 7.4 and section 7.5 specify. |
| CloudEvents | A model for the event envelope of section 4.7. |
| COSE | The signature and envelope format RFC 9943 relies upon, relevant to attestations and receipts. |

The following clauses rest on practice rather than specification text and are collected so a reader can see the set: clause P3-3.38 on declared completeness of a search; clause P3-3.51 on the prohibition of method inference; clause P3-3.73 on recording expected closability; clause P3-4.33 on detecting cessation of registration; clause P3-6.29 on a deterministic primary budget; clause P3-8.11 on recording precondition passes; clause P3-8.12 on periodic reconstruction sampling; and clause P3-9.22 on class level mandatory roles.

**P3-10.3 (MUST) Practice basis recorded.** An implementation that adopts a clause listed in the paragraph above as a control must record that its basis is practice.

### 10.8 Named conflicts

Five conflicts and tensions bear on this part. None is resolved by averaging.

**Whether a use is a reliance.** W3C PROV-DM provides `used`, an undifferentiated relation between an activity and an entity. It carries no notion of whether the activity's outcome depended on the entity. The distinction is not expressible without an extension, and PROV's own approach to uncertainty is through attributes rather than through the relation. **Position taken.** Reliance is a first class property of every citation, admitting three values, per section 3.5, and `CONTEXT` is a distinct role. This is the largest single departure from PROV in the part.

**Whether provenance has a notion of absence.** No reviewed model provides one. PROV has no relation expressing that an activity relied on the non existence of an entity, and nothing in the evidence standards addresses the completeness of a search. **Position taken.** Negative citations are first class and carry a scope and a completeness value, per section 3.7.

**Whether a chain has declared ends.** No reviewed model provides a frontier. PROV chains simply stop where the recorded descriptions stop, and PROV-CONSTRAINTS says nothing about a terminus. The evidence standards address chain of custody, which is a different chain. **Position taken.** Every terminus is a declared frontier of a registered kind, and an undeclared terminus is a defect, per section 3.11.

**Whether an integrity mechanism speaks to completeness.** RFC 9943 is careful: its threat model addresses authenticity and transparency of registered statements and does not claim that registration is exhaustive. Practice is much less careful, and append only ledgers are routinely presented as complete records. **Position taken.** The limit is stated as a requirement rather than left to a reader's inference, per clauses P3-3.116 and P3-3.117, and it is repeated in every verification result and every evidence package.

**Whether accountability may terminate in software.** PROV's `actedOnBehalfOf` imposes no constraint on the terminus of a delegation chain, and nothing in the reviewed standards requires it to be a person or an organisation. **Position taken.** It must, per clause P3-3.75, on the same reasoning `Part 1` gives for signature and `Part 2` for the correspondence claim. Section 13.6 records this as a position rather than a finding and states the argument against it.

### 10.9 What none of the standards supplies

Twelve requirements in this part have no source in any reviewed standard. They are listed so a reader can hold the inventions to a higher standard of scrutiny than the parts with a citation.

The distinction between reliance and availability, and the recording of what was available and unused.

The closed citation role taxonomy, and in particular the roles for a rejected alternative, an accepted non result and a delegation.

The recording of a non result accepted, with its disposition, which is where the hidden decisions of a whole estate become visible.

Negative citations with a declared scope and completeness.

The frontier as a declared, kinded, justified terminus, and the treatment of an undeclared terminus as a defect.

The five conditions of reconstructability as a testable definition, and their separate reporting.

The distinction between reconstructable, sound and correct, and the refusal to assess the third.

Basis defect propagation: the enumeration of every determination that relied on an artifact later found defective, and the separation of that enumeration from any judgement of materiality.

The requirement that a materiality assessment be a named person's act rather than a computation.

The separation of a basis, an audit trail and an instance lineage as three structures with independent retention.

The requirement that a completeness limit statement accompany every verification result and every evidence package.

The detection of a registrant that has ceased registering, which is the only signal that reveals the most consequential failure available to this component.

**P3-10.4 (MUST) Unsourced requirements identified.** An implementation must be able to state, for any control it implements under this part, whether the requirement has a cited source in this section or is listed in section 10.9 as unsourced.
## 11. Anti patterns

Each entry names the mechanism by which the failure occurs, states the consequence, and marks whether the prohibition rests on specification text or on practice.

### 11.1 The log that was going to be the ledger

**Mechanism.** The organisation has application logs, so the provenance requirement is satisfied by retaining them longer. The logs record what happened, at the grain of a function call, in a volume that makes retention unaffordable and search impractical, and they contain no roles, no reliance, no pins and no methods.

**Consequence.** The requirement is closed on paper and nothing is reconstructable. This is the single most common reason a component of this kind is never built, and the belief survives because the logs do contain, somewhere, most of the facts, so any individual question can be answered at sufficient expense by a person who was there.

**Basis.** Specification text, in that NIST SP 800-92's scope is the management of records of events and contains nothing about what a determination rested on.

**P3-11.1 (MUST NOT) No telemetry as a basis.** An implementation must not accept operational logs, traces or metrics into the ledger, and must not construct a basis from them, per clauses P3-1.9 and P3-3.100.

### 11.2 The input list

**Mechanism.** The determining component records everything it read as inputs. Forty fields, three documents, eleven reference values, undifferentiated.

**Consequence.** A reader cannot tell which four mattered. The record is technically complete and epistemically empty, and it is worse than a short record because its completeness is mistaken for rigour. It also makes defect propagation useless: a defect in any of the fifty five artifacts flags the determination, so every propagation returns everything.

**Basis.** Specification text, in that PROV's undifferentiated `used` relation is the model most implementations follow.

**P3-11.2 (MUST NOT) No undifferentiated input list.** An implementation must require a role and a reliance value on every citation and must refuse a registration supplying a list of artifacts without them, per clauses P3-3.20 and P3-3.24.

### 11.3 The chain that trails off

**Mechanism.** Citations are recorded until the recording stops. There is no declaration that the chain ended, so a chain that reached a statute and a chain whose instrumentation was never finished look identical.

**Consequence.** Nobody can distinguish a complete account from an abandoned one, so no assurance activity can be defined over the record. The population of chains cannot be triaged, because triage requires knowing which ones are supposed to stop where they stop.

**Basis.** Practice. No reviewed model provides a frontier.

**P3-11.3 (MUST NOT) No undeclared terminus.** An implementation must record a frontier at every terminus and must treat an undeclared one as a defect, per clauses P3-3.65 and P3-3.68.

### 11.4 The verified empty ledger

**Mechanism.** The ledger's integrity machinery is sound: entries hash chained, segments committed, anchors published, receipts verifiable. Half the components never register anything. Every verification passes.

**Consequence.** The organisation has cryptographic proof that its incomplete record is unaltered, and presents it as evidence that its determinations are accounted for. This is the failure the completeness limit of section 3.17 exists to prevent and it is close to universal in append only systems.

**Basis.** Specification text, in that RFC 9943's threat model addresses authenticity and transparency of registered statements and claims nothing about the exhaustiveness of registration.

**P3-11.4 (MUST NOT) No completeness claim from integrity.** An implementation must state the completeness limit with every verification result and every package, and must not permit an interface to imply completeness, per clauses P3-3.116 and P3-3.117.

### 11.5 The registrant that went quiet

**Mechanism.** A component stops registering determinations, because of a deployment, a configuration change, a failed dependency or a decision nobody recorded. No error is raised. The ledger continues to serve the determinations it already holds and every report about them looks healthy.

**Consequence.** Coverage decays silently and is discovered when someone asks about a determination from the affected period and finds nothing. By then the period is long and the reason is unrecoverable.

**Basis.** Practice.

**P3-11.5 (MUST NOT) No undetected cessation.** An implementation must detect and emit the cessation of registration by a registrant within a declared interval, per clause P3-4.33, and must produce the signal continuously, per clause P3-8.23.

### 11.6 The inferred completeness

**Mechanism.** The ledger checks that every citation it holds resolves, finds that they all do, and reports the basis as complete.

**Consequence.** A basis missing its most important citation passes, because the check can only examine what is present. The report is true about what it examined and false about what it claims.

**Basis.** Practice.

**P3-11.6 (MUST NOT) No inferred completeness.** An implementation must require the owning component to declare completeness and must not represent a basis as complete on the strength of its own checks, per clauses P3-3.16 and P3-3.17.

### 11.7 The default that nobody wrote down

**Mechanism.** A determination receives an indeterminate verdict or an unavailable input and proceeds on a value hard coded in the consuming component. The value is a business rule, it has no authority, no version and no approval, and it appears nowhere in the record.

**Consequence.** The determination rests on something that is not in its basis and is not anywhere else either. `Part 1` and `Part 2` both go to considerable lengths to surface non results to the caller, and this is where all of that work is discarded.

**Basis.** Practice, and it is the specific gap `Part 2` section 13.14 hands to `Part 0`.

**P3-11.7 (MUST NOT) No unrecorded proceeding.** An implementation must require a `non_result_acceptance` with a declared disposition and a pinned default for every non result a determination proceeded despite, per section 3.9.

### 11.8 Withheld recorded as absent

**Mechanism.** A search runs under the searcher's permissions, finds nothing in the part of the scope it can see, and records an absence. The record says no matching records exist.

**Consequence.** A determination rests on a fact that was manufactured by an access decision. This is the third appearance of this mechanism in the standard, after `Part 1`'s withheld outcome and `Part 2`'s withheld path code, and it appears three times because it is the most reliable way to produce a confident false statement in a system of this kind.

**Basis.** Practice.

**P3-11.8 (MUST NOT) No withheld as complete.** An implementation must record `PARTIAL_WITHHELD` where any part of a negative citation's scope was not visible to the searcher, per clause P3-3.40.

### 11.9 The method that was a judgement

**Mechanism.** A conclusion reached by a person weighing considerations is recorded as having followed a procedure, because a procedure exists and the person had read it.

**Consequence.** An investigation concludes that the procedure was followed when it was not consulted, or that it was defective when it was never applied. The record is false in the specific way that makes a review reach the wrong finding about a control.

**Basis.** Specification text, in that ISO/IEC 27042 requires an analysis process to be documented sufficiently for independent reproduction, which a judgement recorded as a procedure defeats.

**P3-11.9 (MUST NOT) No judgement as procedure.** An implementation must record `HUMAN_JUDGEMENT` with a narrative and a named actor wherever the conclusion was not produced by a pinnable method, per clause P3-3.48.

### 11.10 The winner only selection

**Mechanism.** A determination that chose among candidates records the chosen one. The alternatives are not recorded, because they were not part of the outcome.

**Consequence.** A reader cannot tell that a choice occurred, so cannot ask whether the criterion was right or whether an option was overlooked. The determination reads as a computation.

**Basis.** Practice.

**P3-11.10 (MUST NOT) No selection without alternatives.** An implementation must refuse a determination whose owning component reports a selection and supplies no alternatives, per clause P3-3.63.

### 11.11 Provenance by pointer to a live system

**Mechanism.** Citations are recorded as references the originating component can dereference: an internal surrogate key, a session scoped handle, an endpoint path. They work perfectly for years.

**Consequence.** The chain is reconstructable exactly as long as that component runs, which is not the period over which the question will be asked. The failure is invisible until the component is decommissioned, at which point every determination that cited it becomes unreconstructable simultaneously.

**Basis.** Practice.

**P3-11.11 (MUST NOT) No producer dependent pin.** An implementation must record pins dereferenceable without a running instance of the producing component and must report `INCOMPLETE_DEPENDENT_ON_PRODUCER` where one is not, per clauses P3-3.85 and section 7.1.

### 11.12 The determination that was edited

**Mechanism.** A basis is found to be missing a citation, so the citation is added. Or a reliance value is found to be wrong, so it is corrected. The record now says what it should have said.

**Consequence.** The record no longer says what the component actually recorded at the time, which is the only thing it was ever able to attest. A basis that can be improved retrospectively cannot be evidence of anything, and the improvement is indistinguishable from a fabrication.

**Basis.** Specification text, in that 21 CFR Part 11 clause 11.10(e) prohibits obscuring previously recorded information.

**P3-11.12 (MUST NOT) No basis amendment.** An implementation must not add, remove or alter a citation of a recorded determination and must record a correction as a further determination, per clauses P3-3.12 and P3-5.4.

### 11.13 The reasoning reconstructed by replay

**Mechanism.** Asked to explain a determination, the system re runs it against current rules, current reference data and current state, and presents the result as the explanation.

**Consequence.** The explanation is of a different determination. Where the two agree it is reassuring and worthless; where they disagree it looks like a defect in the original. Both parts that feed this one prohibit it explicitly, `Part 2` in its section 12.3 reciprocal and `Part 1` in requiring the resolution outcome rather than a re resolution.

**Basis.** Specification text.

**P3-11.13 (MUST NOT) No replay as explanation.** An implementation must construct every explanation from the records it holds and must not recompute, re evaluate or re resolve anything, per clauses P3-1.5 and P3-4.16.

### 11.14 The single quality score

**Mechanism.** The closure outcome, the soundness overlay and the integrity state are combined into one indicator: a colour, a grade, a percentage.

**Consequence.** A closed chain resting on a retracted authority scores the same as an incomplete chain resting on a sound one, and the two require opposite responses. Whichever way the combination is weighted, the most dangerous case in the part becomes invisible.

**Basis.** Practice.

**P3-11.14 (MUST NOT) No combined indicator.** An implementation must return the closure outcome and the soundness overlay separately and must not combine them, per clause P3-7.29.

### 11.15 The unassessed impact queue

**Mechanism.** Defect propagation works. It enumerates four thousand affected determinations, each with an impact record in `MATERIALITY_UNASSESSED`. Nobody assesses them, because assessment requires judgement and there are four thousand.

**Consequence.** The organisation now knows precisely how exposed it is and has converted that knowledge into a backlog. Within two quarters the backlog is large enough that its existence is the reason nobody looks at it.

**Basis.** Practice. The remedy is a signal and a triage order rather than a prohibition, because the enumeration is correct behaviour.

**P3-11.15 (SHOULD) Impact queue aged and ordered.** An implementation should report unassessed impact records by age and partitioned by the reliance value of the affected citation, so that the ones asserted to have been relied upon are assessable first, per clause P3-6.36.

### 11.16 The materiality computed

**Mechanism.** Faced with the queue of section 11.15, the component assesses materiality itself, by re deriving the determination with the corrected artifact and comparing.

**Consequence.** It has performed a new determination and presented it as an assessment of an old one, using rules, reference data and code that have all moved. Where the comparison shows no difference it certifies soundness it has not established.

**Basis.** Practice.

**P3-11.16 (MUST NOT) No computed materiality.** An implementation must not assess materiality itself and must record `MATERIALITY_UNASSESSED` until a named actor assesses it, per clauses P3-3.90 and P3-5.10.

### 11.17 The context that was everything

**Mechanism.** A registrant discovers that recording reliance is difficult, so it records every citation as `CONTEXT` and one as `INPUT`. Or the converse: everything is `INPUT` and nothing is context.

**Consequence.** The distinction the role set exists to draw is present in form and absent in substance. This is the failure mode of a mandatory field nobody can populate honestly, and the only defence is a signal on the ratio rather than a rule.

**Basis.** Practice.

**P3-11.17 (SHOULD) Reliance ratio monitored per registrant.** An implementation should report the ratio of context to relied upon citations by registrant, so that a registrant not distinguishing is visible, per section 8.5.

### 11.18 The trail ordered by timestamp

**Mechanism.** The audit trail is ordered by an event timestamp drawn from the emitting host. Clocks disagree by milliseconds or by hours.

**Consequence.** The trail silently reorders itself, and the reordering is worst during the incidents when the order matters most, because that is when hosts are restarting and clocks are resyncing. A trail whose order is not stable is not a trail.

**Basis.** Practice.

**P3-11.18 (MUST NOT) No timestamp ordering.** An implementation must order every trail by a sequence it assigns and must not order one by any timestamp, per clause P3-3.96.

### 11.19 The gap that was explained away

**Mechanism.** A sequence gap is detected and closed as a known issue, a retry artefact or a benign allocation, without the allocation record being cited.

**Consequence.** The one mechanism that detects loss is disarmed by the operational convenience of clearing an alert. After a year the gap register is empty and its emptiness is presented as evidence of completeness.

**Basis.** Practice.

**P3-11.19 (MUST NOT) No gap dismissal.** An implementation must not close a gap observation without one of the recorded resolutions, must require the allocation record where a benign allocation is claimed, and must count undetermined causes, per clauses P3-5.20 to P3-5.22.

### 11.20 The anchor to itself

**Mechanism.** Commitments are published to a store the organisation operates: another database, another region, another account. It is described as external.

**Consequence.** An actor able to rewrite the ledger is very likely able to rewrite the anchor, so the anchor establishes nothing against the threat it exists for. The construction is sound and the independence is fictional.

**Basis.** Specification text, in that RFC 9943's threat model contemplates a compromised transparency service and does not assume a single trusted one.

**P3-11.20 (MUST NOT) No self anchoring.** An implementation must refuse to record an anchor publication to a store under its own control and must record how independence was established, per clause P3-4.11.

### 11.21 Accountability terminating in software

**Mechanism.** An automated agent makes a determination. The attribution records the agent as both the actor and the accountable party, because the agent is what acted and no person was involved.

**Consequence.** The record states that nobody is answerable. Every other part of the standard has by then taken care to keep a person in the chain, and this is where the care is undone, because it is the one component where recording the truth about an automated act feels like sufficient rigour.

**Basis.** Practice. PROV imposes no such constraint; see section 13.6.

**P3-11.21 (MUST NOT) No agent as accountable party.** An implementation must refuse an attribution whose accountable party is of agent or process kind, per clause P3-3.75.

### 11.22 The delegation inferred from a role

**Mechanism.** The delegation chain is generated from the organisational hierarchy or from the access grant that permitted the act. It is always complete and always plausible.

**Consequence.** The chain records who could have authorised the act rather than who did, and the two diverge exactly where an investigation cares. An inferred chain is also always present, which removes the signal that would have shown that no delegation existed.

**Basis.** Practice.

**P3-11.22 (MUST NOT) No inferred delegation.** An implementation must not infer a delegation step from a role, a hierarchy or an access grant, per clause P3-3.79.

### 11.23 The basis borrowed

**Mechanism.** A determination that reaches the same conclusion as an earlier one on similar facts cites the earlier determination's citations rather than the earlier determination.

**Consequence.** Two determinations share a reasoning chain and neither records that they do. A defect found against the shared basis propagates to one and not the other, and the reverse index returns an incomplete answer to the only question this component exists to answer.

**Basis.** Practice.

**P3-11.23 (MUST NOT) No basis borrowing.** An implementation must refuse a determination citing the citations of another determination without citing that determination, per clause P3-9.35.

### 11.24 The summary at the boundary

**Mechanism.** A determination cites an evaluation report by recording its violation count, or cites a document resolution by recording the version identifier. The full envelope is large and the summary is what the consuming code needed.

**Consequence.** Every distinction the producing component maintained is discarded at the citation: the vacuity flags, the indeterminate verdicts, the resolution basis, the divergence flag. Both `Part 1` and `Part 2` require the whole envelope specifically to prevent this, and it is prevented only at this boundary.

**Basis.** Specification text, in `Part 1` clause P1-12.6 and `Part 2` clause P2-12.6.

**P3-11.24 (MUST NOT) No summary as a citation.** An implementation must record the whole outcome envelope a resolving component returned and must refuse a citation supplying a count, an identifier or an aggregate in its place, per clause P3-3.21.

### 11.25 The reverse index nobody built

**Mechanism.** Bases are recorded faithfully and only forward traversal is implemented, because forward traversal is what an explanation needs and the reverse direction is expensive to index.

**Consequence.** The question the component exists to answer cannot be asked. On the morning a document is found to have been wrong, the organisation has a perfect record of every determination and no way to find the ones affected. Nobody discovers the omission until that morning.

**Basis.** Practice.

**P3-11.25 (MUST NOT) No forward only traversal.** An implementation must provide the reverse enumeration of determinations relying on an artifact, with a declared latency, per clauses P3-3.124 and P3-4.17.

### 11.26 The ledger that became the system of record

**Mechanism.** The ledger holds copies of everything it cites, because a citation to something that might be deleted is fragile and copying is cheap. Over time components begin reading from the ledger rather than from the owner.

**Consequence.** There are now two answers to every question and the ledger's copy has no lifecycle, no approval and no effectivity. The component that was supposed to record what others determined has become a competing authority, and the divergence between its copy and the original is undetectable because nobody compares them.

**Basis.** Specification text, in that `Part 1` section 12.3 names this absorption directly.

**P3-11.26 (MUST NOT) No authoritative copies.** An implementation must record cited artifacts by identity, version and digest and must not hold or serve a copy as authoritative, per clauses P3-3.15 and P3-3.102.
## 12. Boundaries with other parts

Each subsection states four things: what this component delegates, what it must not absorb, the naive design that conflates the two, and the reciprocal declaration the other part must make. Subsection numbers correspond to part numbers, so section 12.7 states the boundary with `Part 7` and section 12.14 states the boundary with `Part 0`. Section 12.3 is deliberately unused, since it would designate this part. Numbers are permanent.

A boundary is reciprocal. If this part declares that it delegates something, the receiving part must declare that it owns it, in the same terms.

This section carries more weight here than in the two prior parts, for a structural reason. Every component in the standard registers determinations with this one, so this part has thirteen live boundaries rather than one or two, and the failure mode is not that a boundary is crossed but that this component becomes the place everything is kept.

**P3-12.1 (MUST) Declared allocation.** An implementation must be able to state, for every capability named in this section as delegated, which component provides it, and must not provide it within this component.

**P3-12.2 (MUST) Recording rather than substitution.** Where a delegated capability is unavailable, an implementation must record the unavailability against a knowledge time and must not substitute a local implementation of it, per clause P3-4.28.

**P3-12.3 (MUST NOT) No reaching past a neighbour.** An implementation must not read or write the internal state of another component named in this section and must interact with it only through that component's declared interface.

### 12.1 Boundary with Part 1, controlled documents and records

This subsection is the reciprocal declaration `Part 1` clause P1-12.6 and section 12.3 of that part require.

**Delegated.** What was in force at an application time. Document and record identity, version, status, effectivity, supersession, retraction and citability. Clause level locator resolution. The retention rules that govern this component's own records. The controlled documents that carry this component's registries.

**Must not absorb.** The determination of what governed. This component records the resolution outcome another component obtained; it never resolves.

**Naive conflation.** Two forms. This component caches resolution results and begins answering what was in force, at which point there are two answers and the second has no effectivity model behind it. Or `Part 1` takes over the basis, treating a determination as a document with citations, at which point the basis acquires a version lifecycle it should not have, since a basis is a historical fact and not a revisable artifact.

**Reciprocal.** This part declares that it does not determine what was in force, that it obtains that by citation resolution against `Part 1`, and that it records the resolution outcome including its basis and divergence flag rather than the version identifier alone. That is the declaration `Part 1` requires and clauses P3-12.4 and P3-12.5 make it binding.

**P3-12.4 (MUST) Resolution outcome recorded, never re resolved.** An implementation must record the whole resolution outcome envelope `Part 1` returned for every `AS_OF` citation, including its basis and divergence flag, and must not resolve or re resolve a citation itself, per clauses P3-3.21 and P3-6.27.

**P3-12.5 (MUST NOT) No force state held or asserted.** An implementation must not hold, cache beyond a declared validity period, or assert what was in force at any application time.

**P3-12.6 (MUST) Retraction accepted as a basis defect.** An implementation must accept a retraction, withdrawal or divergence report from `Part 1` as a basis defect and must enumerate its impact, per section 3.14.

### 12.2 Boundary with Part 2, business rules and constraint evaluation

This subsection is the reciprocal declaration `Part 2` clause P2-12.6 requires.

**Delegated.** The evaluation of constraints, the verdict taxonomy, the vacuity flag, the evaluation report and its pin set, the explanation of a verdict, and the drift observations that arise when a rule's authority changes.

**Must not absorb.** Evaluation. A verdict is cited, never recomputed. An explanation of a verdict is obtained from `Part 2`'s explanation operation, never assembled by re running the rule.

**Naive conflation.** This component records the evaluation report as a summary, because the report is large. Every distinction `Part 2` maintains is then lost at the citation, per section 11.24.

**Reciprocal.** This part declares that it records the whole evaluation report and its pin set rather than a summary, that it does not re evaluate a rule in order to explain a determination, and that it obtains an explanation from `Part 2`'s explanation operation. Clauses P3-12.7 and P3-12.8 make it binding.

**P3-12.7 (MUST) Whole report recorded.** An implementation must record the whole evaluation report of `Part 2` section 3.17, including its pin set, as the cited artifact, and must refuse a citation supplying a count, a pass indicator or an aggregate.

**P3-12.8 (MUST NOT) No re evaluation.** An implementation must not evaluate or re evaluate a rule and must obtain any explanation of a verdict from `Part 2`.

**P3-12.9 (MUST) Drift accepted as a basis defect.** An implementation must accept a `Part 2` drift observation of a kind affecting a rule relied upon as a basis defect and must enumerate its impact.

### 12.4 Boundary with Part 4, metadata and model repository

**Delegated.** Term and definition identity and versioning. Design level lineage: the assertion that a field derives from other fields by a declared transformation, and the impact analysis of changing a definition.

**Must not absorb.** Design lineage. This component records instance lineage, being what actually happened to actual values.

**Naive conflation.** The two lineages merged. Either this component asserts design relations, at which point the design has two masters, or `Part 4` records instance level transformations, at which point a design repository acquires a volume and a retention obligation it was not built for. The merge is attractive because the two structures look identical, and it destroys the most valuable thing either produces, which is the divergence between them.

**Position taken.** `Part 4` owns lineage as a design fact; this component owns lineage as a historical fact. Section 13.4 records that the boundary is contestable, since a sufficiently detailed design lineage and a sufficiently aggregated instance lineage meet in the middle.

**Reciprocal.** `Part 4` must declare that it owns definition and design lineage identity, that it does not record instance level transformations, and that it exposes design lineage assertions obtainable by pin so that clause P3-3.105 can be satisfied.

**P3-12.10 (MUST) Design lineage cited, not asserted.** An implementation must record the corresponding `Part 4` design lineage assertion where one exists and must not assert, correct or version one.

**P3-12.11 (MUST) Divergence reportable.** An implementation must be able to report every transformation whose positions are not related by any `Part 4` assertion, per clause P3-3.107.

### 12.5 Boundary with Part 5, decision engine

**Delegated.** Selection. Which of several candidate outcomes applies, the criterion by which the choice was made, the resolution of conflicts between authorities, and the artifacts in which criteria are declared and versioned.

**Must not absorb.** Selection, and specifically the temptation to reconstruct which candidate should have been chosen. This component records the alternatives and the criterion as reported; it does not evaluate the criterion against the alternatives.

**Naive conflation.** This component acquires the ability to say whether the right candidate was chosen, which is an assessment of correctness that clause P3-1.3 forbids. Or `Part 5` records only its chosen outcome, and section 11.10 follows.

**Reciprocal.** `Part 5` must declare that it reports every candidate it considered and the criterion it applied, that its criteria are declared and versioned artifacts obtainable by pin, and that it does not record determinations of its own outside this component.

**P3-12.12 (MUST) Alternatives and criterion recorded as reported.** An implementation must record every candidate `Part 5` reports as considered and the criterion it applied, and must refuse a determination reporting a selection with no alternatives, per clause P3-3.63.

**P3-12.13 (MUST NOT) No assessment of the selection.** An implementation must not evaluate a selection criterion against recorded alternatives and must not assert that a different candidate should have been selected.

### 12.6 Boundary with Part 6, workflow and process orchestration

**Delegated.** Control flow: the sequencing of activities, the assignment and escalation of work, the state of a process instance, retries and compensations.

**Must not absorb.** Process state. A process step is not a reason, and a determination's basis is not the sequence of steps that preceded it.

**Naive conflation.** The process history is registered as the basis. A determination made at the end of a nine step process is recorded as citing the nine steps, none of which is an authority, a premise or a method. The record is voluminous and reconstructs nothing.

**Reciprocal.** `Part 6` must declare that it does not own bases, that a process step is registered as a subject act rather than as a citation where it is registered at all, and that its own retention does not govern the retention of the bases of determinations made within it.

**P3-12.14 (MUST) Process steps are acts, not citations.** An implementation must record a process step as a `subject_act` in a trail where it is recorded at all, and must not record one as a citation in a basis.

**P3-12.15 (MUST NOT) No process identity required.** An implementation must not require a process instance identifier in order to register, traverse or read anything specified in this part.

### 12.7 Boundary with Part 7, policy decision point and authorisation

**Delegated.** Every authorisation decision: whether a principal may register a determination, traverse a chain, read a basis, run the reverse enumeration, or export a package. The identification of withheld scope in a search, which arrives here as the `PARTIAL_WITHHELD` completeness value. The validity of a delegation.

**Must not absorb.** Policy. This component records decision references and supplies its own records as attributes.

**Naive conflation.** This component evaluates whether a delegation was valid, because it holds the chain and the instruments. Validity is a policy question with an effective date and a scope, and answering it here creates a second authorisation authority whose answers nobody governs.

**Reciprocal.** `Part 7` must declare that it owns policy evaluation and delegation validity, that it identifies withheld scope to this component as withheld rather than removing it, and that it does not record determinations outside this component.

**P3-12.16 (MUST) Decisions consumed, not made.** An implementation must record the `AUTHREF` of every authorisation decision that permitted an operation and must not evaluate policy.

**P3-12.17 (MUST NOT) No delegation validation.** An implementation must record a delegation chain as asserted and must not assess whether a delegation was valid or in force.

**P3-12.18 (MUST) Withheld scope identified as withheld.** An implementation must require that scope removed from a search by an authorisation decision be identified as withheld and must record `PARTIAL_WITHHELD` accordingly, per clause P3-3.40.

### 12.8 Boundary with Part 8, human task and case management

**Delegated.** The work a person does: assessing a basis defect's materiality, investigating a gap, closing a reconstruction finding, and the case in which that work sits.

**Must not absorb.** Assessment work management. This component records that an assessment was made, by whom and with what reason; it does not manage the assessing.

**Naive conflation.** The impact record and the task are one entity, so closing the task closes the impact record, and an exposure disposed of with a task is an exposure nobody assessed.

**Reciprocal.** `Part 8` must declare that closing a task does not alter an impact record, a soundness state or a gap observation, and that every assessment is effected by a registering operation here whose outcome the task records.

**P3-12.19 (MUST) Assessments recorded independently of tasks.** An implementation must retain every impact assessment, gap resolution and soundness transition unchanged after any task concerning it is disposed of.

**P3-12.20 (MUST NOT) No task driven closure.** An implementation must not provide a means by which a task completion transitions a soundness state, closes an impact record or resolves a gap observation without a recorded assessment naming an actor.

### 12.9 Boundary with Part 9, schema and contract registry

**Delegated.** Schema identity and versioning, and the compatibility rules between schema versions, including the schemas of the event envelopes and registration payloads this component accepts.

**Must not absorb.** Schema validation. This component records the schema reference a payload claims and does not validate against it.

**Naive conflation.** This component validates registration payloads against a cached schema, so that two components disagree about whether a registration was well formed, and a malformed registration is refused for a reason `Part 9` would not give.

**Reciprocal.** `Part 9` must declare that it owns schema identity and compatibility and that it exposes schema versions obtainable by pin.

**P3-12.21 (MUST) Schema reference recorded, not evaluated.** An implementation must record the schema identity and version a registration payload claims and must not validate content against it, and must express a structural refusal as `MALFORMED` without asserting a schema outcome.

### 12.10 Boundary with Part 10, reference and master data management

**Delegated.** Code lists, reference sets and their versioning and retention, including the reference sets cited as premises by determinations.

**Must not absorb.** Vocabulary governance. This component pins a reference set version as cited and does not hold, extend or correct one.

**Naive conflation.** The ledger holds a copy of the reference set version cited, because retaining it guarantees the citation resolves. Section 11.26 follows.

**Reciprocal.** `Part 10` must declare that it retains every superseded reference set version for at least as long as the longest retained determination citing it, that it does not remove or reuse member keys, and that it reports a correction to a reference set as a basis defect to this component.

**P3-12.22 (MUST) Reference sets cited, not held.** An implementation must cite a reference set by identity, version and digest and must not hold or serve a copy as authoritative.

**P3-12.23 (MUST) Reference correction accepted as a defect.** An implementation must accept a `Part 10` report that a reference set version was corrected as a basis defect and must enumerate its impact.

### 12.11 Boundary with Part 11, content addressed artifact store

**Delegated.** The durable storage and retrieval by digest of the octets of anything this component cites or exports, including evidence packages.

**Must not absorb.** Storage semantics. This component owns the mapping from a citation to a digest and a canonical form profile.

**Naive conflation.** The store holds the ledger, because both are append only and content addressed. The ledger's sequence, its segments and its commitments are then properties of a store that has no notion of them, and integrity verification becomes a property of the store's implementation rather than of a pinned procedure.

**Reciprocal.** `Part 11` must declare that it holds no sequence, no commitment and no ledger state, that it does not delete content on its own authority, and that it treats a deletion request as an instruction accompanied by a disposition authorisation reference.

**P3-12.24 (MUST) Digest is the interface.** An implementation must address stored content by digest under a declared canonical form profile and must not rely on a location or path as identity.

**P3-12.25 (MUST NOT) No ledger state in the store.** An implementation must not hold sequence values, segments, commitments or anchors in the artifact store and must not accept them from it.

### 12.12 Boundary with Part 12, conformance and assurance harness

**Delegated.** All assessment of whether an implementation satisfies this part, including the verification of this component's own reconstruction sampling and integrity verification.

**Must not absorb.** Self assessment. This component performs the sampling of clause P3-8.12 and the verification of section 6.8 and records their results as determinations under clause P3-8.43; it does not assess itself against this part.

**Naive conflation.** This component's own sampling results are presented as conformance evidence, which is the condition in which nobody discovers that the sample excluded the difficult chains. It is a particularly acute risk here, because this component is the one everybody else's assurance depends on, so its self report is the most likely to be accepted without challenge.

**Reciprocal.** `Part 12` must declare that it obtains the clause set from this part by resolution, that it records the version of this part an assessment was made against, that it does not write to this ledger while assessing it, and that it independently verifies commitments against published anchors rather than accepting this component's verification results.

**P3-12.26 (MUST) Read only assessment.** An implementation must expose everything `Part 12` requires through read operations and must not require a write in order to be assessed.

**P3-12.27 (MUST NOT) No self assessment as assessment.** An implementation must not present its own sampling, verification or reconciliation results as an assessment of conformance, per clause P3-1.13.

**P3-12.28 (MUST) Independent verification supported.** An implementation must expose the entries, digests, commitment procedures and anchor references necessary for `Part 12` to verify integrity without relying on this component's own verification results.

### 12.13 Boundary with Part 13, model invocation and agent execution

**Delegated.** The invocation record of a model: what it was asked, what it returned, its cost, its retries, its non determinism, and the identity and version of the model.

**Must not absorb.** Invocation. This component cites an invocation record as a method pin or a premise and never invokes anything.

**Naive conflation.** A model output is recorded as a premise without the invocation record, so that the basis says the determination relied on a value and cannot say where the value came from or that it was not reproducible. The determination then appears better founded than it is, because a model output recorded as a plain premise is indistinguishable from a measured fact.

**Position taken.** Where a model produced a value a determination relied upon, the basis must cite the `Part 13` invocation record and not the value alone, and the method citation must record that the method is not deterministic. Where an agent made the determination, the attribution records the agent as the actor and the delegation chain must reach a person or an organisation, per section 3.12.

**Reciprocal.** `Part 13` must declare that it owns the invocation record, that it does not register determinations of its own, that it exposes an invocation record obtainable by pin with its own identity and digest, and that it reports a model found defective as a basis defect to this component.

**P3-12.29 (MUST) Invocation record cited, not the value alone.** An implementation must require a citation to the `Part 13` invocation record wherever a determination relied upon a model output and must refuse a determination citing the output without it.

**P3-12.30 (MUST) Non determinism recorded.** An implementation must record the method as not deterministic wherever a model inference contributed to the conclusion, per clause P3-3.46.

**P3-12.31 (MUST) Model defect accepted as a basis defect.** An implementation must accept a `Part 13` report that a model version was defective as a basis defect of kind `MODEL_DEFECTIVE` and must enumerate its impact.

### 12.14 Boundary with Part 0, system composition

**Delegated.** What happens when all the components run at once: authority over facts more than one component touches, the seams at which values cross boundaries, the propagation of non results, consistency and ordering across components, and pinning across a unit of work spanning several components.

**Must not absorb.** Composition. This part states what it records and what it refuses, and does not state what a component must do when it cannot supply a basis.

**Reciprocal.** `Part 0` must declare that this component holds authority over determination records, bases, citations, frontiers, closure outcomes, soundness overlays, trails, instance lineage and the ledger's integrity state, and that no other component holds any of them. It must state, for every seam, what must hold and how a violation appears here. It must in particular resolve five questions this part hands it.

What a component must do when it cannot supply a basis satisfying the preconditions of section 4.2, given that the alternative to registering is no record at all.

How the registration obligation is imposed on every component, given that this part can refuse a bad registration and cannot compel a missing one.

What happens when this component's record of a determination and the owning component's own record of it disagree, which is the question `Part 2` section 13.14 also hands forward.

How a single unit of work spanning several components produces one determination rather than several, or several with a declared relation, so that a chain is not fragmented across component boundaries.

Whether the pattern this standard repeats, that the governed thing has a lifecycle and the derived belief about it does not, or here that the record has none and the assertions about it do, should be stated once for the whole standard rather than three times.

**P3-12.32 (MUST) Authority declared, not assumed.** An implementation must not accept an assertion about a determination record, a basis, a closure outcome, a soundness state or the ledger's integrity state from another component, and must require that such facts be established by its own operations.

**P3-12.33 (MUST) Refusal is visible to composition.** An implementation must make every registration refusal and every cessation of registration available as a signal to the owner of the registrant, since neither can be remedied within this component, per clauses P3-8.22 and P3-8.23.
## 13. What could not be established

A question recorded as open can be closed by someone with access to the source. A question closed by inference cannot be reopened, because nothing in the document reveals that an inference was made.

### 13.1 Sources not obtained in full text

The following were not available in full text. This part's account of each rests on published status pages, catalogue entries, scope statements, forewords and secondary literature. No clause reproduces text from any of them.

**ISO/IEC 27037:2012.** The four quality principles of auditability, repeatability, reproducibility and justifiability, the DEFR and DES roles, and the currency and review status were obtained from secondary sources. The clause text was not obtained. Section 3.13 maps its five conditions onto these four principles and section 10.4 states the mapping, so the mapping should be checked against the standard before approval. The distinction between repeatability and reproducibility, which this part adopts as vocabulary, is the item most worth verifying.

**ISO/IEC 27041, ISO/IEC 27042:2015 and ISO/IEC 27043.** Scope statements obtained. The requirement attributed to ISO/IEC 27042, that an analysis process be documented sufficiently for an independent analyst to reproduce it, rests on a secondary source and is the basis of section 3.8 and of section 11.9. It should be verified. The periodic review status of ISO/IEC 27043 was reported as pending confirmation and was not established from the ISO catalogue directly.

**ISO 21043 series.** Noted as drawing a boundary with ISO/IEC 27037 for data on storage media, from a secondary source. Not assessed. It may bear on the physical observation frontier of section 3.11 and was not examined for that.

**RFC 9943.** Established as published in June 2026 with its title, working group and core concepts, from the RFC datatracker and from working group draft revisions. The full RFC text was not obtained. The account of its threat model, its receipt mechanism and its contrast with Certificate Transparency rests on draft text and on the datatracker summary, and the difference between the final RFC and the late drafts was not established. Sections 2.1, 3.17 and 10.3 depend on this. This is the most recent and most load bearing source in the part and it warrants direct verification.

**W3C PROV-DM and PROV-O.** PROV-DM was obtained in substance, including the core structures, the ternary Association with a plan, and the bundle concept. PROV-CONSTRAINTS and PROV-SEM were not obtained beyond their abstracts; the claim in section 10.2 that valid instances correspond to satisfiable theories rests on the PROV-SEM abstract. No successor to the 2013 family was found and the absence of a successor was established from the family's own document listing rather than from a W3C working group status page.

**NIST SP 800-92 and SP 800-92r1.** Status established directly from the publisher's project page and publication records. The r1 scope narrowing was established from the draft's own abstract. The full text of neither was obtained.

**21 CFR Part 11 and EU GMP Annex 11.** Carried forward from `Part 1` section 13.1 unchanged, with the same limitations.

Not obtained and not assessed at all: ISO/IEC 27050 on electronic discovery, which may bear on the retention and export requirements of sections 8.6 and 8.7; the in toto attestation framework and SLSA, which are the practice standards for supply chain provenance and may have a better treatment of frontiers than anything found here; and C2PA content credentials, which is the most active current work on provenance of a specific artifact class and was not examined for transferable structure.

**P3-13.1 (MUST) Verification before approval.** An implementation or reviewer must verify the claims listed in section 13.1 against the source standards before this part is approved and must record the outcome of each verification against this section.

### 13.2 Whether reliance can be honestly recorded

Section 3.5 makes reliance a required property of every citation and admits `INDETERMINATE` because a component often cannot recover its own dependency structure. This is the weakest point in the part, and it is weak in a way that the vacuity problem is weak in `Part 2`: the mechanism is right and its population depends on something the specification cannot compel.

A determining component that reads a record and uses four of forty fields knows which four only if it was written to know. Most were not. The honest answer is then `INDETERMINATE` on all forty, and section 8.5 counts that, and counting it does not fix it. The failure predicted in section 11.17 is not a defect an implementation can be required away from.

**Open.** Whether a stronger mechanism exists. Three were considered and none pursued. Instrumented dependency capture, where the reading of a field is recorded by the runtime rather than declared by the developer, which is technically achievable and captures reads rather than reliance, so it produces the input list of section 11.2 with better provenance. Counterfactual testing, where the component re runs with a field perturbed and records whether the conclusion changed, which is expensive, is a form of the replay this part prohibits, and is only sound for deterministic methods. And requiring the method artifact to declare its inputs, which works where the method is a rule set or an expression and fails exactly where reliance is hardest to establish, namely human judgement.

A reviewer who believes one of these should be required should say so. Section 3.6's role taxonomy is the substance of the part and reliance is the property that makes it more than a typed edge list.

### 13.3 What counts as a determination

Section 2.1 defines a determination as a conclusion that had reasons and whose owning component is accountable for having made it, and then declines to say which acts qualify, delegating the judgement to the owning component through the class registry of section 9.6.

This is an evasion and it is load bearing. A component that classifies few acts as determinations has a small, tidy, high quality ledger and no coverage. One that classifies many has coverage and a volume that makes assessment impractical. Nothing in this part constrains the choice, and the coverage projection of section 3.18 reports what was chosen without evaluating it.

**Open.** Whether a criterion exists. The candidate worth examining is that an act is a determination if a person could later be required to explain why it was taken, which is the right test and is not mechanically checkable and depends on a regulatory environment the standard does not know. A weaker and checkable candidate is that an act is a determination if it consumed a verdict, a resolution outcome or a selection, which is objective and misses every judgement made without machine input.

### 13.4 The boundary between design lineage and instance lineage

Section 12.4 allocates design lineage to `Part 4` and instance lineage here, on the ground that one is a statement about the design and the other about history. The test works at the extremes and not in the middle.

A design lineage assertion that carries conditions, so that a field derives from one source or another depending on a value, is approaching instance lineage. An instance lineage aggregated to a daily grain, so that a column derives from a column on a date, is approaching design lineage. Real systems hold both, at both grains, and the boundary is drawn where the tooling happens to sit rather than where the concepts divide.

**Open.** Whether a principled criterion exists, or whether this too is a governance allocation to be declared per organisation. This part behaves as though the second is true, which is the same evasion section 13.3 records, and the two may have one answer.

### 13.5 Whether the completeness limit can be improved upon

Section 3.17 states that no integrity mechanism can establish that everything which should have been recorded was recorded, offers three mitigations, and describes none as a solution. The statement is correct and it may be less final than it sounds.

**Open.** Whether a construction exists that makes non registration detectable rather than merely improbable. Two directions were considered and neither pursued. Mandatory receipts as a precondition of the determining act, where a component cannot complete a determination without holding a receipt from this component, which moves the failure from silent non registration to a visible refusal to act, at the cost of making every determination depend on this component's availability. And cross registration, where a determination's receipt is itself cited by the next determination in a chain, so that a missing registration breaks a chain that another party is checking, which works only where determinations are chained and does not help isolated ones.

The first is worth serious examination and was not examined here. It would change the component from a recorder to a participant, which is a substantial architectural shift and would need `Part 0` to arbitrate.

### 13.6 Whether accountability may terminate in software

Clause P3-3.75 refuses an attribution whose accountable party is an automated agent. This is the third appearance of the same position in the standard, after `Part 1`'s refusal of an agent signature and `Part 2`'s refusal of an agent correspondence claim, and it rests on the same argument: accountability is a relation to a party that can bear it.

The argument is not derived from any cited requirement. Nothing in PROV constrains the terminus of a delegation chain, and no reviewed standard requires it to be a person or an organisation.

The counter argument is stronger here than in the two prior parts. An agent operating under a recorded delegation, with an invocation record, a pinned model version and an accountable owner, produces a more complete record of an act than a person who approves without reading. Refusing to let the chain terminate in the agent does not make anyone more accountable; it requires a name to be recorded, and the name recorded may be of someone who did not know the determination was being made.

**Open.** Whether the requirement should instead be that a delegation chain terminate in a party who has accepted the delegation by a recorded act, which is a stronger requirement than the present one and would exclude the nominal accountability the present clause permits. The draft revision of EU GMP Annex 11 and its associated draft Annex 22 on artificial intelligence, neither finalised as at the date of this part, may bear on this and were not examined for it.

### 13.7 Whether the role set is right

Section 3.6's thirteen roles are closed, and closure is the strongest commitment in the part. Two doubts are worth recording.

The first is whether thirteen is too many. `CONTEXT` is essential and the four highlighted in that section are essential. `DERIVED_INTERMEDIATE` may be an implementation detail of a method rather than a distinct kind of reliance, and `INPUT` and `PREMISE` may be one role: the distinction intended is between a value consumed by a computation and a fact relied upon as true, and the distinction is real and may be unpopulatable in the same way reliance is.

The second is whether a role is missing. A determination that relied on an assumption, being neither a premise established by evidence nor an axiom accepted by policy, has no role of its own, and assumptions are extremely common in real reasoning. They are presently recorded as `PREMISE` with a frontier of kind `AXIOM` or `ATTESTED`, which works and may be a workaround rather than a design.

**Open.** Both. A reviewer should test the set against a sample of real determinations from at least three classes before the closure is accepted, because closing the set is the decision hardest to reverse.

### 13.8 Whether soundness assessment scales

Section 3.14 and section 6.7 produce, from one basis defect, an impact record per affected citation, and section 11.15 predicts what happens next. The prediction is that the queue becomes the reason nobody looks at the queue.

Nothing in this part addresses it beyond the ageing signal of clause P3-11.15 and the reliance partition of clause P3-6.36. Both are triage aids and neither reduces the work.

**Open.** Whether a defect can be assessed at the class level rather than the determination level, so that one assessment covers every determination of a class that relied on the artifact in the same role. This is plainly what an organisation would do in practice and it is not expressible in the model, which requires an assessment per impact record. Admitting a class level assessment would reduce the work by orders of magnitude and would permit exactly the kind of blanket judgement that the per determination requirement exists to prevent. Which risk is worse was not determined.

### 13.9 The cost of the model

No performance, scale, storage or latency requirement is stated anywhere in this part, and the requirements have evident cost.

One entry per citation including every `CONTEXT` citation, at the grain of section 8.2, over every determination in an estate, is the largest data volume the standard requires anywhere. The reverse index of clause P3-3.124 must span it. The retention of clause P3-8.34 must outlive the obligations of everything it explains, which in a regulated setting is decades. And clause P3-8.36 requires the integrity material to outlive the entries.

**Open.** Whether the model is affordable at the grain specified, and if not, which requirement should give way. The candidates are the individual recording of `CONTEXT` citations, which is the largest volume and the least often read, and the per citation impact grain of clause P3-8.7. Both were specified at the finer grain on the principle that the coarser grain destroys a distinction, and neither was costed.

### 13.10 What this part deliberately did not attempt

No conformance assessment of any system was performed or anticipated, per clause P3-1.13.

No mechanism is specified by which a component is compelled to register. This part can refuse a defective registration and cannot compel a missing one, and the whole value of the component depends on registration happening. Section 12.14 hands this to `Part 0` and it is the largest single dependency this part has on another.

No treatment is given of provenance crossing an organisational boundary. A determination that relied on a counterparty's assertion records a frontier of kind `EXTERNAL_AUTHORITY` or `ATTESTED` and stops. Whether two organisations' ledgers can be linked, and what a receipt from another organisation's transparency service would mean here, was not examined, although RFC 9943's federation concerns are directly relevant and section 13.1 records that the RFC was not obtained in full.

No privacy treatment is given. A basis routinely contains personal data, a reverse index over an artifact reveals who made determinations about whom, and the access records of section 8.4 are themselves sensitive. The retention requirements of section 8.7 are in tension with erasure obligations in the same way `Part 1` section 13.2 records for records retention, and that tension is not addressed here at all. This is a substantive gap.

No treatment is given of bases at very high volume determination rates, such as a determination per transaction in a high frequency system. Everything in this part assumes a determination is a considered act.

**P3-13.2 (MUST) Gaps declared, not filled.** An implementation must not represent a matter listed in section 13.10 as specified by this part.

**P3-13.3 (SHOULD) Open questions carried forward.** A reviewer of this part should record a position on each open question in section 13, and where a position is adopted it should be recorded in the review outcome rather than by silent amendment of the clause it affects.

### 13.11 Questions handed to Part 0 rather than answered here

Each was identified while authoring this part.

How the obligation to register a determination is imposed, given that this part can refuse a defective registration and cannot compel a missing one.

What a component must do when it cannot satisfy the registration preconditions of section 4.2, given that the alternative to registering is no record at all.

What happens when this component's record of a determination and the owning component's own record disagree, which `Part 2` section 13.14 also hands forward.

How a unit of work spanning several components yields one determination, or several with a declared relation, so that a chain is not fragmented at component boundaries.

What a component must do with each indeterminacy subclass of `Part 2` section 7.2 and each non result subclass of `Part 1` section 7.2, and how the disposition it chose reaches the `non_result_acceptance` record of section 3.9.

Whether the structural pattern this standard has now repeated three times, that the governed record does not transition and the assertions about it do, should be stated once for the whole standard.

Which component holds authority over actor identity, since three parts now treat it as opaque and this one requires a delegation chain over it.

Whether the erasure and retention tension recorded in `Part 1` section 13.2 and in section 13.10 here has one answer for the whole standard or three different ones.
