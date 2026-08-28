# KAIROS STD 003, KAIROS-BA-03: Elicitation and Collaboration

**Standard.** KAIROS STD 003, the enterprise architecture standard.
**Part.** Pilot document, KAIROS-BA series. Not yet mapped to a numbered Part.
**Title.** Elicitation and collaboration.
**Version.** 0.1.0, pilot.
**Status.** Pilot draft, for structural evaluation only.
**Date of issue.** Not issued. Drafted 2026-08-28.
**Supersedes.** None.

## Binding of requirement language

As KAIROS-BA-01. Clause identifiers have the form `BA03-S.N`.

## Conformance

As KAIROS-BA-01, substituting this document.

## Clause index

| Clause | Modality | Subject |
| --- | --- | --- |
| **Section 1** | | **Scope and responsibilities** |
| `BA03-1.1` | MUST | Purpose satisfaction |
| `BA03-1.2` | MUST NOT | No requirements specification content |
| **Section 3** | | **Data model** |
| `BA03-3.1` | MUST | Prepare for Elicitation output |
| `BA03-3.2` | MUST | Conduct Elicitation output |
| `BA03-3.3` | MUST | Confirm Elicitation Results output |
| `BA03-3.4` | MUST | Communicate BA Information output |
| `BA03-3.5` | MUST | Manage Stakeholder Collaboration output |
| **Section 5** | | **State model** |
| `BA03-5.1` | MUST | Unconfirmed-to-confirmed transition |
| `BA03-5.2` | MUST NOT | No unconfirmed result used downstream |
| **Section 6** | | **Execution semantics** |
| `BA03-6.1` | MUST | Preparation precedes conduct |
| **Section 13** | | **What could not be established** |
| `BA03-13.1` | MUST | Practice basis recorded |
| `BA03-13.2` | MUST | Gaps declared, not filled |

## 1. Scope and responsibilities

### 1.1 What this component is

This document governs the five tasks IIBA groups as Elicitation and Collaboration: Prepare for
Elicitation, Conduct Elicitation, Confirm Elicitation Results, Communicate Business Analysis
Information, and Manage Stakeholder Collaboration. These tasks draw information out of
stakeholders and the enterprise and confirm it before it is used as an input to requirements work.

### 1.2 What this component is NOT

**`BA03-1.2` (MUST NOT) No requirements specification content.** This document must not define
how confirmed elicitation results are turned into specified, modelled, or verified requirements and
designs; that is KAIROS-BA-06's responsibility. This document ends at confirmed, communicated
information.

**`BA03-1.1` (MUST) Purpose satisfaction.** An implementation must be able to produce confirmed,
communicated elicitation results from any stakeholder engagement, with stakeholder willingness to
continue collaborating intact at the end of the activity.

## 2. Terminology

Extends KAIROS-BA-01 Section 2 and the BABOK Glossary. No new terms.

## 3. Data model

**`BA03-3.1` (MUST) Prepare for Elicitation output.** The Prepare for Elicitation task must produce
a defined elicitation activity plan including planned activities, scope, logistics, and anticipated
participants.

**`BA03-3.2` (MUST) Conduct Elicitation output.** The Conduct Elicitation task must produce
unconfirmed elicited information, captured in a format suited to the elicitation activity used.

**`BA03-3.3` (MUST) Confirm Elicitation Results output.** The Confirm Elicitation Results task must
produce confirmed elicitation information, relevant and useful as an input to further business
analysis work.

**`BA03-3.4` (MUST) Communicate BA Information output.** The Communicate Business Analysis
Information task must produce business analysis information that is properly communicated and
understood by stakeholders.

**`BA03-3.5` (MUST) Manage Stakeholder Collaboration output.** The Manage Stakeholder
Collaboration task must produce gained willingness from stakeholders to engage in business
analysis activities.

## 4. Interfaces

The elicitation activity plan (3.1) is a required input to Conduct Elicitation (3.2). Unconfirmed
results (3.2) are a required input to Confirm Elicitation Results (3.3). Confirmed results feed
forward into KAIROS-BA-04 and KAIROS-BA-06 as the raw material for requirements work; this
document's outputs are consumed, not produced, by those documents.

## 5. State model

**`BA03-5.1` (MUST) Unconfirmed-to-confirmed transition.** Elicited information must pass through
an explicit confirmation state, per Sections 3.2 and 3.3, before an implementation treats it as
reliable input to requirements work.

