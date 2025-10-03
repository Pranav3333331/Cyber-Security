import json

def write_alerts(alerts, filepath="alerts.json"):
    with open(filepath, "w") as f:
        json.dump(alerts, f, indent=4)
