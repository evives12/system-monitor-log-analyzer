import os
import time

from metrics_collector import get_system_metrics
from log_analyzer import analyze_log_file
from report_generator import save_full_report
from utils import detect_anomalies


def main():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    log_file_path = os.path.join(base_dir, "logs", "sample.log")

    print("Continuous monitoring started. Press Ctrl+C to stop.\n")

    try:
        while True:
            # Step 1: Collect system metrics
            metrics = get_system_metrics()

            # Step 2: Analyze log file
            log_results = analyze_log_file(log_file_path)

            # Step 3: Detect anomalies
            anomalies = detect_anomalies(metrics, log_results)

            # Step 4: Print current results
            print("System Metrics")
            print(f"CPU Usage: {metrics['cpu_percent']}%")
            print(f"Memory Usage: {metrics['memory_percent']}%")
            print(f"Disk Usage: {metrics['disk_percent']}%")

            print("\nLog Analysis")
            print(f"INFO Count: {log_results['info_count']}")
            print(f"WARNING Count: {log_results['warning_count']}")
            print(f"ERROR Count: {log_results['error_count']}")

            print("\nAnomaly Detection")
            if anomalies:
                for issue in anomalies:
                    print(f"- {issue}")
            else:
                print("No anomalies detected")

            # Step 5: Save report
            report_path = save_full_report(metrics, log_results, anomalies)
            print(f"\nReport saved to: {report_path}")
            print("\n" + "=" * 50 + "\n")

            # Wait before next cycle
            time.sleep(5)

    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")


if __name__ == "__main__":
    main()