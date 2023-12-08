import subprocess
import time
import os
import signal
import csv
from datetime import datetime, timedelta

wh_type = input('WH Brand:')
volume = input('Capacity (gallons):')

yes = ['y', 'Y', 'yes', 'Yes', 'YES']


arguments = []
DRcom = []

baseline = input('Do you want to test Baseline (y/n)?')
if baseline in yes:
    arguments.append(['e\n'])
    DRcom.append(['Baseline'])

shed = input('Do you want to test Shed (y/n)?')
if shed in yes:
    arguments.append(['s\n'])
    DRcom.append(['Shed'])

cpe = input('Do you want to test CriticalPeakEvent (y/n)?')
if cpe in yes:
    arguments.append(['c\n'])
    DRcom.append(['CriticalPeakEvent'])

ge = input('Do you want to test GridEmergency (y/n)?')
if ge in yes:
    arguments.append(['g\n'])
    DRcom.append(['GridEmergency'])

lu = input('do you want to test LoadUp (y/n)?')
if lu in yes:
    arguments.append(['l\n'])
    DRcom.append(['LoadUp'])


print('Testing for the following:')
for com in DRcom:
    print(com[0])


outsideComm = 'o\n'

input_file = 'log.csv'

process = None

########   DEFINITIONS    ######################################

def start_commodity(mode):
    # open commodity service
    global process
    process = subprocess.Popen(['./sample2'], stdin=subprocess.PIPE)

    time.sleep(5)
    # enter mode
    process.stdin.write((mode.encode()))
    process.stdin.flush()

    time.sleep(5)

def update_csv(input_file, output_file, last_line):
    with open(input_file, 'r') as input_csv, open(output_file, 'a') as output_csv:
        reader = csv.reader((row.replace('\0','') for row in input_csv), delimiter=',')
        writer = csv.writer(output_csv)
        for i, row in enumerate(reader):
            if i > last_line:
                writer.writerow(row)
                last_line = i
    return last_line

# end commodity service
def end_service():
    os.kill(process.pid, signal.SIGINT)
    process.wait()
    time.sleep(5)

#########    MAIN     #########################################


# Calculate the time difference between now and 9AM to start commodity serv
now = datetime.now()
run_at = now.replace(hour=9, minute=00, second=0, microsecond=0)

startTime = input('Would you like to start Commodity Service immediately (y/n)?')

no = (['n', 'N', 'no', 'NO', 'No', 'nO'])

if startTime in no:
    if now > run_at:
        run_at += timedelta(days=1)

    delay = (run_at - now).total_seconds()

    print('Commodity Service starting in ' + str(round(delay/3600,2)) + ' hours.   ')
    print(now)

else:
    delay = 0


# Wait until the desired time
time.sleep(delay)


for arg,com in zip(arguments, DRcom):

    output_file = 'testlog/'+wh_type+volume+'_'+com[0]+'.csv' # create new csv output file name

    with open(input_file, 'r', newline='', encoding='utf-8') as input_csv:   # slice log.csv file
        reader = csv.reader((row.replace('\0','') for row in input_csv), delimiter=',')
        last_line = sum(1 for row in reader) - 1

    start_commodity(outsideComm)

    process.stdin.write((arg[0].encode()))
    process.stdin.flush()

    sleep_timer = 60*60*24*2  # sleep for 2 days

    while sleep_timer > 0:
        # send outside comm every 10 minutes
        time.sleep(60 * 5) # sleep 5 minutes

        process.stdin.write((outsideComm.encode()))
        process.stdin.flush()

        time.sleep(60 * 5) # sleep 5 minutes

        process.stdin.write((arg[0].encode()))
        process.stdin.flush()

        sleep_timer -= 60 * 10 # reduce time by 10 minutes for 2 days


    update_csv(input_file, output_file, last_line) # create csv output file

    time.sleep(5)

    end_service() # loop through DR commands until DONE

print('Testing completed for the following events:')
print(wh_type + volume)
for com in DRcom:
    print(com[0])
