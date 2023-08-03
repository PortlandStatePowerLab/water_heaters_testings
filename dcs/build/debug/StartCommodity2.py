import subprocess
import time
import os
import signal
import csv
from datetime import datetime, timedelta
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

%matplotlib inline


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


# plot each csv file
def wh_plot(wh_mode_file):
    # importing csv file
    df = pd.read_csv(wh_mode_file, header=None)
    df = df.dropna(thresh=2) # drops lines with '0'
    error_bad_lines=False

    #delete unnecessary data columns. adjust these column values depending on the delivered log.csv data
    df.drop([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12,14], axis=1, inplace=True)

    # extract time data and converts to datetime
    df.insert(1, 'Time', pd.to_datetime(df[0]))
    df['Time'] = df['Time'].dt.strftime('%H:%M:%S')

    # delete original timestamp data
    df.drop([0], axis=1, inplace=True)

    # convert to numpy array

    wd = np.array(df)

    # create axis variables
    Time = wd[:,0]
    EnergyTake = wd[:,1]
    Current = wd[:,2]/240 # current = power_column/voltage

    # create fig and ax objects
    fig, ax1 = plt.subplots(1,1,figsize=(10,8))
    ax2 = ax1.twinx()

    # plot the values
    ax1.plot(Time, EnergyTake)
    ax2.plot (Time, Current, 'r--')

    # set the labels
    ax1.set_title('EnergyTake and Current vs Time')
    ax1.set_xlabel('Timestamp (H:M:S)')
    ax1.set_ylabel('EnergyTake (Wh)')
    ax2.set_ylabel('Current (A)')

    # set axis ticks
    ax1.xaxis.set_major_locator(plt.MaxNLocator(25)) # set number of ticks on x-axis
    ax1.yaxis.set_major_locator(plt.MaxNLocator(15)) # set number of ticks on y1-axis
    ax2.yaxis.set_major_locator(plt.MaxNLocator(15)) # set number of ticks on y2-axis
    ax1.set_ylim(ymin=0)
    ax2.set_ylim(ymin=0) # forces current axis to start from 0
    fig.legend(['EnergyTake','Current'])

    ax1.tick_params(axis='x', labelrotation=45)

    #fig.autofmt_xdate(rotation=90) # rotate x-axis data
    ax1.grid()

    # display and save the plot
    plt.tight_layout()
    plt.savefig(wh_mode_file+'.jpg', dpi=95, bbox_inches='tight') # change save file name and size of graph
    plt.show()

#########    MAIN     #########################################


# Calculate the time difference between now and 9AM to start commodity serv
now = datetime.now()
run_at = now.replace(hour=9, minute=00, second=0, microsecond=0)

if now > run_at:
    run_at += timedelta(days=1)

delay = (run_at - now).total_seconds()

print('Commodity Service starting in ' + str(round(delay/3600,2)) + ' hours.')
# Wait until the desired time
time.sleep(delay)


for arg,com in zip(arguments, DRcom):

    output_file = 'testlog/'+wh_type+volume+'_'+com[0]+'_log.csv' # create new csv output file name
    output_jpg = 'testlog/'+wh_type+volume+'_'+com[0]+'_log'

    with open(input_file, 'r') as input_csv:   # slice log.csv file
        reader = csv.reader(input_csv)
        last_line = sum(1 for row in reader) - 1

    start_commodity(arg[0]) # DR commands baseline, shed, critical peak event, grid emergency

    time.sleep(172800) # sleep for 2 days

    update_csv(input_file, output_file, last_line) # create csv output file

    time.sleep(10)

    wh_plot(output_jpg)

    end_service() # loop through DR commands until DONE


print(volume+' gallon '+wh_type+' Baseline, Shed, Critical Peak Event,'
        '\n Grid Emergency DONE. Run LoadUp command to complete testing.')
