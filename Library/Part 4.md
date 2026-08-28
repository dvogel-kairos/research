# KAIROS STD 003 Part 4: Metadata and Model Repository

**Standard.** KAIROS STD 003, the enterprise architecture standard.
**Part.** Part 4 of 14 (Part 0 and Parts 1 through 13). Cited as `KAIROS STD 003 Part 4`.
**Title.** Metadata and model repository.
**Version.** 1.0.0.
**Status.** Proposed. This part has not been approved and is not effective. It is issued for review against the authoring brief of 2026-08-17.
**Date of issue.** 2026-08-18.
**Supersedes.** Nothing. This is the first version.

## Binding of requirement language

The key words MUST, MUST NOT, SHOULD, SHOULD NOT and MAY in this part are to be interpreted as described in RFC 2119 and RFC 8174, and only in the upper case forms. This part does not use SHALL, SHALL NOT, REQUIRED, RECOMMENDED, NOT RECOMMENDED or OPTIONAL as requirement keywords.

Every requirement in this part is a numbered clause. A clause identifier has the form `P4-S.N`, where `S` is the section number and `N` is the ordinal of the clause within that section. Clause identifiers are permanent. A clause that is later removed has its identifier retired and never reissued. A clause that is later added to a section takes the next unused ordinal in that section, so ordinals are stable but not contiguous over the life of the part.

Text that is not a numbered clause is not binding. Narrative, tables, graphs, examples and the discussion of standards are provided to make the clauses intelligible and testable, and where a table carries normative content a clause says so explicitly and names the table.

Two words in the title of this part are ambiguous and section 1.4 states which sense each carries. A reader who assumes the other sense of either will misread the whole part.

## Conformance

An implementation conforms to this part if it satisfies every MUST and MUST NOT clause and records, for each SHOULD and SHOULD NOT clause it does not satisfy, the reason. This part does not define conformance levels, profiles or a certification scheme, and it does not define the method of assessment. Assessment method is the subject of `KAIROS STD 003 Part 12` and is out of scope here.

Where a clause states that a value is an implementation decision, conformance requires that the implementation declare the value, not that it adopt a particular one. An undeclared implementation decision is a nonconformity.

## Clause index

The index below is generated from the clause text of this document. It lists every clause identifier, its modality and its subject label. The counts that follow the index are derived by the same extraction and are stated with the grain at which they were counted.

| Clause | Modality | Subject |
| --- | --- | --- |
| **Section 1** | | **Scope and responsibilities** |
| `P4-1.1` | MUST | Purpose satisfaction |
| `P4-1.2` | MUST | Definitions as structured data |
| `P4-1.3` | MUST NOT | No meaning change under an identifier |
| `P4-1.4` | MUST | Change kind declared |
| `P4-1.5` | MUST | Impact spans dependents, not only lineage |
| `P4-1.6` | MUST NOT | No approval |
| `P4-1.7` | MUST NOT | No executable constraint in a definition |
| `P4-1.8` | MUST NOT | No instance lineage |
| `P4-1.9` | MUST | Lineage assertions are attributed |
| `P4-1.10` | MUST NOT | No update in place |
| `P4-1.11` | MUST NOT | No absorption of neighbouring responsibilities |
| `P4-1.12` | SHOULD | Declared exclusions |
| `P4-1.13` | MUST NOT | No conformance self assertion |
| `P4-1.14` | MUST | Time horizon declaration |
| `P4-1.15` | MUST | Metadata sense declared |
| `P4-1.16` | MUST | Both model senses distinguished |
| `P4-1.17` | MUST NOT | No inferential model internals |
| **Section 2** | | **Terminology** |
| `P4-2.1` | MUST | Single meaning per term |
| `P4-2.2` | MUST NOT | No redefinition |
| `P4-2.3` | MUST NOT | No collapsing of the triad |
| `P4-2.4` | MUST NOT | No collapsing of concept and definition text |
| `P4-2.5` | MUST NOT | No collapsing of the two model senses |
| `P4-2.6` | MUST NOT | No collapsing of design and instance lineage |
| `P4-2.7` | MUST NOT | No collapsing of impact and reachability |
| `P4-2.8` | MUST NOT | No collapsing of the three clocks |
| `P4-2.9` | SHOULD | Term registry |
| **Section 3** | | **Data model** |
| `P4-3.1` | MUST | Declared types |
| `P4-3.2` | MUST NOT | No semantic identifiers |
| `P4-3.3` | MUST | Language tag present |
| `P4-3.4` | MUST NOT | No caller supplied knowledge time |
| `P4-3.5` | MUST | Datatype and unit systems named |
| `P4-3.6` | MUST | Three valued domain used unchanged |
| `P4-3.7` | MUST | Three artifacts, separately stored |
| `P4-3.8` | MUST | Concept is the identity |
| `P4-3.9` | MUST NOT | No designation as a key |
| `P4-3.10` | MUST | Many to many admitted |
| `P4-3.11` | MUST | Separate change records |
| `P4-3.12` | MUST NOT | No inference of concept stability |
| `P4-3.13` | MUST | Entity coverage |
| `P4-3.14` | MUST NOT | No update in place |
| `P4-3.15` | MUST NOT | No definition amendment |
| `P4-3.16` | MUST | Steward recorded |
| `P4-3.17` | MUST | Domain recorded |
| `P4-3.18` | MUST | Relations attributed and justified |
| `P4-3.19` | MUST NOT | No concept merger |
| `P4-3.20` | MUST NOT | No concept deletion |
| `P4-3.21` | MUST | Supersession by a different concept recorded as such |
| `P4-3.22` | MUST | Exactly one preferred designation per language and scope |
| `P4-3.23` | MUST | Status recorded |
| `P4-3.24` | MUST | Deprecated designations remain resolvable |
| `P4-3.25` | MUST | Prohibition reasoned |
| `P4-3.26` | MUST | Legacy identifiers registrable |
| `P4-3.27` | MUST | Ambiguity reported, not resolved |
| `P4-3.28` | MUST NOT | No designation reuse across concepts without a scope |
| `P4-3.29` | MUST | Definition text present in at least one language |
| `P4-3.30` | MUST | Singular and positive |
| `P4-3.31` | MUST | Descriptive phrase or sentence |
| `P4-3.32` | MUST NOT | No embedded definitions |
| `P4-3.33` | MUST | Terms referenced or declared primitive |
| `P4-3.34` | MUST | Circularity detected |
| `P4-3.35` | MUST | Exclusions stated where contested |
| `P4-3.36` | MUST | Source cited and relation stated |
| `P4-3.37` | MUST | Contradiction of a source recorded |
| `P4-3.38` | MUST NOT | No translated text as authoritative |
| `P4-3.39` | MUST | Datatype and its system recorded |
| `P4-3.40` | MUST | Unit required for a measured quantity |
| `P4-3.41` | MUST | Cardinality recorded |
| `P4-3.42` | MUST | Null semantics declared |
| `P4-3.43` | MUST NOT | No inference of null semantics |
| `P4-3.44` | MUST | Value set bound by pin |
| `P4-3.45` | MUST NOT | No local value set membership |
| `P4-3.46` | MUST | Precision reportable where absent |
| `P4-3.47` | MUST | Change kinds declared |
| `P4-3.48` | MUST | Multiple kinds permitted and enumerated |
| `P4-3.49` | MUST NOT | No concept replacement as a version |
| `P4-3.50` | MUST | Extension effect declared |
| `P4-3.51` | MUST | Kind and extension effect consistent |
| `P4-3.52` | MUST | Incomparable extension treated as replacement |
| `P4-3.53` | MUST | Retrospectivity declared |
| `P4-3.54` | MUST | Rationale and declarer recorded |
| `P4-3.55` | MUST | Impact analysis reference recorded or its absence reportable |
| `P4-3.56` | MUST NOT | No inferred change kind |
| `P4-3.57` | MUST | Test set bound to the concept |
| `P4-3.58` | MUST | Test set required for a claim of unchanged extension |
| `P4-3.59` | MUST | Test set run before admission |
| `P4-3.60` | MUST | Borderline instances required |
| `P4-3.61` | MUST NOT | No admission on inconsistency |
| `P4-3.62` | MUST | Human classification marked |
| `P4-3.63` | MUST NOT | No generated instances |
| `P4-3.64` | MUST NOT | No correspondence claim from agreement |
| `P4-3.65` | MUST | Instances re run on later versions |
| `P4-3.66` | MUST | Approval obtained, not asserted |
| `P4-3.67` | MUST | Resolution outcome recorded in full |
| `P4-3.68` | MUST | Unapproved versions marked in every read |
| `P4-3.69` | MUST | Approval not sought distinguished from unresolvable |
| `P4-3.70` | MUST | Unapproved versions countable |
| `P4-3.71` | MUST | Effectivity asserted, not inferred from approval |
| `P4-3.72` | MUST | Scope on every effectivity assertion |
| `P4-3.73` | MUST | At most one version in force per scope |
| `P4-3.74` | MUST | Correction by retraction and replacement |
| `P4-3.75` | MUST | Model kind and layer recorded |
| `P4-3.76` | MUST | Elements addressable in a registered scheme |
| `P4-3.77` | MUST | Element count derived |
| `P4-3.78` | MUST | Realisation relations declared |
| `P4-3.79` | MUST NOT | No realisation by name matching |
| `P4-3.80` | MUST | Non realisation recordable |
| `P4-3.81` | MUST | Binding kind recorded |
| `P4-3.82` | MUST | Overlapping bindings reportable |
| `P4-3.83` | MUST NOT | No model content authority |
| `P4-3.84` | MUST | Interface bound to definitions |
| `P4-3.85` | MUST NOT | No model internals |
| `P4-3.86` | MUST | Training period definitions pinned or their absence reportable |
| `P4-3.87` | MUST | Training definition drift reportable |
| `P4-3.88` | MUST | Invocation reference recorded |
| `P4-3.89` | MUST NOT | No performance claims |
| `P4-3.90` | MUST | Closed edge kind set |
| `P4-3.91` | MUST NOT | No generic flow edge |
| `P4-3.92` | MUST | Grain recorded on every node and edge |
| `P4-3.93` | MUST | Filter and conditional dependencies recorded |
| `P4-3.94` | MUST | Transformation pinned where the kind requires it |
| `P4-3.95` | MUST | Semantic effect declared |
| `P4-3.96` | MUST | Meaning changing edges reportable |
| `P4-3.97` | MUST NOT | No cycle in the lineage graph |
| `P4-3.98` | MUST | Method recorded on every edge |
| `P4-3.99` | MUST | Tool pinned where a tool produced the edge |
| `P4-3.100` | MUST | Source artifact pinned where available |
| `P4-3.101` | MUST NOT | No inferred edge as declared |
| `P4-3.102` | MUST | Confirmation recorded separately |
| `P4-3.103` | MUST | Inferred proportion reportable |
| `P4-3.104` | MUST | Every terminus is a declared frontier |
| `P4-3.105` | MUST | Not yet mapped distinguished |
| `P4-3.106` | MUST | Illegitimate frontiers reportable |
| `P4-3.107` | MUST | Completeness declared per node |
| `P4-3.108` | MUST | Partial known and unknown distinguished |
| `P4-3.109` | MUST NOT | No inference of completeness |
| `P4-3.110` | MUST | Divergence recorded, not resolved |
| `P4-3.111` | MUST | Both divergence directions reportable |
| `P4-3.112` | MUST | Grain incomparability recorded |
| `P4-3.113` | MUST | Design lineage exposed by pin |
| `P4-3.114` | MUST | Dependencies registrable by other components |
| `P4-3.115` | MUST | Both version and concept recorded |
| `P4-3.116` | MUST | Binding strength recorded |
| `P4-3.117` | MUST | Source state tracked |
| `P4-3.118` | MUST | Unpinned dependents reportable |
| `P4-3.119` | MUST | External obligations registrable |
| `P4-3.120` | MUST NOT | No dependency inference |
| `P4-3.121` | MUST | Withdrawal recorded, not deleted |
| `P4-3.122` | MUST | Impact spans every source |
| `P4-3.123` | MUST | Reached by recorded |
| `P4-3.124` | MUST | Consequence class on every member |
| `P4-3.125` | MUST | Semantic drift derived where derivable |
| `P4-3.126` | MUST NOT | No assessment of material consequence |
| `P4-3.127` | MUST | Historical reclassification derived from retrospectivity |
| `P4-3.128` | MUST | Confidence recorded per member |
| `P4-3.129` | MUST | Analysis compared with the change made |
| `P4-3.130` | MUST | Pins recorded |
| `P4-3.131` | MUST NOT | No impact set as approval |
| `P4-3.132` | MUST | Projections are pure |
| `P4-3.133` | MUST | Projection recomputable |
| `P4-3.134` | MUST | Named projections available |
| `P4-3.135` | MUST | Reachability and impact separately named |
| `P4-3.136` | MUST | Extension change history available |
| `P4-3.137` | MUST NOT | No writes through a projection |
| `P4-3.138` | MUST | Demonstration satisfiable |
| **Section 4** | | **Interfaces** |
| `P4-4.1` | MUST | Operation classes separated |
| `P4-4.2` | MUST | Refusal is an outcome |
| `P4-4.3` | MUST | Idempotence key accepted |
| `P4-4.4` | MUST NOT | No partial definition recording |
| `P4-4.5` | MUST | Preconditions checked at recording |
| `P4-4.6` | MUST | Whole definition version in one operation |
| `P4-4.7` | MUST | Test set run before the version is recorded |
| `P4-4.8` | MUST NOT | No approval by this component |
| `P4-4.9` | MUST | Supersession and version increment distinguished at the interface |
| `P4-4.10` | MUST | Retirement precondition declared |
| `P4-4.11` | MUST | Edge preconditions checked |
| `P4-4.12` | MUST | Confirmation does not rewrite method |
| `P4-4.13` | MUST NOT | No edge alteration on divergence |
| `P4-4.14` | MUST | Dependency registered by its owner |
| `P4-4.15` | MUST | Source state recordable and reportable |
| `P4-4.16` | MUST | Proposed change recorded before analysis |
| `P4-4.17` | MUST | Consultation state returned |
| `P4-4.18` | MUST | Analysis pins recorded before returning |
| `P4-4.19` | MUST | Assessment attributed |
| `P4-4.20` | MUST NOT | No analysis as a side effect |
| `P4-4.21` | MUST | Comparison available |
| `P4-4.22` | MUST | Times required on temporal resolution |
| `P4-4.23` | MUST | Approval status returned with every version |
| `P4-4.24` | MUST | Lineage returned with its qualifications |
| `P4-4.25` | MUST NOT | No partial artifact set |
| `P4-4.26` | MUST | Caller obligations declared |
| `P4-4.27` | MUST NOT | No implied completeness |
| `P4-4.28` | MUST NOT | No approval implied by presence |
| `P4-4.29` | MUST | Declared unavailability behaviour |
| `P4-4.30` | MUST NOT | No substitution on unavailability |
| `P4-4.31` | MUST | Source unavailability surfaced in the outcome |
| `P4-4.32` | MUST | Minimum event set |
| `P4-4.33` | MUST | Envelope minimum |
| `P4-4.34` | MUST NOT | No event in place of a record |
| `P4-4.35` | MUST | Semantic drift emitted per member |
| `P4-4.36` | MUST | Source cessation detected |
| `P4-4.37` | MUST NOT | No suppression of adverse events |
| **Section 5** | | **State model** |
| `P4-5.1` | MUST | Four models separate |
| `P4-5.2` | MUST | Registered but unapproved reportable |
| `P4-5.3` | MUST NOT | No authority state held |
| `P4-5.4` | MUST | Enumerated states only |
| `P4-5.5` | MUST | Enumerated transitions only |
| `P4-5.6` | MUST | State is a projection |
| `P4-5.7` | MUST | Refused versions retained and countable |
| `P4-5.8` | MUST NOT | No resolution of a draft, refused or withdrawn version |
| `P4-5.9` | MUST | Withdrawal reports its dependents |
| `P4-5.10` | MUST | Superseded versions remain resolvable |
| `P4-5.11` | MUST NOT | No state change from the passage of time |
| `P4-5.12` | MUST | Withdrawal authorised and reasoned |
| `P4-5.13` | MUST | Enumerated concept states |
| `P4-5.14` | MUST NOT | No revival |
| `P4-5.15` | MUST | Dormancy computed and reported |
| `P4-5.16` | MUST | Supersession by concept reports dependents |
| `P4-5.17` | MUST | Enumerated edge states |
| `P4-5.18` | MUST NOT | No promotion of inferred to asserted |
| `P4-5.19` | MUST | Retracted edges retained |
| `P4-5.20` | MUST | Contradicted edges traversed and marked |
| `P4-5.21` | MUST | Resolution of a contradiction reasoned |
| `P4-5.22` | MUST | Enumerated run states |
| `P4-5.23` | MUST | Sources attempted before classification |
| `P4-5.24` | MUST | Partial distinguished from complete |
| `P4-5.25` | MUST | Partial runs still return members |
| `P4-5.26` | MUST | Abandonment detected and recorded |
| `P4-5.27` | MUST | Terminal states are terminal |
| `P4-5.28` | MUST NOT | No amendment of a run |
| **Section 6** | | **Execution semantics** |
| `P4-6.1` | MUST | Identical inputs yield identical results |
| `P4-6.2` | MUST | Traversal order total and declared |
| `P4-6.3` | MUST | Graph state pinned in an analysis |
| `P4-6.4` | MUST | Classification rule version pinned |
| `P4-6.5` | MUST | Irreproducibility reported, not concealed |
| `P4-6.6` | MUST | Algorithm order |
| `P4-6.7` | MUST | Both instants required |
| `P4-6.8` | MUST | Ambiguity returns all candidates |
| `P4-6.9` | MUST | Approval read as recorded |
| `P4-6.10` | MUST | Divergence flag returned |
| `P4-6.11` | MUST | Unapproved resolution distinguished |
| `P4-6.12` | MUST | Exact matching |
| `P4-6.13` | MUST NOT | No lexical equivalence |
| `P4-6.14` | MUST | Designation ambiguity returns all concepts |
| `P4-6.15` | MUST | Designation status returned |
| `P4-6.16` | MUST | Idempotence by key |
| `P4-6.17` | MUST | Deduplication window declared |
| `P4-6.18` | MUST NOT | No idempotence across differing payloads |
| `P4-6.19` | MUST | Duplicate definition detectable |
| `P4-6.20` | MUST | Procedure order |
| `P4-6.21` | MUST | Human involvement recorded per instance |
| `P4-6.22` | MUST | Inconsistent instances named |
| `P4-6.23` | MUST | Instance order declared |
| `P4-6.24` | MUST NOT | No mechanical classification without data |
| `P4-6.25` | MUST | Algorithm order |
| `P4-6.26` | MUST | All five directions traversed |
| `P4-6.27` | MUST | Every source attempt recorded |
| `P4-6.28` | MUST | All applicable consequence classes recorded |
| `P4-6.29` | MUST | Precedence applied as stated |
| `P4-6.30` | MUST | Unassessed is the default |
| `P4-6.31` | MUST | Path qualifications propagated |
| `P4-6.32` | MUST NOT | No pruning by consequence |
| `P4-6.33` | MUST | Three bounds declared |
| `P4-6.34` | MUST | Primary budget deterministic |
| `P4-6.35` | MAY | Secondary non deterministic guard |
| `P4-6.36` | MUST | Non deterministic truncation marked |
| `P4-6.37` | MUST | Truncation point recorded |
| `P4-6.38` | MUST NOT | No silent bound |
| `P4-6.39` | MUST | Knowledge time assigned by this component |
| `P4-6.40` | MUST NOT | No occurrence time assignment |
| `P4-6.41` | MUST | Application time asserted, not inferred |
| `P4-6.42` | MUST | Instants in a declared scale |
| `P4-6.43` | MUST | Monotonic knowledge time within a stream |
| `P4-6.44` | MUST | Permitted computations only |
| `P4-6.45` | MUST NOT | No inference of a definition |
| `P4-6.46` | MUST NOT | No inference of a dependency |
| `P4-6.47` | MUST NOT | No inference of materiality |
| **Section 7** | | **Outcome and failure taxonomy** |
| `P4-7.1` | MUST | Closed resolution outcome set |
| `P4-7.2` | MUST | Unapproved resolution distinguished |
| `P4-7.3` | MUST | Supersession signalled |
| `P4-7.4` | MUST | Ambiguity returns candidates |
| `P4-7.5` | MUST | Not in force distinguished from not found |
| `P4-7.6` | MUST | Withheld distinguished from not found |
| `P4-7.7` | MUST NOT | No mapping onto two values |
| `P4-7.8` | MUST | Closed traversal outcome set |
| `P4-7.9` | MUST | All applicable members returned |
| `P4-7.10` | MUST | Declared and undeclared incompleteness distinguished |
| `P4-7.11` | MUST | Inferred participation reported |
| `P4-7.12` | MUST NOT | No complete outcome from defaulted completeness |
| `P4-7.13` | MUST | Closed impact outcome set |
| `P4-7.14` | MUST | All applicable members returned |
| `P4-7.15` | MUST | Lineage only reported |
| `P4-7.16` | MUST | Stale distinguished from unavailable |
| `P4-7.17` | MUST | Grain reported with the outcome |
| `P4-7.18` | MUST NOT | No complete outcome with any partial condition |
| `P4-7.19` | MUST | Refusal codes |
| `P4-7.20` | MUST | Refusal states what to supply |
| `P4-7.21` | MUST | Refusals recorded and counted |
| `P4-7.22` | MUST | Test set refusal names the instances |
| `P4-7.23` | MUST NOT | No acceptance on placeholder values |
| `P4-7.24` | MUST | Read refusal codes |
| `P4-7.25` | MUST | Unknown distinguished from withheld |
| `P4-7.26` | MUST | Recording obligations honoured |
| `P4-7.27` | MUST | Emission obligations honoured |
| `P4-7.28` | MUST | Reader obligations documented |
| `P4-7.29` | MUST NOT | No adequacy language for a partial outcome |
| `P4-7.30` | MUST | A meaning change is never a version of the same thing |
| `P4-7.31` | MUST | A data flow traversal is never an impact assessment |
| **Section 8** | | **Observability and the audit record** |
| `P4-8.1` | MUST | Own terminology not self governed |
| `P4-8.2` | MUST | Derivative registrations marked |
| `P4-8.3` | MUST | Registries external |
| `P4-8.4` | MUST | Own operations recorded |
| `P4-8.5` | MUST | Declared grain |
| `P4-8.6` | MUST | Approval attempts recorded individually |
| `P4-8.7` | MUST | Per instance classification results recorded |
| `P4-8.8` | MUST | Counting grain stated with every count |
| `P4-8.9` | MUST | Submission recorded as received |
| `P4-8.10` | MUST | Precondition outcomes recorded, including passes |
| `P4-8.11` | MUST | Classification run retained with the version |
| `P4-8.12` | MUST | Approval envelope retained in full |
| `P4-8.13` | MUST | Periodic re resolution of approvals |
| `P4-8.14` | MUST | Reads recorded |
| `P4-8.15` | MUST | Withholding recorded |
| `P4-8.16` | MUST | Impact analyses recorded with their requester |
| `P4-8.17` | SHOULD | Read records retained with the subject |
| `P4-8.18` | MUST | Signals produced |
| `P4-8.19` | MUST | Signals derived from entries |
| `P4-8.20` | MUST NOT | No suppression of a signal |
| `P4-8.21` | MUST | Refusal signal reaches the steward and the steward's owner |
| `P4-8.22` | MUST | Source cessation is a standing measure |
| `P4-8.23` | MUST | Drift signals trended |
| `P4-8.24` | SHOULD | Signal thresholds declared |
| `P4-8.25` | MUST | Package sufficiency |
| `P4-8.26` | MUST | Test set and its results included |
| `P4-8.27` | MUST | Approval content included or its absence stated |
| `P4-8.28` | MUST | Limit statements included |
| `P4-8.29` | MUST | Absence stated, not omitted |
| `P4-8.30` | MUST | Package digest |
| `P4-8.31` | MUST | Self description |
| `P4-8.32` | MUST | Retention obtained, not assigned |
| `P4-8.33` | MUST | Definitions outlive the data they describe |
| `P4-8.34` | MUST | Definitions outlive determinations that relied on them |
| `P4-8.35` | MUST | Test sets retained with their versions |
| `P4-8.36` | MUST | Separate retention per structure |
| `P4-8.37` | MUST | Disposal recorded and citable |
| `P4-8.38` | MUST NOT | No disposal of a definition with undischarged dependents |
| `P4-8.39` | MUST NOT | No amendment of an entry |
| `P4-8.40` | MUST NOT | No amendment of a classification result |
| `P4-8.41` | MUST NOT | No amendment of an impact run |
| `P4-8.42` | MUST | Migration preserves identity and digests |
| `P4-8.43` | MUST NOT | No bulk reclassification on import |
| **Section 9** | | **Extension model** |
| `P4-9.1` | MUST | Closed sets not extended |
| `P4-9.2` | MUST | Unknown member is a defect, not a default |
| `P4-9.3` | MUST | Open sets registered |
| `P4-9.4` | MUST NOT | No generic edge kind by registration |
| `P4-9.5` | MUST | Registry as controlled document |
| `P4-9.6` | MUST NOT | No key reuse |
| `P4-9.7` | MUST | Deprecation rather than removal |
| `P4-9.8` | MUST | Registry version recorded and retained |
| `P4-9.9` | MUST | Semantics in the entry |
| `P4-9.10` | MUST | Datatype semantics stated in full |
| `P4-9.11` | MUST | Numeric behaviour declared |
| `P4-9.12` | MUST | Collation declared for character members |
| `P4-9.13` | MUST | Cross system mappings attributed |
| `P4-9.14` | MUST NOT | No implicit system |
| `P4-9.15` | MUST | Stability declared |
| `P4-9.16` | SHOULD | Stable schemes preferred |
| `P4-9.17` | MUST NOT | No cross scheme comparison |
| `P4-9.18` | MUST | Layers declared per kind |
| `P4-9.19` | MUST | Realisation requirement declared and enforced |
| `P4-9.20` | MUST | Element kinds declared |
| `P4-9.21` | MUST | Traversal behaviour declared per kind |
| `P4-9.22` | MUST | Transitivity declared |
| `P4-9.23` | MUST | Required evidence declared |
| `P4-9.24` | MUST | Both registered and both recorded |
| `P4-9.25` | MUST | Deprecation without invalidation |
| `P4-9.26` | MUST NOT | No digest without a profile |
| `P4-9.27` | MUST | Owning component declared per dependency kind |
| `P4-9.28` | MUST | Currency interval declared per source |
| `P4-9.29` | MUST | Classification behaviour declared per dependency kind |
| `P4-9.30` | MUST | Frontier legitimacy declared |
| `P4-9.31` | MUST | Refusal codes registered with remedy |
| `P4-9.32` | MUST | Event types registered |
| `P4-9.33` | MUST | Model inclusion by pinned version only |
| `P4-9.34` | MUST NOT | No cyclic model inclusion |
| `P4-9.35` | MUST | Composition depth bounded and declared |
| `P4-9.36` | MUST NOT | No composite concept without a definition text |
| `P4-9.37` | MUST | Shared elements versioned in every including model |
| **Section 10** | | **Standards and specifications** |
| `P4-10.1` | MUST | Cited edition recorded |
| `P4-10.2` | MUST | Basis marked |
| `P4-10.3` | MUST | Practice basis recorded |
| `P4-10.4` | MUST | Unsourced requirements identified |
| **Section 11** | | **Anti patterns** |
| `P4-11.1` | MUST NOT | No editable definition |
| `P4-11.2` | MUST NOT | No concept replacement as a version |
| `P4-11.3` | MUST NOT | No unchecked claim of no change |
| `P4-11.4` | MUST NOT | No traversal as an impact set |
| `P4-11.5` | MUST NOT | No assumed completeness |
| `P4-11.6` | MUST NOT | No inference presented as assertion |
| `P4-11.7` | MUST NOT | No unpinned tool assertion |
| `P4-11.8` | MUST NOT | No unqualified grain |
| `P4-11.9` | MUST NOT | No omission of filter and conditional dependencies |
| `P4-11.10` | MUST | Source state tracked and cessation detected |
| `P4-11.11` | MUST NOT | No stale source as current |
| `P4-11.12` | MUST | Consequence class on every member |
| `P4-11.13` | MUST | Semantic drift derived and emitted |
| `P4-11.14` | MUST NOT | No analysis as approval |
| `P4-11.15` | MUST | Analysis compared with the change made |
| `P4-11.16` | MUST NOT | No unapproved version as resolved |
| `P4-11.17` | MUST | Null semantics declared |
| `P4-11.18` | MUST NOT | No designation as an identifier |
| `P4-11.19` | MUST NOT | No lexical equivalence |
| `P4-11.20` | MUST NOT | No concept merger |
| `P4-11.21` | MUST NOT | No self governed vocabulary |
| `P4-11.22` | MUST | Borderline instances required and reported |
| `P4-11.23` | MUST NOT | No generated definition as a steward's assertion |
| `P4-11.24` | SHOULD NOT | No wholesale physical import as concepts |
| `P4-11.25` | MUST | Model interfaces bound and drift reportable |
| `P4-11.26` | MUST NOT | No edge alteration on divergence |
| **Section 12** | | **Boundaries with other parts** |
| `P4-12.1` | MUST | Declared allocation |
| `P4-12.2` | MUST | Recording rather than substitution |
| `P4-12.3` | MUST NOT | No reaching past a neighbour |
| `P4-12.4` | MUST | Approval obtained and recorded in full |
| `P4-12.5` | MUST NOT | No rendition as the definition |
| `P4-12.6` | MUST | Rendition effectivity not held |
| `P4-12.7` | MUST | Definition versions obtainable by pin |
| `P4-12.8` | MUST | Supersession queryable |
| `P4-12.9` | MUST | Rule term references registered as dependencies |
| `P4-12.10` | MUST | Design lineage exposed by pin |
| `P4-12.11` | MUST NOT | No instance lineage held |
| `P4-12.12` | MUST | Divergence recorded in both directions and resolved in neither |
| `P4-12.13` | MUST NOT | No recommendation |
| `P4-12.14` | MUST | Decision criteria registered as dependencies |
| `P4-12.15` | MUST | Registration state independent of process |
| `P4-12.16` | MUST NOT | No process identity required |
| `P4-12.17` | MUST | Decisions consumed, not made |
| `P4-12.18` | MUST NOT | No stewardship as entitlement |
| `P4-12.19` | MUST | Policy attributes registered as dependencies |
| `P4-12.20` | MUST | Assessments independent of tasks |
| `P4-12.21` | MUST NOT | No task driven closure |
| `P4-12.22` | MUST NOT | No schema versioning or validation |
| `P4-12.23` | MUST | Schema bindings registered as dependencies |
| `P4-12.24` | MUST | Binding quality reportable |
| `P4-12.25` | MUST | Value sets bound by pin only |
| `P4-12.26` | MUST | Value set change surfaces as a change kind |
| `P4-12.27` | MUST | Set realisations registered as dependencies |
| `P4-12.28` | MUST | Digest is the interface |
| `P4-12.29` | MUST NOT | No identity in the store |
| `P4-12.30` | MUST | Read only assessment |
| `P4-12.31` | MUST NOT | No self assessment as assessment |
| `P4-12.32` | MUST | Test set composition exposed |
| `P4-12.33` | MUST | Interface held, behaviour not |
| `P4-12.34` | MUST | Model reference pinned |
| `P4-12.35` | MUST | Training definition drift reportable to Part 13 |
| `P4-12.36` | MUST | Authority declared, not assumed |
| `P4-12.37` | MUST | Unpopulated index visible to composition |
| **Section 13** | | **What could not be established** |
| `P4-13.1` | MUST | Verification before approval |
| `P4-13.2` | MUST | Gaps declared, not filled |
| `P4-13.3` | SHOULD | Open questions carried forward |

### Derived counts

Every figure below is derived by extraction from the clause text of this document and not asserted independently. The grain of counting is stated for each figure. A clause is one line of the document matching the clause heading form given under Binding of requirement language, that is, an identifier of the form `P4-S.N`, a modality in parentheses, and a subject label. Narrative sentences containing a requirement keyword are not clauses and are not counted; per that same section they are not binding.

**Total clauses.** 457. Grain: one clause heading.

**By modality.** Grain: one clause heading, counted once against its single declared modality.

| Modality | Clauses | Share |
| --- | --- | --- |
| MUST | 333 | 72.9% |
| MUST NOT | 116 | 25.4% |
| SHOULD | 6 | 1.3% |
| SHOULD NOT | 1 | 0.2% |
| MAY | 1 | 0.2% |
| **All** | **457** | **100.0%** |

**Absolute requirements.** 449 clauses carry MUST or MUST NOT and are therefore conditions of conformance. 7 carry SHOULD or SHOULD NOT and require a recorded reason where not satisfied. 1 carry MAY and constrain nothing. Grain: one clause heading. These three figures sum to the total.

**By section.** Grain: one clause heading, attributed to the numbered section in which its heading appears.

| Section | Title | Clauses | MUST | MUST NOT | SHOULD | SHOULD NOT | MAY |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Scope and responsibilities | 17 | 8 | 8 | 1 | 0 | 0 |
| 2 | Terminology | 9 | 1 | 7 | 1 | 0 | 0 |
| 3 | Data model | 138 | 108 | 30 | 0 | 0 | 0 |
| 4 | Interfaces | 37 | 27 | 10 | 0 | 0 | 0 |
| 5 | State model | 28 | 22 | 6 | 0 | 0 | 0 |
| 6 | Execution semantics | 47 | 37 | 9 | 0 | 0 | 1 |
| 7 | Outcome and failure taxonomy | 31 | 26 | 5 | 0 | 0 | 0 |
| 8 | Observability and the audit record | 43 | 35 | 6 | 2 | 0 | 0 |
| 9 | Extension model | 37 | 29 | 7 | 1 | 0 | 0 |
| 10 | Standards and specifications | 4 | 4 | 0 | 0 | 0 | 0 |
| 11 | Anti patterns | 26 | 7 | 18 | 0 | 1 | 0 |
| 12 | Boundaries with other parts | 37 | 27 | 10 | 0 | 0 | 0 |
| 13 | What could not be established | 3 | 2 | 0 | 1 | 0 | 0 |
| **All** | | **457** | **333** | **116** | **6** | **1** | **1** |

