# KAIROS STD 003, KAIROS-BA-02: Business Analysis Planning and Monitoring

**Standard.** KAIROS STD 003, the enterprise architecture standard.
**Part.** Pilot document, KAIROS-BA series. Not yet mapped to a numbered Part.
**Title.** Business analysis planning and monitoring.
**Version.** 0.1.0, pilot.
**Status.** Pilot draft, for structural evaluation only.
**Date of issue.** Not issued. Drafted 2026-08-28.
**Supersedes.** None.

## Binding of requirement language

As KAIROS-BA-01. Clause identifiers have the form `BA02-S.N`.

## Conformance

As KAIROS-BA-01, substituting this document.

## Clause index

| Clause | Modality | Subject |
| --- | --- | --- |
| **Section 1** | | **Scope and responsibilities** |
| `BA02-1.1` | MUST | Purpose satisfaction |
| `BA02-1.2` | MUST NOT | No elicitation, life cycle, or evaluation content |
| **Section 3** | | **Data model** |
| `BA02-3.1` | MUST | Plan BA Approach output |
| `BA02-3.2` | MUST | Plan Stakeholder Engagement output |
| `BA02-3.3` | MUST | Plan BA Governance output |
| `BA02-3.4` | MUST | Plan BA Information Management output |
| `BA02-3.5` | MUST | Identify BA Performance Improvements output |
| **Section 6** | | **Execution semantics** |
| `BA02-6.1` | SHOULD | Approach-before-engagement ordering |
| `BA02-6.2` | MUST | Governance decision-maker identification |
| **Section 9** | | **Extension model** |
| `BA02-9.1` | SHOULD | Technique selection by context |
| **Section 13** | | **What could not be established** |
| `BA02-13.1` | MUST | Practice basis recorded |
| `BA02-13.2` | MUST | Gaps declared, not filled |

## 1. Scope and responsibilities

### 1.1 What this component is

This document governs the five tasks IIBA groups as Business Analysis Planning and Monitoring:
Plan Business Analysis Approach, Plan Stakeholder Engagement, Plan Business Analysis Governance,
Plan Business Analysis Information Management, and Identify Business Analysis Performance
Improvements. These are the tasks that establish how business analysis work on an initiative will
itself be conducted, before any elicitation, requirements, or evaluation work begins.

### 1.2 What this component is NOT

**`BA02-1.2` (MUST NOT) No elicitation, life cycle, or evaluation content.** This document must not
define how information is actually elicited (KAIROS-BA-03), how requirements and designs are
traced or approved (KAIROS-BA-04), or how a solution is evaluated (KAIROS-BA-07); it defines only
how the approach to that work is planned.

**`BA02-1.1` (MUST) Purpose satisfaction.** An implementation must be able to produce, for any
KAIROS initiative, a defined business analysis approach, stakeholder engagement approach,
governance approach, and information management approach before elicitation work under
KAIROS-BA-03 begins.

## 2. Terminology

Extends KAIROS-BA-01 Section 2 and the BABOK Glossary. No new terms.

## 3. Data model

Each task below has a defined output, per the source standard's task card structure.

**`BA02-3.1` (MUST) Plan BA Approach output.** The Plan Business Analysis Approach task must
produce a defined business analysis approach including planned activities, tasks, and deliverables.

**`BA02-3.2` (MUST) Plan Stakeholder Engagement output.** The Plan Stakeholder Engagement task
must produce a defined stakeholder engagement approach including the stakeholder list, roles and
responsibilities, main characteristics, and a collaboration and communication approach.

**`BA02-3.3` (MUST) Plan BA Governance output.** The Plan Business Analysis Governance task must
produce a defined governance approach including the list of decision-makers and a description of
the change control, prioritization, and approvals process.

**`BA02-3.4` (MUST) Plan BA Information Management output.** The Plan Business Analysis
Information Management task must produce a defined information management approach
describing how business analysis information will be stored, accessed, and actioned during and
after change completion.

**`BA02-3.5` (MUST) Identify BA Performance Improvements output.** The Identify Business Analysis
Performance Improvements task must produce a business analysis performance assessment
including assessment results, identified root causes of variance from expected performance, and
proposed approaches to improve performance.

## 4. Interfaces

The business analysis approach (3.1) is a required input to all four other tasks in this document,
per the source standard's task input/output diagrams. The stakeholder engagement approach (3.2)
and governance approach (3.3) are both required inputs to the information management approach
task (3.4). All four planning outputs feed forward as inputs into KAIROS-BA-03 through 07 tasks.

## 5. State model

These five outputs are living documents, not one-time artifacts; the source standard's adaptive
approach guidance states that planning is repeated per iteration in adaptive and hybrid delivery,
not performed once and frozen. A KAIROS implementation must treat all five outputs of this
document as subject to revision across the life of an initiative, not as fixed at initiation.

