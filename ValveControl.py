import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

VPIN = 17
GPIO.setup(VPIN, GPIO.OUT, initial=GPIO.LOW)

while True:
    x = raw_input('1 to open, 2 to close: ')
    if x == '1':
        GPIO.output(VPIN, GPIO.HIGH)
        print '\n Valve Open \n'
    elif x == '2':
        GPIO.output(VPIN, GPIO.LOW)
        print '\n Valve Closed \n'