**Ordinal integrity.** In this version, the highest ordinal in each section equals the number of clauses in that section, so no identifier has yet been retired. This will cease to be true at the first clause removal, and the count rather than the highest ordinal is then the figure to rely on.

## 1. Scope and responsibilities

### 1.1 What this component is

This part specifies a component that holds the governed definitions of an organisation as structured data rather than as prose, versions them so that what a term meant on a past date is recoverable, records how data elements are designed to derive from one another, and reports what a proposed change to any of it would affect.

The component exists to answer one question reliably: **what did this term mean when this number was produced, and if the meaning changes, what else changes with it.** Every other responsibility in this part is subordinate to that question.

Three properties distinguish this component from a data dictionary, and each is a reason it exists at all.

**A definition is data, not text.** Its concept, its designations and its representation are separate fields with separate governance, so that a renaming, a re typing and a change of meaning are three different events with three different consequences. A dictionary in which the definition is a paragraph cannot distinguish them, so all three appear as an edit.

**A change of meaning is never a version of the same thing.** A definition version may clarify, narrow, broaden or re represent. It may not replace one concept with another under the same identifier, because every consumer will continue using the identifier and will silently mean something new. Section 3.8 makes the distinction a declared, checkable property of every version increment, and section 3.9 supplies the only mechanically checkable test of the declaration.

**Impact is not reachability.** The transitive closure of a lineage graph over declares by orders of magnitude and under declares the things that matter, because the consequences of changing a definition reach rules that cite it, determinations that relied on it, schemas that bind to it and reference sets that realise it, none of which is in the lineage graph. Section 3.17 requires the impact set to span those sources and to say so when it could not.

The component is accountable for the following.

Concept identity: the persistent identity of a governed meaning, independent of any term that names it and any structure that carries it.

Designation: the terms that name a concept, per language, with their status, and the rules governing what a designation may be.

Definition text: the statement of the meaning, with the quality requirements a definition must satisfy to be admitted.

Representation: the datatype, unit, precision, format and cardinality by which a concept is expressed as data, and the binding to the permissible value set that realises it.

Version identity of every definition, and the declared kind of every change between versions.

The classification test set: instances with their asserted membership of a concept's extension, which is the bridge between a definition's text and its use.

The approval and effectivity of a definition version, obtained by resolution rather than asserted, and the marking of definitions that have neither.

Models: the identity, version and structure of information models, their layers, and the realisation relations between layers.

The identity, version and declared interface of an analytic or inferential model, and the definitions its inputs and outputs bind to.

Design lineage: the asserted derivation relations between data elements, at a declared grain, with typed edges, with the provenance of each assertion, and with declared frontiers.

Lineage completeness, declared rather than inferred, and the divergence between asserted design lineage and observed instance lineage.

Dependent registration: the index of what elsewhere in the estate depends on each definition, assembled from the components that hold those dependencies.

Impact analysis: the prospective assessment of what a proposed change would affect, classified by kind of consequence, pinned so that it is repeatable, and never presented as an approval.

The audit record of all of the above, at a grain sufficient to reconstruct any determination this component supplied.

### 1.2 What this component is not

Each exclusion names something a metadata repository absorbs if nobody stops it, and each absorption destroys a property some other component was supposed to guarantee.

The component is not the publisher of definitions. A definition published as a controlled document is a rendition of the definition and belongs to `Part 1`. This is the position `Part 1` section 12.4 takes and section 12.1 here is the reciprocal.

The component is not the approver. A definition version becomes authoritative by being approved through `Part 1`, and this component records the resolution outcome rather than the fact of approval.

The component is not a rules engine. A definition says what a thing is. A rule says which values of it are permissible. The boundary is contestable and section 13.3 records that; what is not contestable is that a definition carrying an executable constraint has put a rule somewhere nobody will look for it.

The component is not a schema registry. A schema says what a well formed instance is; a definition says what its elements mean. Schema identity, versioning, compatibility and validation belong to `Part 9`.

The component is not the owner of reference data. A value domain here names and constrains a permissible value set; the membership of that set and its governance belong to `Part 10`.

The component is not the provenance ledger. Instance lineage, being what actually happened to actual values in actual runs, belongs to `Part 3`. This component holds design lineage, being what the design asserts.

The component is not a model runtime. The invocation of an analytic or inferential model, its cost, its retries and its non determinism belong to `Part 13`.

The component is not a decision engine. Impact analysis reports; it does not choose. Whether to proceed with a change is a decision belonging to `Part 5` and an authorisation belonging to `Part 7`.

The component is not the physical data store, and does not hold the data its definitions describe.

The component is not a discovery and search platform. It must make definitions findable by their governed metadata; ranking, similarity and free text retrieval quality are out of scope.

The component is not an identity provider. Actors are opaque references resolvable elsewhere.

The component is not a conformance assessor, of itself or of anything else.

**P4-1.1 (MUST) Purpose satisfaction.** An implementation must be able to state, for any governed concept and any pair of application time and knowledge time within its retained history, which definition version was in force, or that none was, or that the question is ambiguous, by the mechanism specified in section 6.

**P4-1.2 (MUST) Definitions as structured data.** An implementation must hold the concept, the designations, the definition text and the representation of every governed definition as separately addressable fields, and must not hold a definition only as prose.

**P4-1.3 (MUST NOT) No meaning change under an identifier.** An implementation must not permit a definition version to replace the concept of its predecessor, and must require a new concept identity where the concept has changed, per section 3.8.

**P4-1.4 (MUST) Change kind declared.** An implementation must require a declared change kind on every version increment and must not default it.

**P4-1.5 (MUST) Impact spans dependents, not only lineage.** An implementation must assemble an impact set from design lineage and from the dependent registrations of section 3.16, and must report the outcome `LINEAGE_ONLY` of section 7.4 where it could obtain no dependent registration.

**P4-1.6 (MUST NOT) No approval.** An implementation must not approve a definition, a model or a change, must obtain approval status by resolution against `Part 1`, and must not represent an impact analysis as an approval or an authorisation.

**P4-1.7 (MUST NOT) No executable constraint in a definition.** An implementation must not hold an evaluable expression as part of a definition, and must record a constraint on a concept as a reference to a rule governed by `Part 2`.

**P4-1.8 (MUST NOT) No instance lineage.** An implementation must not record the derivation of a particular value in a particular run, and must record only asserted design relations.

**P4-1.9 (MUST) Lineage assertions are attributed.** An implementation must record, for every lineage assertion, who or what asserted it and by what means, per section 3.14.

**P4-1.10 (MUST NOT) No update in place.** An implementation must not represent any state change specified by this part as a modification or deletion of a previously written row, tuple, object or event.

**P4-1.11 (MUST NOT) No absorption of neighbouring responsibilities.** An implementation must not evaluate rules, validate against schemas, govern reference set membership, record instance lineage, invoke models, select among outcomes or decide authorisation, as those responsibilities are allocated in section 12.

**P4-1.12 (SHOULD) Declared exclusions.** An implementation should publish, as a controlled document under `Part 1`, the list of section 1.2 exclusions that it in fact provides by other means, so that a reader can tell what the implementation does not guarantee.

**P4-1.13 (MUST NOT) No conformance self assertion.** An implementation must not assert conformance to this part on the basis of its own internal checks alone, and must not represent such an assertion as an assessment.

**P4-1.14 (MUST) Time horizon declaration.** An implementation must declare the period for which it undertakes to answer the purpose question, as a duration or an absolute date rather than as an indefinite commitment.

### 1.3 The failure this part exists to prevent

Every organisation of any size has a data dictionary, and almost none of them can answer the purpose question. The reason is worth stating precisely, because the diagnosis determines what the specification has to require.

A dictionary records the current definition. When the definition changes, the entry is edited. The edit is dated, perhaps, and the previous text is retained in a history table nobody reads. What is lost is not the old text; it is the **relation** between the change and everything that depended on it.

The concrete failure runs as follows. In 2027 a term is defined and used in a rule, a report, three schemas and a regulatory submission. In 2029 someone narrows the definition, correctly and with good reason, and edits the entry. The rule continues to evaluate, because its expression did not change. The schemas continue to validate, because the datatype did not change. The report continues to run. Every consumer continues to work and every one of them now means something slightly different from what it meant. In 2032 a regulator asks why two submissions two years apart report different figures for the same measure, and the organisation discovers that it cannot establish what the measure meant in either year, because the dictionary holds one entry and its history is a list of texts with no relation to the consumers that read them.

Three requirements follow directly, and they are the spine of the part.

The change must be classified at the moment it is made, by someone accountable, into a kind whose consequences are known. That is section 3.8.

The classification must be checkable rather than merely asserted, because a narrowing declared as a clarification is the exact failure above and a declaration alone will not prevent it. That is section 3.9.

The set of things affected must be assembled from every component that holds a dependency, not from the lineage graph alone, and must be pinned so that the assessment can be produced again. That is sections 3.16 and 3.17.

### 1.4 Two ambiguous words

**Metadata.** In this part, metadata means descriptions of data: what a data element is, what it means, how it is represented and how it relates to other data elements. It does not mean operational metadata, being the record of when a job ran and how many rows it processed, which is telemetry and is excluded by clause P4-1.11 and by `Part 3` clause P3-1.9. It does not mean the descriptive metadata of a document, which is `Part 1`'s. The sense adopted here follows ISO/IEC 11179-1, which states that in all parts of that standard metadata refers to descriptions of data and that it does not treat metadata generally.

**Model.** In this part, model carries two senses and both are in scope, with a boundary between them that must be stated because it is the boundary with `Part 13`.

An **information model** is a structured, versioned artifact asserting the concepts, definitions, relationships and structures of a domain. Conceptual, logical and physical models are information models at different layers. These are wholly in scope, and section 3.11 specifies them.

An **inferential model** is an artifact that produces outputs from inputs by a fitted, trained or estimated procedure rather than by a declared one: a statistical model, a machine learning model, a scoring model. Its **identity, version, declared inputs and outputs, and the definitions those bind to** are in scope here, because they are governed definitions like any other and because an impact analysis that cannot reach them is incomplete. Everything about its invocation, its behaviour on a given input, its cost, its non determinism and its outputs is `Part 13`'s, and section 12.13 states the seam.

The distinction is not one of technique. It is that an information model asserts what is, and can therefore be read and reviewed, while an inferential model asserts nothing and can only be measured. This component governs artifacts that assert; it registers the existence and interface of artifacts that do not.

**P4-1.15 (MUST) Metadata sense declared.** An implementation must declare, in documentation exposed to any user, that metadata carries the sense of section 1.4, and must not accept operational telemetry or document descriptive metadata as governed metadata under this part.

**P4-1.16 (MUST) Both model senses distinguished.** An implementation must record, for every registered model, whether it is an information model or an inferential model, and must not hold one as a special case of the other.

**P4-1.17 (MUST NOT) No inferential model internals.** An implementation must not hold the parameters, weights, training data or fitted structure of an inferential model, and must record its identity, version and declared interface only.

## 2. Terminology

Terms are defined here only if this component owns them. A term owned by another part is cited to that part and is not redefined. Where a term is taken from an external standard, the standard is named. Where this part narrows or diverges from the external definition, the divergence is stated.

This part is unusual in that its subject matter is definitions, so a reader may reasonably ask what governs the definitions in this section. They are definitions in the sense of ISO 704 and are not governed instances of the model this part specifies, for the reason section 8.1 gives: a component cannot be the authority for its own vocabulary without circularity.

### 2.1 Terms owned by this part

**Object.** Anything perceivable or conceivable, whether material, immaterial or imagined. Term and sense follow ISO 704:2022, which adopts it to avoid the question of whether the thing exists.

**Concept.** A unit of knowledge created by a unique combination of characteristics, being what is meant independently of any term that names it. Sense follows ISO 704:2022 and ISO 1087:2019 and the Concept class of ISO/IEC 11179-3:2023. A concept is the unit of identity in this part: it persists across renamings and re representations and does not persist across a change of meaning.

**Designation.** A term, name, symbol or code that represents a concept in a language. Term follows ISO 704:2022 and the designation facility of ISO/IEC 11179-3:2023.

**Definition text.** The statement in natural language of the concept, satisfying the quality requirements of section 3.6. Distinguished from the concept it states, because two definition texts may state one concept and one text may be revised without the concept changing.

**Representation.** The manner in which a concept is expressed as data: its datatype, unit of measure, precision, format, cardinality and permissible value set. Corresponds broadly to the value domain of ISO/IEC 11179-31:2023, narrowed here to exclude the membership of the value set.

**Value domain binding.** The recorded relation between a representation and the permissible value set that realises it, where the set is governed by `Part 10`.

**Governed definition.** The bound triad of a concept, its designations and its representation, at a version, with its definition text, its classification test set, its approval citation and its effectivity.

**Definition version.** One immutable state of a governed definition, with a declared change kind relative to its predecessor.

**Change kind.** The declared class of a version increment, drawn from the closed set of section 3.8.

**Extension.** The set of objects that fall under a concept. A narrowing or broadening is a change to the extension; a clarification is not.

**Classification test set.** Instances supplied with a definition, each with the asserted answer to whether it falls under the concept, used to check a declared change kind. The bridge specified in section 3.9.

**Information model.** A structured, versioned artifact asserting concepts, definitions, relationships and structures of a domain.

**Model layer.** The level of abstraction at which an information model asserts: conceptual, logical or physical.

**Realisation relation.** A declared relation stating that an element of one model layer realises an element of another.

**Inferential model.** An artifact producing outputs from inputs by a fitted, trained or estimated procedure. Registered here by identity, version and interface only.

**Design lineage.** The asserted derivation relations between data elements, as a matter of design rather than of history.

**Lineage node.** An addressable element that a lineage edge may connect: a definition, a model element or a physical structure.

**Lineage edge.** One asserted derivation relation, of a kind drawn from the closed set of section 3.13.

**Lineage grain.** The level at which lineage is asserted: element level, structure level or system level.

**Lineage frontier.** A declared point at which a lineage graph terminates, with the reason it terminates there. The concept is taken deliberately from `Part 3` section 3.11 and the parallel is noted in section 13.7.

**Dependent registration.** A recorded statement by another component that something it owns depends on a named definition version.

**Impact set.** The assembled set of things a proposed change would affect, with each member classified by the kind of consequence.

**Impact analysis.** One pinned, repeatable assessment producing an impact set for a proposed change.

**Proposed change.** A described but unmade change to a definition, model or lineage assertion, against which an impact analysis is run.

**Application time.** The time dimension in which a definition is in force. Used unchanged from `Part 1` section 2.1.

**Knowledge time.** The instant at which this component durably recorded a fact, assigned by this component. Used unchanged from `Part 1`.

**Occurrence time.** The instant at which a recorded act happened in the world, as asserted by an actor. Used unchanged from `Part 1`.

### 2.2 Clauses governing terminology

**P4-2.1 (MUST) Single meaning per term.** An implementation must use each term defined in section 2.1 with the meaning given there in all of its interfaces, records, reports and documentation.

**P4-2.2 (MUST NOT) No redefinition.** An implementation must not use a term defined in section 2.1 for a different concept, and must not use a different term for a concept defined in section 2.1 in any interface specified by this part.

**P4-2.3 (MUST NOT) No collapsing of the triad.** An implementation must not use one term or one field for a concept, a designation and a representation.

**P4-2.4 (MUST NOT) No collapsing of concept and definition text.** An implementation must not treat a change to a definition text as necessarily a change to the concept, or a stable definition text as evidence that the concept is unchanged.

**P4-2.5 (MUST NOT) No collapsing of the two model senses.** An implementation must not use one term for an information model and an inferential model.

**P4-2.6 (MUST NOT) No collapsing of design and instance lineage.** An implementation must not use one term for an asserted design relation and an observed derivation of a value.

**P4-2.7 (MUST NOT) No collapsing of impact and reachability.** An implementation must not use one term for the transitive closure of a lineage graph and an impact set.

**P4-2.8 (MUST NOT) No collapsing of the three clocks.** An implementation must not use one term or one field for more than one of application time, knowledge time and occurrence time.

**P4-2.9 (SHOULD) Term registry.** An implementation should publish the terms it adds beyond section 2.1, with definitions, as a controlled document under `Part 1`.
## 3. Data model

The model is stated as entities with typed fields. For each field the model gives its type, whether it is required, its cardinality, and what its absence means. Absence semantics are stated because in this component the commonest wrong inference from a missing field is that a definition is authoritative when nobody has approved it.

### 3.1 Type vocabulary

| Type | Value space | Notes |
| --- | --- | --- |
| `ID` | An opaque, globally unique, immutable identifier | Never reused. Never parsed for meaning. |
| `URN` | A persistent name in a declared namespace | Resolvable by the component owning the namespace. |
| `ATIME` | An instant in application time | The dimension in which definitions are in force. |
| `KTIME` | An instant in knowledge time, assigned by this component | Never accepted from a caller. |
| `OTIME` | An instant asserted by an actor as when an act occurred | Never assigned by this component. |
| `SEQ` | A monotonically increasing ordinal within a named stream | Total order within the stream only. |
| `DIGEST` | An algorithm identifier and a value | Algorithm from the registry of section 9.7. |
| `ENUM` | A member of a named closed or registered set | The set is named at every point of use. |
| `TEXT` | A sequence of characters intended for a person | Carries a `LANG`. |
| `LANG` | A language tag per BCP 47 | Required wherever `TEXT` appears. |
| `PIN` | An identity, a version and where available a digest | Sufficient to obtain the identical artifact again. |
| `CITEREF` | A citation resolvable under `Part 1`, carrying its mode | Used for approval and authority citations. |
| `ACTOR` | An opaque reference to a person, organisation or automated agent | Carries its kind. Resolved elsewhere. |
| `AUTHREF` | A reference to an authorisation decision made by `Part 7` | Recorded, never evaluated here. |
| `PATH` | A locator into a model or structure, in a named path scheme | Registered under section 9.4. |
| `DATATYPE` | A datatype identifier in a named datatype system | The system is registered under section 9.5. |
| `UNIT` | A unit of measure identifier in a named unit system | The system is registered under section 9.5. |
| `TRUTH` | One of `TRUE`, `FALSE`, `INDETERMINATE` | The three valued domain, used unchanged from `Part 2` section 6.2. |
| `COUNT` | A non negative integer | Grain stated wherever reported. |
| `DURATION` | A length of time, independent of any instant | |

**P4-3.1 (MUST) Declared types.** An implementation must be able to state, for every field it holds that corresponds to a field in this section, which type of the table above it carries.

**P4-3.2 (MUST NOT) No semantic identifiers.** An implementation must not derive the meaning, status, approval, effectivity or change kind of anything from the characters of its `ID` or `URN`.

**P4-3.3 (MUST) Language tag present.** An implementation must record a `LANG` with every `TEXT` value and must not default it silently.

**P4-3.4 (MUST NOT) No caller supplied knowledge time.** An implementation must assign every `KTIME` itself and must reject an entry supplying one.

**P4-3.5 (MUST) Datatype and unit systems named.** An implementation must record the datatype system with every `DATATYPE` and the unit system with every `UNIT`, and must not rely on a single implicit system.

**P4-3.6 (MUST) Three valued domain used unchanged.** An implementation must use the truth domain of `Part 2` section 6.2 wherever it holds or reports a truth value and must not introduce a two valued reduction.

### 3.2 The triad: concept, designation, representation

This section is the foundation of the part and the reason a governed definition is not a dictionary entry.

A governed definition is three things at once, and they are three artifacts rather than one artifact with three views.

The **concept** is what is meant. It is language independent, structure independent, and it is the unit of identity. Two systems that agree on the concept and disagree on everything else are interoperable; two systems that agree on the term and disagree on the concept are worse than not integrated, because they will exchange data successfully and mean different things by it.

The **designation** is what it is called. There may be several per concept and several per language, with statuses: one preferred, others admitted, others deprecated. A designation is not the concept and must not be treated as its identifier, because designations change and a designation used as a key makes a rename a breaking change.

The **representation** is how it is expressed as data: datatype, unit, precision, format, cardinality, and the permissible value set that realises it. A concept may have more than one representation in different contexts, and the same representation may serve more than one concept, so the relation is neither one to one nor derivable.

The framing is not invented here. ISO 704:2022 establishes the links between objects, concepts, definitions and designations, and its separation of the concept from its designation is the whole basis of terminology work. ISO/IEC 11179-3:2023 specifies common facilities for identification, designation, definition and registration of a registry item, which is the same separation applied to a registry. ISO/IEC 11179-31:2023 supplies the representation side, in which a data element is a data element concept bound to a value domain, so that the concept and its expression are separately registrable.

What is invented here is the consequence. The three parts of the triad have **different change rates and different consequences of change**, and holding them as one field makes the three indistinguishable.

A designation change is nearly always harmless to meaning and nearly always breaks something, because designations are used as keys in places nobody has enumerated.

A representation change is nearly always harmless to meaning and breaks things detectably: a datatype narrows and something fails to load.

A concept change is nearly always harmless to every consumer's operation and destroys the meaning of everything downstream, silently, permanently and retrospectively. It is the only one of the three whose damage is invisible, and it is therefore the one the part is built around.

**P4-3.7 (MUST) Three artifacts, separately stored.** An implementation must hold the concept, its designations and its representations as distinct, separately addressable and separately versionable artifacts.

**P4-3.8 (MUST) Concept is the identity.** An implementation must use the concept identity as the persistent identity of a governed definition and must not use a designation, a code, a datatype or a physical location as that identity.

**P4-3.9 (MUST NOT) No designation as a key.** An implementation must not require a designation in order to address a concept, a definition version or a representation, and must expose a designation independent identifier at every interface.

**P4-3.10 (MUST) Many to many admitted.** An implementation must permit a concept to carry more than one representation and a representation to serve more than one concept, and must record each binding explicitly.

**P4-3.11 (MUST) Separate change records.** An implementation must record a change to a designation, a change to a representation and a change to a concept as distinct events with distinct change kinds, per section 3.8.

**P4-3.12 (MUST NOT) No inference of concept stability.** An implementation must not treat an unchanged designation or an unchanged representation as evidence that the concept is unchanged.

### 3.3 Entity inventory

Every entity is immutable once written. A change is a new row; nothing specified in this part is ever updated in place, for the reason `Part 1` section 3.2 gives and for the additional reason that the whole value of this component is the recoverability of a past meaning, which an editable record cannot supply.

| Group | Entity | Purpose |
| --- | --- | --- |
| Concept | `concept` | The persistent identity of a governed meaning. |
| Concept | `concept_relation` | A declared relation between concepts, of a registered kind. |
| Definition | `definition_version` | One immutable state of a governed definition. |
| Definition | `definition_text` | The natural language statement, per language. |
| Definition | `designation` | One term naming a concept, per language, with status. |
| Definition | `representation` | Datatype, unit, precision, format, cardinality. |
| Definition | `value_domain_binding` | The relation to a `Part 10` permissible value set. |
| Definition | `change_declaration` | The declared kind of a version increment and its reasoning. |
| Definition | `classification_instance` | One test instance with its asserted membership. |
| Definition | `classification_run` | One execution of a test set against a version pair. |
| Definition | `approval_citation` | The `Part 1` resolution establishing approval. |
| Definition | `effectivity_assertion` | The application time interval over which a version is in force. |
| Model | `model` | The persistent identity of a model. |
| Model | `model_version` | One immutable state of a model. |
| Model | `model_element` | One addressable element of a model version. |
| Model | `realisation_relation` | An element of one layer realising an element of another. |
| Model | `element_definition_binding` | A model element's binding to a governed concept. |
| Model | `inferential_model_interface` | The declared inputs and outputs of an inferential model. |
| Lineage | `lineage_node` | An addressable element a lineage edge may connect. |
| Lineage | `lineage_edge` | One asserted derivation relation. |
| Lineage | `lineage_assertion_source` | Who or what asserted an edge, and by what means. |
| Lineage | `lineage_completeness` | The declared completeness of a node's upstream set. |
| Lineage | `lineage_frontier` | A declared terminus of a lineage graph. |
| Lineage | `lineage_divergence` | A recorded disagreement with `Part 3` instance lineage. |
| Dependency | `dependent_registration` | Another component's declared dependency on a definition version. |
| Dependency | `dependency_source_state` | The availability and currency of each dependency source. |
| Impact | `proposed_change` | A described but unmade change. |
| Impact | `impact_analysis_run` | One pinned assessment. |
| Impact | `impact_member` | One affected thing, with its consequence class. |
| Impact | `impact_pin` | One artifact the analysis depended on. |
| Registry | `datatype_system_registration` | A registered datatype system. |
| Registry | `unit_system_registration` | A registered unit system. |
| Registry | `concept_relation_kind_registration` | A registered concept relation kind. |
| Registry | `model_kind_registration` | A registered model kind and layer set. |
| Registry | `lineage_frontier_kind_registration` | A registered lineage frontier kind. |
| Registry | `dependency_kind_registration` | A registered dependency kind and its owning component. |
| Registry | `path_scheme_registration` | A registered path scheme. |

**P4-3.13 (MUST) Entity coverage.** An implementation must be able to state, for every entity in the table above, where the information it carries is held, or that the entity is not applicable because the corresponding optional capability is not provided.

**P4-3.14 (MUST NOT) No update in place.** An implementation must not represent any state change specified by this part as a modification or deletion of a previously written row.

**P4-3.15 (MUST NOT) No definition amendment.** An implementation must not alter the concept, definition text, designations, representation, classification test set or change declaration of a recorded definition version, and must record any correction as a new version with its own change declaration.

### 3.4 The concept

`concept` fields:

| Field | Type | Required | Cardinality | Absence means |
| --- | --- | --- | --- | --- |
| `concept_id` | `ID` | yes | 1 | n/a |
| `concept_urn` | `URN` | yes | 1 | n/a |
| `created_ktime` | `KTIME` | yes | 1 | n/a |
| `domain` | `URN` | yes | 1..n | n/a. The subject field within which the concept is governed. |
| `steward` | `ACTOR` | yes | 1 | n/a. The party accountable for the concept's definition. |
| `superseded_by_concept_id` | `ID` | no | 0..1 | The concept has not been superseded by a different concept. |
| `retired_ktime` | `KTIME` | no | 0..1 | The concept has not been retired. Never means it is in use. |

`concept_relation` fields carry a `from_concept_id`, a `to_concept_id`, a registered `kind`, an `asserted_by`, an `asserted_ktime` and a `justification`. The minimum registered kinds are `GENERALISATION`, being that one concept subsumes another; `PART_WHOLE`; `ASSOCIATIVE`; `EQUIVALENCE_ASSERTED`, being a claim that two concepts are the same, which is a claim and not a merger; and `DISJOINT`.

`EQUIVALENCE_ASSERTED` is deliberately not a merger. Two concepts asserted equivalent remain two concepts with two identities and two histories, because the assertion may be wrong and because merging is irreversible. Merging two concepts destroys the ability to answer what each meant before the merge, which is the purpose question of section 1.1. Clause P4-3.19 forbids it.

**P4-3.16 (MUST) Steward recorded.** An implementation must record an accountable steward for every concept and must not record a component, a team mailbox or a system as the steward where the steward must be a party who can be asked what the concept means.

**P4-3.17 (MUST) Domain recorded.** An implementation must record at least one governing domain for every concept, since a designation is only unambiguous within a domain.

**P4-3.18 (MUST) Relations attributed and justified.** An implementation must record an asserting actor and a justification for every concept relation and must not infer a relation from a designation, a datatype or a lineage edge.

**P4-3.19 (MUST NOT) No concept merger.** An implementation must not merge two concept identities, must record an asserted equivalence as a relation, and must retain both identities and both histories.

**P4-3.20 (MUST NOT) No concept deletion.** An implementation must not delete a concept and must record retirement as an appended fact.

**P4-3.21 (MUST) Supersession by a different concept recorded as such.** An implementation must record, where a concept is replaced by a different concept rather than revised, the identity of the replacing concept, and must not represent the replacement as a version of the original.

### 3.5 Designations

`designation` fields:

| Field | Type | Required | Cardinality | Absence means |
| --- | --- | --- | --- | --- |
| `designation_id` | `ID` | yes | 1 | n/a |
| `concept_id` | `ID` | yes | 1 | n/a |
| `term` | `TEXT` | yes | 1 | n/a |
| `lang` | `LANG` | yes | 1 | n/a |
| `status` | `ENUM` | yes | 1 | n/a. One of `PREFERRED`, `ADMITTED`, `DEPRECATED`, `SUPERSEDED`, `PROHIBITED`. |
| `designation_kind` | `ENUM` | yes | 1 | n/a. One of `TERM`, `ABBREVIATION`, `SYMBOL`, `CODE`, `LEGACY_IDENTIFIER`. |
| `scope` | `URN` | no | 0..n | The designation applies throughout the concept's domains. |
| `asserted_ktime` | `KTIME` | yes | 1 | n/a |
| `retired_ktime` | `KTIME` | no | 0..1 | The designation has not been retired. |

Two statuses are worth distinguishing carefully. `DEPRECATED` means the term should no longer be used and remains valid for reading historical data. `PROHIBITED` means the term must not be used and, critically, is recorded because it is ambiguous or misleading rather than merely obsolete. A prohibited designation is the mechanism by which an organisation records that a word means two things and must be avoided, which is more useful than silence and is invisible in a dictionary that holds only current terms.

`LEGACY_IDENTIFIER` exists because every real estate contains column names, field codes and message tags that designate a concept and that nobody would call a term. Registering them as designations of a known status is how a rename is made analysable, and refusing to register them is how a lineage graph ends up connected by name matching, per section 11.6.

**P4-3.22 (MUST) Exactly one preferred designation per language and scope.** An implementation must permit at most one designation of status `PREFERRED` for a concept in any one language and scope, and must report a violation rather than selecting between candidates.

**P4-3.23 (MUST) Status recorded.** An implementation must record a status for every designation and must not default it.

**P4-3.24 (MUST) Deprecated designations remain resolvable.** An implementation must continue to resolve a deprecated or superseded designation to its concept and must not remove it.

**P4-3.25 (MUST) Prohibition reasoned.** An implementation must record the reason a designation is `PROHIBITED` and must be able to report every prohibited designation.

**P4-3.26 (MUST) Legacy identifiers registrable.** An implementation must permit a physical column name, field code or message tag to be registered as a designation of kind `LEGACY_IDENTIFIER`, so that a rename is analysable.

**P4-3.27 (MUST) Ambiguity reported, not resolved.** An implementation must report where one designation in one language and scope resolves to more than one concept, and must not select between them, per section 7.2.

**P4-3.28 (MUST NOT) No designation reuse across concepts without a scope.** An implementation must not admit a designation identical to an existing one for a different concept in the same language unless a distinguishing scope is recorded.
### 3.6 Definition text and its quality requirements

A definition text is the only part of the triad a person reads, and it is the part on which every downstream interpretation rests. Requiring it to exist is not sufficient; the field is populated in every dictionary in the world and is frequently useless.

ISO/IEC 11179-4 supplies requirements for the formulation of data definitions and this part adopts them as clauses rather than restating them as advice. Its account, as reported in secondary sources, requires that a definition be stated in the singular, state what the concept is rather than only what it is not, be a descriptive phrase or sentence, contain only commonly understood abbreviations, and not embed definitions of other data. ISO 704:2022 supplies the general principles for writing definitions and the object, concept, definition, designation chain within which they sit.

Four additional requirements are added here and are not from either source.

**No circularity within a domain.** A definition that uses the designation of a concept whose own definition uses the designation of the first has defined nothing. Circularity is detectable within the registry and clause P4-3.34 requires it to be detected.

**Every used term registered or declared primitive.** A definition text using a governed term must reference that term's concept, and a definition text using an ungoverned term must be admissible with the term declared primitive. The count of undeclared terms is a signal, per section 8.5. This is the same mechanism `Part 2` section 3.13 applies to rule declarations, applied to prose.

**Exclusions stated where the boundary is contested.** A definition of a concept whose boundary is disputed must state what is excluded. This is a requirement about the hard cases and it is the requirement most likely to be resisted, because stating exclusions is where the disagreement surfaces.

**Provenance of the text.** Where a definition text is taken from a regulation, a standard, a contract or an industry glossary, the source must be cited. A definition adopted from a regulation and then edited is a different definition, and the edit is invisible without the citation.

`definition_text` fields:

| Field | Type | Required | Cardinality | Absence means |
| --- | --- | --- | --- | --- |
| `text_id` | `ID` | yes | 1 | n/a |
| `definition_version_id` | `ID` | yes | 1 | n/a |
| `lang` | `LANG` | yes | 1 | n/a |
| `is_authoritative_language` | `TRUTH` | yes | 1 | n/a |
| `text` | `TEXT` | yes | 1 | n/a |
| `exclusions` | `TEXT` | no | 0..1 | No boundary is contested, which is a positive claim. |
| `source_citation` | `CITEREF` | no | 0..1 | The text is original to this organisation. |
| `source_relation` | `ENUM` | no | 0..1 | Required where a source is cited. One of `ADOPTED_VERBATIM`, `ADOPTED_MODIFIED`, `DERIVED`, `CONTRADICTS_SOURCE`. |
| `used_term_reference` | `ID` | no | 0..n | No governed term is used, or none was identified. |
| `primitive_term` | `TEXT` | no | 0..n | No term was declared primitive. |

`CONTRADICTS_SOURCE` is admissible and is the member that earns the enumeration. An organisation whose internal definition of a measure differs from the regulatory definition it reports against has a fact of considerable consequence, and the alternative to recording it is that the difference lives in somebody's head.

**P4-3.29 (MUST) Definition text present in at least one language.** An implementation must hold at least one definition text for every definition version and must designate exactly one language authoritative.

**P4-3.30 (MUST) Singular and positive.** An implementation must require a definition text to be stated in the singular and to state what the concept is, and must refuse one that states only what the concept is not.

**P4-3.31 (MUST) Descriptive phrase or sentence.** An implementation must require a definition text to be a descriptive phrase or one or more sentences, and must refuse a text that is only a designation, a synonym list or a reference to another definition.

