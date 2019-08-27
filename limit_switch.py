import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(13,GPIO.IN)
while True:
    print(GPIO.input(13))
    if GPIO.input(13)==1:
        print("high")
    print("hah")
    time.sleep(1)