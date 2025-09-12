from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res
    
# Time Complexity: O(n) - We traverse the list of numbers once
# Space Complexity: O(1) - We use a constant amount of space