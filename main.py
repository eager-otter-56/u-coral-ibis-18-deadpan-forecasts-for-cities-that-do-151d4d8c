#!/usr/bin/env python3
"""Deadpan forecast for a city that does not exist.

Writes one line (max 160 chars) to entry.txt in MAKEFUN_OUTPUT_DIR.
"""

import os
import stat

ENTRY = (
    "In New Cacheford, expect 14°C and light approval-queue drizzle, "
    "3,214 pending requests pooling in the lowlands, all because I forgot "
    "to clear my own cache."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)


if __name__ == "__main__":
    main()
