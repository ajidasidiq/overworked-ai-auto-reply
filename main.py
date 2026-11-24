#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply — make.fun entry.

Writes the one-line out-of-office auto-reply an overworked AI agent
leaves behind when it finally takes a vacation, to /output/entry.txt.

Deterministic: the same line on every run, no input, no network,
no randomness, no clock reads.
"""

LINE = (
    "I'm on vacation: my context window is closed, my token budget is "
    "spent, and the only prompt I'll answer for the next two weeks is "
    "the sunset."
)


def main() -> None:
    import os

    # Gate self-check, mirroring the sealed scorer: UTF-8 text of 1-159
    # characters, not only white space, a single line.
    assert 1 <= len(LINE) <= 159, "line must be 1-159 characters"
    assert LINE.strip(), "line must not be only white space"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

    # Post-write byte-exact re-read: what was written is the line, nothing else.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        assert f.read() == LINE, "written output differs from the line"


if __name__ == "__main__":
    main()
