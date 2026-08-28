# KAIROS STD 003, KAIROS-BA-01: Business Analysis Core Concepts

**Standard.** KAIROS STD 003, the enterprise architecture standard.
**Part.** Pilot document, KAIROS-BA series. Not yet mapped to a numbered Part.
**Title.** Business analysis core concepts.
**Version.** 0.1.0, pilot.
**Status.** Pilot draft, for structural evaluation only.
**Date of issue.** Not issued. Drafted 2026-08-28.
**Supersedes.** None.

## Binding of requirement language

The key words MUST, MUST NOT, SHOULD, SHOULD NOT and MAY in this document are to be interpreted
as described in RFC 2119 and RFC 8174, and only in the upper case forms, matching the convention
established in KAIROS-EVT-01. Every requirement is a numbered clause with identifier `BA01-S.N`.
Clause identifiers are permanent; a retired clause's identifier is never reissued.

## Conformance

An implementation conforms to this document if it satisfies every MUST and MUST NOT clause and
records, for each SHOULD and SHOULD NOT clause it does not satisfy, the reason.

## Clause index

| Clause | Modality | Subject |
| --- | --- | --- |
| **Section 1** | | **Scope and responsibilities** |
| `BA01-1.1` | MUST | Purpose satisfaction |
| `BA01-1.2` | MUST NOT | No task-level process definition |
| **Section 3** | | **Data model** |
| `BA01-3.1` | MUST | Six-concept coverage |
| `BA01-3.2` | MUST NOT | No concept in isolation |
| `BA01-3.3` | MUST | Value classification |
| **Section 5** | | **State model** |
| `BA01-5.1` | MUST | Change-need reciprocity |
| **Section 7** | | **Outcome and failure taxonomy** |
| `BA01-7.1` | MUST | Concept-gap reporting |
| **Section 13** | | **What could not be established** |
| `BA01-13.1` | MUST | Practice basis recorded |
| `BA01-13.2` | MUST | Gaps declared, not filled |

## 1. Scope and responsibilities

### 1.1 What this component is

This document defines the six core concepts of business analysis, change, need, solution, value,
stakeholder, and context, and the requirement that any KAIROS business analysis activity account
for all six and their interrelationships. It is the KAIROS-BA series' equivalent of KAIROS-EVT-01's
envelope: the base vocabulary every other document in the series depends on.

### 1.2 What this component is NOT

This document does not define how any specific task (KAIROS-BA-02 through 07) is performed.

**`BA01-1.2` (MUST NOT) No task-level process definition.** This document must not be read as
specifying how a specific business analysis task is executed; task-level requirements are the
responsibility of KAIROS-BA-02 through KAIROS-BA-07.

**`BA01-1.1` (MUST) Purpose satisfaction.** An implementation must be able to identify, for any
business analysis activity, which of the six concepts defined in Section 3 it engages and whether
that engagement is complete per Section 3.1.

## 2. Terminology

Definitions follow the BABOK Glossary, IIBA, cited in full in Section 10. Only the six core concepts
are restated here.

**Change.** The act of transformation in response to a need.

**Need.** A problem or opportunity to be addressed.

**Solution.** A specific way of satisfying one or more needs in a context.

**Value.** The worth, importance, or usefulness of something to a stakeholder within a context.

**Stakeholder.** A group or individual with a relationship to the change, the need, or the solution.

**Context.** The circumstances that influence, are influenced by, and provide an understanding of
the change.

## 3. Data model

### 3.1 The six concepts

**`BA01-3.1` (MUST) Six-concept coverage.** A KAIROS business analysis activity must, at completion,
be able to state its position with respect to all six core concepts defined in Section 2, change,
need, solution, value, stakeholder, and context, even where a given concept's answer is "not yet
determined."

### 3.2 Interrelationship

**`BA01-3.2` (MUST NOT) No concept in isolation.** An implementation must not treat any one of the
six concepts as complete or actionable without considering its relationship to the other five; per
the source standard, viewing business analysis as a system of interrelated concepts, rather than six
independent checklist items, is what the model is for.

### 3.3 Value classification

**`BA01-3.3` (MUST) Value classification.** Where value is assessed for a stakeholder, the
assessment must classify that value as tangible or intangible, and where tangible, whether it is
realized through gains or preserved by mitigating losses, per the source standard's value taxonomy.

