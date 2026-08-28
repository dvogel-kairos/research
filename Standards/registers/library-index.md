# Library index

Derived by `Standards/tools/build_registers.py`. As at 2026-08-28.
One row per source placed in `Library/`, derived from the tracked
`<file>.note.md` sidecars so that this index reproduces identically in
any clone, including one where the gitignored binaries are absent.
File size and local presence are deliberately not recorded here: they
differ between working copies, and a register that changes depending on
who regenerated it is not a register. The tool reports them to the
console instead.

Stage and Azure Component are read from the sidecar per the convention in
`Library/README.md`, and are blank until tags are confirmed.

| Source | Sidecar | Stage | Azure Component |
| --- | --- | --- | --- |
| pragmatic-nassery-2025-next-level-ab-testing.pdf | yes |  |  |
| pragmatic-wengrow-2024-common-sense-guide-to-data-structures-and-algorithms-in-javascript-v1.pdf | yes |  |  |
| pragmatic-zinoviev-2016-python-companion-to-data-science.pdf | yes |  |  |

Sources recorded: **3**.
Confirmed stage tag: **0**. Confirmed Azure component tag: **0**.

**Sources with a sidecar but no confirmed tags (3).**
A sidecar carrying `proposed_stage` is a suggestion awaiting
confirmation, not a tag. Rename the key to `stage` to confirm:
- pragmatic-nassery-2025-next-level-ab-testing.pdf
- pragmatic-wengrow-2024-common-sense-guide-to-data-structures-and-algorithms-in-javascript-v1.pdf
- pragmatic-zinoviev-2016-python-companion-to-data-science.pdf
