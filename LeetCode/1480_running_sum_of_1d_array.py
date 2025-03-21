# 1480. Running Sum of 1d Array

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            nums[i] = nums[i]+nums[i-1]
        return nums
    
# Time complexity: O(n)
# Space complexity: O(1)

