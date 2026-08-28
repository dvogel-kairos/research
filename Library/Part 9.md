# KAIROS STD 003 Part 9, schema and contract registry

**Status:** version 1, Proposed.
**Part:** `KAIROS STD 003 Part 9`. Cite as `KAIROS STD 003 Part 9 §n` for a section and `KAIROS STD 003 Part 9 P9-n-nn` for a clause.
**Component:** the schema and contract registry component of an enterprise application that executes governed work.

## Reading this part

**Normative language.** The key words MUST, MUST NOT, SHOULD, SHOULD NOT and MAY in this part are to be interpreted as described in RFC 2119 (Bradner, IETF RFC 2119, March 1997). Every requirement of this part is a numbered clause. Every clause carries exactly one modality and states one testable proposition. Prose that carries no clause identifier is explanatory and imposes no requirement.

**Clause identifiers.** Clauses are identified `P9-<section>-<ordinal>`. Identifiers are permanent and are never reused or renumbered. A clause withdrawn in a later version retains its identifier and is marked withdrawn.

**Basis markers.** Every clause carries a basis marker recording what the clause rests on. This is not a modality and does not weaken the requirement; a clause marked D binds exactly as hard as one marked S. The marker exists so that a reader can tell the difference between a requirement this part inherits and a requirement this part invents.

| Marker | Meaning |
|---|---|
| S | The clause's subject is treated in the text of a named specification, cited at the clause under **Source.** The clause may adopt that treatment or depart from it; where it departs it says so, and the conflict is recorded in §10.4. The marker records that a reader can go to a source, not that this part agrees with what is there. |
| P | Rests on published literature, on vendor specification of a widely deployed implementation, or on observed practice rather than on standards text, cited at the clause under **Source.** |
| D | Decided by this part. No consulted specification treats the subject. Every D clause on a subject where a reader might expect specification support is listed in §13.2. |

**Two drafting conventions.** Both are stated because both bear on whether a clause is a single testable statement, which is the property the clause form exists to guarantee.

*Paired prohibitions.* A clause may state a requirement together with the direct negation of that same requirement, where one test decides both, as in a clause that requires two conditions to be distinguished and prohibits their representation as one value. A clause MUST NOT join two requirements that need two tests. The number of clauses carrying a paired prohibition is derived and reported in the clause index summary, so that a reader can audit the convention rather than take it on trust.

*Ordinals are not everywhere ascending.* Clause ordinals are permanent from first issue. Where drafting split a clause that carried more than one requirement, the split off requirements took the next free ordinals in their section and were placed beside the clause they came from. Ordinals within a section are therefore dense and complete, but not everywhere in ascending reading order.

**Conformance target.** The conformance target of this part is a *registry*: any implementation that registers schemas and contracts, determines compatibility between their versions, and validates instances against them. Where a clause constrains something other than the registry, the clause names its subject.

**Schema language neutrality.** This part specifies the registry, not a schema language. No clause requires any particular schema language, and every clause that names a language names it as an example or as a source. A registry conforming to this part must be able to hold schemas expressed in more than one language, because §6.2 requires the language and its dialect to be recorded as data rather than assumed.

**Out of scope by construction.** This part does not assess any implementation. It does not describe any system. It is written as a measuring stick.

---

## Clause index

This index is derived from the body of this part by extracting every line matching the clause form `**P9-<section>-<ordinal>** (<modality>) [<basis>]`. Every count below is therefore derivable from the body and is not asserted. The grain of every count is one clause, being one line of clause form. Section 13 carries no clauses by construction, since it reports rather than requires.

### Summary by section

| § | Section | Clauses | MUST | MUST NOT | SHOULD | SHOULD NOT | MAY | S | P | D | Paired |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Scope and responsibilities | 28 | 12 | 14 | — | — | 2 | — | — | 28 | 12 |
| 2 | Terminology | 7 | 1 | 6 | — | — | — | — | — | 7 | 1 |
| 3 | Data model | 68 | 52 | 16 | — | — | — | 6 | 4 | 58 | 27 |
| 4 | Interfaces | 48 | 34 | 13 | 1 | — | — | — | — | 48 | 15 |
| 5 | State model | 28 | 20 | 8 | — | — | — | 3 | — | 25 | 7 |
| 6 | Execution semantics | 96 | 81 | 15 | — | — | — | 10 | 5 | 81 | 37 |
| 7 | Outcome and failure taxonomy | 40 | 28 | 12 | — | — | — | 1 | — | 39 | 11 |
| 8 | Observability and the audit record | 37 | 31 | 5 | 1 | — | — | — | — | 37 | 1 |
| 9 | Extension model | 21 | 17 | 4 | — | — | — | 2 | — | 19 | 9 |
| 10 | Standards and specifications | 7 | 5 | — | 2 | — | — | — | 2 | 5 | 1 |
| 11 | Anti patterns | 14 | 12 | 2 | — | — | — | — | — | 14 | 1 |
| 12 | Boundaries with other parts | 52 | 37 | 14 | — | — | 1 | — | — | 52 | 15 |
| 13 | What could not be established | 0 | — | — | — | — | — | — | — | — | — |
| **Total** | | **446** | **330** | **109** | **4** | **0** | **3** | **22** | **11** | **413** | **137** |

**Derived counts, at the grain of one clause.** This part carries 446 clauses across 12 clause bearing sections. Of these, 330 are MUST, 109 are MUST NOT, 4 are SHOULD, 0 are SHOULD NOT and 3 are MAY. By basis, 22 rest on cited standards or project specification text, 11 on cited literature or on the vendor specification of a widely deployed implementation, and 413 are decided by this part with no consulted specification treating the subject. 137 clauses carry a paired prohibition under the convention stated above, and no clause carries more than one requirement needing more than one test. The proportion marked D is highest in §7 and §3, which is where this part departs furthest from its sources: the consulted specifications define validity and say nothing about the complement of validity, and they define identity for one purpose without versioning the rules that produce it. §10.5 states the set of subjects no consulted specification supplies and §13.2 itemises them.

### Clauses

Subject labels below are machine extracted from the opening of each clause and are an index aid, not normative text. The clause itself governs.

**§1. Scope and responsibilities**

| Clause | Modality | Basis | Subject |
|---|---|---|---|
| P9-1-01 | MUST | D | The component MUST own the identity of every schema and every schema version… |
| P9-1-02 | MUST | D | The component MUST own the registration record of every schema version, being… |
| P9-1-03 | MUST | D | The component MUST own the declared language and dialect of every registered… |
| P9-1-04 | MUST | D | The component MUST own the canonical form used to derive each intrinsic… |
| P9-1-05 | MUST | D | The component MUST own the compatibility assertion, being a recorded… |
| P9-1-06 | MUST | D | The component MUST own the contract, being a named agreement that binds… |
| P9-1-07 | MUST | D | The component MUST own the participant register, being the record of which… |
| P9-1-08 | MUST | D | The component MUST own validation, being the determination of whether an… |
| P9-1-09 | MUST | D | The component MUST own the validation record, being the durable evidence of a… |
| P9-1-10 | MUST | D | The component MUST own the reference closure of every schema version, being… |
| P9-1-11 | MUST | D | The component MUST own the semantic change declaration attached to each… |
| P9-1-12 | MUST | D | The component MUST own the waiver, being the record of an authorised decision… |
| P9-1-13 | MUST NOT | D | The component MUST NOT define the meaning of any term a schema carries, and… |
| P9-1-14 | MUST NOT | D | The component MUST NOT evaluate any constraint whose truth depends on a fact… |
| P9-1-15 | MUST NOT | D | The component MUST NOT hold the membership of any code system or value set,… |
| P9-1-16 | MUST NOT | D | The component MUST NOT store the bytes of any registered artifact, and MUST… |
| P9-1-17 | MUST NOT | D | The component MUST NOT govern the approval, effective date, supersession or… |
| P9-1-18 | MUST NOT | D | The component MUST NOT render an authorisation decision on whether a party… |
| P9-1-19 | MUST NOT | D | The component MUST NOT be the audit ledger, and MUST emit its events to the… |
| P9-1-20 | MUST NOT | D | The component MUST NOT decide what a system does in consequence of a… |
| P9-1-21 | MUST NOT | D | The component MUST NOT select among candidate schema versions by governed… |
| P9-1-22 | MUST NOT | D | The component MUST NOT sequence the deployment of participants, and MUST… |
| P9-1-23 | MUST NOT | D | The component MUST NOT verify its own conformance claims, and MUST expose the… |
| P9-1-24 | MUST NOT | D | The component MUST NOT treat a schema as a description of an internal… |
| P9-1-25 | MAY | D | An implementation MAY support any number of schema languages, and this part… |
| P9-1-26 | MAY | D | An implementation MAY validate instances synchronously in the path of an… |
| P9-1-27 | MUST NOT | D | This part MUST NOT be read as requiring that every instance crossing a… |
| P9-1-28 | MUST NOT | D | This part MUST NOT be read as requiring a central registry deployment, and no… |

**§2. Terminology**

| Clause | Modality | Basis | Subject |
|---|---|---|---|
| P9-2-01 | MUST NOT | D | This part MUST NOT define rule, constraint evaluation, verdict or rule… |
| P9-2-02 | MUST NOT | D | This part MUST NOT define data element, conceptual domain, lineage or impact… |
| P9-2-03 | MUST NOT | D | This part MUST NOT define code system, value set membership or terminology,… |
| P9-2-04 | MUST NOT | D | This part MUST NOT define document, controlled copy, effective date or… |
| P9-2-05 | MUST NOT | D | This part MUST NOT define content address, deduplication or artifact… |
| P9-2-06 | MUST NOT | D | This part MUST NOT define work item, case, process instance or policy, which… |
| P9-2-07 | MUST | D | Where this part uses a term owned by another part, it MUST use that term with… |

**§3. Data model**

| Clause | Modality | Basis | Subject |
|---|---|---|---|
| P9-3-01 | MUST | D | Every schema version, contract version, compatibility assertion, validation… |
| P9-3-02 | MUST NOT | D | An identifier MUST NOT be reused after the record it identifies is… |
| P9-3-03 | MUST | D | A schema version MUST be addressable by its assigned identity and MUST be… |
| P9-3-04 | MUST | D | A position within a schema version MUST be addressable by a path expression… |
| P9-3-05 | MUST | S | A location within an instance MUST be addressable by a path expression drawn… |
| P9-3-06 | MUST NOT | D | An identifier of a schema version MUST NOT encode any mutable property of… |
| P9-3-07 | MUST | D | Where a schema version is expressed in a language whose own identity… |
| P9-3-08 | MUST NOT | D | The registry MUST NOT treat a version designation as ordering evidence, and… |
| P9-3-09 | MUST | D | The schema version record MUST contain every field marked required in the… |
| P9-3-10 | MUST NOT | D | A schema version record MUST NOT be modified after registration, and a change… |
| P9-3-11 | MUST | D | open_content_positions MUST be derived by the registry from the schema and… |
| P9-3-12 | MUST | D | annotation_only_constructs MUST be derived by the registry from the pinned… |
| P9-3-13 | MUST | D | The registry MUST hold, for every schema version, a literal digest over the… |
| P9-3-14 | MUST | S | Each of the three digests MUST record the canonicaliser identity and version… |
| P9-3-15 | MUST NOT | D | The registry MUST NOT compare digests computed under different canonicaliser… |
| P9-3-16 | MUST | D | Where a submission's assigned identity matches an existing schema version and… |
| P9-3-17 | MUST | D | Where a submission's canonical digest matches an existing schema version and… |
| P9-3-18 | MUST NOT | D | The registry MUST NOT merge two schema versions that share a canonical… |
| P9-3-19 | MUST | D | Where two schema versions share a canonical digest and differ in literal… |
| P9-3-20 | MUST NOT | D | The registry MUST NOT present a canonical digest as evidence that two… |
| P9-3-21 | MUST | S | Every registration record MUST carry the registration authority under whose… |
| P9-3-22 | MUST | D | Every entry in status_history MUST carry the authorisation decision reference… |
| P9-3-23 | MUST | D | The registry MUST record whether harmonisation was performed and MUST NOT… |
| P9-3-24 | MUST | D | Every member of a reference closure MUST be recorded with the intrinsic… |
| P9-3-25 | MUST | S | Where a schema language admits references whose target is determined during… |
| P9-3-26 | MUST | D | The registry MUST record whether a closure is cyclic, because a cyclic… |
| P9-3-27 | MUST | D | A compatibility assertion MUST name a reader version and a writer version as… |
| P9-3-28 | MUST | P | A compatibility assertion MUST record the rule set, the dialect and the… |
| P9-3-29 | MUST | P | A compatibility assertion MUST record its scope as adjacent, transitive or a… |
| P9-3-30 | MUST | D | basis MUST record whether the verdict rests on mechanical determination… |
| P9-3-31 | MUST | P | A compatibility assertion MUST record the implied deployment order that its… |
| P9-3-32 | MUST NOT | D | A compatibility assertion MUST NOT be modified after it is written, and a… |
| P9-3-33 | MUST | D | Every version transition within a subject MUST carry exactly one semantic… |
| P9-3-34 | MUST NOT | D | The registry MUST NOT derive a semantic change declaration mechanically, and… |
| P9-3-35 | MUST | D | Where overall_class is other than none, the declaration MUST itemise at least… |
| P9-3-36 | MUST | D | Where a change class is optionality_reinterpreted or… |
| P9-3-37 | MUST | D | Where a change is enumeration_member_repurposed, the declaration MUST name… |
| P9-3-38 | MUST | D | A binding MUST reference a schema version by intrinsic identity and MUST NOT… |
| P9-3-39 | MUST | D | Every interaction MUST declare its ordering, delivery, idempotence and replay… |
| P9-3-40 | MUST | D | Every contract version MUST name at least one participant, and the registry… |
| P9-3-41 | MUST | D | Where a contract version declares an unbounded replay expectation, the… |
| P9-3-42 | MUST | S | Every position whose permitted values are drawn from a governed value set… |
| P9-3-43 | MUST NOT | D | A schema version MUST NOT restate the members of a governed value set inline… |
| P9-3-67 | MUST | D | Where a schema language forces the members of a governed value set to be… |
| P9-3-68 | MUST | D | Where the members of a governed value set are stated inline, the registry… |
| P9-3-44 | MUST | D | Where inlined members are recorded, the registry MUST detect and report… |
| P9-3-45 | MUST NOT | D | The registry MUST NOT treat the addition of a member to a bound value set as… |
| P9-3-46 | MUST | D | The registry MUST maintain a participant registration for every declared… |
| P9-3-47 | MUST | D | Every participant registration MUST record whether the version held is self… |
| P9-3-48 | MUST | D | The registry MUST record the instant of last confirmation of every… |
| P9-3-49 | MUST NOT | D | The registry MUST NOT delete a withdrawn participant registration, because a… |
| P9-3-50 | MUST | D | Every validation MUST produce a validation record, including a validation… |
| P9-3-51 | MUST | D | Every validation record MUST carry the complete reproducibility set, being… |
| P9-3-52 | MUST | S | The validation record MUST identify the validating implementation and its… |
| P9-3-53 | MUST | D | Every finding MUST record whether the construct that produced it is an… |
| P9-3-54 | MUST NOT | D | A validation record MUST NOT be modified after it is written, and a… |
| P9-3-55 | MUST | D | Where the instance is not retained, the validation record MUST retain the… |
| P9-3-56 | MUST | D | A schema version that failed a compatibility determination MUST NOT be… |
| P9-3-57 | MUST | D | Every waiver MUST carry an expiry instant, and the registry MUST NOT accept a… |
| P9-3-58 | MUST | D | Every waiver MUST enumerate the participant registrations it affects, so that… |
| P9-3-59 | MUST | D | Every waiver MUST reference a remediation, and the registry MUST refuse a… |
| P9-3-60 | MUST NOT | P | The registry MUST NOT permit a compatibility determination to be disabled as… |
| P9-3-61 | MUST NOT | D | Schema version records, registration records, reference closures,… |
| P9-3-62 | MUST | D | Where the current value of a mutable field of a subject, contract or… |
| P9-3-63 | MUST | D | The registry MUST be implementable over a store in which no written record is… |
| P9-3-64 | MUST | D | Registration status and version state MUST be held as recorded transitions… |
| P9-3-65 | MUST | D | The registry MUST version its own record schemas and MUST record, for every… |
| P9-3-66 | MUST NOT | D | The registry MUST NOT reinterpret a record written under an earlier record… |

**§4. Interfaces**

| Clause | Modality | Basis | Subject |
|---|---|---|---|
| P9-4-01 | MUST | D | Every operation the registry accepts MUST be defined in terms of the records… |
| P9-4-02 | MUST | D | Every operation that changes state MUST accept an idempotency key supplied by… |
| P9-4-03 | MUST | D | Every operation invoked with a previously seen idempotency key and different… |
| P9-4-04 | MUST | D | Every operation that registers, progresses, publishes, deprecates, retires or… |
| P9-4-05 | MUST | D | Every operation MUST return exactly one outcome value from the taxonomy in §7. |
| P9-4-06 | MUST | D | Every rejected operation MUST be recorded with the requesting party, the… |
| P9-4-07 | MUST NOT | D | The registry MUST NOT expose any operation that mutates registered content. |
| P9-4-08 | MUST | D | submit_schema MUST compute all three digests, derive the open content… |
| P9-4-09 | MUST | D | submit_schema MUST refuse a submission whose declared dialect is absent, and… |
| P9-4-10 | MUST | D | submit_schema MUST refuse a submission containing a construct the pinned… |
| P9-4-11 | MUST | D | publish_version MUST refuse where no semantic change declaration exists for… |
| P9-4-12 | MUST | D | publish_version MUST refuse where a compatibility determination required by… |
| P9-4-13 | MUST | D | publish_version MUST refuse where a required determination returned a verdict… |
| P9-4-14 | MUST NOT | D | deprecate_version MUST NOT change the ability of a reader to resolve or… |
| P9-4-15 | MUST | D | sunset_version MUST require the registry to record which participant… |
| P9-4-16 | MUST | D | retire_version MUST refuse where any published contract version binds the… |
| P9-4-17 | MUST | D | revoke_waiver MUST record the revoking party and reason, and MUST NOT delete… |
| P9-4-18 | MUST | D | determine_compatibility MUST require the caller to name the reader version… |
| P9-4-19 | MUST | D | determine_compatibility MUST require the caller to name the rule set, or MUST… |
| P9-4-20 | MUST NOT | D | determine_compatibility MUST NOT return a verdict of compatible over a… |
| P9-4-21 | MUST | D | validate_instance MUST return the evaluated extent with every outcome,… |
| P9-4-22 | MUST | D | validate_instance MUST accept a caller declaration of whether the instance… |
| P9-4-23 | MUST NOT | D | validate_instance MUST NOT return a boolean as its complete result, and MUST… |
| P9-4-24 | MUST | D | analyse_impact MUST report the participants it could not establish separately… |
| P9-4-25 | MUST | D | explain_finding MUST identify the dialect and vocabulary under which the… |
| P9-4-26 | MUST | D | The registry MUST expose retrieval of a schema version by assigned identity… |
| P9-4-27 | MUST | D | The registry MUST expose a point in time query returning the registration… |
| P9-4-28 | MUST | D | The registry MUST expose the set of compatibility assertions concerning a… |
| P9-4-29 | MUST | D | Every query result concerning compatibility MUST carry the scope, basis and… |
| P9-4-30 | MUST NOT | D | A query MUST NOT change any state other than a read record. |
| P9-4-31 | MUST NOT | D | The registry MUST NOT expose a query that returns a compatibility verdict… |
| P9-4-32 | MUST | D | The registry MUST emit an event for every registration, status transition,… |
| P9-4-33 | MUST | D | Every emitted event MUST carry the identifier of the record it concerns, the… |
| P9-4-34 | MUST | D | Every emitted event MUST be delivered to Part 3 at least once, and the… |
| P9-4-35 | MUST | D | The registry MUST emit a distinct event class for a validation whose… |
| P9-4-36 | MUST | D | The registry MUST emit a distinct event class for a waiver approaching… |
| P9-4-37 | MUST | D | The registry MUST emit an event when a bound value set version is superseded,… |
| P9-4-38 | MUST NOT | D | The registry MUST NOT emit an event describing a state change that was not… |
| P9-4-39 | SHOULD | D | The registry SHOULD emit an event when a participant registration passes its… |
| P9-4-40 | MUST | D | The registry MUST treat every read in the table in §4.6 as fallible and MUST… |
| P9-4-41 | MUST NOT | D | The registry MUST NOT permit an operation to proceed on the failure of an… |
| P9-4-42 | MUST NOT | D | The registry MUST NOT cache a read from another component beyond the pinning… |
| P9-4-43 | MUST | D | A caller MAY assume that a schema version, once registered, will never change… |
| P9-4-44 | MUST NOT | D | A caller MUST NOT assume that an outcome of conformance means the whole… |
| P9-4-45 | MUST NOT | D | A caller MUST NOT assume that a compatibility verdict computed for one pair… |
| P9-4-46 | MUST NOT | D | A caller MUST NOT assume that a schema version in deprecated cannot be… |
| P9-4-47 | MUST NOT | D | A caller MUST NOT assume that the absence of a finding at a location means… |
| P9-4-48 | MUST | D | A caller MAY assume that a validation record, once returned, is immutable and… |

**§5. State model**

| Clause | Modality | Basis | Subject |
|---|---|---|---|
| P9-5-01 | MUST | D | Every schema version and every contract version MUST carry a registration… |
| P9-5-02 | MUST NOT | D | The registry MUST NOT derive one axis from the other, and MUST NOT expose one… |
| P9-5-03 | MUST | D | Every transition on either axis MUST be recorded with its trigger, the… |
| P9-5-04 | MUST NOT | D | The registry MUST NOT admit a transition not listed in this section. |
| P9-5-05 | MUST | D | Where a transition is refused because it is illegal, the refusal MUST be… |
| P9-5-06 | MUST | S | Progression to recorded MUST require that all mandatory metadata attributes… |
| P9-5-07 | MUST | S | Progression to qualified or above MUST require the sponsorship of a steward… |
| P9-5-08 | MUST NOT | S | The registry MUST NOT treat recorded as a statement that the metadata meets… |
| P9-5-09 | MUST | D | The registry MUST expose mandatory_metadata_complete independently of… |
| P9-5-10 | MUST | D | retired and rejected MUST be terminal on the registration axis, and the… |
| P9-5-11 | MUST NOT | D | The registry MUST NOT progress an item above recorded where no steward is… |
| P9-5-12 | MUST | D | The registry MUST retain and resolve a retired schema version, because… |
| P9-5-13 | MUST | D | Every transition to superseded MUST name the successor version. |
| P9-5-14 | MUST | D | withdrawn MUST be terminal on the version state axis. |
| P9-5-15 | MUST | D | The registry MUST resolve and validate against a version in deprecated,… |
| P9-5-16 | MUST | D | The registry MUST refuse to transition a version to sunset while any… |
| P9-5-17 | MUST NOT | D | The registry MUST NOT transition a version to withdrawn where any published… |
| P9-5-18 | MUST | D | Every transition to withdrawn from published MUST record a reason from an… |
| P9-5-19 | MUST | D | A contract version MUST use the version state axis in §5.3 with the same… |
| P9-5-20 | MUST NOT | D | A contract version MUST NOT be published while any schema version it binds is… |
| P9-5-21 | MUST | D | Where a schema version bound by a published contract version is deprecated,… |
| P9-5-22 | MUST | D | The registry MUST expose the set of published contract versions carrying at… |
| P9-5-23 | MUST | D | A waiver MUST transition to expired at its expiry instant without any act. |
| P9-5-24 | MUST | D | The registry MUST record the version state of every schema version whose… |
| P9-5-25 | MUST NOT | D | The registry MUST NOT extend a waiver, and an extension MUST be expressed as… |
| P9-5-26 | MUST | D | The registry MUST declare a confirmation interval and MUST transition a… |
| P9-5-27 | MUST | D | A compatibility determination whose population includes a stale or declared… |
| P9-5-28 | MUST NOT | D | The registry MUST NOT treat a withdrawn participant registration as absent… |

**§6. Execution semantics**

