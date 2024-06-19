import re
import datetime

# Constants
LOGFILE_PATH = '/var/log/ram_usage.log'  # Change this to the path of your log file
# Common threshold for free memory in MB
# ChatGPT recommendation:
# For general usage (browsing, office applications, etc.), having around 10-20% of your total RAM free is often sufficient.
THRESHOLD_MB = 2400

def parse_log_entry(log_entry):
    """
    Parse a log entry and return the timestamp and free memory.
    """
    match = re.search(r'(\d+-\d+-\d+ \d+:\d+:\d+) -.*\nSpeicher:\s+\d+\s+\d+\s+(\d+)\s+', log_entry)
    if match:
        timestamp_str = match.group(1)
        free_memory_mb = int(match.group(2))
        timestamp = datetime.datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S')
        return timestamp, free_memory_mb
    return None, None

def analyze_logfile(logfile_path, threshold_mb):
    """
    Analyze the entire log file and determine if a RAM upgrade is recommended.
    """
    low_memory_count = 0
    total_entries = 0
    min_timestamp = None
    max_timestamp = None

    with open(logfile_path, 'r') as logfile:
        log_content = logfile.read()
        log_entries = re.split(r'(\d+-\d+-\d+ \d+:\d+:\d+)', log_content)  # Split by timestamp format

        for i in range(1, len(log_entries), 2):
            timestamp_str = log_entries[i]
            log_entry = log_entries[i + 1]

            timestamp, free_memory_mb = parse_log_entry(timestamp_str + log_entry)
            if timestamp and free_memory_mb:
                total_entries += 1
                if free_memory_mb < threshold_mb:
                    low_memory_count += 1

                if not min_timestamp or timestamp < min_timestamp:
                    min_timestamp = timestamp
                if not max_timestamp or timestamp > max_timestamp:
                    max_timestamp = timestamp

    if total_entries == 0:
        return "No log entries found."

    low_memory_percentage = (low_memory_count / total_entries) * 100

    recommendation = "No RAM upgrade needed."
    if low_memory_percentage > 20:  # If more than 20% of the entries have low memory, consider an upgrade
        recommendation = "RAM upgrade recommended."

    result = {
        'total_entries': total_entries,
        'low_memory_count': low_memory_count,
        'low_memory_percentage': low_memory_percentage,
        'recommendation': recommendation,
        'first_entry': min_timestamp,
        'last_entry': max_timestamp
    }

    return result

def main():
    result = analyze_logfile(LOGFILE_PATH, THRESHOLD_MB)
    if isinstance(result, dict):
        print(f"Total log entries analyzed: {result['total_entries']}")
        print(f"Entries with low memory: {result['low_memory_count']}")
        print(f"Percentage of entries with low memory: {result['low_memory_percentage']:.2f}%")
        print(f"Recommendation: {result['recommendation']}")
        print(f"First log entry: {result['first_entry']}")
        print(f"Last log entry: {result['last_entry']}")
    else:
        print(result)

if __name__ == "__main__":
    main()
