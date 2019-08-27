
import RPi.GPIO as GPIO
import time
from firebase import firebase 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
TRIG = 23
ECHO = 24
TRIG1=14
ECHO1=15
TRIG2=2
ECHO2=3
TRIG3=27
ECHO3=22

in1 = 20
in2 = 21
in3=19
in4=26
firebase = firebase.FirebaseApplication('https://growthbox-8b3ef.firebaseio.com/', None)

#set GPIO direction (IN / OUT)
#GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
#GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)

GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
 
def distance(GPIO_TRIGGER,GPIO_ECHO):
 GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
 GPIO.setup(GPIO_ECHO, GPIO.IN)


    # set Trigger to HIGH
 GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
 time.sleep(0.00001)
 GPIO.output(GPIO_TRIGGER, False)
 
 StartTime = time.time()
 StopTime = time.time()
 
    # save StartTime
 while GPIO.input(GPIO_ECHO) == 0:
  StartTime = time.time()
 
    # save time of arrival
 while GPIO.input(GPIO_ECHO) == 1:
  StopTime = time.time()
 
    # time difference between start and arrival
 TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
 distance = (TimeElapsed * 34300) / 2
 
 return distance

##def ws(pin):
## GPIO.setup(pin, GPIO.IN)
## a=GPIO.input(pin)
## print(a)
## if (GPIO.input(pin) == 0):
##  return("water absent")
##  print("there is no water")
## if(GPIO.input(pin)==1):
##  print("there is water")
##  return("water present")
 
if __name__ == '__main__':
 l1="Absent"
 l2="Absent"
 l3="Absent"
 try:
  while True:
   dist1 = distance(TRIG,ECHO)
   print ("Measured Distance from the first 90 degree= %.1f cm" % dist1)
   time.sleep(1)

   dist2 = distance(TRIG1,ECHO1)
   print ("Measured Distance from the second 90 degree= %.1f cm" % dist2)
   time.sleep(1)

   dist3 = distance(TRIG2,ECHO2)
   print ("Measured Distance from the third 90 degree= %.1f cm" % dist3)
   time.sleep(1)

   dist4 = distance(TRIG3,ECHO3)
   print ("Measured Distance from the fourth 90 degree= %.1f cm" % dist4)
   time.sleep(1)
   if(dist1<45 or dist2<45 or dist3<45 or dist4<45):
    GPIO.output(in1,GPIO.HIGH)
    print("Made high")
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)
    time.sleep(5)
    GPIO.output(in1,GPIO.LOW)
    print("Made low")
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)
##   p1=ws(ws1)
##   if(p1==0):
##    l1="Absent"
##   if(p1==1):
##    l1="Present"
##   print(p1)
##   p2=ws(ws2)
##   if(p2==0):
##    l2="Absent"
##   if(p2==1):
##    l2="Present"
##
##   print(p2)
##   p3=ws(ws3)
##   if(p3==0):
##    l3="Absent"
##   if(p3==1):
##    l3="Present"
##   print(p3)
##   print(str(l1))
##   print(str(l2))
##   print(str(l3))
   time.sleep(1)
   data = {"distance1": dist1, "distance2": dist2,"distance3":dist3,"distance4":dist4}
   firebase.post('/sensor/ultrasonic', data)
   #data={"watersens1":l1,"watersens2":l2,"watersnes3":l3}
   #firebase.post('/sensor/watersensor',data)
   time.sleep(10)
 except KeyboardInterrupt:
  print("Measurement stopped by User")
  GPIO.cleanup()
