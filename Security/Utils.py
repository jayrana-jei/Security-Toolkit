def unique_ips(logs):
    return list({log["ip"] for log in logs})