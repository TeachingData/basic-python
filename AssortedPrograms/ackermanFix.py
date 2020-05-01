''' 
Created due to the amount of people who use a bad example from 
Learn Python the Hard Way - never, ever use that book.
'''

class Memorize(object):
    '''
    Instead of using a global variable for the cache the Pythonic way is to use
    a decorator class to build a cache. Functions are objects in Python so this
    passes the decorated function (ack) as parameter.

    So *basically* this will wrap the ack function so its init will create a
    cache which is updated on calls.
    '''
    def __init__(self, function):
        self.func = function
        self.cache = {}

    def __call__(self, *args):
        if args in self.cache:
            return self.cache[args]
        retain = self.func(*args)
        self.cache[args] = retain
        return retain


def getNum():
    '''
    Get user input and use a try/except to verify it is a number.
    This is to demonstrate that it is better to ask for forgivness than
    permission in Python.
    '''
    user_num = input("Please enter the number for evaluation: ")
    try: 
        return int(user_num)
    except ValueError:
        print("\n\nInput should be a Whole Number\n\n")
        raise #could use sys.exit(1) or handle otherwise too

@Memorize
def ack(m, n):
    '''
    A two-argument Ackermann–Péter function model

    Standard Given A(m,n) -> if m == 0: n + 1
                             if m > 0 and n == 0: A(m - 1, 1)
                             if m > 0 and n > 0: A(m - 1), A(m, n - 1)
    '''
    if m == 0:
        return n + 1
    elif n == 0:
        return ack(m - 1, 1)
    else:
        return ack(m - 1, ack(m, n - 1))

'''
Main *Function*:
Just to show that you do not need a main function in Python
Gets user values, runs through function, and displays any errors.
'''
firstNum = getNum()
secondNum = getNum()

print(ack(firstNum, secondNum))