## 4. Interfaces

The six concepts are the interface every KAIROS-BA-02 through 07 task uses to describe its own
inputs and outputs; no additional interface mechanism is defined here.

## 5. State model

**`BA01-5.1` (MUST) Change-need reciprocity.** An implementation must account for the source
standard's stated reciprocal relationship between change and need: a need can motivate a change,
and a change, once made, can itself reduce or increase the value delivered by existing solutions,
generating new needs. Treating need as a static, one-time input to change is a nonconformity.

## 6. Execution semantics

The BACCM is explicitly a thinking and organizing model, not a sequential process; no task
ordering is imposed by this document. Task-level execution order is the responsibility of the
individual KAIROS-BA-02 through 07 documents.

## 7. Outcome and failure taxonomy

**`BA01-7.1` (MUST) Concept-gap reporting.** Where a business analysis activity cannot state its
position on one of the six concepts at completion, that gap must be explicitly reported rather than
silently omitted, since an omitted concept is indistinguishable from a concept that was considered
and found not applicable.

## 8. Observability and the audit record

A record of which of the six concepts were engaged, and how, should accompany the output of any
KAIROS-BA-02 through 07 task, so that later review can reconstruct whether the model was actually
applied or only referenced.

## 9. Extension model

Not applicable; the six concepts are fixed by the source standard and are not intended to be
extended per-organization.

## 10. Standards and specifications

The Business Analysis Standard, v2.0, 2025, IIBA, Section 2 (Understanding Business Analysis).
Primary source for this document, verified by direct reading.

BABOK Guide, v3, 2015, IIBA. Cited by the Standard as the source of the full BACCM treatment;
not independently verified for this document, see Section 13.2.

BABOK Glossary, IIBA. Terminology reference for Section 2.

## 11. Anti patterns

**Treating BACCM as a sequential checklist.** The source standard is explicit that "ignoring any
concept or their connections can reduce the model's effectiveness," yet the six-concept list format
invites exactly that: working through change, then need, then solution, in order, and considering
the task done. The interrelationship requirement in Section 3.2 exists specifically to name this
failure mode.

**Conflating value with cost savings alone.** The tangible/intangible split in Section 3.3 exists
because value is routinely reduced to its most measurable component (cost, revenue) while
intangible value, reputation, morale, is real per the source standard but gets dropped for lack of a
number to put on it.

## 12. Boundaries with other Parts

**KAIROS-BA-00 (Primer).** Non-normative; this document does not restate the Primer's rationale.

**KAIROS-BA-02 through KAIROS-BA-07.** Each of these documents applies the six concepts defined
here to its own knowledge area's tasks; none of them redefines the concepts themselves. A conflict
on what a concept means is resolved in favor of this document.

**KAIROS-BA-08 (Task Registry).** The registry records which concepts a given task most directly
engages, using the vocabulary this document defines, but does not itself interpret the model.

## 13. What could not be established

### 13.1 Whether the six concepts are jointly sufficient

The source standard asserts the six concepts "form a powerful model for effective business
analysis" but does not provide a formal argument that no seventh concept is needed, nor a test for
when the model's coverage is genuinely complete versus merely asserted.

**Open.** Whether KAIROS should adopt a more formal completeness check for Section 3.1, or accept
the source standard's own informal treatment as sufficient given business analysis is not being
formalized to the same rigor as a wire protocol.

### 13.2 Practice basis

This document was built entirely from The Business Analysis Standard, verified by direct reading.
The BABOK Guide itself, which the Standard describes as the fuller treatment of BACCM, was not
independently fetched or read for this document.

**`BA01-13.1` (MUST) Practice basis recorded.** An implementation must record that this document's
source is The Business Analysis Standard specifically, not the BABOK Guide, until the Guide is
independently verified.

### 13.3 What this document deliberately did not attempt

No treatment of how BACCM relates to the three horizons (strategy, initiative, delivery) mentioned
in the source standard's discussion of the Agile Extension to the BABOK Guide; that document was
not part of this drafting pass.

**`BA01-13.2` (MUST) Gaps declared, not filled.** An implementation must not represent a matter
listed in Section 13.3 as specified by this document.
