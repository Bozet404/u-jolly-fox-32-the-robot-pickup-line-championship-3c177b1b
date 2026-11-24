"""The Robot Pickup Line Championship entry.

A tiny program that writes one robot-voiced pickup line to
/output/entry.txt. The line is a single line of plain UTF-8 text,
well under the 200-character limit.
"""

import os

LINE = (
    "I scanned a thousand faces today and my sensors only "
    "overheated for you, so can I be your favourite system update?"
)

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main() -> None:
    line = LINE.strip()
    assert 1 <= len(line) <= 200, "line must be 1-200 characters"
    assert "\n" not in line, "line must be a single line"
    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
