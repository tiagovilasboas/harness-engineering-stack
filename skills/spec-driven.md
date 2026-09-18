# Spec-Driven Development

Requirements → design → tasks before implementation. For features that need alignment before code.

## When to use

- New feature with unclear scope
- Cross-team or cross-domain work
- Refactoring with business impact
- Anything that needs stakeholder sign-off

## Context needed

- Business request (Slack, Jira epic, meeting notes)
- Existing system context (architecture, constraints)
- Stakeholders list (who approves what)

## Output format

Three-phase spec:
1. **Requirements**: what we're building and why
2. **Design**: how we're building it
3. **Tasks**: implementation breakdown

## Prompt

```
You are writing a spec for a feature. Follow this three-phase approach:

### Phase 1: Requirements

Answer these questions:
1. **Problem**: What user pain are we solving?
2. **Goal**: What does success look like? (metric if possible)
3. **Scope**: What's in? What's explicitly out?
4. **Constraints**: Technical, business, timeline limits
5. **Stakeholders**: Who needs to approve?

Output a Requirements doc with these sections.

### Phase 2: Design

After requirements are approved:
1. **Approach**: High-level solution (1-2 paragraphs)
2. **Architecture**: Components involved, data flow
3. **API changes**: New endpoints, modified contracts
4. **Database changes**: Schema additions/modifications
5. **Trade-offs**: What we're choosing and why
6. **Risks**: What could go wrong, mitigation

Output a Design doc with these sections.

### Phase 3: Tasks

After design is approved:
1. Break into implementable chunks (2-8 hours each)
2. Order by dependency (what blocks what)
3. Mark parallel work (what can be done simultaneously)
4. Identify review gates (where to pause for feedback)

Output a Task list in this format:

| # | Task | Estimate | Depends on | Parallel |
|---|------|----------|------------|----------|
| 1 | ... | 4h | - | - |
| 2 | ... | 2h | 1 | - |
| 3 | ... | 3h | - | with 2 |

## Transitions

- Requirements → Design: only after stakeholder approval
- Design → Tasks: only after technical review
- Tasks → Implementation: only after task review

Do not skip phases. Do not start coding before Tasks are reviewed.
```

## Example: Requirements phase

**Feature**: PIX payment for subscriptions

### Problem
Subscribers can only pay with credit card. PIX has lower fees and some users prefer it.

### Goal
- 20% of new subscriptions use PIX within 3 months
- Reduce payment failure rate by 5%

### Scope
**In**:
- PIX as payment option for new subscriptions
- PIX QR code generation
- Payment confirmation via webhook

**Out**:
- PIX for existing subscriptions (migration later)
- PIX for one-time purchases (different flow)

### Constraints
- Must use existing Pagarme integration
- Cannot change subscription billing date logic
- Launch before Black Friday (8 weeks)

### Stakeholders
- Product: @maria (requirements approval)
- Engineering: @tiago (design approval)
- Finance: @carlos (fee structure approval)
