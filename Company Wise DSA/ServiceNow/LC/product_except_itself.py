from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroCount = nums.count(0)
        if zeroCount > 1:
            return [0] * len(nums)
        
        if zeroCount == 1:
            total = 1
            for i in nums:
                if i == 0: continue
                total *= i
            
            res = [0] * len(nums)
            for i in range(len(nums)):
                if nums[i] == 0:
                    res[i] = total
            return res
        else:
            total = 1
            for i in nums:
                total *= i
            res = [0] * len(nums)
            for i in range(len(nums)):
                res[i] = total // nums[i]
            return res

            
# Time Complexity: O(n)
# Space Complexity: O(1)