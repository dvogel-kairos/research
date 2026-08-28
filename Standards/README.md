# Standards

Research output. Nothing here is a primary source; sources live in `Library/`.

```
std-003/              the fourteen part enterprise architecture standard
  checkpoints/        one per authoring session, stating what was decided and why
registers/            most derived by tools/build_registers.py, two hand authored
tools/                the generators and validators
```

## registers/

| File | Derived from | Hand maintained |
| --- | --- | --- |
| `clauses.md` | clause identifiers in each part | nothing |
| `questions.md` | each part's questions to Part 0 | nothing |
| `verification.md` | each part's section 13.1 | the status, checker and date columns |
| `library-index.md` | the contents of `Library/`, plus sidecar tags | nothing |
| `allocation.md` | nothing. A decision, not a derivation | all of it |
| `taxonomy.md` | nothing. Supplied by the standards owner verbatim | all of it |
| `collision-map.md` | judgement applied to the above two | all of it |

`verification.md` has a known gap. Parts 1 through 4 predate the convention of
naming unobtained sources in bold at the head of a paragraph, so the generator
finds no rows for them and their section 13.1 needs one manual pass to be
extractable. That is a real finding about the documents rather than a fault in the
tool: the convention emerged partway through the series.

Read `allocation.md` first for the STD 003 collision question, then
`collision-map.md` for the stage and Azure component collision question. They
are independent checks and a proposed series has to clear both.

## Conventions

Clause identifiers are `P{part}-{section}.{ordinal}`, permanent, never renumbered
and never reused. `tools/validate_clauses.py` checks uniqueness, ordering and
contiguity within each section, and every delivered part passes it.

House style: no em dash, en dash or hyphen used as punctuation.

No part names any real organisation, product or system. That constraint is from
the authoring brief and it is checkable by grep.
