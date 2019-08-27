import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
ws1=5
ws2=6
ws3=13
def ws(pin):
 GPIO.setup(pin, GPIO.IN)
 a=GPIO.input(pin)
 print(a)
 if (GPIO.input(pin) == 0):
  return("water absent")
  print("there is no water")
 if(GPIO.input(pin)==1):
  print("there is water")
  return("water present")
if __name__ == '__main__':
 try:
  while True:
   p1=ws(ws1)
   print(p1)
   p2=ws(ws2)
   print(p2)
   p3=ws(ws3)
   print(p3)
   time.sleep(1)
 except KeyboardInterrupt:
  print("Measurement stopped by User")
  GPIO.cleanup()
