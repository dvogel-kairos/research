# Allocation register

**Status: open. This is a decision, not a derivation, and it blocks the research
programme.** Every other register in this folder is generated. This one is
maintained by hand and is empty of answers until the standards owner fills it in.

## The question

The inbound handoff from the research thread proposes thirteen new decomposed
source series and closes by asking the standards owner to confirm, for each,
whether it maps to an existing numbered STD 003 Part, becomes a new Part, or stays
a standalone series. That question has not been answered and it cannot be deferred,
because four of the proposed series cover subjects that unwritten STD 003 parts
already own.

## Why it cannot be deferred

If a series is authored before the part whose subject it covers, it fixes a
vocabulary that the part must then either adopt or diverge from. Section 13.7 of
Parts 4, 5, 6 and 7 records that failure happening *within* this one standard:
eight structures specified independently across seven parts, three vocabularies for
the frontier concept, and Parts 5 and 7 now treating the third value differently in
adjacent components that exchange values. Reproducing that across two bodies of
work deliberately would be worse than reproducing it once by accident.

## Proposed sorting, on the three axes of `taxonomy.md`

The sorting below is unchanged in substance and now carries a stage tag, because
the question "does this collide" and the question "when is this needed" have
different answers and both are needed. A series with a `component` tag of `none`
is safe to author standalone. A series with a component tag must feed that part
rather than precede it.

| Proposed series | Stage | Component | Verdict |
| --- | --- | --- | --- |
| KAIROS-REQ | 4 | 2 | feeds Part 2 |
| KAIROS-API | 5 | 9 | feeds Part 9. Worst collision: Part 9 is wholly a Design stage part |
| KAIROS-DATA | 2, 5 | 4, 10 | feeds Parts 4 and 10 |
| KAIROS-DINT | 1, 6 | 6, 11 | feeds Parts 6 and 11 |
| KAIROS-QA | 7, 8 | 12 | feeds Part 12. Second worst collision, for the same reason |
| KAIROS-SEC | 5, 6, 9 | none | standalone. Spans the security split of stages 5 and 6 |
| KAIROS-AZURE | 5, 6, 8 | none | standalone. Split by function; see below |
| KAIROS-CLOUD | 5, 6 | none | standalone |
| KAIROS-CODE | 6 | none | standalone |
| KAIROS-MOD | 1, 2 | none | standalone, and a **process stage series**; see below |
| KAIROS-PM | 3, 4 | none | standalone |
| KAIROS-GOV | 1, 9 | none | standalone |
| KAIROS-UX | 5 | none | standalone |
| KAIROS-EVT, delivered | 1, 6 | 6 | already a dependency of Parts 1 to 7 |
| KAIROS-BA | 2, 3, 4 | none | standalone, and a **process stage series**; see below |

### The process stage series come first

The stage taxonomy states that stages 1 and 2 are settled before the lifecycle
stages, because every later stage assumes their pattern. Three series carry a
stage 1 or stage 2 tag and no component collision: **KAIROS-MOD**, **KAIROS-GOV**
and **KAIROS-BA**, the last already delivered.

That is an argument for reordering the handoff's priority list. It put SEC first on
the strength of the client base, which is a sound business reason. The taxonomy
supplies a competing structural reason for MOD and GOV first: legacy decomposition
and architecture decision records are how a legacy application enters the
organisation and how the decision to admit it is recorded, and both are stage 1.
The two arguments are not reconcilable by analysis and the standards owner picks.

### KAIROS-AZURE and the axis it is named for

The handoff asks whether AZURE should be one series of eighteen sources or split by
function. The Azure axis answers it: the eighteen sources do not share a subject,
they share a vendor. Splitting by function gives messaging, identity, compute,
data and observability series whose stage tags differ, which is what a reader needs.
Keeping them together gives one series whose only common property is a tag that
`taxonomy.md` forbids from appearing in a standard at all.

Recommendation: split by function, and let the Azure tag do the work of grouping
them in the manifest rather than in the document structure.

### Bucket A, research feeding an unwritten part. Do not author as a series.