## 6. Execution semantics

**`BA02-6.1` (SHOULD) Approach-before-engagement ordering.** The Plan Business Analysis Approach
task should be performed before Plan Stakeholder Engagement, since the source standard lists
approach as a documented input to the stakeholder engagement task, though IIBA does not treat
task ordering as strictly linear and this is a SHOULD, not a MUST, to preserve that flexibility.

**`BA02-6.2` (MUST) Governance decision-maker identification.** The Plan Business Analysis
Governance task must explicitly name the decision-makers for requirements and design approval
before any KAIROS-BA-04 approval task is performed against that initiative; an initiative with
requirements pending approval and no named decision-maker is a nonconformity under this
document, not merely a gap under KAIROS-BA-04.

## 7. Outcome and failure taxonomy

Each of the five tasks either produces its defined output (Section 3) in full or is incomplete;
IIBA's source material does not describe a partial-success state for these planning tasks, and this
document does not invent one.

## 8. Observability and the audit record

The business analysis performance assessment (3.5) is itself an audit artifact and must be retained
across the initiative, not only produced once and discarded, since it is the source standard's
mechanism for continuous improvement of the business analysis work itself.

## 9. Extension model

**`BA02-9.1` (SHOULD) Technique selection by context.** An implementation should select from the
source standard's frequently used techniques for each task (business cases, financial analysis,
functional decomposition, and others per task) based on initiative context, and may substitute an
organization-specific technique not listed in the source standard, provided the technique produces
an equivalent output per Section 3.

## 10. Standards and specifications

The Business Analysis Standard, v2.0, 2025, IIBA, Section 5 (Applying Business Analysis Tasks) and
the Business Analysis Planning and Monitoring task cards. Primary source for this document,
verified by direct reading.

BABOK Guide, v3, 2015, IIBA. Referenced by the source standard for the complete technique list per
task; not independently verified for this document.

## 11. Anti patterns

**Planning once at initiation and never revisiting.** Section 5's living-document requirement exists
because predictive-style planning habits carry over into adaptive and hybrid initiatives where the
source standard explicitly calls for repeated, iteration-level planning instead.

**Approving requirements with no named decision-maker.** `BA02-6.2` exists because this failure is
common and easy to miss: governance planning is treated as a formality rather than a prerequisite,
and approval activity under KAIROS-BA-04 proceeds without anyone having the actual authority to
approve.

## 12. Boundaries with other Parts

**KAIROS-BA-01 (Core Concepts).** This document's five tasks each engage the BACCM's six concepts
per KAIROS-BA-01 Section 3.1; this document does not restate that requirement per task.

**KAIROS-BA-03 (Elicitation and Collaboration).** The stakeholder engagement approach (3.2)
produced here is a required input to every task in KAIROS-BA-03; a conflict on stakeholder scope is
resolved in favor of this document, since planning precedes elicitation.

**KAIROS-BA-04 (Requirements and Designs Life Cycle Management).** The governance approach
(3.3) produced here governs the approval task in KAIROS-BA-04; this document does not itself
define the approval task.

**KAIROS-BA-08 (Task Registry).** All five tasks in this document are registered entries in
KAIROS-BA-08, cross-referenced against the tasks in the other five knowledge area documents for
shared inputs and outputs.

## 13. What could not be established

### 13.1 Threshold for performance improvement action

The Identify Business Analysis Performance Improvements task (3.5) produces "identified root
causes of variances from expected performance," but the source standard does not define what
variance threshold triggers a required response versus an observation logged without action.

**Open.** Whether KAIROS should define a variance threshold, or leave this to organizational
judgment given performance expectations vary too widely across initiative types for one KAIROS
wide number to be meaningful.

### 13.2 Practice basis

The four planning outputs of Sections 3.1 through 3.4 as separate, distinct documents, rather than
one combined planning artifact, follows the source standard's task structure directly. Whether
KAIROS organizations should combine them into fewer physical documents while keeping the
content distinct is not addressed by the source standard and is a KAIROS implementation choice.

**`BA02-13.1` (MUST) Practice basis recorded.** An implementation combining the four planning
outputs into fewer physical documents must record that the four-way content separation, not the
document count, is what this standard actually requires.

### 13.3 What this document deliberately did not attempt

No treatment of the specific techniques listed per task (business cases, financial analysis, and the
rest) beyond naming that they exist; the full technique catalog is BABOK Guide content not
independently verified for this pass.

**`BA02-13.2` (MUST) Gaps declared, not filled.** An implementation must not represent a matter
listed in Section 13.3 as specified by this document.
