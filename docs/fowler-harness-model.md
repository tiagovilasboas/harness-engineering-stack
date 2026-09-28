# Fowler harness model (coding agents)

Reference: [Harness engineering for coding agent users](https://martinfowler.com/articles/harness-engineering.html) (Birgitta Böckeler, 2026).

This public kit implements the **user harness** around any model. Use this vocabulary in skills, `AGENTS.md`, examples, and CI.

## Composition

**Coding agent = model + harness**

- **Vendor harness:** IDE or product (system prompt, tools, orchestration).
- **User harness:** this repo, product `AGENTS.md`, tests, linters, review instructions, observability.

Changing the model does not replace the harness.

## Guia × sensor (both required)

| | Guia (feedforward) | Sensor (feedback) |
|---|-------------------|-------------------|
| **When** | Before generation | After generation; autocorrect before human |
| **Computational** | `AGENTS.md`, scripted pre-checks | Tests, lint, `validate` exit 1 |
| **Inferential** | Skills, steering prose | Review agents, review instructions |

Ship **only guia** or **only sensor** for a concern is incomplete.

## Axes

- **Maintainability** — structure, clarity, review lenses (`skills/code-review.md`).
- **Architecture fitness** — boundaries, dependencies, fitness functions where you have them.
- **Behaviour** — business rules, domain invariants (often KB + sensors).

Do not confuse PR review *questions* with Fowler harness *layers* (vendor / user / model).

## Outer harness

| Phase | Examples in this repo |
|-------|------------------------|
| Pre-merge | `examples/database-migration-checker`, product `AGENTS.md` |
| Loop until sensor passes | `examples/ralph-loop` |
| Knowledge contract | `examples/knowledge-base/AGENTS.md` + `validate` in CI |

## Map this repo

| Path | Typical role |
|------|----------------|
| `skills/` | Guia (inferential) |
| `guardrails/` | Guia + sensor contracts (evidence, write approval) |
| `examples/database-migration-checker` | Guia (skill text) + sensor (script exit 1) |
| `examples/ralph-loop` | Guia (plan file) + sensor (command) |
| `mcp/` | Tool boundary (vendor + user policy) |
| `memory/` | Guia for retrieval; not a sensor by itself |

For a private multi-harness install (Cursor/Kiro/Codex), see [agent-harness](https://github.com/tiagovilasboas/agent-harness) (`harness-core`).
