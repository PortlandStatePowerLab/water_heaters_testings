import subprocess
import time
import os
import signal
import csv
from datetime import datetime, timedelta


wh_type = input('WH Brand:')
volume = input('Capacity (gallons):')

arguments = [['e\n'],['s\n'],['c\n'],['g\n']]
DRcom = [['Baseline'], ['Shed'], ['CriticalPeakEvent'], ['GridEmergency']]

loadup = 'l\n'

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

def update_csv(input_file, output_file, last_line):
    with open(input_file, 'r') as input_csv, open(output_file, 'a') as output_csv:
        reader = csv.reader(input_csv)
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
run_at = now.replace(hour=9, minute=0, second=0, microsecond=0)
if run_at < now:
    run_at += timedelta(days=1)
delay = (run_at - now).total_seconds()

# Wait until the desired time
time.sleep(delay)


for arg,com in zip(arguments, DRcom):

    output_file = 'testlog/'+wh_type+volume+'_'+com[0]+'_log.csv' # create new csv output file name

    with open(input_file, 'r') as input_csv:   # slice log.csv file
        reader = csv.reader(input_csv)
        last_line = sum(1 for row in reader) - 1
    
    start_commodity(arg[0]) # DR commands baseline, shed, critical peak event, grid emergency

    time.sleep(172800) # sleep for 2 days

    update_csv(input_file, output_file, last_line) # create csv output file

    time.sleep(10)

    end_service() # loop through DR commands until DONE

print(volume+' gallon '+wh_type+' Baseline, Shed, Critical Peak Event,'
        '\n Grid Emergency DONE. Run LoadUp command to complete testing.')
    

