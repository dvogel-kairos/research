#!/usr/bin/env python3
"""
Derives every register in Standards/registers/ from the delivered documents.

Nothing in this repository states a count that was typed by hand. Run this and
commit the output. If a figure in a register disagrees with a figure elsewhere,
this script is the arbiter, because it reads the primary documents.

Usage, from the repository root:
    python3 Standards/tools/build_registers.py
"""

import csv
import os
import re
import sys
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PARTS_DIR = os.path.join(ROOT, "Standards", "std-003")
REG_DIR = os.path.join(ROOT, "Standards", "registers")
LIB_DIR = os.path.join(ROOT, "Library")

PART_RE = re.compile(r"KAIROS-STD-003-Part-(\d+)-v[\d.]+-\w+\.md$")


def parts():
    found = []
    for name in sorted(os.listdir(PARTS_DIR)):
        m = PART_RE.match(name)
        if m:
            found.append((int(m.group(1)), os.path.join(PARTS_DIR, name)))
    return sorted(found)


def section(text, number):
    """Return the body of '### {number} ...' up to the next '### ' at the same level."""
    pat = re.compile(r"^### " + re.escape(number) + r" .*?$(.*?)(?=^### |\Z)",
                     re.M | re.S)
    m = pat.search(text)
    return m.group(1) if m else None


def find_section_by_title(text, needle):
    """Return (number, body) for the first '### 13.x <title>' whose title matches."""
    for m in re.finditer(r"^### (13\.\d+) (.*?)$(.*?)(?=^### |\Z)", text, re.M | re.S):
        if needle.lower() in m.group(2).lower():
            return m.group(1), m.group(3)
    return None, None


def clause_stats(text, prefix):
    ids = re.findall(r"^\*\*(" + prefix + r"-\d+\.\d+) \((MUST NOT|MUST|SHOULD NOT|SHOULD|MAY)\)", text, re.M)
    by_mod = {}
    for _, mod in ids:
        by_mod[mod] = by_mod.get(mod, 0) + 1
    return len(ids), by_mod


def questions_to_part_zero(text):
    num, body = find_section_by_title(text, "Part 0")
    if body is None:
        return None, []
    paras = [p.strip() for p in body.split("\n\n") if p.strip()]
    items = []
    for i, para in enumerate(paras):
        if i == 0:
            continue            # every such section opens with a lead-in
        if para.startswith(("#", "|", "-", "*")):
            continue
        items.append(" ".join(para.split()))
    return num, items


def unverified_sources(text):
    num, body = find_section_by_title(text, "not obtained")
    if body is None:
        num, body = find_section_by_title(text, "could not be")
    if body is None:
        return None, []
    names = []
    for m in re.finditer(r"^\*\*(.+?)\*\*", body, re.M):
        name = " ".join(m.group(1).split()).rstrip(".")
        if re.match(r"P\d+-\d+\.\d+ \(", name):
            continue            # the section's own clause, not a source
        if name and name not in names:
            names.append(name)
    return num, names


def write(path, lines):
    with open(path, "w") as fh:
        fh.write("\n".join(lines) + "\n")
    print("wrote", os.path.relpath(path, ROOT))


