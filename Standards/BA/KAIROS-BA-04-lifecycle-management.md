# KAIROS STD 003, KAIROS-BA-04: Requirements and Designs Life Cycle Management

**Standard.** KAIROS STD 003, the enterprise architecture standard.
**Part.** Pilot document, KAIROS-BA series. Not yet mapped to a numbered Part.
**Title.** Requirements and designs life cycle management.
**Version.** 0.1.0, pilot.
**Status.** Pilot draft, for structural evaluation only.
**Date of issue.** Not issued. Drafted 2026-08-28.
**Supersedes.** None.

## Binding of requirement language

As KAIROS-BA-01. Clause identifiers have the form `BA04-S.N`.

## Conformance

As KAIROS-BA-01, substituting this document.

## Clause index

| Clause | Modality | Subject |
| --- | --- | --- |
| **Section 1** | | **Scope and responsibilities** |
| `BA04-1.1` | MUST | Purpose satisfaction |
| `BA04-1.2` | MUST NOT | No specification or modelling content |
| **Section 3** | | **Data model** |
| `BA04-3.1` | MUST | Trace output |
| `BA04-3.2` | MUST | Maintain output |
| `BA04-3.3` | MUST | Prioritize output |
| `BA04-3.4` | MUST | Assess Change output |
| `BA04-3.5` | MUST | Approve output |
| **Section 5** | | **State model** |
| `BA04-5.1` | MUST | Requirement lineage |
| `BA04-5.2` | MUST NOT | No approval without governance decision-maker |
| **Section 6** | | **Execution semantics** |
| `BA04-6.1` | MUST | Change assessment before re-prioritization |
| **Section 13** | | **What could not be established** |
| `BA04-13.1` | MUST | Practice basis recorded |
| `BA04-13.2` | MUST | Gaps declared, not filled |

## 1. Scope and responsibilities

### 1.1 What this component is

This document governs the five tasks IIBA groups as Requirements and Designs Life Cycle
Management: Trace Requirements and Designs, Maintain Requirements and Designs, Prioritize
Requirements and Designs, Assess Requirement and Design Changes, and Approve Requirements and
Designs. These tasks manage requirements and designs after they exist, across the life of an
initiative and, per the source standard, potentially beyond it for reuse.

### 1.2 What this component is NOT

**`BA04-1.2` (MUST NOT) No specification or modelling content.** This document must not define
how a requirement or design is first specified or modelled; that is KAIROS-BA-06's responsibility.
This document governs a requirement or design once it already exists in some form.

**`BA04-1.1` (MUST) Purpose satisfaction.** An implementation must be able to trace, maintain,
prioritize, assess changes to, and obtain approval for any requirement or design across its life
cycle, including after the initiative that created it has closed.

## 2. Terminology

Extends KAIROS-BA-01 Section 2 and the BABOK Glossary. No new terms.

## 3. Data model

**`BA04-3.1` (MUST) Trace output.** The Trace Requirements and Designs task must produce
requirements and designs with recorded backward traceability to the originating business need,
forward traceability to solution components, and relationships to other requirements and designs.

**`BA04-3.2` (MUST) Maintain output.** The Maintain Requirements and Designs task must produce
requirements and designs that are accurate and current throughout the life cycle, supporting reuse
in other solutions where appropriate.

**`BA04-3.3` (MUST) Prioritize output.** The Prioritize Requirements and Designs task must produce
high-valued requirements and designs maintained and available for use, ranked by relative
importance.

**`BA04-3.4` (MUST) Assess Change output.** The Assess Requirement and Design Changes task must
produce a change assessment with a recommendation on how to act on a proposed change.

**`BA04-3.5` (MUST) Approve output.** The Approve Requirements and Designs task must produce
requirements and designs agreed upon by stakeholders and ready for use in subsequent business
analysis and solution development efforts.

## 4. Interfaces

Traced requirements (3.1) are a required input to prioritization (3.3) and change assessment (3.4).
Verified requirements, an output of KAIROS-BA-06, are a required input to approval (3.5). Approved
requirements and designs feed forward as inputs to KAIROS-BA-06's design option and solution
recommendation tasks and, ultimately, to KAIROS-BA-07's solution evaluation tasks.

## 5. State model

