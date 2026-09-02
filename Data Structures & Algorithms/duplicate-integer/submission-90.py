class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''   
        # Lets try a double for loop.
        # For each i, let us go through the entire list and see if 
        #it appears again when compared to j. J is i+1, next element.
        # This will satisfy the "appears more than once in the array".
        # for * for == n * n == O(n^2) should be the time complexity
        for i in range(len(nums)):
            for j in range(i+1,len(nums)): # Do not iterate past the length of the list
                if (nums[i] == nums[j]):
                    return True
        return False

        # Hash-map approach 
        '''
        seen = set()

        for number in nums:
            if number in seen:
                return True
            else:
                seen.add(number)
        
        return False