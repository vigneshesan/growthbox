import RPi.GPIO as GPIO  
GPIO.setmode(GPIO.BCM)  
import time
 
GPIO.setup(9, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

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

def my_callback(channel):
    while True:
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
        if(dist1<45 or dist2<45 or dist3<45 or dist4<45):
            print("Made high")
            time.sleep(2)
            print("Made low")
        time.sleep(1)
    
    
  

  
GPIO.add_event_detect(17, GPIO.RISING, callback=my_callback)  
  
try:  
    GPIO.wait_for_edge(9, GPIO.FALLING)  
    GPIO.cleanup()  
  
except KeyboardInterrupt:  
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit  
GPIO.cleanup()      
