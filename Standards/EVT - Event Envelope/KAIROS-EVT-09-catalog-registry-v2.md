# KAIROS STD 003, KAIROS-EVT-09: Event Catalog and Registry Standard

**Standard.** KAIROS STD 003, the enterprise architecture standard.
**Part.** Pilot document, KAIROS-EVT series. Not yet mapped to a numbered Part.
**Title.** Event catalog and registry standard.
**Version.** 0.2.0, pilot.
**Status.** Pilot draft, for structural evaluation only.
**Date of issue.** Not issued. Drafted 2026-08-28.
**Supersedes.** KAIROS-EVT-09 v0.1.

## Binding of requirement language

As KAIROS-EVT-01. Clause identifiers in this document have the form `EVT09-S.N`.

## Conformance

As KAIROS-EVT-01, substituting this document.

## Clause index

| Clause | Modality | Subject |
| --- | --- | --- |
| **Section 1** | | **Scope and responsibilities** |
| `EVT09-1.1` | MUST | Purpose satisfaction |
| **Section 3** | | **Data model** |
| `EVT09-3.1` | MUST | Mandatory catalog fields |
| `EVT09-3.2` | MUST | PHI-bearing flag presence |
| `EVT09-3.3` | MUST | Registration precedes production |
| **Section 4** | | **Interfaces** |
| `EVT09-4.1` | MUST | Query by domain |
| `EVT09-4.2` | MUST | Query by owning service |
| `EVT09-4.3` | MUST | Query by PHI-bearing status |
| **Section 7** | | **Outcome and failure taxonomy** |
| `EVT09-7.1` | MUST | Outcome vocabulary |
| **Section 13** | | **What could not be established** |
| `EVT09-13.1` | MUST | Practice basis recorded |
| `EVT09-13.2` | MUST | Gaps declared, not filled |

## 1. Scope and responsibilities

### 1.1 What this component is

This document defines the single, authoritative record of every event `type` a KAIROS system produces or consumes: what it means, who owns it, its current and deprecated schema versions, and whether it carries PHI. The CloudEvents specification does not define a catalog concept at all; this document's shape is informed by the general pattern of an API catalog, not extracted from any upstream source.

### 1.2 What this component is NOT

The component is not a schema store. It records a `dataschema` URI per KAIROS-EVT-06; it does not host or serve the schema content itself.

**`EVT09-1.1` (MUST) Purpose satisfaction.** An implementation must be able to answer, for any registered event `type`, its owning service, its current and prior `dataschema` values, its PHI-bearing status, and its deprecation window if any, from the catalog alone.

## 2. Terminology

**Catalog entry.** The registered record for one event `type` value.

**Owning service.** The KAIROS service authorized to produce a given event `type`.

## 3. Data model

**`EVT09-3.1` (MUST) Mandatory catalog fields.** Every catalog entry must include: the full `type` string (KAIROS-EVT-02 Section 3.1); the owning service and its `source` value (KAIROS-EVT-02 Section 3.2); the current `dataschema` URI and all prior, non-retired versions (KAIROS-EVT-06); a PHI-bearing flag; the deprecation window, if any prior version is still being produced (KAIROS-EVT-06 Section 3.3); and a human-readable description of the occurrence the event represents.

**`EVT09-3.2` (MUST) PHI-bearing flag presence.** The PHI-bearing flag must be an explicit boolean value for every catalog entry; it must not be left unset or inferred from the event type's name.

**`EVT09-3.3` (MUST) Registration precedes production.** An event `type` must be registered in the catalog before its owning service produces its first live instance of that type. Retroactive registration of an already-shipping event type is a nonconformity to be remediated, not a normal registration path.

## 4. Interfaces

**`EVT09-4.1` (MUST) Query by domain.** The catalog must be queryable by the domain segment defined in KAIROS-EVT-02 Section 3.1.

**`EVT09-4.2` (MUST) Query by owning service.** The catalog must be queryable by owning service.

**`EVT09-4.3` (MUST) Query by PHI-bearing status.** The catalog must be queryable by PHI-bearing status, so a new consuming service can determine what it is subscribing to before doing so, without inspecting a live event sample first.

## 5. State model

