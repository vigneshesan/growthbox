import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(9, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Button to GPIO23
GPIO.setup(10, GPIO.OUT)  #LED to GPIO24


try:
    while True:
        
        GPIO.add_event_detect(9,GPIO.RISING)
        
        if GPIO.event_detected(9):
            print("Button pressed")
        
except:
    GPIO.cleanup()