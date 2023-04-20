# So this is a fun way to show off a sliding window algorithm and some fun you can do for hashing lists
# The first solution is pretty terrible run time (because of the generator its actually solid memory usage)
# Using this to discuss and build later solutions so will update with those later:
# from https://leetcode.com/problems/contains-duplicate-ii/

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        def slider(n, group):
            # I feel I'll need this at some point
            for i in range(len(n)-group+1):
                yield n[i:i+group]

        if len(nums) == 1:
            #return abs(nums[0]) <= k
            return False
        elif len(set(nums)) < len(nums):
            # trying this first (with dict) ... slow efficiency
            # using while and .idx...which should work with 
            # generator for better
            items = {}
            for i, e in enumerate(nums):
                if e not in items.keys():
                    items[e] = [i]
                else:
                    items[e].append(i)

            for v in items.values():
                if len(v) > 1:
                    for matches in slider(v, 2):
                        if abs(matches[0] - matches[1]) <= k:
                            return True

        return False
