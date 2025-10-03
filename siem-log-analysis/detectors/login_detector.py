def detect_failed_logins(parsed_logs, threshold=2):
    from collections import defaultdict
    failed_attempts = defaultdict(int)
    alerts = []

    for log in parsed_logs:
        msg = log["message"]
        if "Failed password" in msg:
            ip = msg.split("from")[1].split()[0]
            failed_attempts[ip] += 1
            if failed_attempts[ip] == threshold:
                alerts.append(f"Brute-force suspected from IP: {ip}")

    return alerts
