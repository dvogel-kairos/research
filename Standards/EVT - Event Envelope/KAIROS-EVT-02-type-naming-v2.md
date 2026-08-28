# KAIROS STD 003, KAIROS-EVT-02: Event Type and Naming Taxonomy

**Standard.** KAIROS STD 003, the enterprise architecture standard.
**Part.** Pilot document, KAIROS-EVT series. Not yet mapped to a numbered Part.
**Title.** Event type and naming taxonomy.
**Version.** 0.2.0, pilot.
**Status.** Pilot draft, for structural evaluation only.
**Date of issue.** Not issued. Drafted 2026-08-28.
**Supersedes.** KAIROS-EVT-02 v0.1.

## Binding of requirement language

As KAIROS-EVT-01 Binding of requirement language. Clause identifiers in this document have the form `EVT02-S.N`.

## Conformance

As KAIROS-EVT-01 Conformance, substituting this document.

## Clause index

| Clause | Modality | Subject |
| --- | --- | --- |
| **Section 1** | | **Scope and responsibilities** |
| `EVT02-1.1` | MUST | Purpose satisfaction |
| `EVT02-1.2` | MUST NOT | No attribute type definition |
| `EVT02-1.3` | MUST NOT | No serialization or transport rule |
| **Section 2** | | **Terminology** |
| `EVT02-2.1` | MUST | Single meaning per term |
| **Section 3** | | **Data model** |
| `EVT02-3.1` | MUST | `type` structure |
| `EVT02-3.2` | MUST | Domain segment registration |
| `EVT02-3.3` | MUST | Entity segment singularity |
| `EVT02-3.4` | MUST | Action segment tense |
| `EVT02-3.5` | MUST | Version segment format |
| `EVT02-3.6` | MUST | `source` structure |
| `EVT02-3.7` | MUST NOT | Environment identifiers prohibited |
| `EVT02-3.8` | MUST NOT | Subject identifying information prohibited |
| **Section 4** | | **Interfaces** |
| `EVT02-4.1` | MUST | Validation availability |
| **Section 6** | | **Execution semantics** |
| `EVT02-6.1` | MUST | Validation timing |
| **Section 7** | | **Outcome and failure taxonomy** |
| `EVT02-7.1` | MUST | Outcome vocabulary |
| **Section 9** | | **Extension model** |
| `EVT02-9.1` | MUST NOT | No taxonomy extension without registration |
| **Section 13** | | **What could not be established** |
| `EVT02-13.1` | MUST | Practice basis recorded |
| `EVT02-13.2` | MUST | Gaps declared, not filled |

## 1. Scope and responsibilities

### 1.1 What this component is

This document closes a gap the upstream CloudEvents specification leaves open by design: it defines the mandatory internal structure of the `type` and `source` attribute values (KAIROS-EVT-01 Sections 3.1) for every KAIROS-produced event, so that type strings are predictable, sortable, and collision-free without requiring a central lookup for every new event type before it can be parsed.

### 1.2 What this component is NOT

The component is not the attribute type system. What data type `type` and `source` are, string and URI-reference respectively, and their character set and length constraints, is KAIROS-EVT-01's responsibility. This document constrains content within that type, not the type itself.

**`EVT02-1.2` (MUST NOT) No attribute type definition.** This document must not restate or alter the type, character set, or length constraints KAIROS-EVT-01 places on `type` or `source`; it must only further constrain their content.

The component is not a serialization or transport rule. How a `type` string is encoded on the wire is KAIROS-EVT-03 and KAIROS-EVT-04's responsibility.

**`EVT02-1.3` (MUST NOT) No serialization or transport rule.** This document must not be read as specifying byte-level representation or transport mapping of `type` or `source`.

**`EVT02-1.1` (MUST) Purpose satisfaction.** An implementation must be able to determine, for any candidate `type` or `source` value, whether it satisfies Section 3, without reference to any other KAIROS-EVT document.

## 2. Terminology

**Domain segment.** The first content segment of a `type` value, identifying the KAIROS product or bounded context.

**Entity segment.** The second content segment, the noun the event concerns.

**Action segment.** The third content segment, the past-tense verb describing what happened.

**Version segment.** The fourth content segment, governed jointly with KAIROS-EVT-06's increment rule.

**`EVT02-2.1` (MUST) Single meaning per term.** As KAIROS-EVT-01 `EVT01-2.1`, substituting the terms of this section.

## 3. Data model

### 3.1 `type` structure

**`EVT02-3.1` (MUST) `type` structure.** Every `type` value produced by a KAIROS system must match the pattern `com.kairos.<domain>.<entity>.<action>.<version>`, with each segment separated by a single period and no other periods present.

**`EVT02-3.2` (MUST) Domain segment registration.** The `<domain>` segment must be a lower-case string with no separators, and must match an entry in the KAIROS-EVT-09 catalog's registered domain list.

**`EVT02-3.3` (MUST) Entity segment singularity.** The `<entity>` segment must be grammatically singular.

**`EVT02-3.4` (MUST) Action segment tense.** The `<action>` segment must be past tense and must not be a present-tense or imperative verb form.

