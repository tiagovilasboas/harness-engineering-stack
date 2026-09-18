# Evidence Required

No `path:line` citation = no security issue opened.

## The problem

LLMs hallucinate findings. Without evidence, you get:
- False positives that waste reviewer time
- Vague "concerns" that can't be acted on
- Security theater instead of security

## The rule

Every security finding must have:

| Required | Example |
|----------|---------|
| File path | `src/controllers/UserController.php` |
| Line number | `:45` |
| Code snippet | The actual vulnerable code |
| Requirement | OWASP A01, CWE-89, company policy |

**All four or it's a hypothesis, not a finding.**

## Implementation

Add to your review skill:

```markdown
## Evidence contract

For each security finding, you MUST provide:
1. `path:line` - exact location
2. Code snippet - the vulnerable code
3. Risk statement - what can go wrong
4. Requirement - which standard it violates

If you cannot provide all four, state it as a hypothesis:
"Potential issue (needs verification): [description]"

Do not open issues for hypotheses.
```

## Examples

### ✅ Valid finding

```
**Finding**: SQL Injection in user lookup

**Location**: `src/repositories/UserRepository.php:67`

**Code**:
```php
$query = "SELECT * FROM users WHERE id = " . $id;
```

**Risk**: Attacker can extract or modify database contents.

**Requirement**: OWASP A03:2021 - Injection, CWE-89
```

### ❌ Invalid (no evidence)

```
**Finding**: The authentication might be vulnerable

There could be issues with how tokens are validated.
Consider reviewing the auth module.
```

This is a vibe, not a finding. Do not open an issue.

## Exceptions

- **Threat modeling**: hypotheses are expected, label them clearly
- **Architecture review**: systemic issues don't have line numbers
- **Compliance audit**: policy gaps reference documents, not code

## Related

- [agentic-code-review](https://github.com/tiagovilasboas/agentic-code-review) — full AppSec review kit
- OWASP [Secure Agent Playbook](https://owasp.org/www-project-secure-agent-playbook/)
