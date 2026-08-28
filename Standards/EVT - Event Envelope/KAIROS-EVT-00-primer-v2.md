# KAIROS STD 003, KAIROS-EVT-00: Event Handling Primer

**Standard.** KAIROS STD 003, the enterprise architecture standard.
**Part.** Pilot document, KAIROS-EVT series. Not yet mapped to a numbered Part.
**Title.** Event handling primer.
**Version.** 0.2.0, pilot.
**Status.** Pilot draft, for structural evaluation only.
**Date of issue.** Not issued. Drafted 2026-08-28.
**Supersedes.** KAIROS-EVT-00 v0.1.

## Why this document does not use the thirteen section template

KAIROS STD 003 Part 0 establishes the precedent this document follows: a document that specifies interaction or provides orientation, rather than a single component's behavior, is not obliged to use the thirteen section template built for components. This document is non-normative. It contains no MUST, MUST NOT, SHOULD, SHOULD NOT, or MAY clauses, and no clause identifiers. A reader who only needs to implement against the series should read KAIROS-EVT-01 directly and treat this document as optional background.

## 1. Purpose

This document orients a reader to why the KAIROS-EVT series standardizes on the CloudEvents specification, how the nine normative documents in the series divide the subject, and which parts of the series rest on substantial upstream source material versus which are KAIROS-original construction.

## 2. Background

CloudEvents originated inside the CNCF's Serverless Working Group, tasked with investigating a common event format to aid the portability of functions and the interoperability of event streams across cloud providers. The problem it solves: every major event publisher, AWS, Microsoft, Google, and others, described events in its own shape, forcing every consumer to write source-specific logic. The specification reached its stable 1.0 release in October 2019; KAIROS-EVT standardizes on 1.0.2, the current patch release of that same major version.

The specification set is layered into four kinds of documents, and this is the direct reason the KAIROS-EVT series itself is split into multiple normative documents rather than one:

1. A base specification defining the abstract information model, the attributes every event carries.
2. Extensions, optional attributes for specific use cases layered on top of the base model.
3. Event format encodings (JSON, Avro, Protobuf) defining serialization.
4. Protocol bindings (HTTP, AMQP, Kafka) defining how a serialized event moves over a specific transport.

## 3. Design decisions that shape the whole series

Three upstream decisions are worth understanding before reading any normative KAIROS-EVT document, because each one directly explains why a KAIROS-EVT document exists that has no CloudEvents-upstream equivalent to draw from.

**The specification defines interoperability of format, not of processing.** It says nothing about what a consumer does with an event once received, including delivery order, count, or reliability. KAIROS-EVT-08 exists because of this silence; every requirement in that document is Azure Event Grid-specific, not CloudEvents-derived, because there is no CloudEvents position to derive from.

**Security is an explicit non-goal upstream.** The Primer's own Non-Goals section names "mechanism for Authorization, Data Integrity and Confidentiality" as out of scope. KAIROS-EVT-07 is therefore almost entirely KAIROS-original, informed by the general privacy guidance the core specification does offer but not derived from a detailed upstream security model.

**Routing information is deliberately excluded from the event.** The working group concluded that any transport protocol already defines its own routing semantics, and that including a destination in the event itself would prevent redelivery to new actions or dead-letter queues. This is why `source` and `type` are classification and provenance metadata, never delivery addresses, a distinction KAIROS-EVT-01 states directly rather than leaving implicit.

## 4. How the series divides the subject, and what actually backs each document

| Document | Subject | Upstream depth |
|---|---|---|
| EVT-01 Envelope | Required and optional context attributes | Fully specified upstream (Core Specification) |
| EVT-02 Type & Naming Taxonomy | KAIROS-specific structure for `type` and `source` | Structural constraints specified upstream; the specific taxonomy is KAIROS-original |
| EVT-03 Format (JSON) | Byte-level JSON serialization | Fully specified upstream (JSON Event Format) |
| EVT-04 Protocol Binding (Event Grid) | HTTP transport mapping and Event Grid specifics | Fully specified upstream for the HTTP binding; Event Grid's own behavior is a second, independent source |
| EVT-05 Extensions | Structural rules and the recognized extension catalog | Structural rules specified upstream; catalog partially specified upstream (five documented extensions exist, KAIROS adopts a subset) |
| EVT-06 Schema & Versioning | `type` and `dataschema` evolution rules | Fully specified upstream (Primer, Versioning section) |
| EVT-07 Security & Compliance | PHI handling, encryption, access control, audit | Thin upstream (a few paragraphs); mostly KAIROS-original |
| EVT-08 Delivery Semantics | Idempotency, ordering, retry, dead-lettering | Not covered upstream at all; entirely Event Grid-derived |
| EVT-09 Catalog & Registry | Registration and discoverability of event types | Not covered upstream at all; entirely KAIROS-original |

Roughly half the series rests on substantial, citable upstream text. The other half is KAIROS filling a gap the upstream specification leaves open by design. Both halves are legitimate parts of a standard; they simply carry different evidentiary weight, and each normative document's own Section 13 says which kind of document it is.

## 5. Cross-references

KAIROS-EVT-01 through KAIROS-EVT-09. A composition document analogous to STD 003 Part 0, addressing how these nine documents interact as a system rather than pairwise, has not yet been drafted for this series.
