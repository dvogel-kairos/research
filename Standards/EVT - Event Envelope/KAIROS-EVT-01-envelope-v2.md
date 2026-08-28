# KAIROS STD 003, KAIROS-EVT-01: Event Envelope

**Standard.** KAIROS STD 003, the enterprise architecture standard.
**Part.** Pilot document, KAIROS-EVT series. Mapping to a numbered Part of STD 003 is not yet established; this document is written to the Part 1-13 template so that mapping decision can be made by comparison rather than by guesswork.
**Title.** Event envelope.
**Version.** 0.1.0, pilot.
**Status.** Pilot draft, for structural evaluation only. Not proposed, not issued for review.
**Date of issue.** Not issued. Drafted 2026-08-28.
**Supersedes.** KAIROS-EVT-01 v0.1 (generic template), superseded in full by this document.

## Binding of requirement language

The key words MUST, MUST NOT, SHOULD, SHOULD NOT and MAY in this document are to be interpreted as described in RFC 2119 and RFC 8174, and only in the upper case forms. This document does not use SHALL, SHALL NOT, REQUIRED, RECOMMENDED, NOT RECOMMENDED or OPTIONAL as requirement keywords, for the same reason given in KAIROS STD 003 Part 1: RFC 2119 treats several of them as synonyms, and mixing synonyms invites a reader to infer a distinction that was never intended.

Every requirement in this document is a numbered clause. A clause identifier has the form `EVT01-S.N`, where `S` is the section number and `N` is the ordinal of the clause within that section. Clause identifiers are permanent. A retired clause's identifier is never reissued.

Text that is not a numbered clause is not binding.

## Conformance

An implementation conforms to this document if it satisfies every MUST and MUST NOT clause and records, for each SHOULD and SHOULD NOT clause it does not satisfy, the reason. Conformance to this document alone does not constitute conformance to the KAIROS-EVT series; the series' own boundary and composition rules are the subject of a document analogous to STD 003 Part 0, not yet drafted for this series.

## Clause index

| Clause | Modality | Subject |
| --- | --- | --- |
| **Section 1** | | **Scope and responsibilities** |
| `EVT01-1.1` | MUST | Purpose satisfaction |
| `EVT01-1.2` | MUST NOT | No serialization semantics |
| `EVT01-1.3` | MUST NOT | No transport semantics |
| `EVT01-1.4` | MUST NOT | No naming structure |
| `EVT01-1.5` | MUST NOT | No delivery semantics |
| `EVT01-1.6` | MUST NOT | No security mechanism |
| **Section 2** | | **Terminology** |
| `EVT01-2.1` | MUST | Single meaning per term |
| `EVT01-2.2` | MUST NOT | No redefinition |
| **Section 3** | | **Data model** |
| `EVT01-3.1` | MUST | Required attribute presence |
| `EVT01-3.2` | MUST | Identity uniqueness |
| `EVT01-3.3` | MUST NOT | No meaning beyond uniqueness in `id` |
| `EVT01-3.4` | MUST | Type conformance |
| `EVT01-3.5` | MUST | Attribute naming character set |
| `EVT01-3.6` | SHOULD | Attribute name brevity |
| `EVT01-3.7` | MUST | `time` internal consistency |
| `EVT01-3.8` | MUST | Size limit, intermediary forwarding |
| `EVT01-3.9` | SHOULD | Size limit, consumer acceptance |
| **Section 4** | | **Interfaces** |
| `EVT01-4.1` | MUST | Construction completeness |
| `EVT01-4.2` | MUST NOT | No partial envelope exposure |
| **Section 5** | | **State model** |
| `EVT01-5.1` | MUST NOT | No mutation after construction |
| `EVT01-5.2` | MUST | Distinct identity on resend |
| **Section 6** | | **Execution semantics** |
| `EVT01-6.1` | MUST | Validation before transmission |
| `EVT01-6.2` | MUST | Validation order |
| **Section 7** | | **Outcome and failure taxonomy** |
| `EVT01-7.1` | MUST | Outcome vocabulary |
| `EVT01-7.2` | MUST NOT | No silent coercion |
| **Section 8** | | **Observability and the audit record** |
| `EVT01-8.1` | MUST | Rejection logging |
| `EVT01-8.2` | MUST NOT | No payload in rejection log |
| **Section 9** | | **Extension model** |
| `EVT01-9.1` | MUST | Extension structural conformance |
| `EVT01-9.2` | MUST NOT | No extension-only requirement |
| **Section 13** | | **What could not be established** |
| `EVT01-13.1` | MUST | Practice basis recorded |
| `EVT01-13.2` | MUST | Gaps declared, not filled |

