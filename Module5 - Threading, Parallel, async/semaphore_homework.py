# Create a simple semephore with a 5 index queue

from datetime import date
import sys
import threading
import os

pool_sema = threading.BoundedSemaphore(value=5)


def calcage(year:int = 1900, month:int = 1, day:int = 1) -> int:
    dob = date(year, month, day)
    return (date.today() - dob).days // 365


def get_dob(name:str)->list:
    # could just be a list comprehension:
    # [int(input(f"Please enter your {prompt} of birth: ")) for prompt in ["year", "month", "day"]]
    # but this is bad anyway because we don't validate the times - would use library to get actual date
    # or add validation
    dob_ymd = []
    for prompt in ["year", "month", "day"]:
        dob_ymd.append(int(input(f"Please enter {name}'s {prompt} of birth: ")))
    return dob_ymd


def thread_function(first_name:str, last_name:str, dob:list):
    global pool_sema
    # using global mutex for locking

    # Age calc should be in thread (its just a calc) but not mutex
    age = calcage(dob[0], dob[1], dob[2])

    # critical section so use semaphore to add to its queue and process under lock
    with pool_sema:
        with open('mutexrules.txt', 'r+') as f:
            print(f.read())
            f.write(f"{first_name} {last_name}: {age} years old, born {dob[1]}/{dob[2]}/{dob[0]}\n")


if __name__ == "__main__":
    # You could use a simple list - I'm going to use a list of anonymous dictionaries
    # makes calling them easier later (not dependent on index)
    people = []
    
    for name in sys.argv[1:]:
        # not threading because input will be bottleneck and require join anyway
        people.append({
            "fname": name,
            "lname": input(f"What is {name}'s last name: "),
            "dob": get_dob(name)            })

    for person in people:
        # Now we can thread the names and dob of each person
        prth = threading.Thread(target=thread_function, args=(person["fname"], person["lname"], person["dob"]))
        prth.start()
