import cv2
import time
def imagecap():
 cam=cv2.VideoCapture(0)
 s,im=cam.read() 
 return(im)
flag=0
while(1):
 time.sleep(2)
 cam=imagecap()
 cv2.imwrite("/home/pi/timelapse/image{}.jpg".format(flag),cam)
 print("entered")
 flag=flag+1
