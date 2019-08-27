import RPi.GPIO as GPIO  
GPIO.setmode(GPIO.BCM)  
import time
 
GPIO.setup(9, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def my_callback(channel):
    print("Returned back")
    
GPIO.add_event_detect(17, GPIO.FALLING, callback=my_callback,bouncetime=300)  
  
try:  
    GPIO.wait_for_edge(9, GPIO.RISING)  
    GPIO.cleanup()  
  
except KeyboardInterrupt:  
    my_callback()      # clean up GPIO on CTRL+C exit  
GPIO.cleanup()      