**P4-3.32 (MUST NOT) No embedded definitions.** An implementation must refuse a definition text that defines a second concept within itself, and must require that concept to be registered and referenced.

**P4-3.33 (MUST) Terms referenced or declared primitive.** An implementation must require every governed term used in a definition text to reference its concept, must permit an ungoverned term to be declared primitive, and must be able to report every term that is neither.

**P4-3.34 (MUST) Circularity detected.** An implementation must detect a cycle in the graph of definition texts referencing concepts and must refuse a definition version that closes one.

**P4-3.35 (MUST) Exclusions stated where contested.** An implementation must require an exclusions statement wherever the steward declares the concept's boundary contested, and must record the declaration either way.

**P4-3.36 (MUST) Source cited and relation stated.** An implementation must record a source citation and a source relation wherever a definition text was taken from or derived from an external source.

**P4-3.37 (MUST) Contradiction of a source recorded.** An implementation must record `CONTRADICTS_SOURCE` where the definition differs in effect from the cited source and must be able to report every such definition.

**P4-3.38 (MUST NOT) No translated text as authoritative.** An implementation must not designate more than one language authoritative and must not treat a translation as independently governing, consistently with `Part 1` clause P1-3.31.

### 3.7 Representation and value domain binding

`representation` fields:

| Field | Type | Required | Cardinality | Absence means |
| --- | --- | --- | --- | --- |
| `representation_id` | `ID` | yes | 1 | n/a |
| `definition_version_id` | `ID` | yes | 1 | n/a |
| `datatype` | `DATATYPE` | yes | 1 | n/a |
| `datatype_system` | `PIN` | yes | 1 | n/a |
| `unit` | `UNIT` | no | 0..1 | The concept is not a measured quantity. Required where it is. |
| `unit_system` | `PIN` | no | 0..1 | Required wherever a unit is present. |
| `precision` | `TEXT` | no | 0..1 | No precision is constrained. Reportable for numeric datatypes. |
| `scale` | `COUNT` | no | 0..1 | As above. |
| `format` | `TEXT` | no | 0..1 | No format is constrained. |
| `cardinality_min` | `COUNT` | yes | 1 | n/a |
| `cardinality_max` | `COUNT` | no | 0..1 | Unbounded. Absence is a positive claim of unboundedness. |
| `null_semantics` | `ENUM` | yes | 1 | n/a. One of `NOT_PERMITTED`, `MEANS_ABSENT`, `MEANS_WITHHELD`, `MEANS_UNKNOWN`, `MEANS_NOT_APPLICABLE`, `UNDECLARED`. |
| `context` | `URN` | no | 0..n | The representation applies in every context of the concept. |

The `null_semantics` field is the field most often absent and most consequential. `Part 1` distinguishes absent from withheld. `Part 2` yields `INDETERMINATE` for a withheld path and a distinct code for an undeclared one. `Part 3` requires a negative citation to declare whether its search was complete. All three of those distinctions arrive at the physical layer as an empty column, and this is the only place in the standard where the organisation says which of five things an empty column means. A representation whose null semantics are `UNDECLARED` is admissible, is truthful, and is separately countable, because a system in which most representations are undeclared has three components maintaining a distinction that is thrown away at the boundary.

`value_domain_binding` fields carry the `representation_id`, a `PIN` to the `Part 10` permissible value set version, a `binding_kind` of `ENUMERATED`, `SUBSET_OF`, `SUPERSET_ASSERTED` or `UNCONSTRAINED`, and an `asserted_by` and `asserted_ktime`.

**P4-3.39 (MUST) Datatype and its system recorded.** An implementation must record a datatype and the registered system it is drawn from for every representation.

**P4-3.40 (MUST) Unit required for a measured quantity.** An implementation must require a unit and unit system for every representation of a concept the steward has declared a measured quantity, and must refuse one lacking it.

**P4-3.41 (MUST) Cardinality recorded.** An implementation must record a minimum cardinality for every representation and must treat an absent maximum as an assertion of unboundedness.

**P4-3.42 (MUST) Null semantics declared.** An implementation must record a null semantics value for every representation, must permit `UNDECLARED`, and must be able to report every representation carrying it.

**P4-3.43 (MUST NOT) No inference of null semantics.** An implementation must not infer null semantics from a datatype, a cardinality or the behaviour of a physical store.

**P4-3.44 (MUST) Value set bound by pin.** An implementation must record a pin to the `Part 10` permissible value set version wherever a representation is constrained by one, and must not enumerate the set's members itself.

**P4-3.45 (MUST NOT) No local value set membership.** An implementation must not hold, extend or correct the membership of a permissible value set, per section 12.10.

**P4-3.46 (MUST) Precision reportable where absent.** An implementation must be able to report every representation of a numeric datatype for which no precision or scale is recorded, since an unconstrained numeric representation is the mechanism by which two systems disagree about the same figure.

### 3.8 Version identity and the change kind taxonomy

This section and the next are the substance of the part.

A definition version is an immutable state of a governed definition. A version increment carries a **declared change kind**, from a closed set, and the kind determines what consumers must do. The set is closed because a consumer branches on it, and an unrecognised kind will be treated as harmless.

Nine kinds. The table is normative.

| Kind | What changed | Consequence for a consumer | Concept identity |
| --- | --- | --- | --- |
| `EDITORIAL` | Spelling, grammar, formatting, an added example. The definition text's effect is unchanged. | None. | Unchanged. |
| `CLARIFYING` | The definition text changed so as to state the same extension more precisely. | None, and the claim requires the test of section 3.9. | Unchanged. |
| `NARROWING` | The extension is smaller. Objects that fell under the concept no longer do. | Historical data is reclassified. Consumers relying on population size or membership are affected. | Unchanged. |
| `BROADENING` | The extension is larger. | As above. | Unchanged. |
| `DESIGNATION_CHANGE` | A designation was added, deprecated, prohibited or had its status changed. | Consumers keyed on the designation break. Meaning is unaffected. | Unchanged. |
| `REPRESENTATION_CHANGE` | Datatype, unit, precision, scale, format, cardinality or null semantics changed. | Structural. Detectable. May lose precision. | Unchanged. |
| `VALUE_DOMAIN_CHANGE` | The bound permissible value set version changed. | Depends on the set's own change, which is `Part 10`'s. | Unchanged. |
| `RELATION_CHANGE` | A concept relation was added, removed or restated. | Consumers relying on subsumption or disjointness are affected. | Unchanged. |
| `CONCEPT_REPLACEMENT` | The concept itself is different. | **Not permitted as a version.** | Requires a new concept. |

`CONCEPT_REPLACEMENT` appears in the table in order to be refused. It is the change every organisation makes and calls a revision: the meaning of a measure is redefined, the identifier is kept because forty systems use it, and every one of those systems now reports something different under the same name with no signal. Clause P4-3.49 refuses it. The remedy is a new concept, with its own identity, its own designations and its own lineage, and the old concept superseded under clause P4-3.21, which forces every consumer to rebind explicitly and makes the rebinding countable.

`change_declaration` fields:

| Field | Type | Required | Cardinality | Absence means |
| --- | --- | --- | --- | --- |
| `declaration_id` | `ID` | yes | 1 | n/a |
| `definition_version_id` | `ID` | yes | 1 | n/a |
| `predecessor_version_id` | `ID` | no | 0..1 | This is the first version of the definition. Distinguished by `first_version`. |
| `first_version` | `TRUTH` | yes | 1 | n/a |
| `kinds` | `ENUM` | yes | 1..n | n/a. One or more members of the table above. |
| `extension_effect` | `ENUM` | yes | 1 | n/a. One of `UNCHANGED`, `SMALLER`, `LARGER`, `INCOMPARABLE`, `UNASSESSED`. |
| `retrospective` | `TRUTH` | yes | 1 | n/a. Whether the change applies to historical data. |
| `rationale` | `TEXT` | yes | 1 | n/a |
| `declared_by` | `ACTOR` | yes | 1 | n/a |
| `declared_ktime` | `KTIME` | yes | 1 | n/a |
| `impact_analysis_reference` | `PIN` | no | 0..1 | No impact analysis was run before the change. Reportable. |

`extension_effect` is recorded separately from `kinds` because the two are checked against each other. A version declaring `CLARIFYING` and an extension effect of `SMALLER` is internally inconsistent and clause P4-3.51 refuses it. `INCOMPARABLE` records a redefinition where neither extension contains the other, which is almost always a concept replacement in disguise and clause P4-3.52 requires it to be treated as one unless the steward justifies otherwise.

`retrospective` is the field that determines whether the past is reclassified. A narrowing that applies only prospectively leaves historical figures alone; one that applies retrospectively changes what every historical figure meant. Both occur, and the difference is invisible unless it is declared.

**P4-3.47 (MUST) Change kinds declared.** An implementation must require at least one change kind on every version increment other than a first version and must not default it.

**P4-3.48 (MUST) Multiple kinds permitted and enumerated.** An implementation must permit a version increment to carry more than one change kind and must record each, rather than recording only the most severe.

**P4-3.49 (MUST NOT) No concept replacement as a version.** An implementation must refuse a version increment declared or found to be a `CONCEPT_REPLACEMENT` and must require a new concept identity.

**P4-3.50 (MUST) Extension effect declared.** An implementation must require an extension effect on every version increment and must permit `UNASSESSED` only where the classification test set is absent.

**P4-3.51 (MUST) Kind and extension effect consistent.** An implementation must refuse a version increment whose declared kinds and declared extension effect are inconsistent, and must state the inconsistency in the refusal.

**P4-3.52 (MUST) Incomparable extension treated as replacement.** An implementation must treat an extension effect of `INCOMPARABLE` as a concept replacement, and must refuse the version increment unless the steward records a justification for treating it otherwise.

**P4-3.53 (MUST) Retrospectivity declared.** An implementation must require a retrospectivity value on every version increment whose extension effect is not `UNCHANGED`.

**P4-3.54 (MUST) Rationale and declarer recorded.** An implementation must record a rationale and a named declaring actor for every change declaration.

**P4-3.55 (MUST) Impact analysis reference recorded or its absence reportable.** An implementation must record the impact analysis a change declaration relied upon, and must be able to report every version increment made without one.

**P4-3.56 (MUST NOT) No inferred change kind.** An implementation must not infer a change kind from a textual difference, a datatype comparison or a designation comparison, and must require it to be declared by an actor.

### 3.9 The classification test set, and why it is the bridge

A declared change kind is a claim. The most consequential claim available is that a change is `CLARIFYING`, because it asserts that no consumer need do anything, and the assertion is exactly what somebody making a quiet narrowing will make.

Whether two definition texts denote the same extension cannot be established mechanically. This is the same limit `Part 2` section 13.2 records for the correspondence of a rule's statement to its declaration, and it has the same partial remedy.

If the steward supplies instances together with the asserted answer to whether each falls under the concept, then a proposed version can be tested against them. Agreement does not prove that the extension is unchanged. **Disagreement proves that it is not.** That asymmetry is the whole value, and it is why the test set is specified here as a component of the definition rather than in section 12.12 as a testing concern delegated to `Part 12`.

The instances that matter are the borderline ones. A test set of clear cases will agree across any change and prove nothing. Clause P4-3.60 therefore requires the set to contain instances the steward declares borderline, and section 8.5 requires the count of definitions whose test sets contain no borderline instance, because such a set is decoration.

`classification_instance` fields:

| Field | Type | Required | Cardinality | Absence means |
| --- | --- | --- | --- | --- |
| `instance_id` | `ID` | yes | 1 | n/a |
| `concept_id` | `ID` | yes | 1 | n/a. Bound to the concept, not to one version, so that it can be applied across versions. |
| `description` | `TEXT` | yes | 1 | n/a. The instance, described sufficiently for a person to classify it. |
| `instance_data` | `PIN` | no | 0..1 | The instance is described in prose only, so the test is a human judgement. |
| `asserted_membership` | `ENUM` | yes | 1 | n/a. One of `IN`, `OUT`, `BORDERLINE_IN`, `BORDERLINE_OUT`, `INDETERMINATE_BY_DESIGN`. |
| `rationale` | `TEXT` | yes | 1 | n/a. Why it falls where it falls. |
| `asserted_by` | `ACTOR` | yes | 1 | n/a |
| `first_version_id` | `ID` | yes | 1 | n/a. The version against which the assertion was first made. |

`INDETERMINATE_BY_DESIGN` records an instance the definition deliberately does not settle. It is admissible and valuable: it is how a steward records that a boundary case is known and unresolved, which is better than a set that appears to settle everything.

`classification_run` records the application of a concept's test set to a version pair, with the per instance results and a verdict of `CONSISTENT`, `INCONSISTENT`, `PARTIALLY_HUMAN` or `NOT_RUN`. `PARTIALLY_HUMAN` exists because instances described only in prose require a person to classify them, so the run is not fully mechanical and must not be reported as though it were.

**P4-3.57 (MUST) Test set bound to the concept.** An implementation must bind classification instances to the concept rather than to a single definition version, so that a version pair can be compared against the same instances.

**P4-3.58 (MUST) Test set required for a claim of unchanged extension.** An implementation must refuse a version increment declaring an extension effect of `UNCHANGED` where the concept has no classification test set.

**P4-3.59 (MUST) Test set run before admission.** An implementation must run the classification test set for every version increment whose extension effect is declared `UNCHANGED` and must record the run and its per instance results.

**P4-3.60 (MUST) Borderline instances required.** An implementation must require at least one instance of membership `BORDERLINE_IN` or `BORDERLINE_OUT` in the test set of any concept whose steward has declared its boundary contested, and must be able to report every test set containing none.

**P4-3.61 (MUST NOT) No admission on inconsistency.** An implementation must refuse a version increment declaring an extension effect of `UNCHANGED` whose classification run returned `INCONSISTENT`, and must state the disagreeing instances in the refusal.

**P4-3.62 (MUST) Human classification marked.** An implementation must record a run as `PARTIALLY_HUMAN` where any instance required a person to classify it, and must not present such a run as a mechanical check.

**P4-3.63 (MUST NOT) No generated instances.** An implementation must not create a classification instance by applying a definition to data and recording the result, and must record the provenance of every instance.

**P4-3.64 (MUST NOT) No correspondence claim from agreement.** An implementation must not report, present or record that two definition versions have been shown to denote the same extension on the basis of test set agreement.

**P4-3.65 (MUST) Instances re run on later versions.** An implementation must re run a concept's test set against every subsequent version increment and must record a divergence where the results change without a declared extension effect.
### 3.10 Approval and effectivity

The split between this component and `Part 1` is precise and is easy to get wrong in either direction.

This component owns **definition version identity** and **definition effectivity**: which version exists, and the interval of application time over which it governs. `Part 1` clause P1-12.9 forbids `Part 1` from assigning version identity to a definition, so the identity is unambiguously here.

`Part 1` owns **approval**: the act, with its signature, by which someone accepted responsibility for the definition, and the controlled document version in which the definition was published. `Part 1` section 12.4 requires this component to declare that it does not own the approval or effectivity of published renditions, and section 12.1 here makes that declaration.

A definition version therefore becomes authoritative by being approved through `Part 1`, and this component records the resolution outcome rather than a status of its own. The mechanism is the same one `Part 2` uses for rules, with one difference worth stating: a rule's text is the content of the document, whereas a definition is a structured artifact of which the document is a rendition. Both need `Part 1`'s approval; only one lives inside the document.

An unapproved definition version is **admissible**. This is a decision and it will be contested. The alternative is that a definition cannot be registered until it has been through a governance cycle, which guarantees that the registry lags the estate and that the real definitions live in spreadsheets. What the model requires instead is that the absence of approval be visible on the definition, in every read, and countable, per section 8.5.

`approval_citation` fields carry the `definition_version_id`, a `CITEREF` to the `Part 1` document version and locator, the whole resolution outcome envelope as a `PIN`, the `resolved_ktime`, and a `status` of `APPROVED`, `NOT_APPROVED`, `APPROVAL_UNRESOLVABLE` or `APPROVAL_NOT_SOUGHT`.

`effectivity_assertion` fields carry the `definition_version_id`, a `scope` of `URN` cardinality 1..n, `effective_from` and `effective_to` as `ATIME` with the second optional and its absence meaning open ended, an `asserted_by`, an `asserted_ktime`, and a `basis` of `INITIAL`, `SUPERSESSION`, `CORRECTION` or `WITHDRAWAL`. Retractions are recorded as new assertions naming the retracted one, on the append only pattern of `Part 1` section 3.2.

**P4-3.66 (MUST) Approval obtained, not asserted.** An implementation must obtain the approval status of every definition version by resolution against `Part 1` and must not hold an approval, a signature or an approver of its own.

**P4-3.67 (MUST) Resolution outcome recorded in full.** An implementation must record the whole resolution outcome envelope `Part 1` returned, including its basis and divergence flag, and must not record the resolved version identifier alone.

**P4-3.68 (MUST) Unapproved versions marked in every read.** An implementation must return the approval status with every definition version it returns, in every interface, projection and export, and must not omit it.

**P4-3.69 (MUST) Approval not sought distinguished from unresolvable.** An implementation must record `APPROVAL_NOT_SOUGHT` where no approval was ever pursued and `APPROVAL_UNRESOLVABLE` where a citation exists and did not resolve, and must not use one for the other.

**P4-3.70 (MUST) Unapproved versions countable.** An implementation must be able to report every definition version whose approval status is not `APPROVED`, by domain and by steward, and must include the counts in the signals of section 8.5.

**P4-3.71 (MUST) Effectivity asserted, not inferred from approval.** An implementation must record effectivity as an explicit assertion and must not infer an effective date from an approval date, consistently with `Part 1` section 3.5.

**P4-3.72 (MUST) Scope on every effectivity assertion.** An implementation must record at least one scope on every effectivity assertion and must not treat an unscoped assertion as global.

**P4-3.73 (MUST) At most one version in force per scope.** An implementation must permit at most one definition version of a concept to be in force in one scope at one application time, and must report the ambiguity outcome of section 7.2 rather than selecting between candidates.

**P4-3.74 (MUST) Correction by retraction and replacement.** An implementation must record a correction to an effectivity assertion as a retraction naming the earlier assertion and a replacement assertion, and must not modify the earlier one.

### 3.11 Information models, layers and realisation

`model` and `model_version` carry the persistent identity and the immutable states of a model. `model_version` fields include the `model_id`, a registered `kind`, a `layer`, a `document_citation` to the `Part 1` version that published it where one exists, a `created_ktime`, an `authored_by`, and an `element_count` derived from the elements recorded.

The layer enumeration is `CONCEPTUAL`, `LOGICAL`, `PHYSICAL` and `OTHER_REGISTERED`. The three named layers are the common decomposition and `OTHER_REGISTERED` exists because real estates contain canonical models, exchange models, dimensional models and semantic layers that do not fit the three, and forcing them into one of the three loses the distinction that mattered.

`model_element` carries the `model_version_id`, a `path` in a registered scheme, an `element_kind`, a `local_name`, and an optional binding to a governed concept.

`realisation_relation` is the entity that earns this section. It asserts that an element of one layer realises an element of another: that a physical column realises a logical attribute, that a logical attribute realises a conceptual property. Fields: `from_element`, `to_element`, `relation_kind` of `REALISES`, `PARTIALLY_REALISES`, `AGGREGATES`, `SPLITS_ACROSS` or `NOT_REALISED`, an `asserted_by`, an `asserted_ktime`, and a `justification`.

The requirement that matters is clause P4-3.79: a realisation relation must be declared and must not be inferred from name matching. Name matching is how nearly every real mapping is established, it is a guess, and it is wrong in the specific cases that cost money: two columns with the same name realising different concepts, and one concept realised by columns with different names. Section 11.6 names the mechanism.

`NOT_REALISED` is a positive assertion that a logical or conceptual element has no physical realisation. It is useful precisely because it is the thing nobody records: a concept the organisation has defined and does not capture, which is a gap in the estate rather than a gap in the registry.

`element_definition_binding` records that a model element realises a governed concept, with a `binding_kind` of `EXACT`, `NARROWER`, `BROADER`, `OVERLAPPING` or `ASSERTED_UNKNOWN`. `OVERLAPPING` is the honest answer for the very common case where a physical column carries a concept that is not quite the governed one, and recording it is better than an `EXACT` binding that is false.

**P4-3.75 (MUST) Model kind and layer recorded.** An implementation must record a registered kind and a layer for every model version and must not default either.

**P4-3.76 (MUST) Elements addressable in a registered scheme.** An implementation must record every model element with a path in a registered path scheme and must record the scheme.

**P4-3.77 (MUST) Element count derived.** An implementation must derive the element count of a model version from the elements recorded and must not accept it as an input.

**P4-3.78 (MUST) Realisation relations declared.** An implementation must record a realisation relation as an assertion with a named asserting actor and a justification.

**P4-3.79 (MUST NOT) No realisation by name matching.** An implementation must not create a realisation relation or an element definition binding by matching names, and must record any candidate produced by such a method as a proposal that is not a relation until an actor asserts it.

**P4-3.80 (MUST) Non realisation recordable.** An implementation must permit a relation of kind `NOT_REALISED` and must be able to report every conceptual or logical element carrying one.

**P4-3.81 (MUST) Binding kind recorded.** An implementation must record a binding kind on every element definition binding and must not default it to `EXACT`.

**P4-3.82 (MUST) Overlapping bindings reportable.** An implementation must be able to report every binding of kind `OVERLAPPING` or `ASSERTED_UNKNOWN`, since an impact analysis over such a binding is weaker than over an exact one.

**P4-3.83 (MUST NOT) No model content authority.** An implementation must not hold the model artifact as its own authoritative copy where the model is published as a controlled document, and must record the `Part 1` citation and treat its own holding as a registration of the model's structure.

### 3.12 Inferential models

An inferential model is registered here by identity, version and declared interface, and by nothing else. The reason is stated in section 1.4: an inferential model asserts nothing and can only be measured, so there is nothing in it to govern in the sense this part governs definitions.

What is governed is the interface, and the reason it is governed here rather than in `Part 13` is that the interface is a set of bindings to definitions. A scoring model whose input is described as customer tenure is binding to a concept, and if that concept is narrowed the model's meaning changes without the model changing. An impact analysis that cannot reach inferential models is incomplete in exactly the way that matters most, because a model is the consumer least likely to fail visibly when a definition shifts under it.

`inferential_model_interface` fields:

| Field | Type | Required | Cardinality | Absence means |
| --- | --- | --- | --- | --- |
| `interface_id` | `ID` | yes | 1 | n/a |
| `model_version_id` | `ID` | yes | 1 | n/a |
| `input_binding` | `ID` | yes | 1..n | n/a. One element definition binding per declared input. |
| `output_binding` | `ID` | yes | 1..n | n/a. One per declared output. |
| `training_period` | `TEXT` | no | 0..1 | The period of data the model was fitted on was not recorded. Materially weakening. |
| `training_definition_pin` | `PIN` | no | 0..n | The definition versions in force over the training period were not pinned. Reportable. |
| `invocation_reference` | `URN` | yes | 1 | n/a. The `Part 13` artifact this interface describes. |
| `declared_by` | `ACTOR` | yes | 1 | n/a |

`training_definition_pin` is the field that makes this section worth having. A model fitted on data produced under the 2027 definition of a measure and applied to data produced under the 2029 definition is measuring something it was not fitted for. Nothing detects this, nothing fails, and the model's outputs remain plausible. Pinning the definition versions in force over the training period is the only way the condition becomes visible, and clause P4-3.86 requires it or requires its absence to be reportable.

**P4-3.84 (MUST) Interface bound to definitions.** An implementation must record an element definition binding for every declared input and output of an inferential model version.

**P4-3.85 (MUST NOT) No model internals.** An implementation must not hold parameters, weights, training data or fitted structure, per clause P4-1.17.

**P4-3.86 (MUST) Training period definitions pinned or their absence reportable.** An implementation must record the definition versions in force over the training period of an inferential model, or must be able to report that they were not recorded.

**P4-3.87 (MUST) Training definition drift reportable.** An implementation must be able to report every inferential model version whose pinned training definitions have since been superseded by a version with an extension effect other than `UNCHANGED`.

**P4-3.88 (MUST) Invocation reference recorded.** An implementation must record the `Part 13` artifact each interface describes and must not describe an inferential model that has no such artifact.

**P4-3.89 (MUST NOT) No performance claims.** An implementation must not hold, assert or report the accuracy, fitness or performance of an inferential model, since it does not observe its behaviour.

### 3.13 Design lineage: nodes, edges and grain

Design lineage is what the design asserts about how data elements derive from one another. It is not what happened, which is `Part 3`'s instance lineage, and the two are related by the divergence check of section 3.15.

`lineage_node` carries an `ID`, a `node_kind` of `DEFINITION`, `MODEL_ELEMENT`, `PHYSICAL_STRUCTURE` or `EXTERNAL_REFERENCE`, a `reference` `URN`, an optional `path`, and a `grain`.

The grain enumeration is `ELEMENT`, being a single field, column or attribute; `STRUCTURE`, being a table, message or file; and `SYSTEM`. It is recorded on every node and on every edge, and the requirement that follows is the most practically consequential clause in this section.

**Structure level lineage is nearly useless for impact analysis.** An edge saying that a table derives from three tables tells an analyst that a change to any column of any of the three might affect any column of the first. Applied transitively over a real estate the answer is everything. Almost every lineage capability in existence is at structure level, is presented as lineage without qualification, and is used for impact analysis, which is the failure of section 11.4. Clause P4-3.92 requires the grain to be recorded on every edge and section 7.4 requires an impact analysis resting on structure level edges to say so.

`lineage_edge` fields:

| Field | Type | Required | Cardinality | Absence means |
| --- | --- | --- | --- | --- |
| `edge_id` | `ID` | yes | 1 | n/a |
| `from_node_id` | `ID` | yes | 1..n | n/a. More than one where the edge is an expression over several inputs. |
| `to_node_id` | `ID` | yes | 1 | n/a |
| `edge_kind` | `ENUM` | yes | 1 | n/a. Closed set below. |
| `grain` | `ENUM` | yes | 1 | n/a |
| `transform_reference` | `PIN` | no | 0..1 | No transformation artifact was pinned. Required for `EXPRESSION` and `AGGREGATION`. |
| `condition_reference` | `PIN` | no | 0..1 | Required for `CONDITIONAL` and `FILTER_DEPENDENCY`. |
| `semantic_effect` | `ENUM` | yes | 1 | n/a. One of `PRESERVES`, `NARROWS`, `LOSES_PRECISION`, `CHANGES_UNIT`, `CHANGES_MEANING`, `UNASSESSED`. |
| `asserted_ktime` | `KTIME` | yes | 1 | n/a |

The edge kind set is closed. Ten members. The table is normative.

| Kind | Means |
| --- | --- |
| `IDENTITY` | The same value, moved or copied, unchanged. |
| `RENAME` | The same value under a different designation. |
| `TYPE_CONVERSION` | The same value in a different representation. |
| `EXPRESSION` | A value computed from one or more inputs by a pinned transformation. |
| `AGGREGATION` | A value computed over a set of input values. |
| `LOOKUP` | A value obtained from another structure by a key. |
| `FILTER_DEPENDENCY` | An input that determined which values are present rather than what any value is. |
| `CONDITIONAL` | An input that determined which of several derivations applied. |
| `DEFAULT_SUBSTITUTION` | A value supplied where an input was absent. |
| `MANUAL_ENTRY` | A value supplied by a person rather than derived. |

`FILTER_DEPENDENCY` is the member almost never recorded and it matters more than most. A report filtered on a status code depends on that code's definition completely: narrow the definition of active and the report's population changes, and no value in the report was computed from the code. Every lineage tool that traces value derivation misses it, so a narrowing of a filter concept reaches nothing in the lineage graph and changes every figure downstream.

`DEFAULT_SUBSTITUTION` is the second such member. A default is a value with no upstream, and its presence in a lineage graph is the record that a null semantics decision was taken somewhere in a pipeline, which is the counterpart of the representation field of section 3.7.

`semantic_effect` of `CHANGES_MEANING` records an edge across which the concept differs. It is admissible and it is the strongest signal available that a concept binding somewhere is `OVERLAPPING` rather than `EXACT`, and section 8.5 requires the count.

**P4-3.90 (MUST) Closed edge kind set.** An implementation must record exactly one edge kind from the table above on every lineage edge and must not accept a kind outside the set.

**P4-3.91 (MUST NOT) No generic flow edge.** An implementation must not admit an edge whose kind means only that data moves, and must require one of the ten members.

**P4-3.92 (MUST) Grain recorded on every node and edge.** An implementation must record the grain of every lineage node and every lineage edge and must not default it.

**P4-3.93 (MUST) Filter and conditional dependencies recorded.** An implementation must record an edge of kind `FILTER_DEPENDENCY` or `CONDITIONAL` wherever an input determined which values are present or which derivation applied, and must not omit it on the ground that no value was computed from it.

**P4-3.94 (MUST) Transformation pinned where the kind requires it.** An implementation must record a pinned transformation artifact for every edge of kind `EXPRESSION` or `AGGREGATION` and a pinned condition for every edge of kind `CONDITIONAL` or `FILTER_DEPENDENCY`, or must record why none was available.

**P4-3.95 (MUST) Semantic effect declared.** An implementation must record a semantic effect on every edge, must permit `UNASSESSED`, and must be able to report every edge carrying it.

**P4-3.96 (MUST) Meaning changing edges reportable.** An implementation must be able to report every edge of semantic effect `CHANGES_MEANING` and must include the count in the signals of section 8.5.

**P4-3.97 (MUST NOT) No cycle in the lineage graph.** An implementation must detect a cycle in the lineage graph and must refuse an edge that closes one, since a design in which a value derives from itself is either an error or a recursion the design must state differently.
### 3.14 Lineage assertion provenance and frontiers

A lineage edge is an assertion. It can be wrong, and the ways it can be wrong depend entirely on how it was produced.

`lineage_assertion_source` fields:

| Field | Type | Required | Cardinality | Absence means |
| --- | --- | --- | --- | --- |
| `source_id` | `ID` | yes | 1 | n/a |
| `edge_id` | `ID` | yes | 1 | n/a |
| `method` | `ENUM` | yes | 1 | n/a. One of `DECLARED_BY_ACTOR`, `PARSED_FROM_CODE`, `PARSED_FROM_QUERY_LOG`, `DERIVED_FROM_MODEL_MAPPING`, `INFERRED_BY_NAME_MATCH`, `INFERRED_STATISTICALLY`, `IMPORTED_FROM_TOOL`, `UNRECORDED`. |
| `asserted_by` | `ACTOR` | yes | 1 | n/a |
| `tool_pin` | `PIN` | no | 0..1 | Required for every parsed, derived, inferred or imported method. |
| `source_artifact_pin` | `PIN` | no | 0..1 | The artifact parsed was not pinned. Reduces reproducibility. |
| `confirmed_by_actor` | `ACTOR` | no | 0..1 | No person has confirmed the assertion. |
| `confirmed_ktime` | `KTIME` | no | 0..1 | As above. |
| `asserted_ktime` | `KTIME` | yes | 1 | n/a |

The `tool_pin` requirement is the point of the section. An edge parsed by a lineage tool at version 3.2 is a claim by that tool at that version, and when the tool is upgraded the claims change, silently and in bulk. A lineage graph whose edges do not record the parser that produced them cannot be compared with itself across time, so nobody can tell whether the estate changed or the tool got better. Clause P4-3.99 requires the pin.

`INFERRED_BY_NAME_MATCH` and `INFERRED_STATISTICALLY` are admitted and are marked. They are guesses, they are frequently the only thing available, and the requirement is that they be distinguishable from assertions, not that they be excluded. Clause P4-3.101 forbids an inferred edge from being reported as declared, and section 7.4 requires an impact analysis resting on inferred edges to say so.

`confirmed_by_actor` records that a person looked at an inferred edge and accepted it. This is the only mechanism by which an inferred graph becomes an asserted one, and the proportion confirmed is a signal.

**Lineage frontiers.** A lineage graph terminates, and the same argument `Part 3` section 3.11 makes for chains of reasoning applies here: an undeclared terminus and a missing edge are indistinguishable in the record and require opposite responses. The concept is deliberately borrowed rather than reinvented, and section 13.7 records the question of whether it should be a shared concept across the standard.

`lineage_frontier` carries the `node_id`, a registered `kind`, a `declared_by`, a `declared_ktime`, a `justification` and an `expected_to_close` truth value. The minimum kinds:

| Kind | Means | Legitimate |
| --- | --- | --- |
| `EXTERNAL_SOURCE` | The value arrives from outside the organisation. | Yes, permanently. |
| `MANUAL_ENTRY` | A person supplies the value. | Yes. |
| `SYSTEM_OF_ORIGIN` | The value originates in a system declared to be the origin for it. | Yes. |
| `OPAQUE_SYSTEM` | A system supplies the value and exposes no derivation. | Yes as a statement of fact, and a defect in the estate. |
| `MEASUREMENT` | The value is a physical measurement or instrument reading. | Yes. |
| `NOT_YET_MAPPED` | The lineage has not been established. | No. This is work outstanding, not a terminus. |
| `FRONTIER_UNDECLARED` | The graph stops and no reason is recorded. | No. |

`NOT_YET_MAPPED` is separated from `FRONTIER_UNDECLARED` because the two are different states of the same defect: the first records that somebody knows the work is outstanding, the second that nobody has noticed. Both are illegitimate as termini and only the first is a plan.

**P4-3.98 (MUST) Method recorded on every edge.** An implementation must record an assertion method for every lineage edge and must not default it.

**P4-3.99 (MUST) Tool pinned where a tool produced the edge.** An implementation must record a pin to the tool and its version for every edge whose method is parsed, derived, inferred or imported, and must refuse an edge of such a method lacking one.

**P4-3.100 (MUST) Source artifact pinned where available.** An implementation must record a pin to the artifact parsed where the method is a parse, or must record that none was obtainable.

**P4-3.101 (MUST NOT) No inferred edge as declared.** An implementation must not report an edge of method `INFERRED_BY_NAME_MATCH` or `INFERRED_STATISTICALLY` as declared, and must carry the method with the edge in every read.

