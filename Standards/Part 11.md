# KAIROS STD 003 Part 11: Content Addressed Artifact Store

**Standard.** KAIROS STD 003, the enterprise architecture standard.
**Part.** Part 11 of 14 (Part 0 and Parts 1 through 13). Cited as `KAIROS STD 003 Part 11`.
**Title.** Content addressed artifact store.
**Version.** 1.0.0.
**Status.** Proposed. This part has not been approved and is not effective. It is issued for review against the authoring brief of 2026-08-17.
**Date of issue.** 2026-08-18.
**Supersedes.** Nothing. This is the first version.

## Binding of requirement language

The key words MUST, MUST NOT, SHOULD, SHOULD NOT and MAY in this part are to be interpreted as described in RFC 2119 and RFC 8174, and only in the upper case forms. This part does not use SHALL, SHALL NOT, REQUIRED, RECOMMENDED, NOT RECOMMENDED or OPTIONAL as requirement keywords.

Every requirement in this part is a numbered clause. A clause identifier has the form `P11-S.N`, where `S` is the section number and `N` is the ordinal of the clause within that section. Clause identifiers are permanent. A clause that is later removed has its identifier retired and never reissued. A clause that is later added to a section takes the next unused ordinal in that section, so ordinals are stable but not contiguous over the life of the part.

Text that is not a numbered clause is not binding. Narrative, tables, algorithms, examples and the discussion of standards are provided to make the clauses intelligible and testable, and where a table carries normative content a clause says so explicitly and names the table.

Where a clause carries a **Source.** note, the note states the specification or published work on which the clause's subject rests and whether this part adopts that treatment or departs from it. The note is narrative and not binding; the clause governs.

## Conformance

An implementation conforms to this part if it satisfies every MUST and MUST NOT clause and records, for each SHOULD and SHOULD NOT clause it does not satisfy, the reason. This part does not define conformance levels, profiles or a certification scheme, and it does not define the method of assessment. Assessment method is the subject of `KAIROS STD 003 Part 12` and is out of scope here.

Where a clause states that a value is an implementation decision, conformance requires that the implementation declare the value, not that it adopt a particular one. An undeclared implementation decision is a nonconformity.

## Clause index

The index below is generated from the clause text of this document. It lists every clause identifier, its modality and its subject label. The counts that follow the index are derived by the same extraction and are stated with the grain at which they were counted.

| Clause | Modality | Subject |
| --- | --- | --- |
| P11-1.1 | MUST | Octets owned |
| P11-1.2 | MUST | Addresses owned |
| P11-1.3 | MUST | Address profiles owned |
| P11-1.4 | MUST | Algorithm register owned |
| P11-1.5 | MUST | Composite structure owned |
| P11-1.6 | MUST | Ingest records owned |
| P11-1.7 | MUST | Retrieval records owned |
| P11-1.8 | MUST | Fixity records owned |
| P11-1.9 | MUST | Referrer registrations owned |
| P11-1.10 | MUST | Tombstones owned |
| P11-1.11 | MUST | Aliases owned |
| P11-1.12 | MUST | Placement declarations owned |
| P11-1.13 | MUST | Deduplication scope owned |
| P11-1.14 | MUST NOT | Not a record of any determination |
| P11-1.15 | MUST NOT | Not the meaning of what it holds |
| P11-1.16 | MUST NOT | Not a schema authority |
| P11-1.17 | MUST NOT | Not the document authority |
| P11-1.18 | MUST NOT | Not the audit ledger |
| P11-1.19 | MUST NOT | Not a decision point for access |
| P11-1.20 | MUST NOT | Not a reference authority |
| P11-1.21 | MUST NOT | Not a deleter on its own authority |
| P11-1.22 | MUST NOT | Not a mutator |
| P11-1.23 | MUST NOT | Not an assessor of itself |
| P11-1.24 | MUST NOT | Not a work manager |
| P11-1.25 | MUST NOT | Not an identity for the thing the content describes |
| P11-1.26 | MUST NOT | No conformance assessment anticipated |
| P11-2.1 | MUST NOT | No redefinition of another part's terms |
| P11-2.2 | MUST NOT | Address not equated with digest |
| P11-2.3 | MUST NOT | Address not equated with location |
| P11-2.4 | MUST NOT | Artifact not equated with alias |
| P11-2.5 | MUST NOT | Deletion not equated with redaction |
| P11-2.6 | MUST NOT | Fixity not equated with durability |
| P11-2.7 | MUST NOT | Verification not equated with retrieval |
| P11-2.8 | MUST | Kinds registered before use |
| P11-3.1 | MUST | Types declared |
| P11-3.2 | MUST | Length recorded separately from the digest |
| P11-3.3 | MUST NOT | No representation dependent identity |
| P11-3.4 | MUST | Address self describing |
| P11-3.5 | MUST NOT | No bare digest accepted as an address |
| P11-3.6 | MUST | Profile identified in the address |
| P11-3.7 | MUST NOT | No inference of a profile |
| P11-3.8 | MUST | Digest length encoded |
| P11-3.9 | MUST | Address parse failure distinguished |
| P11-3.10 | MUST | Inventory normative |
| P11-3.11 | MUST | Immutability observed |
| P11-3.12 | MUST | Profile immutable in effect |
| P11-3.13 | MUST | One profile per address |
| P11-3.14 | MUST | Canonicalisation declared, never assumed |
| P11-3.15 | MUST NOT | No canonicalisation performed here |
| P11-3.16 | MUST | Chunker registered with its parameters |
| P11-3.17 | MUST | Content defined chunkers declare their bounds |
| P11-3.18 | MUST NOT | No profile change applied retrospectively |
| P11-3.19 | MUST | Record present for every artifact |
| P11-3.20 | MUST | Zero length artifact addressable |
| P11-3.21 | MUST NOT | No claimed content type relied upon |
| P11-3.22 | MUST | Ingest count maintained |
| P11-3.23 | MUST NOT | No artifact record deletion |
| P11-3.24 | MUST | Assembly recorded, not inferred |
| P11-3.25 | MUST | Reconstitution deterministic |
| P11-3.26 | MUST | Part addresses under the same profile |
| P11-3.27 | MUST NOT | No composite address treated as a function of content alone |
| P11-3.28 | MUST | Equivalent roots recorded, never merged |
| P11-3.29 | MUST | Depth bounded |
| P11-3.30 | MUST NOT | No part shared across profiles silently |
| P11-3.31 | MUST | Domain separation applied to every tree |
| P11-3.32 | MUST | Domain separation scheme registered |
| P11-3.33 | MUST NOT | No unprefixed tree accepted |
| P11-3.34 | MUST | Single part tree defined |
| P11-3.35 | MUST | Odd node handling declared |
| P11-3.36 | MUST | More than one algorithm supported |
| P11-3.37 | MUST | Status governs use |
| P11-3.38 | MUST | Collision resistance status recorded |
| P11-3.39 | MUST NOT | No cross algorithm digest comparison |
| P11-3.40 | MUST | Rebinding recorded, original retained |
| P11-3.41 | MUST | Rebinding verified before recording |
| P11-3.42 | MUST NOT | No silent address substitution |
| P11-3.43 | MUST | Address computed by the store |
| P11-3.44 | MUST | Claimed address compared and recorded |
| P11-3.45 | MUST | Claim absence recorded |
| P11-3.46 | MUST NOT | No ingest record deletion |
| P11-3.47 | MUST | Retrieval recorded, including failures |
| P11-3.48 | MUST | Verification state declared on every retrieval |
| P11-3.49 | MUST NOT | No unverified return presented as verified |
| P11-3.50 | MUST | Partial verification extent recorded |
| P11-3.51 | MUST | Referrer registration accepted |
| P11-3.52 | MUST | Retention floor derived from registrations |
| P11-3.53 | MUST NOT | No deletion below the floor |
| P11-3.54 | MUST NOT | No inference of absence of referrers |
| P11-3.55 | MUST | Undeclared referrer population exposed |
| P11-3.56 | MUST | Withdrawal of a registration recorded, not erased |
| P11-3.57 | MUST | Floor rise notified |
| P11-3.58 | MUST | Tombstone on every removal |
| P11-3.59 | MUST | Tombstone resolves |
| P11-3.60 | MUST | Redaction retains the address record |
| P11-3.61 | MUST | Redaction records its scope |
| P11-3.62 | MUST NOT | No erasure claim |
| P11-3.63 | MUST | Referrers notified of removal |
| P11-3.64 | MUST | Verification impossibility recorded |
| P11-3.65 | MUST NOT | No tombstone reuse |
| P11-3.66 | MUST | Alias syntactically distinguishable from an address |
| P11-3.67 | MUST | Every rebinding recorded |
| P11-3.68 | MUST | Resolution recorded |
| P11-3.69 | MUST NOT | No alias in a citation |
| P11-3.70 | MUST | Point in time alias resolution answerable |
| P11-3.71 | MUST NOT | No alias deletion without a tombstone |
| P11-3.72 | MUST | Fixity is recorded, not assumed |
| P11-3.73 | MUST | Passes recorded as well as failures |
| P11-3.74 | MUST | Cadence declared per class |
| P11-3.75 | MUST | Never verified population exposed |
| P11-3.76 | MUST | Replica identified per verification |
| P11-3.77 | MUST | Sampled verification declared as sampled |
| P11-3.78 | MUST | Failure quarantines, never deletes |
| P11-3.79 | MUST NOT | No failure returned as absence |
| P11-3.80 | MUST | Scope declared |
| P11-3.81 | MUST NOT | No digest accepted as proof of possession |
| P11-3.82 | MUST NOT | No observable cross tenant deduplication |
| P11-3.83 | MUST | Response timing controlled where the boundary is global |
| P11-3.84 | MUST NOT | No storage accounting signal |
| P11-3.85 | MUST | Client side deduplication declared and bounded |
| P11-3.86 | MUST | Deduplication recorded per submission |
| P11-3.87 | MUST | Encryption disposition recorded |
| P11-3.88 | MUST NOT | No fixity claim over opaque content it cannot read |
| P11-3.89 | MUST | Address is over what was submitted |
| P11-3.90 | MUST NOT | No convergent encryption without a declared exposure |
| P11-3.91 | MUST | Key custody separated from content custody |
| P11-3.92 | MUST | Replica count and independence recorded |
| P11-3.93 | MUST NOT | No unverified independence presented as verified |
| P11-3.94 | MUST | Durability claim carries its basis |
| P11-3.95 | MUST | Single replica exposed |
| P11-3.96 | MUST | Projections marked as such |
| P11-3.97 | MUST | Content listing is a projection |
| P11-3.98 | MUST NOT | No enumeration that omits tombstones silently |
| P11-4.1 | MUST | Operations defined over the entities of section 3 |
| P11-4.2 | MUST | Idempotency inherent for ingest |
| P11-4.3 | MUST | Idempotency key accepted for state changing operations |
| P11-4.4 | MUST | Authorisation obtained per operation |
| P11-4.5 | MUST NOT | No authorisation inferred from address knowledge |
| P11-4.6 | MUST | One outcome per operation |
| P11-4.7 | MUST | Refusals recorded |
| P11-4.8 | MUST NOT | No operation that mutates content |
| P11-4.9 | MUST | Profile named on submission |
| P11-4.10 | MUST | Length compared where declared |
| P11-4.11 | MUST | Assembly declared before a root is minted |
| P11-4.12 | MUST NOT | No probe that reveals another party's holding |
| P11-4.13 | MUST | Challenge answerable only from content |
| P11-4.14 | MUST | Failed challenge recorded |
| P11-4.15 | MUST | Verification declaration returned to the caller |
| P11-4.16 | MUST | Range retrieval declares its verification limit |
| P11-4.17 | MUST | Part retrieval verifiable independently |
| P11-4.18 | MUST | Describe available for a tombstone |
| P11-4.19 | MUST NOT | No content returned for quarantined content |
| P11-4.20 | MUST | Verify available without retrieval |
| P11-4.21 | MUST | Deletion refused below the floor |
| P11-4.22 | MUST | Deletion refused under legal hold |
| P11-4.23 | MUST | Removal names its referrers |
| P11-4.24 | MUST NOT | No deletion of the last replica without a declared act |
| P11-4.25 | MUST | Rebinding verified first |
| P11-4.26 | MUST | Legal hold overrides a deletion already requested |
| P11-4.27 | MUST | Content at an address never changes |
| P11-4.28 | MUST NOT | No assumption of verification |
| P11-4.29 | MUST NOT | No assumption of durability from success |
| P11-4.30 | MUST NOT | No assumption that absence means never existed |
| P11-4.31 | MUST NOT | No assumption of convergence across profiles |
| P11-4.32 | MUST NOT | No assumption that an alias is stable |
| P11-4.33 | MUST | Describe answers where retrieve does not |
| P11-4.34 | MUST | Reads treated as fallible |
| P11-4.35 | MUST NOT | No proceeding on an authorisation failure |
| P11-4.36 | MUST NOT | No removal on an unresolvable retention schedule |
| P11-4.37 | MUST | Event per state transition |
| P11-4.38 | MUST | Event carries prior state and cause |
| P11-4.39 | MUST | Events delivered to the ledger |
| P11-4.40 | MUST | Fixity failure event distinct |
| P11-4.41 | MUST | Removal event names the referrers |
| P11-4.42 | MUST | Algorithm status change event |
| P11-4.43 | MUST | Unverified retrieval event where a threshold is breached |
| P11-4.44 | SHOULD | Single replica signal |
| P11-5.1 | MUST | States held as transitions |
| P11-5.2 | MUST | One state per axis per instant |
| P11-5.3 | MUST NOT | No derivation of one axis from another |
| P11-5.4 | MUST | Transitions carry authorisation where required |
| P11-5.5 | MUST | Illegal transitions recorded |
| P11-5.6 | MUST NOT | No unlisted transition |
| P11-5.7 | MUST | Deleted is the only terminal state |
| P11-5.8 | MUST | Quarantine is not terminal |
| P11-5.9 | MUST | Degraded distinguished from held |
| P11-5.10 | MUST | Repair verified before reinstatement |
| P11-5.11 | MUST NOT | No transition out of redacted to held |
| P11-5.12 | MUST | Superseded algorithm binding still resolves |
| P11-5.13 | MUST | Tombstoned binding resolves to the tombstone |
| P11-5.14 | MUST | Never verified distinguished from verified |
| P11-5.15 | MUST | Due distinguished from failed |
| P11-5.16 | MUST | Unverifiable declared |
| P11-5.17 | MUST NOT | No fixity state terminal |
| P11-5.18 | MUST | Unbound distinguished from retired |
| P11-5.19 | MUST | Resolution history retained on retirement |
| P11-5.20 | MUST | Replica state held per replica |
| P11-5.21 | MUST | Corrupt replica retained pending repair |
| P11-5.22 | MUST | Artifact state derived from replica states declared |
| P11-5.23 | MUST | Unreachable referrer recorded, not withdrawn |
| P11-5.24 | MUST | Unreachable referrers still bind the floor |
| P11-6.1 | MUST | Address computation deterministic |
| P11-6.2 | MUST NOT | No environmental input to an address |
| P11-6.3 | MUST | Verification deterministic |
| P11-6.4 | MUST | Reproducible from the profile alone |
| P11-6.5 | MUST NOT | No clock in addressing or verification |
| P11-6.6 | MUST | Profile status checked at ingest |
| P11-6.7 | MUST | Length counted, not trusted |
| P11-6.8 | MUST NOT | No partial artifact addressed as whole |
| P11-6.9 | MUST | Interrupted submission leaves no address |
| P11-6.10 | MUST NOT | No referrer registration created by ingest |
| P11-6.11 | MUST | Deduplication decided within the declared scope only |
| P11-6.12 | MUST | Possession requirement applied on every claimed duplicate |
| P11-6.13 | MUST NOT | No content served on an unanswered challenge |
| P11-6.14 | MUST | Challenge derived from content, not from its address |
| P11-6.15 | MUST | Constant response profile where required |
| P11-6.16 | MUST | Deduplication proportion derivable |
| P11-6.17 | MUST NOT | No deduplication across a classification boundary |
| P11-6.18 | MUST | Assembly verified on declaration |
| P11-6.19 | MUST | Root recomputed on declaration |
| P11-6.20 | MUST | Reconstitution verified against the root |
| P11-6.21 | MUST | Missing part named |
| P11-6.22 | MUST | Traversal depth bounded |
| P11-6.23 | MUST | Cycle refused |
| P11-6.24 | MUST | Verification performed by default |
| P11-6.25 | MUST | Conditions permitting unverified return declared |
| P11-6.26 | MUST | Verification failure returned as such |
| P11-6.27 | MUST | Verification failure quarantines |
| P11-6.28 | MUST | Streaming verification declared |
| P11-6.29 | MUST NOT | No verification of a range presented as verification of the whole |
| P11-6.30 | MUST | Repair attempted before failure returned where a replica may be good |
| P11-6.31 | MUST | Cadence applied per class |
| P11-6.32 | MUST | Cadence breach exposed |
| P11-6.33 | MUST | Every replica within the cadence |
| P11-6.34 | MUST | Sampling parameters declared |
| P11-6.35 | MUST NOT | No sampled verification counted as full |
| P11-6.36 | MUST | Verification of opaque content bounded to the ciphertext |
| P11-6.37 | MUST | Migration is additive |
| P11-6.38 | MUST | Migration population countable |
| P11-6.39 | MUST | Rebinding records both addresses |
| P11-6.40 | MUST NOT | No cross algorithm equivalence asserted without verification |
| P11-6.41 | MUST | Withdrawal from minting distinguished from withdrawal from resolution |
| P11-6.42 | MUST NOT | No deletion on the store's own initiative |
| P11-6.43 | MUST | Floor evaluated at the instant of effect |
| P11-6.44 | MUST | Removal refused where the referrer population is unknown and the policy requires it |
| P11-6.45 | MUST | Reference counting is not a substitute for the floor |
| P11-6.46 | MUST | Parts of a composite removed only with the composite |
| P11-6.47 | MUST | Shared part removal refused |
| P11-6.48 | MUST | Redaction of a part propagates a declaration |
| P11-6.49 | MUST | Removal notification attempted and recorded |
| P11-6.50 | MUST | Concurrent identical submissions converge |
| P11-6.51 | MUST | Concurrent removal and retrieval serialised |
| P11-6.52 | MUST | Concurrent alias rebinding serialised |
| P11-6.53 | MUST | Maximum artifact size declared |
| P11-6.54 | MUST | Maximum part count declared |
| P11-6.55 | MUST | Bounds recorded on the operation |
| P11-6.56 | MUST | Addressing and verification only |
| P11-6.57 | MUST NOT | No content inspection |
| P11-6.58 | MUST NOT | No derived representation stored as content |
| P11-7.1 | MUST | One enumeration per value |
| P11-7.2 | MUST NOT | No value outside the enumerations |
| P11-7.3 | MUST | Properties of an outcome exposed |
| P11-7.4 | MUST | Never held distinguished from removed |
| P11-7.5 | MUST NOT | No integrity failure returned as absence |
| P11-7.6 | MUST NOT | No transient unavailability reported as absence |
| P11-7.7 | MUST | Redacted distinguished from deleted |
| P11-7.8 | MUST | Incomplete composite names the missing part |
| P11-7.9 | MUST | Authorisation refusal distinguished from absence |
| P11-7.10 | MUST | Authorisation refusal indistinguishable in effect where the scope requires it |
| P11-7.11 | MUST | Malformed address distinguished from unknown address |
| P11-7.12 | MUST | Algorithm and profile failures distinguished |
| P11-7.13 | MUST | Stored distinguished from deduplicated |
| P11-7.14 | MUST NOT | No deduplication reported before possession is satisfied |
| P11-7.15 | MUST | Claim mismatch reported as such |
| P11-7.16 | MUST | Tombstoned address refused explicitly |
| P11-7.17 | MUST NOT | No sampled pass reported as verified |
| P11-7.18 | MUST NOT | No incomplete read reported as a mismatch |
| P11-7.19 | MUST | Non comparability distinguished from failure |
| P11-7.20 | MUST | Unverifiable causes distinguished |
| P11-7.21 | MUST | Refusal reasons distinguished |
| P11-7.22 | MUST | Loss recorded as loss |
| P11-7.23 | MUST NOT | No loss reported as an authorised removal |
| P11-7.24 | MUST NOT | No fault reported as a statement about content |
| P11-7.25 | MUST | Unsatisfiable placement refuses the ingest |
| P11-7.26 | MUST | Invariant violation halts the affected content |
| P11-7.27 | MUST | Three properties exposed |
| P11-7.28 | MUST | Outcome carried whole |
| P11-7.29 | MUST NOT | No aggregation losing the distinctions |
| P11-7.30 | MUST | Non results retained where unconsumed |
| P11-7.31 | MUST | Counts report each outcome as its own category |
| P11-8.1 | MUST | Completeness of each record declared |
| P11-8.2 | MUST NOT | No citation figure presented as complete |
| P11-8.3 | MUST | Grain stated with every count |
| P11-8.4 | MUST | Artifact counts state their state filter |
| P11-8.5 | MUST | Octet counts state whether they are logical or physical |
| P11-8.6 | MUST | Composite counts state their unit |
| P11-8.7 | MUST NOT | No replica count reported as an artifact count |
| P11-8.8 | MUST | Every submission recorded |
| P11-8.9 | MUST | Every retrieval recorded |
| P11-8.10 | MUST | Every verification recorded |
| P11-8.11 | MUST | Every removal and refusal recorded |
| P11-8.12 | MUST | Every referrer registration and withdrawal recorded |
| P11-8.13 | MUST | Every alias rebinding and resolution recorded |
| P11-8.14 | MUST | Divergence between recorded and returned outcome recorded |
| P11-8.15 | MUST | Every rebinding recorded |
| P11-8.16 | MUST | Every placement change recorded |
| P11-8.17 | MUST | Every possession challenge recorded |
| P11-8.18 | MUST | The profile behind any address |
| P11-8.19 | MUST | The assembly behind any composite address |
| P11-8.20 | MUST | The custody history of any artifact |
| P11-8.21 | MUST | The verification state of any retrieval |
| P11-8.22 | MUST | The referrers at the instant of a removal |
| P11-8.23 | MUST | The reason content is no longer retrievable |
| P11-8.24 | MUST | What an alias resolved to at an instant |
| P11-8.25 | MUST NOT | No reconstruction dependent on this component running |
| P11-8.26 | MUST | Never verified population |
| P11-8.27 | MUST | Overdue verification population |
| P11-8.28 | MUST | Unverified retrieval proportion |
| P11-8.29 | MUST | Quarantine population |
| P11-8.30 | MUST | Unrecoverable loss population |
| P11-8.31 | MUST | Single replica population |
| P11-8.32 | MUST | Degraded placement population |
| P11-8.33 | MUST | Unregistered citation population |
| P11-8.34 | MUST | Broken algorithm population |
| P11-8.35 | MUST | Deprecated profile population |
| P11-8.36 | MUST | Unreachable referrer population |
| P11-8.37 | MUST | Failed possession challenge rate |
| P11-8.38 | MUST | Opaque content proportion |
| P11-8.39 | SHOULD | Deduplication sharing distribution |
| P11-8.40 | MUST | Package assemblable for an artifact |
| P11-8.41 | MUST | Package states what it omits |
| P11-8.42 | MUST | Package integrity protected |
| P11-8.43 | MUST | Package assemblable for a tombstone |
| P11-8.44 | MUST | Records outlive content |
| P11-8.45 | MUST NOT | No alteration of an ingest, retrieval, verification or removal record |
| P11-8.46 | MUST NOT | No alteration of an address binding |
| P11-8.47 | MUST NOT | No removal of a tombstone |
| P11-8.48 | MUST | Legal hold refuses every disposition |
| P11-9.1 | MUST | Closed sets not extended |
| P11-9.2 | MUST | Open sets extended only through a registry |
| P11-9.3 | MUST NOT | No new state for a new storage technology |
| P11-9.4 | MUST | Registration before use |
| P11-9.5 | MUST | Definition mandatory at registration |
| P11-9.6 | MUST | Registration attributable |
| P11-9.7 | MUST NOT | No meaning change under a registered identifier |
| P11-9.8 | MUST | Retirement recorded, content retained |
| P11-9.9 | MUST | Specification reference recorded |
| P11-9.10 | MUST | Digest length recorded |
| P11-9.11 | MUST | Status transitions recorded |
| P11-9.12 | MUST | At least one accepted algorithm at all times |
| P11-9.13 | MUST NOT | No truncated digest admitted as a distinct algorithm without registration |
| P11-9.14 | MUST | Every parameter recorded |
| P11-9.15 | MUST | Profile versioned, never edited |
| P11-9.16 | MUST | Deprecation does not withdraw resolution |
| P11-9.17 | MUST | Default profile declared, never implicit |
| P11-9.18 | MUST | Structure fully specified at registration |
| P11-9.19 | MUST | Domain separation tags recorded |
| P11-9.20 | MUST NOT | No structure without domain separation for a tree |
| P11-9.21 | MUST | Scope boundary and controls recorded |
| P11-9.22 | MUST NOT | No scope broadening without a recorded act |
| P11-9.23 | MUST | Location classes registered with an independence basis |
| P11-9.24 | MUST | Content classes registered with a cadence |
| P11-10.1 | MUST | Cited edition recorded |
| P11-10.2 | MUST | Basis marked |
| P11-10.3 | MUST | Algorithm specification cited by edition |
| P11-10.4 | MUST | Requirements of this part alone identified |
| P11-11.1 | MUST | Address self describing |
| P11-11.2 | MUST | Chunking recorded in the profile and the profile in the address |
| P11-11.3 | MUST | Verification state declared on every retrieval |
| P11-11.4 | MUST NOT | No integrity failure as absence |
| P11-11.5 | MUST | Loss recorded as loss |
| P11-11.6 | MUST NOT | No digest as possession |
| P11-11.7 | MUST NOT | No observable cross tenant deduplication |
| P11-11.8 | MUST NOT | No expiry by age or access |
| P11-11.9 | MUST NOT | No collection on a zero declared count |
| P11-11.10 | MUST NOT | No alias in a citation |
| P11-11.11 | MUST NOT | No entitlement from address knowledge |
| P11-11.12 | MUST NOT | No content inspection |
| P11-11.13 | MUST | Repair restores the octets or fails |
| P11-11.14 | MUST | Single replica population exposed |
| P11-11.15 | MUST | Never verified population exposed |
| P11-11.16 | MUST NOT | No sampled verification reported as full |
| P11-11.17 | MUST | Replica identified per verification |
| P11-11.18 | MUST NOT | No deletion below the floor on the submitter's request |
| P11-11.19 | MUST NOT | No erasure claim beyond custody |
| P11-11.20 | MUST | Redaction retains the record |
| P11-11.21 | MUST | Migration additive |
| P11-11.22 | MUST NOT | No convergent deduplication without a declared exposure |
| P11-11.23 | MUST | Key custody separated |
| P11-11.24 | MUST NOT | No location as identity |
| P11-12.1 | MUST | Retention schedule obtained |
| P11-12.2 | MUST | Disposition authorised, never scheduled |
| P11-12.3 | MUST | Records treated as records |
| P11-12.4 | MUST | Address supplied as a citable identity |
| P11-12.5 | MUST NOT | No content policy evaluated here |
| P11-12.6 | MUST | Octets supplied for evaluation, not evaluated |
| P11-12.7 | MUST | Events emitted to the ledger |
| P11-12.8 | MUST NOT | No chain asserted |
| P11-12.9 | MUST | Retention notification accepted |
| P11-12.10 | MUST | Package material addressed, not inlined |
| P11-12.11 | MUST NOT | No descriptive metadata held |
| P11-12.12 | MUST | Address supplied for a governed artifact |
| P11-12.13 | MUST NOT | No selection among candidate addresses |
| P11-12.14 | MAY | Replica selection permitted |
| P11-12.15 | MUST | State is a fact, not a position |
| P11-12.16 | MUST | Retrieval independent of any process |
| P11-12.17 | MUST | Authorisation obtained per operation |
| P11-12.18 | MUST NOT | No authorisation decision rendered |
| P11-12.19 | MUST NOT | No decision, provenance or policy state held |
| P11-12.20 | MUST | Refusal recorded without leaking holdings |
| P11-12.21 | MUST NOT | No association held |
| P11-12.22 | MUST | Unresolvable distinguished from absent |
| P11-12.23 | MUST | Investigation obtained, not managed |
| P11-12.24 | MUST | Quarantine population exposed outside the store |
| P11-12.25 | MUST NOT | No validation performed |
| P11-12.26 | MUST NOT | No address offered as a schema identity |
| P11-12.27 | MUST | Canonicalised octets accepted as submitted |
| P11-12.28 | MUST | Event payload schema obtained |
| P11-12.29 | MUST NOT | No reference content interpreted |
| P11-12.30 | MUST | Address immutability declared |
| P11-12.31 | MUST | Party identities obtained |
| P11-12.32 | MUST | Unresolvable cause supplied |
| P11-12.33 | MUST | State exposed for verification |
| P11-12.34 | MUST NOT | No self assurance |
| P11-12.35 | MUST | Independent verification supported |
| P11-12.36 | MUST | Outcome taxonomy testable |
| P11-12.37 | MUST NOT | No provenance attribute held |
| P11-12.38 | MUST | Address supplied for invocation material |
| P11-12.39 | MUST NOT | No correctness inferred from addressability |
| P11-12.40 | MUST | Authority declared, not assumed |
| P11-12.41 | MUST | Non results returned unmodified |
| P11-12.42 | MUST | Custody gap exposed to composition |
| P11-13.1 | MUST | Unverified reciprocals declared |
| P11-13.2 | SHOULD | Register maintained |
| P11-13.3 | MUST | Gaps declared, not filled |
| P11-13.4 | SHOULD | Open questions carried forward |

