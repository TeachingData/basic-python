**This follows the same iterated process I always
 apply. In all coding build small (tests) to 
 complex.**
 
 >*Threading* = no speed gain (one this code), single CPU process of single CPU, used with "waiting"
 ><br> *Parallel* = speed gain, multi-CPU processes
 ><br> *async* = actually spawns a new coroutine
 
 1. Starts with threading using a function
     - [01_basic_threading.py](./01_basic_threading.py) shows how to import and run a very small sleep thread generator
     - [TempChange.py](./TempChange.py) (this is just an example of the structure)
     - A realworld example will be added later
 2. Moves to threading using an Object
 3. Parallel operations using Pool (over Process)
     - [TempChangeWithPool.py](./TempChangeWithPool.py)
 4. A minor networked async example