**P4-3.102 (MUST) Confirmation recorded separately.** An implementation must record a person's confirmation of an inferred edge as a distinct fact and must not alter the recorded method upon confirmation.

**P4-3.103 (MUST) Inferred proportion reportable.** An implementation must be able to report the proportion of edges by method, by domain and by system, and must include it in the signals of section 8.5.

**P4-3.104 (MUST) Every terminus is a declared frontier.** An implementation must record a frontier at every point at which a lineage graph terminates, and must record `FRONTIER_UNDECLARED` where no reason was supplied rather than recording nothing.

**P4-3.105 (MUST) Not yet mapped distinguished.** An implementation must record `NOT_YET_MAPPED` where the lineage is known to be incomplete and must not record a legitimate frontier kind in its place.

**P4-3.106 (MUST) Illegitimate frontiers reportable.** An implementation must be able to report every frontier of kind `NOT_YET_MAPPED` or `FRONTIER_UNDECLARED` and must include the counts in the signals of section 8.5.

### 3.15 Lineage completeness and divergence

`lineage_completeness` records, per node, whether the recorded upstream set is the complete set: a value of `COMPLETE`, `PARTIAL_KNOWN`, `PARTIAL_UNKNOWN` or `UNDECLARED`, with a `declared_by`, a `declared_ktime` and a `basis`.

The distinction between `PARTIAL_KNOWN` and `PARTIAL_UNKNOWN` is between knowing that something is missing and not knowing whether anything is. Both are common; only the first can be planned against.

`UNDECLARED` is the default state of every node in every real system and it is admissible for that reason. What clause P4-3.109 forbids is treating it as complete, because an impact analysis over a node of undeclared completeness has an unknown false negative rate and reporting it as an impact set is the failure of section 11.5.

**Divergence.** `Part 3` clause P3-3.105 requires that component to record the corresponding design lineage assertion where one exists, and clause P3-3.107 requires it to report every observed transformation unmatched by any assertion here. This section is the other half of that check, and the reciprocal is in section 12.3.

`lineage_divergence` fields carry a `divergence_kind` of `OBSERVED_NOT_ASSERTED`, being an actual derivation the design does not contain; `ASSERTED_NOT_OBSERVED`, being a design relation no run has exercised; `KIND_DISAGREEMENT`, being an edge both hold with different kinds; and `GRAIN_INCOMPARABLE`, being a pair that cannot be compared because the grains differ.

The two substantive kinds carry opposite meanings and both are valuable. `OBSERVED_NOT_ASSERTED` means either an undocumented process or a defect in the design record, and it is the more urgent. `ASSERTED_NOT_OBSERVED` means either dead design or an untested path, and over a long enough observation window it is the best available signal that a documented flow does not exist.

`GRAIN_INCOMPARABLE` is honest and is the commonest outcome in practice, because design lineage is usually asserted at structure level and instance lineage is observed at element level. Recording it prevents the comparison from silently succeeding.

**P4-3.107 (MUST) Completeness declared per node.** An implementation must record a completeness value for every lineage node and must not default it to `COMPLETE`.

**P4-3.108 (MUST) Partial known and unknown distinguished.** An implementation must distinguish a node known to be missing upstream edges from one whose completeness is unknown.

**P4-3.109 (MUST NOT) No inference of completeness.** An implementation must not treat a node of completeness `UNDECLARED` or `PARTIAL_UNKNOWN` as complete in any traversal, impact analysis or report.

**P4-3.110 (MUST) Divergence recorded, not resolved.** An implementation must record a divergence from `Part 3` instance lineage as a finding and must not create, alter or delete a design lineage edge in response to one.

**P4-3.111 (MUST) Both divergence directions reportable.** An implementation must be able to report divergences of kind `OBSERVED_NOT_ASSERTED` and `ASSERTED_NOT_OBSERVED` separately.

**P4-3.112 (MUST) Grain incomparability recorded.** An implementation must record `GRAIN_INCOMPARABLE` where the grains of the two lineages differ and must not report a comparison as agreeing.

**P4-3.113 (MUST) Design lineage exposed by pin.** An implementation must expose every design lineage assertion obtainable by pin, so that `Part 3` clause P3-3.105 can be satisfied.

### 3.16 Dependent registration

This section is what makes impact analysis possible and it is the section most likely to be omitted in an implementation, because it requires other components to cooperate.

A lineage graph contains data flows. It does not contain the rule that cites a term, the determination that relied on it, the schema element that binds to it, the report a regulator reads, or the contract that defines a service level against it. Those dependencies are held by the components that own them, and this component's job is to index them.

`dependent_registration` fields:

| Field | Type | Required | Cardinality | Absence means |
| --- | --- | --- | --- | --- |
| `registration_id` | `ID` | yes | 1 | n/a |
| `definition_version_id` | `ID` | yes | 1 | n/a. The version depended upon. |
| `concept_id` | `ID` | yes | 1 | n/a. Recorded as well as the version, so that a dependency survives a version increment. |
| `dependent_reference` | `URN` | yes | 1 | n/a. The dependent thing. |
| `dependency_kind` | `ENUM` | yes | 1 | n/a. Registered under section 9.8, with the minimum set below. |
| `owning_component` | `URN` | yes | 1 | n/a |
| `registered_ktime` | `KTIME` | yes | 1 | n/a |
| `binding_strength` | `ENUM` | yes | 1 | n/a. One of `PINNED_VERSION`, `TRACKS_LATEST`, `UNPINNED_UNKNOWN`. |
| `withdrawn_ktime` | `KTIME` | no | 0..1 | The dependency has not been withdrawn. |

The minimum dependency kinds and their sources:

| Kind | Source | What it records |
| --- | --- | --- |
| `RULE_TERM_REFERENCE` | `Part 2` | A rule whose declaration uses the term, per `Part 2` clause P2-12.8. |
| `DETERMINATION_RELIANCE` | `Part 3` | A determination that relied on the definition, per `Part 3` section 3.18. |
| `SCHEMA_ELEMENT_BINDING` | `Part 9` | A schema element claiming to realise the concept. |
| `REFERENCE_SET_REALISATION` | `Part 10` | A value set realising the representation. |
| `DECISION_CRITERION` | `Part 5` | A selection criterion expressed over the concept. |
| `POLICY_ATTRIBUTE` | `Part 7` | An authorisation policy reading the concept as an attribute. |
| `PUBLISHED_DOCUMENT` | `Part 1` | A controlled document publishing or citing the definition. |
| `INFERENTIAL_MODEL_INPUT` | This part | An inferential model input binding, per section 3.12. |
| `EXTERNAL_OBLIGATION` | Declared | A regulatory return, contract or public commitment expressed over the concept. |

`binding_strength` of `TRACKS_LATEST` is the dangerous value. A dependent that tracks the latest version of a definition will silently change meaning on a narrowing, which is the whole failure of section 1.3. `PINNED_VERSION` breaks visibly instead. Both are legitimate and the impact classification of section 3.17 treats them differently, because a pinned dependent suffers a structural break and an unpinned one suffers semantic drift.

`EXTERNAL_OBLIGATION` is the kind with no component to supply it, and it is the one that matters most. A regulatory return defined over a measure is the reason a narrowing of that measure is a serious event, and no component in this standard holds it. Clause P4-3.119 requires it to be registrable and section 8.5 requires the count of concepts carrying one, so that the concepts with external consequences are identifiable.

**P4-3.114 (MUST) Dependencies registrable by other components.** An implementation must accept dependent registrations from the components named in the table above and must record the registering component.

**P4-3.115 (MUST) Both version and concept recorded.** An implementation must record both the definition version depended upon and its concept, so that a dependency remains discoverable across version increments.

**P4-3.116 (MUST) Binding strength recorded.** An implementation must record a binding strength on every dependent registration and must not default it.

**P4-3.117 (MUST) Source state tracked.** An implementation must record, per dependency source, when it last supplied registrations and whether it is currently available, and must be able to report a source that has ceased to supply them.

**P4-3.118 (MUST) Unpinned dependents reportable.** An implementation must be able to report every dependent of binding strength `TRACKS_LATEST` or `UNPINNED_UNKNOWN` by concept, since those are the dependents a semantic change reaches silently.

**P4-3.119 (MUST) External obligations registrable.** An implementation must permit a dependency of kind `EXTERNAL_OBLIGATION` to be registered by a declaring actor, must record the actor, and must be able to report every concept carrying one.

**P4-3.120 (MUST NOT) No dependency inference.** An implementation must not create a dependent registration by inference and must record every one as supplied by a named component or a named actor.

**P4-3.121 (MUST) Withdrawal recorded, not deleted.** An implementation must record the withdrawal of a dependency as an appended fact and must not remove the registration.

### 3.17 Impact analysis

An impact analysis is a pinned, repeatable assessment of what a proposed change would affect. It is prospective, it is not an approval, and it is not the transitive closure of the lineage graph.

`proposed_change` describes an unmade change: the target, the change kinds proposed, the proposed extension effect, the proposed retrospectivity, and the proposer. A proposed change is recorded so that the analysis can be reproduced and so that the analysis that was actually run before a change can be compared with the change that was actually made. Clause P4-3.129 requires that comparison.

`impact_analysis_run` carries the proposed change, the run's bounds, its pins, its outcome per section 7.4, and its counts. `impact_pin` records every artifact the analysis read: the lineage graph state, each dependency source and its currency, the model versions traversed, and the registries.

`impact_member` fields:

| Field | Type | Required | Cardinality | Absence means |
| --- | --- | --- | --- | --- |
| `member_id` | `ID` | yes | 1 | n/a |
| `run_id` | `ID` | yes | 1 | n/a |
| `affected_reference` | `URN` | yes | 1 | n/a |
| `reached_by` | `ENUM` | yes | 1..n | n/a. One or more of `LINEAGE`, `DEPENDENT_REGISTRATION`, `REALISATION`, `CONCEPT_RELATION`, `MODEL_INTERFACE`. |
| `path` | `ID` | yes | 1..n | n/a. The edges or registrations by which it was reached. |
| `distance` | `COUNT` | yes | 1 | n/a. Hops from the target. |
| `consequence_class` | `ENUM` | yes | 1 | n/a. Closed set below. |
| `confidence` | `ENUM` | yes | 1 | n/a. One of `ASSERTED_PATH`, `INFERRED_PATH`, `INCOMPLETE_PATH`. |
| `assessed_by` | `ACTOR` | no | 0..1 | The consequence class was derived, not assessed by a person. |

The consequence class set is closed. Seven members. The table is normative.

| Class | Means | Visible on change |
| --- | --- | --- |
| `SEMANTIC_DRIFT` | The dependent continues to operate and now means something else. | **No.** |
| `STRUCTURAL_BREAK` | The dependent fails. | Yes, immediately. |
| `VALUE_DOMAIN_BREAK` | A value the dependent expects is no longer permissible, or a new one appears. | Usually. |
| `PRECISION_LOSS` | The dependent continues and its values are less precise or differently rounded. | No. |
| `HISTORICAL_RECLASSIFICATION` | Past data now falls differently under the concept. | No, and it affects figures already published. |
| `NO_IMPACT_ASSERTED` | A named actor assessed the member and found no consequence. | n/a |
| `IMPACT_UNASSESSED` | The member was reached and its consequence has not been assessed. | n/a |

`SEMANTIC_DRIFT` is the class the whole part exists to surface. Nothing fails, no alert fires, no test breaks, and every consumer of the affected thing now reports something different. It is systematically absent from every impact report produced by reachability alone, because reachability tells you what is connected and not what the connection means.

`HISTORICAL_RECLASSIFICATION` is the second. It arises only where the proposed change is retrospective, and its consequence is that figures already published are now wrong, or now right, and either way differ from what the organisation said. No lineage traversal produces it; it follows from the retrospectivity declaration of section 3.8.

`IMPACT_UNASSESSED` is the default and is honest. This component reaches members and classifies what it can derive: a structural break follows from a representation change, a value domain break from a value domain change. It cannot derive whether a semantic narrowing matters to a particular report, which is a judgement. Clause P4-3.126 forbids it from assessing that itself, on the same ground `Part 3` clause P3-3.90 forbids computing materiality.

**P4-3.122 (MUST) Impact spans every source.** An implementation must assemble an impact set from design lineage, dependent registrations, realisation relations, concept relations and inferential model interfaces, and must record which sources it consulted.

**P4-3.123 (MUST) Reached by recorded.** An implementation must record, for every impact member, by which of the five means it was reached and the path by which it was reached.

**P4-3.124 (MUST) Consequence class on every member.** An implementation must record a consequence class from the table above on every impact member.

**P4-3.125 (MUST) Semantic drift derived where derivable.** An implementation must classify as `SEMANTIC_DRIFT` every member reached through a dependent registration of binding strength `TRACKS_LATEST` where the proposed extension effect is not `UNCHANGED`.

**P4-3.126 (MUST NOT) No assessment of material consequence.** An implementation must not assess whether a semantic change matters to a particular dependent, and must record `IMPACT_UNASSESSED` until a named actor assesses it.

**P4-3.127 (MUST) Historical reclassification derived from retrospectivity.** An implementation must classify as `HISTORICAL_RECLASSIFICATION` every member reached from a proposed change whose retrospectivity is true and whose extension effect is not `UNCHANGED`.

**P4-3.128 (MUST) Confidence recorded per member.** An implementation must record whether a member was reached by an asserted path, an inferred path or a path through a node of incomplete lineage.

**P4-3.129 (MUST) Analysis compared with the change made.** An implementation must be able to compare the proposed change an impact analysis assessed with the change declaration subsequently recorded, and must report where they differ.

**P4-3.130 (MUST) Pins recorded.** An implementation must record a pin for every artifact and every dependency source an impact analysis read, including the currency of each source.

**P4-3.131 (MUST NOT) No impact set as approval.** An implementation must not represent an impact analysis as an approval, an authorisation or a recommendation, and must not permit an interface to imply that a change is safe.
### 3.18 Projections

Every read is a projection: a pure function of the recorded rows, holding no state of its own, recomputable at any time.

| Projection | Yields |
| --- | --- |
| `definition_at` | The definition version in force for a concept at an application time and a knowledge time, with its approval status. |
| `concept_by_designation` | The concepts a designation resolves to in a language and scope, with the ambiguity outcome where more than one. |
| `designations_of` | Every designation of a concept with its status and kind, including deprecated and prohibited. |
| `definition_history` | Every version of a concept in order, with change kinds, extension effects and retrospectivity. |
| `extension_change_history` | Only those versions whose extension effect was not `UNCHANGED`, which is the history that matters to a consumer. |
| `unapproved_definitions` | Every version whose approval status is not `APPROVED`, by domain and steward. |
| `undeclared_null_semantics` | Every representation whose null semantics are `UNDECLARED`. |
| `contested_boundaries` | Every concept whose boundary is declared contested, with its exclusions statement and test set state. |
| `test_set_state` | Per concept, the test set size, the borderline instance count and the most recent run result. |
| `circularity` | Every cycle detected in the definition text reference graph. |
| `model_layers_of` | The model versions and elements at each layer for a subject area, with realisation relations. |
| `unrealised_elements` | Every conceptual or logical element with a `NOT_REALISED` relation or with none at all. |
| `binding_quality` | Element definition bindings by binding kind, so that overlapping and unknown bindings are visible. |
| `lineage_upstream_of` | The upstream graph of a node, with edge kinds, grains, methods and frontiers, to declared bounds. |
| `lineage_downstream_of` | The downstream graph, which is the direction impact analysis traverses. |
| `lineage_by_method` | Edges partitioned by assertion method, so that inferred edges are separable from declared ones. |
| `lineage_completeness_report` | Nodes by declared completeness, with the illegitimate frontier counts. |
| `lineage_divergence_report` | Divergences from `Part 3` instance lineage, by kind and direction. |
| `dependents_of` | Every dependent registration against a concept or version, by kind, source and binding strength. |
| `dependency_source_currency` | Per source, when it last supplied registrations and whether it is available. |
| `external_obligations_of` | Every concept carrying an external obligation dependency. |
| `impact_of` | The impact set of a proposed change, by consequence class, confidence and distance. |
| `impact_unassessed` | Impact members in `IMPACT_UNASSESSED` beyond a declared age. |
| `analysis_versus_change` | Where a recorded change differs from the proposed change an analysis assessed. |
| `training_definition_drift` | Inferential model versions whose training definitions have since changed extension. |

`extension_change_history` is the projection a consumer should read and almost never has. A version history that lists every increment is dominated by editorial and representational changes, and the two or three that changed meaning are indistinguishable in it. Filtering to extension effect is what turns a history into an answer.

`lineage_downstream_of` and `impact_of` are deliberately separate projections, and the separation is the point of section 11.4. The first is reachability. The second is an impact set. A component that offers only the first, under either name, has not implemented this part.

**P4-3.132 (MUST) Projections are pure.** An implementation must compute every projection as a function of recorded rows alone, holding no state not derivable from them.

**P4-3.133 (MUST) Projection recomputable.** An implementation must be able to recompute every projection from the recorded rows and to demonstrate agreement between a served projection and a recomputation.

**P4-3.134 (MUST) Named projections available.** An implementation must provide every projection in the table above and must name each as named there in any interface it exposes.

**P4-3.135 (MUST) Reachability and impact separately named.** An implementation must provide `lineage_downstream_of` and `impact_of` as separate projections, must not alias one to the other, and must not describe the first as an impact set.

**P4-3.136 (MUST) Extension change history available.** An implementation must provide `extension_change_history` and must return it in preference where a caller requests the history of a definition without qualification.

**P4-3.137 (MUST NOT) No writes through a projection.** An implementation must not permit any state change to be effected by writing to a projection.

### 3.19 Worked demonstration

The demonstration follows one concept across eight years. It is not normative. It exists because the field tables do not show whether the model does the work claimed for it, and because the failure narrated in section 1.3 is the failure it must be shown to catch.

**2027.** Concept `C` is registered in the finance domain, steward named, boundary declared contested. Definition version `V1` records the text, one preferred English designation "active customer", one legacy identifier designation `ACT_CUST_FLG`, a representation of boolean with null semantics `MEANS_NOT_APPLICABLE`, and an approval citation resolving to document `D` version `D3` clause `4.1`, status `APPROVED`. Effectivity is asserted from 2027-01-01, scope enterprise. A classification test set of eleven instances is recorded, three of them borderline. Design lineage records four downstream element level edges: two `IDENTITY`, one `EXPRESSION` into a segmentation attribute, and one `FILTER_DEPENDENCY` into a monthly regulatory return.

Dependent registrations accumulate: a rule from `Part 2` referencing the term, four schema element bindings from `Part 9`, one value set realisation from `Part 10`, one inferential model input binding from a churn model, and one `EXTERNAL_OBLIGATION` declared by an actor naming the monthly return. Six of the dependents are `TRACKS_LATEST`; three are `PINNED_VERSION`.

**2029, the change.** A steward proposes to exclude dormant accounts from the concept. The proposed change is recorded: kinds `NARROWING`, extension effect `SMALLER`, retrospectivity true.

An impact analysis runs. Because the extension effect is not `UNCHANGED` and six dependents are `TRACKS_LATEST`, six members are classified `SEMANTIC_DRIFT` under clause P4-3.125. Because retrospectivity is true, every member is additionally reached by clause P4-3.127 and classified `HISTORICAL_RECLASSIFICATION`. The `FILTER_DEPENDENCY` edge into the regulatory return is reached through lineage, and the return is reached separately through its `EXTERNAL_OBLIGATION` registration, so the member records `reached_by` of both `LINEAGE` and `DEPENDENT_REGISTRATION`. The churn model is reached through `MODEL_INTERFACE`, and its `training_definition_pin` records `V1`, so `training_definition_drift` will flag it from this point.

| Member | Reached by | Consequence | Confidence |
| --- | --- | --- | --- |
| Segmentation attribute | `LINEAGE` | `SEMANTIC_DRIFT` | `ASSERTED_PATH` |
| Monthly regulatory return | `LINEAGE`, `DEPENDENT_REGISTRATION` | `HISTORICAL_RECLASSIFICATION` | `ASSERTED_PATH` |
| Eligibility rule | `DEPENDENT_REGISTRATION` | `SEMANTIC_DRIFT` | `ASSERTED_PATH` |
| Churn model input | `MODEL_INTERFACE` | `SEMANTIC_DRIFT` | `ASSERTED_PATH` |
| Three pinned schema elements | `DEPENDENT_REGISTRATION` | `NO_IMPACT_ASSERTED` after assessment | `ASSERTED_PATH` |
| Two downstream marts | `LINEAGE` | `IMPACT_UNASSESSED` | `INCOMPLETE_PATH` |

The last row is the honest one. Both marts were reached through a node whose lineage completeness is `UNDECLARED`, so the path is marked `INCOMPLETE_PATH` and the analysis cannot claim the set is exhaustive downstream of them.

Nothing in this analysis is an approval. The run's outcome is recorded, the change proceeds by a `Part 1` approval and a `Part 7` authorisation, and clause P4-3.131 forbids the report from saying the change is safe.

**2029, the change made.** Version `V2` is recorded with change declaration kinds `NARROWING`, extension effect `SMALLER`, retrospectivity true, rationale recorded, declarer named, and the impact analysis referenced. The classification test set is re run under clause P4-3.65: two of the eleven instances change from `IN` to `OUT`, which is consistent with the declared effect and is recorded. Had the steward declared `CLARIFYING`, clause P4-3.61 would have refused the version and named those two instances.

**2031, the quiet attempt.** A different steward proposes to redefine `C` to include prospects, described as a clarification. Extension effect declared `UNCHANGED`. The test set runs: four instances change classification. Clause P4-3.61 refuses the version increment and states the four instances. The steward resubmits as `BROADENING`. Clause P4-3.52 is not engaged because the extension is not incomparable, the version is accepted with the correct declaration, and a further impact analysis runs.

**2033, the replacement.** A proposal would redefine `C` in terms of contractual status rather than activity, so that neither extension contains the other. The extension effect is `INCOMPARABLE`. Clause P4-3.52 requires it to be treated as a concept replacement and clause P4-3.49 refuses the version increment. A new concept `C2` is registered, `C` is superseded by `C2` under clause P4-3.21, and every one of the eleven dependents must now rebind explicitly. The count of dependents still bound to the superseded `C` is a signal, so the rebinding is visible rather than assumed.

**2035, the question.** An investigation asks the following.

| Question | Projection | Result |
| --- | --- | --- |
| What did the term mean in 2028? | `definition_at` for 2028-06-01 | `V1`, approved, in force enterprise wide, with its text and exclusions |
| When did the meaning change, as opposed to the entry? | `extension_change_history` | Twice: 2029 `NARROWING` retrospective, 2031 `BROADENING`. The editorial and representational increments are excluded. |
| Were the 2028 figures affected retrospectively? | `impact_of` on the 2029 change | Yes. `HISTORICAL_RECLASSIFICATION`, including the monthly return. |
| Was that known at the time? | `analysis_versus_change` | Yes. The analysis was run, the reference is on the change declaration, and the change made matches the change assessed. |
| Was the churn model affected? | `training_definition_drift` | Yes, from 2029. Fitted on `V1`, applied to `V2` and later. |
| What is still bound to the retired concept? | `dependents_of` on `C` | The count, by kind and component, with the unrebound dependents named. |
| How much of the answer is guesswork? | `lineage_by_method`, `lineage_completeness_report` | The proportion of edges inferred, and the nodes of undeclared completeness through which two members were reached. |

The last row is the pair that matters. Every other row is an answer, and that row is the statement of how far the answers can be trusted. A component that produces the first six rows without the seventh has produced confidence rather than evidence.

**P4-3.138 (MUST) Demonstration satisfiable.** An implementation must be able to answer every question in the table above for any concept within its retained history, using only the projections of section 3.18.
## 4. Interfaces

### 4.1 Interface principles

Operations are specified by their obligations rather than their signatures. No transport, encoding or naming convention is specified.

Operations divide into four groups and the division is enforced: those that record definitions and models, those that record lineage and dependencies, those that analyse, and those that read. The analysing group is separated from the recording group because an impact analysis must never be a side effect of making a change, and from the reading group because it writes a run record.

**P4-4.1 (MUST) Operation classes separated.** An implementation must not provide an operation that both records a definition version and runs an impact analysis.

**P4-4.2 (MUST) Refusal is an outcome.** An implementation must return a refusal outcome of section 7.6 for any operation it declines and must not return an outcome of another class in its place.

**P4-4.3 (MUST) Idempotence key accepted.** An implementation must accept a caller supplied idempotence key on every recording operation and must honour it per section 6.4.

**P4-4.4 (MUST NOT) No partial definition recording.** An implementation must record a definition version together with its texts, designations, representations, change declaration and approval citation, or record none of them.

### 4.2 Recording operations for definitions and models

| # | Operation | Records | Principal refusals |
| --- | --- | --- | --- |
| 1 | Register a concept | `concept` | Duplicate `concept_urn`; no steward; no domain |
| 2 | Assert a concept relation | `concept_relation` | Unknown concept; no justification; a relation that would merge identities |
| 3 | Record a definition version | `definition_version`, `definition_text`, `representation`, `change_declaration` | No change kind; kind inconsistent with extension effect; `CONCEPT_REPLACEMENT` declared or found; `INCOMPARABLE` without justification; definition text failing section 3.6; a text closing a circularity; `UNCHANGED` claimed with no test set; test set run `INCONSISTENT`; no null semantics |
| 4 | Record a designation | `designation` | A second `PREFERRED` in one language and scope; identical term for a different concept with no scope; no status |
| 5 | Record a value domain binding | `value_domain_binding` | Unresolvable `Part 10` pin; enumerated members supplied |
| 6 | Record a classification instance | `classification_instance` | Instance produced by applying the definition to data; no rationale |
| 7 | Run a classification test set | `classification_run` | No test set; version pair not of one concept |
| 8 | Record an approval citation | `approval_citation` | Resolution outcome envelope not supplied in full |
| 9 | Assert effectivity | `effectivity_assertion` | No scope; a second version in force in one scope at one instant |
| 10 | Retract an effectivity assertion | a retraction and a replacement | Retraction without a replacement where one is required |
| 11 | Supersede a concept | `superseded_by_concept_id` | Target concept unknown; the supersession would be a version increment |
| 12 | Retire a concept | `retired_ktime` | Undischarged dependents where the implementation declares that a bar |
| 13 | Record a model version | `model_version`, `model_element` | Unregistered kind or layer; element path in an unregistered scheme |
| 14 | Assert a realisation relation | `realisation_relation` | Method is name matching; no justification |
| 15 | Bind an element to a concept | `element_definition_binding` | Binding kind defaulted; unknown concept |
| 16 | Register an inferential model interface | `inferential_model_interface` | Input or output without a binding; no `Part 13` reference; internals supplied |

Operation 3 is the operation the part is built around, and its refusal list is long for the reason `Part 3` gives for its own: each item is detectable only at the moment of recording, and each is a specific mechanism by which a past meaning becomes unrecoverable.

The refusal a steward will resent most is the refusal of a version claiming `UNCHANGED` whose test set disagrees. It is retained because that is precisely the change section 1.3 narrates, and a declaration that cannot be checked is a declaration nobody will be careful about.

**P4-4.5 (MUST) Preconditions checked at recording.** An implementation must check every precondition in the table above at the moment of recording, must record the outcome of each check, and must not defer a check.

**P4-4.6 (MUST) Whole definition version in one operation.** An implementation must accept the whole artifact set of a definition version in a single operation and must record it atomically.

**P4-4.7 (MUST) Test set run before the version is recorded.** An implementation must run the classification test set before recording a version increment declaring an extension effect of `UNCHANGED` and must refuse the version on inconsistency.

**P4-4.8 (MUST NOT) No approval by this component.** An implementation must not provide an operation that approves a definition version, and must provide only the recording of an approval obtained from `Part 1`.

**P4-4.9 (MUST) Supersession and version increment distinguished at the interface.** An implementation must provide separate operations for recording a version increment and for superseding a concept, and must not permit one to be effected through the other.

**P4-4.10 (MUST) Retirement precondition declared.** An implementation must declare whether it refuses to retire a concept carrying undischarged dependents, and must report the dependents in the refusal where it does.

### 4.3 Recording operations for lineage and dependencies

| # | Operation | Records | Principal refusals |
| --- | --- | --- | --- |
| 17 | Register a lineage node | `lineage_node` | No grain; unknown reference kind |
| 18 | Assert a lineage edge | `lineage_edge`, `lineage_assertion_source` | Generic flow kind; no grain; no method; a tool method with no tool pin; missing transformation pin where the kind requires one; an edge closing a cycle; no semantic effect |
| 19 | Confirm an inferred edge | a confirmation | Edge not of an inferred method |
| 20 | Declare lineage completeness | `lineage_completeness` | Completeness defaulted to `COMPLETE` |
| 21 | Declare a lineage frontier | `lineage_frontier` | Unregistered kind; no justification for a legitimate kind |
| 22 | Record a divergence from instance lineage | `lineage_divergence` | Divergence that would alter an edge |
| 23 | Register a dependency | `dependent_registration` | No binding strength; unregistered kind; registering component not the owner of the kind |
| 24 | Withdraw a dependency | `withdrawn_ktime` | Registration unknown |
| 25 | Record dependency source state | `dependency_source_state` | Source not a registered dependency source |

**P4-4.11 (MUST) Edge preconditions checked.** An implementation must check every precondition for operation 18 at the moment of assertion.

**P4-4.12 (MUST) Confirmation does not rewrite method.** An implementation must record a confirmation of an inferred edge as a distinct fact and must not alter the edge's recorded method, per clause P4-3.102.

**P4-4.13 (MUST NOT) No edge alteration on divergence.** An implementation must not create, alter or delete a lineage edge in the course of recording a divergence from `Part 3`.

**P4-4.14 (MUST) Dependency registered by its owner.** An implementation must refuse a dependent registration of a kind from a component other than the one the registry records as owning that kind, except for `EXTERNAL_OBLIGATION`, which a declaring actor may register.

**P4-4.15 (MUST) Source state recordable and reportable.** An implementation must accept a dependency source state record and must be able to report a source that has not supplied registrations within a declared interval.

### 4.4 Analysing operations

| # | Operation | Records | Returns |
| --- | --- | --- | --- |
| 26 | Record a proposed change | `proposed_change` | The proposal identity |
| 27 | Run an impact analysis | `impact_analysis_run`, `impact_member`, `impact_pin`, access record | The impact set, the per source consultation state, the outcome of section 7.4 |
| 28 | Assess an impact member | assessment on the member | The updated member |
| 29 | Compare an analysis with a change | a comparison record | Differences between the proposed and recorded change |
| 30 | Detect circularity | a detection record | Cycles in the definition text reference graph |
| 31 | Re run a concept's test set against a version pair | `classification_run` | Per instance results and the verdict |

Operation 27's most important returned element is not the impact set. It is the per source consultation state: which dependency sources were consulted, which were unavailable, and which had not supplied registrations recently. An impact set assembled without `Part 2`'s rule term references is missing every rule, and the only thing distinguishing a complete analysis from that one is the consultation state.

**P4-4.16 (MUST) Proposed change recorded before analysis.** An implementation must require a recorded proposed change before running an impact analysis and must not analyse an unrecorded proposal.

**P4-4.17 (MUST) Consultation state returned.** An implementation must return, with every impact analysis, which dependency sources were consulted, which were unavailable, and the currency of each.

**P4-4.18 (MUST) Analysis pins recorded before returning.** An implementation must durably record the pin set of an analysis before returning its result.

**P4-4.19 (MUST) Assessment attributed.** An implementation must record a named actor on every impact member assessment and must not permit an assessment without one.

**P4-4.20 (MUST NOT) No analysis as a side effect.** An implementation must not run an impact analysis as a side effect of recording a definition version, a lineage edge or a dependency.

**P4-4.21 (MUST) Comparison available.** An implementation must provide operation 29 and must be able to compare any recorded change declaration with the proposed change its referenced analysis assessed.

### 4.5 Reading operations

| # | Operation | Returns |
| --- | --- | --- |
| 32 | Read a named projection | The projection of section 3.18, at the times supplied |
| 33 | Resolve a definition as of a time | The version in force, with its approval status and the outcome of section 7.2 |
| 34 | Resolve a designation | The concepts it designates, with the ambiguity outcome where more than one |
| 35 | Get a definition version by pin | The whole artifact set of the version |
| 36 | Get a lineage graph | The upstream or downstream graph with methods, grains, completeness and frontiers |
| 37 | Get an impact analysis | The run, its members, its pins and its consultation state |
| 38 | Export an evidence package | The package of section 8.6 |

**P4-4.22 (MUST) Times required on temporal resolution.** An implementation must require both an application time and a knowledge time for operation 33 and must not default either.

**P4-4.23 (MUST) Approval status returned with every version.** An implementation must return the approval status with every definition version returned from any operation.

**P4-4.24 (MUST) Lineage returned with its qualifications.** An implementation must return the assertion method, grain, completeness and frontier state with every lineage graph, and must not return edges alone.

**P4-4.25 (MUST NOT) No partial artifact set.** An implementation must return the complete artifact set of a definition version from operation 35 or refuse, and must not return a subset without stating what was omitted and why.

### 4.6 What a caller may and may not assume

**P4-4.26 (MUST) Caller obligations declared.** An implementation must document, for every operation, which of the assumptions below the caller may make.

A caller may assume that a returned definition version has the change kinds and extension effect that were declared for it, that a version claiming an unchanged extension passed its classification test set, that a returned lineage edge carries the method by which it was asserted, and that an impact member's consequence class was either derived by a rule of section 3.17 or assessed by the named actor.

A caller may not assume that a definition version is approved, since the status is returned and may be `APPROVAL_NOT_SOUGHT`. A caller may not assume that a lineage graph is complete, since completeness is declared per node and is usually undeclared. A caller may not assume that an impact set is exhaustive, since the consultation state records which sources were missing. A caller may not assume that a declared change kind is correct, since the test set can disprove a claim of no change and cannot prove one. A caller may not assume that an absence of impact members means an absence of impact.

