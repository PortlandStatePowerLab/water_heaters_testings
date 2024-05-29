import RPi.GPIO as GPIO
from time import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
FMPIN = 6
VPIN = 17
GPIO.setup(FMPIN, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(VPIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.add_event_detect(FMPIN, GPIO.RISING)   #add rising edge detection

while True:
    target = raw_input('Enter desired water volume in gallons:')
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
            volume = float(numPulses) / 424
            #print ('Pulses: %1f' % numPulses)
            #print ('Volume: %f' % volume)
        run_time = time()
        elapsed_time = run_time - start_time
        if elapsed_time > 60:
            print ('Timeout Error.')
            break

    GPIO.output(VPIN, GPIO.LOW) #close valve
    print('Volume drawn: %.2f gallons' % volume)
