# KAIROS STD 003, KAIROS-EVT-04: Protocol Binding Standard, Azure Event Grid

**Standard.** KAIROS STD 003, the enterprise architecture standard.
**Part.** Pilot document, KAIROS-EVT series. Not yet mapped to a numbered Part.
**Title.** Protocol binding standard, Azure Event Grid.
**Version.** 0.2.0, pilot.
**Status.** Pilot draft, for structural evaluation only.
**Date of issue.** Not issued. Drafted 2026-08-28.
**Supersedes.** KAIROS-EVT-04 v0.1.

## Binding of requirement language

As KAIROS-EVT-01. Clause identifiers in this document have the form `EVT04-S.N`.

## Conformance

As KAIROS-EVT-01, substituting this document.

## Clause index

| Clause | Modality | Subject |
| --- | --- | --- |
| **Section 1** | | **Scope and responsibilities** |
| `EVT04-1.1` | MUST | Purpose satisfaction |
| `EVT04-1.2` | MUST NOT | No delivery guarantee stated here |
| **Section 3** | | **Data model** |
| `EVT04-3.1` | MUST | Schema requirement |
| `EVT04-3.2` | MUST NOT | Legacy schema prohibited for new topics |
| **Section 4** | | **Interfaces** |
| `EVT04-4.1` | MUST | Content mode support |
| `EVT04-4.2` | MUST | Structured mode content type |
| `EVT04-4.3` | MUST | Binary mode header mapping |
| `EVT04-4.4` | MUST | Header value percent-encoding |
| `EVT04-4.5` | MUST | Batch consumer tolerance |
| **Section 7** | | **Outcome and failure taxonomy** |
| `EVT04-7.1` | MUST | Outcome vocabulary |
| **Section 13** | | **What could not be established** |
| `EVT04-13.1` | MUST | Practice basis recorded |
| `EVT04-13.2` | MUST | Gaps declared, not filled |

## 1. Scope and responsibilities

### 1.1 What this component is

This document defines how a KAIROS-conformant event, per KAIROS-EVT-01 and serialized per KAIROS-EVT-03, is carried over Azure Event Grid, combining the CNCF HTTP Protocol Binding specification, which Event Grid implements, with Event Grid's own configuration requirements.

### 1.2 What this component is NOT

The component is not a delivery semantics specification.

**`EVT04-1.2` (MUST NOT) No delivery guarantee stated here.** This document must not be read as making any claim about delivery order, count, retry behavior, or dead-lettering; those are KAIROS-EVT-08's responsibility in full.

**`EVT04-1.1` (MUST) Purpose satisfaction.** An implementation must be able to determine, for any Event Grid topic configuration, whether it satisfies Section 3 and Section 4, independent of the delivery behavior that configuration will exhibit.

## 2. Terminology

**Binary content mode.** `data` is placed directly in the HTTP body; other attributes map to HTTP headers.

**Structured content mode.** Attributes and `data` are both placed in the HTTP body together, using KAIROS-EVT-03.

**Batched content mode.** Multiple events, structured-mode, in a single HTTP body as a JSON array.

## 3. Data model

**`EVT04-3.1` (MUST) Schema requirement.** Every KAIROS Event Grid topic must be configured to use the CloudEvents v1.0 schema.

**`EVT04-3.2` (MUST NOT) Legacy schema prohibited for new topics.** A new Event Grid topic must not be configured to use the Event Grid-proprietary event schema; Microsoft's own documentation states that schema will receive no further improvement.

## 4. Interfaces

**`EVT04-4.1` (MUST) Content mode support.** An implementation must support structured content mode and should support binary content mode.

**`EVT04-4.2` (MUST) Structured mode content type.** Where structured mode is used, the `Content-Type` header must be `application/cloudevents+json; charset=UTF-8`.

**`EVT04-4.3` (MUST) Binary mode header mapping.** Where binary mode is used, every KAIROS-EVT-01 attribute other than `data` must be mapped to an HTTP header of the form `ce-<attributename>`.

