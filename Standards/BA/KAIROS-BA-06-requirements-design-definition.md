# KAIROS STD 003, KAIROS-BA-06: Requirements Analysis and Design Definition

**Standard.** KAIROS STD 003, the enterprise architecture standard.
**Part.** Pilot document, KAIROS-BA series. Not yet mapped to a numbered Part.
**Title.** Requirements analysis and design definition.
**Version.** 0.1.0, pilot.
**Status.** Pilot draft, for structural evaluation only.
**Date of issue.** Not issued. Drafted 2026-08-28.
**Supersedes.** None.

## Binding of requirement language

As KAIROS-BA-01. Clause identifiers have the form `BA06-S.N`.

## Conformance

As KAIROS-BA-01, substituting this document.

## Clause index

| Clause | Modality | Subject |
| --- | --- | --- |
| **Section 1** | | **Scope and responsibilities** |
| `BA06-1.1` | MUST | Purpose satisfaction |
| `BA06-1.2` | MUST NOT | No life cycle management content |
| **Section 3** | | **Data model** |
| `BA06-3.1` | MUST | Requirement/design distinction |
| `BA06-3.2` | MUST | Specify and Model output |
| `BA06-3.3` | MUST | Verify output |
| `BA06-3.4` | MUST | Validate output |
| `BA06-3.5` | MUST | Requirements Architecture output |
| `BA06-3.6` | MUST | Design Options output |
| `BA06-3.7` | MUST | Recommend Solution output |
| **Section 5** | | **State model** |
| `BA06-5.1` | MUST | Specified-verified-validated sequence |
| `BA06-5.2` | MUST NOT | No validation before verification |
| **Section 13** | | **What could not be established** |
| `BA06-13.1` | MUST | Practice basis recorded |
| `BA06-13.2` | MUST | Gaps declared, not filled |

## 1. Scope and responsibilities

### 1.1 What this component is

This document governs the six tasks IIBA groups as Requirements Analysis and Design Definition:
Specify and Model Requirements and Designs, Verify Requirements and Designs, Validate
Requirements and Designs, Define Requirements Architecture, Define Design Options, and Analyze
Potential Value and Recommend Solution. This is where confirmed elicitation results become
specified, quality-checked requirements and designs, and where a solution is ultimately
recommended.

### 1.2 What this component is NOT

**`BA06-1.2` (MUST NOT) No life cycle management content.** This document must not define how a
requirement or design is traced, maintained, prioritized, or approved once specified; that is
KAIROS-BA-04's responsibility. This document ends at a recommended solution, ready for the
approval task in KAIROS-BA-04.

**`BA06-1.1` (MUST) Purpose satisfaction.** An implementation must be able to produce a specified,
verified, and validated set of requirements and designs, structured into a requirements
architecture, with a recommended solution selected from assessed design options.

## 2. Terminology

Extends KAIROS-BA-01 Section 2 and the BABOK Glossary.

**Requirement.** A usable representation of a need.

**Design.** A usable representation of a solution.

## 3. Data model

**`BA06-3.1` (MUST) Requirement/design distinction.** An implementation must maintain the source
standard's distinction between requirements, which focus on understanding what kind of value
could be delivered, and designs, which focus on understanding how value might be realized if a
solution is built; the two are interdependent and cyclical, per the source standard, but must not be
collapsed into a single undifferentiated artifact.

**`BA06-3.2` (MUST) Specify and Model output.** The Specify and Model Requirements and Designs
task must produce requirements and designs specified and modelled in text, matrices, or diagrams.

**`BA06-3.3` (MUST) Verify output.** The Verify Requirements and Designs task must produce
requirements and designs of sufficient quality, internally consistent, to serve as a basis for further
work.

**`BA06-3.4` (MUST) Validate output.** The Validate Requirements and Designs task must produce
requirements and designs confirmed to align with business goals and objectives and to deliver value
to stakeholders.

**`BA06-3.5` (MUST) Requirements Architecture output.** The Define Requirements Architecture
task must produce a defined requirements architecture showing the interrelationships among
requirements and designs as a single supporting whole.

**`BA06-3.6` (MUST) Design Options output.** The Define Design Options task must produce defined
design options, build, purchase, or a combination, that satisfy the business need.

**`BA06-3.7` (MUST) Recommend Solution output.** The Analyze Potential Value and Recommend
Solution task must produce a recommendation of the most appropriate solution based on evaluation
of all defined design options.

## 4. Interfaces

Confirmed elicitation results from KAIROS-BA-03 are a required input to Specify and Model (3.2).
Specified requirements and designs (3.2) are a required input to Verify (3.3); verified requirements
(3.3) are a required input to Validate (3.4) and to KAIROS-BA-04's approval task. The change
strategy and solution scope from KAIROS-BA-05 are required inputs to Define Design Options (3.6).
The solution recommendation (3.7) is a required input to KAIROS-BA-04's prioritization and
approval tasks and, once implemented, to KAIROS-BA-07's evaluation tasks.

