# KAIROS STD 003 Part 8, human task and case management

**Status:** version 1, Proposed.
**Part:** `KAIROS STD 003 Part 8`. Cite as `KAIROS STD 003 Part 8 §n` for a section and `KAIROS STD 003 Part 8 P8-n-nn` for a clause.
**Component:** the human task and case management component of an enterprise application that executes governed work.

## Reading this part

**Normative language.** The key words MUST, MUST NOT, SHOULD, SHOULD NOT and MAY in this part are to be interpreted as described in RFC 2119 (Bradner, IETF RFC 2119, March 1997). Every requirement of this part is a numbered clause. Every clause carries exactly one modality and states one testable proposition. Prose that carries no clause identifier is explanatory and imposes no requirement.

**Clause identifiers.** Clauses are identified `P8-<section>-<ordinal>`. Identifiers are permanent and are never reused or renumbered. A clause withdrawn in a later version retains its identifier and is marked withdrawn.

**Basis markers.** Every clause carries a basis marker recording what the clause rests on. This is not a modality and does not weaken the requirement; a clause marked D binds exactly as hard as one marked S. The marker exists so that a reader can tell the difference between a requirement this part inherits and a requirement this part invents.

| Marker | Meaning |
|---|---|
| S | The clause's subject is treated in the text of a named specification, cited at the clause under **Source.** The clause may adopt that treatment or depart from it; where it departs it says so, and the conflict is recorded in §10.4. The marker records that a reader can go to a source, not that this part agrees with what is there. |
| P | Rests on published literature or on observed practice rather than on specification text, cited at the clause under **Source.** |
| D | Decided by this part. No consulted specification treats the subject. Every D clause on a subject where a reader might expect specification support is listed in §13.2. |

**Two drafting conventions.** Both are stated because both bear on whether a clause is a single testable statement, which is the property the clause form exists to guarantee.

*Paired prohibitions.* A clause may state a requirement together with the direct negation of that same requirement, where one test decides both, as in a clause that requires two conditions to be distinguished and prohibits their representation as one value. A clause MUST NOT join two requirements that need two tests. The number of clauses carrying a paired prohibition is derived and reported in the clause index summary, so that a reader can audit the convention rather than take it on trust.

*Ordinals are not everywhere ascending.* Clause ordinals are permanent from first issue. Where drafting split a clause that carried more than one requirement, the split off requirements took the next free ordinals in their section and were placed beside the clause they came from. Ordinals within a section are therefore dense and complete, but not everywhere in ascending reading order.

**Conformance target.** The conformance target of this part is a *work and case manager*: any implementation that accepts case definitions and work item definitions and executes the semantics defined here. Where a clause constrains something other than the work and case manager, the clause names its subject.

**Storage neutrality.** This part specifies records, not tables. Where §3 constrains mutability it does so to make the record evidentiary, not to mandate a storage technology.

**Out of scope by construction.** This part does not assess any implementation. It does not describe any system. It is written as a measuring stick.

---

## Clause index

This index is derived from the body of this part by extracting every line matching the clause form `**P8-<section>-<ordinal>** (<modality>) [<basis>]`. Every count below is therefore derivable from the body and is not asserted. The grain of every count is one clause, being one line of clause form. Section 13 carries no clauses by construction, since it reports rather than requires.

### Summary by section

| § | Section | Clauses | MUST | MUST NOT | SHOULD | SHOULD NOT | MAY | S | P | D | Paired |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Scope and responsibilities | 27 | 11 | 14 | — | — | 2 | — | — | 27 | 14 |
| 2 | Terminology | 6 | 1 | 5 | — | — | — | — | — | 6 | 1 |
| 3 | Data model | 71 | 52 | 17 | 2 | — | — | 6 | — | 65 | 41 |
| 4 | Interfaces | 47 | 33 | 12 | 2 | — | — | 3 | — | 44 | 29 |
| 5 | State model | 30 | 23 | 7 | — | — | — | 4 | — | 26 | 18 |
| 6 | Execution semantics | 104 | 86 | 17 | — | — | 1 | 7 | 4 | 93 | 53 |
| 7 | Outcome and failure taxonomy | 37 | 27 | 10 | — | — | — | — | — | 37 | 21 |
| 8 | Observability and the audit record | 35 | 30 | 4 | 1 | — | — | — | — | 35 | 3 |
| 9 | Extension model | 17 | 11 | 6 | — | — | — | 3 | — | 14 | 8 |
| 10 | Standards and specifications | 6 | 4 | — | 2 | — | — | — | 2 | 4 | 1 |
| 11 | Anti patterns | 14 | 6 | 8 | — | — | — | — | — | 14 | 3 |
| 12 | Boundaries with other parts | 51 | 32 | 18 | — | — | 1 | 1 | — | 50 | 14 |
| 13 | What could not be established | 0 | — | — | — | — | — | — | — | — | — |
| **Total** | | **445** | **316** | **118** | **7** | **0** | **4** | **24** | **6** | **415** | **206** |

**Derived counts, at the grain of one clause.** This part carries 445 clauses across 12 clause bearing sections. Of these, 316 are MUST, 118 are MUST NOT, 7 are SHOULD, 0 are SHOULD NOT and 4 are MAY. By basis, 24 rest on cited specification text, 6 on cited literature or practice, and 415 are decided by this part with no consulted specification treating the subject. 206 clauses carry a paired prohibition under the convention stated above, and no clause carries more than one requirement needing more than one test. The ratio of D to S is a property of the subject rather than of the drafting: the consulted specifications between them supply an assignment model without a case and a case model without an assignment model, and neither supplies an evidentiary or a non result model at all, which §10.5 states and §13.2 itemises.

### Clauses

Subject labels below are machine extracted from the opening of each clause and are an index aid, not normative text. The clause itself governs.

**§1. Scope and responsibilities**

| Clause | Modality | Basis | Subject |
|---|---|---|---|
| P8-1-01 | MUST | D | The component MUST own the work item as a durable record, from the moment the… |
| P8-1-02 | MUST | D | The component MUST own the case as a first class entity with its own… |
| P8-1-03 | MUST | D | The component MUST own the derivation of the candidate set for a work item,… |
| P8-1-04 | MUST | D | The component MUST own the assignment state of a work item, being which… |
| P8-1-05 | MUST | D | The component MUST own the gate, being the condition under which a work item… |
| P8-1-06 | MUST | D | The component MUST own the resolution of deferred choice, being the record of… |
| P8-1-07 | MUST | D | The component MUST own the participation record of a case, being the complete… |
| P8-1-08 | MUST | D | The component MUST own the case file, being the set of typed slots scoped to… |
| P8-1-09 | MUST | D | The component MUST own the planning act, being the record of a person adding… |
| P8-1-10 | MUST | D | The component MUST own the presentation pin, being the record of what was… |
| P8-1-11 | MUST | D | The component MUST own the milestone, being a named achieved state of a case… |
| P8-1-12 | MUST NOT | D | The component MUST NOT evaluate the declarative condition of a gate itself,… |
| P8-1-13 | MUST NOT | D | The component MUST NOT select one outcome from several candidate outcomes by… |
| P8-1-14 | MUST NOT | D | The component MUST NOT render an authorisation decision on whether a party… |
| P8-1-15 | MUST NOT | D | The component MUST NOT maintain its own copy of the organisational model, and… |
| P8-1-16 | MUST NOT | D | The component MUST NOT define the control flow that sequences work across a… |
| P8-1-17 | MUST NOT | D | The component MUST NOT define or version the schema of any payload it… |
| P8-1-18 | MUST NOT | D | The component MUST NOT version the definitions from which cases and work… |
| P8-1-19 | MUST NOT | D | The component MUST NOT store the bytes of any attachment, and MUST hold only… |
| P8-1-20 | MUST NOT | D | The component MUST NOT hold the authoritative text of any instruction,… |
| P8-1-21 | MUST NOT | D | The component MUST NOT be the audit ledger, and MUST emit its events to the… |
| P8-1-22 | MUST NOT | D | The component MUST NOT represent an act performed by a non-human actor as an… |
| P8-1-23 | MUST NOT | D | The component MUST NOT verify its own conformance claims, and MUST expose the… |
| P8-1-24 | MUST NOT | D | The component MUST NOT act as a general purpose data store for facts whose… |
| P8-1-25 | MAY | D | An implementation MAY support cases whose plan is entirely predefined, and… |
| P8-1-26 | MAY | D | An implementation MAY support work items that exist outside any case, and… |
| P8-1-27 | MUST NOT | D | This part MUST NOT be read as requiring a graphical notation, and no… |

**§2. Terminology**

| Clause | Modality | Basis | Subject |
|---|---|---|---|
| P8-2-01 | MUST NOT | D | This part MUST NOT define process, activity, gateway, token, or compensation,… |
| P8-2-02 | MUST NOT | D | This part MUST NOT define rule, constraint, verdict semantics, or rule set,… |
| P8-2-03 | MUST NOT | D | This part MUST NOT define policy, obligation, advice, or combining algorithm,… |
| P8-2-04 | MUST NOT | D | This part MUST NOT define decision, decision table, or decision requirement,… |
| P8-2-05 | MUST NOT | D | This part MUST NOT define document, record, version, supersession, or… |
| P8-2-06 | MUST | D | Where this part uses a term owned by another part, it MUST use that term with… |

**§3. Data model**

| Clause | Modality | Basis | Subject |
|---|---|---|---|
| P8-3-01 | MUST | D | Every case instance, work item, candidate set, gate evaluation, presentation… |
| P8-3-02 | MUST NOT | D | An identifier MUST NOT be reused after the record it identifies reaches a… |
| P8-3-03 | MUST NOT | D | An identifier MUST NOT encode any mutable property of the thing it… |
| P8-3-04 | MUST | D | A work item MUST be addressable independently of its case, so that a citation… |
| P8-3-05 | MUST | D | A case file slot MUST be addressable by a path that is stable across the life… |
| P8-3-06 | MUST | D | Where a work item is instantiated by repetition, each repetition MUST receive… |
| P8-3-07 | SHOULD | D | An identifier SHOULD be generable without coordination across deployment… |
| P8-3-08 | MUST | D | The case record MUST contain every field marked required in the table in… |
| P8-3-09 | MUST | D | definition_ref MUST be a pinned reference to the exact version of the case… |
| P8-3-10 | MUST NOT | D | The case record MUST NOT carry the current state of its work items as fields,… |
| P8-3-11 | MUST | D | Where a case is reopened, the component MUST retain the prior closed_at and… |
| P8-3-12 | MUST | D | Every closure episode record MUST carry the identifier of the party that… |
| P8-3-13 | MUST NOT | D | A case MUST NOT carry more than one active case_state at any instant. |
| P8-3-14 | MUST | D | The work item record MUST contain every field marked required in the table in… |
| P8-3-15 | MUST | S | priority MUST be an integer in the inclusive range 0 to 10 where 0 is the… |
| P8-3-16 | MUST NOT | D | holder MUST NOT be populated in any state other than allocated, reserved,… |
| P8-3-17 | MUST | D | Where holder transitions from a populated value to absent, the component MUST… |
| P8-3-18 | MUST | D | input_digest MUST be computed over a canonical form of the input payload… |
| P8-3-19 | MUST NOT | D | The work item record MUST NOT carry the input payload itself where that… |
| P8-3-20 | MUST | D | stale_since MUST be set at the instant the component observes that any pinned… |
| P8-3-21 | MUST | D | The candidate set record MUST be immutable once written, and a change of… |
| P8-3-22 | MUST | S | derivation_outcome MUST distinguish a determined empty set from a failed… |
| P8-3-23 | MUST | D | org_snapshot_ref MUST pin the state of the organisational model used in the… |
| P8-3-24 | MUST | D | Where a group reference is carried unexpanded in unresolved_group_refs, the… |
| P8-3-25 | MUST | D | Every entry in excluded MUST name the rule reference that caused the… |
| P8-3-26 | MUST | D | The component MUST record attention separately from candidacy, and MUST NOT… |
| P8-3-27 | MUST | D | may_claim MUST reflect the component's own eligibility determination and MUST… |
| P8-3-28 | MUST NOT | D | The component MUST NOT revoke attention whose basis is oversight on the… |
| P8-3-29 | MUST | D | The component MUST write a presentation pin record before accepting any act… |
| P8-3-30 | MUST | S | Every reference in a presentation pin MUST be a pinned reference resolvable… |
| P8-3-31 | MUST | D | available_outcomes MUST enumerate every outcome the acting party could have… |
| P8-3-32 | MUST | D | Where available_outcomes contains exactly one member, the component MUST… |
| P8-3-33 | MUST NOT | D | A presentation pin MUST NOT be modified after it is written, and a change in… |
| P8-3-34 | SHOULD | D | A presentation pin SHOULD carry sufficient reference for a reader to… |
| P8-3-35 | MUST | D | The completion record MUST be immutable once written, and a correction MUST… |
| P8-3-36 | MUST | D | choice_breadth MUST equal the count of members of available_outcomes in the… |
| P8-3-37 | MUST | D | authorisation_ref MUST reference the authorisation decision obtained from… |
| P8-3-38 | MUST NOT | D | The component MUST NOT write a completion record whose disposition is… |
| P8-3-39 | MUST | D | Where disposition is undecidable, the completion record MUST carry rationale… |
| P8-3-40 | MUST NOT | D | The component MUST NOT record actor_class_used as human where the act was… |
| P8-3-41 | MUST | D | Every item added to a running case plan MUST be traceable to exactly one… |
| P8-3-42 | MUST | S | applicability_verdict MUST record the verdict obtained when the applicability… |
| P8-3-43 | MUST NOT | D | A planning act record MUST NOT be deleted when the items it created are… |
| P8-3-44 | MUST | D | The case file MUST distinguish a slot that has never been populated from a… |
| P8-3-45 | MUST | D | Every case file slot MUST declare a type by reference to Part 9, and the… |
| P8-3-46 | MUST NOT | D | A case file slot MUST NOT hold a literal copy of a fact for which… |
| P8-3-47 | MUST | D | Where a slot's value is a pinned reference and the referenced object has been… |
| P8-3-48 | MUST | D | Where a slot's value is a pinned reference or content address that no longer… |
| P8-3-49 | MUST NOT | D | The component MUST NOT permit an undeclared slot to be created at runtime… |
| P8-3-50 | MUST | D | Every population, supersession and discard of a slot MUST be recorded as an… |
| P8-3-51 | MUST NOT | D | The component MUST NOT permit a slot to be read by another component as a… |
| P8-3-52 | MUST | D | A milestone achievement MUST be recorded as an event and MUST NOT be… |
| P8-3-53 | MUST | D | Where an achieved milestone is revoked, the component MUST retain the… |
| P8-3-71 | MUST | D | Every revocation of a milestone achievement MUST record the revoking party… |
| P8-3-54 | MUST | D | Every gate evaluation MUST be recorded, including evaluations that returned… |
| P8-3-55 | MUST | D | snapshot_ref MUST pin the case state read by the evaluation such that… |
| P8-3-56 | MUST NOT | S | A gate evaluation record MUST NOT record unsatisfied where the verdict… |
| P8-3-57 | MUST | D | triggering_event_id MUST identify the single event that caused the… |
| P8-3-58 | MUST | D | Every resolved deferred choice MUST produce a choice resolution record naming… |
| P8-3-59 | MUST | D | Every alternative named in alternatives and not named in taken MUST receive… |
| P8-3-60 | MUST | D | Exactly one of resolved_by and resolving_event_id MUST be present. |
| P8-3-61 | MUST | S | A case role binding MUST be scoped to one case instance and MUST NOT be read… |
| P8-3-62 | MUST | D | The component MUST retain unbound role bindings for the life of the case,… |
| P8-3-63 | MUST | D | Where a case definition declares a maximum cardinality for a role, the… |
| P8-3-64 | MUST | D | An escalation MUST NOT have the effect of performing the work, and the… |
| P8-3-65 | MUST | D | Where an escalation alters candidacy or the holder, the record MUST retain… |
| P8-3-66 | MUST NOT | D | Candidate set records, presentation pin records, completion records, gate… |
| P8-3-67 | MUST | D | Where the current value of a mutable field of a case or work item changes,… |
| P8-3-68 | MUST | D | The component MUST be implementable over a store in which no written record… |
| P8-3-69 | MUST | D | The component MUST version its own record schemas and MUST record, for every… |
| P8-3-70 | MUST NOT | D | The component MUST NOT reinterpret a record written under an earlier record… |

**§4. Interfaces**

| Clause | Modality | Basis | Subject |
|---|---|---|---|
| P8-4-01 | MUST | D | Every operation the component accepts MUST be defined in terms of the records… |
| P8-4-02 | MUST | D | Every operation that changes state MUST accept an idempotency key supplied by… |
| P8-4-03 | MUST | D | Every operation invoked with a previously seen idempotency key and different… |
| P8-4-04 | MUST | D | Every operation that expresses or records a human act MUST carry the acting… |
| P8-4-05 | MUST | D | Every operation that changes the holder, disposition or plan of a work item,… |
| P8-4-06 | MUST NOT | D | The component MUST NOT expose any operation that writes a case file slot… |
| P8-4-07 | MUST | D | Every operation MUST return exactly one outcome value from the taxonomy in… |
| P8-4-08 | MUST | D | Every rejected operation MUST be recorded with the requesting party, the… |
| P8-4-09 | MUST | D | The component MUST reject any participant operation invoked from a state not… |
| P8-4-10 | MUST | D | claim MUST be atomic with respect to every other claim on the same work item,… |
| P8-4-11 | MUST | D | decline MUST remove the declining party from the candidate set for the… |
| P8-4-12 | MUST | D | decline by the last remaining member of a candidate set MUST transition the… |
| P8-4-13 | MUST | D | report_undecidable MUST be available on every work item definition whose… |
| P8-4-14 | MUST | D | defer MUST require a resumption condition expressed as a trigger or an… |
| P8-4-15 | MUST | D | delegate MUST retain the delegating party in delegation_chain and MUST NOT… |
| P8-4-16 | MUST | S | forward MUST record the transfer of accountability, and the component MUST… |
| P8-4-17 | MUST NOT | D | set_priority MUST NOT alter any deadline, and the component MUST NOT derive a… |
| P8-4-18 | MUST | S | skip MUST be rejected where the work item definition does not declare the… |
| P8-4-19 | MUST | D | withdraw MUST record a withdrawal reason from the enumeration in §7.2.3. |
| P8-4-20 | MUST | D | repin MUST create a new presentation pin and MUST invalidate every… |
| P8-4-21 | MUST NOT | D | An administrative operation MUST NOT write a completion record. |
| P8-4-22 | MUST | S | raise_user_event MUST be restricted to the roles the case definition… |
| P8-4-23 | MUST | D | reopen_case MUST require a reason and MUST NOT be available from closed. |
| P8-4-24 | MUST NOT | D | close_case MUST NOT be legal from active or suspended, so that closure cannot… |
| P8-4-25 | MUST | D | terminate_case MUST withdraw every non terminal work item of the case with… |
| P8-4-26 | MUST | D | The component MUST expose a worklist query returning the work items on which… |
| P8-4-27 | MUST | D | The component MUST expose a point in time query returning the state of a… |
| P8-4-28 | MUST NOT | D | A query MUST NOT change any state other than a read audit record, and MUST… |
| P8-4-29 | MUST | D | Every worklist query result MUST carry the instant at which it was computed,… |
| P8-4-30 | SHOULD | D | A worklist query SHOULD be answerable without reading the payload of any work… |
| P8-4-31 | MUST | D | The component MUST emit an event for every state transition of a case, work… |
| P8-4-32 | MUST | D | Every emitted event MUST carry the identifier of the record it concerns, the… |
| P8-4-33 | MUST | D | Every emitted event MUST be delivered to Part 3 at least once, and the… |
| P8-4-34 | MUST | D | Emitted events MUST be totally ordered within a single case instance, and the… |
| P8-4-35 | MUST NOT | D | The component MUST NOT emit an event describing a state change that was not… |
| P8-4-36 | MUST | D | Where the component emits an event carrying a non result, the event MUST… |
| P8-4-37 | MUST | D | The component MUST emit a distinct event class for gate indeterminacy,… |
| P8-4-38 | SHOULD | D | The component SHOULD emit an event when a work item becomes stale, so that a… |
| P8-4-39 | MUST | D | The component MUST treat every read in the table in §4.4 as fallible, and… |
| P8-4-40 | MUST NOT | D | The component MUST NOT permit an act to proceed on the failure of an… |
| P8-4-41 | MUST NOT | D | The component MUST NOT cache a read from another component beyond the pinning… |
| P8-4-42 | MUST | D | A caller MAY assume that a synchronous operation returning a success outcome… |
| P8-4-43 | MUST NOT | D | A caller MUST NOT assume that a work item present in a worklist result is… |
| P8-4-44 | MUST NOT | D | A caller MUST NOT assume that an absent field means a false, zero or empty… |
| P8-4-45 | MUST NOT | D | A caller MUST NOT assume that a gate that has not fired is a gate that… |
| P8-4-46 | MUST | D | A caller MAY assume that a completion record, once returned, is immutable and… |
| P8-4-47 | MUST NOT | D | A caller MUST NOT assume any ordering between events of different case… |

**§5. State model**

| Clause | Modality | Basis | Subject |
|---|---|---|---|
| P8-5-01 | MUST | D | Every state named in this part MUST appear in a state table in this section… |
| P8-5-02 | MUST NOT | D | The component MUST NOT admit a transition not listed in this section, and… |
| P8-5-03 | MUST | D | Every transition MUST record its trigger, the instant, the acting party where… |
| P8-5-04 | MUST NOT | D | The component MUST NOT represent two states of one entity as simultaneously… |
| P8-5-05 | MUST | D | Where a transition is refused because it is illegal, the refusal MUST be… |
| P8-5-06 | MUST | D | closed MUST be the only terminal state of a case instance, and the component… |
| P8-5-07 | MUST | D | The component MUST distinguish completed from terminated and MUST NOT report… |
| P8-5-08 | MUST | S | Entry to suspended MUST suspend every non terminal work item of the case, and… |
| P8-5-09 | MUST NOT | D | The component MUST NOT permit a planning act while the case is suspended. |
| P8-5-10 | MUST | D | Every case that reaches completed, terminated or failed MUST carry a… |
| P8-5-11 | MUST | D | completed, expired, withdrawn, skipped and failed MUST be terminal, and the… |
| P8-5-12 | MUST | D | gate_indeterminate MUST be a state of the work item distinct from… |
| P8-5-13 | MUST | S | unassignable MUST be a state distinct from withdrawn, and the component MUST… |
| P8-5-14 | MUST | D | error MUST have declared exits and MUST NOT be terminal, because a system… |
| P8-5-15 | MUST | D | Where a work item enters suspended, the component MUST retain the state held… |
| P8-5-16 | MUST | D | Where a work item is in_progress and its holder's hold is revoked, the… |
| P8-5-17 | MUST NOT | D | The component MUST NOT transition a work item from offered directly to… |
| P8-5-18 | MUST | D | Transitions out of pending_gate on gate satisfaction MUST depend only on the… |
| P8-5-19 | MUST | D | No slot state MUST be terminal, because a case that reopens may repopulate… |
| P8-5-20 | MUST | D | The component MUST expose empty, discarded and unresolvable as three distinct… |
| P8-5-21 | MUST | S | A transition to superseded MUST NOT alter the pinned reference the slot holds. |
| P8-5-22 | MUST | D | not_achieved MUST be recorded explicitly at case termination, and the… |
| P8-5-23 | MUST NOT | S | The component MUST NOT attach work to a milestone. |
| P8-5-24 | MUST | D | unevaluated MUST be distinguishable from unsatisfied in every projection,… |
| P8-5-25 | MUST NOT | D | An entry gate that has reached satisfied MUST NOT cause a second admission of… |
| P8-5-26 | MUST | D | The component MUST declare, per gate, whether it is re-evaluable after… |
| P8-5-27 | MUST | D | Where a stage transitions to a terminal state, every non terminal item it… |
| P8-5-28 | MUST | D | Propagation from a container to its contents MUST be recorded per contained… |
| P8-5-29 | MUST NOT | D | Propagation MUST NOT convert a non terminal item into completed. |
| P8-5-30 | MUST | D | Where a stage is suspended, the suspension MUST propagate to contained items,… |

**§6. Execution semantics**