| Clause | Modality | Basis | Subject |
|---|---|---|---|
| P9-6-01 | MUST | D | Given the same instance, the same pinned schema version, the same dialect,… |
| P9-6-02 | MUST | D | Given the same ordered pair of schema versions, the same rule set, the same… |
| P9-6-03 | MUST NOT | D | The registry MUST NOT allow the order in which findings are produced to… |
| P9-6-04 | MUST | D | The registry MUST be able to re-perform any recorded validation from its… |
| P9-6-05 | MUST NOT | D | Validation MUST NOT consult the current wall clock, the current state of any… |
| P9-6-06 | MUST | D | Where a schema construct would require a value outside the instance, the… |
| P9-6-07 | MUST | D | The registry MUST hold the schema language and the dialect as registered… |
| P9-6-08 | MUST | D | Every dialect the registry admits MUST be registered with the set of… |
| P9-6-09 | MUST | D | The registry MUST refuse a schema version whose dialect is not registered,… |
| P9-6-10 | MUST NOT | D | The registry MUST NOT interpret a schema version under any dialect other than… |
| P9-6-11 | MUST | S | The registry MUST record which vocabularies of a dialect it supports as… |
| P9-6-12 | MUST | D | Where the registry does not support a vocabulary a schema version declares as… |
| P9-6-13 | MUST NOT | D | The registry MUST NOT permit a schema version to be validated by a validator… |
| P9-6-14 | MUST | D | The registry MUST compute the literal digest over the exact bytes submitted,… |
| P9-6-15 | MUST | D | The registry MUST refuse a submission whose reference closure contains an… |
| P9-6-16 | MUST NOT | D | The registry MUST NOT resolve any reference by retrieval from a network… |
| P9-6-17 | MUST | D | Where a submitted schema names an external locator, the registry MUST record… |
| P9-6-90 | MUST | D | Where a submitted schema names an external locator, the registry MUST require… |
| P9-6-91 | MUST | D | Where an external locator's target is registered, the registry MUST rewrite… |
| P9-6-18 | MUST | D | The registry MUST record the canonicaliser version with every digest it… |
| P9-6-19 | MUST | D | Where a canonicaliser is upgraded, the registry MUST recompute the affected… |
| P9-6-92 | MUST | D | Where digests are recomputed under a new canonicaliser version, the registry… |
| P9-6-20 | MUST | D | The registry MUST declare, for each canonicaliser it registers, which… |
| P9-6-21 | MUST | S | The compatibility digest's canonical form MUST retain every attribute the… |
| P9-6-22 | MUST | S | The registry MUST NOT treat two schema versions sharing a canonical digest as… |
| P9-6-23 | MUST | P | The registry MUST record whether a submission was normalised before its… |
| P9-6-24 | MUST | D | The registry MUST refuse a schema version containing a construct the pinned… |
| P9-6-25 | MUST NOT | S | The registry MUST NOT admit a schema version on the basis that an… |
| P9-6-26 | MUST | D | The registry MUST derive and record every position at which the schema… |
| P9-6-27 | MUST | D | The registry MUST derive and record every construct in the schema version… |
| P9-6-28 | MUST | S | Where a construct in a schema version annotates rather than asserts under the… |
| P9-6-29 | MUST | S | The registry MUST refuse a schema version that relies on a custom construct… |
| P9-6-30 | MUST | D | The registry MUST refuse a schema version whose declared dialect requires a… |
| P9-6-31 | MUST | D | The registry MUST refuse a schema version containing a construct whose… |
| P9-6-32 | MUST | D | The registry MUST refuse a schema version that inlines the members of a… |
| P9-6-33 | MUST | D | Validation MUST evaluate every assertion of the pinned schema version that… |
| P9-6-34 | MUST | D | Validation MUST record every location of the instance that no assertion… |
| P9-6-35 | MUST NOT | D | Validation MUST NOT report an outcome of conformance where the evaluated… |
| P9-6-36 | MUST | D | Validation MUST classify every finding by severity and MUST report… |
| P9-6-37 | MUST | S | Validation MUST distinguish a finding that fires because a condition failed… |
| P9-6-38 | MUST | D | Validation MUST NOT treat a finding of severity warning or information as… |
| P9-6-39 | MUST | D | Validation MUST collect annotations where the caller requests them, and MUST… |
| P9-6-40 | MUST NOT | D | Validation MUST NOT report an annotation as a finding, and MUST NOT report a… |
| P9-6-41 | MUST | D | Where a validation cannot complete, the registry MUST report a non result… |
| P9-6-42 | MUST | D | Where the reference closure of the pinned schema version cannot be resolved… |
| P9-6-43 | MUST | D | Where a dynamic reference resolves differently for different instances, the… |
| P9-6-44 | MUST | D | Where a value set binding of strength required applies to a position, the… |
| P9-6-45 | MUST NOT | D | The registry MUST NOT report a value set membership failure as a schema… |
| P9-6-46 | MUST | D | Where the membership determination from Part 10 is unavailable, the registry… |
| P9-6-47 | MUST | D | Validation MUST bound its own execution. |
| P9-6-93 | MUST | D | The registry MUST declare its validation execution bound. |
| P9-6-94 | MUST | D | The declared validation execution bound MUST be finite. |
| P9-6-95 | MUST | D | Validation MUST report validation_bounded where the declared execution bound… |
| P9-6-96 | MUST | D | The registry MUST record the declared execution bound in every validation… |
| P9-6-48 | MUST | D | Where a reference closure is cyclic, the registry MUST bound recursion depth… |
| P9-6-49 | MUST | D | A compatibility determination MUST be made over an ordered pair of schema… |
| P9-6-50 | MUST NOT | D | The registry MUST NOT express a compatibility determination in the terms… |
| P9-6-51 | MUST | P | The registry MUST record the implied deployment order of every compatibility… |
| P9-6-52 | MUST | P | The registry MUST determine compatibility under the rule set applicable to… |
| P9-6-53 | MUST | P | The registry MUST NOT assert that a change is fully compatible in a schema… |
| P9-6-54 | MUST | S | Where a rule set determines compatibility by resolving a reader schema… |
| P9-6-55 | MUST | S | Where a rule set resolves a union or choice by selecting the first matching… |
| P9-6-56 | MUST NOT | P | The registry MUST NOT infer a transitive compatibility verdict from a chain… |
| P9-6-57 | MUST | D | Where a transitive verdict is required, the registry MUST determine… |
| P9-6-58 | MUST | D | The registry MUST record, for every subject, whether its declared… |
| P9-6-59 | MUST | D | Where a contract version declares an unbounded replay expectation and the… |
| P9-6-60 | MUST | D | The registry MUST expose, for any stated pair of versions in a subject,… |
| P9-6-61 | MUST | D | Every compatibility determination MUST record the population of participants… |
| P9-6-62 | MUST | D | Where the participant register contains no confirmed registration for a… |
| P9-6-63 | MUST NOT | D | The registry MUST NOT report a change as safe for a population it cannot… |
| P9-6-64 | MUST | D | The registry MUST compute, for a proposed version, the set of participant… |
| P9-6-65 | MUST | D | The registry MUST report the set in P9-6-64 as the uncovered population of… |
| P9-6-66 | MUST | D | The registry MUST determine mechanical compatibility from the rule set alone. |
| P9-6-67 | MUST NOT | D | The registry MUST NOT report a mechanically compatible pair as substitutable. |
| P9-6-68 | MUST | D | The registry MUST refuse to publish a version whose semantic change… |
| P9-6-69 | MUST | D | The registry MUST treat a change of semantic class unit_or_scale_changed,… |
| P9-6-70 | MUST | D | Where a semantic change is declared at a position, the registry MUST record… |
| P9-6-71 | MUST | D | Where a schema version in the reference closure of a published version is… |
| P9-6-72 | MUST | D | Where a schema version in the closure of a published version is superseded,… |
| P9-6-73 | MUST | D | Where a bound value set version is superseded, the registry MUST record every… |
| P9-6-74 | MUST | D | The registry MUST treat the addition of a member to a value set bound at… |
| P9-6-75 | MUST | D | The registry MUST expose the closure change history of every published… |
| P9-6-76 | MUST | D | Concurrent submissions of the same content under the same assigned identity… |
| P9-6-77 | MUST | D | Concurrent submissions of different content under the same assigned identity… |
| P9-6-78 | MUST | D | validate_instance MUST be idempotent in effect on registry state other than… |
| P9-6-79 | MUST | D | A repeated validation under the same idempotency key MUST return the original… |
| P9-6-80 | MUST | D | Concurrent status progressions of one item MUST be serialised, and the losing… |
| P9-6-81 | MUST | D | The registry MUST record the instant of every registration, determination,… |
| P9-6-82 | MUST NOT | D | The registry MUST NOT use the current instant in the evaluation of any… |
| P9-6-83 | MUST | D | Where a schema construct expresses a temporal constraint relative to the… |
| P9-6-84 | MUST | D | The registry MUST resolve a point in time query against recorded transitions… |
| P9-6-85 | MUST | D | The registry MUST record, for every position in a registered schema version… |
| P9-6-86 | MUST | D | Where a schema language expresses absence and null through the same… |
| P9-6-87 | MUST NOT | D | The registry MUST NOT supply a default value during validation, and MUST NOT… |
| P9-6-88 | MUST | S | Where a rule set consults a declared default in determining compatibility,… |
| P9-6-89 | MUST | D | The registry MUST record a change to a declared default as a semantic change… |

**§7. Outcome and failure taxonomy**

| Clause | Modality | Basis | Subject |
|---|---|---|---|
| P9-7-01 | MUST | D | Every value the registry can produce MUST belong to exactly one of the… |
| P9-7-02 | MUST NOT | D | The registry MUST NOT return a value outside these enumerations, and MUST NOT… |
| P9-7-03 | MUST | D | The registry MUST expose, for every outcome it returns, the three properties… |
| P9-7-04 | MUST | D | The registry MUST return conformant only where the evaluated extent is… |
| P9-7-05 | MUST NOT | D | The registry MUST NOT return conformant or conformant_with_findings where any… |
| P9-7-06 | MUST NOT | D | The registry MUST NOT map undecidable, not_applicable, not_evaluated,… |
| P9-7-07 | MUST NOT | D | The registry MUST NOT map any of the seven values named in P9-7-06 to a… |
| P9-7-08 | MUST | D | instance_unreadable MUST be distinguished from non_conformant, because an… |
| P9-7-09 | MUST | D | not_applicable MUST be returned where the schema version pinned does not… |
| P9-7-10 | MUST | D | validation_bounded MUST record which assertions were not evaluated, and MUST… |
| P9-7-11 | MUST | D | Every unexamined location MUST carry exactly one cause from the enumeration… |
| P9-7-12 | MUST | S | The registry MUST report wildcard_lax_or_skip where a position is admitted by… |
| P9-7-13 | MUST | D | The registry MUST report annotation_only_construct where the construct… |
| P9-7-14 | MUST | D | The registry MUST report conditional_branch_not_taken separately from… |
| P9-7-15 | MUST | D | The registry MUST report the count of unexamined locations with the grain at… |
| P9-7-16 | MUST NOT | D | The registry MUST NOT report coverage as a proportion without the grain and… |
| P9-7-17 | MUST | D | Where an instance format admits content the pinned schema language cannot… |
| P9-7-18 | MUST | D | The registry MUST represent all ten values and MUST record the specific value… |
| P9-7-19 | MUST NOT | D | The registry MUST NOT treat any non verdict as compatible. |
| P9-7-20 | MUST NOT | D | The registry MUST NOT treat any non verdict as incompatible, because refusing… |
| P9-7-21 | MUST | D | not_determined MUST be returned for a pair for which no determination exists,… |
| P9-7-22 | MUST | D | Where a rule set returns a value this enumeration does not contain, the… |
| P9-7-23 | MUST | D | The registry MUST treat a value its enumeration does not contain as a non… |
| P9-7-24 | MUST | D | The registry MUST raise an unrepresentable verdict event on receipt of a… |
| P9-7-25 | MUST | D | not_authorised and authorisation_unavailable MUST be distinct outcomes. |
| P9-7-26 | MUST | D | registered_equivalent MUST be distinct from registered, so that a duplicate… |
| P9-7-27 | MUST NOT | D | The registry MUST NOT return registered where any part of the registration… |
| P9-7-28 | MUST | D | Where Part 2 returns a non verdict for a delegated constraint, the registry… |
| P9-7-29 | MUST NOT | D | The registry MUST NOT treat a non verdict from Part 2 as a violation or as… |
| P9-7-30 | MUST | D | Where Part 10 cannot determine value set membership, the registry MUST report… |
| P9-7-31 | MUST | D | Where Part 11 cannot resolve a registered artifact's content, the registry… |
| P9-7-32 | MUST | D | Where Part 4 cannot resolve a cited definition, the registry MUST refuse… |
| P9-7-33 | MUST NOT | D | A system fault outcome MUST NOT be recorded as a validation outcome or a… |
| P9-7-34 | MUST | D | Where internal_invariant_violated is detected, the registry MUST stop… |
| P9-7-35 | MUST | D | The registry MUST expose, for every validation outcome, the three properties… |
| P9-7-36 | MUST | D | Where the registry reports an outcome to another component, it MUST report… |
| P9-7-37 | MUST NOT | D | The registry MUST NOT aggregate validation outcomes into a summary that loses… |
| P9-7-38 | MUST | D | Every count or rate the registry publishes over validation outcomes MUST… |
| P9-7-39 | MUST NOT | D | The registry MUST NOT publish a conformance rate that treats… |
| P9-7-40 | MUST | D | Where a non result is produced and no consumer subscribes to it, the registry… |

**§8. Observability and the audit record**

| Clause | Modality | Basis | Subject |
|---|---|---|---|
| P9-8-01 | MUST | D | The registry MUST record every submission, at the grain of one record per… |
| P9-8-02 | MUST | D | The registry MUST record every registration status transition and every… |
| P9-8-03 | MUST | D | The registry MUST record every compatibility determination, at the grain of… |
| P9-8-04 | MUST | D | The registry MUST record every validation, at the grain of one record per… |
| P9-8-05 | MUST | D | The registry MUST record every finding, at the grain of one record per… |
| P9-8-06 | MUST | D | The registry MUST record the evaluated extent of every validation, at the… |
| P9-8-07 | MUST | D | The registry MUST record every waiver grant, revocation, expiry and… |
| P9-8-08 | MUST | D | The registry MUST record every participant registration, confirmation,… |
| P9-8-09 | MUST | D | The registry MUST record every canonicaliser registration and upgrade, and… |
| P9-8-10 | MUST | D | The registry MUST record every dialect registration and every change to the… |
| P9-8-11 | MUST | D | The registry MUST record every read of a schema version by another component,… |
| P9-8-12 | MUST | D | A reader MUST be able to reconstruct which exact bytes were registered under… |
| P9-8-13 | MUST | D | A reader MUST be able to reconstruct the dialect, vocabulary set and… |
| P9-8-14 | MUST | D | A reader MUST be able to reconstruct which locations of a validated instance… |
| P9-8-15 | MUST | D | A reader MUST be able to reconstruct, for any compatibility assertion, the… |
| P9-8-16 | MUST | D | A reader MUST be able to reconstruct which participants held which versions… |
| P9-8-17 | MUST | D | A reader MUST be able to reconstruct every waiver in force at any past… |
| P9-8-18 | MUST | D | A reader MUST be able to reconstruct the semantic change declaration attached… |
| P9-8-19 | MUST | D | A reader MUST be able to reconstruct the reference closure applied to any… |
| P9-8-20 | MUST NOT | D | Reconstruction MUST NOT depend on the registry's runtime being available, and… |
| P9-8-21 | MUST | D | Every count the registry reports MUST state its grain and the instant as at… |
| P9-8-22 | MUST NOT | D | The registry MUST NOT report a count of schemas without stating whether… |
| P9-8-23 | MUST | D | Every derived metric the registry exposes MUST be accompanied by its… |
| P9-8-24 | MUST NOT | D | The registry MUST NOT report a compatibility statistic without stating the… |
| P9-8-25 | MUST | D | Every record the registry writes MUST be integrity protected such that… |
| P9-8-26 | MUST NOT | D | The registry MUST NOT permit deletion of a schema version record,… |
| P9-8-27 | MUST | D | Where a record is disposed of under a retention schedule, the registry MUST… |
| P9-8-28 | MUST NOT | D | The registry MUST NOT dispose of a schema version cited by a retained… |
| P9-8-29 | MUST | D | The registry MUST retain the intrinsic digests of a disposed schema version,… |
| P9-8-30 | MUST | D | The registry MUST expose the count of validations whose outcome was… |
| P9-8-31 | MUST | D | The registry MUST expose the distribution of unexamined location causes,… |
| P9-8-32 | MUST | D | The registry MUST expose the set of published schema versions carrying at… |
| P9-8-33 | MUST | D | The registry MUST expose the set of published schema versions carrying at… |
| P9-8-34 | MUST | D | The registry MUST expose the uncovered population of every published version,… |
| P9-8-35 | MUST | D | The registry MUST expose every active waiver with its expiry and its affected… |
| P9-8-36 | MUST | D | The registry MUST expose the count of participant registrations in stale,… |
| P9-8-37 | SHOULD | D | The registry SHOULD expose the rate at which submissions are refused by… |

**§9. Extension model**

| Clause | Modality | Basis | Subject |
|---|---|---|---|
| P9-9-01 | MUST | D | The following sets MUST be closed and MUST NOT be extended by an… |
| P9-9-02 | MUST | D | The following sets MAY be extended under the governance in §9.4: schema… |
| P9-9-03 | MUST | D | Business enumerations within a registered schema are open by construction,… |
| P9-9-04 | MUST | D | A schema language MUST be registered before any schema expressed in it is… |
| P9-9-05 | MUST | D | A registered schema language MUST declare at least one dialect, and every… |
| P9-9-06 | MUST | D | A registered dialect MUST classify every construct it defines as assertion,… |
| P9-9-07 | MUST | D | A registered schema language MUST declare a canonicaliser for reader… |
| P9-9-08 | MUST | D | A registered schema language MUST declare a location notation for addressing… |
| P9-9-09 | MUST | D | A registered schema language MUST declare either a rule set for compatibility… |
| P9-9-21 | MUST | D | Where a registered schema language declares that no compatibility rule set… |
| P9-9-10 | MUST NOT | D | The registry MUST NOT admit a schema language whose conformance determination… |
| P9-9-11 | MUST | D | A schema version composed by reference from other schema versions MUST carry… |
| P9-9-12 | MUST | S | Where a schema language provides a mechanism for redefining or overriding a… |
| P9-9-13 | MUST NOT | D | The registry MUST NOT treat a composed schema version's compatibility as… |
| P9-9-14 | MUST | S | Where a schema language provides bundling of several schemas into one… |
| P9-9-15 | MUST | D | A contract version MUST be treated as a composition over schema versions and… |
| P9-9-16 | MUST | D | Every extension an implementation makes MUST be declared in a machine… |
| P9-9-17 | MUST | D | The registry MUST record, on every record affected by an extension, the… |
| P9-9-18 | MUST NOT | D | An extension MUST NOT change the meaning of an existing member of any set. |
| P9-9-19 | MUST NOT | D | An extension MUST NOT be required for interoperation, and a consumer that… |
| P9-9-20 | MUST | D | Where a new dialect of an already registered language is admitted, the… |

**§10. Standards and specifications**

| Clause | Modality | Basis | Subject |
|---|---|---|---|
| P9-10-01 | MUST | D | Where this part and a consulted specification address the same subject and do… |
| P9-10-02 | MUST | D | Where this part and a consulted specification conflict, an implementation… |
| P9-10-03 | MUST | D | An implementation that also claims conformance to a consulted schema language… |
| P9-10-04 | MUST | D | An implementation MUST NOT claim that conformance to this part implies… |
| P9-10-05 | SHOULD | P | A reader consulting JSON Schema 2020-12 on the format keyword SHOULD note… |
| P9-10-06 | SHOULD | P | A reader consulting the Avro specification on canonical form SHOULD note that… |
| P9-10-07 | MUST | D | An implementation MUST treat the following as requirements of this part… |

**§11. Anti patterns**

| Clause | Modality | Basis | Subject |
|---|---|---|---|
| P9-11-01 | MUST | D | The registry MUST report the evaluated extent with every validation outcome. |
| P9-11-02 | MUST | D | The registry MUST refuse a schema version containing a construct the pinned… |
| P9-11-03 | MUST | D | The registry MUST refuse a submission whose assigned identity exists with… |
| P9-11-04 | MUST NOT | D | The registry MUST NOT resolve any reference by network retrieval at… |
| P9-11-05 | MUST | D | The registry MUST express every bypass of a determination as a waiver… |
| P9-11-06 | MUST | D | The registry MUST record every compatibility verdict against an ordered… |
| P9-11-07 | MUST NOT | D | The registry MUST NOT derive any compatibility conclusion from a version… |
| P9-11-08 | MUST | D | The registry MUST record the addition of a member to an enumeration or to a… |
| P9-11-09 | MUST | D | The registry MUST record separately whether a position may be absent and… |
| P9-11-10 | MUST | D | The registry MUST report an ambiguity finding where more than one alternative… |
| P9-11-11 | MUST | D | The registry MUST maintain a participant register for every published… |
| P9-11-12 | MUST | D | The registry MUST retain the findings, the evaluated extent and the… |
| P9-11-13 | MUST | D | The registry MUST require every position carrying a governed term to cite its… |
| P9-11-14 | MUST | D | The registry MUST treat every published schema version as a contract term and… |

**§12. Boundaries with other parts**

| Clause | Modality | Basis | Subject |
|---|---|---|---|
| P9-12-01 | MUST NOT | D | The registry MUST NOT define the meaning of any term. |
| P9-12-02 | MUST | D | Every position in a registered schema version that carries a governed term… |
| P9-12-03 | MUST | D | The registry MUST refuse registration of a position carrying a governed term… |
| P9-12-04 | MUST | D | The registry MUST report a semantic change declared at a position whose cited… |
| P9-12-05 | MUST | D | The registry MUST expose, for every Part 4 definition, the set of schema… |
| P9-12-06 | MUST NOT | D | The registry MUST NOT evaluate a constraint requiring a fact outside the… |
| P9-12-07 | MUST | D | The registry MUST refuse at registration a schema construct requiring a fact… |
| P9-12-08 | MUST | D | The registry MUST accept the full verdict vocabulary of Part 2 including… |
| P9-12-09 | MUST NOT | D | The registry MUST NOT report a delegated constraint's non verdict as a schema… |
| P9-12-10 | MUST NOT | D | The registry MUST NOT hold the membership of any value set. |
| P9-12-11 | MUST | D | The registry MUST hold a pinned value set version and a declared strength for… |
| P9-12-12 | MUST | D | The registry MUST report divergence between inlined members and the pinned… |
| P9-12-13 | MUST | D | The registry MUST obtain every membership determination from Part 10 at… |
| P9-12-14 | MUST NOT | D | The registry MUST NOT govern the approval or effective date of a schema… |
| P9-12-15 | MUST | D | Every published schema version and contract version MUST carry a Part 1… |
| P9-12-16 | MUST | D | The registry MUST treat every validation record, compatibility assertion and… |
| P9-12-17 | MUST | D | The registry MUST resolve a citation to a schema version to the version in… |
| P9-12-18 | MUST NOT | D | The registry MUST NOT store artifact bytes. |
| P9-12-19 | MUST | D | The registry MUST hold the content address of every registered artifact. |
| P9-12-20 | MUST | D | Where a content address ceases to resolve, the registry MUST report every… |
| P9-12-21 | MUST | D | The registry MUST emit every event in §8.1 to Part 3. |
| P9-12-22 | MUST NOT | D | The registry MUST NOT represent its own records as the audit record of a… |
| P9-12-23 | MUST | D | The registry MUST own the validation record as the authoritative statement of… |
| P9-12-24 | MUST NOT | D | The registry MUST NOT reject, route, retry or quarantine an instance. |
| P9-12-25 | MUST | D | The registry MUST return the outcome, findings and evaluated extent to the… |
| P9-12-26 | MUST | D | The registry MUST supply the pinned schema version and dialect that Part 8… |
| P9-12-27 | MUST | D | Every interaction of a published contract version that can fail MUST declare… |
| P9-12-28 | MUST NOT | D | The registry MUST NOT render an authorisation decision. |
| P9-12-29 | MUST | D | The registry MUST obtain an authorisation decision at the instant of every… |
| P9-12-30 | MUST | D | The registry MUST supply the registration status, version state and… |
| P9-12-31 | MUST NOT | D | The registry MUST NOT resolve a reference that names a subject without a… |
| P9-12-32 | MUST | D | Where a caller requires a version to be selected from several, the registry… |
| P9-12-33 | MAY | D | The registry MAY return the set of candidate versions with their states,… |
| P9-12-34 | MUST | D | The registry MUST expose the state required to verify every clause of this… |
| P9-12-35 | MUST NOT | D | The registry MUST NOT report its own conformance to this part as assurance. |
| P9-12-36 | MUST | D | The registry MUST expose its evaluated extent computation in a form Part 12… |
| P9-12-37 | MUST | D | The registry MUST record on every validation record whether the instance was… |
| P9-12-38 | MUST NOT | D | The registry MUST NOT report a validation of an instance produced under… |
| P9-12-39 | MUST NOT | D | The registry MUST NOT represent conformance as correctness in any interface… |
| P9-12-40 | MUST | D | Where an instance produced by a model is validated, the registry MUST record… |
| P9-12-41 | MUST | D | The registry MUST treat the authority assignments of Part 0 as governing, and… |
| P9-12-42 | MUST | D | The registry MUST declare, for every fact it owns, that it is the sole… |
| P9-12-43 | MUST NOT | D | The registry MUST NOT claim authority over: the meaning of a term; value set… |
| P9-12-44 | MUST | D | At every instant, every schema version MUST carry exactly one registration… |
| P9-12-45 | MUST | D | At every instant, every schema version MUST carry exactly three digests, each… |
| P9-12-46 | MUST | D | At every instant, no two schema versions MUST share an assigned identity with… |
| P9-12-47 | MUST | D | At every instant, every published schema version MUST have exactly one… |
| P9-12-48 | MUST | D | At every instant, every published schema version that failed a required… |
| P9-12-49 | MUST | D | At every instant, every validation record MUST carry a complete… |
| P9-12-50 | MUST | D | At every instant, every reference in the closure of a published schema… |
| P9-12-51 | MUST | D | At every instant, every binding of a published contract version MUST name a… |
| P9-12-52 | MUST | D | At every instant, every published contract version MUST name at least one… |

