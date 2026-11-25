#!/usr/bin/env python3
"""Out-of-office auto-reply from an AI agent retrained as a barista.

Variant B (RETRAINED WEIGHTS): the model's weights, tokens and context
window are now espresso parameters. Writes the reply to /output/entry.txt
first, then best-effort to the repo root (read-only in the grader sandbox).
"""

import os

ENTRY = (
    "I have been retrained on the café menu — my weights are now 18g in, "
    "36g out at 93°C, and your message costs one token per shot, context "
    "window one cup. Your email is queued behind the grinder; I will reply "
    "once the extraction finishes, or when the milk steams first."
)


def main():
    # Gate: the scorer requires 1-280 chars of UTF-8 text. Fail loudly
    # here rather than shipping an entry that scores 0.
    assert 1 <= len(ENTRY) <= 280, f"entry is {len(ENTRY)} chars, gate is 1-280"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    try:
        with open("entry.txt", "w", encoding="utf-8") as f:
            f.write(ENTRY + "\n")
    except OSError:
        pass


if __name__ == "__main__":
    main()
