# Skill Anatomy

How to write a skill that actually works.

## What is a skill?

A skill is a **reusable prompt** that encodes domain knowledge. It turns a generic LLM into a specialist for a specific task.

**Not a skill:**
- Generic instructions ("be helpful")
- One-off prompts
- System prompts (those are steering)

**Is a skill:**
- Code review with AppSec lenses
- Incident triage with structured output
- Spec writing with approval gates

## Required sections

Every skill needs four sections:

### 1. When to use

Trigger conditions. Be specific.

```markdown
## When to use

- Reviewing pull requests before merge
- Security audit of code changes
- NOT for: architecture review (use spec-driven instead)
```

**Why it matters:** Agents need to know when to load a skill. Vague triggers = wrong skill = bad output.

### 2. Context needed

What the skill needs to work.

```markdown
## Context needed

- The PR diff (files changed)
- Repository coding standards (if any)
- Recent related incidents (if security review)
```

**Why it matters:** Skills without context hallucinate. List exactly what to gather first.

### 3. Output format

What the skill produces.

```markdown
## Output format

Structured review with:
1. Summary: one-line verdict
2. Security: findings with path:line
3. Suggestions: actionable improvements
```

**Why it matters:** Consistent output = predictable automation. You can parse it, route it, act on it.

### 4. Prompt

The actual instructions.

```markdown
## Prompt

You are reviewing a pull request. Apply these lenses:

### Security
- Check for auth bypasses
- Look for injection points
...
```

**Why it matters:** This is the skill. Everything else is metadata.

## Optional sections

### Examples

Show input → output. Real examples beat abstract rules.

```markdown
## Example

**Input**: PR adding user deletion endpoint

**Output**:
Summary: Request changes - missing auth check
Security: `UserController.php:45` - no authorization
```

### Anti-patterns

What to avoid.

```markdown
## Anti-patterns

- Don't flag style issues as security
- Don't approve without reading all files
```

### Related skills

When to use something else.

```markdown
## Related

- For architecture decisions: `spec-driven.md`
- For production issues: `incident-triage.md`
```

## Quality checklist

Before committing a skill:

- [ ] Trigger conditions are specific (not "when needed")
- [ ] Context list is complete (skill won't hallucinate)
- [ ] Output format is structured (can be parsed)
- [ ] Prompt has clear steps (not vague instructions)
- [ ] At least one example (shows expected output)
- [ ] No internal references (sanitized)

## File template

```markdown
# Skill Name

One-line description.

## When to use

- Specific trigger 1
- Specific trigger 2
- NOT for: anti-trigger

## Context needed

- Required context 1
- Required context 2

## Output format

Structured output with:
1. Section 1
2. Section 2

## Prompt

```
[The actual instructions]
```

## Example

**Input**: [description]

**Output**:
[expected output]
```

## Related

- [skills/](../skills/) — production skills using this format
