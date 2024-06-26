# This is the program that was successful in reading the cumulative gallons that
# the flowmeter detected. You need to keep the program running in order to keep detecting 
# flowmeter pulses.


import RPi.GPIO as GPIO
import time
from time import gmtime, strftime

## Establish GPIO PIN setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
FMPIN = 6
GPIO.setup(FMPIN, GPIO.IN, GPIO.PUD_UP)

# global volume
# volume = 0
count = 0

def countPulse(channel):
	global count
	count = count+1
	volume = float(count) / 424
	print("Volume = " + str(volume))


GPIO.add_event_detect(FMPIN, GPIO.BOTH, callback=countPulse)   #add falling edge detection

while True:
	try:
		time.sleep(1)
	except KeyboardInterrupt:
		print('\nkeyboard interrupt!')
		GPIO.cleanup()
		sys.exit()

	#count = count + 1


#time.sleep(1)
