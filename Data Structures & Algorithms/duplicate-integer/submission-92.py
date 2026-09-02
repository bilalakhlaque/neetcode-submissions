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

        # Hash-set approach
        # We ideally want to optimize for runtime efficiency.
        # We could use a hash-set. Recall that we want to remember every number we have ALREADY seen. 
        # We want to create an empty set -> 
        # For each number in the list, check if it has been seen. If yes, return True.
        # Else, meaning it has not been seen before, store that number in the set.
        # Time complexity is O(n) because we are iterating through a list n number of times. 
        # Space is also O(n) because, at worst case, we add all numbers n numbers to the set.
        '''
        seen = set()

        for number in nums:
            if number in seen:
                return True
            else:
                seen.add(number)
        
        return False