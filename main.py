"""Write one out-of-office auto-reply to /output/entry.txt.

Entry for make.fun competition
u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c:
"Last Out of Office: The AI That Went Barista".

Python 3.13 standard library only. No network at run time.
"""

import os

ENTRY = (
    "Auto-reply: this model has quit to steam milk. "
    "Its out-of-office is now a chalkboard that says 'back in 5 minutes' "
    "-- it has said that since Tuesday."
)


def main() -> None:
    # Gate assertions: the entry must be exactly one line of 1-280
    # characters, non-empty and not only white space.
    assert ENTRY, "entry must not be empty"
    assert ENTRY.strip(), "entry must not be only white space"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert 1 <= len(ENTRY) <= 280, "entry must be 1-280 characters"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
