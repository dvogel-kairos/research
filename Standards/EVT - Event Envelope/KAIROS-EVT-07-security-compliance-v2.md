# KAIROS STD 003, KAIROS-EVT-07: Event Security and Compliance Standard

**Standard.** KAIROS STD 003, the enterprise architecture standard.
**Part.** Pilot document, KAIROS-EVT series. Not yet mapped to a numbered Part.
**Title.** Event security and compliance standard.
**Version.** 0.2.0, pilot.
**Status.** Pilot draft, for structural evaluation only.
**Date of issue.** Not issued. Drafted 2026-08-28.
**Supersedes.** KAIROS-EVT-07 v0.1.

## Binding of requirement language

As KAIROS-EVT-01. Clause identifiers in this document have the form `EVT07-S.N`.

## Conformance

As KAIROS-EVT-01, substituting this document.

## Clause index

| Clause | Modality | Subject |
| --- | --- | --- |
| **Section 1** | | **Scope and responsibilities** |
| `EVT07-1.1` | MUST | Purpose satisfaction |
| **Section 3** | | **Data model** |
| `EVT07-3.1` | MUST NOT | Sensitive content attributes prohibited |
| `EVT07-3.2` | MUST | PHI encryption in transit |
| `EVT07-3.3` | MUST | PHI encryption at rest |
| `EVT07-3.4` | MUST | Subscription access control |
| `EVT07-3.5` | MUST | Audit logging for PHI-bearing types |
| `EVT07-3.6` | MUST NOT | No payload in audit or rejection logs |
| **Section 7** | | **Outcome and failure taxonomy** |
| `EVT07-7.1` | MUST | Outcome vocabulary |
| **Section 13** | | **What could not be established** |
| `EVT07-13.1` | MUST | Practice basis recorded |
| `EVT07-13.2` | MUST | Gaps declared, not filled |

## 1. Scope and responsibilities

### 1.1 What this component is

The upstream CloudEvents specification places "mechanism for Authorization, Data Integrity and Confidentiality" explicitly out of scope. This document is where KAIROS fills that gap, given PHI exposure risk across event traffic in SPARK and related systems.

### 1.2 What this component is NOT

The component is not the encryption mechanism itself; Azure Key Vault, governed by its own source-library entry, is the mechanism. This document states when encryption is required, not how it is implemented.

**`EVT07-1.1` (MUST) Purpose satisfaction.** An implementation must be able to determine, for any KAIROS event, whether it satisfies the content, encryption, access-control, and audit requirements of Section 3.

## 2. Terminology

**PHI-bearing event type.** An event `type` registered in the KAIROS-EVT-09 catalog with its PHI-bearing flag set to true.

**Context attribute.** As defined in KAIROS-EVT-01 Section 2.

## 3. Data model

### 3.1 Context attribute restrictions

**`EVT07-3.1` (MUST NOT) Sensitive content attributes prohibited.** An implementation must not place sensitive information, including PHI, in any context attribute (`type`, `source`, `subject`, or any extension attribute), since context attributes are commonly logged and inspected by intermediaries without deserializing `data`.

### 3.2 PHI in `data`

**`EVT07-3.2` (MUST) PHI encryption in transit.** Where `data` contains PHI, it must be protected by the transport-level TLS already required by KAIROS-EVT-04.

**`EVT07-3.3` (MUST) PHI encryption at rest.** Where `data` containing PHI is persisted, including in dead-letter destinations, replay logs, or audit stores, it must be encrypted at rest using Azure Key Vault-managed keys.

### 3.3 Access control

**`EVT07-3.4` (MUST) Subscription access control.** A subscription to a PHI-bearing event topic must be restricted to identities with an explicit, auditable business need, enforced via Entra ID role assignment, not via a shared secret or connection string.

### 3.4 Audit

**`EVT07-3.5` (MUST) Audit logging for PHI-bearing types.** Every event of a PHI-bearing type must be logged, at minimum by `id`, `source`, `type`, and `time`, to a retained audit store meeting HITRUST logging and monitoring control requirements.

**`EVT07-3.6` (MUST NOT) No payload in audit or rejection logs.** An audit or rejection log entry must not include the value of `data`, regardless of whether that specific event's `data` is believed to contain PHI.

## 4. Interfaces

An implementation must expose the PHI-bearing flag from KAIROS-EVT-09 to any component deciding whether Section 3.2, 3.3, or 3.5 applies to a given event type, since those requirements are conditional on that flag.

## 5. State model

Not applicable; this document's requirements attach to an event type's registration state (KAIROS-EVT-09), not to a per-instance state model.

## 6. Execution semantics

