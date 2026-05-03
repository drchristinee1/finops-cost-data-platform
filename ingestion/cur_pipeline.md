# Cost Data Ingestion (AWS CUR Pipeline)

## Overview

This layer is responsible for ingesting raw cost and usage data from cloud providers and external vendors into the FinOps data platform.

## AWS CUR Pipeline

- Source: AWS Cost and Usage Report (CUR)
- Storage: Amazon S3
- Query Layer: Amazon Athena
- Processing: Python (boto3)

## Pipeline Flow

1. AWS CUR data is delivered to S3 in hourly/daily partitions
2. Athena is used to query and structure cost data
3. Python scripts extract and transform data into standardized formats
4. Data is prepared for downstream modeling and allocation

## Key Considerations

- Data normalization across services and accounts
- Handling large-scale datasets (billions of rows)
- Partitioning for efficient querying
- Ensuring consistency with billing data

## Future Extensions

- GCP Billing Export ingestion (BigQuery)
- Kubernetes cost ingestion via OpenCost
- SaaS API ingestion (Snowflake, Datadog)