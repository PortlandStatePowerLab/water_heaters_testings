#!/bin/bash

trap "exit" INT TERM ERR
trap "kill 0" EXIT

echo "1. Daily draw schedule (Dana)"
echo "2. Cold water dump, peripheral (Dana)"
echo "3. Test program (Dana)"
read -p "Which draw profile would you like to run? (Enter 1, 2, or 3): " user_choice

# Check if the user entered a valid choice
if [[ "$user_choice" != "1" && "$user_choice" != "2" && "$user_choice" != "3" ]]; then
    echo "Invalid entry. Please enter 1, 2, or 3."
    exit 1
fi

read -p "Do you want to start immediately? (y/n): " start_now

current_time=$(date +%s)
target_time=$(date -d '09:00:00' +%s)
end_time=$(date -d '10:00:00' +%s)

if [[ "$start_now" == "y" ]]; then
    sleep_seconds=0
else
    sleep_seconds=$(($target_time - $current_time))

    if ((current_time > end_time)); then
        sleep_seconds=$(($sleep_seconds+60*60*24))
    elif ((current_time >= target_time && current_time <= end_time)); then
        sleep_seconds=0
    fi
fi

hours=$(($sleep_seconds/3600))

printf 'Draw Controller will start in %.2s hour(s)   ' "$hours"
date
printf '\n\n'

sleep $sleep_seconds &

PID=$!

wait $PID

i=4
while [ $i -gt 0 ]; do
    python3 DrawController_Conformance.py "$user_choice" &
    sleep 86400 &
    PID=$!
    wait $PID
    pkill -f DrawController_Conformance.py
    printf '\n\nTurning off Draw Controller for 24 Hr   '
    date
    printf '\n\n'
    sleep 86400 &
    PID=$!
    wait $PID
    ((i--))
done
