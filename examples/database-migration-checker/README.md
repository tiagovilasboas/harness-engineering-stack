# database-migration-checker

Working example of a skill that executes: the text (`SKILL.md`) is the guide, the script is the sensor.

## Run

```bash
# PASS: backfill-safe column, concurrent index, lock timeout set
python3 scripts/validate_migration.py --path fixtures/good.sql

# FAIL: NOT NULL without DEFAULT, plain CREATE INDEX, DROP without confirmation
python3 scripts/validate_migration.py --path fixtures/bad.sql
```

Expected: `good.sql` prints `PASS`. `bad.sql` prints 3 `FAIL` lines and exits 1.

## What stops the merge

The script exit code. Wire it as a pre-commit hook or a CI step: non-zero keeps the PR blocked until the file changes. A bigger model does not replace this. The sensor refuses; the model describes.
