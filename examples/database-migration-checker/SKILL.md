# Database Migration Checker

## When to use

- A new migration file appears in a PR (`migrations/`, `prisma/migrations/`, `db/migrate/`)
- Someone mentions migration, schema or DDL
- Before merging anything that alters tables, columns or indexes

## Context needed

- The migration file path
- Which database it targets (rules below assume PostgreSQL; adjust per engine)
- The PR diff, to confirm the file is the whole change

## Output format

- `PASS`: no blocking finding. Warnings listed, if any.
- `FAIL`: one blocking finding per line, each with `file:line`, the rule and the fix.
- Destructive statements without explicit confirmation always FAIL.

## Prompt

1. Locate the migration files in the diff.
2. Run the sensor script. It refuses, you describe:

```bash
python3 examples/database-migration-checker/scripts/validate_migration.py --path <migration_file>
```

3. Enforce the sensor output. Script FAIL = PR blocked until the file changes.
4. Warnings (lock timeout) become review comments, not blocks.
5. Never approve a destructive statement (`DROP TABLE`, `DROP COLUMN`, `TRUNCATE`) without a `-- CONFIRM DESTRUCTIVE: <reason>` line in the file and a human confirming it.

## Guide vs sensor

This text is the guide: it enters before generation. The script is the sensor: it runs after and refuses the step. A skill that only describes the checks without running them is still a guide. Whoever stops the destructive merge is the sensor, not a bigger model.
