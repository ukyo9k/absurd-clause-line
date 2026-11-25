#!/usr/bin/env python3
"""Entry for The Absurd Clause Contest (make.fun).

Writes one absurd terms-of-service clause to ``entry.txt`` inside
``$MAKEFUN_OUTPUT_DIR`` (default ``/output/entry.txt``), then reads the
file back and verifies the round-trip is byte-identical, so the entry
on disk is exactly the clause defined below.

Standard library only; no network access.
"""

import os
import sys

# The clause: deadpan legal boilerplate with a quiet absurd twist.
# 188 characters, one line, no trailing newline.
CLAUSE = (
    "Section 14.2: All disputes arising under these Terms shall be "
    "settled by binding arbitration before a panel of three (3) pigeons, "
    "whose decision is final, binding, and legally enforceable."
)

MAX_LENGTH = 200


def validate(clause: str) -> list[str]:
    """Return a list of guard violations (empty when the clause is valid)."""
    problems: list[str] = []
    if not clause:
        problems.append("clause is empty")
    if "\n" in clause or "\r" in clause:
        problems.append("clause must be a single line")
    if clause != clause.strip():
        problems.append("clause has leading or trailing whitespace")
    if len(clause) > MAX_LENGTH:
        problems.append(
            f"clause is {len(clause)} characters, over the "
            f"{MAX_LENGTH}-character limit"
        )
    return problems


def main() -> int:
    problems = validate(CLAUSE)
    if problems:
        for problem in problems:
            print(f"error: {problem}", file=sys.stderr)
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")

    data = CLAUSE.encode("utf-8")
    with open(path, "wb") as handle:
        handle.write(data)

    with open(path, "rb") as handle:
        written = handle.read()

    if written != data:
        print("error: round-trip mismatch, entry.txt differs from clause",
              file=sys.stderr)
        return 1
    if written.endswith(b"\n"):
        print("error: entry.txt ends with a newline", file=sys.stderr)
        return 1

    print(f"wrote {len(written)} bytes ({len(CLAUSE)} chars) to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