### Derived counts

Every figure below is derived by extraction from the clause text of this document and not asserted independently. The grain of counting is stated for each figure. A clause is one line of the document matching the clause heading form given under Binding of requirement language, that is, an identifier of the form `P11-S.N`, a modality in parentheses, and a subject label. Narrative sentences containing a requirement keyword are not clauses and are not counted; per that same section they are not binding. No clause of this part states a requirement keyword in its prose, so the modality of a clause is unambiguous.

**Total clauses.** 435. Grain: one clause heading.

**By modality.** Grain: one clause heading, counted once against its single declared modality.

| Modality | Clauses | Share |
| --- | --- | --- |
| MUST | 308 | 70.8% |
| MUST NOT | 122 | 28.0% |
| SHOULD | 4 | 0.9% |
| SHOULD NOT | 0 | 0.0% |
| MAY | 1 | 0.2% |
| **All** | **435** | **100.0%** |

**Absolute requirements.** 430 clauses carry MUST or MUST NOT and are therefore conditions of conformance. 4 carry SHOULD or SHOULD NOT and require a recorded reason where not satisfied. 1 carry MAY and constrain nothing. Grain: one clause heading. These three figures sum to the total.

**By section.** Grain: one clause heading, attributed to the numbered section in which its heading appears.

| Section | Title | Clauses | MUST | MUST NOT | SHOULD | SHOULD NOT | MAY |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Scope and responsibilities | 26 | 13 | 13 | 0 | 0 | 0 |
| 2 | Terminology | 8 | 1 | 7 | 0 | 0 | 0 |
| 3 | Data model | 98 | 70 | 28 | 0 | 0 | 0 |
| 4 | Interfaces | 44 | 31 | 12 | 1 | 0 | 0 |
| 5 | State model | 24 | 20 | 4 | 0 | 0 | 0 |
| 6 | Execution semantics | 58 | 46 | 12 | 0 | 0 | 0 |
| 7 | Outcome and failure taxonomy | 31 | 22 | 9 | 0 | 0 | 0 |
| 8 | Observability and the audit record | 48 | 41 | 6 | 1 | 0 | 0 |
| 9 | Extension model | 24 | 19 | 5 | 0 | 0 | 0 |
| 10 | Standards and specifications | 4 | 4 | 0 | 0 | 0 | 0 |
| 11 | Anti patterns | 24 | 11 | 13 | 0 | 0 | 0 |
| 12 | Boundaries with other parts | 42 | 28 | 13 | 0 | 0 | 1 |
| 13 | What could not be established | 4 | 2 | 0 | 2 | 0 | 0 |
| **All** | | **435** | **308** | **122** | **4** | **0** | **1** |

**Ordinal integrity.** In this version, the highest ordinal in each section equals the number of clauses in that section, so no identifier has yet been retired. This will cease to be true at the first clause removal, and the count rather than the highest ordinal is then the figure to rely on.

**Sourced clauses.** 13 clauses carry a **Source.** note naming the specification or published work their subject rests on. Grain: one clause heading carrying at least one Source note. Section 10.1 states how the notes are to be read and section 13.1 lists the sources not obtained in full text.

**Cross part citations.** This part cites six clauses of other parts: P7-12.30, P8-12-28, P8-12-30, P9-12-18, P9-12-19 and P10-12.35. Every one was verified against the delivered text of the part concerned. Grain: one distinct clause identifier cited.

## 1. Scope and responsibilities

### 1.1 What this component is

This component holds octets and returns them. It is the simplest component in the standard and it is the one most often built wrong, because the property it exists to provide is not the property it appears to provide.

It appears to provide storage. What it actually provides is a binding between a name and a sequence of octets that cannot be broken without the name changing, and the value of that binding to every other component is that a citation made years ago either resolves to exactly what was cited or fails loudly. Nine other parts of this standard pin something here. `Part 1` pins the octets of a controlled document, `Part 3` pins the material of an evidence package, `Part 8` pins an attachment, `Part 9` pins a schema artifact, `Part 10` pins a release, and `Part 13` pins a model artifact and an invocation payload. Every one of those pins is a promise that this component keeps or silently fails to keep.

**P11-1.1 (MUST) Octets owned.** An implementation must own the durable custody of the octet sequences submitted to it.

**P11-1.2 (MUST) Addresses owned.** An implementation must own the content address, being the self describing name under which an octet sequence is retrievable.

**P11-1.3 (MUST) Address profiles owned.** An implementation must own the address profile, being the identified set of parameters under which an address is computed from octets.

**P11-1.4 (MUST) Algorithm register owned.** An implementation must own the register of digest algorithms it accepts, their status and their permitted uses.

**P11-1.5 (MUST) Composite structure owned.** An implementation must own the assembly of a composite artifact from its constituent parts, and the structure by which the composite's address is derived.

**P11-1.6 (MUST) Ingest records owned.** An implementation must own the record of every submission, its submitter, its instant, its computed address and whether it deduplicated against existing content.

**P11-1.7 (MUST) Retrieval records owned.** An implementation must own the record of every retrieval, including whether the octets returned were verified against the address they were requested under.

**P11-1.8 (MUST) Fixity records owned.** An implementation must own the record of every verification of stored content against its address, including verifications that passed.

**P11-1.9 (MUST) Referrer registrations owned.** An implementation must own the register of components and records that have declared a reference to an address, and the retention obligation each creates.

**P11-1.10 (MUST) Tombstones owned.** An implementation must own the tombstone, being the durable record that an address once resolved and no longer does, with the reason.

**P11-1.11 (MUST) Aliases owned.** An implementation must own the alias, being a mutable name that resolves to an address, and the history of what it resolved to.

**P11-1.12 (MUST) Placement declarations owned.** An implementation must own the declaration of where content is held, in how many independent copies, and under what durability claim.

**P11-1.13 (MUST) Deduplication scope owned.** An implementation must own the declared scope within which identical content is stored once, and the boundary across which it is not.

### 1.2 What this component is not

The list is longer than for most parts, because a store that returns anything on request is the natural place to put everything, and every other part has something it would rather not keep.

**P11-1.14 (MUST NOT) Not a record of any determination.** An implementation must not hold as authoritative any decision, verdict, determination, attribute value provenance or policy state. **Source.** Required of this component by `Part 7` section 12.11, whose reciprocal requires this part to declare that it holds no decision, no attribute value provenance and no policy state.

**P11-1.15 (MUST NOT) Not the meaning of what it holds.** An implementation must not interpret, parse, validate or attribute meaning to the octets it holds beyond what addressing requires.

**P11-1.16 (MUST NOT) Not a schema authority.** An implementation must not validate content against a schema and must not version a schema, which are `Part 9`'s.

**P11-1.17 (MUST NOT) Not the document authority.** An implementation must not govern approval, effective date, supersession as a document, retention schedule or disposition authority, which are `Part 1`'s.

**P11-1.18 (MUST NOT) Not the audit ledger.** An implementation must not represent its own integrity records as the evidentiary chain of a determination, which is `Part 3`'s.

**P11-1.19 (MUST NOT) Not a decision point for access.** An implementation must not decide whether a party may read or write content, and must obtain that decision from `Part 7`.

**P11-1.20 (MUST NOT) Not a reference authority.** An implementation must not hold a code system, a value set or a master record as content it interprets, which are `Part 10`'s.

**P11-1.21 (MUST NOT) Not a deleter on its own authority.** An implementation must not remove content on its own initiative, including for cost, capacity or age. **Source.** Required of this component by `Part 7` section 12.11, whose reciprocal requires this part to declare that it does not delete content on its own authority.

**P11-1.22 (MUST NOT) Not a mutator.** An implementation must not expose any operation that changes the octets retrievable under an existing address.

**P11-1.23 (MUST NOT) Not an assessor of itself.** An implementation must not report its own conformance to this part as assurance, and must expose the state `Part 12` requires.

**P11-1.24 (MUST NOT) Not a work manager.** An implementation must not manage the work by which a custodian investigates a fixity failure, and must obtain the work item from `Part 8`.

**P11-1.25 (MUST NOT) Not an identity for the thing the content describes.** An implementation must not permit an address to be used as the identity of the entity, document or record the content describes, since two representations of one thing have two addresses and one representation of two things has one.

### 1.3 The three failures this part exists to prevent

*The address that is only a digest.* A hexadecimal string is not a name. It does not say which algorithm produced it, so a store that accepts it must guess, and a store that accepts more than one algorithm must guess wrong eventually. It does not say what was hashed, so a digest over canonicalised content and a digest over raw octets are indistinguishable. It does not say how a large object was divided and assembled, so the same octets submitted to two implementations yield two different names, both correct. Section 3.2 and section 3.4 exist to prevent this, and section 3.6 exists because the composite case is where it bites hardest.

*The retrieval that was never verified.* Content is returned as the content at an address, and nothing checked that it hashes to that address. The store's entire value proposition is that this cannot happen, and the check is the first thing sacrificed for latency at scale. The failure is silent in both directions: corruption passes as content, and a substitution passes as the original. Section 6.5 and section 7.2 exist to prevent this, and the requirement is that an unverified return be *labelled* as unverified rather than forbidden, because forbidding it produces implementations that verify nothing and claim they do.

*The deletion nobody could see coming.* Deduplication means one octet sequence serves many referrers. The store knows its addresses and does not know who cites them, so a deletion that is correct for the requesting referrer destroys the citation of eight others, and a retention obligation held by one referrer is invisible to the deletion path. `Part 10` section 3.15 met the same structure and `Part 10` section 13.7 predicted it would arrive here. Sections 3.11, 6.8 and 7.5 exist to prevent it, and the position is that the store cannot discover its referrers and must therefore be told, must count what it has not been told, and must refuse to delete into the gap.

### 1.4 What this part is written for

A reviewer should read section 3.2 first, then section 7.2. Section 3.2 states the position on which the part turns, being that an address is a name with a profile and not a hash, and section 7.2 is where the part is testable, because it distinguishes six conditions that a conventional store returns as a single not found.

A reviewer should also know where this part is most likely to be wrong. Section 13.2 records that this part requires the address profile to be recoverable from the address and that no consulted format supplies a field for it, so the central requirement of section 3.2 is one this part cannot say how to satisfy. Section 13.5 records that a redaction retaining a digest is, for low entropy content, a means of confirming that content, which may make the redaction model incoherent for exactly the content most likely to be redacted. And section 13.4 records that this component cannot enumerate its referrers, which makes every deletion in it either unsafe or refused. Those three are the places to look first.

**P11-1.26 (MUST NOT) No conformance assessment anticipated.** An implementation must not read this part as assessing any system, and must treat assessment as the subject of `Part 12`.

## 2. Terminology

### 2.1 Terms owned by this part

**Artifact.** One immutable octet sequence held by this component, together with the records describing its custody. The octets are the artifact; a name for them is not.

**Octet sequence.** The ordered bytes submitted, of length zero or more. A zero length sequence is a valid artifact and has an address.

**Content address.** The self describing name under which an artifact is retrievable, from which the digest algorithm, the address profile and the structure of the addressed content are recoverable without external context. The self describing property is taken from the multiformats content identifier, whose version 1 form prefixes a digest with codes identifying the hash function, the digest length and the content type.

**Digest.** The output of a digest algorithm over a defined input. A digest is an input to an address and is not an address.

**Address profile.** The identified, versioned set of parameters under which an address is computed: the digest algorithm, the canonicalisation applied to the octets or the declaration that none was, the chunking parameters where the content is divided, the assembly structure where the content is composite, and the domain separation scheme where a tree is built. The concept corresponds to what the content identifier community documents as a profile, being a standard combination of chunking, layout and codec settings recorded because reproducible addresses across implementations require the parameters to be fixed.

**Simple artifact.** An artifact whose address is computed over its whole octet sequence in one operation.

**Composite artifact.** An artifact whose address is computed over a structure of constituent parts, each itself addressed.

**Part.** One constituent of a composite artifact. Used in this sense only where the word is lower case; `Part` with an initial capital and a number refers to a part of this standard.

**Assembly structure.** The declared arrangement by which the parts of a composite artifact reconstitute its octet sequence, and by which its address is derived from its parts' addresses.

**Domain separation.** The practice of prefixing a distinguishable tag to a leaf input and a different tag to an interior node input before hashing, so that no interior node's digest can be presented as a leaf's. RFC 9162 prescribes it for the Merkle tree of a certificate transparency log.

**Deduplication.** The storing of one copy of an octet sequence submitted more than once.

**Deduplication scope.** The declared boundary within which deduplication occurs, and outside which identical content is stored separately.

**Convergence.** The property that two independent submissions of identical octets under one address profile yield one address.

**Verification.** The recomputation of an address from octets and its comparison with the address claimed.

**Fixity.** The property of stored octets still matching the address under which they are held. Preservation practice treats fixity as information to be recorded about an object rather than as an assumed property, and this part follows it.

**Fixity verification.** A scheduled or requested verification of stored content, recorded whether it passed or failed.

**Quarantine.** The state of content whose fixity verification failed, in which it is retained, not returned as content, and not deleted.

**Referrer.** A component or record outside this component that has declared a reference to an address.

**Referrer registration.** The record of a declared reference, and of the retention obligation it creates.

**Retention floor.** The latest instant to which a declared referrer's citation is retained, below which this component must not delete. The structure is inherited from `Part 10` section 3.15, where `Part 7` imposed it first.

**Tombstone.** The durable record that an address once resolved and no longer does, carrying the address, the digest, the size, the reason and the authorising act.

**Redaction.** The authorised removal of an artifact's octets with the retention of its address, digest, size and record. Distinguished from deletion, which removes the artifact and its address from the resolvable set, and from erasure, which is a claim about the world that this component cannot make.

**Alias.** A mutable name that resolves to an address at a given instant.

**Alias resolution record.** The record of what an alias resolved to at a stated instant.

**Placement.** The set of independent locations holding copies of an artifact, with a declared independence claim.

**Durability claim.** The declared expectation of survival of an artifact over a stated interval, with the basis on which it is claimed.

**Proof of possession.** Evidence that a party holds the octets of an artifact, which a digest is not.

**Custodian.** The party accountable for the continued availability and fixity of a declared class of content.

### 2.2 Clauses governing terminology

**P11-2.1 (MUST NOT) No redefinition of another part's terms.** An implementation must not redefine a term this standard allocates to another part, and must use it with the meaning that part gives it.

**P11-2.2 (MUST NOT) Address not equated with digest.** An implementation must not treat a bare digest as a content address and must not accept one where an address is required.

**P11-2.3 (MUST NOT) Address not equated with location.** An implementation must not treat a path, a URL, a bucket key or any other location as an address, and must not derive identity from a location. **Source.** `Part 7` clause P7-12.30 requires that stored content be addressed by digest under a declared canonical form profile and that a location or path not be relied upon as identity.

**P11-2.4 (MUST NOT) Artifact not equated with alias.** An implementation must not treat an alias as an artifact and must not permit an alias where a citation is required.

**P11-2.5 (MUST NOT) Deletion not equated with redaction.** An implementation must not represent a redaction as a deletion or a deletion as a redaction.

**P11-2.6 (MUST NOT) Fixity not equated with durability.** An implementation must not represent a durability claim as evidence of fixity, since a claim about survival is not a verification of content.

**P11-2.7 (MUST NOT) Verification not equated with retrieval.** An implementation must not represent the successful return of octets as evidence that they were verified.

**P11-2.8 (MUST) Kinds registered before use.** An implementation must register every digest algorithm, address profile, assembly structure, alias namespace, deduplication scope and tombstone reason kind before content or an operation uses it, per section 9.

## 3. Data model

### 3.1 Type vocabulary

