# 268. Missing Number

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = (n*(n+1))//2
        s = sum(nums)
        return total-s
    
# Time Complexity: O(n) - We traverse the list of numbers once
# Space Complexity: O(1) - We use a constant amount of space