A catalog entry transitions through registration (Section 3.3), active production, and, where superseded per KAIROS-EVT-06, deprecation. This document does not specify a retirement or deletion state for a catalog entry; see Section 13.1.

## 6. Execution semantics

Registration must occur before first production (Section 3.3). A schema-versioning event under KAIROS-EVT-06 Section 6 must update the affected catalog entry's `dataschema` history and deprecation window as part of the same change, not as a separate, later step.

## 7. Outcome and failure taxonomy

**`EVT09-7.1` (MUST) Outcome vocabulary.** A catalog conformance check must report exactly one of: `REGISTERED_CONFORMANT`, `MISSING_MANDATORY_FIELD`, `UNSET_PHI_FLAG`, or `PRODUCED_BEFORE_REGISTRATION`.

## 8. Observability and the audit record

Every change to a catalog entry, including PHI-flag changes, schema version additions, and deprecation window changes, must be recorded with the identity of the actor making the change and a timestamp, since the catalog is itself the audit trail KAIROS-EVT-06 and KAIROS-EVT-07 depend on.

## 9. Extension model

Not applicable; this document does not define an extension mechanism of its own, though a catalog entry may reference which KAIROS-EVT-05 extensions a given event type is expected to carry.

## 10. Standards and specifications

KAIROS-EVT-02 (Type & Naming Taxonomy), for the domain and service-name values a catalog entry's identity depends on.

KAIROS-EVT-06 (Schema & Versioning), for the versioning history a catalog entry must carry.

KAIROS-EVT-07 (Security & Compliance), for the consequence of the PHI-bearing flag this document requires.

No CloudEvents specification text is cited, since none exists on this subject; see Section 13.2.

## 11. Anti patterns

**Registering an event type with the PHI-bearing flag defaulted to false.** A default-false flag that nobody actively confirms is a compliance defect waiting to surface the first time that event type actually carries PHI; `EVT09-3.2` requires an explicit value specifically to prevent a silent default from substituting for a decision.

**Treating the catalog as documentation rather than as enforced state.** A catalog that a producer can bypass by shipping an unregistered event type defeats `EVT09-3.3`'s purpose; the catalog must be a gate, not a wiki page nobody is required to consult.

## 12. Boundaries with other Parts

**KAIROS-EVT-02 (Type & Naming Taxonomy).** This document's identity fields (Section 3.1) depend on the domain and service-name structure KAIROS-EVT-02 defines; a conflict on what constitutes a valid domain or service name is resolved in favor of KAIROS-EVT-02.

**KAIROS-EVT-06 (Schema & Versioning).** This document stores what KAIROS-EVT-06 decides; KAIROS-EVT-06 owns the compatibility judgment, this document owns the record of that judgment's outcome.

**KAIROS-EVT-07 (Security & Compliance).** This document's PHI-bearing flag is the trigger mechanism for every Section 3 requirement in KAIROS-EVT-07; an incorrectly set flag here is a compliance defect there.

## 13. What could not be established

### 13.1 Catalog entry retirement

Section 5 does not specify what happens to a catalog entry for an event type that a service stops producing entirely, as distinct from superseding with a new version under KAIROS-EVT-06. Whether such an entry should be marked retired, archived, or left indefinitely as active is not established.

**Open.** Whether an obsolescence concept analogous to STD 003 Part 1's lineage-level obsolescence (as distinct from version-level supersession or withdrawal) is needed for event types, and if so, whether it belongs in this document or in a future composition document for the KAIROS-EVT series.

### 13.2 Practice basis

This document in its entirety is KAIROS-original. No upstream CloudEvents source addresses cataloging or registry concepts; the shape adopted here, a queryable record with mandatory fields and a registration gate, follows the general pattern of an API catalog rather than any cited specification.

**`EVT09-13.1` (MUST) Practice basis recorded.** An implementation must record that this document in its entirety rests on practice, not on the CloudEvents specification or any other cited standard, wherever it is invoked as authority.

### 13.3 What this document deliberately did not attempt

No treatment of the catalog's technical storage mechanism, query language, or hosting platform is given.

No treatment of catalog access control (who may register or modify an entry) is given; this is assumed to follow general KAIROS identity and access governance, not restated here.

**`EVT09-13.2` (MUST) Gaps declared, not filled.** An implementation must not represent a matter listed in Section 13.3 as specified by this document.