**P4-4.27 (MUST NOT) No implied completeness.** An implementation must not describe an impact set as complete or exhaustive and must describe it as the set assembled from the sources named in its consultation state.

**P4-4.28 (MUST NOT) No approval implied by presence.** An implementation must not present the existence of a definition version as evidence that it is approved or in force.

### 4.7 Reads from other components

| Read | From | On unavailability |
| --- | --- | --- |
| Resolve an approval citation | `Part 1` | Record `APPROVAL_UNRESOLVABLE`; do not refuse the recording |
| Obtain rule term references | `Part 2` | Record the source unavailable; report `PARTIAL_SOURCE_UNAVAILABLE` |
| Obtain determination reliance | `Part 3` | As above |
| Obtain a decision criterion dependency | `Part 5` | As above |
| Obtain an authorisation decision | `Part 7` | Refuse the operation |
| Obtain schema element bindings | `Part 9` | Record the source unavailable |
| Obtain a permissible value set version | `Part 10` | Record the pin as unresolved; refuse a new binding |
| Obtain an inferential model artifact reference | `Part 13` | Refuse the interface registration |

The asymmetry between rows two through six and rows one, seven and eight is deliberate. An unavailable dependency source does not prevent an impact analysis, because refusing to analyse when a source is down would deny the capability exactly when the estate is unstable; the analysis proceeds and reports the outcome `PARTIAL_SOURCE_UNAVAILABLE` of section 7.4. An unresolvable `Part 10` value set does prevent a new binding, because binding to a set that cannot be obtained records a relation to nothing.

**P4-4.29 (MUST) Declared unavailability behaviour.** An implementation must implement the unavailability behaviour of the table above for every read and must record which behaviour it took.

**P4-4.30 (MUST NOT) No substitution on unavailability.** An implementation must not substitute a cached, default, current or successor version of any artifact in the table above.

**P4-4.31 (MUST) Source unavailability surfaced in the outcome.** An implementation must report an impact analysis run with any unavailable dependency source under the outcome of section 7.4 and must not return it as complete.

### 4.8 Events emitted

The envelope carries at minimum an event identity, a type from the registered set, the knowledge time assigned by this component, the subject, the actor, a correlation reference, a schema reference and a digest over the event body.

The minimum event set. An implementation may emit more.

Concept registered. Concept superseded. Concept retired. Concept relation asserted. Definition version recorded. Definition version refused. Extension changed. Retrospective change recorded. Concept replacement refused. Clarification refused on test set inconsistency. Designation recorded. Preferred designation changed. Designation prohibited. Designation ambiguity detected. Representation changed. Null semantics undeclared. Value domain binding recorded. Classification instance recorded. Classification run completed. Classification divergence detected. Approval citation recorded. Approval unresolvable. Effectivity asserted. Effectivity retracted. Effectivity ambiguity detected. Model version recorded. Realisation relation asserted. Element unrealised. Inferential model interface registered. Training definition drift detected. Lineage node registered. Lineage edge asserted. Inferred edge confirmed. Lineage completeness declared. Lineage frontier declared. Undeclared lineage frontier recorded. Lineage divergence recorded. Dependency registered. Dependency withdrawn. Dependency source ceased supplying. Proposed change recorded. Impact analysis run. Impact analysis partial. Semantic drift member identified. Historical reclassification member identified. Impact member assessed. Analysis and change diverged. Circularity detected. Evidence package exported.

Three of these are the operationally important ones and are the least obvious. **Dependency source ceased supplying** is the analogue of `Part 3`'s cessation event: a source that stops registering produces silence, and every impact analysis afterwards is quietly narrower. **Semantic drift member identified** must be emitted per member rather than as part of a run summary, because it is the class nobody looks for. **Analysis and change diverged** fires when the change made is not the change assessed, which is the commonest way a governance process is satisfied on paper.

**P4-4.32 (MUST) Minimum event set.** An implementation must emit an event for every member of the set above and must register any additional type under section 9.9.

**P4-4.33 (MUST) Envelope minimum.** An implementation must include every envelope element named above in every event it emits.

**P4-4.34 (MUST NOT) No event in place of a record.** An implementation must not rely on event emission to satisfy any recording obligation of section 3 or section 8.

**P4-4.35 (MUST) Semantic drift emitted per member.** An implementation must emit a distinct event for each impact member classified `SEMANTIC_DRIFT` or `HISTORICAL_RECLASSIFICATION` and must not emit them only as counts on a run.

**P4-4.36 (MUST) Source cessation detected.** An implementation must detect, within a declared interval, that a dependency source which previously supplied registrations has ceased to do so, must emit the event, and must declare the interval.

**P4-4.37 (MUST NOT) No suppression of adverse events.** An implementation must not provide a configuration that suppresses the emission of a refusal, an extension change, a semantic drift member, a historical reclassification member, an undeclared frontier, a classification divergence, a source cessation, an analysis divergence or an approval unresolvable.
## 5. State model

### 5.1 Four state models, deliberately separated

This part specifies four state machines and keeps them apart. The separation follows the pattern the three prior parts establish, and section 13.7 hands `Part 0` the question of whether the pattern should be stated once for the whole standard.

The **registration state** of a definition version is owned here. It describes how far the definition has progressed through this component's own admission process.

The **authority state** of a definition version is not owned here at all. Whether a version is approved is a `Part 1` fact obtained by resolution, and whether it is in force at an application time follows from the effectivity assertions of section 3.10 combined with that approval. This part holds no field carrying it.

The **lineage assertion state** of an edge describes whether an assertion is inferred, confirmed or contradicted.

The **impact analysis run state** describes the progress of one assessment.

Keeping registration and authority apart matters for the same reason it matters in `Part 2`. A definition can be fully registered here, with texts, designations, representation and a passing test set, and not be approved by anyone. A single status field must then report either that the definition does not exist, which is false and hides the estate's real vocabulary, or that it is available, which conceals that nobody has accepted responsibility for it. Both readings cause harm and the second causes more.

**P4-5.1 (MUST) Four models separate.** An implementation must not represent registration state and authority state in one field and must not derive either from the other.

**P4-5.2 (MUST) Registered but unapproved reportable.** An implementation must be able to report every definition version whose registration state is complete and whose approval status is not `APPROVED`, and must include the count in the signals of section 8.5.

**P4-5.3 (MUST NOT) No authority state held.** An implementation must not hold, cache beyond a declared validity period, or assert the approval status of a definition version, and must obtain it by resolution.

### 5.2 Registration state of a definition version

States:

`DRAFT`. The version exists and its artifact set is incomplete. It is readable, is marked, and must not be resolved by any temporal read.

`CHECKING`. The preconditions of operation 3 are being applied.

`REGISTERED`. Every precondition passed. The version is resolvable subject to approval and effectivity.

`REFUSED`. A precondition failed. The reason is recorded per check. The version is retained as a record of what was attempted and is never resolvable.

`SUPERSEDED`. A later version of the same concept has been registered. The version remains resolvable for a read whose application time falls within its effectivity.

`WITHDRAWN`. The version was withdrawn deliberately, with an authorisation reference and a reason, on the ground that it should not have been registered. It remains readable and is not resolvable.

`CONCEPT_RETIRED`. The concept has been retired or superseded by a different concept. The version remains resolvable for historical reads.

Transitions:

| From | To | Trigger | Requires |
| --- | --- | --- | --- |
| `DRAFT` | `CHECKING` | Registration requested | Complete artifact set |
| `CHECKING` | `REGISTERED` | All preconditions passed | Test set run where required |
| `CHECKING` | `REFUSED` | Any precondition failed | Recorded reason per failed check |
| `REFUSED` | `CHECKING` | Registration requested again | A new artifact set, that is, a new version |
| `REGISTERED` | `SUPERSEDED` | A later version registered | Identity of the successor and its change declaration |
| `REGISTERED` | `WITHDRAWN` | Deliberate withdrawal | `AUTHREF` and reason |
| `SUPERSEDED` | `WITHDRAWN` | Deliberate withdrawal | `AUTHREF` and reason |
| `REGISTERED`, `SUPERSEDED` | `CONCEPT_RETIRED` | Concept retired or superseded | Concept level act |

`REFUSED` does not transition to `REGISTERED` without a new version, because the refusal was a finding about an immutable artifact set. A refused version is retained rather than discarded, and this is a decision: the record that a steward attempted to register a narrowing as a clarification is exactly the record an assurance function needs, and discarding refusals removes the only evidence that the check is doing work. Clause P4-5.7 requires retention and section 8.5 requires the count.

`WITHDRAWN` is distinguished from `SUPERSEDED` because they assert different things. A superseded version was right and is no longer current. A withdrawn version should not have been registered, which means anything that relied on it while it stood relied on something the organisation now disowns, and clause P4-5.9 requires the dependents to be reported.

**P4-5.4 (MUST) Enumerated states only.** An implementation must represent the registration state of a definition version as exactly one member of the set above.

**P4-5.5 (MUST) Enumerated transitions only.** An implementation must not effect a transition absent from the table above.

**P4-5.6 (MUST) State is a projection.** An implementation must compute registration state from recorded rows and must not hold it as an updatable field.

**P4-5.7 (MUST) Refused versions retained and countable.** An implementation must retain every refused version with its per check outcomes, must not delete it, and must be able to report refusals by steward, by concept and by failed precondition.

**P4-5.8 (MUST NOT) No resolution of a draft, refused or withdrawn version.** An implementation must not return a version in state `DRAFT`, `REFUSED` or `WITHDRAWN` from any temporal resolution, and must return it only from an explicit read by identity.

**P4-5.9 (MUST) Withdrawal reports its dependents.** An implementation must report every dependent registration against a version at the moment of its withdrawal and must record the report with the withdrawal.

**P4-5.10 (MUST) Superseded versions remain resolvable.** An implementation must continue to resolve a superseded version for a read whose application time falls within its effectivity and must not substitute the successor.

**P4-5.11 (MUST NOT) No state change from the passage of time.** An implementation must not transition registration state as a consequence of a date passing and must effect every transition by a recorded act.

**P4-5.12 (MUST) Withdrawal authorised and reasoned.** An implementation must record an `AUTHREF` and a reason for every transition to `WITHDRAWN`.

### 5.3 Concept state

States: `ACTIVE`, `SUPERSEDED_BY_CONCEPT`, `RETIRED`, `DORMANT`.

`DORMANT` is a concept with no version in force and no successor: the definition lapsed and nothing replaced it. This is a distinct and common condition and it is invisible in a model with only active and retired, because a lapsed concept appears active. Clause P4-5.15 requires it to be computed and reported, since the count of concepts nobody has defined for a year is a governance measure.

There is no transition from `RETIRED` or `SUPERSEDED_BY_CONCEPT` back to `ACTIVE`. A concept the organisation has retired and then needs again is a new registration, because reviving an identity makes the gap in its history indistinguishable from continuity.

**P4-5.13 (MUST) Enumerated concept states.** An implementation must represent the state of every concept as exactly one member of the set above, computed from entries.

**P4-5.14 (MUST NOT) No revival.** An implementation must not transition a concept from `RETIRED` or `SUPERSEDED_BY_CONCEPT` to `ACTIVE`.

**P4-5.15 (MUST) Dormancy computed and reported.** An implementation must compute `DORMANT` where a concept has no version in force and no successor, must not report it as active, and must include the count in the signals of section 8.5.

**P4-5.16 (MUST) Supersession by concept reports dependents.** An implementation must report every dependent registration against any version of a concept at the moment the concept is superseded or retired, and must record the report.

### 5.4 Lineage assertion state of an edge

States: `INFERRED`, `ASSERTED`, `CONFIRMED`, `CONTRADICTED`, `RETRACTED`.

`INFERRED` is an edge produced by name matching, statistics or an import without confirmation. `ASSERTED` is an edge a named actor declared or a parser produced from a pinned artifact. `CONFIRMED` is an inferred edge a person has accepted. `CONTRADICTED` is an edge a `Part 3` divergence of kind `ASSERTED_NOT_OBSERVED` has run against, or which an actor has stated to be wrong without yet retracting. `RETRACTED` is an edge an actor has withdrawn, retained as a record.

| From | To | Trigger |
| --- | --- | --- |
| `INFERRED` | `CONFIRMED` | A person confirms it |
| `INFERRED` | `RETRACTED` | A person rejects it |
| `ASSERTED` | `CONTRADICTED` | A divergence or an actor's statement |
| `CONFIRMED` | `CONTRADICTED` | As above |
| `CONTRADICTED` | `ASSERTED` | The contradiction is resolved in the edge's favour, with a reason |
| `CONTRADICTED` | `RETRACTED` | The contradiction is resolved against the edge |
| any | `RETRACTED` | Retraction by an actor with a reason |

There is no transition from `INFERRED` to `ASSERTED`. The two describe how the edge came to exist and that does not change; confirmation is a separate state precisely so that the origin remains legible, per clause P4-3.102.

`CONTRADICTED` is not terminal and does not remove the edge from a traversal. An edge in that state continues to appear in a lineage graph and in an impact set, marked, because removing it would narrow every impact analysis on the strength of an unresolved disagreement. Clause P4-5.20 requires the marking and the continued traversal.

**P4-5.17 (MUST) Enumerated edge states.** An implementation must represent the state of every lineage edge as exactly one member of the set above.

**P4-5.18 (MUST NOT) No promotion of inferred to asserted.** An implementation must not transition an edge from `INFERRED` to `ASSERTED` and must record acceptance as `CONFIRMED`.

**P4-5.19 (MUST) Retracted edges retained.** An implementation must retain a retracted edge with its reason and must exclude it from traversal while continuing to return it on an explicit read.

**P4-5.20 (MUST) Contradicted edges traversed and marked.** An implementation must continue to include a contradicted edge in lineage traversals and impact sets, must mark it, and must not narrow a result by excluding it.

**P4-5.21 (MUST) Resolution of a contradiction reasoned.** An implementation must record a reason and a named actor for every transition out of `CONTRADICTED`.

### 5.5 Impact analysis run state

States: `REQUESTED`, `ASSEMBLING_LINEAGE`, `CONSULTING_SOURCES`, `CLASSIFYING`, `COMPLETED`, `PARTIAL`, `REFUSED`, `ABANDONED`.

| From | To | Trigger |
| --- | --- | --- |
| `REQUESTED` | `ASSEMBLING_LINEAGE` | Proposal recorded and authorised |
| `REQUESTED` | `REFUSED` | Proposal unknown, target unknown, or not authorised |
| `ASSEMBLING_LINEAGE` | `CONSULTING_SOURCES` | Lineage traversal complete to its bounds |
| `CONSULTING_SOURCES` | `CLASSIFYING` | Every dependency source attempted |
| `CLASSIFYING` | `COMPLETED` | Every member classified and every source consulted |
| `CLASSIFYING` | `PARTIAL` | A source was unavailable, a bound was reached, or a path passed through incomplete lineage |
| any | `ABANDONED` | Loss of the executing process |

`PARTIAL` and `COMPLETED` are separate terminal states rather than one state with a flag, because the distinction is the one a reader must not be able to miss. An impact analysis that could not reach `Part 2` is not a smaller version of a complete analysis; it is an analysis with no rules in it, and every rule in the estate that uses the term is absent from a report that otherwise looks finished.

**P4-5.22 (MUST) Enumerated run states.** An implementation must represent every impact analysis run as exactly one member of the set above.

**P4-5.23 (MUST) Sources attempted before classification.** An implementation must attempt every registered dependency source before classifying members and must record the attempt and its result per source.

**P4-5.24 (MUST) Partial distinguished from complete.** An implementation must record `PARTIAL` where any source was unavailable, any bound was reached or any path passed through a node of incomplete lineage, and must not record `COMPLETED`.

**P4-5.25 (MUST) Partial runs still return members.** An implementation must return the members a partial run found together with its consultation state, and must not discard them.

**P4-5.26 (MUST) Abandonment detected and recorded.** An implementation must transition a run whose executing process is lost to `ABANDONED` within a declared interval and must declare the interval.

**P4-5.27 (MUST) Terminal states are terminal.** An implementation must not transition out of `COMPLETED`, `PARTIAL`, `REFUSED` or `ABANDONED`, and must record a further assessment as a new run.

**P4-5.28 (MUST NOT) No amendment of a run.** An implementation must not alter the members, pins or consultation state of a recorded run, and must record an assessment of a member as an appended fact against it.
## 6. Execution semantics

### 6.1 Determinism and reproducibility

Two properties, distinguished as in `Part 2` section 6.1.

**Determinism.** A resolution, a traversal or an impact analysis performed twice against the same recorded rows and the same dependency source responses yields the same result.

**Reproducibility.** An impact analysis run in 2029 can be run again in 2035, from its recorded pins, and yield the same result. This is harder and matters more, because the whole use of an impact analysis in a later investigation is to establish what was known at the time.

Reproducibility of an impact analysis fails in four ways and three are unobvious. The lineage graph changed, which pinning the graph state prevents. A dependency source's registrations changed, which pinning the source state prevents. The classification rules of section 3.17 changed, which pinning this part's version prevents. And a dependency source that was available then is gone now, which nothing prevents and which clause P4-6.5 requires to be reported rather than papered over.

**P4-6.1 (MUST) Identical inputs yield identical results.** An implementation must return the same resolution outcome, the same traversal and the same impact set for two operations against the same recorded rows and the same source responses.

**P4-6.2 (MUST) Traversal order total and declared.** An implementation must impose a declared total order on the traversal of a lineage graph and must not permit the order to vary between traversals of the same rows.

**P4-6.3 (MUST) Graph state pinned in an analysis.** An implementation must pin the state of the lineage graph an impact analysis read, in terms sufficient to reconstruct the same subgraph.

**P4-6.4 (MUST) Classification rule version pinned.** An implementation must pin the version of this part, or of its own implementation of section 3.17, under which an impact member was classified.

**P4-6.5 (MUST) Irreproducibility reported, not concealed.** An implementation must report a re run of an impact analysis whose pinned source state cannot be obtained as irreproducible, must name the source, and must not substitute a current response.

### 6.2 Resolution of a definition as of a time

```
resolve(concept, atime, ktime, scope):
  1  if concept unknown:                     return NOT_FOUND
  2  decision = obtain authorisation from Part 7
     if not permitted:                       return REFUSED(NOT_AUTHORISED)
  3  assertions = effectivity_assertions(concept)
       where asserted_ktime <= ktime
         and not retracted as at ktime
         and scope matches
         and effective_from <= atime
         and (effective_to absent or effective_to > atime)
  4  if assertions is empty:                 return NOT_IN_FORCE_AT_INSTANT
  5  if assertions has more than one distinct version:
                                             return AMBIGUOUS_MULTIPLE with all candidates
  6  version = the single version
  7  if registration_state(version) in {DRAFT, REFUSED, WITHDRAWN}:
                                             return NOT_RESOLVABLE with the state
  8  approval = approval_citation(version)   // recorded, not re resolved
  9  if approval.status != APPROVED:          outcome = RESOLVED_UNAPPROVED
     else if version is superseded:           outcome = RESOLVED_SUPERSEDED
     else:                                    outcome = RESOLVED
 10  compare belief now against belief at ktime; set divergence flag
 11  return outcome, version, artifact set, approval status, divergence flag
```

Step 5 returns every candidate rather than choosing. This is the same position `Part 1` takes on citation ambiguity and `Part 2` takes on rule contradiction: where the record admits two answers, reporting one is a decision the component is not entitled to make.

Step 8 reads the recorded approval citation rather than re resolving against `Part 1`. Re resolving would give the approval status as at today, which is a different question from the status as at the knowledge time requested, and the difference is exactly the thing a bitemporal read exists to expose.

Step 10 carries forward the divergence flag concept from `Part 1` section 6.2: the comparison between what was believed at the requested knowledge time and what is believed now. A definition resolved as of 2028, under 2028's beliefs, that differs from what is now believed to have been in force in 2028, is the most important single fact such a read can return.

**P4-6.6 (MUST) Algorithm order.** An implementation must perform the steps above in the order given.

**P4-6.7 (MUST) Both instants required.** An implementation must require both an application time and a knowledge time and must not default either.

**P4-6.8 (MUST) Ambiguity returns all candidates.** An implementation must return every candidate version where more than one is in force in a scope at an instant and must not select between them.

**P4-6.9 (MUST) Approval read as recorded.** An implementation must return the approval status recorded at the requested knowledge time and must not re resolve it against `Part 1` during a temporal read.

**P4-6.10 (MUST) Divergence flag returned.** An implementation must compute and return the divergence between belief at the requested knowledge time and present belief.

**P4-6.11 (MUST) Unapproved resolution distinguished.** An implementation must return `RESOLVED_UNAPPROVED` rather than `RESOLVED` where the version's approval status is not `APPROVED`.

### 6.3 Designation resolution

```
resolve_designation(term, lang, scope, atime, ktime):
  1  candidates = designations where term matches exactly, lang matches,
       scope matches or designation scope absent, asserted_ktime <= ktime,
       and not retired as at ktime
  2  if empty:                                return NOT_FOUND
  3  concepts = distinct concepts of candidates
  4  if concepts has more than one:           return AMBIGUOUS_DESIGNATION with all
  5  resolve(concept, atime, ktime, scope) and return with the designation status
```

Matching is exact. No normalisation, no case folding, no stemming, no fuzzy matching. A component that resolves "Active Customer" and "active_customer" to the same designation has made a lexical guess and produced a resolution that looks authoritative, and the guess is wrong in the cases that matter, which are the ones where two similar strings designate two different concepts. Where an organisation needs a normalised lookup, the normalisation is a registered designation of kind `LEGACY_IDENTIFIER` or `ABBREVIATION`, which makes the equivalence a recorded assertion rather than an inference. Clause P4-6.13 forbids the inference.

**P4-6.12 (MUST) Exact matching.** An implementation must match a designation exactly and must not case fold, normalise, stem or fuzzy match in the course of a resolution.

**P4-6.13 (MUST NOT) No lexical equivalence.** An implementation must not treat two designations as equivalent on the basis of their characters and must require an equivalence to be a recorded designation of the same concept.

**P4-6.14 (MUST) Designation ambiguity returns all concepts.** An implementation must return every concept a designation resolves to where more than one and must not select between them.

**P4-6.15 (MUST) Designation status returned.** An implementation must return the status of the designation matched, so that a caller resolving through a deprecated or prohibited term is told.

### 6.4 Idempotence

**P4-6.16 (MUST) Idempotence by key.** An implementation must return the originally recorded outcome for a repeated recording operation bearing an idempotence key already seen within its declared deduplication window and must not record again.

**P4-6.17 (MUST) Deduplication window declared.** An implementation must declare its deduplication window as a duration and must state what happens to a key repeated after it.

**P4-6.18 (MUST NOT) No idempotence across differing payloads.** An implementation must refuse an operation bearing a seen key with a different payload.

**P4-6.19 (MUST) Duplicate definition detectable.** An implementation must be able to report definition versions of one concept whose texts, representations and change declarations coincide, so that a duplicate recorded without a key is discoverable.

### 6.5 The classification test procedure

```
run_test_set(concept, version_a, version_b):
  1  instances = classification_instances(concept)
  2  if instances empty:                      return NOT_RUN
  3  human_required = false
  4  for each instance in declared order:
       for each version in {version_a, version_b}:
         if instance has instance_data and the version's representation admits
            a mechanical test:
              result = mechanical classification
         else:
              result = the classification a person recorded for that version
              human_required = true
       record per instance results for both versions
  5  inconsistent = instances where the two versions classify differently
  6  if inconsistent is empty and not human_required:  verdict = CONSISTENT
     if inconsistent is empty and human_required:      verdict = PARTIALLY_HUMAN
     if inconsistent is not empty:                     verdict = INCONSISTENT
  7  record the run with per instance results and the verdict
  8  return verdict, inconsistent instances
```

The procedure is honest about its own limit. Most classification instances in most organisations will be prose descriptions, so most runs will be `PARTIALLY_HUMAN`, which is not a mechanical check at all: it is a structured prompt to a person to classify eleven cases against two texts and a record of what they said. That is still far more than a declaration alone, because it produces a dated, attributed, instance level record of the judgement, and because the two or three instances where a person's answers differ between the versions are precisely the extension change the steward may not have noticed.

**P4-6.20 (MUST) Procedure order.** An implementation must perform the steps above in the order given and must record per instance results for both versions.

**P4-6.21 (MUST) Human involvement recorded per instance.** An implementation must record, per instance, whether the classification was mechanical or a person's, and must not record a run as mechanical where any instance was not.

**P4-6.22 (MUST) Inconsistent instances named.** An implementation must return and record the identity of every instance the two versions classify differently.

**P4-6.23 (MUST) Instance order declared.** An implementation must declare the order in which instances are presented and must not vary it between runs of the same set.

**P4-6.24 (MUST NOT) No mechanical classification without data.** An implementation must not classify an instance mechanically where the instance carries no instance data, and must record the classification as a person's.

### 6.6 The impact analysis algorithm

```
analyse(proposed_change, bounds):
  1  target = proposed_change.target
     if unknown:                               return REFUSED(TARGET_UNKNOWN)
  2  decision = obtain authorisation from Part 7
     if not permitted:                          return REFUSED(NOT_AUTHORISED)
  3  pin the lineage graph state, this part's classification rule version,
     and the registries
  4  members = {}
  5  // lineage direction
     traverse lineage_downstream_of(target) within bounds
       for each node reached:
         members += member(node, reached_by=LINEAGE, path, distance)
         if completeness(node) != COMPLETE:
              mark the path INCOMPLETE_PATH
         if any edge on the path has an inferred method:
              mark the path INFERRED_PATH
  6  // realisation and concept relation directions
     traverse realisation relations and concept relations from the target
       members += member(..., reached_by=REALISATION or CONCEPT_RELATION)
  7  // dependency direction
     for each registered dependency source:
         attempt to obtain registrations against the target concept and version
         record the attempt, its result and the source currency
         if obtained:
             members += member(..., reached_by=DEPENDENT_REGISTRATION)
         else:
             record the source unavailable
  8  // model interface direction
     members += inferential model interfaces binding to the target
  9  // classification
     for each member:
         if proposed extension_effect != UNCHANGED
            and member binding_strength in {TRACKS_LATEST, UNPINNED_UNKNOWN}:
                consequence = SEMANTIC_DRIFT
         else if proposed retrospectivity and extension_effect != UNCHANGED:
                consequence = HISTORICAL_RECLASSIFICATION
         else if proposed kinds include REPRESENTATION_CHANGE
                 and member binding_strength == PINNED_VERSION:
                consequence = STRUCTURAL_BREAK
         else if proposed kinds include REPRESENTATION_CHANGE
                 and the change reduces precision or scale:
                consequence = PRECISION_LOSS
         else if proposed kinds include VALUE_DOMAIN_CHANGE:
                consequence = VALUE_DOMAIN_BREAK
         else if proposed kinds include DESIGNATION_CHANGE
                 and the member is keyed on the designation:
                consequence = STRUCTURAL_BREAK
         else:  consequence = IMPACT_UNASSESSED
 10  outcome = COMPLETE if every source consulted, no bound reached and no
     INCOMPLETE_PATH; else the appropriate partial member of section 7.4
 11  record run, members, pins, consultation state; emit per member events
 12  return members, consultation state, outcome
```

Three properties of step 9 are decisions rather than derivations.

A member may receive more than one consequence class in principle, and the algorithm assigns one, in the order given. The order puts `SEMANTIC_DRIFT` and `HISTORICAL_RECLASSIFICATION` above the structural classes, because a member that both drifts semantically and breaks structurally will be found by the break and the drift is the finding nobody would otherwise look for. Clause P4-6.28 requires the other applicable classes to be recorded alongside, so the precedence orders the headline and hides nothing.

`IMPACT_UNASSESSED` is the default rather than `NO_IMPACT_ASSERTED`. The difference is between not knowing and having looked, and defaulting to the second is how an impact report comes to consist mostly of assertions nobody made.

Step 7 records the attempt to every source, including the sources that returned nothing. A source that was consulted and had no registrations is a different fact from a source that was unavailable, and both are different from a source that was never registered as a source at all.

**P4-6.25 (MUST) Algorithm order.** An implementation must perform the steps above in the order given and must pin before traversing.

**P4-6.26 (MUST) All five directions traversed.** An implementation must traverse lineage, realisation, concept relations, dependency registrations and model interfaces, and must record which it traversed.

**P4-6.27 (MUST) Every source attempt recorded.** An implementation must record the attempt to every registered dependency source, including sources that returned no registrations, and must distinguish that case from unavailability.

**P4-6.28 (MUST) All applicable consequence classes recorded.** An implementation must record every consequence class applicable to a member alongside the one assigned by the precedence, and must not discard the others.

**P4-6.29 (MUST) Precedence applied as stated.** An implementation must apply the classification precedence of step 9 in the order given.

**P4-6.30 (MUST) Unassessed is the default.** An implementation must assign `IMPACT_UNASSESSED` where no rule of step 9 applies and must not assign `NO_IMPACT_ASSERTED` without a recorded assessment by a named actor.

**P4-6.31 (MUST) Path qualifications propagated.** An implementation must mark a member's confidence as `INCOMPLETE_PATH` where any node on its path is of incomplete completeness and as `INFERRED_PATH` where any edge on its path is of an inferred method.

**P4-6.32 (MUST NOT) No pruning by consequence.** An implementation must not omit a member from a run because its consequence class was assessed immaterial, and must record the assessment against the member.

### 6.7 Bounds and budget

Traversal must terminate. A lineage graph over a real estate is large and a defect in it can make a traversal unbounded.

Three bounds are required: **depth**, in hops from the target; **breadth**, in edges traversed from any one node; and a **budget** on a declared resource. As in `Part 2` section 6.7 and `Part 3` section 6.6, the primary budget must be on a deterministic resource, because a budget on wall clock time makes the same analysis complete on one day and truncate on another, and the two results then disagree about the impact set for reasons the record does not contain.

**P4-6.33 (MUST) Three bounds declared.** An implementation must declare a depth bound, a breadth bound and a budget, and must state the resource the budget bounds.

**P4-6.34 (MUST) Primary budget deterministic.** An implementation must make its primary budget a bound on a deterministic resource.

**P4-6.35 (MAY) Secondary non deterministic guard.** An implementation may enforce an additional bound on a non deterministic resource.

**P4-6.36 (MUST) Non deterministic truncation marked.** An implementation must mark a run truncated by a non deterministic bound as not repeatable.

**P4-6.37 (MUST) Truncation point recorded.** An implementation must record the node and edge at which truncation occurred, so that a later run with larger bounds can be compared.

**P4-6.38 (MUST NOT) No silent bound.** An implementation must not apply an undeclared bound and must not return a truncated result without stating the bound that truncated it.

### 6.8 Clocks

Three clocks, on the same basis and with the same names as `Part 1` section 3.1.

**P4-6.39 (MUST) Knowledge time assigned by this component.** An implementation must assign every knowledge time from its own clock and must refuse an entry supplying one.

**P4-6.40 (MUST NOT) No occurrence time assignment.** An implementation must not assign an occurrence time and must record every one as asserted by a named actor.

**P4-6.41 (MUST) Application time asserted, not inferred.** An implementation must record effectivity in application time as an explicit assertion and must not derive it from a knowledge time or an approval date.

**P4-6.42 (MUST) Instants in a declared scale.** An implementation must record every instant in a declared time scale with a declared offset and must not record a local time without its offset.

**P4-6.43 (MUST) Monotonic knowledge time within a stream.** An implementation must assign knowledge times that do not decrease within a stream and must record any correction of its own clock as an entry.

### 6.9 What this component may compute, and what it may not

It may compute: the resolution of a definition as of a pair of instants; the resolution of a designation; the transitive closure of the lineage graph to declared bounds; circularity in the definition text reference graph; the classification test verdict; the impact set and the consequence classes derivable by section 3.17; the divergence between design and instance lineage; and every count and projection of section 3.18.

It may not compute: whether a definition text is correct, which is a steward's judgement; whether a change kind was declared honestly beyond what the test set disproves; whether a semantic change matters to a dependent, which clause P4-3.126 reserves to a named actor; whether a definition is approved, which is `Part 1`'s; whether a lineage edge is true, which it can only record as asserted; whether an inferential model performs well, which it does not observe; and whether a change should proceed, which is a decision and an authorisation.

**P4-6.44 (MUST) Permitted computations only.** An implementation must not compute any determination allocated to another component by section 12 and must return the recorded outcome that component supplied.

**P4-6.45 (MUST NOT) No inference of a definition.** An implementation must not generate, complete or suggest a definition text, a change kind, an extension effect or a classification and record it as a steward's assertion.

**P4-6.46 (MUST NOT) No inference of a dependency.** An implementation must not create a dependent registration by inference, per clause P4-3.120.

**P4-6.47 (MUST NOT) No inference of materiality.** An implementation must not assess whether an impact member matters and must record `IMPACT_UNASSESSED` until a named actor assesses it.
## 7. Outcome and failure taxonomy

### 7.1 Why the taxonomy is the specification

This component produces three kinds of answer and each has a way of being wrong that is invisible in the answer itself.

A **resolution** says what a term meant. It is wrong invisibly when it returns a definition nobody approved, or when it returns one answer where the record admits two.

A **traversal** says what is connected. It is wrong invisibly when it returns a graph whose completeness is undeclared, because the reader cannot tell an exhaustive answer from a fragment.

An **impact set** says what a change would affect. It is wrong invisibly when a dependency source was unavailable, because the report looks the same size and is missing an entire class of dependents.

In all three cases a well formed, plausible, confidently presented answer is the failure mode. The taxonomy exists so that the qualification travels with the answer rather than being available on request, and clause P7 requirements below are written to make omission of a qualification a nonconformity rather than an inconvenience.

### 7.2 Resolution outcomes

Nine members, three classes. The table is normative.

