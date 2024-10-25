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



print('\nTesting for the following:')
for com in DRcom:
    print(com[0])


outsideComm = 'o\n'
loadup = 'l\n'
endShed = 'e\n'

input_file = 'log.csv'

process = None

########   DEFINITIONS    ######################################

def start_commodity(mode):
    # open commodity service
    global process
    process = subprocess.Popen(['./sample2'], stdin=subprocess.PIPE)

    time.sleep(1)
    # enter mode
    process.stdin.write((mode.encode()))
    process.stdin.flush()

    time.sleep(1)

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
print('\nSelect Test Start Time:\n')
hr = int(input('Hour:'))
mn =  int(input('Minute:'))

now = datetime.now()
run_at = now.replace(hour=hr, minute=mn, second=0, microsecond=0)

if now > run_at:
    run_at += timedelta(days=1)

delay = (run_at - now).total_seconds()


timeLoad0 = float(input('Load Up Duration (minutes):'))
timeShed0 = float(input('Shed Event Duration (hours):')) * 60

print('Commodity Service starting in ' + str(round(delay/3600,2)) + ' hours.   ')
print(now)

delay = (run_at - now).total_seconds()


# Wait until the desired time
time.sleep(delay)


for arg,com in zip(arguments, DRcom):

    timeLoad = timeLoad0
    timeShed = timeShed0
    timeEnd = timeLoad0

    output_file = 'testlog/'+wh_type+volume+'_'+com[0]+'.csv' # create new csv output file name

    with open(input_file, 'r', newline='', encoding='utf-8') as input_csv:   # slice log.csv file
        reader = csv.reader((row.replace('\0','') for row in input_csv), delimiter=',')
        last_line = sum(1 for row in reader) - 1

        start_commodity(outsideComm)
        process.stdin.flush()


    while timeLoad > 0: # load up loop
        process.stdin.write((loadup.encode()))
        process.stdin.flush()

        time.sleep(60)

        process.stdin.write((outsideComm.encode()))
        process.stdin.flush()

        time.sleep(60*4)

        timeLoad -= 5


    while timeShed > 0: # shed loop
        process.stdin.write((arg[0].encode()))
        process.stdin.flush()
        time.sleep(60)

        process.stdin.write((outsideComm.encode()))
        process.stdin.flush()

        time.sleep(60 * 4)

        timeShed -= 5


    while timeEnd > 0:
        process.stdin.write((endShed.encode()))
        process.stdin.flush()
        time.sleep(60)

        process.stdin.write((outsideComm.encode()))
        process.stdin.flush()
        time.sleep(60 * 4)

        timeEnd -= 5

    update_csv(input_file, output_file, last_line) # create csv output file
    end_service() # loop through DR commands until DONE

print('\n\nTesting completed for the following events:')
print(wh_type + volume)
for com in DRcom:
    print(com[0])
print(datetime.now())