**`BA03-5.2` (MUST NOT) No unconfirmed result used downstream.** An implementation must not
pass unconfirmed elicitation results (the output of 3.2) directly into KAIROS-BA-04 or KAIROS-BA-06
as though they were confirmed; the source standard's own stated purpose of the confirmation task
is to check gathered information for errors, omissions, conflicts, and ambiguity before it is relied
upon.

## 6. Execution semantics

**`BA03-6.1` (MUST) Preparation precedes conduct.** The Prepare for Elicitation task must be
performed, and its output (3.1) available, before the Conduct Elicitation task begins for the same
activity; the source standard lists the elicitation activity plan as a required input to conducting
elicitation, not an optional one.

## 7. Outcome and failure taxonomy

Elicitation results are either confirmed (ready for downstream use) or unconfirmed (not ready);
there is no partial-confirmation state in the source material, and this document does not invent
one.

## 8. Observability and the audit record

Confirmed elicitation results (3.3) should be retained with a record of which stakeholders
participated and which elicitation technique was used, since traceability of a requirement back to
its elicitation source is a recurring need across KAIROS-BA-04's traceability task.

## 9. Extension model

An implementation may select from the source standard's frequently used techniques per task
(benchmarking, document analysis, interviews, focus groups, workshops, brainstorming, and others)
based on context, or substitute an organization-specific technique that produces an equivalent
output per Section 3.

## 10. Standards and specifications

The Business Analysis Standard, v2.0, 2025, IIBA, the Elicitation and Collaboration task cards.
Primary source for this document, verified by direct reading.

BABOK Guide, v3, 2015, IIBA. Referenced for the complete technique list per task; not independently
verified for this document.

## 11. Anti patterns

**Treating conducted elicitation as confirmed by default.** `BA03-5.2` exists because the pressure
to move quickly makes it tempting to skip the confirmation step, particularly when the same person
who conducted elicitation is also the one who would confirm it, and self-confirmation defeats the
purpose of an independent check for errors, omissions, and ambiguity.

**Treating stakeholder collaboration as a one-time task.** The source standard frames Manage
Stakeholder Collaboration as ongoing, "maintain the free flow of information when obstacles and
setbacks occur," not a task performed once early in an initiative and considered complete.

## 12. Boundaries with other Parts

**KAIROS-BA-02 (Planning and Monitoring).** The stakeholder engagement approach produced in
KAIROS-BA-02 Section 3.2 is a required input to every task in this document; this document does
not redefine stakeholder engagement strategy.

**KAIROS-BA-04 (Requirements and Designs Life Cycle Management), KAIROS-BA-06 (Requirements
Analysis and Design Definition).** Both consume this document's confirmed elicitation results as
input; neither redefines what "confirmed" means, that definition belongs to this document.

**KAIROS-BA-08 (Task Registry).** All five tasks in this document are registered entries,
cross-referenced for their consumption of KAIROS-BA-02 outputs and production of inputs to
KAIROS-BA-04 and KAIROS-BA-06.

## 13. What could not be established

### 13.1 Confirmation authority

The source standard states confirmation "typically involves any stakeholders that have relevant
knowledge or experience," but does not specify whether the person who conducted the elicitation
may also serve as its sole confirmer, or whether independent confirmation is required.

**Open.** Whether KAIROS should require confirmation by someone other than the elicitation
conductor for higher-risk requirements, given the self-confirmation anti-pattern named in Section
11, or whether this is better left to KAIROS-BA-02's governance approach to decide per initiative.

### 13.2 Practice basis

The requirement that unconfirmed results never pass downstream (`BA03-5.2`) is a KAIROS
formalization of a purpose statement in the source standard, not a restatement of an explicit
upstream prohibition; IIBA describes what confirmation is for but does not itself say "unconfirmed
results must not be used."

**`BA03-13.1` (MUST) Practice basis recorded.** An implementation must record that `BA03-5.2` is a
KAIROS-original hardening of the source standard's descriptive guidance, not a direct restatement
of an IIBA requirement.

### 13.3 What this document deliberately did not attempt

No treatment of the specific elicitation techniques (workshops, interviews, focus groups, and the
rest) beyond naming that they exist and are context-dependent; per-technique guidance is BABOK
Guide content not independently verified for this pass.

**`BA03-13.2` (MUST) Gaps declared, not filled.** An implementation must not represent a matter
listed in Section 13.3 as specified by this document.
