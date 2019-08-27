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

    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)

    time.sleep(2000)
    GPIO.output(in1,LOW)
    GPIO.output(in2,LOW)
    GPIO.output(in3,LOW)
    GPIO.output(in4,LOW)

except KeyboardInterrupt:
    GPIO.cleanup()
