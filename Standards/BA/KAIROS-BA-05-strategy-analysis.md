# KAIROS STD 003, KAIROS-BA-05: Strategy Analysis

**Standard.** KAIROS STD 003, the enterprise architecture standard.
**Part.** Pilot document, KAIROS-BA series. Not yet mapped to a numbered Part.
**Title.** Strategy analysis.
**Version.** 0.1.0, pilot.
**Status.** Pilot draft, for structural evaluation only.
**Date of issue.** Not issued. Drafted 2026-08-28.
**Supersedes.** None.

## Binding of requirement language

As KAIROS-BA-01. Clause identifiers have the form `BA05-S.N`.

## Conformance

As KAIROS-BA-01, substituting this document.

## Clause index

| Clause | Modality | Subject |
| --- | --- | --- |
| **Section 1** | | **Scope and responsibilities** |
| `BA05-1.1` | MUST | Purpose satisfaction |
| `BA05-1.2` | MUST NOT | No solution-level design content |
| **Section 3** | | **Data model** |
| `BA05-3.1` | MUST | Analyze Current State output |
| `BA05-3.2` | MUST | Define Future State output |
| `BA05-3.3` | MUST | Assess Risks output |
| `BA05-3.4` | MUST | Define Change Strategy output |
| **Section 6** | | **Execution semantics** |
| `BA05-6.1` | MUST | Current state before future state |
| `BA05-6.2` | MUST | Risk assessment before strategy selection |
| **Section 13** | | **What could not be established** |
| `BA05-13.1` | MUST | Practice basis recorded |
| `BA05-13.2` | MUST | Gaps declared, not filled |

## 1. Scope and responsibilities

### 1.1 What this component is

This document governs the four tasks IIBA groups as Strategy Analysis: Analyze Current State,
Define Future State, Assess Risks, and Define Change Strategy. These tasks establish why an
enterprise needs to change, what it is changing toward, and how, before requirements are specified
in detail.

### 1.2 What this component is NOT

**`BA05-1.2` (MUST NOT) No solution-level design content.** This document must not define specific
design options or solution components; that is KAIROS-BA-06's responsibility. This document
establishes the change strategy and solution scope that KAIROS-BA-06's design work operates
within.

**`BA05-1.1` (MUST) Purpose satisfaction.** An implementation must be able to produce a current
state description, future state description, risk analysis, and change strategy for any KAIROS
initiative before detailed requirements specification under KAIROS-BA-06 begins.

## 2. Terminology

Extends KAIROS-BA-01 Section 2 and the BABOK Glossary. No new terms.

## 3. Data model

**`BA05-3.1` (MUST) Analyze Current State output.** The Analyze Current State task must produce a
clearly defined business need and a gained understanding of the enterprise's current state.

**`BA05-3.2` (MUST) Define Future State output.** The Define Future State task must produce a
future state description, business objectives, and the potential value expected.

**`BA05-3.3` (MUST) Assess Risks output.** The Assess Risks task must produce risk analysis results
documenting understood risks and the recommended strategy to address them.

**`BA05-3.4` (MUST) Define Change Strategy output.** The Define Change Strategy task must produce
a defined change strategy and a defined solution scope.

## 4. Interfaces

The current state description (3.1) is a required input to Define Future State (3.2). Both current
and future state descriptions are required inputs to Assess Risks (3.3) and, together with risk
analysis results, to Define Change Strategy (3.4). The solution scope produced by 3.4 is a required
input to KAIROS-BA-04's prioritization and approval tasks and to KAIROS-BA-06's design option task.

## 5. State model

Not applicable; the four outputs of this document are analysis artifacts, not stateful records with
their own life cycle beyond the maintenance and versioning already governed by KAIROS-BA-04.

## 6. Execution semantics

**`BA05-6.1` (MUST) Current state before future state.** The Analyze Current State task must be
performed, and its output (3.1) available, before the Define Future State task begins; the source
standard lists current state understanding as the basis from which future state is defined, not a
parallel or independent activity.

