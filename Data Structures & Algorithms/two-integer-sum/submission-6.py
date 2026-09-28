class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        #Brute force
        # Always remember, range stop is non-inclusive
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target and i != j: 
                    # if true and I am not on the same index, return
                    return [i,j]
        # Run-time: O(n^2)
        # Space Comp: O(1)
        '''
        # Optimized
        seen = {}
        for i, num in enumerate(nums):
            remainder = target - num
            if remainder in seen:
                return [seen[remainder], i]
            seen[num] = i

        # Run-time: O(n)
        # Space-comp: O(n)