## 1. Scope and responsibilities

### 1.1 What this component is

This document specifies the envelope of a KAIROS event: the fixed set of context attributes that every event carries, independent of how that event is serialized, transported, or delivered. It exists to answer one question: given a candidate event, does it carry the metadata a KAIROS consumer is entitled to assume is present, correctly typed, and internally consistent, before any consumer attempts to interpret `data`.

The component is accountable for:

Identity of the attribute set: which attributes exist, which are required, which are optional.

The type system those attributes draw from, and the canonical string encoding of each type.

Structural rules governing extension attributes, as distinct from which specific extensions exist.

Size constraints on the envelope as a whole.

### 1.2 What this component is NOT

The component is not a serialization format. How the attributes defined here are rendered as bytes, JSON, Avro, or otherwise, is KAIROS-EVT-03's responsibility. This document's data model is format-agnostic by construction.

**`EVT01-1.2` (MUST NOT) No serialization semantics.** This document must not be read as specifying byte-level or format-level representation of any attribute; such representation is the subject of KAIROS-EVT-03.

The component is not a transport binding. How an envelope moves over HTTP, Event Grid, or any other carrier is KAIROS-EVT-04's responsibility.

**`EVT01-1.3` (MUST NOT) No transport semantics.** This document must not be read as specifying header mapping, content mode, or any transport-level behavior; such behavior is the subject of KAIROS-EVT-04.

The component is not a naming authority. The internal structure required of the `type` and `source` values, beyond the type-system and character-set constraints in Section 3, is KAIROS-EVT-02's responsibility.

**`EVT01-1.4` (MUST NOT) No naming structure.** This document must not impose a structure on the content of `type` or `source` beyond Section 3; such structure is the subject of KAIROS-EVT-02.

The component is not a delivery guarantor. Whether an event arrives once, more than once, in order, or at all is KAIROS-EVT-08's responsibility, and follows from the transport chosen under KAIROS-EVT-04, not from anything in this document.

**`EVT01-1.5` (MUST NOT) No delivery semantics.** This document must not be read as making any claim about delivery order, count, or reliability.

The component is not a security control. What may or may not appear inside an otherwise-conformant attribute value, and what must happen to `data`, is KAIROS-EVT-07's responsibility.

**`EVT01-1.6` (MUST NOT) No security mechanism.** This document must not be read as specifying encryption, access control, or content restriction; such restriction is the subject of KAIROS-EVT-07.

**`EVT01-1.1` (MUST) Purpose satisfaction.** An implementation must be able to determine, for any candidate event and without reference to its serialized form, whether it satisfies the requirements of Section 3, by the procedure specified in Section 6.

## 2. Terminology

Definitions are given in the singular. A definition is not a clause and is not binding on its own.

**Occurrence.** The capture of a statement of fact during the operation of a system: a signal raised or observed, a state change, a timer elapsing, or comparable noteworthy activity. Follows CloudEvents Core Specification v1.0.2, section "Notations and Terminology."

**Event.** A data record expressing an occurrence and its context. A single occurrence MAY result in more than one event. Follows CloudEvents Core Specification v1.0.2.

**Producer.** The instance, process, or device that constructs the envelope for an event.

**Source.** The context in which the occurrence happened. A source MAY include more than one producer, in which case those producers MUST collaborate so that `source` plus `id` remains unique (Section 3.2). Follows CloudEvents Core Specification v1.0.2; KAIROS-EVT-02 additionally constrains the permitted structure of the `source` value.

**Consumer.** The process that receives an envelope and acts on it.

**Context attribute.** A named, typed metadata element of the envelope, as distinct from `data`, the event payload.

**Extension attribute.** A context attribute not enumerated in Section 3.1 or 3.2, governed structurally by Section 9 and, for the catalog of specific extensions KAIROS recognizes, by KAIROS-EVT-05.

