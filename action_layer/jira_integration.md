# Action Layer (Jira Integration)

## Overview

This layer connects cost insights to engineering action.

Instead of stopping at dashboards, the platform drives accountability through workflow integration.

---

## Core Flow

1. Detect anomaly or cost signal
2. Classify (baseline, growth, inefficiency)
3. Translate into engineering context
4. Create Jira ticket
5. Assign ownership
6. Track resolution
7. Validate savings in billing data

---

## Example Use Case

- Spike in Lambda cost detected
- Root cause: increased invocation frequency
- Action: reduce unnecessary triggers / optimize logic
- Jira ticket created and assigned to service owner

---

## Key Features

- Automated ticket creation
- Ownership mapping (team, service)
- Status tracking (open → in progress → resolved)
- Feedback loop to validate outcomes

---

## Integration

- Jira API
- Python automation scripts
- Cost signals from ingestion + modeling layers

---

## Outcome

- Faster anomaly resolution
- Clear accountability
- Measurable cost savings

---

## FinOps Impact

This layer transforms:

Cost Data → Insight → Ownership → Action → Verified Savings