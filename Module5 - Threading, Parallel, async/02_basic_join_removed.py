# a simple thread adventure - We added join in the last version
# but join is horrible for fixing the algorithm which introduced a race_condition
# Students were tasked with finding a way to alter the algorithm and better fix the threading
# This is one example of a non-join answer for the problem

from random import random
import sys
import threading
import time


def readask_function(name) -> str:
    # Still first thing is to read the file
    # Then we return the input they gave
    # so we can use the function as a direct call
    with open("names.txt", 'r') as namesfile:
        print(namesfile.read())
    return input("Please enter your message: ")
  
  
def writesleep_function(name, message, s):
    # here is were we would consider using a mutex lock
    time.sleep(s) # wait to simulate mutex which we create in lesson 2
    with open("names.txt", 'a') as namesfile:
        namesfile.write(f"thread name is {name}\t{message}\n")
        namesfile.write(f'{time.strftime("%H:%M:%S", time.localtime())}: Thread {name} is done\n')
        
        
if __name__ == "__main__":
    # So our input is the bottleneck and threading doesn't help with it
    # Threading will help with a wait and write function that we just want to get done when it gets done
    # answer was to move these two operations to a seperate function and then only thread them
    for n in sys.argv[1:]:
        prth = threading.Thread(target=writesleep_function, args=(n, readask_function(n), random()+2))
        prth.start()