**`EVT01-2.1` (MUST) Single meaning per term.** An implementation must use each term defined in this section with the meaning given here, in all interfaces, records, and documentation governed by this document.

**`EVT01-2.2` (MUST NOT) No redefinition.** An implementation must not use a term defined in this section for a different concept in any interface specified by this document.

## 3. Data model

### 3.1 Required attributes

Every envelope MUST include the following four attributes, each non-empty:

**`id`** (String). Identifies the event. The pair (`source`, `id`) MUST be unique for each distinct event. A resend of the same occurrence, for example after a network error, MAY reuse the same `id`; a consumer MAY treat two events with identical `source` and `id` as duplicates. The upstream CloudEvents specification asserts this uniqueness claim without specifying the mechanism by which a producer is to guarantee it; that gap is carried forward, unresolved, in Section 13.1, rather than papered over here.

**`source`** (URI-reference). Identifies the context of the occurrence. An absolute URI is RECOMMENDED by the upstream specification; KAIROS-EVT-02 makes this a MUST for KAIROS-produced events and further constrains its structure.

**`specversion`** (String). Identifies the version of the envelope specification in use.

**`type`** (String). Describes the type of event related to the occurrence. This document imposes no structure on its content beyond Section 3.4 and 3.5; KAIROS-EVT-02 imposes structure.

### 3.2 Optional attributes

**`datacontenttype`** (String, per RFC 2046). The media type of `data`. Governed further by KAIROS-EVT-03.

**`dataschema`** (URI). Identifies the schema `data` adheres to. Governed further by KAIROS-EVT-06.

**`subject`** (String). The subject of the event within the context of `source`.

**`time`** (Timestamp, per RFC 3339). When the occurrence happened, or, where the actual time cannot be determined, a substitute value.

### 3.3 Type system

Every attribute value MUST be one of: `Boolean`, `Integer` (signed 32-bit range), `String`, `Binary` (canonical encoding: Base64 per RFC 4648), `URI` (per RFC 3986 section 4.3), `URI-reference` (per RFC 3986 section 4.1), or `Timestamp` (per RFC 3339).

**`EVT01-3.4` (MUST) Type conformance.** Every context attribute value in a conformant envelope must satisfy the type constraint given for that attribute in Section 3.1 or 3.2, or, for an extension attribute, the type constraint declared for it under Section 9.

**`EVT01-3.1` (MUST) Required attribute presence.** A conformant envelope must include all four attributes of Section 3.1, each non-empty.

**`EVT01-3.2` (MUST) Identity uniqueness.** An implementation must ensure that the pair (`source`, `id`) is unique for each distinct event it produces, except where a resend of the same occurrence is intended.

**`EVT01-3.3` (MUST NOT) No meaning beyond uniqueness in `id`.** An implementation must not rely on any property of an `id` value other than its uniqueness within the scope of Section 3.2; in particular, `id` must not be used as a correlation key, a sort key, or a carrier of business meaning.

### 3.4 Attribute naming

**`EVT01-3.5` (MUST) Attribute naming character set.** Every attribute name, standard or extension, must consist only of lower-case ASCII letters (`a` to `z`) and digits (`0` to `9`).

**`EVT01-3.6` (SHOULD) Attribute name brevity.** An attribute name should be descriptive and terse and should not exceed 20 characters.

### 3.5 Internal consistency

**`EVT01-3.7` (MUST) `time` internal consistency.** Where an implementation cannot determine the actual occurrence time and substitutes another value, every producer for a given `source` must use the same substitution method, so that `time` values remain comparable across events from that source.

### 3.6 Size limits

**`EVT01-3.8` (MUST) Size limit, intermediary forwarding.** An intermediary must forward envelopes, inclusive of `data`, of 64 KB or less in wire size.

**`EVT01-3.9` (SHOULD) Size limit, consumer acceptance.** A consumer should accept envelopes of at least 64 KB in wire size.

## 4. Interfaces

**`EVT01-4.1` (MUST) Construction completeness.** An implementation exposing a construction interface for an envelope must not permit an envelope satisfying Section 3.1 to be returned or transmitted with any required attribute absent or empty.

