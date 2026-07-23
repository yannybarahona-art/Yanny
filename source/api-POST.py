import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent / "dev api"))

from fake_api.resources.alerts import AlertsResource
from fake_api.config import APIConfig


def main():
    config = APIConfig()
    alerts = AlertsResource(config)
    payload = {
        "customer_id": 1001,
        "severity": "High",
        "status": "Open",
        "category": "Fraud"
    }
    response=create_post(payload, alerts)
    print_status(response)

def create_post(payload, alerts):
    response = alerts.create(payload)
    return response

def print_status(response):
    print("Status:", response.status_code)
    print("Data:", response.data)

if __name__ == "__main__":
    main()