# RAM Usage Monitoring and Analysis

This repository contains tools to monitor and analyze RAM usage on a Linux system. It includes a shell script to log RAM usage over time and a Python script to analyze the generated log file and recommend whether a RAM upgrade is needed.

## Contents

- [Shell Script: `memlogger.sh`](#shell-script-log_ram_usagesh)
- [Python Analyzer: `analyzer/analyze.py`](#python-analyzer-analyze_ram_logpy)

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
...
