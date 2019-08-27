import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

try:
    in1=38
    in2=40
    in3=35
    in4=37

    GPIO.setup(in1,GPIO.OUT)
    GPIO.setup(in2,GPIO.OUT)
    GPIO.setup(in3,GPIO.OUT)
    GPIO.setup(in4,GPIO.OUT)

    print('motor high')

    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)

    time.sleep(2000)

except KeyboardInterrupt:
    GPIO.cleanup()