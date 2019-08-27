import RPi.GPIO as GPIO
import time
import ssl
import RPi.GPIO as GPIO
import time
from firebase import firebase
import cv2
import os
import shutil
import time


#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

#set GPIO Pins
TRIG = 5
ECHO = 6
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
GPIO.output(4, GPIO.LOW)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(13,GPIO.IN)
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

### State Machine
# Initialisation - > when reset is pressed, while (15<=h<=20) stay the same else if h < 15 moveUp and elif h > 20 moveDown
# Run time - height check, water check, timer based lighting, photo capture one day:


def my_callback(channel):
    #fpo
    #if (ultrasonic check 15-20)
    #goUp()
    
    print("Program Reseted")
    while True:
        print(GPIO.input(13))
        if GPIO.input(13)==0:
            break
        print("motor run")
        print("motor up")
        GPIO.output(in1,GPIO.LOW)
        print("Made high down")
        GPIO.output(in2,GPIO.HIGH)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)
        
        
    
    
GPIO.add_event_detect(17, GPIO.FALLING, callback=my_callback,bouncetime=300)
try:
 while True:
    
    print("Image captured")

       
    for i in range (8):
        flag=0
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
         
        if((dist1>15 and dist1<20) or(dist2>15 and dist2<20) or (dist3>15 and dist3<20) or (dist4>15 and dist4<20)):
            GPIO.output(in1,GPIO.LOW)
            print("Made low")
            GPIO.output(in2,GPIO.LOW)
            GPIO.output(in3,GPIO.LOW)
            GPIO.output(in4,GPIO.LOW)
            
        elif(dist1<15 or dist2<15 or dist3<15 or dist4<15):
            print("motor up")
            GPIO.output(in1,GPIO.LOW)
            print("Made high down")
            GPIO.output(in2,GPIO.HIGH)
            GPIO.output(in3,GPIO.LOW)
            GPIO.output(in4,GPIO.HIGH)
            
            time.sleep(180)
            
            GPIO.output(in1,GPIO.LOW)
            print("Made low")
            GPIO.output(in2,GPIO.LOW)
            GPIO.output(in3,GPIO.LOW)
            GPIO.output(in4,GPIO.LOW)
            
        elif(dist1>20 or dist2>20 or dist3>20 or dist4>20):
            print("motor down")
            GPIO.output(in1,GPIO.HIGH)
            print("Made high down")
            GPIO.output(in2,GPIO.LOW)
            GPIO.output(in3,GPIO.HIGH)
            GPIO.output(in4,GPIO.LOW)
            
            time.sleep(180)
            
            GPIO.output(in1,GPIO.LOW)
            print("Made low")
            GPIO.output(in2,GPIO.LOW)
            GPIO.output(in3,GPIO.LOW)
            GPIO.output(in4,GPIO.LOW)
            
    
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
    time.sleep(1)
    data = {"distance1": dist1, "distance2": dist2,"distance3":dist3,"distance4":dist4}
    firebase.post('/sensor/ultrasonic', data)
    data={"water":water}
    firebase.post('/sensor/water',data)
    #data={"watersens1":l1,"watersens2":l2,"watersnes3":l3}
    #firebase.post('/sensor/watersensor',data)
    GPIO.output(4, GPIO.LOW)
    print("I'm ON")
    time.sleep(5)
    GPIO.output(4, GPIO.HIGH)
    print("I'm OFF")
    time.sleep(1)
    time.sleep(10)
except KeyboardInterrupt:
 GPIO.output(in1,GPIO.LOW)
 GPIO.output(in2,GPIO.LOW)
 GPIO.output(in3,GPIO.LOW)
 GPIO.output(in4,GPIO.LOW)
 
 GPIO.cleanup()

