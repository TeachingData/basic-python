# a simple thread adventure - this version adds both a join and a simple start for examples
# meant as a basic iteration for understanding and setting up a mediator class and chatroom
import logging
import sys
import threading
import time

def readwrite_function(name):

    # now we can use that read and then append because the join is waiting
    with open("names.txt", 'r+') as namesfile:
        print(namesfile.read())
        message = input("Please enter your message: ")
        namesfile.write(f"thread name is {name}\t{message}\n")

def wait_function(name):
    # Now to fix let's wait seperately in a new thread
    # But wait is not really working - it just slows it - so what I really need is an input
    # But I don't want an input.... I need an EVENT! continued with reactive/event based processes
    time.sleep(5)
    with open("names.txt", 'a') as namesfile:
        namesfile.write(f'{time.strftime("%H:%M:%S", time.localtime())}: Thread {name} is done\n')


if __name__ == "__main__":
    for n in sys.argv[1:]:
        prth = threading.Thread(target=readwrite_function, args=(n,))
        prth.start()
        prth.join()

    for n in sys.argv[1:]:
        prth = threading.Thread(target=wait_function, args=(n,))
        prth.start()
