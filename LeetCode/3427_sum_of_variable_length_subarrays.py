# 3427. Sum of Variable Length Subarrays

class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            start = max(0,i-nums[i])
            res += sum(nums[start:i+1])
        return res
    
# Time complexity: O(n^2)
# Space complexity: O(1)