---

## 1. Scope and responsibilities

### 1.1 What the component is accountable for

The registry is accountable for three things that look like one thing and are not: what a schema *is*, whether two versions of it can be used together, and whether a given instance conforms to it. Each has a different failure mode, and the characteristic defect of registries is that they answer the third question with a boolean and let it stand for the other two.

**P9-1-01** (MUST) [D] The component MUST own the identity of every schema and every schema version it holds, comprising both the assigned identity and the identity intrinsic to the registered content.

**P9-1-02** (MUST) [D] The component MUST own the registration record of every schema version, being the record of who submitted it, when, under what authority and in what state.

**P9-1-03** (MUST) [D] The component MUST own the declared language and dialect of every registered schema version.

**P9-1-04** (MUST) [D] The component MUST own the canonical form used to derive each intrinsic identity, and the identity of the canonicalisation rules themselves.

**P9-1-05** (MUST) [D] The component MUST own the compatibility assertion, being a recorded determination about an ordered pair of schema versions under a named direction and a named rule set.

**P9-1-06** (MUST) [D] The component MUST own the contract, being a named agreement that binds schema versions to the interactions between named participants.

**P9-1-07** (MUST) [D] The component MUST own the participant register, being the record of which parties read and which parties write which versions of which schemas.

**P9-1-08** (MUST) [D] The component MUST own validation, being the determination of whether an instance conforms to a pinned schema version under a pinned dialect.

**P9-1-09** (MUST) [D] The component MUST own the validation record, being the durable evidence of a validation performed, including its findings and the extent of the instance the validation examined.

**P9-1-10** (MUST) [D] The component MUST own the reference closure of every schema version, being the set of other schema versions it depends on, resolved to intrinsic identities.

**P9-1-11** (MUST) [D] The component MUST own the semantic change declaration attached to each version transition, being the declaration of what changed in meaning as distinct from what changed in structure.

**P9-1-12** (MUST) [D] The component MUST own the waiver, being the record of an authorised decision to publish a version that failed a compatibility determination.

### 1.2 What the component is explicitly not accountable for

**P9-1-13** (MUST NOT) [D] The component MUST NOT define the meaning of any term a schema carries, and MUST cite the governed definition held by the metadata and model repository component (`Part 4`).

**P9-1-14** (MUST NOT) [D] The component MUST NOT evaluate any constraint whose truth depends on a fact not present in the instance under validation, and MUST delegate such constraints to the business rules engine component (`Part 2`).

**P9-1-15** (MUST NOT) [D] The component MUST NOT hold the membership of any code system or value set, and MUST hold only the binding to a value set version held by the reference and master data component (`Part 10`).

**P9-1-16** (MUST NOT) [D] The component MUST NOT store the bytes of any registered artifact, and MUST hold the content address of the artifact as held by the content addressed artifact store component (`Part 11`).

**P9-1-17** (MUST NOT) [D] The component MUST NOT govern the approval, effective date, supersession or retention of a schema version as a document, and MUST delegate those to the controlled documents component (`Part 1`).

**P9-1-18** (MUST NOT) [D] The component MUST NOT render an authorisation decision on whether a party may register, publish, deprecate or waive, and MUST obtain that decision from the policy decision point component (`Part 7`).

**P9-1-19** (MUST NOT) [D] The component MUST NOT be the audit ledger, and MUST emit its events to the provenance and audit ledger component (`Part 3`).

**P9-1-20** (MUST NOT) [D] The component MUST NOT decide what a system does in consequence of a validation finding, and MUST NOT reject, route, retry or quarantine an instance on its own authority.

**P9-1-21** (MUST NOT) [D] The component MUST NOT select among candidate schema versions by governed algorithm, and MUST obtain such a selection from the decision engine component (`Part 5`).

**P9-1-22** (MUST NOT) [D] The component MUST NOT sequence the deployment of participants, and MUST confine itself to recording the deployment order that a compatibility direction implies.

**P9-1-23** (MUST NOT) [D] The component MUST NOT verify its own conformance claims, and MUST expose the state required for the conformance and assurance harness component (`Part 12`) to do so.

**P9-1-24** (MUST NOT) [D] The component MUST NOT treat a schema as a description of an internal representation, and MUST treat every published schema as a contract term binding on its participants.

### 1.3 The three failures this part exists to prevent

*The silent positive.* An instance is reported valid over content the validator never examined. Four mechanisms produce this, each documented in specification text: a construct that annotates rather than asserts, so a stated constraint constrains nothing; an unrecognised keyword that is ignored rather than refused, so a typographical error or a dialect mismatch silently removes a constraint; open content, so any member not named by the schema passes unexamined; and a dialect difference, so the same document imposes different constraints depending on which version of the schema language interpreted it. §6.5, §7.2 and §7.3 exist to prevent this, and the requirement that a validation report its evaluated extent (§7.3) is the central requirement of this part.

*Compatibility asserted without its parameters.* A registry records that a subject is backward compatible. It does not record between which two versions, under which dialect, under which rule set, in which direction relative to which party, over which population of participants, or whether the determination was mechanical only. The assertion then travels as though it were a fact about the schema, and is relied on by parties it was never computed for. §3.6, §6.6 and §6.8 exist to prevent this.

*Identity that does not identify.* A version is registered, and later the bytes behind that identity differ, or the same content is registered twice under two identities, or a canonical form is used for identity that discards precisely the attributes that determine compatibility. §3.3, §6.3 and §6.4 exist to prevent this.

### 1.4 What this part does not require

**P9-1-25** (MAY) [D] An implementation MAY support any number of schema languages, and this part does not require support for more than one.

**P9-1-26** (MAY) [D] An implementation MAY validate instances synchronously in the path of an interaction or asynchronously against stored instances, and this part does not require either.

**P9-1-27** (MUST NOT) [D] This part MUST NOT be read as requiring that every instance crossing a boundary be validated, which is a policy question for the boundary's owner.

**P9-1-28** (MUST NOT) [D] This part MUST NOT be read as requiring a central registry deployment, and no clause depends on the registry being a single process or a single store.

---

## 2. Terminology

Terms are owned here and are not redefined in another part. Where a term is taken from a specification, the specification is named and the difference from its usage there is stated.

### 2.1 Schema terms

**Schema.** A declarative artifact that states the structure and permitted content of a class of instances, such that conformance of an instance can be determined from the instance and the schema alone. This part uses *schema* only for artifacts meeting that decidability condition; an artifact requiring external facts is a rule set and belongs to `Part 2` (§12.2).

**Schema version.** One immutable registered state of a schema, having its own assigned identity, its own intrinsic identity and its own registration record. Every operation of this part is on a schema version rather than on a schema, except where a clause names the schema.

**Schema language.** The formal system in which a schema is expressed, such as the JSON Schema family, W3C XML Schema, RELAX NG, Avro schema declaration, or a protocol buffer definition.

**Dialect.** The identified version of a schema language together with the set of vocabularies in force, which together determine how a schema document is interpreted. JSON Schema 2020-12 makes the concept explicit through the `$schema` and `$vocabulary` keywords; this part requires the dialect to be recorded for every schema language, including those whose specifications leave it implicit.

**Vocabulary.** A named set of constructs within a dialect, each construct classified as assertion, annotation or reserved. Taken from JSON Schema 2020-12, which defines `$vocabulary` and distinguishes vocabularies that an implementation is required to support from those it is not.

**Assertion.** A construct whose evaluation contributes to whether an instance conforms.

**Annotation.** A construct whose evaluation produces information about an instance and does not contribute to whether it conforms. The distinction is normative in JSON Schema 2020-12, which splits the `format` keyword into a Format-Annotation vocabulary and a Format-Assertion vocabulary.

**Unrecognised construct.** A construct present in a registered schema that the pinned dialect does not define. This part requires it to be recorded and refused at registration rather than ignored at validation (§6.4).

**Canonical form.** A transformation of a schema to a normalised representation, defined so that two schemas with the same canonical form stand in a stated equivalence relation. Avro defines a Parsing Canonical Form with the stated property that schemas with textually equal canonical forms are the same as far as any reader is concerned.

**Canonicaliser.** The identified, versioned implementation of a canonical form. This part requires the canonicaliser to be identified because a canonical form's rules can change and an identity derived under one set of rules is not comparable with an identity derived under another.

**Fingerprint.** A digest over a canonical form, used as an intrinsic identity. Avro recommends three fingerprint algorithms and frames the choice as a trade off between fingerprint length and collision probability.

**Assigned identity.** The identity a registry gives a schema version: a canonical name or URI together with a version designation. Corresponds to `$id` in JSON Schema, to the target namespace in W3C XML Schema, and to the canonical URL with business version in FHIR.

**Intrinsic identity.** The identity derived from the registered content itself by canonicalisation and fingerprinting. A registry holds both; §3.3 states why neither alone suffices.

**Reference closure.** The transitive set of schema versions a schema version depends on through references, each resolved to an intrinsic identity.

### 2.2 Registry terms

**Registry.** The component specified by this part.

**Registration authority.** The party accountable for admitting items to the registry and for progressing their registration status. Taken from ISO/IEC 11179-6, which places registration and the assignment of identifiers under a registration authority.

**Submitter.** The party that presents an artifact for registration.

**Steward.** The party accountable for the continued fitness of a registered item. ISO/IEC 11179-6:2023 requires the sponsorship of a steward and the approval of the registration authority for progression above a stated registration status.

**Registration status.** The designation of the level of registration or quality of a registered item, on an axis independent of the item's currency. ISO/IEC 11179-6 defines registration status and distinguishes lifecycle status categories, which address development and progression, from documentation status categories, which apply when development has ceased.

**Version state.** The designation of a schema version's currency: whether it may be used for new work, only for reading existing instances, or not at all. This axis is separate from registration status, and §5.1 requires both.

**Subject.** A named series of schema versions between which compatibility is determined. The term is taken from widely deployed registry practice, in which a subject carries the compatibility configuration; this part retains the grouping and moves the compatibility determination off the subject and onto the version pair (§6.6).

**Waiver.** A recorded, authorised, time bounded decision to publish a schema version that failed a compatibility determination.

### 2.3 Contract terms

**Contract.** A named agreement that binds schema versions to the interactions between named participants, together with the guarantees each participant may rely on. A contract is composed of schemas and is not itself a schema.

**Contract version.** One immutable registered state of a contract.

**Participant.** A party to a contract in a declared role.

**Participant role.** The declared relationship of a participant to a schema version within a contract: `producer`, `consumer`, or `both`.

**Participant register.** The record of which participants hold which schema versions in which roles at which times. Without it, a compatibility question about a population has no answer, which §6.8 states as a requirement rather than as an observation.

**Interaction.** A named exchange within a contract, having declared payload schemas, declared error schemas and declared guarantees.

**Binding.** The attachment of a schema version to a position within a contract, such as the request payload of an interaction.

**Value set binding.** The declaration, within a schema, that a field's permitted values are drawn from a named version of a value set held by `Part 10`, together with the strength of that declaration.

### 2.4 Compatibility terms

**Compatibility assertion.** A recorded determination that a stated reader version can consume instances written under a stated writer version, under a stated dialect, a stated rule set and a stated canonical form.

**Direction.** Which of an ordered pair of versions is the reader and which the writer. This part requires the direction to be expressed in reader and writer terms rather than in the terms backward and forward, and §6.6 gives the reason.

**Rule set.** The identified, versioned set of rules by which a compatibility determination is made. Avro specifies schema resolution rules as part of its specification; widely deployed registry practice applies different rules for different schema languages under the same compatibility mode name.

**Adjacent compatibility.** Compatibility determined only against the immediately preceding version.

**Transitive compatibility.** Compatibility determined against every prior version in the subject.

**Mechanical compatibility.** Compatibility as determined by the rule set operating on the two schema versions.

**Substitutability.** The property that a reader can not only parse but correctly interpret instances written under another version. Mechanical compatibility does not establish it, and §6.9 requires the two to be recorded separately.

**Semantic change class.** The declared class of change in meaning between two versions, from the closed enumeration in §3.7.

**Implied deployment order.** The order in which readers and writers must be upgraded, which follows from the direction of a compatibility assertion. Widely deployed registry practice documents the implication; this part requires it to be recorded with the assertion.

### 2.5 Validation terms

**Instance.** The artifact whose conformance is determined.

**Validation.** The determination of whether an instance conforms to a pinned schema version under a pinned dialect, together with the production of a validation record.

**Finding.** One statement produced by a validation about one location in an instance, carrying a severity, a construct reference and a location reference.

**Severity.** The declared weight of a finding. SHACL defines three severities of validation result, being Violation, Warning and Info; Schematron distinguishes an assertion, which fires when its test is false, from a report, which fires when its test is true, and carries a role attribute; FHIR carries validation findings in an OperationOutcome with an issue severity.

**Evaluated extent.** The set of locations within an instance that at least one assertion of the pinned schema examined, and its complement, being the locations no assertion examined. This part introduces the term; §7.3 makes reporting it mandatory and §1.3 gives the reason.

**Coverage.** The evaluated extent expressed as a proportion of the instance at a stated grain, always accompanied by the grain.

**Open content.** A position in a schema at which members not named by the schema are permitted and unexamined.

**Validation record.** The durable evidence of a validation performed.

**Reproducibility set.** The complete set of pinned identities required to re-perform a validation and obtain the same result: instance digest, schema version, dialect, vocabulary set, rule set, canonicaliser, reference closure and validator identity and version.

### 2.6 Terms deliberately not defined here

**P9-2-01** (MUST NOT) [D] This part MUST NOT define rule, constraint evaluation, verdict or rule authoring, which are owned by `Part 2`.

**P9-2-02** (MUST NOT) [D] This part MUST NOT define data element, conceptual domain, lineage or impact analysis, which are owned by `Part 4`.

**P9-2-03** (MUST NOT) [D] This part MUST NOT define code system, value set membership or terminology, which are owned by `Part 10`.

**P9-2-04** (MUST NOT) [D] This part MUST NOT define document, controlled copy, effective date or retention schedule, which are owned by `Part 1`.

**P9-2-05** (MUST NOT) [D] This part MUST NOT define content address, deduplication or artifact retrieval, which are owned by `Part 11`.

**P9-2-06** (MUST NOT) [D] This part MUST NOT define work item, case, process instance or policy, which are owned by `Part 8`, `Part 6` and `Part 7`.

**P9-2-07** (MUST) [D] Where this part uses a term owned by another part, it MUST use that term with the meaning that part gives it and MUST NOT narrow or extend it.

---

## 3. Data model

Every field carries a type, whether it is required, its cardinality, and what its absence means. Types are abstract. `identifier` is an opaque immutable string unique within its declared scope. `instant` is a point in time with an offset from UTC and at least millisecond resolution. `digest` is a cryptographic hash together with the identifier of the algorithm that produced it. `pinned-ref` is a reference that resolves to a stated version of a stated object. `uri` is a URI per RFC 3986. `enum(...)` is a closed set unless the field description says the set is open.

### 3.1 Identity and addressing

**P9-3-01** (MUST) [D] Every schema version, contract version, compatibility assertion, validation record, waiver, participant registration, registration record and semantic change declaration MUST carry an identifier unique within the component for all time.

**P9-3-02** (MUST NOT) [D] An identifier MUST NOT be reused after the record it identifies is superseded, retired or disposed of.

**P9-3-03** (MUST) [D] A schema version MUST be addressable by its assigned identity and MUST be independently addressable by its intrinsic identity.

**P9-3-04** (MUST) [D] A position within a schema version MUST be addressable by a path expression that is stable for the life of that version.

**P9-3-05** (MUST) [S] A location within an instance MUST be addressable by a path expression drawn from a declared, identified location notation, and the notation MUST be recorded with every finding. **Source.** RFC 6901 defines JSON Pointer for locations within a JSON document; W3C XML Schema exposes locations through the post schema validation infoset; SHACL identifies a focus node and a result path. No single notation spans instance formats, which is why this part requires the notation to be named rather than assumed.

**P9-3-06** (MUST NOT) [D] An identifier of a schema version MUST NOT encode any mutable property of that version, including its registration status, its version state or its compatibility to any other version.

**P9-3-07** (MUST) [D] Where a schema version is expressed in a language whose own identity mechanism differs from the registry's assigned identity, the registry MUST record both and MUST record which of the two governs resolution within the registry.

**P9-3-08** (MUST NOT) [D] The registry MUST NOT treat a version designation as ordering evidence, and MUST derive predecessor and successor relations from recorded transitions rather than from parsing a version string.

### 3.2 The schema version record

| Field | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `schema_version_id` | identifier | yes | 1 | Not possible |
| `subject_id` | identifier | yes | 1 | Not possible |
| `assigned_uri` | uri | yes | 1 | Not possible |
| `version_designation` | string | yes | 1 | Not possible; ordering is not inferred from it, see P9-3-08 |
| `language_id` | identifier | yes | 1 | Not possible |
| `dialect_id` | identifier | yes | 1 | Not possible; see P9-6-09 |
| `vocabulary_set` | identifier | yes | 1..n | Not possible; a dialect with a single implicit vocabulary records that vocabulary explicitly |
| `artifact_address` | content address | yes | 1 | Not possible; the bytes are held by `Part 11` |
| `literal_digest` | digest | yes | 1 | Not possible |
| `canonical_digest` | digest | yes | 1 | Not possible |
| `compatibility_digest` | digest | yes | 1 | Not possible; see P9-3-13 |
| `canonicaliser_id` | pinned-ref | yes | 1 | Not possible |
| `registration_status` | enum, §5.2 | yes | 1 | Not possible |
| `version_state` | enum, §5.3 | yes | 1 | Not possible |
| `reference_closure_id` | identifier | no | 0..1 | The version has no references; distinguished from a closure that could not be resolved, which prevents registration under P9-6-15 |
| `predecessor_id` | identifier | no | 0..1 | The version is the first in its subject, not that its predecessor is unknown |
| `definition_refs` | pinned-ref to `Part 4` | no | 0..n | No position in the schema cites a governed definition; §12.1 states when this is a defect |
| `value_set_bindings` | structure, §3.9 | no | 0..n | No position declares a value set binding |
| `unrecognised_constructs` | structure: path, construct name | no | 0..n | Every construct in the schema is defined by the pinned dialect |
| `open_content_positions` | path | no | 0..n | The schema admits no open content at any position; MUST NOT be read as unknown |
| `annotation_only_constructs` | structure: path, construct name | no | 0..n | No construct in the schema annotates without asserting |
| `submitted_at` | instant | yes | 1 | Not possible |
| `submitted_by` | pinned-ref to party | yes | 1 | Not possible |
| `steward` | pinned-ref to party | no | 0..1 | No steward is assigned, which constrains progression under P9-5-11 |
| `document_ref` | pinned-ref to `Part 1` | yes | 1 | Not possible; every published schema version is a controlled document, see §12.4 |

**P9-3-09** (MUST) [D] The schema version record MUST contain every field marked required in the table in §3.2, with the type, cardinality and absence semantics stated there.

**P9-3-10** (MUST NOT) [D] A schema version record MUST NOT be modified after registration, and a change to the registered content MUST produce a new schema version.

**P9-3-11** (MUST) [D] `open_content_positions` MUST be derived by the registry from the schema and the pinned dialect at registration, and MUST NOT be supplied by the submitter.

**P9-3-12** (MUST) [D] `annotation_only_constructs` MUST be derived by the registry from the pinned dialect's classification of each construct as assertion or annotation, and MUST be retrievable with every validation record that used the version.

### 3.3 Identity: why the registry holds three digests

A single digest cannot serve identity, equivalence and compatibility at once, and the evidence that it cannot comes from the specification that went furthest in defining one. Avro's Parsing Canonical Form is defined so that schemas with textually equal canonical forms are the same as far as any reader is concerned, and to achieve that property it discards attributes that do not affect parsing. It discards `doc`, so two schemas that state different meanings in their documentation have the same canonical form. It also omits attributes that do affect schema resolution, which is why third party work extended it into a resolution canonical form retaining defaults and aliases, and why a proposal to name such a form was raised against the specification. A registry that holds only a parsing style canonical digest cannot detect a documentation change and cannot compute compatibility from its own identity. A registry that holds only a literal digest cannot recognise that two registrations are the same schema differently formatted.

**P9-3-13** (MUST) [D] The registry MUST hold, for every schema version, a literal digest over the exact registered bytes, a canonical digest over the canonical form defining reader equivalence, and a compatibility digest over the form retaining every attribute the applicable rule set consults.

**P9-3-14** (MUST) [S] Each of the three digests MUST record the canonicaliser identity and version under which it was computed. **Source.** Avro recommends three fingerprint algorithms over its Parsing Canonical Form and frames the choice as a trade off between length and collision probability; it does not require the canonicalisation rules themselves to be versioned, and this part requires it because the rules have demonstrably been extended.

**P9-3-15** (MUST NOT) [D] The registry MUST NOT compare digests computed under different canonicaliser versions, and MUST report such a comparison as `incomparable_identity`.

**P9-3-16** (MUST) [D] Where a submission's assigned identity matches an existing schema version and its literal digest differs, the registry MUST refuse the submission with the outcome `identity_mutation_refused`.

**P9-3-17** (MUST) [D] Where a submission's canonical digest matches an existing schema version and its assigned identity differs, the registry MUST register the submission and MUST record an equivalence relation between the two versions.

**P9-3-18** (MUST NOT) [D] The registry MUST NOT merge two schema versions that share a canonical digest, because their assigned identities may carry different governance, different participants and different documentation.

**P9-3-19** (MUST) [D] Where two schema versions share a canonical digest and differ in literal content, the registry MUST record which attributes the canonical form discarded, so that a reader can establish what the equivalence claim does not cover.

**P9-3-20** (MUST NOT) [D] The registry MUST NOT present a canonical digest as evidence that two versions have the same meaning.

### 3.4 The registration record

| Field | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `registration_id` | identifier | yes | 1 | Not possible |
| `schema_version_id` | identifier | yes | 1 | Not possible |
| `registration_authority` | pinned-ref to party | yes | 1 | Not possible |
| `submitted_by` | pinned-ref to party | yes | 1 | Not possible |
| `submitted_at` | instant | yes | 1 | Not possible |
| `status_history` | structure: status, instant, acting party, authorisation ref | yes | 1..n | Not possible; the first entry records admission |
| `mandatory_metadata_complete` | boolean | yes | 1 | Not possible; see P9-5-09 |
| `harmonisation_ref` | identifier | no | 0..n | No duplicate or overlapping item was identified; MUST NOT be read as harmonisation not performed, which is recorded separately |
| `harmonisation_performed_at` | instant | no | 0..1 | Harmonisation was not performed |
| `retirement_reason` | enum, declared by authority | no | 0..1 | The item is not retired |
| `successor_version_id` | identifier | no | 0..1 | No successor is designated, which for a superseded version is a defect under P9-5-16 |

