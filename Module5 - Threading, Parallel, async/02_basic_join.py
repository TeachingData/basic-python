import logging
import sys
import threading
import time

def readwrite_function(name):

    with open("names.txt", 'r') as namesfile:
        print(namesfile.read())

    # lets read then reopen for the append instead of r+
    with open("names.txt", 'a') as namesfile:
        message = input("Please enter your message: ")
        namesfile.write(f"thread name is {name}\t{message}\n")
        time.sleep(5)
        namesfile.write(f'{time.strftime("%H:%M:%S", time.localtime())}: Thread {name} is done\n')
    # to solve just add to write: print(f"Thread {name} is done") #this is going to cause a problem
    # but that doesn't solve the read - the read would take a join


if __name__ == "__main__":
    # This will show the difference between .join and not running .join as example
    # This is an ill suited example for using .join because of the sleep but a good iteration for making
    #            a mediator class later
    for n in sys.argv[1:]:
        prth = threading.Thread(target=readwrite_function, args=(n,))
        prth.start()
        prth.join()