**`EVT01-4.2` (MUST NOT) No partial envelope exposure.** An implementation must not expose a consumer-facing read interface that returns a subset of context attributes as though it were the whole envelope, without indicating that attributes have been filtered.

## 5. State model

An envelope, once constructed, has no state transitions. It is a single immutable value. This section exists to say so explicitly, since the absence of a state model is itself a property a consumer is entitled to rely on.

**`EVT01-5.1` (MUST NOT) No mutation after construction.** An implementation must not modify any attribute of an envelope after it has been transmitted to any consumer or intermediary.

**`EVT01-5.2` (MUST) Distinct identity on resend.** Where an implementation resends an occurrence with any attribute value changed other than transport metadata, the resulting envelope must be treated as a distinct event and is not exempt from Section 3.2's uniqueness requirement by virtue of representing the same occurrence.

## 6. Execution semantics

**`EVT01-6.1` (MUST) Validation before transmission.** An implementation must validate an envelope against Section 3 before transmitting it to any consumer or intermediary.

**`EVT01-6.2` (MUST) Validation order.** Validation must check required attribute presence (Section 3.1) before type conformance (Section 3.4), and type conformance before size limits (Section 3.6), so that a validation failure report identifies the most fundamental defect first.

## 7. Outcome and failure taxonomy

**`EVT01-7.1` (MUST) Outcome vocabulary.** A validation procedure conformant with Section 6 must report exactly one of: `VALID`, `MISSING_REQUIRED_ATTRIBUTE`, `TYPE_MISMATCH`, `NAMING_VIOLATION`, or `SIZE_EXCEEDED`, and must not report success where any of the latter four conditions holds.

**`EVT01-7.2` (MUST NOT) No silent coercion.** An implementation must not silently coerce an attribute value to satisfy Section 3.4; a value that requires coercion to conform must be reported as `TYPE_MISMATCH`.

## 8. Observability and the audit record

**`EVT01-8.1` (MUST) Rejection logging.** An implementation must record every envelope rejected under Section 7, at minimum by the outcome code, the attribute or attributes implicated, and a timestamp.

**`EVT01-8.2` (MUST NOT) No payload in rejection log.** A rejection log entry must not include the value of `data`, whether or not `data` is believed to contain sensitive information; see KAIROS-EVT-07 for the governing rationale.

## 9. Extension model

**`EVT01-9.1` (MUST) Extension structural conformance.** An extension attribute must satisfy Section 3.4 and Section 3.5 identically to a standard attribute.

**`EVT01-9.2` (MUST NOT) No extension-only requirement.** An implementation must not require the presence of any extension attribute for an envelope to be considered `VALID` under Section 7, unless that requirement is imposed by KAIROS-EVT-05 for a specific, named extension.

## 10. Standards and specifications

CloudEvents Specification, Version 1.0.2, Cloud Native Computing Foundation. Primary source for Sections 1 through 3.

RFC 2119, Key words for use in RFCs to Indicate Requirement Levels.

RFC 8174, Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words.

RFC 3339, Date and Time on the Internet: Timestamps.

RFC 3986, Uniform Resource Identifier (URI): Generic Syntax.

RFC 4648, The Base16, Base32, and Base64 Data Encodings.

RFC 2046, Multipurpose Internet Mail Extensions (MIME) Part Two: Media Types.

## 11. Anti patterns