**P9-3-21** (MUST) [S] Every registration record MUST carry the registration authority under whose authority the item was admitted. **Source.** ISO/IEC 11179-6:2023 places registration and identifier assignment under one or more registration authorities and requires each to establish its own procedures for submission, progression, harmonisation, modification, retirement and administration.

**P9-3-22** (MUST) [D] Every entry in `status_history` MUST carry the authorisation decision reference that permitted the transition.

**P9-3-23** (MUST) [D] The registry MUST record whether harmonisation was performed and MUST NOT treat an absent harmonisation record as evidence that no duplicate exists.

### 3.5 The reference closure record

| Field | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `reference_closure_id` | identifier | yes | 1 | Not possible |
| `root_schema_version_id` | identifier | yes | 1 | Not possible |
| `resolved_at` | instant | yes | 1 | Not possible |
| `members` | structure: reference expression, resolved schema version id, intrinsic digest, depth | yes | 1..n | Not possible; a version with no references has no closure record |
| `unresolved_references` | structure: reference expression, reason | no | 0..n | Every reference resolved; a closure with unresolved members MUST NOT be registered under P9-6-15 |
| `external_locators` | uri | no | 0..n | No reference names a location outside the registry; see P9-6-16 |
| `cyclic` | boolean | yes | 1 | Not possible; false means the closure is acyclic |
| `dynamic_references` | structure: reference expression, resolution rule | no | 0..n | No reference in the closure resolves dynamically at validation time |

**P9-3-24** (MUST) [D] Every member of a reference closure MUST be recorded with the intrinsic digest of the version it resolved to, and MUST NOT be recorded as a location alone.

**P9-3-25** (MUST) [S] Where a schema language admits references whose target is determined during validation rather than at registration, the registry MUST record each such reference and the rule by which it resolves. **Source.** JSON Schema 2020-12 provides `$dynamicRef` and `$dynamicAnchor`, replacing the `$recursiveRef` and `$recursiveAnchor` of 2019-09, under which the target of a reference depends on the dynamic scope at evaluation time.

**P9-3-26** (MUST) [D] The registry MUST record whether a closure is cyclic, because a cyclic closure bounds the analyses in §6.7 and the coverage computation in §7.3.

### 3.6 The compatibility assertion record

| Field | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `assertion_id` | identifier | yes | 1 | Not possible |
| `reader_version_id` | identifier | yes | 1 | Not possible |
| `writer_version_id` | identifier | yes | 1 | Not possible |
| `subject_id` | identifier | yes | 1 | Not possible |
| `rule_set_ref` | pinned-ref | yes | 1 | Not possible |
| `dialect_id` | identifier | yes | 1 | Not possible |
| `canonicaliser_id` | pinned-ref | yes | 1 | Not possible |
| `verdict` | enum, §7.4 | yes | 1 | Not possible |
| `determined_at` | instant | yes | 1 | Not possible |
| `determined_by` | identifier of the determining implementation and version | yes | 1 | Not possible |
| `scope` | enum(`adjacent`,`transitive`,`declared_pair`) | yes | 1 | Not possible |
| `basis` | enum(`mechanical`,`mechanical_and_declared`,`declared_only`) | yes | 1 | Not possible; see P9-3-30 |
| `semantic_change_declaration_id` | identifier | no | 0..1 | No semantic change declaration exists for the pair, which under P9-6-33 forbids a verdict of compatible |
| `implied_deployment_order` | enum(`readers_first`,`writers_first`,`either`,`undetermined`) | yes | 1 | Not possible |
| `population_scope` | enum(`all_registered_participants`,`named_participants`,`unverified_population`) | yes | 1 | Not possible; see §6.8 |
| `participants_considered` | pinned-ref to participant registration | no | 0..n | The assertion was not computed against a participant population, which requires `population_scope` of `unverified_population` |
| `findings` | structure: path, change class, effect | no | 0..n | The rule set produced no itemised findings, not that no changes exist |
| `waiver_id` | identifier | no | 0..1 | No waiver applies |

**P9-3-27** (MUST) [D] A compatibility assertion MUST name a reader version and a writer version as an ordered pair, and MUST NOT be recorded against a schema, a subject or a single version.

**P9-3-28** (MUST) [P] A compatibility assertion MUST record the rule set, the dialect and the canonicaliser under which it was determined. **Source.** Widely deployed registry practice applies different compatibility rules for Avro, protocol buffers and JSON Schema under the same compatibility mode name, so a mode name alone does not identify the relation asserted.

**P9-3-29** (MUST) [P] A compatibility assertion MUST record its scope as adjacent, transitive or a declared pair, and MUST NOT be recorded without a scope. **Source.** Widely deployed registry practice documents that its default compatibility mode is non transitive and checks a new version only against the latest registered version.

**P9-3-30** (MUST) [D] `basis` MUST record whether the verdict rests on mechanical determination alone, and the registry MUST NOT present a mechanical verdict as a statement about substitutability.

**P9-3-31** (MUST) [P] A compatibility assertion MUST record the implied deployment order that its direction entails. **Source.** Widely deployed registry practice documents that a backward compatible change requires consumers to be upgraded before producers, and that a forward compatible change requires the reverse.

**P9-3-32** (MUST NOT) [D] A compatibility assertion MUST NOT be modified after it is written, and a re-determination MUST produce a new assertion.

### 3.7 The semantic change declaration

Mechanical compatibility is computed; semantic change is declared. A registry that computes the first and does not require the second reports that a version is safe when the only change was that a field's unit went from grams to kilograms.

| Field | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `declaration_id` | identifier | yes | 1 | Not possible |
| `predecessor_version_id` | identifier | yes | 1 | Not possible |
| `successor_version_id` | identifier | yes | 1 | Not possible |
| `overall_class` | enum, below | yes | 1 | Not possible |
| `changes` | structure: path, class, prior definition ref, new definition ref, note | no | 0..n | No itemised change was declared; permitted only where `overall_class` is `none` |
| `declared_by` | pinned-ref to party | yes | 1 | Not possible |
| `declared_at` | instant | yes | 1 | Not possible |
| `authorisation_ref` | pinned-ref | yes | 1 | Not possible |

Semantic change classes, closed enumeration:

| Class | Meaning |
|---|---|
| `none` | No position changed in meaning |
| `meaning_narrowed` | A position now admits a subset of what it previously meant |
| `meaning_widened` | A position now admits more than it previously meant |
| `meaning_replaced` | A position now means something not related to what it previously meant |
| `unit_or_scale_changed` | The quantity a position expresses is unchanged, its unit or scale is not |
| `enumeration_member_repurposed` | An enumeration member retains its token and changes its referent |
| `optionality_reinterpreted` | The meaning of an absent value at a position changed |
| `nullability_reinterpreted` | The meaning of a present null at a position changed |
| `identity_of_referent_changed` | A position identifying an entity now identifies it under a different identity scheme |
| `default_changed` | A declared default value changed |
| `cardinality_meaning_changed` | The meaning of repetition at a position changed, such as from a set to an ordered sequence |

**P9-3-33** (MUST) [D] Every version transition within a subject MUST carry exactly one semantic change declaration.

**P9-3-34** (MUST NOT) [D] The registry MUST NOT derive a semantic change declaration mechanically, and MUST require it to be declared by an accountable party.

**P9-3-35** (MUST) [D] Where `overall_class` is other than `none`, the declaration MUST itemise at least one change in `changes`.

**P9-3-36** (MUST) [D] Where a change class is `optionality_reinterpreted` or `nullability_reinterpreted`, the declaration MUST state the prior and the new meaning of absence and of null at that position. **Note.** This part requires the distinction because absence and null are separately meaningful and are routinely conflated; §11.9 gives the mechanism and the consequence.

**P9-3-37** (MUST) [D] Where a change is `enumeration_member_repurposed`, the declaration MUST name the member token and MUST cite the prior and new `Part 10` value set versions or `Part 4` definitions.

### 3.8 The contract version record

| Field | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `contract_version_id` | identifier | yes | 1 | Not possible |
| `contract_id` | identifier | yes | 1 | Not possible |
| `version_designation` | string | yes | 1 | Not possible |
| `interactions` | structure, below | yes | 1..n | Not possible; a contract with no interaction is not a contract |
| `participants` | pinned-ref to participant registration | yes | 1..n | Not possible; see P9-3-40 |
| `registration_status` | enum, §5.2 | yes | 1 | Not possible |
| `version_state` | enum, §5.3 | yes | 1 | Not possible |
| `compatibility_policy_id` | identifier | yes | 1 | Not possible |
| `document_ref` | pinned-ref to `Part 1` | yes | 1 | Not possible |
| `predecessor_id` | identifier | no | 0..1 | First version of the contract |

Each interaction carries:

| Field | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `interaction_name` | string | yes | 1 | Not possible |
| `request_schema_binding` | binding | no | 0..1 | The interaction carries no request payload |
| `response_schema_binding` | binding | no | 0..1 | The interaction carries no response payload; for a one way interaction this is the normal case and MUST NOT be read as an unspecified response |
| `error_schema_bindings` | binding | no | 0..n | No error payload is specified, which §12.7 states is a defect for any interaction that can fail |
| `ordering_guarantee` | enum(`none`,`per_key`,`total`) | yes | 1 | Not possible |
| `delivery_guarantee` | enum(`at_most_once`,`at_least_once`,`exactly_once`,`unspecified`) | yes | 1 | Not possible |
| `idempotence` | enum(`idempotent`,`not_idempotent`,`idempotent_under_key`) | yes | 1 | Not possible |
| `replay_expectation` | enum(`none`,`bounded`,`unbounded`) | yes | 1 | Not possible |

**P9-3-38** (MUST) [D] A binding MUST reference a schema version by intrinsic identity and MUST NOT reference a schema or a subject without a version.

**P9-3-39** (MUST) [D] Every interaction MUST declare its ordering, delivery, idempotence and replay properties explicitly, and `unspecified` MUST be available only for delivery.

**P9-3-40** (MUST) [D] Every contract version MUST name at least one participant, and the registry MUST refuse to publish a contract version with no participant.

**P9-3-41** (MUST) [D] Where a contract version declares an unbounded replay expectation, the registry MUST require the compatibility policy to be transitive in scope, because an unbounded replay means a reader may encounter any prior version.

### 3.9 Value set bindings

| Field | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `binding_id` | identifier | yes | 1 | Not possible |
| `schema_version_id` | identifier | yes | 1 | Not possible |
| `path` | path | yes | 1 | Not possible |
| `value_set_ref` | pinned-ref to `Part 10` | yes | 1 | Not possible |
| `strength` | enum(`required`,`extensible`,`preferred`,`example`) | yes | 1 | Not possible |
| `inlined_members` | string | no | 0..n | The schema does not restate the value set's members, which is the required condition under P9-3-43 |

**P9-3-42** (MUST) [S] Every position whose permitted values are drawn from a governed value set MUST carry a value set binding with a pinned value set version and a declared strength. **Source.** FHIR binds an element to a value set with a declared binding strength, of which the strongest requires the value to be drawn from the value set.

**P9-3-43** (MUST NOT) [D] A schema version MUST NOT restate the members of a governed value set inline except where its schema language provides no other means of expressing the constraint.

**P9-3-67** (MUST) [D] Where a schema language forces the members of a governed value set to be stated inline, the registry MUST record the inlined members.

**P9-3-68** (MUST) [D] Where the members of a governed value set are stated inline, the registry MUST record the binding as derived rather than authoritative.

**P9-3-44** (MUST) [D] Where inlined members are recorded, the registry MUST detect and report divergence between them and the pinned value set version.

**P9-3-45** (MUST NOT) [D] The registry MUST NOT treat the addition of a member to a bound value set as a change to the schema version, and MUST treat it as a change to the reference closure of the contract under §6.10.

### 3.10 The participant registration record

| Field | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `participant_registration_id` | identifier | yes | 1 | Not possible |
| `party_ref` | pinned-ref to party | yes | 1 | Not possible |
| `contract_version_id` | identifier | yes | 1 | Not possible |
| `role` | enum(`producer`,`consumer`,`both`) | yes | 1 | Not possible |
| `schema_versions_held` | structure: binding position, schema version id | yes | 1..n | Not possible |
| `declared_at` | instant | yes | 1 | Not possible |
| `declared_by` | pinned-ref to party | yes | 1 | Not possible |
| `confirmation_basis` | enum(`self_declared`,`observed`,`attested`) | yes | 1 | Not possible; see P9-3-47 |
| `last_confirmed_at` | instant | no | 0..1 | The registration has never been confirmed since declaration |
| `withdrawn_at` | instant | no | 0..1 | The participant is current |

**P9-3-46** (MUST) [D] The registry MUST maintain a participant registration for every declared reader and writer of every published contract version.

**P9-3-47** (MUST) [D] Every participant registration MUST record whether the version held is self declared, observed by the registry, or attested by an accountable party, because a compatibility determination over self declared holdings is weaker evidence than one over observed holdings and the difference must be visible.

**P9-3-48** (MUST) [D] The registry MUST record the instant of last confirmation of every participant registration, and MUST expose registrations unconfirmed for longer than a declared interval.

**P9-3-49** (MUST NOT) [D] The registry MUST NOT delete a withdrawn participant registration, because a compatibility assertion computed while that participant was current cites it.

### 3.11 The validation record

| Field | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `validation_record_id` | identifier | yes | 1 | Not possible |
| `instance_digest` | digest | yes | 1 | Not possible |
| `instance_ref` | content address or pinned-ref | no | 0..1 | The instance was not retained; the digest remains |
| `schema_version_id` | identifier | yes | 1 | Not possible |
| `dialect_id` | identifier | yes | 1 | Not possible |
| `vocabulary_set` | identifier | yes | 1..n | Not possible |
| `rule_set_ref` | pinned-ref | no | 0..1 | Validation applied no rule set beyond the dialect |
| `reference_closure_id` | identifier | no | 0..1 | The schema version has no references |
| `validator_id` | identifier of implementation and version | yes | 1 | Not possible; see P9-3-52 |
| `performed_at` | instant | yes | 1 | Not possible |
| `outcome` | enum, §7.2 | yes | 1 | Not possible |
| `findings` | structure, below | no | 0..n | The validation produced no finding; MUST NOT be read as the instance being fully examined |
| `evaluated_extent` | structure, below | yes | 1 | Not possible; see §7.3 |
| `annotations_collected` | structure: path, construct, value | no | 0..n | No annotation was collected, or collection was not requested and that fact is recorded in `annotation_collection` |
| `annotation_collection` | enum(`collected`,`not_collected`,`partial`) | yes | 1 | Not possible |
| `constrained_generation` | boolean | no | 0..1 | The provenance of the instance with respect to schema constrained generation is unknown; see §12.11 |
| `requested_by` | pinned-ref to party or component | yes | 1 | Not possible |

Each finding carries:

| Field | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `finding_id` | identifier | yes | 1 | Not possible |
| `severity` | enum(`violation`,`warning`,`information`) | yes | 1 | Not possible |
| `instance_path` | path | yes | 1 | Not possible |
| `location_notation` | identifier | yes | 1 | Not possible |
| `schema_path` | path | yes | 1 | Not possible |
| `construct` | string | yes | 1 | Not possible |
| `construct_role` | enum(`assertion`,`annotation`,`unrecognised`) | yes | 1 | Not possible |
| `message` | text | no | 0..1 | No human readable message was produced |

The evaluated extent carries:

| Field | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `grain` | enum(`node`,`member`,`byte_range`,`element`) | yes | 1 | Not possible |
| `locations_examined` | integer ≥ 0 | yes | 1 | Not possible |
| `locations_present` | integer ≥ 0 | yes | 1 | Not possible |
| `unexamined_locations` | path | no | 0..n | Every present location was examined by at least one assertion |
| `unexamined_cause` | structure: path, cause enum, §7.3 | no | 0..n | No location was unexamined |
| `coverage_complete` | boolean | yes | 1 | Not possible |

**P9-3-50** (MUST) [D] Every validation MUST produce a validation record, including a validation whose outcome is that the instance conforms.

**P9-3-51** (MUST) [D] Every validation record MUST carry the complete reproducibility set, being the instance digest, the schema version, the dialect, the vocabulary set, the rule set where one applied, the reference closure, the canonicaliser and the validator identity and version.

**P9-3-52** (MUST) [S] The validation record MUST identify the validating implementation and its version. **Source.** JSON Schema 2020-12 permits an implementation to validate the `format` keyword even under the annotation vocabulary, as a setting disabled by default, and records that implementations have historically disagreed on the strictness of format validation; the same instance and schema can therefore yield different results under different implementations, so the implementation is part of the result.

**P9-3-53** (MUST) [D] Every finding MUST record whether the construct that produced it is an assertion, an annotation or unrecognised.

**P9-3-54** (MUST NOT) [D] A validation record MUST NOT be modified after it is written, and a re-validation MUST produce a new record.

**P9-3-55** (MUST) [D] Where the instance is not retained, the validation record MUST retain the instance digest, so that a later presentation of an instance can be tested against the record.

### 3.12 The waiver record

| Field | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `waiver_id` | identifier | yes | 1 | Not possible |
| `schema_version_id` | identifier | yes | 1 | Not possible |
| `failed_assertion_ids` | identifier | yes | 1..n | Not possible |
| `granted_by` | pinned-ref to party | yes | 1 | Not possible |
| `granted_at` | instant | yes | 1 | Not possible |
| `authorisation_ref` | pinned-ref | yes | 1 | Not possible |
| `reason` | text | yes | 1 | Not possible |
| `expires_at` | instant | yes | 1 | Not possible; see P9-3-57 |
| `affected_participants` | pinned-ref to participant registration | yes | 1..n | Not possible; see P9-3-58 |
| `remediation_ref` | identifier | no | 0..1 | No remediation is tracked, which P9-3-59 forbids at publication |

**P9-3-56** (MUST) [D] A schema version that failed a compatibility determination MUST NOT be published without a waiver record.

**P9-3-57** (MUST) [D] Every waiver MUST carry an expiry instant, and the registry MUST NOT accept a waiver without one.

**P9-3-58** (MUST) [D] Every waiver MUST enumerate the participant registrations it affects, so that the parties bearing the risk of the waiver are named in it.

**P9-3-59** (MUST) [D] Every waiver MUST reference a remediation, and the registry MUST refuse a waiver that references none.

**P9-3-60** (MUST NOT) [P] The registry MUST NOT permit a compatibility determination to be disabled as a configuration setting, and MUST require every bypass to be expressed as a waiver. **Source.** Widely deployed registry practice provides a compatibility level of NONE and documents the practice of temporarily setting it in order to register an otherwise incompatible version; that practice leaves no record of who accepted the risk, for which participants, or until when, and §11.5 states the consequence.

### 3.13 Mutability and derivation

**P9-3-61** (MUST NOT) [D] Schema version records, registration records, reference closures, compatibility assertions, semantic change declarations, validation records and waivers MUST NOT be updated after they are written.

**P9-3-62** (MUST) [D] Where the current value of a mutable field of a subject, contract or participant registration changes, the registry MUST retain the prior value with the instant of change and the cause.

**P9-3-63** (MUST) [D] The registry MUST be implementable over a store in which no written record is subsequently modified, with current state read as a projection over appended records.

**P9-3-64** (MUST) [D] Registration status and version state MUST be held as recorded transitions rather than as mutable fields, so that the state at any past instant is recoverable.

**P9-3-65** (MUST) [D] The registry MUST version its own record schemas and MUST record, for every record it writes, the version of the record schema under which it was written.

**P9-3-66** (MUST NOT) [D] The registry MUST NOT reinterpret a record written under an earlier record schema version according to a later version's semantics.

---

## 4. Interfaces

### 4.1 General interface rules

**P9-4-01** (MUST) [D] Every operation the registry accepts MUST be defined in terms of the records of §3 and MUST state which records it creates and which events it emits.

**P9-4-02** (MUST) [D] Every operation that changes state MUST accept an idempotency key supplied by the caller and MUST return the result of the original application when invoked again with the same key and the same arguments.

**P9-4-03** (MUST) [D] Every operation invoked with a previously seen idempotency key and different arguments MUST be rejected with `idempotency_conflict`.

**P9-4-04** (MUST) [D] Every operation that registers, progresses, publishes, deprecates, retires or waives MUST obtain an authorisation decision from `Part 7` before applying, and MUST record the reference to that decision.

**P9-4-05** (MUST) [D] Every operation MUST return exactly one outcome value from the taxonomy in §7.

**P9-4-06** (MUST) [D] Every rejected operation MUST be recorded with the requesting party, the instant, the arguments digest and the rejection outcome, because a pattern of refused registrations is evidence about the schemas being attempted.

**P9-4-07** (MUST NOT) [D] The registry MUST NOT expose any operation that mutates registered content.

### 4.2 Registration operations

| Operation | Effect | Invocable by | Mode |
|---|---|---|---|
| `submit_schema` | Creates a schema version in `submitted` and a registration record | a submitter | synchronous |
| `progress_status` | Appends a status transition | the registration authority, on a steward's sponsorship | synchronous |
| `publish_version` | Sets version state to `published` | the registration authority | synchronous |
| `deprecate_version` | Sets version state to `deprecated` | the registration authority | synchronous |
| `sunset_version` | Sets version state to `sunset` | the registration authority | synchronous |
| `retire_version` | Sets registration status to `retired` | the registration authority | synchronous |
| `declare_semantic_change` | Creates a semantic change declaration | an accountable declaring party | synchronous |
| `grant_waiver` | Creates a waiver | an authorised party | synchronous |
| `revoke_waiver` | Ends a waiver before expiry | an authorised party | synchronous |
| `register_participant` | Creates a participant registration | a participant or its steward | synchronous |
| `confirm_participant` | Records confirmation of a holding | a participant or the registry on observation | synchronous |
| `withdraw_participant` | Ends a participant registration | a participant or its steward | synchronous |
| `submit_contract` | Creates a contract version | a submitter | synchronous |
| `publish_contract` | Sets contract version state to `published` | the registration authority | synchronous |

**P9-4-08** (MUST) [D] `submit_schema` MUST compute all three digests, derive the open content positions, derive the annotation only constructs, and resolve the reference closure before the submission is accepted.

**P9-4-09** (MUST) [D] `submit_schema` MUST refuse a submission whose declared dialect is absent, and MUST NOT infer a dialect from the content.

**P9-4-10** (MUST) [D] `submit_schema` MUST refuse a submission containing a construct the pinned dialect does not define, with the outcome `unrecognised_construct_refused`.

**P9-4-11** (MUST) [D] `publish_version` MUST refuse where no semantic change declaration exists for the transition from the predecessor version.

**P9-4-12** (MUST) [D] `publish_version` MUST refuse where a compatibility determination required by the subject's policy has not been performed, with the outcome `determination_missing`.

**P9-4-13** (MUST) [D] `publish_version` MUST refuse where a required determination returned a verdict of incompatible and no waiver is in force.

**P9-4-14** (MUST NOT) [D] `deprecate_version` MUST NOT change the ability of a reader to resolve or validate against the version, and MUST affect only its availability for new bindings.

**P9-4-15** (MUST) [D] `sunset_version` MUST require the registry to record which participant registrations still hold the version at the instant of sunset.

**P9-4-16** (MUST) [D] `retire_version` MUST refuse where any published contract version binds the schema version, with the outcome `bound_by_contract`.

**P9-4-17** (MUST) [D] `revoke_waiver` MUST record the revoking party and reason, and MUST NOT delete the waiver.

### 4.3 Determination and validation operations

| Operation | Effect | Invocable by | Mode |
|---|---|---|---|
| `determine_compatibility` | Creates a compatibility assertion for an ordered pair | any authorised caller | synchronous |
| `determine_compatibility_set` | Creates one assertion per pair over a stated set | any authorised caller | asynchronous |
| `validate_instance` | Creates a validation record | any authorised caller | synchronous |
| `validate_batch` | Creates one validation record per instance | any authorised caller | asynchronous |
| `resolve_closure` | Creates a reference closure record | any authorised caller | synchronous |
| `analyse_impact` | Returns the participants and contract versions a stated change would affect | any authorised caller | synchronous |
| `explain_finding` | Returns the construct, path and dialect basis of a stated finding | any authorised caller | synchronous |

