import RPi.GPIO as GPIO  
GPIO.setmode(GPIO.BCM)  
import time
import signal
import time

GPIO.setup(9, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
def keyboardInterruptHandler(signal,frame):
    print("entered again")
    while True:
        
        print("ahgjsdkj")
        time.sleep(1)
signal.signal(signal.SIGINT,keyboardInterruptHandler)
print("enterhds")

while True:
    pass