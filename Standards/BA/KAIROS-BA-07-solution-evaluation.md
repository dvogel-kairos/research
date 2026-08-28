# KAIROS STD 003, KAIROS-BA-07: Solution Evaluation

**Standard.** KAIROS STD 003, the enterprise architecture standard.
**Part.** Pilot document, KAIROS-BA series. Not yet mapped to a numbered Part.
**Title.** Solution evaluation.
**Version.** 0.1.0, pilot.
**Status.** Pilot draft, for structural evaluation only.
**Date of issue.** Not issued. Drafted 2026-08-28.
**Supersedes.** None.

## Binding of requirement language

As KAIROS-BA-01. Clause identifiers have the form `BA07-S.N`.

## Conformance

As KAIROS-BA-01, substituting this document.

## Clause index

| Clause | Modality | Subject |
| --- | --- | --- |
| **Section 1** | | **Scope and responsibilities** |
| `BA07-1.1` | MUST | Purpose satisfaction |
| `BA07-1.2` | MUST NOT | No pre-implementation design content |
| **Section 3** | | **Data model** |
| `BA07-3.1` | MUST | Measure Performance output |
| `BA07-3.2` | MUST | Analyze Performance output |
| `BA07-3.3` | MUST | Solution Limitations output |
| `BA07-3.4` | MUST | Enterprise Limitations output |
| `BA07-3.5` | MUST | Recommended Actions output |
| **Section 5** | | **State model** |
| `BA07-5.1` | MUST NOT | No limitation conflation |
| **Section 6** | | **Execution semantics** |
| `BA07-6.1` | MUST | Measurement before analysis |
| **Section 13** | | **What could not be established** |
| `BA07-13.1` | MUST | Practice basis recorded |
| `BA07-13.2` | MUST | Gaps declared, not filled |

## 1. Scope and responsibilities

### 1.1 What this component is

This document governs the five tasks IIBA groups as Solution Evaluation: Measure Solution
Performance, Analyze Performance Measures, Assess Solution Limitations, Assess Enterprise
Limitations, and Recommend Actions to Increase Solution Value. These tasks operate on an
implemented or constructed solution to determine whether it is delivering the value it was intended
to deliver.

### 1.2 What this component is NOT

**`BA07-1.2` (MUST NOT) No pre-implementation design content.** This document must not define
how a solution is designed or built; that is KAIROS-BA-06's responsibility. This document begins
once a solution exists, whether fully or partially implemented, and evaluates it.

**`BA07-1.1` (MUST) Purpose satisfaction.** An implementation must be able to measure and analyze
an implemented solution's performance, assess limitations both internal and external to the
solution, and produce recommended actions to close the gap between potential and actual value.

## 2. Terminology

Extends KAIROS-BA-01 Section 2 and the BABOK Glossary.

**Solution limitation.** A factor internal to the solution restricting the full realization of value.

**Enterprise limitation.** A factor external to the solution, but internal to the enterprise,
restricting value realization.

## 3. Data model

**`BA07-3.1` (MUST) Measure Performance output.** The Measure Solution Performance task must
produce solution performance measures against defined metrics such as stakeholder satisfaction,
process efficiency, and financial outcomes.

**`BA07-3.2` (MUST) Analyze Performance output.** The Analyze Performance Measures task must
produce a solution performance analysis, the results of the measurements collected and analyzed.

**`BA07-3.3` (MUST) Solution Limitations output.** The Assess Solution Limitations task must
produce a description of the current limitations of the solution, including constraints and defects.

**`BA07-3.4` (MUST) Enterprise Limitations output.** The Assess Enterprise Limitations task must
produce a description of the current limitations of the enterprise, including how solution
performance is impacting the enterprise.

**`BA07-3.5` (MUST) Recommended Actions output.** The Recommend Actions to Increase Solution
Value task must produce a compiled list of recommendations to maximize solution performance and
value realization, which may include removing, improving, replacing, or retiring solution elements,
or taking no action.

## 4. Interfaces

Performance measures (3.1) are a required input to the performance analysis task (3.2). The
performance analysis is a required input to both the solution limitations task (3.3) and, together
with the current state description from KAIROS-BA-05, the enterprise limitations task (3.4). Both
limitation assessments are required inputs to the recommended actions task (3.5). Recommended
actions that constitute a new need feed back as an input to KAIROS-BA-05's current state analysis
for a subsequent change cycle.

## 5. State model

