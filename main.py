#!/usr/bin/env python3
"""Office Artifacts: The One-Line Placard Contest — one-line museum placard entry.

The placard is assembled from three fragments and validated before it is
written: 1-180 characters, UTF-8, not only whitespace, no trailing newline.
"""

import os

MAX_CHARS = 180
MAX_WORDS = 35

# The placard, in three parts: the object, its date and material; the
# imagined ritual use; the deadpan donor note.
FRAGMENTS = [
    "Stapler, c. 1998. Steel and spring.",
    "A ritual press that wed two sheets with a single tooth;",
    "gift of the filing clerks, who believed no page should die alone.",
]

# Rejected drafts, kept as a record of what lost and why.
REJECTED = [
    # Microwave: "humming shrine" is a good misreading, but "ate standing
    # up" is a generic office joke, not a catalogue detail that sells the
    # artifact; the donor line does no work.
    "Microwave, c. 2009. A humming shrine where cold offerings were "
    "warmed for the midday rite. Donated by the night shift, who ate "
    "standing up.",
    # Lanyard: "one of the initiated" is a decent conceit, but the line
    # explains its own joke ("marking its wearer as...") instead of
    # letting the catalogue details carry it.
    "Lanyard, c. 2016. Woven cord of office, marking its wearer as one "
    "of the initiated. Bequeathed by Security, who knew every face by "
    "heart.",
]


def assemble(fragments):
    """Join the fragments into one single-line placard."""
    return " ".join(fragment.strip() for fragment in fragments)


def validate(text):
    """The gate: 1-180 characters, at most 35 words, UTF-8, one line."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} chars, got {len(text)}")
    if len(text.split()) > MAX_WORDS:
        raise ValueError(f"entry must be at most {MAX_WORDS} words")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")
    return text


def main():
    entry = validate(assemble(FRAGMENTS))
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