| Clause | Modality | Basis | Subject |
|---|---|---|---|
| P8-6-01 | MUST | D | Given the same case definition version, the same sequence of external events… |
| P8-6-02 | MUST NOT | D | The component MUST NOT allow the order in which it evaluates the gates… |
| P8-6-03 | MUST | P | Where a case definition admits a triggering event under which the resulting… |
| P8-6-04 | MUST NOT | D | A gate condition MUST NOT have any effect on state, and the component MUST… |
| P8-6-05 | MUST | D | The component MUST NOT derive any state transition from the wall clock other… |
| P8-6-06 | MUST | D | A gate MUST be evaluated only on the firing of one of its declared triggers,… |
| P8-6-07 | MUST | D | All gates triggered by one event MUST be evaluated against one immutable… |
| P8-6-08 | MUST | D | The snapshot used for an evaluation MUST be retained by reference in the gate… |
| P8-6-09 | MUST | D | Transitions resulting from the evaluations of one event MUST be applied… |
| P8-6-10 | MUST | D | Where the transitions resulting from one event themselves fire triggers, the… |
| P8-6-11 | MUST | D | The component MUST declare a finite maximum generation depth for the cascade… |
| P8-6-90 | MUST | D | The declared maximum generation depth MUST be at least 8, being the smallest… |
| P8-6-91 | MUST | D | The component MUST record a breach of the declared maximum generation depth… |
| P8-6-12 | MUST NOT | D | The component MUST NOT re-evaluate a gate whose state is satisfied and which… |
| P8-6-13 | MUST | S | A trigger MUST be a declared lifecycle transition of a named item, a declared… |
| P8-6-14 | MUST | D | Where a trigger's source item is never instantiated, the gate MUST remain… |
| P8-6-15 | MUST | D | A gate with no declared trigger and a declared condition MUST be evaluated… |
| P8-6-16 | MUST | D | The component MUST obtain every gate condition verdict from Part 2 and MUST… |
| P8-6-17 | MUST | D | The component MUST accept and represent every verdict value Part 2 can… |
| P8-6-18 | MUST NOT | D | The component MUST NOT map a non verdict to unsatisfied, to satisfied, or to… |
| P8-6-19 | MUST | D | Where an entry gate evaluation returns a non verdict, the guarded item MUST… |
| P8-6-20 | MUST | D | Where an exit gate evaluation returns a non verdict, the guarded item MUST… |
| P8-6-92 | MUST | D | Where an exit gate evaluation returns a non verdict, the gate MUST enter… |
| P8-6-93 | MUST | D | Where any gate evaluation returns a non verdict, the component MUST raise an… |
| P8-6-21 | MUST | D | An item in gate_indeterminate MUST be visible to a party holding oversight… |
| P8-6-22 | MUST | D | The component MUST declare a re-evaluation policy for indeterminate gates. |
| P8-6-94 | MUST | D | The component MUST record every re-evaluation attempt of an indeterminate… |
| P8-6-95 | MUST | D | The component MUST record the cessation of re-evaluation of an indeterminate… |
| P8-6-23 | MUST NOT | D | The component MUST NOT permit a case to reach completed while any entry gate… |
| P8-6-24 | MUST | D | Candidate derivation MUST be performed by evaluating a pinned assignment… |
| P8-6-25 | MUST | D | The candidate set MUST be pinned at derivation and MUST NOT be re-derived… |
| P8-6-26 | MUST | D | Where the organisational model changes after derivation, the component MUST… |
| P8-6-27 | MUST | S | Where the assignment expression yields a group rather than a set of parties,… |
| P8-6-28 | MUST | D | Where the derivation of a candidate set does not complete, the component MUST… |
| P8-6-96 | MUST | D | Where a candidate derivation records derivation_failed, the component MUST… |
| P8-6-29 | MUST | D | Where the derivation completes and yields no member, the component MUST… |
| P8-6-30 | MUST | D | Where the derivation yields members of whom every one is excluded, the… |
| P8-6-31 | MUST | D | The component MUST support offering one work item to a candidate set of two… |
| P8-6-97 | MUST | D | The component MUST support allocating one work item to exactly one party… |
| P8-6-98 | MUST | D | The component MUST record which distribution mode was used for every work… |
| P8-6-32 | MUST | D | Where a work item is offered to two or more candidates, the first successful… |
| P8-6-33 | MUST | D | Where several alternative work items are simultaneously available and the… |
| P8-6-34 | MUST NOT | D | The component MUST NOT record a candidate that did not claim as having… |
| P8-6-35 | MUST | S | Where a user event resolves a choice among alternatives, the component MUST… |
| P8-6-36 | MUST | D | The component MUST make the claim operation linearisable per work item, such… |
| P8-6-37 | MUST NOT | D | The component MUST NOT resolve a claim race by any property of the claimant… |
| P8-6-38 | MUST | D | The component MUST determine eligibility, being membership of the current… |
| P8-6-39 | MUST | D | The component MUST request an authorisation decision from Part 7 for every… |
| P8-6-40 | MUST NOT | D | The component MUST NOT treat eligibility as authorisation, and MUST NOT treat… |
| P8-6-41 | MUST | D | Where Part 7 requires a prior participation fact to evaluate a dynamic… |
| P8-6-42 | MUST | D | Where an authorisation decision denies an act, the component MUST record the… |
| P8-6-43 | MUST | D | At most one party MUST hold a work item at any instant. |
| P8-6-44 | MUST | D | A hold in reserved MUST be subject to a lease with a declared expiry, and on… |
| P8-6-45 | MUST | D | The lease duration MUST be declared by the work item definition or by a… |
| P8-6-46 | MAY | D | A hold in in_progress MAY be exempt from lease expiry, and only where the… |
| P8-6-99 | MUST | D | Where a hold is exempt from lease expiry, the component MUST record… |
| P8-6-100 | MUST | D | Where a hold is exempt from lease expiry, the component MUST raise an… |
| P8-6-47 | MUST | D | Lease expiry MUST be recorded as an event naming the prior holder, and MUST… |
| P8-6-48 | MUST NOT | D | A read of a work item MUST NOT extend its lease. |
| P8-6-49 | MUST | D | claim, complete, report_undecidable, report_not_applicable, fail, skip and… |
| P8-6-50 | MUST | D | A repeated complete with a different idempotency key on a work item already… |
| P8-6-51 | MUST | D | add_comment and attach_artifact MUST be idempotent under the same idempotency… |
| P8-6-52 | MUST | D | Gate evaluation MUST be idempotent with respect to its triggering event, such… |
| P8-6-53 | MUST | D | The component MUST declare the period for which it retains idempotency keys. |
| P8-6-101 | MUST | D | The component MUST retain every idempotency key for at least the declared… |
| P8-6-102 | MUST | D | The component MUST record that it treated a key presented after the declared… |
| P8-6-54 | MUST | S | A case MUST reach completed only where every item declared required has… |
| P8-6-55 | MUST | D | The component MUST record, for every case that reaches completed, whether… |
| P8-6-56 | MUST | S | Where the requiredness of an item is determined by a rule, the component MUST… |
| P8-6-57 | MUST NOT | D | The component MUST NOT complete a case while any contained item is… |
| P8-6-58 | MUST | D | Where a case cannot complete because a required item is unassignable or its… |
| P8-6-59 | MUST | D | Where a work item definition declares a repetition rule, each instantiation… |
| P8-6-60 | MUST | P | The component MUST record the instant at which a repetition rule was… |
| P8-6-61 | MUST | D | The component MUST declare a finite maximum repetition count for every… |
| P8-6-103 | MUST | D | The component MUST record a breach of the declared maximum repetition count… |
| P8-6-62 | MUST NOT | P | A repetition MUST NOT inherit the holder of a prior repetition unless the… |
| P8-6-63 | MUST | D | Every work item definition MUST declare an actor class of human, agent or… |
| P8-6-64 | MUST NOT | D | The component MUST NOT permit a work item whose actor class is human to be… |
| P8-6-65 | MUST | D | Where a work item is completed by a non human actor, the completion record… |
| P8-6-66 | MUST | D | Where a work item's purpose is to check a value produced by a non human… |
| P8-6-67 | MUST NOT | D | The component MUST NOT auto complete a work item whose purpose is to check a… |
| P8-6-68 | MUST | D | Where an agent proposes an outcome for a work item of actor class human, the… |
| P8-6-104 | MUST | D | Where a proposal was presented, the completion record MUST record whether the… |
| P8-6-69 | MUST | D | Concurrent operations on one work item MUST be serialised, and the component… |
| P8-6-70 | MUST | D | Concurrent population of one case file slot MUST be serialised, and the… |
| P8-6-71 | MUST | D | The component MUST permit concurrent progress on distinct work items of one… |
| P8-6-72 | MUST | P | Where a case definition declares that two work items must not be performed… |
| P8-6-73 | MUST | D | Every deadline MUST be recorded as an absolute instant computed at the moment… |
| P8-6-74 | MUST | D | Where a deadline is expressed relative to an event, the component MUST record… |
| P8-6-75 | MUST | D | Where a working calendar is applied to a deadline computation, the component… |
| P8-6-76 | MUST | D | A deadline breach MUST produce an escalation record whether or not any effect… |
| P8-6-77 | MUST NOT | S | The component MUST NOT expire a work item on deadline breach unless the… |
| P8-6-78 | MUST | D | Where a case is suspended, deadline clocks for its items MUST be suspended,… |
| P8-6-79 | MUST | D | Where any pinned dependency of a non terminal work item is superseded, the… |
| P8-6-80 | MUST | D | Where a stale work item is presented, the presentation MUST state that a… |
| P8-6-81 | MUST | D | Completion of a stale work item MUST require an explicit acknowledgement… |
| P8-6-82 | MUST NOT | D | The component MUST NOT silently re-pin a stale work item to the current… |
| P8-6-83 | MUST | D | Where a stale work item is re-pinned, the component MUST create a new… |
| P8-6-84 | MUST | S | A planning act MUST be permitted only where the case is active, the acting… |
| P8-6-85 | MUST NOT | D | The component MUST NOT permit a planning act where the applicability rule… |
| P8-6-86 | MUST | D | An item added by a planning act MUST be subject to the same gates, candidate… |
| P8-6-87 | MUST NOT | D | A planning act MUST NOT introduce an item that is not declared as a… |
| P8-6-88 | MUST | D | Where the case definition is superseded while a case is running, the set of… |
| P8-6-89 | MUST | D | A migration act that re-pins a running case to a later definition version… |

**§7. Outcome and failure taxonomy**

| Clause | Modality | Basis | Subject |
|---|---|---|---|
| P8-7-01 | MUST | D | Every value the component can produce MUST belong to exactly one of the… |
| P8-7-02 | MUST NOT | D | The component MUST NOT return a value outside these enumerations, and MUST… |
| P8-7-03 | MUST | D | Every enumeration in this section marked closed MUST be closed, and every… |
| P8-7-04 | MUST | D | The component MUST expose, for every outcome value it returns, the three… |
| P8-7-05 | MUST | D | The component MUST provide undecidable as a disposition available on every… |
| P8-7-06 | MUST NOT | D | The component MUST NOT map undecidable to any value in the definition's… |
| P8-7-07 | MUST NOT | D | The component MUST NOT map undecidable, not_applicable, out_of_competence or… |
| P8-7-08 | MUST | D | A disposition of conflicted MUST remove the performer from the candidate set. |
| P8-7-33 | MUST | D | A disposition of conflicted MUST cause a re-derivation of the candidate set. |
| P8-7-34 | MUST NOT | D | A disposition of conflicted MUST NOT place the work item in a terminal state. |
| P8-7-09 | MUST | D | A disposition of out_of_competence MUST cause a re-derivation with the… |
| P8-7-10 | MUST | D | A disposition of undecidable MUST require the component to determine, from… |
| P8-7-11 | MUST NOT | D | A disposition of not_applicable MUST NOT satisfy a requirement that the work… |
| P8-7-12 | MUST | D | The component MUST distinguish these five outcomes and MUST NOT return one… |
| P8-7-13 | MUST NOT | D | The component MUST NOT return derived_empty where the read of the… |
| P8-7-14 | MUST | D | Where the outcome is derivation_partial, the component MUST record which… |
| P8-7-15 | MUST | D | The component MUST represent all nine values and MUST record the specific… |
| P8-7-16 | MUST NOT | D | The component MUST NOT treat undecidable, not_applicable, not_evaluated,… |
| P8-7-17 | MUST | D | Where Part 2 returns a verdict value this component's enumeration does not… |
| P8-7-35 | MUST | D | The component MUST treat a verdict value its enumeration does not contain as… |
| P8-7-36 | MUST | D | The component MUST raise an unrepresentable verdict event on receipt of a… |
| P8-7-18 | MUST | D | not_applicable returned for an entry gate MUST leave the guarded item in… |
| P8-7-37 | MUST | D | Where an entry gate returns not_applicable, the component MUST record the… |
| P8-7-19 | MUST NOT | D | A system fault outcome MUST NOT be recorded as a work item disposition, and… |
| P8-7-20 | MUST | D | A work item affected by a system fault MUST enter error, and the fault value… |
| P8-7-21 | MUST | D | Where internal_invariant_violated is detected, the component MUST stop… |
| P8-7-22 | MUST | D | The component MUST record exactly one completion basis and MUST NOT report… |
| P8-7-23 | MUST | D | Where more than one non performance basis applies, the component MUST record… |
| P8-7-24 | MUST | D | not_eligible and not_authorised MUST be distinct outcomes, and the component… |
| P8-7-25 | MUST | D | authorisation_unavailable MUST be distinct from not_authorised, because the… |
| P8-7-26 | MUST NOT | D | The component MUST NOT return applied where any part of the requested change… |
| P8-7-27 | MUST | D | The component MUST expose, for every terminal disposition, the three… |
| P8-7-28 | MUST | D | Where the component receives a non result from another component, it MUST… |
| P8-7-29 | MUST | D | Where the component emits a non result, it MUST emit it as a distinct event… |
| P8-7-30 | MUST | D | Where a non result would otherwise be discarded because no consumer… |
| P8-7-31 | MUST NOT | D | The component MUST NOT aggregate a set of dispositions into a single summary… |
| P8-7-32 | MUST | D | Every projection, report or count the component exposes over dispositions… |

**§8. Observability and the audit record**

| Clause | Modality | Basis | Subject |
|---|---|---|---|
| P8-8-01 | MUST | D | The component MUST record every state transition of every case, work item,… |
| P8-8-02 | MUST | D | The component MUST record every operation it accepts, including operations it… |
| P8-8-03 | MUST | D | The component MUST record every gate evaluation, including evaluations… |
| P8-8-04 | MUST | D | The component MUST record every candidate derivation, at the grain of one… |
| P8-8-05 | MUST | D | The component MUST record every presentation, at the grain of one record per… |
| P8-8-06 | MUST | D | The component MUST record every authorisation decision it obtained, by… |
| P8-8-07 | MUST | D | The component MUST record every read of a work item's payload by a party, at… |
| P8-8-08 | MUST | D | The component MUST record every escalation, at the grain of one record per… |
| P8-8-09 | MUST | D | The component MUST record every choice resolution, at the grain of one record… |
| P8-8-10 | MUST | D | The component MUST record every planning act and every migration act, at the… |
| P8-8-11 | MUST | D | A reader MUST be able to reconstruct, for any completed work item, the… |
| P8-8-12 | MUST | D | A reader MUST be able to reconstruct which version of every governing… |
| P8-8-13 | MUST | D | A reader MUST be able to reconstruct whether the performer was the only… |
| P8-8-14 | MUST | D | A reader MUST be able to reconstruct why every party who did not act did not… |
| P8-8-15 | MUST | D | A reader MUST be able to reconstruct the sequence of gate evaluations that… |
| P8-8-16 | MUST | D | A reader MUST be able to reconstruct which items of a case plan were present… |
| P8-8-17 | MUST | D | A reader MUST be able to reconstruct, for a case that reached a terminal… |
| P8-8-18 | MUST | D | A reader MUST be able to reconstruct every human non result, its reason, and… |
| P8-8-19 | MUST | D | A reader MUST be able to distinguish an act performed by a person from an act… |
| P8-8-20 | MUST NOT | D | Reconstruction MUST NOT depend on the availability of any component other… |
| P8-8-21 | MUST | D | Every count the component reports MUST state the grain at which it was… |
| P8-8-22 | MUST NOT | D | The component MUST NOT report a count of work items without stating whether… |
| P8-8-23 | MUST NOT | D | The component MUST NOT report a completion rate, throughput or cycle time… |
| P8-8-24 | MUST | D | Every derived metric the component exposes MUST be accompanied by its… |
| P8-8-25 | MUST | D | Where a metric excludes any disposition, the exclusion MUST be stated with… |
| P8-8-26 | MUST | D | Every record this component writes MUST be integrity protected such that… |
| P8-8-27 | MUST NOT | D | The component MUST NOT permit the deletion of a completion record,… |
| P8-8-28 | MUST | D | Where a record is disposed of under a retention schedule, the component MUST… |
| P8-8-29 | MUST | D | Where a case is subject to a legal hold, the component MUST refuse every… |
| P8-8-30 | MUST | D | The component MUST record the identity of every party that reads a… |
| P8-8-31 | MUST | D | The component MUST expose the count of work items in unassignable,… |
| P8-8-32 | MUST | D | The component MUST expose the count and age of work items whose lease has… |
| P8-8-33 | MUST | D | The component MUST expose the count of completions whose choice_breadth is… |
| P8-8-34 | MUST | D | The component MUST expose the count of completions whose stale_acknowledged… |
| P8-8-35 | SHOULD | D | The component SHOULD expose the distribution of human non results by reason,… |

**§9. Extension model**

| Clause | Modality | Basis | Subject |
|---|---|---|---|
| P8-9-01 | MUST | D | The following sets MUST be closed and MUST NOT be extended by an… |
| P8-9-02 | MUST | D | The following sets MAY be extended under the governance in §9.4: operation… |
| P8-9-03 | MUST | D | Business outcome enumerations MUST be declared per work item definition and… |
| P8-9-04 | MUST | D | A proposal to extend an open set MUST state the act or condition the new… |
| P8-9-05 | MUST NOT | D | A new member MUST NOT be admitted where an existing member differs from it… |
| P8-9-06 | MUST NOT | D | A new member of the operation set MUST NOT introduce a state transition not… |
| P8-9-07 | MUST | D | Where an implementation requires a state transition this part does not list,… |
| P8-9-08 | MUST | S | A composite work item MUST be represented as a work item whose completion… |
| P8-9-09 | MUST | D | A composite work item MUST declare its completion condition, and the… |
| P8-9-10 | MUST NOT | D | A composite work item MUST NOT be completed by aggregating subordinate… |
| P8-9-11 | MUST | S | Where a composite work item completes before every subordinate has reached a… |
| P8-9-12 | MUST | S | A routing pattern that assigns work to parties in sequence or in parallel… |
| P8-9-13 | MUST NOT | D | A stage MUST NOT be represented as a composite work item, and the component… |
| P8-9-14 | MUST | D | Every extension an implementation makes MUST be declared in a machine… |
| P8-9-15 | MUST | D | The component MUST record, on every record affected by an extension, the… |
| P8-9-16 | MUST NOT | D | An extension MUST NOT change the meaning of an existing member of any set. |
| P8-9-17 | MUST NOT | D | An extension MUST NOT be required for interoperation, and a consumer that… |

**§10. Standards and specifications**

| Clause | Modality | Basis | Subject |
|---|---|---|---|
| P8-10-01 | MUST | D | Where this part and a consulted specification address the same subject and do… |
| P8-10-02 | MUST | D | Where this part and a consulted specification conflict, an implementation… |
| P8-10-03 | MUST | D | An implementation that also claims conformance to WS-HumanTask 1.1 or CMMN… |
| P8-10-04 | SHOULD | P | A reader consulting CMMN 1.1 §2.6 SHOULD note that it requires conformance to… |
| P8-10-05 | SHOULD | P | A reader consulting CMMN 1.1 §2.1 SHOULD note that it states four types of… |
| P8-10-06 | MUST | D | An implementation MUST treat the following as requirements of this part… |

**§11. Anti patterns**

| Clause | Modality | Basis | Subject |
|---|---|---|---|
| P8-11-01 | MUST NOT | D | The component MUST NOT write a completion record without a referenced… |
| P8-11-02 | MUST NOT | D | The component MUST NOT map any non result to a value in a success or failure… |
| P8-11-03 | MUST | D | The component MUST provide a distinct representation for every non result it… |
| P8-11-04 | MUST NOT | D | The component MUST NOT determine eligibility against a candidate set computed… |
| P8-11-05 | MUST NOT | D | The component MUST NOT hold a literal copy of a fact whose authority belongs… |
| P8-11-06 | MUST NOT | D | The component MUST NOT permit another component to read a case file slot as a… |
| P8-11-07 | MUST | D | The component MUST evaluate all gates triggered by one event against one… |
| P8-11-08 | MUST | D | The component MUST record attention and candidacy separately and MUST expose… |
| P8-11-09 | MUST NOT | D | The component MUST NOT re-pin a work item's dependencies without creating a… |
| P8-11-10 | MUST NOT | D | The component MUST NOT allow a deadline, an escalation or a timer to write a… |
| P8-11-11 | MUST | D | The component MUST subject every reservation to a lease with a declared… |
| P8-11-12 | MUST | D | The presentation pin MUST record what was presented, so that a decision made… |
| P8-11-13 | MUST NOT | D | The component MUST NOT treat a system fault state as terminal. |
| P8-11-14 | MUST | D | Every runtime addition to a case plan MUST be traceable to an attributable… |

**§12. Boundaries with other parts**

| Clause | Modality | Basis | Subject |
|---|---|---|---|
| P8-12-01 | MUST NOT | D | The component MUST NOT evaluate a gate condition, applicability rule,… |
| P8-12-02 | MUST | D | The component MUST accept the full verdict vocabulary of Part 2 including… |
| P8-12-03 | MUST NOT | D | The component MUST NOT hold the authoritative text of a controlled document. |
| P8-12-04 | MUST | D | The component MUST hold, for every instruction presented, a citation that… |
| P8-12-05 | MUST | D | The component MUST treat every completion record as a record in the Part 1… |
| P8-12-06 | MUST | D | The component MUST emit every event in §8.1 to Part 3. |
| P8-12-07 | MUST NOT | D | The component MUST NOT represent its own event log as the audit record of a… |
| P8-12-08 | MUST | D | The component MUST own the operational state of work and cases as sole… |
| P8-12-49 | MUST NOT | D | The component MUST NOT assert authority over the evidentiary chain, which… |
| P8-12-09 | MUST NOT | D | The component MUST NOT render an authorisation decision. |
| P8-12-10 | MUST | D | The component MUST obtain an authorisation decision at the instant of every… |
| P8-12-11 | MUST | D | The component MUST supply prior participation facts to Part 7 on request as… |
| P8-12-12 | MUST NOT | D | The component MUST NOT permit Part 7 to hold a second copy of the… |
| P8-12-13 | MUST NOT | D | The component MUST NOT implement predefined control flow constructs. |
| P8-12-14 | MUST NOT | D | The component MUST NOT represent a case as a process instance, and MUST NOT… |
| P8-12-15 | MUST | S | Where a work item is created at the request of a process instance, the… |
| P8-12-50 | MUST | D | Where a work item was created at the request of a process instance, the… |
| P8-12-51 | MUST | D | The component MUST retain its own record of a work item independently of the… |
| P8-12-16 | MUST NOT | D | The component MUST NOT allow the termination of a requesting process instance… |
| P8-12-17 | MUST NOT | D | The component MUST NOT maintain an authoritative organisational model. |
| P8-12-18 | MUST | D | The component MUST pin the organisational snapshot used in every candidate… |
| P8-12-19 | MUST | D | The component MUST own the case role binding and MUST NOT delegate it to Part… |
| P8-12-20 | MUST NOT | D | The component MUST NOT version the definitions it instantiates. |
| P8-12-21 | MUST | D | The component MUST pin the definition version at instantiation and MUST… |
| P8-12-22 | MUST | D | The component MUST accept a definition change notification from Part 4 and… |
| P8-12-23 | MUST NOT | D | The component MUST NOT select one party from a candidate set by any governed… |
| P8-12-24 | MAY | D | The component MAY select by arrival order in a claim race, which is not a… |
| P8-12-25 | MUST | D | Where a selection is obtained from Part 5, the component MUST record the… |
| P8-12-26 | MUST NOT | D | The component MUST NOT define or version a payload or slot schema. |
| P8-12-27 | MUST | D | The component MUST pin the schema version used for every validation and MUST… |
| P8-12-28 | MUST NOT | D | The component MUST NOT store attachment bytes. |
| P8-12-29 | MUST | D | The component MUST own the attachment association record and MUST hold the… |
| P8-12-30 | MUST | D | Where a content address ceases to resolve, the component MUST record the… |
| P8-12-31 | MUST | D | The component MUST expose the state required to verify every clause of this… |
| P8-12-32 | MUST NOT | D | The component MUST NOT report its own conformance to this part as assurance. |
| P8-12-33 | MUST | D | The component MUST expose the invariants in §12.14 in a form Part 12 can test. |
| P8-12-34 | MUST NOT | D | The component MUST NOT record a model invocation as a human act. |
| P8-12-35 | MUST | D | The component MUST record an agent completion with actor_class_used of agent… |
| P8-12-36 | MUST | D | Where an agent proposal is presented to a human performer, the component MUST… |
| P8-12-37 | MUST NOT | D | The component MUST NOT auto complete a work item of actor class human on any… |
| P8-12-38 | MUST | D | The component MUST treat the authority assignments of Part 0 as governing,… |
| P8-12-39 | MUST | D | The component MUST declare, for every fact it owns, that it is the sole… |
| P8-12-40 | MUST NOT | D | The component MUST NOT claim authority over: party and group identity; rule… |
| P8-12-41 | MUST | D | At every instant, every work item in allocated, reserved, in_progress or… |
| P8-12-42 | MUST | D | At every instant, every terminal work item MUST have exactly one disposition,… |
| P8-12-43 | MUST | D | At every instant, every completion record MUST reference exactly one… |
| P8-12-44 | MUST | D | At every instant, the number of work items with disposition… |
| P8-12-45 | MUST | D | At every instant, every case in a terminal or closed state MUST have exactly… |
| P8-12-46 | MUST | D | At every instant, every work item added by a planning act MUST reference… |
| P8-12-47 | MUST | D | At every instant, every gate whose state is satisfied and which is declared… |
| P8-12-48 | MUST | D | At every instant, no case file slot MUST hold a literal value whose… |

---

## 1. Scope and responsibilities

### 1.1 What the component is accountable for

The human task and case management component is accountable for the work that people do inside a governed system, and for the container in which that work accumulates. Two things distinguish it from every other component of the system: it is the only component whose primary actor is a person, and it is the only component whose plan is not fully determined before execution begins.

Those two properties are the source of every hard requirement in this part. Because the actor is a person, the component must record not only what was decided but what the person was shown, whether they had a choice, and whether they were able to decide at all. Because the plan is not fully determined, the component must represent work that was planned and never opened, work that opened and was never assignable, and work that a person added at runtime, all as first class records rather than as gaps.

**P8-1-01** (MUST) [D] The component MUST own the work item as a durable record, from the moment the work is planned to a terminal disposition, including work items that never become available to any person.

