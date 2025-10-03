from parsers.syslog_parser import parse_syslog_line
from detectors.login_detector import detect_failed_logins
from alerts.alert_writer import write_alerts

def read_logs(filepath):
    with open(filepath, "r") as f:
        return f.readlines()

if __name__ == "__main__":
    lines = read_logs("logs/sample_syslog.log")
    parsed_logs = [parse_syslog_line(line) for line in lines]
    alerts = detect_failed_logins(parsed_logs)
    write_alerts(alerts)
    print("Analysis complete. Alerts saved to alerts.json")
