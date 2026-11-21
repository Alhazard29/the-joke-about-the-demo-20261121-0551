#!/usr/bin/env python3
"""Write a one-line joke about working beside AI coding agents.

The joke is written to /output/entry.txt as UTF-8 text: one line,
122 characters, no trailing newline.
"""

import os

JOKE = (
    "My AI agent aced every rehearsal \u2014 then went live, found a bug "
    "that didn't exist, fixed it, and broke everything that did."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