**`BA07-5.1` (MUST NOT) No limitation conflation.** An implementation must not attribute a
limitation to the solution (3.3) when its actual source is external to the solution but internal to the
enterprise (3.4), or the reverse; the source standard's own example, an underutilized data
warehousing solution, illustrates that the same symptom, low value realization, can stem from
either category, and misattributing it produces a recommended action aimed at the wrong target.

## 6. Execution semantics

**`BA07-6.1` (MUST) Measurement before analysis.** Solution performance measures (3.1) must be
collected before the Analyze Performance Measures task (3.2) is performed against them; analysis
without underlying measurement data is not analysis under this document.

## 7. Outcome and failure taxonomy

The recommended actions output (3.5) is explicit that "taking no action" is itself a valid outcome per
the source standard; this document does not treat the absence of a corrective action as a failure of
the evaluation tasks, provided the evaluation itself, Sections 3.1 through 3.4, was actually performed.

## 8. Observability and the audit record

Performance measures (3.1) and their analysis (3.2) should be retained over time, not only at a
single evaluation point, since the source standard frames solution evaluation as an activity that
can recur across the solution's operational life, particularly for iterative improvement of an existing
process or product.

## 9. Extension model

An implementation may select from the source standard's frequently used techniques per task
(acceptance and evaluation criteria, benchmarking, metrics and KPIs, non-functional requirements
analysis, financial analysis, data mining, observation, root cause analysis, decision analysis,
process analysis, and others) based on context, or substitute an organization-specific technique
that produces an equivalent output per Section 3.

## 10. Standards and specifications

The Business Analysis Standard, v2.0, 2025, IIBA, the Solution Evaluation task cards. Primary
source for this document, verified by direct reading.

BABOK Guide, v3, 2015, IIBA. Referenced for the complete technique list per task; not independently
verified for this document.

## 11. Anti patterns

**Assuming underperformance is always a solution defect.** `BA07-5.1` exists because the reflex
when a solution underperforms is to look for a defect in the solution itself, when the source
standard's own example shows the cause is frequently external, unclear supporting processes,
stakeholders who do not understand the solution's capabilities, rather than anything wrong with
the solution as built.

**Treating evaluation as a one-time post-launch event.** Section 8's retention requirement exists
because solution evaluation is often performed once, shortly after launch, and never repeated, even
though the source standard frames ongoing measurement as the basis for continuous improvement
across the solution's operational life.

## 12. Boundaries with other Parts

**KAIROS-BA-05 (Strategy Analysis).** The current state description from KAIROS-BA-05 is a required
input to this document's enterprise limitations task; a recommended action that amounts to a new
need feeds back into KAIROS-BA-05's current state analysis for a subsequent cycle, closing the loop
described in KAIROS-BA-01's change-need reciprocity clause.

**KAIROS-BA-06 (Requirements Analysis and Design Definition).** This document evaluates the
solution KAIROS-BA-06 recommended and, ultimately, that was implemented from KAIROS-BA-06's
approved design; it does not itself define how that solution was built.

**KAIROS-BA-08 (Task Registry).** All five tasks in this document are registered entries,
cross-referenced for their feedback relationship into KAIROS-BA-05 when recommended actions
constitute a new need.

## 13. What could not be established

### 13.1 Evaluation cadence

The source standard does not specify how frequently solution evaluation should recur once a
solution is in operation; this is left to organizational judgment.

**Open.** Whether KAIROS should define a minimum evaluation cadence for business-critical
solutions, or whether cadence is too dependent on solution criticality and rate of change for one
KAIROS wide answer to be meaningful.

### 13.2 Practice basis

The distinction and non-conflation requirement between solution and enterprise limitations
(`BA07-5.1`) is drawn directly from the source standard's own task definitions and its worked
example; this is one of the more directly upstream-sourced clauses in this document rather than a
KAIROS-original hardening.

**`BA07-13.1` (MUST) Practice basis recorded.** An implementation must record that `BA07-5.1`
traces closely to the source standard's own worked example, unlike several other clauses in the
KAIROS-BA series that are KAIROS-original formalizations of descriptive guidance.

### 13.3 What this document deliberately did not attempt

No treatment of the specific evaluation techniques (data mining, root cause analysis, and the rest)
beyond naming that they exist; per-technique guidance is BABOK Guide content not independently
verified for this pass.

**`BA07-13.2` (MUST) Gaps declared, not filled.** An implementation must not represent a matter
listed in Section 13.3 as specified by this document.
