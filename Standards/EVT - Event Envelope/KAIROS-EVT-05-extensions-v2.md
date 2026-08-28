# KAIROS STD 003, KAIROS-EVT-05: Event Extensions Standard

**Standard.** KAIROS STD 003, the enterprise architecture standard.
**Part.** Pilot document, KAIROS-EVT series. Not yet mapped to a numbered Part.
**Title.** Event extensions standard.
**Version.** 0.2.0, pilot.
**Status.** Pilot draft, for structural evaluation only.
**Date of issue.** Not issued. Drafted 2026-08-28.
**Supersedes.** KAIROS-EVT-05 v0.1, which flagged this document's Section 4 catalog as incomplete pending a fetch of the Documented Extensions specification. That fetch has now occurred; see Section 3.2.

## Binding of requirement language

As KAIROS-EVT-01. Clause identifiers in this document have the form `EVT05-S.N`.

## Conformance

As KAIROS-EVT-01, substituting this document.

## Clause index

| Clause | Modality | Subject |
| --- | --- | --- |
| **Section 1** | | **Scope and responsibilities** |
| `EVT05-1.1` | MUST | Purpose satisfaction |
| **Section 3** | | **Data model** |
| `EVT05-3.1` | MUST | Structural conformance |
| `EVT05-3.2` | MUST | Top-level serialization |
| `EVT05-3.3` | SHOULD | Minimality |
| `EVT05-3.4` | MUST NOT | No domain data in extensions |
| **Section 4** | | **Recognized extension catalog** |
| `EVT05-4.1` | MUST | Distributed tracing adoption |
| `EVT05-4.2` | MUST | Dataref conditions |
| `EVT05-4.3` | MAY | Sequence adoption |
| `EVT05-4.4` | MUST NOT | Partitioning and sampled-rate not adopted |
| **Section 7** | | **Outcome and failure taxonomy** |
| `EVT05-7.1` | MUST | Outcome vocabulary |
| **Section 13** | | **What could not be established** |
| `EVT05-13.1` | MUST | Practice basis recorded |
| `EVT05-13.2` | MUST | Gaps declared, not filled |

## 1. Scope and responsibilities

### 1.1 What this component is

This document governs how KAIROS defines and uses CloudEvents extension attributes: the structural rules every extension must follow, and the catalog of specific extensions KAIROS recognizes.

### 1.2 What this component is NOT

The component is not the base attribute set; see KAIROS-EVT-01. It is not a serialization rule beyond citing KAIROS-EVT-03's top-level-placement requirement.

**`EVT05-1.1` (MUST) Purpose satisfaction.** An implementation must be able to determine, for any extension attribute a KAIROS event carries, whether it is structurally conformant (Section 3) and whether it is a recognized extension (Section 4).

## 2. Terminology

**Extension attribute.** An additional context attribute beyond KAIROS-EVT-01 Sections 3.1 and 3.2, with no meaning defined by the base specification.

**Documented extension.** An extension formally specified by the upstream CloudEvents project, as distinct from an ad hoc, undocumented extension a producer might introduce independently.

## 3. Data model

**`EVT05-3.1` (MUST) Structural conformance.** An extension attribute must satisfy the naming convention and type system of KAIROS-EVT-01 Sections 3.4 and 3.5 identically to a standard attribute.

**`EVT05-3.2` (MUST) Top-level serialization.** Per KAIROS-EVT-03, an extension attribute must be serialized as a top-level JSON member alongside standard attributes, never nested under a separate `extensions` property.

**`EVT05-3.3` (SHOULD) Minimality.** An implementation should keep the aggregate size and number of extension attributes minimal, since HTTP binary mode maps every attribute to a header and many HTTP servers reject requests once aggregate header size passes limits as low as 8 KB.

**`EVT05-3.4` (MUST NOT) No domain data in extensions.** An implementation must not use an extension attribute to carry information that belongs in `data`; an extension attribute is warranted only where the information is needed for routing, correlation, or pre-deserialization processing.

## 4. Recognized extension catalog

The upstream CloudEvents project documents five extensions: Dataref (the claim check pattern), Distributed Tracing, Partitioning, Sampled Rate, and Sequence. KAIROS adopts a subset.

**`EVT05-4.1` (MUST) Distributed tracing adoption.** An implementation must support the Distributed Tracing extension (`traceparent`, `tracestate`), embedding W3C Trace Context, for correlating KAIROS events with the OpenTelemetry entry in the KAIROS source library. Where an event traverses a single hop from source to sink directly, the extension's attribute values must carry the same trace information as any protocol-specific tracing headers present on the same message; where the two would differ, the value produced by general CloudEvents serialization rules (the extension attribute) governs.

**`EVT05-4.2` (MUST) Dataref conditions.** An implementation may use the Dataref extension (claim check pattern) to reference a location where `data` is stored instead of, or in addition to, embedding it directly, and where both `data` and `dataref` are present, the information at both must be identical.

