#!/bin/bash

DATE=$(date +"%Y-%m-%d")
LOGFILE="/var/log/ram_usage-$DATE.log"
INTERVAL=5  # Intervall in Sekunden

echo "Start RAM usage monitoring at $(date)" >> $LOGFILE

while true
do
    DATE=$(date "+%Y-%m-%d %H:%M:%S")
    FREE_OUTPUT=$(free -m)
    echo "$DATE - $FREE_OUTPUT" >> $LOGFILE
    sleep $INTERVAL
done
