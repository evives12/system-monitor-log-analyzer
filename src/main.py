import os
import time
from datetime import datetime

from metrics_collector import get_system_metrics
from log_analyzer import analyze_log_file
from report_generator import save_full_report
from utils import detect_anomalies


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    log_file_path = os.path.join(base_dir, "logs", "sample.log")

    print("Continuous monitoring started. Press Ctrl+C to stop.\n")

    try:
        while True:
            metrics = get_system_metrics()
            log_results = analyze_log_file(log_file_path)
            anomalies = detect_anomalies(metrics, log_results)

            report_path = save_full_report(metrics, log_results, anomalies)

            clear_screen()

            print("========================================")
            print("     SYSTEM MONITORING DASHBOARD")
            print("========================================\n")

            print(f"CPU Usage:     {metrics['cpu_percent']}%")
            print(f"Memory Usage:  {metrics['memory_percent']}%")
            print(f"Disk Usage:    {metrics['disk_percent']}%\n")

            print("----------------------------------------\n")

            print("Log Analysis:")
            print(f"INFO:     {log_results['info_count']}")
            print(f"WARNING:  {log_results['warning_count']}")
            print(f"ERROR:    {log_results['error_count']}\n")

            print("----------------------------------------\n")

            print("Anomalies:")
            if anomalies:
                for issue in anomalies:
                    print(f"- {issue}")
            else:
                print("No anomalies detected")

            print("\n----------------------------------------\n")

            print(f"Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print("Refresh Interval: 3 seconds")
            print(f"Latest Report: {os.path.basename(report_path)}")

            time.sleep(3)

    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")



if __name__ == "__main__":
    main()