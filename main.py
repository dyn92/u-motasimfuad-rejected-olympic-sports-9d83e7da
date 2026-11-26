#!/usr/bin/env python3
"""Rejected Olympic Sports — one-liner entry.

Prints exactly one line (the rejected sport) to stdout and writes the
same single line to /output/entry.txt, as the bounty requires.
Pure standard library, deterministic: no randomness, no time, no network.
"""

import os
import sys

ENTRY = (
    "Competitive apologising: two athletes collide, then keep saying "
    "sorry until one of them finally means it. Canada wins by forfeit."
)

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def self_check(line: str) -> None:
    """Fail loudly if the entry is not exactly one line of <=200 chars."""
    if not line or line != line.strip():
        raise ValueError("entry must be non-empty with no leading/trailing whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry is {len(line)} chars, over the {MAX_CHARS} limit")
    # The gate rejects whitespace-only entries, so require real content.
    if not any(ch.isalnum() for ch in line):
        raise ValueError("entry must contain at least one alphanumeric character")


def verify_written(path: str, line: str) -> None:
    """Re-read the written file and confirm it holds exactly the entry."""
    with open(path, "r", encoding="utf-8") as fh:
        written = fh.read()
    if written != line + "\n":
        raise ValueError("written entry.txt does not match the printed line")


def main() -> int:
    self_check(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(ENTRY + "\n")
    verify_written(OUTPUT_PATH, ENTRY)
    sys.stdout.write(ENTRY + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
