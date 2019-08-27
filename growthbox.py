
import ssl
import RPi.GPIO as GPIO
import time
from firebase import firebase
import cv2
import os
import shutil
import time
from pydrive.auth import GoogleAuth
gauth=GoogleAuth()
gauth.LocalWebserverAuth()
from pydrive.drive import GoogleDrive
drive=GoogleDrive(gauth)

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
water_trig=5
water_echo=6
in1 = 20
in2 = 21
in3=19
in4=26

#SSLSocket.getpeercert()
firebase = firebase.FirebaseApplication('https://plantapp-90209.firebaseio.com', None)

GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)
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


 
if __name__ == '__main__':

 try:
  os.mkdir("/home/pi/images")
  cap=cv2.VideoCapture(0)
  ret,img=cap.read()
  cv2.imwrite('/home/pi/images/img_.png',img)
  print("Image captured")
  cap.release()
  time.sleep(1)
    

 
  cv2.destroyAllWindows()


  file1=drive.CreateFile()
  file1.SetContentFile('/home/pi/images/img_.png')
  file1.Upload()
    

  shutil.rmtree('/home/pi/images')
  GPIO.output(4, GPIO.LOW)
  print("I'm ON")
  time.sleep(5)
  GPIO.output(4, GPIO.HIGH)
  print("I'm OFF")
  time.sleep(1)
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
   
   water_pres= distance(water_trig,water_echo)
   print ("water present= %.1f cm" % water_pres)
   time.sleep(1)
   water_pres=14-water_pres
   print(water_pres)
   if(water_pres==4):
       water="water present"
   elif(water_pres>4):
       water="More water"
       
   elif(water_pres>2 and water_pres<2):
       water="Add 1 litre water"
   else:
       water="In need of water"
   print(water)
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

   time.sleep(1)
   data = {"distance1": dist1, "distance2": dist2,"distance3":dist3,"distance4":dist4}
   firebase.post('/sensor/ultrasonic', data)
   data={"water":water}
   firebase.post('/sensor/water',data)
   #data={"watersens1":l1,"watersens2":l2,"watersnes3":l3}
   #firebase.post('/sensor/watersensor',data)
   time.sleep(10)
 except KeyboardInterrupt:
  print("Measurement stopped by User")
  GPIO.cleanup()

