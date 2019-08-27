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
for i in range(10):
    cap=cv2.VideoCapture(0)
    ret,img=cap.read()
    cv2.imwrite('/home/pi/images/img_'+str(i).zfill(4)+'.png',img)
    print("Image captured")
    cap.release()
    time.sleep(1)
    
images=[img for img in os.listdir('/home/pi/images') if img.endswith(".png")]
frame=cv2.imread(os.path.join('/home/pi/images',images[0]))
height,width,layers=frame.shape

video=cv2.VideoWriter('final.mp4',0,2,(1920,1080))

for image in images:
    video.write(cv2.imread(os.path.join('/home/pi/images',image)))
 
cv2.destroyAllWindows()
print("video done")
video.release()
shutil.rmtree('/home/pi/images')

file1=drive.CreateFile()
file1.SetContentFile('/home/pi/final.mp4')
file1.Upload()
    
