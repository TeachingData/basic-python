import logging
import threading
import time
import sys
# this will handle and run a few write threads

# v3 - changed sleep thread to write to a file thread and now its appending
# single name file with each person on seperate line
def sleep_thread(name):
    logging.info(f"Thread {name}: starting")

    with open("names.txt",'a',encoding = 'utf-8') as personfile:
        personfile.write(f"name: {name}\nfor threading\n")

    logging.info(f"Thread {name}: finished")

if __name__ == "__main__":
    logging.basicConfig(format="%(asctime)s: %(message)s", level=logging.INFO,
            datefmt="%H:%M:%S")

    for i in sys.argv[1:]:
        logging.info(f"Main: Thread {i} creation started")
        slth = threading.Thread(target=sleep_thread, args=(i,))

        logging.info(f"Main: Thread {i} created, preparing to run")
        slth.start()

        logging.info(f"Main: Thread {i} launched - will notify when complete")
        logging.info("Rest of program running\n")
