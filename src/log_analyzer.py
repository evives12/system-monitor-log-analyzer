def analyze_log_file(log_file_path):
    results = {
        "info_count": 0,
        "warning_count": 0,
        "error_count": 0
    }

    with open(log_file_path, "r") as file:
        for line in file:
            if "INFO" in line:
                results["info_count"] += 1
            elif "WARNING" in line:
                results["warning_count"] += 1
            elif "ERROR" in line:
                results["error_count"] += 1

    return results