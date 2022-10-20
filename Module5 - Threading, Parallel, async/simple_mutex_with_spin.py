import threading
import time

# mutex is not locked so False
mutex = False

def acquire():
    global mutex
    #if mutex False its unlocked so Lock it and continue
    if not mutex:
        # now locked so True
        mutex = True
    return mutex

def release():
    global mutex
    mutex = False


def fun1():
    global mutex
    while mutex:
        continue
    acquire()
    print("I got the mutex!")
    release()


def fun2():
    global mutex
    while mutex:
        continue
    acquire()
    print("I got the mutex as well!")
    release()

t1 = threading.Thread(target=fun1).start()
t2 = threading.Thread(target=fun2).start()