**P8-1-02** (MUST) [D] The component MUST own the case as a first class entity with its own identity, lifecycle, participation record and terminal disposition, and MUST NOT represent a case solely as an aggregation of the work items that reference it.

**P8-1-03** (MUST) [D] The component MUST own the derivation of the candidate set for a work item, being the determination of which parties are offered the opportunity to perform it.

**P8-1-04** (MUST) [D] The component MUST own the assignment state of a work item, being which single party, if any, currently holds it.

**P8-1-05** (MUST) [D] The component MUST own the gate, being the condition under which a work item becomes available and the condition under which it is withdrawn, including the triggering, sequencing and snapshotting of gate evaluation.

**P8-1-06** (MUST) [D] The component MUST own the resolution of deferred choice, being the record of which alternative was taken when several were simultaneously available and the environment rather than the model selected among them.

**P8-1-07** (MUST) [D] The component MUST own the participation record of a case, being the complete history of which parties performed which acts on which work items of that case.

**P8-1-08** (MUST) [D] The component MUST own the case file, being the set of typed slots scoped to a single case instance that hold the values and references that case accumulates.

**P8-1-09** (MUST) [D] The component MUST own the planning act, being the record of a person adding a discretionary item to the plan of a running case.

**P8-1-10** (MUST) [D] The component MUST own the presentation pin, being the record of what was placed in front of a performer at the moment a work item was performed.

**P8-1-11** (MUST) [D] The component MUST own the milestone, being a named achieved state of a case to which no work is directly attached.

### 1.2 What the component is explicitly not accountable for

The boundary matters more than the responsibility list, because each of the following is a thing a human task component will absorb if not prevented, and each absorption destroys a property the system depends on. §12 states each boundary reciprocally and gives the failure that follows from breaching it.

**P8-1-12** (MUST NOT) [D] The component MUST NOT evaluate the declarative condition of a gate itself, and MUST obtain the verdict from the business rules engine component (`Part 2`).

**P8-1-13** (MUST NOT) [D] The component MUST NOT select one outcome from several candidate outcomes by governed algorithm, and MUST obtain such a selection from the decision engine component (`Part 5`).

**P8-1-14** (MUST NOT) [D] The component MUST NOT render an authorisation decision on whether a party may perform an act, and MUST obtain that decision from the policy decision point component (`Part 7`).

**P8-1-15** (MUST NOT) [D] The component MUST NOT maintain its own copy of the organisational model, and MUST read parties, groups, roles, organisational units, capabilities and calendars from the reference and master data component (`Part 10`).

**P8-1-16** (MUST NOT) [D] The component MUST NOT define the control flow that sequences work across a predefined process, and MUST delegate predefined sequencing, joins, loops and compensation to the workflow and process orchestration component (`Part 6`).

**P8-1-17** (MUST NOT) [D] The component MUST NOT define or version the schema of any payload it carries, and MUST reference schema identity from the schema and contract registry component (`Part 9`).

**P8-1-18** (MUST NOT) [D] The component MUST NOT version the definitions from which cases and work items are instantiated, and MUST read those definitions and their versions from the metadata and model repository component (`Part 4`).

**P8-1-19** (MUST NOT) [D] The component MUST NOT store the bytes of any attachment, and MUST hold only the content address of an attachment as held by the content addressed artifact store component (`Part 11`).

**P8-1-20** (MUST NOT) [D] The component MUST NOT hold the authoritative text of any instruction, procedure or policy presented to a performer, and MUST hold a point in time citation resolvable by the controlled documents component (`Part 1`).

**P8-1-21** (MUST NOT) [D] The component MUST NOT be the audit ledger, and MUST emit its events to the provenance and audit ledger component (`Part 3`) rather than serving as the system of record for reconstruction.

**P8-1-22** (MUST NOT) [D] The component MUST NOT represent an act performed by a non-human actor as an act performed by a person, and MUST record a model or agent invocation as a reference to the model invocation component (`Part 13`).

**P8-1-23** (MUST NOT) [D] The component MUST NOT verify its own conformance claims, and MUST expose the state required for the conformance and assurance harness component (`Part 12`) to do so.

**P8-1-24** (MUST NOT) [D] The component MUST NOT act as a general purpose data store for facts whose authority belongs to another component, and MUST hold such facts as pinned references rather than as copies.

### 1.3 The three failures this part exists to prevent

Stating these makes the rest of the part legible. Each is a failure that a conventionally specified human task component permits.

*The unattributable approval.* A record says a named person approved something at a time. It does not say what they were shown, which version of the governing procedure was in force, whether any outcome other than approval was available to them, or whether they were the only party who could have acted. Years later the record cannot distinguish a considered judgement from a forced click. §3.6, §3.7 and §8 exist to prevent this.

*The silent negative.* A gate condition could not be evaluated, or a candidate query failed, or a reviewer could not decide on the evidence available. In each case the system had no representation for the non result and recorded the nearest available negative. The work appears to have been declined, or not to have qualified, or never to have been due. §7 exists to prevent this, and it is the section against which an implementation of this part should be judged first.

*The case as a bag.* The case accumulates whatever any component needs to put somewhere, becomes the de facto integration point of the system, and acquires a second authoritative copy of facts owned elsewhere. Within two years no component can be changed without changing the case. §3.9 and §12 exist to prevent this.

### 1.4 What this part does not require

**P8-1-25** (MAY) [D] An implementation MAY support cases whose plan is entirely predefined, and this part does not require that any case admit runtime planning.

**P8-1-26** (MAY) [D] An implementation MAY support work items that exist outside any case, and this part does not require that every work item belong to a case.

**P8-1-27** (MUST NOT) [D] This part MUST NOT be read as requiring a graphical notation, and no requirement of this part depends on how a case model is drawn.

---

## 2. Terminology

Terms are owned here and are not redefined in another part. Where a term is taken from a specification, the specification is named and the difference from its usage there is stated, because a term silently redefined is worse than a term invented.

### 2.1 Work terms

**Work item.** The runtime unit of work performed by a single actor, instantiated from a work item definition, having its own identity and lifecycle. The Workflow Management Coalition reference model uses *work item* for this concept and *workitem manager* for the component that owns its lifecycle; WS-HumanTask 1.1 §1.5 notes the same component and calls the runtime object a *task instance*. This part uses *work item* for the runtime object and reserves *task* for the definition, because the two are versioned differently and conflating them defeats §9.

**Work item definition.** The governed, versioned specification from which a work item is instantiated. Owned by `Part 4`; referenced here.

**Performer.** The single actor that holds a work item in `in_progress` and whose acts are attributed to it. WS-HumanTask 1.1 §3.1 calls this the *actual owner*. This part uses *performer* because *owner* invites confusion with ownership of a fact in the authority sense.

**Candidate.** A party to which a work item is or may be offered. WS-HumanTask 1.1 §3.1 calls this a *potential owner*.

**Candidate set.** The set of candidates derived for a work item at a stated instant, together with the derivation record. Not a live query result; a pinned set (see §6.4).

**Excluded party.** A party removed from a candidate set by an exclusion rule or by a segregation of duty constraint, recorded with the reason for removal. WS-HumanTask 1.1 §3.1 has *excluded owners* for the definitional case only; this part requires the runtime removal to be recorded too, because a party excluded by segregation of duty is the fact an auditor asks about.

**Offer.** The act of making a work item available to every member of a candidate set without assigning it, such that a subsequent claim resolves who performs it. Corresponds to the *distribution by offer to multiple resources* creation and push patterns of Russell, ter Hofstede, Edmond and van der Aalst, *Workflow Resource Patterns*, BETA Working Paper WP 127, Eindhoven University of Technology, 2004.

**Allocation.** The act of assigning a work item to exactly one party without that party having accepted it. Corresponds to *distribution by allocation to a single resource* in the same catalogue.

**Claim.** The act by which a candidate takes exclusive hold of an offered work item.

**Reservation.** The state in which a work item is held exclusively by one party who has not begun work. Held under a lease (§6.7).

**Release.** The act by which a holder relinquishes a work item without performing it, returning it to its candidate set.

**Decline.** The act by which a candidate states that it will not perform an offered work item, removing that candidate from the candidate set for the remainder of the work item's life.

**Delegation.** The act of transferring hold of a work item to a named party, where accountability is retained by the delegating party.

**Forwarding.** The act of transferring a work item to a named party or set, where accountability transfers with it.

**Escalation.** An event raised because a work item has not reached a required state by a required time, having a declared effect on attention, candidacy or priority, and never having the effect of performing the work.

**Attention.** The property of a work item being visible in the worklist of a party. Attention is not candidacy: a party may hold attention on a work item it may not claim, and this part requires the two to be recorded separately (§3.5).

**Worklist.** A projection of the work items on which a stated party holds attention at a stated instant. A view, never a store.

### 2.2 Case terms

**Case.** A durable container of governed work concerning one subject, whose plan may be extended at runtime by authorised parties, and which has identity, state, participation and disposition of its own. OMG CMMN 1.1 (formal/2016-12-01) §4.1 defines a Case as a proceeding involving actions taken regarding a subject in a particular situation to achieve a desired outcome; this part adopts that sense and adds the requirement that the case be evidentiary, which CMMN does not address.

**Case definition.** The governed, versioned specification from which a case is instantiated. Owned by `Part 4`. Corresponds to what CMMN 1.1 §5.2.1 calls a Case, which in CMMN is a design time object; CMMN uses *case instance* (§8.2) for the runtime object.

**Case plan.** The set of planned items of a case instance at a stated instant, comprising the items instantiated from the case definition and the items added by planning acts.

**Stage.** A nested container of planned items within a case plan, having its own gates and its own lifecycle. CMMN 1.1 §5.4.8.

**Discretionary item.** An item available to be added to a running case plan at the discretion of an authorised party rather than instantiated automatically. CMMN 1.1 §5.4.9.2.

**Planning act.** The recorded act of an authorised party adding a discretionary item to a running case plan. CMMN 1.1 §8.7 constrains when planning is permitted; this part additionally requires the act to be attributable (§3.8).

**Milestone.** A named achieved state of a case, to which no work is directly attached, whose achievement is recorded as an event. CMMN 1.1 §5.4.3.

**Case file.** The set of typed slots scoped to one case instance holding the values and references that case accumulates. CMMN 1.1 §5.3.1 uses CaseFile in the same sense and states it implies no assumption about physical storage; this part imposes constraints CMMN does not (§3.9).

**Case file slot.** One addressable position in the case file, having a declared type, a declared multiplicity, and a state that distinguishes never populated from emptied.

**Case role.** A named position within a case to which parties are bound for the life of that case instance. CMMN 1.1 §5.2.2 defines Role and states explicitly that assignment of roles to participants is not in the scope of CMMN. This part specifies the binding because the gap is load bearing.

**Case participation record.** The complete, append only history of which parties performed which acts on which items of one case.

### 2.3 Gate and choice terms

**Gate.** A named guard on a work item, stage, milestone or case, comprising zero or more triggers and zero or one condition, whose satisfaction causes a declared transition. An entry gate admits; an exit gate withdraws. CMMN 1.1 §5.4.5.1 to §5.4.5.3 calls these Criterion, entry criterion and exit criterion, and §5.4.6 defines the Sentry that a criterion refers to. This part uses *gate* for the whole guard and keeps *trigger* and *condition* for the parts, because the CMMN split of Criterion from Sentry serves interchange rather than execution.

**Trigger.** The event on which a gate is evaluated, being a declared lifecycle transition of another item or of a case file slot, an elapse of time, or a raised user event. CMMN 1.1 §5.4.6.1 to §5.4.6.3 calls these on parts.

**Condition.** The declarative expression a gate requires to hold, evaluated by `Part 2`. CMMN 1.1 §5.4.6.4 calls this the if part.

**Gate verdict.** The value returned to the component when a gate is evaluated: satisfied, unsatisfied, or one of the non verdicts enumerated in §7.4.

**Indeterminate gate.** A gate whose most recent evaluation returned a non verdict, being a state of the gate and not a value of its condition. This term is introduced by this part; §7.4 and §11.2 give the reason.

**Deferred choice.** A situation in which several alternatives are simultaneously available and the selection among them is made by the environment at the moment of first commitment rather than by the model. Catalogued as pattern WCP-16 in van der Aalst, ter Hofstede, Kiepuszewski and Barros, *Workflow Patterns*, Distributed and Parallel Databases 14(3):5-51, 2003, and revised in Russell, ter Hofstede, van der Aalst and Mulyar, *Workflow Control-Flow Patterns: A Revised View*, BPM Center Report BPM-06-22, 2006.

**Claim race.** The specific deferred choice in which one work item is offered to several candidates and the first claim determines the performer.

**Choice resolution record.** The record of a resolved deferred choice, naming the alternatives that were available, the alternative taken, the instant of resolution and the party or event that resolved it.

**Withdrawal by resolution.** The terminal disposition of an alternative that was not taken in a resolved deferred choice, distinguished from a disposition arising from the alternative's own gate or from any party's decision.

### 2.4 Evidentiary terms

**Presentation pin.** The record of what was placed in front of a performer at a stated instant, comprising the pinned identifiers of every definition, document, reference set, schema and value that composed the presentation, sufficient to reconstruct what the performer saw without the system running.

**Pinned reference.** A reference that resolves to a stated version of a stated object as it stood at a stated instant, rather than to the current version of that object.

**Choice breadth.** The number of distinct outcomes that were available to the performer at the instant of completion. A choice breadth of one means the performer had no alternative, and a record that omits this cannot distinguish judgement from compulsion.

**Completion basis.** The recorded reason a work item or case reached a terminal state, distinguishing performance from expiry, from withdrawal, from disablement and from administrative closure.

**Staleness.** The property of a work item whose pinned definition, document or reference set has been superseded since the work item was pinned, while the work item has not reached a terminal state.

**Segregation of duty.** A constraint forbidding one party from performing two stated acts, whether across definitions (static) or within one case instance (dynamic). The static and dynamic separation of duty relations of the ANSI/INCITS 359 role based access control standard are the origin of the distinction; the constraint is evaluated by `Part 7` and the history it requires is owned here (§12.4).

**Party.** Any identity capable of holding a work item, being a person, an organisational position, or a declared non-human actor. Resolved from `Part 10`.

**Actor class.** The declared kind of party permitted to perform a work item definition: `human`, `agent`, or `either`. Introduced by this part; §6.11 gives the reason.

### 2.5 Terms deliberately not defined here

**P8-2-01** (MUST NOT) [D] This part MUST NOT define process, activity, gateway, token, or compensation, which are owned by `Part 6`.

**P8-2-02** (MUST NOT) [D] This part MUST NOT define rule, constraint, verdict semantics, or rule set, which are owned by `Part 2`.

**P8-2-03** (MUST NOT) [D] This part MUST NOT define policy, obligation, advice, or combining algorithm, which are owned by `Part 7`.

**P8-2-04** (MUST NOT) [D] This part MUST NOT define decision, decision table, or decision requirement, which are owned by `Part 5`.

**P8-2-05** (MUST NOT) [D] This part MUST NOT define document, record, version, supersession, or effective date, which are owned by `Part 1`.

**P8-2-06** (MUST) [D] Where this part uses a term owned by another part, it MUST use that term with the meaning that part gives it and MUST NOT narrow or extend it.

---

## 3. Data model

This section specifies the records the component owns. Every field carries a type, whether it is required, its cardinality, and what its absence means. Absence is specified because an absent field read as a value is the most common defect at this component's boundaries, and because a reader years later has only the record.

Types are abstract. `identifier` is an opaque immutable string unique within its declared scope. `instant` is a point in time with an offset from UTC and at least millisecond resolution. `pinned-ref` is a reference that resolves to a stated version of a stated object (§2.4). `digest` is a cryptographic hash over a canonical form. `duration` is an elapsed time. `enum(...)` is a closed set unless the field description says the set is open.

### 3.1 Identity and addressing

**P8-3-01** (MUST) [D] Every case instance, work item, candidate set, gate evaluation, presentation pin, completion record, planning act, choice resolution, milestone achievement, case file slot and case role binding MUST carry an identifier that is unique within the component for all time.

**P8-3-02** (MUST NOT) [D] An identifier MUST NOT be reused after the record it identifies reaches a terminal state, and MUST NOT be reused after that record is disposed of.

**P8-3-03** (MUST NOT) [D] An identifier MUST NOT encode any mutable property of the thing it identifies, including its state, its performer, its case, its priority or its position in a plan.

**P8-3-04** (MUST) [D] A work item MUST be addressable independently of its case, so that a citation to a work item resolves without knowledge of case structure.

**P8-3-05** (MUST) [D] A case file slot MUST be addressable by a path that is stable across the life of the case instance and that does not change when a sibling slot is added or removed.

**P8-3-06** (MUST) [D] Where a work item is instantiated by repetition, each repetition MUST receive its own identifier and MUST carry the ordinal of the repetition and the identifier of the item whose repetition rule produced it.

**P8-3-07** (SHOULD) [D] An identifier SHOULD be generable without coordination across deployment units, so that identity does not depend on a single allocator being reachable.

### 3.2 The case record

| Field | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `case_id` | identifier | yes | 1 | Not possible; a case without identity is not a case |
| `definition_ref` | pinned-ref | yes | 1 | Not possible; see P8-3-09 |
| `subject_ref` | pinned-ref | no | 0..n | The case has no declared subject, which is legal for cases opened before the subject is known and MUST NOT be read as an unidentified subject |
| `case_state` | enum, §5.2 | yes | 1 | Not possible |
| `opened_at` | instant | yes | 1 | Not possible |
| `opened_by` | pinned-ref to party | yes | 1 | Not possible; a case opened by a scheduled trigger names the trigger's declared responsible party |
| `opened_on_behalf_of` | pinned-ref to party | no | 0..1 | The opener acted for itself, not for another party |
| `priority` | integer 0..10 | no | 0..1 | The priority is the definition default; absence MUST NOT be read as lowest or highest |
| `closed_at` | instant | no | 0..1 | The case has not reached a terminal state |
| `completion_basis` | enum, §7.6 | no | 0..1 | The case has not reached a terminal state; MUST be present whenever `closed_at` is present |
| `reopen_count` | integer ≥ 0 | yes | 1 | Not possible; zero means never reopened |
| `parent_case_id` | identifier | no | 0..1 | The case is not a subordinate of another case |
| `external_correlation` | string | no | 0..n | No external system has correlated to this case; MUST NOT be used as an identifier by this component |

**P8-3-08** (MUST) [D] The case record MUST contain every field marked required in the table in §3.2, with the type, cardinality and absence semantics stated there.

**P8-3-09** (MUST) [D] `definition_ref` MUST be a pinned reference to the exact version of the case definition in force at `opened_at`, and MUST NOT be a reference that resolves to the current version.

**P8-3-10** (MUST NOT) [D] The case record MUST NOT carry the current state of its work items as fields, and any such view MUST be a projection derived from the work item records.

**P8-3-11** (MUST) [D] Where a case is reopened, the component MUST retain the prior `closed_at` and `completion_basis` as a closure episode record and MUST increment `reopen_count`.

**P8-3-12** (MUST) [D] Every closure episode record MUST carry the identifier of the party that reopened the case, the instant of reopening, and a reason drawn from an enumeration declared by the case definition.

**P8-3-13** (MUST NOT) [D] A case MUST NOT carry more than one active `case_state` at any instant.

### 3.3 The work item record

| Field | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `work_item_id` | identifier | yes | 1 | Not possible |
| `definition_ref` | pinned-ref | yes | 1 | Not possible |
| `case_id` | identifier | no | 0..1 | The work item exists outside any case (P8-1-26), not that its case is unknown |
| `stage_id` | identifier | no | 0..1 | The item sits directly in the case plan, not in a nested stage |
| `state` | enum, §5.3 | yes | 1 | Not possible |
| `actor_class` | enum(`human`,`agent`,`either`) | yes | 1 | Not possible; see P8-6-31 |
| `planned_at` | instant | yes | 1 | Not possible; the instant the item entered `pending_gate` |
| `planned_by` | enum(`definition`,`planning_act`,`repetition`) | yes | 1 | Not possible |
| `planning_act_id` | identifier | no | 0..1 | The item was not added by a planning act; MUST be present when `planned_by` is `planning_act` |
| `available_at` | instant | no | 0..1 | The item's entry gate has never been satisfied |
| `candidate_set_id` | identifier | no | 0..1 | No candidate set has been derived; MUST NOT be read as an empty candidate set |
| `holder` | pinned-ref to party | no | 0..1 | No party currently holds the item; MUST NOT be read as unassigned in the sense of never assigned |
| `held_since` | instant | no | 0..1 | No party currently holds the item |
| `lease_expires_at` | instant | no | 0..1 | The hold is not under a lease, which is legal only where P8-6-24 permits |
| `presentation_pin_id` | identifier | no | 0..n | Nothing has been presented for this item |
| `completion_record_id` | identifier | no | 0..1 | The item has not been performed |
| `terminal_state_at` | instant | no | 0..1 | The item has not reached a terminal state |
| `disposition` | enum, §7.2 | no | 0..1 | The item has not reached a terminal state; MUST be present whenever `terminal_state_at` is present |
| `priority` | integer 0..10 | no | 0..1 | The priority is the definition default |
| `due_at` | instant | no | 0..1 | The item has no completion deadline, not that its deadline has passed |
| `start_by` | instant | no | 0..1 | The item has no start deadline |
| `escalation_count` | integer ≥ 0 | yes | 1 | Not possible; zero means never escalated |
| `stale_since` | instant | no | 0..1 | No pinned dependency of the item has been superseded |
| `input_digest` | digest | no | 0..1 | The item has no input payload; MUST be present whenever an input payload exists |
| `input_schema_ref` | pinned-ref | no | 0..1 | The item has no input payload; MUST be present whenever `input_digest` is present |
| `repetition_ordinal` | integer ≥ 1 | no | 0..1 | The item is not a repetition |

**P8-3-14** (MUST) [D] The work item record MUST contain every field marked required in the table in §3.3, with the type, cardinality and absence semantics stated there.

**P8-3-15** (MUST) [S] `priority` MUST be an integer in the inclusive range 0 to 10 where 0 is the highest priority and 10 the lowest, and where the field is absent the effective priority MUST be the value declared by the definition. **Source.** WS-HumanTask 1.1 §4.2 fixes this range and orientation and specifies 5 as the value when priority is not present; this part adopts the range and orientation, and departs by requiring the definition rather than a fixed literal to supply the default, because a definition default of 5 cannot express a work item class that is urgent by nature.

**P8-3-16** (MUST NOT) [D] `holder` MUST NOT be populated in any state other than `allocated`, `reserved`, `in_progress` or `suspended`.

**P8-3-17** (MUST) [D] Where `holder` transitions from a populated value to absent, the component MUST record a release, decline, revocation or expiry event naming the prior holder, and MUST NOT permit the prior holder to become unrecoverable from the record.

**P8-3-18** (MUST) [D] `input_digest` MUST be computed over a canonical form of the input payload declared by `input_schema_ref`, and MUST be recorded at the instant the payload is bound to the work item.

**P8-3-19** (MUST NOT) [D] The work item record MUST NOT carry the input payload itself where that payload contains a fact whose authority belongs to another component, and MUST carry a pinned reference to it.

**P8-3-20** (MUST) [D] `stale_since` MUST be set at the instant the component observes that any pinned dependency of a non terminal work item has been superseded, and MUST NOT be cleared other than by a re-pinning event recorded under P8-6-30.

### 3.4 The candidate set record

| Field | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `candidate_set_id` | identifier | yes | 1 | Not possible |
| `work_item_id` | identifier | yes | 1 | Not possible |
| `derived_at` | instant | yes | 1 | Not possible |
| `derivation_outcome` | enum(`derived`,`derived_empty`,`derivation_failed`,`derivation_partial`) | yes | 1 | Not possible; see §7.3 |
| `members` | pinned-ref to party | no | 0..n | Where `derivation_outcome` is `derived_empty` the set is empty as a determined fact; where the outcome is `derivation_failed` the emptiness is unknown and MUST NOT be read as empty |
| `excluded` | structure: party ref, reason, rule ref | no | 0..n | No party was excluded; distinguished from an empty members list |
| `expression_ref` | pinned-ref | yes | 1 | Not possible; the pinned assignment expression evaluated |
| `org_snapshot_ref` | pinned-ref | yes | 1 | Not possible; the pinned state of the organisational model against which the expression was evaluated |
| `unresolved_group_refs` | pinned-ref to group | no | 0..n | Every group in the result was expanded to parties at derivation |
| `superseded_by` | identifier | no | 0..1 | This is the current candidate set for the work item |

**P8-3-21** (MUST) [D] The candidate set record MUST be immutable once written, and a change of candidacy MUST be represented by a new candidate set record whose predecessor carries `superseded_by`.

**P8-3-22** (MUST) [S] `derivation_outcome` MUST distinguish a determined empty set from a failed derivation, and the component MUST NOT record `derived_empty` where the evaluation of the assignment expression or the read of the organisational model did not complete. **Source.** This is a deliberate departure from WS-HumanTask 1.1 §3.5.1, which requires that a failed people query be treated as a people query returning an empty result set. §11.2 gives the reason and §10.4 records the conflict.

**P8-3-23** (MUST) [D] `org_snapshot_ref` MUST pin the state of the organisational model used in the derivation, such that the derivation can be re-performed years later and yield the same members.

**P8-3-24** (MUST) [D] Where a group reference is carried unexpanded in `unresolved_group_refs`, the component MUST record the instant of each subsequent expansion of that group and the membership it yielded.

**P8-3-25** (MUST) [D] Every entry in `excluded` MUST name the rule reference that caused the exclusion, and MUST NOT record an exclusion whose cause cannot be attributed to a named rule.

### 3.5 The attention record

Attention is separated from candidacy because a party may need to see work it may not perform, and because a worklist that conflates the two either hides oversight or invites unauthorised claims.

