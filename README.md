# Harness Engineer Stack

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![DEV.to](https://img.shields.io/badge/DEV.to-Article-black?logo=devdotto)](https://dev.to/tiagovilasboas/harness-engineering-o-dev-que-nao-conhece-vai-ficar-pra-tras-3h1n)

Professional harness stack for AI-assisted development. Skills, MCP servers, memory architecture, and HITL guardrails.

**Maintainer:** [Tiago Montanha](https://github.com/tiagovilasboas) · Staff · Agentic AI · AppSec

---

## What is a Harness Engineer?

A harness engineer builds the **infrastructure around the model**, not the model itself:

| Layer | What it does | You own |
|-------|--------------|---------|
| **Context** | What the model sees | Skills, steering, RAG |
| **Tools** | What the model can do | MCP servers, permissions |
| **Memory** | What persists across sessions | Logseq, vector stores |
| **Guardrails** | What the model cannot do | HITL, audit, sandbox |

The model is a commodity. The harness is the moat.

---

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        HARNESS                              │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐        │
│  │ Context │  │  Tools  │  │ Memory  │  │  Guard  │        │
│  │ skills/ │  │  mcp/   │  │ memory/ │  │ guard/  │        │
│  └────┬────┘  └────┬────┘  └────┬────┘  └────┬────┘        │
│       │            │            │            │              │
│       └────────────┴─────┬──────┴────────────┘              │
│                          │                                  │
│                    ┌─────▼─────┐                            │
│                    │   MODEL   │                            │
│                    │ (any LLM) │                            │
│                    └───────────┘                            │
└─────────────────────────────────────────────────────────────┘
```

---

## Quick Start

```bash
# Clone
git clone https://github.com/tiagovilasboas/harness-engineer-stack.git
cd harness-engineer-stack

# See the stack
tree -L 2

# Copy a skill to your project
cp skills/code-review.md ~/.kiro/skills/
```

---

## Layout

```
harness-engineer-stack/
├── skills/              # Reusable prompts for specific tasks
│   ├── code-review.md       # PR review with AppSec lenses
│   ├── incident-triage.md   # Production incident analysis
│   └── spec-driven.md       # Requirements → design → tasks
├── mcp/                 # MCP server configurations
│   ├── jira-atlassian.json  # Jira + Confluence
│   ├── sentry.json          # Error tracking
│   └── mysql-readonly.json  # Database queries (RO)
├── memory/              # Memory architecture patterns
│   ├── logseq-hub.md        # Hub-first knowledge base
│   └── rag-contract.md      # What goes where
├── guardrails/          # HITL and safety patterns
│   ├── evidence-required.md # No path:line = no issue
│   └── write-approval.md    # Human approval on writes
├── examples/            # Working examples
│   └── kiro-setup/          # Minimal Kiro harness
├── docs/                # Deep dives
│   ├── why-harness.md       # The case for harness engineering
│   └── skill-anatomy.md     # How to write a good skill
├── AGENTS.md            # Contract for coding agents
├── CONTRIBUTING.md      # How to add skills/patterns
└── LICENSE              # MIT
```

---

## Skills

Skills are **reusable prompts** that encode domain knowledge. They turn a generic LLM into a specialist.

| Skill | Use when |
|-------|----------|
| [`code-review.md`](skills/code-review.md) | Reviewing PRs with security lenses |
| [`incident-triage.md`](skills/incident-triage.md) | Analyzing production incidents |
| [`spec-driven.md`](skills/spec-driven.md) | Building features with requirements first |

**Anatomy of a skill:**

```markdown
# Skill Name

## When to use
- Trigger conditions

## Context needed
- Files to read first

## Output format
- What the skill produces

## Prompt
[The actual instructions]
```

See [`docs/skill-anatomy.md`](docs/skill-anatomy.md) for the full guide.

---

## MCP Servers

MCP (Model Context Protocol) gives models **typed access to external systems**.

| Server | Access | Use case |
|--------|--------|----------|
| [Jira/Confluence](mcp/jira-atlassian.json) | Read/Write | Issue tracking, documentation |
| [Sentry](mcp/sentry.json) | Read | Error analysis, stack traces |
| [MySQL](mcp/mysql-readonly.json) | Read-only | Database queries for investigation |

**Setup:**

```bash
# Copy to your harness config
cp mcp/*.json ~/.kiro/settings/

# Or merge into existing mcp.json
cat mcp/sentry.json >> ~/.kiro/settings/mcp.json
```

---

## Memory Architecture

Memory is what **persists across sessions**. Without it, every conversation starts from zero.

### Hub-first pattern

```
~/Logseq/rag-kb/
├── pages/
│   ├── ops/_hub.md          # Operations knowledge
│   ├── carreira/_hub.md     # Career/growth
│   └── meta/rag-contract.md # What goes where
└── journals/                # Daily logs
```

**Rule:** Always check the hub before answering. Cite `[[scope/page]]` in responses.

See [`memory/logseq-hub.md`](memory/logseq-hub.md) for the full pattern.

---

## Guardrails

Guardrails define **what the model cannot do** without human approval.

### Evidence-required

No `path:line` citation = no security issue opened. Vibes are not findings.

```markdown
## Evidence contract

Every finding must have:
- [ ] File path
- [ ] Line number
- [ ] Code snippet
- [ ] Requirement violated (OWASP, CWE, company policy)

Without all four, the finding is a hypothesis, not an issue.
```

### Write-approval

Destructive operations require explicit human confirmation:

- `git push --force`
- `DROP TABLE`
- Production deploys
- Bulk deletes

See [`guardrails/write-approval.md`](guardrails/write-approval.md).

---

## Examples

### Minimal Kiro setup

```bash
cd examples/kiro-setup
tree
```

```
kiro-setup/
├── .kiro/
│   ├── steering/
│   │   └── project-context.md
│   ├── skills/
│   │   └── code-review/
│   │       └── SKILL.md
│   └── settings/
│       └── mcp.json
└── README.md
```

Copy to a new project:

```bash
cp -r examples/kiro-setup/.kiro ~/my-project/
```

---

## Related

This repo is the **harness stack**. Siblings are scoped kits:

| Repo | Focus |
|------|-------|
| [jarvis-architecture](https://github.com/tiagovilasboas/jarvis-architecture) | Multi-agent runtime (brain · workers · ops) |
| [agentic-code-review](https://github.com/tiagovilasboas/agentic-code-review) | AppSec PR review (skills, runbooks) |
| [kiro-playbook](https://github.com/tiagovilasboas/kiro-playbook) | Kiro-specific steerings and hooks |
| [awesome-agentic-ai](https://github.com/tiagovilasboas/awesome-agentic-ai) | Curated links with Staff criteria |

---

## From the article

This repo materializes the concepts from [Harness Engineering: o dev que não conhece vai ficar pra trás?](https://dev.to/tiagovilasboas/harness-engineering-o-dev-que-nao-conhece-vai-ficar-pra-tras-3h1n).

**TL;DR from the article:**

> O modelo é commodity. O harness é o moat.
>
> Harness Engineering é arquitetura antes do código: contexto, ferramentas, permissões e auditoria ao redor do modelo.

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to add skills, MCP configs, or patterns.

**Agent notes:** [AGENTS.md](AGENTS.md)

---

## License

MIT. See [LICENSE](LICENSE).
