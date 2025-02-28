# 977. Squares of a Sorted Array

from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i, j = 0, n-1
        res = [0]*n
        for k in reversed(range(n)):
            if nums[i]**2 > nums[j]**2:
                res[k] = nums[i]**2
                i+=1
            else:
                res[k] = nums[j]**2
                j-=1
        return res
    
# Time complexity: O(n)
# Space complexity: O(1)