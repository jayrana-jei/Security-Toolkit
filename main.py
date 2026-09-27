from Security import Validation, logs, Utils


logs_enteries = [
    {"ip": "192.168.1.10", "status": "success"},
    {"ip": "192.168.1.20", "status": "failed"},
    {"ip": "192.168.1.50", "status": "failed"},
    {"ip": "192.168.1.50", "status": "success"}
]
print("Port is valid : ",Validation.is_valid(443))

print("Total Failed IPs : ",logs.count_failed_log(logs_enteries))

print("Failed IPs :",logs.get_failed_ips(logs_enteries))

print("Unique IPs : ",Utils.unique_ips(logs_enteries))

