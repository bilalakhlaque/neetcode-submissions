class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''   
        # Lets try a double for loop.
        # For each i, let us go through the entire list and see if 
        # it appears again when compared to j. J is i+1, next element.
        # This will satisfy the "appears more than once in the array".
        # for * for == n * n == O(n^2) should be the time complexity
        # Because we are only ever traversing through the list, its space complexity is O(1).

        for i in range(len(nums)):
            for j in range(i+1,len(nums)): # Do not iterate past the length of the list
                if (nums[i] == nums[j]):
                    return True
        return False

        # Hash-map approach
        # We ideally would want to optimize for run-time efficiency.
        # We could use a hash-set. Recall that we want to remember every number we have ALREADY seen. 
        # So lets use a set. It can store an object like a list as the value.
        # We want to create an empty set -> 
        # see if each number is in the array object, which is in the set "seen". If it is, true, theres a duplicate. 
        # Else, meaning it has not been seen before, store that number in the set.
        # Time complexity is O(n) because we are iterating through a list n number of times. 
        # Space is also O(n) because we are adding to that set at max, n amount of times.
        '''
        seen = set()

        for number in nums:
            if number in seen:
                return True
            else:
                seen.add(number)
        
        return False