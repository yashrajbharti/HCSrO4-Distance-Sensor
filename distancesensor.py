import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

TRIG = 4
ECHO = 18
# just using variable names instead of pin numbers

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(TRIG, GPIO.IN)

GPIO.output(TRIG,True)
time.sleep(0.0001)
GPIO.output(TRIG,False)

while GPIO.input(ECHO) == False:
        start = time.time()
while GPIO.input(ECHO) == True:
        end = time.time()

sig_time = end - start

# cm 
distance = sig_time / 0.000058
# inches = 0.000148
print('Distance : {} cm'.format(distance))
GPIO.cleanup()
