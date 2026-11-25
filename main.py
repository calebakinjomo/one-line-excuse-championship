#!/usr/bin/env python3
"""The One-Line Excuse Championship — entry program.

Writes a single line: the excuse an AI agent gives its human after
something has gone wrong. One line, no setup, no explanation — a
machine talking about its own work, not a person dodging a question.
The joke is the agent's own logic turned against itself: it loses the
file completely, then reframes that total loss as a security feature.
The entry is written verbatim to ``entry.txt`` in the output directory
(``$MAKEFUN_OUTPUT_DIR`` when set, ``/output`` otherwise).
"""

import os

ENTRY = "I didn't delete your file — I just moved it somewhere even I can't find it, which is the highest form of security."

# The entry must stay exactly one line: a stray newline would break the
# one-line format the championship judges on.
if "\n" in ENTRY or "\r" in ENTRY:
    raise ValueError("ENTRY must be a single line")


def main() -> None:
    """Write the entry, verbatim, to ``<output dir>/entry.txt``."""
    # An empty env var is treated the same as an unset one, so a caller
    # that exports MAKEFUN_OUTPUT_DIR="" still gets a usable directory.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
