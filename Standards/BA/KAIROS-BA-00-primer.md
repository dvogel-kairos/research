# KAIROS STD 003, KAIROS-BA-00: Business Analysis Primer

**Standard.** KAIROS STD 003, the enterprise architecture standard.
**Part.** Pilot document, KAIROS-BA series. Not yet mapped to a numbered Part.
**Title.** Business analysis primer.
**Version.** 0.1.0, pilot.
**Status.** Pilot draft, for structural evaluation only.
**Date of issue.** Not issued. Drafted 2026-08-28.
**Supersedes.** None.

## Why this document does not use the thirteen section template

As with KAIROS-EVT-00 and STD 003 Part 0 before it, a document providing orientation rather than
specifying a single component's behavior is not obliged to use the thirteen section template. This
document is non-normative: no MUST, MUST NOT, SHOULD, SHOULD NOT, or MAY clauses, and no
clause identifiers. A reader who only needs to implement against the series should start at
KAIROS-BA-01 directly.

## 1. Purpose

This document orients a reader to why the KAIROS-BA series standardizes on IIBA's Business
Analysis Core Concept Model (BACCM) and the 30-task structure from the BABOK Guide and its free
companion, The Business Analysis Standard, and how the nine documents in the series divide the
subject.

## 2. Source material and its nature

Two IIBA documents anchor this series. The BABOK Guide (version 3, 2015) is the full body of
knowledge, paywalled, membership or purchase required. The Business Analysis Standard (version
2.0, 2025) is IIBA's free companion, covering the same six knowledge areas and the same 30 tasks at
a summary level. The KAIROS-BA series is built primarily from the Standard, since it is the source
actually verified by direct reading during this drafting pass, with the Guide cited as the deeper
source where the Standard itself points to it.

One property of the source material shapes every document in this series: IIBA writes in descriptive
prose, not in RFC 2119 modal language. A task card says "this task defines the scope of the
elicitation activity," not "the analyst MUST define the scope." Every normative clause in the
KAIROS-BA series is therefore a KAIROS translation of IIBA's descriptive guidance into a testable
requirement, not a restatement of an upstream requirement that already existed in that form. This
is a real difference from the KAIROS-EVT series, where the CloudEvents specification already used
MUST/SHOULD/MAY language KAIROS could largely adopt directly. Each KAIROS-BA document's Section
13 says so explicitly rather than letting the modal verbs imply a false precision in the source.

## 3. The Business Analysis Core Concept Model (BACCM)

Six concepts, change, need, solution, value, stakeholder, and context, form the model IIBA uses to
describe effective business analysis. The Standard frames this as a "thinking model" and an
"organizing model," not a sequential process; the six concepts and their interrelationships are meant
to be considered together, not worked through in order. KAIROS-BA-01 is built around this model
because every one of the 30 tasks in KAIROS-BA-02 through 07 touches at least one of these six
concepts, and several touch all six.

## 4. The 30 tasks and six knowledge areas

The Standard organizes its 30 business analysis tasks into six knowledge areas:

| Knowledge Area | Task Count | KAIROS Document |
|---|---|---|
| Business Analysis Planning and Monitoring | 5 | KAIROS-BA-02 |
| Elicitation and Collaboration | 5 | KAIROS-BA-03 |
| Requirements and Designs Life Cycle Management | 5 | KAIROS-BA-04 |
| Strategy Analysis | 4 | KAIROS-BA-05 |
| Requirements Analysis and Design Definition | 6 | KAIROS-BA-06 |
| Solution Evaluation | 5 | KAIROS-BA-07 |

IIBA is explicit that these tasks "may not follow a linear sequence and can be carried out
concurrently," and that some tasks generate outputs other tasks depend on regardless of knowledge
area boundaries. This is why KAIROS-BA-08, the Task Registry, exists as a ninth document: it is the
single place that tracks which task produces which artifact and which task consumes it, since that
dependency graph cuts across the six knowledge area documents rather than living inside any one of
them.

## 5. What this series does not cover

The Standard explicitly does not include the knowledge areas' full technique catalog (more than 90
techniques across four IIBA documents) or detailed guidance on adjacent disciplines it references,
cybersecurity analysis, data analytics, and product ownership analysis, each of which IIBA publishes
as a separate guide. KAIROS-BA cites these as the technique source but does not attempt to restate
them; a KAIROS standard for technique selection itself, if one is warranted, is a separate future
effort.

## 6. Cross-references

KAIROS-BA-01 through KAIROS-BA-08 (this series). A composition document analogous to STD 003
Part 0, addressing how these nine documents interact as a system, has not yet been drafted for this
series, matching the same gap noted in KAIROS-EVT-00.
