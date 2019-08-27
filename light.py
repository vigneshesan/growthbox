import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
for i in range(0,5):
    GPIO.output(7, GPIO.LOW)
    print("I'm ON")
    time.sleep(2)
    GPIO.output(7, GPIO.HIGH)
    print("I'm OFF")
    time.sleep(1)
 