Types in this section are abstract and impose no representation. `identifier` is an opaque immutable string unique within its declared scope. `address` is a content address per section 3.4. `digest` is an algorithm identifier together with a digest value. `instant` is a point in time with an offset from UTC and at least millisecond resolution. `octets` is a length together with the bytes themselves, never held in a record of this component but named as the thing a record describes. `pin` is a reference resolving to a stated version of a stated object as it stood at a stated instant. `enum(...)` is a closed set unless the field description states otherwise.

**P11-3.1 (MUST) Types declared.** An implementation must declare the concrete representation it adopts for every abstract type in section 3.1 and must not vary it between records of one class.

**P11-3.2 (MUST) Length recorded separately from the digest.** An implementation must record the octet length of every artifact as a field in its own right and must not require the length to be obtained by reading the octets.

**P11-3.3 (MUST NOT) No representation dependent identity.** An implementation must not derive the identity of any record from its representation.

### 3.2 The address is not the digest

This is the position on which the part turns. A digest is a number computed from an input. An address is a name that says what was computed, over what, and how the input was arrived at. The difference is not pedantry; it is the difference between a store whose names mean one thing and a store whose names mean whatever the implementation that minted them happened to do.

Three parameters have to be recoverable from the name and are routinely absent from it. The algorithm, because a store accepting more than one must know which to recompute, and because an algorithm withdrawn from use must be distinguishable from one in use without inspecting the content. The canonicalisation, because a digest over the raw octets and a digest over a canonicalised form of the same content are different numbers and both are legitimate, and a name that omits which was used cannot be verified. And the assembly, because content large enough to be divided is divided by parameters, and identical octets under two different chunk sizes yield two different names.

The third is the one that surprises implementers. It is documented in the ecosystem that took content addressing furthest: the content identifier community publishes profiles, being standard combinations of chunking, layout and codec settings, precisely because identical files otherwise acquire different identifiers in different tools, and users encountering it report it as a defect when it is the specified behaviour. A store that treats a composite address as a function of the content alone has told its callers something untrue.

`Part 7` reached the same conclusion from the other side. Its clause P7-12.30 requires content to be addressed by digest under a declared canonical form profile, which is a requirement on this component expressed in that component's vocabulary. This section is the discharge of it.

**P11-3.4 (MUST) Address self describing.** An implementation must ensure that the digest algorithm, the address profile and whether the addressed content is simple or composite are recoverable from the address alone, without reference to any record.

**P11-3.5 (MUST NOT) No bare digest accepted as an address.** An implementation must reject a request that supplies a bare digest where an address is required.

**P11-3.6 (MUST) Profile identified in the address.** An implementation must encode the address profile identity in the address and must not carry it only in an accompanying record.

**P11-3.7 (MUST NOT) No inference of a profile.** An implementation must not infer an address profile from the content, from the submitter, from a default or from any source other than the address itself or an explicit parameter of the submission.

**P11-3.8 (MUST) Digest length encoded.** An implementation must encode the digest length in the address and must reject an address whose digest length does not match the length the named algorithm produces. **Source.** The content identifier specification requires that the digest length field consume the remaining bytes exactly and that a decoder reject a truncated digest or any trailing bytes.

**P11-3.9 (MUST) Address parse failure distinguished.** An implementation must return the outcome that names an unparseable or malformed address and must not return a not found outcome for one.

### 3.3 Entity inventory

The table is normative as to which entities exist and which component owns each.

| Entity | Immutable once written | Owned here |
|---|---|---|
| Artifact record | yes, save for its state | yes |
| Address binding | yes | yes |
| Address profile | no, versions are | yes |
| Digest algorithm registration | no, its status changes | yes |
| Assembly structure record | yes | yes |
| Ingest record | yes | yes |
| Retrieval record | yes | yes |
| Fixity verification record | yes | yes |
| Referrer registration | no, its floor rises | yes |
| Tombstone | yes | yes |
| Redaction record | yes | yes |
| Alias | no | yes |
| Alias resolution record | yes | yes |
| Placement declaration | no | yes |
| Deduplication scope declaration | no | yes |
| Custodian assignment | no | yes |
| Quarantine record | yes | yes |
| Authorisation decision | — | no, `Part 7` |
| Document identity and retention schedule | — | no, `Part 1` |
| Evidentiary chain | — | no, `Part 3` |
| Schema identity | — | no, `Part 9` |
| Code system, value set, master record | — | no, `Part 10` |

**P11-3.10 (MUST) Inventory normative.** An implementation must hold every entity the table in section 3.3 marks as owned here and must not hold as its own any entity the table allocates to another part.

**P11-3.11 (MUST) Immutability observed.** An implementation must not modify any record the table in section 3.3 marks immutable once written, and must express a correction as a new record superseding it.

### 3.4 The address and the address profile

| Field, address profile | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `profile_id` | identifier | yes | 1 | Not possible |
| `profile_version` | string | yes | 1 | Not possible |
| `algorithm_id` | identifier | yes | 1 | Not possible |
| `canonicalisation` | enum(`none`,`declared`) | yes | 1 | Not possible; see P11-3.14 |
| `canonicalisation_ref` | pin | no | 0..1 | Canonicalisation is `none`; required where it is `declared` |
| `mode` | enum(`simple`,`composite`) | yes | 1 | Not possible |
| `chunker_id` | identifier | no | 0..1 | The mode is simple; required where it is composite |
| `chunk_parameters` | structure: fixed size, or minimum, target and maximum for a content defined chunker | no | 0..1 | The mode is simple; required where it is composite |
| `assembly_structure_id` | identifier | no | 0..1 | The mode is simple; required where it is composite |
| `domain_separation_id` | identifier | no | 0..1 | The mode is simple; required where the assembly is a tree |
| `status` | enum(`active`,`deprecated`,`withdrawn`) | yes | 1 | Not possible |
| `registered_at` | instant | yes | 1 | Not possible |

**P11-3.12 (MUST) Profile immutable in effect.** An implementation must not alter the parameters of a registered address profile version and must express a change as a new profile version.

**P11-3.13 (MUST) One profile per address.** An implementation must compute every address under exactly one profile version and must record which.

**P11-3.14 (MUST) Canonicalisation declared, never assumed.** An implementation must record whether the octets were canonicalised before hashing and must reject a profile that leaves it unstated.

**P11-3.15 (MUST NOT) No canonicalisation performed here.** An implementation must not itself canonicalise submitted content, and where a profile declares canonicalisation the submitter must supply the canonicalised octets and the reference to the canonicalisation the profile names.

Clause P11-3.15 is a boundary decision rather than a technical one. Canonicalisation is a property of a content type, so a store that canonicalises acquires knowledge of content types and becomes a parser, which clause P11-1.15 forbids. The component that owns the content type canonicalises and submits the result; this component records which canonicalisation was declared and hashes what it is given.

**P11-3.16 (MUST) Chunker registered with its parameters.** An implementation must register every chunker with its kind and its parameters, and must reject a composite profile naming an unregistered chunker.

**P11-3.17 (MUST) Content defined chunkers declare their bounds.** An implementation must record the minimum, target and maximum chunk size of every content defined chunker, and must reject one that declares no maximum.

**P11-3.18 (MUST NOT) No profile change applied retrospectively.** An implementation must not recompute an existing address under a new profile version and must not represent an address computed under one profile version as computed under another.

### 3.5 The artifact record

| Field | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `artifact_id` | identifier | yes | 1 | Not possible |
| `primary_address` | address | yes | 1 | Not possible |
| `additional_addresses` | address | no | 0..n | The artifact is addressed under one profile and algorithm only |
| `length` | integer, zero or greater | yes | 1 | Not possible; zero is a valid length |
| `mode` | enum(`simple`,`composite`) | yes | 1 | Not possible |
| `assembly_record_id` | identifier | no | 0..1 | The artifact is simple |
| `state` | enum, section 5.2 | yes | 1 | Not possible |
| `first_ingested_at` | instant | yes | 1 | Not possible |
| `ingest_count` | integer, one or greater | yes | 1 | Not possible; a count above one records deduplicated resubmissions |
| `dedup_scope_id` | identifier | yes | 1 | Not possible |
| `custodian` | pin to party | yes | 1 | Not possible |
| `placement_id` | identifier | yes | 1 | Not possible |
| `retention_floor` | instant | no | 0..1 | No referrer has declared a retention obligation, which is not the same as no referrer existing; see P11-3.36 |
| `declared_referrer_count` | integer, zero or greater | yes | 1 | Not possible; zero means no referrer has registered |
| `last_fixity_verified_at` | instant | no | 0..1 | Never verified since ingest; see P11-3.44 |
| `content_type_claimed` | string | no | 0..1 | No submitter claim was made; the store makes no claim of its own |
| `encryption` | enum(`none`,`opaque_to_store`,`store_managed`) | yes | 1 | Not possible; see section 3.16 |
| `legal_hold` | boolean | yes | 1 | Not possible |

**P11-3.19 (MUST) Record present for every artifact.** An implementation must hold an artifact record containing every field marked required in the table in section 3.5, with the type, cardinality and absence semantics stated there.

**P11-3.20 (MUST) Zero length artifact addressable.** An implementation must accept, address, store and return a zero length octet sequence, and must not treat its address as absent content.

**P11-3.21 (MUST NOT) No claimed content type relied upon.** An implementation must not use a submitter's claimed content type for any purpose other than returning it unchanged, and must not represent it as verified.

**P11-3.22 (MUST) Ingest count maintained.** An implementation must increment the ingest count on every resubmission of identical content within a deduplication scope, so that the number of independent submissions is recoverable.

**P11-3.23 (MUST NOT) No artifact record deletion.** An implementation must not delete an artifact record, and must express the removal of content as a state transition with a tombstone or a redaction record.

### 3.6 Composite artifacts and assembly

| Field, assembly record | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `assembly_record_id` | identifier | yes | 1 | Not possible |
| `root_address` | address | yes | 1 | Not possible |
| `assembly_structure_id` | identifier | yes | 1 | Not possible |
| `profile_version` | string | yes | 1 | Not possible |
| `parts` | structure: ordinal, part address, offset, length | yes | 1..n | Not possible |
| `depth` | integer, one or greater | yes | 1 | Not possible |
| `interior_node_count` | integer, zero or greater | yes | 1 | Not possible |
| `domain_separation_id` | identifier | no | 0..1 | The structure is not a tree |
| `equivalent_roots` | address | no | 0..n | No other root address over identical octets is known; see P11-3.28 |

**P11-3.24 (MUST) Assembly recorded, not inferred.** An implementation must record the assembly of every composite artifact and must not require the assembly to be reconstructed by reading the parts.

**P11-3.25 (MUST) Reconstitution deterministic.** An implementation must be able to reconstitute the exact octet sequence of a composite artifact from its assembly record and its parts, and must reject an assembly record from which the octet sequence cannot be reconstituted deterministically.

**P11-3.26 (MUST) Part addresses under the same profile.** An implementation must address every part of a composite artifact under the same profile version as the composite and must reject an assembly mixing profile versions.

**P11-3.27 (MUST NOT) No composite address treated as a function of content alone.** An implementation must not represent a composite address as determined by the octets alone, since it is determined by the octets together with the chunking and assembly parameters. **Source.** The content identifier community publishes profiles, being standard combinations of chunking, layout and codec settings, because reproducible identifiers across implementations require the parameters to be fixed; the default chunker of the principal implementation divides content into fixed blocks of 262144 octets, and altering the leaf encoding or the layout changes the root identifier for identical content.

**P11-3.28 (MUST) Equivalent roots recorded, never merged.** An implementation must record, where it establishes that two composite root addresses cover identical octet sequences, an equivalence between them, and must not merge the two artifacts or substitute one address for the other.

**P11-3.29 (MUST) Depth bounded.** An implementation must declare a maximum assembly depth, must reject an assembly exceeding it, and must record the depth of every assembly. The value is an implementation decision because the useful depth depends on the maximum artifact size and the chunk size admitted, neither of which this part constrains.

**P11-3.30 (MUST NOT) No part shared across profiles silently.** An implementation must not present a part addressed under one profile version as a part of a composite addressed under another.

### 3.7 Merkle construction and domain separation

**P11-3.31 (MUST) Domain separation applied to every tree.** An implementation must apply domain separation to every tree assembly, prefixing a distinguishable tag to a leaf input and a different tag to an interior node input before hashing. **Source.** RFC 9162 prescribes prefixing a leaf hash input with one octet value and an interior node hash input with another for the Merkle tree of a certificate transparency log, and the purpose of the practice is that no interior node's digest can be presented as a leaf's.

**P11-3.32 (MUST) Domain separation scheme registered.** An implementation must register every domain separation scheme with its leaf and interior tags and must reject a tree assembly naming none.

**P11-3.33 (MUST NOT) No unprefixed tree accepted.** An implementation must reject an assembly structure that hashes leaf and interior inputs without distinguishable prefixes.

**P11-3.34 (MUST) Single part tree defined.** An implementation must declare the address of a tree over exactly one part and must not leave the single part case to the implementation, since a tree that returns the leaf's digest as its root permits a leaf to be presented as a root.

**P11-3.35 (MUST) Odd node handling declared.** An implementation must declare, per assembly structure, how a level with an odd number of nodes is handled, and must reject a structure that leaves it unstated.

### 3.8 The digest algorithm register and algorithm agility

| Field | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `algorithm_id` | identifier | yes | 1 | Not possible |
| `algorithm_name` | string | yes | 1 | Not possible |
| `digest_length` | integer | yes | 1 | Not possible |
| `specification_ref` | string | yes | 1 | Not possible |
| `status` | enum(`accepted`,`deprecated`,`verify_only`,`withdrawn`) | yes | 1 | Not possible |
| `status_changed_at` | instant | no | 0..1 | The status has never changed |
| `permitted_uses` | enum(`ingest`,`verify`,`resolve`) | yes | 1..n | Not possible |
| `collision_resistance_claim` | enum(`asserted`,`disputed`,`broken`) | yes | 1 | Not possible; see P11-3.38 |

**P11-3.36 (MUST) More than one algorithm supported.** An implementation must support at least two digest algorithms concurrently, so that a migration is possible without an interruption in service.

**P11-3.37 (MUST) Status governs use.** An implementation must refuse to mint a new address under an algorithm whose status is `verify_only` or `withdrawn`, and must continue to resolve and verify addresses already minted under it.

**P11-3.38 (MUST) Collision resistance status recorded.** An implementation must record the collision resistance status of every registered algorithm and must expose every artifact addressed under an algorithm whose status is `disputed` or `broken`. **Source.** A practical collision was demonstrated against SHA-1 in 2017 and national standards guidance has since set a date for its withdrawal from use; a store that does not know which of its addresses rest on a broken algorithm cannot begin a migration.

**P11-3.39 (MUST NOT) No cross algorithm digest comparison.** An implementation must not compare digests computed under different algorithms and must return the outcome that names the mismatch of algorithms.

**P11-3.40 (MUST) Rebinding recorded, original retained.** An implementation must record every addition of an address under a new algorithm to existing content as a rebinding, must retain the original address as resolvable, and must not retire it.

**P11-3.41 (MUST) Rebinding verified before recording.** An implementation must verify the content against its existing address before computing a new address over it, and must not rebind content whose fixity is unverified.

**P11-3.42 (MUST NOT) No silent address substitution.** An implementation must not return a different address than the one requested, and must not redirect a request for a deprecated address to its rebinding without recording the redirection in the retrieval record.

### 3.9 The ingest record

| Field | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `ingest_record_id` | identifier | yes | 1 | Not possible |
| `computed_address` | address | yes | 1 | Not possible |
| `claimed_address` | address | no | 0..1 | The submitter claimed no address; see P11-3.45 |
| `submitter` | pin to party | yes | 1 | Not possible |
| `submitted_at` | instant | yes | 1 | Not possible |
| `length` | integer | yes | 1 | Not possible |
| `profile_version` | string | yes | 1 | Not possible |
| `outcome` | enum, section 7.3 | yes | 1 | Not possible |
| `deduplicated` | boolean | yes | 1 | Not possible |
| `dedup_scope_id` | identifier | yes | 1 | Not possible |
| `possession_evidence` | enum(`full_transfer`,`challenge_response`,`none`) | yes | 1 | Not possible; see section 3.15 |
| `authorisation_ref` | pin to `Part 7` | yes | 1 | Not possible |

**P11-3.43 (MUST) Address computed by the store.** An implementation must compute the address of submitted content itself and must not accept a submitter's computed address as the address.

**P11-3.44 (MUST) Claimed address compared and recorded.** An implementation must compare a submitter's claimed address with the address it computed, must record both, and must reject the submission where they differ.

**P11-3.45 (MUST) Claim absence recorded.** An implementation must record that no address was claimed where none was, and must not represent an unclaimed submission as one whose claim matched.

**P11-3.46 (MUST NOT) No ingest record deletion.** An implementation must not delete an ingest record when the artifact it concerns is deleted or redacted.

### 3.10 The retrieval record and the verification declaration

| Field | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `retrieval_record_id` | identifier | yes | 1 | Not possible |
| `requested_address` | address | yes | 1 | Not possible |
| `resolved_address` | address | no | 0..1 | Nothing was returned |
| `requester` | pin to party or component | yes | 1 | Not possible |
| `requested_at` | instant | yes | 1 | Not possible |
| `outcome` | enum, section 7.2 | yes | 1 | Not possible |
| `verification` | enum(`verified_full`,`verified_partial`,`unverified`,`verification_failed`) | yes | 1 | Not possible; see P11-3.48 |
| `verified_extent` | structure: octets verified, octets returned | no | 0..1 | Verification was `unverified`; required where it is `verified_partial` |
| `bytes_returned` | integer | yes | 1 | Not possible; zero where nothing was returned |
| `redirected_from` | address | no | 0..1 | No redirection occurred |
| `authorisation_ref` | pin to `Part 7` | yes | 1 | Not possible |

**P11-3.47 (MUST) Retrieval recorded, including failures.** An implementation must record every retrieval attempt, including those returning nothing.

**P11-3.48 (MUST) Verification state declared on every retrieval.** An implementation must record, for every retrieval that returned octets, whether they were fully verified against the requested address, partially verified, or returned unverified.

**P11-3.49 (MUST NOT) No unverified return presented as verified.** An implementation must not represent an unverified or partially verified return as verified, in the record or in the response to the caller.

**P11-3.50 (MUST) Partial verification extent recorded.** An implementation must record how many octets were verified and how many returned where verification was partial, and must not report partial verification without both.

Clauses P11-3.48 to P11-3.50 exist because the alternative positions are both worse. Requiring full verification on every retrieval produces implementations that verify nothing under load and report success, since the requirement is unobservable from outside. Permitting unverified retrieval silently produces a store whose central guarantee is unenforced and unmeasured. Labelling the return makes the trade visible, makes the unverified proportion countable under section 8.5, and leaves the decision with the caller, which is where it belongs.

### 3.11 Referrers and the retention floor

The store cannot discover who cites it. Every address is a name any component may hold in any record, and nothing in the act of holding it informs this component. `Part 10` section 3.15 met this structure first, imposed on it by `Part 7`; this part inherits it and it is more acute here, because deduplication means one artifact commonly serves many referrers with different retention obligations.

| Field, referrer registration | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `referrer_registration_id` | identifier | yes | 1 | Not possible |
| `address` | address | yes | 1 | Not possible |
| `referrer_component` | identifier | yes | 1 | Not possible |
| `referrer_record_ref` | string | no | 0..1 | The referrer declared a reference without identifying the citing record |
| `declared_at` | instant | yes | 1 | Not possible |
| `retention_until` | instant | no | 0..1 | The referrer declares no retention obligation, which is not the same as declaring none applies |
| `retention_basis` | enum(`schedule`,`legal_hold`,`open_ended`,`undeclared`) | yes | 1 | Not possible |
| `withdrawn_at` | instant | no | 0..1 | The registration is current |

**P11-3.51 (MUST) Referrer registration accepted.** An implementation must accept a referrer registration from any component and must record it against the address.

**P11-3.52 (MUST) Retention floor derived from registrations.** An implementation must derive the retention floor of an artifact as the latest `retention_until` of its current referrer registrations, and must record an open ended basis as an absent floor that forbids deletion rather than as no floor.

**P11-3.53 (MUST NOT) No deletion below the floor.** An implementation must refuse a deletion or redaction of an artifact before its retention floor and must record the refusal.

**P11-3.54 (MUST NOT) No inference of absence of referrers.** An implementation must not treat the absence of a referrer registration as evidence that no referrer exists.

**P11-3.55 (MUST) Undeclared referrer population exposed.** An implementation must expose the count of artifacts with no referrer registration, and must describe it as content whose citation status is unknown rather than as uncited content.

**P11-3.56 (MUST) Withdrawal of a registration recorded, not erased.** An implementation must retain a withdrawn referrer registration, since a deletion refused on its basis was refused for a reason that must remain readable.

**P11-3.57 (MUST) Floor rise notified.** An implementation must accept a notification that a referrer's retention obligation has been extended and must raise the floor accordingly.

### 3.12 Tombstones, redaction and the limits of erasure

Three operations remove content and they are not the same. Deletion removes the artifact from the resolvable set and leaves a tombstone. Redaction removes the octets and retains the address, the digest, the length and the record, so that a citation still resolves to a description of what was there. Erasure is a claim that the content no longer exists anywhere, which this component cannot make about copies it never held.

| Field, tombstone | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `tombstone_id` | identifier | yes | 1 | Not possible |
| `address` | address | yes | 1 | Not possible |
| `digest` | digest | yes | 1 | Not possible |
| `length` | integer | yes | 1 | Not possible |
| `reason` | enum, section 7.5 | yes | 1 | Not possible |
| `authorising_act` | pin to `Part 7` | yes | 1 | Not possible |
| `authorising_party` | pin to party | yes | 1 | Not possible |
| `effected_at` | instant | yes | 1 | Not possible |
| `referrers_at_effect` | identifier | no | 0..n | No referrer was registered at the instant of effect |
| `notified_referrers` | identifier | no | 0..n | No referrer was notified |

**P11-3.58 (MUST) Tombstone on every removal.** An implementation must write a tombstone for every artifact whose content ceases to be retrievable, whatever the cause.

**P11-3.59 (MUST) Tombstone resolves.** An implementation must resolve a request for a tombstoned address to the tombstone, and must not return a not found outcome for it. **Source.** Required of this component by `Part 10` section 12.11, whose reciprocal requires this part to report an unresolvable address rather than an absent one, and by `Part 8` clause P8-12-30, which requires that component to record an association as unresolvable rather than delete it, which it can only do if this component distinguishes the two.

**P11-3.60 (MUST) Redaction retains the address record.** An implementation must retain the address, digest, length and artifact record of a redacted artifact and must not tombstone it as never having existed.

