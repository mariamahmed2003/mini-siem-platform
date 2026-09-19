import json
from datetime import datetime

def generate_report(alerts_file="alerts.json"):
    with open(alerts_file) as f:
        alerts = json.load(f)
    report = f"""
=========================================
    MINI SIEM - SECURITY REPORT
    Generated: {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}
=========================================

TOTAL ALERTS: {len(alerts)}

"""
    for a in alerts:
        report += f"""
[{a['severity']}] {a['type']}
  Source IP :  {a['ip']}
  Attempts  :  {a['attempts']}
  Time      :  {a['timestamp']}
---
"""
    report_file = f"report_{datetime.utcnow() .strftime('%Y%m%d_%H%M')}.txt"
    with open(report_file, "w") as f:
        f.write(report)
    print(report)
    print(f"Report saved to {report_file}")
if __name__ == "__main__":
    generate_report()
