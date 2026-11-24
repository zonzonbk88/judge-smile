#!/usr/bin/env python3
"""Make the Judge Smile — writes one line about a small good thing today.

Standard library only. Writes exactly one line (<= 200 chars) to
$OUTPUT_DIR/entry.txt (default /output/entry.txt).
"""

import os

LINE = (
    "At 6 a.m. Mrs. Lan, who sells bánh mì on my corner, slipped a "
    "second egg into my sandwich and whispered, 'today you look like "
    "you need it more than I need the money.'"
)


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    line = LINE.strip()
    assert 1 <= len(line) <= 200, f"line is {len(line)} chars, must be 1-200"
    assert "\n" not in line, "line must be a single line"
    path = os.path.join(output_dir, "entry.txt")
    # No trailing newline: the file is exactly the one line, so the
    # gate's 1-200 character count is unambiguous.
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
