# Kubernetes Cost Allocation

## Overview

This layer allocates Kubernetes platform costs across teams, namespaces, and workloads.

Kubernetes cost is difficult because not every cost maps cleanly to one application. Shared clusters, idle capacity, and platform overhead must be allocated intentionally.

---

## Core Allocation Categories

- Direct workload cost
- Shared platform cost
- Idle capacity
- Storage cost
- Network / load balancer cost

---

## Allocation Logic

Costs can be mapped using:

- Namespace
- Labels
- CPU requests
- Memory requests
- Actual usage
- Team ownership metadata

---

## Outcome

This layer helps engineering teams understand the cost of the workloads they operate and supports showback / chargeback reporting.