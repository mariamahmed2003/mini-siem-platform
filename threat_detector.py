import os
from elasticsearch import Elasticsearch
from collections import defaultdict
from datetime import datetime
import json

es = Elasticsearch("http://localhost:9200" , basic_auth=("elastic", os.environ.get("ES_PWD")))

THRESHOLD = 5

def detect_brute_force():
    query = {
        "query": {
            "bool": {
                "must": [
                    {"match":  {"log_message": "Failed password"}},
                    {"range":  {"@timestamp": {"gte": "now-1h"}}}
              
                ]
            }
    },
    "size": 1000
  
    }


    res = es.search(index="siem-logs-*", body=query)
    ip_count = defaultdict(int)
    for hit in res["hits"]["hits"]:
        msg = hit["_source"].get("log_message", "")
        parts = msg.split("from ")
        if len(parts) >1:
           ip = parts[1].split()[0]
           ip_count[ip] += 1
    alerts =[]
    for ip, count in ip_count.items():
        if count >= THRESHOLD:
           alert = {
               "type": "BRUTE_FORCE",
               "ip": ip,
               "attempts": count,
               "timestamp": datetime.utcnow().isoformat(),
               "severity": "HIGH"
           }
           alerts.append(alert)
           print(f"[ALERT] Brute-force detected from {ip} - {count} attempts")
    return alerts
if __name__ == "__main__":
    alerts = detect_brute_force()
    with open("alerts.json", "w") as f:
        json.dump(alerts, f, indent=2)
    print(f"\n{len(alerts)} alert(s) written to alerts.json")