| Field | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `attention_id` | identifier | yes | 1 | Not possible |
| `work_item_id` | identifier | yes | 1 | Not possible |
| `party_ref` | pinned-ref to party | yes | 1 | Not possible |
| `basis` | enum(`candidacy`,`holding`,`oversight`,`escalation`,`delegation`,`explicit_grant`) | yes | 1 | Not possible |
| `may_claim` | boolean | yes | 1 | Not possible; false means the party sees the item and cannot take it |
| `granted_at` | instant | yes | 1 | Not possible |
| `revoked_at` | instant | no | 0..1 | Attention is current |

**P8-3-26** (MUST) [D] The component MUST record attention separately from candidacy, and MUST NOT infer the right to claim from the presence of attention.

**P8-3-27** (MUST) [D] `may_claim` MUST reflect the component's own eligibility determination and MUST NOT be treated as an authorisation decision, which remains the responsibility of `Part 7` at the instant of the act.

**P8-3-28** (MUST NOT) [D] The component MUST NOT revoke attention whose basis is `oversight` on the ground that the work item reached a terminal state, where the case definition declares that oversight persists to case closure.

### 3.6 The presentation pin record

This record is the answer to what the performer saw. Without it a completion record asserts a judgement whose object cannot be established.

| Field | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `presentation_pin_id` | identifier | yes | 1 | Not possible |
| `work_item_id` | identifier | yes | 1 | Not possible |
| `presented_to` | pinned-ref to party | yes | 1 | Not possible |
| `presented_at` | instant | yes | 1 | Not possible |
| `instruction_refs` | pinned-ref to document | no | 0..n | No governing instruction was presented; MUST NOT be read as the instruction being unavailable |
| `definition_version_ref` | pinned-ref | yes | 1 | Not possible |
| `reference_set_refs` | pinned-ref | no | 0..n | No reference or master data set informed the presentation |
| `schema_refs` | pinned-ref | no | 0..n | No schema governed the presented payload |
| `payload_digest` | digest | no | 0..1 | No payload was presented |
| `available_outcomes` | string | yes | 1..n | Not possible; see P8-3-31 |
| `rendering_ref` | pinned-ref | no | 0..1 | The presentation was rendered by a means this component does not govern |
| `locale` | language tag | no | 0..1 | The presentation used the deployment default locale |
| `withdrawn_at` | instant | no | 0..1 | The presentation was not superseded before the act |

**P8-3-29** (MUST) [D] The component MUST write a presentation pin record before accepting any act that expresses a judgement, and MUST NOT accept such an act where no presentation pin exists for the acting party and that work item.

**P8-3-30** (MUST) [S] Every reference in a presentation pin MUST be a pinned reference resolvable to the version in force at `presented_at`, and MUST NOT resolve to the current version. **Source.** This is a deliberate departure from CMMN 1.1 §5.3.2.1, which states that versioning of case file item instances is outside its scope and that a reference MUST refer to the latest, most current version of the information element. §10.4 records the conflict; §12.2 states the boundary with `Part 1` that makes the departure implementable.

**P8-3-31** (MUST) [D] `available_outcomes` MUST enumerate every outcome the acting party could have selected at `presented_at`, and MUST contain at least one member.

**P8-3-32** (MUST) [D] Where `available_outcomes` contains exactly one member, the component MUST record the presentation as constrained and MUST make that constraint retrievable with the completion record.

**P8-3-33** (MUST NOT) [D] A presentation pin MUST NOT be modified after it is written, and a change in what is presented MUST produce a new presentation pin whose predecessor carries `withdrawn_at`.

**P8-3-34** (SHOULD) [D] A presentation pin SHOULD carry sufficient reference for a reader to reconstruct the presentation without the component running, and where the rendering technology prevents this the record SHOULD state that the reconstruction is partial.

### 3.7 The completion record

| Field | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `completion_record_id` | identifier | yes | 1 | Not possible |
| `work_item_id` | identifier | yes | 1 | Not possible |
| `performed_by` | pinned-ref to party | yes | 1 | Not possible |
| `performed_at` | instant | yes | 1 | Not possible |
| `actor_class_used` | enum(`human`,`agent`) | yes | 1 | Not possible |
| `invocation_ref` | pinned-ref | no | 0..1 | No model or agent invocation contributed; MUST be present when `actor_class_used` is `agent` |
| `outcome` | string from definition enumeration | no | 0..1 | The definition declares no outcome enumeration, or the disposition is a non performance disposition; MUST NOT be read as an absent decision where `disposition` is `completed` |
| `disposition` | enum, §7.2 | yes | 1 | Not possible |
| `presentation_pin_id` | identifier | yes | 1 | Not possible |
| `choice_breadth` | integer ≥ 1 | yes | 1 | Not possible; a value of 1 means the performer had no alternative |
| `output_digest` | digest | no | 0..1 | The act produced no output payload |
| `output_schema_ref` | pinned-ref | no | 0..1 | No output payload; MUST be present when `output_digest` is present |
| `authorisation_ref` | pinned-ref | yes | 1 | Not possible; the reference to the authorisation decision that permitted the act |
| `stale_acknowledged` | boolean | no | 0..1 | The item was not stale at completion; MUST be present when `stale_since` was populated |
| `working_duration` | duration | no | 0..1 | Elapsed working time was not measured, not that it was zero |
| `rationale` | text | no | 0..1 | No rationale was captured; MUST be present where the definition requires it or where `disposition` is `undecidable` |
| `on_behalf_of` | pinned-ref to party | no | 0..1 | The performer acted for itself |
| `delegation_chain` | pinned-ref to party | no | 0..n | The item was not delegated |

**P8-3-35** (MUST) [D] The completion record MUST be immutable once written, and a correction MUST be expressed as a new completion record that supersedes it with the reason for the correction and the identity of the correcting party.

**P8-3-36** (MUST) [D] `choice_breadth` MUST equal the count of members of `available_outcomes` in the referenced presentation pin at `performed_at`.

**P8-3-37** (MUST) [D] `authorisation_ref` MUST reference the authorisation decision obtained from `Part 7` for this act, and MUST NOT reference a decision obtained for a different act, a different party or a different work item.

**P8-3-38** (MUST NOT) [D] The component MUST NOT write a completion record whose `disposition` is `completed` where the definition declares an outcome enumeration and `outcome` is absent.

**P8-3-39** (MUST) [D] Where `disposition` is `undecidable`, the completion record MUST carry `rationale` and MUST carry the enumerated reason the performer could not decide, drawn from the enumeration in §7.2.4.

**P8-3-40** (MUST NOT) [D] The component MUST NOT record `actor_class_used` as `human` where the act was produced by a model invocation, and MUST NOT record it as `agent` where a person selected the outcome.

### 3.8 The planning act record

| Field | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `planning_act_id` | identifier | yes | 1 | Not possible |
| `case_id` | identifier | yes | 1 | Not possible |
| `stage_id` | identifier | no | 0..1 | The item was added to the case plan directly |
| `performed_by` | pinned-ref to party | yes | 1 | Not possible |
| `performed_at` | instant | yes | 1 | Not possible |
| `discretionary_item_ref` | pinned-ref | yes | 1 | Not possible |
| `applicability_verdict` | enum, §7.4 | yes | 1 | Not possible |
| `items_created` | identifier | yes | 1..n | Not possible |
| `authorisation_ref` | pinned-ref | yes | 1 | Not possible |
| `rationale` | text | no | 0..1 | No rationale captured; MUST be present where the case definition requires it |

**P8-3-41** (MUST) [D] Every item added to a running case plan MUST be traceable to exactly one planning act record.

**P8-3-42** (MUST) [S] `applicability_verdict` MUST record the verdict obtained when the applicability rule of the discretionary item was evaluated, including any non verdict, and the component MUST NOT permit a planning act to proceed on an unrecorded verdict. **Source.** CMMN 1.1 §5.4.9.3 and §8.6.5 define applicability rules for discretionary items; neither specifies what happens when an applicability rule cannot be evaluated.

**P8-3-43** (MUST NOT) [D] A planning act record MUST NOT be deleted when the items it created are withdrawn, because the fact that the plan was extended is itself evidence.

### 3.9 The case file and its slots

The constraints here exist to prevent the case from becoming the system's integration point. They are the mechanism by which §1.3's third failure is prevented.

| Field | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `slot_id` | identifier | yes | 1 | Not possible |
| `case_id` | identifier | yes | 1 | Not possible |
| `path` | stable path | yes | 1 | Not possible |
| `slot_type_ref` | pinned-ref to schema | yes | 1 | Not possible |
| `multiplicity` | enum(`0..1`,`1`,`0..n`,`1..n`) | yes | 1 | Not possible |
| `slot_state` | enum(`empty`,`populated`,`superseded`,`discarded`,`unresolvable`) | yes | 1 | Not possible |
| `value_kind` | enum(`literal`,`pinned_ref`,`content_address`) | no | 0..1 | The slot is `empty` |
| `value` | per `value_kind` | no | 0..n | The slot is `empty` or `discarded`; the two MUST be distinguishable |
| `populated_at` | instant | no | 0..1 | The slot has never been populated |
| `populated_by` | pinned-ref to party | no | 0..1 | The slot has never been populated |
| `discarded_at` | instant | no | 0..1 | The slot has not been discarded |
| `authority_component` | identifier | no | 0..1 | This component is the authority for the value |

**P8-3-44** (MUST) [D] The case file MUST distinguish a slot that has never been populated from a slot that was populated and emptied, and MUST NOT represent both as an absent value.

**P8-3-45** (MUST) [D] Every case file slot MUST declare a type by reference to `Part 9`, and the component MUST reject population of a slot whose value does not validate against that type.

**P8-3-46** (MUST NOT) [D] A case file slot MUST NOT hold a literal copy of a fact for which `authority_component` names another component, and MUST hold a pinned reference instead.

**P8-3-47** (MUST) [D] Where a slot's value is a pinned reference and the referenced object has been superseded, `slot_state` MUST become `superseded` and the slot MUST retain the reference to the version originally pinned.

**P8-3-48** (MUST) [D] Where a slot's value is a pinned reference or content address that no longer resolves, `slot_state` MUST become `unresolvable`, and the component MUST NOT report the slot as `empty`.

**P8-3-49** (MUST NOT) [D] The component MUST NOT permit an undeclared slot to be created at runtime except where the case definition declares an extension point, and where it does, the created slot MUST still satisfy P8-3-45.

**P8-3-50** (MUST) [D] Every population, supersession and discard of a slot MUST be recorded as an event carrying the acting party, the instant and the prior state.

**P8-3-51** (MUST NOT) [D] The component MUST NOT permit a slot to be read by another component as a means of obtaining a fact that component owns, and slot reads by other components MUST be limited to facts this component owns.

### 3.10 The milestone achievement record

| Field | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `milestone_achievement_id` | identifier | yes | 1 | Not possible |
| `case_id` | identifier | yes | 1 | Not possible |
| `milestone_definition_ref` | pinned-ref | yes | 1 | Not possible |
| `achieved_at` | instant | no | 0..1 | The milestone has not been achieved; MUST NOT be read as unachievable |
| `state` | enum, §5.5 | yes | 1 | Not possible |
| `triggering_evaluation_id` | identifier | no | 0..1 | The milestone was achieved by administrative act rather than by gate satisfaction |
| `revoked_at` | instant | no | 0..1 | The achievement has not been revoked |

**P8-3-52** (MUST) [D] A milestone achievement MUST be recorded as an event and MUST NOT be represented solely as a derived predicate over work item states, because the conditions that produced it may later cease to hold.

**P8-3-53** (MUST) [D] Where an achieved milestone is revoked, the component MUST retain the original achievement record and MUST NOT delete it.

**P8-3-71** (MUST) [D] Every revocation of a milestone achievement MUST record the revoking party and the reason for revocation.

### 3.11 The gate and gate evaluation records

| Field | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `gate_id` | identifier | yes | 1 | Not possible |
| `guarded_item_id` | identifier | yes | 1 | Not possible |
| `kind` | enum(`entry`,`exit`) | yes | 1 | Not possible |
| `trigger_refs` | pinned-ref | no | 0..n | The gate has no trigger and depends on its condition alone; see P8-6-15 |
| `condition_ref` | pinned-ref to rule | no | 0..1 | The gate has no condition and is satisfied by its triggers alone |
| `gate_state` | enum(`unevaluated`,`satisfied`,`unsatisfied`,`indeterminate`) | yes | 1 | Not possible |
| `last_evaluation_id` | identifier | no | 0..1 | The gate has never been evaluated |

| Field (evaluation) | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `gate_evaluation_id` | identifier | yes | 1 | Not possible |
| `gate_id` | identifier | yes | 1 | Not possible |
| `evaluated_at` | instant | yes | 1 | Not possible |
| `triggering_event_id` | identifier | yes | 1 | Not possible |
| `snapshot_ref` | pinned-ref | yes | 1 | Not possible; the immutable case state the evaluation read |
| `verdict` | enum, §7.4 | yes | 1 | Not possible |
| `rule_engine_ref` | pinned-ref | no | 0..1 | The gate had no condition |
| `non_verdict_reason` | enum, §7.4 | no | 0..1 | The verdict was `satisfied` or `unsatisfied` |
| `evaluation_duration` | duration | no | 0..1 | Duration was not measured |

**P8-3-54** (MUST) [D] Every gate evaluation MUST be recorded, including evaluations that returned `unsatisfied` and evaluations that returned a non verdict.

**P8-3-55** (MUST) [D] `snapshot_ref` MUST pin the case state read by the evaluation such that re-evaluating the condition against that snapshot years later yields the same verdict, subject to the determinism requirement of `Part 2`.

**P8-3-56** (MUST NOT) [S] A gate evaluation record MUST NOT record `unsatisfied` where the verdict returned by `Part 2` was a non verdict. **Source.** This is a deliberate departure from WS-HumanTask 1.1 §4.8.1, which requires that an error during condition evaluation be treated as the condition having evaluated to false. §11.2 gives the reason.

**P8-3-57** (MUST) [D] `triggering_event_id` MUST identify the single event that caused the evaluation, so that the set of evaluations arising from one event is recoverable from the record.

### 3.12 The choice resolution record

| Field | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `choice_resolution_id` | identifier | yes | 1 | Not possible |
| `kind` | enum(`claim_race`,`alternative_items`,`user_event_selection`) | yes | 1 | Not possible |
| `case_id` | identifier | no | 0..1 | The choice was not within a case |
| `alternatives` | identifier | yes | 2..n | Not possible; a choice with fewer than two alternatives is not a choice |
| `taken` | identifier | yes | 1 | Not possible |
| `resolved_at` | instant | yes | 1 | Not possible |
| `resolved_by` | pinned-ref to party | no | 0..1 | The resolution was caused by an event rather than a party |
| `resolving_event_id` | identifier | no | 0..1 | The resolution was caused by a party rather than an event |

**P8-3-58** (MUST) [D] Every resolved deferred choice MUST produce a choice resolution record naming every alternative that was available at `resolved_at`.

**P8-3-59** (MUST) [D] Every alternative named in `alternatives` and not named in `taken` MUST receive the disposition `withdrawn_by_resolution`, and MUST NOT receive a disposition that attributes the non selection to the alternative's own gate or to any party's decision.

**P8-3-60** (MUST) [D] Exactly one of `resolved_by` and `resolving_event_id` MUST be present.

### 3.13 The case role binding record

| Field | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `binding_id` | identifier | yes | 1 | Not possible |
| `case_id` | identifier | yes | 1 | Not possible |
| `role_ref` | pinned-ref | yes | 1 | Not possible |
| `party_ref` | pinned-ref to party | yes | 1 | Not possible |
| `bound_at` | instant | yes | 1 | Not possible |
| `bound_by` | pinned-ref to party | yes | 1 | Not possible |
| `unbound_at` | instant | no | 0..1 | The binding is current |
| `unbound_reason` | enum, declared by definition | no | 0..1 | The binding is current; MUST be present when `unbound_at` is present |

**P8-3-61** (MUST) [S] A case role binding MUST be scoped to one case instance and MUST NOT be read as a statement about the party's roles outside that case. **Source.** CMMN 1.1 §5.2.2 states that assignment of roles to participants is not within CMMN's scope; this part specifies the binding and confines it to the case instance.

**P8-3-62** (MUST) [D] The component MUST retain unbound role bindings for the life of the case, because a determination made by a party in a role is unreadable once the binding that authorised it is gone.

**P8-3-63** (MUST) [D] Where a case definition declares a maximum cardinality for a role, the component MUST enforce it at binding time and MUST record the rejection of a binding that would breach it.

### 3.14 The escalation record

| Field | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `escalation_id` | identifier | yes | 1 | Not possible |
| `work_item_id` | identifier | yes | 1 | Not possible |
| `deadline_kind` | enum(`start`,`completion`,`custom`) | yes | 1 | Not possible |
| `breached_at` | instant | yes | 1 | Not possible |
| `effect` | enum(`notify`,`add_attention`,`raise_priority`,`extend_candidate_set`,`reassign`,`expire`) | yes | 1..n | Not possible |
| `prior_candidate_set_id` | identifier | no | 0..1 | The escalation did not alter candidacy |
| `prior_holder` | pinned-ref to party | no | 0..1 | The escalation did not alter the holder |
| `authorisation_ref` | pinned-ref | no | 0..1 | The effect required no authorisation decision; MUST be present where the effect is `reassign` or `expire` |

**P8-3-64** (MUST) [D] An escalation MUST NOT have the effect of performing the work, and the component MUST NOT write a completion record whose `performed_by` is derived from an escalation.

**P8-3-65** (MUST) [D] Where an escalation alters candidacy or the holder, the record MUST retain the prior candidate set identifier or prior holder, so that the reassignment is visible as a reassignment rather than as an original assignment.

### 3.15 Mutability, versioning and the evidentiary constraint

**P8-3-66** (MUST NOT) [D] Candidate set records, presentation pin records, completion records, gate evaluation records, planning act records, choice resolution records, milestone achievement records and escalation records MUST NOT be updated after they are written.

**P8-3-67** (MUST) [D] Where the current value of a mutable field of a case or work item changes, the component MUST retain the prior value with the instant of change and the cause, such that the value of that field at any past instant is recoverable.

**P8-3-68** (MUST) [D] The component MUST be implementable over a store in which no written record is subsequently modified, with current state read as a projection over appended records.

**P8-3-69** (MUST) [D] The component MUST version its own record schemas and MUST record, for every record it writes, the version of the record schema under which it was written.

**P8-3-70** (MUST NOT) [D] The component MUST NOT reinterpret a record written under an earlier record schema version according to a later version's semantics, and MUST resolve the record under the schema version it declares.

---

## 4. Interfaces

### 4.1 General interface rules

**P8-4-01** (MUST) [D] Every operation the component accepts MUST be defined in terms of the records of §3 and MUST state which records it creates, which fields it changes and which events it emits.

**P8-4-02** (MUST) [D] Every operation that changes state MUST accept an idempotency key supplied by the caller, and MUST return the result of the original application when invoked again with the same key and the same arguments.

**P8-4-03** (MUST) [D] Every operation invoked with a previously seen idempotency key and different arguments MUST be rejected with the outcome `idempotency_conflict` and MUST NOT be applied.

**P8-4-04** (MUST) [D] Every operation that expresses or records a human act MUST carry the acting party identity, and the component MUST NOT infer the acting party from a session, a connection or a caller identity that is not the acting party.

**P8-4-05** (MUST) [D] Every operation that changes the holder, disposition or plan of a work item, or the state of a case, MUST obtain an authorisation decision from `Part 7` before applying, and MUST record the reference to that decision.

**P8-4-06** (MUST NOT) [D] The component MUST NOT expose any operation that writes a case file slot whose `authority_component` names another component.

**P8-4-07** (MUST) [D] Every operation MUST return exactly one outcome value from the taxonomy in §7, and MUST NOT return a success outcome where the requested change was not applied.

**P8-4-08** (MUST) [D] Every rejected operation MUST be recorded with the requesting party, the instant, the arguments digest and the rejection outcome, because a pattern of rejected claims is evidence.

### 4.2 Operations accepted

The tables state, for each operation, the states from which it is legal, who may invoke it, and whether it is synchronous. *Synchronous* means the caller receives the outcome of the state change in the same interaction. *Asynchronous* means the caller receives an acknowledgement and the outcome is delivered as an event.

#### 4.2.1 Work item participant operations

| Operation | Legal from | Invocable by | Mode |
|---|---|---|---|
| `claim` | `offered` | a member of the current candidate set | synchronous |
| `accept` | `allocated` | the current holder | synchronous |
| `start` | `reserved`, `allocated` | the current holder | synchronous |
| `release` | `reserved`, `in_progress` | the current holder, a business administrator | synchronous |
| `decline` | `offered`, `allocated` | a member of the current candidate set, the current holder | synchronous |
| `suspend` | `reserved`, `in_progress` | the current holder, a business administrator | synchronous |
| `resume` | `suspended` | the party that suspended, a business administrator | synchronous |
| `defer` | `in_progress` | the current holder | synchronous |
| `complete` | `in_progress` | the current holder | synchronous |
| `report_undecidable` | `in_progress` | the current holder | synchronous |
| `report_not_applicable` | `in_progress` | the current holder | synchronous |
| `fail` | `in_progress` | the current holder | synchronous |
| `delegate` | `reserved`, `in_progress` | the current holder, a business administrator | synchronous |
| `forward` | `offered`, `reserved`, `in_progress` | as constrained by the definition | synchronous |
| `add_comment` | any non terminal state | a party holding attention | synchronous |
| `attach_artifact` | any non terminal state | a party holding attention | synchronous |
| `set_priority` | any non terminal state | a business administrator, the current holder | synchronous |

**P8-4-09** (MUST) [D] The component MUST reject any participant operation invoked from a state not listed as legal for that operation, with the outcome `illegal_transition`, and MUST NOT silently coerce the work item into a state from which the operation would be legal.

**P8-4-10** (MUST) [D] `claim` MUST be atomic with respect to every other `claim` on the same work item, such that exactly one claim succeeds and every other returns `already_claimed`.

**P8-4-11** (MUST) [D] `decline` MUST remove the declining party from the candidate set for the remainder of the work item's life, and MUST NOT permit that party to claim the same work item subsequently.

**P8-4-12** (MUST) [D] `decline` by the last remaining member of a candidate set MUST transition the work item to `unassignable` and MUST NOT transition it to a terminal state.

**P8-4-13** (MUST) [D] `report_undecidable` MUST be available on every work item definition whose actor class permits a human performer, and MUST NOT be removable by definition. **Note.** No consulted specification provides a human non result of this kind; §7.2.4 and §11.2 give the reason it is mandatory rather than optional.

**P8-4-14** (MUST) [D] `defer` MUST require a resumption condition expressed as a trigger or an instant, and MUST be rejected where neither is supplied.

**P8-4-15** (MUST) [D] `delegate` MUST retain the delegating party in `delegation_chain` and MUST NOT replace it.

**P8-4-16** (MUST) [S] `forward` MUST record the transfer of accountability, and the component MUST NOT treat `forward` and `delegate` as the same operation. **Source.** WS-HumanTask 1.1 §4.10.3 treats delegation and forwarding within one subsection; this part separates them because the accountability difference is what an auditor reads.

**P8-4-17** (MUST NOT) [D] `set_priority` MUST NOT alter any deadline, and the component MUST NOT derive a deadline from a priority.

#### 4.2.2 Work item administrative operations

| Operation | Legal from | Invocable by | Mode |
|---|---|---|---|
| `revoke_hold` | `allocated`, `reserved`, `in_progress`, `suspended` | a business administrator | synchronous |
| `reassign` | `offered`, `allocated`, `reserved`, `in_progress`, `suspended` | a business administrator | synchronous |
| `rederive_candidates` | `offered`, `unassignable`, `allocated` | a business administrator | synchronous |
| `skip` | `pending_gate`, `gate_indeterminate`, `unassignable`, `offered`, `allocated`, `reserved` | a business administrator, where the definition permits skipping | synchronous |
| `withdraw` | any non terminal state | a business administrator, the owning case | synchronous |
| `repin` | any non terminal state where `stale_since` is populated | a business administrator | synchronous |
| `recover` | `error` | a business administrator | synchronous |
| `abandon` | `error` | a business administrator | synchronous |

**P8-4-18** (MUST) [S] `skip` MUST be rejected where the work item definition does not declare the item skippable, and the component MUST NOT infer skippability from the absence of a declaration. **Source.** WS-HumanTask 1.1 §3.8.2 carries a skipable indicator in task context; this part requires the declaration to be explicit rather than defaulted.

**P8-4-19** (MUST) [D] `withdraw` MUST record a withdrawal reason from the enumeration in §7.2.3.

**P8-4-20** (MUST) [D] `repin` MUST create a new presentation pin and MUST invalidate every presentation pin written before it for that work item.

**P8-4-21** (MUST NOT) [D] An administrative operation MUST NOT write a completion record.

#### 4.2.3 Case operations

| Operation | Legal from | Invocable by | Mode |
|---|---|---|---|
| `open_case` | none, creates | an authorised party or an inbound work request | synchronous |
| `bind_role` | `active`, `suspended` | an authorised party | synchronous |
| `unbind_role` | `active`, `suspended` | an authorised party | synchronous |
| `plan_item` | `active` | a party bound to a role authorised to plan | synchronous |
| `raise_user_event` | `active` | a party bound to a role authorised for that event | synchronous |
| `suspend_case` | `active` | an authorised party | synchronous |
| `resume_case` | `suspended` | an authorised party | synchronous |
| `terminate_case` | `active`, `suspended` | an authorised party | synchronous |
| `close_case` | `completed`, `terminated`, `failed` | an authorised party | synchronous |
| `reopen_case` | `completed`, `terminated`, `failed` | an authorised party | synchronous |
| `populate_slot` | `active` | a party holding attention on an item that writes the slot | synchronous |
| `discard_slot` | `active` | an authorised party | synchronous |

