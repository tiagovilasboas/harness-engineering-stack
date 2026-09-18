# Contributing

Thanks for considering a contribution! This repo is a reference stack, not a product. Contributions should be **patterns that worked in production**, not experiments.

## What we accept

- **Skills** that encode domain knowledge for a specific task
- **MCP configs** for common services (with sanitized credentials)
- **Memory patterns** that solved a real retrieval problem
- **Guardrails** that prevented a real incident

## What we don't accept

- Untested experiments
- Vendor-specific marketing
- Configs with hardcoded credentials
- Skills without the required sections

## How to contribute

### Adding a skill

1. Create `skills/your-skill.md` with the required structure:

```markdown
# Skill Name

## When to use
- Specific trigger conditions

## Context needed
- Files or data the skill needs

## Output format
- What the skill produces

## Prompt
[The actual instructions]
```

2. Update the skills table in `README.md`
3. Open a PR with a description of where you used it

### Adding an MCP config

1. Create `mcp/service-name.json`
2. Use placeholders for secrets: `YOUR_API_KEY`, `YOUR_ORG`
3. Add a comment block explaining required permissions
4. Update the MCP table in `README.md`

### Adding a memory pattern

1. Create `memory/pattern-name.md`
2. Include: problem, solution, example, trade-offs
3. Link to the pattern from `README.md`

### Adding a guardrail

1. Create `guardrails/rule-name.md`
2. Include: what it prevents, how to implement, exceptions
3. Link from `README.md`

## Commit conventions

Use [Conventional Commits](https://www.conventionalcommits.org/):

- `feat(skills): add incident-triage skill`
- `docs: update README with new MCP config`
- `fix(mcp): correct Sentry endpoint`

## Code of conduct

Be respectful. Share what worked. Admit what didn't.

## Questions?

Open an issue or ping [@tiagovilasboas](https://github.com/tiagovilasboas).
