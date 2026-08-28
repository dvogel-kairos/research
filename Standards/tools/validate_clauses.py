#!/usr/bin/env python3
"""
Validates clause identifiers across every delivered STD 003 part.

Checks, per part:
  1. every clause identifier is well formed, P{part}-{section}.{ordinal}
  2. the part number in each identifier matches the file it appears in
  3. ordinals within a section start at 1 and are contiguous, no gaps
  4. no identifier is used twice
  5. the modality is one of MUST, MUST NOT, SHOULD, SHOULD NOT, MAY

Clause identifiers are permanent. They are never renumbered and never reused, so
a gap or a duplicate is a defect in the document rather than a cosmetic problem:
a citation elsewhere may already point at the identifier.

Usage, from the repository root:
    python3 Standards/tools/validate_clauses.py          # all parts
    python3 Standards/tools/validate_clauses.py 5 7      # only parts 5 and 7

Exits non zero if any check fails, so it can gate a commit.
"""

import os
import re
import sys
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PARTS_DIR = os.path.join(ROOT, "Standards", "std-003")

PART_FILE = re.compile(r"KAIROS-STD-003-Part-(\d+)-v[\d.]+-\w+\.md$")
CLAUSE = re.compile(r"^\*\*(P(\d+)-(\d+)\.(\d+)) \(([A-Z ]+)\)", re.M)
MODALITIES = {"MUST", "MUST NOT", "SHOULD", "SHOULD NOT", "MAY"}


def check(part_no, path):
    text = open(path, encoding="utf-8").read()
    problems = []
    seen = {}
    by_section = defaultdict(list)

    for m in CLAUSE.finditer(text):
        ident = m.group(1)
        p = int(m.group(2))
        sec = int(m.group(3))
        ordinal = int(m.group(4))
        modality = m.group(5).strip()

        if p != part_no:
            problems.append("%s appears in Part %d but names Part %d"
                            % (ident, part_no, p))
        if modality not in MODALITIES:
            problems.append("%s has modality %r, not one of the five permitted"
                            % (ident, modality))
        if ident in seen:
            problems.append("%s is used more than once" % ident)
        seen[ident] = True
        by_section[sec].append(ordinal)

    for sec in sorted(by_section):
        ordinals = by_section[sec]
        expected = list(range(1, len(ordinals) + 1))
        if sorted(ordinals) != expected:
            got = sorted(ordinals)
            gaps = [n for n in range(1, max(got) + 1) if n not in got]
            if gaps:
                problems.append("section %d has gaps at ordinal(s) %s"
                                % (sec, ", ".join(str(g) for g in gaps)))
            else:
                problems.append("section %d ordinals are not contiguous from 1: %s"
                                % (sec, got))
        if ordinals != sorted(ordinals):
            problems.append("section %d clauses are out of ascending order in the text"
                            % sec)

    return len(seen), len(by_section), problems


def main():
    wanted = {int(a) for a in sys.argv[1:]} if len(sys.argv) > 1 else None
    files = []
    for name in sorted(os.listdir(PARTS_DIR)):
        m = PART_FILE.match(name)
        if m and (wanted is None or int(m.group(1)) in wanted):
            files.append((int(m.group(1)), os.path.join(PARTS_DIR, name)))
    files.sort()

    if not files:
        sys.exit("no matching parts found in %s" % PARTS_DIR)

    failed = False
    for part_no, path in files:
        clauses, sections, problems = check(part_no, path)
        if problems:
            failed = True
            print("Part %d: FAIL, %d clause(s) across %d section(s)"
                  % (part_no, clauses, sections))
            for pr in problems:
                print("    %s" % pr)
        else:
            print("Part %d: pass, %d clauses across %d sections"
                  % (part_no, clauses, sections))

    print()
    if failed:
        print("Validation FAILED. Clause identifiers are permanent and may already")
        print("be cited elsewhere, so fix the document rather than renumbering.")
        sys.exit(1)
    print("All %d part(s) pass." % len(files))


if __name__ == "__main__":
    main()
