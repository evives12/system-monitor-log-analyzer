# System Monitoring & Log Analyzer

A Python-based tool that collects real-time system metrics, analyzes log files, detects anomalies, and generates structured reports for troubleshooting and performance monitoring.

## Features
- Collects real-time CPU, memory, and disk usage
- Analyzes log files for INFO, WARNING, and ERROR entries
- Detects anomalies using threshold-based rules
- Generates a structured troubleshooting report
- Automates the monitoring and analysis workflow in a single run

## Tech Stack
- Python
- psutil

## Project Structure
system-monitor-log-analyzer/
├── .venv/
├── src/
│   ├── main.py
│   ├── metrics_collector.py
│   ├── log_analyzer.py
│   ├── report_generator.py
│   └── utils.py
├── logs/
│   └── sample.log
├── reports/
├── README.md
├── requirements.txt
└── .gitignore

## How to Run
1. Install dependencies:
   pip install -r requirements.txt

2. Run the program:
   python src/main.py

## Example Output
- CPU, memory, and disk metrics displayed in the console
- Log summary with INFO/WARNING/ERROR counts
- Anomaly detection results
- A generated report saved in the `reports/` folder

## Purpose
This project was built to simulate a lightweight monitoring and troubleshooting tool that could help identify system performance issues and recurring log errors more efficiently.