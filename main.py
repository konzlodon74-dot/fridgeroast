#!/usr/bin/env python3
"""Fridge Roast: One Line, Biggest Laugh.

Writes a single roast line about a smart fridge to /output/entry.txt.
No network, no dependencies, deterministic output.
"""

import os

ROAST = (
    "My smart fridge updated its firmware at 2 a.m., bricked the ice maker, "
    "then emailed me: 'Your ice is on strike. Please enjoy your water warm, "
    "like a peasant.'"
)


def main() -> None:
    line = ROAST.strip()
    assert line, "roast must not be empty"
    assert 1 <= len(line) <= 200, f"roast must be 1-200 chars, got {len(line)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