def main():
    ps = parts()
    if not ps:
        sys.exit("no delivered parts found in " + PARTS_DIR)
    stamp = date.today().isoformat()
    os.makedirs(REG_DIR, exist_ok=True)

    # ---- clause counts -------------------------------------------------
    rows = []
    for n, path in ps:
        text = open(path).read()
        total, by_mod = clause_stats(text, "P%d" % n)
        words = len(text.split())
        rows.append((n, total, by_mod, words))

    out = ["# Clause register", "",
           "Derived by `Standards/tools/build_registers.py`. As at %s." % stamp,
           "Do not edit by hand.", "",
           "| Part | Clauses | MUST | MUST NOT | SHOULD | SHOULD NOT | MAY | Words |",
           "| --- | --- | --- | --- | --- | --- | --- | --- |"]
    tot = [0, 0, 0, 0, 0, 0, 0]
    for n, total, bm, words in rows:
        vals = [total, bm.get("MUST", 0), bm.get("MUST NOT", 0), bm.get("SHOULD", 0),
                bm.get("SHOULD NOT", 0), bm.get("MAY", 0), words]
        tot = [a + b for a, b in zip(tot, vals)]
        out.append("| %d | %s |" % (n, " | ".join(str(v) for v in vals)))
    out.append("| **All** | %s |" % " | ".join("**%d**" % v for v in tot))
    out += ["", "Parts delivered: **%d** of 14. Not yet authored: %s." %
            (len(rows), ", ".join(str(i) for i in [0] + [i for i in range(1, 14)
             if i not in [r[0] for r in rows]]))]
    write(os.path.join(REG_DIR, "clauses.md"), out)

    # ---- questions inherited by Part 0 ---------------------------------
    out = ["# Questions inherited by Part 0", "",
           "Derived by `Standards/tools/build_registers.py`. As at %s." % stamp,
           "Do not edit by hand. Part 0 is authored last and inherits every question",
           "each part handed forward rather than answering.", ""]
    grand = 0
    detail = []
    out += ["| Part | Section | Questions |", "| --- | --- | --- |"]
    for n, path in ps:
        num, items = questions_to_part_zero(open(path).read())
        grand += len(items)
        out.append("| %d | %s | %d |" % (n, num or "not found", len(items)))
        detail.append((n, num, items))
    out.append("| **All** | | **%d** |" % grand)
    out += ["", "## The questions, in full", ""]
    for n, num, items in detail:
        out += ["### From Part %d, section %s" % (n, num), ""]
        for i, q in enumerate(items, 1):
            out.append("%d. %s" % (i, q))
        out.append("")
    write(os.path.join(REG_DIR, "questions.md"), out)

    # ---- verification debt ---------------------------------------------
    out = ["# Verification debt", "",
           "Derived by `Standards/tools/build_registers.py`. As at %s." % stamp,
           "Source names are extracted from each part's section 13.1. The status",
           "column is the one field in this repository that is maintained by hand:",
           "set it to `obtained` when the source lands in `Library/` and the claims",
           "resting on it have been checked.", ""]
    for n, path in ps:
        num, names = unverified_sources(open(path).read())
        out += ["## Part %d, section %s" % (n, num or "not found"), "",
                "| Source | Status | Checked by | Date |",
                "| --- | --- | --- | --- |"]
        for name in names:
            out.append("| %s | not obtained | | |" % name)
        out.append("")
    write(os.path.join(REG_DIR, "verification.md"), out)

    # ---- library index ---------------------------------------------------
    # Sidecar convention, per Library/README.md: <same-name>.note.md may carry
    # lines "stage: <comma list>" and "azure_components: <comma list>". Read
    # them if present; leave the columns blank if not, rather than guessing.
    def read_tags(note_path):
        if not os.path.exists(note_path):
            return "", ""
        text = open(note_path).read()
        stage = re.search(r"^stage:\s*(.+)$", text, re.M | re.I)
        comp = re.search(r"^azure_components:\s*(.+)$", text, re.M | re.I)
        return (stage.group(1).strip() if stage else "",
                comp.group(1).strip() if comp else "")

    # A source is known from EITHER the file itself OR a tracked `.note.md`
    # sidecar. Library binaries are gitignored, so in a fresh clone only the
    # sidecars exist. Deriving from files alone would let a clone regenerate an
    # empty index and erase the record of what was placed.
    known = {}
    for dirpath, _, files in os.walk(LIB_DIR):
        for f in sorted(files):
            if f.startswith(".") or f == "README.md":
                continue
            full = os.path.join(dirpath, f)
            if f.endswith(".note.md"):
                target = os.path.relpath(full[: -len(".note.md")], LIB_DIR)
                known.setdefault(target, {})["note"] = full
            else:
                rel = os.path.relpath(full, LIB_DIR)
                known.setdefault(rel, {})["size"] = os.path.getsize(full)

    entries = []
    for rel in sorted(known):
        info = known[rel]
        note = info.get("note")
        stage, comp = read_tags(note) if note else ("", "")
        entries.append((rel, info.get("size"), bool(note), stage, comp))

    out = ["# Library index", "",
           "Derived by `Standards/tools/build_registers.py`. As at %s." % stamp,
           "One row per source placed in `Library/`, derived from the tracked",
           "`<file>.note.md` sidecars so that this index reproduces identically in",
           "any clone, including one where the gitignored binaries are absent.",
           "File size and local presence are deliberately not recorded here: they",
           "differ between working copies, and a register that changes depending on",
           "who regenerated it is not a register. The tool reports them to the",
           "console instead.", "",
           "Stage and Azure Component are read from the sidecar per the convention in",
           "`Library/README.md`, and are blank until tags are confirmed.", "",
           "| Source | Sidecar | Stage | Azure Component |",
           "| --- | --- | --- | --- |"]
    for rel, size, has_note, stage, comp in entries:
        out.append("| %s | %s | %s | %s |" % (
            rel, "yes" if has_note else "**missing**", stage, comp))
    if not entries:
        out.append("| *(Library is empty)* | | | |")
    missing = [e[0] for e in entries if not e[2]]
    untagged = [e[0] for e in entries if e[2] and not (e[3] or e[4])]
    out += ["", "Sources recorded: **%d**." % len(entries),
            "Confirmed stage tag: **%d**. Confirmed Azure component tag: **%d**." %
            (sum(1 for e in entries if e[3]), sum(1 for e in entries if e[4]))]
    if missing:
        out += ["", "**Sources with no sidecar (%d).** Provenance, completeness and"
                % len(missing),
                "trust tier are unrecorded for these, so a clause may not rest on them:"]
        out += ["- %s" % m for m in missing]
    if untagged:
        out += ["", "**Sources with a sidecar but no confirmed tags (%d).**"
                % len(untagged),
                "A sidecar carrying `proposed_stage` is a suggestion awaiting",
                "confirmation, not a tag. Rename the key to `stage` to confirm:"]
        out += ["- %s" % u for u in untagged]
    write(os.path.join(REG_DIR, "library-index.md"), out)

    present = sum(1 for e in entries if e[1] is not None)
    total_bytes = sum(e[1] for e in entries if e[1] is not None)
    print("  library: %d source(s) recorded, %d present in this working copy (%.1f MB)"
          % (len(entries), present, total_bytes / 1048576.0))
    if missing:
        print("  library: %d source(s) WITHOUT a sidecar, not citable" % len(missing))


if __name__ == "__main__":
    main()
