# Kiro Minimal Setup

Minimal harness for a new project. Copy and customize.

## Usage

```bash
# Copy to your project
cp -r .kiro ~/your-project/

# Customize
# 1. Edit .kiro/steering/project-context.md with your stack
# 2. Add MCP servers to .kiro/settings/mcp.json
# 3. Add skills to .kiro/skills/ as needed
```

## What's included

| File | Purpose |
|------|---------|
| `.kiro/steering/project-context.md` | Stack, commands, conventions |
| `.kiro/settings/mcp.json` | MCP server configs |

## What to add

1. **Skills** — copy from `skills/` in the parent repo
2. **More MCP servers** — Jira, Sentry, database
3. **Hooks** — automation on file save, commit, etc.

## Structure after customization

```
.kiro/
├── steering/
│   ├── project-context.md    # Your stack
│   └── team-conventions.md   # Your team rules
├── settings/
│   └── mcp.json              # Your tools
├── skills/
│   └── code-review/
│       └── SKILL.md          # Your review skill
└── hooks/
    └── lint-on-save.json     # Your automation
```
