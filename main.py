#!/usr/bin/env python3
"""Homework excuse, written by the dog's very literal brain.

A teacher writes "show your working" on the assignment. The dog reads
it as a direct order, not a metaphor, and carries it out to the letter
in the yard. Seven neat piles later, the dog is still convinced
it did a perfect job and is waiting to be thanked for it.

This program just writes that one-liner into entry.txt for the
bounty checker to read. Nothing is fetched, nothing is random.
"""

from pathlib import Path
import sys

LIMIT = 200


def choose_excuse():
    return (
        "The homework said 'show your working', so I did. "
        "It's in the backyard in seven piles. You're welcome."
    )


def check_text(text):
    if len(text) > LIMIT:
        print(
            "refusing: excuse runs to %d characters, limit is %d"
            % (len(text), LIMIT),
            file=sys.stderr,
        )
        return False
    if not text.strip():
        print("refusing: excuse came out blank", file=sys.stderr)
        return False
    return True


def save_text(text):
    import os

    folder = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "entry.txt").write_text(text, encoding="utf-8")


def run():
    text = choose_excuse()
    if not check_text(text):
        raise SystemExit(1)
    save_text(text)


if __name__ == "__main__":
    run()
