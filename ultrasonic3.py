import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

TRIG =27 
ECHO =24
TRIG1=23
ECHO1=15
TRIG2=14
ECHO2=3


def distance(TRIG,ECHO):

 print ("Distance Measurement In Progress")

 GPIO.setup(TRIG,GPIO.OUT)
 GPIO.setup(ECHO,GPIO.IN)
 GPIO.setup(TRIG1,GPIO.OUT)
 GPIO.setup(ECHO1,GPIO.IN)
 GPIO.setup(TRIG2,GPIO.OUT)
 GPIO.setup(ECHO2,GPIO.IN)
 
 GPIO.output(TRIG, False)
 print ("Waiting For Sensor To Settle")
 time.sleep(2)

 GPIO.output(TRIG, True)
 time.sleep(0.00001)
 GPIO.output(TRIG, False)

 while GPIO.input(ECHO)==0:
   pulse_start = time.time()

 while GPIO.input(ECHO)==1:
   pulse_end = time.time()

 pulse_duration = pulse_end - pulse_start

 distance = pulse_duration * 17150

 distance = round(distance, 2)

 print ("Distance:",distance,"cm")

 GPIO.cleanup()
if __name__ == '__main__':
 try:
  while True:
   dist = distance(TRIG,ECHO)
   dist1=distance(TRIG1,ECHO1)
   dist2=distance(TRIG2,ECHO2)
   time.sleep(1)
 except KeyboardInterrupt:
   print("Measurement stopped by User")
   GPIO.cleanup()

