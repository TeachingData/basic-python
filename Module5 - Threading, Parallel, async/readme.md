**This follows the same iterated process I always
 apply. In all coding build small (tests) to 
 complex.**
 
 >*Threading* = not always a speed gain, due to GPL its still: single CPU process of single CPU, used with "waiting" or backend processes with little user interruption it is still useful (and may increase speed in those cases)
 ><br> *Parallel* = speed gain, multi-CPU processes
 ><br> *async* = actually spawns a new coroutine
 
 1. Starts with threading using a function
     - [01_basic_threading.py](./01_basic_threading.py) shows how to import and run a very small sleep thread generator
     - [01a_basic_threading.py](./01a_basic_threading.py) basically same as 01 but shows writting (v2) and appending (v3) to a file(s)
     - [01b_basic_threading.py](./01b_basic_threading.py) so here we added a read then write process (much like a chatroom) but not correctly. We need to add a mediator class/function to handle our other threads and ensure everyone can read/write correctly. It is meant to fail as an example for students.
     - 02_basicjoin.py (and alpha): used to show a basic join and for students to correct
     - [TempChange.py](./TempChange.py) (this is just an example of the structure)
     - A realworld example will be added later
 2. Moves to threading using an Object
 3. Parallel operations using Pool (over Process)
     - [TempChangeWithPool.py](./TempChangeWithPool.py)
 4. A minor networked async example
