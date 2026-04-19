def detect_anomalies(metrics, log_results):
    anomalies = []

    # Thresholds
    if metrics["cpu_percent"] > 80:
        anomalies.append("High CPU usage detected")

    if metrics["memory_percent"] > 80:
        anomalies.append("High memory usage detected")

    if metrics["disk_percent"] > 90:
        anomalies.append("High disk usage detected")

    if log_results["error_count"] > 1:
        anomalies.append("Multiple errors found in logs")

    return anomalies