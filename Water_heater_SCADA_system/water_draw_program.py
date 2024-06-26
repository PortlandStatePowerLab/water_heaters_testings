# This is a file which performs a water draw and writes the results to a file.
# This program is set up so that you could connect to a host and transfer the file via SSH.

import RPi.GPIO as GPIO
from time import time
from time import gmtime, strftime
import paramiko
import os

# Update the next three lines with your
# server's information

host = "131.252.223.182"
username = "hank"
password = "Jbcasf18"

## Set up SSH connection to server
client = paramiko.client.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=username, password=password)
print("Connection made.")


## Establish GPIO PIN setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
FMPIN = 6
VPIN = 17
GPIO.setup(FMPIN, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(VPIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.add_event_detect(FMPIN, GPIO.RISING)   #add rising edge detection

## Perform water draw
while True:
    target = input('Enter desired water volume in gallons:')
    target = float(target)
    if target == 0:
        GPIO.output(VPIN, GPIO.LOW) #close valve and quit if no water is requested
        print('Exiting program.')
        quit()

    print ('Drawing %.2f gallon(s).' % target)
    volume = 0
    numPulses = 0
    GPIO.output(VPIN, GPIO.HIGH)    #open valve

    start_time = time()
    while volume < target:  #target test volume in gallons
        if GPIO.event_detected(FMPIN):
            numPulses += 1
            volume = float(numPulses) / 476
            #print ('Pulses: %1f' % numPulses)
            #print ('Volume: %f' % volume)
        run_time = time()
        elapsed_time = run_time - start_time
        if elapsed_time > 60:
            print ('Timeout Error.')
            break

    GPIO.output(VPIN, GPIO.LOW) #close valve
    print('Volume drawn: %.2f gallons' % volume)

    ## Write data to file
    actual_time = strftime("%Y-%m-%d %H-%M-%S", gmtime())
    fobj_out = open("Water draw data - " + str(actual_time) + ".txt", "w")
    fobj_out.write("Water draw results:\nVolume: %.2f gallons" % volume)

    break