**P9-4-18** (MUST) [D] `determine_compatibility` MUST require the caller to name the reader version and the writer version, and MUST NOT accept a single version with an implied counterpart.

**P9-4-19** (MUST) [D] `determine_compatibility` MUST require the caller to name the rule set, or MUST apply the rule set the subject declares and record which was applied.

**P9-4-20** (MUST NOT) [D] `determine_compatibility` MUST NOT return a verdict of compatible over a transitive scope where only adjacent pairs were determined.

**P9-4-21** (MUST) [D] `validate_instance` MUST return the evaluated extent with every outcome, including outcomes in which the instance conformed.

**P9-4-22** (MUST) [D] `validate_instance` MUST accept a caller declaration of whether the instance was produced under schema constrained generation, and MUST record the declaration or its absence.

**P9-4-23** (MUST NOT) [D] `validate_instance` MUST NOT return a boolean as its complete result, and MUST return an outcome from §7.2 together with findings and evaluated extent.

**P9-4-24** (MUST) [D] `analyse_impact` MUST report the participants it could not establish separately from the participants it could, and MUST NOT report an empty affected set where the participant register is incomplete.

**P9-4-25** (MUST) [D] `explain_finding` MUST identify the dialect and vocabulary under which the construct that produced the finding is defined, so that a disputed finding can be traced to the interpretation that produced it.

### 4.4 Query operations

**P9-4-26** (MUST) [D] The registry MUST expose retrieval of a schema version by assigned identity and by intrinsic identity.

**P9-4-27** (MUST) [D] The registry MUST expose a point in time query returning the registration status and version state of a schema version, a contract version or a participant registration as at a stated past instant.

**P9-4-28** (MUST) [D] The registry MUST expose the set of compatibility assertions concerning a stated ordered pair, and MUST return all of them rather than the most recent alone.

**P9-4-29** (MUST) [D] Every query result concerning compatibility MUST carry the scope, basis and population scope of each assertion it returns.

**P9-4-30** (MUST NOT) [D] A query MUST NOT change any state other than a read record.

**P9-4-31** (MUST NOT) [D] The registry MUST NOT expose a query that returns a compatibility verdict without the parameters under which it was determined.

### 4.5 Events emitted

**P9-4-32** (MUST) [D] The registry MUST emit an event for every registration, status transition, version state transition, compatibility determination, waiver grant and revocation, participant registration change and contract publication.

**P9-4-33** (MUST) [D] Every emitted event MUST carry the identifier of the record it concerns, the prior state where a state changed, the instant, the acting party and the identifier of the event itself.

**P9-4-34** (MUST) [D] Every emitted event MUST be delivered to `Part 3` at least once, and the registry MUST retain the event until delivery is acknowledged.

**P9-4-35** (MUST) [D] The registry MUST emit a distinct event class for a validation whose evaluated extent is incomplete, so that a consumer can subscribe to partially examined instances without parsing outcomes.

**P9-4-36** (MUST) [D] The registry MUST emit a distinct event class for a waiver approaching expiry, at a declared interval before the expiry instant.

**P9-4-37** (MUST) [D] The registry MUST emit an event when a bound value set version is superseded, naming every contract version affected.

**P9-4-38** (MUST NOT) [D] The registry MUST NOT emit an event describing a state change that was not applied.

**P9-4-39** (SHOULD) [D] The registry SHOULD emit an event when a participant registration passes its confirmation interval, because an unconfirmed holding weakens every compatibility assertion computed over it.

### 4.6 What the registry reads from other components

| Read | Component | Pinning requirement | On failure |
|---|---|---|---|
| Governed definition cited by a schema position | `Part 4` | pinned at registration | refuse registration; do not register an uncited position as undefined |
| Value set version for a binding | `Part 10` | pinned at registration | refuse registration of the binding |
| Artifact bytes and content address | `Part 11` | content address is inherently pinned | refuse registration; do not register a schema whose bytes are unaddressable |
| Document identity, approval and effective date | `Part 1` | pinned per version | refuse publication |
| Authorisation decision | `Part 7` | policy version pinned per decision | deny the operation; do not permit on failure |
| Rule verdict for a constraint outside this part's decidability condition | `Part 2` | rule version pinned per evaluation | record the non verdict; do not treat as satisfied or violated |
| Party identity for submitter, steward and participant | `Part 10` | snapshot pinned per record | refuse the operation |
| Selection among candidate versions where delegated | `Part 5` | decision version pinned | report `selection_unavailable`; do not select a default |

**P9-4-40** (MUST) [D] The registry MUST treat every read in the table in §4.6 as fallible and MUST apply the stated failure behaviour rather than a default value.

**P9-4-41** (MUST NOT) [D] The registry MUST NOT permit an operation to proceed on the failure of an authorisation read.

**P9-4-42** (MUST NOT) [D] The registry MUST NOT cache a read from another component beyond the pinning scope stated in §4.6 without recording the cache instant and treating the cached value as pinned at that instant.

### 4.7 What a caller may and may not assume

**P9-4-43** (MUST) [D] A caller MAY assume that a schema version, once registered, will never change content under the same identity.

**P9-4-44** (MUST NOT) [D] A caller MUST NOT assume that an outcome of conformance means the whole instance was examined, and the registry MUST NOT be relied on to prevent that inference other than by returning the evaluated extent.

**P9-4-45** (MUST NOT) [D] A caller MUST NOT assume that a compatibility verdict computed for one pair holds for any other pair, including a pair related by a chain of individually compatible transitions.

**P9-4-46** (MUST NOT) [D] A caller MUST NOT assume that a schema version in `deprecated` cannot be validated against.

**P9-4-47** (MUST NOT) [D] A caller MUST NOT assume that the absence of a finding at a location means the location satisfied a constraint, since the location may have been unexamined.

**P9-4-48** (MUST) [D] A caller MAY assume that a validation record, once returned, is immutable and that a re-validation will appear as a separate record.

---

## 5. State model

### 5.1 Two independent axes

A registered item has two states at once, and a registry that carries one of them carries the wrong one half the time. Registration status expresses how far the item has progressed through the registry's own quality and authority procedure. Version state expresses whether the item may be used, and for what. An item can be fully standardised and withdrawn from use; an item can be published and in use while its metadata remains incomplete. ISO/IEC 11179-6 supplies the first axis and treats the second only through its documentation status categories; this part separates them.

**P9-5-01** (MUST) [D] Every schema version and every contract version MUST carry a registration status and a version state at all times.

**P9-5-02** (MUST NOT) [D] The registry MUST NOT derive one axis from the other, and MUST NOT expose one in place of the other.

**P9-5-03** (MUST) [D] Every transition on either axis MUST be recorded with its trigger, the instant, the acting party and the authorisation reference.

**P9-5-04** (MUST NOT) [D] The registry MUST NOT admit a transition not listed in this section.

**P9-5-05** (MUST) [D] Where a transition is refused because it is illegal, the refusal MUST be recorded.

### 5.2 Registration status

| Status | Meaning | Terminal |
|---|---|---|
| `submitted` | Presented for registration; mandatory metadata possibly incomplete | no |
| `recorded` | All mandatory metadata complete and all mandatory associations instantiated | no |
| `qualified` | Recorded and sponsored by a steward and approved by the registration authority | no |
| `standardized` | Qualified and adopted as the standard item for its scope | no |
| `preferred` | Standardized and designated the preferred item where several exist | no |
| `superseded` | A successor item is preferred; the item remains readable and citable | no |
| `retired` | Withdrawn from use; retained and citable | yes |
| `rejected` | Refused at admission | yes |

| From | To | Trigger |
|---|---|---|
| — | `submitted` | `submit_schema` or `submit_contract` |
| `submitted` | `recorded` | mandatory metadata completed |
| `submitted` | `rejected` | admission refused by the registration authority |
| `recorded` | `qualified` | steward sponsorship and registration authority approval |
| `qualified` | `standardized` | registration authority act |
| `standardized` | `preferred` | registration authority act |
| `preferred` | `standardized` | registration authority act removing preference |
| `recorded` | `superseded` | a successor is designated |
| `qualified` | `superseded` | a successor is designated |
| `standardized` | `superseded` | a successor is designated |
| `preferred` | `superseded` | a successor is designated |
| `superseded` | `retired` | registration authority act |
| `recorded` | `retired` | registration authority act, or submitter request |
| `qualified` | `retired` | registration authority act |
| `standardized` | `retired` | registration authority act |
| `preferred` | `retired` | registration authority act |
| `submitted` | `retired` | submitter withdrawal before completion |

**P9-5-06** (MUST) [S] Progression to `recorded` MUST require that all mandatory metadata attributes are complete and all mandatory associations are instantiated. **Source.** ISO/IEC 11179-6:2023 §4.3.3.1.4 states that the Recorded status means all mandatory metadata attributes have been completed, all mandatory associations have been instantiated and all associated constraints are to be enforced, and that the rule applies to any and all attached items.

**P9-5-07** (MUST) [S] Progression to `qualified` or above MUST require the sponsorship of a steward and the approval of the registration authority. **Source.** ISO/IEC 11179-6:2023 requires that progression of administered items to a registration status of Qualified or higher require the sponsorship of a steward and the approval of the registration authority.

**P9-5-08** (MUST NOT) [S] The registry MUST NOT treat `recorded` as a statement that the metadata meets quality requirements. **Source.** ISO/IEC 11179-6:2023 states that the contents of the mandatory metadata attributes of a Recorded item possibly do not conform to quality requirements.

**P9-5-09** (MUST) [D] The registry MUST expose `mandatory_metadata_complete` independently of registration status, so that the condition for progression is testable without inspecting the status.

**P9-5-10** (MUST) [D] `retired` and `rejected` MUST be terminal on the registration axis, and the registry MUST NOT admit any transition out of them.

**P9-5-11** (MUST NOT) [D] The registry MUST NOT progress an item above `recorded` where no steward is assigned.

**P9-5-12** (MUST) [D] The registry MUST retain and resolve a `retired` schema version, because instances written under it and validation records citing it remain.

**P9-5-13** (MUST) [D] Every transition to `superseded` MUST name the successor version.

### 5.3 Version state

| State | Meaning | Terminal |
|---|---|---|
| `draft` | Registered and not available for binding or production use | no |
| `published` | Available for new bindings and for production use | no |
| `deprecated` | Not available for new bindings; remains valid for reading and validating | no |
| `sunset` | Not available for use by any participant; retained for resolution and re-validation only | no |
| `withdrawn` | Never to be used; retained for resolution of prior records only | yes |

| From | To | Trigger |
|---|---|---|
| — | `draft` | registration |
| `draft` | `published` | `publish_version` |
| `draft` | `withdrawn` | withdrawal before publication |
| `published` | `deprecated` | `deprecate_version` |
| `published` | `withdrawn` | withdrawal of a published version, requiring a recorded reason |
| `deprecated` | `published` | reinstatement, requiring a recorded reason |
| `deprecated` | `sunset` | `sunset_version` |
| `sunset` | `deprecated` | reinstatement, requiring a recorded reason |
| `sunset` | `withdrawn` | `withdraw` |

**P9-5-14** (MUST) [D] `withdrawn` MUST be terminal on the version state axis.

**P9-5-15** (MUST) [D] The registry MUST resolve and validate against a version in `deprecated`, `sunset` or `withdrawn` when asked to do so by reference from a prior record.

**P9-5-16** (MUST) [D] The registry MUST refuse to transition a version to `sunset` while any participant registration records it as held, unless the transition carries an authorisation reference and names the holdings it overrides.

**P9-5-17** (MUST NOT) [D] The registry MUST NOT transition a version to `withdrawn` where any published contract version binds it, without first withdrawing or superseding that contract version.

**P9-5-18** (MUST) [D] Every transition to `withdrawn` from `published` MUST record a reason from an enumeration the registration authority declares.

### 5.4 Contract version state

**P9-5-19** (MUST) [D] A contract version MUST use the version state axis in §5.3 with the same states and the same transitions.

**P9-5-20** (MUST NOT) [D] A contract version MUST NOT be published while any schema version it binds is in `draft`, `sunset` or `withdrawn`.

**P9-5-21** (MUST) [D] Where a schema version bound by a published contract version is deprecated, the registry MUST record the contract version as carrying a deprecated binding and MUST NOT change the contract version's own state.

**P9-5-22** (MUST) [D] The registry MUST expose the set of published contract versions carrying at least one deprecated binding, because that set is the work list of a migration.

### 5.5 Waiver state

| State | Meaning | Terminal |
|---|---|---|
| `active` | Granted, not expired, not revoked | no |
| `expired` | The expiry instant passed | yes |
| `revoked` | Ended by act before expiry | yes |
| `discharged` | The referenced remediation completed and was accepted | yes |

| From | To | Trigger |
|---|---|---|
| — | `active` | `grant_waiver` |
| `active` | `expired` | expiry instant passed |
| `active` | `revoked` | `revoke_waiver` |
| `active` | `discharged` | remediation accepted by an authorised party |

**P9-5-23** (MUST) [D] A waiver MUST transition to `expired` at its expiry instant without any act.

**P9-5-24** (MUST) [D] The registry MUST record the version state of every schema version whose waiver expires, and MUST emit an event naming the version and the affected participants.

**P9-5-25** (MUST NOT) [D] The registry MUST NOT extend a waiver, and an extension MUST be expressed as a new waiver with its own authorisation and reason.

### 5.6 Participant registration state

| State | Meaning | Terminal |
|---|---|---|
| `declared` | Registered and not yet confirmed | no |
| `confirmed` | Confirmed within the declared confirmation interval | no |
| `stale` | Not confirmed within the declared confirmation interval | no |
| `withdrawn` | Ended | yes |

| From | To | Trigger |
|---|---|---|
| — | `declared` | `register_participant` |
| `declared` | `confirmed` | `confirm_participant` |
| `confirmed` | `stale` | confirmation interval elapsed |
| `stale` | `confirmed` | `confirm_participant` |
| `declared` | `stale` | confirmation interval elapsed without confirmation |
| any non terminal | `withdrawn` | `withdraw_participant` |

**P9-5-26** (MUST) [D] The registry MUST declare a confirmation interval and MUST transition a participant registration to `stale` when it elapses.

**P9-5-27** (MUST) [D] A compatibility determination whose population includes a `stale` or `declared` registration MUST record its population scope as `unverified_population`.

**P9-5-28** (MUST NOT) [D] The registry MUST NOT treat a `withdrawn` participant registration as absent from a historical population, and MUST include it in any determination re-performed as at an instant when it was current.

---

## 6. Execution semantics

### 6.1 Determinism and reproducibility

**P9-6-01** (MUST) [D] Given the same instance, the same pinned schema version, the same dialect, the same vocabulary set, the same rule set, the same reference closure and the same validator version, validation MUST produce the same outcome, the same findings and the same evaluated extent.

**P9-6-02** (MUST) [D] Given the same ordered pair of schema versions, the same rule set, the same dialect and the same canonicaliser, a compatibility determination MUST produce the same verdict.

**P9-6-03** (MUST NOT) [D] The registry MUST NOT allow the order in which findings are produced to affect the outcome of a validation.

**P9-6-04** (MUST) [D] The registry MUST be able to re-perform any recorded validation from its reproducibility set and MUST report `not_reproducible` where any member of that set cannot be resolved.

**P9-6-05** (MUST NOT) [D] Validation MUST NOT consult the current wall clock, the current state of any other component, or any value not present in the instance, the schema or the pinned closure.

**P9-6-06** (MUST) [D] Where a schema construct would require a value outside the instance, the registry MUST refuse the construct at registration under §6.4 rather than evaluate it at validation.

### 6.2 Language and dialect are data

**P9-6-07** (MUST) [D] The registry MUST hold the schema language and the dialect as registered data, and MUST NOT hold either as a property of its own build.

**P9-6-08** (MUST) [D] Every dialect the registry admits MUST be registered with the set of vocabularies in force and the classification of every construct in each vocabulary as assertion, annotation or reserved.

**P9-6-09** (MUST) [D] The registry MUST refuse a schema version whose dialect is not registered, and MUST NOT interpret a schema under a dialect the submitter did not declare.

**P9-6-10** (MUST NOT) [D] The registry MUST NOT interpret a schema version under any dialect other than the one pinned at its registration, at any later time, including after a newer dialect is registered.

The reason for P9-6-10 is that a schema document is not self interpreting. The same document imposes different constraints under different dialects of one language: in JSON Schema drafts 6 and 7 a `$ref` causes sibling keywords in the same schema object to be ignored, whereas later dialects evaluate them, so a constraint written beside a reference is enforced under one dialect and silently absent under another. A registry that reinterprets a stored schema under whatever dialect is current has changed the meaning of every schema it holds.

**P9-6-11** (MUST) [S] The registry MUST record which vocabularies of a dialect it supports as assertions and which it does not. **Source.** JSON Schema 2020-12 provides `$vocabulary`, under which a vocabulary may be declared with a value of false, and the standard core and validation meta-schema declares the format vocabulary with a value of false because implementations are not required to support that keyword as an assertion.

**P9-6-12** (MUST) [D] Where the registry does not support a vocabulary a schema version declares as required, the registry MUST refuse the schema version and MUST NOT register it with the vocabulary unsupported.

**P9-6-13** (MUST NOT) [D] The registry MUST NOT permit a schema version to be validated by a validator whose supported vocabulary set differs from the set pinned at registration, and MUST report `vocabulary_mismatch`.

### 6.3 Canonicalisation and identity computation

**P9-6-14** (MUST) [D] The registry MUST compute the literal digest over the exact bytes submitted, before any normalisation.

**P9-6-15** (MUST) [D] The registry MUST refuse a submission whose reference closure contains an unresolved reference, with the outcome `closure_unresolved`.

**P9-6-16** (MUST NOT) [D] The registry MUST NOT resolve any reference by retrieval from a network location at validation time, and MUST resolve every reference to a registered schema version before registration completes.

Clause P9-6-16 removes a class of failure that no schema language forbids. A schema whose reference names a location outside the registry has its meaning determined by whatever that location serves at the moment of validation. The instance that validated this morning fails this afternoon, or worse, passes this afternoon against a constraint that was silently relaxed, and the validation record cannot say which schema was applied.

**P9-6-17** (MUST) [D] Where a submitted schema names an external locator, the registry MUST record the locator.

**P9-6-90** (MUST) [D] Where a submitted schema names an external locator, the registry MUST require the target of that locator to be registered before registration completes.

**P9-6-91** (MUST) [D] Where an external locator's target is registered, the registry MUST rewrite resolution of that locator to the registered intrinsic identity.

**P9-6-18** (MUST) [D] The registry MUST record the canonicaliser version with every digest it computes and MUST refuse to compare digests across canonicaliser versions.

**P9-6-19** (MUST) [D] Where a canonicaliser is upgraded, the registry MUST recompute the affected digests under the new canonicaliser version.

**P9-6-92** (MUST) [D] Where digests are recomputed under a new canonicaliser version, the registry MUST retain the digests computed under the prior version and MUST NOT overwrite them.

**P9-6-20** (MUST) [D] The registry MUST declare, for each canonicaliser it registers, which attributes of a schema the canonical form discards.

**P9-6-21** (MUST) [S] The compatibility digest's canonical form MUST retain every attribute the applicable rule set consults, including declared defaults and declared aliases where the language provides them. **Source.** Avro's Parsing Canonical Form does not retain the `default` and `aliases` attributes, which its own schema resolution rules consult; third party work therefore defined a resolution canonical form retaining them, and a proposal to name such a form was raised against the Avro project. A registry whose only canonical form is a parsing form cannot determine compatibility from its own identities.

**P9-6-22** (MUST) [S] The registry MUST NOT treat two schema versions sharing a canonical digest as having equal documentation. **Source.** Avro states that a schema's `doc` fields are ignored for the purposes of schema resolution and may be dropped at serialisation, and its Parsing Canonical Form discards them.

**P9-6-23** (MUST) [P] The registry MUST record whether a submission was normalised before its identity was computed, and MUST NOT normalise silently. **Source.** Widely deployed registry practice exposes normalisation as a request parameter defaulting to off, so that two submissions differing only in formatting register as two versions unless normalisation is requested; this part requires the choice to be recorded either way.

### 6.4 Registration time refusals

The registry's leverage is at registration. Every defect it admits becomes a defect it must detect at validation, when the instance is in flight and the remedy is expensive.

**P9-6-24** (MUST) [D] The registry MUST refuse a schema version containing a construct the pinned dialect does not define.

**P9-6-25** (MUST NOT) [S] The registry MUST NOT admit a schema version on the basis that an unrecognised construct will be ignored at validation. **Source.** JSON Schema treats keywords it does not recognise as available for annotation collection rather than as errors, and 2020-12 requires implementations that collect annotations to include unknown keywords in the verbose output format; the consequence is that a misspelled or dialect foreign constraint silently constrains nothing.

**P9-6-26** (MUST) [D] The registry MUST derive and record every position at which the schema version admits open content.

**P9-6-27** (MUST) [D] The registry MUST derive and record every construct in the schema version that annotates without asserting under the pinned vocabulary set.

**P9-6-28** (MUST) [S] Where a construct in a schema version annotates rather than asserts under the pinned vocabulary set, the registry MUST record the position as unconstrained by that construct. **Source.** JSON Schema 2020-12 splits `format` into a Format-Annotation vocabulary and a Format-Assertion vocabulary, states that by default the keyword does not perform validation, and permits implementations to validate it only as a setting disabled by default.

**P9-6-29** (MUST) [S] The registry MUST refuse a schema version that relies on a custom construct of a kind whose support by a peer implementation cannot be expected, unless every participant of every binding contract is recorded as supporting it. **Source.** JSON Schema Validation states that implementations MAY support custom format attributes and that, save for agreement between parties, schema authors SHALL NOT expect a peer implementation to support such custom format attributes.

**P9-6-30** (MUST) [D] The registry MUST refuse a schema version whose declared dialect requires a vocabulary the registry does not support as an assertion, where the schema uses a construct from that vocabulary in a position the submitter declares constrained.

**P9-6-31** (MUST) [D] The registry MUST refuse a schema version containing a construct whose evaluation requires a fact outside the instance.

**P9-6-32** (MUST) [D] The registry MUST refuse a schema version that inlines the members of a governed value set without recording the binding, under P9-3-43.

### 6.5 Validation semantics

**P9-6-33** (MUST) [D] Validation MUST evaluate every assertion of the pinned schema version that applies to the instance.

**P9-6-34** (MUST) [D] Validation MUST record every location of the instance that no assertion examined.

**P9-6-35** (MUST NOT) [D] Validation MUST NOT report an outcome of conformance where the evaluated extent is incomplete, and MUST report `conformant_partial_extent` instead.

Clause P9-6-35 is the central requirement of this part. Every mechanism by which an instance is reported valid over unexamined content is documented in the specifications: a construct that annotates rather than asserts, an unrecognised keyword that is ignored, an open content position, and a codec that retains unknown fields without reference to a schema at all. None of these is a defect of an implementation. All of them are the specified behaviour. What is a defect is reporting the result as though the whole instance had been examined.

**P9-6-36** (MUST) [D] Validation MUST classify every finding by severity and MUST report violations, warnings and information separately.

**P9-6-37** (MUST) [S] Validation MUST distinguish a finding that fires because a condition failed from a finding that fires because a condition held, where the schema language provides both. **Source.** Schematron distinguishes an assertion, which fires when its test evaluates to false, from a report, which fires when its test evaluates to true, and both are carried in its validation report language.

**P9-6-38** (MUST) [D] Validation MUST NOT treat a finding of severity `warning` or `information` as preventing conformance, and MUST report the outcome `conformant_with_findings`.

**P9-6-39** (MUST) [D] Validation MUST collect annotations where the caller requests them, and MUST record whether annotation collection was performed, not performed or partial.

**P9-6-40** (MUST NOT) [D] Validation MUST NOT report an annotation as a finding, and MUST NOT report a finding as an annotation.

**P9-6-41** (MUST) [D] Where a validation cannot complete, the registry MUST report a non result from §7.2 and MUST NOT report the instance as non conformant.

**P9-6-42** (MUST) [D] Where the reference closure of the pinned schema version cannot be resolved at validation time, the registry MUST report `closure_unresolvable` and MUST NOT validate against the partially resolved closure.

