"""The Internet in One Word — make.fun bounty entry.

Writes exactly one word to /output/entry.txt: the single word that
best describes the whole internet. Pure Python stdlib, no dependencies,
fully deterministic: every run produces byte-identical output.
"""

import os

WORD = "Cookies"  # Every site on the internet begs you to accept cookies:
# the whole web runs on them, and the word itself is warm and funny.
# Short (7 chars), instantly readable, surprising, true of the internet
# as a whole rather than one app or one mood.


def _check_gate(word: str) -> None:
    """Enforce the bounty gate locally: 1-30 chars, not whitespace-only."""
    if not (1 <= len(word) <= 30):
        raise ValueError("entry must be 1-30 characters")
    if not word.strip():
        raise ValueError("entry must not be only whitespace")
    if " " in word:
        raise ValueError("entry must be a single word")


def main() -> None:
    _check_gate(WORD)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
