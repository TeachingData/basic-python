from random import random
from threading import Thread
from threading import Semaphore
from time import sleep

# our thread function
def some_task(semaphore, number):
    # attempt to acquire semaphore
    with semaphore:
        # critical section
        r_value = random()
        sleep(r_value)
        #Hopefully not to bad
        print(f'Thread {number} sleeped for {r_value}')

#create a semaphore
semaphore = Semaphore(2)
#make a bunch of threads to fork
for i in range(10):
    worker = Thread(target=some_task, args=(semaphore, i)).start()
