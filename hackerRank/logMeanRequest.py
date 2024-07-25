from datetime import datetime
import re

def calculate_mean_from_log_lines(lines):
    """
    Calculates the average request latency from log lines.

    Args:
        lines: An iterable of log file lines.

    Returns:
        The average (mean) request latency in seconds, or 0.0 if no requests were found.
    """

    request_times = {}
    total_duration = 0
    num_requests = 0

    LOG_LINE_REGEX = r"(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}) (\w+) #(\d+)"

    for line in lines:
        match = re.match(LOG_LINE_REGEX, line)  # Use regex here

        if match:
            timestamp, event_type, request_id_str = match.groups()
            request_id = int(request_id_str)
            if event_type == "Started":
                request_times[request_id] = timestamp_to_seconds(timestamp)
            elif event_type == "Finished":
                if request_id in request_times:
                    start_time = request_times.pop(request_id)
                    print(start_time)
                    end_time = timestamp_to_seconds(timestamp)
                    duration = end_time - start_time
                    total_duration += duration
                    num_requests += 1

    return total_duration / num_requests if num_requests > 0 else 0.0



def timestamp_to_seconds(timestamp):
    """
    Parses an ISO datetime string and returns seconds since the UNIX epoch.

    Args:
        timestamp: An ISO-formatted datetime string (e.g., "2020-07-01T14:10:10.100").

    Returns:
        The number of seconds since the UNIX epoch as a float.
    """

    return datetime.fromisoformat(timestamp).timestamp()



# Test Case
test_log_lines = [
    "2020-07-01T14:10:10.100 Started #4257",
    "2020-07-01T14:10:10.250 Started #4258",
    "2020-07-01T14:10:10.300 Finished #4258",
    "2020-07-01T14:10:15.320 Finished #4257",
]

mean_duration = calculate_mean_from_log_lines(test_log_lines)
print("Average request duration:", mean_duration, "seconds")