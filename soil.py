



#!/usr/bin/python
import RPi.GPIO as GPIO
import time
 
#GPIO SETUP
channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)
while(True): 
 if GPIO.input(channel):
  print ("No Water Detected!")
  water=0
 else:
  print ("Water Detected!")
  water=1
 time.sleep(2)
