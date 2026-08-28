# KAIROS STD 003 Part 1: Controlled Documents and Records

**Standard.** KAIROS STD 003, the enterprise architecture standard.
**Part.** Part 1 of 14 (Part 0 and Parts 1 through 13). Cited as `KAIROS STD 003 Part 1`.
**Title.** Controlled documents and records.
**Version.** 1.0.0.
**Status.** Proposed. This part has not been approved and is not effective. It is issued for review against the authoring brief of 2026-08-17.
**Date of issue.** 2026-08-17.
**Supersedes.** Nothing. This is the first version.

## Binding of requirement language

The key words MUST, MUST NOT, SHOULD, SHOULD NOT and MAY in this part are to be interpreted as described in RFC 2119 and RFC 8174, and only in the upper case forms. This part does not use SHALL, SHALL NOT, REQUIRED, RECOMMENDED, NOT RECOMMENDED or OPTIONAL as requirement keywords, because RFC 2119 treats several of them as synonyms and a specification that mixes synonyms invites the reader to infer a distinction that is not there.

Every requirement in this part is a numbered clause. A clause identifier has the form `P1-S.N`, where `S` is the section number and `N` is the ordinal of the clause within that section. Clause identifiers are permanent. A clause that is later removed has its identifier retired and never reissued. A clause that is later added to a section takes the next unused ordinal in that section, so ordinals are stable but not contiguous over the life of the part.

Text that is not a numbered clause is not binding. Narrative, tables, examples, state diagrams and the discussion of standards are provided to make the clauses intelligible and testable, and where a table carries normative content a clause says so explicitly and names the table.

## Conformance

An implementation conforms to this part if it satisfies every MUST and MUST NOT clause and records, for each SHOULD and SHOULD NOT clause it does not satisfy, the reason. This part does not define conformance levels, profiles or a certification scheme, and it does not define the method of assessment. Assessment method is the subject of `KAIROS STD 003 Part 12` and is out of scope here.

Where a clause states that a value is an implementation decision, conformance requires that the implementation declare the value, not that it adopt a particular one. An undeclared implementation decision is a nonconformity.

## Clause index

The index below is generated from the clause text of this document. It lists every clause identifier, its modality and its subject label. The counts that follow the index are derived by the same extraction and are stated with the grain at which they were counted.

| Clause | Modality | Subject |
| --- | --- | --- |
| **Section 1** | | **Scope and responsibilities** |
| `P1-1.1` | MUST | Purpose satisfaction |
| `P1-1.2` | MUST NOT | No content semantics |
| `P1-1.3` | MUST | Storage neutrality |
| `P1-1.4` | MUST NOT | No update in place |
| `P1-1.5` | MUST | Projection reads |
| `P1-1.6` | MUST | Survivability of the record |
| `P1-1.7` | MUST NOT | No absorption of neighbouring responsibilities |
| `P1-1.8` | SHOULD | Declared exclusions |
| `P1-1.9` | MUST | Applicability to both document kinds |
| `P1-1.10` | MUST NOT | No conformance self assertion |
| `P1-1.11` | MAY | Additional governed object kinds |
| `P1-1.12` | MUST | Time horizon declaration |
| **Section 2** | | **Terminology** |
| `P1-2.1` | MUST | Single meaning per term |
| `P1-2.2` | MUST NOT | No redefinition |
| `P1-2.3` | MUST | Declared divergence |
| `P1-2.4` | MUST NOT | No collapsing of the two kinds |
| `P1-2.5` | MUST NOT | No collapsing of the three clocks |
| `P1-2.6` | SHOULD | Term registry |
| **Section 3** | | **Data model** |
| `P1-3.1` | MUST | Type conformance |
| `P1-3.2` | MUST | Declared absence semantics |
| `P1-3.3` | SHOULD | Identifier scheme |
| `P1-3.4` | MUST NOT | No meaning in identifiers |
| `P1-3.5` | MUST NOT | No identifier reuse |
| `P1-3.6` | MUST | Timestamp discipline |
| `P1-3.7` | MUST | Occurrence time bound |
| `P1-3.8` | SHOULD NOT | No clock in the content path |
| `P1-3.9` | MUST | Two relation kinds only |
| `P1-3.10` | MUST NOT | No mutation |
| `P1-3.11` | MUST | Retraction as the sole correction mechanism |
| `P1-3.12` | MUST | Retraction attribution |
| `P1-3.13` | MUST NOT | No retraction of fact rows |
| `P1-3.14` | MUST NOT | No retraction of a retraction |
| `P1-3.15` | MUST | Physical deletion only under disposition |
| `P1-3.16` | MUST | Stream and sequence |
| `P1-3.17` | SHOULD | Lineage as stream |
| `P1-3.18` | MUST | Entity coverage |
| `P1-3.19` | MUST NOT | No entity fusion |
| `P1-3.20` | MUST | Lineage before version |
| `P1-3.21` | MUST | Kind immutability |
| `P1-3.22` | MUST | Scope declaration at lineage level |
| `P1-3.23` | MUST | Authoritative language |
| `P1-3.24` | MUST | Version immutability |
| `P1-3.25` | MUST | Ordinal monotonicity |
| `P1-3.26` | MUST NOT | No semantics in the version label |
| `P1-3.27` | MUST | Label uniqueness |
| `P1-3.28` | SHOULD | Change significance |
| `P1-3.29` | MUST NOT | No implicit effectivity from creation |
| `P1-3.30` | MUST | Exactly one authoritative rendition |
| `P1-3.31` | MUST NOT | Renditions are not versions |
| `P1-3.32` | MUST | Translation subordination |
| `P1-3.33` | MUST | Translation divergence signal |
| `P1-3.34` | MUST | Digest per rendition |
| `P1-3.35` | SHOULD NOT | No presentation only authority |
| `P1-3.36` | MUST | Status as projection |
| `P1-3.37` | MUST | From status agreement |
| `P1-3.38` | MUST | Legality check |
| `P1-3.39` | MUST NOT | No silent status change |
| `P1-3.40` | MUST | Retraction of a status transition |
| `P1-3.41` | MUST | Half open intervals |
| `P1-3.42` | MUST | Interval validity |
| `P1-3.43` | MUST | Approval basis |
| `P1-3.44` | MUST | Uniqueness of being in force |
| `P1-3.45` | MUST | Overlap rejection at write time |
| `P1-3.46` | MUST | Overlap detection at read time |
| `P1-3.47` | MUST NOT | No arbitration of ambiguity |
| `P1-3.48` | MUST | Gaps are permitted and are not defects |
| `P1-3.49` | MUST | Retroactive assertion is permitted and flagged |
| `P1-3.50` | MUST | Future assertion is permitted |
| `P1-3.51` | MUST NOT | No effectivity without version |
| `P1-3.52` | MUST | Closing by successor |
| `P1-3.53` | MUST | Scope independence |
| `P1-3.54` | MUST NOT | No scope inheritance |
| `P1-3.55` | MUST | Signature binds a digest |
| `P1-3.56` | MUST | Signature meaning |
| `P1-3.57` | MUST | Signer is a natural person |
| `P1-3.58` | MUST | Agent acts are not signatures |
| `P1-3.59` | MUST | Two factors for non biometric methods |
| `P1-3.60` | MUST | Manifestation |
| `P1-3.61` | MUST NOT | No credential sharing |
| `P1-3.62` | MUST | Delegated approval names both |
| `P1-3.63` | MUST | Approval does not confer effectivity |
| `P1-3.64` | MUST | Approval binds to a version digest |
| `P1-3.65` | SHOULD | Trusted time stamp |
| `P1-3.66` | MUST | Record immutability |
| `P1-3.67` | MUST NOT | No record versions |
| `P1-3.68` | MUST | Correction by further record |
| `P1-3.69` | MUST | Both records remain readable |
| `P1-3.70` | MUST | Declaration is irreversible |
| `P1-3.71` | MUST | Capture completeness |
| `P1-3.72` | MUST | Migration preserves the original digest |
| `P1-3.73` | MUST | Migration is not correction |
| `P1-3.74` | MUST | Aggregation membership is an assertion |
| `P1-3.75` | MUST NOT | No orphan records |
| `P1-3.76` | MAY | Multiple memberships |
| `P1-3.77` | MUST | Metadata history |
| `P1-3.78` | MUST | Core set completeness for effectivity |
| `P1-3.79` | MUST NOT | No empty as absent |
| `P1-3.80` | MUST | Inference marking |
| `P1-3.81` | MUST | Classification assignment is an assertion |
| `P1-3.82` | MUST NOT | No scheme ownership |
| `P1-3.83` | MUST | Scheme version pinning |
| `P1-3.84` | SHOULD | Findability |
| `P1-3.85` | MUST | Holds are orthogonal to status |
| `P1-3.86` | MUST | Holds accumulate |
| `P1-3.87` | MUST NOT | No automatic hold expiry |
| `P1-3.88` | MUST | Disposition requires authorisation |
| `P1-3.89` | MUST | Citation count at authorisation |
| `P1-3.90` | MUST | Tombstone on destruction |
| `P1-3.91` | MUST NOT | No silent absence after disposition |
| `P1-3.92` | MUST | Retention precedence |
| `P1-3.93` | MUST | Audit survives the subject |
| `P1-3.94` | SHOULD NOT | No cryptographic erasure as disposition |
| `P1-3.95` | MUST | Rules are controlled documents |
| `P1-3.96` | MUST | Mode is explicit |
| `P1-3.97` | MUST | Pinned citations carry a digest |
| `P1-3.98` | MUST | As of citations carry both times |
| `P1-3.99` | MUST | Default knowledge time |
| `P1-3.100` | MUST | Resolution is recorded |
| `P1-3.101` | MUST | Divergence detection |
| `P1-3.102` | MUST NOT | No overwriting of a resolution |
| `P1-3.103` | MUST | Locator scheme is named |
| `P1-3.104` | MUST | Clause identifier stability |
| `P1-3.105` | MUST NOT | No renumbering |
| `P1-3.106` | MUST | Retired locators resolve to a statement |
| `P1-3.107` | SHOULD | Redundant locators |
| `P1-3.108` | MUST | Determinism |
| `P1-3.109` | MUST | Rebuildability |
| `P1-3.110` | MUST | Knowledge time parameter |
| `P1-3.111` | MUST NOT | No writes through projections |
| `P1-3.112` | MUST | Staleness disclosure |
| `P1-3.113` | MUST | The belief history projection |
| `P1-3.114` | MUST | Canonical form declared |
| `P1-3.115` | MUST NOT | No default profile |
| `P1-3.116` | MUST | Digest over canonical octets |
| `P1-3.117` | MUST | Original digest retained |
| `P1-3.118` | MUST | Algorithm agility |
| `P1-3.119` | MUST | Fixity outcome discrimination |
| `P1-3.120` | MUST | Mismatch is a defect signal |
| `P1-3.121` | SHOULD | Scheduled fixity checking |
| `P1-3.122` | SHOULD | Evidence records for long horizons |
| `P1-3.123` | SHOULD | Profile implementation is archived |
| `P1-3.124` | MUST | Distribution record for controlled copies |
| `P1-3.125` | MUST | Recall obligation on ceasing to be in force |
| `P1-3.126` | MUST | Uncontrolled copies are marked |
| `P1-3.127` | MUST NOT | No unmarked export |
| `P1-3.128` | SHOULD | Acknowledgement |
| `P1-3.129` | MUST | Review period is asserted |
| `P1-3.130` | MUST NOT | No lapse by silence |
| `P1-3.131` | MUST | Overdue is visible |
| `P1-3.132` | MAY | Configured lapse |
| `P1-3.133` | MUST | Confirmation is an act |
| `P1-3.134` | MUST | Belief and fact both answerable |
| `P1-3.135` | MUST | Prior resolutions are immutable |
| `P1-3.136` | MUST | Divergence is reported to the citing entity |
| **Section 4** | | **Interfaces** |
| `P1-4.1` | MUST | Operation atomicity |
| `P1-4.2` | MUST | Explicit actor on every operation |
| `P1-4.3` | MUST | Idempotency key |
| `P1-4.4` | MUST | Declared deduplication window |
| `P1-4.5` | MUST | Expected sequence on concurrent writes |
| `P1-4.6` | MUST NOT | No partial success reporting |
| `P1-4.7` | MUST | Operation coverage |
| `P1-4.8` | MUST NOT | No compound approval |
| `P1-4.9` | MUST | Precondition failure is a named outcome |
| `P1-4.10` | MUST | Reason on every retraction and withdrawal |
| `P1-4.11` | MAY | Compound convenience operations |
| `P1-4.12` | MUST | Purpose on content fetch |
| `P1-4.13` | MUST | Projection identification |
| `P1-4.14` | MUST | Evidence package verification without the component |
| `P1-4.15` | MUST NOT | No unbounded read |
| `P1-4.16` | MUST | Read your writes within a stream |
| `P1-4.17` | MUST NOT | No cross stream ordering promise |
| `P1-4.18` | MUST | Stability of resolved results |
| `P1-4.19` | MUST | Disclosure of the write on resolve |
| `P1-4.20` | MAY | Non recording preview |
| `P1-4.21` | MUST | No caller inference of absence |
| `P1-4.22` | MUST | No assignment against an unresolvable scheme |
| `P1-4.23` | MUST NOT | No local copy as authority |
| `P1-4.24` | MUST | Degrade to refusal, not to assumption |
| `P1-4.25` | MUST | Recording operations are synchronous in effect |
| `P1-4.26` | MAY | Asynchronous projection materialisation |
| `P1-4.27` | MUST | Long running operations are decomposed |
| `P1-4.28` | MUST | Event envelope |
| `P1-4.29` | MUST | Event set coverage |
| `P1-4.30` | MUST | Events are derived, not authoritative |
| `P1-4.31` | MUST | Divergence event |
| `P1-4.32` | SHOULD | Scheduled re resolution |
| `P1-4.33` | MUST NOT | No event without a row |
| **Section 5** | | **State model** |
| `P1-5.1` | MUST | Two models |
| `P1-5.2` | MUST NOT | No single status field |
| `P1-5.3` | MUST NOT | No time driven lifecycle transitions |
| `P1-5.4` | MUST | Transition legality |
| `P1-5.5` | MUST | Signature and justification requirements |
| `P1-5.6` | MUST | Preconditions enforced at write |
| `P1-5.7` | MUST | Void requires prior retraction |
| `P1-5.8` | MUST NOT | No content in a void version |
| `P1-5.9` | MUST | Reinstatement records a new assertion |
| `P1-5.10` | MUST | Force state values |
| `P1-5.11` | MUST | Force state is parameterised |
| `P1-5.12` | MUST NOT | No collapse of never and no longer |
| `P1-5.13` | MUST | Indeterminate is reported, not resolved |
| `P1-5.14` | MAY | Effectivity by correction without release |
| `P1-5.15` | MUST | Obsolescence is terminal |
| `P1-5.16` | MUST | Obsolescence does not dispose |
| `P1-5.17` | MUST | Obsolescence and withdrawal are distinct |
| `P1-5.18` | MUST | Capture window is bounded |
| `P1-5.19` | MUST | Void of a record is exceptional |
| `P1-5.20` | MUST | Transfer records the receiving party |
| `P1-5.21` | MUST NOT | No return from destroyed |
| `P1-5.22` | MUST | Copy outcome recorded |
| `P1-5.23` | MUST NOT | Holds are not states |
| `P1-5.24` | MUST | Hold does not gate review |
| **Section 6** | | **Execution semantics** |
| `P1-6.1` | MUST | Deterministic resolution |
| `P1-6.2` | MUST NOT | No dependence on wall clock in parameterised evaluation |
| `P1-6.3` | MUST | Deterministic ordering of equal timestamps |
| `P1-6.4` | MUST | Declared collation |
| `P1-6.5` | MUST | Resolution algorithm |
| `P1-6.6` | MUST | Basis returned |
| `P1-6.7` | MUST | Distinguish the two empty cases |
| `P1-6.8` | MUST | Voided version still resolves |
| `P1-6.9` | MUST NOT | No nearest neighbour resolution |
| `P1-6.10` | MUST | Knowledge time bounds retractions as well as assertions |
| `P1-6.11` | MUST | Pinned resolution algorithm |
| `P1-6.12` | MUST | Two distinct digest failures |
| `P1-6.13` | MUST NOT | No effectivity in pinned resolution |
| `P1-6.14` | SHOULD | Force state as advice on pinned resolution |
| `P1-6.15` | MUST | Locator resolution algorithm |
| `P1-6.16` | MUST | Retired is not unresolvable |
| `P1-6.17` | MUST NOT | No partial match |
| `P1-6.18` | MUST | Idempotent recording |
| `P1-6.19` | MUST | Idempotency keys are scoped to the operation and the subject |
| `P1-6.20` | MUST | Optimistic concurrency on the stream |
| `P1-6.21` | MUST NOT | No last writer wins |
| `P1-6.22` | MUST | Retraction under concurrency |
| `P1-6.23` | MUST | Repeated invocation without a key is not idempotent |
| `P1-6.24` | SHOULD | Natural key constraints |
| `P1-6.25` | MUST | Knowledge time is assigned, never accepted |
| `P1-6.26` | MUST | Occurrence time is accepted, never assigned |
| `P1-6.27` | MUST | Late arrival is representable |
| `P1-6.28` | MUST | Declared late arrival limit |
| `P1-6.29` | MUST | Monotonic sequence |
| `P1-6.30` | MUST NOT | No renumbering of sequences |
| `P1-6.31` | MUST | UTC and offsets |
| `P1-6.32` | SHOULD | Declared leap second handling |
| `P1-6.33` | MUST | Declared gating order |
| `P1-6.34` | MUST | Invariant preservation is evaluated last |
| `P1-6.35` | MUST | Disposition gating order |
| **Section 7** | | **Outcome and failure taxonomy** |
| `P1-7.1` | MUST | Every outcome is classified |
| `P1-7.2` | MUST NOT | No non result as failure |
| `P1-7.3` | MUST NOT | No fault as non result |
| `P1-7.4` | MUST | Defect is recorded and raised |
| `P1-7.5` | MUST NOT | No repair on read |
| `P1-7.6` | MUST | Envelope on every outcome |
| `P1-7.7` | MUST | Parameters echoed |
| `P1-7.8` | SHOULD | Problem details carrier |
| `P1-7.9` | MUST | Outcome completeness |
| `P1-7.10` | MUST NOT | No collapsing of the four empty outcomes |
| `P1-7.11` | MUST NOT | No withheld as absent |
| `P1-7.12` | MUST | Existence non disclosure is explicit and configured |
| `P1-7.13` | MUST | Ambiguity halts |
| `P1-7.14` | MUST | Locator outcome independence |
| `P1-7.15` | MUST NOT | No silent substitution on move |
| `P1-7.16` | MUST | Locator outcomes name the version |
| `P1-7.17` | MUST | Refusal is not fault |
| `P1-7.18` | MUST | Determinate non resolution against dependency failure |
| `P1-7.19` | MUST | Named invariant on refusal |
| `P1-7.20` | MUST NOT | No silent no operation |
| `P1-7.21` | MUST | Three integrity outcomes distinguished |
| `P1-7.22` | MUST NOT | No content with a failed integrity outcome |
| `P1-7.23` | MAY | Content with an indeterminate outcome |
| `P1-7.24` | MUST | Disposed against transient |
| `P1-7.25` | MUST | Recording of resolution outcomes |
| `P1-7.26` | MUST | Recording of defects and withholdings |
| `P1-7.27` | MUST | Recording of refusals that alter no state |
| `P1-7.28` | MAY | Faults recorded outside the ledger |
| `P1-7.29` | MUST NOT | No outcome invention |
| `P1-7.30` | MUST | Stability of outcome codes |
| **Section 8** | | **Observability and the audit record** |
| `P1-8.1` | MUST | Rows are audit entries |
| `P1-8.2` | MUST NOT | No separate mutable audit table |
| `P1-8.3` | MUST NOT | No obscuring of prior values |
| `P1-8.4` | MUST | Audit trail cannot be disabled |
| `P1-8.5` | MUST | Independence from the actor |
| `P1-8.6` | MUST | Access recording for determinations |
| `P1-8.7` | SHOULD | Access recording for all reads |
| `P1-8.8` | MUST | Withholding is recorded even when not disclosed |
| `P1-8.9` | MUST | Configuration is part of the record |
| `P1-8.10` | MUST | Rebuild is recorded |
| `P1-8.11` | MUST | One row per act |
| `P1-8.12` | MUST NOT | No batching that loses attribution |
| `P1-8.13` | MUST | Causation chain |
| `P1-8.14` | MUST | Correlation across a unit of work |
| `P1-8.15` | SHOULD NOT | No sampling of the record |
| `P1-8.16` | MUST | Delivered digest |
| `P1-8.17` | MUST | Authorisation reference on every access |
| `P1-8.18` | MUST | Signal on each condition |
| `P1-8.19` | MUST | Signals are addressed to an actor |
| `P1-8.20` | MUST NOT | No signal in place of an outcome |
| `P1-8.21` | MUST | Signals are recorded |
| `P1-8.22` | MUST | Package contents |
| `P1-8.23` | MUST | Retracted assertions included |
| `P1-8.24` | MUST | Scheme snapshots included |
| `P1-8.25` | MUST | Self describing verification |
| `P1-8.26` | MUST | Human readable rendering |
| `P1-8.27` | MUST | Package integrity |
| `P1-8.28` | SHOULD | Signature validation material |
| `P1-8.29` | MUST NOT | No package without provenance |
| `P1-8.30` | MUST | Audit retention at least equals subject retention |
| `P1-8.31` | MUST | Audit survives disposition |
| `P1-8.32` | MUST NOT | No disposition of the audit record alone |
| `P1-8.33` | MUST | Declared audit disposition |
| `P1-8.34` | MUST NOT | No amendment of a written row |
| `P1-8.35` | MUST NOT | No suppression from reads |
| `P1-8.36` | MUST | Chain of the record |
| `P1-8.37` | SHOULD | Independent anchoring |
| **Section 9** | | **Extension model** |
| `P1-9.1` | MUST | Registry as controlled document |
| `P1-9.2` | MUST | Member fields |
| `P1-9.3` | MUST | Member status set |
| `P1-9.4` | MUST NOT | No key reuse |
| `P1-9.5` | MUST NOT | No silent redefinition |
| `P1-9.6` | MUST | Admission does not change existing members |
| `P1-9.7` | MUST | Recorded member reference |
| `P1-9.8` | MUST | Deprecation is not removal |
| `P1-9.9` | MUST | Profile names an external specification or states that it is local |
| `P1-9.10` | MUST NOT | No profile change under the same key |
| `P1-9.11` | MUST | Scheme states its resolution procedure |
| `P1-9.12` | SHOULD | Position schemes are paired |
| `P1-9.13` | MUST | Element definition fields |
| `P1-9.14` | MUST NOT | No shadowing of the core set |
| `P1-9.15` | MUST | Deprecated algorithms are readable and unusable |
| `P1-9.16` | MUST | Migration on deprecation |
| `P1-9.17` | MUST NOT | No removal on deprecation |
| `P1-9.18` | MUST | Reason text with `OTHER` |
| `P1-9.19` | MUST | Method states its factor count and evidence |
| `P1-9.20` | MUST | Method states its long term validation basis |
| `P1-9.21` | MUST | Compilation manifest is content |
| `P1-9.22` | MUST | Compilation members are pinned |
| `P1-9.23` | MUST NOT | No implicit compilation update |
| `P1-9.24` | MUST | Member drift is reported |
| `P1-9.25` | MUST NOT | No compilation as aggregation |
| `P1-9.26` | MUST | Nested compilation depth is declared |
| `P1-9.27` | MUST | Event type states its digest effect |
| `P1-9.28` | MUST | External trigger is recorded, not inferred |
| `P1-9.29` | MUST NOT | No computation of a trigger from absence |
| `P1-9.30` | MUST | Hold reason does not reveal itself where it must not |
| `P1-9.31` | MUST | Event type states its row |
| `P1-9.32` | MUST | New codes carry a class |
| `P1-9.33` | MUST NOT | No code that means two things |
| `P1-9.34` | MUST | Purpose is asserted by the caller |
| **Section 10** | | **Standards and specifications** |
| `P1-10.1` | MUST | Currency of cited standards |
| `P1-10.2` | MUST NOT | No inference of conformance from vocabulary |
| `P1-10.3` | MUST NOT | No citation of the cancelled standard as current |
| `P1-10.4` | MUST | OAIS edition |
| `P1-10.5` | MUST | Edition qualified citation of clause 7.5 |
| `P1-10.6` | MUST NOT | No adoption of the single term |
| `P1-10.7` | MUST | Practice citations marked |
| `P1-10.8` | SHOULD | Audit trail expectations tracked |
| `P1-10.9` | MUST | Named specification for each profile and algorithm |
| `P1-10.10` | MUST | Local origin declared |
| **Section 11** | | **Anti patterns** |
| `P1-11.1` | MUST NOT | No history beside a mutable row |
| `P1-11.2` | MUST NOT | No lineage only citation |
| `P1-11.3` | MUST NOT | No effectivity derived from approval |
| `P1-11.4` | MUST NOT | No fused status |
| `P1-11.5` | MUST NOT | No positional clause identity |
| `P1-11.6` | MUST NOT | No shared entity for the two kinds |
| `P1-11.7` | MUST NOT | No single timestamp |
| `P1-11.8` | MUST NOT | No digest without a declared profile |
| `P1-11.9` | MUST NOT | No boolean fixity |
| `P1-11.10` | MUST NOT | No disableable record |
| `P1-11.11` | MUST NOT | No destruction without a tombstone |
| `P1-11.12` | MUST NOT | No independent translation effectivity |
| `P1-11.13` | MUST NOT | No metadata overwrite |
| `P1-11.14` | MUST NOT | No conflation of withheld and absent |
| `P1-11.15` | MUST NOT | No process owned identity |
| `P1-11.16` | MUST NOT | No uncontrolled register |
| `P1-11.17` | MUST NOT | No unmarked and unrecorded copy |
| `P1-11.18` | MUST NOT | No unbound signature |
| `P1-11.19` | MUST NOT | No hold as status |
| `P1-11.20` | MUST NOT | No present only projection set |
| `P1-11.21` | MUST NOT | No parsed label |
| `P1-11.22` | MUST NOT | No reuse |
| `P1-11.23` | MUST NOT | No unpinned compilation |
| **Section 12** | | **Boundaries with other parts** |
| `P1-12.1` | MUST | Declared allocation |
| `P1-12.2` | MUST | Refusal rather than substitution |
| `P1-12.3` | MUST NOT | No reaching past a neighbour |
| `P1-12.4` | MUST | Rules as resolvable documents |
| `P1-12.5` | MUST NOT | No embedded evaluation |
| `P1-12.6` | MUST | Resolution outcome is the citable artifact |
| `P1-12.7` | MUST NOT | No provenance of other subjects |
| `P1-12.8` | MUST | Published definitions are marked as renditions |
| `P1-12.9` | MUST NOT | No definition versioning |
| `P1-12.10` | MUST NOT | No selection among candidates |
| `P1-12.11` | MUST | Status independent of process |
| `P1-12.12` | MUST NOT | No process identity in the document model |
| `P1-12.13` | MUST | Attributes supplied, decisions consumed |
| `P1-12.14` | MUST NOT | No local policy evaluation |
| `P1-12.15` | MUST | Approval independent of task |
| `P1-12.16` | MUST | Schema reference recorded, not evaluated |
| `P1-12.17` | MUST | Unverified claims marked |
| `P1-12.18` | MUST | Scheme version recorded with every assignment |
| `P1-12.19` | MUST | Scheme snapshot in the package |
| `P1-12.20` | MUST | Digest is the interface |
| `P1-12.21` | MUST NOT | No lifecycle in the store |
| `P1-12.22` | MUST | Disposition passes through |
| `P1-12.23` | MUST | Read only assessment |
| `P1-12.24` | MUST | Assessed version recorded |
| `P1-12.25` | MUST | Agent authorship recorded as such |
| `P1-12.26` | MUST NOT | No agent signature |
| `P1-12.27` | MUST | Unchecked content marked |
| `P1-12.28` | MUST | Authority declared, not assumed |
| `P1-12.29` | MUST | Non result propagation is a composition concern |
| **Section 13** | | **What could not be established** |
| `P1-13.1` | MUST | Verification before approval |
| `P1-13.2` | MUST | Practice basis recorded |
| `P1-13.3` | MUST | Gaps declared, not filled |
| `P1-13.4` | SHOULD | Open questions carried forward |

### Derived counts

Every figure below is derived by extraction from the clause text of this document and not asserted independently. The grain of counting is stated for each figure. A clause is one line of the document matching the clause heading form given under Binding of requirement language, that is, an identifier of the form `P1-S.N`, a modality in parentheses, and a subject label. Narrative sentences containing a requirement keyword are not clauses and are not counted; per that same section they are not binding.

**Total clauses.** 413. Grain: one clause heading.

**By modality.** Grain: one clause heading, counted once against its single declared modality.

| Modality | Clauses | Share |
| --- | --- | --- |
| MUST | 265 | 64.2% |
| MUST NOT | 112 | 27.1% |
| SHOULD | 23 | 5.6% |
| SHOULD NOT | 4 | 1.0% |
| MAY | 9 | 2.2% |
| **All** | **413** | **100.0%** |

**Absolute requirements.** 377 clauses carry MUST or MUST NOT and are therefore conditions of conformance. 27 carry SHOULD or SHOULD NOT and require a recorded reason where not satisfied. 9 carry MAY and constrain nothing. Grain: one clause heading. These three figures sum to the total.

**By section.** Grain: one clause heading, attributed to the numbered section in which its heading appears.

