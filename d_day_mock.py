import RPi.GPIO as GPIO
import time
import ssl
import RPi.GPIO as GPIO
import time

import cv2
import os
import shutil
import time


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

while True:
    
    print("Image captured")

       
    for i in range (8):
        
         
    
            GPIO.output(in1,GPIO.LOW)
            print("Made low")
            GPIO.output(in2,GPIO.LOW)
            GPIO.output(in3,GPIO.LOW)
            GPIO.output(in4,GPIO.LOW)
            
        
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


