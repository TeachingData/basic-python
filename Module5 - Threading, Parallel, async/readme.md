**This follows the same iterated process I always
 apply. In all coding build small (tests) to 
 complex.**
 
 >*Threading* = no speed gain, single CPU process, used with "waiting"
 ><br> *Parallel* = speed gain, multi-CPU processes
 ><br> *async* = actually spawns a new coroutine
 
 1. Starts with threading using a function
     - [TempChange.py](./TempChange.py)   
 2. Moves to threading using an Object
 3. Parallel operations using similar steps
 4. A minor networked async example