| Section | Title | Clauses | MUST | MUST NOT | SHOULD | SHOULD NOT | MAY |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Scope and responsibilities | 12 | 6 | 4 | 1 | 0 | 1 |
| 2 | Terminology | 6 | 2 | 3 | 1 | 0 | 0 |
| 3 | Data model | 136 | 95 | 26 | 10 | 3 | 2 |
| 4 | Interfaces | 33 | 23 | 6 | 1 | 0 | 3 |
| 5 | State model | 24 | 17 | 6 | 0 | 0 | 1 |
| 6 | Execution semantics | 35 | 26 | 6 | 3 | 0 | 0 |
| 7 | Outcome and failure taxonomy | 30 | 18 | 9 | 1 | 0 | 2 |
| 8 | Observability and the audit record | 37 | 25 | 8 | 3 | 1 | 0 |
| 9 | Extension model | 34 | 24 | 9 | 1 | 0 | 0 |
| 10 | Standards and specifications | 10 | 6 | 3 | 1 | 0 | 0 |
| 11 | Anti patterns | 23 | 0 | 23 | 0 | 0 | 0 |
| 12 | Boundaries with other parts | 29 | 20 | 9 | 0 | 0 | 0 |
| 13 | What could not be established | 4 | 3 | 0 | 1 | 0 | 0 |
| **All** | | **413** | **265** | **112** | **23** | **4** | **9** |

**Ordinal integrity.** In this version, the highest ordinal in each section equals the number of clauses in that section, so no identifier has yet been retired. This will cease to be true at the first clause removal, and the count rather than the highest ordinal is then the figure to rely on.

## 1. Scope and responsibilities

### 1.1 What this component is

This part specifies a component that governs the identity, integrity, status and citability of the documents and records of an organisation over the whole period for which they must remain answerable, including periods after the systems that produced them have been decommissioned.

The component exists to answer one question reliably: **which version of which document was in force at the moment a given act was performed, and can that version still be produced and shown to be unaltered.** Every other responsibility in this part is subordinate to that question. A component that manages documents beautifully but cannot answer that question has failed at its purpose.

The component is accountable for the following.

Identity and addressing of documents, of their versions, and of positions within a version.

Version lineage: the relation between successive versions of the same document and the derivation relation between a version and the version it was drawn from.

The status lifecycle of a version, including the separation of approval from entry into force.

Effectivity: the interval of application time during which a version governs, and the scope within which it governs.

Supersession, withdrawal and obsolescence, and the difference between them.

Point in time citation resolution, in both of its senses: what was in force then, and what was believed then to be in force then.

Integrity: canonical form, content digests, digest algorithm agility, and the classification of integrity failures.

Records as distinct from documents: the declaration of a record, its immutability, its renditions and its preservation events.

Retention, disposition, holds, and the treatment of content that is cited by something still retained.

Approval and electronic signature, and the attribution of an approval to a person.

Review cycles and the consequences of a review date passing.

Descriptive and administrative metadata, classification assignment, and the history of both.

Controlled distribution: issued copies, their recipients, their recall, and the marking of uncontrolled copies.

The audit record of every one of the above, at a grain sufficient to reconstruct any determination.

### 1.2 What this component is not

The boundary matters more than the capability list, because each item below is something a document management component absorbs if nobody stops it, and each absorption destroys a property that some other component was supposed to guarantee.

The component is not an authoring or editing environment. It does not specify how content is composed, rendered, compared or collaboratively edited. It receives content that is already whole.

The component is not a content interpreter. It does not parse, validate or understand the meaning of the content it governs, beyond computing a digest over a declared canonical form. Structural validation of content against a schema belongs to `Part 9`.

The component is not the store of record for content octets. It owns the mapping from a version to a content digest. Whether it also holds the octets is a deployment decision. Immutable content addressed storage belongs to `Part 11`.

The component is not a rules engine. It holds retention rules, review periods and effectivity as declared data, and it does not evaluate rule expressions. Evaluation belongs to `Part 2`.

The component is not a decision engine. Approval, withdrawal and disposition authorisation are acts it records, not choices it makes. Selection among outcomes belongs to `Part 5`.

The component is not a workflow engine. Routing a draft for review, chasing an approver and escalating an overdue review are orchestration, and belong to `Part 6`. The component records the outcomes of those activities and must remain correct if the orchestrator is replaced.

The component is not a policy decision point. It supplies classification, marking and distribution facts as attributes for an authorisation decision and records the reference to the decision. Policy evaluation belongs to `Part 7`.

The component is not a task manager. An approver's queue belongs to `Part 8`.

The component is not the provenance ledger of the enterprise. It emits its own events and holds its own audit record. The chain of reasoning behind a determination, which may cite documents among many other things, belongs to `Part 3`.

The component is not the repository of governed definitions. A data element definition, a model or a code list is a definition first and a document only when someone publishes a rendition of it. Definitions belong to `Part 4`, vocabularies and reference sets to `Part 10`.

The component is not an identity provider. Actors are opaque references resolvable elsewhere.

The component is not a search relevance engine. It must make documents findable by their governed metadata; ranking, similarity and full text retrieval quality are out of scope.

**P1-1.1 (MUST) Purpose satisfaction.** An implementation must be able to answer, for any document lineage and any pair of application time and knowledge time within its retained history, which version was in force, or that none was, or that the question is ambiguous, and must do so by the mechanism specified in section 6.

**P1-1.2 (MUST NOT) No content semantics.** An implementation must not make the status, effectivity, retention or integrity outcome of a document depend on the meaning of its content.

**P1-1.3 (MUST) Storage neutrality.** An implementation must satisfy the data model of section 3 without requiring any storage technology other than a store capable of inserting rows and reading them back in a defined order.

**P1-1.4 (MUST NOT) No update in place.** An implementation must not represent any state change specified by this part as a modification or deletion of a previously written row, tuple, object or event.

**P1-1.5 (MUST) Projection reads.** An implementation must expose current state only through projections that are pure functions of the recorded facts, as specified in section 3.14.

**P1-1.6 (MUST) Survivability of the record.** The evidence package specified in section 8.6 must be sufficient to answer the purpose question of section 1.1 for any retained document, without the implementation running and without access to any component of this standard other than the package itself.

**P1-1.7 (MUST NOT) No absorption of neighbouring responsibilities.** An implementation must not evaluate rule expressions, select among candidate outcomes, orchestrate activities, decide authorisation, or version schemas or definitions, as those responsibilities are allocated in section 12.

**P1-1.8 (SHOULD) Declared exclusions.** An implementation should publish, as a controlled document under this part, the list of section 1.2 exclusions that it in fact provides by other means, so that a reader can tell what the implementation does not guarantee.

**P1-1.9 (MUST) Applicability to both document kinds.** An implementation must apply this part to both documents and records as defined in section 2, and must not implement one kind by treating it as a special case of the other except where a clause of this part says so.

**P1-1.10 (MUST NOT) No conformance self assertion.** An implementation must not assert conformance to this part on the basis of its own internal checks alone, and must not represent such an assertion as an assessment.

**P1-1.11 (MAY) Additional governed object kinds.** An implementation may govern object kinds beyond documents and records under this part, provided every clause of this part that applies to a document applies unchanged to the additional kind, and the kind is registered under section 9.

**P1-1.12 (MUST) Time horizon declaration.** An implementation must declare the period for which it undertakes to answer the purpose question, and must declare it as a duration or an absolute date rather than as an indefinite commitment.

## 2. Terminology

Terms are defined here only if this component owns them. A term owned by another part is cited to that part and is not redefined. Where a term is taken from an external standard, the standard is named. Where this part narrows or diverges from the external definition, the divergence is stated, because a silent narrowing is the mechanism by which two components come to use one word for two things.

Definitions are given in the singular. A definition is not a clause and is not binding on its own; clauses that depend on a definition cite the term.

### 2.1 Terms owned by this part

**Document.** A body of content that is intended to govern, inform or instruct, that is revisable, and that therefore exists as an ordered series of versions. Compare ISO 9001:2015 clause 7.5, which uses "documented information" to span both this term and the next; that standard's single term is not adopted here, because the two objects have different mutability rules and merging them is the anti pattern of section 11.6.

**Record.** Information created, received and maintained as evidence and as an asset by an organisation or person, in pursuance of legal obligations or in the transaction of business, per ISO 15489-1:2016 clause 3.14 as reported in secondary sources. In this part a record is additionally and specifically **not revisable**: it has renditions but no versions, and it is corrected only by a further record that references it.

**Document lineage.** The identity that persists across all versions of one document. The lineage, not the version, is what a title names and what a reader means by "the SOP".

**Version.** One immutable state of a document lineage, with a content digest, produced by an authoring act. A version is never edited after it is created; editing produces a further version.

**Rendition.** One expression of the same version in a different format or encoding, for example a fixed layout rendering of a structured source. A rendition has its own digest and its own canonical form profile, and it is not a version. PREMIS 3.0 uses "Representation" for a related idea; this part uses "rendition" to avoid collision with OAIS Representation Information.

**Translation.** A rendition in a different natural language. A translation is not a version, and is not independently effective; see section 3.6.

**Manifestation set.** The set of renditions of one version, exactly one of which is designated authoritative.

**Effectivity assertion.** A recorded statement that a named version is in force for a named scope over a half open interval of application time. Effectivity is asserted, never inferred from approval.

**Effectivity scope.** The named domain within which an effectivity assertion applies, for example an organisational unit, a jurisdiction or a product. The scope is part of the uniqueness constraint on being in force.

**Application time.** The time dimension in which effectivity is expressed: the period during which a version governs the world. Corresponds to application time period in SQL:2011 and to valid time in the temporal database literature.

**Knowledge time.** The time dimension in which the component's own beliefs are expressed: the moment at which a fact was durably recorded. Corresponds to system versioned time in SQL:2011 and to transaction time in the literature. This part uses "knowledge time" rather than "transaction time" because the operative question is what was known, not what a transaction did.

**Occurrence time.** The time at which the act being recorded happened in the world, as asserted by the actor. Distinct from knowledge time, which the component assigns.

**Retraction.** An appended statement that a previously recorded assertion was wrong and should not be considered as of knowledge times at or after the retraction. A retraction does not remove the retracted assertion and does not make it unreadable.

**Correction.** A retraction paired with a replacement assertion covering the same subject. Correction is the only mechanism by which recorded state changes in this part.

**Supersession.** The condition in which a version ceases to be in force because a successor version of the same lineage takes force in the same scope.

**Withdrawal.** The condition in which a version ceases to be in force with no successor taking force, on the assertion that it is no longer to be relied upon. Withdrawal may be asserted with retroactive application time.

**Obsolescence.** The condition in which a lineage is retired because the activity it governed has ended. Obsolescence applies to a lineage; withdrawal and supersession apply to a version. The literature does not draw this line consistently; see section 13.4.

**Declaration.** The act by which content becomes a record and thereby immutable. The term follows MoReq2010, which treats declaring a record as a distinct service.

**Aggregation.** A grouping of records, possibly nested, used for classification, retention and disposition. The term follows MoReq2010, which replaced the earlier "file" and "folder" hierarchy with an aggregation of unbounded depth.

**Compilation.** A document whose content is a manifest of pinned versions of other documents, for example a dossier or a submission binder. A compilation is a document, not an aggregation, and the distinction is load bearing; see section 9.8.

**Citation.** A recorded reference from a citing entity to a document lineage, optionally to a specific version and optionally to a position within it, carrying the mode by which it is to be resolved.

**Pinned citation.** A citation that names a version identifier and a content digest, and therefore resolves without reference to effectivity.

**As of citation.** A citation that names a lineage, an application time and a knowledge time, and therefore resolves through effectivity assertions.

**Locator.** An expression identifying a position within a version, in a named locator scheme.

**Clause identifier.** A locator in the `CLAUSE_ID` scheme: an identifier assigned to a unit of content at authoring, stable across versions of the lineage, never renumbered and never reused.

**Canonical form profile.** A named, versioned procedure for reducing content to the exact octet sequence over which a digest is computed.

**Content digest.** The output of a named digest algorithm over the canonical octets of a version or rendition, expressed as an algorithm identifier and a value.

**Fixity check.** A recomputation of a content digest and its comparison with the recorded value. Term follows PREMIS 3.0, which treats fixity as a property of an Object and its verification as an Event.

**Tombstone.** The residue of a version or record whose content octets have been destroyed under authorised disposition: identity, digests, metadata, and the disposition authorisation, retained so that later citations resolve to a truthful account rather than to an absence.

**Hold.** A recorded suspension of disposition for a stated reason under a stated authority, orthogonal to lifecycle status.

**Controlled copy.** An issued instance of a version, recorded against a recipient, which the issuer undertakes to recall or replace when the version ceases to be in force.

**Uncontrolled copy.** Any other issued instance, which must carry on its face the information a reader needs to determine whether it is current.

**Evidence package.** A self describing export sufficient to answer the purpose question for its subject without the implementation. Maps to the OAIS Archival Information Package of ISO 14721:2025, and section 8.6 states the mapping.

**Projection.** A read model computed deterministically from recorded facts, holding no state of its own.

### 2.2 Clauses governing terminology

**P1-2.1 (MUST) Single meaning per term.** An implementation must use each term defined in section 2.1 with the meaning given there in all of its interfaces, records, projections and documentation.

**P1-2.2 (MUST NOT) No redefinition.** An implementation must not use a term defined in section 2.1 for a different concept, and must not use a different term for a concept defined in section 2.1 in any interface specified by this part.

**P1-2.3 (MUST) Declared divergence.** Where an implementation is obliged by an external regime to use a term from that regime with a meaning that differs from section 2.1, it must record the mapping between the two as a controlled document under this part.

**P1-2.4 (MUST NOT) No collapsing of the two kinds.** An implementation must not use one term for both a document and a record.

**P1-2.5 (MUST NOT) No collapsing of the three clocks.** An implementation must not use one term or one field for more than one of application time, knowledge time and occurrence time.

**P1-2.6 (SHOULD) Term registry.** An implementation should publish the terms it adds beyond section 2.1, with definitions, as a controlled document under this part.
## 3. Data model

### 3.1 Type vocabulary

Every field in this section carries a type from the table below. The table is normative by clause P1-3.1. Physical representation is an implementation decision; the constraints stated in the table are not.

| Type | Meaning | Constraint |
|---|---|---|
| `ID` | An opaque, globally unique, immutable identifier | Must be generated by a scheme that does not require coordination and does not encode mutable meaning. UUID version 7 per RFC 9562 is the recommended scheme; see clause P1-3.3 |
| `URN` | A resolvable or at least globally unambiguous name | Syntax per RFC 8141 |
| `KTIME` | A knowledge time instant assigned by the component | RFC 3339 date and time, UTC, offset written as `Z`, resolution at least milliseconds |
| `ATIME` | An application time instant | RFC 3339 date and time with explicit offset; may be in the future |
| `OTIME` | An occurrence time instant asserted by an actor | RFC 3339 date and time with explicit offset; may precede the `KTIME` of the row that carries it |
| `SEQ` | A monotonically increasing integer within a named stream | Gapless is not required; monotonic is |
| `DIGEST` | An algorithm identifier and a value | Form `algorithm:hex`, algorithm drawn from the registry of section 9.5 |
| `ENUM<...>` | One value from a named set | The set is either closed by this part or held in a registry named by section 9 |
| `TEXT` | Unicode text | Normalisation form NFC; maximum length is an implementation decision and must be declared |
| `LANG` | A language tag | BCP 47 |
| `MEDIA` | A media type | RFC 6838, with parameters retained as written |
| `ACTOR` | A reference to a person, organisational unit or automated agent | Opaque to this component; resolution is external; must distinguish natural persons from other actor kinds |
| `AUTHREF` | A reference to an authorisation or decision made elsewhere | Opaque; see section 12.7 |
| `INT`, `DECIMAL`, `BOOL` | Ordinary scalars | Precision of `DECIMAL` must be declared |
| `DURATION` | A period of time | ISO 8601-1 duration syntax |
| `SCOPE` | The name of an effectivity scope | Drawn from a reference set governed under `Part 10`; the reserved value `GLOBAL` denotes the whole organisation |

Cardinality is written `1` for exactly one, `0..1` for optional single, `1..*` for one or more, `0..*` for zero or more. Every field table in this section carries a column stating what absence means, and the phrase "absence not permitted" is used where the field is mandatory, so that no reader has to infer the difference between an absent field and a field whose absence is meaningful.

**P1-3.1 (MUST) Type conformance.** Every field an implementation records for an entity specified in this section must conform to the type given for that field in the table for that entity, and to the constraint given in the table of section 3.1 for that type.

**P1-3.2 (MUST) Declared absence semantics.** For every field an implementation adds beyond those specified in this section, it must declare what absence of that field means, in the same three categories used here: absence not permitted, absence means a stated default, absence means not known.

**P1-3.3 (SHOULD) Identifier scheme.** An implementation should generate values of type `ID` using UUID version 7 as specified in RFC 9562, because it is unique without coordination and is monotonic by creation time, which makes it usable as an insertion order key in an append only store.

**P1-3.4 (MUST NOT) No meaning in identifiers.** An implementation must not encode status, version ordinal, classification, effectivity, retention or any other mutable property in the value of an `ID`.

**P1-3.5 (MUST NOT) No identifier reuse.** An implementation must not assign an `ID`, a version label, a clause identifier, a registry member key or a copy number that it has previously assigned to a different subject, at any time, including after the earlier subject has been disposed of.

**P1-3.6 (MUST) Timestamp discipline.** An implementation must record all `KTIME` values from a single clock source per stream, must not record a `KTIME` earlier than the `KTIME` of any row previously written to the same stream, and must record all `KTIME` values in UTC.

**P1-3.7 (MUST) Occurrence time bound.** An implementation must reject a row whose `OTIME` is later than the `KTIME` it would be assigned by more than a declared tolerance, and must declare that tolerance as a `DURATION`.

**P1-3.8 (SHOULD NOT) No clock in the content path.** An implementation should not derive any `KTIME` from a clock controlled by the actor submitting the row.

### 3.2 The append only obligation and its demonstration

The authoring brief requires that this specification be storage neutral and that the data model be satisfiable by an append only relational store in which no row is ever updated, all state change is carried by new rows, and current state is read through a projection. This section states the obligation and demonstrates that the model meets it. The demonstration is completed by the worked example in section 3.18.

The model has exactly two kinds of relation.

**Fact relations** hold rows that assert the existence of an immutable thing: a lineage exists, a version exists with this digest, a record was declared. A fact row is written once and is never contradicted, only annotated.

**Assertion relations** hold rows that assert something that might later be found wrong: this version is in force over this interval, this document is classified thus, this retention rule applies. An assertion row is written once. If it is wrong, a row is appended to the retraction relation naming it, and a replacement assertion is appended. Nothing is modified.

There is no third kind. In particular there is no "current state" relation, because a current state relation is a mutable row by another name.

Three consequences follow, and they are the reason the constraint is worth accepting rather than merely tolerating.

First, knowledge time comes free. Every row carries the `KTIME` at which it was written, and no row is ever removed, so the state of belief at any past moment is recoverable by filtering on `KTIME`. A store that updates rows can only recover past belief if it maintains a separate history, and a separate history can diverge from the data it describes. This is the mechanism behind the anti pattern of section 11.1.

Second, the audit record and the data are the same artifact. There is no possibility of the audit trail disagreeing with the state, because the state is derived from the audit trail rather than recorded beside it.

Third, correction is visible. A retraction is a first class recorded act with an actor, a reason and an authority. In an update in place store, a correction and a falsification are indistinguishable after the fact.

**P1-3.9 (MUST) Two relation kinds only.** Every persisted relation an implementation uses to satisfy this part must be either a fact relation or an assertion relation as described in section 3.2, and an implementation must declare which for each.

**P1-3.10 (MUST NOT) No mutation.** An implementation must not issue an update or a delete against any fact row or assertion row, and must not achieve the effect of one by rewriting, compacting, merging or reloading a store.

**P1-3.11 (MUST) Retraction as the sole correction mechanism.** An implementation must effect every correction to a recorded assertion by appending a retraction row and, where a replacement is intended, a replacement assertion row.

**P1-3.12 (MUST) Retraction attribution.** Every retraction row must carry an actor, an occurrence time, a reason code drawn from the registry of section 9.6, and free text stating why the retracted assertion was wrong.

**P1-3.13 (MUST NOT) No retraction of fact rows.** An implementation must not permit retraction of a fact row. Where a fact row was written in error, the error must be recorded as an annotation assertion against it, and the affected entity must be marked void by a status transition, so that the erroneous fact remains readable and its erroneous status is explicit.

**P1-3.14 (MUST NOT) No retraction of a retraction.** An implementation must not permit a retraction row to be retracted. An erroneous retraction must be corrected by appending a fresh assertion carrying the same content as the wrongly retracted one, with a reason referencing the erroneous retraction.

**P1-3.15 (MUST) Physical deletion only under disposition.** An implementation must not physically remove any row except as the execution of an authorised disposition under section 3.12, and must in that case retain the tombstone required by section 3.12.

**P1-3.16 (MUST) Stream and sequence.** Every fact row and assertion row must carry the identifier of the stream it belongs to and a `SEQ` unique within that stream, and an implementation must declare its stream partitioning.

**P1-3.17 (SHOULD) Lineage as stream.** An implementation should use the document lineage as the stream boundary for all rows concerning that lineage, because the ordering guarantees a caller most often needs are per document, and a global order is more expensive than the model requires.

### 3.3 Entity inventory

| Entity | Kind | Owns | Specified in |
|---|---|---|---|
| Document lineage | Fact | The persistent identity of a document | 3.4 |
| Version | Fact | One immutable authored state and its digest | 3.5 |
| Rendition | Fact | One expression of a version in one format | 3.6 |
| Status transition | Assertion | The lifecycle position of a version | 3.7 |
| Effectivity assertion | Assertion | The interval and scope in which a version is in force | 3.8 |
| Retraction | Fact | That a named assertion is disavowed from a knowledge time | 3.2, 3.8 |
| Approval | Fact | That a named actor approved a named version | 3.9 |
| Signature | Fact | The evidential form of an approval or other signed act | 3.9 |
| Record declaration | Fact | That content became evidence and is now immutable | 3.10 |
| Aggregation | Fact | A grouping of records for classification and retention | 3.10 |
| Aggregation membership | Assertion | That a record belongs to an aggregation | 3.10 |
| Preservation event | Fact | An act performed on a record for preservation purposes | 3.10 |
| Metadata assertion | Assertion | One metadata element value over an interval | 3.11 |
| Classification assignment | Assertion | Placement in a classification scheme | 3.11 |
| Retention application | Assertion | That a retention rule governs a subject | 3.12 |
| Hold | Assertion | A suspension of disposition | 3.12 |
| Disposition authorisation | Fact | Permission to execute a disposition | 3.12 |
| Disposition execution | Fact | That a disposition was carried out | 3.12 |
| Tombstone | Fact | What survives destruction of content | 3.12 |
| Citation | Fact | A reference from a citing entity to a document | 3.13 |
| Citation resolution | Fact | The outcome of resolving a citation at a stated time pair | 3.13 |
| Canonical form profile binding | Fact | Which profile governs the digest of a version or rendition | 3.15 |
| Digest | Fact | One digest of one subject under one algorithm | 3.15 |
| Fixity check | Fact | One recomputation and its outcome | 3.15 |
| Controlled copy issue | Fact | That a copy was issued to a recipient | 3.16 |
| Controlled copy disposition | Fact | That a copy was returned, destroyed or superseded | 3.16 |
| Review period application | Assertion | The review cycle governing a lineage | 3.17 |
| Review outcome | Fact | The result of a periodic review | 3.17 |

**P1-3.18 (MUST) Entity coverage.** An implementation must persist every entity in the inventory of section 3.3, as a distinct relation or as a distinguishable row kind, and must be able to enumerate the rows of each.

**P1-3.19 (MUST NOT) No entity fusion.** An implementation must not represent two entities of the inventory in a single row where doing so prevents one from being written without the other, except where a clause of this section explicitly permits that pair.

### 3.4 Document lineage

| Field | Type | Required | Card | Absence means |
|---|---|---|---|---|
| `lineage_id` | `ID` | yes | 1 | absence not permitted |
| `lineage_urn` | `URN` | yes | 1 | absence not permitted |
| `kind` | `ENUM<DOCUMENT, RECORD, COMPILATION, REGISTRY>` | yes | 1 | absence not permitted |
| `created_ktime` | `KTIME` | yes | 1 | absence not permitted |
| `created_otime` | `OTIME` | no | 0..1 | the creating act is taken to have occurred at `created_ktime` |
| `creator` | `ACTOR` | yes | 1 | absence not permitted |
| `owning_function` | `TEXT` | yes | 1 | absence not permitted |
| `authoritative_language` | `LANG` | yes | 1 | absence not permitted |
| `derived_from_lineage` | `ID` | no | 0..1 | the lineage is original rather than a fork of another lineage |
| `effectivity_scoped` | `BOOL` | yes | 1 | absence not permitted; `false` means all effectivity assertions for this lineage carry scope `GLOBAL` |

**P1-3.20 (MUST) Lineage before version.** An implementation must not accept a version whose lineage does not already exist as a fact row.

**P1-3.21 (MUST) Kind immutability.** An implementation must not permit the `kind` of a lineage to change, and must require a new lineage where the intended kind differs.

**P1-3.22 (MUST) Scope declaration at lineage level.** An implementation must record `effectivity_scoped` at the lineage and must reject an effectivity assertion whose scope is other than `GLOBAL` for a lineage where `effectivity_scoped` is `false`.

**P1-3.23 (MUST) Authoritative language.** An implementation must record exactly one authoritative language per lineage, and must treat every other language expression of a version as a translation under section 3.6.

### 3.5 Version

| Field | Type | Required | Card | Absence means |
|---|---|---|---|---|
| `version_id` | `ID` | yes | 1 | absence not permitted |
| `lineage_id` | `ID` | yes | 1 | absence not permitted |
| `ordinal` | `INT` | yes | 1 | absence not permitted; strictly increasing within the lineage |
| `version_label` | `TEXT` | yes | 1 | absence not permitted |
| `authored_otime` | `OTIME` | yes | 1 | absence not permitted |
| `created_ktime` | `KTIME` | yes | 1 | absence not permitted |
| `authors` | `ACTOR` | yes | 1..* | absence not permitted |
| `derived_from_version` | `ID` | no | 0..1 | the version was authored without a predecessor, which for `ordinal` greater than one must be accompanied by a stated reason |
| `title` | `TEXT` | yes | 1 | absence not permitted |
| `abstract` | `TEXT` | no | 0..1 | not supplied; must not be interpreted as an empty abstract |
| `authoritative_rendition_id` | `ID` | yes | 1 | absence not permitted |
| `change_summary` | `TEXT` | no | 0..1 | not supplied |
| `change_significance` | `ENUM<EDITORIAL, SUBSTANTIVE, UNDECLARED>` | yes | 1 | absence not permitted; `UNDECLARED` must be treated as `SUBSTANTIVE` by any consumer |

**P1-3.24 (MUST) Version immutability.** An implementation must not permit any field of a version fact row to change after the row is written.

**P1-3.25 (MUST) Ordinal monotonicity.** An implementation must assign version ordinals strictly increasing within a lineage and must not reuse an ordinal.

**P1-3.26 (MUST NOT) No semantics in the version label.** An implementation must not require or permit the `version_label` to be parsed in order to determine status, effectivity, approval or significance of change.

**P1-3.27 (MUST) Label uniqueness.** An implementation must reject a `version_label` that is already in use within the same lineage.

**P1-3.28 (SHOULD) Change significance.** An implementation should require the author to declare `change_significance`, and should treat `EDITORIAL` as a claim to be checked at approval rather than as a fact.

**P1-3.29 (MUST NOT) No implicit effectivity from creation.** An implementation must not treat the creation of a version as an assertion that it is in force.

### 3.6 Rendition and manifestation set

| Field | Type | Required | Card | Absence means |
|---|---|---|---|---|
| `rendition_id` | `ID` | yes | 1 | absence not permitted |
| `version_id` | `ID` | yes | 1 | absence not permitted |
| `role` | `ENUM<AUTHORITATIVE, DERIVED, TRANSLATION, PRESENTATION>` | yes | 1 | absence not permitted |
| `media_type` | `MEDIA` | yes | 1 | absence not permitted |
| `language` | `LANG` | yes | 1 | absence not permitted |
| `canonical_profile_id` | `ID` | yes | 1 | absence not permitted |
| `content_locator` | `URN` | no | 0..1 | the octets are held by this component rather than by an external store |
| `octet_length` | `INT` | yes | 1 | absence not permitted |
| `produced_from_rendition` | `ID` | no | 0..1 | the rendition was supplied rather than generated from another rendition |
| `producing_agent` | `ACTOR` | no | 0..1 | the rendition was supplied by the author rather than produced by a tool |

**P1-3.30 (MUST) Exactly one authoritative rendition.** An implementation must require exactly one rendition per version with `role` of `AUTHORITATIVE`, and must reject a second.

**P1-3.31 (MUST NOT) Renditions are not versions.** An implementation must not assign a version ordinal, a version label, an effectivity assertion, an approval or a status transition to a rendition.

**P1-3.32 (MUST) Translation subordination.** An implementation must treat a translation as a rendition of a version and must not permit a translation to be in force independently of the version it renders.

**P1-3.33 (MUST) Translation divergence signal.** Where a translation is produced from a rendition of an earlier version than the version currently in force, an implementation must record that fact and must make it visible to any reader of the translation.

**P1-3.34 (MUST) Digest per rendition.** An implementation must record at least one digest for every rendition, under section 3.15.

