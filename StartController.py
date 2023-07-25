import subprocess
import schedule
import time
import os
import signal

process = None
arguments = [['Baseline'],['Shed'],['Critical Peak Event'],['Grid Emergency']]


####### FUNCTIONS #####################################################################

def SchedDraw(mode):
    # initialize Scheduled Draw
    process = subprocess.Popen(['python3', 'controller/DrawController.py'], stdin=subprocess.PIPE)

    print('Starting Draw Controller in '+mode)

    time.sleep(60*60*24) # run scheduled draw for 24 hours

    os.kill(process.pid, signal.SIGINT)
    process.wait()

    print('Idle in '+mode)

    time.sleep(60*60*24) # run idle mode for 24 hours


######### MAIN #########################################################################

for arg in arguments:
    SchedDraw(arg[0])