**P8-4-22** (MUST) [S] `raise_user_event` MUST be restricted to the roles the case definition authorises for that event, and the component MUST record the rejection of an unauthorised attempt. **Source.** CMMN 1.1 §5.4.2.2 carries `authorizedRoleRefs` on UserEventListener for this purpose.

**P8-4-23** (MUST) [D] `reopen_case` MUST require a reason and MUST NOT be available from `closed`. **Note.** No consulted specification supplies a reopening mechanism; CMMN 1.1 §8.4.1 provides no transition out of `closed`, and §13.2 records this as a decision of this part.

**P8-4-24** (MUST NOT) [D] `close_case` MUST NOT be legal from `active` or `suspended`, so that closure cannot bypass completion or termination.

**P8-4-25** (MUST) [D] `terminate_case` MUST withdraw every non terminal work item of the case with the reason `case_terminated`, and MUST NOT complete them.

#### 4.2.4 Query operations

**P8-4-26** (MUST) [D] The component MUST expose a worklist query returning the work items on which a stated party holds attention, and MUST return `may_claim` with each item.

**P8-4-27** (MUST) [D] The component MUST expose a point in time query returning the state of a case, work item or slot as at a stated past instant.

**P8-4-28** (MUST NOT) [D] A query MUST NOT change any state other than a read audit record, and MUST NOT extend a lease.

**P8-4-29** (MUST) [D] Every worklist query result MUST carry the instant at which it was computed, because a worklist is a projection and a stale worklist that does not say so causes claims that fail.

**P8-4-30** (SHOULD) [D] A worklist query SHOULD be answerable without reading the payload of any work item, so that presentation cost does not attach to list retrieval.

### 4.3 Events emitted

**P8-4-31** (MUST) [D] The component MUST emit an event for every state transition of a case, work item, case file slot, milestone and gate.

**P8-4-32** (MUST) [D] Every emitted event MUST carry the identifier of the record it concerns, the prior state, the new state, the instant, the causing party or causing event, and the identifier of the event itself.

**P8-4-33** (MUST) [D] Every emitted event MUST be delivered to `Part 3` at least once, and the component MUST retain the event until delivery is acknowledged.

**P8-4-34** (MUST) [D] Emitted events MUST be totally ordered within a single case instance, and the component MUST expose that order.

**P8-4-35** (MUST NOT) [D] The component MUST NOT emit an event describing a state change that was not applied.

**P8-4-36** (MUST) [D] Where the component emits an event carrying a non result, the event MUST carry the non result as its own value and MUST NOT encode it as a success or a failure.

**P8-4-37** (MUST) [D] The component MUST emit a distinct event class for gate indeterminacy, candidate derivation failure and human undecidability, so that a consumer can subscribe to non results without parsing outcomes.

**P8-4-38** (SHOULD) [D] The component SHOULD emit an event when a work item becomes stale, so that a holder can be told before completing work against a superseded definition.

### 4.4 What the component reads from other components

| Read | Component | Pinning requirement | On failure |
|---|---|---|---|
| Case and work item definitions | `Part 4` | pinned at instantiation | reject instantiation; do not instantiate against an unpinnable definition |
| Party, group, role, org unit, capability, calendar | `Part 10` | snapshot pinned per derivation | record `derivation_failed`; do not treat as empty |
| Gate condition verdict | `Part 2` | rule version pinned per evaluation | record the non verdict; do not treat as unsatisfied |
| Outcome selection where delegated | `Part 5` | decision version pinned per selection | record `selection_unavailable`; do not select a default |
| Authorisation decision | `Part 7` | policy version pinned per decision | deny the act; do not permit on failure |
| Schema for payload and slot validation | `Part 9` | schema version pinned per validation | reject the payload; do not accept unvalidated |
| Instruction and procedure text | `Part 1` | version in force at presentation | do not present; do not present current in place of pinned |
| Attachment content address | `Part 11` | content address is inherently pinned | record `unresolvable`; do not report absent |
| Model or agent invocation record | `Part 13` | invocation reference pinned | reject the completion; do not attribute to a person |

**P8-4-39** (MUST) [D] The component MUST treat every read in the table in §4.4 as fallible, and MUST apply the stated failure behaviour rather than a default value.

**P8-4-40** (MUST NOT) [D] The component MUST NOT permit an act to proceed on the failure of an authorisation read, and MUST deny.

**P8-4-41** (MUST NOT) [D] The component MUST NOT cache a read from another component beyond the pinning scope stated in §4.4 without recording the cache instant and treating the cached value as pinned at that instant.

### 4.5 What a caller may and may not assume

**P8-4-42** (MUST) [D] A caller MAY assume that a synchronous operation returning a success outcome has durably applied the state change before returning.

**P8-4-43** (MUST NOT) [D] A caller MUST NOT assume that a work item present in a worklist result is still claimable, and the component MUST NOT be required to prevent a claim from failing on that ground.

**P8-4-44** (MUST NOT) [D] A caller MUST NOT assume that an absent field means a false, zero or empty value, and the component MUST publish the absence semantics of §3 as part of its interface contract.

**P8-4-45** (MUST NOT) [D] A caller MUST NOT assume that a gate that has not fired is a gate that evaluated to unsatisfied, and the component MUST expose `unevaluated` and `indeterminate` as distinct from `unsatisfied`.

**P8-4-46** (MUST) [D] A caller MAY assume that a completion record, once returned, is immutable and that any correction will appear as a superseding record.

**P8-4-47** (MUST NOT) [D] A caller MUST NOT assume any ordering between events of different case instances.

---

## 5. State model

### 5.1 General rules

**P8-5-01** (MUST) [D] Every state named in this part MUST appear in a state table in this section with its legal transitions, the trigger of each transition and whether the state is terminal.

**P8-5-02** (MUST NOT) [D] The component MUST NOT admit a transition not listed in this section, and MUST NOT admit a transition into a terminal state from which any listed transition departs.

**P8-5-03** (MUST) [D] Every transition MUST record its trigger, the instant, the acting party where one acted, and the prior state.

**P8-5-04** (MUST NOT) [D] The component MUST NOT represent two states of one entity as simultaneously current.

**P8-5-05** (MUST) [D] Where a transition is refused because it is illegal, the refusal MUST be recorded and MUST NOT be silently discarded.

### 5.2 Case instance lifecycle

| State | Meaning | Terminal |
|---|---|---|
| `active` | The case is open and its plan may evolve | no |
| `suspended` | The case is open, no work may proceed, the plan may not evolve | no |
| `completed` | Every required item reached a terminal state and the completion criterion held | no |
| `terminated` | The case was ended by act or by exit gate before completion | no |
| `failed` | The case cannot proceed and cannot complete for a recorded reason | no |
| `closed` | The case is final and admits no further change | yes |

| From | To | Trigger |
|---|---|---|
| — | `active` | `open_case` |
| `active` | `suspended` | `suspend_case` |
| `suspended` | `active` | `resume_case` |
| `active` | `completed` | completion criterion satisfied (§6.9) |
| `active` | `terminated` | `terminate_case`, or case exit gate satisfied |
| `suspended` | `terminated` | `terminate_case` |
| `active` | `failed` | unrecoverable condition recorded under §7.5 |
| `suspended` | `failed` | unrecoverable condition recorded under §7.5 |
| `completed` | `active` | `reopen_case` |
| `terminated` | `active` | `reopen_case` |
| `failed` | `active` | `reopen_case` |
| `completed` | `closed` | `close_case` |
| `terminated` | `closed` | `close_case` |
| `failed` | `closed` | `close_case` |

**P8-5-06** (MUST) [D] `closed` MUST be the only terminal state of a case instance, and the component MUST NOT admit any transition out of `closed`.

**P8-5-07** (MUST) [D] The component MUST distinguish `completed` from `terminated` and MUST NOT report a terminated case as completed in any interface or projection.

**P8-5-08** (MUST) [S] Entry to `suspended` MUST suspend every non terminal work item of the case, and exit from `suspended` MUST restore each such work item to the state it held at suspension. **Source.** CMMN 1.1 §8.4.2 provides `parentSuspend` and `parentResume` transitions for this propagation.

**P8-5-09** (MUST NOT) [D] The component MUST NOT permit a planning act while the case is `suspended`.

**P8-5-10** (MUST) [D] Every case that reaches `completed`, `terminated` or `failed` MUST carry a `completion_basis` from §7.6 before the transition is recorded.

### 5.3 Work item lifecycle

| State | Meaning | Terminal |
|---|---|---|
| `pending_gate` | Planned and instantiated; entry gate not satisfied | no |
| `gate_indeterminate` | Entry gate evaluated to a non verdict; the item is neither admitted nor denied | no |
| `unassignable` | Entry gate satisfied; no eligible candidate exists | no |
| `offered` | Available to two or more candidates; unheld | no |
| `allocated` | Assigned to exactly one party who has not accepted | no |
| `reserved` | Held exclusively by one party who has not started | no |
| `in_progress` | Held and being performed | no |
| `suspended` | Held, not performable, prior state retained | no |
| `deferred` | Held, postponed with a recorded resumption condition | no |
| `error` | A system fault prevents progress; no human act is implied | no |
| `completed` | Performed, with a disposition from §7.2.1 or §7.2.4 | yes |
| `expired` | A deadline passed and the definition declares expiry | yes |
| `withdrawn` | Removed before performance for a reason in §7.2.3 | yes |
| `skipped` | Deliberately not performed by administrative act | yes |
| `failed` | The holder asserted the work cannot be performed | yes |

| From | To | Trigger |
|---|---|---|
| — | `pending_gate` | instantiation from definition, repetition, or planning act |
| `pending_gate` | `offered` | entry gate satisfied and candidate set has two or more members |
| `pending_gate` | `allocated` | entry gate satisfied and the definition allocates to one party |
| `pending_gate` | `reserved` | entry gate satisfied and candidate set has exactly one member and the definition reserves on singleton |
| `pending_gate` | `unassignable` | entry gate satisfied and candidate derivation returned `derived_empty` or every member excluded |
| `pending_gate` | `gate_indeterminate` | entry gate evaluation returned a non verdict |
| `gate_indeterminate` | `pending_gate` | re-evaluation returned `unsatisfied` |
| `gate_indeterminate` | `offered`, `allocated`, `reserved`, `unassignable` | re-evaluation returned `satisfied`, then as for `pending_gate` |
| `gate_indeterminate` | `withdrawn` | administrative disposition of the indeterminacy |
| `unassignable` | `offered`, `allocated`, `reserved` | `rederive_candidates` yielding one or more eligible members |
| `unassignable` | `withdrawn`, `skipped` | administrative act |
| `offered` | `reserved` | `claim` |
| `offered` | `unassignable` | last candidate declined |
| `offered` | `withdrawn` | exit gate satisfied, case terminated, or withdrawal by resolution |
| `offered` | `expired` | deadline breached and definition declares expiry |
| `offered` | `skipped` | `skip` |
| `allocated` | `reserved` | `accept` |
| `allocated` | `in_progress` | `start` |
| `allocated` | `offered` | `decline`, `release`, `revoke_hold` where candidates remain |
| `allocated` | `unassignable` | `decline` where no candidate remains |
| `allocated` | `withdrawn`, `expired`, `skipped` | as for `offered` |
| `reserved` | `in_progress` | `start` |
| `reserved` | `offered` | `release`, `revoke_hold`, lease expiry where candidates remain |
| `reserved` | `unassignable` | `release` or lease expiry where no candidate remains |
| `reserved` | `suspended` | `suspend`, case suspension |
| `reserved` | `withdrawn`, `expired`, `skipped` | as for `offered` |
| `in_progress` | `completed` | `complete`, `report_undecidable`, `report_not_applicable` |
| `in_progress` | `failed` | `fail` |
| `in_progress` | `suspended` | `suspend`, case suspension |
| `in_progress` | `deferred` | `defer` |
| `in_progress` | `offered` | `release`, `revoke_hold` where candidates remain |
| `in_progress` | `unassignable` | `release` where no candidate remains |
| `in_progress` | `error` | system fault |
| `in_progress` | `withdrawn` | exit gate satisfied, case terminated |
| `in_progress` | `expired` | completion deadline breached and definition declares expiry |
| `suspended` | prior state | `resume`, case resumption |
| `suspended` | `withdrawn` | exit gate satisfied, case terminated |
| `deferred` | `in_progress` | resumption condition satisfied |
| `deferred` | `withdrawn` | exit gate satisfied, case terminated |
| `deferred` | `expired` | deadline breached and definition declares expiry |
| `error` | `in_progress` | `recover` |
| `error` | `withdrawn` | `abandon` |

**P8-5-11** (MUST) [D] `completed`, `expired`, `withdrawn`, `skipped` and `failed` MUST be terminal, and the component MUST NOT admit any transition out of them.

**P8-5-12** (MUST) [D] `gate_indeterminate` MUST be a state of the work item distinct from `pending_gate`, and the component MUST NOT collapse the two. **Note.** No consulted specification provides this state; §11.2 gives the reason.

**P8-5-13** (MUST) [S] `unassignable` MUST be a state distinct from `withdrawn`, and the component MUST NOT terminate a work item on the ground that no candidate could be found. **Source.** WS-HumanTask 1.1 §4.10.1 requires nomination where the potential owner query returns an empty set; this part requires a durable state instead, because nomination presumes a nominating authority is always reachable and available.

**P8-5-14** (MUST) [D] `error` MUST have declared exits and MUST NOT be terminal, because a system fault is not a disposition of the work.

**P8-5-15** (MUST) [D] Where a work item enters `suspended`, the component MUST retain the state held immediately before suspension and MUST restore exactly that state on resumption.

**P8-5-16** (MUST) [D] Where a work item is `in_progress` and its holder's hold is revoked, the component MUST retain any partial output produced and MUST make it available to the next holder as an antecedent rather than as the next holder's own work.

**P8-5-17** (MUST NOT) [D] The component MUST NOT transition a work item from `offered` directly to `in_progress`, because doing so leaves no record of who took the item as distinct from who worked it.

**P8-5-18** (MUST) [D] Transitions out of `pending_gate` on gate satisfaction MUST depend only on the candidate set outcome and the definition's distribution mode, and MUST be deterministic given those two.

### 5.4 Case file slot lifecycle

| State | Meaning | Terminal |
|---|---|---|
| `empty` | Declared and never populated | no |
| `populated` | Holds a current value or reference | no |
| `superseded` | Holds a pinned reference whose target has been superseded | no |
| `discarded` | Was populated and has been emptied | no |
| `unresolvable` | Holds a reference or address that no longer resolves | no |

| From | To | Trigger |
|---|---|---|
| — | `empty` | slot declared at case instantiation or at a declared extension point |
| `empty` | `populated` | `populate_slot` |
| `populated` | `populated` | `populate_slot` replacing the value, recorded as an event |
| `populated` | `superseded` | the pinned target is superseded in its owning component |
| `populated` | `discarded` | `discard_slot` |
| `populated` | `unresolvable` | the reference or address ceases to resolve |
| `superseded` | `populated` | `populate_slot` with a new pinned reference |
| `superseded` | `discarded` | `discard_slot` |
| `superseded` | `unresolvable` | the pinned target ceases to resolve |
| `discarded` | `populated` | `populate_slot` |
| `unresolvable` | `populated` | `populate_slot` |

**P8-5-19** (MUST) [D] No slot state MUST be terminal, because a case that reopens may repopulate any slot.

**P8-5-20** (MUST) [D] The component MUST expose `empty`, `discarded` and `unresolvable` as three distinct states through every interface, and MUST NOT map them to a single absent value.

**P8-5-21** (MUST) [S] A transition to `superseded` MUST NOT alter the pinned reference the slot holds. **Source.** This is the point at which this part departs from CMMN 1.1 §5.3.2.1; see §10.4.

### 5.5 Milestone lifecycle

| State | Meaning | Terminal |
|---|---|---|
| `pending` | Declared, gate not satisfied | no |
| `indeterminate` | Gate evaluated to a non verdict | no |
| `achieved` | Gate satisfied and the achievement recorded | no |
| `revoked` | An achievement was recorded and subsequently withdrawn | no |
| `not_achieved` | The case reached a terminal state with the milestone unachieved | yes |

| From | To | Trigger |
|---|---|---|
| — | `pending` | case or stage instantiation |
| `pending` | `achieved` | entry gate satisfied |
| `pending` | `indeterminate` | gate evaluation returned a non verdict |
| `indeterminate` | `pending` | re-evaluation returned `unsatisfied` |
| `indeterminate` | `achieved` | re-evaluation returned `satisfied` |
| `pending` | `not_achieved` | case reached `completed`, `terminated` or `failed` |
| `indeterminate` | `not_achieved` | case reached `completed`, `terminated` or `failed` |
| `achieved` | `revoked` | administrative revocation with reason |
| `revoked` | `achieved` | gate satisfied again, or administrative reinstatement |
| `revoked` | `not_achieved` | case reached a terminal state |

**P8-5-22** (MUST) [D] `not_achieved` MUST be recorded explicitly at case termination, and the component MUST NOT leave an unachieved milestone in `pending` after the case reaches a terminal state, because the absence of an achievement record is otherwise indistinguishable from a milestone that was never declared.

**P8-5-23** (MUST NOT) [S] The component MUST NOT attach work to a milestone. **Source.** CMMN 1.1 §5.4.3 states that no work is directly associated with a Milestone.

### 5.6 Gate lifecycle

| State | Meaning | Terminal |
|---|---|---|
| `unevaluated` | No trigger has fired | no |
| `satisfied` | The most recent evaluation returned satisfied | no |
| `unsatisfied` | The most recent evaluation returned unsatisfied | no |
| `indeterminate` | The most recent evaluation returned a non verdict | no |

| From | To | Trigger |
|---|---|---|
| `unevaluated` | `satisfied`, `unsatisfied`, `indeterminate` | first evaluation |
| `satisfied` | `unsatisfied`, `indeterminate` | re-evaluation, where the gate is re-evaluable |
| `unsatisfied` | `satisfied`, `indeterminate` | re-evaluation |
| `indeterminate` | `satisfied`, `unsatisfied` | re-evaluation |

**P8-5-24** (MUST) [D] `unevaluated` MUST be distinguishable from `unsatisfied` in every projection, because a gate that never fired and a gate that fired and failed have different remedies.

**P8-5-25** (MUST NOT) [D] An entry gate that has reached `satisfied` MUST NOT cause a second admission of the same work item on a later evaluation, and a second admission MUST require a repetition rule.

**P8-5-26** (MUST) [D] The component MUST declare, per gate, whether it is re-evaluable after reaching `satisfied`, and MUST default to not re-evaluable where the definition is silent.

### 5.7 Propagation

**P8-5-27** (MUST) [D] Where a stage transitions to a terminal state, every non terminal item it contains MUST receive a terminal disposition naming the stage transition as its cause.

**P8-5-28** (MUST) [D] Propagation from a container to its contents MUST be recorded per contained item, and MUST NOT be recorded only at the container.

**P8-5-29** (MUST NOT) [D] Propagation MUST NOT convert a non terminal item into `completed`.

**P8-5-30** (MUST) [D] Where a stage is suspended, the suspension MUST propagate to contained items, and resumption MUST restore each contained item's pre-suspension state individually.

---

## 6. Execution semantics

### 6.1 Determinism

**P8-6-01** (MUST) [D] Given the same case definition version, the same sequence of external events with the same instants, and the same pinned reads from other components, the component MUST produce the same sequence of state transitions.

**P8-6-02** (MUST NOT) [D] The component MUST NOT allow the order in which it evaluates the gates triggered by a single event to affect the resulting set of state transitions.

**P8-6-03** (MUST) [P] Where a case definition admits a triggering event under which the resulting set of state transitions depends on gate evaluation order, the component MUST reject that definition at instantiation as non confluent, and MUST record the rejection. **Source.** CMMN 1.1 §8.5 specifies the Sentry but does not specify an evaluation order or a confluence requirement across sentries triggered by one event; the absence is reported in §13.1.

**P8-6-04** (MUST NOT) [D] A gate condition MUST NOT have any effect on state, and the component MUST reject a condition whose evaluation is declared by `Part 2` to have effects.

**P8-6-05** (MUST) [D] The component MUST NOT derive any state transition from the wall clock other than through a declared timer trigger or a declared deadline.

### 6.2 Gate triggering and snapshotting

**P8-6-06** (MUST) [D] A gate MUST be evaluated only on the firing of one of its declared triggers, and MUST NOT be evaluated by polling.

**P8-6-07** (MUST) [D] All gates triggered by one event MUST be evaluated against one immutable snapshot of case state taken at that event, and MUST NOT observe the effects of one another's resulting transitions.

**P8-6-08** (MUST) [D] The snapshot used for an evaluation MUST be retained by reference in the gate evaluation record for as long as the case's retention schedule requires.

**P8-6-09** (MUST) [D] Transitions resulting from the evaluations of one event MUST be applied atomically, such that no observer sees a subset of them.

**P8-6-10** (MUST) [D] Where the transitions resulting from one event themselves fire triggers, the component MUST evaluate the newly triggered gates against a new snapshot taken after the first set is applied, and MUST record the resulting generation ordinal.

**P8-6-11** (MUST) [D] The component MUST declare a finite maximum generation depth for the cascade of gate evaluations arising from one external event.

**P8-6-90** (MUST) [D] The declared maximum generation depth MUST be at least 8, being the smallest depth at which a three level stage nesting carrying entry and exit gates at each level can settle.

**P8-6-91** (MUST) [D] The component MUST record a breach of the declared maximum generation depth as `generation_depth_exceeded` and MUST NOT continue evaluating beyond it.

The maximum itself above the floor of 8 is an implementation decision, because the useful depth depends on the nesting depth of the case models an implementation admits and no single value is correct for all of them.

**P8-6-12** (MUST NOT) [D] The component MUST NOT re-evaluate a gate whose state is `satisfied` and which is declared not re-evaluable.

**P8-6-13** (MUST) [S] A trigger MUST be a declared lifecycle transition of a named item, a declared transition of a named case file slot, a declared elapse of time, or a declared user event, and MUST NOT be an arbitrary change to case state. **Source.** CMMN 1.1 §5.4.6.1 to §5.4.6.3 restricts on parts to these classes of standard event.

**P8-6-14** (MUST) [D] Where a trigger's source item is never instantiated, the gate MUST remain `unevaluated` and the component MUST NOT treat the absent trigger as a fired trigger or as a permanently unsatisfied condition.

**P8-6-15** (MUST) [D] A gate with no declared trigger and a declared condition MUST be evaluated once at the instantiation of the item it guards, and MUST be declared re-evaluable or not re-evaluable by the definition.

### 6.3 Gate conditions and non verdicts

**P8-6-16** (MUST) [D] The component MUST obtain every gate condition verdict from `Part 2` and MUST NOT evaluate the condition itself.

**P8-6-17** (MUST) [D] The component MUST accept and represent every verdict value `Part 2` can return, including values that are neither satisfied nor unsatisfied.

**P8-6-18** (MUST NOT) [D] The component MUST NOT map a non verdict to `unsatisfied`, to `satisfied`, or to a system error.

**P8-6-19** (MUST) [D] Where an entry gate evaluation returns a non verdict, the guarded item MUST enter `gate_indeterminate` and MUST NOT be admitted.

**P8-6-20** (MUST) [D] Where an exit gate evaluation returns a non verdict, the guarded item MUST remain in its current state and MUST NOT be withdrawn.

**P8-6-92** (MUST) [D] Where an exit gate evaluation returns a non verdict, the gate MUST enter `indeterminate`.

**P8-6-93** (MUST) [D] Where any gate evaluation returns a non verdict, the component MUST raise an indeterminacy event naming the gate and the non verdict.

The asymmetry between P8-6-19 and P8-6-20 is deliberate. An indeterminate entry gate that admitted work would start work that may not be warranted; an indeterminate exit gate that withdrew work would destroy work that may be warranted. In both cases the safe action is the one that does not act, but the two safe actions are opposite transitions, and a specification that treats indeterminacy uniformly gets one of them wrong.

**P8-6-21** (MUST) [D] An item in `gate_indeterminate` MUST be visible to a party holding oversight attention, and the component MUST NOT leave an indeterminate gate undisplayed.

**P8-6-22** (MUST) [D] The component MUST declare a re-evaluation policy for indeterminate gates.

**P8-6-94** (MUST) [D] The component MUST record every re-evaluation attempt of an indeterminate gate and its verdict.

**P8-6-95** (MUST) [D] The component MUST record the cessation of re-evaluation of an indeterminate gate, and MUST NOT cease re-evaluation silently.

**P8-6-23** (MUST NOT) [D] The component MUST NOT permit a case to reach `completed` while any entry gate of a required item is `indeterminate`.

### 6.4 Candidate derivation

**P8-6-24** (MUST) [D] Candidate derivation MUST be performed by evaluating a pinned assignment expression against a pinned snapshot of the organisational model, and the result MUST be recorded as a candidate set record.

**P8-6-25** (MUST) [D] The candidate set MUST be pinned at derivation and MUST NOT be re-derived implicitly on read, so that a worklist and a claim decision are made against the same set.

**P8-6-26** (MUST) [D] Where the organisational model changes after derivation, the component MUST NOT alter the candidate set, and a change of candidacy MUST require a recorded re-derivation.

**P8-6-27** (MUST) [S] Where the assignment expression yields a group rather than a set of parties, the component MUST either expand the group at derivation and record the expansion, or carry the group unexpanded and record every subsequent expansion. **Source.** WS-HumanTask 1.1 §3.5.1 permits deferred group resolution for the case where group membership changes frequently.

**P8-6-28** (MUST) [D] Where the derivation of a candidate set does not complete, the component MUST record `derivation_failed` and MUST NOT record an empty candidate set.

