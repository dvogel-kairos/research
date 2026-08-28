# KAIROS STD 003, KAIROS-BA-08: Business Analysis Task Registry

**Standard.** KAIROS STD 003, the enterprise architecture standard.
**Part.** Pilot document, KAIROS-BA series. Not yet mapped to a numbered Part.
**Title.** Business analysis task registry.
**Version.** 0.1.0, pilot.
**Status.** Pilot draft, for structural evaluation only.
**Date of issue.** Not issued. Drafted 2026-08-28.
**Supersedes.** None.

## Binding of requirement language

As KAIROS-BA-01. Clause identifiers have the form `BA08-S.N`.

## Conformance

As KAIROS-BA-01, substituting this document.

## Clause index

| Clause | Modality | Subject |
| --- | --- | --- |
| **Section 1** | | **Scope and responsibilities** |
| `BA08-1.1` | MUST | Purpose satisfaction |
| `BA08-1.2` | MUST NOT | No task-content redefinition |
| **Section 3** | | **Data model** |
| `BA08-3.1` | MUST | Mandatory registry fields |
| `BA08-3.2` | MUST | Complete 30-task coverage |
| **Section 4** | | **Interfaces** |
| `BA08-4.1` | MUST | Cross-knowledge-area dependency recording |
| **Section 13** | | **What could not be established** |
| `BA08-13.1` | MUST | Practice basis recorded |
| `BA08-13.2` | MUST | Gaps declared, not filled |

## 1. Scope and responsibilities

### 1.1 What this component is

This document is the single, authoritative record of all 30 business analysis tasks across the six
knowledge areas governed by KAIROS-BA-02 through KAIROS-BA-07, tracking which task produces
which output, which task consumes it, and where that dependency crosses a knowledge area
boundary. It plays the same role for the KAIROS-BA series that KAIROS-EVT-09 plays for the
KAIROS-EVT series.

### 1.2 What this component is NOT

**`BA08-1.2` (MUST NOT) No task-content redefinition.** This document must not restate or alter
what any individual task requires; that is the responsibility of the KAIROS-BA-02 through
KAIROS-BA-07 document that owns it. This document records the map, not the content.

**`BA08-1.1` (MUST) Purpose satisfaction.** An implementation must be able to determine, for any of
the 30 business analysis tasks, which knowledge area document governs it, what it consumes, what
it produces, and which other tasks depend on that output.

## 2. Terminology

Extends KAIROS-BA-01 Section 2 and the BABOK Glossary.

**Registry entry.** The recorded mapping for one of the 30 tasks: its owning knowledge area
document, its required inputs, its produced outputs, and its downstream consumers.

## 3. Data model

**`BA08-3.1` (MUST) Mandatory registry fields.** Every registry entry must record, at minimum: the
task name; the owning KAIROS-BA document (02 through 07); the task's required inputs and their
source tasks; the task's produced outputs; and every other task, in any knowledge area, that
consumes that output.

**`BA08-3.2` (MUST) Complete 30-task coverage.** The registry must contain exactly 30 entries,
matching the task count in KAIROS-BA-00 Section 4's table, no more and no fewer; a task appearing
in a KAIROS-BA-02 through 07 document without a corresponding registry entry is a nonconformity
under this document.

## 4. Interfaces

**`BA08-4.1` (MUST) Cross-knowledge-area dependency recording.** Where a task's output is
consumed by a task in a different knowledge area document, for example KAIROS-BA-03's confirmed
elicitation results feeding KAIROS-BA-06's specification task, that dependency must be recorded in
both tasks' registry entries, not only in the consuming task's entry.

## 5. State model

A registry entry's status (registered, in use, superseded) tracks the same life cycle as any
KAIROS-EVT-09 catalog entry; a task that is renamed or restructured across a revision of its
governing document requires the registry entry to be updated in the same revision, not
independently.

## 6. Execution semantics

The registry is queried, not executed; it has no task ordering of its own beyond what is already
specified in each governing document's Section 6.

## 7. Outcome and failure taxonomy

A registry entry is either complete per Section 3.1 or incomplete; there is no partial-completeness
state.

## 8. Observability and the audit record

The registry itself is the audit record of task interdependency across the KAIROS-BA series; no
separate audit mechanism is defined here.

## 9. Extension model

An organization may add a KAIROS-original task to the registry, provided it is also documented in
an appropriately extended or new knowledge area document; this document does not itself gate
what tasks may be added, only that any addition be registered.

## 10. Standards and specifications

KAIROS-BA-00 through KAIROS-BA-07, this series, for the task definitions this registry indexes.

The Business Analysis Standard, v2.0, 2025, IIBA, Section 5.3 (Business Analysis Knowledge Areas),
for the six-knowledge-area, 30-task structure this registry's completeness check (3.2) is measured
against.

## 11. Anti patterns

**Letting the registry drift from the governing documents.** A registry maintained separately from
the documents it indexes will silently go stale the first time a task's inputs or outputs change in its
governing document without a corresponding registry update; `BA08-3.2`'s exact-count requirement
exists partly to make drift detectable rather than only theoretically undesirable.

**Recording a dependency only on the consuming side.** `BA08-4.1` exists because it is natural to
update the registry entry for the task you are currently working on and forget the entry for the task
whose output it consumes, producing a registry where dependencies are traceable in one direction
but not the other.

## 12. Boundaries with other Parts

**KAIROS-BA-00 (Primer).** The Primer's task-count table (Section 4) is the non-normative
description this registry's `BA08-3.2` completeness check enforces normatively.

**KAIROS-BA-01 (Core Concepts).** The registry may record which of the six core concepts a task
most directly engages, using KAIROS-BA-01's vocabulary, but does not interpret the model itself.

**KAIROS-BA-02 through KAIROS-BA-07.** Each of these six documents owns the content of the tasks
this registry indexes; a conflict between the registry's recorded inputs/outputs and a governing
document's Section 3 is resolved in favor of the governing document, and the registry entry must be
corrected.

## 13. What could not be established

### 13.1 Registry technical implementation

As with KAIROS-EVT-09, this document does not specify the registry's storage mechanism, query
interface, or hosting platform.

**Open.** Whether the KAIROS-BA registry and the KAIROS-EVT registry should share a common
implementation given both follow the same pattern, or whether domain separation argues for
keeping them independent.

### 13.2 Practice basis

This document, like KAIROS-EVT-09 before it, is entirely KAIROS-original; no upstream IIBA source
describes a task registry or dependency-tracking concept. The shape adopted here follows the
KAIROS-EVT-09 precedent directly rather than any business-analysis-specific source.

**`BA08-13.1` (MUST) Practice basis recorded.** An implementation must record that this document
in its entirety rests on the KAIROS-EVT-09 precedent, not on any IIBA source, wherever it is invoked
as authority.

### 13.3 What this document deliberately did not attempt

No treatment of registry access control is given; this is assumed to follow general KAIROS identity
and access governance, not restated here, matching the same omission in KAIROS-EVT-09.

**`BA08-13.2` (MUST) Gaps declared, not filled.** An implementation must not represent a matter
listed in Section 13.3 as specified by this document.
