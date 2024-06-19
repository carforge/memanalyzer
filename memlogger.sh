#!/bin/bash

LOGFILE="/var/log/ram_usage.log"
INTERVAL=10  # Intervall in Sekunden

echo "Start RAM usage monitoring at $(date)" >> $LOGFILE

while true
do
    DATE=$(date "+%Y-%m-%d %H:%M:%S")
    FREE_OUTPUT=$(free -m)
    echo "$DATE - $FREE_OUTPUT" >> $LOGFILE
    sleep $INTERVAL
done
