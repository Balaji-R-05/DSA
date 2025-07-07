# 268. Missing Number

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = (n*(n+1))//2
        s = sum(nums)
        return total-s
    
# Time Complexity: O(n)
# Space Complexity: O(1)