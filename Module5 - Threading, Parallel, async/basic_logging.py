import logging
import sys

# This is used with threading to explain the basic logging functions with the built-in library
# Students used this as a base when building own assignments

def stuff_function(somelist):
    logging.info(", ".join([str(i) for i in somelist]))

    
if __name__ == "__main__":
    logfile = ""

    try:
        logfile = sys.argv[1]
    except IndexError:
        logfile = "standardlog.log"

    logging.basicConfig(format="%(asctime)s: %(message)s", level=logging.INFO,
            datefmt="%m/%d/%Y %H:%M:%S", filename=logfile)

    logging.info("Starting")

    testlist = [10,22,34,89]

    for i in range(0,10):
        testlist.append(i)
        stuff_function(testlist)
    logging.info("Complete")