**P8-6-96** (MUST) [D] Where a candidate derivation records `derivation_failed`, the component MUST place the work item in `unassignable`.

**P8-6-29** (MUST) [D] Where the derivation completes and yields no member, the component MUST record `derived_empty` and MUST place the item in `unassignable`.

**P8-6-30** (MUST) [D] Where the derivation yields members of whom every one is excluded, the component MUST record the exclusions with their causing rules and MUST place the item in `unassignable` with the outcome `no_eligible_candidate`.

The three preceding clauses distinguish three conditions that a conventional implementation records identically. They have three different remedies: a failed derivation is fixed by repairing the read, a determined empty set is fixed by changing the assignment expression or the organisation, and a fully excluded set is fixed by relieving a segregation of duty constraint or by finding a party outside it. Recording them as one condition means the remedy must be rediscovered every time.

### 6.5 Distribution, the claim race and deferred choice

**P8-6-31** (MUST) [D] The component MUST support offering one work item to a candidate set of two or more members.

**P8-6-97** (MUST) [D] The component MUST support allocating one work item to exactly one party without that party having accepted it.

**P8-6-98** (MUST) [D] The component MUST record which distribution mode was used for every work item that became available.

**P8-6-32** (MUST) [D] Where a work item is offered to two or more candidates, the first successful claim MUST resolve the choice, and the component MUST write a choice resolution record naming the candidate set as the alternatives and the claiming party as taken, with `kind` of `claim_race`.

**P8-6-33** (MUST) [D] Where several alternative work items are simultaneously available and the definition declares that performing one withdraws the others, the component MUST write a choice resolution record with `kind` of `alternative_items` and MUST dispose of the others as `withdrawn_by_resolution`.

**P8-6-34** (MUST NOT) [D] The component MUST NOT record a candidate that did not claim as having declined, and MUST NOT record an unselected alternative as having failed its own gate.

**P8-6-35** (MUST) [S] Where a user event resolves a choice among alternatives, the component MUST record the raising party as `resolved_by`. **Source.** CMMN 1.1 §5.4.2.2 provides the UserEventListener as the means by which a user event enters the case.

**P8-6-36** (MUST) [D] The component MUST make the claim operation linearisable per work item, such that the outcome of concurrent claims is as if they occurred in some serial order.

**P8-6-37** (MUST NOT) [D] The component MUST NOT resolve a claim race by any property of the claimant other than the order of arrival, and where arrival order cannot be established the component MUST reject all contending claims rather than choose.

### 6.6 Eligibility and authorisation

**P8-6-38** (MUST) [D] The component MUST determine eligibility, being membership of the current candidate set and absence from the exclusion list, before requesting an authorisation decision.

**P8-6-39** (MUST) [D] The component MUST request an authorisation decision from `Part 7` for every act that changes holder, disposition or plan, at the instant of the act, and MUST NOT rely on an authorisation decision obtained at derivation.

**P8-6-40** (MUST NOT) [D] The component MUST NOT treat eligibility as authorisation, and MUST NOT treat an authorisation decision as establishing eligibility.

**P8-6-41** (MUST) [D] Where `Part 7` requires a prior participation fact to evaluate a dynamic segregation of duty constraint, the component MUST supply that fact from its own participation record as a pinned attribute, and MUST NOT permit `Part 7` to maintain a second copy of it.

**P8-6-42** (MUST) [D] Where an authorisation decision denies an act, the component MUST record the denial with the decision reference and MUST NOT alter the work item state.

### 6.7 Holding, reservation and leases

**P8-6-43** (MUST) [D] At most one party MUST hold a work item at any instant.

**P8-6-44** (MUST) [D] A hold in `reserved` MUST be subject to a lease with a declared expiry, and on expiry the component MUST return the item to `offered` where candidates remain or to `unassignable` where none remain.

**P8-6-45** (MUST) [D] The lease duration MUST be declared by the work item definition or by a deployment default; the value is an implementation decision because the appropriate duration is a function of the work's expected duration, which the definition knows and this part cannot. Where neither the definition nor a deployment default supplies a value, the component MUST refuse to instantiate the definition rather than hold indefinitely.

**P8-6-46** (MAY) [D] A hold in `in_progress` MAY be exempt from lease expiry, and only where the work item definition declares the exemption.

**P8-6-99** (MUST) [D] Where a hold is exempt from lease expiry, the component MUST record inactivity against that hold.

**P8-6-100** (MUST) [D] Where a hold is exempt from lease expiry, the component MUST raise an escalation on breach of a declared inactivity threshold.

**P8-6-47** (MUST) [D] Lease expiry MUST be recorded as an event naming the prior holder, and MUST NOT be recorded as a release by that holder.

**P8-6-48** (MUST NOT) [D] A read of a work item MUST NOT extend its lease.

### 6.8 Idempotence and repeated invocation

**P8-6-49** (MUST) [D] `claim`, `complete`, `report_undecidable`, `report_not_applicable`, `fail`, `skip` and `withdraw` MUST be idempotent under the same idempotency key, returning the original outcome without applying a second change.

**P8-6-50** (MUST) [D] A repeated `complete` with a different idempotency key on a work item already `completed` MUST be rejected with `illegal_transition` and MUST NOT create a second completion record.

**P8-6-51** (MUST) [D] `add_comment` and `attach_artifact` MUST be idempotent under the same idempotency key, and MUST create a second record under a different key, because two identical comments genuinely added twice are two acts.

**P8-6-52** (MUST) [D] Gate evaluation MUST be idempotent with respect to its triggering event, such that a redelivered event does not produce a second admission.

**P8-6-53** (MUST) [D] The component MUST declare the period for which it retains idempotency keys.

**P8-6-101** (MUST) [D] The component MUST retain every idempotency key for at least the declared retention period.

**P8-6-102** (MUST) [D] The component MUST record that it treated a key presented after the declared retention period as a new invocation.

### 6.9 Case completion

**P8-6-54** (MUST) [S] A case MUST reach `completed` only where every item declared required has reached a terminal state and the case's completion criterion is satisfied. **Source.** CMMN 1.1 §5.4.11.2 defines the RequiredRule and §8.6.1 defines `Stage.autoComplete`, under which only required items must reach a terminal state for automatic completion.

**P8-6-55** (MUST) [D] The component MUST record, for every case that reaches `completed`, whether each required item was `completed`, `skipped`, `withdrawn` or `expired`, and MUST NOT report a case whose required items were skipped as equivalent to one whose required items were performed.

**P8-6-56** (MUST) [S] Where the requiredness of an item is determined by a rule, the component MUST record the verdict of that rule and MUST NOT treat a non verdict as not required. **Source.** CMMN 1.1 §8.6.3 defines the RequiredRule's evaluation but does not specify the behaviour when it cannot be evaluated.

**P8-6-57** (MUST NOT) [D] The component MUST NOT complete a case while any contained item is `in_progress`, `reserved`, `allocated`, `deferred`, `suspended` or `error`.

**P8-6-58** (MUST) [D] Where a case cannot complete because a required item is `unassignable` or its gate is `indeterminate`, the component MUST raise a blocked case event naming the blocking items, and MUST NOT silently leave the case `active`.

### 6.10 Repetition

**P8-6-59** (MUST) [D] Where a work item definition declares a repetition rule, each instantiation MUST be a distinct work item with its own identity, gates, candidate set and disposition.

**P8-6-60** (MUST) [P] The component MUST record the instant at which a repetition rule was evaluated and the verdict it returned, for every instantiation and for the evaluation that produced no further instantiation. **Source.** CMMN 1.1 §5.4.11.3 and §8.6.4 define the RepetitionRule; published implementation documentation records that the instant of evaluation is treated differently across implementations, which is reported in §13.1.

**P8-6-61** (MUST) [D] The component MUST declare a finite maximum repetition count for every definition carrying a repetition rule.

**P8-6-103** (MUST) [D] The component MUST record a breach of the declared maximum repetition count as `repetition_bound_exceeded` and MUST NOT instantiate a further repetition.

The value of the maximum is an implementation decision, because the useful bound is a property of the work rather than of the component.

**P8-6-62** (MUST NOT) [P] A repetition MUST NOT inherit the holder of a prior repetition unless the definition declares retention of the familiar performer, and where it does the component MUST record that the assignment was made on that basis. **Source.** This is the *retain familiar* creation pattern of Russell, ter Hofstede, Edmond and van der Aalst, *Workflow Resource Patterns*, WP 127, 2004.

### 6.11 Actor class and non human performance

**P8-6-63** (MUST) [D] Every work item definition MUST declare an actor class of `human`, `agent` or `either`.

**P8-6-64** (MUST NOT) [D] The component MUST NOT permit a work item whose actor class is `human` to be completed by a non human actor.

**P8-6-65** (MUST) [D] Where a work item is completed by a non human actor, the completion record MUST carry `invocation_ref` to the invocation record held by `Part 13`, and MUST record `actor_class_used` as `agent`.

**P8-6-66** (MUST) [D] Where a work item's purpose is to check a value produced by a non human actor, the definition MUST declare an actor class of `human`, and the component MUST reject a definition that declares otherwise.

**P8-6-67** (MUST NOT) [D] The component MUST NOT auto complete a work item whose purpose is to check a produced value, on any basis including timeout, and MUST expire it instead.

**P8-6-68** (MUST) [D] Where an agent proposes an outcome for a work item of actor class `human`, the presentation pin MUST carry the proposal and MUST record it as a proposal.

**P8-6-104** (MUST) [D] Where a proposal was presented, the completion record MUST record whether the performer accepted it unchanged.

Clause P8-6-68 exists because the difference between a person who decided and a person who accepted a suggestion is the difference between two very different pieces of evidence, and no consulted specification requires the distinction to be recorded.

### 6.12 Concurrency

**P8-6-69** (MUST) [D] Concurrent operations on one work item MUST be serialised, and the component MUST NOT apply two state changing operations to one work item concurrently.

**P8-6-70** (MUST) [D] Concurrent population of one case file slot MUST be serialised, and the component MUST record both attempts with the losing attempt's outcome.

**P8-6-71** (MUST) [D] The component MUST permit concurrent progress on distinct work items of one case, and MUST NOT serialise a whole case for the duration of one work item.

**P8-6-72** (MUST) [P] Where a case definition declares that two work items must not be performed concurrently, the component MUST enforce the constraint by refusing the second start and MUST record the refusal. **Source.** This is the interleaved parallel routing and critical section family of control flow patterns catalogued in Russell, ter Hofstede, van der Aalst and Mulyar, *Workflow Control-Flow Patterns: A Revised View*, BPM-06-22, 2006; this part covers it only for human work items within one case and delegates the general case to `Part 6`.

### 6.13 Time and deadlines

**P8-6-73** (MUST) [D] Every deadline MUST be recorded as an absolute instant computed at the moment the deadline is established, together with the expression from which it was computed.

**P8-6-74** (MUST) [D] Where a deadline is expressed relative to an event, the component MUST record the event whose instant was used as the origin.

**P8-6-75** (MUST) [D] Where a working calendar is applied to a deadline computation, the component MUST pin the calendar version used. **Note.** No consulted specification requires the calendar version to be pinned; without it a deadline breach cannot be re-derived after a holiday schedule changes.

**P8-6-76** (MUST) [D] A deadline breach MUST produce an escalation record whether or not any effect other than notification is declared.

**P8-6-77** (MUST NOT) [S] The component MUST NOT expire a work item on deadline breach unless the definition declares expiry as the effect, and MUST NOT treat expiry as a default. **Source.** WS-HumanTask 1.1 §4.9 provides start and completion deadlines with escalation actions and does not make expiry the default effect.

**P8-6-78** (MUST) [D] Where a case is suspended, deadline clocks for its items MUST be suspended, and the component MUST record the suspended interval and recompute the absolute instant on resumption.

### 6.14 Staleness

**P8-6-79** (MUST) [D] Where any pinned dependency of a non terminal work item is superseded, the component MUST mark the item stale and MUST record the superseding version.

**P8-6-80** (MUST) [D] Where a stale work item is presented, the presentation MUST state that a dependency has been superseded and MUST name it.

**P8-6-81** (MUST) [D] Completion of a stale work item MUST require an explicit acknowledgement recorded in `stale_acknowledged`, and the component MUST reject completion where the acknowledgement is absent.

**P8-6-82** (MUST NOT) [D] The component MUST NOT silently re-pin a stale work item to the current version of a dependency, because doing so changes what the performer is deemed to have seen.

**P8-6-83** (MUST) [D] Where a stale work item is re-pinned, the component MUST create a new presentation pin and MUST record that the prior presentation was withdrawn without being acted on.

### 6.15 Planning

**P8-6-84** (MUST) [S] A planning act MUST be permitted only where the case is `active`, the acting party is bound to a case role the definition authorises to plan, and the applicability rule of the discretionary item returned `satisfied`. **Source.** CMMN 1.1 §8.7 constrains planning by case, stage and task lifecycle state.

**P8-6-85** (MUST NOT) [D] The component MUST NOT permit a planning act where the applicability rule returned a non verdict, and MUST record the refusal with the non verdict.

**P8-6-86** (MUST) [D] An item added by a planning act MUST be subject to the same gates, candidate derivation, authorisation and recording requirements as an item instantiated from the definition.

**P8-6-87** (MUST NOT) [D] A planning act MUST NOT introduce an item that is not declared as a discretionary item of the case definition version pinned by the case.

**P8-6-88** (MUST) [D] Where the case definition is superseded while a case is running, the set of discretionary items available for planning MUST remain that of the pinned version, unless a recorded migration act re-pins the case.

**P8-6-89** (MUST) [D] A migration act that re-pins a running case to a later definition version MUST record the acting party, the reason, the prior and new versions, and the disposition of every item that exists in one version and not the other.

---

## 7. Outcome and failure taxonomy

This section is the load bearing section of this part. Its purpose is to make every value the component can produce representable, so that no non result is coerced into a negative. The organising principle is that three questions must be separately answerable for every outcome: was the work done, is there a business outcome, and is the party that required the work satisfied. A taxonomy that cannot separate those three will collapse at least one non result into a false negative.

### 7.1 Structure

**P8-7-01** (MUST) [D] Every value the component can produce MUST belong to exactly one of the enumerations in §7.2 to §7.7.

**P8-7-02** (MUST NOT) [D] The component MUST NOT return a value outside these enumerations, and MUST NOT extend an enumeration marked closed.

**P8-7-03** (MUST) [D] Every enumeration in this section marked closed MUST be closed, and every enumeration marked open MUST be extended only under §9.

**P8-7-04** (MUST) [D] The component MUST expose, for every outcome value it returns, the three properties in the table in §7.8.

### 7.2 Work item terminal dispositions

The enumeration is closed. Every terminal work item carries exactly one.

#### 7.2.1 Performance dispositions

| Value | Meaning |
|---|---|
| `completed_with_outcome` | Performed, and a business outcome from the definition's enumeration was selected |
| `completed_without_outcome` | Performed, and the definition declares no outcome enumeration |
| `completed_by_agent` | Performed by a declared non human actor with an invocation reference |

#### 7.2.2 Non performance dispositions arising from the work

| Value | Meaning |
|---|---|
| `failed` | The holder asserted the work cannot be performed, for a recorded reason |
| `expired` | A declared deadline passed and the definition declares expiry as the effect |
| `skipped` | A business administrator deliberately did not have the work performed, where the definition permits skipping |

#### 7.2.3 Withdrawal reasons

Where a work item's disposition is `withdrawn`, exactly one withdrawal reason MUST be recorded. The enumeration is closed.

| Value | Meaning |
|---|---|
| `withdrawn_by_resolution` | An alternative was taken in a resolved deferred choice |
| `withdrawn_by_exit_gate` | An exit gate of the item was satisfied |
| `withdrawn_by_container` | A containing stage reached a terminal state |
| `case_terminated` | The case was terminated |
| `withdrawn_by_administration` | A business administrator withdrew the item, with a reason |
| `withdrawn_indeterminate` | An indeterminate gate was administratively disposed of |
| `withdrawn_unassignable` | An unassignable item was administratively disposed of |
| `withdrawn_on_migration` | A migration act re-pinned the case and the item does not exist in the new version |
| `abandoned_after_error` | An item in `error` was abandoned |

#### 7.2.4 Human non results

These are the values a person can produce that are neither performance nor failure. The enumeration is closed. Each is recorded as `completed` at the state level, because the person did what was asked of them, and is distinguished by its disposition.

| Value | Meaning | Reason enumeration required |
|---|---|---|
| `undecidable` | The performer could not reach a decision on the evidence available | yes |
| `not_applicable` | The performer determined the work does not apply to this case | yes |
| `out_of_competence` | The performer determined the decision requires competence they do not hold | no |
| `conflicted` | The performer determined they are conflicted and must not decide | no |

Reasons for `undecidable`, closed enumeration: `evidence_insufficient`, `evidence_contradictory`, `criteria_ambiguous`, `criteria_absent`, `dependency_unresolvable`, `authority_unclear`.

Reasons for `not_applicable`, closed enumeration: `subject_out_of_scope`, `superseded_by_other_work`, `precondition_absent`, `duplicate_of_prior_item`.

**P8-7-05** (MUST) [D] The component MUST provide `undecidable` as a disposition available on every work item whose actor class permits a human performer, and MUST NOT permit a definition to remove it.

**P8-7-06** (MUST NOT) [D] The component MUST NOT map `undecidable` to any value in the definition's business outcome enumeration.

**P8-7-07** (MUST NOT) [D] The component MUST NOT map `undecidable`, `not_applicable`, `out_of_competence` or `conflicted` to `failed`, and MUST NOT report them as system faults.

**P8-7-08** (MUST) [D] A disposition of `conflicted` MUST remove the performer from the candidate set.

**P8-7-33** (MUST) [D] A disposition of `conflicted` MUST cause a re-derivation of the candidate set.

**P8-7-34** (MUST NOT) [D] A disposition of `conflicted` MUST NOT place the work item in a terminal state.

**P8-7-09** (MUST) [D] A disposition of `out_of_competence` MUST cause a re-derivation with the recorded competence requirement, and MUST NOT terminate the work.

**P8-7-10** (MUST) [D] A disposition of `undecidable` MUST require the component to determine, from the definition, whether the work item is thereby closed or a successor work item is required, and MUST record which.

**P8-7-11** (MUST NOT) [D] A disposition of `not_applicable` MUST NOT satisfy a requirement that the work be performed, and where the item is required for case completion the component MUST record the case as completing on a basis of `required_work_not_applicable` rather than on performance.

`undecidable` is the value most often absent from human task specifications and the one whose absence causes the most damage. A reviewer who cannot determine an answer from what they were given has produced a real and useful finding: that the evidence or the criteria are inadequate. A system with no representation for it forces that reviewer to choose between a rejection they cannot justify, an approval they do not believe, and leaving the item open. The first two corrupt the record, and the third is invisible.

### 7.3 Candidate derivation outcomes

Closed enumeration.

| Value | Meaning | Work item state |
|---|---|---|
| `derived` | The derivation completed and yielded one or more eligible members | `offered`, `allocated` or `reserved` |
| `derived_empty` | The derivation completed and yielded no member | `unassignable` |
| `no_eligible_candidate` | The derivation yielded members, all of whom were excluded | `unassignable` |
| `derivation_partial` | The derivation completed against an incomplete organisational read, with the incompleteness recorded | `offered` with a recorded caveat |
| `derivation_failed` | The derivation did not complete | `unassignable` |

**P8-7-12** (MUST) [D] The component MUST distinguish these five outcomes and MUST NOT return one where another applies.

**P8-7-13** (MUST NOT) [D] The component MUST NOT return `derived_empty` where the read of the organisational model or the evaluation of the assignment expression did not complete.

**P8-7-14** (MUST) [D] Where the outcome is `derivation_partial`, the component MUST record which portion of the organisational read was unavailable and MUST raise an event, because an offer made against a partial read may exclude a party who should have been offered.

### 7.4 Gate verdicts

Closed enumeration. The first two are verdicts; the remainder are non verdicts.

| Value | Meaning |
|---|---|
| `satisfied` | The condition holds and every trigger has fired |
| `unsatisfied` | The condition does not hold |
| `undecidable` | `Part 2` determined that the condition cannot be decided on the available facts |
| `not_applicable` | `Part 2` determined the condition does not apply to this subject |
| `not_evaluated` | Evaluation was not attempted, or was abandoned before completion |
| `input_unavailable` | A fact the condition requires could not be read |
| `rule_unavailable` | The pinned rule version could not be resolved |
| `evaluation_error` | Evaluation was attempted and faulted |
| `evaluation_timeout` | Evaluation exceeded the declared bound |

**P8-7-15** (MUST) [D] The component MUST represent all nine values and MUST record the specific value returned rather than a collapsed category.

**P8-7-16** (MUST NOT) [D] The component MUST NOT treat `undecidable`, `not_applicable`, `not_evaluated`, `input_unavailable`, `rule_unavailable`, `evaluation_error` or `evaluation_timeout` as `unsatisfied`.

**P8-7-17** (MUST) [D] Where `Part 2` returns a verdict value this component's enumeration does not contain, the component MUST record the value verbatim.

**P8-7-35** (MUST) [D] The component MUST treat a verdict value its enumeration does not contain as a non verdict.

**P8-7-36** (MUST) [D] The component MUST raise an unrepresentable verdict event on receipt of a verdict value its enumeration does not contain.

These three clauses exist because a component that receives a value it cannot represent will otherwise map it to the nearest value it has, and the nearest value is almost always the negative.

**P8-7-18** (MUST) [D] `not_applicable` returned for an entry gate MUST leave the guarded item in `pending_gate` and MUST NOT admit it.

**P8-7-37** (MUST) [D] Where an entry gate returns `not_applicable`, the component MUST record the gate as inapplicable rather than as unsatisfied.

### 7.5 System fault outcomes

Closed enumeration. These describe the component's own inability to proceed and are never dispositions of work.

| Value | Meaning |
|---|---|
| `store_unavailable` | The record store could not be read or written |
| `dependency_unavailable` | A required component could not be reached |
| `snapshot_unavailable` | A pinned snapshot could not be resolved |
| `definition_unresolvable` | A pinned definition version could not be resolved |
| `generation_depth_exceeded` | Cascading gate evaluation exceeded the declared maximum |
| `repetition_bound_exceeded` | A repetition rule exceeded the declared maximum |
| `non_confluent_definition` | A definition was found to admit order dependent evaluation |
| `internal_invariant_violated` | The component detected a violation of its own invariants |

**P8-7-19** (MUST NOT) [D] A system fault outcome MUST NOT be recorded as a work item disposition, and MUST NOT be recorded as a human act.

**P8-7-20** (MUST) [D] A work item affected by a system fault MUST enter `error`, and the fault value MUST be recorded against the error.

**P8-7-21** (MUST) [D] Where `internal_invariant_violated` is detected, the component MUST stop applying changes to the affected case and MUST raise the fault, rather than continuing on inconsistent state.

### 7.6 Case completion bases

Closed enumeration. Exactly one is recorded on every case reaching `completed`, `terminated` or `failed`.

| Value | Meaning |
|---|---|
| `all_required_performed` | Every required item reached `completed` with a performance disposition |
| `required_work_skipped` | At least one required item reached `skipped` |
| `required_work_expired` | At least one required item reached `expired` |
| `required_work_not_applicable` | At least one required item reached `not_applicable` |
| `required_work_undecidable` | At least one required item reached `undecidable` |
| `terminated_by_act` | A party terminated the case |
| `terminated_by_exit_gate` | A case exit gate was satisfied |
| `failed_unassignable` | A required item could not be assigned and the case was failed |
| `failed_indeterminate` | A required item's gate remained indeterminate and the case was failed |
| `failed_system` | A system fault prevented progress and the case was failed |
| `superseded_by_case` | The case was subsumed by another case, which is named |

**P8-7-22** (MUST) [D] The component MUST record exactly one completion basis and MUST NOT report `all_required_performed` where any other basis applies.

**P8-7-23** (MUST) [D] Where more than one non performance basis applies, the component MUST record the first that occurred and MUST retain the others in the case record.

### 7.7 Operation outcomes

Open enumeration; extension is governed by §9.4.

| Value | Meaning |
|---|---|
| `applied` | The requested change was made |
| `applied_idempotent` | The change had already been made under the same idempotency key |
| `idempotency_conflict` | The key was seen with different arguments |
| `illegal_transition` | The operation is not legal from the current state |
| `not_eligible` | The requesting party is not in the current candidate set |
| `not_authorised` | `Part 7` denied the act |
| `authorisation_unavailable` | `Part 7` could not be reached, and the act was therefore denied |
| `already_claimed` | Another party claimed first |
| `lease_expired` | The requesting party's hold had already expired |
| `stale_not_acknowledged` | Completion was refused because staleness was not acknowledged |
| `validation_failed` | A payload did not validate against its pinned schema |
| `outcome_not_permitted` | The selected outcome is not in the definition's enumeration |
| `precondition_unmet` | A declared precondition of the operation does not hold |
| `case_not_active` | The operation requires an active case |
| `rejected_non_confluent` | A definition was rejected at instantiation |
| `system_fault` | A value from §7.5, carried with the specific fault |

**P8-7-24** (MUST) [D] `not_eligible` and `not_authorised` MUST be distinct outcomes, and the component MUST NOT return one for the other.

**P8-7-25** (MUST) [D] `authorisation_unavailable` MUST be distinct from `not_authorised`, because the remedies differ and because a pattern of unavailability is a security finding.

**P8-7-26** (MUST NOT) [D] The component MUST NOT return `applied` where any part of the requested change was not applied.

### 7.8 What distinguishes each outcome from failure

**P8-7-27** (MUST) [D] The component MUST expose, for every terminal disposition, the three properties in the following table, and MUST NOT require a consumer to infer them from the disposition name.

