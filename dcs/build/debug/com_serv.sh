#!/usr/bin/expect -f
spawn ./sample2

expect "choice:"
send "e\r"
interact
sleep 20

send "s\r"
interact
sleep 20

send "s\r"
sleep 86400

send "c\r"
sleep 86400

send "c\r"
sleep 86400

send "g\r"
sleep 86400

send "g\r"
sleep 86400

send "l\r"

interact

