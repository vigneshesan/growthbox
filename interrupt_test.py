import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(13,GPIO.IN)

### State Machine
# Initialisation - > when reset is pressed, while (15<=h<=20) stay the same else if h < 15 moveUp and elif h > 20 moveDown
# Run time - height check, water check, timer based lighting, photo capture one day:



def goUp():
    
    pass

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
        
        
    
GPIO.add_event_detect(17, GPIO.FALLING, callback=my_callback,bouncetime=300)

while True:
    time.sleep(1)
    print("Ok")