**P11-3.61 (MUST) Redaction records its scope.** An implementation must record, for every redaction, whether the octets were destroyed, rendered unreadable by key destruction, or overwritten, and must not represent one as another.

**P11-3.62 (MUST NOT) No erasure claim.** An implementation must not assert that content has been erased beyond its own custody, and must confine its assertion to the copies it held.

**P11-3.63 (MUST) Referrers notified of removal.** An implementation must notify every registered referrer of a removal and must record which referrers were notified and which could not be.

**P11-3.64 (MUST) Verification impossibility recorded.** An implementation must record, on redaction, that every determination citing the address can no longer be verified against content, since that is the consequence a citing component must be able to discover.

**P11-3.65 (MUST NOT) No tombstone reuse.** An implementation must not permit an address with a tombstone to be reingested as new content, and must record a resubmission of identical content as a reinstatement with its own record.

### 3.13 Aliases

An alias is where the immutability of the store leaks, and it leaks because callers want a name that follows the content rather than one that identifies it. The store may offer them, and must offer them in a way that cannot be mistaken for an address.

| Field | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `alias_id` | identifier | yes | 1 | Not possible |
| `namespace` | identifier | yes | 1 | Not possible |
| `name` | string | yes | 1 | Not possible |
| `current_address` | address | no | 0..1 | The alias resolves to nothing at present |
| `mutable` | boolean | yes | 1 | Not possible; a value of false records an alias bound once and never rebound |
| `owner` | pin to party | yes | 1 | Not possible |

**P11-3.66 (MUST) Alias syntactically distinguishable from an address.** An implementation must ensure that an alias cannot be mistaken for an address by inspection, and must reject an alias namespace whose names could parse as addresses.

**P11-3.67 (MUST) Every rebinding recorded.** An implementation must record every change of an alias's target with the prior address, the new address, the instant and the acting party.

**P11-3.68 (MUST) Resolution recorded.** An implementation must record, for every resolution of an alias, the address it resolved to and the instant.

**P11-3.69 (MUST NOT) No alias in a citation.** An implementation must not accept an alias where a citation to content is required, and must require the address.

**P11-3.70 (MUST) Point in time alias resolution answerable.** An implementation must answer, for any stated past instant, the address an alias resolved to at that instant.

**P11-3.71 (MUST NOT) No alias deletion without a tombstone.** An implementation must retain the resolution history of a deleted alias.

### 3.14 Fixity verification

**P11-3.72 (MUST) Fixity is recorded, not assumed.** An implementation must record fixity as the outcome of verifications performed and must not represent it as a property of stored content. **Source.** Preservation practice treats fixity as information recorded about an object, and the reference model for an open archival information system places fixity information within the preservation description information of an archived package rather than treating integrity as an assumed property of storage.

| Field, fixity verification record | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `verification_id` | identifier | yes | 1 | Not possible |
| `address` | address | yes | 1 | Not possible |
| `performed_at` | instant | yes | 1 | Not possible |
| `trigger` | enum(`scheduled`,`on_retrieval`,`on_request`,`on_rebinding`,`on_repair`) | yes | 1 | Not possible |
| `scope` | enum(`full`,`sampled`,`part`) | yes | 1 | Not possible |
| `replica_id` | identifier | yes | 1..n | Not possible; which copies were verified |
| `outcome` | enum, section 7.4 | yes | 1 | Not possible |
| `octets_read` | integer | yes | 1 | Not possible |

**P11-3.73 (MUST) Passes recorded as well as failures.** An implementation must record a verification that passed, since the interval since the last successful verification is the figure that matters and it cannot be derived from failures alone.

**P11-3.74 (MUST) Cadence declared per class.** An implementation must declare a fixity verification cadence for every declared class of content and must record the cadence in force at each verification. The cadence is an implementation decision because it trades cost against the interval within which undetected corruption can persist, and no interval is correct for all content.

**P11-3.75 (MUST) Never verified population exposed.** An implementation must expose the count and the oldest ingest instant of artifacts never verified since ingest.

**P11-3.76 (MUST) Replica identified per verification.** An implementation must record which replica a verification read, since a verification of one copy is not a verification of the others.

**P11-3.77 (MUST) Sampled verification declared as sampled.** An implementation must record a verification that read less than the whole artifact as sampled, with the sampling parameters, and must not report it as full.

**P11-3.78 (MUST) Failure quarantines, never deletes.** An implementation must place content whose verification failed into quarantine, must retain it, and must not delete it.

**P11-3.79 (MUST NOT) No failure returned as absence.** An implementation must not return a not found outcome for quarantined content and must return the outcome that names the integrity failure.

### 3.15 Deduplication scope and proof of possession

Deduplication is the operation that makes content addressing economical and the operation that makes it dangerous, and both for the same reason: identical content submitted by two parties is recognised as identical, which means the store has learned something about the second party from the fact that the first submitted it.

| Field, deduplication scope | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `dedup_scope_id` | identifier | yes | 1 | Not possible |
| `boundary` | enum(`global`,`tenant`,`classification`,`none`) | yes | 1 | Not possible |
| `client_side_permitted` | boolean | yes | 1 | Not possible |
| `possession_requirement` | enum(`full_transfer`,`challenge_response`) | yes | 1 | Not possible; see P11-3.81 |
| `observability_controls` | enum(`constant_time_response`,`no_storage_accounting_signal`,`none`) | yes | 1..n | Not possible |

**P11-3.80 (MUST) Scope declared.** An implementation must declare the deduplication scope of every artifact and must not deduplicate across a boundary the scope does not permit.

**P11-3.81 (MUST NOT) No digest accepted as proof of possession.** An implementation must not treat knowledge of an address or a digest as evidence that a party holds the content, and must require either the full transfer of the octets or a challenge response over content the party could not answer without holding it. **Source.** Harnik, Pinkas and Shulman-Peleg, Side channels in cloud services: deduplication in cloud storage, IEEE Security and Privacy 8(6):40 to 47, 2010, identify that an attacker who knows the hash of a file can convince a service performing client side deduplication that it owns the file and thereby obtain the whole of it, and record that a subset of the attacks was observed in the wild against a file synchronisation service. The remedy of proofs of ownership is developed in Halevi, Harnik, Pinkas and Shulman-Peleg, Proofs of ownership in remote storage systems, ACM CCS 2011, pages 491 to 500.

**P11-3.82 (MUST NOT) No observable cross tenant deduplication.** An implementation must not permit a party to determine from a submission's response whether identical content was already held by another party. **Source.** The same 2010 work identifies three attacks that follow from an observable cross user deduplication: learning the contents of a file by guessing it and observing whether it deduplicated, identifying whether a specific file is stored in the service, and establishing a covert channel by the presence or absence of a chosen file.

**P11-3.83 (MUST) Response timing controlled where the boundary is global.** An implementation must declare and apply a control that removes the timing difference between a deduplicated and a stored submission wherever the deduplication boundary is broader than a single tenant.

**P11-3.84 (MUST NOT) No storage accounting signal.** An implementation must not report storage consumption in a way that reveals whether a submission deduplicated against content the submitter does not hold.

**P11-3.85 (MUST) Client side deduplication declared and bounded.** An implementation must declare whether client side deduplication is permitted within a scope and must not permit it where the possession requirement is full transfer.

**P11-3.86 (MUST) Deduplication recorded per submission.** An implementation must record whether each submission deduplicated, so that the proportion of stored content serving more than one referrer is derivable.

### 3.16 Encryption and custody

**P11-3.87 (MUST) Encryption disposition recorded.** An implementation must record, per artifact, whether the octets are unencrypted, encrypted opaquely to the store, or encrypted under keys the store manages.

**P11-3.88 (MUST NOT) No fixity claim over opaque content it cannot read.** An implementation must not claim to verify content it cannot read, and must record a verification of an opaque ciphertext as a verification of the ciphertext and not of the plaintext.

**P11-3.89 (MUST) Address is over what was submitted.** An implementation must compute the address over the octets it received and must record whether those octets were plaintext or ciphertext, since an address over ciphertext does not converge with an address over the plaintext.

**P11-3.90 (MUST NOT) No convergent encryption without a declared exposure.** An implementation must not deduplicate content encrypted deterministically from its own plaintext without declaring that the deduplication reveals plaintext equality to the store and to any party able to observe it.

**P11-3.91 (MUST) Key custody separated from content custody.** An implementation must not hold both the only copy of an encryption key and the only copy of the content it protects, and must record where each is held.

### 3.17 Placement and durability

| Field | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `placement_id` | identifier | yes | 1 | Not possible |
| `replicas` | structure: replica id, location class, independence claim | yes | 1..n | Not possible |
| `replica_count` | integer, one or greater | yes | 1 | Not possible |
| `independence_basis` | enum(`asserted`,`verified`,`unknown`) | yes | 1 | Not possible |
| `durability_claim` | structure: interval, basis | no | 0..1 | No durability claim is made, which must not be read as a claim of none |

**P11-3.92 (MUST) Replica count and independence recorded.** An implementation must record how many copies of an artifact exist and on what basis they are claimed to be independent.

**P11-3.93 (MUST NOT) No unverified independence presented as verified.** An implementation must not present an asserted independence of replicas as verified.

**P11-3.94 (MUST) Durability claim carries its basis.** An implementation must record the basis of every durability claim it publishes and must not publish a figure without one.

**P11-3.95 (MUST) Single replica exposed.** An implementation must expose every artifact held in one replica, since it is content whose loss is a single event.

### 3.18 Projections

**P11-3.96 (MUST) Projections marked as such.** An implementation must mark every projection it exposes as a projection and must not permit a projection to be cited as a record.

**P11-3.97 (MUST) Content listing is a projection.** An implementation must expose any enumeration of held addresses as a projection with the instant at which it was computed.

**P11-3.98 (MUST NOT) No enumeration that omits tombstones silently.** An implementation must state, in every enumeration of addresses, whether tombstoned and redacted addresses are included.

### 3.19 Worked demonstration

The demonstration is narrative and binds nothing. It exists because the difference between this model and a conventional store is not visible in a field list.

A component submits 700000 octets under profile `PF-2` version 3, which declares algorithm `sha2-256`, canonicalisation `none`, mode `composite`, a fixed chunker of 262144 octets, a binary tree assembly and domain separation scheme `DS-1`. The store divides the content into three parts of 262144, 262144 and 175712 octets, addresses each as a leaf with the leaf tag prefixed, builds one interior node over the first two with the interior tag prefixed, builds the root over that node and the third leaf, and mints root address `A-1`. The address carries the algorithm, the digest length, the profile identity and the composite marker, so a reader years later can recompute it without consulting any record.

A second component submits the identical 700000 octets under profile `PF-3`, which is identical except that its chunker is 1048576 octets. The content is a single part and the root address `A-2` differs from `A-1`. Both are correct. Under clause P11-3.28 the store records an equivalence between `A-1` and `A-2` and under the same clause does not merge them, because a determination citing `A-1` must continue to resolve to `A-1` and because the two were minted under different declared profiles.

`Part 9` separately holds three digests over the same artifact, computed over canonical forms of its own choosing for its own purposes. None of those is a content address and none of them is `A-1`. The seam is recorded at section 12.9: this component addresses octets, that component canonicalises content, and the two produce different numbers over the same file by design.

Eleven months later a retrieval of `A-1` returns octets after verifying only the first part, because the caller streamed and abandoned the read. The retrieval record carries `verified_partial` with 262144 octets verified of 700000 returned. Under clause P11-3.49 the response says so, and the unverified proportion enters the figure of clause P11-8.28.

A scheduled fixity verification then fails on replica 2 of part 3. Under clause P11-3.78 that part is quarantined and not deleted, and under clause P11-3.79 a retrieval of `A-1` now returns the outcome naming an integrity failure at a named part rather than a not found. Under clause P11-6.42 the store repairs from replica 1, verifies the repair, and records both the failure and the repair. Had no good replica existed, the artifact would have remained quarantined and the outcome would have remained an integrity failure, which is the honest answer and is not available to a store whose taxonomy has only success and absence.

Two years later a referrer requests deletion. Four referrer registrations exist, one with a retention basis of `legal_hold`. Under clause P11-3.53 the deletion is refused and recorded. When the hold lifts and the deletion proceeds, a tombstone carries the address, the digest, the length, the reason and the four referrers registered at the instant of effect, three of which were notified and one of which could not be. A citation to `A-1` now resolves to that tombstone, which is what `Part 8` clause P8-12-30 and `Part 10` clause P10-12.35 both need in order to record their own reference as unresolvable rather than delete it.

## 4. Interfaces

### 4.1 Interface principles

**P11-4.1 (MUST) Operations defined over the entities of section 3.** An implementation must define every operation it exposes in terms of the entities of section 3 and must state which records each creates and which events it emits.

**P11-4.2 (MUST) Idempotency inherent for ingest.** An implementation must treat a resubmission of identical content within one deduplication scope as idempotent in effect, creating a new ingest record and no new artifact.

**P11-4.3 (MUST) Idempotency key accepted for state changing operations.** An implementation must accept a caller supplied idempotency key on every operation that changes state other than ingest, and must return the original result when invoked again with the same key and arguments.

**P11-4.4 (MUST) Authorisation obtained per operation.** An implementation must obtain an authorisation decision from `Part 7` before applying any ingest, retrieval, deletion, redaction, rebinding, alias change or placement change, and must record the decision reference.

**P11-4.5 (MUST NOT) No authorisation inferred from address knowledge.** An implementation must not treat a caller's knowledge of an address as evidence of entitlement to the content at it.

Clause P11-4.5 is the consequence of content addressing that most stores get wrong. Because the name is derived from the content, anyone who can guess or compute the content can compute the name, and anyone who has ever seen the name has it forever. An address is therefore a capability only if the content is unguessable, and a store that relies on that has made the security of every artifact a function of its entropy.

**P11-4.6 (MUST) One outcome per operation.** An implementation must return exactly one outcome from section 7 for every operation and must not return a success outcome where any part of the requested change was not applied.

**P11-4.7 (MUST) Refusals recorded.** An implementation must record every refused operation with the requesting party, the instant, the address or argument digest and the refusal code.

**P11-4.8 (MUST NOT) No operation that mutates content.** An implementation must not expose an operation that changes the octets retrievable under an existing address.

### 4.2 Ingest operations

| Operation | Effect |
|---|---|
| `submit_content` | Computes an address, stores or deduplicates, creates an ingest record |
| `submit_part` | Submits one part of a composite artifact |
| `declare_assembly` | Creates an assembly record over submitted parts and mints a root address |
| `probe_address` | Reports whether an address is held, subject to the controls of section 3.15 |
| `initiate_challenge` | Issues a possession challenge for a claimed duplicate |
| `answer_challenge` | Answers a possession challenge |

**P11-4.9 (MUST) Profile named on submission.** An implementation must require the address profile to be named on every submission and must reject a submission that names none.

**P11-4.10 (MUST) Length compared where declared.** An implementation must compare a declared length with the octets received and must reject a submission where they differ.

**P11-4.11 (MUST) Assembly declared before a root is minted.** An implementation must require every part of a composite artifact to be held before it mints the root address, and must reject an assembly naming an unheld part.

**P11-4.12 (MUST NOT) No probe that reveals another party's holding.** An implementation must not answer a probe in a way that reveals whether content is held by a party other than the requester, within a deduplication boundary broader than the requester's own.

**P11-4.13 (MUST) Challenge answerable only from content.** An implementation must construct a possession challenge such that it cannot be answered from the address alone, and must reject a challenge scheme that can be.

**P11-4.14 (MUST) Failed challenge recorded.** An implementation must record every failed possession challenge with the claiming party and the address claimed, since a pattern of them is an attempt to obtain content by name.

### 4.3 Retrieval operations

| Operation | Effect |
|---|---|
| `retrieve` | Returns octets, with a verification declaration |
| `retrieve_range` | Returns a stated octet range, with a verification declaration |
| `retrieve_part` | Returns one part of a composite artifact |
| `describe` | Returns the artifact record without the octets |
| `resolve_alias` | Returns the address an alias currently resolves to, recording the resolution |
| `verify` | Performs a verification without returning octets |

**P11-4.15 (MUST) Verification declaration returned to the caller.** An implementation must return the verification state with every retrieval and must not return octets without it.

**P11-4.16 (MUST) Range retrieval declares its verification limit.** An implementation must record and return, for a range retrieval, that verification of the whole artifact was not performed, unless it verified the whole artifact.

**P11-4.17 (MUST) Part retrieval verifiable independently.** An implementation must permit a part of a composite artifact to be verified against its own part address without retrieving the whole.

**P11-4.18 (MUST) Describe available for a tombstone.** An implementation must answer a describe request for a tombstoned or redacted address with the tombstone or redaction record.

**P11-4.19 (MUST NOT) No content returned for quarantined content.** An implementation must not return the octets of quarantined content as content, and may return them only under an operation that declares them unverifiable and names the failure.

**P11-4.20 (MUST) Verify available without retrieval.** An implementation must expose an operation that verifies stored content against its address and returns the outcome without transferring the octets to the caller.

### 4.4 Custody operations

| Operation | Effect |
|---|---|
| `register_referrer` | Records a declared reference and its retention obligation |
| `withdraw_referrer` | Ends a referrer registration |
| `extend_retention` | Raises the retention floor |
| `request_deletion` | Requests removal, subject to the floor |
| `request_redaction` | Requests removal of octets with retention of the record |
| `place_legal_hold` | Sets a legal hold |
| `release_legal_hold` | Releases a legal hold |
| `rebind_algorithm` | Adds an address under a further algorithm |
| `schedule_fixity` | Sets or changes a verification cadence for a class |
| `bind_alias` | Creates or rebinds an alias |
| `declare_placement` | Sets or changes the placement of an artifact |
| `assign_custodian` | Assigns or changes a custodian |

**P11-4.21 (MUST) Deletion refused below the floor.** An implementation must refuse a deletion or redaction request where the artifact's retention floor has not passed, and must record the refusal with the registrations that caused it.

**P11-4.22 (MUST) Deletion refused under legal hold.** An implementation must refuse every removal of an artifact under legal hold and must record the refusal.

**P11-4.23 (MUST) Removal names its referrers.** An implementation must record, on every removal, every referrer registration current at the instant of effect.

**P11-4.24 (MUST NOT) No deletion of the last replica without a declared act.** An implementation must not reduce the replica count of an artifact to zero other than by a deletion or redaction operation carrying an authorisation reference.

**P11-4.25 (MUST) Rebinding verified first.** An implementation must verify content against its existing address before minting a further address over it.

**P11-4.26 (MUST) Legal hold overrides a deletion already requested.** An implementation must refuse a pending deletion where a legal hold is placed before it is effected, and must record the refusal.

### 4.5 What a caller may and may not assume

**P11-4.27 (MUST) Content at an address never changes.** A caller may assume that the octets retrievable under an address will never differ from those originally addressed under it, or that the request will fail.

**P11-4.28 (MUST NOT) No assumption of verification.** A caller must not assume that returned octets were verified, and must read the verification declaration.

**P11-4.29 (MUST NOT) No assumption of durability from success.** A caller must not assume from a successful ingest that the content will remain retrievable for any interval, and must register as a referrer to create a retention obligation.

**P11-4.30 (MUST NOT) No assumption that absence means never existed.** A caller must not read a failure to retrieve as evidence that the address never resolved, and must distinguish the outcomes of section 7.2.

**P11-4.31 (MUST NOT) No assumption of convergence across profiles.** A caller must not assume that identical octets submitted under two profiles yield one address.

**P11-4.32 (MUST NOT) No assumption that an alias is stable.** A caller must not treat an alias as a citation and must record the address it resolved to.

**P11-4.33 (MUST) Describe answers where retrieve does not.** A caller may assume that a describe request answers for every address that has ever resolved, including tombstoned and redacted ones.

### 4.6 Reads from other components

| Read | Component | Pinning | On failure |
|---|---|---|---|
| Authorisation decision | `Part 7` | policy version pinned per decision | deny the operation; never permit on failure |
| Document identity and retention schedule | `Part 1` | pinned per artifact class | refuse the removal; do not remove on an unresolvable schedule |
| Party identity for submitter, custodian and referrer | `Part 10` | snapshot pinned per record | refuse the operation |
| Work item for a fixity investigation | `Part 8` | work item reference | leave the quarantine in place; do not resolve it |
| Schema of an event payload | `Part 9` | schema version pinned | refuse to emit; do not emit unvalidated |

**P11-4.34 (MUST) Reads treated as fallible.** An implementation must treat every read in the table in section 4.6 as fallible and must apply the stated failure behaviour rather than a default.

**P11-4.35 (MUST NOT) No proceeding on an authorisation failure.** An implementation must not proceed with an operation when the authorisation read fails, and must deny.

**P11-4.36 (MUST NOT) No removal on an unresolvable retention schedule.** An implementation must not remove content where the retention schedule governing it cannot be resolved.

### 4.7 Events emitted

**P11-4.37 (MUST) Event per state transition.** An implementation must emit an event for every artifact state transition, algorithm status change, quarantine, repair, removal, rebinding, alias rebinding and placement change.

**P11-4.38 (MUST) Event carries prior state and cause.** An implementation must carry on every event the address, the prior state where one changed, the instant, the acting party and the event's own identifier.

**P11-4.39 (MUST) Events delivered to the ledger.** An implementation must deliver every event to `Part 3` at least once and must retain the event until delivery is acknowledged.

**P11-4.40 (MUST) Fixity failure event distinct.** An implementation must emit a distinct event class for a fixity verification failure, naming the address, the part and the replica.

**P11-4.41 (MUST) Removal event names the referrers.** An implementation must name every registered referrer on the event announcing a removal.

**P11-4.42 (MUST) Algorithm status change event.** An implementation must emit an event on a change of a digest algorithm's status or collision resistance status, naming the count of artifacts addressed under it.

**P11-4.43 (MUST) Unverified retrieval event where a threshold is breached.** An implementation must emit an event where the proportion of unverified retrievals over a declared interval exceeds a declared threshold.

**P11-4.44 (SHOULD) Single replica signal.** An implementation should emit an event when an artifact's replica count falls to one.

## 5. State model

### 5.1 Six state models

Six, and the reason is that the questions are independent. The artifact state answers whether content is retrievable. The address binding state answers whether the name still resolves, which differs because a tombstoned address resolves and yields no content. The fixity state answers when the content was last known to match its address, which is a question about the past and not about now. The replica state answers the same question per copy, because corruption is a property of a copy and not of an artifact. The alias state answers whether a mutable name currently points anywhere. And the referrer registration state answers whether the obligations binding a deletion are current.

A store that carries one state instead of six answers all six questions with whichever it has. The commonest collapse is to fold fixity into artifact state, so content never verified and content verified this morning are both held, and the interval that matters is unrecoverable.

**P11-5.1 (MUST) States held as transitions.** An implementation must hold every state as a sequence of recorded transitions and must not hold it as a mutable field.

