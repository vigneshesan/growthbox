import RPi.GPIO as GPIO  
GPIO.setmode(GPIO.BCM)  
import time
import signal
import time

GPIO.setup(9, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

class Error(Exception):
    "Base class"
    pass
class Buttonpressed(Error):
    
    