from datetime import datetime, timedelta
import RPi.GPIO as GPIO
from time import time, sleep

# Initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
FMPIN = 6    # flow meter GPIO pin
VPIN = 17    # valve GPIO pin
GPIO.setup(FMPIN, GPIO.IN, GPIO.PUD_UP) # setup flow meter pin as input
GPIO.setup(VPIN, GPIO.OUT, initial=GPIO.LOW)    # setup valve pin as output
GPIO.add_event_detect(FMPIN, GPIO.RISING)   # add rising edge detection

arguments = [[8], [5], [3], [5], [8], [5], [3]] # Five 5 gallon water draws --> 25 gallons total
drawInterval = int(25 * 60) # Time between water draws (arguments) --> 20 minutes
shedDelay = int(10 * 60) # Time delay after Shed mode initializes --> 5 minutes

########   DEFINITIONS    ######################################

def draw_water(targetVol):
    if targetVol <= 0:
        return()
    print ('Drawing %.2f gallon(s).' % targetVol)
    volume = 0
    numPulses = 0
    start_time = time()
    GPIO.output(VPIN, GPIO.HIGH)    #open valve
    while volume < targetVol:  #keep valve open until desired volume has passed
        if GPIO.event_detected(FMPIN):
            numPulses += 1    #Count pulses from flow meter
            volume = float(numPulses) / 476    #Calculate volume
        run_time = time()
        elapsed_time = run_time - start_time
        if elapsed_time > 240:
            print('Timeout Error.')
            break
    GPIO.output(VPIN, GPIO.LOW) #close valve
    print ('Volume drawn: %.2f gallon(s).' % volume)

#########    MAIN     #########################################


# Calculate the time difference between now and 9AM to start commodity serv
print('Select Test Start Time:\n')
hr = int(input('Hour:'))
mn =  int(input('Minute:'))
timeLoad = float(input('\nLoad Up Duration (minutes):')) * 60
timeShed = float(input('Shed Event Duration (hours):')) * 60 * 60
cycles = float(input('Number of Intervals: '))
print('\n##################################################\n')



now = datetime.now()
run_at = now.replace(hour=hr, minute=mn, second=0, microsecond=0)

if now > run_at:
    run_at += timedelta(days=1)

delay = (run_at - now).total_seconds()

print(now)
print('Draw Schedule Starting in ' + str(round(delay/3600,2)) + ' hours.\n')


# Wait until the desired time
sleep(delay)

cycleCount = 0

while cycleCount != cycles:
    now = datetime.now()
    print(now)
    print('Waiting for WH to Load Up . . . \n')


    # Wait until Load Up is done
    sleep(timeLoad)


    start = datetime.now()
    print(start)
    print('Load Up Completed.\nWater draws initiating for Shed Event. . .\n')
    sleep(shedDelay)

    ########################################
    #     ACTIVE  WATER   DRAWS
    ########################################

    i = 0
    index = len(arguments)
    for arg in arguments:
        x = datetime.now() # time before water drawi
        print(x)
        draw_water(arg[0])
        i += 1
        print(f'[{i}/{index:.0f}]\n')
        n = datetime.now() # time after water draw
        delay = (n - x).total_seconds() # processing delay
        t = drawInterval - delay
        sleep(t)


    ########################################
    #  WAIT UNTIL SHED DURATION DONE
    ########################################

    now = datetime.now() # take current time
    later = start + timedelta(seconds = timeShed) # create Shed Duration End time
    rest = (later - now).total_seconds() # end of shed duration - current time
    print(now)
    print(f'Shed Event will conclude in {rest/60:.0f} minutes...\n') # rest until end of shed duration
    sleep(rest)


    ########################################
    #   WAIT UNTIL END SHED DONE
    ########################################

    now = datetime.now()
    later = later + timedelta(seconds = timeLoad)
    rest = (later - now).total_seconds()
    print(now)
    print('Shed Event Completed. Sending EndShed.\n')
    sleep(rest) # wait until EndShed has completed
    cycleCount += 1
    now = datetime.now()
    print(now)
    print(f'Interval [{cycleCount}/{cycles:.0f}] completed.') # display current/total test
    print('\n################################################\n')

now = datetime.now()
print(now)
print(f'{cycleCount} Interval(s) Completed.')