| Class | Member | Means |
| --- | --- | --- |
| Resolved | `RESOLVED` | One version in force, approved, at the instants requested. |
| Resolved | `RESOLVED_SUPERSEDED` | One version in force at the requested application time, since superseded. Correct and worth signalling. |
| Resolved | `RESOLVED_UNAPPROVED` | One version in force whose approval status is not `APPROVED`. |
| Non result | `NOT_IN_FORCE_AT_INSTANT` | The concept exists and no version was in force at the instants requested, in the scope requested. |
| Non result | `NOT_RESOLVABLE` | The only candidate version is in a registration state that is not resolvable. |
| Non result | `NOT_FOUND` | No such concept or designation is held. |
| Ambiguous | `AMBIGUOUS_MULTIPLE` | More than one version is in force in the scope at the instant. |
| Ambiguous | `AMBIGUOUS_DESIGNATION` | The designation resolves to more than one concept in the language and scope. |
| Withheld | `WITHHELD` | The concept is held and the principal is not permitted to see it. |

Four distinctions are load bearing.

**`RESOLVED` against `RESOLVED_UNAPPROVED`.** A single member covering both would let an unapproved definition be consumed as though someone had accepted responsibility for it. Given clause P4-3.10's admission of unapproved versions, this separation is the whole safeguard.

**`RESOLVED` against `RESOLVED_SUPERSEDED`.** A read as of a past instant should return the version in force then, and it is correct that the version has since been superseded. A reader who does not know that will assume the definition is current, and the read will silently become a source of stale meaning.

**`NOT_IN_FORCE_AT_INSTANT` against `NOT_FOUND`.** The first says the concept exists and had no definition then, which is a governance gap in a known thing. The second says the organisation has no such concept. Merging them makes a lapsed definition indistinguishable from an unknown term, and the remedies are different.

**`WITHHELD` against `NOT_FOUND`.** The same distinction `Part 1`, `Part 2` and `Part 3` all maintain, for the same reason. Returning not found for a concept the reader may not see is a false statement about the estate.

**P4-7.1 (MUST) Closed resolution outcome set.** An implementation must return exactly one member of the table above from every resolution and must not return a value outside the set.

**P4-7.2 (MUST) Unapproved resolution distinguished.** An implementation must return `RESOLVED_UNAPPROVED` where the approval status is not `APPROVED` and must not return `RESOLVED`.

**P4-7.3 (MUST) Supersession signalled.** An implementation must return `RESOLVED_SUPERSEDED` where the version resolved has since been superseded, together with the successor identity.

**P4-7.4 (MUST) Ambiguity returns candidates.** An implementation must return every candidate with an ambiguous outcome and must not select between them.

**P4-7.5 (MUST) Not in force distinguished from not found.** An implementation must not return `NOT_FOUND` for a concept it holds.

**P4-7.6 (MUST) Withheld distinguished from not found.** An implementation must return `WITHHELD` for a concept it holds and may not disclose and must not return `NOT_FOUND`.

**P4-7.7 (MUST NOT) No mapping onto two values.** An implementation must not provide an interface that maps the nine members onto a found or not found pair and must not document such a mapping as canonical.

### 7.3 Traversal outcomes

| Member | Means |
| --- | --- |
| `TRAVERSED_COMPLETE` | Every node on every path declared its completeness as `COMPLETE`, and no frontier was illegitimate. |
| `TRAVERSED_TO_FRONTIER` | As above, and the graph terminated at one or more legitimate declared frontiers. |
| `TRAVERSED_INCOMPLETE_DECLARED` | A node on a path declared its completeness as `PARTIAL_KNOWN`. |
| `TRAVERSED_INCOMPLETE_UNDECLARED` | A node on a path declared `PARTIAL_UNKNOWN` or `UNDECLARED`. |
| `TRAVERSED_TO_ILLEGITIMATE_FRONTIER` | A path terminated at `NOT_YET_MAPPED` or `FRONTIER_UNDECLARED`. |
| `TRAVERSED_TRUNCATED` | A declared bound was reached. |
| `TRAVERSED_INFERRED_IN_PART` | A path traversed an edge of an inferred method. |
| `REFUSED` | The traversal was declined. |

The table is normative. More than one may apply, and clause P4-7.9 requires all applicable members to be returned rather than a single precedence winner, because the qualifications are not ordered: an incomplete graph and an inferred graph are different weaknesses and a reader needs both.

`TRAVERSED_COMPLETE` will be rare in any real estate and that is the point. A component that returns it frequently is a component whose completeness declarations are being defaulted, and clause P4-3.107 forbids that default precisely so that this member remains meaningful.

**P4-7.8 (MUST) Closed traversal outcome set.** An implementation must return members of the table above from every traversal and must not return a value outside the set.

**P4-7.9 (MUST) All applicable members returned.** An implementation must return every applicable traversal outcome member rather than a single one, and must not order them by severity.

**P4-7.10 (MUST) Declared and undeclared incompleteness distinguished.** An implementation must distinguish a path through a node known to be incomplete from one through a node whose completeness is unknown.

**P4-7.11 (MUST) Inferred participation reported.** An implementation must return `TRAVERSED_INFERRED_IN_PART` where any path traversed an inferred edge and must identify the edges.

**P4-7.12 (MUST NOT) No complete outcome from defaulted completeness.** An implementation must not return `TRAVERSED_COMPLETE` where any node on any path has a completeness value of `UNDECLARED`.

### 7.4 Impact analysis outcomes

| Member | Means |
| --- | --- |
| `IMPACT_COMPLETE` | Every registered dependency source consulted and returned; no bound reached; no incomplete path; no inferred path. |
| `IMPACT_PARTIAL_SOURCE_UNAVAILABLE` | A registered dependency source could not be reached. |
| `IMPACT_PARTIAL_SOURCE_STALE` | A source responded and its registrations are older than its declared currency interval. |
| `IMPACT_PARTIAL_LINEAGE_INCOMPLETE` | A path passed through a node of `PARTIAL_UNKNOWN` or `UNDECLARED` completeness. |
| `IMPACT_PARTIAL_TRUNCATED` | A declared bound was reached. |
| `IMPACT_PARTIAL_INFERRED` | A member was reached only through an inferred edge. |
| `IMPACT_LINEAGE_ONLY` | No dependency source was consulted at all. |
| `IMPACT_STRUCTURE_GRAIN_ONLY` | Every lineage edge traversed was at structure or system grain. |
| `REFUSED` | The analysis was declined. |

The table is normative and more than one member may apply.

`IMPACT_LINEAGE_ONLY` is the most important member in this part. It names, and makes reportable, the state that nearly every real impact analysis capability is in: a traversal of a data flow graph, presented as an impact assessment, containing no rule, no determination, no schema binding, no policy attribute and no external obligation. A component in that state is not producing a weaker impact set; it is producing a different thing under the same name, and the whole of section 3.16 exists so that this member can be avoided and this member exists so that it cannot be hidden.

`IMPACT_STRUCTURE_GRAIN_ONLY` is the second. An impact set derived from table level edges reaches everything and identifies nothing, and its size is what makes it look thorough. Clause P4-7.17 requires the grain to be reported with the outcome so that the size can be read correctly.

`IMPACT_PARTIAL_SOURCE_STALE` is separated from `IMPACT_PARTIAL_SOURCE_UNAVAILABLE` because an available source with old registrations is the more dangerous of the two: it returns data, the analysis proceeds, and the dependents registered since the source stopped updating are simply absent.

**P4-7.13 (MUST) Closed impact outcome set.** An implementation must return members of the table above from every impact analysis and must not return a value outside the set.

**P4-7.14 (MUST) All applicable members returned.** An implementation must return every applicable member rather than a single one.

**P4-7.15 (MUST) Lineage only reported.** An implementation must return `IMPACT_LINEAGE_ONLY` where it consulted no dependency source, and must not present such a result as an impact set without the member.

**P4-7.16 (MUST) Stale distinguished from unavailable.** An implementation must return `IMPACT_PARTIAL_SOURCE_STALE` where a source responded with registrations older than its declared currency interval and must not return `IMPACT_COMPLETE`.

**P4-7.17 (MUST) Grain reported with the outcome.** An implementation must return `IMPACT_STRUCTURE_GRAIN_ONLY` where every traversed edge was at structure or system grain, and must return the grain distribution of traversed edges with every impact result.

**P4-7.18 (MUST NOT) No complete outcome with any partial condition.** An implementation must not return `IMPACT_COMPLETE` where any partial member applies.

### 7.5 Recording refusals

Refusals of a recording operation are consequential here for a reason particular to this component: a refused definition version means the estate contains a meaning the registry does not, and the steward will keep the meaning and abandon the registration.

| Code | Cause |
| --- | --- |
| `CHANGE_KIND_ABSENT` | A version increment with no declared change kind |
| `EXTENSION_EFFECT_ABSENT` | No declared extension effect |
| `KIND_EFFECT_INCONSISTENT` | Declared kinds and extension effect contradict |
| `CONCEPT_REPLACEMENT_REFUSED` | The increment replaces the concept |
| `INCOMPARABLE_WITHOUT_JUSTIFICATION` | An incomparable extension with no steward justification |
| `TEST_SET_ABSENT` | `UNCHANGED` claimed with no classification test set |
| `TEST_SET_INCONSISTENT` | `UNCHANGED` claimed and the run disagreed |
| `DEFINITION_TEXT_DEFICIENT` | The text fails a requirement of section 3.6 |
| `CIRCULARITY` | The text closes a cycle in the reference graph |
| `NULL_SEMANTICS_ABSENT` | A representation with no null semantics value |
| `SECOND_PREFERRED_DESIGNATION` | A second preferred designation in one language and scope |
| `DESIGNATION_COLLISION` | An identical term for a different concept with no distinguishing scope |
| `EFFECTIVITY_OVERLAP` | A second version in force in one scope at one instant |
| `SCOPE_ABSENT` | An effectivity assertion with no scope |
| `LINEAGE_KIND_GENERIC` | A lineage edge whose kind means only that data moves |
| `LINEAGE_GRAIN_ABSENT` | A lineage node or edge with no grain |
| `LINEAGE_METHOD_ABSENT` | A lineage edge with no assertion method |
| `TOOL_PIN_ABSENT` | A tool produced edge with no tool pin |
| `LINEAGE_CYCLE` | An edge closing a cycle |
| `NAME_MATCH_REALISATION` | A realisation relation produced by name matching |
| `BINDING_STRENGTH_ABSENT` | A dependency registration with no binding strength |
| `DEPENDENCY_KIND_NOT_OWNED` | A dependency kind registered by a component that does not own it |
| `MODEL_INTERNALS_SUPPLIED` | Parameters, weights or training data supplied |
| `NOT_AUTHORISED` | `Part 7` did not permit the operation |
| `MALFORMED` | The submission was not well formed |
| `IDEMPOTENCE_KEY_CONFLICT` | A seen key with a different payload |

The set is open under section 9.9. Every refusal must state what to supply, and every refusal must be counted by steward and by code, because the refusal is returned to a person who may simply stop trying and no other signal reveals that.

**P4-7.19 (MUST) Refusal codes.** An implementation must return one of the codes above, or a registered code, for every refused recording.

**P4-7.20 (MUST) Refusal states what to supply.** An implementation must state, with every refusal, what must be added or corrected.

**P4-7.21 (MUST) Refusals recorded and counted.** An implementation must record every refusal with its code, its submitting actor and the knowledge time, and must include the counts by steward and code in the signals of section 8.5.

**P4-7.22 (MUST) Test set refusal names the instances.** An implementation must name, in a refusal of code `TEST_SET_INCONSISTENT`, every instance the two versions classify differently.

**P4-7.23 (MUST NOT) No acceptance on placeholder values.** An implementation must not accept a resubmission whose missing element was supplied as a placeholder, an empty value or an unregistered default.

### 7.6 Read and analysis refusals

| Code | Cause | Retryable |
| --- | --- | --- |
| `CONCEPT_UNKNOWN` | No such concept is held | No |
| `VERSION_UNKNOWN` | No such definition version is held | No |
| `PROPOSAL_UNKNOWN` | No such proposed change is recorded | Yes, with a proposal |
| `TARGET_UNKNOWN` | The proposed change names an unknown target | No |
| `TIMES_ABSENT` | A temporal read without both instants | Yes |
| `BOUNDS_INVALID` | Requested bounds exceed declared maxima | Yes |
| `PROJECTION_UNKNOWN` | The named projection is not one of section 3.18 | Yes |
| `NOT_AUTHORISED` | `Part 7` did not permit the operation | No, without a changed decision |

**P4-7.24 (MUST) Read refusal codes.** An implementation must return one of the codes above, or a registered code, for every refused read or analysis.

**P4-7.25 (MUST) Unknown distinguished from withheld.** An implementation must return `CONCEPT_UNKNOWN` only where it holds no such concept and must return the `WITHHELD` outcome of section 7.2 where it holds one the principal may not see.

### 7.7 Outcome obligations

Normative.

| Outcome | Component records | Component emits | Reader must |
| --- | --- | --- | --- |
| `RESOLVED` | Access record | Nothing beyond the read | Nothing |
| `RESOLVED_UNAPPROVED` | Access record | Nothing beyond the read | Not treat the definition as one anyone has accepted responsibility for |
| `RESOLVED_SUPERSEDED` | Access record | Nothing beyond the read | Not treat the definition as current |
| `AMBIGUOUS_MULTIPLE`, `AMBIGUOUS_DESIGNATION` | Access record and an ambiguity detection | Ambiguity detected | Resolve the ambiguity in governance, not by choosing |
| Any traversal partial member | Run record | Nothing beyond the read | Not treat the graph as exhaustive |
| `IMPACT_LINEAGE_ONLY` | Run record and consultation state | Impact analysis partial | Treat the result as a data flow traversal and not an impact assessment |
| Any other impact partial member | As above | As above | Read the consultation state before relying on the set |
| `SEMANTIC_DRIFT` member | Member record | Semantic drift member identified | Assess the member; nothing will fail to prompt it |
| `HISTORICAL_RECLASSIFICATION` member | Member record | Historical reclassification member identified | Establish what was already published under the old meaning |
| Recording `REFUSED` | Refusal, code, actor | Definition version refused | Supply what is missing rather than abandoning the registration |

**P4-7.26 (MUST) Recording obligations honoured.** An implementation must record everything the table above requires for every outcome it produces.

**P4-7.27 (MUST) Emission obligations honoured.** An implementation must emit every event the table above requires.

**P4-7.28 (MUST) Reader obligations documented.** An implementation must document the reader obligations above and must state that it does not enforce them.

**P4-7.29 (MUST NOT) No adequacy language for a partial outcome.** An implementation must not describe an impact set as an impact assessment, an assessment of consequences or a completed analysis where any partial member of section 7.4 applies.

### 7.8 The two things this section is for

Two requirements carry the part. If the rest is compromised by schedule, these survive.

**P4-7.30 (MUST) A meaning change is never a version of the same thing.** An implementation must not, by any mechanism, configuration, default, migration, import or administrative operation, permit a definition version to carry a concept different from its predecessor's under the same concept identity.

**P4-7.31 (MUST) A data flow traversal is never an impact assessment.** An implementation must not, by any mechanism, configuration, default, aggregation, projection, interface, export or summary, represent a traversal that consulted no dependency source as an assessment of what a change would affect.
## 8. Observability and the audit record

### 8.1 The circularity, and where it stops

This component holds the governed definitions of an organisation. Its own vocabulary is a set of definitions. If they were governed instances of its own model, then the definition of "concept" would be a concept, its change would be a change declaration, and its meaning would depend on the meaning of "definition", which would depend on it.

The circularity is stopped in three places and the stopping is declared rather than hidden.

**This part's own terminology is not a governed instance.** Section 2.1 is definitional text in the sense of ISO 704 and is governed by the version identity of this part under `Part 1`, not by the model this part specifies. An implementation may register the terms of section 2.1 as concepts for convenience; if it does, those registrations are derivative and clause P4-8.2 requires them to be marked as such and forbids them from being authoritative.

**The registries are controlled documents.** The datatype systems, unit systems, relation kinds, frontier kinds and dependency kinds this component requires are content of `Part 1` document versions, per section 9.2, so their governance is external to the model they parameterise.

**Assessment is external.** Whether this component satisfies this part is assessed by `Part 12`.

**P4-8.1 (MUST) Own terminology not self governed.** An implementation must not treat the terminology of section 2.1 as governed by the model this part specifies and must obtain its meaning from the version of this part in force.

**P4-8.2 (MUST) Derivative registrations marked.** An implementation that registers the terms of this part as concepts must mark those registrations as derivative and must not present them as authoritative for the meaning of this part's clauses.

**P4-8.3 (MUST) Registries external.** An implementation must hold every registry this part requires as content of a `Part 1` document version, per section 9.2.

**P4-8.4 (MUST) Own operations recorded.** An implementation must record its own recording refusals, classification runs, traversals, impact analyses, exports and reads as entries, and must not exclude its own activity from the audit record.

### 8.2 Grain

| Subject | Grain |
| --- | --- |
| Concept | One entry per concept, plus one per state change. |
| Definition version | One entry per version. Never amended. |
| Definition text | One entry per version per language. |
| Designation | One entry per designation, plus one per status change. |
| Representation | One entry per representation. |
| Change declaration | One entry per version increment. |
| Classification instance | One entry per instance. |
| Classification run | One entry per run, plus one result per instance per version. |
| Approval citation | One entry per resolution attempt, not one per version. |
| Effectivity assertion | One entry per assertion and one per retraction. |
| Model version | One entry per version, plus one per element. |
| Realisation relation | One entry per relation, plus one per confirmation. |
| Lineage node | One entry per node. |
| Lineage edge | One entry per edge, plus one assertion source per edge. |
| Lineage completeness | One entry per node per declaration. |
| Lineage divergence | One entry per divergence. |
| Dependent registration | One entry per dependent per version. |
| Dependency source state | One entry per source per observation interval. |
| Impact analysis run | One entry per run, plus one member per affected thing, plus one pin per artifact and source. |
| Impact assessment | One entry per assessment act. |
| Recording refusal | One entry per refusal, with one outcome per failed check. |
| Read | One entry per resolution, traversal, analysis or package returned to a principal. |
| Signal | One entry per signal per observation interval. |

Two grains are worth stating explicitly.

**One approval citation entry per resolution attempt.** Not one per version. A version whose approval was unresolvable in March and approved in June has two entries, and the history of when the organisation could and could not establish approval is itself the record. A single mutable status field loses it.

**One dependent registration entry per dependent per version.** Not per concept. A dependent that rebinds from version four to version five produces a new registration, and the pair is how a rebinding becomes countable after a concept supersession.

**P4-8.5 (MUST) Declared grain.** An implementation must record at the grain of the table above, or declare a finer grain, and must not record at a coarser one.

**P4-8.6 (MUST) Approval attempts recorded individually.** An implementation must record every approval resolution attempt as its own entry and must not hold approval as a single mutable status.

**P4-8.7 (MUST) Per instance classification results recorded.** An implementation must record the result of every classification instance for both versions of every run and must not record only the run verdict.

**P4-8.8 (MUST) Counting grain stated with every count.** An implementation must state the grain of every count it reports.

### 8.3 What must be recorded with every definition version

Sufficient to establish what the term meant and how the change was justified, without this component running.

Required: the submission as received, including the idempotence key; the whole artifact set; the change declaration with its kinds, extension effect, retrospectivity, rationale and declaring actor; the classification run and its per instance results; the outcome of every precondition check, including the ones that passed; the approval resolution outcome envelope; the effectivity assertions; the impact analysis reference where one was relied upon; and the assigned knowledge time.

Recording the checks that passed is required for the reason `Part 3` clause P3-8.11 gives. A version recorded in 2028 under one precondition set, read in 2035 under a stronger one, will look deficient, and the record of which checks were applied distinguishes a version admitted under a weaker regime from one that evaded a check.

**P4-8.9 (MUST) Submission recorded as received.** An implementation must record the submission as received and must not record a normalised form in its place.

**P4-8.10 (MUST) Precondition outcomes recorded, including passes.** An implementation must record the outcome of every precondition check applied and the version of the precondition set applied.

**P4-8.11 (MUST) Classification run retained with the version.** An implementation must retain the classification run and its per instance results for as long as the version.

**P4-8.12 (MUST) Approval envelope retained in full.** An implementation must retain the whole `Part 1` resolution outcome envelope and must not retain a status alone.

**P4-8.13 (MUST) Periodic re resolution of approvals.** An implementation must re resolve the approval citation of a declared sample of definition versions on a declared cycle, must record every outcome that differs from the one previously recorded, and must declare the sample and the cycle.

### 8.4 Access records

**P4-8.14 (MUST) Reads recorded.** An implementation must record every resolution, traversal, impact analysis, projection read and evidence package export returned to a principal, with the principal, the subject, the purpose and the knowledge time.

**P4-8.15 (MUST) Withholding recorded.** An implementation must record a read that was refused or reduced by an authorisation decision, with the decision reference, whether or not the requester was told.

**P4-8.16 (MUST) Impact analyses recorded with their requester.** An implementation must record the requester of every impact analysis, since an analysis over a concept reveals the estate's dependency structure.

**P4-8.17 (SHOULD) Read records retained with the subject.** An implementation should retain the read records of a definition version for as long as the version.

### 8.5 Signals

Each signal measures a specific way in which this part's guarantees are hollowed out while every individual operation continues to succeed.

| Signal | Grain | Why it matters |
| --- | --- | --- |
| Definition versions not approved, by domain and steward | One version | The proportion of the vocabulary nobody has accepted responsibility for. |
| Approval citations unresolvable | One version | Definitions whose approval cannot be established, which is worse than none. |
| Concepts dormant | One concept | Definitions that lapsed and were not replaced. Invisible in an active or retired model. |
| Recording refusals by code and steward | One refusal | Where the estate's meanings are failing to enter the registry, and whose. |
| Refusals of code `TEST_SET_INCONSISTENT` | One refusal | Attempted narrowings declared as clarifications. The single most diagnostic signal in the part. |
| Refusals of code `CONCEPT_REPLACEMENT_REFUSED` | One refusal | Attempted redefinitions under an existing identity. |
| Concepts with no classification test set | One concept | Concepts for which no change kind claim can ever be checked. |
| Test sets with no borderline instance | One concept | Test sets that will agree across any change and prove nothing. |
| Classification runs of verdict `PARTIALLY_HUMAN` | One run | The proportion of the check that is a person's judgement rather than a mechanism. |
| Version increments made with no impact analysis reference | One version | Changes made without anyone looking. |
| Analyses diverging from the change made | One comparison | Governance satisfied on paper. |
| Representations with `UNDECLARED` null semantics | One representation | Three components maintaining the absent, withheld and unknown distinctions, thrown away here. |
| Numeric representations with no precision or scale | One representation | The mechanism by which two systems disagree about one figure. |
| Designation ambiguities detected | One designation | Words meaning two things. |
| Prohibited designations | One designation | Recorded ambiguity, which is a positive signal. |
| Element definition bindings by binding kind | One binding | The proportion of the physical estate bound `OVERLAPPING` or `ASSERTED_UNKNOWN`. |
| Conceptual and logical elements unrealised | One element | Concepts the organisation has defined and does not capture. |
| Lineage edges by assertion method | One edge | The proportion of the lineage graph that is a guess. |
| Lineage edges of semantic effect `CHANGES_MEANING` or `UNASSESSED` | One edge | Edges across which the concept differs, or nobody looked. |
| Lineage nodes of completeness `UNDECLARED` | One node | The proportion of the graph over which no impact set can be exhaustive. |
| Lineage frontiers of kind `NOT_YET_MAPPED` or `FRONTIER_UNDECLARED` | One frontier | Work outstanding, and work nobody has noticed. |
| Lineage divergences from `Part 3`, by direction | One divergence | Undocumented processes, and documented flows that do not run. |
| Dependency sources not supplying within their interval | One source | Every impact analysis afterwards is quietly narrower and looks the same. |
| Impact analyses by outcome member | One run | How often the analysis was `IMPACT_LINEAGE_ONLY` or partial. |
| Impact members classified `SEMANTIC_DRIFT` and unassessed beyond an age | One member | Known silent drift nobody has looked at. |
| Concepts carrying an `EXTERNAL_OBLIGATION` dependency | One concept | The concepts whose redefinition has consequences outside the organisation. |
| Dependents still bound to a superseded concept | One dependent | Rebinding not done after a concept replacement. |
| Inferential model versions with training definition drift | One model version | Models measuring something they were not fitted for. |
| Reads with no recorded purpose | One read | Erosion of the access record. |

**P4-8.18 (MUST) Signals produced.** An implementation must produce every signal in the table above at a declared interval and must declare the interval.

**P4-8.19 (MUST) Signals derived from entries.** An implementation must derive every signal from recorded entries and must be able to enumerate the entries behind any signal value.

**P4-8.20 (MUST NOT) No suppression of a signal.** An implementation must not provide a means of disabling, filtering or thresholding a signal such that a non zero value is reported as zero.

**P4-8.21 (MUST) Refusal signal reaches the steward and the steward's owner.** An implementation must make the recording refusal signal available to the submitting steward and to the party accountable for the domain, since a refusal returned to one person may end there.

**P4-8.22 (MUST) Source cessation is a standing measure.** An implementation must produce the dependency source signal continuously rather than on demand, since its value depends on absence and nobody will request it.

**P4-8.23 (MUST) Drift signals trended.** An implementation must be able to report the count of unassessed `SEMANTIC_DRIFT` members over time, so that a growing backlog is distinguishable from a stable one.

**P4-8.24 (SHOULD) Signal thresholds declared.** An implementation should declare, for each signal, the value at which it requires attention, and should record the declaration as a controlled document under `Part 1`.

### 8.6 The evidence package

A self describing export sufficient to establish what a term meant, on whose authority, and what depended on it, without this component running.

Contents, all required.

The concept with its identity, domains, steward and state.

The definition version in full: every text with its language, authoritativeness, exclusions, source citation and source relation; every designation with its status and kind; every representation with its datatype, unit, precision, cardinality and null semantics; and the value domain binding with its `Part 10` pin.

The change declaration: kinds, extension effect, retrospectivity, rationale, declaring actor and impact analysis reference.

The classification test set with every instance, its asserted membership, its rationale, and the per instance results of every run against this version.

The approval resolution outcome envelope in full, and the content of the approving document version where obtainable, or the statement that it was not.

Every effectivity assertion and retraction bearing on this version.

The predecessor and successor version identities, and the extension change history of the concept.

The design lineage immediately upstream and downstream of the definition, with edge kinds, grains, assertion methods, tool pins, completeness declarations and frontiers.

Every dependent registration against this version, with its kind, source, owning component and binding strength.

Every impact analysis in which this version was the target or a member, with its outcome, consultation state and pins.

The registries referenced, at the versions referenced, or the statement that they could not be obtained.

The statement of the completeness limits: that the dependency index is only as complete as the sources that supplied it, and that lineage completeness is declared per node rather than established.

A statement of the version of this part the package claims to conform to.

**P4-8.25 (MUST) Package sufficiency.** An implementation must produce a package sufficient to establish what the term meant, on whose authority, and what depended on it, without the implementation running and without access to any component of this standard other than the package.

**P4-8.26 (MUST) Test set and its results included.** An implementation must include the classification test set and the per instance results of every run against the version, since they are the only evidence bearing on whether a declared change kind was honest.

**P4-8.27 (MUST) Approval content included or its absence stated.** An implementation must include the content of the approving document version, or must state that it could not be obtained together with the reason and the knowledge time of the attempt.

**P4-8.28 (MUST) Limit statements included.** An implementation must include the completeness limit statements in every package.

**P4-8.29 (MUST) Absence stated, not omitted.** An implementation must state, for every required element it could not include, that it could not be included and why.

**P4-8.30 (MUST) Package digest.** An implementation must record a digest over a declared canonical form of the package and must include the profile identity.

**P4-8.31 (MUST) Self description.** An implementation must include a description of the package's structure sufficient for a reader with no knowledge of the implementation to locate each required element.

### 8.7 Retention

**P4-8.32 (MUST) Retention obtained, not assigned.** An implementation must obtain the retention period of every record it holds from a retention rule expressed under `Part 1` and must not assign one of its own.

**P4-8.33 (MUST) Definitions outlive the data they describe.** An implementation must retain a definition version, its texts, its representation and its change declaration for at least as long as the longest retained data described by it, where that period is known to it, and must record where it is not known.

**P4-8.34 (MUST) Definitions outlive determinations that relied on them.** An implementation must retain a definition version for at least as long as the longest retained `Part 3` determination that relied upon it, since a determination whose definition has been disposed of cannot be accounted for.

**P4-8.35 (MUST) Test sets retained with their versions.** An implementation must retain a classification test set and its run results for as long as any version they were run against.

**P4-8.36 (MUST) Separate retention per structure.** An implementation must permit the retention of definitions, models, lineage and impact analyses to be set independently, since their volumes and their evidential value differ by orders of magnitude.

**P4-8.37 (MUST) Disposal recorded and citable.** An implementation must record the disposal of any record it holds with its authorisation reference, must retain the identity of what was disposed of, and must make the disposal citable as a `Part 3` frontier of kind `RETENTION_EXPIRED`.

**P4-8.38 (MUST NOT) No disposal of a definition with undischarged dependents.** An implementation must not dispose of a definition version against which an active dependent registration stands and must report the dependents in the refusal.

### 8.8 What cannot be changed

**P4-8.39 (MUST NOT) No amendment of an entry.** An implementation must not modify any recorded entry by any mechanism, including administrative, migration, correction and support mechanisms.

**P4-8.40 (MUST NOT) No amendment of a classification result.** An implementation must not modify a recorded classification run or its per instance results and must record a later run as a further run.

**P4-8.41 (MUST NOT) No amendment of an impact run.** An implementation must not modify the members, pins or consultation state of a recorded impact analysis run.

**P4-8.42 (MUST) Migration preserves identity and digests.** An implementation that migrates its records must preserve every concept identity, every version identity and every recorded digest unchanged, must record the migration as an entry, and must not recompute a digest under a different canonical form profile without recording both.

**P4-8.43 (MUST NOT) No bulk reclassification on import.** An implementation must not assign a change kind, an extension effect, a completeness value, an assertion method or a binding kind in bulk during an import, and must record every imported artifact lacking one as carrying the undeclared value for that field.
## 9. Extension model

### 9.1 Closed sets, open sets, and why

Five sets in this part are closed.

**The change kind set of section 3.8 is closed.** A consumer branches on it to decide whether it must act, and an unrecognised kind will be treated as harmless. This is the strongest closure in the part.

**The extension effect set of section 3.8 is closed.** It is the field the classification test checks against, and a sixth value would have no defined relation to the test.

**The lineage edge kind set of section 3.13 is closed.** Ten members, and the reason for closure is that the two members implementations habitually omit, `FILTER_DEPENDENCY` and `DEFAULT_SUBSTITUTION`, would be the first casualties of an open set. A registry would let an implementation register a generic flow kind and satisfy the letter of clause P4-3.90.

**The consequence class set of section 3.17 is closed.** A new class is a new kind of harm and consumers must be exhaustive over it.

**The three resolution, traversal and impact outcome sets of section 7 are closed.**

Everything else is open under a registry: datatype systems, unit systems, concept relation kinds, model kinds and their layer sets, path schemes, lineage frontier kinds, dependency kinds, digest algorithms, canonical form profiles, refusal codes, event types and evaluation purposes.

**P4-9.1 (MUST) Closed sets not extended.** An implementation must not add a member to the change kind set, the extension effect set, the lineage edge kind set, the consequence class set or the outcome sets of section 7.

**P4-9.2 (MUST) Unknown member is a defect, not a default.** An implementation must treat receipt of a member outside a closed set as a defect and must not map it to a member it does recognise.

**P4-9.3 (MUST) Open sets registered.** An implementation must admit a member of an open set only through the registry mechanics of section 9.2 and must not accept an unregistered member at any interface.

**P4-9.4 (MUST NOT) No generic edge kind by registration.** An implementation must not register a lineage frontier kind, a dependency kind or any other registered member whose effect is to permit an undifferentiated data flow edge, an undeclared completeness or an unjustified frontier to satisfy a clause of section 3.

### 9.2 Registry mechanics

A registry is content of a controlled document version under `Part 1`, so a registration has an effective date, an approval and an author. Keys are permanent and never reused. A member is deprecated rather than removed. Every registration states what the member means, not only what it is called.

The retention obligation on these registries is the longest in the standard, for a specific reason: a definition version recorded in 2028 references a datatype system version, and interpreting that version's representation in 2050 requires the datatype system as it stood in 2028. Clause P4-9.8 states the obligation.

**P4-9.5 (MUST) Registry as controlled document.** An implementation must express every registry as content of a document version under `Part 1` and must resolve the registry version in force at the knowledge time of any entry referencing it.

**P4-9.6 (MUST NOT) No key reuse.** An implementation must not reuse a registry key and must not remove a member that any retained entry references.

**P4-9.7 (MUST) Deprecation rather than removal.** An implementation must deprecate a member with an effective date and a reason and must continue to interpret entries referencing it.

**P4-9.8 (MUST) Registry version recorded and retained.** An implementation must record the registry version in force when an entry referencing a registered member was recorded, and must retain that registry version for at least as long as the entry.

**P4-9.9 (MUST) Semantics in the entry.** An implementation must not admit a registry entry that does not state the meaning of the member in terms a consumer can act on.

### 9.3 Datatype and unit system registries

A representation is meaningless without the system its datatype is drawn from. A datatype named `DECIMAL` means one thing in one system and another in another, and the difference between them is exactly the precision behaviour that makes two systems disagree about a figure.

A datatype system registration must state: the system's identity and version; the members and their value spaces; the precision and rounding behaviour of each numeric member; the collation applicable to each character member; the representation of absence, if the system has one; and the mapping to at least one other registered system where the implementation asserts one.

A unit system registration must state the members, their dimensions, and the conversion factors the implementation asserts between members. A conversion factor is an assertion and must be attributed, for the same reason a lineage edge must be.

**P4-9.10 (MUST) Datatype semantics stated in full.** An implementation must state every element listed above in every datatype system registration.

**P4-9.11 (MUST) Numeric behaviour declared.** An implementation must state the precision and rounding behaviour of every numeric datatype member, since a representation without it cannot be compared across systems.

**P4-9.12 (MUST) Collation declared for character members.** An implementation must state the applicable collation and the Unicode version for every character datatype member, consistently with `Part 2` clause P2-6.3.

**P4-9.13 (MUST) Cross system mappings attributed.** An implementation must record an asserting actor for every mapping it asserts between datatype systems or between unit members and must not present a mapping as a property of the systems.

