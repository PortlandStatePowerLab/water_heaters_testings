#!/bin/bash

trap "exit" INT TERM ERR
trap "kill 0" EXIT

current_time=$(date +%s)
target_time=$(date -d '09:00:00' +%s)
end_time=$(date -d '10:00:00' +%s)


sleep_seconds=$(($target_time - $current_time))

if((current_time > end_time)); then
    sleep_seconds=$(($sleep_seconds+60*60*24))
elif((current_time >= target_time && current_time <= end_time)); then
    sleep_seconds=0
fi

hours=$(($sleep_seconds/3600))

printf 'Draw Controller will start in %.2s hour(s)   ' "$hours"
date
printf '\n\n'

sleep $sleep_seconds &

PID=$!

wait $PID

i=4
while [ $i -gt 0 ];
do
    python3 DrawController.py &
    sleep 86400 &
    PID=$!
    wait $PID
    pkill -f DrawController.py
    printf '\n\nTurning off Draw Controller for 24 Hr   '
    date
    printf '\n\n'
    sleep 86400 &
    PID=$!
    wait $PID
    ((i--))
done
