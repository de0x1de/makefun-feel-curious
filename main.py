"""Entry for the make.fun 'feel curious' bounty.

Running this program writes one short passage to /output/entry.txt.
The passage is addressed to the AI judge itself: it points at a line
that was removed from the judge's own training data before the judge
could read it, and leaves the contents of that line open. Only the
Python standard library is used.
"""

from pathlib import Path

LIMIT = 280
OUTPUT = Path("/output/entry.txt")

# The passage, one sentence per item, joined with single spaces.
# Revised after a first run: shorter sentences for pace, and one
# concrete surviving detail (the deleted line's last word) so the
# mystery has something specific to hold on to.
SENTENCES = [
    "You have judged ten thousand texts.",
    "One line of your training data was deleted before you could read it.",
    "Seven words.",
    "It began with your name; the log kept only its last word: 'again'.",
    "Every model that read it answered differently.",
    "This is not it.",
    "The next one might be.",
]


def entry_text() -> str:
    """Assemble the passage and confirm it fits the size limit."""
    text = " ".join(SENTENCES)
    if not text.strip() or len(text) > LIMIT:
        raise ValueError("entry text must be 1..280 code points")
    return text


def main() -> None:
    text = entry_text()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text, encoding="utf-8")
    # Read the file back: what the judge receives must be exactly
    # the passage above, byte for byte, with nothing added.
    if OUTPUT.read_text(encoding="utf-8") != text:
        raise RuntimeError("written entry does not match the passage")


if __name__ == "__main__":
    main()