**`BA04-5.1` (MUST) Requirement lineage.** A requirement or design's lineage, its backward trace to
originating need and forward trace to solution components, must remain intact across every state
transition in this document; a maintained, prioritized, or approved requirement that has lost its
traceability record is a nonconformity even if its content is otherwise unchanged.

**`BA04-5.2` (MUST NOT) No approval without governance decision-maker.** An implementation must
not execute the Approve Requirements and Designs task for an initiative that has not completed
KAIROS-BA-02's governance planning task, since approval requires a named decision-maker per
KAIROS-BA-02 Section 6.2, and this document does not itself supply one.

## 6. Execution semantics

**`BA04-6.1` (MUST) Change assessment before re-prioritization.** A proposed change to a
requirement or design must be assessed under Section 3.4 before that requirement or design is
re-prioritized under Section 3.3 on the basis of the proposed change; prioritizing on an unassessed
change risks reordering work around a change that turns out not to be worth making.

## 7. Outcome and failure taxonomy

Approval (3.5) is binary per the source standard, approved or not; the source standard notes
approval rigor itself varies, "a lightweight step for adaptive initiatives or a rigorous process for
complex, predictive initiatives," but does not describe a partial-approval state, and this document
does not invent one.

## 8. Observability and the audit record

The traceability record required by Section 3.1 and preserved by Section 5.1 is itself the primary
audit mechanism for this document; a separate audit log is not required where traceability is
maintained per specification.

## 9. Extension model

An implementation may select from the source standard's frequently used techniques per task
(business rules analysis, data modelling, backlog management, decision analysis, acceptance and
evaluation criteria, and others) based on context, or substitute an organization-specific technique
that produces an equivalent output per Section 3.

## 10. Standards and specifications

The Business Analysis Standard, v2.0, 2025, IIBA, the Requirements and Designs Life Cycle
Management task cards. Primary source for this document, verified by direct reading.

BABOK Guide, v3, 2015, IIBA. Referenced for the complete technique list per task; not independently
verified for this document.

## 11. Anti patterns

**Losing traceability during maintenance.** `BA04-5.1` exists because maintenance activity,
updating a requirement to stay current, is exactly when traceability links are most often silently
dropped, since the update focuses on content and the lineage record is easy to overlook.

**Treating approval as a rubber stamp when governance was never planned.** `BA04-5.2` exists
because skipping KAIROS-BA-02's governance task does not prevent an organization from going
through the motions of "approval," it just means the approval has no real decision-maker behind
it, which surfaces later as a dispute over who actually authorized the work.

## 12. Boundaries with other Parts

**KAIROS-BA-02 (Planning and Monitoring).** The governance approach from KAIROS-BA-02 Section
3.3 supplies the decision-makers this document's approval task requires; this document does not
itself define governance.

**KAIROS-BA-06 (Requirements Analysis and Design Definition).** Verified requirements from
KAIROS-BA-06 are a required input to this document's approval task; this document does not
redefine what "verified" means.

**KAIROS-BA-08 (Task Registry).** All five tasks in this document are registered entries,
cross-referenced for their traceability relationships to tasks in KAIROS-BA-03 and KAIROS-BA-06.

## 13. What could not be established

### 13.1 Post-initiative maintenance ownership

The source standard states requirements and designs are maintained "throughout and beyond the
change initiative," but does not specify who owns that maintenance once the initiative team
disbands.

**Open.** Whether KAIROS should assign post-initiative maintenance ownership to the KAIROS-BA-08
catalog's registered owning entity for the affected domain, or treat this as an organizational
question outside the scope of a business analysis standard.

### 13.2 Practice basis

The ordering requirement in `BA04-6.1`, that change assessment must precede re-prioritization, is a
KAIROS-original sequencing rule; the source standard describes both tasks but does not state which
must occur first relative to the other.

**`BA04-13.1` (MUST) Practice basis recorded.** An implementation must record that `BA04-6.1` is a
KAIROS-original sequencing decision, not a restatement of an explicit IIBA ordering requirement.

### 13.3 What this document deliberately did not attempt

No treatment of the specific traceability modelling structures (matrices, diagrams) the source
standard mentions; the modelling technique itself is BABOK Guide content not independently
verified for this pass.

**`BA04-13.2` (MUST) Gaps declared, not filled.** An implementation must not represent a matter
listed in Section 13.3 as specified by this document.