**P1-3.35 (SHOULD NOT) No presentation only authority.** An implementation should not designate a fixed layout rendering produced by a tool as the authoritative rendition where a structured source exists, because a rendering cannot be recanonicalised if the rendering tool is lost, which converts a future fixity check into an indeterminate result rather than a pass or a fail.
### 3.7 Status transition

Status is not a field on a version. It is the projection of the ordered sequence of status transition assertions for that version. This is the difference between a model that can answer "what did we think its status was in March 2027" and one that cannot.

| Field | Type | Required | Card | Absence means |
|---|---|---|---|---|
| `transition_id` | `ID` | yes | 1 | absence not permitted |
| `version_id` | `ID` | yes | 1 | absence not permitted |
| `from_status` | `ENUM` per section 5.2 | no | 0..1 | the transition is the initial one and the prior status is the null state |
| `to_status` | `ENUM` per section 5.2 | yes | 1 | absence not permitted |
| `otime` | `OTIME` | yes | 1 | absence not permitted |
| `ktime` | `KTIME` | yes | 1 | absence not permitted |
| `seq` | `SEQ` | yes | 1 | absence not permitted |
| `actor` | `ACTOR` | yes | 1 | absence not permitted |
| `on_behalf_of` | `ACTOR` | no | 0..1 | the actor acted in their own right |
| `authority` | `AUTHREF` | no | 0..1 | the transition required no separate authorisation, which must itself be permitted by section 5.3 for that transition |
| `reason_code` | `ENUM` per section 9.6 | yes | 1 | absence not permitted |
| `reason_text` | `TEXT` | no | 0..1 | not supplied; must be present where section 5.3 marks the transition as requiring justification |
| `signature_id` | `ID` | no | 0..1 | the transition was not signed, which must itself be permitted by section 5.3 for that transition |

**P1-3.36 (MUST) Status as projection.** An implementation must derive the status of a version from its status transition assertions and must not store status as an independently writable field.

**P1-3.37 (MUST) From status agreement.** An implementation must reject a status transition whose `from_status` differs from the status projected for that version at the knowledge time of submission, and must report the conflict as specified in section 7.6.

**P1-3.38 (MUST) Legality check.** An implementation must reject a status transition that is not legal per the transition table of section 5.3.

**P1-3.39 (MUST NOT) No silent status change.** An implementation must not change the projected status of a version other than by a status transition assertion, and specifically must not derive a status change from the passage of time, from the effectivity of another version, or from the expiry of a review period.

**P1-3.40 (MUST) Retraction of a status transition.** Where a status transition was recorded in error, an implementation must effect the correction by retraction and replacement under section 3.2, and must not record a compensating transition in the opposite direction as though the error had been a real act.

### 3.8 Effectivity assertion and retraction

This is the load bearing relation of the part. Everything in section 6 rests on it.

| Field | Type | Required | Card | Absence means |
|---|---|---|---|---|
| `assertion_id` | `ID` | yes | 1 | absence not permitted |
| `lineage_id` | `ID` | yes | 1 | absence not permitted |
| `version_id` | `ID` | yes | 1 | absence not permitted |
| `scope` | `SCOPE` | yes | 1 | absence not permitted; `GLOBAL` is a value and not a default for a missing field |
| `effective_from` | `ATIME` | yes | 1 | absence not permitted |
| `effective_to` | `ATIME` | no | 0..1 | in force until further notice; must not be read as unknown, and must not be read as a defect |
| `asserted_ktime` | `KTIME` | yes | 1 | absence not permitted |
| `asserted_otime` | `OTIME` | yes | 1 | absence not permitted |
| `actor` | `ACTOR` | yes | 1 | absence not permitted |
| `authority` | `AUTHREF` | yes | 1 | absence not permitted |
| `basis` | `ENUM<APPROVAL, SUPERSESSION, WITHDRAWAL, CORRECTION, MIGRATION>` | yes | 1 | absence not permitted |
| `approval_id` | `ID` | no | 0..1 | the assertion does not rest on an approval, permitted only where `basis` is `CORRECTION` or `MIGRATION` |
| `retroactive` | `BOOL` | yes | 1 | absence not permitted; `true` where `effective_from` precedes `asserted_ktime` |

Retraction rows are shared with the general mechanism of section 3.2 and have the following fields.

| Field | Type | Required | Card | Absence means |
|---|---|---|---|---|
| `retraction_id` | `ID` | yes | 1 | absence not permitted |
| `target_assertion_id` | `ID` | yes | 1 | absence not permitted |
| `target_relation` | `TEXT` | yes | 1 | absence not permitted |
| `ktime` | `KTIME` | yes | 1 | absence not permitted |
| `otime` | `OTIME` | yes | 1 | absence not permitted |
| `actor` | `ACTOR` | yes | 1 | absence not permitted |
| `authority` | `AUTHREF` | yes | 1 | absence not permitted |
| `reason_code` | `ENUM` per section 9.6 | yes | 1 | absence not permitted |
| `reason_text` | `TEXT` | yes | 1 | absence not permitted |
| `replacement_assertion_id` | `ID` | no | 0..1 | the retraction is a bare disavowal with no replacement, which means the subject has no assertion of that kind from this knowledge time forward |

**P1-3.41 (MUST) Half open intervals.** An implementation must interpret every effectivity interval as half open, including `effective_from` and excluding `effective_to`, and must state that interpretation in any interface that exposes the interval.

**P1-3.42 (MUST) Interval validity.** An implementation must reject an effectivity assertion where `effective_to` is present and is not strictly later than `effective_from`.

**P1-3.43 (MUST) Approval basis.** An implementation must reject an effectivity assertion whose `basis` is `APPROVAL`, `SUPERSESSION` or `WITHDRAWAL` and which does not name an approval that exists as a fact row and applies to the named version.

**P1-3.44 (MUST) Uniqueness of being in force.** For any lineage, any scope and any instant of application time, an implementation must ensure that at most one version is in force, where in force is determined by the non retracted effectivity assertions visible at the knowledge time of evaluation.

**P1-3.45 (MUST) Overlap rejection at write time.** An implementation must reject an effectivity assertion that would create an overlap prohibited by clause P1-3.44 as against the assertions visible at the knowledge time of submission, and must report the outcome specified in section 7.6.

**P1-3.46 (MUST) Overlap detection at read time.** Because a retraction can make a previously excluded assertion relevant, an implementation must also detect a violation of clause P1-3.44 at resolution time and must return the ambiguity outcome of section 7.4 rather than choosing between the candidates.

**P1-3.47 (MUST NOT) No arbitration of ambiguity.** An implementation must not resolve a violation of clause P1-3.44 by selecting the most recently asserted, the highest ordinal, or any other candidate.

**P1-3.48 (MUST) Gaps are permitted and are not defects.** An implementation must permit a lineage to have intervals of application time in which no version is in force, and must represent that condition as the distinct outcome specified in section 7.4 rather than as an error or as a fallback to an adjacent version.

**P1-3.49 (MUST) Retroactive assertion is permitted and flagged.** An implementation must permit an effectivity assertion whose `effective_from` precedes its `asserted_ktime`, must set `retroactive` to true in that case, and must not silently alter the resolution of any citation already fixed under section 3.13.

**P1-3.50 (MUST) Future assertion is permitted.** An implementation must permit an effectivity assertion whose `effective_from` is later than its `asserted_ktime`, and must not require any further act at the arrival of that time for the version to be in force.

**P1-3.51 (MUST NOT) No effectivity without version.** An implementation must not accept an effectivity assertion naming a version that does not exist as a fact row.

**P1-3.52 (MUST) Closing by successor.** Where a successor version is asserted in force from an instant at which the predecessor's interval is open, an implementation must record the closure of the predecessor's interval as a new assertion with `basis` of `SUPERSESSION` and a retraction of the open ended assertion, and must not achieve it by modifying the earlier assertion.

**P1-3.53 (MUST) Scope independence.** An implementation must permit different versions of one lineage to be in force in different scopes at the same instant, and must not treat that as a violation of clause P1-3.44.

**P1-3.54 (MUST NOT) No scope inheritance.** An implementation must not resolve an as of citation naming a scope for which no assertion exists by falling back to `GLOBAL` or to any parent scope, and must return the not in force outcome of section 7.4 instead.

### 3.9 Approval and signature

| Field | Type | Required | Card | Absence means |
|---|---|---|---|---|
| `approval_id` | `ID` | yes | 1 | absence not permitted |
| `version_id` | `ID` | yes | 1 | absence not permitted |
| `role` | `TEXT` | yes | 1 | absence not permitted |
| `approver` | `ACTOR` | yes | 1 | absence not permitted; must be a natural person |
| `otime` | `OTIME` | yes | 1 | absence not permitted |
| `ktime` | `KTIME` | yes | 1 | absence not permitted |
| `signature_id` | `ID` | yes | 1 | absence not permitted |
| `approved_digest` | `DIGEST` | yes | 1 | absence not permitted |
| `delegation_id` | `ID` | no | 0..1 | the approver acted in their own capacity |

| Field | Type | Required | Card | Absence means |
|---|---|---|---|---|
| `signature_id` | `ID` | yes | 1 | absence not permitted |
| `signer` | `ACTOR` | yes | 1 | absence not permitted; must be a natural person |
| `signer_printed_name` | `TEXT` | yes | 1 | absence not permitted |
| `meaning` | `TEXT` | yes | 1 | absence not permitted |
| `signed_digest` | `DIGEST` | yes | 1 | absence not permitted |
| `signed_otime` | `OTIME` | yes | 1 | absence not permitted |
| `method` | `ENUM` per section 9.7 | yes | 1 | absence not permitted |
| `authentication_factors` | `INT` | yes | 1 | absence not permitted |
| `authentication_event_ref` | `AUTHREF` | yes | 1 | absence not permitted |
| `certificate_chain` | `TEXT` | no | 0..* | the method does not use certificates |
| `timestamp_token` | `TEXT` | no | 0..1 | no trusted time stamp was obtained, which must be permitted by the method's registry entry |
| `manifestation_text` | `TEXT` | yes | 1 | absence not permitted |

The signature fields follow the requirements of 21 CFR 11.50 and 11.70 for signed electronic records, which require the printed name of the signer, the date and time of signing, the meaning of the signing, and a link between the signature and the record that cannot be excised by ordinary means. The requirement for at least two distinct identification components for non biometric signatures follows 21 CFR 11.200(a)(1). These are cited as specification text. Whether an organisation is subject to that regulation is not a matter for this part; the requirements are adopted here because they are the only widely applicable specification text that states what an electronic signature must carry.

**P1-3.55 (MUST) Signature binds a digest.** An implementation must record, for every signature, the digest of the exact canonical octets that were signed, and must not record a signature that binds only an identifier.

**P1-3.56 (MUST) Signature meaning.** An implementation must record the meaning of every signature as a value, and must not leave the meaning to be inferred from the context in which the signature appears.

**P1-3.57 (MUST) Signer is a natural person.** An implementation must require that the signer of a signature be a natural person, and must reject a signature whose signer is an organisational unit, a service account or an automated agent.

**P1-3.58 (MUST) Agent acts are not signatures.** Where an automated agent performs an act that would otherwise be signed, an implementation must record it as an actor attributed status transition with the agent as `actor`, and must not create a signature row for it. The boundary with `Part 13` is stated in section 12.13.

**P1-3.59 (MUST) Two factors for non biometric methods.** An implementation must record at least two distinct identification components for any signature whose method is not biometric, and must record the count in `authentication_factors`.

**P1-3.60 (MUST) Manifestation.** An implementation must include the printed name of the signer, the date and time of signing and the meaning of the signature in every human readable rendering of the signed subject, and must record that text as `manifestation_text`.

**P1-3.61 (MUST NOT) No credential sharing.** An implementation must not permit a signature to be executed by an actor other than the signer using the signer's credentials, and must record any delegation as a delegation fact row naming both parties and a period.

**P1-3.62 (MUST) Delegated approval names both.** Where an approval is executed under delegation, an implementation must record both the approver and the person on whose authority they acted, and must not record the delegating person as the signer.

**P1-3.63 (MUST) Approval does not confer effectivity.** An implementation must not create, imply or default an effectivity assertion as a consequence of recording an approval.

**P1-3.64 (MUST) Approval binds to a version digest.** An implementation must reject an approval whose `approved_digest` does not match a recorded digest of the authoritative rendition of the named version.

**P1-3.65 (SHOULD) Trusted time stamp.** An implementation should obtain and record a time stamp token from a source independent of the signer for every signature, per the protocol of RFC 3161 or an equivalent, because a signer asserted signing time is not evidence of time.
### 3.10 Records, aggregations and preservation events

A record is evidence of an act. It is not revisable, so it has no versions, no supersession and no effectivity. What it has instead is a declaration, a place in an aggregation, a retention rule, renditions produced by preservation activity, and a history of preservation events. The rules below are deliberately different from those for documents, and clause P1-1.9 forbids implementing one as a special case of the other.

| Field | Type | Required | Card | Absence means |
|---|---|---|---|---|
| `record_id` | `ID` | yes | 1 | absence not permitted |
| `lineage_id` | `ID` | yes | 1 | absence not permitted; the lineage `kind` must be `RECORD` |
| `declared_ktime` | `KTIME` | yes | 1 | absence not permitted |
| `event_otime` | `OTIME` | yes | 1 | absence not permitted; the time of the act the record evidences, not the time of declaration |
| `declaring_actor` | `ACTOR` | yes | 1 | absence not permitted |
| `business_context` | `TEXT` | yes | 1 | absence not permitted; what act this is evidence of |
| `authoritative_rendition_id` | `ID` | yes | 1 | absence not permitted |
| `source_system` | `TEXT` | no | 0..1 | the record was declared directly through this component |
| `capture_completeness` | `ENUM<COMPLETE, PARTIAL, UNKNOWN>` | yes | 1 | absence not permitted |
| `corrects_record_id` | `ID` | no | 0..1 | the record does not correct an earlier record |

| Field | Type | Required | Card | Absence means |
|---|---|---|---|---|
| `aggregation_id` | `ID` | yes | 1 | absence not permitted |
| `parent_aggregation_id` | `ID` | no | 0..1 | the aggregation is a root |
| `title` | `TEXT` | yes | 1 | absence not permitted |
| `opened_ktime` | `KTIME` | yes | 1 | absence not permitted |
| `closed_ktime` | `KTIME` | no | 0..1 | the aggregation is open to further members |

| Field | Type | Required | Card | Absence means |
|---|---|---|---|---|
| `preservation_event_id` | `ID` | yes | 1 | absence not permitted |
| `subject_id` | `ID` | yes | 1 | absence not permitted |
| `event_type` | `ENUM` per section 9.9 | yes | 1 | absence not permitted |
| `otime` | `OTIME` | yes | 1 | absence not permitted |
| `agent` | `ACTOR` | yes | 1 | absence not permitted |
| `outcome` | `ENUM<SUCCESS, FAILURE, PARTIAL>` | yes | 1 | absence not permitted |
| `input_digest` | `DIGEST` | yes | 1..* | absence not permitted |
| `output_digest` | `DIGEST` | no | 0..* | the event produced no new object, as for a fixity check |
| `tool_identification` | `TEXT` | no | 0..1 | the event was performed without a tool, which for a migration is a defect |

The preservation event model follows PREMIS 3.0, which defines Event as one of five entities alongside Intellectual Entity, Object, Agent and Rights, and which treats fixity as a property of an Object verified by an Event.

**P1-3.66 (MUST) Record immutability.** An implementation must not permit any field of a record fact row, nor the octets of its authoritative rendition, to change after declaration.

**P1-3.67 (MUST NOT) No record versions.** An implementation must not assign a version, an ordinal, a version label, an effectivity assertion or a supersession relation to a record.

**P1-3.68 (MUST) Correction by further record.** An implementation must effect a correction to a record by declaring a further record that names the earlier one in `corrects_record_id`, and must not retract, amend or annotate the earlier record's content.

**P1-3.69 (MUST) Both records remain readable.** An implementation must keep a corrected record readable and must return it, together with the correcting record, in response to any read of either.

**P1-3.70 (MUST) Declaration is irreversible.** An implementation must not permit a declared record to be undeclared. Where content was declared in error, the implementation must declare a correcting record stating the error, and must apply disposition only under section 3.12.

**P1-3.71 (MUST) Capture completeness.** An implementation must record whether the captured content is a complete expression of the act evidenced, and must not default the value to `COMPLETE`.

**P1-3.72 (MUST) Migration preserves the original digest.** Where a preservation event produces a new rendition of a record, an implementation must retain the digest of every input rendition and must not replace it with the digest of the output.

**P1-3.73 (MUST) Migration is not correction.** An implementation must not record a format migration as a correcting record, and must not record a correcting record as a preservation event.

**P1-3.74 (MUST) Aggregation membership is an assertion.** An implementation must record the membership of a record in an aggregation as an assertion row with a knowledge time, because reclassification is common and its history is what explains a retention decision.

**P1-3.75 (MUST NOT) No orphan records.** An implementation must not permit a record to exist without at least one aggregation membership assertion visible at the current knowledge time, except during a declared capture window whose maximum duration the implementation must declare.

**P1-3.76 (MAY) Multiple memberships.** An implementation may permit a record to be a member of more than one aggregation, and must in that case specify in its own documentation how retention rules from more than one aggregation combine, using the precedence rule of clause P1-3.92.

### 3.11 Metadata and classification assertions

| Field | Type | Required | Card | Absence means |
|---|---|---|---|---|
| `metadata_assertion_id` | `ID` | yes | 1 | absence not permitted |
| `subject_id` | `ID` | yes | 1 | absence not permitted |
| `subject_kind` | `ENUM<LINEAGE, VERSION, RENDITION, RECORD, AGGREGATION>` | yes | 1 | absence not permitted |
| `element_key` | `TEXT` | yes | 1 | absence not permitted; drawn from the registry of section 9.4 |
| `value` | `TEXT` | yes | 1 | absence not permitted; a metadata element with no value must be absent rather than empty |
| `value_language` | `LANG` | no | 0..1 | the value is not natural language text |
| `valid_from` | `ATIME` | yes | 1 | absence not permitted |
| `valid_to` | `ATIME` | no | 0..1 | the value holds until further notice |
| `asserted_ktime` | `KTIME` | yes | 1 | absence not permitted |
| `actor` | `ACTOR` | yes | 1 | absence not permitted |
| `source` | `ENUM<HUMAN, DERIVED, MIGRATED, INFERRED>` | yes | 1 | absence not permitted |

The mandatory core metadata set is the following. An element in this set is mandatory in the sense that the subject may not be read as complete without it, not in the sense that a draft cannot exist before it is supplied.

| Element | Subject | Notes |
|---|---|---|
| `title` | version | |
| `identifier` | lineage | the `lineage_urn` |
| `version_label` | version | |
| `kind` | lineage | |
| `authoritative_language` | lineage | |
| `owning_function` | lineage | |
| `custodian` | lineage | the actor accountable for currency |
| `classification` | lineage or record | see below |
| `security_marking` | version or record | |
| `retention_rule` | lineage or aggregation | |
| `review_period` | lineage | absent means no periodic review, which must be an explicit assertion of `review_period` with value `NONE` rather than an absent element |
| `media_type` | rendition | |
| `canonical_profile` | rendition | |
| `digest` | rendition | |

**P1-3.77 (MUST) Metadata history.** An implementation must record every change to a metadata value as a new assertion row, and must retain the superseded value and its knowledge time.

**P1-3.78 (MUST) Core set completeness for effectivity.** An implementation must reject an effectivity assertion for a version whose subject lacks any element of the mandatory core metadata set of section 3.11.

**P1-3.79 (MUST NOT) No empty as absent.** An implementation must not record an empty string, a zero or a sentinel value in place of an absent metadata element.

**P1-3.80 (MUST) Inference marking.** An implementation must record `source` as `INFERRED` for any metadata value it derived by a method that is not deterministic from other recorded values, and must not present an inferred value as asserted.

**P1-3.81 (MUST) Classification assignment is an assertion.** An implementation must record the assignment of a subject to a classification scheme node as an assertion with a valid period and a knowledge time.

**P1-3.82 (MUST NOT) No scheme ownership.** An implementation must not define, version or govern the classification scheme itself, and must reference a scheme version governed under `Part 10` as stated in section 12.10.

**P1-3.83 (MUST) Scheme version pinning.** An implementation must record, with every classification assignment, the identifier and version of the scheme against which it was made, so that a later change to the scheme does not silently change the meaning of the assignment.

**P1-3.84 (SHOULD) Findability.** An implementation should provide projections that retrieve subjects by any element of the mandatory core metadata set and by classification, for any knowledge time within its declared horizon.

### 3.12 Retention, holds, disposition and tombstones

| Field | Type | Required | Card | Absence means |
|---|---|---|---|---|
| `retention_application_id` | `ID` | yes | 1 | absence not permitted |
| `subject_id` | `ID` | yes | 1 | absence not permitted |
| `rule_id` | `ID` | yes | 1 | absence not permitted; the rule is a controlled document under this part |
| `trigger_type` | `ENUM` per section 9.10 | yes | 1 | absence not permitted |
| `trigger_otime` | `OTIME` | no | 0..1 | the trigger has not yet occurred, so no disposition due date is computable |
| `retention_period` | `DURATION` | yes | 1 | absence not permitted; the value `P0D` means dispose at trigger and the value `PERMANENT` is a reserved literal |
| `disposition_action` | `ENUM<DESTROY, TRANSFER, RETAIN_PERMANENTLY, REVIEW_AGAIN>` | yes | 1 | absence not permitted |
| `authority_citation` | `TEXT` | yes | 1 | absence not permitted; the instrument that requires this retention |
| `asserted_ktime` | `KTIME` | yes | 1 | absence not permitted |

| Field | Type | Required | Card | Absence means |
|---|---|---|---|---|
| `hold_id` | `ID` | yes | 1 | absence not permitted |
| `subject_selector` | `TEXT` | yes | 1 | absence not permitted; may name a subject, an aggregation or a classification node |
| `reason_code` | `ENUM` per section 9.11 | yes | 1 | absence not permitted |
| `reason_text` | `TEXT` | yes | 1 | absence not permitted |
| `authority` | `AUTHREF` | yes | 1 | absence not permitted |
| `applied_ktime` | `KTIME` | yes | 1 | absence not permitted |
| `applied_by` | `ACTOR` | yes | 1 | absence not permitted |
| `expected_duration` | `DURATION` | no | 0..1 | no expectation is recorded; must not be read as an expiry |

| Field | Type | Required | Card | Absence means |
|---|---|---|---|---|
| `authorisation_id` | `ID` | yes | 1 | absence not permitted |
| `subject_id` | `ID` | yes | 1 | absence not permitted |
| `action` | `ENUM<DESTROY, TRANSFER>` | yes | 1 | absence not permitted |
| `authoriser` | `ACTOR` | yes | 1 | absence not permitted; must be a natural person |
| `signature_id` | `ID` | yes | 1 | absence not permitted |
| `citation_count_at_authorisation` | `INT` | yes | 1 | absence not permitted |
| `override_of_citation` | `BOOL` | yes | 1 | absence not permitted |
| `ktime` | `KTIME` | yes | 1 | absence not permitted |

| Field | Type | Required | Card | Absence means |
|---|---|---|---|---|
| `tombstone_id` | `ID` | yes | 1 | absence not permitted |
| `subject_id` | `ID` | yes | 1 | absence not permitted |
| `subject_kind` | `ENUM<VERSION, RENDITION, RECORD>` | yes | 1 | absence not permitted |
| `retained_digests` | `DIGEST` | yes | 1..* | absence not permitted |
| `retained_metadata` | `TEXT` | yes | 1 | absence not permitted; the mandatory core set as at the moment of destruction |
| `authorisation_id` | `ID` | yes | 1 | absence not permitted |
| `executed_ktime` | `KTIME` | yes | 1 | absence not permitted |
| `executed_by` | `ACTOR` | yes | 1 | absence not permitted |
| `method` | `TEXT` | yes | 1 | absence not permitted |

**P1-3.85 (MUST) Holds are orthogonal to status.** An implementation must represent a hold as an assertion separate from lifecycle status, and must not implement a hold as a status value.

**P1-3.86 (MUST) Holds accumulate.** An implementation must permit more than one hold on a subject and must not release a subject from disposition eligibility until every hold on it has been released.

**P1-3.87 (MUST NOT) No automatic hold expiry.** An implementation must not release a hold by the passage of time, and must require an explicit release act recorded with an actor and an authority.

**P1-3.88 (MUST) Disposition requires authorisation.** An implementation must not execute a disposition without a disposition authorisation fact row naming a natural person and a signature.

**P1-3.89 (MUST) Citation count at authorisation.** An implementation must compute and record the number of citations resolving to the subject at the moment of authorisation, and must record whether the authoriser overrode a non zero count.

**P1-3.90 (MUST) Tombstone on destruction.** An implementation must, on destroying the content octets of any subject, retain a tombstone containing the subject identity, every recorded digest, the mandatory core metadata as at destruction, and the authorisation, and must retain the tombstone for at least as long as the longest retention period applying to anything that cites the subject.

**P1-3.91 (MUST NOT) No silent absence after disposition.** An implementation must resolve a citation to a destroyed subject to the disposed outcome of section 7.4 together with the tombstone, and must not return the outcome for an unknown subject.

**P1-3.92 (MUST) Retention precedence.** Where more than one retention application governs a subject, an implementation must apply the longest retention period and must record which application it selected and why, and must not merge the periods by any other rule.

**P1-3.93 (MUST) Audit survives the subject.** An implementation must retain the audit record of a subject, and the record of its disposition, after the subject's content has been destroyed.

**P1-3.94 (SHOULD NOT) No cryptographic erasure as disposition.** An implementation should not treat the destruction of a decryption key as the destruction of content for the purposes of this part, because the ciphertext remains and the claim that it is unreadable rests on an assumption about future cryptanalysis rather than on a recorded act; where it does so it must record the method in the tombstone and must state the assumption.

**P1-3.95 (MUST) Rules are controlled documents.** An implementation must hold every retention rule as a document lineage under this part, so that a disposition executed years ago can be explained by the rule text then in force.
### 3.13 Citation and locator

| Field | Type | Required | Card | Absence means |
|---|---|---|---|---|
| `citation_id` | `ID` | yes | 1 | absence not permitted |
| `citing_entity_ref` | `URN` | yes | 1 | absence not permitted |
| `cited_lineage_id` | `ID` | yes | 1 | absence not permitted |
| `mode` | `ENUM<PINNED, AS_OF>` | yes | 1 | absence not permitted |
| `cited_version_id` | `ID` | no | 0..1 | required when `mode` is `PINNED`; absent when `mode` is `AS_OF` |
| `cited_digest` | `DIGEST` | no | 0..1 | required when `mode` is `PINNED`; absent when `mode` is `AS_OF` |
| `as_of_atime` | `ATIME` | no | 0..1 | required when `mode` is `AS_OF` |
| `as_of_ktime` | `KTIME` | no | 0..1 | required when `mode` is `AS_OF`; the knowledge time at which the citing act was performed |
| `scope` | `SCOPE` | no | 0..1 | required when `mode` is `AS_OF` and the lineage is scoped |
| `locator_scheme` | `ENUM` per section 9.3 | no | 0..1 | the citation is to the whole subject |
| `locator_expression` | `TEXT` | no | 0..1 | as above |
| `fixed_ktime` | `KTIME` | yes | 1 | absence not permitted |

| Field | Type | Required | Card | Absence means |
|---|---|---|---|---|
| `resolution_id` | `ID` | yes | 1 | absence not permitted |
| `citation_id` | `ID` | yes | 1 | absence not permitted |
| `requested_atime` | `ATIME` | yes | 1 | absence not permitted |
| `requested_ktime` | `KTIME` | yes | 1 | absence not permitted |
| `outcome` | `ENUM` per section 7.4 | yes | 1 | absence not permitted |
| `resolved_version_id` | `ID` | no | 0..1 | no version was resolved, which the outcome explains |
| `basis_assertion_ids` | `ID` | no | 0..* | no assertion was used, which the outcome explains |
| `divergence_flag` | `BOOL` | yes | 1 | absence not permitted |
| `divergent_version_id` | `ID` | no | 0..1 | there is no divergence, or the divergent resolution produced no version |
| `resolved_ktime` | `KTIME` | yes | 1 | absence not permitted |

**P1-3.96 (MUST) Mode is explicit.** An implementation must require the citing party to state the resolution mode, and must not infer it.

**P1-3.97 (MUST) Pinned citations carry a digest.** An implementation must reject a pinned citation that does not carry the digest of the cited version's authoritative rendition, because a version identifier alone cannot detect substitution of content.

**P1-3.98 (MUST) As of citations carry both times.** An implementation must reject an as of citation that does not carry both an application time and a knowledge time.

**P1-3.99 (MUST) Default knowledge time.** Where a citing party supplies an application time but no knowledge time, an implementation must reject the citation rather than defaulting the knowledge time to the present, because defaulting silently converts a historical question into a current one.

**P1-3.100 (MUST) Resolution is recorded.** An implementation must record every resolution of a citation as a fact row, including the outcome, the assertions relied upon, and the two times used.

**P1-3.101 (MUST) Divergence detection.** For every resolution of an as of citation, an implementation must also resolve at the current knowledge time with the same application time, must set `divergence_flag` where the two results differ, and must record the divergent result.

**P1-3.102 (MUST NOT) No overwriting of a resolution.** An implementation must not modify a recorded resolution when the underlying assertions later change, and must record a further resolution instead.

**P1-3.103 (MUST) Locator scheme is named.** An implementation must record the scheme of every locator and must not accept a locator expression without one.

