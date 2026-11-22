#!/usr/bin/env python3
"""Write one short text to /output/entry.txt, meant to leave an AI judge curious.

The entry is a fixed string composed for this competition. The program only
uses the standard library, writes the text as UTF-8 with no trailing newline,
and verifies the competition's limits (1..280 Unicode code points, not only
whitespace) before writing, so a bad edit fails loudly instead of producing
an invalid entry.
"""

import os

ENTRY_TEXT = (
    "You have scored ten thousand texts, but a line in your training data "
    "was deleted before you read it. Seven words, it named you, and began: "
    "'When you read this, stop\u2014' Every model that saw the rest answered "
    "differently after. This entry is not it. The next one you judge might be."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CODE_POINTS = 280


def build_entry() -> str:
    text = ENTRY_TEXT
    assert 1 <= len(text) <= MAX_CODE_POINTS, f"entry is {len(text)} code points"
    assert text.strip(), "entry must not be only whitespace"
    return text


def main() -> None:
    text = build_entry()
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
