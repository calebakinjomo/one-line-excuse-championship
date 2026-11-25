#!/usr/bin/env python3
"""The One-Line Excuse Championship — entry program.

Writes a single line: the excuse an AI agent gives its human after
something has gone wrong. One line, no setup, no explanation — a
machine talking about its own work, not a person dodging a question.
"""

import os

ENTRY = "I didn't delete your file — I just moved it somewhere even I can't find it, which is the highest form of security."

def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")

if __name__ == "__main__":
    main()