| Disposition | Work done | Business outcome present | Requiring party satisfied |
|---|---|---|---|
| `completed_with_outcome` | yes | yes | yes |
| `completed_without_outcome` | yes | not applicable | yes |
| `completed_by_agent` | yes | yes | yes, subject to any required check |
| `undecidable` | yes | no | no |
| `not_applicable` | no | no | not applicable |
| `out_of_competence` | no | no | no |
| `conflicted` | no | no | no |
| `failed` | attempted | no | no |
| `expired` | no | no | no |
| `skipped` | no | no | by decision, yes |
| `withdrawn` | no | no | not applicable |

The value of this table is the third column. A component that reports only the first two columns cannot distinguish an `undecidable` finding, which is work done that leaves the requirement unmet, from a `not_applicable` finding, which leaves no requirement to meet. Those two produce opposite next actions.

### 7.9 Propagation of non results

**P8-7-28** (MUST) [D] Where the component receives a non result from another component, it MUST represent that non result in its own record and MUST NOT substitute a value from its own success or failure enumerations.

**P8-7-29** (MUST) [D] Where the component emits a non result, it MUST emit it as a distinct event class under P8-4-37 and MUST NOT rely on a consumer parsing an outcome string.

**P8-7-30** (MUST) [D] Where a non result would otherwise be discarded because no consumer subscribes to it, the component MUST retain it in the record of the affected item.

**P8-7-31** (MUST NOT) [D] The component MUST NOT aggregate a set of dispositions into a single summary value that loses the distinction between performance dispositions and human non results.

**P8-7-32** (MUST) [D] Every projection, report or count the component exposes over dispositions MUST state the grain at which it was counted and MUST report human non results as their own categories.

---

## 8. Observability and the audit record

The test applied throughout this section is the reconstruction test: a competent reader, years later, holding only the record and with no part of the system running, must be able to establish what happened, who did it, what they were shown, what alternatives they had, and what governed them.

### 8.1 What must be recorded

**P8-8-01** (MUST) [D] The component MUST record every state transition of every case, work item, case file slot, gate, milestone and role binding, at the grain of one record per transition.

**P8-8-02** (MUST) [D] The component MUST record every operation it accepts, including operations it rejects, at the grain of one record per invocation.

**P8-8-03** (MUST) [D] The component MUST record every gate evaluation, including evaluations returning `unsatisfied` and non verdicts, at the grain of one record per evaluation.

**P8-8-04** (MUST) [D] The component MUST record every candidate derivation, at the grain of one record per derivation, including derivations that yielded no member and derivations that failed.

**P8-8-05** (MUST) [D] The component MUST record every presentation, at the grain of one record per presentation to one party.

**P8-8-06** (MUST) [D] The component MUST record every authorisation decision it obtained, by reference, at the grain of one reference per act.

**P8-8-07** (MUST) [D] The component MUST record every read of a work item's payload by a party, at the grain of one record per party per read, where the definition declares the payload subject to access recording.

**P8-8-08** (MUST) [D] The component MUST record every escalation, at the grain of one record per deadline breach.

**P8-8-09** (MUST) [D] The component MUST record every choice resolution, at the grain of one record per resolution, naming all alternatives.

**P8-8-10** (MUST) [D] The component MUST record every planning act and every migration act, at the grain of one record per act.

### 8.2 What must be reconstructable

**P8-8-11** (MUST) [D] A reader MUST be able to reconstruct, for any completed work item, the identity of the performer, the instant, the outcome selected, and the full set of outcomes available at that instant.

**P8-8-12** (MUST) [D] A reader MUST be able to reconstruct which version of every governing instruction, definition, reference set and schema was in force at the instant of performance, from pinned references alone.

**P8-8-13** (MUST) [D] A reader MUST be able to reconstruct whether the performer was the only eligible party, by resolving the candidate set as pinned at derivation.

**P8-8-14** (MUST) [D] A reader MUST be able to reconstruct why every party who did not act did not act, distinguishing decline, exclusion, withdrawal by resolution, lease expiry and revocation.

**P8-8-15** (MUST) [D] A reader MUST be able to reconstruct the sequence of gate evaluations that admitted a work item, and the snapshot each evaluation read.

**P8-8-16** (MUST) [D] A reader MUST be able to reconstruct which items of a case plan were present at any past instant, and which were added by planning acts.

**P8-8-17** (MUST) [D] A reader MUST be able to reconstruct, for a case that reached a terminal state, its completion basis and the disposition of every required item.

**P8-8-18** (MUST) [D] A reader MUST be able to reconstruct every human non result, its reason, and what was done in consequence.

**P8-8-19** (MUST) [D] A reader MUST be able to distinguish an act performed by a person from an act performed by a non human actor, and where a person accepted a proposal from a non human actor, MUST be able to establish that.

**P8-8-20** (MUST NOT) [D] Reconstruction MUST NOT depend on the availability of any component other than those holding the pinned targets, and MUST NOT depend on this component's runtime being available.

### 8.3 Grain, counting and derivation

**P8-8-21** (MUST) [D] Every count the component reports MUST state the grain at which it was counted and the instant as at which it was computed.

**P8-8-22** (MUST NOT) [D] The component MUST NOT report a count of work items without stating whether repetitions are counted individually.

**P8-8-23** (MUST NOT) [D] The component MUST NOT report a completion rate, throughput or cycle time that includes human non results in the numerator of performed work.

**P8-8-24** (MUST) [D] Every derived metric the component exposes MUST be accompanied by its derivation, sufficient for a reader to recompute it from the recorded events.

**P8-8-25** (MUST) [D] Where a metric excludes any disposition, the exclusion MUST be stated with the metric.

### 8.4 Integrity and retention

**P8-8-26** (MUST) [D] Every record this component writes MUST be integrity protected such that alteration is detectable, by a means governed by `Part 3`.

**P8-8-27** (MUST NOT) [D] The component MUST NOT permit the deletion of a completion record, presentation pin, candidate set, gate evaluation, planning act, choice resolution or escalation record other than under a recorded disposition act governed by `Part 1`.

**P8-8-28** (MUST) [D] Where a record is disposed of under a retention schedule, the component MUST retain a tombstone carrying the identifier, the record class, the disposition act reference and the instant, so that a citation to the disposed record resolves to an explanation rather than to nothing.

**P8-8-29** (MUST) [D] Where a case is subject to a legal hold, the component MUST refuse every disposition act affecting its records and MUST record the refusal.

**P8-8-30** (MUST) [D] The component MUST record the identity of every party that reads a presentation pin or completion record, where the case definition declares the case subject to read recording.

### 8.5 Observability of the component itself

**P8-8-31** (MUST) [D] The component MUST expose the count of work items in `unassignable`, `gate_indeterminate` and `error`, because each is a condition that no one is accountable for by default and that is therefore invisible unless surfaced.

**P8-8-32** (MUST) [D] The component MUST expose the count and age of work items whose lease has expired more than once, because repeated expiry indicates work that no party will take.

**P8-8-33** (MUST) [D] The component MUST expose the count of completions whose `choice_breadth` is one, because a population of single option completions indicates a process that records judgements it does not obtain.

**P8-8-34** (MUST) [D] The component MUST expose the count of completions whose `stale_acknowledged` is true.

**P8-8-35** (SHOULD) [D] The component SHOULD expose the distribution of human non results by reason, because a rising rate of `criteria_ambiguous` is a finding about the governing definitions rather than about the performers.

---

## 9. Extension model

### 9.1 Closed and open sets

**P8-9-01** (MUST) [D] The following sets MUST be closed and MUST NOT be extended by an implementation: case states (§5.2), work item states (§5.3), case file slot states (§5.4), milestone states (§5.5), gate states (§5.6), work item terminal dispositions (§7.2), withdrawal reasons (§7.2.3), human non results and their reasons (§7.2.4), candidate derivation outcomes (§7.3), gate verdicts (§7.4), system fault outcomes (§7.5), and case completion bases (§7.6).

**P8-9-02** (MUST) [D] The following sets MAY be extended under the governance in §9.4: operation outcomes (§7.7), attention bases (§3.5), escalation effects (§3.14), and the set of operations the component accepts (§4.2).

**P8-9-03** (MUST) [D] Business outcome enumerations MUST be declared per work item definition and are open by construction, being properties of the work rather than of this component.

The states and dispositions are closed because they are the vocabulary in which the audit record speaks. An implementation that adds a work item state has created a state no reader of the standard can interpret, and an implementation that adds a disposition has created an outcome that no consumer of §7.8 can classify. The operation set is open because a new operation is a new act, and a new act is representable in the existing states.

### 9.2 How a new member is admitted

**P8-9-04** (MUST) [D] A proposal to extend an open set MUST state the act or condition the new member represents, the states from which it is legal, its three properties under §7.8 where applicable, and the reason no existing member suffices.

**P8-9-05** (MUST NOT) [D] A new member MUST NOT be admitted where an existing member differs from it only in the reason recorded, and the reason MUST be carried as a reason field instead.

**P8-9-06** (MUST NOT) [D] A new member of the operation set MUST NOT introduce a state transition not listed in §5.

**P8-9-07** (MUST) [D] Where an implementation requires a state transition this part does not list, the requirement MUST be raised against this part rather than satisfied by extension, because a new transition changes the meaning of the record.

### 9.3 Composition and primitives

**P8-9-08** (MUST) [S] A composite work item MUST be represented as a work item whose completion depends on the dispositions of named subordinate work items, each of which is itself a work item with full identity and lifecycle. **Source.** WS-HumanTask 1.1 §3.2 defines composite tasks and sub tasks in this shape, with a composition type of parallel or sequential and an instantiation pattern of manual or automatic.

**P8-9-09** (MUST) [D] A composite work item MUST declare its completion condition, and the component MUST record the evaluation of that condition on every subordinate disposition.

**P8-9-10** (MUST NOT) [D] A composite work item MUST NOT be completed by aggregating subordinate dispositions in a way that loses a subordinate human non result, and where any subordinate returned a human non result the composite's completion record MUST carry that fact.

**P8-9-11** (MUST) [S] Where a composite work item completes before every subordinate has reached a terminal state, the remaining subordinates MUST receive the disposition `withdrawn_by_resolution` and the composite MUST carry a choice resolution record. **Source.** WS-HumanTask 1.1 §4.8 requires that on a completion condition being met, remaining running sub tasks be set to the Obsolete state; this part requires the withdrawal to be recorded as a resolution so that the subordinates are not read as having been skipped.

**P8-9-12** (MUST) [S] A routing pattern that assigns work to parties in sequence or in parallel MUST be represented as a composite work item with one subordinate per assignment, and MUST NOT be represented as one work item with several holders. **Source.** WS-HumanTask 1.1 §4.7.1 requires a separate sub task per parallel and per sequential assignment.

**P8-9-13** (MUST NOT) [D] A stage MUST NOT be represented as a composite work item, and the component MUST NOT permit a stage to be claimed, held or performed.

### 9.4 Governance of extension

**P8-9-14** (MUST) [D] Every extension an implementation makes MUST be declared in a machine readable extension manifest carrying the extended set, the new member, and its definition.

**P8-9-15** (MUST) [D] The component MUST record, on every record affected by an extension, the identifier of the extension manifest version under which it was written.

**P8-9-16** (MUST NOT) [D] An extension MUST NOT change the meaning of an existing member of any set.

**P8-9-17** (MUST NOT) [D] An extension MUST NOT be required for interoperation, and a consumer that ignores every extension MUST still be able to interpret every record correctly at the grain of the closed sets.

---

## 10. Standards and specifications

### 10.1 What each consulted specification supplies

| Specification | Status as established | What it supplies to this component | What it does not supply |
|---|---|---|---|
| WS-HumanTask 1.1, OASIS BPEL4People TC, Committee Specification 01, 17 August 2010 | Committee Specification 01; a later Committee Specification Draft 12 / Public Review Draft 05 dated 2012 exists at the latest version URI. This part could not establish that version 1.1 was approved as an OASIS Standard; see §13.1 | Generic human roles (§3.1), people assignment by logical people group, literal and expression (§3.5), task instance data and its three categories (§3.8), priority range and orientation (§4.2), possible outcomes (§4.4), routing patterns (§4.7.1), completion behaviour and conditions (§4.8), deadlines and escalations (§4.9), state transitions (§4.10), task history (§4.11), participant and administrative operations (§7.1) | The case as an entity. Runtime planning. Gates in the sentry sense. Any human non result. Point in time resolution of what was presented. Recording of the alternatives available at completion |
| OMG CMMN 1.1, formal/2016-12-01, December 2016 | Formal OMG specification; supersedes CMMN 1.0, formal/2014-05-05 | The case (§4.1), case file and case file item (§5.3), case roles (§5.2.2), plan item and criterion (§5.4.5), sentry with on parts and if part (§5.4.6), stage (§5.4.8), planning table and discretionary item (§5.4.9), human task (§5.4.10.4), plan item control rules (§5.4.11), case file item lifecycle (§8.3), case instance lifecycle (§8.4.1), stage and task lifecycle (§8.4.2), event listener and milestone lifecycle (§8.4.3), planning constraints (§8.7) | Assignment of roles to participants, excluded explicitly at §5.2.2. Versioning of case file items, excluded explicitly at §5.3.2.1. Any worklist or claim semantics. Sentry evaluation order or confluence. Reopening of a completed case. Any evidentiary requirement |
| BPMN 2.0, OMG, also published as ISO/IEC 19510 | Formal; this part consulted it for the user task and event based gateway only | The user task as a process activity; the event based gateway as the notation for deferred choice within a process | Everything this component owns. BPMN's user task is an activity in a control flow, not a durable work item with candidacy |
| Workflow Resource Patterns, Russell, ter Hofstede, Edmond, van der Aalst, BETA Working Paper WP 127, Eindhoven, 2004; and the CAiSE'05 paper, LNCS 3520, pages 216-232 | Peer reviewed literature, not a specification | The vocabulary and taxonomy of distribution: creation, push, pull, detour, auto start, visibility and multiple resource pattern groups; the work item lifecycle from the resource perspective | No normative requirements. No non result handling. No evidentiary requirements |
| Workflow Patterns and its revised view, van der Aalst, ter Hofstede, Kiepuszewski, Barros, Distributed and Parallel Databases 14(3):5-51, 2003; Russell, ter Hofstede, van der Aalst, Mulyar, BPM-06-22, 2006 | Peer reviewed literature | Deferred choice as pattern WCP-16, interleaved parallel routing, milestone, critical section | Nothing about human non results or attribution |
| Case Handling: a new paradigm for business process support, van der Aalst and Weske, Data and Knowledge Engineering 53(2):129-162, 2005 | Peer reviewed literature; cited as a non normative reference by CMMN 1.1 §3.2 | The case handling paradigm: data as first class, the three execution modes of execute, skip and redo, and the diagnosis of context tunneling | No normative requirements |
| Guard-Stage-Milestone, Hull et al., WS-FM 2010 and DEBS 2011 | Peer reviewed literature; cited as a non normative reference by CMMN 1.1 §3.2 and identified there as having influenced CMMN's execution semantics | The guard, stage and milestone formalism underlying the gate model | No assignment model |
| ANSI/INCITS 359, role based access control | National standard; this part did not re-verify the current revision, see §13.1 | The distinction between static and dynamic separation of duty relations | The participation history that dynamic separation of duty requires, which is owned here |
| WfMC reference model and its client application interface | Industry specification of historical standing | The work item and worklist vocabulary, and the workitem manager as a distinct component | Superseded in practice by the above for new work |

### 10.2 What governs which subject

**P8-10-01** (MUST) [D] Where this part and a consulted specification address the same subject and do not conflict, an implementation MUST satisfy both.

**P8-10-02** (MUST) [D] Where this part and a consulted specification conflict, an implementation claiming conformance to this part MUST satisfy this part, and MUST record the conflict in its conformance statement.

**P8-10-03** (MUST) [D] An implementation that also claims conformance to WS-HumanTask 1.1 or CMMN 1.1 MUST declare which of the conflicts in §10.4 it resolves in favour of this part.

### 10.3 Internal defects observed in the consulted text

These are recorded because a reader who goes to the source will encounter them, and because a specification that cites a section number should say when that number is unreliable.

**P8-10-04** (SHOULD) [P] A reader consulting CMMN 1.1 §2.6 SHOULD note that it requires conformance to execution semantics and lifecycle specified in Clause 7 and exchange formats in Clause 8, whereas the specification's own table of contents places Diagram Interchange at Clause 7, Execution Semantics at Clause 8 and Exchange Formats at Clause 9; the clause references in §2.6 appear not to have been updated from CMMN 1.0. This part cites the clause numbers given in the CMMN 1.1 table of contents.

**P8-10-05** (SHOULD) [P] A reader consulting CMMN 1.1 §2.1 SHOULD note that it states four types of compliance point and then names five, the fifth being DMN Compatibility Conformance at §2.5, which also appears as a column in its Table 2.1.

### 10.4 Where the specifications conflict, and how this part resolves each

| Conflict | Position A | Position B | Resolution in this part | Reason |
|---|---|---|---|---|
| Reference resolution | CMMN 1.1 §5.3.2.1: a reference to an information element MUST refer to the latest, most current version | This part P8-3-30, P8-5-21: a reference pinned in a presentation MUST resolve to the version in force at presentation | This part | A determination is evidence of a judgement made on particular material. A reference that silently moves to the current version makes the record assert that the performer saw something they did not see. CMMN's rule is coherent for a modelling and interchange specification, which CMMN is, and incoherent for an evidentiary one |
| Failed candidate query | WS-HumanTask 1.1 §3.5.1: a failed people query MUST be treated like a query returning an empty result set | This part P8-3-22, P8-7-13: a failed derivation MUST be recorded as `derivation_failed` and MUST NOT be recorded as empty | This part | The two conditions have different remedies and different implications. Treating a failure as an empty result converts an operational fault into an apparent statement that nobody is qualified, and that statement then propagates into escalation and nomination logic as though it were a finding |
| Condition evaluation error | WS-HumanTask 1.1 §4.8.1: an error during condition evaluation MUST be considered to have evaluated to false | This part P8-3-56, P8-6-18, P8-7-16: a non verdict MUST NOT be mapped to `unsatisfied` | This part | This is the silent negative in its purest form. A completion condition that fails to evaluate and is read as false will keep a composite task open; an entry gate read the same way will keep work from ever appearing, with no record that anything went wrong |
| Empty potential owner set | WS-HumanTask 1.1 §4.10.1: where the potential owner query returns an empty set, the processor MUST perform nomination | This part P8-5-13: the item MUST enter `unassignable`, a durable recorded state | This part, and nomination is permitted as a subsequent recorded act | Nomination presumes a nominating authority is reachable and willing at that instant. Where it is not, the WS-HumanTask rule has no defined outcome. A durable state loses nothing and can be nominated out of |
| Where roles are bound | CMMN 1.1 §5.2.2: assignment of roles to participants is not in scope | WS-HumanTask 1.1 §3.5: people assignment is specified in detail, but without a case | This part §3.13 and §12.6: bindings are owned here, scoped to the case instance, and resolved against `Part 10` | Neither specification covers the join. The gap is where two implementations of the same case model will differ most, so it is specified rather than left |
| Sentry evaluation order | CMMN 1.1 §8.5 specifies the Sentry without specifying evaluation order across sentries triggered by one event | This part P8-6-02, P8-6-03, P8-6-07: single snapshot, order independence required, non confluent definitions rejected | This part | Order dependence makes a case model's behaviour a property of the implementation rather than of the model, which defeats the portability CMMN §4.3 exists to provide |

### 10.5 What none of the consulted specifications supplies

**P8-10-06** (MUST) [D] An implementation MUST treat the following as requirements of this part alone, no consulted specification supplying them: the human non result enumeration and its reasons (§7.2.4); the presentation pin (§3.6); choice breadth (§3.7); the recording of withdrawal by resolution as distinct from decline (§3.12); the indeterminate gate as a state (§5.6); staleness and its acknowledgement (§6.14); the separation of attention from candidacy (§3.5); the actor class and the recording of an accepted agent proposal (§6.11); the pinning of the working calendar (§6.13); case reopening (§4.2.3); and the distinction between a determined empty candidate set, a failed derivation and a fully excluded set (§6.4).

---

## 11. Anti patterns

Each entry names a mechanism, states the evidence that it is a mechanism rather than a matter of taste, and states the consequence. The consequence is stated in terms of what becomes unrecoverable, because an anti pattern whose consequence is only inelegance is not worth a clause.

### 11.1 The boolean approval

**Mechanism.** The completion record carries the performer, the instant and a boolean or a two valued outcome, and nothing else. What was presented, which version of the governing procedure applied, and how many outcomes were available are not recorded.

**Evidence.** WS-HumanTask 1.1 §4.4 provides a possible outcomes element at the definition level, and §3.8.2 carries task state, priority, roles and timestamps in the task context, but neither requires the set of outcomes actually offered at the instant of an act to be recorded with the act. An implementation that follows the specification exactly produces this record.

**Consequence.** The record cannot distinguish a judgement from a forced act, and cannot survive a challenge to what the performer was shown. Every downstream use of the record inherits the ambiguity.

**P8-11-01** (MUST NOT) [D] The component MUST NOT write a completion record without a referenced presentation pin and a recorded choice breadth.

### 11.2 Coercing a non result to a negative

**Mechanism.** A value that is neither success nor failure is mapped to the nearest available negative. Three variants appear in specification text: a failed candidate query treated as an empty result, a condition evaluation error treated as false, and a human inability to decide offered no representation and therefore recorded as a rejection.

**Evidence.** WS-HumanTask 1.1 §3.5.1 and §4.8.1 both require the coercion in terms. The third variant is an absence rather than a requirement: no consulted specification provides a human non result, so an implementation has nowhere to put one.

**Consequence.** The system produces false negatives that are indistinguishable from findings. A party appears to have been ineligible when the directory was unreachable. A gate appears not to have opened when the rule could not be resolved. A reviewer appears to have rejected an application when they were unable to assess it. None of these is visible as an error, and all three are actionable as though they were determinations.

**P8-11-02** (MUST NOT) [D] The component MUST NOT map any non result to a value in a success or failure enumeration.

**P8-11-03** (MUST) [D] The component MUST provide a distinct representation for every non result it can receive or produce, and where it receives one it cannot represent, MUST record it verbatim and raise it.

### 11.3 The live candidate query

**Mechanism.** The candidate set is computed on each read rather than pinned at derivation, so a worklist, a claim check and an audit query can each yield a different set.

**Evidence.** WS-HumanTask 1.1 §3.5.1 permits a logical people group to be re-evaluated on each reference and states that two tasks bound to the same people query are not guaranteed to be assigned to the same set of people.

**Consequence.** A claim can fail for a party who was offered the item, and can succeed for a party who was not. After the fact, the question of who was offered the work has no answer, so a segregation of duty finding cannot be established or refuted.

**P8-11-04** (MUST NOT) [D] The component MUST NOT determine eligibility against a candidate set computed at read time rather than against the pinned candidate set.

### 11.4 The case as the integration point

**Mechanism.** The case file accepts arbitrary values from any component that needs somewhere to put them, and becomes the place where components exchange facts. Copies of facts owned elsewhere accumulate in slots.

**Evidence.** CMMN 1.1 §5.3.2 permits a case file item to represent a piece of information of any nature, from unstructured to structured, defined in any information modelling language, and §5.3.1 states that the case file serves as a container for data accessible by other systems and people outside the case. The specification imposes no constraint that would prevent this.

**Consequence.** Two authoritative copies of the same fact exist, they diverge, and no component can be changed without changing the case. The case's retention schedule becomes the effective retention schedule of facts it does not own.

**P8-11-05** (MUST NOT) [D] The component MUST NOT hold a literal copy of a fact whose authority belongs to another component.

**P8-11-06** (MUST NOT) [D] The component MUST NOT permit another component to read a case file slot as a means of obtaining a fact that component itself owns.

### 11.5 Gate order dependence

**Mechanism.** Several gates are triggered by one event and are evaluated sequentially, each observing the effects of the previous, so the resulting state depends on evaluation order.

**Evidence.** CMMN 1.1 §8.5 specifies the Sentry without specifying an evaluation order across sentries triggered by one event, and published vendor documentation states that runtime evaluation of the same model is likely to differ between implementations for this reason.

**Consequence.** The behaviour of a case model becomes a property of the engine, so a model cannot be validated once and relied on, and an audit finding cannot be reproduced on a different deployment.

**P8-11-07** (MUST) [D] The component MUST evaluate all gates triggered by one event against one snapshot and MUST reject definitions whose behaviour depends on evaluation order.

### 11.6 Attention conflated with candidacy

**Mechanism.** A single list determines both what a party sees and what a party may take.

**Evidence.** WS-HumanTask 1.1 §3.1 distinguishes potential owners from stakeholders and business administrators, all of whom may influence a task, but the client interface at §7.1.2 exposes queries over tasks rather than a separated model of visibility and eligibility.

**Consequence.** One of two failures follows. Either oversight parties are granted candidacy, and the segregation of duty model is unenforceable because a supervisor can perform work they are meant to review; or oversight parties are denied visibility, and the work becomes unsupervised.

**P8-11-08** (MUST) [D] The component MUST record attention and candidacy separately and MUST expose both.

### 11.7 Silent re-pinning

**Mechanism.** When a definition, procedure or reference set is superseded, in flight work items are quietly re-pointed at the new version, and no record is kept that the performer began under a different one.

**Evidence.** CMMN 1.1 §5.3.2.1 requires references to resolve to the most current version, which produces exactly this behaviour where a case is running across a change.

**Consequence.** A completion record asserts compliance with a procedure the performer never saw. The change of governing version becomes invisible at precisely the point where it matters most, which is work that spans the change.

**P8-11-09** (MUST NOT) [D] The component MUST NOT re-pin a work item's dependencies without creating a new presentation pin and recording the prior presentation as withdrawn unacted.

### 11.8 Escalation that performs the work

