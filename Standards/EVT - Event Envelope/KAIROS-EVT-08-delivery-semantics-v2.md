# KAIROS STD 003, KAIROS-EVT-08: Event Delivery Semantics Standard

**Standard.** KAIROS STD 003, the enterprise architecture standard.
**Part.** Pilot document, KAIROS-EVT series. Not yet mapped to a numbered Part.
**Title.** Event delivery semantics standard.
**Version.** 0.2.0, pilot.
**Status.** Pilot draft, for structural evaluation only.
**Date of issue.** Not issued. Drafted 2026-08-28.
**Supersedes.** KAIROS-EVT-08 v0.1.

## Binding of requirement language

As KAIROS-EVT-01. Clause identifiers in this document have the form `EVT08-S.N`.

## Conformance

As KAIROS-EVT-01, substituting this document.

## Clause index

| Clause | Modality | Subject |
| --- | --- | --- |
| **Section 1** | | **Scope and responsibilities** |
| `EVT08-1.1` | MUST | Purpose satisfaction |
| **Section 3** | | **Data model** |
| `EVT08-3.1` | MUST | Idempotency key |
| **Section 4** | | **Interfaces** |
| `EVT08-4.1` | MUST | Idempotent consumer implementation |
| `EVT08-4.2` | MUST NOT | No ordering assumption |
| `EVT08-4.3` | MUST | Dead-letter destination configured |
| `EVT08-4.4` | MUST NOT | No atomic-batch assumption |
| **Section 7** | | **Outcome and failure taxonomy** |
| `EVT08-7.1` | MUST | Outcome vocabulary |
| **Section 13** | | **What could not be established** |
| `EVT08-13.1` | MUST | Practice basis recorded |
| `EVT08-13.2` | MUST | Gaps declared, not filled |

## 1. Scope and responsibilities

### 1.1 What this component is

The CloudEvents specification defines no delivery guarantees; this entire document exists to fill that silence for Azure Event Grid specifically. It defines what a KAIROS consumer may and may not assume about delivery order, uniqueness, and failure handling.

### 1.2 What this component is NOT

The component is not a transport binding; see KAIROS-EVT-04 for how an envelope is carried. This document assumes KAIROS-EVT-04's binding is in place and addresses only what happens after transmission.

**`EVT08-1.1` (MUST) Purpose satisfaction.** An implementation must be able to state, for any KAIROS consumer of an Event Grid subscription, whether that consumer is idempotent, order-independent, and dead-letter-configured per Section 3 and Section 4.

## 2. Terminology

**At-least-once delivery.** A guarantee that an event is delivered one or more times, never zero, with no upper bound on duplicate delivery.

**Dead-letter destination.** A storage location events are routed to after exhausting the retry policy, rather than being silently discarded.

## 3. Data model

**`EVT08-3.1` (MUST) Idempotency key.** Deduplication of a delivered event must be keyed on the pair (`source`, `id`) as defined in KAIROS-EVT-01 Section 3.2, which the upstream CloudEvents specification guarantees is unique per distinct event.

## 4. Interfaces

**`EVT08-4.1` (MUST) Idempotent consumer implementation.** Every KAIROS event consumer must be idempotent against duplicate delivery of the same (`source`, `id`) pair.

**`EVT08-4.2` (MUST NOT) No ordering assumption.** A consumer must not assume events arrive in `time` order, in send order, or in any other order. Where correctness depends on ordering, the consumer must implement its own sequencing logic using data in the payload or the Sequence extension (KAIROS-EVT-05 Section 4.3); Event Grid provides no ordering primitive to rely on instead.

**`EVT08-4.3` (MUST) Dead-letter destination configured.** Every Event Grid subscription carrying a business-critical event type must have a dead-letter destination configured.

**`EVT08-4.4` (MUST NOT) No atomic-batch assumption.** Where batched delivery (KAIROS-EVT-04 Section 4.1) is used, a consumer failure on one event within a batch must not be assumed to fail or retry the entire batch atomically unless the consumer explicitly implements and documents that behavior.

