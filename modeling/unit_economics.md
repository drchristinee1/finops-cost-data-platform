# Cost Modeling & Unit Economics

## Overview

This layer transforms raw billing data into structured cost drivers, unit economics, and decision-ready metrics.

The goal is to translate infrastructure cost into business value.

---

## Core Models

### 1. Cost by Service / Team

- Aggregates cost across services (EC2, RDS, Lambda, etc.)
- Maps resources to teams and environments
- Enables ownership-based accountability

---

### 2. Unit Economics

Examples:

- Cost per API request
- Cost per user
- Cost per transaction

Formula:

Cost per Unit = Total Cost / Total Usage

---

### 3. Commitment Metrics

- Savings Plan / RI Coverage %
- Utilization %
- Effective vs On-Demand rate comparison

---

## Data Model (Conceptual)

Fact Table:

- date
- service
- account_id
- usage_quantity
- cost

Dimension Tables:

- resource → team, environment, owner
- service → pricing model
- time → day, month, quarter

---

## Key Design Principles

- Traceability (bill → workload → team)
- Consistency with Finance reporting
- Scalability across multi-cloud environments
- Alignment with engineering systems

---

## Outcome

This layer enables:

- Accurate forecasting
- Cost driver visibility
- Decision-making at engineering and executive levels