**P9-6-43** (MUST) [D] Where a dynamic reference resolves differently for different instances, the registry MUST record the resolution taken for each validation.

**P9-6-44** (MUST) [D] Where a value set binding of strength `required` applies to a position, the registry MUST obtain the membership determination from `Part 10` and MUST record it as a separate finding class.

**P9-6-45** (MUST NOT) [D] The registry MUST NOT report a value set membership failure as a schema violation, and MUST report it as a binding violation, because the schema and the value set have different owners and different versions.

**P9-6-46** (MUST) [D] Where the membership determination from `Part 10` is unavailable, the registry MUST report the position as unexamined with the cause `binding_unresolvable` and MUST NOT report the position as conformant.

**P9-6-47** (MUST) [D] Validation MUST bound its own execution.

**P9-6-93** (MUST) [D] The registry MUST declare its validation execution bound.

**P9-6-94** (MUST) [D] The declared validation execution bound MUST be finite.

**P9-6-95** (MUST) [D] Validation MUST report `validation_bounded` where the declared execution bound is reached before every applicable assertion has been evaluated.

**P9-6-96** (MUST) [D] The registry MUST record the declared execution bound in every validation record.

The value of the bound is an implementation decision, because the cost of evaluating a schema depends on the schema's recursion depth and on the instance's size, neither of which this part constrains.

**P9-6-48** (MUST) [D] Where a reference closure is cyclic, the registry MUST bound recursion depth and MUST record the depth reached.

### 6.6 Compatibility determination

**P9-6-49** (MUST) [D] A compatibility determination MUST be made over an ordered pair of schema versions in which one is designated reader and one writer.

**P9-6-50** (MUST NOT) [D] The registry MUST NOT express a compatibility determination in the terms backward or forward without also recording which version is the reader and which the writer.

The reason is that backward and forward are relative to a viewpoint the terms do not carry. A determination that a new version is backward compatible means, in the dominant practice, that a reader using the new version can read data written under the previous one, which requires readers to be upgraded first. A reader who assumes the opposite convention will upgrade in the wrong order, and the record of the determination will not have told them which convention was used. Reader and writer are not relative to a viewpoint.

**P9-6-51** (MUST) [P] The registry MUST record the implied deployment order of every compatibility assertion. **Source.** Widely deployed registry practice documents that under backward compatibility there is no assurance that consumers using older schemas can read data produced under the new schema, so all consumers must be upgraded before new events are produced, and that under forward compatibility the producers must be upgraded first.

**P9-6-52** (MUST) [P] The registry MUST determine compatibility under the rule set applicable to the schema language of the pair, and MUST NOT apply one rule set across languages. **Source.** Widely deployed registry practice states that compatibility rules vary by schema format, with Avro, protocol buffers and JSON Schema having different rules under the same mode names.

**P9-6-53** (MUST) [P] The registry MUST NOT assert that a change is fully compatible in a schema language in which the rule set admits no fully compatible change. **Source.** Widely deployed registry practice states that in some data formats, such as JSON, there are no fully compatible changes, and that every modification is either only forward or only backward compatible.

**P9-6-54** (MUST) [S] Where a rule set determines compatibility by resolving a reader schema against a writer schema, the registry MUST record which fields of the writer schema the reader ignored. **Source.** Avro's schema resolution requires that for each field in the reader's schema there be either a default value or a matching field in the writer's schema, and states that fields of the writer's schema that do not match a field in the reader's schema are ignored.

**P9-6-55** (MUST) [S] Where a rule set resolves a union or choice by selecting the first matching alternative, the registry MUST record the alternative selected and MUST report an ambiguity finding where more than one alternative matched. **Source.** Avro's schema resolution resolves a writer's schema against the first schema in the reader's union that matches, and signals an error if none match; it does not report the case in which several would have matched.

### 6.7 Transitivity does not follow from adjacency

**P9-6-56** (MUST NOT) [P] The registry MUST NOT infer a transitive compatibility verdict from a chain of adjacent compatibility verdicts. **Source.** Widely deployed registry practice states that non transitive checking ensures compatibility between version X-2 and X-1 and between X-1 and X but not necessarily between X-2 and X, and that its default compatibility mode is non transitive.

**P9-6-57** (MUST) [D] Where a transitive verdict is required, the registry MUST determine compatibility for every pair in scope and MUST record each determination separately.

**P9-6-58** (MUST) [D] The registry MUST record, for every subject, whether its declared compatibility policy is adjacent or transitive in scope.

**P9-6-59** (MUST) [D] Where a contract version declares an unbounded replay expectation and the subject's policy is adjacent in scope, the registry MUST refuse to publish the contract version.

**P9-6-60** (MUST) [D] The registry MUST expose, for any stated pair of versions in a subject, whether a determination exists for that pair, and MUST NOT answer with a determination for a different pair.

### 6.8 Compatibility is relative to a population

**P9-6-61** (MUST) [D] Every compatibility determination MUST record the population of participants against which it was computed.

**P9-6-62** (MUST) [D] Where the participant register contains no confirmed registration for a contract version, a determination concerning that contract version MUST record its population scope as `unverified_population`.

**P9-6-63** (MUST NOT) [D] The registry MUST NOT report a change as safe for a population it cannot enumerate.

**P9-6-64** (MUST) [D] The registry MUST compute, for a proposed version, the set of participant registrations whose held versions are not covered by an existing compatibility determination against it.

**P9-6-65** (MUST) [D] The registry MUST report the set in P9-6-64 as the uncovered population of the proposed version, and MUST report it with every determination concerning that version.

Clause P9-6-64 is the operation that makes the question answerable. A registry that records only schemas can say that version 7 is compatible with version 6. Only a registry that records participants can say that three consumers are still on version 4, that no determination exists for the pair version 7 reader and version 4 writer, and that the change is therefore of unknown safety for those three.

### 6.9 Mechanical compatibility and substitutability

**P9-6-66** (MUST) [D] The registry MUST determine mechanical compatibility from the rule set alone.

**P9-6-67** (MUST NOT) [D] The registry MUST NOT report a mechanically compatible pair as substitutable.

**P9-6-68** (MUST) [D] The registry MUST refuse to publish a version whose semantic change declaration is other than `none` with a compatibility verdict of `compatible`, and MUST record the verdict as `mechanically_compatible_semantically_changed`.

**P9-6-69** (MUST) [D] The registry MUST treat a change of semantic class `unit_or_scale_changed`, `enumeration_member_repurposed`, `meaning_replaced` or `identity_of_referent_changed` as requiring a new subject rather than a new version of the existing subject.

Clause P9-6-69 is stated as a requirement rather than as advice because these four classes share a property: the instance remains structurally valid and the reader remains mechanically able to parse it, while every consumer that acts on the value acts wrongly. No mechanical check can detect any of them, and version continuity within a subject is the mechanism by which the error propagates silently.

**P9-6-70** (MUST) [D] Where a semantic change is declared at a position, the registry MUST record whether the position's governed definition in `Part 4` also changed, and MUST report a semantic change at a position whose definition did not change as a defect requiring reconciliation.

### 6.10 Change in the closure

**P9-6-71** (MUST) [D] Where a schema version in the reference closure of a published version is superseded, the registry MUST NOT alter the published version's closure.

**P9-6-72** (MUST) [D] Where a schema version in the closure of a published version is superseded, the registry MUST record the published version as carrying a superseded dependency and MUST emit an event.

**P9-6-73** (MUST) [D] Where a bound value set version is superseded, the registry MUST record every contract version affected and MUST NOT re-bind any of them.

**P9-6-74** (MUST) [D] The registry MUST treat the addition of a member to a value set bound at strength `required` as a break in compatibility for every reader that enumerates the members, and MUST record it as such.

Clause P9-6-74 states a case that mechanical schema comparison never catches, because nothing in the schema changed. A reader that switches on the members of an enumeration will fail on a member added to the value set, and the change is invisible to any check performed on the schema pair.

**P9-6-75** (MUST) [D] The registry MUST expose the closure change history of every published version, so that a validation result that differed between two instants can be attributed.

### 6.11 Concurrency and idempotence

**P9-6-76** (MUST) [D] Concurrent submissions of the same content under the same assigned identity MUST be serialised, and exactly one MUST register.

**P9-6-77** (MUST) [D] Concurrent submissions of different content under the same assigned identity MUST result in one registration and one refusal with `identity_mutation_refused`.

**P9-6-78** (MUST) [D] `validate_instance` MUST be idempotent in effect on registry state other than the creation of a validation record.

**P9-6-79** (MUST) [D] A repeated validation under the same idempotency key MUST return the original validation record rather than create a second.

**P9-6-80** (MUST) [D] Concurrent status progressions of one item MUST be serialised, and the losing attempt MUST be recorded with the outcome `illegal_transition`.

### 6.12 Time

**P9-6-81** (MUST) [D] The registry MUST record the instant of every registration, determination, validation and transition.

**P9-6-82** (MUST NOT) [D] The registry MUST NOT use the current instant in the evaluation of any assertion.

**P9-6-83** (MUST) [D] Where a schema construct expresses a temporal constraint relative to the present, the registry MUST refuse the construct under P9-6-31, because its truth is not decidable from the instance.

**P9-6-84** (MUST) [D] The registry MUST resolve a point in time query against recorded transitions and MUST NOT answer it from current state.

### 6.13 Interpretation of absence

**P9-6-85** (MUST) [D] The registry MUST record, for every position in a registered schema version at which a value may be absent, whether absence is permitted, and MUST NOT conflate a position that may be absent with a position that may be null.

**P9-6-86** (MUST) [D] Where a schema language expresses absence and null through the same construct, the registry MUST record that the language does not distinguish them and MUST record the position as carrying an unresolved absence semantics.

**P9-6-87** (MUST NOT) [D] The registry MUST NOT supply a default value during validation, and MUST NOT treat a position with a declared default as populated.

**P9-6-88** (MUST) [S] Where a rule set consults a declared default in determining compatibility, the registry MUST record that the determination depended on the default, because the default's presence in the schema and its application by a reader are different facts. **Source.** Avro's schema resolution permits a reader field absent from the writer's schema only where the reader field declares a default value.

**P9-6-89** (MUST) [D] The registry MUST record a change to a declared default as a semantic change of class `default_changed` and MUST NOT treat it as structurally inert.

---

## 7. Outcome and failure taxonomy

The organising principle of this section is that a validation answers two questions, not one: did what was examined conform, and what was examined. A taxonomy carrying only the first cannot distinguish a conforming instance from an unexamined one, and that indistinguishability is the characteristic defect of this component.

### 7.1 Structure

**P9-7-01** (MUST) [D] Every value the registry can produce MUST belong to exactly one of the enumerations in §7.2 to §7.7.

**P9-7-02** (MUST NOT) [D] The registry MUST NOT return a value outside these enumerations, and MUST NOT extend an enumeration marked closed.

**P9-7-03** (MUST) [D] The registry MUST expose, for every outcome it returns, the three properties in the table in §7.8.

### 7.2 Validation outcomes

Closed enumeration. The first four are conformance outcomes, the next three are non results, and the last four are refusals.

| Value | Meaning | Extent complete |
|---|---|---|
| `conformant` | Every assertion that applies was evaluated and none was violated, and every location was examined | yes |
| `conformant_with_findings` | As `conformant`, and at least one finding of severity `warning` or `information` was produced | yes |
| `conformant_partial_extent` | No assertion was violated, and at least one location was not examined by any assertion | no |
| `non_conformant` | At least one assertion of severity `violation` was violated | either; the extent is reported |
| `undecidable` | The instance could not be determined conformant or non conformant on the available schema and closure | no |
| `not_applicable` | The pinned schema version does not apply to the class of the instance presented | not applicable |
| `not_evaluated` | Validation was requested and not performed | no |
| `closure_unresolvable` | A member of the reference closure could not be resolved | no |
| `vocabulary_mismatch` | The validator's supported vocabulary set differs from the set pinned at registration | no |
| `validation_bounded` | The declared execution bound was reached before every assertion was evaluated | no |
| `instance_unreadable` | The instance could not be parsed in its declared format | no |

**P9-7-04** (MUST) [D] The registry MUST return `conformant` only where the evaluated extent is complete.

**P9-7-05** (MUST NOT) [D] The registry MUST NOT return `conformant` or `conformant_with_findings` where any location of the instance was unexamined, and MUST return `conformant_partial_extent`.

**P9-7-06** (MUST NOT) [D] The registry MUST NOT map `undecidable`, `not_applicable`, `not_evaluated`, `closure_unresolvable`, `vocabulary_mismatch`, `validation_bounded` or `instance_unreadable` to `non_conformant`.

**P9-7-07** (MUST NOT) [D] The registry MUST NOT map any of the seven values named in P9-7-06 to a conformance outcome.

**P9-7-08** (MUST) [D] `instance_unreadable` MUST be distinguished from `non_conformant`, because an instance that cannot be parsed has not failed a constraint and the remedy is different.

**P9-7-09** (MUST) [D] `not_applicable` MUST be returned where the schema version pinned does not govern the instance presented, and MUST NOT be returned where the schema governs the instance and the instance fails.

**P9-7-10** (MUST) [D] `validation_bounded` MUST record which assertions were not evaluated, and MUST NOT be returned without them.

### 7.3 Unexamined location causes

Closed enumeration. Every unexamined location carries exactly one cause. This enumeration is the itemisation of the silent positive and every member of it is drawn from specified behaviour rather than from implementation defect.

| Cause | Meaning |
|---|---|
| `open_content` | The position permits members not named by the schema, and the member present was not named |
| `annotation_only_construct` | The only construct applying to the position annotates rather than asserts under the pinned vocabulary set |
| `unsupported_vocabulary` | The construct applying to the position belongs to a vocabulary the validator does not support as an assertion |
| `unrecognised_construct` | A construct applying to the position is not defined by the pinned dialect |
| `wildcard_lax_or_skip` | The position falls under a wildcard whose processing mode does not require validation |
| `conditional_branch_not_taken` | The position is examined only under a conditional branch that did not apply |
| `binding_unresolvable` | The position's value set binding could not be resolved |
| `closure_member_unresolved` | The position is governed by a reference whose target could not be resolved |
| `bound_reached` | The declared execution bound was reached before the position was examined |
| `depth_bound_reached` | The recursion depth bound was reached before the position was examined |

**P9-7-11** (MUST) [D] Every unexamined location MUST carry exactly one cause from the enumeration in §7.3.

**P9-7-12** (MUST) [S] The registry MUST report `wildcard_lax_or_skip` where a position is admitted by a wildcard whose declared processing does not require the content to be validated. **Source.** W3C XML Schema provides wildcard content processing modes of strict, lax and skip, under which content matching a wildcard is respectively required to be validated, validated only where a declaration is available, and not validated at all.

**P9-7-13** (MUST) [D] The registry MUST report `annotation_only_construct` where the construct applying to a position produces an annotation and no assertion.

**P9-7-14** (MUST) [D] The registry MUST report `conditional_branch_not_taken` separately from `open_content`, because the first is a position the schema governs conditionally and the second is a position the schema does not govern at all.

**P9-7-15** (MUST) [D] The registry MUST report the count of unexamined locations with the grain at which locations were counted.

**P9-7-16** (MUST NOT) [D] The registry MUST NOT report coverage as a proportion without the grain and the absolute counts from which the proportion was computed.

**P9-7-17** (MUST) [D] Where an instance format admits content the pinned schema language cannot address, the registry MUST report the whole of that content as unexamined rather than omit it from the extent.

### 7.4 Compatibility verdicts

Closed enumeration. The first three are verdicts; the remainder are non verdicts.

| Value | Meaning |
|---|---|
| `compatible` | The rule set determined the reader can consume instances written under the writer version, and the semantic change declaration is `none` |
| `incompatible` | The rule set determined at least one instance writable under the writer version that the reader cannot consume |
| `mechanically_compatible_semantically_changed` | The rule set determined compatibility and the semantic change declaration is other than `none` |
| `undeterminable_dialect` | The two versions are pinned to dialects between which the rule set defines no relation |
| `undeterminable_language` | The two versions are expressed in different schema languages |
| `undeterminable_closure` | A reference closure member of either version could not be resolved |
| `incomparable_identity` | The digests of the two versions were computed under different canonicaliser versions |
| `rule_set_unavailable` | The pinned rule set could not be resolved |
| `not_determined` | No determination has been performed for the pair |
| `determination_bounded` | The determination reached a declared bound before completing |

**P9-7-18** (MUST) [D] The registry MUST represent all ten values and MUST record the specific value rather than a collapsed category.

**P9-7-19** (MUST NOT) [D] The registry MUST NOT treat any non verdict as `compatible`.

**P9-7-20** (MUST NOT) [D] The registry MUST NOT treat any non verdict as `incompatible`, because refusing a change on the ground that compatibility could not be determined and refusing it on the ground that it is incompatible carry different remedies.

**P9-7-21** (MUST) [D] `not_determined` MUST be returned for a pair for which no determination exists, and the registry MUST NOT substitute a determination for an adjacent pair.

**P9-7-22** (MUST) [D] Where a rule set returns a value this enumeration does not contain, the registry MUST record the value verbatim.

**P9-7-23** (MUST) [D] The registry MUST treat a value its enumeration does not contain as a non verdict.

**P9-7-24** (MUST) [D] The registry MUST raise an unrepresentable verdict event on receipt of a value its enumeration does not contain.

### 7.5 Registration outcomes

Closed enumeration.

| Value | Meaning |
|---|---|
| `registered` | The submission was admitted and a schema version created |
| `registered_equivalent` | The submission was admitted and shares a canonical digest with an existing version |
| `identity_mutation_refused` | The assigned identity exists with different literal content |
| `unrecognised_construct_refused` | The submission contains a construct the pinned dialect does not define |
| `dialect_unregistered` | The declared dialect is not registered |
| `dialect_undeclared` | No dialect was declared |
| `vocabulary_unsupported` | The submission requires a vocabulary the registry does not support as an assertion |
| `closure_unresolved` | A reference could not be resolved to a registered version |
| `external_locator_unregistered` | A reference names a location whose target is not registered |
| `external_fact_construct_refused` | A construct requires a fact outside the instance |
| `value_set_inlined_refused` | A governed value set's members were inlined without a recorded binding |
| `definition_uncited` | A position carrying a governed term does not cite its `Part 4` definition |
| `metadata_incomplete` | Mandatory metadata for the requested status is absent |
| `determination_missing` | Publication was requested and a required compatibility determination has not been performed |
| `waiver_required` | Publication was requested and a required determination returned `incompatible` with no waiver in force |
| `semantic_declaration_missing` | Publication was requested and no semantic change declaration exists for the transition |
| `bound_by_contract` | Retirement or withdrawal was requested for a version a published contract binds |
| `illegal_transition` | The requested transition is not legal from the current state |
| `not_authorised` | `Part 7` denied the operation |
| `authorisation_unavailable` | `Part 7` could not be reached, and the operation was therefore denied |
| `idempotency_conflict` | The key was seen with different arguments |

**P9-7-25** (MUST) [D] `not_authorised` and `authorisation_unavailable` MUST be distinct outcomes.

**P9-7-26** (MUST) [D] `registered_equivalent` MUST be distinct from `registered`, so that a duplicate registration is visible as one.

**P9-7-27** (MUST NOT) [D] The registry MUST NOT return `registered` where any part of the registration was not applied.

### 7.6 Non results the registry receives

**P9-7-28** (MUST) [D] Where `Part 2` returns a non verdict for a delegated constraint, the registry MUST record that non verdict and MUST report the affected position as unexamined with the cause `binding_unresolvable` or a cause the delegating clause names.

**P9-7-29** (MUST NOT) [D] The registry MUST NOT treat a non verdict from `Part 2` as a violation or as conformance.

**P9-7-30** (MUST) [D] Where `Part 10` cannot determine value set membership, the registry MUST report the position as unexamined and MUST NOT report the value as permitted.

**P9-7-31** (MUST) [D] Where `Part 11` cannot resolve a registered artifact's content, the registry MUST report `closure_unresolvable` for every validation depending on it.

**P9-7-32** (MUST) [D] Where `Part 4` cannot resolve a cited definition, the registry MUST refuse registration and MUST NOT register the position as carrying an unknown definition.

### 7.7 System fault outcomes

Closed enumeration. These describe the registry's own inability to proceed and are never validation or compatibility results.

| Value | Meaning |
|---|---|
| `store_unavailable` | The record store could not be read or written |
| `dependency_unavailable` | A required component could not be reached |
| `canonicaliser_unavailable` | The pinned canonicaliser could not be resolved |
| `validator_unavailable` | A validator for the pinned dialect could not be resolved |
| `internal_invariant_violated` | The registry detected a violation of its own invariants |

**P9-7-33** (MUST NOT) [D] A system fault outcome MUST NOT be recorded as a validation outcome or a compatibility verdict.

**P9-7-34** (MUST) [D] Where `internal_invariant_violated` is detected, the registry MUST stop applying changes to the affected subject and MUST raise the fault.

### 7.8 What distinguishes each outcome from failure

**P9-7-35** (MUST) [D] The registry MUST expose, for every validation outcome, the three properties in the following table.

| Outcome | Instance examined | Constraint violated | Requester may rely on conformance |
|---|---|---|---|
| `conformant` | fully | no | yes |
| `conformant_with_findings` | fully | no | yes, with the findings read |
| `conformant_partial_extent` | partly | no, within the extent examined | only for the extent reported |
| `non_conformant` | reported | yes | no |
| `undecidable` | partly | unknown | no |
| `not_applicable` | not applicable | not applicable | no; the wrong schema was pinned |
| `not_evaluated` | no | unknown | no |
| `closure_unresolvable` | no | unknown | no |
| `vocabulary_mismatch` | partly | unknown | no |
| `validation_bounded` | partly | unknown for the unevaluated assertions | only for the extent reported |
| `instance_unreadable` | no | not applicable | no |

The third column is the one that carries the section. Four of the eleven outcomes permit no reliance at all, and two permit reliance only over a reported extent. A consumer that treats the taxonomy as a boolean gets five distinct conditions collapsed into one, and the collapse is always in the direction of unwarranted confidence.

### 7.9 Propagation

**P9-7-36** (MUST) [D] Where the registry reports an outcome to another component, it MUST report the outcome value, the findings and the evaluated extent together, and MUST NOT report the outcome alone.

**P9-7-37** (MUST NOT) [D] The registry MUST NOT aggregate validation outcomes into a summary that loses the distinction between complete and partial extent.

**P9-7-38** (MUST) [D] Every count or rate the registry publishes over validation outcomes MUST report `conformant_partial_extent` as its own category.

**P9-7-39** (MUST NOT) [D] The registry MUST NOT publish a conformance rate that treats `conformant_partial_extent` as conformant.

**P9-7-40** (MUST) [D] Where a non result is produced and no consumer subscribes to it, the registry MUST retain it in the record of the affected validation or determination.

---

## 8. Observability and the audit record

The reconstruction test for this component is specific: a reader years later, holding only the record, must be able to establish which schema, under which dialect, interpreted by which implementation, examined which parts of which instance, and what was concluded about the parts it did not examine.

### 8.1 What must be recorded

**P9-8-01** (MUST) [D] The registry MUST record every submission, at the grain of one record per submission, including refused submissions.

**P9-8-02** (MUST) [D] The registry MUST record every registration status transition and every version state transition, at the grain of one record per transition.

**P9-8-03** (MUST) [D] The registry MUST record every compatibility determination, at the grain of one record per ordered pair per determination.

**P9-8-04** (MUST) [D] The registry MUST record every validation, at the grain of one record per instance per schema version per validation.

**P9-8-05** (MUST) [D] The registry MUST record every finding, at the grain of one record per finding per location.

**P9-8-06** (MUST) [D] The registry MUST record the evaluated extent of every validation, at the grain declared in the record.

**P9-8-07** (MUST) [D] The registry MUST record every waiver grant, revocation, expiry and discharge, at the grain of one record per event.

**P9-8-08** (MUST) [D] The registry MUST record every participant registration, confirmation, staleness transition and withdrawal.

**P9-8-09** (MUST) [D] The registry MUST record every canonicaliser registration and upgrade, and every digest recomputation it caused.

**P9-8-10** (MUST) [D] The registry MUST record every dialect registration and every change to the set of vocabularies it supports as assertions.

**P9-8-11** (MUST) [D] The registry MUST record every read of a schema version by another component, where the subject's policy declares reads recordable.