**`EVT04-4.4` (MUST) Header value percent-encoding.** A header value derived from an attribute must be percent-encoded for any character outside the printable ASCII range U+0021 to U+007E, or that is a space, double-quote, or percent sign, per the upstream binding specification Section 3.1.3.2.

**`EVT04-4.5` (MUST) Batch consumer tolerance.** A consumer must correctly process a batch of size one and must not assume a fixed or minimum batch size.

## 5. State model

Not applicable to the binding itself; see KAIROS-EVT-08 for the state considerations of delivery.

## 6. Execution semantics

A receiver determines content mode by inspecting `Content-Type`: a value prefixed `application/cloudevents` indicates structured mode, a value prefixed `application/cloudevents-batch` indicates batched mode, and any other value defaults to binary mode.

## 7. Outcome and failure taxonomy

**`EVT04-7.1` (MUST) Outcome vocabulary.** A binding-level validation procedure must report exactly one of: `CONFORMANT`, `WRONG_SCHEMA_CONFIGURED`, `CONTENT_MODE_AMBIGUOUS`, or `HEADER_ENCODING_VIOLATION`.

## 8. Observability and the audit record

As KAIROS-EVT-01 Section 8, substituting the outcome vocabulary of Section 7.

## 9. Extension model

Extension attributes follow the same header-mapping rule as standard attributes in binary mode (Section 4.3); no additional binding-level extension mechanism exists.

## 10. Standards and specifications

HTTP Protocol Binding for CloudEvents, Version 1.0.2, Cloud Native Computing Foundation. Primary source for Section 4.

Azure Event Grid documentation, Microsoft. Primary source for Section 3 and the schema-deprecation basis of `EVT04-3.2`.

RFC 7230, Hypertext Transfer Protocol (HTTP/1.1): Message Syntax and Routing.

## 11. Anti patterns

**Configuring a new topic on the legacy Event Grid schema.** Beyond violating `EVT04-3.2` directly, this forfeits the portability the rest of the KAIROS-EVT series is built on, since the legacy schema has no relationship to the CloudEvents attribute model KAIROS-EVT-01 through KAIROS-EVT-03 define.

**Assuming `Content-Type` absence means binary mode is safe to parse without checking.** A message with no CloudEvents-prefixed `Content-Type` is not necessarily a CloudEvent at all; per the upstream specification, a receiver can only reasonably infer this if all mandatory attributes are present as headers, and even then correctness depends on the sender's intent, not a guarantee.

## 12. Boundaries with other Parts

**KAIROS-EVT-01 (Envelope), KAIROS-EVT-03 (JSON Format).** This document transports what those two documents define and serialize; it does not redefine either.

**KAIROS-EVT-08 (Delivery Semantics).** This document configures the transport; KAIROS-EVT-08 defines what a consumer may assume about how reliably and in what order that transport delivers.

## 13. What could not be established

### 13.1 Practice basis

The requirement that new topics avoid the legacy Event Grid schema (`EVT04-3.2`) rests on Microsoft's own current guidance rather than a CloudEvents specification requirement; the legacy schema is Event Grid's own prior design, not a CloudEvents-defined alternative.

**`EVT04-13.1` (MUST) Practice basis recorded.** An implementation citing `EVT04-3.2` as authority must record that its basis is current Microsoft product guidance, not the CloudEvents specification, since that guidance could change independent of any CloudEvents revision.

### 13.2 What this document deliberately did not attempt

No treatment of AMQP, Kafka, MQTT, or any binding other than HTTP is given, since Event Grid's native binding is HTTP-based.

No treatment of Event Grid namespace topics versus basic tier topics is given; whether this document's requirements apply identically to both tiers was not established.

**`EVT04-13.2` (MUST) Gaps declared, not filled.** An implementation must not represent a matter listed in Section 13.2 as specified by this document.