| Proposed series | Part that owns the subject |
| --- | --- |
| KAIROS-API. OpenAPI, JSON:API, REST guidelines, Fielding, Richardson | Part 9, schema and contract registry |
| KAIROS-QA. ISTQB, ISO/IEC/IEEE 29119, DORA, SRE | Part 12, conformance and assurance harness |
| KAIROS-DATA. normalization, Kimball, Data Model Resource Book | Part 10, reference and master data; Part 4, metadata repository |
| KAIROS-DINT. Enterprise Integration Patterns, DMBOK, Medallion, Delta Lake | Part 6, orchestration; Part 11, artifact store |
| KAIROS-REQ. IEEE/ISO/IEC 29148, INVEST, Gherkin | Part 2 adjacent. 29148 sits upstream of the whole standard |

The output of bucket A work is source acquisition into `Library/` plus notes, not a
parallel document series.

### Bucket B, no collision. Safe to author in parallel, in any order.

KAIROS-SEC, KAIROS-AZURE, KAIROS-CLOUD, KAIROS-CODE, KAIROS-MOD, KAIROS-PM,
KAIROS-GOV, KAIROS-UX.

The handoff puts SEC first on the strength of the healthcare and pharmaceutical
client base. That priority stands and is reinforced by the absence of any
collision: SEC cannot create a vocabulary conflict with an unwritten part.

Note the handoff's own warning on SEC before starting. ASVS and the OWASP Cheat
Sheet Series are reference-manual scale and a single pass will not responsibly
cover either; plan partial coverage and declare it in section 13.

### Bucket C, delivered, and one of them is already load bearing.

| Series | Status question |
| --- | --- |
| KAIROS-EVT, 10 documents, CloudEvents | **Already a dependency of STD 003.** All seven delivered parts cite CloudEvents as their event envelope model in section 4 and section 10. It is not a parallel pilot. |
| KAIROS-BA, 9 documents, IIBA Business Analysis Standard | No STD 003 dependency. Standalone. |

Both need an explicit status: numbered part, or "standalone reference series, cited
by STD 003 but not part of it." The second is probably right for both and needs
saying rather than defaulting.

## Sequencing that follows from the sorting

1. **Now.** The standards owner confirms or amends the buckets above, and places
   the Source Library spreadsheet and Research Roadmap HTML in `Library/`.
2. **Then.** Acquire the four priority sources named in `Library/README.md` and
   close those rows in `verification.md`. Each currently supports a MUST NOT that
   refuses a construct implementers use routinely, on secondary description.
3. **Then.** Finish STD 003. Part 8 is in draft. Parts 9 through 13 follow, each
   drawing on its bucket A acquisitions rather than being preceded by a series.
   Part 0 last, inheriting the questions in `questions.md`.
4. **In parallel throughout.** Bucket B series, SEC first.

## The naming constraint, and an unresolved conflict

`taxonomy.md` records it and it needs a decision. STD 003 parts may not name a real
organisation, product or system; all seven delivered parts are verified clean.
KAIROS-EVT names Azure Event Grid. Either the constraint binds only STD 003 parts,
or EVT has a defect. My reading is the former and the boundary needs stating; it is
not mine to settle.

## What is needed and is not here

The Source Library spreadsheet and the Research Roadmap HTML. The handoff instructs
that both be pulled before starting anything. Neither is in `Library/`. Without
them the 117 catalogued sources are names with no live link, no access status, no
trust tier and no rating, and bucket A cannot be sequenced.

## A second, independent collision check

This register answers one question: does a proposed series collide with an
unwritten STD 003 part. A second, orthogonal question is now tracked in
`Standards/registers/collision-map.md`, against the stage and Azure component
taxonomy the standards owner supplied on 2026-08-28: does a proposed series
collide with *another proposed series*. Bucket B in particular, cleared here
because it does not touch a STD 003 part, still has real internal collisions:
Azure DevOps Pipelines is currently claimed by AZURE, CLOUD, CODE and QA at
once. A series must clear both checks before it is authored, not just this one.
