import os
from datetime import datetime


def save_full_report(metrics, log_results,anomalies):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    reports_dir = os.path.join(base_dir, "reports")
    os.makedirs(reports_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    filename = f"system_report_{timestamp}.txt"
    file_path = os.path.join(reports_dir, filename)

    with open(file_path, "w") as file:
        file.write("System Monitoring & Log Analysis Report\n")
        file.write("=======================================\n\n")

        file.write("System Metrics\n")
        file.write("--------------\n")
        file.write(f"CPU Usage: {metrics['cpu_percent']}%\n")
        file.write(f"Memory Usage: {metrics['memory_percent']}%\n")
        file.write(f"Disk Usage: {metrics['disk_percent']}%\n\n")

        file.write("Log Analysis\n")
        file.write("------------\n")
        file.write(f"INFO Count: {log_results['info_count']}\n")
        file.write(f"WARNING Count: {log_results['warning_count']}\n")
        file.write(f"ERROR Count: {log_results['error_count']}\n")

        file.write("\nAnomaly Detection\n")
        file.write("------------------\n")

        if anomalies:
            for issue in anomalies:
                file.write(f"- {issue}\n")
        else:
            file.write("No anomalies detected\n")


    return file_path