## 5. State model

A dead-letter destination accumulates state (failed deliveries) over time; this document does not specify a retention or replay policy for that state, see Section 13.1.

## 6. Execution semantics

On receipt, a consumer checks the (`source`, `id`) pair against previously processed events before acting; on a duplicate, it must return success without reprocessing, since Event Grid interprets any non-success response as a delivery failure subject to retry.

## 7. Outcome and failure taxonomy

**`EVT08-7.1` (MUST) Outcome vocabulary.** A consumer's per-event outcome must be exactly one of: `PROCESSED`, `DUPLICATE_SKIPPED`, `TRANSIENT_FAILURE` (eligible for retry), or `PERMANENT_FAILURE` (should be dead-lettered rather than retried indefinitely).

## 8. Observability and the audit record

An implementation must log every `DUPLICATE_SKIPPED` outcome distinctly from `PROCESSED`, so that duplicate delivery rates are visible and not conflated with successful throughput.

## 9. Extension model

The Sequence extension (KAIROS-EVT-05 Section 4.3), where adopted, supplies an ordering signal a consumer may use to satisfy Section 4.2's sequencing-logic requirement; its presence does not change Event Grid's own lack of an ordering guarantee.

## 10. Standards and specifications

Azure Event Grid documentation, Microsoft. Primary source for this document in full; the CloudEvents specification is silent on delivery semantics by design (Section 1.1).

KAIROS-EVT-01 (Envelope), for the `id`/`source` uniqueness basis of Section 3.1.

## 11. Anti patterns

**Assuming exactly-once delivery.** Event Grid delivers at-least-once; a consumer that is not idempotent will eventually process a duplicate as if it were new, which is precisely the failure Section 4.1 exists to prevent.

**Silently dropping permanently failing events.** An unconfigured dead-letter destination means a permanently failing delivery is lost with no record, which this document treats as a defect in subscription configuration, not an acceptable failure mode.

## 12. Boundaries with other Parts

**KAIROS-EVT-01 (Envelope).** This document's idempotency key (Section 3.1) depends on, but does not alter, the uniqueness guarantee KAIROS-EVT-01 Section 3.2 establishes.

**KAIROS-EVT-04 (Protocol Binding).** This document assumes the binding configuration KAIROS-EVT-04 defines is already in place; it addresses only post-transmission behavior.

**KAIROS-EVT-05 (Extensions).** The Sequence extension, where adopted under KAIROS-EVT-05, interacts with this document's Section 4.2 as described in Section 9, but does not override it.

**KAIROS-EVT-07 (Security & Compliance).** Dead-letter destinations created under Section 4.3 are subject to KAIROS-EVT-07 Section 3.3 and 3.5 for PHI-bearing event types.

## 13. What could not be established

### 13.1 Dead-letter retention and replay policy

Section 4.3 requires a dead-letter destination but does not specify how long dead-lettered events must be retained, or whether a mechanism for replaying them once the underlying failure is fixed is required.

**Open.** Whether retention and replay should be specified in this document or delegated to a general KAIROS data-retention policy outside the EVT series.

### 13.2 Practice basis

This entire document rests on Azure Event Grid's current documented behavior, which is a product commitment, not a specification guarantee in the sense KAIROS-EVT-01 through KAIROS-EVT-06 enjoy from the CloudEvents specification. Event Grid's delivery behavior could change with a future product revision in a way that would require this document to be revised in step.

**`EVT08-13.1` (MUST) Practice basis recorded.** An implementation must record that this document's requirements rest on current Azure Event Grid product documentation, not on the CloudEvents specification, and must be reviewed against Event Grid's documentation on any Azure platform version change.

### 13.3 What this document deliberately did not attempt

No treatment of AMQP-based or Kafka-based delivery semantics is given, since KAIROS's chosen transport is Event Grid over HTTP.

No performance or throughput requirement is stated for consumer idempotency checks.

**`EVT08-13.2` (MUST) Gaps declared, not filled.** An implementation must not represent a matter listed in Section 13.3 as specified by this document.