**`EVT05-4.3` (MAY) Sequence adoption.** An implementation may adopt the Sequence extension where a consumer requires an explicit ordering signal; see KAIROS-EVT-08 Section 4.2, which states that Event Grid provides no ordering guarantee this extension could rely on being honored by the transport.

**`EVT05-4.4` (MUST NOT) Partitioning and sampled-rate not adopted.** An implementation must not rely on the Partitioning or Sampled Rate extensions as part of a conformant KAIROS event; neither is currently adopted, pending the open question in Section 13.1.

## 5. State model

Not applicable.

## 6. Execution semantics

Validation of extension attributes proceeds after KAIROS-EVT-01 Section 6.1's base validation and after KAIROS-EVT-02's taxonomy validation, since an extension attribute cannot be meaningfully checked against Section 4 until the base envelope is known to be well-formed.

## 7. Outcome and failure taxonomy

**`EVT05-7.1` (MUST) Outcome vocabulary.** A validation procedure must report exactly one of: `NO_EXTENSIONS_PRESENT`, `RECOGNIZED_EXTENSIONS_CONFORMANT`, `UNSTRUCTURED_EXTENSION` (fails Section 3.1), or `UNRECOGNIZED_EXTENSION` (present but not in Section 4, which is not itself a conformance failure per `EVT05-3.1` unless Section 3 is also violated, but must be reported so the catalog can be extended deliberately rather than by accretion).

## 8. Observability and the audit record

An implementation must log any `UNRECOGNIZED_EXTENSION` occurrence, since a pattern of the same undocumented extension appearing repeatedly is the trigger for a deliberate Section 4 revision rather than continued ad hoc use.

## 9. Extension model

This document is itself about the extension model; see Section 3 and Section 4.

## 10. Standards and specifications

CloudEvents Documented Extensions specification, Cloud Native Computing Foundation. Primary source for Section 4's catalog.

CloudEvents Distributed Tracing Extension specification. Primary source for `EVT05-4.1`.

CloudEvents Dataref (Claim Check Pattern) Extension specification. Primary source for `EVT05-4.2`.

W3C Trace Context. Referenced by the Distributed Tracing extension for the `traceparent`/`tracestate` structure.

CloudEvents Core Specification v1.0.2, Extension Context Attributes section. Primary source for Section 3.

## 11. Anti patterns

**Reinventing an undocumented tracing extension.** Where distributed tracing correlation is needed, using a custom attribute name instead of the documented `traceparent`/`tracestate` pair forfeits interoperability with any tooling built against the standard extension, for no benefit.

**Growing the unrecognized-extension list without ever revisiting Section 4.** `EVT05-7.1`'s `UNRECOGNIZED_EXTENSION` outcome exists specifically so this doesn't happen silently; an implementation that logs the outcome but never acts on the pattern has defeated the purpose of collecting it.

## 12. Boundaries with other Parts

**KAIROS-EVT-01 (Envelope).** This document's structural rules extend, but do not alter, KAIROS-EVT-01 Sections 3.4 and 3.5.

**KAIROS-EVT-03 (JSON Format).** This document's Section 3.2 restates, and does not override, KAIROS-EVT-03's serialization rule for extensions.

**KAIROS-EVT-08 (Delivery Semantics).** The Sequence extension (Section 4.3) interacts directly with KAIROS-EVT-08 Section 4.2's no-ordering-guarantee requirement; a consumer must not treat Sequence's presence as overriding that guarantee unless KAIROS-EVT-08 is separately revised.

## 13. What could not be established

### 13.1 Whether Partitioning or Sampled Rate should be adopted

Section 4.4 currently excludes both. Partitioning could plausibly assist consumers that need to distribute processing across a fixed number of workers while preserving order within a partition key; Sampled Rate could plausibly assist high-volume telemetry-style events where full delivery is not required. Neither has an identified KAIROS use case as of this draft.

**Open.** Whether a concrete SPARK or NorthStar use case will surface a need for either extension, at which point Section 4.4 would need revision rather than an ad hoc, undocumented workaround being adopted first.

### 13.2 Practice basis

The specific subset adopted in Section 4 (mandatory tracing, conditional dataref, optional sequence, excluded partitioning and sampled-rate) is a KAIROS decision informed by, but not dictated by, the upstream catalog, which takes no position on which extensions any adopter should use.

**`EVT05-13.1` (MUST) Practice basis recorded.** An implementation must record that the specific adoption decisions in Section 4 are KAIROS-original, not upstream requirements.

### 13.3 What this document deliberately did not attempt

No treatment of defining a new, KAIROS-original extension not present in the upstream Documented Extensions catalog is given.

**`EVT05-13.2` (MUST) Gaps declared, not filled.** An implementation must not represent a matter listed in Section 13.3 as specified by this document.