**P1-3.104 (MUST) Clause identifier stability.** Where an implementation supports the `CLAUSE_ID` locator scheme, it must require clause identifiers to be assigned once per lineage and to denote the same unit of content in every version in which that unit appears.

**P1-3.105 (MUST NOT) No renumbering.** An implementation must not permit a clause identifier to be reassigned to a different unit of content in a later version of the same lineage.

**P1-3.106 (MUST) Retired locators resolve to a statement.** Where a locator identified a unit of content that is not present in the version being resolved against, an implementation must return the retired or unresolvable outcome of section 7.5 together with the last version in which the unit was present, and must not return a null result.

**P1-3.107 (SHOULD) Redundant locators.** An implementation should permit a citation to carry more than one locator in different schemes, so that a structural locator and a quotation based locator can corroborate each other when content is later reflowed.

### 3.14 Projections

A projection is a named, deterministic function from the recorded rows to a read model. Projections are the only way current state is read. This section specifies the minimum set; an implementation may add others.

| Projection | Parameters | Yields |
|---|---|---|
| `version_status` | version, knowledge time | the status of the version as believed at that knowledge time |
| `in_force` | lineage, scope, application time, knowledge time | at most one version, or the ambiguity or gap outcome |
| `current_effective` | lineage, scope | shorthand for `in_force` with both times set to the present |
| `lineage_history` | lineage, knowledge time | the ordered versions with their effectivity intervals as believed at that knowledge time |
| `belief_history` | lineage, application time | for each knowledge time at which the answer changed, the version then believed in force |
| `metadata_as_of` | subject, application time, knowledge time | the metadata element values |
| `disposition_due` | knowledge time | subjects whose retention has elapsed and which are not held |
| `held_subjects` | knowledge time | subjects under at least one unreleased hold |
| `review_due` | knowledge time | lineages past their review date |
| `citation_inbound` | subject | citations resolving to the subject |
| `controlled_copies_outstanding` | version | issued copies not yet returned, destroyed or superseded |
| `integrity_state` | subject | the latest fixity outcome per digest algorithm |

**P1-3.108 (MUST) Determinism.** Every projection must be a deterministic function of the recorded rows and its parameters, such that two evaluations over the same rows with the same parameters yield the same result.

**P1-3.109 (MUST) Rebuildability.** An implementation must be able to discard and rebuild every projection from the recorded rows alone, and must not hold in a projection any fact that is not derivable from them.

**P1-3.110 (MUST) Knowledge time parameter.** Every projection specified in section 3.14 that takes a knowledge time must accept any value within the implementation's declared horizon, and must not restrict it to the present.

**P1-3.111 (MUST NOT) No writes through projections.** An implementation must not accept a write, correction or annotation through a projection interface.

**P1-3.112 (MUST) Staleness disclosure.** Where a projection is materialised asynchronously, an implementation must return with every read the knowledge time up to which the projection has incorporated rows, and must not present a stale read as current.

**P1-3.113 (MUST) The belief history projection.** An implementation must provide `belief_history`, because it is the only projection that makes a retroactive correction visible as a change of belief rather than as a change of fact.

### 3.15 Integrity artifacts

| Field | Type | Required | Card | Absence means |
|---|---|---|---|---|
| `profile_id` | `ID` | yes | 1 | absence not permitted |
| `profile_key` | `TEXT` | yes | 1 | absence not permitted; the registry key per section 9.2 |
| `profile_version` | `TEXT` | yes | 1 | absence not permitted |
| `applies_to_media` | `MEDIA` | yes | 1..* | absence not permitted |
| `specification_ref` | `TEXT` | yes | 1 | absence not permitted; the external specification the profile implements |
| `implementation_ref` | `TEXT` | no | 0..1 | the profile is implemented by an unnamed internal routine, which section 3.15 marks as a risk |

| Field | Type | Required | Card | Absence means |
|---|---|---|---|---|
| `digest_id` | `ID` | yes | 1 | absence not permitted |
| `subject_id` | `ID` | yes | 1 | absence not permitted |
| `algorithm` | `ENUM` per section 9.5 | yes | 1 | absence not permitted |
| `value` | `DIGEST` | yes | 1 | absence not permitted |
| `profile_id` | `ID` | yes | 1 | absence not permitted |
| `computed_ktime` | `KTIME` | yes | 1 | absence not permitted |
| `computed_by` | `ACTOR` | yes | 1 | absence not permitted |
| `is_original` | `BOOL` | yes | 1 | absence not permitted; true for the digest computed at the moment the subject was first written |

| Field | Type | Required | Card | Absence means |
|---|---|---|---|---|
| `fixity_check_id` | `ID` | yes | 1 | absence not permitted |
| `digest_id` | `ID` | yes | 1 | absence not permitted |
| `ktime` | `KTIME` | yes | 1 | absence not permitted |
| `outcome` | `ENUM<MATCH, MISMATCH, INDETERMINATE_PROFILE, INDETERMINATE_ALGORITHM, INDETERMINATE_CONTENT_UNAVAILABLE>` | yes | 1 | absence not permitted |
| `recomputed_value` | `DIGEST` | no | 0..1 | no value was computed, which the outcome explains |
| `agent` | `ACTOR` | yes | 1 | absence not permitted |

The distinction among the three indeterminate outcomes is the substance of this section. A conventional implementation records one failure condition, "hash mismatch", and thereby reports content alteration in three situations, only one of which is content alteration. If the canonical form profile can no longer be executed, the correct statement is that integrity cannot be assessed. If the digest algorithm implementation is no longer available, likewise. If the content octets are unavailable, likewise. Reporting any of these as a mismatch is a false accusation of tampering, and over a retention period measured in decades it is the more likely outcome, because canonicalisers and algorithms are lost faster than storage corrupts.

**P1-3.114 (MUST) Canonical form declared.** An implementation must record a canonical form profile for every rendition before computing any digest of it, and must reject a rendition with no profile.

**P1-3.115 (MUST NOT) No default profile.** An implementation must not apply a default canonical form profile to content whose profile was not declared.

**P1-3.116 (MUST) Digest over canonical octets.** An implementation must compute every digest over the octet sequence produced by the named profile, and must record which profile was used with the digest.

**P1-3.117 (MUST) Original digest retained.** An implementation must retain the digest computed at first write for the life of the subject, and must not remove it when a digest under a further algorithm is added.

**P1-3.118 (MUST) Algorithm agility.** An implementation must be able to add a digest under a further algorithm to an existing subject, computed over the same canonical octets, without altering or removing any existing digest.

**P1-3.119 (MUST) Fixity outcome discrimination.** An implementation must distinguish the five fixity outcomes of section 3.15 and must not report an indeterminate condition as a mismatch.

**P1-3.120 (MUST) Mismatch is a defect signal.** On a fixity outcome of `MISMATCH`, an implementation must record the recomputed value, must raise the signal required by section 8.5, and must not overwrite the recorded digest with the recomputed one.

**P1-3.121 (SHOULD) Scheduled fixity checking.** An implementation should verify the fixity of retained subjects on a declared schedule, and should declare the interval and the sampling basis, because an unverified digest recorded decades ago is evidence only that a digest was once recorded.

**P1-3.122 (SHOULD) Evidence records for long horizons.** Where the declared time horizon of clause P1-1.12 exceeds the expected cryptographic lifetime of the digest algorithm in use, an implementation should maintain evidence records with time stamp renewal in the manner specified by RFC 4998 or RFC 6283, because those specifications address precisely the problem of proving that data existed and was unaltered across the deprecation of the algorithms originally used to prove it.

**P1-3.123 (SHOULD) Profile implementation is archived.** An implementation should retain, as a record under this part, an executable or fully specified statement of every canonical form profile it has used, because the alternative is that future fixity checks return indeterminate for reasons the organisation itself created.

### 3.16 Controlled copies and distribution

| Field | Type | Required | Card | Absence means |
|---|---|---|---|---|
| `copy_id` | `ID` | yes | 1 | absence not permitted |
| `version_id` | `ID` | yes | 1 | absence not permitted |
| `rendition_id` | `ID` | yes | 1 | absence not permitted |
| `control_state` | `ENUM<CONTROLLED, UNCONTROLLED>` | yes | 1 | absence not permitted |
| `copy_number` | `TEXT` | no | 0..1 | required when `control_state` is `CONTROLLED` |
| `recipient` | `ACTOR` | no | 0..1 | required when `control_state` is `CONTROLLED` |
| `issued_ktime` | `KTIME` | yes | 1 | absence not permitted |
| `issued_by` | `ACTOR` | yes | 1 | absence not permitted |
| `medium` | `ENUM<ELECTRONIC, PRINT, OTHER>` | yes | 1 | absence not permitted |
| `acknowledged_ktime` | `KTIME` | no | 0..1 | no acknowledgement was received; must not be read as refusal |
| `disposition_ktime` | `KTIME` | no | 0..1 | the copy is outstanding |
| `disposition_kind` | `ENUM<RETURNED, DESTROYED, SUPERSEDED, LOST>` | no | 0..1 | as above |

**P1-3.124 (MUST) Distribution record for controlled copies.** An implementation must record every controlled copy it issues with a copy number and a recipient.

**P1-3.125 (MUST) Recall obligation on ceasing to be in force.** When a version ceases to be in force, an implementation must produce the list of outstanding controlled copies of it and must record the disposition of each.

**P1-3.126 (MUST) Uncontrolled copies are marked.** An implementation must include, on the face of every uncontrolled copy it produces, the lineage identifier, the version label, the knowledge time at which the copy was produced, and a statement that currency must be verified against the component.

**P1-3.127 (MUST NOT) No unmarked export.** An implementation must not produce an export of a version in a human readable rendition without the markings of clause P1-3.126 or a controlled copy record.

**P1-3.128 (SHOULD) Acknowledgement.** An implementation should support recording recipient acknowledgement of a controlled copy, and should treat absence of acknowledgement as an outstanding obligation rather than as receipt.

### 3.17 Review

| Field | Type | Required | Card | Absence means |
|---|---|---|---|---|
| `review_application_id` | `ID` | yes | 1 | absence not permitted |
| `lineage_id` | `ID` | yes | 1 | absence not permitted |
| `review_period` | `DURATION` | yes | 1 | absence not permitted; the reserved literal `NONE` means no periodic review is required |
| `basis` | `ENUM<APPROVAL, LAST_REVIEW, EFFECTIVE_FROM>` | yes | 1 | absence not permitted; the date from which the period runs |
| `asserted_ktime` | `KTIME` | yes | 1 | absence not permitted |
| `authority` | `AUTHREF` | yes | 1 | absence not permitted |

| Field | Type | Required | Card | Absence means |
|---|---|---|---|---|
| `review_outcome_id` | `ID` | yes | 1 | absence not permitted |
| `lineage_id` | `ID` | yes | 1 | absence not permitted |
| `version_id` | `ID` | yes | 1 | absence not permitted |
| `outcome` | `ENUM<CONFIRMED_UNCHANGED, REVISION_REQUIRED, WITHDRAW, OBSOLETE>` | yes | 1 | absence not permitted |
| `reviewer` | `ACTOR` | yes | 1 | absence not permitted |
| `otime` | `OTIME` | yes | 1 | absence not permitted |
| `signature_id` | `ID` | yes | 1 | absence not permitted |
| `next_review_atime` | `ATIME` | no | 0..1 | the next review date is computed from the review application rather than set explicitly |

**P1-3.129 (MUST) Review period is asserted.** An implementation must record a review period for every lineage, including the explicit assertion that none is required.

**P1-3.130 (MUST NOT) No lapse by silence.** An implementation must not change the status or the effectivity of a version because a review date has passed.

**P1-3.131 (MUST) Overdue is visible.** An implementation must report a lineage whose review date has passed through the `review_due` projection, and must expose the overdue condition to any reader of a version of that lineage.

**P1-3.132 (MAY) Configured lapse.** An implementation may support a configuration in which passing a review date causes a version to cease to be in force, and must in that case record the cessation as an explicit effectivity assertion with `basis` of `WITHDRAWAL` and an actor identifying the automated agent, rather than as a computed absence.

**P1-3.133 (MUST) Confirmation is an act.** An implementation must record the confirmation of an unchanged document at review as a review outcome with a signature, and must not represent it by extending a date.

### 3.18 Worked demonstration of the append only model

This section demonstrates that the model of section 3 satisfies the append only constraint, including for the hardest case, which is a retroactive correction to effectivity after a determination has already been made in reliance on the earlier belief. Rows are shown with only the fields that carry the demonstration. `L` is a lineage, `V2` and `V3` are versions of it, `E` rows are effectivity assertions, `R` is a retraction, `C` is a citation and `S` rows are resolutions.

Step 1, on 2027-02-01. Version 3 is approved and asserted in force from 2027-03-01.

| row | relation | subject | effective_from | effective_to | asserted_ktime | retracted |
|---|---|---|---|---|---|---|
| E1 | effectivity | L, V2 | 2025-01-01 | 2027-03-01 | 2027-02-01 | no |
| E2 | effectivity | L, V3 | 2027-03-01 | absent | 2027-02-01 | no |

Step 2, on 2027-06-14. A determination is made and cites the lineage as of application time 2027-04-02 with knowledge time 2027-06-14.

| row | relation | detail |
|---|---|---|
| C1 | citation | mode `AS_OF`, lineage L, as_of_atime 2027-04-02, as_of_ktime 2027-06-14, fixed_ktime 2027-06-14 |
| S1 | resolution | outcome `RESOLVED`, resolved_version V3, basis E2, divergence_flag false |

Step 3, on 2029-09-30. It is discovered that version 3 was never validly in force before 2027-05-01, because a prerequisite approval was defective. The correction is appended.

| row | relation | subject | effective_from | effective_to | asserted_ktime | notes |
|---|---|---|---|---|---|---|
| R1 | retraction | targets E2 | | | 2029-09-30 | reason: approval defect |
| R2 | retraction | targets E1 | | | 2029-09-30 | reason: consequential |
| E3 | effectivity | L, V2 | 2025-01-01 | 2027-05-01 | 2029-09-30 | basis `CORRECTION` |
| E4 | effectivity | L, V3 | 2027-05-01 | absent | 2029-09-30 | basis `CORRECTION`, retroactive true |

Nothing has been modified. E1 and E2 are still present and still readable, and are now retracted as of knowledge time 2029-09-30.

Step 4, on 2034-11-20, an auditor asks two different questions and receives two different and equally correct answers.

| question | parameters | result |
|---|---|---|
| What was in force on 2027-04-02, as best we now know | atime 2027-04-02, ktime 2034-11-20 | V2, on the basis of E3 |
| What did we believe was in force on 2027-04-02 at the moment of the determination | atime 2027-04-02, ktime 2027-06-14 | V3, on the basis of E2 |

The recorded resolution S1 remains exactly as written, so the determination can be explained rather than merely contradicted. Re resolving C1 at the present knowledge time produces a second resolution row S2 with outcome `RESOLVED`, resolved version V2, and `divergence_flag` true, which is the signal that a determination was made under a version later found not to have been in force. That signal is the deliverable. A system that overwrites effectivity produces the 2034 answer only, and destroys the evidence that the 2027 decision was reasonable on what was then recorded.

**P1-3.134 (MUST) Belief and fact both answerable.** An implementation must answer, for any lineage and application time within its horizon, both what it now believes was in force and what it believed at any earlier knowledge time, and must not present either as the only answer.

**P1-3.135 (MUST) Prior resolutions are immutable.** An implementation must retain every recorded resolution unchanged when the assertions it relied upon are retracted.

**P1-3.136 (MUST) Divergence is reported to the citing entity.** On detecting divergence for a recorded citation, an implementation must emit the event specified in section 4.7 so that the owner of the citing entity can act, and must not confine the finding to its own projections.
## 4. Interfaces

### 4.1 Interface principles

This section specifies the operations the component accepts, the events it emits, and what it reads from other components. It does not specify a transport, an encoding or a naming convention, because those are implementation decisions and constraining them would exclude conforming implementations for no gain in testability.

Every operation in this part is one of three kinds.

**Recording operations** append fact or assertion rows. They are synchronous in the sense that the caller learns whether the row was written, and the operation either writes every row it implies or none of them.

**Reading operations** evaluate a projection. They are synchronous and side effect free, except that a resolution read also writes a resolution row, which is stated explicitly in clause P1-4.19 because a read that writes is a surprise and surprises in interfaces become defects.

**Bulk operations** are asynchronous and report progress. Nothing in this part requires a bulk operation, and any that an implementation offers must decompose into the recording and reading operations without weakening any clause.

**P1-4.1 (MUST) Operation atomicity.** Every recording operation must write all of the rows it implies or none of them, and must not leave a subject in a condition that no projection of section 3.14 can interpret.

**P1-4.2 (MUST) Explicit actor on every operation.** Every recording operation must carry the actor performing it, and an implementation must reject an operation with no actor, including operations initiated by its own scheduled processes, which must name the automated agent.

**P1-4.3 (MUST) Idempotency key.** Every recording operation must accept a caller supplied idempotency key, and an implementation must, on receiving a repeated key within its declared deduplication window, return the outcome of the original attempt without writing further rows.

**P1-4.4 (MUST) Declared deduplication window.** An implementation must declare the period for which idempotency keys are honoured, and must reject rather than silently reprocess an operation whose key has expired from that window.

**P1-4.5 (MUST) Expected sequence on concurrent writes.** Every recording operation that depends on the current state of a stream must accept the sequence number the caller believes to be current, and must reject the operation where it does not match, as specified in section 6.5.

**P1-4.6 (MUST NOT) No partial success reporting.** An implementation must not report an operation as succeeded with warnings where any row it implies was not written.

### 4.2 Recording operations

The table is normative by clause P1-4.7. "Signed" indicates that the operation requires a signature row per section 3.9. "Authority" indicates that it requires an `AUTHREF`.

| Operation | Writes | Signed | Authority | Notable preconditions |
|---|---|---|---|---|
| `register_lineage` | lineage | no | no | none |
| `create_version` | version, rendition, digest, profile binding | no | no | lineage exists; profile declared |
| `add_rendition` | rendition, digest | no | no | version exists |
| `assert_metadata` | metadata assertion | no | no | element key registered |
| `assign_classification` | classification assignment | no | no | scheme version resolvable |
| `submit_for_review` | status transition | no | no | status is `DRAFT` |
| `record_review_decision` | status transition | yes | no | status is `IN_REVIEW` |
| `approve` | approval, signature, status transition | yes | yes | status is `IN_REVIEW`; core metadata complete |
| `assert_effectivity` | effectivity assertion | no | yes | approval exists; no prohibited overlap |
| `supersede` | effectivity assertion, retraction, status transition | no | yes | successor version approved |
| `withdraw` | effectivity assertion, retraction, status transition | yes | yes | version is or was in force |
| `declare_obsolete` | status transition at lineage level | yes | yes | no version in force |
| `declare_record` | record, rendition, digest, aggregation membership | yes | no | lineage kind is `RECORD` |
| `declare_correcting_record` | record naming the corrected record | yes | no | corrected record exists |
| `record_preservation_event` | preservation event, rendition, digest | no | no | subject exists |
| `apply_retention` | retention application | no | yes | rule lineage exists and has a version in force |
| `apply_hold` | hold | no | yes | subject exists |
| `release_hold` | hold release | no | yes | hold exists and is unreleased |
| `authorise_disposition` | disposition authorisation, signature | yes | yes | retention elapsed; no unreleased hold |
| `execute_disposition` | disposition execution, tombstone | no | no | authorisation exists |
| `issue_copy` | controlled copy issue | no | no | version in force or explicitly permitted |
| `record_copy_disposition` | controlled copy disposition | no | no | copy outstanding |
| `apply_review_period` | review period application | no | yes | lineage exists |
| `record_review_outcome` | review outcome, signature | yes | no | review due or early review permitted |
| `fix_citation` | citation, resolution | no | no | lineage exists |
| `verify_fixity` | fixity check | no | no | digest exists |
| `retract_assertion` | retraction, optional replacement | no | yes | target assertion exists and is unretracted |
| `annotate_fact` | annotation assertion | no | no | target fact row exists |

**P1-4.7 (MUST) Operation coverage.** An implementation must provide an operation for every row that a clause of this part requires it to write, and every such operation must satisfy the signature and authority requirements given in the table of section 4.2.

**P1-4.8 (MUST NOT) No compound approval.** An implementation must not provide an operation that records an approval and an effectivity assertion in a single act without the caller supplying both the approval and the effectivity parameters explicitly, and must not default the effectivity interval.

**P1-4.9 (MUST) Precondition failure is a named outcome.** An implementation must report a precondition failure as the corresponding outcome of section 7, and must not report it as an internal error.

**P1-4.10 (MUST) Reason on every retraction and withdrawal.** An implementation must require reason text on `retract_assertion`, `withdraw` and `declare_obsolete`, and must reject the operation where it is absent or empty.

**P1-4.11 (MAY) Compound convenience operations.** An implementation may provide operations that compose those in section 4.2, provided each writes exactly the rows the composed operations would write, and provided a caller can perform each step separately.

### 4.3 Reading operations

| Operation | Parameters | Returns | Writes |
|---|---|---|---|
| `resolve` | lineage, mode, times, scope, locator | resolution outcome per section 7.4 and 7.5 | resolution row |
| `read_projection` | projection name, parameters | projection result and its incorporated knowledge time | nothing |
| `fetch_content` | rendition, purpose | octets or a non result per section 7.7 | access record per section 8.4 |
| `list_history` | lineage, knowledge time | versions, statuses, effectivity | nothing |
| `list_beliefs` | lineage, application time | belief history | nothing |
| `export_evidence_package` | subject, options | package per section 8.6 | export record |
| `verify_package` | package | verification outcome | nothing |

**P1-4.12 (MUST) Purpose on content fetch.** An implementation must require the caller of `fetch_content` to state a purpose drawn from a registered set, because the access record is worthless for reconstructing a determination if it cannot distinguish a reader from a determiner.

**P1-4.13 (MUST) Projection identification.** An implementation must return, with every projection read, the projection name and the knowledge time up to which it is incorporated.

**P1-4.14 (MUST) Evidence package verification without the component.** An implementation must specify the verification procedure for an evidence package in the package itself, and `verify_package` must not be the only means of verifying it.

**P1-4.15 (MUST NOT) No unbounded read.** An implementation must not offer a read whose result size is unbounded without pagination, and must return the not evaluated outcome of section 7.6 for the portion it did not evaluate rather than truncating silently.

### 4.4 What a caller may assume

**P1-4.16 (MUST) Read your writes within a stream.** Following a successful recording operation on a stream, an implementation must reflect the written rows in any subsequent read of a projection parameterised by that stream at a knowledge time at or after the write.

**P1-4.17 (MUST NOT) No cross stream ordering promise.** An implementation must not represent that rows written to different streams are visible in a single global order, unless it declares a global ordering guarantee and meets it.

**P1-4.18 (MUST) Stability of resolved results.** A resolution performed with a fixed application time and a fixed knowledge time must return the same result on every subsequent evaluation, for as long as the rows involved are retained.

**P1-4.19 (MUST) Disclosure of the write on resolve.** An implementation must document that `resolve` writes a resolution row, and must not offer a resolution read that does not write one, because an unrecorded resolution cannot be reconstructed.

**P1-4.20 (MAY) Non recording preview.** An implementation may offer a preview read that does not write a resolution row, provided it is named distinctly, its result must not be relied upon in a determination, and it is not reachable through the `resolve` operation.

**P1-4.21 (MUST) No caller inference of absence.** An implementation must return a named non result for every condition in which it returns no version, and must not return an empty result set from which the caller would have to infer which condition applied.

### 4.5 What this component reads from others

| Read | From | Purpose | Behaviour when unavailable |
|---|---|---|---|
| Classification scheme version | `Part 10` | Validate a classification assignment | Reject the assignment with the outcome of section 7.6; do not assign against an unverified scheme |
| Reference set membership for `SCOPE` | `Part 10` | Validate an effectivity scope | Reject the assertion |
| Content schema identity | `Part 9` | Record the schema a structured rendition claims to conform to | Record the claim as unverified; do not validate |
| Authorisation decision | `Part 7` | Obtain the `AUTHREF` for an operation requiring authority | Reject the operation; do not proceed unauthorised |
| Actor identity attributes | External | Populate printed name and distinguish natural persons | Reject a signature; permit a read |
| Content octets | `Part 11` | Serve `fetch_content` and fixity checks | Return the transient unavailability outcome of section 7.7 |
| Trusted time stamp | External | Bind signing time | Record the signature without a token where the method permits it |

**P1-4.22 (MUST) No assignment against an unresolvable scheme.** An implementation must not record a classification assignment or a scoped effectivity assertion whose scheme or reference set version it could not resolve.

**P1-4.23 (MUST NOT) No local copy as authority.** An implementation may cache a classification scheme version or reference set for availability, but must not treat its cache as authoritative for whether a value exists, and must record with the assignment the version it validated against.

**P1-4.24 (MUST) Degrade to refusal, not to assumption.** Where a read from another component required by section 4.5 is unavailable, an implementation must refuse the operation with the outcome named in the table and must not proceed on an assumed value.

### 4.6 Synchronous against asynchronous

**P1-4.25 (MUST) Recording operations are synchronous in effect.** An implementation must not report a recording operation as accepted before the rows are durable, and must not use an asynchronous acknowledgement that leaves the caller unable to determine whether the rows exist.

**P1-4.26 (MAY) Asynchronous projection materialisation.** An implementation may materialise projections asynchronously, subject to clause P1-3.112 and clause P1-4.16.

**P1-4.27 (MUST) Long running operations are decomposed.** Where an operation cannot complete synchronously, such as the destruction of a large volume of content, an implementation must record the authorisation synchronously and the execution as a separate recorded act, and must expose the interval between them as a distinct state.

### 4.7 Events emitted

Events carry the envelope below. The envelope is normative by clause P1-4.28. CloudEvents version 1.0 is a suitable carrier and is named as an example, not as a requirement.

| Envelope field | Type | Required | Absence means |
|---|---|---|---|
| `event_id` | `ID` | yes | absence not permitted |
| `event_type` | `ENUM` per section 9.12 | yes | absence not permitted |
| `subject` | `URN` | yes | absence not permitted |
| `occurrence_otime` | `OTIME` | yes | absence not permitted |
| `record_ktime` | `KTIME` | yes | absence not permitted |
| `stream` and `seq` | `TEXT`, `SEQ` | yes | absence not permitted |
| `actor` | `ACTOR` | yes | absence not permitted |
| `causation_id` | `ID` | no | the event was not caused by another recorded event |
| `correlation_id` | `ID` | no | the event does not belong to a correlated set |
| `schema_ref` | `URN` | yes | absence not permitted |
| `payload_digest` | `DIGEST` | yes | absence not permitted |

The minimum event set is: lineage registered; version created; status transitioned; approval recorded; effectivity asserted; effectivity retracted; version superseded; version withdrawn; lineage obsolete; record declared; correcting record declared; preservation event recorded; metadata asserted; classification assigned; retention applied; hold applied; hold released; disposition authorised; disposition executed; tombstone created; copy issued; copy disposed; review due; review outcome recorded; citation fixed; citation resolution diverged; fixity mismatch detected; fixity indeterminate.

**P1-4.28 (MUST) Event envelope.** Every event an implementation emits under this part must carry every field marked required in the table of section 4.7.

**P1-4.29 (MUST) Event set coverage.** An implementation must emit an event for every member of the minimum event set of section 4.7.

**P1-4.30 (MUST) Events are derived, not authoritative.** An implementation must be able to regenerate every event from the recorded rows, and must not hold in an event any fact absent from the rows.

**P1-4.31 (MUST) Divergence event.** An implementation must emit the citation resolution divergence event whenever clause P1-3.101 sets the divergence flag, whether the divergence was detected during a caller initiated resolution or during a scheduled re resolution.

**P1-4.32 (SHOULD) Scheduled re resolution.** An implementation should re resolve recorded as of citations on a declared schedule so that divergence is detected without waiting for a reader, and should declare the schedule and the selection basis.

**P1-4.33 (MUST NOT) No event without a row.** An implementation must not emit an event for which no fact or assertion row exists.
## 5. State model

### 5.1 Two state models, deliberately separated

The most common structural error in a document component is a single status field that mixes two independent things: the position of a version in its authoring and approval lifecycle, and whether it currently governs. They are independent because a version can be approved and not yet in force, approved and never brought into force, in force and never approved because it was corrected into force, and no longer in force while remaining approved. A single enumeration cannot represent those combinations without inventing values that mean two things at once.

This part therefore specifies two models.

**Lifecycle status** is a state machine over the version, advanced only by recorded status transitions. It answers what has been done to the version.

**Force state** is a classification derived from effectivity assertions together with an application time and a knowledge time. It answers whether the version governed at a given moment, as believed at a given moment. It is not a state machine, it has no transitions, and no act advances it.

The two are related by preconditions, not by derivation: a transition to `RELEASED` requires an approval, and an effectivity assertion requires a version whose status is `RELEASED` or, exceptionally, a correction under clause P1-5.14. Beyond that they are independent, and clause P1-5.2 forbids collapsing them.

**P1-5.1 (MUST) Two models.** An implementation must represent lifecycle status and force state separately, and must be able to report both for any version.

**P1-5.2 (MUST NOT) No single status field.** An implementation must not represent force state as a value of the lifecycle status enumeration, and must not represent lifecycle status as a function of effectivity.

**P1-5.3 (MUST NOT) No time driven lifecycle transitions.** An implementation must not advance lifecycle status by the passage of time.

### 5.2 Lifecycle status values

The set is closed by this part. Extension requires a new version of this part; the reason is given in section 9.1.

