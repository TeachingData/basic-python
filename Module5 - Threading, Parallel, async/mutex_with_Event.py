import threading
import time

mutex = threading.Lock()
# not a global but a reference to a defined function

def fun1():
    while True:
        mutex.acquire()
        print("I'm in the mutex!")
        mutex.release()
        # we are going to need the next line
        # you have to interrupt out
        time.sleep(2)

def fun2():
    while True:
        mutex.acquire()
        print("ME TOO!")
        mutex.release()
        time.sleep(2)

t1 = threading.Thread(target=fun1).start()
t2 = threading.Thread(target=fun2).start()
