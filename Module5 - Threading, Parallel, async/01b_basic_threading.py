import logging
import threading
import time
import sys
# this will handle and run a few file creation threads
# Except it won't - Used as example of why Mediator Design Pattern is needed here
#                   This will fail to correctly write to files and has other bugs.
#                   Fixing it to work will be a student task.

# v2 - changed sleep thread to write to a file thread
# v3 - changed file thread to now open for reading and then appending a message from the client
# Each file is seperate per person (persons_name.txt)
def person_thread(name):
    logging.info(f"Thread {name}: starting")

    with open(f"names.txt",'r+',encoding = 'utf-8') as personfile:
        logging.info(f"The file currently contains:\n{personfile.read()}")

        message = input(f"Hi {name}! Enter chat message: ")
        personfile.write(f"name: {name}: {message}\n")

    logging.info(f"Thread {name}: finished")

if __name__ == "__main__":
    logging.basicConfig(format="%(asctime)s: %(message)s", level=logging.INFO,
            datefmt="%H:%M:%S")

    for i in sys.argv[1:]:
        logging.info(f"Main: Thread {i} creation started")
        slth = threading.Thread(target=person_thread, args=(i,))

        logging.info(f"Main: Thread {i} created, preparing to run")
        slth.start()

        logging.info(f"Main: Thread {i} launched - will notify when complete")
        logging.info("Rest of program running\n")
