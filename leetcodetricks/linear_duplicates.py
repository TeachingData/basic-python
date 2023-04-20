# these are not complete and don't directly answer any question but are meant to show algorithms

"""
So duplicates could use a brute-force method which is basically a bubble sort:
   double for loop: first loops thourgh 0-end, second loops through 1-end
   returns False (no dups) if it gets through both, returns True the minute it finds a duplicate
   
If you see a double for-loop - its "bad-code smell" (not nesscarily wrong but typically inefficient)

Second version shown in checkSet: convert to set (sets have to be unique values) and see if same length as list
   if it is: return False (no dup) if its not: return True (at least 1 dup)
"""
def checkSet(n_list: List[int]) -> bool:
        # if empty list or only 1 element we know no dups:
        if len(n_list) <= 1:
            return False
        
        # baseline just convert to set and check length
        s = set(n_list)
        if len(s) < len(n_list):
            return True
        return False