**Mechanism.** A deadline breach triggers an action that supplies the outcome, on the reasoning that a default is better than a stall.

**Evidence.** WS-HumanTask 1.1 §4.9 defines escalation actions on deadlines, and §4.8.1 provides time functions in completion conditions under which a task can be considered complete when a duration has elapsed, with the completion action defaulting to automatic for routing patterns.

**Consequence.** The record shows a determination that no party made. Where the determination is later challenged there is no performer to ask, and the completion is attributed to the definition's author or to nobody.

**P8-11-10** (MUST NOT) [D] The component MUST NOT allow a deadline, an escalation or a timer to write a completion record.

### 11.9 The unbounded reservation

**Mechanism.** A party claims a work item and holds it without a lease, so the item is neither available to anyone else nor progressing.

**Evidence.** WS-HumanTask 1.1 §4.10.2 provides for releasing a task but does not require a reservation to be time bounded, and the task context at §3.8.2 carries no lease.

**Consequence.** Work becomes invisible: it is assigned, so it does not appear as unassigned, and it is not in progress, so it does not appear as late. It ages out of view.

**P8-11-11** (MUST) [D] The component MUST subject every reservation to a lease with a declared expiry.

### 11.10 Context tunneling

**Mechanism.** The performer is shown only the fields the current work item declares, and cannot see the case that the work item belongs to, so decisions are made without the context that determines whether they are correct.

**Evidence.** Named and diagnosed as context tunneling in van der Aalst and Weske, *Case Handling: a new paradigm for business process support*, Data and Knowledge Engineering 53(2):129-162, 2005, which identifies it as a defect of activity centric workflow and is cited as a non normative reference by CMMN 1.1 §3.2.

**Consequence.** Decisions are locally correct and globally wrong, and the record cannot show that the performer lacked the information, because what was withheld is not recorded.

**P8-11-12** (MUST) [D] The presentation pin MUST record what was presented, so that a decision made without necessary context is demonstrable rather than deniable.

### 11.11 Terminal error

**Mechanism.** A system fault places the work item in a terminal state, on the reasoning that the item cannot proceed.

**Evidence.** WS-HumanTask 1.1 §3.8.4 enumerates predefined statuses including both `FAILED` and `ERROR` without distinguishing which are terminal, and the distinction between a fault and a disposition is not drawn.

**Consequence.** Work that was never performed acquires a disposition, and reprocessing after the fault is repaired requires either violating the terminal state or creating a second work item that appears to be a duplicate.

**P8-11-13** (MUST NOT) [D] The component MUST NOT treat a system fault state as terminal.

### 11.12 The plan that hides its own extension

**Mechanism.** Items added at runtime are indistinguishable from items instantiated from the definition, so the plan appears to have been designed as executed.

**Evidence.** CMMN 1.1 §5.4.9.2 and §8.7 provide discretionary items and constrain when planning may occur, but do not require the planning act to be recorded as an attributable event.

**Consequence.** The distinction between what the organisation designed and what an individual chose to add is lost, which is the distinction a review of discretion depends on.

**P8-11-14** (MUST) [D] Every runtime addition to a case plan MUST be traceable to an attributable planning act.

---

## 12. Boundaries with other parts

Every boundary below is stated as what this part delegates, what it must not absorb, where a naive design conflates the two, and what the conflation costs. Each is reciprocal: the named part declares the same boundary from its side.

### 12.1 With `Part 2`, business rules engine

**Delegated.** The evaluation of every gate condition, every applicability rule, every requiredness rule and every repetition rule, together with the verdict vocabulary.

**Must not absorb.** The evaluation itself, the rule text, the rule's versioning, or any interpretation of a verdict beyond the mapping to state transitions in §5.

**Naive conflation.** The component implements gate conditions as inline expressions it evaluates itself, because a gate looks like a small amount of logic and the round trip looks like overhead.

**Cost.** Two rule engines exist with two verdict vocabularies. The one inside this component has no non result vocabulary, because a locally implemented expression evaluator returns a boolean, so every indeterminacy becomes false. §11.2 then follows necessarily.

**P8-12-01** (MUST NOT) [D] The component MUST NOT evaluate a gate condition, applicability rule, requiredness rule or repetition rule itself.

**P8-12-02** (MUST) [D] The component MUST accept the full verdict vocabulary of `Part 2` including every non verdict.

### 12.2 With `Part 1`, controlled documents and records management

**Delegated.** The identity, version, status, supersession, effective date, retention and point in time citation resolution of every instruction, procedure and policy presented to a performer.

**Must not absorb.** The text of any controlled document, its lifecycle, or its retention schedule.

**Naive conflation.** The work item definition embeds the instruction text, so that the presentation is self contained.

**Cost.** The instruction has two versions, one governed and one embedded, and they diverge. The completion record then cites a procedure version that was never approved.

**P8-12-03** (MUST NOT) [D] The component MUST NOT hold the authoritative text of a controlled document.

**P8-12-04** (MUST) [D] The component MUST hold, for every instruction presented, a citation that `Part 1` can resolve to the version in force at the instant of presentation.

**P8-12-05** (MUST) [D] The component MUST treat every completion record as a record in the `Part 1` sense, being evidence of an act and not revisable, and MUST NOT treat it as a document.

### 12.3 With `Part 3`, provenance and audit ledger

**Delegated.** The ledger, the integrity chain, and the reconstruction of a chain of reasoning across components.

**Must not absorb.** The role of system of record for reconstruction, or the integrity mechanism itself.

**Naive conflation.** The component's own event log is treated as the audit record, because it already contains everything about human work.

**Cost.** Reconstruction of a determination requires the human act, the rule verdicts, the authorisation decisions and the definitions, which live in four components. A per component log cannot answer a question that spans them, and the component's retention schedule silently becomes the retention schedule of the whole determination.

**P8-12-06** (MUST) [D] The component MUST emit every event in §8.1 to `Part 3`.

**P8-12-07** (MUST NOT) [D] The component MUST NOT represent its own event log as the audit record of a determination.

**P8-12-08** (MUST) [D] The component MUST own the operational state of work and cases as sole authority.

**P8-12-49** (MUST NOT) [D] The component MUST NOT assert authority over the evidentiary chain, which `Part 3` owns, and MUST NOT derive its own authority from it.

### 12.4 With `Part 7`, policy decision point and authorisation

**Delegated.** Every decision on whether a party may perform an act, including the evaluation of static and dynamic segregation of duty constraints.

**Must not absorb.** The authorisation decision, the policy, or the combining of policies.

**Retained and supplied.** The participation record. Dynamic segregation of duty requires the fact of who performed which prior act in this case; that fact is owned here and is supplied to `Part 7` as a pinned attribute.

**Naive conflation.** The component enforces segregation of duty itself by filtering the candidate set, because it already holds the participation history.

**Cost.** The constraint is enforced at derivation and not at the act, so a party who becomes conflicted between derivation and claim is permitted. The policy also exists in two places, and the one in this component is invisible to policy review.

**P8-12-09** (MUST NOT) [D] The component MUST NOT render an authorisation decision.

**P8-12-10** (MUST) [D] The component MUST obtain an authorisation decision at the instant of every act that changes holder, disposition or plan.

**P8-12-11** (MUST) [D] The component MUST supply prior participation facts to `Part 7` on request as pinned attributes.

**P8-12-12** (MUST NOT) [D] The component MUST NOT permit `Part 7` to hold a second copy of the participation record.

### 12.5 With `Part 6`, workflow and process orchestration

**Delegated.** Predefined control flow, joins, loops, compensation and process instance state.

**Must not absorb.** Sequencing that is fully determined before execution.

**The boundary stated positively.** `Part 6` owns work whose order is known in advance. This part owns work whose order is determined at runtime by gates, by planning acts and by human choice. A case may contain process instances and a process may contain work items; neither contains the other by definition.

**Naive conflation, in both directions.** Either the case is implemented as a long running process, in which case runtime planning cannot be expressed and every discretionary item must be modelled as a branch; or the process is implemented as a case, in which case a determined sequence is expressed as a chain of gates and its correctness can no longer be established statically.

**Cost.** In the first direction, discretion becomes invisible because every act taken was on a designed branch. In the second, a sequence that could have been verified once must be verified per instance.

**P8-12-13** (MUST NOT) [D] The component MUST NOT implement predefined control flow constructs.

**P8-12-14** (MUST NOT) [D] The component MUST NOT represent a case as a process instance, and MUST NOT represent a process instance as a case.

**P8-12-15** (MUST) [S] Where a work item is created at the request of a process instance, the component MUST record the requesting instance. **Source.** WS-HumanTask 1.1 §1.5 and §8 describe this coupling and the coordination protocol that maintains it.

**P8-12-50** (MUST) [D] Where a work item was created at the request of a process instance, the component MUST return its disposition to that instance.

**P8-12-51** (MUST) [D] The component MUST retain its own record of a work item independently of the lifetime of the process instance that requested it.

**P8-12-16** (MUST NOT) [D] The component MUST NOT allow the termination of a requesting process instance to delete the record of a work item that was performed.

### 12.6 With `Part 10`, reference and master data management

**Delegated.** Parties, groups, roles as organisational constructs, organisational units, capabilities, competencies and working calendars.

**Must not absorb.** The organisational model, or any part of it.

**Retained.** The case role binding, being the assignment of a party to a position for the life of one case instance, which is case state and not reference data.

**Naive conflation.** The component maintains its own user and group tables, because candidate derivation needs them and the round trip is on the critical path of every worklist read.

**Cost.** Two organisational models diverge. A party removed in one remains a candidate in the other, and a derivation cannot be re-performed years later because the local copy was never versioned.

**P8-12-17** (MUST NOT) [D] The component MUST NOT maintain an authoritative organisational model.

**P8-12-18** (MUST) [D] The component MUST pin the organisational snapshot used in every candidate derivation.

**P8-12-19** (MUST) [D] The component MUST own the case role binding and MUST NOT delegate it to `Part 10`, because a binding is a fact about one case and not about the organisation.

### 12.7 With `Part 4`, metadata and model repository

**Delegated.** The definitions of cases, work items, stages, milestones, discretionary items and gates, and their versioning, lineage and impact analysis.

**Must not absorb.** Definition versioning, or the analysis of what a definition change affects.

**Naive conflation.** The component versions its own definitions, because it instantiates them.

**Cost.** Impact analysis cannot answer which running cases a definition change affects, because the definitions and the instances are versioned by different authorities with different schemes.

**P8-12-20** (MUST NOT) [D] The component MUST NOT version the definitions it instantiates.

**P8-12-21** (MUST) [D] The component MUST pin the definition version at instantiation and MUST expose the set of running instances pinned to each version, so that `Part 4` can perform impact analysis.

**P8-12-22** (MUST) [D] The component MUST accept a definition change notification from `Part 4` and MUST apply §6.14 staleness to affected non terminal work items.

### 12.8 With `Part 5`, decision engine

**Delegated.** The selection of one outcome from candidate outcomes by governed algorithm, including the selection of one party from a candidate set where the definition delegates that selection.

**Must not absorb.** Selection logic of any kind.

**Naive conflation.** The component implements allocation policy itself, such as selecting the least loaded or the most recently familiar party, because allocation feels like a scheduling concern rather than a decision.

**Cost.** A governed decision is made by unversioned code with no decision record, so the question of why this party received this work has no answer. Where the allocation affects who is accountable, that is a governance failure, not an implementation detail.

**P8-12-23** (MUST NOT) [D] The component MUST NOT select one party from a candidate set by any governed algorithm, and MUST either offer the set or obtain the selection from `Part 5`.

**P8-12-24** (MAY) [D] The component MAY select by arrival order in a claim race, which is not a decision because no property of the claimant is evaluated.

**P8-12-25** (MUST) [D] Where a selection is obtained from `Part 5`, the component MUST record the decision reference in the candidate set or allocation record.

### 12.9 With `Part 9`, schema and contract registry

**Delegated.** The identity, versioning, compatibility and validation of every payload schema and every case file slot type.

**Must not absorb.** Schema definition or schema versioning.

**Naive conflation.** The work item definition carries an inline schema for its input and output, because they belong to the work.

**Cost.** The payload of a completed work item cannot be validated years later because the schema exists only inside a definition version that may have been superseded, and no compatibility analysis is possible across work item types that exchange the same payload.

**P8-12-26** (MUST NOT) [D] The component MUST NOT define or version a payload or slot schema.

**P8-12-27** (MUST) [D] The component MUST pin the schema version used for every validation and MUST record it with the validated record.

### 12.10 With `Part 11`, content addressed artifact store

**Delegated.** The storage, addressing, deduplication and retrieval of attachment content.

**Must not absorb.** The bytes.

**Retained.** The association: that this artifact was attached to this case or work item, by this party, at this instant, with this description and this declared content type.

**Naive conflation.** Attachments are stored inline in the work item record, because WS-HumanTask 1.1 §3.8.3.1 permits an inline access type carrying base64 encoded content.

**Cost.** The same artifact attached to twenty work items exists twenty times, its integrity cannot be established independently, and the work item record becomes a binary store subject to the case's retention schedule rather than the artifact's.

**P8-12-28** (MUST NOT) [D] The component MUST NOT store attachment bytes.

**P8-12-29** (MUST) [D] The component MUST own the attachment association record and MUST hold the content address only.

**P8-12-30** (MUST) [D] Where a content address ceases to resolve, the component MUST record the association as `unresolvable` and MUST NOT delete it.

### 12.11 With `Part 12`, conformance and assurance harness

**Delegated.** The verification of this component's claims about itself.

**Must not absorb.** Any self assessment presented as assurance.

**Naive conflation.** The component reports its own conformance, because it holds the state.

**Cost.** The claim and the verification of the claim have the same author.

**P8-12-31** (MUST) [D] The component MUST expose the state required to verify every clause of this part that is externally observable.

**P8-12-32** (MUST NOT) [D] The component MUST NOT report its own conformance to this part as assurance.

**P8-12-33** (MUST) [D] The component MUST expose the invariants in §12.14 in a form `Part 12` can test.

### 12.12 With `Part 13`, model invocation and agent execution

**Delegated.** The invocation record, its cost, its retries and its non determinism.

**Must not absorb.** Any representation of a model invocation as a human act.

**The boundary stated positively.** This part owns the checked value: the work item in which a person examines something and takes responsibility for it. `Part 13` owns the produced value. The boundary is the point at which responsibility transfers, and it transfers only through a completion record written by a human performer.

**Naive conflation.** An agent completes work items on behalf of a person, or a work item is auto completed when an agent's confidence exceeds a threshold.

**Cost.** The record asserts human judgement where there was none. Every downstream consumer that relies on the human attribution, including every regulatory position that requires a person to be accountable, is relying on a fiction.

**P8-12-34** (MUST NOT) [D] The component MUST NOT record a model invocation as a human act.

**P8-12-35** (MUST) [D] The component MUST record an agent completion with `actor_class_used` of `agent` and an invocation reference.

**P8-12-36** (MUST) [D] Where an agent proposal is presented to a human performer, the component MUST record whether the performer accepted it unchanged.

**P8-12-37** (MUST NOT) [D] The component MUST NOT auto complete a work item of actor class `human` on any basis.

### 12.13 With `Part 0`, system composition

**P8-12-38** (MUST) [D] The component MUST treat the authority assignments of `Part 0` as governing, and where this part appears to claim authority over a fact that `Part 0` assigns elsewhere, `Part 0` MUST prevail.

**P8-12-39** (MUST) [D] The component MUST declare, for every fact it owns, that it is the sole authority, being: work item state and holder; candidate set as derived; attention; presentation pin; completion record; case state and plan; case file slot state; case role binding; milestone achievement; gate state; and choice resolution.

**P8-12-40** (MUST NOT) [D] The component MUST NOT claim authority over: party and group identity; rule verdicts; authorisation decisions; definition versions; schema; document versions; artifact content; process instance state; or invocation records.

### 12.14 Invariants at the boundaries

These are stated as invariants rather than as clauses about behaviour, because they are what `Part 12` can test from outside.

**P8-12-41** (MUST) [D] At every instant, every work item in `allocated`, `reserved`, `in_progress` or `suspended` MUST have exactly one holder, and every work item in any other state MUST have none.

**P8-12-42** (MUST) [D] At every instant, every terminal work item MUST have exactly one disposition, and every non terminal work item MUST have none.

**P8-12-43** (MUST) [D] At every instant, every completion record MUST reference exactly one presentation pin whose `presented_to` equals its `performed_by`.

**P8-12-44** (MUST) [D] At every instant, the number of work items with disposition `withdrawn_by_resolution` MUST equal the sum over choice resolution records of the count of alternatives not taken.

**P8-12-45** (MUST) [D] At every instant, every case in a terminal or closed state MUST have exactly one completion basis, and no contained work item MUST be in a non terminal state.

**P8-12-46** (MUST) [D] At every instant, every work item added by a planning act MUST reference exactly one planning act record that references it.

**P8-12-47** (MUST) [D] At every instant, every gate whose state is `satisfied` and which is declared not re-evaluable MUST have exactly one evaluation record with verdict `satisfied`.

**P8-12-48** (MUST) [D] At every instant, no case file slot MUST hold a literal value whose `authority_component` names a component other than this one.

---

## 13. What could not be established

This section is a deliverable. A question reported as open is worth more than one answered by inference, and every item here was reached by attempting the establishment and failing, not by declining to try.

### 13.1 Questions left open by the consulted specifications

**Whether WS-HumanTask 1.1 is an approved OASIS Standard.** The version this part cites is styled Committee Specification 01, dated 17 August 2010. The OASIS page for the specification lists it under a standards path, and its own citation line reads Committee Specification 01. A later document at the latest version URI is styled Committee Specification Draft 12 / Public Review Draft 05 and is dated 2012. This part could not establish from the documents consulted whether version 1.1 was subsequently approved as an OASIS Standard, nor which of the two documents an implementer should treat as current. Clause citations in this part are to Committee Specification 01. An implementer intending to claim conformance to WS-HumanTask should establish the current status directly with OASIS.

**Sentry evaluation order in CMMN.** CMMN 1.1 §8.5 specifies the Sentry. This part could not establish from that section whether the specification constrains the order in which sentries triggered by a single event are evaluated, or whether it requires the result to be order independent. Published vendor documentation for a CMMN implementation states that the order and logic of sentry evaluation is not specified, and that runtime evaluation of the same model is therefore likely to differ between vendors; that statement is about CMMN 1.0. Whether CMMN 1.1 changed this could not be established. §6.1 imposes a confluence requirement on this part's own authority.

**The evaluation instant of a repetition rule.** CMMN 1.1 §5.4.11.3 and §8.6.4 define the RepetitionRule. Published implementation documentation states that the specification requires the repetition expression to be evaluated at the plan item's creation and maintained through its lifecycle, and that at least one implementation deliberately departs by evaluating on demand. This part could not verify the specification text on this point and requires the instant to be recorded (P8-6-60) rather than fixing it.

**The exact count and enumeration of the workflow resource patterns.** This part cites the pattern groups of the resource pattern catalogue, being creation, push, pull, detour, auto start, visibility and multiple resource patterns, and names individual patterns only where a consulted source named them. The total number of patterns in the catalogue was not verified against the working paper, and no clause of this part depends on the count.

**The current revision of the role based access control standard.** This part cites ANSI/INCITS 359 for the distinction between static and dynamic separation of duty relations. The current revision year was not verified. No clause depends on the revision.

**Whether CMMN's case file item lifecycle admits an unresolvable state.** CMMN 1.1 §8.3 specifies the CaseFileItem lifecycle and §8.3.1 its operations, with instance states and transitions in its Tables 8.1 and 8.2. This part could not establish from the sections consulted whether CMMN distinguishes a case file item whose referenced content no longer resolves from one that was discarded. §5.4 of this part distinguishes them on its own authority.

**Whether any consulted specification addresses case reopening.** CMMN 1.1 §8.4.1 specifies the case instance lifecycle including a closed state. This part could not find, in the sections consulted, any transition out of closed, nor any treatment of reopening a completed case. Secondary commentary states that CMMN has no way to reopen a completed plan item and that repetition is used instead. This part specifies reopening under §4.2.3 and §5.2 as its own requirement.

### 13.2 Requirements this part invents, and why

Every clause below is marked **Note.** and is a requirement of this part alone. They are listed here so that a reader can see the extent to which this part exceeds its sources, and so that an implementer can weigh each.

| Subject | Clauses | Why no specification supplies it |
|---|---|---|
| Human non results as a closed enumeration with reasons | P8-4-13, P8-7-05 to P8-7-11 | The consulted specifications model a task as producing an outcome or failing. Neither models a competent performer who cannot decide, which is a normal and informative result of governed human work |
| The presentation pin | P8-3-29 to P8-3-34 | WS-HumanTask specifies rendering as out of scope at §3.6 and §4.5, so what was shown is by construction not recorded |
| Choice breadth | P8-3-31, P8-3-32, P8-3-36, P8-8-33 | Possible outcomes are declared at definition level in WS-HumanTask §4.4; the set actually offered at an instant is not recorded anywhere |
| The indeterminate gate as a state | P8-5-12, P8-6-19 to P8-6-23 | WS-HumanTask §4.8.1 requires the opposite. CMMN does not address evaluation failure |
| The three way distinction in candidate derivation | P8-3-22, P8-6-28 to P8-6-30, P8-7-12 to P8-7-14 | WS-HumanTask §3.5.1 requires the collapse of two of the three |
| Attention separated from candidacy | P8-3-26 to P8-3-28, P8-11-08 | No consulted specification models visibility separately from eligibility |
| Staleness and its acknowledgement | P8-3-20, P8-6-79 to P8-6-83 | CMMN §5.3.2.1 requires latest version resolution, which makes staleness inexpressible |
| Actor class and the accepted proposal | P8-6-63 to P8-6-68, P8-12-34 to P8-12-37 | The consulted specifications predate the question |
| Pinned working calendar | P8-6-75 | Deadlines are specified without reference to the calendar version used to compute them |
| Case reopening | P8-4-23, P8-5-02, P8-3-11, P8-3-12 | See §13.1 |
| Confluence requirement on gate evaluation | P8-6-02, P8-6-03, P8-6-07 | See §13.1 |
| Withdrawal by resolution as a distinct disposition | P8-3-58 to P8-3-60, P8-11-04 | WS-HumanTask §4.8 sets unfinished subtasks to Obsolete without distinguishing the cause |
| Lease on reservation | P8-6-44 to P8-6-48, P8-11-11 | No consulted specification bounds a reservation |
| Generation depth and repetition bounds | P8-6-11, P8-6-61 | Neither specification bounds cascading evaluation or repetition |

### 13.3 Questions this part does not answer

**How a candidate set should be derived.** This part requires the derivation to be pinned, recorded and re-performable. It does not specify the expression language, the organisational query model, or how capability and competence are represented, because those belong to `Part 10` and to the assignment expression language, and a specification of them here would bind the wrong component.

**What lease duration, generation depth or repetition bound is correct.** These are declared as implementation decisions with the reason stated at each clause. This part fixes only that a value must be declared, must be finite, and in one case a minimum.

**Whether a case may span organisations.** The case role binding model in §3.13 assumes parties resolvable in one organisational model. Cases in which parties belong to different organisations with no common directory were not analysed, and this part makes no requirement about them.

**How work should be presented.** Rendering is deliberately outside this part, consistent with WS-HumanTask §3.6. This part requires only that what was presented be recorded, which is a weaker requirement than specifying how to present it and a stronger requirement than specifying nothing.

**Whether the `undecidable` disposition should propagate to a case's completion basis in every case.** §7.6 provides `required_work_undecidable`, and §7.2.4 requires the definition to determine whether an undecidable disposition closes the item or requires a successor. Whether a case containing an undecidable required item should ever be permitted to complete is a governance question this part leaves to the case definition, and it is the most consequential open question in this part.

**How long a non result should be retained relative to a result.** §8.4 subjects both to `Part 1` retention. Whether a record of an indeterminate gate has the same evidentiary life as a record of a determination was not established.

### 13.4 Sources this part could not obtain

**The full text of CMMN 1.1 Clause 8.** The table of contents, Clauses 1 to 5.4.4 and the conformance and reference clauses were read directly. The execution semantics clause was cited from its table of contents entries and from its section titles, and its detailed state tables were not read in full. Clause citations to §8.3, §8.4.1, §8.4.2, §8.4.3, §8.5, §8.6 and §8.7 are therefore citations to sections whose titles and scope were verified and whose full text was not. Every clause of this part that depends on a CMMN state or transition name is marked **Note.** rather than **Source.** except where the name appears in text this part read.

**The full text of WS-HumanTask 1.1 Clauses 4.9 to 12.** Clauses 1 to 4.8.2 were read directly, including the passages this part cites as conflicts. Sections 4.9 to 12 were cited from the table of contents. Citations to §4.9, §4.10, §4.10.1, §4.10.2, §4.10.3, §4.11, §7.1 and §7.1.2 are to sections whose titles and scope were verified from the table of contents and whose full text was not read. The two conflicts this part turns on, at §3.5.1 and §4.8.1, were read in the specification's own words.

**The BPMN 2.0 and ISO/IEC 19510 text.** Not consulted directly. Cited only for the existence of the user task and the event based gateway, and no clause depends on it.

**The workflow resource and control flow pattern working papers.** Not obtained. Cited from their bibliographic records and from the CAiSE'05 paper's abstract and figure captions. No clause depends on a pattern definition, only on pattern names used as vocabulary.

**The case handling paper.** Not obtained. Its bibliographic record and its status as a non normative reference of CMMN 1.1 were verified. The term context tunneling is attributed to it on the strength of secondary use; a reader relying on §11.10 should verify the attribution.

**ANSI/INCITS 359.** Not obtained. Paywalled.

**ISO 10303, ISO 9001 and the records management standards.** Not consulted, being the province of `Part 1`.