**`BA05-6.2` (MUST) Risk assessment before strategy selection.** Risk analysis results (3.3) must be
available before the Define Change Strategy task selects a recommended approach (3.4); the source
standard describes change strategy selection as an assessment of options including their risk, which
requires risk analysis to already exist.

## 7. Outcome and failure taxonomy

These four tasks are analytical rather than pass/fail; the source standard describes their outputs
as understanding gained and options assessed, not conformant/nonconformant states. This
document does not impose a binary outcome taxonomy on tasks the source material treats as
inherently a matter of analytical judgment.

## 8. Observability and the audit record

The change strategy (3.4) and its supporting risk analysis (3.3) should be retained as the documented
basis for the solution scope, since disputes over why a particular change approach was chosen, small
evolutionary change versus large transformation, are best resolved by reference to the original risk
and current/future state analysis rather than reconstructed after the fact.

## 9. Extension model

An implementation may select from the source standard's frequently used techniques per task
(benchmarking, SWOT analysis, business capability analysis, brainstorming, financial analysis, root
cause analysis, business model canvas, and others) based on context, or substitute an
organization-specific technique that produces an equivalent output per Section 3.

## 10. Standards and specifications

The Business Analysis Standard, v2.0, 2025, IIBA, the Strategy Analysis task cards. Primary source
for this document, verified by direct reading.

BABOK Guide, v3, 2015, IIBA. Referenced for the complete technique list per task; not independently
verified for this document.

## 11. Anti patterns

**Defining future state without a documented current state.** `BA05-6.1` exists because it is
common to jump directly to describing a desired future state, particularly when the future state
feels obvious to those proposing it, skipping the current state analysis that would reveal whether
the proposed future actually addresses the real gap.

**Selecting a change strategy before risks are understood.** `BA05-6.2` exists because change
strategy selection is often driven by preference, aggressive transformation versus cautious
evolution, formed before risk analysis exists to inform that choice, then the risk analysis is
performed afterward to justify a decision already made.

## 12. Boundaries with other Parts

**KAIROS-BA-01 (Core Concepts).** Current state, future state, and change strategy are direct
applications of the change and need concepts defined in KAIROS-BA-01; this document does not
redefine those concepts.

**KAIROS-BA-04 (Requirements and Designs Life Cycle Management).** The solution scope produced
here (3.4) bounds what KAIROS-BA-04's prioritization and approval tasks may act on; a requirement
outside the defined solution scope is a KAIROS-BA-04 nonconformity, not a defect in this document.

**KAIROS-BA-06 (Requirements Analysis and Design Definition).** This document's change strategy
and solution scope are required inputs to KAIROS-BA-06's design option task; this document does
not itself define design options.

**KAIROS-BA-08 (Task Registry).** All four tasks in this document are registered entries,
cross-referenced for their role as upstream inputs to KAIROS-BA-04 and KAIROS-BA-06.

## 13. What could not be established

### 13.1 Revisiting strategy mid-initiative

The source standard does not specify what triggers a return to Strategy Analysis once an initiative
has moved into requirements work under KAIROS-BA-06; in practice, discoveries made during
detailed requirements work sometimes invalidate the original current or future state analysis.

**Open.** Whether KAIROS should define explicit re-entry criteria into this document's tasks from
KAIROS-BA-06, or leave this to the change assessment task in KAIROS-BA-04 Section 3.4 to catch as
a downstream signal instead.

### 13.2 Practice basis

The ordering requirements in `BA05-6.1` and `BA05-6.2` are KAIROS-original sequencing rules; the
source standard describes all four tasks and their typical relationships but does not state them as
strict prerequisites in RFC 2119 terms.

**`BA05-13.1` (MUST) Practice basis recorded.** An implementation must record that the sequencing
in Section 6 is a KAIROS-original formalization of the source standard's descriptive task
relationships, not a restatement of an explicit IIBA ordering requirement.

### 13.3 What this document deliberately did not attempt

No treatment of the specific strategy analysis techniques (SWOT, business capability analysis, and
the rest) beyond naming that they exist; per-technique guidance is BABOK Guide content not
independently verified for this pass.

**`BA05-13.2` (MUST) Gaps declared, not filled.** An implementation must not represent a matter
listed in Section 13.3 as specified by this document.
