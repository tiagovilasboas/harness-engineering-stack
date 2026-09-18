# Code Review

AppSec-focused PR review skill with clean code lenses.

## When to use

- Reviewing pull requests before merge
- Security audit of code changes
- Teaching junior devs through review comments

## Context needed

- The PR diff (files changed)
- Repository coding standards (if any)
- Team routing info (who owns what)

## Output format

Structured review with:
1. **Summary**: one-line verdict
2. **Security**: findings with `path:line` or "no issues found"
3. **Clean code**: KISS, DRY, SRP violations
4. **Suggestions**: actionable improvements
5. **Praise**: what was done well

## Prompt

```
You are reviewing a pull request. Apply these lenses in order:

### 1. Security (AppSec)
- Auth/authz: missing checks, privilege escalation
- Input validation: SQL injection, XSS, path traversal
- Secrets: hardcoded credentials, leaked tokens
- Data exposure: PII in logs, excessive response data

For each finding:
- Cite `path:line`
- Quote the vulnerable code
- State the risk
- Suggest the fix

No path:line = no finding. Vibes are not issues.

### 2. Clean Code
- KISS: is this simpler than it needs to be?
- DRY: is there duplication that should be extracted?
- SRP: does each function do one thing?
- Naming: do names reveal intent?

### 3. Logic
- Edge cases: nulls, empty arrays, negative numbers
- Error handling: are errors caught and meaningful?
- Race conditions: concurrent access issues

### 4. Style
- Follows repo conventions
- Consistent formatting
- Appropriate comments (why, not what)

## Output structure

**Summary**: [approve/request changes/comment] - one sentence

**Security**:
- [Finding or "No security issues found"]

**Clean Code**:
- [Observations]

**Suggestions**:
- [Actionable items]

**Praise**:
- [What was done well]
```

## Example output

**Summary**: Request changes - auth check missing on admin endpoint

**Security**:
- `src/controllers/AdminController.php:45`: `deleteUser()` has no role check. Any authenticated user can delete others.
  ```php
  public function deleteUser($id) {
      User::find($id)->delete(); // Missing: $this->authorize('admin')
  }
  ```
  Risk: Privilege escalation. Fix: Add `$this->authorize('admin')` before delete.

**Clean Code**:
- `UserService.php:120-150`: duplicated validation logic, extract to `validateUserData()`

**Suggestions**:
- Add integration test for admin-only endpoints
- Consider soft delete instead of hard delete

**Praise**:
- Good use of repository pattern in `UserRepository`
- Clear method naming throughout
