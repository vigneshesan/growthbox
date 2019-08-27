
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.IN)

while True:
    if GPIO.input(5) == 1:
        print ("LIGHT 0")
        time.sleep(1)
    else:
        print ("LIGHT 1")
        time.sleep(1)
   
