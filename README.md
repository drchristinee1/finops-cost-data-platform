# FinOps Cost Data Platform (RevealCostAI Architecture)

This project demonstrates how to design and operate a centralized cost and vendor data platform that consolidates usage and billing data across:

- AWS (CUR)
- GCP (Billing Export)
- Kubernetes (OpenCost / metrics)
- SaaS vendors (Snowflake, Datadog, etc.)
- AI providers (OpenAI, Anthropic)

into a **single, trusted source of truth**.

---

## 🎯 Objective

To transform fragmented cloud and vendor cost data into:

- Structured cost models
- Unit economics
- Ownership-driven insights
- Actionable workflows

---

## 🧠 Architecture Overview

Sources → Ingestion → Modeling → Storage → Action Layer

This platform is designed not just for visibility, but for **execution and accountability**.
```text
AWS CUR ─┐
GCP ─────┼──> Ingestion Layer ──> Cost Modeling ──> Data Warehouse ──> Action Layer (Jira)
K8s ─────┤
SaaS ────┘

## 🧠 Architecture Overview

```text
                ┌───────────────┐
                │  Cost Sources │
                │───────────────│
                │ AWS (CUR)     │
                │ GCP Billing   │
                │ Kubernetes    │
                │ SaaS Vendors  │
                │ AI Providers  │
                └───────┬───────┘
                        │
                        ▼
                ┌───────────────┐
                │  Ingestion    │
                │───────────────│
                │ S3 + Athena   │
                │ APIs          │
                │ ETL Pipelines │
                └───────┬───────┘
                        │
                        ▼
                ┌───────────────┐
                │ Cost Modeling │
                │───────────────│
                │ Unit Economics│
                │ Cost Drivers  │
                │ Allocation    │
                └───────┬───────┘
                        │
                        ▼
                ┌───────────────┐
                │ Data Platform │
                │───────────────│
                │ Warehouse     │
                │ (Snowflake)   │
                └───────┬───────┘
                        │
                        ▼
                ┌───────────────┐
                │ Action Layer  │
                │───────────────│
                │ Jira Tickets  │
                │ Ownership     │
                │ Alerts        │
                └───────────────┘

---

## 🔧 Core Capabilities

- Unified cost ingestion pipelines
- Cost driver and unit economics modeling
- Kubernetes cost allocation (shared + idle)
- Commitment strategy optimization (RIs, Savings Plans)
- Automated anomaly detection
- Jira-based action routing and ownership tracking
- AI-powered cost explanation layer

---

## 🧩 Platform Layers

### 1. Ingestion
Collects cost and usage data from multiple systems.

### 2. Modeling
Transforms raw data into cost drivers and business metrics.

### 3. Allocation
Distributes shared and platform costs across teams.

### 4. Action Layer
Routes insights into Jira for execution and tracking.

### 5. AI Layer
Explains anomalies and cost drivers in engineering terms.

---

## 🔗 Supporting Repositories

- reveal-finops-lab (cost ingestion + anomaly detection)
- driver-based-finops-modeling-engine (unit economics)
- Kubernetes-Economic-Attribution-Engine (allocation)
- claude-lambda-finops-agent (AI reasoning layer)

---

## 🚀 Outcome

This platform enables organizations to:

- Move from cost visibility → cost action
- Align engineering and finance
- Validate savings in actual billing data
- Build a scalable FinOps operating model
---
---

## 📊 Key FinOps Metrics

This platform is designed to support decision-making through measurable outcomes:

- Commitment Coverage %
- Commitment Utilization %
- Cost per Unit (API, user, transaction)
- Idle Resource %
- Anomaly Detection & Resolution Time
- Budget vs Forecast Variance

These metrics connect infrastructure cost directly to business performance and engineering behavior.

## 🧪 Examples

This repository includes sample artifacts demonstrating how the platform operates:

- **AWS CUR Query**  
  Example SQL used to aggregate cost data:  
  `examples/sample_cur_query.sql`

- **Anomaly → Jira Automation**  
  Python example that converts cost anomalies into Jira tickets:  
  `examples/anomaly_to_jira.py`