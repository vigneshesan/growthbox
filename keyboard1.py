import signal
import time
def keyboardInterruptHandler(signal,frame):
    print("entered again")
    while True:
        
        print("ahgjsdkj")
        time.sleep(1)
signal.signal(signal.SIGINT,keyboardInterruptHandler)
print("enterhds")

while True:
    pass