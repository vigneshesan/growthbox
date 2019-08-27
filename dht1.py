import RPi.GPIO as GPIO
import time

def callback(pin): 
   print("Pin {} was pressed".format(pin))
   GPIO.output(led,GPIO.HIGH)
   time.sleep(2)
   GPIO.output(led,GPIO.LOW)
try:
    pin = 9
    led=10
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led,GPIO.OUT)
    GPIO.setup(pin, GPIO.IN)
    
    GPIO.add_event_detect(pin, GPIO.FALLING, callback)

    while True:
        time.sleep(2000)
finally:
    GPIO.cleanup()
