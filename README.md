# RAM Usage Monitoring and Analysis

This repository contains tools to monitor and analyze RAM usage on a Linux system. It includes a shell script to log RAM usage over time and a Python script to analyze the generated log file and recommend whether a RAM upgrade is needed.

## Contents

- [Shell Script: `memlogger.sh`](#smemlogger.sh)
- [Python Analyzer: `analyzer/analyze.py`](#analyzer/analyze.py)

## Shell Script: `memlogger.sh`

The `memlogger.sh` script logs the system's RAM usage at regular intervals. This can help you track memory usage patterns and identify periods of high memory consumption.

### Usage

1. **Make the script executable**:

    ```bash
    chmod +x memlogger.sh
    ```

2. **Run the script**:

    ```bash
    sudo ./memlogger.sh
    ```

    By default, the script logs RAM usage every 10 seconds. You can modify the interval by changing the `INTERVAL` variable within the script.

### Description

The script records the following details:
- Total memory
- Used memory
- Free memory
- Shared memory
- Buffer/cache memory
- Available memory
- Swap memory (total, used, and free)

These details are logged with a timestamp to the file `ram_usage-DATE.log` in the current directory.

### Sample Output

```plaintext
Start RAM usage monitoring at Mi 19. Jun 21:17:39 CEST 2024
2024-06-19 21:17:39 -                gesamt       benutzt     frei      gemns.  Puffer/Cache verfügbar
Speicher:      14803        5730        1082          75        7990        7974
Auslager:      18898        1356       17541
2024-06-19 21:17:49 -                gesamt       benutzt     frei      gemns.  Puffer/Cache verfügbar
Speicher:      14803        5745        1065          75        7992        7961
Auslager:      18898        1352       17545
```


## Python Analyzer: `analyze_ram_log.py`

The `analyze.py` script analyzes the log file generated by the `log_ram_usage.sh` script and provides a recommendation on whether a RAM upgrade is needed based on the percentage of log entries with low free memory.

### Usage

1. **Ensure you have Python installed**.

2. **Run the script**:

    ```bash
    python3 analyze.py
    ```

    Make sure the `ram_usage.log` file is in the same directory as the Python script, or update the `LOGFILE_PATH` constant in the script to point to the correct location.

### Description

The script performs the following actions:
- Reads and parses the `ram_usage.log` file.
- Analyzes the entries to count how many times the free memory was below a specified threshold (default is 1GB).
- Calculates the percentage of entries with low free memory.
- Provides a recommendation based on the analysis (e.g., recommending a RAM upgrade if more than 20% of entries have low free memory).

### Configuration

- **Threshold**: You can modify the `THRESHOLD_MB` constant to set a different threshold for low free memory.
- **Log File Path**: Update the `LOGFILE_PATH` constant to point to the location of your `ram_usage.log` file.

### Output

The script outputs the following information:
- Total log entries analyzed
- Number of entries with low memory
- Percentage of entries with low memory
- Recommendation based on the analysis
- Timestamp of the first log entry
- Timestamp of the last log entry

### Sample Output

```plaintext
Total log entries analyzed: 238
Entries with low memory: 135
Percentage of entries with low memory: 56.72%
Recommendation: RAM upgrade recommended.
First log entry: 2024-06-19 21:17:39
Last log entry: 2024-06-19 21:57:11
