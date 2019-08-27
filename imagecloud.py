import cv2
import os
import shutil
import time
from pydrive.auth import GoogleAuth
gauth=GoogleAuth()
gauth.LocalWebserverAuth()
from pydrive.drive import GoogleDrive
drive=GoogleDrive(gauth)


os.mkdir("/home/pi/images")

cap=cv2.VideoCapture(0)
ret,img=cap.read()
cv2.imwrite('/home/pi/images/img_.png',img)
print("Image captured")
cap.release()
time.sleep(1)
    

 
cv2.destroyAllWindows()



file1=drive.CreateFile()
file1.SetContentFile('/home/pi/images/img_.png')
file1.Upload()
    
shutil.rmtree('/home/pi/images')