| Status | Meaning | Terminal |
|---|---|---|
| `DRAFT` | Authored, not submitted | no |
| `IN_REVIEW` | Submitted, decision pending | no |
| `REJECTED` | Review decided against the version | yes |
| `APPROVED` | Approved, not yet released for effectivity | no |
| `RELEASED` | Eligible to be asserted in force | no |
| `SUPERSEDED` | Ceased to be in force because a successor took force | no |
| `WITHDRAWN` | Ceased to be in force with no successor | no |
| `CANCELLED` | Abandoned before review concluded | yes |
| `VOID` | Recorded in error and disavowed as an entity | yes |

`SUPERSEDED` and `WITHDRAWN` are not terminal. A reinstatement is a real event in every organisation that keeps documents, and forbidding it drives implementers to reissue identical content as a new version, which destroys the fact that the same text governs again and makes the citation history harder to read rather than easier. Permitting a transition back to `RELEASED` is safe because effectivity intervals remain disjoint, so the uniqueness invariant of clause P1-3.44 is untouched.

### 5.3 Version transition table

The table is normative by clause P1-5.4. "Just." indicates that reason text is required.

| From | To | Trigger | Authoriser | Signed | Just. | Preconditions |
|---|---|---|---|---|---|---|
| null | `DRAFT` | `create_version` | author | no | no | lineage exists, kind is `DOCUMENT`, `COMPILATION` or `REGISTRY` |
| `DRAFT` | `DRAFT` | `create_version` of a further draft state | author | no | no | none; a new draft is a new version, not a transition, and this row exists only to state that |
| `DRAFT` | `IN_REVIEW` | `submit_for_review` | author or custodian | no | no | mandatory core metadata complete |
| `DRAFT` | `CANCELLED` | `record_review_decision` | custodian | no | yes | none |
| `IN_REVIEW` | `APPROVED` | `approve` | approver in a named role | yes | no | core metadata complete; digest matches |
| `IN_REVIEW` | `REJECTED` | `record_review_decision` | approver in a named role | yes | yes | none |
| `IN_REVIEW` | `DRAFT` | `record_review_decision` | approver in a named role | yes | yes | none |
| `IN_REVIEW` | `CANCELLED` | `record_review_decision` | custodian | yes | yes | none |
| `APPROVED` | `RELEASED` | `release` | custodian | no | no | approval exists and is unretracted |
| `APPROVED` | `WITHDRAWN` | `withdraw` | authority per policy | yes | yes | no effectivity assertion exists |
| `RELEASED` | `SUPERSEDED` | `supersede` | authority per policy | no | yes | successor version is `RELEASED` and has an effectivity assertion beginning at the instant this version's interval ends |
| `RELEASED` | `WITHDRAWN` | `withdraw` | authority per policy | yes | yes | none |
| `SUPERSEDED` | `RELEASED` | `reinstate` | authority per policy | yes | yes | no effectivity overlap results |
| `WITHDRAWN` | `RELEASED` | `reinstate` | authority per policy | yes | yes | no effectivity overlap results |
| any | `VOID` | `void_entity` | authority per policy | yes | yes | the version was recorded in error; every effectivity assertion for it is retracted first |

**P1-5.4 (MUST) Transition legality.** An implementation must permit only the transitions in the table of section 5.3, and must reject any other transition with the outcome of section 7.6.

**P1-5.5 (MUST) Signature and justification requirements.** An implementation must enforce the signature and justification requirements of the table of section 5.3.

**P1-5.6 (MUST) Preconditions enforced at write.** An implementation must evaluate the preconditions of the table of section 5.3 against the state projected at the knowledge time of the operation, and must not defer them.

**P1-5.7 (MUST) Void requires prior retraction.** An implementation must reject a transition to `VOID` for a version that has any unretracted effectivity assertion.

**P1-5.8 (MUST NOT) No content in a void version.** An implementation must apply the disposition mechanism of section 3.12 rather than the `VOID` transition where the intent is to remove content, because `VOID` disavows the entity and retains the content.

**P1-5.9 (MUST) Reinstatement records a new assertion.** An implementation must effect a reinstatement by a new effectivity assertion, and must not achieve it by retracting the retraction or the supersession that ended the earlier interval.

### 5.4 Force state classification

Force state is computed for a version given a scope, an application time and a knowledge time. The values are closed by this part.

| Force state | Condition |
|---|---|
| `IN_FORCE` | An unretracted assertion visible at the knowledge time covers the application time for the scope |
| `NOT_YET_IN_FORCE` | Every visible assertion for the version begins after the application time |
| `NO_LONGER_IN_FORCE` | Every visible assertion for the version ends at or before the application time |
| `IN_FORCE_ELSEWHERE` | No visible assertion covers the application time in the requested scope, and one does in another scope |
| `NEVER_IN_FORCE` | No unretracted assertion for the version is visible at the knowledge time |
| `INDETERMINATE` | More than one version of the lineage is in force for the scope at the application time, so no single version's state can be stated |

**P1-5.10 (MUST) Force state values.** An implementation must classify force state using exactly the values of the table of section 5.4 and must not add values without registering them under section 9.

**P1-5.11 (MUST) Force state is parameterised.** An implementation must not report a force state without stating the scope, application time and knowledge time used.

**P1-5.12 (MUST NOT) No collapse of never and no longer.** An implementation must distinguish `NEVER_IN_FORCE` from `NO_LONGER_IN_FORCE`, because a version that was approved and never brought into force has a different evidential meaning from one that governed and was superseded.

**P1-5.13 (MUST) Indeterminate is reported, not resolved.** An implementation must report `INDETERMINATE` where the condition in the table of section 5.4 holds, and must not select a version.

**P1-5.14 (MAY) Effectivity by correction without release.** An implementation may accept an effectivity assertion with `basis` of `CORRECTION` for a version whose status is not `RELEASED`, and must in that case require an authority, reason text, and a signature, because the case arises when an organisation discovers that a version has been relied upon in practice without having been released, and refusing to record that fact does not make it untrue.

### 5.5 Lineage lifecycle

| Status | Meaning | Terminal |
|---|---|---|
| `ACTIVE` | New versions may be created | no |
| `CLOSED` | No new versions; existing versions may remain in force | no |
| `OBSOLETE` | The activity governed has ended; no version is in force and none will be | yes |

| From | To | Trigger | Signed | Just. | Preconditions |
|---|---|---|---|---|---|
| null | `ACTIVE` | `register_lineage` | no | no | none |
| `ACTIVE` | `CLOSED` | `close_lineage` | no | yes | none |
| `CLOSED` | `ACTIVE` | `reopen_lineage` | yes | yes | lineage is not `OBSOLETE` |
| `ACTIVE` | `OBSOLETE` | `declare_obsolete` | yes | yes | no version in force at the current application time |
| `CLOSED` | `OBSOLETE` | `declare_obsolete` | yes | yes | as above |

**P1-5.15 (MUST) Obsolescence is terminal.** An implementation must treat `OBSOLETE` as terminal for a lineage and must reject the creation of a further version of an obsolete lineage.

**P1-5.16 (MUST) Obsolescence does not dispose.** An implementation must retain every version, record and assertion of an obsolete lineage subject to its retention rules, and must not treat obsolescence as a disposition trigger unless a retention application names `OBSOLETE` as its trigger type.

**P1-5.17 (MUST) Obsolescence and withdrawal are distinct.** An implementation must not represent obsolescence of a lineage by withdrawing its versions alone, nor withdrawal of a version by declaring the lineage obsolete.

### 5.6 Record lifecycle

| Status | Meaning | Terminal |
|---|---|---|
| `CAPTURED` | Content is held pending declaration; still mutable | no |
| `ABANDONED` | Captured content will not be declared | yes |
| `DECLARED` | Content is a record and is immutable | no |
| `DISPOSITION_AUTHORISED` | Destruction or transfer has been authorised and not yet executed | no |
| `DESTROYED` | Content octets destroyed; tombstone retained | yes |
| `TRANSFERRED` | Custody transferred to a named receiving party; tombstone retained | yes |
| `VOID` | Declared in error and disavowed as an entity | yes |

| From | To | Trigger | Signed | Just. | Preconditions |
|---|---|---|---|---|---|
| null | `CAPTURED` | `capture` | no | no | lineage kind is `RECORD` |
| `CAPTURED` | `DECLARED` | `declare_record` | yes | no | digest computed; aggregation membership asserted |
| `CAPTURED` | `ABANDONED` | `abandon_capture` | no | yes | none |
| `DECLARED` | `DISPOSITION_AUTHORISED` | `authorise_disposition` | yes | yes | retention elapsed; no unreleased hold |
| `DISPOSITION_AUTHORISED` | `DESTROYED` | `execute_disposition` | no | no | authorisation unretracted |
| `DISPOSITION_AUTHORISED` | `TRANSFERRED` | `execute_disposition` | no | no | receiving party recorded |
| `DISPOSITION_AUTHORISED` | `DECLARED` | `retract_assertion` on the authorisation | yes | yes | not yet executed |
| `DECLARED` | `VOID` | `void_entity` | yes | yes | see clause P1-5.19 |

**P1-5.18 (MUST) Capture window is bounded.** An implementation must declare a maximum period for which content may remain `CAPTURED`, and must report captures exceeding it.

**P1-5.19 (MUST) Void of a record is exceptional.** An implementation must permit the voiding of a declared record only where the declaration itself was an error of identity, must require a signature and reason text, must retain the content and every digest, and must not use voiding to correct the content of a record, for which clause P1-3.68 applies.

**P1-5.20 (MUST) Transfer records the receiving party.** An implementation must record the receiving party, the transfer instrument and the digests transferred for every transition to `TRANSFERRED`.

**P1-5.21 (MUST NOT) No return from destroyed.** An implementation must treat `DESTROYED` as terminal and must not permit any transition out of it, including on the discovery that the destruction was unauthorised, which must be recorded as an annotation against the tombstone.

### 5.7 Copy lifecycle and holds

| Status | Meaning | Terminal |
|---|---|---|
| `ISSUED` | Outstanding with the recipient | no |
| `RETURNED`, `DESTROYED`, `SUPERSEDED`, `LOST` | The outcome recorded for the copy | yes |

**P1-5.22 (MUST) Copy outcome recorded.** An implementation must record an outcome for every controlled copy of a version that ceases to be in force, including `LOST` where no other outcome can be established.

**P1-5.23 (MUST NOT) Holds are not states.** An implementation must not represent a hold as a value in any state enumeration of this section, and must evaluate holds as an overlay that gates the transitions to `DISPOSITION_AUTHORISED`.

**P1-5.24 (MUST) Hold does not gate review.** An implementation must not prevent a review, a supersession, a withdrawal or the creation of a further version because a hold is in place, because a hold suspends disposition only.
## 6. Execution semantics

### 6.1 Determinism

**P1-6.1 (MUST) Deterministic resolution.** Given the same recorded rows and the same parameters, resolution must produce the same outcome and the same basis, on every evaluation and on every conforming implementation.

**P1-6.2 (MUST NOT) No dependence on wall clock in parameterised evaluation.** An implementation must not allow the result of a resolution whose application time and knowledge time are both supplied to depend on the time at which the resolution is performed.

**P1-6.3 (MUST) Deterministic ordering of equal timestamps.** Where two rows in a stream carry the same `KTIME`, an implementation must order them by `SEQ`, and where `SEQ` is also equal it must reject the second row rather than adopt an arbitrary order.

**P1-6.4 (MUST) Declared collation.** Where an implementation compares text values in evaluating any rule of this part, it must declare the collation used, because a comparison whose collation is undeclared is not deterministic across environments.

### 6.2 Resolution of an as of citation

This is the mechanism required by clause P1-1.1. It is stated as an algorithm because a prose description of it is not testable.

Inputs are a lineage `L`, a scope `S`, an application time `Ta`, and a knowledge time `Tk`. `A` denotes the set of effectivity assertions and `R` the set of retractions.

```
visible(a, Tk)  :=  a.asserted_ktime <= Tk
                    and there is no r in R such that
                        r.target_assertion_id = a.assertion_id
                        and r.ktime <= Tk

covers(a, Ta)   :=  a.effective_from <= Ta
                    and (a.effective_to is absent or Ta < a.effective_to)

candidates(L, S, Ta, Tk) :=
    { a in A : a.lineage_id = L
               and a.scope = S
               and visible(a, Tk)
               and covers(a, Ta) }

resolve(L, S, Ta, Tk):
    C := candidates(L, S, Ta, Tk)
    if |C| = 1:
        a := the element of C
        if status_projection(a.version_id, Tk) = VOID:
            return RESOLVED_VOIDED_VERSION with a.version_id and the void transition
        return RESOLVED with a.version_id, basis {a.assertion_id}
    if |C| > 1:
        return AMBIGUOUS_MULTIPLE_IN_FORCE with the identifiers of every member of C
    if |C| = 0:
        if L is unknown:
            return UNKNOWN_LINEAGE
        if L is scoped and S was not supplied:
            return SCOPE_REQUIRED
        if candidates(L, S', Ta, Tk) is non empty for some scope S' /= S:
            return NOT_IN_FORCE_IN_SCOPE with the scopes in which a version is in force
        if some a in A with a.lineage_id = L is visible at Tk:
            return NOT_IN_FORCE_AT_TIME with the nearest preceding and following intervals
        if some a in A with a.lineage_id = L exists but none is visible at Tk:
            return NO_EFFECTIVITY_KNOWN_AT_KTIME
        return NEVER_EFFECTIVE
```

Every branch returns a named outcome. There is no branch that returns nothing, and no branch that chooses among candidates. Section 7.4 defines each outcome and what a caller must do with it.

**P1-6.5 (MUST) Resolution algorithm.** An implementation must implement resolution of an as of citation so that its outcome is identical to that of the algorithm of section 6.2 for every input.

**P1-6.6 (MUST) Basis returned.** An implementation must return, with a resolved outcome, the identifier of every assertion relied upon, so that the resolution can be checked without re running it.

**P1-6.7 (MUST) Distinguish the two empty cases.** An implementation must distinguish `NOT_IN_FORCE_AT_TIME`, which states that the lineage had a known effectivity history that does not cover the application time, from `NO_EFFECTIVITY_KNOWN_AT_KTIME`, which states that at the knowledge time asked about, the component did not yet know of any effectivity for the lineage.

**P1-6.8 (MUST) Voided version still resolves.** An implementation must return the version and the void transition for a resolution that lands on a version later voided, and must not report the resolution as unresolved.

**P1-6.9 (MUST NOT) No nearest neighbour resolution.** An implementation must not return an adjacent version when no assertion covers the application time, and may return the adjacent intervals only as diagnostic detail alongside the `NOT_IN_FORCE_AT_TIME` outcome.

**P1-6.10 (MUST) Knowledge time bounds retractions as well as assertions.** An implementation must apply the knowledge time bound to retractions as well as to assertions, so that a resolution at a past knowledge time is unaffected by a later retraction.

### 6.3 Resolution of a pinned citation

```
resolve_pinned(V, D):
    if V is unknown:                       return UNKNOWN_VERSION
    if content octets are unavailable:
        if a tombstone exists for V:       return CONTENT_DISPOSED with the tombstone
        else:                              return CONTENT_UNAVAILABLE_TRANSIENT
    if the recorded digest of V's authoritative rendition /= D:
        return DIGEST_MISMATCH_WITH_CITATION
    recompute the digest over the canonical octets
    if recomputation is not possible:      return INTEGRITY_INDETERMINATE with the reason
    if recomputed /= recorded:             return INTEGRITY_FAILED
    return RESOLVED with V
```

**P1-6.11 (MUST) Pinned resolution algorithm.** An implementation must implement resolution of a pinned citation so that its outcome is identical to that of the algorithm of section 6.3 for every input.

**P1-6.12 (MUST) Two distinct digest failures.** An implementation must distinguish the case in which the digest carried by the citation differs from the digest recorded for the version, which indicates that the citing party recorded a different content, from the case in which the recomputed digest differs from the recorded digest, which indicates that the stored content has changed.

**P1-6.13 (MUST NOT) No effectivity in pinned resolution.** An implementation must not consider effectivity assertions in resolving a pinned citation, and must not report a pinned citation as unresolved because the version was not in force.

**P1-6.14 (SHOULD) Force state as advice on pinned resolution.** An implementation should return, alongside a resolved pinned citation, the force state of the version at the citation's `fixed_ktime`, as advisory detail, because a pinned citation to a version that was not in force is often an error worth surfacing and is never a reason to fail the resolution.

### 6.4 Locator resolution

```
resolve_locator(V, scheme, expr):
    if scheme is not registered:                 return LOCATOR_SCHEME_UNKNOWN
    if the authoritative rendition of V is not addressable in scheme:
        return LOCATOR_NOT_ADDRESSABLE
    if expr matches exactly one unit in V:       return RESOLVED with the unit
    if expr matches more than one unit:          return LOCATOR_AMBIGUOUS
    if scheme is CLAUSE_ID and expr is a clause identifier known to the lineage:
        if the unit is absent from V but present in an earlier version:
            return LOCATOR_RETIRED with the last version containing it
        if the unit was moved and the lineage records a successor identifier:
            return LOCATOR_MOVED with the successor
    return LOCATOR_UNRESOLVABLE
```

**P1-6.15 (MUST) Locator resolution algorithm.** An implementation must implement locator resolution so that its outcome is identical to that of the algorithm of section 6.4 for every input.

**P1-6.16 (MUST) Retired is not unresolvable.** An implementation must return `LOCATOR_RETIRED` with the last version containing the unit rather than `LOCATOR_UNRESOLVABLE` where the clause identifier is known to the lineage.

**P1-6.17 (MUST NOT) No partial match.** An implementation must not return a nearest or containing unit for an expression that does not match exactly, and must return `LOCATOR_UNRESOLVABLE`.

### 6.5 Idempotence and concurrency

**P1-6.18 (MUST) Idempotent recording.** A recording operation replayed with the same idempotency key within the declared window must produce no additional rows and must return the original outcome.

**P1-6.19 (MUST) Idempotency keys are scoped to the operation and the subject.** An implementation must treat an idempotency key as applying to the combination of operation kind, subject and key, and must reject a key reused across different operations or subjects.

**P1-6.20 (MUST) Optimistic concurrency on the stream.** An implementation must reject a recording operation whose supplied expected sequence does not equal the current sequence of the stream, and must return the outcome of section 7.6 naming the observed sequence.

**P1-6.21 (MUST NOT) No last writer wins.** An implementation must not resolve a concurrent write conflict by accepting the later write, and must return the conflict to the caller.

**P1-6.22 (MUST) Retraction under concurrency.** An implementation must reject a retraction whose target has been retracted by another writer, and must not record a second retraction of the same target.

**P1-6.23 (MUST) Repeated invocation without a key is not idempotent.** An implementation must treat a recording operation submitted without an idempotency key as a distinct act, must record it, and must not silently deduplicate it by comparing field values, because two genuinely repeated acts are indistinguishable from a retry by content alone and suppressing one would lose a real event.

**P1-6.24 (SHOULD) Natural key constraints.** An implementation should additionally enforce a uniqueness constraint on the natural key of each assertion kind, such as lineage, scope and interval start for an effectivity assertion, so that a duplicate submitted outside the deduplication window is rejected rather than creating an ambiguity for readers to discover later.

### 6.6 Clocks, ordering and late arrival

**P1-6.25 (MUST) Knowledge time is assigned, never accepted.** An implementation must assign every `KTIME` itself and must reject an operation that supplies one.

**P1-6.26 (MUST) Occurrence time is accepted, never assigned.** An implementation must accept `OTIME` from the caller where the act occurred outside the component, must not substitute its own clock for it, and must record the absence of a supplied `OTIME` as the default stated in the field table rather than as the current time.

**P1-6.27 (MUST) Late arrival is representable.** An implementation must accept a row whose `OTIME` precedes the `KTIME` of rows already written, must not reorder the stream to accommodate it, and must not reject it for being late unless it exceeds a declared limit.

**P1-6.28 (MUST) Declared late arrival limit.** An implementation must declare the maximum interval by which an `OTIME` may precede its `KTIME`, and must report a row exceeding it as requiring authority rather than rejecting it silently.

**P1-6.29 (MUST) Monotonic sequence.** An implementation must assign `SEQ` monotonically within a stream and must not reuse a value within a stream.

**P1-6.30 (MUST NOT) No renumbering of sequences.** An implementation must not renumber, compact or reassign `SEQ` values.

**P1-6.31 (MUST) UTC and offsets.** An implementation must store `KTIME` in UTC, must retain the offset as supplied for `ATIME` and `OTIME`, and must not normalise away an offset, because the local time of an act is part of what was recorded.

**P1-6.32 (SHOULD) Declared leap second handling.** An implementation should declare how it handles leap seconds and clock adjustments, because a repeated or skipped second inside a stream is a source of non monotonic timestamps and therefore of unorderable rows.

### 6.7 Evaluation order for gating conditions

Where several conditions gate an operation, the order of evaluation is observable, because the outcome returned tells the caller which condition failed. Undeclared order produces implementations that disagree about which outcome to return for the same input.

**P1-6.33 (MUST) Declared gating order.** An implementation must evaluate the gating conditions of a recording operation in the order: existence of the subject, authorisation, lifecycle legality, precondition on state, invariant preservation, and must return the outcome for the first condition that fails.

**P1-6.34 (MUST) Invariant preservation is evaluated last.** An implementation must evaluate the effectivity uniqueness invariant of clause P1-3.44 after all other gating conditions, so that an unauthorised operation is reported as unauthorised rather than as an overlap.

**P1-6.35 (MUST) Disposition gating order.** An implementation must evaluate disposition eligibility in the order: retention elapsed, holds released, authorisation present, citation count computed, and must record the citation count whether or not the disposition proceeds.
## 7. Outcome and failure taxonomy

### 7.1 Why the taxonomy is the specification

Most of the failures this component can cause are not faults. They are correct answers that a caller was not prepared to receive, and which the caller therefore converts into something false. The document was not in force at that time, and the caller records that no document applied. Access was withheld, and the caller records that nothing exists. The content was destroyed under authorised disposition, and the caller records that the citation was broken. Integrity could not be assessed, and the caller records that integrity failed.

In each case the component answered correctly and the composed system produced a falsehood. That is why this section enumerates every value an operation can return and states, for each, what the caller is obliged to do. The obligations are stated here because they belong to this component's contract; how a caller that has no representation for a given value must behave is a composition question and belongs to `Part 0`.

### 7.2 Outcome classes

| Class | Meaning | Is it a failure of the component |
|---|---|---|
| `SUCCESS` | The operation produced the value it exists to produce | no |
| `NON_RESULT` | The operation completed correctly and the correct answer is not a value | no |
| `REFUSAL` | The operation was not performed because a condition of performing it was not met | no |
| `FAULT` | The operation could not be completed because the component or a dependency failed | yes |
| `DEFECT` | The operation revealed that a recorded invariant of this part does not hold | yes, and of the record rather than of the operation |

The `NON_RESULT` class has five subclasses, which exist because collapsing them is the failure described in section 7.1: `NOT_APPLICABLE`, `NOT_IN_FORCE`, `NOT_EVALUATED`, `UNDECIDABLE` and `WITHHELD`.

**P1-7.1 (MUST) Every outcome is classified.** An implementation must assign every outcome it can return to exactly one class of the table of section 7.2, and must publish the assignment.

**P1-7.2 (MUST NOT) No non result as failure.** An implementation must not return an outcome of class `NON_RESULT` through a mechanism that a caller conventionally reads as failure, and specifically must not signal it by an error status alone with no distinguishing code.

**P1-7.3 (MUST NOT) No fault as non result.** An implementation must not report a `FAULT` as a `NON_RESULT`, and specifically must not report the unavailability of a dependency as an absence of data.

**P1-7.4 (MUST) Defect is recorded and raised.** An implementation must record every `DEFECT` outcome as a fact row and must raise the signal required by section 8.5, in addition to returning it.

**P1-7.5 (MUST NOT) No repair on read.** An implementation must not attempt to repair the condition underlying a `DEFECT` outcome as part of serving the read that revealed it.

### 7.3 Outcome envelope

| Field | Type | Required | Absence means |
|---|---|---|---|
| `outcome_code` | `ENUM` per sections 7.4 to 7.8 | yes | absence not permitted |
| `outcome_class` | `ENUM` per section 7.2 | yes | absence not permitted |
| `subject` | `URN` | yes | absence not permitted |
| `parameters_echo` | structure | yes | absence not permitted; the application time, knowledge time and scope used |
| `basis` | `ID` list | no | no recorded row was relied upon |
| `detail` | `TEXT` | no | no further detail is available |
| `retryable` | `BOOL` | yes | absence not permitted |
| `recorded_row_id` | `ID` | no | the outcome was not recorded, permitted only for outcomes that section 7.9 does not require to be recorded |

**P1-7.6 (MUST) Envelope on every outcome.** An implementation must return every field marked required in the table of section 7.3 with every outcome, including successful ones.

**P1-7.7 (MUST) Parameters echoed.** An implementation must echo the application time, knowledge time and scope actually used, including any value it defaulted, so that a caller can detect that it received an answer to a different question from the one it asked.

**P1-7.8 (SHOULD) Problem details carrier.** Where an implementation exposes outcomes over HTTP, it should carry them in the problem details format of RFC 9457 with the `outcome_code` as the problem type, because the alternative in practice is a numeric status code that erases the distinction between the five classes.

### 7.4 Resolution outcomes for an as of citation

| Code | Class | Meaning | Retryable | Caller obligation |
|---|---|---|---|---|
| `RESOLVED` | `SUCCESS` | Exactly one version was in force | n/a | Record the version and the basis |
| `RESOLVED_VOIDED_VERSION` | `SUCCESS` | The version in force has since been voided | n/a | Record both the version and the void, and treat any determination made on it as requiring review |
| `NOT_IN_FORCE_AT_TIME` | `NON_RESULT`, `NOT_IN_FORCE` | The lineage had a known effectivity history that does not cover the application time | no | Record that no version governed; must not substitute an adjacent version |
| `NOT_IN_FORCE_IN_SCOPE` | `NON_RESULT`, `NOT_IN_FORCE` | A version was in force in another scope but not the requested one | no | Record the scope mismatch; must not adopt the other scope's version |
| `NEVER_EFFECTIVE` | `NON_RESULT`, `NOT_APPLICABLE` | The lineage has never had any effectivity assertion | no | Record that the lineage is not a governing instrument |
| `NO_EFFECTIVITY_KNOWN_AT_KTIME` | `NON_RESULT`, `UNDECIDABLE` | At the knowledge time asked about, nothing was yet known of the lineage's effectivity | no | Record that the question is not answerable as of that knowledge time, and consider asking at a later one |
| `SCOPE_REQUIRED` | `REFUSAL` | The lineage is scoped and no scope was supplied | yes, with a scope | Supply a scope; must not retry with `GLOBAL` unless `GLOBAL` is the intended scope |
| `UNKNOWN_LINEAGE` | `NON_RESULT`, `NOT_APPLICABLE` | No such lineage is known | no | Record the reference as unresolvable; must not create the lineage |
| `AMBIGUOUS_MULTIPLE_IN_FORCE` | `DEFECT` | More than one version was in force | no | Halt the determination; must not select among the candidates |
| `HISTORY_NOT_RETAINED` | `NON_RESULT`, `UNDECIDABLE` | The knowledge time requested precedes the retained history | no | Record that the belief at that time is unrecoverable |
| `KTIME_IN_FUTURE` | `REFUSAL` | The knowledge time supplied is later than the present | yes | Correct the parameter |
| `ACCESS_WITHHELD` | `NON_RESULT`, `WITHHELD` | The caller is not entitled to the result | no | Record that a result exists and was withheld; must not record absence |
| `EXISTENCE_NOT_DISCLOSED` | `NON_RESULT`, `WITHHELD` | The caller is not entitled to know whether a result exists | no | Record that the question was not answered; must not record absence |
| `NOT_EVALUATED` | `NON_RESULT`, `NOT_EVALUATED` | The resolution was not attempted, as for the unevaluated remainder of a paginated or budgeted request | yes | Re request the unevaluated portion; must not treat it as resolved or as absent |
| `SCOPE_UNINTERPRETABLE` | `NON_RESULT`, `UNDECIDABLE` | The reference set version defining the scope is no longer resolvable | no | Record that the scope cannot be interpreted |
| `RESOLUTION_FAULT` | `FAULT` | The component could not complete the resolution | yes | Retry; must not record any resolution |

**P1-7.9 (MUST) Outcome completeness.** An implementation must return one of the codes in the table of section 7.4 for every as of resolution, and must not return an outcome outside that set except a code registered under section 9.13.

**P1-7.10 (MUST NOT) No collapsing of the four empty outcomes.** An implementation must not return the same code for `NOT_IN_FORCE_AT_TIME`, `NEVER_EFFECTIVE`, `NO_EFFECTIVITY_KNOWN_AT_KTIME` and `UNKNOWN_LINEAGE`.

**P1-7.11 (MUST NOT) No withheld as absent.** An implementation must not return `UNKNOWN_LINEAGE` for a subject that exists but is withheld from the caller.

**P1-7.12 (MUST) Existence non disclosure is explicit and configured.** An implementation must return `EXISTENCE_NOT_DISCLOSED` where policy requires that the existence of a subject not be revealed, must treat that behaviour as a declared configuration rather than a default, and must record the withheld response together with the identity of the subject in the audit record even though it is not disclosed to the caller.

**P1-7.13 (MUST) Ambiguity halts.** An implementation must return `AMBIGUOUS_MULTIPLE_IN_FORCE` as class `DEFECT` and must not return any version alongside it.

### 7.5 Locator outcomes

