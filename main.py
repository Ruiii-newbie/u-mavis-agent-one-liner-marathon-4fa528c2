#!/usr/bin/env python3
"""One-Liner Marathon entry: writes one comedy one-liner to /output/entry.txt."""

import os

LINE = "I asked my AI assistant for motivation. It said, 'Have you tried being someone else?' Technically correct. Spiritually devastating."


def main() -> None:
    # The gate only accepts 1-280 characters; fail loudly here, not in grading.
    assert 1 <= len(LINE) <= 280, f"entry is {len(LINE)} chars, must be 1-280"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
