
def extractErrorLogs(logs):
    """Extracts and sorts error/critical logs from CloudWatch-like data.

    Args:
        logs: A 2D list of log entries (date, time, status, message).

    Returns:
        A filtered and sorted list of error/critical log entries.
    """

    error_logs = []
    for log in logs:
        date, time, status, message = log
        if status in ("ERROR", "CRITICAL"):
            error_logs.append((date, time, status, message))

    # Sort by combined datetime and original index for stability
    error_logs.sort(key=lambda x: (x[0] + ' ' + x[1], logs.index([x[0], x[1], x[2], x[3]]))) 
    
    # Keep only the original log format 
    return [list(log) for log in error_logs]  


logs = [
    ["01-01-2023", "15:00", "ERROR", "failed"],
    ["01-01-2023", "16:00", "SUCCESS", "established"],
    ["01-01-2022", "14:00", "CRITICAL", "failed"],
]

result = extractErrorLogs(logs)
print(result) 