**P11-5.2 (MUST) One state per axis per instant.** An implementation must not represent two states of one entity on one axis as simultaneously current.

**P11-5.3 (MUST NOT) No derivation of one axis from another.** An implementation must not derive artifact state from fixity state, or alias state from artifact state.

**P11-5.4 (MUST) Transitions carry authorisation where required.** An implementation must record the authorising decision reference on every transition that requires one under section 4.

**P11-5.5 (MUST) Illegal transitions recorded.** An implementation must record every refused transition and must not discard the attempt.

**P11-5.6 (MUST NOT) No unlisted transition.** An implementation must not admit a transition this section does not list.

### 5.2 Artifact state

| State | Meaning | Terminal |
|---|---|---|
| `held` | Content is present and retrievable | no |
| `quarantined` | A fixity verification failed; content retained, not returned as content | no |
| `degraded` | Fewer replicas exist than the placement declares | no |
| `redacted` | Octets removed; address, digest, length and record retained | no |
| `deleted` | Content and address removed from the resolvable set; tombstone retained | yes |

Legal transitions: to `held` on first ingest; `held` to `quarantined` on a failed verification; `quarantined` to `held` on a verified repair; `held` to `degraded` on replica loss; `degraded` to `held` on replica restoration; `degraded` to `quarantined` on a failed verification; `held`, `quarantined` or `degraded` to `redacted` on an authorised redaction; `held`, `quarantined`, `degraded` or `redacted` to `deleted` on an authorised deletion.

**P11-5.7 (MUST) Deleted is the only terminal state.** An implementation must treat `deleted` as terminal and must not admit any transition out of it.

**P11-5.8 (MUST) Quarantine is not terminal.** An implementation must admit a transition out of `quarantined` on a verified repair, since a fixity failure on one replica is not a disposition of the artifact.

**P11-5.9 (MUST) Degraded distinguished from held.** An implementation must distinguish an artifact held in fewer replicas than declared from one at its declared placement, and must not report the first as the second.

**P11-5.10 (MUST) Repair verified before reinstatement.** An implementation must verify a repaired artifact against its address before returning it to `held`.

**P11-5.11 (MUST NOT) No transition out of redacted to held.** An implementation must not return a redacted artifact to `held` by reingestion of identical content, and must record such a reingestion as a distinct reinstatement artifact with its own ingest record. **Source.** A redaction is ordinarily performed because the content should not be held; permitting reingestion to reverse it silently defeats the act, and clause P11-3.65 forbids reuse of a tombstoned address for the same reason.

### 5.3 Address binding state

| State | Meaning | Terminal |
|---|---|---|
| `bound` | The address resolves to content or to a record of it | no |
| `superseded_algorithm` | The address remains bound and its algorithm's status is `verify_only` or `withdrawn` | no |
| `tombstoned` | The address resolves to a tombstone only | yes |

**P11-5.12 (MUST) Superseded algorithm binding still resolves.** An implementation must continue to resolve an address whose algorithm has been withdrawn from minting, and must not treat withdrawal from minting as withdrawal from resolution.

**P11-5.13 (MUST) Tombstoned binding resolves to the tombstone.** An implementation must resolve a tombstoned address to its tombstone and must not return a not found outcome.

### 5.4 Fixity state of an artifact

| State | Meaning | Terminal |
|---|---|---|
| `never_verified` | No verification has been performed since ingest | no |
| `verified_current` | The most recent verification passed and the cadence interval has not elapsed | no |
| `verification_due` | The cadence interval has elapsed since the last verification | no |
| `verification_failed` | The most recent verification failed | no |
| `unverifiable` | The content cannot be verified, being opaque to the store or redacted | no |

**P11-5.14 (MUST) Never verified distinguished from verified.** An implementation must distinguish content never verified since ingest from content whose verification passed, and must not treat successful ingest as a verification.

**P11-5.15 (MUST) Due distinguished from failed.** An implementation must distinguish content whose verification is overdue from content whose verification failed.

**P11-5.16 (MUST) Unverifiable declared.** An implementation must record content it cannot verify as unverifiable rather than as verified or as failed.

**P11-5.17 (MUST NOT) No fixity state terminal.** An implementation must not treat any fixity state as terminal, since a verification may be performed at any time.

### 5.5 Alias state

| State | Meaning | Terminal |
|---|---|---|
| `bound` | The alias resolves to an address | no |
| `unbound` | The alias exists and resolves to nothing | no |
| `retired` | The alias is withdrawn; its resolution history is retained | yes |

**P11-5.18 (MUST) Unbound distinguished from retired.** An implementation must distinguish an alias that currently resolves to nothing from one withdrawn from use.

**P11-5.19 (MUST) Resolution history retained on retirement.** An implementation must retain the full resolution history of a retired alias.

### 5.6 Replica state

| State | Meaning | Terminal |
|---|---|---|
| `present` | The replica holds the content and its last verification passed | no |
| `unverified` | The replica holds the content and has not been verified | no |
| `corrupt` | The replica's content failed verification | no |
| `lost` | The replica no longer holds the content | yes |

**P11-5.20 (MUST) Replica state held per replica.** An implementation must hold the state of each replica separately and must not report an artifact as present on the basis of one replica alone.

**P11-5.21 (MUST) Corrupt replica retained pending repair.** An implementation must retain a corrupt replica's record and must not delete the record when the replica is repaired or replaced.

**P11-5.22 (MUST) Artifact state derived from replica states declared.** An implementation must declare the rule by which artifact state follows from replica states and must apply it uniformly.

### 5.7 Referrer registration state

| State | Meaning | Terminal |
|---|---|---|
| `current` | The registration is in force and contributes to the retention floor | no |
| `withdrawn` | The registration is ended; retained for the record | yes |
| `unreachable` | The referrer could not be notified at the last attempt | no |

**P11-5.23 (MUST) Unreachable referrer recorded, not withdrawn.** An implementation must record a referrer it could not notify as unreachable and must not withdraw its registration on that ground.

**P11-5.24 (MUST) Unreachable referrers still bind the floor.** An implementation must continue to count an unreachable referrer's retention obligation in the floor.

## 6. Execution semantics

### 6.1 Determinism

**P11-6.1 (MUST) Address computation deterministic.** An implementation must produce the same address given the same octets and the same address profile version.

**P11-6.2 (MUST NOT) No environmental input to an address.** An implementation must not allow the instant, the submitter, the location, the storage layout or any value other than the octets and the profile parameters to affect an address.

**P11-6.3 (MUST) Verification deterministic.** An implementation must produce the same verification outcome given the same octets and the same address.

**P11-6.4 (MUST) Reproducible from the profile alone.** An implementation must be able to state, for any address it minted, the profile version under which it was minted, and must report `profile_unresolvable` where that profile version cannot be resolved.

**P11-6.5 (MUST NOT) No clock in addressing or verification.** An implementation must not consult the current instant in the computation of an address or the evaluation of a verification.

### 6.2 Ingest

The algorithm is narrative and binds nothing except where a clause names a step.

Resolve the named profile version and refuse where it is not `active`. Read the octets, counting the length. Where the profile mode is composite, divide the octets by the named chunker, address each part with the leaf tag prefixed, build the assembly by the named structure with the interior tag prefixed at each interior node, and mint the root. Where the mode is simple, address the whole. Compare the computed address with any claimed address and refuse a mismatch. Determine, within the declared deduplication scope, whether the address is already held. Where it is, apply the possession requirement, increment the ingest count, and record the submission as deduplicated. Where it is not, store to the declared placement and record the submission as stored. Write the ingest record with the outcome. Do not create a referrer registration; that is a separate declaration.

**P11-6.6 (MUST) Profile status checked at ingest.** An implementation must refuse a submission naming a profile version whose status is `deprecated` or `withdrawn` for minting, and must state which.

**P11-6.7 (MUST) Length counted, not trusted.** An implementation must count the octets it receives and must record its own count as the length.

**P11-6.8 (MUST NOT) No partial artifact addressed as whole.** An implementation must not mint an address over an incomplete transfer, and must refuse a submission whose transfer did not complete.

**P11-6.9 (MUST) Interrupted submission leaves no address.** An implementation must ensure that an interrupted submission mints no address and creates no artifact record, and must record the attempt.

**P11-6.10 (MUST NOT) No referrer registration created by ingest.** An implementation must not treat a submission as a declaration of reference, since the submitter may not be the party whose citation creates the retention obligation.

**P11-6.11 (MUST) Deduplication decided within the declared scope only.** An implementation must determine duplication only within the deduplication scope declared for the submission.

### 6.3 Deduplication and possession

**P11-6.12 (MUST) Possession requirement applied on every claimed duplicate.** An implementation must apply the scope's possession requirement to every submission it would deduplicate, and must not skip it because the address matches.

**P11-6.13 (MUST NOT) No content served on an unanswered challenge.** An implementation must not return content to a party whose possession challenge was not answered.

**P11-6.14 (MUST) Challenge derived from content, not from its address.** An implementation must derive a possession challenge from the octets, such as by requiring digests of positions the challenger selects, and must not derive it from the address.

**P11-6.15 (MUST) Constant response profile where required.** An implementation must apply the declared observability control on every submission within a scope whose boundary is broader than a single tenant, and must not apply it selectively.

**P11-6.16 (MUST) Deduplication proportion derivable.** An implementation must record enough for the proportion of stored octets serving more than one submitter to be derived, since that proportion is the measure of the exposure section 3.15 constrains.

**P11-6.17 (MUST NOT) No deduplication across a classification boundary.** An implementation must not deduplicate content across a boundary the deduplication scope declares as separating classifications.

### 6.4 Composite assembly and traversal

**P11-6.18 (MUST) Assembly verified on declaration.** An implementation must verify, on declaring an assembly, that each named part is held and that its address matches the address recorded in the assembly.

**P11-6.19 (MUST) Root recomputed on declaration.** An implementation must recompute the root address from the parts and the structure on declaring an assembly and must not accept a submitted root.

**P11-6.20 (MUST) Reconstitution verified against the root.** An implementation must verify a reconstituted octet sequence against the root address before returning it as verified.

**P11-6.21 (MUST) Missing part named.** An implementation must name the part that is missing where a composite artifact cannot be reconstituted, and must not report the composite as absent.

**P11-6.22 (MUST) Traversal depth bounded.** An implementation must bound the depth of assembly traversal, must record the depth reached and must report the bound being reached.

**P11-6.23 (MUST) Cycle refused.** An implementation must refuse an assembly in which a part's address appears among its own descendants, and must report the refusal.

### 6.5 Retrieval and verification

**P11-6.24 (MUST) Verification performed by default.** An implementation must verify content against the requested address on retrieval unless the caller has requested otherwise or a declared condition prevents it.

**P11-6.25 (MUST) Conditions permitting unverified return declared.** An implementation must declare the conditions under which it returns content unverified, must record which condition applied on each such retrieval, and must not return content unverified under an undeclared condition.

**P11-6.26 (MUST) Verification failure returned as such.** An implementation must return the outcome that names an integrity failure where verification fails, and must not return the octets as content.

**P11-6.27 (MUST) Verification failure quarantines.** An implementation must place content into quarantine on a verification failure detected during retrieval, and must emit the fixity failure event.

**P11-6.28 (MUST) Streaming verification declared.** An implementation must declare, where it returns octets before verification completes, that the return is unverified or partially verified, and must not declare it verified retrospectively.

**P11-6.29 (MUST NOT) No verification of a range presented as verification of the whole.** An implementation must not represent verification of a retrieved range as verification of the artifact.

**P11-6.30 (MUST) Repair attempted before failure returned where a replica may be good.** An implementation must attempt retrieval from another replica before returning an integrity failure where the placement declares more than one replica, and must record every replica read.

### 6.6 Fixity verification

**P11-6.31 (MUST) Cadence applied per class.** An implementation must perform scheduled verifications at the cadence declared for the artifact's class and must record every verification.

**P11-6.32 (MUST) Cadence breach exposed.** An implementation must expose the population of artifacts whose verification is overdue against the cadence in force.

**P11-6.33 (MUST) Every replica within the cadence.** An implementation must apply the cadence to each replica and must not treat a verification of one replica as satisfying the cadence for the others.

**P11-6.34 (MUST) Sampling parameters declared.** An implementation must declare the sampling parameters of any verification that reads less than the whole artifact and must record them on the verification.

**P11-6.35 (MUST NOT) No sampled verification counted as full.** An implementation must not count a sampled verification as satisfying a cadence declared as full.

**P11-6.36 (MUST) Verification of opaque content bounded to the ciphertext.** An implementation must record a verification of content it cannot read as a verification of the octets as held and must not represent it as a verification of the content's meaning or plaintext.

### 6.7 Algorithm migration

**P11-6.37 (MUST) Migration is additive.** An implementation must effect a migration to a new algorithm by adding addresses and must not retire existing addresses.

**P11-6.38 (MUST) Migration population countable.** An implementation must expose, for every algorithm whose status is other than `accepted`, the count of artifacts addressed under it and the count already rebound.

**P11-6.39 (MUST) Rebinding records both addresses.** An implementation must record, for every rebinding, the prior address, the new address, the instant, the verification that preceded it and the acting party.

**P11-6.40 (MUST NOT) No cross algorithm equivalence asserted without verification.** An implementation must not record two addresses as covering identical octets unless it verified the octets against both.

**P11-6.41 (MUST) Withdrawal from minting distinguished from withdrawal from resolution.** An implementation must permit an algorithm to be withdrawn from minting while remaining available for resolution and verification, and must record the two independently.

### 6.8 Deletion, redaction and garbage collection

The store cannot collect garbage safely, because it cannot enumerate its referrers. What it can do is refuse to collect into the gap and count the size of the gap.

**P11-6.42 (MUST NOT) No deletion on the store's own initiative.** An implementation must not delete or redact content except on an authorised request naming the content, and must not delete for capacity, cost, age or absence of access.

**P11-6.43 (MUST) Floor evaluated at the instant of effect.** An implementation must evaluate the retention floor at the instant a removal is effected and not at the instant it was requested.

**P11-6.44 (MUST) Removal refused where the referrer population is unknown and the policy requires it.** An implementation must declare whether a removal may proceed for an artifact with no referrer registration, must apply the declaration uniformly, and must record which was applied.

**P11-6.45 (MUST) Reference counting is not a substitute for the floor.** An implementation must not delete content on the basis that its referrer count reached zero, since a count of declared referrers is not a count of actual referrers.

**P11-6.46 (MUST) Parts of a composite removed only with the composite.** An implementation must not remove a part of a composite artifact while the composite's address remains bound, unless the removal is a redaction of the composite recorded as such.

**P11-6.47 (MUST) Shared part removal refused.** An implementation must refuse the removal of a part that is a constituent of another composite artifact whose retention floor has not passed.

**P11-6.48 (MUST) Redaction of a part propagates a declaration.** An implementation must record, on redacting a part, that every composite artifact containing it can no longer be reconstituted or verified, and must name them.

**P11-6.49 (MUST) Removal notification attempted and recorded.** An implementation must attempt to notify every current referrer of a removal and must record which notifications succeeded and which did not.

### 6.9 Concurrency, idempotence and bounds

**P11-6.50 (MUST) Concurrent identical submissions converge.** An implementation must ensure that concurrent submissions of identical content within one scope produce one artifact and one address, with an ingest record for each submission.

**P11-6.51 (MUST) Concurrent removal and retrieval serialised.** An implementation must serialise a removal against a retrieval of the same artifact and must not return partially removed content.

**P11-6.52 (MUST) Concurrent alias rebinding serialised.** An implementation must serialise concurrent rebindings of one alias and must record the losing attempt.

Bounds are declared rather than fixed because none of them can be set correctly for all content, and they are declared rather than left implicit because in this component an undeclared bound is discovered by a caller hitting it in production with a submission it cannot complete. A store that refuses a 40 gigabyte artifact without having said it would has not enforced a limit; it has failed an ingest for a reason the caller could not have anticipated, which is the same defect as an undeclared implementation decision anywhere else in this standard.

**P11-6.53 (MUST) Maximum artifact size declared.** An implementation must declare a maximum artifact size and must refuse a submission exceeding it. The value is an implementation decision because it trades against the chunking parameters and the placement, neither of which this part constrains.

**P11-6.54 (MUST) Maximum part count declared.** An implementation must declare a maximum part count for a composite artifact and must refuse an assembly exceeding it.

**P11-6.55 (MUST) Bounds recorded on the operation.** An implementation must record every bound it applied on any operation whose result the bound could have affected.

### 6.10 What this component may compute and what it may not

**P11-6.56 (MUST) Addressing and verification only.** An implementation must confine its computation over content to addressing, verification, chunking and assembly, and must not compute any other function over the octets.

**P11-6.57 (MUST NOT) No content inspection.** An implementation must not parse, index, transform, transcode, scan or extract from the octets it holds.

**P11-6.58 (MUST NOT) No derived representation stored as content.** An implementation must not store a thumbnail, preview, extracted text or other derived representation as an attribute of an artifact, and must require any derived representation to be submitted as its own artifact with its own address.

Clause P11-6.58 exists because a derived representation is content, and content in this component has an address, a fixity record and a retention obligation. A preview held as an attribute of another artifact has none of those, is not addressable, cannot be cited and will not survive a migration, and the component that generated it will assume it is durable.

## 7. Outcome and failure taxonomy

### 7.1 Why the taxonomy is the specification

A conventional store has two answers, being the content and not found, and a third it does not admit, being an error. Six distinct conditions arrive at the caller as not found: content that never existed, content deleted, content redacted, content quarantined after a fixity failure, content whose parts are incomplete, and content the caller may not have. They have six different remedies and one of them is a data loss incident. A caller that receives not found treats every one of them as the first.

This section is the specification because it is the only part of this component whose absence is not detectable from outside. A store that returns the wrong content is caught by the first verification. A store that returns not found where it should return an integrity failure is never caught, because the caller's own logic treats absence as an ordinary condition and moves on.

**P11-7.1 (MUST) One enumeration per value.** An implementation must draw every value it returns from exactly one enumeration in this section.

**P11-7.2 (MUST NOT) No value outside the enumerations.** An implementation must not return a value outside these enumerations and must not extend one marked closed.

**P11-7.3 (MUST) Properties of an outcome exposed.** An implementation must expose, for every retrieval outcome, the three properties in the table in section 7.7.

### 7.2 Retrieval outcomes

Closed enumeration.

| Value | Meaning |
|---|---|
| `returned_verified` | The octets were returned and verified in full against the requested address |
| `returned_verified_partial` | The octets were returned and a stated extent of them was verified |
| `returned_unverified` | The octets were returned and were not verified, under a declared condition |
| `never_held` | The address is well formed and this store has never held content under it |
| `deleted` | The address resolved and the content was removed by an authorised deletion |
| `redacted` | The address resolves and the octets were removed by an authorised redaction |
| `quarantined` | The content is held and failed verification, and is not returned as content |
| `incomplete_composite` | A part of a composite artifact is not available, and the part is named |
| `unverifiable_opaque` | The store cannot verify the content because it is opaque to it |
| `not_authorised` | `Part 7` denied the retrieval |
| `authorisation_unavailable` | `Part 7` could not be reached, and the retrieval was therefore denied |
| `address_malformed` | The address could not be parsed |
| `algorithm_unsupported` | The address names a digest algorithm this store does not implement |
| `profile_unresolvable` | The address names an address profile version this store cannot resolve |
| `unavailable_transient` | The content is held and could not be read at this attempt |
| `not_evaluated` | The retrieval was requested and not attempted |

**P11-7.4 (MUST) Never held distinguished from removed.** An implementation must distinguish an address it has never held from one whose content it removed, and must not report the second as the first.

**P11-7.5 (MUST NOT) No integrity failure returned as absence.** An implementation must not return `never_held`, `deleted` or `unavailable_transient` where verification failed, and must return `quarantined`. **Source.** This is the third instance in this standard of the same principle. `Part 7` refuses to return not applicable as deny because a coverage gap reported as a negative can never be found, and `Part 10` refuses to return an unknown code as non membership for the same reason. Here a corruption reported as absence is a data loss incident reported as an ordinary condition.

**P11-7.6 (MUST NOT) No transient unavailability reported as absence.** An implementation must not return `never_held` or `deleted` where the content is held and could not be read, and must return `unavailable_transient`.

**P11-7.7 (MUST) Redacted distinguished from deleted.** An implementation must distinguish content whose octets were removed with the record retained from content removed with only a tombstone retained.

**P11-7.8 (MUST) Incomplete composite names the missing part.** An implementation must name the unavailable part and its outcome when returning `incomplete_composite`, and must not report the composite as `never_held`.

**P11-7.9 (MUST) Authorisation refusal distinguished from absence.** An implementation must return `not_authorised` where a retrieval is denied and must not return `never_held`, since the two would otherwise be used to probe holdings.

**P11-7.10 (MUST) Authorisation refusal indistinguishable in effect where the scope requires it.** An implementation must, where a deduplication scope declares an observability control, ensure that the difference between `not_authorised` and `never_held` is not observable in timing or in any other channel, while recording the true outcome internally.

Clauses P11-7.9 and P11-7.10 pull in opposite directions and are both required. The record must be honest, because a caller that was refused and a caller whose content was never held need different remedies and an auditor needs to tell them apart. The externally observable behaviour must not permit holdings to be enumerated by a party who is refused. The resolution is that the recorded outcome is precise and the returned response is uniform where the scope requires it, and clause P11-8.14 makes the divergence itself recorded.

**P11-7.11 (MUST) Malformed address distinguished from unknown address.** An implementation must return `address_malformed` for an address it cannot parse and must not return `never_held`.

**P11-7.12 (MUST) Algorithm and profile failures distinguished.** An implementation must distinguish an address naming an algorithm it does not implement from one naming a profile version it cannot resolve.

### 7.3 Ingest outcomes

Closed enumeration.

| Value | Meaning |
|---|---|
| `stored` | The content was not held and is now stored |
| `deduplicated` | The content was already held within the scope, and the possession requirement was satisfied |
| `deduplicated_pending_possession` | The address matched and a possession challenge is outstanding |
| `claim_mismatch` | The submitter's claimed address differs from the computed address |
| `length_mismatch` | The declared length differs from the octets received |
| `transfer_incomplete` | The transfer did not complete and no address was minted |
| `profile_not_active` | The named profile version may not be used for minting |
| `algorithm_not_permitted_for_ingest` | The named algorithm's status forbids minting |
| `size_bound_exceeded` | The declared maximum artifact size was exceeded |
| `part_count_bound_exceeded` | The declared maximum part count was exceeded |
| `assembly_part_unheld` | An assembly named a part not held |
| `assembly_cycle_refused` | An assembly named a part among its own descendants |
| `tombstoned_address_refused` | The computed address bears a tombstone |
| `scope_not_permitted` | The submitter may not submit into the named deduplication scope |
| `not_authorised` | `Part 7` denied the submission |
| `authorisation_unavailable` | `Part 7` could not be reached, and the submission was denied |

