# KAIROS STD 003, KAIROS-EVT-03: Event Format Standard (JSON)

**Standard.** KAIROS STD 003, the enterprise architecture standard.
**Part.** Pilot document, KAIROS-EVT series. Not yet mapped to a numbered Part.
**Title.** Event format standard, JSON.
**Version.** 0.2.0, pilot.
**Status.** Pilot draft, for structural evaluation only.
**Date of issue.** Not issued. Drafted 2026-08-28.
**Supersedes.** KAIROS-EVT-03 v0.1.

## Binding of requirement language

As KAIROS-EVT-01. Clause identifiers in this document have the form `EVT03-S.N`.

## Conformance

As KAIROS-EVT-01, substituting this document.

## Clause index

| Clause | Modality | Subject |
| --- | --- | --- |
| **Section 1** | | **Scope and responsibilities** |
| `EVT03-1.1` | MUST | Purpose satisfaction |
| `EVT03-1.2` | MUST NOT | No attribute-set definition |
| `EVT03-1.3` | MUST NOT | Non-JSON formats prohibited without exception |
| **Section 3** | | **Data model** |
| `EVT03-3.1` | MUST | Type system mapping |
| `EVT03-3.2` | MUST | Null handling on decode |
| `EVT03-3.3` | MUST | Envelope media type |
| `EVT03-3.4` | MUST | Binary data encoding |
| `EVT03-3.5` | MUST | JSON-content data encoding |
| `EVT03-3.6` | MUST NOT | No mutual `data`/`data_base64` presence |
| `EVT03-3.7` | MUST | Batch media type |
| `EVT03-3.8` | MUST | Batch specversion uniformity |
| **Section 6** | | **Execution semantics** |
| `EVT03-6.1` | MUST | Content type declares mode |
| **Section 7** | | **Outcome and failure taxonomy** |
| `EVT03-7.1` | MUST | Outcome vocabulary |
| **Section 13** | | **What could not be established** |
| `EVT03-13.1` | MUST | Practice basis recorded |
| `EVT03-13.2` | MUST | Gaps declared, not filled |

## 1. Scope and responsibilities

### 1.1 What this component is

This document specifies how the attributes defined in KAIROS-EVT-01 are serialized as JSON, the sole event format KAIROS permits.

### 1.2 What this component is NOT

The component is not the attribute definition. Which attributes exist and their abstract types is KAIROS-EVT-01's responsibility.

**`EVT03-1.2` (MUST NOT) No attribute-set definition.** This document must not add, remove, or redefine any attribute; it may only define that attribute's JSON representation.

The component is not a transport binding.

**`EVT03-1.3` (MUST NOT) Non-JSON formats prohibited without exception.** An implementation must not serialize a KAIROS event using Avro, Protobuf, XML, or any format other than JSON, without a documented, approved exception.

**`EVT03-1.1` (MUST) Purpose satisfaction.** An implementation must be able to serialize any envelope conformant with KAIROS-EVT-01 into a JSON representation satisfying Section 3, and deserialize it back without loss of any attribute value.

## 2. Terminology

**Envelope (JSON sense).** The single JSON object representing a whole event, distinct from the attribute-set sense of "envelope" used in KAIROS-EVT-01.

**Structured-mode message.** A message in which event metadata and `data` are both encoded together using this format.

## 3. Data model

### 3.1 Type system mapping

**`EVT03-3.1` (MUST) Type system mapping.** Every KAIROS-EVT-01 attribute type must be serialized as follows: `Boolean` as a JSON boolean; `Integer` as a JSON number, integer component only; `String` as a JSON string; `Binary` as a Base64-encoded JSON string; `URI` and `URI-reference` as JSON strings; `Timestamp` as an RFC 3339-formatted JSON string.

**`EVT03-3.2` (MUST) Null handling on decode.** A decoder encountering a JSON `null` value for any optional attribute must treat it identically to that attribute being entirely absent.

### 3.2 Envelope

**`EVT03-3.3` (MUST) Envelope media type.** A single serialized KAIROS event must use the media type `application/cloudevents+json`.

### 3.3 Handling of `data`

