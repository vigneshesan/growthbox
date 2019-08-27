import signal
import sys
import time
def func():
    while True:
        print("haha")
        time.sleep(2)
def signal_handler(signal,frame):
    print("u pressed")
    func()
signal.signal(signal.DFL,signal_handler)
print("press Clt c")
signal.pause()
    