A producer must determine an event type's PHI-bearing status from the KAIROS-EVT-09 catalog before constructing the first instance of that type, and must apply Section 3.2 through 3.5 accordingly for every subsequent instance.

## 7. Outcome and failure taxonomy

**`EVT07-7.1` (MUST) Outcome vocabulary.** A compliance check must report exactly one of: `CONFORMANT`, `SENSITIVE_CONTEXT_ATTRIBUTE`, `UNENCRYPTED_PHI_TRANSIT`, `UNENCRYPTED_PHI_REST`, `SUBSCRIPTION_ACCESS_VIOLATION`, or `AUDIT_LOG_MISSING`.

## 8. Observability and the audit record

This document's Section 3.5 is itself the observability requirement for PHI-bearing event types; there is no separate, lesser observability tier for non-PHI-bearing types under this document, though KAIROS-EVT-01 Section 8's rejection logging applies uniformly regardless of PHI status.

## 9. Extension model

Not applicable; this document does not define an extension mechanism of its own, though it constrains what content any extension attribute, including a KAIROS-EVT-05 recognized extension, may carry (Section 3.1).

## 10. Standards and specifications

CloudEvents Core Specification v1.0.2, Privacy and Security section, Cloud Native Computing Foundation. Source for the general principle behind Section 3.1; the upstream text is general guidance, not a detailed requirement, and Sections 3.2 through 3.5 are KAIROS-original.

HIPAA Security Rule, 45 CFR Part 164, Subpart C. Source for the PHI encryption and access-control obligations this document operationalizes for event traffic specifically.

HITRUST CSF v11.8.0. Source for the audit and logging control basis of Section 3.5.

## 11. Anti patterns

**Using `subject` as a patient identifier.** This is the single most likely way Section 3.1 gets violated in practice, since `subject` is the attribute most naturally reused to carry a record identifier, and a patient medical record number in `subject` is PHI in a context attribute by definition.

**Encrypting `data` but not the dead-letter queue it lands in after a failed delivery.** A PHI-bearing event that fails delivery and is dead-lettered (KAIROS-EVT-08 Section 4.3) remains PHI; Section 3.3's at-rest requirement applies to every location the event is persisted, not only its primary path.

## 12. Boundaries with other Parts

**KAIROS-EVT-01 (Envelope).** This document restricts what context attributes, defined there, may contain; it does not redefine the attributes themselves.

**KAIROS-EVT-02 (Type & Naming Taxonomy).** KAIROS-EVT-02 Section 3.8 prohibits subject-identifying information in `type` and `source` specifically; this document's Section 3.1 is the broader rationale that clause implements.

**KAIROS-EVT-04 (Protocol Binding).** This document relies on, but does not define, the transport-level TLS Section 3.2 cites.

**KAIROS-EVT-08 (Delivery Semantics).** Dead-letter destinations created under KAIROS-EVT-08 Section 4.3 are subject to this document's Section 3.3 and 3.5 identically to primary delivery.

**KAIROS-EVT-09 (Catalog & Registry).** This document depends entirely on the PHI-bearing flag KAIROS-EVT-09 Section 4.1 requires; an incorrectly set flag is a compliance defect under this document even though the flag itself is KAIROS-EVT-09's data.

## 13. What could not be established

### 13.1 Encryption key rotation cadence for event-scoped keys

Section 3.3 requires at-rest encryption via Key Vault-managed keys but does not specify a rotation cadence specific to event data, as distinct from whatever general Key Vault rotation policy KAIROS otherwise maintains.

**Open.** Whether event-scoped PHI, given its typically short operational lifetime compared to a full medical record, warrants a different rotation cadence than the general policy, or whether adopting the general policy without modification is adequate.

### 13.2 Practice basis

Sections 3.2 through 3.5 in their entirety rest on HIPAA and HITRUST as the compliance basis, not on the CloudEvents specification, which is explicitly silent on security. Section 3.1's principle traces to the upstream specification's general privacy guidance, but its specific application to KAIROS's context attributes is this document's own extension of that principle.

**`EVT07-13.1` (MUST) Practice basis recorded.** An implementation must record that Sections 3.2 through 3.5 rest on HIPAA and HITRUST, not on the CloudEvents specification, wherever this document is cited as authority for those requirements.

### 13.3 What this document deliberately did not attempt

No treatment of non-PHI sensitive data (trade secrets, financial data not covered by HIPAA) is given; this document is scoped to PHI specifically, following the HIPAA and HITRUST sources it rests on.

No treatment of cross-border data residency for event traffic is given.

**`EVT07-13.2` (MUST) Gaps declared, not filled.** An implementation must not represent a matter listed in Section 13.3 as specified by this document.
