import urllib.request
import sys

import Adafruit_DHT

import requests
import threading
import json
import time
import adafruit_dht
import RPi.GPIO as GPIO
TRIG = 18
ECHO = 24
channel=21
GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.IN)
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(channel, GPIO.IN)

def thingspeak_post():
 
 while(True):
  global sensor
  if GPIO.input(5) == 1:
   print ("LIGHT 0")
   c="LIGHT OFF"
   time.sleep(2)
  else:
   print ("LIGHT 1")
   c="LIGHT ON"
   time.sleep(2)
  if GPIO.input(channel):
   print ("No Water Detected!")
   water="Water absent"
  else:
   print ("Water Detected!")
   water="Water present"
  time.sleep(2)

  print ("Distance Measurement In Progress")
  #TRIG = 18
  #ECHO = 24
  #GPIO.setup(TRIG,GPIO.OUT)
  #GPIO.setup(ECHO,GPIO.IN)
  #GPIO.output(TRIG, False)
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
  if(distance<1024):
   print ("Distance:",distance,"cm")
  else:
   continue
  try:
   sensor=adafruit_dht.DHT22(12)
   sensor.measure()
   a=sensor.temperature
   print("The Temperature "+ str(a))
   b=sensor.humidity
   if(b>100):
    continue
   print("The humidity"+str(b))
   print("\n")
   URl='https://api.thingspeak.com/update?api_key='
   KEY='7LJU9O896AZ847RZ'
   HEADER='&field1={}&field2={}&field3={}&field4={}&field5={}'.format(humidity,temperature,c,distance,water)
   NEW_URL=URl+KEY+HEADER
   print(NEW_URL)
   data=urllib.request.urlopen(NEW_URL)
   time.sleep(5)
  except RuntimeError:
   continue
try: 
 
 TRIG = 18
 ECHO = 24
 GPIO.setmode(GPIO.BCM)
 GPIO.setup(5, GPIO.IN)
 GPIO.setup(TRIG,GPIO.OUT)
 GPIO.setup(ECHO,GPIO.IN)

 thingspeak_post()
except:
 GPIO.cleanup()

