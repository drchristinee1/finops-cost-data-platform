"""
Minimal example: take an anomaly signal and create a Jira ticket.
(Replace placeholders with your values)
"""
import requests
from requests.auth import HTTPBasicAuth

JIRA_URL = "https://your-domain.atlassian.net"
EMAIL = "you@example.com"
API_TOKEN = "your_api_token"

def create_ticket(summary, description):
    url = f"{JIRA_URL}/rest/api/3/issue"
    headers = {"Accept": "application/json", "Content-Type": "application/json"}
    payload = {
        "fields": {
            "project": {"key": "FIN"},
            "summary": summary,
            "description": description,
            "issuetype": {"name": "Task"}
        }
    }
    r = requests.post(
        url,
        headers=headers,
        json=payload,
        auth=HTTPBasicAuth(EMAIL, API_TOKEN)
    )
    r.raise_for_status()
    return r.json()

if __name__ == "__main__":
    anomaly = {
        "service": "AWS Lambda",
        "change_pct": 42,
        "driver": "Invocation spike"
    }
    summary = f"[Cost Anomaly] {anomaly['service']} +{anomaly['change_pct']}%"
    description = (
        f"Detected anomaly in {anomaly['service']}.\n"
        f"Likely driver: {anomaly['driver']}.\n"
        f"Recommended action: review triggers and concurrency settings."
    )
    print(create_ticket(summary, description))