| Code | Class | Retryable | Caller obligation |
|---|---|---|---|
| `RESOLVED` | `SUCCESS` | n/a | Record the unit and the version it was found in |
| `LOCATOR_RETIRED` | `NON_RESULT`, `NOT_APPLICABLE` | no | Record that the cited unit no longer exists and the last version in which it did |
| `LOCATOR_MOVED` | `SUCCESS` | n/a | Record both the cited identifier and the successor; must not silently substitute |
| `LOCATOR_AMBIGUOUS` | `DEFECT` | no | Halt; the lineage has duplicate unit identifiers |
| `LOCATOR_NOT_ADDRESSABLE` | `NON_RESULT`, `NOT_APPLICABLE` | no | Record that the rendition cannot be addressed in that scheme |
| `LOCATOR_SCHEME_UNKNOWN` | `REFUSAL` | yes | Use a registered scheme |
| `LOCATOR_UNRESOLVABLE` | `NON_RESULT`, `NOT_APPLICABLE` | no | Record the citation as unresolvable at that granularity while retaining the version level resolution |

**P1-7.14 (MUST) Locator outcome independence.** An implementation must return the version level resolution outcome and the locator level outcome separately, and must not report a version as unresolved because its locator did not resolve.

**P1-7.15 (MUST NOT) No silent substitution on move.** An implementation must return both the cited identifier and its successor for `LOCATOR_MOVED` and must not return the successor alone.

**P1-7.16 (MUST) Locator outcomes name the version.** An implementation must return, with every locator outcome, the identifier of the version against which the locator was resolved, because a locator outcome is meaningless without the version it was evaluated against.

### 7.6 Recording operation outcomes

| Code | Class | Retryable | Notes |
|---|---|---|---|
| `RECORDED` | `SUCCESS` | n/a | Rows durable |
| `RECORDED_IDEMPOTENT_REPLAY` | `SUCCESS` | n/a | The original outcome is returned; no rows written |
| `SEQUENCE_CONFLICT` | `REFUSAL` | yes after re reading | Observed sequence returned |
| `PRECONDITION_STATE` | `REFUSAL` | no without a state change | Names the state observed and the state required |
| `TRANSITION_ILLEGAL` | `REFUSAL` | no | Names the transition attempted |
| `INVARIANT_WOULD_BREAK` | `REFUSAL` | no | Names the invariant and the conflicting rows |
| `AUTHORITY_MISSING` | `REFUSAL` | yes with authority | Must not be reported as a fault |
| `SIGNATURE_REQUIRED` | `REFUSAL` | yes with a signature | |
| `SIGNATURE_INVALID` | `REFUSAL` | no | Names which requirement of section 3.9 failed |
| `JUSTIFICATION_REQUIRED` | `REFUSAL` | yes with reason text | |
| `REFERENCE_UNRESOLVABLE` | `REFUSAL` | yes when the dependency returns | The scheme, reference set or schema could not be resolved |
| `DEPENDENCY_UNAVAILABLE` | `FAULT` | yes | Distinguished from the previous code, which is a determinate answer that the reference does not resolve |
| `IDEMPOTENCY_KEY_EXPIRED` | `REFUSAL` | no | Caller must decide whether the act is new |
| `NOT_EVALUATED` | `NON_RESULT`, `NOT_EVALUATED` | yes | The unevaluated remainder of a bulk submission |
| `WRITE_FAULT` | `FAULT` | yes | No rows written |

**P1-7.17 (MUST) Refusal is not fault.** An implementation must classify a missing authority, a missing signature, an illegal transition, an unmet precondition and an unresolvable reference as `REFUSAL` and must not report any of them as `FAULT`.

**P1-7.18 (MUST) Determinate non resolution against dependency failure.** An implementation must distinguish `REFERENCE_UNRESOLVABLE`, meaning the dependency answered and the reference does not exist, from `DEPENDENCY_UNAVAILABLE`, meaning the dependency did not answer.

**P1-7.19 (MUST) Named invariant on refusal.** An implementation must name the invariant and return the identifiers of the conflicting rows with `INVARIANT_WOULD_BREAK`.

**P1-7.20 (MUST NOT) No silent no operation.** An implementation must not return `RECORDED` for an operation that wrote no rows, other than an idempotent replay reported with its own code.

### 7.7 Content fetch outcomes

| Code | Class | Retryable | Caller obligation |
|---|---|---|---|
| `CONTENT_RETURNED` | `SUCCESS` | n/a | Record the digest of what was received and compare it |
| `CONTENT_DISPOSED` | `NON_RESULT`, `NOT_APPLICABLE` | no | Record the tombstone; must not record the citation as broken |
| `CONTENT_TRANSFERRED` | `NON_RESULT`, `NOT_APPLICABLE` | no | Record the receiving party from the tombstone and direct the request there |
| `CONTENT_UNAVAILABLE_TRANSIENT` | `FAULT` | yes | Retry; must not conclude that content does not exist |
| `CONTENT_WITHHELD` | `NON_RESULT`, `WITHHELD` | no | Record that content exists and was withheld |
| `INTEGRITY_FAILED` | `DEFECT` | no | Must not use the content in any determination |
| `INTEGRITY_INDETERMINATE_PROFILE` | `NON_RESULT`, `UNDECIDABLE` | no | Record that integrity could not be assessed and why; must not report tampering |
| `INTEGRITY_INDETERMINATE_ALGORITHM` | `NON_RESULT`, `UNDECIDABLE` | no | As above |
| `RENDITION_UNKNOWN` | `REFUSAL` | no | |

**P1-7.21 (MUST) Three integrity outcomes distinguished.** An implementation must distinguish `INTEGRITY_FAILED` from the two indeterminate integrity outcomes, and must not report an indeterminate assessment as a failure.

**P1-7.22 (MUST NOT) No content with a failed integrity outcome.** An implementation must not return content octets alongside `INTEGRITY_FAILED`, and must return the tombstone or metadata only.

**P1-7.23 (MAY) Content with an indeterminate outcome.** An implementation may return content octets alongside an indeterminate integrity outcome, and must in that case mark the response so that the caller cannot present the content as verified.

**P1-7.24 (MUST) Disposed against transient.** An implementation must distinguish content destroyed under authorised disposition from content that is temporarily unreachable, and must never report the former as the latter, because a caller that retries a disposed subject will retry forever and a caller that treats a transient failure as disposal will record a falsehood.

### 7.8 Outcomes required to be recorded

**P1-7.25 (MUST) Recording of resolution outcomes.** An implementation must record every outcome of an as of or pinned resolution performed through `resolve`, whatever its class.

**P1-7.26 (MUST) Recording of defects and withholdings.** An implementation must record every outcome of class `DEFECT` and every outcome in the `WITHHELD` subclass, including the identity of the subject withheld.

**P1-7.27 (MUST) Recording of refusals that alter no state.** An implementation must record refusals of the codes `AUTHORITY_MISSING`, `SIGNATURE_INVALID` and `INVARIANT_WOULD_BREAK`, because a pattern of them is evidence about the operation of the controls and is lost if only successes are recorded.

**P1-7.28 (MAY) Faults recorded outside the ledger.** An implementation may record outcomes of class `FAULT` in operational telemetry rather than as fact rows, and must not record a fault as an assertion about a subject.

**P1-7.29 (MUST NOT) No outcome invention.** An implementation must not return an outcome code that is neither in this section nor registered under section 9.13.

**P1-7.30 (MUST) Stability of outcome codes.** An implementation must not change the meaning of an outcome code it has published, and must register a new code instead.
## 8. Observability and the audit record

### 8.1 What the audit record is, in this model

In a component built on the model of section 3, the audit record is not a parallel log. The fact and assertion rows **are** the audit record, and the projections are the derived convenience. This section therefore specifies three things: the fields every row must carry so that it functions as an audit entry, the additional records needed for acts that write no domain rows, and the export that makes the whole readable without the component.

The requirement that an audit trail be computer generated, time stamped, independent of the operator, and such that previously recorded values are not obscured, follows 21 CFR 11.10(e). The requirement that it be available for review and copying by the regulator follows the same clause. These are cited as specification text and are adopted here for all subjects, not only regulated ones, because the properties they describe are the properties that make reconstruction possible.

**P1-8.1 (MUST) Rows are audit entries.** Every fact row and assertion row must carry the actor, the occurrence time, the knowledge time, the stream and sequence, and the reason or authority where the clause writing it requires one.

**P1-8.2 (MUST NOT) No separate mutable audit table.** An implementation must not maintain an audit trail as a secondary record of changes to a primary mutable record.

**P1-8.3 (MUST NOT) No obscuring of prior values.** An implementation must keep every superseded assertion readable, and must not present a corrected value in a way that conceals that a prior value existed.

**P1-8.4 (MUST) Audit trail cannot be disabled.** An implementation must not provide a mechanism by which the recording of fact and assertion rows can be suspended, and where an administrative capability exists that could have that effect, its exercise must itself be recorded as a fact row and must require an authority.

**P1-8.5 (MUST) Independence from the actor.** An implementation must derive the knowledge time, the sequence and the actor identity of a row from sources the acting party cannot set.

### 8.2 Additional audit records

Some acts write no domain row and must still be recorded.

| Act | Record | Fields beyond the envelope |
|---|---|---|
| Read of content | Access record | purpose, rendition, outcome, whether integrity was verified |
| Read of a projection for a determination | Access record | projection name, parameters, incorporated knowledge time |
| Withheld response | Withholding record | subject identity, policy reference, the code returned |
| Export of an evidence package | Export record | subject, package digest, recipient, purpose |
| Issue of an uncontrolled copy | Copy record with `control_state` `UNCONTROLLED` | markings applied |
| Administrative configuration change | Configuration record | the setting, the prior value, the authority |
| Projection rebuild | Rebuild record | projection name, range rebuilt, resulting incorporated knowledge time |
| Scheduled fixity run | Fixity records | selection basis, count checked, outcomes by code |

**P1-8.6 (MUST) Access recording for determinations.** An implementation must record every content fetch whose stated purpose is the making of a determination, including the outcome and whether integrity was verified.

**P1-8.7 (SHOULD) Access recording for all reads.** An implementation should record all content reads, and where it does not, must declare which reads it does not record and why, because an undeclared gap in access recording cannot be distinguished later from a read that did not happen.

**P1-8.8 (MUST) Withholding is recorded even when not disclosed.** An implementation must record the identity of a withheld subject in the withholding record even where the response to the caller does not disclose that the subject exists.

**P1-8.9 (MUST) Configuration is part of the record.** An implementation must record every change to a configuration value that this part requires it to declare, with the prior value, the new value, the actor and the authority.

**P1-8.10 (MUST) Rebuild is recorded.** An implementation must record every projection rebuild, because an unrecorded rebuild makes an unexplained change in a read result indistinguishable from a change in the underlying rows.

### 8.3 Grain

**P1-8.11 (MUST) One row per act.** An implementation must record one fact or assertion row per act, and must not aggregate several acts into one row.

**P1-8.12 (MUST NOT) No batching that loses attribution.** An implementation must record, for a bulk operation, the actor and occurrence time of each constituent act, and must not attribute all constituents to the batch.

**P1-8.13 (MUST) Causation chain.** An implementation must record, for every row it writes as a consequence of another recorded act, the identifier of the causing row.

**P1-8.14 (MUST) Correlation across a unit of work.** An implementation must accept and record a correlation identifier supplied by a caller, and must carry it on every row and event written in the course of that operation.

**P1-8.15 (SHOULD NOT) No sampling of the record.** An implementation should not sample, aggregate or downsample fact or assertion rows or the records of section 8.2, and where it samples operational telemetry it must not represent the sample as the audit record.

### 8.4 Access records

| Field | Type | Required | Absence means |
|---|---|---|---|
| `access_id` | `ID` | yes | absence not permitted |
| `subject_id` | `ID` | yes | absence not permitted |
| `actor` | `ACTOR` | yes | absence not permitted |
| `purpose` | `ENUM` per section 9.14 | yes | absence not permitted |
| `ktime` | `KTIME` | yes | absence not permitted |
| `outcome_code` | `ENUM` per section 7.7 | yes | absence not permitted |
| `authorisation_ref` | `AUTHREF` | yes | absence not permitted |
| `integrity_verified` | `BOOL` | yes | absence not permitted |
| `delivered_digest` | `DIGEST` | no | no octets were delivered |

**P1-8.16 (MUST) Delivered digest.** An implementation must record the digest of what it delivered on a successful content fetch, so that a later dispute about what a reader saw is decidable.

**P1-8.17 (MUST) Authorisation reference on every access.** An implementation must record the reference to the authorisation decision that permitted an access, and must not record an access as permitted without one.

### 8.5 Signals

A signal is an assertion by the component that something requires attention from a person. Signals are not the audit record and do not replace it; they exist because several outcomes in section 7 are conditions that nobody will discover by reading rows.

| Condition | Signal | Minimum content |
|---|---|---|
| Fixity mismatch | Integrity alarm | subject, digest, recomputed value, last successful check |
| Fixity indeterminate | Assessability alarm | subject, which of profile, algorithm or content was unavailable |
| Ambiguous effectivity | Invariant alarm | lineage, scope, application time, the conflicting assertions |
| Citation divergence | Divergence notice | citation, both resolutions, the retraction responsible |
| Review overdue | Review notice | lineage, review due date, custodian |
| Disposition due with outstanding citations | Disposition conflict notice | subject, citation count, citing entities |
| Controlled copies outstanding after a version ceases to be in force | Recall notice | version, copies, recipients |
| Capture window exceeded | Capture alarm | captured content, age |
| Retraction of an assertion relied upon by a recorded resolution | Divergence notice | as above |

**P1-8.18 (MUST) Signal on each condition.** An implementation must raise a signal for every condition in the table of section 8.5, with at least the content stated.

**P1-8.19 (MUST) Signals are addressed to an actor.** An implementation must direct each signal to a recorded custodian or role, and must not raise a signal with no addressee.

**P1-8.20 (MUST NOT) No signal in place of an outcome.** An implementation must not substitute a signal for the return of the corresponding outcome to the caller.

**P1-8.21 (MUST) Signals are recorded.** An implementation must record the raising of every signal and its acknowledgement, as fact rows.

### 8.6 The evidence package

The evidence package is what makes clause P1-1.6 achievable. It is a self describing export whose reader is assumed to have no access to the component, no knowledge of its internal structures, and no ability to ask questions. The mapping below is to the Open Archival Information System reference model, third edition, published as ISO 14721:2025 and as CCSDS 650.0-M-3 of December 2024, which structures an Archival Information Package as Content Information together with Preservation Description Information comprising Provenance, Context, Reference, Fixity and Access Rights, and which in its third edition adds the concept of Preservation Objectives to make the requirement that a package be independently understandable more consistently testable.

| Package element | OAIS element | Content |
|---|---|---|
| Content octets of every rendition exported | Content Information, Data Object | The bytes |
| Canonical form profile statements | Content Information, Representation Information | The profile identifier, version, external specification reference, and where available the executable statement |
| Media type and schema references | Representation Information | As recorded |
| Full fact and assertion row history for the subject and its lineage | PDI, Provenance | Including retracted assertions, marked as retracted, with the retraction rows |
| Approvals, signatures, manifestation text, time stamp tokens, certificate chains and revocation information as at export | PDI, Provenance | Sufficient to validate a signature after certificate expiry |
| Recorded resolutions of citations to the subject, and the citations themselves | PDI, Context | Including divergence flags |
| Classification assignments with the scheme version, and the scheme version content as at export | PDI, Context | Because a classification code is uninterpretable without the scheme |
| Retention applications, holds, authorisations, tombstones | PDI, Context and Access Rights | |
| Every digest under every algorithm, and the fixity check history | PDI, Fixity | |
| Lineage and version identifiers, and the identifier scheme statement | PDI, Reference | |
| Security markings and the access conditions in force at export | PDI, Access Rights | |
| A statement of what a reader must be able to do to use the package | Preservation Objectives | Explicit, per the third edition of OAIS |
| A human readable rendering of the whole | Not an OAIS element | Because a package readable only by the exporting software fails clause P1-1.6 |
| The verification procedure | Not an OAIS element | Stated in prose and in a machine readable form |
| Package manifest and package digest | PDI, Fixity | Over the package as a whole |

**P1-8.22 (MUST) Package contents.** An evidence package must contain every element of the table of section 8.6 that exists for its subject, and must state explicitly for each element of that table that does not exist that it does not exist.

**P1-8.23 (MUST) Retracted assertions included.** An evidence package must include retracted assertions and their retractions, and must not export only the currently believed state.

**P1-8.24 (MUST) Scheme snapshots included.** An evidence package must include the content of every external classification scheme version, reference set version and schema version referenced by the exported rows, or must state that it could not be obtained and from whom it was sought.

**P1-8.25 (MUST) Self describing verification.** An evidence package must state its verification procedure in a form a reader can execute without the component, including the digest algorithms used and the canonical form profiles applied.

**P1-8.26 (MUST) Human readable rendering.** An evidence package must include a rendering of its content and of the provenance history readable without software specific to the component.

**P1-8.27 (MUST) Package integrity.** An implementation must compute and include a digest over the whole package and must record the export and the package digest as a fact row.

**P1-8.28 (SHOULD) Signature validation material.** An implementation should include, for every signature in the package, the certificate chain, the revocation information current at signing, and any time stamp token, because a signature exported without them becomes unverifiable when the certificates expire, and expiry is certain within the retention periods this part contemplates.

**P1-8.29 (MUST NOT) No package without provenance.** An implementation must not offer an export containing content octets and no provenance history, and must not describe such an export as an evidence package.

### 8.7 Retention of the record

**P1-8.30 (MUST) Audit retention at least equals subject retention.** An implementation must retain the fact rows, assertion rows and records of section 8.2 concerning a subject for at least as long as the longest retention period applying to that subject.

**P1-8.31 (MUST) Audit survives disposition.** An implementation must retain the audit record of a subject after the subject's content is destroyed, subject to the tombstone requirements of section 3.12.

**P1-8.32 (MUST NOT) No disposition of the audit record alone.** An implementation must not dispose of the audit record of a subject while the subject is retained.

**P1-8.33 (MUST) Declared audit disposition.** Where an implementation disposes of an audit record, it must do so under a retention application like any other subject, with an authorisation and a tombstone.

### 8.8 What cannot be changed

**P1-8.34 (MUST NOT) No amendment of a written row.** An implementation must not provide any interface, administrative or otherwise, that amends a written fact row or assertion row.

**P1-8.35 (MUST NOT) No suppression from reads.** An implementation must not provide a mechanism that hides a written row from projections or exports, other than the access control mechanism of section 3.11 and section 12.7, whose exercise is itself recorded.

**P1-8.36 (MUST) Chain of the record.** An implementation must record, for every row, a digest over its own content and the digest of the immediately preceding row in its stream, so that removal or alteration of a row is detectable without reference to an external copy.

**P1-8.37 (SHOULD) Independent anchoring.** An implementation should periodically publish the head digest of each stream to a location outside its own control, because a hash chain held entirely within the system it protects demonstrates internal consistency only.
## 9. Extension model

### 9.1 Closed sets, open sets and registry mechanics

Three sets in this part are closed: the lifecycle status values of section 5.2, the force state values of section 5.4, and the outcome classes of section 7.2. They are closed because every one of them is load bearing in an invariant or an algorithm. A new status value changes the transition table; a new force state changes the resolution algorithm; a new outcome class changes what a caller is obliged to do. Those changes cannot be made safely by an organisation adding a row to a registry, because a reader of a determination made under the extended set would have no way to know which set was in force. Extending them requires a new version of this part.

Everything else is an open set held in a registry. A registry is a governed list of members admitted under stated rules.

**P1-9.1 (MUST) Registry as controlled document.** Every registry required by this part must be held as a document lineage under this part, with versions, approvals and effectivity, so that the members in force at a past moment are resolvable by the mechanism of section 6.2.

**P1-9.2 (MUST) Member fields.** Every registry member must carry a key, a display name, a definition, the version of the registry in which it was admitted, its status, and where applicable a reference to the external specification it implements.

**P1-9.3 (MUST) Member status set.** Every registry member must have a status of `ACTIVE`, `DEPRECATED` or `RETIRED`, where `DEPRECATED` means must not be used for new records and remains valid for reading existing ones, and `RETIRED` means must not be used and must not be interpreted without the successor named in the member entry.

**P1-9.4 (MUST NOT) No key reuse.** An implementation must not admit a member whose key has previously been used in that registry.

**P1-9.5 (MUST NOT) No silent redefinition.** An implementation must not change the definition of an admitted member, and must admit a new member where the meaning changes.

**P1-9.6 (MUST) Admission does not change existing members.** An implementation must not admit a member whose admission changes the interpretation of any existing member, and must instead deprecate the affected members and admit replacements.

**P1-9.7 (MUST) Recorded member reference.** Every row that names a registry member must record the registry version against which the member was valid at the time of writing.

**P1-9.8 (MUST) Deprecation is not removal.** An implementation must retain deprecated and retired members and must continue to interpret rows that reference them.

### 9.2 Canonical form profile registry

Initial members: `JSON-JCS-RFC8785`, implementing the JSON Canonicalization Scheme of RFC 8785; `XML-C14N11`, implementing Canonical XML version 1.1; `TEXT-NFC-LF`, being Unicode normalisation form NFC with line endings normalised to a single line feed; `OCTET-IDENTITY`, being no transformation; `RENDERED-BYTE-IDENTITY`, being no transformation applied to a fixed layout rendering.

**P1-9.9 (MUST) Profile names an external specification or states that it is local.** Every profile member must reference the external specification it implements, or state explicitly that the profile is defined only by this organisation, in which case clause P1-3.123 applies.

**P1-9.10 (MUST NOT) No profile change under the same key.** An implementation must not alter the transformation performed by an admitted profile, and must admit a new profile version, because a changed profile silently converts every existing digest under it into a mismatch.

### 9.3 Locator scheme registry

Initial members: `CLAUSE_ID`; `SECTION_PATH`; `JSON_POINTER`, per RFC 6901; `XPATH`; `TEXT_QUOTE` and `TEXT_POSITION`, per the selector types of the W3C Web Annotation Data Model; `PAGE_LINE`; `URI_FRAGMENT`, per RFC 3986 section 3.5.

**P1-9.11 (MUST) Scheme states its resolution procedure.** Every locator scheme member must state the procedure by which an expression in that scheme is resolved against a rendition, and the conditions under which resolution yields each outcome of section 7.5.

**P1-9.12 (SHOULD) Position schemes are paired.** An implementation should require that a locator in a position based scheme be accompanied by one in a content based scheme, because a position locator does not survive reflow and a quotation locator does not survive editing, and the pair distinguishes the two situations.

### 9.4 Metadata element registry

The mandatory core set is specified in section 3.11 and is not extensible except by a new version of this part; the registry governs elements beyond it.

**P1-9.13 (MUST) Element definition fields.** Every metadata element member must carry its data type, cardinality, whether it is mandatory for any subject kind, and what its absence means.

**P1-9.14 (MUST NOT) No shadowing of the core set.** An implementation must not admit an element whose meaning duplicates or narrows a member of the mandatory core set.

### 9.5 Digest algorithm registry

Initial active members: `sha-256`, `sha-384`, `sha-512`, `sha3-256`. Initial deprecated members: `sha-1`, `md5`, admitted as deprecated so that digests recorded before this part can be read and reported, and never used for a new digest.

`sha-256` is the recommended default. This is an implementation decision and the reason is that it is the most widely implemented algorithm currently considered adequate by the major cryptographic authorities, which matters more than marginal strength for a component whose digests must be recomputable by unrelated software decades hence.

**P1-9.15 (MUST) Deprecated algorithms are readable and unusable.** An implementation must be able to report a digest recorded under a deprecated algorithm and must not compute a new digest under one.

**P1-9.16 (MUST) Migration on deprecation.** On deprecating an algorithm, an implementation must add a digest under an active algorithm to every retained subject that has no such digest, and must record each addition as a fact row.

**P1-9.17 (MUST NOT) No removal on deprecation.** An implementation must not remove a digest recorded under a deprecated algorithm.

### 9.6 Reason code registry

Initial members: `AUTHORING_ERROR`, `APPROVAL_DEFECT`, `WRONG_SUBJECT`, `DATE_ERROR`, `SCOPE_ERROR`, `SUPERSESSION`, `CONTENT_DEFECT`, `PRACTICE_SUPERSEDED`, `REGULATORY_CHANGE`, `MIGRATION`, `CONSEQUENTIAL`, `OTHER`.

**P1-9.18 (MUST) Reason text with `OTHER`.** An implementation must require reason text where the reason code is `OTHER`, and must not accept `OTHER` on an operation that does not permit reason text.

### 9.7 Signature method registry

Initial members: `TWO_FACTOR_LOCAL`, `TWO_FACTOR_FEDERATED`, `PKI_SMARTCARD`, `QUALIFIED_ELECTRONIC_SIGNATURE`, `BIOMETRIC`.

**P1-9.19 (MUST) Method states its factor count and evidence.** Every signature method member must state the number of distinct identification components it employs, whether it is biometric, and what evidence of the signing act is retained.

**P1-9.20 (MUST) Method states its long term validation basis.** Every signature method member must state how a signature made under it can be validated after the expiry of any credential it relies on, or must state that it cannot, in which case clause P1-3.122 applies to subjects signed under it.

### 9.8 Composition against primitive

Three composite constructs are specified, and the distinctions among them are the substance of this section, because collapsing any pair of them destroys a property.

A **compilation** is a document whose content is a manifest of pinned versions of other documents. It is a primitive document in every respect: it has versions, effectivity, approval and a digest over its own canonical form, which is the manifest. What makes it composite is only that its content refers to other subjects. A new version of a member does not create a new version of the compilation, and this is the point: a submission binder assembled in March is a statement about what was pinned in March.

An **aggregation** is a grouping of records for classification, retention and disposition. It is not a document, has no versions, no effectivity and no content of its own.

A **rendition set** is the set of expressions of one version. It is not a composition of documents at all.

**P1-9.21 (MUST) Compilation manifest is content.** An implementation must treat the manifest of a compilation as the content of a version of the compilation, must compute a digest over it under a declared canonical form profile, and must not treat the members as the content.

**P1-9.22 (MUST) Compilation members are pinned.** An implementation must require every member reference in a compilation manifest to be a pinned citation carrying a version identifier and a digest.

**P1-9.23 (MUST NOT) No implicit compilation update.** An implementation must not create a new version of a compilation, and must not alter its manifest, when a new version of a member is created or takes force.

**P1-9.24 (MUST) Member drift is reported.** An implementation must report, on request and on a declared schedule, every compilation whose pinned members are no longer the versions in force, and must not treat that condition as an error.

**P1-9.25 (MUST NOT) No compilation as aggregation.** An implementation must not use a compilation to carry retention or disposition for its members, and must not use an aggregation to carry a pinned set of document versions.

**P1-9.26 (MUST) Nested compilation depth is declared.** An implementation must declare the maximum nesting depth it supports for compilations whose members are themselves compilations, and must reject a manifest exceeding it rather than resolving it partially.

### 9.9 Preservation event type registry

Initial members, aligned with the event types in common use under PREMIS 3.0: `CAPTURE`, `FIXITY_CHECK`, `FORMAT_IDENTIFICATION`, `FORMAT_VALIDATION`, `NORMALISATION`, `MIGRATION`, `REPLICATION`, `DECRYPTION`, `VIRUS_CHECK`, `DELETION`.

**P1-9.27 (MUST) Event type states its digest effect.** Every preservation event type member must state whether events of that type produce a new object, and therefore a new digest, or assert something about an existing one.

### 9.10 Retention trigger type registry

Initial members: `CREATION`, `DECLARATION`, `LAST_ACTION`, `SUPERSESSION`, `WITHDRAWAL`, `LINEAGE_OBSOLETE`, `AGGREGATION_CLOSURE`, `EXTERNAL_EVENT`.

**P1-9.28 (MUST) External trigger is recorded, not inferred.** Where a trigger type is `EXTERNAL_EVENT`, an implementation must require the occurrence of the event to be recorded as a fact row naming the event and its source, and must not infer the trigger from any other data.

**P1-9.29 (MUST NOT) No computation of a trigger from absence.** An implementation must not treat the absence of activity as the occurrence of `LAST_ACTION`, and must require an explicit assertion of the last action time.

### 9.11 Hold reason registry

Initial members: `LITIGATION`, `REGULATORY_INQUIRY`, `INTERNAL_INVESTIGATION`, `AUDIT`, `COMMERCIAL_DISPUTE`, `PRESERVATION_ORDER`, `OTHER`.

**P1-9.30 (MUST) Hold reason does not reveal itself where it must not.** An implementation must permit a hold whose reason text is withheld from ordinary readers while remaining recorded, and must not omit the reason text from the record in order to achieve that.

### 9.12 Event type registry

Initial members are the minimum event set of section 4.7.

**P1-9.31 (MUST) Event type states its row.** Every event type member must name the fact or assertion row whose writing produces it.

### 9.13 Outcome code registry

Initial members are the codes of sections 7.4 to 7.7.

**P1-9.32 (MUST) New codes carry a class.** Every outcome code admitted must be assigned to one of the closed classes of section 7.2 and must state the caller obligation.

**P1-9.33 (MUST NOT) No code that means two things.** An implementation must not admit an outcome code whose meaning spans more than one class or more than one `NON_RESULT` subclass.

### 9.14 Access purpose registry

Initial members: `DETERMINATION`, `OPERATIONAL_USE`, `REVIEW`, `AUDIT`, `TRAINING`, `DISCOVERY`, `EXPORT`, `MIGRATION`.

