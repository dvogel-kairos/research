# KAIROS STD 003, KAIROS-EVT-06: Event Schema and Versioning Standard

**Standard.** KAIROS STD 003, the enterprise architecture standard.
**Part.** Pilot document, KAIROS-EVT series. Not yet mapped to a numbered Part.
**Title.** Event schema and versioning standard.
**Version.** 0.2.0, pilot.
**Status.** Pilot draft, for structural evaluation only.
**Date of issue.** Not issued. Drafted 2026-08-28.
**Supersedes.** KAIROS-EVT-06 v0.1.

## Binding of requirement language

As KAIROS-EVT-01. Clause identifiers in this document have the form `EVT06-S.N`.

## Conformance

As KAIROS-EVT-01, substituting this document.

## Clause index

| Clause | Modality | Subject |
| --- | --- | --- |
| **Section 1** | | **Scope and responsibilities** |
| `EVT06-1.1` | MUST | Purpose satisfaction |
| **Section 3** | | **Data model** |
| `EVT06-3.1` | MUST | `type` stability under compatible change |
| `EVT06-3.2` | MUST | Version increment on incompatible change |
| `EVT06-3.3` | SHOULD | Deprecation window |
| `EVT06-3.4` | MUST | `dataschema` immutability |
| `EVT06-3.5` | MUST NOT | Fixed-URI mutable-content approach prohibited |
| **Section 4** | | **Interfaces** |
| `EVT06-4.1` | MUST | Stability declaration timing |
| **Section 7** | | **Outcome and failure taxonomy** |
| `EVT06-7.1` | MUST | Outcome vocabulary |
| **Section 13** | | **What could not be established** |
| `EVT06-13.1` | MUST | Practice basis recorded |
| `EVT06-13.2` | MUST | Gaps declared, not filled |

## 1. Scope and responsibilities

### 1.1 What this component is

This document defines how the `type` and `dataschema` attributes (KAIROS-EVT-01) are used together to manage schema evolution of `data` without breaking existing consumers.

### 1.2 What this component is NOT

The component is not the taxonomy governing `type`'s content structure beyond the version segment; see KAIROS-EVT-02.

**`EVT06-1.1` (MUST) Purpose satisfaction.** An implementation must be able to determine, for any two versions of an event type's `data` schema, whether the change between them requires a `type` version increment under Section 3.

## 2. Terminology

**Backwardly-compatible change.** A change to `data`'s structure that every existing consumer can still correctly process without modification.

**Backwardly-incompatible change.** Any change that is not backwardly compatible.

## 3. Data model

**`EVT06-3.1` (MUST) `type` stability under compatible change.** Where a change to `data` is backwardly compatible, the `<version>` segment of `type` (KAIROS-EVT-02 Section 3.1) must not change.

**`EVT06-3.2` (MUST) Version increment on incompatible change.** Where a change to `data` is backwardly incompatible, the `<version>` segment must increment.

**`EVT06-3.3` (SHOULD) Deprecation window.** A producer should continue producing the prior `type` version for a documented deprecation window after introducing an incompatible change, to avoid disrupting consumers that have not yet migrated.

**`EVT06-3.4` (MUST) `dataschema` immutability.** Each `dataschema` URI value, once published, must be immutable; a schema change must be reflected by a new URI, never by changing the content served at an existing URI.

**`EVT06-3.5` (MUST NOT) Fixed-URI mutable-content approach prohibited.** An implementation must not adopt the upstream-permitted alternative of holding the `dataschema` URI fixed while changing its resolved content, since this breaks consumer-side caching by URI.

## 4. Interfaces

**`EVT06-4.1` (MUST) Stability declaration timing.** An implementation must decide and document its versioning approach for a given event type before declaring that type stable for external consumption, including the specific triggers that constitute a backwards-incompatible change for that type.

## 5. State model

A `dataschema` URI, once published, does not change state (`EVT06-3.4`); a `type` value's current version is state held in KAIROS-EVT-09's catalog, not in this document.

## 6. Execution semantics

A producer determines whether a proposed `data` change is compatible before publishing it, applies Section 3.1 or 3.2 accordingly, and, on an incompatible change, registers the new version and its deprecation window in KAIROS-EVT-09 before producing the first live instance.

## 7. Outcome and failure taxonomy

**`EVT06-7.1` (MUST) Outcome vocabulary.** A schema-change review must report exactly one of: `COMPATIBLE_NO_ACTION`, `INCOMPATIBLE_VERSION_REQUIRED`, or `INCOMPATIBLE_UNVERSIONED` (a nonconformity: an incompatible change shipped without a version increment).

## 8. Observability and the audit record

Every `INCOMPATIBLE_VERSION_REQUIRED` determination and the resulting new `type` and `dataschema` values must be recorded in the KAIROS-EVT-09 catalog entry for the affected event type.

## 9. Extension model

Not applicable; this document does not define an extension mechanism of its own.

## 10. Standards and specifications

CloudEvents Primer, Version 1.0.2, Cloud Native Computing Foundation, Versioning of CloudEvents section. Primary source for this document in full.

KAIROS-EVT-02 (Type & Naming Taxonomy), for the `<version>` segment format this document's increment rule applies to.

## 11. Anti patterns

**Incrementing `type` on every deploy.** Conflating a service's release cadence with its data schema's compatibility produces version churn that gives consumers no useful signal, since most releases do not change `data` at all.

**Silently repurposing a `dataschema` URI.** Changing what a `dataschema` URI resolves to, rather than publishing a new URI, breaks any consumer that cached the schema by that URI, exactly the failure mode `EVT06-3.5` exists to prevent.

## 12. Boundaries with other Parts

**KAIROS-EVT-01 (Envelope).** This document governs how `type` and `dataschema`, defined there, change over time; it does not redefine either attribute.

**KAIROS-EVT-02 (Type & Naming Taxonomy).** This document's Section 3.1 and 3.2 govern when the version segment KAIROS-EVT-02 Section 3.1 defines must change.

**KAIROS-EVT-09 (Catalog & Registry).** This document requires that versioning decisions and deprecation windows be recorded in the catalog; KAIROS-EVT-09 owns the catalog itself.

## 13. What could not be established

### 13.1 Automated compatibility detection

Sections 3.1 and 3.2 assume a human or process can correctly classify a `data` change as compatible or incompatible. No mechanism for automatically verifying this classification, for example schema-diffing tooling integrated into a CI pipeline, is specified.

**Open.** Whether KAIROS should require automated schema-compatibility checking before a producer may ship a `data` change, or whether manual classification per Section 6 is adequate given the deprecation window's role as a safety margin.

### 13.2 Practice basis

The immutable-URI approach mandated in `EVT06-3.4` and `EVT06-3.5` is the upstream-permitted approach the CloudEvents Primer describes as more convenient for consumers; the specification itself treats both approaches as valid and does not mandate either.

**`EVT06-13.1` (MUST) Practice basis recorded.** An implementation must record that the mandatory choice between the two upstream-permitted approaches is a KAIROS decision, not a CloudEvents requirement.

### 13.3 What this document deliberately did not attempt

No treatment of a schema registry's technical implementation, storage, or query interface is given; that is KAIROS-EVT-09's responsibility.

**`EVT06-13.2` (MUST) Gaps declared, not filled.** An implementation must not represent a matter listed in Section 13.3 as specified by this document.
