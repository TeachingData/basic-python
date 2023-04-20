# these are not complete and don't directly answer any question but are meant to show algorithms

"""
So duplicates could use a brute-force method which is basically a bubble sort:
   double for loop: first loops thourgh 0-end, second loops through 1-end
   returns False (no dups) if it gets through both, returns True the minute it finds a duplicate
   
If you see a double for-loop - its "bad-code smell" (not nesscarily wrong but typically inefficient)

Second version shown is what I see from many applicatants (trying to be Pythonic) - its not just uses some built-ins
   Without thinking about O() notation: why is this only a little more memory efficient and faster than the brute force?
       If helps (0 and 1 elements cannot be faster than just returning).
       Count the number of times it has to loop over values - there are 3

Third version shown is checkSet: convert to set (sets have to be unique values) and see if same length as list
   if it is: return False (no dup) if its not: return True (at least 1 dup)
   This is much faster and efficient then brute force but a set lookup is around O(1) so ...can get a bit better
   Try and figure out why the last version is faster (its still a set and if I needed the duplicates for stuff I'd use this)
   
Use a Counter (either the collection tool or make your own with normal dictionary)
"""

def bruteForce (n_list: List[int]) -> bool:
        # Using a list slice to ignore first number in 2nd for
        for i in n_list:
            for j in n_list[1:]:
               if i == j: return True
        return False

   
def fancierNotFaster(self, n_list: List[int]) -> bool:
        # Yep this helps: ignores a few cases
        if len(n_list) <= 1:
            # if empty or only 1 element cannot have dups
            return False

        # wonder if I can use Counter - yep, horrible though
        return any([i-1 for i in Counter(n_list).values()])

      
def checkSet(n_list: List[int]) -> bool:
        # if empty list or only 1 element we know no dups:
        if len(n_list) <= 1:
            return False
        
        # baseline just convert to set and check length
        s = set(n_list)
        if len(s) < len(n_list):
            return True
        return False

# The next two are variance on set answer - first has slight memory improvement & second has slight speed increase   

def checkSetComprehension(n_list: List[int]) -> bool:
        # Fun fact - this is the same speed but comprehension makes it use around ~.1Mb less memory
        # Also removes need fro first if check (cause 0 length would just exit comprhension and 1 len just one pass)
        s = {e for e in nums}

        if len(s) < len(nums):
            return True
        return False
   

def individualCheckSet(n_list: List[int]) -> bool:
   # This has same memory usage as checkSet but is a bit faster above - why?
        if len(nums) <= 1:
            # if empty or only 1 element cannot have dups
            return False
        # Here we will make a set but not initiate it with the list
        s = set()

        # now we will manually add in each element
        for e in nums:
            if not len(s):
                # 0 = False, anything else = True
                s.add(e)
            else:
                if e in s:
                    return True
                else:
                    s.add(e)
        return False
