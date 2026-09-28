# AGENTS.md

Contract for coding agents working on this repository.

## What this repo is

A **reference stack** for harness engineering: skills, MCP configs, memory patterns, guardrails. Not a product, not an SDK, not runnable code.

## What to do

1. **Read first:** `README.md` → four layers (context, tools, memory, guardrails). For harness **design** work, also read `docs/fowler-harness-model.md` (guia/sensor, outer harness) and align examples with both loops.
2. **Respect structure:** skills go in `skills/`, MCP configs in `mcp/`, etc.
3. **Copy, don't fork:** users copy individual files to their projects, not the whole repo

## What NOT to do

- Do not generate application code: this is documentation and configuration
- Do not create new top-level directories without discussing
- Do not add dependencies: this repo has no `package.json` or build step
- Do not modify the architecture diagram without updating the explanation

## File conventions

| Directory | Format | Naming |
|-----------|--------|--------|
| `skills/` | Markdown | `kebab-case.md` |
| `mcp/` | JSON | `service-name.json` |
| `memory/` | Markdown | `pattern-name.md` |
| `guardrails/` | Markdown | `rule-name.md` |
| `docs/` | Markdown | `topic-name.md` |

## Skill structure

Every skill must have:

```markdown
# Skill Name

## When to use
## Context needed
## Output format
## Prompt
```

See `docs/skill-anatomy.md` for the full template.

## Pull request checklist

- [ ] File is in the correct directory
- [ ] Follows naming convention
- [ ] Has all required sections (for skills)
- [ ] README.md table updated (if adding a new skill)
- [ ] No broken links

## Questions?

Open an issue or ping [@tiagovilasboas](https://github.com/tiagovilasboas).
