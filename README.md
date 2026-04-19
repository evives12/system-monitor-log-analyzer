# System Monitoring & Log Analyzer

A Python-based tool that collects real-time system metrics, analyzes log files, detects anomalies, and generates structured reports for troubleshooting and performance monitoring.

## Purpose

This project simulates a lightweight monitoring and troubleshooting tool that automates system health checks, log analysis, anomaly detection, and live dashboard output to reduce manual debugging effort.


## Features

- Collects real-time CPU, memory, and disk usage
- Analyzes log files for INFO, WARNING, and ERROR entries
- Detects anomalies using threshold-based rules
- Generates structured timestamped reports
- Runs continuously at fixed intervals
- Displays a live console dashboard for monitoring output


## How It Works

The system runs in a continuous loop:

1. Collects live system metrics
2. Reads and analyzes log data
3. Applies anomaly detection rules
4. Generates a timestamped report
5. Refreshes the console dashboard
6. Repeats every few seconds



## Tech Stack
- Python
- psutil

## Project Structure
```
system-monitor-log-analyzer/
├── src/
│ ├── main.py
│ ├── metrics_collector.py
│ ├── log_analyzer.py
│ ├── report_generator.py
│ └── utils.py
├── logs/
│ └── sample.log
├── reports/
├── README.md
├── requirements.txt
└── .gitignore
```

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

