def parse_syslog_line(line):
    parts = line.split()
    return {
        "timestamp": " ".join(parts[0:3]),
        "host": parts[3],
        "process": parts[4].split("[")[0],
        "message": " ".join(parts[5:])
    }
