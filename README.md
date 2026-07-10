## Mini SIEM & Threat Detection Platform
A lightweight Security Information and Event Management (SIEM) system built with Python and the ELK Stack.
Collects system logs, detects brute-force attacks, visualizes security events on a live dashboard, and generates automated reports.
Work in progress — see status below.

## Features & Status
Collect Linux logs via Logstash (auth.log → Elasticsearch).
Collect Windows logs (Winlogbeat).
Detect brute-force SSH attacks (Python detection engine) — script written.
Real-time Kibana dashboard with alerts — configured, pending live data.
Automated security report generation (Python) — script written.

## Tech Stack
Python 3 · Elasticsearch · Logstash · Kibana · Linux · Oracle VirtualBox

## Architecture
[ Linux auth.log ]  [ Windows Events ]
        │                   │
        └─────────┬─────────┘
                  ▼
           [ Logstash ]
         Parse & ship logs
                  │
                  ▼
        [ Elasticsearch ]
        Store & index logs
          │              │
          ▼              ▼
      [ Kibana ]    [ Python Engine ]
      Dashboard     Brute-force detection
                         │
              ┌──────────┴──────────┐
              ▼                     ▼
        [ alerts.json ]      [ report.txt ]

## Project Structure
mini-siem-platform/
├── configs/
│   └── siem.conf            # Logstash pipeline config
├── scripts/
│   ├── threat_detector.py   # Brute-force detection engine
│   └── report_generator.py  # Security report generator
├── outputs/
│   ├── alerts.json          # Sample alert output
│   └── report_sample.txt    # Sample report
└── README.md