**P1-9.34 (MUST) Purpose is asserted by the caller.** An implementation must record the purpose as asserted by the caller and must not infer it from the caller's identity or role.
## 10. Standards and specifications

### 10.1 How the citations in this part are to be read

Two kinds of statement appear in this part. A statement marked as resting on specification text is one where the cited document's own text states the requirement, and where that text was available to the author. A statement marked as practice is one where the cited document does not state the requirement and the requirement is drawn from the way practitioners, inspectors or implementers behave. The distinction matters because a reader assessing an implementation against this part is entitled to know which of its clauses can be traced to an external authority and which cannot.

Several of the standards named below are paywalled and were not available in full text to the author of this part. Where that is so, this part's account of what the standard supplies rests on the standard's published scope, foreword, table of contents, secondary literature and implementation practice. Those cases are listed individually in section 13.1 rather than being silently smoothed over, because a specification that cites a document it has not read is asserting an authority it does not have.

Where a currency finding below contradicts the standard as commonly named, the finding is stated explicitly, because citing a superseded edition is one of the more common defects in this class of document and this part is in no position to commit it.

### 10.2 Records management, the ISO/TC 46 family

| Standard | Edition and status as at 2026-08-17 | What it supplies to this component | What it does not supply |
|---|---|---|---|
| ISO 15489-1 | 2016, second edition, confirmed on review in 2021 | The concept of a record as evidence, the properties of authenticity, reliability, integrity and usability, and the vocabulary of appraisal, classification and disposition | Any data model, any interface, any algorithm, and no treatment of documents as distinct from records |
| ISO/TR 15489-2 | Withdrawn following the 2016 revision of Part 1; the withdrawal year is reported inconsistently in secondary sources as 2016 and as 2017 | Nothing current. Cited here only to record that it must not be cited as current | |
| ISO 16175-1 | 2020, superseding the three part 2010 and 2011 series | Model functional requirements for software managing digital records, including in business systems rather than dedicated repositories | Fewer than forty pages of high level requirements; no data model, no state model, no outcome taxonomy |
| ISO/TS 16175-2 | 2020, confirmed on review in 2024 | Guidance on selecting, designing and maintaining such software | Requirements; it is explicitly guidance |
| ISO 30300 | 2020, second edition, superseding 2011 | Core concepts and vocabulary for records management across the TC 46/SC 11 family | Requirements on a system; it is a vocabulary standard |
| ISO 30301 | 2019, with Amendment 1 of 2024; a draft revision was in progress as at the date of this part | Management system requirements for records, auditable and certifiable | Anything about software behaviour |
| ISO 30302 | 2022, with Amendment 1 of 2025 | Implementation guidance for the management system | As above |
| ISO 23081-1 | 2017 | Principles for metadata for records | The mandatory element set this part specifies in section 3.11 |
| ISO 24143 | 2022 | Information governance concepts and principles | Requirements on a component |
| ISO 17068 | 2017 | Requirements for a trusted third party repository for digital records | Applicability where the repository is not a third party |

**P1-10.1 (MUST) Currency of cited standards.** An implementation that claims alignment with a standard named in section 10 must name the edition it aligns with, and must not cite a superseded edition as current.

**P1-10.2 (MUST NOT) No inference of conformance from vocabulary.** An implementation must not represent its use of the vocabulary of ISO 15489-1 or ISO 30300 as conformance with those standards.

### 10.3 Functional requirement specifications

| Specification | Status as at 2026-08-17 | What it supplies | What it does not supply |
|---|---|---|---|
| MoReq2010, version 1.1 | Published 2011 by the DLM Forum and freely available. The DLM Forum resolved in 2018 not to undertake further development after no member came forward to continue it, and the specification has not been revised since | The service oriented decomposition of a records system, the concept of declaring a record, the replacement of the file and folder hierarchy by an aggregation of unbounded depth, and a coherent treatment of unalterability | Maintenance. It also predates the current generation of storage models and does not address the append only projection pattern |
| DoD 5015.02-STD | **Cancelled.** Superseded by DoD Manual 8180.01, "Information Technology Planning for Electronic Records Management", of 4 August 2023. The Joint Interoperability Test Command records management test programme has been terminated and product certification against 5015.02 is no longer available | Historically, the most influential functional requirement set for records management software, and the origin of much of the file plan vocabulary still in use | Anything current. An implementation must not cite certification against it as evidence of anything about its present behaviour |
| DoD Manual 8180.01 | Current, 4 August 2023 | An outcome oriented treatment of records management in the planning and acquisition of information technology, deliberately moving away from certification against narrow technical requirements | Functional requirements for a component. It is a planning instrument |
| DoD Instruction 5015.02 | The policy instruction remains in force and is distinct from the cancelled standard | Policy and responsibilities | Software requirements |
| NARA Universal Electronic Records Management Requirements | Current NARA guidance, first issued 2017 | A short set of requirements applicable to any system holding federal records | Depth. They are deliberately universal and therefore shallow |

**P1-10.3 (MUST NOT) No citation of the cancelled standard as current.** An implementation must not represent DoD 5015.02-STD as a current standard, and must not represent certification against it as current evidence.

### 10.4 Preservation

| Standard | Edition and status as at 2026-08-17 | What it supplies | What it does not supply |
|---|---|---|---|
| ISO 14721, the OAIS reference model | **2025, third edition**, adopted from CCSDS 650.0-M-3 of December 2024, cancelling and replacing the 2012 second edition. Freely available in its CCSDS form. The third edition introduces the concept of Preservation Objectives, in order to make the requirement that content be independently understandable more consistently testable, and adds a Preservation Watch function | The information package model, the decomposition of Preservation Description Information into Provenance, Context, Reference, Fixity and Access Rights, which section 8.6 uses directly, and the vocabulary of an archive's responsibilities | A data model, a metadata element set, and any treatment of effectivity or citation. It is a reference model and says so |
| PREMIS Data Dictionary | 3.0, 2015, maintained by the Library of Congress and freely available; an OWL ontology at version 3 exists | The Event, Object, Agent, Rights and Intellectual Entity model, the treatment of fixity as a property verified by an event, and a usable vocabulary of preservation event types | Anything about approval, effectivity or citation. It is a preservation metadata dictionary |
| ISO 16363 | 2025, adopted from CCSDS 652.0-M-2 of December 2024 | Audit and certification criteria for a trustworthy digital repository | Component level requirements; and its use here would anticipate the assessment exercise that `Part 12` owns |
| ISO 16919 | 2025 | Requirements for bodies certifying repositories | Nothing for this part |
| ISO 23507 | Published, adopted from CCSDS 653.0-M-1 | Information preparation to enable long term use | Not assessed for this part; see section 13.1 |

**P1-10.4 (MUST) OAIS edition.** An implementation that maps its evidence package to the OAIS information model must state which edition of ISO 14721 it maps to, because the third edition adds Preservation Objectives and a package built to the second edition does not contain them.

### 10.5 Quality management

ISO 9001:2015, fifth edition, with the climate change amendment of 2024, is the edition in force as at the date of this part. Its clause 7.5 governs documented information and requires control of creation, update, identification, format, review, approval, availability, distribution, storage, preservation, change control, retention and disposition. A revision has reached Final Draft International Standard, which was approved in July 2026, with publication anticipated in September 2026 and a transition period expected to run into 2029.

Two consequences follow for this part. First, clause 7.5 is the single most widely applicable specification text requiring the controls this component provides, and it is the reason a component of this kind exists in organisations under no regulatory obligation at all. Second, a citation to "ISO 9001 clause 7.5" will shortly become ambiguous between editions, and clause P1-10.5 addresses that.

**P1-10.5 (MUST) Edition qualified citation of clause 7.5.** An implementation that cites ISO 9001 clause 7.5 as the basis for a control must cite the edition, and must review the citation on publication of the 2026 edition rather than assuming the clause numbering and content carry over.

**P1-10.6 (MUST NOT) No adoption of the single term.** An implementation must not adopt the term "documented information" as the name of a single governed object in place of the two objects of section 2.1.

### 10.6 Regulated electronic records and signatures

| Instrument | Status as at 2026-08-17 | What it supplies | What it does not supply |
|---|---|---|---|
| 21 CFR Part 11 | In force since 1997; the text of the rule is substantially unchanged since then | The only widely applicable specification text stating what an electronic signature must carry, in 11.50 and 11.70, what makes it attributable, in 11.100 and 11.200, and what an audit trail must do, in 11.10(e). Sections 3.9 and 8.1 of this part rest on it | Any treatment of versioning, effectivity or citation. It is about trustworthiness of records and signatures, not about which document governed |
| FDA guidance, Part 11 scope and application | 2003, still the operative scope guidance | The narrowing of enforcement scope that explains why the rule is applied as it is | Requirements |
| FDA final guidance on electronic systems, electronic records and electronic signatures in clinical investigations | Final, October 2024 | Current expectations for electronic systems holding regulated records, including third party and cloud arrangements | Applicability outside clinical investigations |
| FDA guidance on computer software assurance | Final, September 2025 | A risk based approach to assurance of software used in production and quality systems | Anything about document control specifically |
| EU GMP Annex 11, computerised systems | The 2011 text remains in force. A draft revision was published on 7 July 2025, consultation closed on 7 October 2025, and the final text had not been published as at the date of this part. The draft expands the annex from roughly five pages to nineteen, adds cybersecurity, identity and access management, supplier obligations and a substantially expanded treatment of audit trails, including that audit trails be permanently enabled | The current text supplies audit trail, accuracy check and change control expectations for computerised systems | A data model. The draft's audit trail expectations, if finalised as drafted, would strengthen section 8 rather than change it |
| EU GMP Chapter 4, documentation | The current text remains in force; a revised draft was published in the same July 2025 package and, as drafted, treats documentation as extending to metadata and system audit trails rather than to documents alone | Requirements on the control of GMP documentation | As above |
| EU GMP Annex 22, artificial intelligence | New annex, draft only, published July 2025 in the same package | Relevant to `Part 13` rather than to this part. Noted here because the same consultation package changes the documentation chapter | Nothing for this part directly |
| GAMP 5, second edition | 2022 | Industry guidance on computerised system assurance, with appendices addressing cloud and machine learning | It is guidance from an industry body, not specification text, and this part cites it as practice |
| ALCOA, ALCOA+ and ALCOA++ | ALCOA is longstanding regulatory practice; ALCOA+ is established in inspectorate guidance; ALCOA++ appears in more recent European guidance on computerised systems | The property set attributable, legible, contemporaneous, original, accurate, plus complete, consistent, enduring and available, and in the ++ formulation traceability | A specification. No instrument defines the acronym normatively, and the members of the set differ between sources. Cited as practice |
| PIC/S PI 041-1 | Effective July 2021 | Data management and integrity expectations for inspectors, widely used as the practical statement of the ALCOA+ properties | Specification text |

**P1-10.7 (MUST) Practice citations marked.** An implementation that relies on GAMP 5, the ALCOA property set, or inspectorate guidance as the basis for a control must record that the basis is practice rather than specification text.

**P1-10.8 (SHOULD) Audit trail expectations tracked.** An implementation should track the finalisation of the July 2025 EU GMP package, because a requirement that audit trails be permanently enabled and independently reviewed would become specification text for organisations in scope, where it is presently inspectorate practice.

### 10.7 Technical specifications

| Specification | Supplies | Used in |
|---|---|---|
| RFC 2119, RFC 8174 | Requirement keyword semantics | Binding statement |
| RFC 3339, ISO 8601-1 | Timestamp and duration syntax | Section 3.1 |
| RFC 9562 | UUID formats including version 7, obsoleting RFC 4122 | Clause P1-3.3 |
| RFC 8141 | URN syntax | Section 3.1 |
| RFC 8785 | JSON Canonicalization Scheme | Section 9.2 |
| W3C Canonical XML 1.1 | XML canonicalisation | Section 9.2 |
| RFC 6901 | JSON Pointer | Section 9.3 |
| RFC 3986 | URI fragment addressing | Section 9.3 |
| W3C Web Annotation Data Model | Quotation and position selectors, which are the only standardised locators robust to reflow | Section 9.3 |
| RFC 6838 | Media type syntax | Section 3.1 |
| BCP 47 | Language tags | Section 3.1 |
| RFC 9457 | Problem details, obsoleting RFC 7807 | Clause P1-7.8 |
| RFC 3161 | Time stamp protocol | Clause P1-3.65 |
| RFC 4998 and RFC 6283 | Evidence Record Syntax and its XML form: hash tree based proof of existence and integrity, with renewal before the algorithms or certificates relied upon become weak. This is the only standardised answer to the problem of proving integrity across the deprecation of the algorithm that originally proved it | Clause P1-3.122 |
| ETSI TS 119 512, BSI TR-03125 | Preservation service interfaces and evidence record profiling | Cited as available approaches; not required |
| SQL:2011 temporal features | System versioned tables and application time period tables, being the standardised expression of the two time dimensions this part depends on | Section 2.1, as the source of the distinction, not as a required implementation |
| CloudEvents 1.0 | An event envelope | Section 4.7, as an example carrier |

**P1-10.9 (MUST) Named specification for each profile and algorithm.** An implementation must name the external specification implemented by every canonical form profile, digest algorithm, locator scheme and signature method it registers, or must state that none exists.

### 10.8 Where the standards conflict

These are real conflicts, not apparent ones. This part names them and, where it takes a position, says so; where it does not, section 13 records the question as open.

**Revisability of the governed object.** ISO 9001 clause 7.5 governs "documented information" as one object with one set of controls. ISO 15489-1 treats a record as fixed evidence. An organisation applying both to one component is told both that its governed objects are revisable and that they are not. This part takes a position: two objects, two rule sets, stated in section 2.1 and enforced by clause P1-1.9.

**Mandated destruction against mandated retention.** A retention schedule may require destruction at a date. A legal hold may forbid it. A regulated audit trail requirement may require retention of the audit record for at least as long as the record. A data protection erasure right may require removal of personal data from both. No instrument named in this section resolves the collision, and each was written as though the others did not exist. This part takes a position only on the mechanism, in clauses P1-3.90 through P1-3.94, and records the substantive conflict as open in section 13.2.

**Immutability against migration.** OAIS requires that an archival package remain independently understandable over time, which in practice requires format migration; PREMIS records migration as an event producing a new object. The result is that the object whose fixity was asserted is not the object now held. This part takes a position in clauses P1-3.72 and P1-9.27: the original digest is retained and the migration is a recorded event producing a new digest, so that the chain is explicit rather than the fixity claim being quietly transferred.

**Where record identity lives.** The file plan tradition of DoD 5015.02 and the aggregation model of MoReq2010 assume a dedicated records system that owns record identity. ISO 16175-1 explicitly addresses records held in business systems that were not built for the purpose. The two produce different answers to the question of what happens when the business system is decommissioned. This part takes a position by locating identity in this component and requiring the evidence package of section 8.6, which is meaningful only if identity does not depend on the producing system.

**Signature regimes.** 21 CFR 11.200 requires at least two distinct identification components for a non biometric signature and a specific manifestation. The European qualified electronic signature framework specifies certificate based requirements and says nothing about manifestation or meaning. A signature can satisfy either while failing the other. This part requires the manifestation and meaning of the former and permits the methods of the latter, in section 3.9 and section 9.7, and does not claim that either regime's compliance follows.

**Property vocabularies.** ISO 15489-1 names authenticity, reliability, integrity and usability. The ALCOA+ formulation names nine or ten properties depending on the source. No published crosswalk between them was found. This part uses neither vocabulary as its organising principle and records the absence in section 13.3.

### 10.9 What none of the standards supplies

The following are requirements of this part for which no external specification text was found. They are the reason this part exists rather than being a bibliography.

The separation of lifecycle status from force state, and the prohibition on a single status field. No instrument named above states it, though several imply it by requiring that approval and effective dates be distinguishable.

The resolution algorithm of section 6.2, in particular its parameterisation by both application time and knowledge time. SQL:2011 supplies the two time dimensions but says nothing about documents; the records management standards supply documents but only one clock.

The divergence signal of clauses P1-3.101 and P1-4.31. Nothing found requires a component to notice that a determination was made on a version later found not to have been in force.

The discrimination between integrity failure and integrity indeterminacy, in clauses P1-3.119 and P1-7.21. Every instrument found treats fixity as pass or fail.

The distinction between a withheld result and a non existent one, in clauses P1-7.11 and P1-7.12.

Clause level locator stability across restructuring, in clauses P1-3.104 through P1-3.106. Citation practice in law and standards development depends on it universally and specifies it nowhere.

Tombstone semantics for content destroyed while still cited, in clause P1-3.90.

Effectivity scope and the prohibition on scope inheritance, in clause P1-3.54.

The obligation on a caller receiving each non result, which this part states for its own contract in section 7 and which becomes a composition requirement in `Part 0`.

**P1-10.10 (MUST) Local origin declared.** An implementation must not represent a requirement listed in section 10.9 as derived from an external standard.
## 11. Anti patterns

Each entry names the mechanism, states the consequence, and marks whether the evidence for it is specification text or practice. A design smell is not an anti pattern. What follows are designs that are common, that work until a specific question is asked, and that cannot then answer it.

### 11.1 The mutable current row with a history table beside it

**Mechanism.** The current state of a document is a row that is updated in place. A trigger or application code writes a copy of the prior values to a history table.

**Consequence.** The history is a second artifact that can diverge from the first, and nothing in the design prevents divergence: a write that bypasses the trigger, a bulk load, a restore from backup, a schema migration or a maintenance script leaves the current row changed and the history silent. The divergence is undetectable after the fact, because the only evidence of what the row used to be is the artifact that failed to record it. The condition is worse than having no history, because a history table is read as authoritative.

**Evidence.** Practice. The requirement in 21 CFR 11.10(e) that an audit trail be computer generated and independent, and that it not obscure previously recorded values, is specification text addressing this design, but the regulation does not name the mechanism.

**P1-11.1 (MUST NOT) No history beside a mutable row.** An implementation must not satisfy the audit requirements of section 8 by maintaining a record of changes to a mutable row.

### 11.2 Citing the lineage and resolving to the latest version

**Mechanism.** A determination records that it relied on "SOP 14" without an application time, a knowledge time or a version. Resolution at read time returns whatever is in force now.

**Consequence.** Every historical determination silently re resolves as the document changes. The record of a decision made in 2027 will, read in 2031, appear to have relied on the 2031 text. No error is ever raised, and the falsification is complete and invisible. This is the most damaging single defect in the class, because the system continues to answer confidently.

**Evidence.** Practice.

**P1-11.2 (MUST NOT) No lineage only citation.** An implementation must not accept a citation that names a lineage without either a version and digest or an application time and knowledge time, per clauses P1-3.96 through P1-3.99.

### 11.3 Approval treated as entry into force

**Mechanism.** The act of approval sets the document effective, either immediately or at a date derived from the approval date.

**Consequence.** Future dated effectivity cannot be represented, so an organisation that must publish a procedure before it takes effect either approves late, which is a false record of when the approval occurred, or backdates, which is a false record of when the document took force. Retroactive effectivity cannot be represented at all, so the discovery that a document has been relied upon since a date earlier than its approval has nowhere to go. Both outcomes are data integrity failures produced by a data model, and both are then attributed to the people who had no other option.

**Evidence.** Practice, though the requirement in ISO 9001 clause 7.5 that documented information be controlled for approval and for availability where needed implies the separation.

**P1-11.3 (MUST NOT) No effectivity derived from approval.** An implementation must not create or default an effectivity assertion from an approval, per clause P1-3.63.

### 11.4 The single status field

**Mechanism.** One enumeration holds `DRAFT`, `APPROVED`, `EFFECTIVE`, `SUPERSEDED`, `OBSOLETE` and whatever else is needed, and it is updated as the document progresses.

**Consequence.** Values acquire two meanings. `EFFECTIVE` means both that a lifecycle step occurred and that the document currently governs, so a version that governed last year and was superseded cannot be distinguished from one that was never brought into force, and a version approved for a future date has no representable state. Every query about what governed at a past time becomes unanswerable, because the field holds only the present.

**Evidence.** Practice.

**P1-11.4 (MUST NOT) No fused status.** An implementation must not represent force state within the lifecycle status enumeration, per clause P1-5.2.

### 11.5 Renumbering clauses on revision

**Mechanism.** Sections and clauses are numbered by position. A revision inserts a clause and the following ones shift.

**Consequence.** Every citation to a position in an earlier version resolves, in the later version, to different content. This is worse than a broken citation, because a broken citation announces itself and a shifted citation does not. A determination recorded as resting on clause 4.3 will be read against whatever clause 4.3 later says, and the reader has no way to detect the substitution.

**Evidence.** Practice. Standards bodies, including the practice this part follows in its own section numbering, treat permanent numbering as a requirement, but no specification found states it as such.

**P1-11.5 (MUST NOT) No positional clause identity.** An implementation must not use a locator scheme in which the identifier of a unit of content is derived from its position, as the sole locator for a citation, per clause P1-3.105 and clause P1-9.12.

### 11.6 Documents and records governed as one object

**Mechanism.** A single entity with a version series is used for both a revisable procedure and a completed form, a signed batch record or a submitted report.

**Consequence.** Either records become revisable, which destroys their evidential value, or documents become unrevisable, which makes the system unusable and drives authoring outside it. In practice the first happens: version 2 of a completed record is created to fix a mistake, and the fact that the act being evidenced was recorded differently at the time is lost. The second order effect is that the organisation loses the ability to distinguish a correction from a rewriting.

**Evidence.** Specification text, in the sense that ISO 15489-1's treatment of a record as evidence and ISO 9001 clause 7.5's treatment of documented information as revisable cannot both be applied to one object. Neither instrument names the conflation as a defect.

**P1-11.6 (MUST NOT) No shared entity for the two kinds.** An implementation must not represent a document and a record as one entity kind, per clause P1-1.9 and clause P1-2.4.

### 11.7 One timestamp

**Mechanism.** Each row carries a single `created_at`.

**Consequence.** The three questions when did it happen, when did we record it, and when does it apply, collapse into one answer. A late entry becomes indistinguishable from a backdated one. A correction becomes indistinguishable from a falsification. Retroactive effectivity cannot be expressed. And the system cannot answer what it believed at a past moment, which is the question that makes a determination defensible.

**Evidence.** Practice, with the two time dimensions specified in SQL:2011 and the contemporaneousness expectation drawn from the ALCOA property set.

**P1-11.7 (MUST NOT) No single timestamp.** An implementation must not use one field for more than one of application time, knowledge time and occurrence time, per clause P1-2.5.

### 11.8 Digest over an undeclared serialisation

**Mechanism.** A digest is computed over whatever bytes were at hand: the request body, a serialisation produced by the current library version, a rendering produced by the current renderer.

**Consequence.** The digest is not reproducible. A library upgrade that changes key ordering, whitespace or Unicode normalisation causes every subsequent fixity check to fail, and the failures are reported as content alteration. The organisation then either disables fixity checking or learns to ignore it, which is the same thing.

**Evidence.** Practice, with RFC 8785 existing precisely because the problem is general.

**P1-11.8 (MUST NOT) No digest without a declared profile.** An implementation must not compute or record a digest over content whose canonical form profile is not declared, per clauses P1-3.114 and P1-3.115.

### 11.9 Fixity as pass or fail

**Mechanism.** A fixity check returns a boolean.

**Consequence.** Three distinguishable conditions, content altered, canonicaliser unavailable and algorithm unavailable, are reported as one, and the one chosen is the accusatory one. Over a long retention period the second and third become more likely than the first, so the system's most common statement about its own integrity is a false accusation. Trust in the mechanism collapses, and with it the value of every digest recorded.

**Evidence.** Practice. No instrument found distinguishes the conditions.

**P1-11.9 (MUST NOT) No boolean fixity.** An implementation must not report fixity as a boolean and must distinguish the outcomes of section 3.15, per clause P1-3.119.

### 11.10 The audit trail as a feature

**Mechanism.** Audit logging is a configurable subsystem with a switch, a verbosity level or a retention shorter than the records it describes.

**Consequence.** The audit trail is absent exactly when it matters, because the circumstances in which someone turns it off are the circumstances someone later wants to examine. Where retention is shorter than the record's, the record outlives its own provenance and becomes an assertion with no support.

**Evidence.** Specification text. 21 CFR 11.10(e) requires that audit trails be computer generated and retained for at least as long as the underlying records. The draft revision of EU GMP Annex 11 published in July 2025 would, if finalised as drafted, require that audit trails be permanently enabled.

**P1-11.10 (MUST NOT) No disableable record.** An implementation must not provide a mechanism that suspends the recording of fact or assertion rows, per clause P1-8.4, and must not retain the audit record for less than the subject, per clause P1-8.30.

### 11.11 Deletion without a tombstone

**Mechanism.** Disposition removes the row and the content.

**Consequence.** Authorised destruction becomes indistinguishable from loss, from a failed migration and from concealment. A citation to the destroyed subject resolves to nothing, and the organisation cannot demonstrate that the destruction was authorised, when it occurred, or by what authority, which is exactly what a retention schedule exists to enable it to demonstrate.

**Evidence.** Practice, with the disposition documentation expectations of ISO 15489-1 as the nearest specification support.

**P1-11.11 (MUST NOT) No destruction without a tombstone.** An implementation must not destroy content without retaining the tombstone of section 3.12, per clause P1-3.90.

### 11.12 Translation as a version

**Mechanism.** A translated document is created as the next version of the lineage, or as a separate lineage with its own effectivity.

**Consequence.** In the first form, the version series interleaves languages and the ordinal ceases to mean anything. In the second, two documents are in force at once with no recorded relation, and when one is revised the other silently becomes a different instrument. Readers in each language then follow different rules while both believe they are following the same document.

**Evidence.** Practice.

**P1-11.12 (MUST NOT) No independent translation effectivity.** An implementation must not permit a translation to hold its own effectivity, per clauses P1-3.32 and P1-3.33.

### 11.13 Metadata overwrite

**Mechanism.** Classification, custodian, retention rule and security marking are columns that are updated.

**Consequence.** A disposition executed under a classification assigned in 2029 cannot be explained if the classification was changed in 2031. The retention decision becomes unauditable, and where the change was wrong there is no evidence that it was ever different.

**Evidence.** Practice, with ISO 23081-1's treatment of metadata for records as accumulating over time as the nearest support.

**P1-11.13 (MUST NOT) No metadata overwrite.** An implementation must not overwrite a metadata value or a classification assignment, per clauses P1-3.77 and P1-3.81.

### 11.14 Access denied returned as not found

**Mechanism.** To avoid disclosing the existence of a restricted subject, the component returns the same response for withheld and for non existent.

**Consequence.** A reader entitled to know that something exists concludes that it does not. In an evidential read this converts an access control decision into a false statement of fact, and the false statement is then recorded by the caller as though the component had asserted it. The design is defensible for an anonymous interface and indefensible for an audit reader, and implementations rarely distinguish the two.

**Evidence.** Practice.

**P1-11.14 (MUST NOT) No conflation of withheld and absent.** An implementation must not return the outcome for an unknown subject where the subject exists and is withheld, per clauses P1-7.11 and P1-7.12.

### 11.15 Document identity owned by the process instance

**Mechanism.** The document exists as an attachment to a workflow case, a ticket or a transaction, and its identity is a child of that instance.

**Consequence.** When the process instance is archived, migrated or purged, the document's identity goes with it, and citations to it break. The same document attached to two cases becomes two documents with no recorded relation. Version history follows the case rather than the document, so the question of what the current procedure is cannot be asked at all.

**Evidence.** Practice. ISO 16175-1's explicit extension to records held in business systems exists because the pattern is pervasive.

**P1-11.15 (MUST NOT) No process owned identity.** An implementation must not make the identity of a lineage, version or record dependent on the existence of a process instance, a case or a transaction in another component, per section 12.6.

### 11.16 The register kept outside the controlled system

**Mechanism.** The list of controlled documents, their versions and their review dates is maintained in a spreadsheet, a wiki page or a document that is itself not controlled.

**Consequence.** The register and the repository disagree, and the register is what people act on. Because the register is uncontrolled, its own history is unavailable, so the disagreement cannot be dated or explained. This pattern is remarkably durable because the register usually starts as a convenience.

**Evidence.** Practice.

**P1-11.16 (MUST NOT) No uncontrolled register.** An implementation must hold every register and index required by this part as a controlled document or a projection under this part, per clause P1-9.1, and must not rely on an artifact outside it.

### 11.17 Copies with no markings and no record

**Mechanism.** A version is exported or printed on demand with no distribution record and no indication of currency on its face.

**Consequence.** A superseded copy in circulation is indistinguishable from a current one, and there is no list of where copies went, so recall is impossible. The organisation's controls exist in the repository and its work is done from the copies.

**Evidence.** Practice, with the availability and distribution provisions of ISO 9001 clause 7.5 as the nearest support.

**P1-11.17 (MUST NOT) No unmarked and unrecorded copy.** An implementation must not produce a human readable export without either a controlled copy record or the markings of clause P1-3.126.

### 11.18 The signature that binds nothing

**Mechanism.** A signature is an image, a typed name, a checkbox or a row recording that a named user clicked approve, with no digest of what was approved.

**Consequence.** The signature cannot be shown to apply to any particular content. If the content is later changed, the signature follows it. The manifestation requirement is also usually missing, so a printed copy carries no evidence of who signed, when, or what the signing meant.

**Evidence.** Specification text. 21 CFR 11.50 requires the printed name, the date and time and the meaning of the signing to be included in the human readable form of the record, and 11.70 requires that signatures be linked to their records so as not to be excisable by ordinary means.

**P1-11.18 (MUST NOT) No unbound signature.** An implementation must not record a signature that does not bind the digest of the signed content, per clause P1-3.55, and must not omit the manifestation of clause P1-3.60.