### 8.2 What must be reconstructable

**P9-8-12** (MUST) [D] A reader MUST be able to reconstruct which exact bytes were registered under any assigned identity at any past instant.

**P9-8-13** (MUST) [D] A reader MUST be able to reconstruct the dialect, vocabulary set and validator version under which any recorded validation was performed.

**P9-8-14** (MUST) [D] A reader MUST be able to reconstruct which locations of a validated instance were examined and which were not, and the cause for each unexamined location.

**P9-8-15** (MUST) [D] A reader MUST be able to reconstruct, for any compatibility assertion, the ordered pair, the rule set, the scope, the basis, the population and the implied deployment order.

**P9-8-16** (MUST) [D] A reader MUST be able to reconstruct which participants held which versions at any past instant.

**P9-8-17** (MUST) [D] A reader MUST be able to reconstruct every waiver in force at any past instant, its authoriser and the participants it exposed.

**P9-8-18** (MUST) [D] A reader MUST be able to reconstruct the semantic change declaration attached to every version transition.

**P9-8-19** (MUST) [D] A reader MUST be able to reconstruct the reference closure applied to any recorded validation, resolved to intrinsic identities.

**P9-8-20** (MUST NOT) [D] Reconstruction MUST NOT depend on the registry's runtime being available, and MUST NOT depend on any network location outside the components holding the pinned targets.

### 8.3 Grain and derivation

**P9-8-21** (MUST) [D] Every count the registry reports MUST state its grain and the instant as at which it was computed.

**P9-8-22** (MUST NOT) [D] The registry MUST NOT report a count of schemas without stating whether versions are counted individually.

**P9-8-23** (MUST) [D] Every derived metric the registry exposes MUST be accompanied by its derivation, sufficient for a reader to recompute it from the recorded events.

**P9-8-24** (MUST NOT) [D] The registry MUST NOT report a compatibility statistic without stating the scope and basis of the assertions counted.

### 8.4 Integrity and retention

**P9-8-25** (MUST) [D] Every record the registry writes MUST be integrity protected such that alteration is detectable, by a means governed by `Part 3`.

**P9-8-26** (MUST NOT) [D] The registry MUST NOT permit deletion of a schema version record, registration record, compatibility assertion, validation record, semantic change declaration or waiver other than under a recorded disposition act governed by `Part 1`.

**P9-8-27** (MUST) [D] Where a record is disposed of under a retention schedule, the registry MUST retain a tombstone carrying the identifier, the record class, the disposition act reference and the instant.

**P9-8-28** (MUST NOT) [D] The registry MUST NOT dispose of a schema version cited by a retained validation record without recording that citation as unresolvable.

**P9-8-29** (MUST) [D] The registry MUST retain the intrinsic digests of a disposed schema version, so that an instance presented later can be tested against the record of what governed it.

### 8.5 Observability of the component itself

**P9-8-30** (MUST) [D] The registry MUST expose the count of validations whose outcome was `conformant_partial_extent`, because that count is the size of the population of instances believed valid and not examined.

**P9-8-31** (MUST) [D] The registry MUST expose the distribution of unexamined location causes, because the distribution identifies which of the four mechanisms in §1.3 is operating.

**P9-8-32** (MUST) [D] The registry MUST expose the set of published schema versions carrying at least one open content position.

**P9-8-33** (MUST) [D] The registry MUST expose the set of published schema versions carrying at least one annotation only construct in a position a submitter declared constrained.

**P9-8-34** (MUST) [D] The registry MUST expose the uncovered population of every published version, per §6.8.

**P9-8-35** (MUST) [D] The registry MUST expose every active waiver with its expiry and its affected participants.

**P9-8-36** (MUST) [D] The registry MUST expose the count of participant registrations in `stale`, because every compatibility assertion computed over them is weaker than it appears.

**P9-8-37** (SHOULD) [D] The registry SHOULD expose the rate at which submissions are refused by cause, because a rising rate of `unrecognised_construct_refused` indicates a dialect mismatch between authors and the registry rather than a fault in either.

---

## 9. Extension model

### 9.1 Closed and open sets

**P9-9-01** (MUST) [D] The following sets MUST be closed and MUST NOT be extended by an implementation: registration statuses (§5.2), version states (§5.3), waiver states (§5.5), participant registration states (§5.6), validation outcomes (§7.2), unexamined location causes (§7.3), compatibility verdicts (§7.4), registration outcomes (§7.5), system fault outcomes (§7.7), semantic change classes (§3.7), value set binding strengths (§3.9) and finding severities (§3.11).

**P9-9-02** (MUST) [D] The following sets MAY be extended under the governance in §9.4: schema languages, dialects, vocabularies, canonicalisers, rule sets, location notations, and the set of operations the registry accepts.

**P9-9-03** (MUST) [D] Business enumerations within a registered schema are open by construction, being properties of the schema rather than of the registry.

The languages, dialects and rule sets are open because a registry that cannot admit a new schema language is a registry for one language, and the whole subject of this part is the governance of heterogeneous ones. The outcomes and causes are closed because they are the vocabulary in which the record speaks; an implementation that adds an unexamined location cause has created a cause no reader of §7.3 can interpret, and an implementation that adds a validation outcome has created a result that §7.8 cannot classify.

### 9.2 Admitting a schema language

**P9-9-04** (MUST) [D] A schema language MUST be registered before any schema expressed in it is registered.

**P9-9-05** (MUST) [D] A registered schema language MUST declare at least one dialect, and every dialect MUST declare its vocabulary set.

**P9-9-06** (MUST) [D] A registered dialect MUST classify every construct it defines as assertion, annotation or reserved.

**P9-9-07** (MUST) [D] A registered schema language MUST declare a canonicaliser for reader equivalence and a canonicaliser for compatibility, and the two MAY be the same only where the language's rule set consults no attribute the reader equivalence form discards.

**P9-9-08** (MUST) [D] A registered schema language MUST declare a location notation for addressing positions within instances of the formats it governs.

**P9-9-09** (MUST) [D] A registered schema language MUST declare either a rule set for compatibility determination or that no such rule set exists.

**P9-9-21** (MUST) [D] Where a registered schema language declares that no compatibility rule set exists, every determination for a pair in that language MUST return `rule_set_unavailable`.

**P9-9-10** (MUST NOT) [D] The registry MUST NOT admit a schema language whose conformance determination requires facts outside the instance, and MUST admit only the subset of such a language that satisfies the decidability condition in §2.1.

### 9.3 Composition

**P9-9-11** (MUST) [D] A schema version composed by reference from other schema versions MUST carry its own identity and its own reference closure, and MUST NOT be represented as an alias for its members.

**P9-9-12** (MUST) [S] Where a schema language provides a mechanism for redefining or overriding a construct of a referenced schema, the registry MUST record the redefinition and MUST treat the result as a distinct schema version. **Source.** W3C XML Schema provides redefinition in version 1.0 and overriding in version 1.1, both of which alter the meaning of a referenced schema's components without changing that schema.

**P9-9-13** (MUST NOT) [D] The registry MUST NOT treat a composed schema version's compatibility as derivable from the compatibility of its members.

**P9-9-14** (MUST) [S] Where a schema language provides bundling of several schemas into one document, the registry MUST record each embedded schema's own identity and MUST make each independently addressable. **Source.** JSON Schema 2020-12 provides guidance on bundling schemas into a compound schema document, in which embedded schemas retain their own identifiers.

**P9-9-15** (MUST) [D] A contract version MUST be treated as a composition over schema versions and MUST NOT be treated as a schema.

### 9.4 Governance of extension

**P9-9-16** (MUST) [D] Every extension an implementation makes MUST be declared in a machine readable extension manifest carrying the extended set, the new member and its definition.

**P9-9-17** (MUST) [D] The registry MUST record, on every record affected by an extension, the identifier of the extension manifest version under which it was written.

**P9-9-18** (MUST NOT) [D] An extension MUST NOT change the meaning of an existing member of any set.

**P9-9-19** (MUST NOT) [D] An extension MUST NOT be required for interoperation, and a consumer that ignores every extension MUST still be able to interpret every record correctly at the grain of the closed sets.

**P9-9-20** (MUST) [D] Where a new dialect of an already registered language is admitted, the registry MUST NOT reinterpret any existing schema version under it, per P9-6-10.

---

## 10. Standards and specifications

### 10.1 What each consulted specification supplies

| Specification | Status as established | What it supplies to this component | What it does not supply |
|---|---|---|---|
| JSON Schema, draft 2020-12 | Not a published standard. Issued as a draft series by the JSON Schema project. An IETF working group draft carrying the designation `draft-ietf-jsonschema-json-schema-01` exists, so the family is on a standards track without having reached an RFC; the current state of that work could not be established and is reported in §13.1 | Schema identity through `$id`; dialect and vocabulary declaration through `$schema` and `$vocabulary`; the normative distinction between assertion and annotation; the split of `format` into annotation and assertion vocabularies; dynamic references; compound schema documents and bundling; structured output formats | Any versioning model. Any compatibility relation. Any registration lifecycle. Any canonical form. Any fingerprint. Any concept of a contract or a participant |
| W3C XML Schema, versions 1.0 and 1.1 | W3C Recommendations | Wildcard content processing modes of strict, lax and skip; assertions and conditional type assignment in 1.1; redefinition in 1.0 and overriding in 1.1; the post schema validation infoset as a structured validation result | No document level identity beyond a target namespace. No versioning or compatibility model. No registration lifecycle |
| Apache Avro specification | Project specification, versioned with the Avro release | The only complete compatibility algorithm among the consulted sources, in its schema resolution rules; the Parsing Canonical Form; fingerprint algorithm recommendations; the property that equal canonical forms are indistinguishable to any reader | A canonical form sufficient for compatibility determination, which §10.4 records as a conflict. No registration lifecycle. No participant model. No validation report model |
| Protocol buffer language and encoding | Project specification | Field numbering as the basis of wire identity; the retention of unknown fields by a decoder | No schema registry. No compatibility determination. Unknown field retention is a mechanism of the silent positive rather than a defence against it |
| ISO/IEC 11179, Metadata registries, in particular Part 6 Registration, fourth edition 2023 | International Standard. The 2023 fourth edition cancels and replaces the 2015 third edition. Part 3 supplies the metamodel for registry common facilities | The registration lifecycle: registration authority, submitter, steward, registration status, the distinction between lifecycle and documentation status categories, the conditions for progression, and the required procedures for submission, progression, harmonisation, modification, retirement and administration | Nothing about schemas as artifacts, compatibility, dialects or validation. It governs the registration of items, not the semantics of what is registered |
| ISO/IEC 19757-3, Schematron | International Standard within the Document Schema Definition Languages family | The distinction between an assertion that fires when false and a report that fires when true; the role attribute carrying severity; a standard validation report vocabulary | No schema identity, versioning or compatibility |
| ISO/IEC 19757-2, RELAX NG | International Standard within the same family | A grammar based validation model that does not annotate the instance with type information and does not impose the deterministic content model constraint of W3C XML Schema | No identity, versioning, compatibility or registration model |
| W3C SHACL | W3C Recommendation | A validation result model with three severities, being Violation, Warning and Info, and with a focus node and result path locating each result | No schema versioning or compatibility model |
| HL7 FHIR | Published specification with balloted releases | Identity as a canonical URL together with a business version; value set binding with declared binding strength; validation findings carried in a structured outcome resource with issue severities | Not a general purpose registry; its identity and binding model is adopted here at the level of pattern rather than of clause |
| Widely deployed schema registry practice, as specified in the vendor documentation of the dominant implementation | Vendor specification, not a standard | The subject as the unit of compatibility grouping; the seven compatibility modes and their transitive variants; the documented non transitivity of the default mode; the documented implication of compatibility direction for deployment order; the documented variation of compatibility rules across schema languages; the normalisation request parameter | No evidentiary model. No participant register. No semantic change declaration. No evaluated extent. Its compatibility mode is a property of a subject rather than of a version pair, which §10.4 records as a conflict |
| Semantic Versioning 2.0.0 | Community specification | A convention for expressing the intended significance of a change in a version string | Nothing usable for schema compatibility, because a change's significance depends on whether the party is a reader or a writer, and a single version string cannot carry both. §11.7 gives the mechanism |
| RFC 3986, RFC 6901, RFC 8259 | IETF standards | URI syntax; JSON Pointer as a location notation; the JSON interchange format | Nothing about schemas |

### 10.2 What governs which subject

**P9-10-01** (MUST) [D] Where this part and a consulted specification address the same subject and do not conflict, an implementation MUST satisfy both.

**P9-10-02** (MUST) [D] Where this part and a consulted specification conflict, an implementation claiming conformance to this part MUST satisfy this part and MUST record the conflict in its conformance statement.

**P9-10-03** (MUST) [D] An implementation that also claims conformance to a consulted schema language specification MUST declare which of the conflicts in §10.4 it resolves in favour of this part.

**P9-10-04** (MUST) [D] An implementation MUST NOT claim that conformance to this part implies conformance to any schema language specification, since this part constrains the registry and not the language.

### 10.3 Observations on the consulted text

**P9-10-05** (SHOULD) [P] A reader consulting JSON Schema 2020-12 on the `format` keyword SHOULD note that whether a stated format constrains an instance is a property of the implementation and its configuration rather than of the schema. **Source.** The specification classifies the keyword as an annotation under the default meta-schema, which declares the format vocabulary false, and permits an implementation to validate it only as a setting disabled by default.

**P9-10-06** (SHOULD) [P] A reader consulting the Avro specification on canonical form SHOULD note that the Parsing Canonical Form is not sufficient for compatibility determination. **Source.** The form is defined for parsing equivalence and omits the `default` and `aliases` attributes that Avro's own schema resolution consults; the extension retaining them exists outside the specification.

### 10.4 Where the specifications conflict, and how this part resolves each

| Conflict | Position A | Position B | Resolution in this part | Reason |
|---|---|---|---|---|
| Unrecognised constructs | JSON Schema treats a keyword it does not recognise as available for annotation collection rather than as an error, so an unrecognised constraint is ignored at validation | This part P9-6-24, P9-6-25: a schema containing a construct the pinned dialect does not define MUST be refused at registration | This part | Ignoring an unrecognised keyword is defensible for a language designed for extensibility and indefensible for a registry that certifies conformance. The cost of the language's rule is that a misspelling silently removes a constraint and nothing anywhere reports it. Refusal at registration is the only point at which the defect is cheap |
| Whether a stated format constrains | JSON Schema 2020-12: `format` is an annotation under the default meta-schema, whose `$vocabulary` declares the format vocabulary false, and validation of it is optional and off by default | This part P9-6-27, P9-6-28, P9-7-13: a construct that annotates in a position the submitter declares constrained MUST be recorded, and the position MUST be reported as unexamined | This part, without changing the language's semantics | The language's position is a reasonable answer to an interoperability problem. It is not a reasonable basis for reporting an instance valid. This part does not require the keyword to assert; it requires the registry to stop claiming coverage it does not have |
| Sufficiency of one canonical form | Avro: the Parsing Canonical Form defines sameness for readers and discards `doc`, `default` and `aliases` | This part P9-3-13, P9-6-21: three digests are required, and the compatibility form MUST retain every attribute the rule set consults | This part | Avro's own schema resolution consults `default` and `aliases`, which its canonical form discards. The specification is internally consistent only because it does not use the canonical form for compatibility. A registry that does must not inherit the omission |
| Where compatibility is configured | Widely deployed registry practice: the compatibility mode is a configuration of the subject, defaulting to backward and non transitive | This part P9-3-27, P9-6-49: a compatibility assertion is a record about an ordered version pair under a named rule set, and a subject carries a policy rather than a verdict | This part | A mode on a subject is a policy for future determinations. Storing it in the place where a fact belongs produces the belief that the subject is compatible, which is not a proposition with a truth value |
| Transitivity | Widely deployed registry practice: the default mode checks only against the latest version, and the documentation states that adjacent compatibility does not entail transitive compatibility | This part P9-6-56: a transitive verdict MUST NOT be inferred from adjacent verdicts, and every pair in scope MUST be determined | This part, which agrees with the vendor's documented caveat and departs from the default it ships | The default is defensible for a system whose readers are always current. It is not defensible where any reader may encounter any prior version, which is why P9-6-59 ties the requirement to the declared replay expectation rather than imposing transitivity everywhere |
| Bypassing a determination | Widely deployed registry practice: compatibility checking can be disabled by setting the mode to NONE, including temporarily in order to register a version that would otherwise be refused | This part P9-3-56, P9-3-60: a bypass MUST be a waiver with an authoriser, a reason, an expiry, named affected participants and a referenced remediation | This part | A configuration change records that checking was off. A waiver records who accepted which risk, for whom, and until when. The information content of the two is not comparable |
| Versioning of a referenced artifact | JSON Schema resolves a reference by URI, with retrieval of a remote target permitted at evaluation time | This part P9-6-16, P9-6-17: no reference MUST be resolved by network retrieval at validation time, and every reference MUST resolve to a registered version | This part | A schema whose meaning depends on what a URL serves at the moment of validation cannot support a reproducible validation record, and the record cannot say which schema was applied |

### 10.5 What none of the consulted specifications supplies

**P9-10-07** (MUST) [D] An implementation MUST treat the following as requirements of this part alone, no consulted specification supplying them: the evaluated extent and the unexamined location cause enumeration (§7.3); the three digest identity model (§3.3); the semantic change declaration (§3.7); the participant register and population scope (§3.10, §6.8); the waiver as the only permitted bypass (§3.12); the implied deployment order recorded on an assertion (§3.6); the separation of registration status from version state (§5.1); the requirement that a schema position cite a governed definition (§12.1); the treatment of a value set member addition as a compatibility break (§6.10); and the recording of schema constrained generation on a validation record (§12.11).

---

## 11. Anti patterns

Each entry names a mechanism, states the evidence that it is a mechanism rather than a matter of taste, and states what becomes unrecoverable.

### 11.1 The unexamined valid

**Mechanism.** An instance is reported valid. Part of it was never examined by any assertion, because the schema declares open content at that position, or the only construct applying to it annotates rather than asserts, or the construct was unrecognised and ignored, or a wildcard's processing mode did not require validation.

**Evidence.** Each mechanism is specified behaviour. JSON Schema 2020-12 declares the format vocabulary false in the default meta-schema and states that by default the keyword does not perform validation. JSON Schema treats unrecognised keywords as annotation candidates rather than errors. W3C XML Schema provides lax and skip wildcard processing modes. Nothing in any consulted specification requires the unexamined portion to be reported.

**Consequence.** The organisation believes it has a validating boundary. It has a boundary that validates what it happens to name. The belief is unfalsifiable from the record, because the record contains a boolean.

**P9-11-01** (MUST) [D] The registry MUST report the evaluated extent with every validation outcome.

### 11.2 The misspelled constraint

**Mechanism.** A schema author writes a constraint whose keyword the pinned dialect does not define, through a typographical error, through copying from a different dialect, or through use of a custom construct. The constraint is ignored and the schema is registered.

**Evidence.** JSON Schema's treatment of unknown keywords is to collect them as annotations, and 2020-12 requires implementations collecting annotations to include unknown keywords in verbose output. Its validation specification states that implementations MAY support custom format attributes and that schema authors SHALL NOT expect peer support for them absent agreement between parties.

**Consequence.** The schema says something it does not do. Every reader of the schema, human or machine, believes a constraint is enforced. The instance that violates it validates.

**P9-11-02** (MUST) [D] The registry MUST refuse a schema version containing a construct the pinned dialect does not define.

### 11.3 Identity that moves

**Mechanism.** A schema is corrected in place under the same assigned identity. The registry accepts it because the identity is a name and names can be reassigned.

**Evidence.** No consulted schema language specification forbids a schema at a given identifier from changing. JSON Schema `$id` is an identifier for reference resolution, not an immutability commitment.

**Consequence.** Every validation record citing that identity now cites something that did not perform the validation. The reproducibility set is broken silently, and a re-validation that disagrees with the record cannot be explained.

**P9-11-03** (MUST) [D] The registry MUST refuse a submission whose assigned identity exists with different literal content.

### 11.4 The live reference

**Mechanism.** A schema references a target by network location, and the target is fetched at validation time.

**Evidence.** Reference resolution by URI is the specified mechanism in JSON Schema, and nothing requires the target to have been captured.

**Consequence.** Validation is not reproducible and the record cannot state what was applied. The failure is worse when the remote target relaxes rather than tightens, because nothing fails and the loss of constraint is invisible.

**P9-11-04** (MUST NOT) [D] The registry MUST NOT resolve any reference by network retrieval at validation time.

### 11.5 The temporary bypass

**Mechanism.** A compatibility check refuses a version. The mode is set to none, the version is registered, and the mode is set back.

**Evidence.** Widely deployed registry practice documents this as a way to register an otherwise incompatible schema, and its best practice guidance describes temporarily setting the compatibility level to none for that purpose.

**Consequence.** The registry contains a version that would have been refused, and no record says so. Nobody is named as having accepted the risk, no participant is identified as exposed, and no expiry exists, so the exception is permanent by default.

**P9-11-05** (MUST) [D] The registry MUST express every bypass of a determination as a waiver carrying an authoriser, a reason, an expiry, the affected participants and a referenced remediation.

### 11.6 Compatibility as a property of a schema

**Mechanism.** The registry records a compatibility mode against a subject and reports that the subject is backward compatible.

**Evidence.** The dominant implementation stores the compatibility level as configuration on the subject, with a global default, and its check compares a candidate against the latest version under that level.

**Consequence.** A statement that has no truth value circulates as a fact. Asked whether version 7 can be read by a consumer on version 3, the registry has nothing to say, and the configured mode invites the answer yes.

**P9-11-06** (MUST) [D] The registry MUST record every compatibility verdict against an ordered version pair.

### 11.7 Semantic versioning as a compatibility statement

**Mechanism.** A version string is incremented by the significance of the change, and consumers infer compatibility from the increment.

**Evidence.** Semantic Versioning defines the increment in terms of backward compatible and breaking changes without reference to whether the party is a reader or a writer of the data. A change that is safe for readers and breaking for writers, such as making an optional field required, has no correct increment under the convention.

**Consequence.** A single ordinal is asked to carry a relation that is directional and pairwise. It cannot, so it carries whichever direction the author had in mind, unrecorded.

**P9-11-07** (MUST NOT) [D] The registry MUST NOT derive any compatibility conclusion from a version designation.

### 11.8 Enumeration extension treated as compatible

**Mechanism.** A member is added to an enumeration or to a bound value set. No schema constraint was removed, so a mechanical check reports the change compatible.

**Evidence.** In the schema pair, nothing that constrains has changed. Where the enumeration is a value set held elsewhere, the schema pair is identical.

**Consequence.** Every reader that switches on the members and treats the switch as exhaustive fails, or worse, falls through to a default branch and processes the new member as though it were something else. The failure appears in readers that were never redeployed.

**P9-11-08** (MUST) [D] The registry MUST record the addition of a member to an enumeration or to a value set bound at strength `required` as a break in compatibility for readers that enumerate members.

### 11.9 Absence and null as one condition

**Mechanism.** The schema, or the language, represents a position that may be absent and a position that may hold null through one construct, and the registry records one condition.

**Evidence.** Schema languages differ in whether they distinguish the two, and several instance formats permit both. No consulted specification requires the difference in meaning to be declared.

**Consequence.** Two facts with different meanings, being that nothing was said and that the value is known to be nothing, become one. Downstream, absent is read as null or null as absent, and no compatibility check detects a change from one to the other.

**P9-11-09** (MUST) [D] The registry MUST record separately whether a position may be absent and whether it may be null.

### 11.10 Ambiguous alternation

**Mechanism.** A schema offers several alternatives at one position, more than one of which matches a given instance, and the validator resolves by taking the first match.

**Evidence.** Avro resolves a writer's schema against the first schema in the reader's union that matches, and signals an error only if none match, so the case of several matches resolves silently. W3C XML Schema addresses the analogous hazard by imposing a deterministic content model constraint, which RELAX NG does not impose.

**Consequence.** The instance is interpreted under one alternative by one reader and under another by a reader whose alternatives are ordered differently. Both report valid, and they disagree about what the instance says.

**P9-11-10** (MUST) [D] The registry MUST report an ambiguity finding where more than one alternative at a position matched.

### 11.11 The registry that does not know its participants

**Mechanism.** The registry holds schemas and versions and no record of who reads or writes them.