**`EVT02-3.5` (MUST) Version segment format.** The `<version>` segment must be the letter `v` followed by a positive integer with no leading zero, and must increment only under the rule specified in KAIROS-EVT-06 Section 4.1.

### 3.2 `source` structure

**`EVT02-3.6` (MUST) `source` structure.** Every `source` value produced by a KAIROS system must be an absolute URI of the form `https://kairos.internal/<domain>/<service-name>`, where `<domain>` matches the domain segment used in that service's `type` values and `<service-name>` matches a service name registered in the KAIROS-EVT-09 catalog.

### 3.3 Prohibited content

**`EVT02-3.7` (MUST NOT) Environment identifiers prohibited.** A `type` value must not contain an environment identifier, including but not limited to `dev`, `test`, `staging`, or `prod`.

**`EVT02-3.8` (MUST NOT) Subject identifying information prohibited.** A `type` or `source` value must not contain PHI, PII, or any value that identifies a specific data subject; see KAIROS-EVT-07 Section 4 for the governing rationale.

## 4. Interfaces

**`EVT02-4.1` (MUST) Validation availability.** An implementation producing KAIROS events must expose a means of validating a candidate `type` or `source` value against Section 3 prior to event construction.

## 5. State model

Not applicable. A `type` or `source` value, once assigned to a specific event instance, does not change state independent of KAIROS-EVT-01 Section 5.

## 6. Execution semantics

**`EVT02-6.1` (MUST) Validation timing.** Validation against this document's Section 3 must occur before, or as part of, the validation required by KAIROS-EVT-01 Section 6.1.

## 7. Outcome and failure taxonomy

**`EVT02-7.1` (MUST) Outcome vocabulary.** A validation procedure conformant with this document must report exactly one of: `CONFORMANT`, `MALFORMED_PATTERN`, `UNREGISTERED_DOMAIN`, `UNREGISTERED_SERVICE`, or `PROHIBITED_CONTENT`.

## 8. Observability and the audit record

As KAIROS-EVT-01 Section 8, substituting the outcome vocabulary of Section 7 above.

## 9. Extension model

**`EVT02-9.1` (MUST NOT) No taxonomy extension without registration.** An implementation must not introduce a fifth segment or an alternate segment structure to the `type` pattern of Section 3.1 without registering the change as a revision to this document, since consumers built against the four-segment pattern would otherwise silently mis-parse a fifth segment.

## 10. Standards and specifications

CloudEvents Specification, Version 1.0.2, Cloud Native Computing Foundation, `type` and `source` attribute guidance (structural constraints only; the taxonomy itself is KAIROS-original).

KAIROS-EVT-01 (Envelope Standard), for the base attribute definitions this document constrains further.

## 11. Anti patterns

**Encoding environment in the event type.** Environment is a deployment concern. An event type that differs between dev and production breaks the assumption that the same consumer code can be tested against non-production events and trusted in production.

**Treating the version segment as a content version rather than a schema version.** The `<version>` segment increments on backwards-incompatible `data` changes (KAIROS-EVT-06), not on every release of the producing service; conflating the two produces version churn disconnected from what a consumer actually needs to know.

## 12. Boundaries with other Parts

**KAIROS-EVT-01 (Envelope).** This document assumes `type` is a String and `source` is a URI-reference, as defined there, and does not restate that type system.

**KAIROS-EVT-06 (Schema & Versioning).** This document defines the version segment's format; KAIROS-EVT-06 defines when it must change.

**KAIROS-EVT-07 (Security & Compliance).** This document prohibits subject-identifying content in `type` and `source`; KAIROS-EVT-07 defines the full set of content restrictions on the event as a whole.

**KAIROS-EVT-09 (Catalog & Registry).** This document requires that domain and service-name segments match registered values; KAIROS-EVT-09 owns the registry itself.

## 13. What could not be established

### 13.1 Whether four segments are sufficient long-term

The pattern in Section 3.1 assumes domain, entity, action, and version fully disambiguate an event type. It is not established whether a KAIROS domain will eventually need sub-domains (for example, distinguishing SPARK's claims processing from SPARK's eligibility checking) in a way this four-segment pattern cannot express without either overloading the entity segment or requiring a breaking change to this document.

**Open.** Whether to reserve a structural extension point now, at the cost of complexity for domains that never need it, or to accept a future breaking revision if and when a domain outgrows four segments.

### 13.2 Practice basis

The four-segment structure itself, the choice of reverse-DNS-style `com.kairos` prefix, past-tense actions, and integer versioning, is KAIROS-original design, informed by the upstream specification's non-binding guidance (`type` SHOULD be prefixed with a reverse-DNS name; example `type` values shown upstream use a similar shape) but not required by it.

**`EVT02-13.1` (MUST) Practice basis recorded.** An implementation must record that the specific taxonomy of Section 3 is a KAIROS design choice, not a CloudEvents requirement, wherever this document is cited as authority for that taxonomy.

### 13.3 What this document deliberately did not attempt

No treatment of whether existing, pre-KAIROS-EVT event types must be migrated to this taxonomy, or may be grandfathered.

No performance or throughput requirement is stated for taxonomy validation.

**`EVT02-13.2` (MUST) Gaps declared, not filled.** An implementation must not represent a matter listed in Section 13.3 as specified by this document.