**`EVT03-3.4` (MUST) Binary data encoding.** Where the runtime type of `data` is `Binary`, it must be Base64-encoded and stored under the member name `data_base64`, and `datacontenttype` must reflect the original binary format.

**`EVT03-3.5` (MUST) JSON-content data encoding.** Where `datacontenttype` declares JSON-formatted content, or is absent, `data` must be stored as a native JSON value under the member name `data`, not as a string-encoded document.

**`EVT03-3.6` (MUST NOT) No mutual `data`/`data_base64` presence.** A serialized event must not include both `data` and `data_base64` members simultaneously.

### 3.4 Batch format

**`EVT03-3.7` (MUST) Batch media type.** A batch of KAIROS events must be represented as a JSON array using media type `application/cloudevents-batch+json`.

**`EVT03-3.8` (MUST) Batch specversion uniformity.** Every event within a single batch must share the same `specversion` value.

## 4. Interfaces

As KAIROS-EVT-01 Section 4, substituting JSON serialization and deserialization as the interface operations governed.

## 5. State model

Not applicable; serialization is a pure transformation with no state of its own.

## 6. Execution semantics

**`EVT03-6.1` (MUST) Content type declares mode.** A receiver must determine whether a message is a single event, a batch, or non-CloudEvents content by inspecting the `Content-Type` value before attempting to parse the body as JSON.

## 7. Outcome and failure taxonomy

**`EVT03-7.1` (MUST) Outcome vocabulary.** A deserialization procedure must report exactly one of: `VALID`, `MALFORMED_JSON`, `TYPE_MAPPING_FAILURE`, or `AMBIGUOUS_DATA_MEMBER` (both `data` and `data_base64` present).

## 8. Observability and the audit record

As KAIROS-EVT-01 Section 8, substituting the outcome vocabulary of Section 7.

## 9. Extension model

Extension attributes are serialized identically to standard attributes, as top-level JSON members, per KAIROS-EVT-05 Section 4.1.

## 10. Standards and specifications

JSON Event Format for CloudEvents, Version 1.0.2, Cloud Native Computing Foundation. Primary source for this document.

RFC 8259, The JavaScript Object Notation (JSON) Data Interchange Format.

RFC 2046, Multipurpose Internet Mail Extensions (MIME) Part Two: Media Types.

RFC 4648, The Base16, Base32, and Base64 Data Encodings.

## 11. Anti patterns

**Double-encoding JSON `data`.** Storing a JSON-formatted payload as a string-encoded JSON document, rather than as a native JSON value under `data`, is explicitly prohibited by Section 3.5 and is one of the most common implementation defects observed in the wider CloudEvents ecosystem, since it superficially appears to work until a consumer attempts to query into the payload structurally.

**Assuming a fixed batch size.** Treating batch delivery as though it always contains exactly one event, or a specific fixed number, breaks the first time an intermediary batches differently.

## 12. Boundaries with other Parts

**KAIROS-EVT-01 (Envelope).** This document serializes but does not define the attributes; a conflict on attribute existence is resolved in favor of KAIROS-EVT-01.

**KAIROS-EVT-04 (Protocol Binding).** This document defines the JSON representation; KAIROS-EVT-04 defines how that representation maps onto HTTP content modes.

**KAIROS-EVT-05 (Extensions).** This document's Section 9 states the serialization rule for extensions; KAIROS-EVT-05 owns which extensions exist.

## 13. What could not be established

### 13.1 Practice basis

No clause in this document rests on practice; every requirement traces to the JSON Event Format specification or the RFCs cited in Section 10.

**`EVT03-13.1` (MUST) Practice basis recorded.** Not applicable; recorded here for structural consistency with the series template.

### 13.2 What this document deliberately did not attempt

No treatment of Avro, Protobuf, or XML formats is given, per Section 1.2.

No treatment of JSON Schema validation of `data` content itself is given; `dataschema` (KAIROS-EVT-01, KAIROS-EVT-06) is a reference, not an enforced validation mechanism under this document.

**`EVT03-13.2` (MUST) Gaps declared, not filled.** An implementation must not represent a matter listed in Section 13.2 as specified by this document.