**P4-9.14 (MUST NOT) No implicit system.** An implementation must not admit a representation whose datatype system is not recorded, per clause P4-3.5.

### 9.4 Path scheme registry

A path addresses an element within a model or a physical structure. A registration states the syntax, what a path denotes, and whether a path remains valid across changes to the structure.

Stability matters here as it does in `Part 3` section 9.4. A path expressed as an ordinal position denotes a different element after an insertion, and a lineage edge or a realisation relation recorded against it silently comes to point at something else.

**P4-9.15 (MUST) Stability declared.** An implementation must declare, for every registered path scheme, whether a path remains valid across changes to the structure, and must record the scheme with every path.

**P4-9.16 (SHOULD) Stable schemes preferred.** An implementation should record lineage and realisation paths in a scheme declared stable and should record both a stable and a positional path where only the positional one is available.

**P4-9.17 (MUST NOT) No cross scheme comparison.** An implementation must not compare, deduplicate or match paths recorded in different schemes.

### 9.5 Model kind and layer registry

A model kind registration states: the kind's identity; the layers a model of that kind may occupy; the element kinds admissible within it; whether realisation relations to another layer are required; and the `Part 1` publication expectation.

The requirement that earns this registry is clause P4-9.19. An organisation with a canonical model, a dimensional model and an exchange model has three model kinds whose relations to the conceptual layer differ, and registering the layer set per kind is how a realisation requirement becomes enforceable rather than aspirational.

**P4-9.18 (MUST) Layers declared per kind.** An implementation must record the layers admissible for every registered model kind and must refuse a model version whose layer is not among them.

**P4-9.19 (MUST) Realisation requirement declared and enforced.** An implementation must record, per model kind, whether realisation relations to another layer are required, and must be able to report every element of such a kind carrying neither a realisation relation nor a `NOT_REALISED` assertion.

**P4-9.20 (MUST) Element kinds declared.** An implementation must record the element kinds admissible within each model kind and must refuse an element of an inadmissible kind.

### 9.6 Concept relation kind registry

A relation kind registration states: what the relation asserts; whether it is transitive; whether it is symmetric; whether an impact analysis traverses it and in which direction; and what evidence must accompany an assertion of it.

Traversal is the field that matters. `GENERALISATION` is traversed downward by an impact analysis, because narrowing a general concept affects its specialisations. `ASSOCIATIVE` is not traversed at all, because association carries no implication about meaning. An implementation that traverses every relation kind produces the reachability failure of section 11.4 through a second route.

**P4-9.21 (MUST) Traversal behaviour declared per kind.** An implementation must record, for every registered concept relation kind, whether an impact analysis traverses it and in which direction, and must not traverse a kind whose registration does not permit it.

**P4-9.22 (MUST) Transitivity declared.** An implementation must record whether each relation kind is transitive and must not compute a transitive closure over a kind not declared transitive.

**P4-9.23 (MUST) Required evidence declared.** An implementation must state what evidence must accompany an assertion of each relation kind and must refuse an assertion lacking it.

### 9.7 Digest and canonical form registries

**P4-9.24 (MUST) Both registered and both recorded.** An implementation must register digest algorithms and canonical form profiles separately and must record both with every digest.

**P4-9.25 (MUST) Deprecation without invalidation.** An implementation must be able to deprecate a digest algorithm without invalidating any recorded digest and must record an additional digest under a current algorithm rather than replacing the original.

**P4-9.26 (MUST NOT) No digest without a profile.** An implementation must not record a digest whose canonical form profile is not recorded.

### 9.8 Dependency kind and frontier kind registries

A dependency kind registration states: what the dependency is; the component that owns it and is entitled to register it; the currency interval within which registrations are expected; how an impact analysis classifies a member reached through it; and whether a declaring actor may register it in place of a component.

The currency interval is the field that makes clause P4-7.16 enforceable. Without a declared interval there is no such thing as a stale source, and a source that stopped supplying registrations two years ago is indistinguishable from one that has nothing to supply.

A lineage frontier kind registration states, as in `Part 3` section 9.3, what the kind reports, whether it is a legitimate permanent terminus, and what evidence must accompany it. `NOT_YET_MAPPED` and `FRONTIER_UNDECLARED` are registered as illegitimate and must not be re registered as legitimate.

**P4-9.27 (MUST) Owning component declared per dependency kind.** An implementation must record the component entitled to register each dependency kind and must refuse a registration from another, per clause P4-4.14.

**P4-9.28 (MUST) Currency interval declared per source.** An implementation must record an expected currency interval for every dependency kind and source and must use it to determine staleness.

**P4-9.29 (MUST) Classification behaviour declared per dependency kind.** An implementation must record how an impact analysis classifies a member reached through each dependency kind.

**P4-9.30 (MUST) Frontier legitimacy declared.** An implementation must record whether each lineage frontier kind is a legitimate permanent terminus and must not register `NOT_YET_MAPPED` or `FRONTIER_UNDECLARED` as legitimate.

### 9.9 Code and event registries

**P4-9.31 (MUST) Refusal codes registered with remedy.** An implementation must state, in every refusal code registration, what must be supplied or corrected.

**P4-9.32 (MUST) Event types registered.** An implementation must register every event type it emits beyond the minimum set of section 4.8.

### 9.10 Composition

Four compositions are distinguished and confusing them produces specific defects.

**A concept related to a concept.** A relation, traversed or not according to its registered kind. This is the only composition of concepts the model provides.

**A model containing elements, and an element realising an element.** Containment within a version, and realisation across layers. Both permitted, and realisation is required to be declared rather than inferred, per clause P4-3.79.

**A definition composed of definitions.** A concept whose definition text references other concepts, which is required by clause P4-3.33 and constrained against circularity by clause P4-3.34. The composition is by reference and never by embedding, per clause P4-3.32.

**A model version including another model version.** Permitted only by pinned version, for the reason `Part 2` clause P2-9.32 gives for rule sets: inclusion by lineage would make the including version's content change without the including version changing, which defeats the purpose of versioning it.

There is a fifth thing that resembles composition and is prohibited. A **composite concept** whose meaning is defined as the conjunction of other concepts, with no definition text of its own. It is prohibited because such a concept has no reviewable meaning: a reader must reconstruct it from its parts, the reconstruction is not recorded, and a change to any part changes the composite silently. Clause P4-9.36 requires a definition text for every concept regardless of how it is composed.

**P4-9.33 (MUST) Model inclusion by pinned version only.** An implementation must permit a model version to include another model version only by pinned version and must not permit inclusion by lineage.

**P4-9.34 (MUST NOT) No cyclic model inclusion.** An implementation must refuse a model version whose inclusion graph contains a cycle.

**P4-9.35 (MUST) Composition depth bounded and declared.** An implementation must declare the maximum inclusion depth it accepts and must refuse a version exceeding it.

**P4-9.36 (MUST NOT) No composite concept without a definition text.** An implementation must refuse a concept whose meaning is expressed only as a composition of other concepts and must require a definition text satisfying section 3.6.

**P4-9.37 (MUST) Shared elements versioned in every including model.** An implementation must treat a change to a model element referenced by more than one model version as producing a new version of each, and must pin the element version in each.
## 10. Standards and specifications

### 10.1 How the citations in this part are to be read

Every entry states what the source supplies, the edition established as current at the date of this part, and whether this part's account rests on specification text or on secondary sources. Section 13.1 lists the sources not obtained.

Currency was established from publisher catalogues and status pages rather than inferred. Three findings bear on how a reader should treat this section. The principal standard for this subject was restructured in 2023 and its part numbering changed, so a citation to a part number without an edition is likely to name a withdrawn document. One of its parts is presently under revision. And the parts most relevant to two of the three subjects the brief named, lineage and impact analysis, do not exist in any reviewed standard.

**P4-10.1 (MUST) Cited edition recorded.** An implementation must record the edition or version of every external standard it relies upon and must not cite a standard without its edition.

**P4-10.2 (MUST) Basis marked.** An implementation must record, for every control it adopts from a source named in this section, whether the basis is specification text or practice.

### 10.2 Metadata registries: the ISO/IEC 11179 family

The family was restructured for the 2023 editions and the new part numbering does not correspond to the old. This is the most consequential currency finding in the part.

| Part | Status established | Supplies |
| --- | --- | --- |
| ISO/IEC 11179-1:2023, Framework | Edition 4, published January 2023. Available at no charge. | The framework relating the parts, and the statement that in all parts of the standard metadata means descriptions of data and that it does not treat metadata generally. |
| ISO/IEC 11179-3:2023, Metamodel for registry common facilities | Edition 4, published January 2023. Cancels and replaces the third edition of 2013 and incorporates its Amendment 1 of 2020. An Amendment 1 dated 2026 has been published. | Common facilities for **identification, designation, definition and registration** of any registry item. A Core Model with basic classes and predefined datatypes. A Concept class each instance of which models a concept. Modelling conventions, conformance rules and modular packages. Mapping facilities. |
| ISO/IEC 11179-31:2023, Metamodel for data specification registration | Published 2023. | Registration of data elements, data element concepts, object classes, properties, conceptual domains, conceptual domain subsets, value meanings, value domains, value domain subsets, datatypes, permissible values, units of measure and derivation rules. |
| ISO/IEC 11179-32:2023, Metamodel for concept system registration | Published 2023. | Registration of concept systems including ontologies, and a pointer to ISO/IEC 19763-3 where an ontology is defined elsewhere. |
| ISO/IEC 11179-33:2023, Metamodel for data set registration | Published 2023. | Registration of data sets, including provenance, quality, fitness for role and risk assessments of a data set. |
| ISO/IEC 11179-35:2023, Metamodel for model registration | Published 2023. | Registration of models and their metamodels, covering information models, data models, process models and models of web services, and the mappings between models, between metamodels, and between models and their metamodels. |
| ISO/IEC 11179-4:2004, Formulation of data definitions | Second edition. The 1995 first edition is withdrawn. Its status within the restructured series was not established. | Requirements and recommendations for constructing definitions, addressing semantics only. |
| ISO/IEC 11179-5:2015, Naming principles | Published 2015. **Under revision**; a Draft International Standard was reported as expected to replace it. | Naming of concepts, data element concepts, conceptual domains, data elements and value domains, and principles by which naming conventions can be developed. |
| ISO/IEC 11179-6, Registration | Published. Edition not established. | The information to be specified, the conditions to be met and the procedures to be followed for registration. |

Three of these bear directly on the design.

**11179-3's four common facilities** are the framing this part adopts. Identification, designation, definition and registration as separate facilities of any registry item is the same separation section 3.2 makes, and the Concept class is the identity anchor of section 3.4.

**11179-31's data element as a data element concept bound to a value domain** is the representation side of the triad. This part narrows it: a representation here excludes the membership of the value set, which section 12.10 allocates to `Part 10`.

**11179-35's model registration** is the model repository half of this part's title, including the mapping facilities that section 3.11's realisation relations use.

The account of 11179-1, 11179-31, 11179-32, 11179-33 and 11179-35 rests on published scope statements. The account of 11179-3 rests on its foreword, scope and a secondary description of its clause structure. The account of 11179-4's five definition requirements, which section 3.6 adopts as clauses, rests on secondary sources and is flagged in section 13.1 as requiring verification before approval.

### 10.3 Terminology work

| Standard | Status established | Supplies |
| --- | --- | --- |
| ISO 704:2022, Terminology work, principles and methods | Fourth edition, July 2022, 80 pages. Cancels and replaces ISO 704:2009, which is cancelled. | The links between **objects, concepts, definitions and designations**. General principles for the formation of terms and for the writing of definitions. The treatment of an object as anything perceivable or conceivable, whether material, immaterial or imagined, with the observation that arguing about whether an object exists is unproductive. |
| ISO 1087:2019, Terminology work and terminology science, vocabulary | Published 2019. | The vocabulary of terminology work, cited by ISO 704 for terminology work and concept entry. |
| ISO 10241-1:2011 | Published. | Requirements for terminological entries in standards, which ISO 704 explicitly does not cover. |

ISO 704's object, concept, definition, designation chain is the strongest available anchor for section 3.2, and its treatment of the object is what permits section 2.1 to define concepts without taking a position on the existence of what they denote. The account rests on the standard's scope, its foreword and quoted extracts, not on its clause text.

### 10.4 Model registration and interoperability

| Standard | Status established | Supplies |
| --- | --- | --- |
| ISO/IEC 19763-1:2023, Metamodel framework for interoperability, Framework | Published 2023, superseding the 2015 second edition. | A framework of normative metamodels for registering many types of model, each expressed as a UML class diagram and in text, working with ISO/IEC 11179-3. The explicit statement that the models themselves may live in a model repository or exist only as paper documents, and that the series specifies no physical structure for a registry. |
| ISO/IEC 19763 further parts | Family includes a core model and basic mapping of models, information model registration, form design registration, ontology registration, and a technical report on on demand model selection. Editions of individual parts not established. | Model registration metamodels, including model to model mapping. |

The 19763-1 statement that the series specifies no physical registry structure is the reason this part specifies entities and obligations rather than a schema, and section 13.1 records that the individual part editions were not established.

### 10.5 Adjacent standards deliberately not used

| Standard | Why not used here |
| --- | --- |
| W3C SKOS | Concept schemes and semantic relations for controlled vocabularies. The governance of a concept scheme's membership is `Part 10`'s, and adopting SKOS here would put a vocabulary model in two components. |
| W3C PROV | Provenance. Used in `Part 3` for instance lineage and cited here only for the boundary of section 12.3. |
| OMG MOF and UML | Metamodelling and model notation. Relevant to how an information model is expressed, which this part deliberately does not specify. |
| ISO/IEC 25012, data quality model, and the ISO 8000 series | Data quality characteristics and master data quality. A definition's quality requirements here are the definitional requirements of section 3.6, not the quality of the data described. |
| ISO/IEC 42001 and ISO/IEC 23894 | Artificial intelligence management and risk. Relevant to inferential models and allocated to `Part 13`. |

### 10.6 Supporting specifications

| Specification | Used for |
| --- | --- |
| RFC 2119 and RFC 8174 | Requirement keywords. |
| BCP 47 | Language tags on every designation and definition text. |
| RFC 3339 and ISO 8601 | Instant representation for the three clocks. |
| The Unicode Standard and the Unicode Collation Algorithm | Collation declaration for character datatypes under clause P4-9.12. |
| RFC 8785 | An example of a canonical form profile of the kind section 9.7 requires. |
| RFC 9457 | A model for conveying a refusal of the kind sections 7.5 and 7.6 specify. |
| CloudEvents | A model for the event envelope of section 4.8. |

The following clauses rest on practice rather than specification text and are collected so a reader can see the set: clause P4-3.35 on stating exclusions where a boundary is contested; clause P4-3.60 on requiring borderline instances; clause P4-3.99 on pinning the tool that produced a lineage edge; clause P4-3.107 on declaring lineage completeness per node; clause P4-3.119 on registering external obligations; clause P4-4.36 on detecting dependency source cessation; clause P4-6.34 on a deterministic primary budget; clause P4-8.10 on recording precondition passes; and clause P4-8.13 on periodic re resolution of approvals.

**P4-10.3 (MUST) Practice basis recorded.** An implementation that adopts a clause listed in the paragraph above as a control must record that its basis is practice.

### 10.7 Named conflicts

Five conflicts and tensions bear on this part. None is resolved by averaging.

**Where the boundary between a definition and a constraint falls.** ISO/IEC 11179-31 registers derivation rules and permissible values within the metadata registry, so a value constraint is registry content. This part excludes evaluable constraints by clause P4-1.7 and allocates them to `Part 2`, keeping only the value domain binding and the representation. **Position taken.** The registry holds what a thing is and the shape of its permitted values; it does not hold an evaluable rule. Section 13.3 records that the boundary is contestable and that 11179 draws it differently.

**Whether a concept system belongs in the metadata registry.** ISO/IEC 11179-32 provides for registering concept systems including ontologies, and points to ISO/IEC 19763-3 where the ontology is defined elsewhere. This part registers concepts and their relations and allocates controlled vocabulary membership to `Part 10`. **Position taken.** The concept and its relations are here; the enumerated members of a value set are there. The split is not the one 11179 makes and section 13.4 records it.

**Whether naming is standardisable.** ISO/IEC 11179-5 provides principles by which naming conventions can be developed rather than a convention, and is under revision. **Position taken.** This part specifies the structure of a designation, its status set and the rules against reuse and inference, and specifies no naming convention. An organisation's convention is its own and belongs in a controlled document.

**Whether a definition's adequacy can be specified.** ISO/IEC 11179-4 states requirements for the formulation of definitions and describes its rules as mandatory and testable for compliance. In practice the requirements that can be tested mechanically are the weakest ones, and the ones that matter, such as whether the definition states the concept, cannot be. **Position taken.** The testable requirements are clauses in section 3.6, the untestable ones are stated as clauses that a steward satisfies rather than a machine checks, and the classification test set of section 3.9 is offered as the only mechanical check on whether a definition's extension is what the steward says it is. Section 13.2 records that this is a partial answer.

**Whether the registry specifies a physical structure.** ISO/IEC 19763-1 states explicitly that the series does not. ISO/IEC 11179-3 specifies a conceptual data model. **Position taken.** This part follows both: entities and obligations, no schema, no serialisation, per section 3.

### 10.8 What none of the standards supplies

Twelve requirements in this part have no source in any reviewed standard. Two of the three subjects the authoring brief named for this part fall almost entirely into this list, which is itself the most important finding in section 10.

The change kind taxonomy of section 3.8, and in particular the refusal of a concept replacement under an existing identity. No reviewed standard classifies a version increment by whether the meaning changed.

The declared extension effect, and the requirement that it be consistent with the declared change kinds.

Retrospectivity as a declared property of a change, and its consequence for data already published.

The classification test set as a required component of a definition and as the bridge between a declaration and the meaning it claims.

Lineage. Neither ISO/IEC 11179 nor ISO/IEC 19763 specifies the derivation of a data element from other data elements. 11179-33 mentions the provenance of a data set as registrable metadata, and 19763's mapping facilities relate models to models rather than elements to elements. The typed edge kinds of section 3.13, the grain requirement, the assertion method and the frontier treatment are all unsourced.

The distinction between design lineage and instance lineage, and the divergence check between them.

Lineage completeness as a declared property per node.

Impact analysis. No reviewed standard specifies it at all. The consequence class taxonomy, the requirement that an impact set span dependency sources rather than lineage alone, and the outcome `IMPACT_LINEAGE_ONLY` are all unsourced.

Dependent registration as a cross component index, and the treatment of an external obligation as a registrable dependency.

The requirement that a semantic change's materiality be a named actor's assessment rather than a computation.

The governance of an inferential model's interface as a set of definition bindings, and the detection of training definition drift.

The requirement that null semantics be declared, and its relation to the absent, withheld and unknown distinctions the three prior parts maintain.

**P4-10.4 (MUST) Unsourced requirements identified.** An implementation must be able to state, for any control it implements under this part, whether the requirement has a cited source in this section or is listed in section 10.8 as unsourced.
## 11. Anti patterns

Each entry names the mechanism by which the failure occurs, states the consequence, and marks whether the prohibition rests on specification text or on practice.

### 11.1 The dictionary that is edited

**Mechanism.** The registry holds one entry per term. A change to the meaning is an edit to the entry. The previous text is kept in a history table with a timestamp and no classification of what changed.

**Consequence.** The purpose question cannot be answered, and the reason is not that the old text is gone but that the relation between the change and its consumers was never recorded. This is the failure narrated in section 1.3 and it is the state of nearly every data dictionary in existence.

**Basis.** Practice.

**P4-11.1 (MUST NOT) No editable definition.** An implementation must record every change as a new version with a declared change kind and must not permit a recorded version to be amended, per clauses P4-3.15 and P4-3.47.

### 11.2 The redefinition under the same name

**Mechanism.** A measure is redefined and the identifier is kept, because forty systems reference it and rebinding forty systems is expensive. The change is recorded as a revision.

**Consequence.** Every one of the forty continues to work and now means something different. Nothing fails, no test breaks, and the divergence is permanent and retrospective. This is the most damaging single event this part exists to prevent, and it is prevented only by refusing it at the moment of registration.

**Basis.** Practice.

**P4-11.2 (MUST NOT) No concept replacement as a version.** An implementation must refuse a version increment that replaces the concept and must require a new concept identity, per clauses P4-3.49 and P4-7.30.

### 11.3 The narrowing declared as a clarification

**Mechanism.** A steward tightens a definition, believes the tightening merely makes explicit what was always intended, and declares the change clarifying. Sometimes the belief is correct.

**Consequence.** Where it is not correct, the extension has changed and every consumer has been told it need do nothing. The declaration is made in good faith, which is why a declaration alone cannot prevent it and why section 3.9 exists.

**Basis.** Practice.

**P4-11.3 (MUST NOT) No unchecked claim of no change.** An implementation must run the classification test set before accepting a version increment declaring an unchanged extension and must refuse it on inconsistency, per clauses P4-3.59 and P4-3.61.

### 11.4 Reachability presented as impact

**Mechanism.** The impact analysis is the transitive closure of the lineage graph. It is computed correctly, it is fast, and it is presented as an assessment of what a change would affect.

**Consequence.** Two failures at once. It over reports: at structure grain, applied transitively, the answer approaches the whole estate, and a report naming four thousand affected objects is not actionable and will be ignored. And it under reports the things that matter: the rule that cites the term, the determination that relied on it, the regulatory return defined over it and the model fitted on it are not in the lineage graph and do not appear.

**Basis.** Practice. No reviewed standard specifies impact analysis at all.

**P4-11.4 (MUST NOT) No traversal as an impact set.** An implementation must assemble an impact set from dependency registrations as well as lineage, must return `IMPACT_LINEAGE_ONLY` where it consulted no source, and must not alias a traversal projection to an impact projection, per clauses P4-3.122, P4-7.15, P4-3.135 and P4-7.31.

### 11.5 Completeness assumed

**Mechanism.** Lineage is captured for the systems that expose it and not for the rest. Nothing records which nodes are complete. An impact analysis traverses what exists and returns a result.

**Consequence.** The false negative rate is unknown and unknowable, and the result looks identical to a complete one. A reader cannot distinguish a thorough answer from a fragment, so the answer is either over trusted or discarded, and both are worse than a qualified answer.

**Basis.** Practice.

**P4-11.5 (MUST NOT) No assumed completeness.** An implementation must record completeness per node, must not default it to complete, and must mark every path through an incomplete node, per clauses P4-3.107, P4-3.109 and P4-6.31.

### 11.6 Lineage by name matching

**Mechanism.** Edges and realisation relations are created by matching column names across systems. It works most of the time and requires no cooperation from anybody.

**Consequence.** It is wrong in exactly the cases that cost money: two columns with the same name carrying different concepts, and one concept carried by columns with different names. The first produces a false edge that makes an impact analysis reach something unaffected. The second produces a missing edge that makes it miss something affected. Neither is visible, because the graph looks complete and plausible.

**Basis.** Practice.

**P4-11.6 (MUST NOT) No inference presented as assertion.** An implementation must record the assertion method on every edge and relation, must refuse a realisation relation produced by name matching, and must not report an inferred edge as declared, per clauses P4-3.79, P4-3.98 and P4-3.101.

### 11.7 The unpinned parser

**Mechanism.** Lineage is parsed from code by a tool. The edges are recorded. The tool's version is not.

**Consequence.** The graph cannot be compared with itself over time, because when the tool is upgraded thousands of edges change and nobody can tell whether the estate changed or the parser improved. Every trend, every completeness measure and every impact comparison across the upgrade is meaningless.

**Basis.** Practice.

**P4-11.7 (MUST NOT) No unpinned tool assertion.** An implementation must refuse an edge produced by a tool without a pin to the tool and its version, per clause P4-3.99.

### 11.8 Structure grain sold as lineage

**Mechanism.** Lineage is captured at table or file grain, because that is what the platform exposes. It is called lineage without qualification and used for impact analysis.

**Consequence.** An edge saying one table derives from three tells an analyst that any change to any column of any of the three may affect any column of the first. Transitively, everything affects everything. The result is not merely imprecise; it is uninformative, and its size makes it look thorough.

**Basis.** Practice.

**P4-11.8 (MUST NOT) No unqualified grain.** An implementation must record grain on every node and edge and must return `IMPACT_STRUCTURE_GRAIN_ONLY` where every traversed edge was at structure or system grain, per clauses P4-3.92 and P4-7.17.

### 11.9 The filter dependency nobody records

**Mechanism.** Lineage tools trace value derivation. A report filtered on a status code has no value derived from that code, so no edge is recorded.

**Consequence.** Narrowing the definition of the filter concept changes every figure in the report and reaches nothing in the lineage graph. This is the most systematic false negative in lineage practice and it affects exactly the concepts most likely to be redefined, since status, eligibility and classification concepts are both the most contested and the most used as filters.

**Basis.** Practice.

**P4-11.9 (MUST NOT) No omission of filter and conditional dependencies.** An implementation must record an edge of kind `FILTER_DEPENDENCY` or `CONDITIONAL` wherever an input determined which values are present or which derivation applied, per clause P4-3.93.

### 11.10 The dependency index nobody populates

**Mechanism.** Section 3.16 requires other components to register their dependencies. It is optional work for them and mandatory infrastructure for this component. Nobody does it.

**Consequence.** Every impact analysis is `IMPACT_LINEAGE_ONLY` and the outcome member becomes the normal case rather than an exception. The component then has all the cost of the model and none of its value, and the outcome member is the only thing that reveals it.

**Basis.** Practice.

**P4-11.10 (MUST) Source state tracked and cessation detected.** An implementation must record dependency source state, must detect a source that has ceased to supply registrations, and must produce the signal continuously, per clauses P4-3.117, P4-4.36 and P4-8.22.

### 11.11 The stale source that answers

**Mechanism.** A dependency source is reachable and its registrations are two years old, because the integration broke quietly. Every impact analysis consults it, gets a response, and proceeds.

**Consequence.** Worse than an unavailable source, because the analysis reports as complete. Every dependent registered in two years is absent and nothing indicates it.

**Basis.** Practice.

**P4-11.11 (MUST NOT) No stale source as current.** An implementation must declare a currency interval per source, must return `IMPACT_PARTIAL_SOURCE_STALE` where registrations exceed it, and must not return `IMPACT_COMPLETE`, per clauses P4-9.28 and P4-7.16.

### 11.12 The impact report of everything

**Mechanism.** The analysis is thorough, the graph is at element grain, the sources are populated, and the report names two thousand affected objects with no consequence classification.

**Consequence.** Nobody reads it. The correct response to a two thousand item list with no severity is to ignore it, and the organisation learns that impact analysis produces noise. The failure is not the size of the set; it is the absence of the classification that would let it be triaged.

**Basis.** Practice.

**P4-11.12 (MUST) Consequence class on every member.** An implementation must classify every impact member and must not return an unclassified set, per clause P4-3.124.

### 11.13 Semantic drift unreported

**Mechanism.** The consequence classification exists and reports structural breaks, because those are derivable from a datatype comparison. Semantic drift is not derivable from a comparison of artifacts, so it is not reported.

**Consequence.** The one class of consequence that nothing else will surface is the one absent from the report. Every dependent that tracks the latest version continues to operate and now means something else, and the report that was supposed to catch it lists only the things that would have failed anyway.

**Basis.** Practice.

**P4-11.13 (MUST) Semantic drift derived and emitted.** An implementation must classify as `SEMANTIC_DRIFT` every member reached through an unpinned dependency where the extension effect is not unchanged, and must emit an event per member, per clauses P4-3.125 and P4-4.35.

### 11.14 The impact analysis that is an approval

**Mechanism.** The change process requires an impact analysis. The analysis runs, the report is attached to the change request, and the presence of the report is what permits the change to proceed.

**Consequence.** The analysis becomes a procedural artifact rather than an assessment. Nobody assesses the unassessed members, because the report's existence discharged the obligation. Within a year the analysis is run automatically at submission and read by nobody.

**Basis.** Practice.

**P4-11.14 (MUST NOT) No analysis as approval.** An implementation must not represent an impact analysis as an approval, an authorisation or a recommendation, and must not permit an interface to imply that a change is safe, per clauses P4-1.6 and P4-3.131.

### 11.15 The change that was not the change assessed

**Mechanism.** An impact analysis is run against a proposal. The proposal is revised during review. The change is made. The original analysis is the one on file.

**Consequence.** The governance record shows an analysis and a change, and they are of different things. This is the commonest way a change control process is satisfied on paper, and it is undetectable without an explicit comparison.

**Basis.** Practice.

**P4-11.15 (MUST) Analysis compared with the change made.** An implementation must be able to compare a recorded change declaration with the proposed change its referenced analysis assessed and must report where they differ, per clause P4-3.129.

### 11.16 The unapproved definition consumed as authoritative

**Mechanism.** A definition is registered so that work can proceed. Approval is pursued later, or not. Consumers read the registry, find a definition, and use it.

**Consequence.** The registry becomes the authority for meanings nobody accepted responsibility for, which is worse than a registry with gaps, because a gap prompts a question and a definition does not.

**Basis.** Practice.

**P4-11.16 (MUST NOT) No unapproved version as resolved.** An implementation must return `RESOLVED_UNAPPROVED` and must carry the approval status with every version in every interface, per clauses P4-3.68, P4-4.23 and P4-7.2.

### 11.17 Null semantics undeclared

**Mechanism.** A representation records a datatype and a cardinality. What an empty value means is left to the consumer.

**Consequence.** `Part 1` distinguishes absent from withheld, `Part 2` yields indeterminate for a withheld path, and `Part 3` requires a search's completeness to be declared. All three distinctions arrive at the physical layer as an empty column and are lost here, so three components maintain a distinction that is discarded at the one place it becomes data.

**Basis.** Specification text, in that all three prior parts require the distinction to be maintained.

**P4-11.17 (MUST) Null semantics declared.** An implementation must record a null semantics value on every representation, must not infer it, and must report every representation carrying `UNDECLARED`, per clauses P4-3.42 and P4-3.43.

### 11.18 The designation as the key

**Mechanism.** The term is the identifier. Systems reference the definition by name, reports are keyed on the label, and interfaces pass the string.

**Consequence.** A rename becomes a breaking change and is therefore never done, so incorrect and misleading terms persist for decades. The alternative failure is that the rename is done and breaks things nobody enumerated, since the set of places using the name was never recorded.

**Basis.** Specification text, in that ISO/IEC 11179-3 separates identification from designation as distinct facilities.

**P4-11.18 (MUST NOT) No designation as an identifier.** An implementation must expose a designation independent identifier at every interface and must not require a designation to address a concept, per clause P4-3.9.

### 11.19 The lexical resolver

**Mechanism.** Designation lookup normalises case, strips punctuation, and matches loosely, because users type inconsistently and exact matching is unhelpful.

**Consequence.** Two designations that differ meaningfully resolve to one concept. The resolution is confident and wrong, and it is wrong precisely where two similar strings name two different things, which is the case a registry exists to disambiguate.

**Basis.** Practice.

**P4-11.19 (MUST NOT) No lexical equivalence.** An implementation must match designations exactly and must require an equivalence to be a recorded designation, per clauses P4-6.12 and P4-6.13.

### 11.20 The concept merged

**Mechanism.** Two concepts are found to mean the same thing. They are merged into one, and the redundant identity is deleted or aliased.

**Consequence.** The ability to answer what each meant before the merge is destroyed, and the merge may have been wrong. Data recorded under each is now indistinguishable, and if the two were in fact subtly different the difference is unrecoverable.

**Basis.** Practice.

**P4-11.20 (MUST NOT) No concept merger.** An implementation must record an asserted equivalence as a relation and must retain both identities and both histories, per clause P4-3.19.

### 11.21 The definition of a definition

**Mechanism.** The registry's own vocabulary is registered as governed concepts within itself, for consistency. The concept of "concept" is a concept.

**Consequence.** The meaning of the registry's own model depends on entries in the registry, which can be changed by the same process the model governs. A steward can redefine "extension effect" and thereby change what every change declaration meant.

**Basis.** Practice.

**P4-11.21 (MUST NOT) No self governed vocabulary.** An implementation must obtain the meaning of this part's terminology from the version of this part in force and must mark any registration of those terms as derivative, per clauses P4-8.1 and P4-8.2.

### 11.22 The test set of easy cases

**Mechanism.** A classification test set is required, so one is created from clear examples: obvious members and obvious non members.

**Consequence.** The set agrees across every change, including the narrowings it was meant to catch, and its agreement is reported as evidence that the extension is unchanged. The check runs, passes and proves nothing, which is worse than not having it because it produces assurance.

**Basis.** Practice.

**P4-11.22 (MUST) Borderline instances required and reported.** An implementation must require a borderline instance where the boundary is declared contested and must report every test set containing none, per clause P4-3.60.

### 11.23 The generated definition

**Mechanism.** Definitions are generated: from column comments, from a model tool's descriptions, from an inferential model asked to describe a field. The registry fills up quickly.

**Consequence.** The definitions are plausible, unattributed and unowned. A steward who did not write a definition will not defend it, and a definition nobody will defend is not a governed definition. The registry's coverage improves and its authority does not exist.

**Basis.** Practice.

**P4-11.23 (MUST NOT) No generated definition as a steward's assertion.** An implementation must not generate a definition text, change kind, extension effect or classification and record it as a steward's assertion, per clause P4-6.45.

### 11.24 The model that is the registry

**Mechanism.** The physical model is imported and becomes the registry's content. Every column is a concept. There are ninety thousand.

**Consequence.** Nothing is governed, because governance at that volume is impossible and the volume was chosen by the estate rather than by anyone. The concepts that matter are indistinguishable from the ones that do not, and the stewardship requirement of clause P4-3.16 becomes a formality satisfied by assigning a team name to ninety thousand rows.

**Basis.** Practice.

**P4-11.24 (SHOULD NOT) No wholesale physical import as concepts.** An implementation should not register a physical structure's elements as governed concepts in bulk, should register them as model elements bound to concepts where a concept exists, and should be able to report elements bound to no concept.

### 11.25 The inferential model outside the registry

