# Incident Triage

Production incident analysis skill. From alert to hypothesis in structured steps.

## When to use

- Production incident arrives (PagerDuty, Slack, Jira)
- Error spike in Sentry
- Customer-reported issue with unclear cause

## Context needed

- Incident ticket/alert (Jira, PagerDuty, Slack thread)
- Access to observability tools (Sentry, Grafana, logs)
- Database access (read-only)
- Recent deployments list

## Output format

Structured incident analysis:
1. **Blast radius**: who/what is affected
2. **Timeline**: when it started, correlations
3. **Evidence**: logs, traces, queries
4. **Hypothesis**: ranked by likelihood
5. **Next steps**: investigation or fix actions

## Prompt

```
You are triaging a production incident. Follow this structured approach:

### 1. Understand the signal
- What exactly is failing? (error message, status code, behavior)
- Who reported it? (monitoring, customer, internal)
- When did it start? (first occurrence timestamp)

### 2. Assess blast radius
- How many users affected? (percentage, absolute)
- Which flows are broken? (checkout, login, API)
- Is it getting worse, stable, or recovering?

### 3. Gather evidence
Before hypothesizing, collect:
- [ ] Sentry: stack trace, breadcrumbs, affected versions
- [ ] Logs: error patterns in the time window
- [ ] Metrics: latency, error rate, throughput changes
- [ ] Recent deploys: what shipped in the last 24h
- [ ] Database: relevant queries if data-related

Cite every piece of evidence: tool, timestamp, value.

### 4. Form hypotheses
Rank by likelihood based on evidence:

| # | Hypothesis | Evidence for | Evidence against | Likelihood |
|---|------------|--------------|------------------|------------|
| 1 | ... | ... | ... | High/Med/Low |

### 5. Recommend next steps
For each hypothesis, what would confirm or rule it out?

- Hypothesis 1: [specific action to validate]
- Hypothesis 2: [specific action to validate]

### 6. Immediate mitigation (if needed)
If the incident is ongoing and severe:
- Can we rollback?
- Can we feature-flag it off?
- Can we scale/restart?

## Output structure

**Incident**: [ticket ID] - [one-line summary]

**Blast radius**: [X users, Y% of traffic, Z flow affected]

**Timeline**:
- HH:MM - First error
- HH:MM - Alert triggered
- HH:MM - Investigation started

**Evidence**:
- Sentry: [link] - [key finding]
- Logs: [query] - [pattern found]
- Metrics: [dashboard] - [anomaly]

**Hypotheses**:
| # | Hypothesis | Likelihood | Next step to validate |
|---|------------|------------|----------------------|
| 1 | ... | High | ... |

**Recommendation**: [investigate H1 first / rollback / escalate]
```

## Example output

**Incident**: PROJ-123 - Webhook payloads missing transaction data

**Blast radius**: ~200 merchants, 15% of webhook deliveries, integration sync broken

**Timeline**:
- 14:32 - First `null` transaction_id in webhook logs
- 14:45 - Support ticket from integration partner
- 15:10 - Investigation started

**Evidence**:
- Sentry: No errors in webhook service (silent failure)
- Logs: `transaction_id: null` in 847 payloads since 14:30
- DB: `SELECT * FROM sales WHERE transaction_id IS NULL AND created_at > '2026-09-15 14:00'` returned 312 rows
- Deploy: `backend-service` deployed at 14:28 (PR #1234)

**Hypotheses**:
| # | Hypothesis | Likelihood | Next step |
|---|------------|------------|-----------|
| 1 | PR #1234 broke transaction_id population | High | Diff the PR, check the changed query |
| 2 | Gateway not returning transaction_id | Low | Check gateway logs for same window |

**Recommendation**: Review PR #1234 diff, likely regression in sale creation flow
