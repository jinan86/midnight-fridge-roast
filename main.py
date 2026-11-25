"""Midnight Fridge Roast — make.fun entry (program/v1).

Writes a single one-line roast of a smart fridge that refuses to open
after midnight to /output/entry.txt. Deterministic: the same line every run.

No randomness, no network, no clock: the output depends on nothing but
the ENTRY constant below.
"""

import os

# The entry: one line, <= 200 UTF-8 characters, no trailing newline.
ENTRY = (
    'My fridge locks at midnight, then texts the whole house: '
    '"Snack attempt logged at 00:03. Judgment pending."'
)

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def validate(text: str) -> None:
    """Gate: 1-200 characters, not only whitespace, single line."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
        )


def main() -> None:
    validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # No trailing newline: write the exact bytes of the line.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
