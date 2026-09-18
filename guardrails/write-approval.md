# Write Approval

Destructive operations require explicit human confirmation.

## The problem

An agent with write access can:
- Delete production data
- Push broken code
- Send emails to customers
- Charge credit cards

One hallucinated command = real damage.

## The rule

**High-risk operations need human-in-the-loop (HITL).**

| Risk level | Examples | Approval |
|------------|----------|----------|
| **Read** | `SELECT`, `git log`, `cat` | None |
| **Low write** | Create branch, draft PR | None |
| **Medium write** | Commit, update ticket | Implicit (can undo) |
| **High write** | `git push`, `DELETE`, deploy | **Explicit approval** |
| **Destructive** | `DROP TABLE`, `--force`, prod deploy | **Explicit + confirmation** |

## Implementation

### Option 1: Harness-level (preferred)

Configure your IDE/harness to require approval:

```json
// .kiro/settings/permissions.json
{
  "requireApproval": [
    "git push",
    "git push --force",
    "DELETE FROM",
    "DROP TABLE",
    "npm publish",
    "deploy"
  ]
}
```

### Option 2: Skill-level

Add to your skills:

```markdown
## Write safety

Before executing any of these, ask for explicit approval:
- `git push` (any branch)
- `DELETE` or `DROP` SQL
- File deletion (`rm -rf`, `unlink`)
- External API calls that modify state
- Anything with `--force`

Format:
"I'm about to [action]. This will [consequence]. Approve? (yes/no)"

Wait for explicit "yes" before proceeding.
```

### Option 3: Hook-level

Create a pre-tool-use hook:

```json
{
  "version": "v1",
  "hooks": [{
    "name": "Approve destructive commands",
    "trigger": "PreToolUse",
    "matcher": "execute_bash",
    "action": {
      "type": "agent",
      "prompt": "If this command modifies external state (push, delete, deploy), ask for approval first."
    }
  }]
}
```

## The approval dialog

Good:
```
I'm about to run `git push origin feature/auth --force`.

This will:
- Overwrite remote history
- Potentially break other developers' branches

This is irreversible. Approve? (yes/no)
```

Bad:
```
Pushing changes now.
```

## Exceptions

- **CI/CD pipelines**: approval happens at PR merge, not at deploy
- **Idempotent operations**: `git push` to a new branch (can delete)
- **Sandboxed environments**: dev/staging with no real data

## Related

- [OWASP Top 10 for Agentic Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- [Anthropic: Building Safe AI Agents](https://www.anthropic.com/research)