**P11-7.13 (MUST) Stored distinguished from deduplicated.** An implementation must distinguish a submission that stored new content from one that matched existing content, and must record which.

**P11-7.14 (MUST NOT) No deduplication reported before possession is satisfied.** An implementation must not return `deduplicated` where a possession challenge is outstanding and must return `deduplicated_pending_possession`.

**P11-7.15 (MUST) Claim mismatch reported as such.** An implementation must return `claim_mismatch` where a claimed address differs from the computed one and must not silently accept the content under the computed address.

**P11-7.16 (MUST) Tombstoned address refused explicitly.** An implementation must return `tombstoned_address_refused` where the computed address bears a tombstone, and must not store the content under that address.

### 7.4 Verification outcomes

Closed enumeration.

| Value | Meaning |
|---|---|
| `verified` | The recomputed address matches the address claimed |
| `mismatch` | The recomputed address differs from the address claimed |
| `mismatch_length_only` | The length differs and the digest could therefore not be compared meaningfully |
| `algorithm_mismatch` | The two addresses name different algorithms and are not comparable |
| `profile_mismatch` | The two addresses name different profile versions and are not comparable |
| `incomplete_read` | The read did not complete and no comparison was made |
| `sampled_pass` | A sampled verification found no mismatch within the sample |
| `unverifiable_opaque` | The store cannot read the content |
| `unverifiable_redacted` | The octets no longer exist |
| `not_performed` | The verification was requested and not performed |

**P11-7.17 (MUST NOT) No sampled pass reported as verified.** An implementation must not return `verified` for a sampled verification and must return `sampled_pass` with the sampling parameters.

**P11-7.18 (MUST NOT) No incomplete read reported as a mismatch.** An implementation must not return `mismatch` where the read did not complete, and must return `incomplete_read`.

**P11-7.19 (MUST) Non comparability distinguished from failure.** An implementation must distinguish an algorithm or profile mismatch, which is a non comparison, from a digest mismatch, which is a failure.

**P11-7.20 (MUST) Unverifiable causes distinguished.** An implementation must distinguish content it cannot read from content whose octets no longer exist.

### 7.5 Removal outcomes and tombstone reasons

Closed enumeration of outcomes.

| Value | Meaning |
|---|---|
| `deleted` | The content and the address binding were removed and a tombstone written |
| `redacted` | The octets were removed and the address, digest, length and record retained |
| `refused_retention_floor` | The retention floor has not passed |
| `refused_legal_hold` | A legal hold is in force |
| `refused_shared_part` | The content is a part of a composite artifact whose floor has not passed |
| `refused_referrer_unknown` | The referrer population is unknown and the declared policy forbids removal in that case |
| `refused_not_authorised` | `Part 7` denied the removal |
| `refused_authorisation_unavailable` | `Part 7` could not be reached |
| `refused_schedule_unresolvable` | The governing retention schedule could not be resolved |

Closed enumeration of tombstone reasons: `authorised_deletion`, `authorised_redaction`, `retention_expiry_with_authorisation`, `legal_erasure_order`, `unrecoverable_loss`, `migration_supersession`.

**P11-7.21 (MUST) Refusal reasons distinguished.** An implementation must return the specific refusal reason for a removal and must not return one refusal for another.

**P11-7.22 (MUST) Loss recorded as loss.** An implementation must record an artifact that became unretrievable without an authorised act with the tombstone reason `unrecoverable_loss` and must not record it as a deletion.

**P11-7.23 (MUST NOT) No loss reported as an authorised removal.** An implementation must not attribute an unrecoverable loss to an authorising party or an authorising act.

Clause P11-7.23 prevents the most consequential misrecording this component can make. Content that was lost and content that was deleted are the same absence and completely different events. Recording a loss as a deletion attributes an accident to a decision, removes it from every loss figure, and destroys the evidence that the store failed.

### 7.6 System fault outcomes

Closed enumeration. These are the store's own inability to proceed and are never a statement about content.

| Value | Meaning |
|---|---|
| `metadata_store_unavailable` | The record store could not be read or written |
| `content_store_unavailable` | The octet store could not be reached |
| `dependency_unavailable` | A required component could not be reached |
| `placement_unsatisfiable` | The declared placement could not be achieved for a new artifact |
| `internal_invariant_violated` | The store detected a violation of its own invariants |

**P11-7.24 (MUST NOT) No fault reported as a statement about content.** An implementation must not report a system fault as a retrieval, ingest, verification or removal outcome.

**P11-7.25 (MUST) Unsatisfiable placement refuses the ingest.** An implementation must refuse an ingest it cannot store to the declared placement and must not store to a lesser placement silently.

**P11-7.26 (MUST) Invariant violation halts the affected content.** An implementation must stop applying changes to the affected artifact on detecting `internal_invariant_violated` and must raise the fault.

### 7.7 What distinguishes each outcome from absence

**P11-7.27 (MUST) Three properties exposed.** An implementation must expose the three properties in the following table with every retrieval outcome it returns.

| Outcome | Store ever held it | Octets exist now | Caller may infer the content is gone |
|---|---|---|---|
| `returned_verified` | yes | yes | not applicable |
| `returned_verified_partial` | yes | yes | not applicable |
| `returned_unverified` | yes | probably | not applicable |
| `never_held` | no | unknown | no, this store never had it |
| `deleted` | yes | no, in this store | yes, in this store |
| `redacted` | yes | no | yes, in this store |
| `quarantined` | yes | yes, and they do not match | no |
| `incomplete_composite` | yes | partly | no |
| `unverifiable_opaque` | yes | yes | not applicable |
| `not_authorised` | unknown to the caller | unknown to the caller | no |
| `authorisation_unavailable` | unknown to the caller | unknown to the caller | no |
| `address_malformed` | not applicable | not applicable | no |
| `algorithm_unsupported` | unknown | unknown | no |
| `profile_unresolvable` | unknown | unknown | no |
| `unavailable_transient` | yes | yes | no |
| `not_evaluated` | unknown | unknown | no |

Two of the sixteen license the inference that the content is gone. A store returning a single not found has told the caller that all sixteen are one of those two, and the caller that acts on it deletes its own reference, writes off the citation, or reports the record as unavailable to a regulator, in each case on evidence the store did not have.

### 7.8 Propagation

**P11-7.28 (MUST) Outcome carried whole.** An implementation must return the outcome together with its qualifying identifiers, being the named part, the named replica, the named refusal reason or the verification extent, and must not return the outcome value alone.

**P11-7.29 (MUST NOT) No aggregation losing the distinctions.** An implementation must not aggregate outcomes into a summary that loses the distinction between absence, removal and integrity failure.

**P11-7.30 (MUST) Non results retained where unconsumed.** An implementation must retain a non result in the record of the affected retrieval where no consumer subscribes to it.

**P11-7.31 (MUST) Counts report each outcome as its own category.** An implementation must report every outcome value as its own category in any count it publishes.

## 8. Observability and the audit record

### 8.1 What this component can and cannot see

This component can see everything about itself and nothing about its use. It knows every octet it holds, every address it minted and every retrieval it served, all completely, because it performs them. It does not know who cites its addresses, whether a caller verified what it returned after receiving it, or whether the content it holds still matters to anyone.

That is the same asymmetry `Part 7` and `Part 10` record, and this component's instance of it is narrower. `Part 7` cannot see enforcement; `Part 10` cannot see consumption; this component cannot see citation. In each case the component's own record is complete and the estate's state is not derivable from it.

**P11-8.1 (MUST) Completeness of each record declared.** An implementation must declare, for every population figure it publishes, whether the underlying record is complete by construction or incomplete by construction.

**P11-8.2 (MUST NOT) No citation figure presented as complete.** An implementation must not publish a figure about the citation of its content without publishing the count of artifacts with no referrer registration.

### 8.2 Grain

**P11-8.3 (MUST) Grain stated with every count.** An implementation must state the grain and the instant of computation with every count it reports.

**P11-8.4 (MUST) Artifact counts state their state filter.** An implementation must state which artifact states a count of artifacts includes, and in particular whether redacted and deleted artifacts are counted.

Deduplication makes every storage figure in this component ambiguous, and the ambiguity runs in the direction that flatters the store. The octets submitted and the octets stored differ by the deduplication ratio, so a figure reported without saying which it is will be read as the first by anyone assessing exposure and as the second by anyone assessing cost, and both readings are load bearing. The same ambiguity affects counts: an artifact serving nine referrers is one artifact, nine citations and one stored copy, and each of the three is the right answer to a different question.

**P11-8.5 (MUST) Octet counts state whether they are logical or physical.** An implementation must distinguish the octets submitted from the octets stored, since deduplication makes the two differ, and must state which a figure reports.

**P11-8.6 (MUST) Composite counts state their unit.** An implementation must state whether a count of artifacts counts composites, parts, or both.

**P11-8.7 (MUST NOT) No replica count reported as an artifact count.** An implementation must not report the number of stored copies as the number of artifacts.

### 8.3 What must be recorded

**P11-8.8 (MUST) Every submission recorded.** An implementation must record every submission, including refused and interrupted ones, at the grain of one record per submission.

**P11-8.9 (MUST) Every retrieval recorded.** An implementation must record every retrieval attempt with its outcome and its verification declaration, at the grain of one record per attempt.

**P11-8.10 (MUST) Every verification recorded.** An implementation must record every verification, whether it passed, failed or was not performed, at the grain of one record per verification per replica.

**P11-8.11 (MUST) Every removal and refusal recorded.** An implementation must record every removal and every refused removal with its reason.

**P11-8.12 (MUST) Every referrer registration and withdrawal recorded.** An implementation must record every referrer registration, extension and withdrawal.

**P11-8.13 (MUST) Every alias rebinding and resolution recorded.** An implementation must record every alias rebinding and every alias resolution.

**P11-8.14 (MUST) Divergence between recorded and returned outcome recorded.** An implementation must record, where an observability control caused the returned response to differ from the recorded outcome, both the recorded outcome and the fact that the response was uniform.

**P11-8.15 (MUST) Every rebinding recorded.** An implementation must record every algorithm rebinding with the verification that preceded it.

**P11-8.16 (MUST) Every placement change recorded.** An implementation must record every change to an artifact's placement and every replica loss.

**P11-8.17 (MUST) Every possession challenge recorded.** An implementation must record every possession challenge issued and its answer or failure.

### 8.4 What must be reconstructable

**P11-8.18 (MUST) The profile behind any address.** A reader must be able to reconstruct the address profile version under which any address was minted, and every parameter of it.

**P11-8.19 (MUST) The assembly behind any composite address.** A reader must be able to reconstruct the parts, order, offsets and structure of any composite artifact.

**P11-8.20 (MUST) The custody history of any artifact.** A reader must be able to reconstruct every ingest, verification, quarantine, repair, rebinding, placement change and removal affecting an artifact, in order.

**P11-8.21 (MUST) The verification state of any retrieval.** A reader must be able to establish, for any past retrieval, whether the octets returned were verified and to what extent.

**P11-8.22 (MUST) The referrers at the instant of a removal.** A reader must be able to reconstruct which referrers were registered when content was removed and which were notified.

**P11-8.23 (MUST) The reason content is no longer retrievable.** A reader must be able to establish, for any address that no longer resolves to content, whether it was deleted, redacted, lost or quarantined, and under whose authority where an authority acted.

**P11-8.24 (MUST) What an alias resolved to at an instant.** A reader must be able to reconstruct the address an alias resolved to at any past instant.

**P11-8.25 (MUST NOT) No reconstruction dependent on this component running.** An implementation must not require its own runtime to be available for the reconstruction of any record in section 8.4, and must be able to export the records in a form that outlives it.

### 8.5 Signals

Each signal names a population this component can count and cannot remedy alone.

**P11-8.26 (MUST) Never verified population.** An implementation must expose the count of artifacts never verified since ingest and the ingest instant of the oldest.

**P11-8.27 (MUST) Overdue verification population.** An implementation must expose the count of artifacts whose verification is overdue against the cadence in force, by class.

**P11-8.28 (MUST) Unverified retrieval proportion.** An implementation must expose the proportion of retrievals over a declared interval that returned octets unverified or partially verified.

**P11-8.29 (MUST) Quarantine population.** An implementation must expose every quarantined artifact with the instant of failure and the replica affected.

**P11-8.30 (MUST) Unrecoverable loss population.** An implementation must expose every artifact recorded as an unrecoverable loss, and must not aggregate it with authorised removals.

**P11-8.31 (MUST) Single replica population.** An implementation must expose every artifact held in one replica.

**P11-8.32 (MUST) Degraded placement population.** An implementation must expose every artifact held in fewer replicas than its placement declares.

**P11-8.33 (MUST) Unregistered citation population.** An implementation must expose the count of artifacts with no referrer registration, described as content whose citation status is unknown.

**P11-8.34 (MUST) Broken algorithm population.** An implementation must expose the count of artifacts whose primary address rests on an algorithm whose collision resistance status is `disputed` or `broken`, and the count already rebound.

**P11-8.35 (MUST) Deprecated profile population.** An implementation must expose the count of artifacts addressed under a profile version whose status is `deprecated` or `withdrawn`.

**P11-8.36 (MUST) Unreachable referrer population.** An implementation must expose every referrer it could not notify at the last attempt.

**P11-8.37 (MUST) Failed possession challenge rate.** An implementation must expose the rate of failed possession challenges by claiming party, since a pattern of them is an attempt to obtain content by name.

**P11-8.38 (MUST) Opaque content proportion.** An implementation must expose the proportion of held octets it cannot verify because they are opaque to it.

**P11-8.39 (SHOULD) Deduplication sharing distribution.** An implementation should expose the distribution of artifacts by the number of distinct submitters whose submissions they serve, since it is the measure of the exposure section 3.15 constrains.

### 8.6 The evidence package

**P11-8.40 (MUST) Package assemblable for an artifact.** An implementation must be able to assemble, for any artifact, a package containing its record, its address and profile, its assembly where composite, its full ingest, verification, quarantine, repair and removal history, its referrer registrations and its placement history.

**P11-8.41 (MUST) Package states what it omits.** An implementation must state, in every package, every element it could not include and why.

**P11-8.42 (MUST) Package integrity protected.** An implementation must integrity protect every package by a means governed by `Part 3`.

**P11-8.43 (MUST) Package assemblable for a tombstone.** An implementation must be able to assemble a package for a tombstoned address containing the tombstone, the last verification before removal and the referrers at the instant of effect.

### 8.7 Retention and what cannot be changed

**P11-8.44 (MUST) Records outlive content.** An implementation must retain the artifact record, ingest records, verification records and tombstone of an artifact after its content is removed, for at least as long as the longest retention obligation any referrer declared.

**P11-8.45 (MUST NOT) No alteration of an ingest, retrieval, verification or removal record.** An implementation must not alter any of those records once written.

**P11-8.46 (MUST NOT) No alteration of an address binding.** An implementation must not change the content an address binds to, in any circumstance including repair, which must restore the original octets or fail.

**P11-8.47 (MUST NOT) No removal of a tombstone.** An implementation must not remove a tombstone, since it is the only thing that distinguishes content removed from content never held.

**P11-8.48 (MUST) Legal hold refuses every disposition.** An implementation must refuse every removal of content under legal hold and must record the refusal.

## 9. Extension model

### 9.1 Closed sets and open sets

**P11-9.1 (MUST) Closed sets not extended.** An implementation must not extend the following: artifact states, address binding states, fixity states, alias states, replica states, referrer registration states, retrieval outcomes, ingest outcomes, verification outcomes, removal outcomes, tombstone reasons, system fault outcomes, verification declarations, encryption dispositions and possession requirements.

**P11-9.2 (MUST) Open sets extended only through a registry.** An implementation must extend the following only through the registries of section 9.2: digest algorithms, address profiles, chunkers, assembly structures, domain separation schemes, alias namespaces, deduplication scopes, location classes, content classes for cadence purposes and refusal codes.

**P11-9.3 (MUST NOT) No new state for a new storage technology.** An implementation must not introduce an artifact state to represent a storage tier, a medium or a latency class, and must express those as placement attributes.

The outcomes and states are closed because they are the vocabulary in which the record speaks, and section 7.7 classifies exactly the members listed. The algorithms and profiles are open because the whole of section 6.7 exists to admit new ones, and a store that cannot register a new digest algorithm cannot survive the retirement of the one it was built on.

### 9.2 Registry mechanics

**P11-9.4 (MUST) Registration before use.** An implementation must require every open set member to be registered before content or an operation uses it.

**P11-9.5 (MUST) Definition mandatory at registration.** An implementation must require a definition of every registered member's meaning and, for an algorithm, a reference to its specification.

**P11-9.6 (MUST) Registration attributable.** An implementation must record the registering party, the instant and the authorising decision for every registration.

**P11-9.7 (MUST NOT) No meaning change under a registered identifier.** An implementation must not alter the meaning or parameters of a registered member and must express a change as a new member or a new version.

**P11-9.8 (MUST) Retirement recorded, content retained.** An implementation must retain every artifact addressed under a retired member and must not remove the member from the register.

### 9.3 The digest algorithm registry

**P11-9.9 (MUST) Specification reference recorded.** An implementation must record a reference to the specification defining every registered digest algorithm.

**P11-9.10 (MUST) Digest length recorded.** An implementation must record the digest length of every registered algorithm and must reject an address whose digest length disagrees.

**P11-9.11 (MUST) Status transitions recorded.** An implementation must record every change of an algorithm's status and collision resistance status with its instant and its basis.

**P11-9.12 (MUST) At least one accepted algorithm at all times.** An implementation must maintain at least one algorithm with status `accepted` and must refuse to withdraw the last one.

**P11-9.13 (MUST NOT) No truncated digest admitted as a distinct algorithm without registration.** An implementation must register a truncated variant of a digest algorithm as its own member with its own length and must not accept a truncated digest under the full algorithm's identifier.

### 9.4 The address profile registry

**P11-9.14 (MUST) Every parameter recorded.** An implementation must record every parameter of a registered address profile version, being the algorithm, the canonicalisation declaration, the mode, the chunker and its parameters, the assembly structure and the domain separation scheme.

**P11-9.15 (MUST) Profile versioned, never edited.** An implementation must express any change to a profile as a new profile version and must retain the prior version as resolvable.

**P11-9.16 (MUST) Deprecation does not withdraw resolution.** An implementation must continue to resolve and verify addresses minted under a deprecated or withdrawn profile version.

**P11-9.17 (MUST) Default profile declared, never implicit.** An implementation must declare which profile version applies where a submitter names none, or must refuse such a submission, and must not vary the choice between submissions.

### 9.5 The assembly structure and domain separation registries

**P11-9.18 (MUST) Structure fully specified at registration.** An implementation must record, for every assembly structure, the arity, the ordering rule, the odd node handling and the single part case.

**P11-9.19 (MUST) Domain separation tags recorded.** An implementation must record the leaf tag and the interior tag of every domain separation scheme.

**P11-9.20 (MUST NOT) No structure without domain separation for a tree.** An implementation must not register a tree assembly structure that names no domain separation scheme.

### 9.6 The deduplication scope and placement registries

**P11-9.21 (MUST) Scope boundary and controls recorded.** An implementation must record the boundary, possession requirement and observability controls of every deduplication scope.

**P11-9.22 (MUST NOT) No scope broadening without a recorded act.** An implementation must not broaden the boundary of a deduplication scope without an authorised act, and must record the artifacts affected.

**P11-9.23 (MUST) Location classes registered with an independence basis.** An implementation must register every location class with the basis on which copies in different locations are claimed independent.

**P11-9.24 (MUST) Content classes registered with a cadence.** An implementation must register every content class used for fixity purposes with its verification cadence.

## 10. Standards and specifications

### 10.1 How the citations in this part are to be read

Each entry states what the source supplies, the edition established as current at the date of this part, and whether this part's account rests on specification text or on secondary sources. Section 13.1 lists the sources not obtained in full text.

This part's subject has more implemented practice than specified standard. Content addressing is specified in one ecosystem, in the multiformats content identifier, which is a community specification rather than a standard of a recognised body. Digest algorithms are specified in national standards. Merkle tree construction with domain separation is specified in an IETF standard for a purpose adjacent to this one. Deduplication's security properties are established in peer reviewed literature and in no standard at all. Fixity is treated as recorded information by preservation standards, which is the position this part adopts. Nothing consulted specifies a store of the kind this part specifies.

**P11-10.1 (MUST) Cited edition recorded.** An implementation must record the edition or version of every external standard it relies upon and must not cite a standard without its edition.

**P11-10.2 (MUST) Basis marked.** An implementation must record, for every control it adopts from a source named in this section, whether the basis is specification text or practice.

**P11-10.3 (MUST) Algorithm specification cited by edition.** An implementation must cite the specification and edition of every digest algorithm it registers.

### 10.2 Content addressing: the multiformats content identifier

**Supplies.** The self describing address. A version 1 content identifier is a binary structure prefixing a digest with a version code, a content type code and a multihash, the multihash itself prefixing a hash function code and a digest length. It supplies the requirement that a decoder reject a truncated digest or trailing bytes. It supplies, through the community's published profiles, the recognition that reproducible addresses across implementations require the chunking, layout and codec settings to be fixed.

**Does not supply.** Custody, fixity, retention, referrers, deletion, redaction or authorisation. It is an identifier specification and not a store specification.

**Basis.** Specification text for the structure and the decoder requirements. Documentation and community text for the profile concept and the default chunk size of 262144 octets.

### 10.3 Merkle construction: RFC 9162

**Supplies.** The construction of a Merkle tree with domain separation, prefixing leaf and interior node inputs with distinguishable octet values, and the inclusion and consistency proof structures over it.

**Does not supply.** Anything about storage. Its purpose is a verifiable append only log, not an artifact store, and this part adopts only the construction.

**Basis.** Specification text for the domain separation practice. This part did not obtain the full specification in this session and section 13.1 records it.

### 10.4 Digest algorithms and their retirement

**Supplies.** The algorithms themselves, in national standards for the second and third generation secure hash families, and the transition guidance that sets dates for the withdrawal of superseded algorithms.

**Does not supply.** Any model of how a store migrates. Section 6.7 is this part's own.

**Basis.** Secondary. A practical collision against the first generation algorithm was demonstrated in 2017 and national guidance has since set a withdrawal date; neither the collision paper nor the guidance was obtained in this session.

### 10.5 Deduplication security: the side channel literature