**Using `id` as a business key.** Section 3.3 exists because implementations repeatedly reuse `id` as a correlation identifier or sort key once they notice it is unique. This silently couples consumer logic to a property (`id`'s uniqueness scope) that the producer is free to change.

**Treating `source` as a delivery address.** The upstream specification is explicit that routing information is deliberately excluded from the envelope; an implementation that parses `source` to determine where to send a response has reintroduced routing into a field that was designed to exclude it.

**Silent truncation at the size limit.** An implementation that truncates `data` to fit under 64 KB rather than rejecting or restructuring the event produces a `VALID`-looking envelope with corrupted content, which Section 7 is written to prevent by making size a distinct, reported failure mode.

## 12. Boundaries with other Parts

**KAIROS-EVT-00 (Primer).** Non-normative. This document does not restate the Primer's rationale and cites it only where a specific design decision needs grounding.

**KAIROS-EVT-02 (Type & Naming).** This document defines that `type` and `source` are strings and URI-references respectively; KAIROS-EVT-02 defines what those strings and references must contain. A conflict between the two on structural matters (character set, length) is resolved in favor of this document; a conflict on semantic structure is resolved in favor of KAIROS-EVT-02.

**KAIROS-EVT-03 (JSON Format).** This document is serialization-agnostic per Section 1.2. KAIROS-EVT-03 owns every byte-level representation decision.

**KAIROS-EVT-04 (Protocol Binding).** This document is transport-agnostic per Section 1.2. KAIROS-EVT-04 owns header mapping and content mode.

**KAIROS-EVT-05 (Extensions).** This document owns the structural rules any extension attribute must satisfy (Section 9). KAIROS-EVT-05 owns the catalog of which extensions exist and what they mean.

**KAIROS-EVT-06 (Schema & Versioning).** This document hosts the `type` and `dataschema` attributes. KAIROS-EVT-06 owns the rules governing how their values change over time.

**KAIROS-EVT-07 (Security & Compliance).** This document states, in Section 8.2, that a rejection log must not carry `data`. KAIROS-EVT-07 owns every other content-security requirement on attribute values.

**KAIROS-EVT-08 (Delivery Semantics).** This document makes no delivery claim per Section 1.2. KAIROS-EVT-08 owns idempotency, ordering, and retry.

**KAIROS-EVT-09 (Catalog & Registry).** This document does not require registration of any `type` value. KAIROS-EVT-09 owns the registration requirement and its timing.

## 13. What could not be established

### 13.1 The mechanism behind `id` uniqueness

Section 3.2 requires that (`source`, `id`) be unique, and Section 3.3 forbids relying on any other property of `id`. The upstream CloudEvents Core Specification asserts the same uniqueness requirement but states plainly that it does not explain how a producer is to guarantee it, describing this as out of the specification's scope. This document inherits that gap rather than closing it.

**Open.** Whether KAIROS should mandate a specific `id` generation scheme, for example UUIDv7 for its sortable-by-time property, or leave it producer-defined as the upstream specification does. A mandated scheme would let KAIROS-EVT-08 make stronger deduplication guarantees than idempotency-by-convention; an unmandated scheme preserves producer flexibility already assumed by existing non-KAIROS event sources that may need adapting.

### 13.2 What constitutes a distinct occurrence for resend purposes

Section 5.2 requires a resent event with a changed attribute to be treated as distinct, but does not state which attribute changes are administrative, transport-level metadata a resend may legitimately alter, versus substantive, changes that indicate a genuinely different occurrence. The upstream specification does not draw this line either.

**Open.** Whether this document or KAIROS-EVT-08 is the correct place to enumerate which attributes fall on which side of that line.

### 13.3 Practice basis

No clause of this document rests on practice rather than on the CloudEvents Core Specification, RFC 2119, RFC 8174, RFC 3339, RFC 3986, RFC 4648, or RFC 2046. This absence is itself notable: it means every normative statement here is directly traceable to a cited source, at the cost of leaving Section 13.1 and 13.2 open rather than settled by convention.

**`EVT01-13.1` (MUST) Practice basis recorded.** An implementation adopting a resolution to Section 13.1 or 13.2 as a local control must record that its basis is practice, not this document.

### 13.4 What this document deliberately did not attempt

No treatment of `id` generation scheme is given, per Section 13.1.

No treatment of which attribute changes constitute a distinct occurrence is given, per Section 13.2.

No performance or throughput requirement is stated for envelope construction or validation.

**`EVT01-13.2` (MUST) Gaps declared, not filled.** An implementation must not represent a matter listed in Section 13.4 as specified by this document.

### 13.5 Questions handed to a future KAIROS-EVT-00-equivalent composition document

Whether `id` generation should be standardized across the whole KAIROS-EVT series or left per-producer, since KAIROS-EVT-08's deduplication guarantees depend on the answer.

Which component in the broader KAIROS architecture, outside this series, owns the identity of a `source` value's issuing service, since this document treats `source` as an opaque URI and does not itself validate that the service it names exists or is authorized to produce under that name.
