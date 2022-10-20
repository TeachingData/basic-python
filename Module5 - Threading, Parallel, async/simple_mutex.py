import threading
import time

# do not use this - use Events with the functions included in the mutex library
# this is an example for students to understand the concept
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
        time.sleep(5)
    acquire()
    print("I got the mutex!")
    release()


def fun2():
    global mutex
    while mutex:
        time.sleep(5)
    acquire()
    print("I got the mutex as well!")
    release()

t1 = threading.Thread(target=fun1).start()
t2 = threading.Thread(target=fun2).start()