**Mechanism.** Models are governed by a model risk process of their own, with its own inventory. Their input definitions are not registered here, because the model inventory records them.

**Consequence.** An impact analysis cannot reach models, which are the consumers least likely to fail visibly when a definition shifts and most likely to have been fitted under an earlier meaning. The model inventory records what the model uses and not which governed concept version it was fitted against, so the drift of section 3.12 is invisible in both places.

**Basis.** Practice.

**P4-11.25 (MUST) Model interfaces bound and drift reportable.** An implementation must record an element definition binding for every declared input and output of an inferential model version and must be able to report training definition drift, per clauses P4-3.84 and P4-3.87.

### 11.26 The lineage that is corrected to match observation

**Mechanism.** `Part 3` reports an observed derivation the design does not contain. The design lineage is updated to include it.

**Consequence.** The divergence disappears and with it the only signal that an undocumented process exists. The design record now describes what the systems do rather than what they were designed to do, and the two structures become one, which is the merge `Part 3` section 12.4 exists to prevent.

**Basis.** Specification text, in `Part 3` clause P3-3.110 and section 12.4 of that part.

**P4-11.26 (MUST NOT) No edge alteration on divergence.** An implementation must record a divergence as a finding and must not create, alter or delete a lineage edge in response to one, per clauses P4-3.110 and P4-4.13.
## 12. Boundaries with other parts

Each subsection states four things: what this component delegates, what it must not absorb, the naive design that conflates the two, and the reciprocal declaration the other part must make. Subsection numbers correspond to part numbers, so section 12.7 states the boundary with `Part 7` and section 12.14 states the boundary with `Part 0`. Section 12.4 is deliberately unused, since it would designate this part. Numbers are permanent.

A boundary is reciprocal. If this part declares that it delegates something, the receiving part must declare that it owns it, in the same terms.

Three of this part's boundaries carry obligations already committed by the parts on the other side, and this section discharges them: `Part 1` clauses P1-12.8 and P1-12.9, `Part 2` clauses P2-12.8 and P2-12.9, and `Part 3` clauses P3-12.10 and P3-12.11.

**P4-12.1 (MUST) Declared allocation.** An implementation must be able to state, for every capability named in this section as delegated, which component provides it, and must not provide it within this component.

**P4-12.2 (MUST) Recording rather than substitution.** Where a delegated capability is unavailable, an implementation must take the behaviour of section 4.7 and must not substitute a local implementation of it.

**P4-12.3 (MUST NOT) No reaching past a neighbour.** An implementation must not read or write the internal state of another component named in this section and must interact with it only through that component's declared interface.

### 12.1 Boundary with Part 1, controlled documents and records

This subsection is the reciprocal declaration `Part 1` section 12.4 requires.

**Delegated.** The approval and signature of every definition version and model version. The publication of a definition as a controlled document, which is a rendition of the definition. The identity, versioning, effectivity and retention of every document that publishes or authorises anything here, including this part's registries. The retention rules governing this component's own records.

**Must not absorb.** Approval. This component records the resolution outcome and holds no approval, signature or approver.

**Naive conflation.** Two forms, both named in `Part 1` section 12.4. The data dictionary becomes a document, so the authoritative definition is a paragraph in a version of a word processing file and consumers either parse prose or keep a second copy. Or this component acquires approvals and effective dates of its own, so the organisation has two answers to what was approved and when.

**Position taken, and the precise split.** This component owns definition version identity and definition effectivity. `Part 1` owns approval and owns the effectivity of the published rendition. The distinction is fine and it is the one `Part 1` clause P1-12.9 draws: `Part 1` must not assign version identity to a definition, and `Part 1`'s reciprocal requirement is that this part not own the approval or effectivity of published renditions. A definition version therefore has its own identity and its own effectivity here, and becomes authoritative by an approval obtained there.

**Reciprocal.** This part declares that it owns definition identity and versioning, that it does not own the approval or effectivity of published renditions, and that where it needs an approved publication it obtains it from `Part 1`. That is the declaration `Part 1` requires and clauses P4-12.4 through P4-12.6 make it binding.

**P4-12.4 (MUST) Approval obtained and recorded in full.** An implementation must obtain the approval of every definition version and model version by resolution against `Part 1`, must record the whole resolution outcome envelope, and must not hold an approval of its own, per clauses P4-3.66 and P4-3.67.

**P4-12.5 (MUST NOT) No rendition as the definition.** An implementation must not treat a published document as the authoritative definition and must record the relation between a rendition and the definition version it was generated from.

**P4-12.6 (MUST) Rendition effectivity not held.** An implementation must not hold or assert the effectivity of a published rendition and must hold only the effectivity of the definition version itself.

### 12.2 Boundary with Part 2, business rules and constraint evaluation

This subsection is the reciprocal declaration `Part 2` clause P2-12.8 and section 12.4 of that part require.

**Delegated.** The expression, evaluation and versioning of every constraint on a governed concept. The rule that says which values of a concept are permissible, in what circumstances, with what enforcement level.

**Must not absorb.** Constraints. A definition says what a thing is; a rule says what is permitted. Clause P4-1.7 forbids an evaluable expression in a definition.

**Naive conflation.** The definition acquires a validation expression, because the constraint is obviously part of what the field is. There are then two places a constraint can live, the one here has no enforcement level, no statement, no authority and no verdict taxonomy, and a violation of it is a registry defect rather than a rule outcome. The converse conflation is a rule defining its own terms, which `Part 2` clause P2-12.9 forbids.

**Reciprocal.** This part declares that it owns term identity and versioning, that it exposes a definition version obtainable by pin, and that it is queryable about supersession so that `Part 2` clause P2-3.80 can be satisfied. Clauses P4-12.7 through P4-12.9 make it binding.

**P4-12.7 (MUST) Definition versions obtainable by pin.** An implementation must expose every definition version obtainable by pin, with its whole artifact set, so that `Part 2` clause P2-12.8 can be satisfied.

**P4-12.8 (MUST) Supersession queryable.** An implementation must be able to report, for any pinned definition version, whether it has been superseded and by what, so that `Part 2` clause P2-3.80 can be satisfied, and must not silently rebind a pin to a successor.

**P4-12.9 (MUST) Rule term references registered as dependencies.** An implementation must accept `Part 2` rule term references as dependent registrations of kind `RULE_TERM_REFERENCE` and must include them in every impact set, per section 3.16.

### 12.3 Boundary with Part 3, provenance and audit ledger

This subsection is the reciprocal declaration `Part 3` clause P3-12.10 and section 12.4 of that part require.

**Delegated.** Instance lineage: what actually happened to actual values in actual runs. The provenance of determinations that relied on a definition, and the reverse index by which they are found. The recording of this component's own determinations where they are cited by others.

**Must not absorb.** Instance lineage. This component holds design lineage, being what the design asserts, and clause P4-1.8 forbids recording the derivation of a particular value.

**Naive conflation.** The two lineages merged, in either direction, as `Part 3` section 12.4 states. The merge destroys the divergence check, which is the most valuable output either structure produces.

**Reciprocal.** This part declares that it owns definition and design lineage identity, that it does not record instance level transformations, and that it exposes design lineage assertions obtainable by pin so that `Part 3` clause P3-3.105 can be satisfied. Clauses P4-12.10 through P4-12.12 make it binding.

**P4-12.10 (MUST) Design lineage exposed by pin.** An implementation must expose every design lineage assertion obtainable by pin, with its edge kind, grain, assertion method and completeness declaration, so that `Part 3` clause P3-3.105 can be satisfied.

**P4-12.11 (MUST NOT) No instance lineage held.** An implementation must not record the derivation of a particular value in a particular run and must record only asserted design relations.

**P4-12.12 (MUST) Divergence recorded in both directions and resolved in neither.** An implementation must record a divergence reported by `Part 3` as a finding, must be able to report both directions per clause P4-3.111, and must not alter a lineage edge in response.

### 12.5 Boundary with Part 5, decision engine

**Delegated.** Every selection. Whether a proposed change should proceed. Which of several candidate definitions or representations to adopt where more than one is available. The criterion by which a steward's choice is made, where that criterion is itself a governed artifact.

**Must not absorb.** Selection. An impact analysis reports consequences; it does not recommend.

**Naive conflation.** The impact analysis acquires a verdict: a risk score, a traffic light, a recommendation to proceed. The report then becomes the decision, the decision has no recorded criterion, and the analysis's own qualifications are collapsed into the score, per section 11.14.

**Reciprocal.** `Part 5` must declare that it does not resolve definitions, that a decision requiring a governed meaning obtains it by resolution here, and that a selection criterion expressed over a concept is registered here as a dependency of kind `DECISION_CRITERION`.

**P4-12.13 (MUST NOT) No recommendation.** An implementation must not produce a score, grade, rating or recommendation from an impact analysis and must return the members with their consequence classes.

**P4-12.14 (MUST) Decision criteria registered as dependencies.** An implementation must accept `Part 5` selection criteria as dependent registrations of kind `DECISION_CRITERION` and must include them in every impact set.

### 12.6 Boundary with Part 6, workflow and process orchestration

**Delegated.** The process by which a definition is drafted, reviewed, approved and published. The routing of a proposed change, the chasing of an impact assessment, and the state of a change request.

**Must not absorb.** Process state. The registration states of section 5.2 record what was established, not who is waiting for whom.

**Naive conflation.** The registration state becomes a position in a change workflow, so a definition version has no state when no request is open and reconstructing its history requires reading process instances designed to be transient.

**Reciprocal.** `Part 6` must declare that it does not own registration state, definition identity or effectivity, that it invokes the recording operations of section 4.2, and that its own retention does not govern the retention of the definitions it routed.

**P4-12.15 (MUST) Registration state independent of process.** An implementation must compute and expose the registration state of every definition version without reference to any process instance and must remain correct where the orchestrator is replaced.

**P4-12.16 (MUST NOT) No process identity required.** An implementation must not require a process instance identifier in order to record, resolve, traverse or analyse anything specified in this part.

### 12.7 Boundary with Part 7, policy decision point and authorisation

**Delegated.** Every authorisation decision: whether a principal may register a concept, record a version, assert a lineage edge, run an impact analysis, run the reverse dependency enumeration or export a package. Whether a principal may see a concept at all.

**Must not absorb.** Policy. This component supplies definitions as attributes where a decision depends on one and records decision references.

**Naive conflation.** Stewardship is treated as authorisation, so the recorded steward of a concept becomes the entitlement to change it. Stewardship is accountability for meaning and authorisation is a policy decision with an effective date and a scope, and merging them creates a second authorisation authority nobody governs.

**Reciprocal.** `Part 7` must declare that it owns policy evaluation, that it obtains governed definitions by resolution here where a policy reads one as an attribute, that a policy attribute expressed over a concept is registered here as a dependency, and that it does not hold definition state.

**P4-12.17 (MUST) Decisions consumed, not made.** An implementation must record the `AUTHREF` of every authorisation decision that permitted an operation and must not evaluate policy.

**P4-12.18 (MUST NOT) No stewardship as entitlement.** An implementation must not derive an entitlement from a recorded stewardship and must obtain every entitlement from `Part 7`.

**P4-12.19 (MUST) Policy attributes registered as dependencies.** An implementation must accept `Part 7` policy attribute bindings as dependent registrations of kind `POLICY_ATTRIBUTE` and must include them in every impact set.

### 12.8 Boundary with Part 8, human task and case management

**Delegated.** The work a person does: assessing an impact member, classifying a borderline instance, reviewing a definition text, investigating a lineage divergence, and the case in which that work sits.

**Must not absorb.** Assessment work management. This component records that an assessment was made, by whom, with what reason.

**Naive conflation.** The impact member and the task are one entity, so closing the task closes the member, and an unassessed semantic drift is disposed of with a work item rather than assessed.

**Reciprocal.** `Part 8` must declare that closing a task does not alter an impact member, a classification instance or a registration state, and that every assessment is effected by a recording operation here whose outcome the task records.

**P4-12.20 (MUST) Assessments independent of tasks.** An implementation must retain every impact assessment and classification assertion unchanged after any task concerning it is disposed of.

**P4-12.21 (MUST NOT) No task driven closure.** An implementation must not provide a means by which a task completion classifies an impact member, transitions a registration state or resolves a divergence without a recorded act naming an actor.

### 12.9 Boundary with Part 9, schema and contract registry

**Delegated.** Schema identity, schema versioning, compatibility between schema versions, and the validation of an instance against its schema.

**Must not absorb.** Schema validation and schema versioning. This component holds the concept a schema element claims to realise.

**Naive conflation.** The schema becomes the definition, because the schema is machine readable and enforced. A field's meaning is then whatever its type and its name suggest, there is no concept identity, and a redefinition is a schema change with no extension effect and no impact analysis. The converse conflation is this component versioning schemas, which gives a schema two version identities.

**Position taken.** A schema says what a well formed instance is. A definition says what its elements mean. The boundary is stated the same way `Part 2` section 12.9 states its own: by authority rather than by mechanism.

**Reciprocal.** `Part 9` must declare that it owns schema identity and compatibility, that it does not define the meaning of a schema element, that it registers every element's concept binding here as a dependency of kind `SCHEMA_ELEMENT_BINDING`, and that it exposes schema versions obtainable by pin.

**P4-12.22 (MUST NOT) No schema versioning or validation.** An implementation must not assign version identity to a schema and must not validate an instance against one.

**P4-12.23 (MUST) Schema bindings registered as dependencies.** An implementation must accept `Part 9` schema element bindings as dependent registrations and must include them in every impact set.

**P4-12.24 (MUST) Binding quality reportable.** An implementation must be able to report schema element bindings by binding kind, so that a schema bound `OVERLAPPING` to a concept is distinguishable from one bound exactly, per clause P4-3.82.

### 12.10 Boundary with Part 10, reference and master data management

**Delegated.** The membership of every permissible value set, its governance, its versioning, its retention, and the meaning of each member.

**Must not absorb.** Value set membership. A representation here names and constrains a value set by pin; it does not enumerate it.

**Naive conflation.** The registry enumerates a code list inside a representation, because the list is short and the binding is inconvenient. The list then has two masters and a member added in one place is missing in the other with no signal. The converse conflation is `Part 10` holding concept definitions, which puts the vocabulary in two components.

**Reciprocal.** `Part 10` must declare that it owns value set membership and versioning, that it does not define concepts, that it retains every superseded set version for at least as long as the longest retained definition version binding to it, that it does not remove or reuse member keys, and that it reports a correction to a set as a dependency affecting event to this component.

**P4-12.25 (MUST) Value sets bound by pin only.** An implementation must bind a representation to a permissible value set by pin and must not hold, enumerate, extend or correct the set's membership, per clauses P4-3.44 and P4-3.45.

**P4-12.26 (MUST) Value set change surfaces as a change kind.** An implementation must record a change to the bound value set version as a version increment of change kind `VALUE_DOMAIN_CHANGE` and must not permit the binding to follow a set version silently.

**P4-12.27 (MUST) Set realisations registered as dependencies.** An implementation must accept `Part 10` realisation registrations as dependencies of kind `REFERENCE_SET_REALISATION` and must include them in every impact set.

### 12.11 Boundary with Part 11, content addressed artifact store

**Delegated.** The durable storage and retrieval by digest of the octets of anything this component pins or exports: model artifacts, transformation artifacts, classification instance data and evidence packages.

**Must not absorb.** Storage semantics. This component owns the mapping from a pin to a digest and a canonical form profile.

**Naive conflation.** The store holds the model artifact and becomes the model's identity, so a model version is a digest rather than a governed thing with a layer, elements and realisation relations.

**Reciprocal.** `Part 11` must declare that it holds no concept identity, no version identity and no lineage, and that it does not delete content on its own authority.

**P4-12.28 (MUST) Digest is the interface.** An implementation must address stored content by digest under a declared canonical form profile and must not rely on a location or path as identity.

**P4-12.29 (MUST NOT) No identity in the store.** An implementation must not hold concept identity, version identity, change declarations or lineage in the artifact store and must not accept them from it.

### 12.12 Boundary with Part 12, conformance and assurance harness

**Delegated.** All assessment of whether an implementation satisfies this part, including the verification of the properties this part requires an implementation to demonstrate: projection agreement, classification run correctness, traversal determinism and impact reproducibility.

**Must not absorb.** Self assessment. This component runs the classification tests of section 6.5, the sampling of clause P4-8.13 and the circularity detection of clause P4-3.34, and records their results; it does not assess itself against this part.

**Naive conflation.** The component's own classification run results are presented as evidence that the vocabulary is well governed. A test set of easy cases passes every run, per section 11.22, and the pass rate becomes the assurance metric.

**Reciprocal.** `Part 12` must declare that it obtains the clause set from this part by resolution, that it records the version of this part an assessment was made against, that it does not write to this registry while assessing it, and that it independently examines the composition of classification test sets rather than accepting their pass rates.

**P4-12.30 (MUST) Read only assessment.** An implementation must expose everything `Part 12` requires through read operations and must not require a write in order to be assessed.

**P4-12.31 (MUST NOT) No self assessment as assessment.** An implementation must not present its own classification run results, sampling or detection results as an assessment of conformance, per clause P4-1.13.

**P4-12.32 (MUST) Test set composition exposed.** An implementation must expose the composition of every classification test set, including the count of borderline instances, so that `Part 12` can assess whether a passing run proves anything.

### 12.13 Boundary with Part 13, model invocation and agent execution

**Delegated.** Everything about the running of an inferential model: its invocation, its inputs and outputs on any occasion, its cost, its retries, its non determinism, its performance and its behaviour. The model artifact itself.

**Must not absorb.** Invocation and behaviour. This component holds an inferential model's identity, version and declared interface, and nothing else, per clause P4-1.17.

**Naive conflation.** Two forms. This component acquires model performance and monitoring, because it already holds the interface, and becomes a model risk system with no observation of behaviour. Or `Part 13` holds the input definitions, so the concepts a model consumes are recorded in a model inventory that has no version identity for them and no impact analysis over them, which is the failure of section 11.25.

**Position taken.** The interface is governed here because it is a set of definition bindings and because an impact analysis must reach it. The artifact and its behaviour are `Part 13`'s. The seam is the interface: this component says what the model claims to consume and produce, and that component says what happened when it ran.

**Reciprocal.** `Part 13` must declare that it owns the invocation record and the model artifact, that it does not hold definition identity or versioning, that it exposes a model artifact reference obtainable by pin so that clause P4-3.88 can be satisfied, and that it obtains the concept a declared input binds to by resolution here.

**P4-12.33 (MUST) Interface held, behaviour not.** An implementation must record an inferential model's identity, version and declared interface bindings and must not hold, assert or report its performance, fitness or behaviour, per clause P4-3.89.

**P4-12.34 (MUST) Model reference pinned.** An implementation must record a pin to the `Part 13` artifact each registered interface describes and must refuse an interface registration lacking one.

**P4-12.35 (MUST) Training definition drift reportable to Part 13.** An implementation must expose the training definition drift of clause P4-3.87 so that `Part 13` can record it against the model's invocations.

### 12.14 Boundary with Part 0, system composition

**Delegated.** What happens when all the components run at once: authority over facts more than one component touches, the seams at which values cross boundaries, the propagation of non results, and pinning across a unit of work spanning several components.

**Must not absorb.** Composition. This part states what it holds and what it refuses, and does not state how the dependency registration obligation is imposed on components that have no incentive to meet it.

**Reciprocal.** `Part 0` must declare that this component holds authority over concept identity, definition version identity, definition effectivity, designations, representations, change declarations, information model identity, design lineage and the dependency index, and that `Part 1` holds authority over the approval of all of it. It must state, for every seam, what must hold and how a violation appears here. It must in particular resolve six questions this part hands it.

How the dependency registration obligation of section 3.16 is imposed, given that this part can index what it is given and cannot compel what it is not, and that an unpopulated index reduces every impact analysis to `IMPACT_LINEAGE_ONLY`. This is the same shape as the question `Part 3` section 13.10 hands forward about registration.

What a component must do when it holds a meaning this registry refuses to record, since the refusals of section 7.5 are all detectable at recording and none is remediable by this component.

How a concept supersession propagates: which component compels the eleven dependents of the worked demonstration to rebind, and what happens to those that do not.

Whether the absent, withheld, unknown and not applicable distinctions maintained by `Part 1`, `Part 2` and `Part 3` and declared here as null semantics have one enterprise wide answer or one per representation.

How a unit of work spanning this component and `Part 9` pins one definition version across both, so that a schema and the definition it realises cannot drift within a release.

Whether the frontier concept, now specified in `Part 3` for chains of reasoning and in this part for lineage graphs, and the pattern by which a governed record has no lifecycle while assertions about it do, should each be stated once for the whole standard.

**P4-12.36 (MUST) Authority declared, not assumed.** An implementation must not accept an assertion about concept identity, definition version identity, effectivity, a change declaration or a lineage edge from another component, and must require every such fact to be established by its own operations.

**P4-12.37 (MUST) Unpopulated index visible to composition.** An implementation must make the dependency source state and the impact outcome distribution available as signals, since neither an unpopulated index nor a ceased source can be remedied within this component, per clauses P4-8.21 and P4-8.22.
## 13. What could not be established

A question recorded as open can be closed by someone with access to the source. A question closed by inference cannot be reopened, because nothing in the document reveals that an inference was made.

### 13.1 Sources not obtained in full text

The following were not available in full text. This part's account of each rests on published catalogue entries, scope statements, forewords, sample pages and secondary literature. No clause reproduces text from any of them.

**ISO/IEC 11179-4:2004, Formulation of data definitions.** The five requirements section 3.6 adopts as clauses P4-3.30 through P4-3.32, being that a definition be stated in the singular, state what the concept is, be a descriptive phrase or sentence, use only commonly understood abbreviations and not embed definitions of other data, rest entirely on secondary sources. This is the most load bearing unverified claim in the part and should be checked first. The claim that the standard describes its rules as mandatory and testable for compliance also rests on a secondary source.

Separately, **the status of Part 4 within the restructured series was not established.** The 2023 restructure introduced Parts 1, 3, 31, 32, 33 and 35. Whether Part 4 was withdrawn, absorbed into another part, or remains current alongside them could not be determined from the sources obtained, and one source describing Part 4 as active also described the series structure in its pre 2023 form and is therefore unreliable on this point. A reviewer with catalogue access should settle it, because if Part 4 was withdrawn then section 3.6's clauses have no standing source and belong in section 10.8.

**ISO/IEC 11179-3:2023.** The foreword, scope, the four common facilities and a description of the clause structure were obtained. The clause text was not. The Concept class reference at clause 6.4.2.2 rests on a sample page. An **Amendment 1 dated 2026** was established as published and its content was not obtained at all, which is a material gap given that this part's section 3.2 rests on the edition it amends.

**ISO/IEC 11179-1, -31, -32, -33 and -35:2023.** Scope statements obtained from the publisher. No clause text. Section 10.2's account of what each supplies is therefore an account of its scope and not of its requirements. Part 31's registration of derivation rules and Part 35's mapping facilities are both cited in this part's design reasoning and neither was examined.

**ISO/IEC 11179-5:2015 and -6.** Scope of Part 5 obtained, together with the statement that it is expected to be replaced by a Draft International Standard. Whether that replacement has since been published was not determined. Part 6's edition was not established at all.

**ISO 704:2022.** The scope, foreword, publication date, page count and the object, concept, definition, designation chain were obtained, along with quoted extracts on the treatment of an object. The clause text was not obtained, and section 3.2's use of the chain as an anchor rests on the scope statement.

**ISO 1087:2019 and ISO 10241-1:2011.** Cited only as referenced by ISO 704. Neither was obtained or assessed.

**ISO/IEC 19763-1:2023 and the further parts.** The scope of Part 1 was obtained, including the statement that the series specifies no physical registry structure. The editions of the individual parts were established only from a 2015 listing and are therefore likely stale; the family composition as at the date of this part was not determined.

Not obtained and not assessed at all: ISO/IEC 25012 and the ISO 8000 series, which may bear on section 3.6's quality requirements; W3C SKOS, which may have a better treatment of designation status than the enumeration of section 3.5; OMG MOF and the ISO adoptions of UML, whose currency relative to the OMG versions was not examined and which bear on section 3.11; and the practice standards for data lineage interchange, which were not examined at all and which are the only likely source for anything in section 3.13.

**P4-13.1 (MUST) Verification before approval.** An implementation or reviewer must verify the claims listed in section 13.1 against the source standards before this part is approved and must record the outcome of each verification against this section.

### 13.2 Whether the classification test set does the work claimed for it

Section 3.9 offers the test set as the bridge between a declared change kind and the meaning it claims, and section 6.5 admits that most runs will be `PARTIALLY_HUMAN`. The admission is worth taking seriously, because it means the mechanism is in most cases a structured prompt rather than a check.

What the mechanism actually delivers, at its weakest, is this: at the moment a steward claims a change is clarifying, someone must classify a set of recorded borderline instances against both texts, and the answers are recorded per instance with an attribution and a date. That is materially more than a declaration and it is not a mechanical check.

Three weaknesses follow and none is addressed.

The steward who writes the test set and the steward who classifies against it are frequently the same person, so the check is a person disagreeing with themselves, which is possible and not reliable.

A test set can be curated to agree, per section 11.22, and the borderline instance requirement of clause P4-3.60 is enforceable only where the boundary has been declared contested, which is itself a declaration by the same steward.

The instances are recorded at first version and the concept's difficult cases change over time, so a set adequate in 2027 may miss the boundary that matters in 2033.

**Open.** Whether a stronger bridge exists. Three candidates were considered and none pursued. Independent classification, where two parties classify the same instances against the same texts and disagreement is the finding rather than agreement being the pass. Population testing, where the two definitions are applied to a data sample and the size of the symmetric difference is measured, which is mechanical and requires the instance data section 3.9 makes optional and is only available where the definitions are executable, which by clause P4-1.7 they are not. And requiring instances to be contributed by consumers rather than by the steward, which changes who is being tested.

The second candidate deserves attention despite the tension with clause P4-1.7, because it would turn an extension effect declaration into a measured quantity. A reviewer who thinks the prohibition on executable definitions should be relaxed for this purpose should say so; section 13.3 is the related question.

### 13.3 The boundary between a definition and a constraint

Clause P4-1.7 excludes evaluable constraints from definitions and allocates them to `Part 2`. ISO/IEC 11179-31 registers derivation rules and permissible values within the metadata registry, so the standard draws the line differently.

The test offered in section 12.2, that a definition says what a thing is and a rule says what is permitted, works at the extremes. In the middle there is a large class of statements that are both. A definition of "active customer" that says the customer must have transacted within twenty four months is a definition containing a threshold, and the threshold is a rule. Moving it to `Part 2` leaves a definition that says less than the organisation means; leaving it here puts an unevaluated constraint in the registry.

The present treatment is that the threshold stays in the definition text as prose and the evaluable form lives in a rule that cites the concept, with no mechanism ensuring the two agree. That is the same unbridged correspondence `Part 2` section 13.2 records for its own statement and declaration, appearing a second time at a different boundary.

**Open.** Whether the two should be bound as `Part 2` binds its own triad, so that a definition and the rule realising it are approved together and their correspondence is asserted by an accountable actor. That would be consistent and would create a cross component binding no other part attempts.

### 13.4 Where a concept system ends and reference data begins

Section 12.10 allocates value set membership to `Part 10` and concepts and their relations here. ISO/IEC 11179-32 provides for registering concept systems including ontologies in the metadata registry, so the standard again draws the line differently.

The difficulty is that a controlled vocabulary is both. Each member of a code list has a meaning, so each member is a concept with a definition, a designation and a boundary. Treating the list as reference data puts a hundred concept definitions in a component that governs membership rather than meaning; treating it as concepts puts a hundred registrations in a component that will not be able to govern them at that volume, per section 11.24.

The present treatment is that this component governs the concept the list realises and `Part 10` governs the members. That leaves the meaning of an individual code member unowned by either, which is the commonest source of the question nobody can answer: what exactly does status code 07 mean.

**Open.** Whether a value meaning, in the sense ISO/IEC 11179-31 registers, should be a governed concept here bound to a member there. That would resolve the gap and would multiply the registry's volume by the size of the organisation's code lists, which is the trade section 11.24 warns about from the other direction.

### 13.5 Whether the change kind set is right

Section 3.8's nine kinds are closed, and closure is the strongest commitment in the part.

Two doubts. `EDITORIAL` and `CLARIFYING` may be one kind, since the distinction between them is whether the text's effect changed, and a change that does not change the effect is by definition editorial. Keeping them separate is defensible because the two are declared differently, and it may be a distinction without a consequence.

More seriously, there may be a missing kind. A change to the **exclusions statement** of section 3.6, where the definition's positive text is unchanged and a boundary case is newly stated to be out, is presently a `NARROWING` if the exclusion changes the extension and a `CLARIFYING` if it makes an existing exclusion explicit. Which of the two it is is exactly the disputed question, and the test set is the only arbiter. A separate kind for it would make the ambiguity visible rather than forcing a declaration.

**Open.** Both. A reviewer should test the set against a sample of real definition changes from at least three domains before the closure is accepted, on the same basis `Part 3` section 13.7 recommends for its role set.

### 13.6 Whether an impact set can be bounded usefully

Section 6.7 requires depth, breadth and budget bounds and says nothing about what values are useful. Section 11.12 names the failure of an unbounded set and section 11.4 names the failure of a bounded one at the wrong grain, and this part offers no guidance between them.

The honest position is that the useful bound depends on the consequence classification rather than on distance. A member three hops away classified `SEMANTIC_DRIFT` through an external obligation matters more than a member one hop away classified `NO_IMPACT_ASSERTED`. Bounding by distance is therefore the wrong axis, and it is the only axis specified.

**Open.** Whether the traversal should be bounded by consequence rather than by distance: continuing along a path while the reachable consequence classes remain material and stopping where they do not. That is a more useful bound and it is not computable in advance, since the consequence of a member is known only once it is reached, so it would have to be an iterative deepening with a declared stopping rule. This was not designed and should be.

### 13.7 Repeated structure across the standard

Three structures now appear in more than one part and each was specified independently.

**The frontier.** `Part 3` section 3.11 specifies frontiers for chains of reasoning; section 3.14 here specifies them for lineage graphs. The kinds differ, the concept does not, and both parts treat an undeclared terminus as a defect.

**The immutable record with stateful assertions about it.** `Part 1` separates lifecycle status from derived force state, `Part 2` separates admission from force, `Part 3` gives the record no lifecycle at all, and section 5.1 here separates registration from authority. Four parts, one pattern, four statements of it.

**The bridge against an unverifiable correspondence.** `Part 2` uses worked examples to test a rule's declaration against its statement; section 3.9 here uses classification instances to test a version's extension against its declaration. Both are asymmetric: they disprove and cannot prove.

**Open.** Whether each should be specified once, in `Part 0` or in a shared part, and referenced. The argument for is that four independent specifications of one pattern will drift, and that a reader who has understood it once should not have to learn it again. The argument against is that each instance has different members and different consequences, and a shared abstraction would be thinner than any of the four. Section 12.14 hands the question forward and this part does not answer it.

### 13.8 What this part deliberately did not attempt

No conformance assessment of any system was performed or anticipated, per clause P4-1.13.

No naming convention is specified, per section 10.7, and none is recommended.

No expression of an information model is specified. Whether a logical model is expressed in UML, in a relational notation, in a graph schema or in prose is out of scope, and section 3.11 specifies only that its elements be addressable in a registered path scheme. This is deliberate for the reason ISO/IEC 19763-1 gives for its own silence, and it means this part cannot check anything about a model's internal consistency.

No mechanism compels a component to register a dependency. This part can index what it is given and cannot compel what it is not, and an unpopulated index reduces every impact analysis to a data flow traversal. Section 12.14 hands this to `Part 0` and it is this part's largest dependency on another.

No treatment is given of definitions that cross an organisational boundary. A concept defined by a regulator, a counterparty or an industry body is presently a definition text with a source citation and a source relation, and the question of what happens when the external definition changes is not addressed. Given that `EXTERNAL_OBLIGATION` is the dependency kind this part says matters most, this is a substantive gap.

No treatment is given of multilingual estates beyond the designation and text structures. Whether a concept can be governed by stewards in two languages with equal standing, and what happens when the authoritative language text and a translation diverge in effect, is not addressed.

No performance or scale requirement is stated. The dependency index must span every component, the lineage graph is the largest structure this part specifies, and an impact analysis traverses both. Nothing here is costed, and section 11.24 records a volume concern without a threshold.

**P4-13.2 (MUST) Gaps declared, not filled.** An implementation must not represent a matter listed in section 13.8 as specified by this part.

**P4-13.3 (SHOULD) Open questions carried forward.** A reviewer of this part should record a position on each open question in section 13, and where a position is adopted it should be recorded in the review outcome rather than by silent amendment of the clause it affects.

### 13.9 Questions handed to Part 0 rather than answered here

Each was identified while authoring this part and is recorded so that `Part 0` inherits it rather than rediscovering it.

How the dependency registration obligation of section 3.16 is imposed on components that have no incentive to meet it, given that an unpopulated index makes every impact analysis a data flow traversal.

What a component must do when it holds a meaning this registry refuses to record, since every refusal in section 7.5 is detectable only at recording and none is remediable here.

How a concept supersession propagates: which component compels a dependent to rebind, and what the estate does about the dependents that do not.

Whether the absent, withheld, unknown and not applicable distinctions maintained by `Part 1`, `Part 2` and `Part 3` and declared here as null semantics have one enterprise wide answer or one per representation.

How a unit of work spanning this component and `Part 9` pins one definition version across both, so that a schema and the definition it realises cannot drift within a release.

Whether the frontier concept, the immutable record with stateful assertions pattern, and the asymmetric bridge pattern should each be specified once for the whole standard, per section 13.7.

Which component holds authority over actor identity, since four parts now treat it as opaque and this one requires a steward who can be asked what a concept means.

Whether the retention obligations now committed by four parts, each requiring its records to outlive something another part holds, are jointly satisfiable, since this part's clause P4-8.34 requires a definition to outlive a `Part 3` determination, `Part 3` clause P3-8.31 requires rule artifacts to outlive verdicts, and `Part 1` section 13.2 records the erasure tension unresolved.