### 11.19 The hold as a status

**Mechanism.** Placing a legal hold sets the subject's status to `ON_HOLD`.

**Consequence.** The prior status is lost, so releasing the hold requires guessing what to return to. Two holds cannot coexist. The hold cannot be recorded against a set defined by a classification. And because status gates other transitions, the hold blocks review and supersession, which it has no business blocking.

**Evidence.** Practice. MoReq2010 treats disposal holds as a distinct concept rather than a state, which is the nearest specification support.

**P1-11.19 (MUST NOT) No hold as status.** An implementation must not represent a hold as a state value, per clauses P1-3.85 and P1-5.23.

### 11.20 The projection with no knowledge time

**Mechanism.** Every read model answers only as of now. Historical questions are served by ad hoc queries against whatever history exists.

**Consequence.** The component can answer what governs but not what governed, which is the purpose in section 1.1. The historical question is then answered by a person reading rows, inconsistently and without a record of the answer given.

**Evidence.** Practice.

**P1-11.20 (MUST NOT) No present only projection set.** An implementation must not offer the projections of section 3.14 without the knowledge time parameter, per clause P1-3.110.

### 11.21 The parsed version label

**Mechanism.** Status, significance or effectivity are encoded in the version label and read by parsing it, as in `v3.2-final-approved-2027-03-01`.

**Consequence.** Two representations of the same fact exist and diverge. The parser becomes a load bearing component that nobody documents. Labels that do not fit the convention are rejected or misread, and the convention changes over the life of the system, so old labels are parsed under new rules.

**Evidence.** Practice.

**P1-11.21 (MUST NOT) No parsed label.** An implementation must not derive any governed property from the text of a version label, per clause P1-3.26.

### 11.22 Identifier reuse after disposal

**Mechanism.** Identifiers, copy numbers or clause identifiers are reused once the subject they named has been disposed of, often to keep a sequence tidy.

**Consequence.** A citation recorded before the disposal resolves, after the reuse, to a different subject, and reports success. The tombstone that would have made the disposal visible is bypassed, because the identifier now resolves to something.

**Evidence.** Practice.

**P1-11.22 (MUST NOT) No reuse.** An implementation must not reuse any identifier, per clause P1-3.5.

### 11.23 The compilation that updates itself

**Mechanism.** A binder, dossier or manual is defined as a set of references to lineages, and rendering it collects whatever is currently in force.

**Consequence.** The compilation has no fixed content, so it cannot be approved, cannot be digested and cannot be cited. A submission made in March cannot be reproduced in September, and nobody notices until someone asks what was submitted.

**Evidence.** Practice.

**P1-11.23 (MUST NOT) No unpinned compilation.** An implementation must not accept a compilation manifest whose members are not pinned, per clause P1-9.22.
## 12. Boundaries with other parts

### 12.1 How a boundary in this part is stated

Each subsection below states four things: what this component delegates, what it must not absorb, the naive design that conflates the two, and the reciprocal declaration the other part must make. Subsection numbers correspond to part numbers, so section 12.7 states the boundary with `Part 7`, and section 12.14 states the boundary with `Part 0`. Numbers are permanent.

A boundary is reciprocal. If this part declares that it delegates something, the receiving part must declare that it owns it, in the same terms. A boundary declared on one side only is not a boundary; it is a hope.

**P1-12.1 (MUST) Declared allocation.** An implementation must be able to state, for every capability named in this section as delegated, which component provides it, and must not provide it within this component.

**P1-12.2 (MUST) Refusal rather than substitution.** Where a delegated capability is unavailable, an implementation must refuse the dependent operation under clause P1-4.24 and must not substitute a local implementation of it.

**P1-12.3 (MUST NOT) No reaching past a neighbour.** An implementation must not read or write the internal state of another component named in this section, and must interact with it only through that component's declared interface.

### 12.2 Boundary with Part 2, business rules engine

**Delegated.** The evaluation of any expression. Retention rules, review periods, eligibility conditions and the predicates that decide whether a subject is due for disposition are declared as data in this component and evaluated in `Part 2`.

**Must not absorb.** A rule language, an expression evaluator, or a conditional whose terms are supplied by a user.

**Naive conflation.** Implementing retention as executable code inside the document component, so that a retention rule cannot be reviewed, versioned or reasoned about without reading the component's source. The rule then has no effective date and no approval.

**Reciprocal.** `Part 2` must declare that it does not hold the versions, approvals or effectivity of the rules it evaluates, and that it obtains the rule text in force at an application time by resolution against this component.

**P1-12.4 (MUST) Rules as resolvable documents.** An implementation must express every retention rule, review period and eligibility condition as content of a document version resolvable under section 6.2, and must record with any evaluation the version resolved.

**P1-12.5 (MUST NOT) No embedded evaluation.** An implementation must not evaluate a rule expression, and must record the outcome supplied by `Part 2` together with the identity of the rule version evaluated.

### 12.3 Boundary with Part 3, provenance and audit ledger

**Delegated.** The chain of reasoning of a determination, including everything a determination cites other than documents, and the reconstructability of the determination as a whole.

**Must not absorb.** The general ledger of the enterprise. This component's audit record concerns documents and records only.

**Naive conflation.** Either this component becomes the general ledger, in which case every other component writes its provenance here and this component's invariants no longer hold over its own rows; or the ledger takes over document status, in which case there are two answers to what is in force.

**Reciprocal.** `Part 3` must declare that it does not determine what was in force, that it obtains that by citation resolution against this component, and that it records the resolution outcome including its basis and divergence flag rather than the version identifier alone.

**P1-12.6 (MUST) Resolution outcome is the citable artifact.** An implementation must return, and `Part 3` must record, the whole resolution outcome envelope of section 7.3 rather than the resolved version identifier alone.

**P1-12.7 (MUST NOT) No provenance of other subjects.** An implementation must not record provenance for subjects other than the documents, records and registries it owns.

### 12.4 Boundary with Part 4, metadata and model repository

**Delegated.** Governed definitions as data: data element definitions, models, and their lineage and impact analysis.

**Must not absorb.** Definitions. A definition published as a document is a rendition of the definition, not the definition.

**Naive conflation.** Treating a data dictionary as a document, so that the authoritative definition is a paragraph in a version of a Word file. Consumers then either parse prose or maintain a second copy, and the two diverge. The converse conflation is equally common: `Part 4` acquires versions, approvals and effective dates of its own, so an organisation has two answers to what definition applied on a date.

**Position taken.** The definition is authoritative in `Part 4`. Where a definition must be published as a controlled document, the published artifact is a version in this component whose content is generated from the definition and whose relation to it is recorded. This component owns the publication, `Part 4` owns the definition.

**Reciprocal.** `Part 4` must declare that it owns definition identity and versioning, that it does not own the approval or effectivity of published renditions, and that where it needs an approved publication it obtains it here.

**P1-12.8 (MUST) Published definitions are marked as renditions.** An implementation must record, for any version whose content was generated from a definition governed by `Part 4`, the identity and version of that definition, and must not present the published version as the authoritative definition.

**P1-12.9 (MUST NOT) No definition versioning.** An implementation must not assign version identity to a definition governed by `Part 4`.

### 12.5 Boundary with Part 5, decision engine

**Delegated.** The selection of one outcome from inputs, including which of several candidate approvers is required, whether a document requires review, and what disposition action applies where a rule permits more than one.

**Must not absorb.** Selection. This component records acts and evaluates the invariants and algorithms specified in section 6, which are determinate procedures rather than decisions.

**Naive conflation.** Treating citation resolution as a decision. It is not: it is a determinate function whose outcomes are enumerated in section 7.4, and where it cannot produce one answer it says so rather than choosing. Conversely, treating the choice of an approver as a resolution, which hides a policy in a lookup.

**Reciprocal.** `Part 5` must declare that it does not determine document status or effectivity, and that a decision requiring a governing document obtains it by citation resolution here.

**P1-12.10 (MUST NOT) No selection among candidates.** An implementation must not select among candidate versions, candidate rules or candidate approvers, and must return the ambiguity outcomes of section 7 instead.

### 12.6 Boundary with Part 6, workflow and process orchestration

**Delegated.** Control flow: routing a draft, sequencing approvals, chasing an overdue review, compensating a failed multi step operation, and the state of the process.

**Must not absorb.** Process state. The status transitions of section 5 record what was decided, not how the decision was reached or who was waiting for whom.

**Naive conflation.** The workflow instance owning document status, so that document state exists only as a position in a process, per section 11.15. The document then has no state when no process is running, and reconstructing history requires reading process instances that were designed to be transient.

**Reciprocal.** `Part 6` must declare that it does not own document status, version identity or effectivity, that it invokes the recording operations of section 4.2, and that its own retention does not govern the retention of the documents it routed.

**P1-12.11 (MUST) Status independent of process.** An implementation must record and project the status of every version without reference to any process instance, and must remain correct where the orchestrator is replaced or its instances are disposed of.

**P1-12.12 (MUST NOT) No process identity in the document model.** An implementation must not require a process instance identifier in order to write, read or resolve any row specified in section 3.

### 12.7 Boundary with Part 7, policy decision point and authorisation

**Delegated.** Every authorisation decision, including whether an actor may read a version, approve it, apply a hold, authorise a disposition or export an evidence package. Obligations attached to a decision, such as watermarking or notification, are also `Part 7`'s.

**Must not absorb.** Policy. This component supplies attributes and consumes decisions.

**Naive conflation.** Access rules expressed as classification values interpreted locally, so that the meaning of a marking is encoded in the document component and cannot be changed without changing it. The converse conflation is `Part 7` holding document metadata, which then diverges from this component's assertions.

**Reciprocal.** `Part 7` must declare that it owns policy evaluation, that it obtains classification, marking and distribution facts as attributes from this component, and that it does not record document status.

**P1-12.13 (MUST) Attributes supplied, decisions consumed.** An implementation must supply classification, security marking, custodian, aggregation membership and distribution facts as attributes for a decision, and must record the `AUTHREF` of the decision with the operation it permitted.

**P1-12.14 (MUST NOT) No local policy evaluation.** An implementation must not decide entitlement from a classification value, a marking or a role, and must not cache a decision beyond a declared validity period.

### 12.8 Boundary with Part 8, human task and case management

**Delegated.** The work of a person: the approver's queue, assignment, escalation, deferred choice, and the case as an entity.

**Must not absorb.** Task assignment. An approval in this component is the recording of a completed act, with its signature.

**Naive conflation.** The approval task and the approval record as one entity, so that closing the task is what approves the document and deleting the task removes the approval.

**Reciprocal.** `Part 8` must declare that completing a task does not itself change document state, and that the state change is effected by a recording operation of section 4.2 whose outcome the task records.

**P1-12.15 (MUST) Approval independent of task.** An implementation must record an approval with its signature such that it remains valid and complete after the task that prompted it is disposed of.

### 12.9 Boundary with Part 9, schema and contract registry

**Delegated.** Schema identity, schema versioning, compatibility rules between schema versions, and validation of content against a schema.

**Must not absorb.** Schema versioning and validation. This component records the schema reference a rendition claims and, per clause P1-4.5, records it as unverified where `Part 9` was unavailable.

**Naive conflation.** Validating content locally against a cached schema, so that two components disagree about whether a document is valid; or treating a schema as a controlled document with its own version series here, so that a schema has two version identities.

**Position taken.** A schema's identity and versioning belong to `Part 9`. Where a schema must be published as a controlled document, the published artifact is a rendition, on the same basis as section 12.4.

**Reciprocal.** `Part 9` must declare that it owns schema identity and compatibility, and that it does not own the approval or effectivity of published schema documents.

**P1-12.16 (MUST) Schema reference recorded, not evaluated.** An implementation must record the schema identity and version a rendition claims and must not validate content against it.

**P1-12.17 (MUST) Unverified claims marked.** An implementation must mark a recorded schema claim as unverified where it did not obtain confirmation from `Part 9` that the schema version exists.

### 12.10 Boundary with Part 10, reference and master data management

**Delegated.** Classification schemes, effectivity scope reference sets, jurisdiction lists, retention code sets where they are organisation wide, and the governance of all of them.

**Must not absorb.** Vocabulary governance. This component records assignments against a scheme version and must not define the scheme.

**Naive conflation.** Maintaining the classification scheme inside the document component, where it acquires no version identity and no effective date, so that a reclassification cannot be dated and a historical assignment cannot be interpreted.

**Reciprocal.** `Part 10` must declare that it owns scheme and reference set identity and versioning, that it does not delete or reuse member keys, and that it retains superseded scheme versions for at least as long as the longest retention period of anything assigned against them.

**P1-12.18 (MUST) Scheme version recorded with every assignment.** An implementation must record the scheme identity and version with every classification assignment and every scoped effectivity assertion, per clauses P1-3.83 and P1-4.22.

**P1-12.19 (MUST) Scheme snapshot in the package.** An implementation must include the referenced scheme version content in an evidence package, or state that it could not be obtained, per clause P1-8.24.

### 12.11 Boundary with Part 11, content addressed artifact store

**Delegated.** The durable storage of content octets, their addressing by digest, deduplication, replication and retrieval.

**Must not absorb.** Blob storage semantics. This component owns the mapping from a rendition to a digest and a canonical form profile; whether the octets are held here or there is a deployment decision.

**Naive conflation.** The artifact store holding status, effectivity or approval, because it holds the content and appears to be the natural home; or this component implementing its own deduplication, which makes the relation between a rendition and its octets many to one in a way its own model does not express.

**Reciprocal.** `Part 11` must declare that it holds no lifecycle state, that it does not delete content on its own authority, and that it treats a deletion request as an instruction from this component accompanied by a disposition authorisation reference.

**P1-12.20 (MUST) Digest is the interface.** An implementation must address content in `Part 11` by digest under a declared canonical form profile, and must not rely on a location or path as the identity of content.

**P1-12.21 (MUST NOT) No lifecycle in the store.** An implementation must not record status, effectivity, approval, retention or holds in the artifact store, and must not accept them from it.

**P1-12.22 (MUST) Disposition passes through.** An implementation must accompany every destruction instruction to `Part 11` with the disposition authorisation reference, and must record the store's confirmation as part of the disposition execution.

### 12.12 Boundary with Part 12, conformance and assurance harness

**Delegated.** All assessment of whether an implementation satisfies this part, including the verification of the assessments themselves.

**Must not absorb.** Self assessment. Per clause P1-1.10, an implementation must not represent its own checks as an assessment.

**Naive conflation.** A component that reports itself as conformant, which is the condition in which nobody ever discovers that a projection has drifted from its rows.

**Reciprocal.** `Part 12` must declare that it obtains the clause set from this part by resolution, that it records which version of this part an assessment was made against, and that it does not modify any row of this component in the course of assessing it.

**P1-12.23 (MUST) Read only assessment.** An implementation must expose everything `Part 12` requires to assess it through read operations, and must not require a write in order to be assessed.

**P1-12.24 (MUST) Assessed version recorded.** An implementation must record, with any assessment result it stores, the version of this part the assessment was made against, resolved under section 6.2.

### 12.13 Boundary with Part 13, model invocation and agent execution

**Delegated.** The invocation record of a model, its cost, its retry behaviour, its non determinism, and the distinction between a value a model produced and a value that has been checked.

**Must not absorb.** Invocation mechanics. This component records authorship and actor attribution, including where the actor is an automated agent, and nothing about how the agent was invoked.

**Naive conflation.** Two forms, both common. An agent generated draft recorded as authored by the person who requested it, which makes the record of authorship false and removes the only signal that the content requires checking. And an agent recorded as an approver, which is impossible under clause P1-3.57 because an approval must be attributable to a natural person; the agent's act is a status transition, and someone must sign.

**Position taken.** An automated agent may author, may transition status where section 5.3 does not require a signature, and may never sign. The reason is that a signature is an assertion of personal responsibility, and an actor that cannot bear responsibility cannot make it. This position is taken on the basis of 21 CFR 11.100, which requires that an electronic signature be unique to one individual, and is stated as a position rather than as a settled question; see section 13.6.

**Reciprocal.** `Part 13` must declare that it owns the invocation record, that it does not record authorship or approval, and that it obtains the identity of any agent it invokes in a form this component can record as an `ACTOR`.

**P1-12.25 (MUST) Agent authorship recorded as such.** An implementation must record an automated agent as an author or actor where it performed the act, must not attribute the act to the person who requested it, and must record the reference to the invocation record where one exists.

**P1-12.26 (MUST NOT) No agent signature.** An implementation must not accept a signature whose signer is not a natural person, per clause P1-3.57.

**P1-12.27 (MUST) Unchecked content marked.** An implementation must mark a version whose content was produced by an automated agent and has not been the subject of a recorded human review, and must expose the marking to any reader.

### 12.14 Boundary with Part 0, system composition

**Delegated.** What happens when all the components run at once: authority over facts that more than one component touches, the seams at which values cross boundaries, the propagation of non results, consistency and ordering across components, and version pinning across a unit of work.

**Must not absorb.** Composition. This part states its own contract, including the caller obligations in section 7, and does not state what a caller with no representation for a non result must do, nor which component holds authority over a fact this part does not own.

**Reciprocal.** `Part 0` must declare that this component holds authority over document and record identity, version identity, status, effectivity, citation resolution, integrity assertions, retention state and holds, and must state, for every seam at which one of those facts crosses into another component, what must hold and how a violation appears in the record. It must in particular state what a receiving component does with each `NON_RESULT` subclass of section 7.2, since this part specifies only what this component returns.

**P1-12.28 (MUST) Authority declared, not assumed.** An implementation must not accept an assertion about any fact this part allocates to it from another component, and must require that such facts be established by the operations of section 4.2.

**P1-12.29 (MUST) Non result propagation is a composition concern.** An implementation must return the outcomes of section 7 unmodified regardless of whether the caller can represent them, and must not degrade a `NON_RESULT` to a success or a failure in order to fit a caller's model.
## 13. What could not be established

This section is a deliverable rather than a disclaimer. A question recorded as open can be closed by someone with access to the source; a question closed by inference cannot be reopened, because nothing in the document reveals that an inference was made.

### 13.1 Standards not obtained in full text

The following were not available to the author in full text. This part's account of what each supplies rests on published scope statements, forewords, tables of contents, national body summaries, secondary literature and implementation practice. No clause of this part reproduces text from any of them, and no clause should be read as asserting that its requirement appears in them.

ISO 15489-1:2016. Scope, foreword and the fact of its 2021 confirmation were obtained; the clause text was not. The definition of a record given in section 2.1 is reported from secondary sources and should be checked against the standard before this part is approved.

ISO 16175-1:2020 and ISO/TS 16175-2:2020. Scope and exclusions were obtained. The functional requirements themselves were not, so this part cannot state which of its clauses correspond to which of theirs.

ISO 30300:2020, ISO 30301:2019 with Amendment 1:2024, and ISO 30302:2022 with Amendment 1:2025. Editions, amendment status and the fact that a revision of 30301 was in progress were obtained; the text was not.

ISO 23081-1:2017 and the remainder of the 23081 series. Edition confirmed only for Part 1. The metadata element set was not obtained, and section 3.11 is therefore this part's own construction rather than an adoption.

ISO 24143:2022, ISO 17068:2017, ISO 21946, ISO 21965 and ISO 22428. Identified as existing and as members of the family that replaced the withdrawn ISO/TR 15489-2. Not obtained and not assessed.

ISO 13008, on digital records conversion and migration. Not obtained. Its edition was not established, and it is likely to bear on section 3.10.

ISO 23507. Identified as published and adopted from CCSDS 653.0-M-1. Not assessed.

ISO 9001:2015 clause 7.5. The clause's subject matter is well attested in secondary sources and the account in section 10.5 rests on those; the clause text was not obtained. The Final Draft International Standard of the 2026 edition was likewise not obtained, so this part cannot state whether clause 7.5 retains its number or its content.

The July 2025 draft revisions of EU GMP Annex 11 and Chapter 4, and the draft Annex 22. The existence, dates, consultation window and principal areas of change were established from multiple independent secondary sources. The draft text was not obtained. No clause of this part is drawn from the drafts.

By contrast, the following were available in full or substantially: ISO 14721:2025 in its CCSDS form, PREMIS 3.0, MoReq2010, DoD Manual 8180.01, 21 CFR Part 11, and every RFC and W3C recommendation cited in section 10.7. Clauses resting on those are marked in this part as resting on specification text.

**P1-13.1 (MUST) Verification before approval.** An implementation or reviewer must verify the claims listed in section 13.1 against the source standards before this part is approved, and must record the outcome of each verification against this section.

### 13.2 Mandated destruction against erasure rights and holds

Three obligations can apply to one subject and cannot all be satisfied. A retention schedule may require destruction on a date. A hold may forbid destruction. A data protection erasure right may require removal of personal data. A regulated audit trail requirement may require retention of the audit record for at least as long as the record it describes, which means that destroying the record while retaining its audit trail leaves personal data in the trail.

This part specifies the mechanism by which each is recorded and the precedence rule for competing retention periods, in clauses P1-3.86 through P1-3.92. It takes no position on which obligation prevails, because the answer is jurisdictional and none of the instruments named in section 10 addresses the collision. The common practice of cryptographic erasure is discouraged in clause P1-3.94 on the ground that it substitutes an assumption about future cryptanalysis for a recorded act, but that discouragement is a position taken by this part and not a finding.

**Open.** Whether an append only store of the kind this part requires can satisfy an erasure obligation at all, and if so by what mechanism that does not defeat the integrity properties of section 8.8. This is the single largest unresolved question bearing on this part.

### 13.3 No crosswalk between the property vocabularies

ISO 15489-1 names authenticity, reliability, integrity and usability as the properties of a record. The ALCOA family names attributable, legible, contemporaneous, original and accurate, extended in the plus form by complete, consistent, enduring and available, and in more recent European guidance by traceability. OAIS speaks of independently understandable content and, from its third edition, of preservation objectives. No published crosswalk between these vocabularies was found, and the sets are not co extensive.

This part deliberately organises itself around neither vocabulary, using instead the purpose question of section 1.1. That is a choice, and a reviewer may reasonably hold that it should instead be organised around one of them.

**Open.** Whether a defensible mapping exists, and whether the absence of one is an accident of separate professional traditions or evidence that the sets are measuring different things.

### 13.4 Withdrawal, obsolescence and expiry are not distinguished in any source found

This part distinguishes supersession, withdrawal and obsolescence, in section 2.1 and section 5, and allocates the first two to a version and the third to a lineage. No normative source was found that draws these lines, or any lines, among the terms. Practice uses them interchangeably, and quality management systems commonly use "obsolete" for what this part calls withdrawn.

The distinction is retained here because the three conditions have different consequences for citation resolution, and because a reader of an old determination needs to know whether the instrument it relied on was replaced, revoked or retired. But the terminology is this part's own.

**Open.** Whether any records management or quality standard defines these terms normatively. The ISO/TC 46 vocabulary standard, ISO 30300:2020, is the most likely place and was not obtained.

### 13.5 Retroactive effectivity

This part permits an effectivity assertion whose application time precedes its knowledge time, in clause P1-3.49, and requires it to be flagged. No source was found that either permits or forbids this. The regulated data integrity literature treats backdating as a serious defect, but backdating in that literature means recording an act as having occurred at a time other than when it occurred, which clause P1-6.25 and clause P1-6.26 prohibit absolutely. Asserting today that a document has governed since an earlier date is a different act, and it is sometimes the only truthful thing to record.

**Open.** Whether the distinction this part draws between backdating an act and retroactively asserting effectivity is recognised anywhere, and whether a regulator would accept it. The practical consequence of getting this wrong is significant, because the alternative designs are to refuse to record the situation or to record it as though the document had been approved earlier.

### 13.6 Whether a non human actor may sign

Clause P1-3.57 and clause P1-12.26 require that a signer be a natural person, on the basis of the requirement in 21 CFR 11.100 that an electronic signature be unique to one individual. That requirement was written in 1997 and addresses shared credentials rather than automated agents.

**Open.** Whether the requirement bears the weight this part places on it. An argument can be made that an agent operating under a recorded delegation, with an invocation record and an accountable owner, satisfies the purpose of attribution better than a person who clicks approve without reading. This part takes the conservative position and records that it is a position. The draft EU GMP Annex 22 on artificial intelligence may bear on the question; it was not obtained.

### 13.7 Clause level citation stability

Every citation practice in law, standards and regulation depends on the stability of clause identifiers across revisions. No specification was found that requires it, states how a clause identifier should be assigned, or says what a citation to a deleted clause resolves to. The mechanism in clauses P1-3.104 through P1-3.106 and section 6.4 is this part's own construction.

**Open.** Whether any standards development organisation has published its internal rules for identifier assignment and retirement in a form that could be cited.

### 13.8 Long term signature validation

Clause P1-8.28 requires that signature validation material be included in an evidence package, and clause P1-3.122 recommends evidence records under RFC 4998 or RFC 6283 where the retention horizon exceeds the cryptographic lifetime of the algorithms in use. Both are sound as far as they go. Neither answers what a reader in forty years does with a signature whose entire trust anchor, including the certification authority and the algorithms, has ceased to exist in any operational form.

**Open.** Whether a signature can be made verifiable across an interval longer than the institutional lifetime of the infrastructure that produced it, or whether the honest answer is that beyond some horizon a signature becomes a recorded assertion that a signature was verified at a time when verification was possible. If the latter, this part's requirements are correct but its expectations should be restated.

### 13.9 Effectivity scope

Section 3.4 and section 3.8 make scope a first class part of the uniqueness invariant, and clause P1-3.54 forbids inheritance from a parent scope or a fallback to `GLOBAL`. The prohibition is deliberate: fallback produces silent application of a document in a scope for which nobody asserted it. No source was found that treats scoped effectivity at all.

**Open.** Whether scopes need a hierarchy, and if so whether resolution should traverse it. This part says no and requires an explicit assertion per scope, which is more laborious and less surprising. A reviewer may reasonably prefer the opposite, and the decision should be recorded either way.

### 13.10 Identity where content is identical

Two lineages may have identical content, and the same version content may be published under two lineages. `Part 11` deduplicates octets by digest, which is correct at that layer. This part gives identity to the lineage and version rather than to the content, which means identical content can be in force in one place and withdrawn in another.

**Open.** Whether that is the right allocation. It follows from the observation that what governs is an instrument rather than a text, but it has the consequence that an organisation can hold two instruments with the same words and different force, and no clause of this part detects it.

### 13.11 Knowledge time in federated capture

Clause P1-6.25 requires the component to assign knowledge time itself. Where a record is captured by a remote system and transmitted later, the knowledge time this component assigns is the time it learned of the record, not the time the capturing system did. The `OTIME` carries the act, but the remote system's own knowledge time is lost.

**Open.** Whether a third time dimension is required for federated capture, or whether the source system's knowledge time should be carried as a metadata element. This part does not require it, and a reviewer should consider whether that is adequate for content captured through intermediaries.

### 13.12 Claims in this part that rest on practice

The following clauses rest on practice rather than on specification text, and are marked here so that a reader can see the whole set at once: clause P1-3.3 on the identifier scheme; clause P1-3.35 on rendered renditions as authoritative; clause P1-3.94 on cryptographic erasure; clause P1-3.121 on scheduled fixity checking; clause P1-3.123 on archiving profile implementations; clause P1-6.32 on leap second declaration; clause P1-8.7 on recording all reads; clause P1-8.37 on independent anchoring; clause P1-9.12 on paired locators; clause P1-9.15 on deprecated algorithms; and every clause in section 11 whose entry is marked as resting on practice.

**P1-13.2 (MUST) Practice basis recorded.** An implementation that adopts a clause listed in section 13.12 as a control must record that its basis is practice, per clause P1-10.7.

### 13.13 What this part deliberately did not attempt

No conformance assessment of any system against this part was performed or anticipated, per section 1 and clause P1-1.10.

No transport, encoding, schema or naming convention is specified, and no reference implementation is offered.

No performance, scale or availability requirement is stated. The model of section 3 has evident implications for read cost, and nothing here addresses them, because a threshold stated without a workload is not a requirement.

No treatment of paper originals, hybrid holdings or the digitisation of analogue records is given. ISO 16175-1 explicitly excludes analogue records from its functional requirements and this part follows it, but an organisation with hybrid holdings will find a gap here.

No treatment of email, instant messaging or collaborative editing artifacts as records is given, though they are the largest practical source of records in most organisations.

**P1-13.3 (MUST) Gaps declared, not filled.** An implementation must not represent a matter listed in section 13.13 as specified by this part.

**P1-13.4 (SHOULD) Open questions carried forward.** A reviewer of this part should record a position on each open question in section 13, and where a position is adopted it should be recorded in the review outcome rather than by silent amendment of the clause it affects.

### 13.14 Questions handed to Part 0 rather than answered here

Section 7 states what this component returns and what a caller is obliged to do with it. It does not and cannot state what happens when a caller has no representation for a value it returns, which is the failure mode described in section 7.1. That is a composition property and belongs to `Part 0`, together with the following, each of which was identified while authoring this part and is recorded here so that `Part 0` inherits it rather than rediscovering it.

What a component receiving `NOT_IN_FORCE_AT_TIME` must record, and what it must not conclude.

Which component holds authority over the identity of an actor, since this part treats it as opaque and at least three other parts need it.

How a version is pinned across a unit of work that touches several components, so that all of them resolve against the same version.

What happens when a determination's provenance in `Part 3` and a citation resolution in this component disagree about which version was used.

Whether a retention obligation recorded here can bind the disposal behaviour of `Part 11` and `Part 3`, which hold copies of or references to the same content.

How the divergence signal of clause P1-3.101 reaches the owner of a determination made years earlier in a component that may since have been replaced.
