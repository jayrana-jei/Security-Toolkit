def count_failed_log(logs):
    count = 0

    for log in logs:
        if log["status"] == "failed":
            count += 1
    return count



def get_failed_ips(logs):
    failed_ips = []
    for log in logs:
        if log["status"] == "failed":
            failed_ips.append(log["ip"])
    return failed_ips