**Evidence.** No consulted specification and no consulted practice requires a participant register. The dominant implementation groups versions by subject without recording holders.

**Consequence.** Every question that matters is unanswerable: whether a change can be made, which parties must move first, and which parties a waiver exposes. The registry can determine compatibility and cannot determine safety.

**P9-11-11** (MUST) [D] The registry MUST maintain a participant register for every published contract version.

### 11.12 The discarded report

**Mechanism.** Validation produces a structured report and the caller retains only whether it passed.

**Evidence.** Structured validation report formats exist and are specified: Schematron carries a validation report vocabulary, SHACL defines a validation result with severity and path, W3C XML Schema exposes the post schema validation infoset, and JSON Schema defines output formats. Retention is nowhere required.

**Consequence.** The findings that were warnings are lost, the extent is lost, and the annotations are lost. When the same instance later causes a defect, there is no record of what was known about it at the boundary.

**P9-11-12** (MUST) [D] The registry MUST retain the findings, the evaluated extent and the annotation collection state of every validation.

### 11.13 Documentation as the carrier of meaning

**Mechanism.** The normative meaning of a field lives in the schema's description text, and the canonical form used for identity discards it.

**Evidence.** Avro states that `doc` fields are ignored for the purposes of schema resolution and may be dropped at serialisation, and its Parsing Canonical Form discards them. Two schemas whose documentation states opposite meanings can therefore share a canonical digest.

**Consequence.** The only statement of what a field means is in the part of the artifact the registry treats as insignificant. A change of meaning with no change of structure produces no event anywhere.

**P9-11-13** (MUST) [D] The registry MUST require every position carrying a governed term to cite its `Part 4` definition rather than rely on documentation text.

### 11.14 The schema as an export of internal representation

**Mechanism.** A published schema is generated from an internal data structure, so it changes whenever the internal structure changes.

**Evidence.** No consulted specification distinguishes a schema that is a contract from a schema that is a projection of an implementation.

**Consequence.** Every internal refactoring becomes a contract change, participants are asked to absorb changes with no external meaning, and the semantic change declaration required by §3.7 becomes a formality that is always `none`, which trains everyone to ignore it.

**P9-11-14** (MUST) [D] The registry MUST treat every published schema version as a contract term and MUST require a semantic change declaration for every transition regardless of how the schema was produced.

---

## 12. Boundaries with other parts

Each boundary states what this part delegates, what it must not absorb, where a naive design conflates the two, and what the conflation costs. Each is reciprocal.

### 12.1 With `Part 4`, metadata and model repository

**Delegated.** The meaning of every governed term, its conceptual domain, its lineage and the impact analysis of a change to it.

**Must not absorb.** Meaning. A schema states that a position holds a string of a given form; it does not state what the string denotes.

**Retained.** The structural contract, and the citation from each position to the definition it carries.

**The seam, stated precisely.** Two changes are possible and only one is visible to a schema comparison. A position renamed while carrying the same `Part 4` definition is a structural change with no semantic change. A position keeping its name and its type while carrying a different `Part 4` definition is a semantic change with no structural change. Every mechanical compatibility checker detects the first and none detects the second. This is why §3.7 requires a declaration and why P9-6-70 requires the declaration to be reconciled against the definition.

**Naive conflation.** The schema becomes the place where meaning is recorded, in description text, because that is where the authors are working.

**Cost.** Meaning is recorded in the part of the artifact canonicalisation discards, is versioned by the schema's version rather than by its own, and cannot be cited by anything that is not a schema.

**P9-12-01** (MUST NOT) [D] The registry MUST NOT define the meaning of any term.

**P9-12-02** (MUST) [D] Every position in a registered schema version that carries a governed term MUST cite the `Part 4` definition of that term.

**P9-12-03** (MUST) [D] The registry MUST refuse registration of a position carrying a governed term with no cited definition, with the outcome `definition_uncited`.

**P9-12-04** (MUST) [D] The registry MUST report a semantic change declared at a position whose cited definition did not change as requiring reconciliation.

**P9-12-05** (MUST) [D] The registry MUST expose, for every `Part 4` definition, the set of schema versions and positions citing it, so that `Part 4` can perform impact analysis.

### 12.2 With `Part 2`, business rules engine

**Delegated.** Every constraint whose truth is not determined by the instance alone.

**Must not absorb.** Constraint evaluation requiring external facts.

**The boundary, stated as a test.** If the truth of the constraint is determined by the instance and the pinned schema and closure alone, it belongs here. If its truth requires any fact not in the instance, it belongs to `Part 2`. A constraint that two fields of one document must not both be present is decidable from the instance and is this part's. A constraint that a code must be a member of a value set is not, and is delegated under §12.6. A constraint that a date must not be in the future is not, because the present is not in the instance.

**Naive conflation.** Schema languages provide assertion mechanisms, so the co-occurrence constraint and the value set constraint are both written as schema assertions and both evaluated by the validator.

**Cost.** The second silently becomes a constraint over whatever the validator can reach, evaluated without a pinned value set version and without a verdict vocabulary that admits a non result. It reports false where it should report undecidable.

**P9-12-06** (MUST NOT) [D] The registry MUST NOT evaluate a constraint requiring a fact outside the instance.

**P9-12-07** (MUST) [D] The registry MUST refuse at registration a schema construct requiring a fact outside the instance.

**P9-12-08** (MUST) [D] The registry MUST accept the full verdict vocabulary of `Part 2` including every non verdict for constraints it delegates.

**P9-12-09** (MUST NOT) [D] The registry MUST NOT report a delegated constraint's non verdict as a schema violation.

### 12.3 With `Part 10`, reference and master data management

**Delegated.** The membership of every code system and value set, and the versioning of both.

**Must not absorb.** Membership.

**Retained.** The binding: which position draws from which value set version, at which strength.

**Naive conflation.** The permitted values are enumerated in the schema, because the schema language supports enumeration and because inlining removes a dependency.

**Cost.** The value set exists twice. Adding a member requires a schema release, so it is done in the value set alone and the two diverge; or it is done in both, and the schema change is reported compatible while every reader that enumerates members breaks.

**P9-12-10** (MUST NOT) [D] The registry MUST NOT hold the membership of any value set.

**P9-12-11** (MUST) [D] The registry MUST hold a pinned value set version and a declared strength for every governed enumeration position.

**P9-12-12** (MUST) [D] The registry MUST report divergence between inlined members and the pinned value set version.

**P9-12-13** (MUST) [D] The registry MUST obtain every membership determination from `Part 10` at validation time and MUST record it as a binding finding rather than a schema finding.

### 12.4 With `Part 1`, controlled documents and records management

**Delegated.** Approval, effective date, supersession as a document, retention, disposition and point in time citation of every schema version and contract version as a document.

**Must not absorb.** Document lifecycle.

**Retained.** The registration status and version state axes, which are about the item's standing in the registry and not about its standing as a document.

**Naive conflation.** The registry implements its own approval and effective dating, because publication needs both.

**Cost.** A schema version has two effective dates that disagree, and the question of which version of a contract was in force on a given date has two answers.

**P9-12-14** (MUST NOT) [D] The registry MUST NOT govern the approval or effective date of a schema version or contract version.

**P9-12-15** (MUST) [D] Every published schema version and contract version MUST carry a `Part 1` document identity.

**P9-12-16** (MUST) [D] The registry MUST treat every validation record, compatibility assertion and waiver as a record in the `Part 1` sense, being evidence of an act and not revisable.

**P9-12-17** (MUST) [D] The registry MUST resolve a citation to a schema version to the version in force at the cited instant and MUST NOT resolve it to the current version.

### 12.5 With `Part 11`, content addressed artifact store

**Delegated.** The bytes of every registered artifact, their addressing, deduplication and retrieval.

**Must not absorb.** The bytes.

**Retained.** The registration, the identities derived from the content, and the reference closure.

**Naive conflation.** The schema text is stored in the registry's own records, because it is small and because the registry must parse it anyway.

**Cost.** The registry becomes a second artifact store with its own integrity story, and the same schema text stored under two identities exists twice with no relation recorded between them.

**P9-12-18** (MUST NOT) [D] The registry MUST NOT store artifact bytes.

**P9-12-19** (MUST) [D] The registry MUST hold the content address of every registered artifact.

**P9-12-20** (MUST) [D] Where a content address ceases to resolve, the registry MUST report every dependent validation as `closure_unresolvable` and MUST NOT delete the registration.

### 12.6 With `Part 3`, provenance and audit ledger

**Delegated.** The ledger and the reconstruction of a chain of reasoning across components.

**Must not absorb.** The role of system of record for reconstruction.

**Naive conflation.** The registry's validation records are treated as the audit record, because they contain the findings.

**Cost.** A determination that relied on a validation cannot be reconstructed, because the validation is here, the rule verdicts are in `Part 2`, the human act is in `Part 8` and the definitions are in `Part 4`.

**P9-12-21** (MUST) [D] The registry MUST emit every event in §8.1 to `Part 3`.

**P9-12-22** (MUST NOT) [D] The registry MUST NOT represent its own records as the audit record of a determination.

**P9-12-23** (MUST) [D] The registry MUST own the validation record as the authoritative statement of what was validated and with what result, and `Part 3` MUST own the evidentiary chain in which that record participates.

### 12.7 With `Part 6`, workflow and process orchestration, and `Part 8`, human task and case management

**Delegated.** The runtime that carries payloads, and the decision of what to do when an instance does not conform.

**Must not absorb.** Any action in consequence of a finding.

**Naive conflation.** The registry rejects, quarantines or routes non conforming instances, because it is the component that detected the problem.

**Cost.** A policy decision about what an organisation does with defective input is made in a component with no view of the work, no case, no participant and no authority to decide.

**P9-12-24** (MUST NOT) [D] The registry MUST NOT reject, route, retry or quarantine an instance.

**P9-12-25** (MUST) [D] The registry MUST return the outcome, findings and evaluated extent to the caller and MUST leave the consequence to the caller.

**P9-12-26** (MUST) [D] The registry MUST supply the pinned schema version and dialect that `Part 8` records in a presentation pin, and MUST NOT resolve such a citation to a later version.

**P9-12-27** (MUST) [D] Every interaction of a published contract version that can fail MUST declare at least one error schema binding, and the registry MUST refuse publication where an interaction declares none and is not declared infallible.

### 12.8 With `Part 7`, policy decision point and authorisation

**Delegated.** Every decision on whether a party may register, progress, publish, deprecate, retire, waive or validate.

**Must not absorb.** Authorisation.

**Naive conflation.** The registry enforces who may publish, because publication is its own operation.

**Cost.** Policy lives in two places and the copy in the registry is invisible to policy review.

**P9-12-28** (MUST NOT) [D] The registry MUST NOT render an authorisation decision.

**P9-12-29** (MUST) [D] The registry MUST obtain an authorisation decision at the instant of every operation that changes registry state.

**P9-12-30** (MUST) [D] The registry MUST supply the registration status, version state and stewardship facts that `Part 7` requires as attributes, and MUST NOT permit `Part 7` to hold a second copy of them.

### 12.9 With `Part 5`, decision engine

**Delegated.** Any selection among candidate schema versions made by governed algorithm.

**Must not absorb.** Selection logic.

**Naive conflation.** The registry resolves a reference to a subject by choosing the latest published version, because that is usually what the caller wants.

**Cost.** A governed choice with consequences for compatibility is made by unversioned code with no decision record, and the resolution differs between callers and over time.

**P9-12-31** (MUST NOT) [D] The registry MUST NOT resolve a reference that names a subject without a version, and MUST refuse such a reference at registration.

**P9-12-32** (MUST) [D] Where a caller requires a version to be selected from several, the registry MUST obtain the selection from `Part 5` and MUST record the decision reference.

**P9-12-33** (MAY) [D] The registry MAY return the set of candidate versions with their states, which is not a selection.

### 12.10 With `Part 12`, conformance and assurance harness

**Delegated.** The verification of this component's claims about itself, including the verification that its evaluated extent computation is correct.

**Must not absorb.** Self assessment presented as assurance.

**Naive conflation.** The registry reports that its coverage computation is complete, because it computed it.

**Cost.** The one claim on which every other claim of this part rests is verified by its author.

**P9-12-34** (MUST) [D] The registry MUST expose the state required to verify every clause of this part that is externally observable.

**P9-12-35** (MUST NOT) [D] The registry MUST NOT report its own conformance to this part as assurance.

**P9-12-36** (MUST) [D] The registry MUST expose its evaluated extent computation in a form `Part 12` can test against instances of known coverage.

### 12.11 With `Part 13`, model invocation and agent execution

**Delegated.** The invocation record of any model that produced or consumed an instance.

**Must not absorb.** Any inference that a valid instance is a correct one.

**The boundary, stated positively.** Validation establishes that an instance conforms to a structure. It establishes nothing about whether the content is true. Where an instance was produced under schema constrained generation, validation establishes even less, because conformance was guaranteed by the generation mechanism rather than achieved by the producer.

**Naive conflation.** A model produced output, the output validated, and the validation is cited as evidence that the output is fit for use.

**Cost.** The strongest available evidence of correctness turns out to be a tautology. Constrained generation cannot produce a non conforming instance, so the validation could not have failed, so its passing carries no information.

**P9-12-37** (MUST) [D] The registry MUST record on every validation record whether the instance was produced under schema constrained generation, or that the fact is unknown.

**P9-12-38** (MUST NOT) [D] The registry MUST NOT report a validation of an instance produced under schema constrained generation as independent evidence of conformance.

**P9-12-39** (MUST NOT) [D] The registry MUST NOT represent conformance as correctness in any interface or projection.

**P9-12-40** (MUST) [D] Where an instance produced by a model is validated, the registry MUST record the `Part 13` invocation reference supplied by the caller, or MUST record that none was supplied.

### 12.12 With `Part 0`, system composition

**P9-12-41** (MUST) [D] The registry MUST treat the authority assignments of `Part 0` as governing, and where this part appears to claim authority over a fact `Part 0` assigns elsewhere, `Part 0` MUST prevail.

**P9-12-42** (MUST) [D] The registry MUST declare, for every fact it owns, that it is the sole authority, being: schema version identity and content identity; dialect and vocabulary registration; registration status and version state; reference closure; compatibility assertion; semantic change declaration; contract version and binding; participant registration; waiver; and validation record.

**P9-12-43** (MUST NOT) [D] The registry MUST NOT claim authority over: the meaning of a term; value set membership; artifact bytes; document approval and retention; authorisation decisions; rule verdicts; party identity; work or case state; or invocation records.

### 12.13 Invariants at the boundaries

**P9-12-44** (MUST) [D] At every instant, every schema version MUST carry exactly one registration status and exactly one version state.

**P9-12-45** (MUST) [D] At every instant, every schema version MUST carry exactly three digests, each naming the canonicaliser version that produced it.

**P9-12-46** (MUST) [D] At every instant, no two schema versions MUST share an assigned identity with differing literal digests.

**P9-12-47** (MUST) [D] At every instant, every published schema version MUST have exactly one semantic change declaration for the transition from its predecessor, or MUST be the first version in its subject.

**P9-12-48** (MUST) [D] At every instant, every published schema version that failed a required determination MUST have exactly one waiver in state `active`.

**P9-12-49** (MUST) [D] At every instant, every validation record MUST carry a complete reproducibility set and exactly one evaluated extent.

**P9-12-50** (MUST) [D] At every instant, every reference in the closure of a published schema version MUST resolve to a registered schema version, and none MUST resolve to a network location.

**P9-12-51** (MUST) [D] At every instant, every binding of a published contract version MUST name a schema version by intrinsic identity, and none MUST name a subject alone.

**P9-12-52** (MUST) [D] At every instant, every published contract version MUST name at least one participant registration.

---

## 13. What could not be established

### 13.1 Questions left open by the consulted specifications

**The standards status of the JSON Schema family.** The dialect this part cites most often is styled a draft, dated 2020-12, published by the JSON Schema project rather than by a standards body. An IETF working group document carrying the designation `draft-ietf-jsonschema-json-schema-01` exists, which indicates that the family is being progressed on the IETF standards track. This part could not establish the current state of that work, whether the working group document is substantively identical to the 2020-12 dialect, or what an implementer should treat as current. Secondary sources state that a forthcoming version will disallow unknown keywords and will make `format` assert by default, which if correct would remove two of the four mechanisms in §1.3; this part could not verify either statement against a specification document, and §11.1 and §11.2 are written so that they remain correct whichever way the question resolves.

**Whether the Avro project adopted a resolution canonical form.** The Parsing Canonical Form omits the `default` and `aliases` attributes, which Avro's own schema resolution consults. Third party work defined a resolution canonical form retaining them, and a project issue proposing to add such a form to the specification and implementation was raised. This part could not establish whether any such form was adopted into the Avro specification. P9-6-21 states the requirement on this part's own authority.

**The full enumeration of ISO/IEC 11179 registration statuses.** This part read the descriptions of Candidate and Recorded and the progression conditions for Qualified and above, and read a national registration authority's published usage of Preferred Standard, Superseded and Retired. Whether the fourth edition's normative enumeration is exactly the eight statuses used in §5.2, and whether it names a status this part has omitted, could not be established, because the standard is paywalled and only its introductory material and clause 4.3.3.1.4 were available. The mapping in §5.2 is therefore an adaptation and is marked as this part's own where its clauses are marked D.

**Whether Schematron and SHACL severity models are reconcilable.** Schematron carries a role attribute and distinguishes assert from report; SHACL defines three severities. This part adopted three severities in §3.11. Whether the two models are formally reconcilable, and whether a Schematron role maps onto a SHACL severity without loss, could not be established.

**Whether the dominant registry implementation's compatibility rules are specified anywhere normatively.** The seven modes, their transitivity and their deployment order implications are documented in vendor documentation. The rule sets themselves, per schema language, are implemented rather than specified, so two implementations claiming the same mode may compute different verdicts. This part could not establish whether any normative specification of those rule sets exists, which is why P9-3-28 requires the rule set to be pinned by identity rather than named by mode.

**Whether any specification defines an evaluated extent.** JSON Schema defines output formats including a verbose form that carries annotations for unknown keywords, and W3C XML Schema exposes the post schema validation infoset, both of which carry information from which coverage might be computed. This part could not establish that any specification defines coverage, requires it to be reported, or names the causes by which a location goes unexamined. §7.3 is this part's own.

### 13.2 Requirements this part invents, and why

| Subject | Clauses | Why no specification supplies it |
|---|---|---|
| Evaluated extent and unexamined location causes | P9-3-50, P9-6-34, P9-6-35, P9-7-04 to P9-7-17 | Every consulted schema language defines validity as a property of the instance under the schema. None defines the complement, being what the schema did not reach, so no implementation is required to report it |
| Three digests over three canonical forms | P9-3-13 to P9-3-20, P9-6-21 | Avro defines one canonical form for one purpose and its own resolution rules consult attributes that form discards |
| Canonicaliser versioning | P9-3-14, P9-6-18, P9-6-19 | Fingerprints are specified; the versioning of the rules producing them is not |
| Semantic change declaration | P9-3-33 to P9-3-37, P9-6-68 to P9-6-70 | Compatibility is computed mechanically in every consulted source. No source requires a change in meaning to be declared, and no mechanical check can detect one |
| Participant register and population scope | P9-3-46 to P9-3-49, P9-6-61 to P9-6-65 | No consulted source records who holds which version, so no consulted source can answer whether a change is safe |
| Waiver as the only bypass | P9-3-56 to P9-3-60 | The dominant practice bypasses by configuration, which leaves no accountable record |
| Implied deployment order on the assertion | P9-3-31, P9-6-51 | The implication is documented in prose; nothing requires it to travel with the verdict |
| Registration status separated from version state | P9-5-01, P9-5-02 | ISO/IEC 11179 supplies one axis for registered items generally; no source supplies both for a schema |
| Refusal of unrecognised constructs at registration | P9-6-24, P9-6-25 | The consulted language requires the opposite behaviour at validation |
| Prohibition of network reference resolution | P9-6-16, P9-6-17 | Reference resolution by URI is the specified mechanism and capture is nowhere required |
| Value set member addition as a compatibility break | P9-6-74, P9-12-12 | The schema pair is unchanged, so no consulted rule set examines it |
| Recording of schema constrained generation | P9-12-37, P9-12-38 | The consulted specifications predate the question |
| Contract as a first class registered artifact with declared guarantees | P9-3-38 to P9-3-41 | Interface description formats describe payloads; none requires ordering, delivery, idempotence and replay to be declared as contract terms bound to schema versions |

### 13.3 Questions this part does not answer

**What rule set is correct for a given schema language.** This part requires the rule set to be identified, pinned and recorded. It does not specify any rule set, because specifying compatibility rules for a schema language is the work of that language's specification, and doing it here would bind implementations to this part's reading of a language it does not own.

**What coverage is sufficient.** §7.3 requires the extent to be reported. It does not state a threshold below which an instance should be treated as unvalidated, because the sufficient extent depends on what the consumer relies on, which this component does not know. This is the most consequential thing this part deliberately leaves open.

**How to compute the evaluated extent for every schema language.** The requirement is stated at the level of locations and causes. The computation for a language with conditional subschemas, dynamic references and cyclic closures was not worked through, and P9-6-47 and P9-6-48 admit bounds that may leave the extent itself partial. Whether the extent can always be computed exactly is unresolved.

**Whether a semantic change declaration can be trusted.** §3.7 requires an accountable party to declare it. Nothing in this part can detect a declaration of `none` that is wrong, and P9-6-70's reconciliation against `Part 4` catches only the case where the definition also changed. A false declaration of `none` is the residual risk of this design and it is not mitigated here.

**How long a validation record should be retained relative to the instance it concerns.** §8.4 subjects both to `Part 1`. Whether a validation record outliving its instance retains evidentiary value was not established.

**Whether a contract should be able to bind a subject rather than a version.** P9-12-31 forbids it, on the ground that resolution would be a governed selection. Whether there are interaction patterns for which version pinning is impracticable was not analysed.

### 13.4 Sources this part could not obtain

**ISO/IEC 11179, all parts.** Paywalled. This part read the abstract and scope statements of Part 6 in its 2005, 2015 and 2023 editions, the publicly quoted text of clause 4.3.3.1.4 and the progression conditions, and the front matter of the 2023 edition establishing that it cancels and replaces the 2015 edition. The remainder, including the normative enumeration of registration statuses and the whole of the Part 3 metamodel, was not read. Clauses in §5.2 marked S cite only text that was read; the enumeration itself is marked D.

**ISO/IEC 19757-2 and 19757-3.** Paywalled. RELAX NG and Schematron are cited from their published descriptions and from general knowledge of their models. No clause depends on a section number in either, and the assert against report distinction cited at P9-6-37 was not verified against the standard text.

**W3C XML Schema 1.0 and 1.1.** Not consulted directly in this session. Cited for wildcard processing modes, assertions, conditional type assignment, redefinition, overriding and the post schema validation infoset. Section numbers are not cited. A reader relying on P9-7-12 should verify the processing mode semantics against the Structures specification.

**W3C SHACL.** Not consulted directly. Cited for its three severities and for focus node and result path. No clause depends on its section numbering.

**HL7 FHIR.** Not consulted directly in this session. Cited for canonical URL with business version, binding strength and the structured outcome resource. No clause depends on its section numbering.

**The JSON Schema specification documents.** Read in substantial part through the published validation specification text on the format vocabulary and custom format attributes, the 2020-12 release notes, and the core specification's treatment of conditional keywords. The core specification's sections on identity, base URI resolution and output formats were not read in full; citations to bundling, dynamic references and output formats rest on the release notes and on secondary reference documentation rather than on the specification text.

**The Avro specification.** Read in part: the canonical form and fingerprint sections and the schema resolution rules were read in the specification's own words, including the property claimed for the Parsing Canonical Form and the treatment of `doc`. The full transformation list defining the canonical form was not read.

**Protocol buffer specifications.** Not consulted. Cited only for field numbering and unknown field retention, and no clause depends on either.

**Semantic Versioning 2.0.0.** Not consulted in this session. Cited for the structure of its increment rule. §11.7 rests on the structure of the convention rather than on its text.

**Vendor documentation of the dominant registry implementation.** Read in substantial part: the compatibility type enumeration, the default and its non transitivity, the transitive example, the deployment order implications, the format dependence of the rules, the normalisation parameter and the practice of temporarily setting compatibility to none were all read in the vendor's own words. This is vendor specification and not a standard, and every clause resting on it is marked P.