**Supplies.** The three attacks that follow from an observable cross user deduplication, being the learning of file contents by guessing and observing whether a submission deduplicated, the identification of whether a specific file is stored, and the establishment of a covert channel by the presence of a chosen file. It supplies the attack in which a party who knows a file's hash convinces a service performing client side deduplication that it owns the file and thereby obtains it, and records that a subset of the attacks was observed in the wild. It supplies the remedy, being proofs of ownership.

**Does not supply.** A standard. This is peer reviewed literature and there is no standard for secure deduplication.

**Basis.** Secondary, from the abstracts and from citing literature. Harnik, Pinkas and Shulman-Peleg, IEEE Security and Privacy 8(6):40 to 47, 2010; Halevi, Harnik, Pinkas and Shulman-Peleg, ACM CCS 2011, pages 491 to 500.

### 10.6 Fixity as recorded information: the preservation standards

**Supplies.** The treatment of fixity as information recorded about an object rather than an assumed property of storage, and the placement of fixity information within the preservation description of an archived package. It supplies the practice of recording verification events with their outcome.

**Does not supply.** A cadence, a sampling model or a quarantine state.

**Basis.** Secondary. Neither the reference model nor the preservation metadata dictionary was obtained in this session.

### 10.7 Named conflicts

| Conflict | Position A | Position B | Resolution | Reason |
|---|---|---|---|---|
| Whether a bare digest is an address | Widespread practice, including container distribution, addresses content by an algorithm prefixed hexadecimal digest with no profile | This part, clauses P11-3.4 to P11-3.7: the profile must be recoverable from the address | This part | The practice is adequate where only one profile has ever existed and one algorithm is in use. It fails at the first migration and at the first composite artifact, and it fails silently in both cases |
| Whether identical content has one address | The intuition of content addressing, and the reason it is adopted | This part, clauses P11-3.27 and P11-3.28: a composite address is a function of the octets and the profile, and equivalent roots are recorded rather than merged | This part | Documented in the ecosystem that took content addressing furthest, where users report the behaviour as a defect and the community answer is to publish profiles |
| Whether retrieval must verify | Practice verifies at ingest and not at retrieval, for latency | This part, clauses P11-6.24 and P11-3.48: verification by default, and where not performed the return is labelled unverified | This part, with the concession that unverified return is permitted where declared | A requirement to always verify is unobservable and will be ignored; a labelled return makes the trade measurable and leaves it with the caller |
| Whether knowledge of a hash establishes possession | Client side deduplication practice accepts a hash as a claim of possession, since that is what makes it save bandwidth | This part, clause P11-3.81: never | This part | The attack is published, was observed in the wild, and turns the store into a service that hands over any file whose digest is known |
| Whether a not found answer suffices | Practice returns one absence outcome | This part, section 7.2: sixteen outcomes of which two license the inference that content is gone | This part | A corruption reported as absence is a data loss incident reported as an ordinary condition |
| Whether the store may reclaim space | Practice permits lifecycle rules that expire content by age or tier | This part, clauses P11-1.21 and P11-6.42: never on its own initiative | This part, as required of it by `Part 7` section 12.11 | The store cannot enumerate its referrers, so no age or access based rule can establish that content is no longer cited |

### 10.8 What none of the standards supplies

**P11-10.4 (MUST) Requirements of this part alone identified.** An implementation must treat the following as requirements of this part alone, no consulted source supplying them: the address profile as a registered versioned entity; the recording of equivalent composite roots without merging them; the verification declaration on every retrieval; the sixteen member retrieval outcome enumeration and its distinctions; the retention floor derived from referrer registrations; the tombstone as a resolvable record; redaction as distinct from deletion and from erasure; the prohibition on removal by the store's own initiative; the quarantine state; the unrecoverable loss tombstone reason and its separation from authorised removal; and the algorithm migration model of section 6.7.

## 11. Anti patterns

### 11.1 The digest presented as an address

**Mechanism.** Content is named by a hexadecimal digest, optionally with an algorithm prefix, and nothing else.

**Evidence.** It is the dominant practice. The self describing alternative exists and is specified, prefixing the digest with codes for the hash function and the digest length within a structure that also types the content.

**Consequence.** At the first algorithm migration the store cannot tell which of its names to recompute how. At the first composite artifact two implementations mint different names for identical octets and both are right. Neither failure is visible until it is expensive.

**P11-11.1 (MUST) Address self describing.** An implementation must ensure the algorithm, profile and mode are recoverable from the address alone.

### 11.2 The chunking parameter nobody recorded

**Mechanism.** Large content is divided for storage and transfer, the root is minted over the division, and the division parameters are a property of the code rather than of the name.

**Evidence.** The ecosystem that took content addressing furthest publishes profiles for exactly this reason, and its users report identical files acquiring different identifiers in different tools.

**Consequence.** The store's central promise, that the name determines the content, holds; the converse, that the content determines the name, does not, and callers assume both. Two components that independently address the same file cannot recognise that they hold the same thing.

**P11-11.2 (MUST) Chunking recorded in the profile and the profile in the address.** An implementation must record the chunking parameters in the profile and identify the profile in the address.

### 11.3 The unverified retrieval reported as content

**Mechanism.** Octets are streamed to the caller as they are read, because verification requires the whole object and latency matters, and the response says nothing.

**Evidence.** Verification is the store's only distinctive guarantee and is the first thing sacrificed under load. Nothing in any consulted specification requires the omission to be disclosed.

**Consequence.** Corruption is served as content and a substitution is served as the original. The proportion of unverified reads is unknown, so the guarantee's actual strength is unknown, and no incident will reveal it because the caller has no basis on which to doubt what it received.

**P11-11.3 (MUST) Verification state declared on every retrieval.** An implementation must declare on every retrieval whether the octets were verified.

### 11.4 The integrity failure returned as not found

**Mechanism.** A read fails its checksum, the store has no outcome for it, and it returns absence.

**Evidence.** Section 7.2 requires sixteen outcomes; a conventional store has two.

**Consequence.** A data loss incident is delivered as an ordinary condition. The caller marks its reference unresolvable and moves on, the loss is never escalated, and the store's loss figure is zero because losses are indistinguishable from deletions.

**P11-11.4 (MUST NOT) No integrity failure as absence.** An implementation must not return an absence outcome where verification failed.

### 11.5 The loss recorded as a deletion

**Mechanism.** Content becomes unretrievable, the operator records a deletion to tidy the state, and the tombstone carries an authorising party.

**Evidence.** Both produce the same absence and only one has a decision behind it.

**Consequence.** An accident is attributed to a decision. It leaves every loss figure, the store reports full durability, and the evidence that it failed is destroyed by the act of recording the failure.

**P11-11.5 (MUST) Loss recorded as loss.** An implementation must record unrecoverable loss with its own tombstone reason and must not attribute it to an authorising act.

### 11.6 The hash accepted as proof of possession

**Mechanism.** A client offers a digest, the store recognises it, and the upload is skipped and the content made available to the client.

**Evidence.** The attack is published and was observed in the wild against a file synchronisation service: a party knowing a file's hash can convince a service performing client side deduplication that it owns the file and thereby obtain the whole of it. The remedy of proofs of ownership followed a year later.

**Consequence.** The store is a service that hands over any file whose digest is known, and digests circulate freely because they are how content is cited.

**P11-11.6 (MUST NOT) No digest as possession.** An implementation must not treat knowledge of a digest as evidence of possession.

### 11.7 The observable deduplication

**Mechanism.** A submission that deduplicates returns faster, or consumes no quota, and the difference is visible to the submitter.

**Evidence.** Three attacks follow, published in the same work: learning a file's contents by guessing it and observing whether it deduplicated, establishing whether a specific file is stored, and signalling a bit by the presence of a chosen file.

**Consequence.** The store becomes an oracle answering whether any guessable content exists anywhere in it, across every tenant, for anyone able to submit.

**P11-11.7 (MUST NOT) No observable cross tenant deduplication.** An implementation must not permit a submitter to determine whether content was already held by another party.

### 11.8 The lifecycle rule that reclaimed cited content

**Mechanism.** Content untouched for a declared interval is expired to a cheaper tier or deleted, because access is a proxy for value.

**Evidence.** Access is not a proxy for citation. An evidence package assembled once and cited in a determination retained for twenty five years will not be read again until it is needed.

**Consequence.** Precisely the content whose value is highest is deleted first, because value here is inversely related to access frequency.

**P11-11.8 (MUST NOT) No expiry by age or access.** An implementation must not remove content on the basis of its age or its access frequency.

### 11.9 The reference count taken for a referrer count

**Mechanism.** The store counts declared references, reaches zero and collects.

**Evidence.** Clause P11-3.54. A count of declared referrers is a count of those that declared.

**Consequence.** Content is deleted while cited by every component that never registered, which is every component that was not told it had to. The failure appears years later as a citation that resolves to nothing.

**P11-11.9 (MUST NOT) No collection on a zero declared count.** An implementation must not delete content because its declared referrer count reached zero.

### 11.10 The tag treated as a citation

**Mechanism.** A mutable name is used where an address was required, because it is readable and because it follows the content.

**Evidence.** An alias is a pointer with a history; an address is a name with a guarantee.

**Consequence.** A determination cites a name that resolves to different content next month. Everything downstream of it is unreproducible and nothing reports that anything changed.

**P11-11.10 (MUST NOT) No alias in a citation.** An implementation must not accept an alias where a citation is required.

### 11.11 The address treated as a capability

**Mechanism.** Content is protected by the unguessability of its address, since a caller who does not know the address cannot fetch it.

**Evidence.** The address is derived from the content, so anyone who can guess the content can compute the address, and anyone who has ever held the address holds it permanently.

**Consequence.** Authorisation is a function of content entropy. A short, structured or guessable document is readable by anyone who guesses it, and a leaked address cannot be revoked because it is not a credential.

**P11-11.11 (MUST NOT) No entitlement from address knowledge.** An implementation must not treat knowledge of an address as entitlement to the content.

### 11.12 The store that learned to read

**Mechanism.** The store extracts text, generates previews, indexes content or transcodes formats, because it has the octets and the need is real.

**Evidence.** Clause P11-1.15 and clause P11-6.57. Every such capability requires knowledge of content types.

**Consequence.** The store acquires a parser, and with it a vulnerability surface over untrusted content, a dependency on format libraries, and a reason to fail an ingest for a content reason. Its derived outputs are held as attributes, so they are unaddressable, uncitable and will not survive a migration.

**P11-11.12 (MUST NOT) No content inspection.** An implementation must not parse, index, transform or extract from the octets it holds.

### 11.13 The repair that changed the content

**Mechanism.** A corrupt object is repaired by regenerating it from a source, and the regenerated object differs slightly from the original.

**Evidence.** Regeneration reproduces content, not octets. A recompressed image, a re-serialised document and a rebuilt archive are new octets with a new address.

**Consequence.** The address now binds to content that is not what was addressed, which is the one thing the store exists to make impossible. Every past verification record becomes false and every citation is silently misdirected.

**P11-11.13 (MUST) Repair restores the octets or fails.** An implementation must restore the original octets on repair and must fail rather than bind an address to different content.

### 11.14 The single replica behind a durability figure

**Mechanism.** A durability figure is published from the storage layer's specification while content is held in one copy in one location.

**Evidence.** Clause P11-2.6. A durability claim is a claim about survival and not a verification of content.

**Consequence.** The figure describes a configuration that is not in force. The population held in one replica is not exposed, so nobody knows the exposure, and the first correlated failure takes content that was reported as safe.

**P11-11.14 (MUST) Single replica population exposed.** An implementation must expose every artifact held in one replica.

### 11.15 Fixity assumed from the absence of failures

**Mechanism.** No verification failures have been reported, so fixity is assumed good.

**Evidence.** Preservation practice treats fixity as recorded information. Where verification is not performed, there are no failures to report.

**Consequence.** A store that has never verified anything reports the same figure as one that verifies everything nightly. The interval within which undetected corruption can persist is the age of the store.

**P11-11.15 (MUST) Never verified population exposed.** An implementation must expose the count and oldest ingest instant of artifacts never verified.

### 11.16 The sampled verification counted as a verification

**Mechanism.** A percentage of octets or of objects is verified, and the result is reported as the fixity of the whole.

**Evidence.** Clause P11-3.77.

**Consequence.** A figure that describes a sample is read as describing the population. Corruption in the unsampled remainder is not merely undetected but reported as absent.

**P11-11.16 (MUST NOT) No sampled verification reported as full.** An implementation must not report a sampled verification as a full one.

### 11.17 The one replica verified for all

**Mechanism.** Verification reads whichever replica is cheapest and the result is recorded against the artifact.

**Evidence.** Clause P11-3.76. Corruption is a property of a copy.

**Consequence.** The replica that is never read is never verified, and it is the one that will be needed when the primary fails. The verification programme has been measuring the copy that is least at risk.

**P11-11.17 (MUST) Replica identified per verification.** An implementation must record which replica each verification read.

### 11.18 The deduplicated part deleted for one referrer

**Mechanism.** A referrer requests deletion of content it submitted, and the store deletes it, because the requester is the owner.

**Evidence.** Deduplication means the requester's submission and eight other referrers' citations are the same octets.

**Consequence.** Eight citations break on one party's request. The store cannot tell the requester that its content is shared without revealing that others hold it, which is why clause P11-3.53 makes the floor rather than the requester's ownership the governing condition.

**P11-11.18 (MUST NOT) No deletion below the floor on the submitter's request.** An implementation must not delete content below its retention floor on the request of the party that submitted it.

### 11.19 The erasure that could not be performed

**Mechanism.** An erasure obligation arrives, the store deletes its copies, and reports the obligation discharged.

**Evidence.** Clause P11-3.62. The store held some copies and did not hold every copy.

**Consequence.** A report of erasure is made on evidence the store does not have, and the party relying on it believes an obligation is discharged that is not.

**P11-11.19 (MUST NOT) No erasure claim beyond custody.** An implementation must confine an erasure assertion to the copies it held.

### 11.20 The redaction that erased the record

**Mechanism.** Content is redacted and its record removed with it, so that nothing remains.

**Evidence.** Clause P11-3.60. A citation to the address still exists in another component.

**Consequence.** The citing component's reference resolves to nothing, and it cannot distinguish content it was never entitled to from content that was removed. `Part 8` and `Part 10` both require the distinction and neither can make it without this component.

**P11-11.20 (MUST) Redaction retains the record.** An implementation must retain the address, digest, length and record of redacted content.

### 11.21 The migration that retired the old address

**Mechanism.** Content is rebound under a stronger algorithm and the old address is withdrawn to force adoption.

**Evidence.** Every citation ever made used the old address.

**Consequence.** Every existing citation breaks at once, and the citations that break are the oldest ones, which are the ones in the determinations with the longest retention.

**P11-11.21 (MUST) Migration additive.** An implementation must retain the prior address as resolvable after a rebinding.

### 11.22 The convergent encryption that leaked equality

**Mechanism.** Content is encrypted with a key derived from itself so that identical plaintexts encrypt identically and still deduplicate.

**Evidence.** The scheme is well known and its exposure is inherent: the store, and anyone observing it, learns that two parties hold the same plaintext.

**Consequence.** The encryption is defeated for its most likely purpose, which is concealing which of a known set of documents a party holds, and the exposure is undeclared because it looks like ordinary deduplication.

**P11-11.22 (MUST NOT) No convergent deduplication without a declared exposure.** An implementation must not deduplicate deterministically encrypted content without declaring the exposure.

### 11.23 The store that held the only key

**Mechanism.** The store encrypts content at rest and holds the keys, so that a key loss is a content loss and a key compromise is a content compromise.

**Evidence.** Clause P11-3.91.

**Consequence.** The independence of the replicas is defeated by a dependency none of them records. Every copy is unreadable on one event, and the durability figure describes the octets rather than the content.

**P11-11.23 (MUST) Key custody separated.** An implementation must not hold both the only key and the only copy of the content it protects.

### 11.24 The location that became the identity

**Mechanism.** Content is referred to by its path, bucket key or URL, because that is what the storage layer returns.

**Evidence.** `Part 7` clause P7-12.30 requires addressing by digest and forbids reliance on a location as identity.

**Consequence.** A migration, a re-tiering or a re-organisation invalidates every reference, and nothing detects it because a location that resolves to different content is a location doing its job.

**P11-11.24 (MUST NOT) No location as identity.** An implementation must not derive identity from a location.

## 12. Boundaries with other parts

Every subsection states what this component delegates, what it must not absorb, the naive conflation, and the reciprocal this part requires of the other. Subsection numbers correspond to part numbers; there is no 12.11 because this is Part 11.

### 12.1 Boundary with Part 1, controlled documents and records

**Delegated.** Approval, effective date, supersession as a document, retention schedule, disposition authority and point in time citation of every controlled document whose octets this component holds.

**Must not absorb.** Document lifecycle and disposition authority. This component holds octets and refuses to remove them without an authorised act; it does not decide when the act is due.

**Naive conflation.** The store implements retention itself, because it knows the ingest instant and can compute an expiry, so content is deleted on a schedule the document authority never approved and a controlled record is disposed of by a storage rule.

**Reciprocal.** `Part 1` must declare that it owns the retention schedule and the disposition authority for the content this component holds, that it requires an authorised disposition act rather than an expiry rule, that it treats an address as the citation of a document's octets and resolves such a citation to the version in force at the cited instant, and that it accepts a tombstone as the resolution of a citation to removed content.

**P11-12.1 (MUST) Retention schedule obtained.** An implementation must obtain the retention schedule governing any class of content from `Part 1` and must not compute an expiry of its own.

**P11-12.2 (MUST) Disposition authorised, never scheduled.** An implementation must require an authorised disposition act for every removal and must not remove content on the elapse of a schedule alone.

**P11-12.3 (MUST) Records treated as records.** An implementation must treat its ingest, retrieval, verification, removal and tombstone records as records in the `Part 1` sense and must not revise one.

**P11-12.4 (MUST) Address supplied as a citable identity.** An implementation must supply an address that `Part 1` can cite as the identity of a document version's octets, and must resolve that citation to the same octets for as long as they are held.

### 12.2 Boundary with Part 2, business rules and constraint evaluation

**Delegated.** Every rule about what content may be submitted, retained or removed, and every constraint whose evaluation requires anything beyond the octets and the profile.

**Must not absorb.** Rule evaluation. Addressing and verification are computations, not evaluations, and everything else this component might decide is a rule.

**Naive conflation.** The store enforces a content policy, refusing submissions on size, type or scanning outcome, so a policy exists in a component with no rule identity, no versioning and no verdict vocabulary.

**Reciprocal.** `Part 2` must declare that it owns rule identity, evaluation and verdicts, that it does not hold content, and that where a rule's evaluation requires content it obtains the octets by address from this component rather than holding them.

**P11-12.5 (MUST NOT) No content policy evaluated here.** An implementation must not refuse a submission on any ground other than those enumerated in section 7.3.

**P11-12.6 (MUST) Octets supplied for evaluation, not evaluated.** An implementation must supply octets by address where a rule's evaluation requires them and must not evaluate the rule.

### 12.3 Boundary with Part 3, provenance and audit ledger

**Delegated.** The evidentiary chain, and the reconstruction of a determination spanning components.

**Must not absorb.** The chain. The store's digests establish that octets are the octets that were addressed; they establish nothing about what any determination concluded.

**Naive conflation.** The store's Merkle structures are treated as the audit chain, because they are hash linked and tamper evident, so a reader finds integrity without provenance and cannot establish what any of it was for. Or, in the other direction, the ledger stores its own material inline and becomes a second artifact store with its own integrity story.

**Reciprocal.** `Part 3` must declare that it owns the evidentiary chain, that it holds the octets of any evidence package by address here rather than inline, that the integrity of an artifact and the integrity of a chain are separate claims, and that it notifies this component of the retention obligation any determination citing an address creates.

**P11-12.7 (MUST) Events emitted to the ledger.** An implementation must emit every event of section 4.7 to `Part 3`.

**P11-12.8 (MUST NOT) No chain asserted.** An implementation must not represent its addressing or assembly structures as the evidentiary chain of a determination.

**P11-12.9 (MUST) Retention notification accepted.** An implementation must accept a notification from `Part 3` that a determination citing an address is retained to a stated instant, and must raise the retention floor accordingly.

**P11-12.10 (MUST) Package material addressed, not inlined.** An implementation must accept the octets of an evidence package as artifacts with addresses and must supply them by address.

### 12.4 Boundary with Part 4, metadata and model repository

**Delegated.** The meaning, lineage and governed definition of anything the content describes.

**Must not absorb.** Meaning. The store's only metadata about content is what addressing requires and what the submitter claimed.

**Naive conflation.** The store becomes the metadata repository because it is where the files are, so descriptive metadata accumulates as artifact attributes, unversioned, uncitable and outside impact analysis.

**Reciprocal.** `Part 4` must declare that it owns governed definitions and their lineage, that it holds no octets, and that where a definition is carried in a document it references that document's octets by address here.

**P11-12.11 (MUST NOT) No descriptive metadata held.** An implementation must not hold descriptive or governed metadata about content beyond the submitter's claimed content type and the fields of section 3.5.

**P11-12.12 (MUST) Address supplied for a governed artifact.** An implementation must supply an address that `Part 4` can hold as the reference to the octets of a governed artifact.

### 12.5 Boundary with Part 5, decision engine

**Delegated.** Any selection among candidate content, replicas, placements or profiles that is a governed business outcome.

**Must not absorb.** Business selection. Selecting the nearest replica to read is an operational optimisation; selecting which of two candidate documents is authoritative is a decision.

**Naive conflation.** The store resolves which of several addresses is the right one for a caller, because it can see them all.

**Reciprocal.** `Part 5` must declare that it owns business outcome selection and that it identifies content by address rather than by description.

**P11-12.13 (MUST NOT) No selection among candidate addresses.** An implementation must not select among candidate addresses on a caller's behalf and must return the set with its records.

**P11-12.14 (MAY) Replica selection permitted.** An implementation may select which replica to read, which is an operational choice and not a decision, and must record the replica read.

### 12.6 Boundary with Part 6, workflow and process orchestration

**Delegated.** The sequencing of ingest, review, verification and disposition where that sequencing is a defined process.

**Must not absorb.** Control flow. An artifact's state transitions are facts about content, not a process instance's position.

**Naive conflation.** The custody lifecycle is implemented as a workflow, so the state of an artifact cannot be read without the process engine and a stalled process makes content unretrievable.

**Reciprocal.** `Part 6` must declare that it owns control flow, that an artifact state is a fact held here, and that it references any payload it carries by address rather than embedding it.

**P11-12.15 (MUST) State is a fact, not a position.** An implementation must hold every state of section 5 as its own fact and must not derive it from a process instance's position.

**P11-12.16 (MUST) Retrieval independent of any process.** An implementation must serve a retrieval without reference to the state of any process instance.

### 12.7 Boundary with Part 7, policy decision point and authorisation