## 5. State model

**`BA06-5.1` (MUST) Specified-verified-validated sequence.** A requirement or design must pass
through specified (3.2), then verified (3.3), then validated (3.4) states in that order; each state
represents a distinct quality gate, internal consistency for verification, business alignment for
validation, and neither may be skipped.

**`BA06-5.2` (MUST NOT) No validation before verification.** An implementation must not validate a
requirement or design (3.4) that has not first passed verification (3.3); validating an internally
inconsistent requirement risks confirming business alignment for something that cannot actually be
built as specified.

## 6. Execution semantics

Requirements and designs are interdependent and cyclical per the source standard: as designs are
created, they can reveal new insights that enhance requirements, and changing requirements can
lead to design updates. This document does not impose a single linear pass through Sections 3.2
through 3.7 for this reason; the state ordering in Section 5 applies per requirement or design
instance, not as a single initiative-wide gate.

## 7. Outcome and failure taxonomy

Verification (3.3) and validation (3.4) are each pass/fail per instance; a requirement or design
failing either returns to specification (3.2) for rework, per the cyclical relationship described in
Section 6.

## 8. Observability and the audit record

The state of each requirement or design, specified, verified, or validated, should be recorded and
traceable per KAIROS-BA-04 Section 3.1's traceability requirement, so that the quality gate history
of any given requirement can be reconstructed.

## 9. Extension model

An implementation may select from the source standard's frequently used techniques per task
(data modelling, interface analysis, use cases and scenarios, user stories, acceptance and evaluation
criteria, metrics and KPIs, vendor assessment, and others) based on context, or substitute an
organization-specific technique that produces an equivalent output per Section 3.

## 10. Standards and specifications

The Business Analysis Standard, v2.0, 2025, IIBA, Section 4.4 (Understanding Requirements and
Designs) and the Requirements Analysis and Design Definition task cards. Primary source for this
document, verified by direct reading.

BABOK Guide, v3, 2015, IIBA, Section 2.5 (Requirements and Designs), cited by the source standard
as the origin of the requirements/design cycle diagram. Not independently verified for this
document.

## 11. Anti patterns

**Collapsing requirements and designs into one document.** `BA06-3.1` exists because it is common
to write a single document that mixes what is needed with how it will be built, which makes it
impossible to verify the requirement independent of a specific implementation choice, defeating the
purpose of keeping the two distinct.

**Validating before verifying.** `BA06-5.2` exists because validation, checking business alignment,
is often performed as a satisfying-feeling milestone review while the underlying internal
consistency check that verification represents gets skipped or rushed, producing a validated
requirement that cannot actually be implemented as written.

## 12. Boundaries with other Parts

**KAIROS-BA-03 (Elicitation and Collaboration).** Confirmed elicitation results are the required raw
material this document's specification task operates on; this document does not redefine what
"confirmed" means.

**KAIROS-BA-04 (Requirements and Designs Life Cycle Management).** Verified and validated
requirements from this document are required inputs to KAIROS-BA-04's approval task; this
document does not itself define approval, traceability, or prioritization.

**KAIROS-BA-05 (Strategy Analysis).** The change strategy and solution scope from KAIROS-BA-05
bound this document's design option task; a design option outside the solution scope is a
nonconformity under this document.

**KAIROS-BA-08 (Task Registry).** All six tasks in this document are registered entries,
cross-referenced for their position in the specified-verified-validated sequence and their downstream
consumption by KAIROS-BA-04 and KAIROS-BA-07.

## 13. What could not be established

### 13.1 Quality bar for verification

The source standard states verification ensures requirements are of "sufficient quality" and
"internally consistent" but does not define a measurable quality bar; sufficiency is left to the
verifying stakeholder's judgment.

**Open.** Whether KAIROS should define a checklist-based quality bar for verification to reduce
reliance on individual judgment, or whether requirements quality is inherently too context-dependent
for a fixed checklist to be meaningful across all KAIROS initiative types.

### 13.2 Practice basis

The strict state-ordering requirement in `BA06-5.1` and `BA06-5.2` is a KAIROS-original hardening;
the source standard describes verification and validation as related but does not explicitly prohibit
performing them out of order or in parallel.

**`BA06-13.1` (MUST) Practice basis recorded.** An implementation must record that the ordering in
Section 5 is a KAIROS-original quality-gate decision, not a restatement of an explicit IIBA sequencing
requirement.

### 13.3 What this document deliberately did not attempt

No treatment of the specific modelling notations (data models, use cases, and the rest) beyond
naming that they exist; per-notation guidance is BABOK Guide content not independently verified for
this pass.

**`BA06-13.2` (MUST) Gaps declared, not filled.** An implementation must not represent a matter
listed in Section 13.3 as specified by this document.
