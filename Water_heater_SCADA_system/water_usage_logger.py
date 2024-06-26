# This program was a prototype that was going to be used to automatically detect the flowmeter of water heater to log the 
# water usage in a file "Water_log_file.csv"

import RPi.GPIO as GPIO
import time
from time import gmtime, strftime

## Establish GPIO PIN setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
FMPIN = 6
GPIO.setup(FMPIN, GPIO.IN, GPIO.PUD_UP)

#global volume
#volume = 0
#global count
count = 0

def countPulse(channel):
	global count
	if start_counter == 1:
		count = count+1
		#volume = float(count) / 476
		#print("Volume = " + str(volume))

GPIO.add_event_detect(FMPIN, GPIO.FALLING, callback=countPulse)   #add falling edge detection

# GPIO.add_event_detect(FMPIN, GPIO.RISING)


# Log water volume
while True:
	try:
		start_counter = 1 # initializes counter in countPulse function
		time.sleep(1)
		start_counter = 0
		volume = float(count) / 476
		print("Volume = " + str(volume))
		if GPIO.event_detected(FMPIN):
			break
		#count = 0
		#time.sleep(15)
	except KeyboardInterrupt:
		print('\nkeyboard interrupt!')
		GPIO.cleanup()
		sys.exit()

time.sleep(1)
