import cv2
import urllib.request
import requests
import threading
import json
import time
import RPi.GPIO as GPIO
channel=21
TRIG = 18
ECHO = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.IN)
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)	
GPIO.setup(channel, GPIO.IN)

def thingspeak_post():
 flag=0
 while(True):
  time.sleep(2)
  cam=cv2.VideoCapture(0)
  s,im=cam.read()
  cam=im
  cv2.imwrite("/home/pi/timelapse/image{}.jpg".format(flag),cam)
  print("entered")
  flag=flag+1

  if GPIO.input(5) == 1:
   print ("LIGHT 0")
   c=0
   time.sleep(2)
  else:
   print ("LIGHT 1")
   c=1
   time.sleep(2)
  if GPIO.input(channel):
   print ("No Water Detected!")
   water=0
  else:
   print ("Water Detected!")
   water=1
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
  if(distance<1024):
   print ("Distance:",distance,"cm")
  else:
   continue

  URl='https://api.thingspeak.com/update?api_key='
  KEY='O40MFQM51YV3ZFD0'
  #HEADER='&field1={}&field2={}&field3={}&field4={}&field5={}'.format(a,b,c,distance,water)
  HEADER='&field1={}&field2={}&field3={}'.format(c,water,distance)
  NEW_URL=URl+KEY+HEADER
  print(NEW_URL)
  data=urllib.request.urlopen(NEW_URL)
  time.sleep(600)
try:
 thingspeak_post()
except:
 GPIO.cleanup()