**Delegated.** Every decision on whether a party may submit, retrieve, describe, remove, redact, rebind, or bind an alias.

**Must not absorb.** Authorisation, and in particular the temptation to treat the address as the credential.

**Naive conflation.** Address knowledge is the access control, so a leaked address is a permanent unrevocable grant, and content with low entropy is readable by anyone who guesses it.

**Reciprocal, and its discharge.** `Part 7` section 12.11 requires this part to declare three things. That it holds no decision, no attribute value provenance and no policy state: clause P11-1.14. That it does not delete content on its own authority: clauses P11-1.21 and P11-6.42. And clause P7-12.30 requires that content be addressed by digest under a declared canonical form profile with no reliance on location as identity, which sections 3.2 and 3.4 discharge and clause P11-2.3 states directly.

**P11-12.17 (MUST) Authorisation obtained per operation.** An implementation must obtain an authorisation decision at the instant of every operation section 4.1 requires one for, and must record the reference.

**P11-12.18 (MUST NOT) No authorisation decision rendered.** An implementation must not decide whether a party may read or change content.

**P11-12.19 (MUST NOT) No decision, provenance or policy state held.** An implementation must not hold a decision, an attribute value provenance or a policy state as its authoritative record.

**P11-12.20 (MUST) Refusal recorded without leaking holdings.** An implementation must record an authorisation refusal precisely and must not permit the difference between a refusal and an absence to be observable where a deduplication scope declares a control, per clauses P11-7.9 and P11-7.10.

### 12.8 Boundary with Part 8, human task and case management

**Delegated.** The work by which a custodian investigates a fixity failure, adjudicates a removal request or reviews a loss: the queue, the assignment and the case. Also the association of an artifact with a case or a work item.

**Must not absorb.** Task management, and the association. The store holds octets and does not know that they are an attachment to anything.

**Naive conflation.** The store acquires the association, so the reason an artifact exists lives in the component that cannot interpret it, and the quarantine backlog is a list nobody outside the store can see.

**Reciprocal, and its discharge.** `Part 8` clauses P8-12-28 to P8-12-30 require that component not to store attachment bytes, to hold the content address and own the association, and to record an association as unresolvable where an address ceases to resolve rather than deleting it. The last requires this component to make the distinction available, which clause P11-3.59 and section 7.2 do: a tombstoned address resolves to its tombstone, and `never_held`, `deleted`, `redacted` and `quarantined` are four distinct outcomes rather than one absence.

**P11-12.21 (MUST NOT) No association held.** An implementation must not hold the association between an artifact and a case, work item, party or purpose.

**P11-12.22 (MUST) Unresolvable distinguished from absent.** An implementation must distinguish an address that once resolved from one it never held, so that a citing component can record its reference as unresolvable rather than delete it.

**P11-12.23 (MUST) Investigation obtained, not managed.** An implementation must obtain the work by which a person investigates a quarantine or a loss from `Part 8` and must record the work item reference on the resulting record.

**P11-12.24 (MUST) Quarantine population exposed outside the store.** An implementation must expose the quarantine and loss populations so that they can be worked outside this component.

### 12.9 Boundary with Part 9, schema and contract registry

**Delegated.** Schema identity, versioning, compatibility and validation, including of this component's own event payloads.

**Must not absorb.** Validation, versioning, and the canonical digests that component computes for its own purposes.

**The seam, stated precisely.** Both components compute digests over the same artifact and neither is the other. This component addresses the octets as submitted, under a profile that declares whether any canonicalisation was applied and by whom. That component computes a literal digest over the registered bytes, a canonical digest over a form defining reader equivalence, and a compatibility digest over a form retaining what its rule sets consult. Four numbers over one file, all correct, none interchangeable. A store that offers its address as the schema's identity, or a registry that offers its canonical digest as an address, has conflated two purposes.

**Reciprocal, and its discharge.** `Part 9` clauses P9-12-18 and P9-12-19 require that component not to store artifact bytes and to hold the content address of every registered artifact, retaining the identities it derives from the content. This component discharges the corresponding obligation by clause P11-3.15, which refuses to canonicalise on its own initiative, and by clause P11-12.26, which requires the address and the registry's digests to be recorded as distinct.

**P11-12.25 (MUST NOT) No validation performed.** An implementation must not validate content against a schema.

**P11-12.26 (MUST NOT) No address offered as a schema identity.** An implementation must not represent an address as the identity of a schema, and must not represent a digest computed by `Part 9` as an address.

**P11-12.27 (MUST) Canonicalised octets accepted as submitted.** An implementation must accept canonicalised octets as the content submitted, must record which canonicalisation the profile declared, and must not canonicalise on its own initiative.

**P11-12.28 (MUST) Event payload schema obtained.** An implementation must obtain the schema of every event payload it emits from `Part 9` by pin.

### 12.10 Boundary with Part 10, reference and master data management

**Delegated.** Every code system, value set, master record and party identity this component references, including the identities of submitters, custodians, referrers and location classes.

**Must not absorb.** Reference content, and the interpretation of a release artifact's contents.

**Naive conflation.** The store holds the release artifacts of the reference data component and becomes a second source for reference content, so a consumer reads a code list out of the store without its version, its registration status or its withheld count.

**Reciprocal, and its discharge.** `Part 10` section 12.11 requires this part to declare that it owns artifact content, addressing and retrieval, that a content address is immutable, and that it reports an unresolvable address rather than an absent one. Clauses P11-1.1 to P11-1.3 declare the ownership, clauses P11-4.8, P11-4.27 and P11-8.46 declare the immutability, and clauses P11-3.59, P11-7.4 and P11-7.7 declare the reporting of unresolvable rather than absent. `Part 10` clause P10-12.35 further requires it to report an unresolvable release artifact, which section 7.2 supplies at the grain of the specific cause.

**P11-12.29 (MUST NOT) No reference content interpreted.** An implementation must not interpret, expand or serve as reference content the artifacts it holds on behalf of `Part 10`.

**P11-12.30 (MUST) Address immutability declared.** An implementation must declare that the octets retrievable under an address never change, and must fail rather than return different octets.

**P11-12.31 (MUST) Party identities obtained.** An implementation must obtain the identity of every submitter, custodian and referrer party from `Part 10` and must pin the snapshot used.

**P11-12.32 (MUST) Unresolvable cause supplied.** An implementation must supply the specific cause by which an address no longer resolves, so that `Part 10` can record a release as unresolvable rather than deleted.

### 12.12 Boundary with Part 12, conformance and assurance harness

**Delegated.** The verification of this component's claims about itself, and in particular of its fixity and durability claims.

**Must not absorb.** Self assessment presented as assurance. This component's central claims are precisely the ones it is least able to verify about itself: that its content is intact, that its replicas are independent and that its retrievals were verified.

**Naive conflation.** The store's own fixity programme is the assurance, so the component that would detect a systematic verification failure is the component performing the verification.

**Reciprocal.** `Part 12` must declare that it verifies the claims this component makes, that it may perform an independent verification by retrieving content and recomputing its address without relying on this component's verification, that it may plant known content to test the outcome taxonomy, and that it treats a durability or independence claim as a claim requiring evidence rather than as a fact.

**P11-12.33 (MUST) State exposed for verification.** An implementation must expose the state required to verify every externally observable clause of this part.

**P11-12.34 (MUST NOT) No self assurance.** An implementation must not report its own conformance to this part as assurance.

**P11-12.35 (MUST) Independent verification supported.** An implementation must support the retrieval of content and the independent recomputation of its address by `Part 12` without relying on this component's own verification result.

**P11-12.36 (MUST) Outcome taxonomy testable.** An implementation must permit `Part 12` to elicit each outcome of section 7.2 under controlled conditions, since an outcome that cannot be elicited cannot be shown to be implemented.

### 12.13 Boundary with Part 13, model invocation and agent execution

**Delegated.** The invocation record, its cost, its non determinism, and the meaning of any artifact a model produced or consumed.

**Must not absorb.** Any distinction between produced and checked content. To this component a model output is octets.

**Naive conflation.** The store distinguishes model generated content from other content, or holds an invocation record as an artifact attribute, so a provenance claim lives in a component that cannot substantiate it.

**Reciprocal.** `Part 13` must declare that it owns the invocation record, that it references every prompt, artifact and output by address here rather than holding them, that it does not rely on the store to distinguish produced content from checked content, and that a produced value's address establishes what the octets are and nothing about whether they are correct.

**P11-12.37 (MUST NOT) No provenance attribute held.** An implementation must not hold, as an attribute of an artifact, the claim that a model produced it.

**P11-12.38 (MUST) Address supplied for invocation material.** An implementation must accept prompts, artifacts and outputs as artifacts with addresses and must supply them by address.

**P11-12.39 (MUST NOT) No correctness inferred from addressability.** An implementation must not represent the fact that content is addressed and verified as evidence that the content is correct.

### 12.14 Boundary with Part 0, system composition

**Delegated.** What happens when the components run at once: authority over facts more than one component touches, the seams at which values cross boundaries, the propagation of non results, and the pinning of versions across a unit of work spanning several components.

**Must not absorb.** Composition. This part states what it holds and what it refuses to decide, and does not state what the estate does when a citation resolves to a tombstone.

**Reciprocal.** `Part 0` must declare that this component holds authority over addresses, address profiles, algorithm registrations, artifact custody, assembly, ingest, retrieval, verification, placement, referrer registrations, tombstones and aliases, and over nothing else. It must state, for every seam, what must hold and how a violation appears here. It must in particular resolve the eight questions section 13.9 hands it.

**P11-12.40 (MUST) Authority declared, not assumed.** An implementation must not accept an assertion about an address, an artifact's custody, a verification outcome or a placement from another component, and must require every such fact to be established by its own operations.

**P11-12.41 (MUST) Non results returned unmodified.** An implementation must return every outcome of section 7 unmodified regardless of whether the caller can represent it, and must not degrade one to a success or an absence to fit a caller's model.

**P11-12.42 (MUST) Custody gap exposed to composition.** An implementation must make the unregistered citation population, the never verified population and the unrecoverable loss population available as signals, since none can be remedied within this component.

## 13. What could not be established

### 13.1 Sources not obtained in full text

**The multiformats content identifier specification.** Obtained in relevant part. The version 1 structure, the multihash prefixing of hash function code and digest length, the decoder requirement to reject a truncated digest or trailing bytes, the version 0 form as a bare secure hash multihash with an implicit content type, and the community's publication of profiles as standard combinations of chunking, layout and codec settings were all read in the specification's or the project documentation's own words. The multicodec, multibase and multihash registries themselves were not obtained.

**RFC 9162.** Not obtained in this session. The domain separation practice cited at clause P11-3.31 rests on the author's knowledge of the specification and was not verified against its text. A reviewer should verify the tag values and the tree construction before approval. No clause of this part depends on the specific octet values, only on the requirement that leaf and interior inputs be distinguishably prefixed.

**RFC 6920, naming things with hashes.** Not consulted. It specifies a named information URI scheme for content addressed names and is directly adjacent to section 3.4; its absence is the most significant gap in this part's source base for the addressing model, because it is the one IETF standard on the subject and this part did not read it.

**The secure hash standards and the transition guidance.** Not obtained. The digest algorithms are cited generically and the retirement of the first generation algorithm rests on general knowledge of the 2017 collision demonstration and of subsequent national guidance setting a withdrawal date. No clause depends on a date.

**The deduplication side channel literature.** Obtained at second hand. The three attacks, the hash as possession attack, the observation in the wild against a file synchronisation service and the proofs of ownership remedy were read in abstracts and in citing literature, not in the papers themselves. The bibliographic details in section 10.5 were verified. A reviewer relying on clauses P11-3.81 to P11-3.86 should read the 2010 paper directly.

**The preservation standards.** Not obtained. The reference model for an open archival information system and the preservation metadata dictionary are cited for the treatment of fixity as recorded information, on general knowledge. Clause P11-3.72 rests on that treatment and a reviewer should verify it.

**Object storage and container distribution specifications.** Not consulted. The practice this part departs from in section 10.7, being the algorithm prefixed hexadecimal digest as an address and the lifecycle rule that expires content, is described from general knowledge of those specifications and no clause cites them.

**Prior parts of this standard.** `Part 7`, `Part 8`, `Part 9` and `Part 10` were available and their reciprocals concerning this component are discharged at sections 12.7, 12.8, 12.9 and 12.10 with the discharging clauses named. `Part 1` through `Part 6` were not available. Sections 12.1 through 12.6 are written from this part's own analysis of each boundary and not from those parts' text.

**P11-13.1 (MUST) Unverified reciprocals declared.** An implementation must not represent sections 12.1 through 12.6 as discharging a reciprocal statement of `Part 1` through `Part 6`, since the text of those parts was not read.

### 13.2 Whether the profile can be carried in the address in practice

Clauses P11-3.4 and P11-3.6 require the address profile to be recoverable from the address. The content identifier structure carries a content type code and a hash function code, which is not the same thing: it does not carry the chunker, the assembly structure or the domain separation scheme. This part therefore requires something no consulted format supplies, and it does not specify how.

Three constructions are available and none is adopted. A profile registry identifier encoded as an additional field, which requires a format extension and makes the address resolvable only against a registry, defeating self description. A content type code allocated per profile, which works within the existing structure and exhausts the code space quickly. Or a convention in which each profile is a distinct content type, which is closest to what the existing ecosystem does in practice by treating raw leaves and wrapped leaves as different codecs. A reviewer should expect this to be the clause an implementer most wants relaxed, and the relaxation to be that the profile lives in a record rather than in the address, which clause P11-3.6 forbids precisely because a record can be lost while an address travels.

### 13.3 The cost of the model

One retrieval record per retrieval attempt, with a verification declaration, is the largest volume commitment in this part and it is uncosted. A store serving high volumes of small artifacts will find the record larger than the content.

One verification record per artifact per replica per cadence interval is the second. For a store holding a hundred million artifacts in three replicas with a quarterly cadence, that is 1.2 billion records a year, all of which record a pass. Clause P11-3.73 requires the passes to be recorded because the interval since the last successful verification is the figure that matters, and that requirement is what makes the volume unavoidable. Aggregation by verification sweep rather than by artifact would reduce it by orders of magnitude and would lose the per artifact interval, and this part does not specify the aggregation or permit it.

### 13.4 Whether the store can ever know its referrers

This is the largest gap in the part and it is the third appearance of the same structure in three consecutive parts.

The store cannot enumerate the components and records that hold its addresses. Section 3.11 makes the honest position, which is that referrers declare themselves, the undeclared population is countable, and deletion is refused into the gap. None of that causes a single component to register.

Three constructions were considered and none pursued. Mandatory registration at first retrieval, which catches only referrers that retrieve and misses every one that holds an address without ever reading it, which is the majority. Scanning other components' records for address shaped strings, which requires this component to read other components' data and is refused for that reason. And requiring `Part 0` to make referrer registration a composition level obligation of every component that pins an address, which is the only construction that works and is not this component's to impose. Section 13.9 hands it forward.

The same conclusion has now been reached three times. `Part 7` cannot compel an enforcement report, `Part 10` cannot compel a consumption report, and this component cannot compel a referrer registration. All three concluded that the remedy is not available within the component and all three named `Part 12` or `Part 0` as the place it must live.

### 13.5 Whether redaction is coherent

Section 3.12 distinguishes deletion, redaction and erasure and asserts that this component can perform the first two and not the third. The distinction is necessary and it may not be sufficient.

A redaction retains the address, the digest and the length. The digest of the removed content is retained deliberately, so that a later presentation of the content can be tested against the record. That retained digest is also, for content with low entropy, a means of confirming the content: a party holding a candidate can test it against the digest. For a document this is no exposure; for a short structured value it is a complete one. This part does not resolve it, and clause P11-3.61 requires only that the scope of the redaction be recorded. A reviewer should consider whether a redaction should be permitted to remove the digest as well, and if so what a citation to the address then resolves to.

### 13.6 Whether a store can be told it lost something

Clause P11-7.22 requires an unrecoverable loss to be recorded with its own tombstone reason. The store can detect a loss it observes, being a failed verification with no good replica. It cannot detect a loss it never looked for, and the interval within which such a loss goes unrecorded is the fixity cadence.

So the loss figure this part requires is a figure of detected losses, and its relationship to actual losses is a function of the cadence. This part requires the cadence to be declared and the never verified population to be exposed, which makes the relationship computable in principle, and it does not require the computation or state how to perform it. A store with a five year cadence and an honest loss figure of zero has said very little.

### 13.7 Repeated structure across the standard, now eleven parts

`Part 4` recorded three repeated structures, `Part 5` five, `Part 6` six, `Part 7` eight with one divergence, `Part 10` eleven with two. This part carries the register forward and adds one.

**The authority that can prove what it did and not what happened.** Now three components with one structure. `Part 7` cannot see enforcement, `Part 10` cannot see consumption, this component cannot see citation. All three keep two records and never merge them, all three treat the absence of the second as ordinary, all three count the unknown population as the honest measure, all three expose it as a signal they cannot remedy, and all three conclude that the remedy lies outside the component. Three independent arrivals at one structure and one undesigned remedy. This is now the clearest candidate in the register for being specified once, and the third consecutive part to say so.

**The retention obligation a component cannot discover.** Second appearance, as `Part 10` section 13.7 predicted. `Part 7` imposed it on `Part 10`, and `Part 3`, `Part 7`, `Part 8`, `Part 9` and `Part 10` all impose it here. `Part 10` recorded it as a composition device rather than a component requirement, and this part's section 3.11 is the second implementation of it with the second vocabulary. Two parts, two vocabularies, one device.

**The refusal to return absence for a non result.** This part's contribution to the pattern is the third instance of the specific form. `Part 7` refuses to return not applicable as deny, `Part 10` refuses to return an unknown code as non membership, and this part refuses to return an integrity failure as absence. Three parts, three subjects, one principle, and each with a different reason for the same conclusion: that a negative reported in place of a non result is a condition that can never be found.

**The declared completeness of a set.** Now nine parts. This part contributes the verification declaration, the verified extent and the sampled verification declaration, which are the same structure as `Part 9`'s evaluated extent: a result whose extent is not declared cannot be relied upon.

**The honest undeclared or unreported value.** Now eleven parts. This part contributes `never_held`, `unavailable_transient`, `unverifiable_opaque`, `never_verified` and `unregistered citation`.

**The immutable record with stateful assertions about it.** Now eleven parts. This part's instance is the immutable address binding carrying an artifact whose custody state changes.

**The refusal of order dependent resolution.** Unchanged at seven parts. This part has no ordering question and does not add to it.

**The refusal to arbitrate.** Now six. This part returns the set of candidate addresses rather than choosing among them, per clause P11-12.13.

**The residue model.** Still two, `Part 6` and `Part 7`.

**The extended third value.** Still an inconsistency between `Part 5` and `Part 7`, still unresolved, and this part does not adopt an extended form.

**The asymmetric bridge that disproves and cannot prove.** Two parts have one; four record that they should and do not. This part makes five without one, and its candidate is the strongest of the five because it is cheap: a set of artifacts of known content planted at ingest and retrieved on a schedule, which would catch a store whose verification is not performing the comparison it reports. Clause P11-12.36 requires the outcome taxonomy to be elicitable by `Part 12`, which is the interface such a bridge would use, and this part stops short of requiring the bridge itself.

**The marking vocabulary for restricted content.** Now six parts. This part's tombstone and redaction records are the same distinction again, in a sixth vocabulary.

**The divergence in clause convention.** `Part 8` and `Part 9` remain outside the convention the other nine parts share, and neither exposes a section 12.11, so this part derived both boundaries from their content as `Part 10` did before it. This is the second part to be affected and the cost is now recurrent rather than incidental.

**Open.** All of it. This is the sixth consecutive part to record the register and the fifth to recommend acting before the next part. Twelve items across eleven parts, two of them inconsistencies, and the first item has now been independently arrived at three times.

**P11-13.2 (SHOULD) Register maintained.** An author of a subsequent part should carry this register forward, add to it, and state whether each entry is a repetition or an inconsistency.

### 13.8 What this part deliberately did not attempt

No conformance assessment of any system was performed or anticipated, per clause P11-1.26.

No storage technology, medium, tiering model, erasure coding scheme or replication protocol is specified. Placement is a declaration with a replica count and an independence basis, and nothing beyond.

No chunking algorithm is specified. Content defined chunkers are admitted as registered kinds with declared bounds and their construction is not specified.

No wire protocol, transfer encoding, resumable upload mechanism or range request syntax is specified.

No encryption scheme or key management is specified. Section 3.16 requires the disposition to be recorded and the custody to be separated and specifies neither.

No proof of retrievability or proof of storage protocol is specified, though the literature cited in section 10.5 supplies candidates. Clause P11-3.81 requires a challenge that cannot be answered from the address and does not say how to construct one.

No treatment is given of a store distributed across parties who do not trust each other, where no single party can verify the whole and the placement independence cannot be asserted by anyone.

No performance or scale requirement is stated, and section 13.3 records the volume concern without a threshold.

**P11-13.3 (MUST) Gaps declared, not filled.** An implementation must not represent a matter listed in section 13.8 as specified by this part.

**P11-13.4 (SHOULD) Open questions carried forward.** A reviewer of this part should record a position on each open question in section 13, and where a position is adopted it should be recorded in the review outcome rather than by silent amendment of the clause it affects.

### 13.9 Questions handed to Part 0 rather than answered here

Whether referrer registration should be a composition level obligation of every component that pins an address. Section 13.4 concludes that it is the only construction that works and that this component cannot impose it. Three components now have the same unanswerable question about a population they cannot enumerate.

Whether the retention floor should be a composition level device, as `Part 10` section 13.9 also asks. Two parts now implement it with two vocabularies and six parts impose obligations of the kind on this one.

How the address profile is to be carried in an address, per section 13.2, given that no consulted format supplies a field for it and that this part forbids carrying it in a record alone.

What a citing component should do when its citation resolves to a tombstone. This component supplies the outcome and refuses to decide the consequence; `Part 8` and `Part 10` both record the reference as unresolvable and neither states what follows.

Whether a redaction may remove the digest, per section 13.5, given that a retained digest of low entropy content is a means of confirming that content.

Whether the estate has one deduplication boundary or many. A boundary broader than a tenant is economical and observable, and section 3.15 requires controls rather than prohibition. Whether the estate accepts the residual exposure is not this component's decision.

Whether an address is a system wide identity for content or this component's identity for it, given that `Part 1`, `Part 3`, `Part 4`, `Part 8`, `Part 9`, `Part 10` and `Part 13` all hold addresses and that a second store would mint different addresses for the same content under a different profile.

Whether the twelve repeated structures now identified should each be specified once, per section 13.7, and in particular whether the first of them, which three components have now independently arrived at, should be specified as a single composition level construct before `Part 12` is authored.
