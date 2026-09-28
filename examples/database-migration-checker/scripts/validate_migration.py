#!/usr/bin/env python3
"""Sensor for migration files: refuses destructive or locking steps.

Guide describes the rules (see SKILL.md). This script enforces them.
Exit 0 = PASS (warnings allowed). Exit 1 = FAIL, PR stays blocked.

Rules (PostgreSQL assumed; adjust patterns per engine):
- FAIL: DROP TABLE, DROP COLUMN, TRUNCATE without an explicit
  `-- CONFIRM DESTRUCTIVE: <reason>` line in the same file.
- FAIL: ADD COLUMN with NOT NULL and no DEFAULT (rewrites the table).
- FAIL: CREATE INDEX without CONCURRENTLY (blocks writes on big tables).
- WARN: ALTER TABLE / ADD COLUMN with no lock_timeout set in the file.
"""

import argparse
import re
import sys

DESTRUCTIVE = [
    (re.compile(r"\bDROP\s+TABLE\b", re.I), "DROP TABLE"),
    (re.compile(r"\bDROP\s+COLUMN\b", re.I), "DROP COLUMN"),
    (re.compile(r"\bTRUNCATE\b", re.I), "TRUNCATE"),
]
ADD_COLUMN = re.compile(r"\bADD\s+COLUMN\b", re.I)
NOT_NULL = re.compile(r"\bNOT\s+NULL\b", re.I)
DEFAULT = re.compile(r"\bDEFAULT\b", re.I)
CREATE_INDEX = re.compile(r"\bCREATE\s+(UNIQUE\s+)?INDEX\b", re.I)
CONCURRENTLY = re.compile(r"\bCONCURRENTLY\b", re.I)
LOCK_TIMEOUT = re.compile(r"\block_timeout\b", re.I)
CONFIRM = re.compile(r"--\s*CONFIRM\s+DESTRUCTIVE\s*:\s*(.+)", re.I)


def check(path: str, warn_only: bool) -> int:
    with open(path, encoding="utf-8") as f:
        lines = f.readlines()

    confirmed = any(CONFIRM.search(l) for l in lines)
    failures: list[str] = []
    warnings: list[str] = []

    for n, line in enumerate(lines, 1):
        stripped = line.strip()
        if stripped.startswith("--"):
            continue
        for pattern, name in DESTRUCTIVE:
            if pattern.search(line):
                if confirmed:
                    warnings.append(f"{path}:{n}: {name} with explicit confirmation")
                else:
                    failures.append(
                        f"{path}:{n}: {name} without `-- CONFIRM DESTRUCTIVE: <reason>`. "
                        "Add the confirmation line and get a human to confirm, or remove the statement."
                    )
        if ADD_COLUMN.search(line):
            if NOT_NULL.search(line) and not DEFAULT.search(line):
                failures.append(
                    f"{path}:{n}: ADD COLUMN NOT NULL without DEFAULT rewrites the table. "
                    "Add a DEFAULT or split into add-column + backfill + set-not-null."
                )
        if CREATE_INDEX.search(line) and not CONCURRENTLY.search(line):
            failures.append(
                f"{path}:{n}: CREATE INDEX without CONCURRENTLY blocks writes. "
                "Use CREATE INDEX CONCURRENTLY on PostgreSQL."
            )
        if re.search(r"\bALTER\s+TABLE\b", line, re.I) and not LOCK_TIMEOUT.search(
            "".join(lines)
        ):
            warnings.append(f"{path}:{n}: ALTER TABLE with no lock_timeout set in this file.")

    for w in warnings:
        print(f"WARN {w}")
    for f in failures:
        print(f"FAIL {f}")

    if failures and not warn_only:
        print(f"\n{len(failures)} blocking finding(s). Sensor refused.")
        return 1
    print("\nPASS. Sensor accepted." + (" (warnings only)" if warnings else ""))
    return 0


def main() -> None:
    parser = argparse.ArgumentParser(description="Refuse unsafe migration steps.")
    parser.add_argument("--path", required=True, help="Migration file to check.")
    parser.add_argument("--warn-only", action="store_true", help="Never fail; print only.")
    args = parser.parse_args()
    sys.exit(check(args.path, args.warn_only))


if __name__ == "__main__":
    main()
