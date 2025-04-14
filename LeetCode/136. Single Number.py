# 136. Single Number

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums: res ^= num
        return res
    
# Time complexity: O(n)
# Space complexity: O(1)

# Test cases

s = Solution()
print(s.singleNumber(nums=[4,1,2,1,2]))
print(s.singleNumber(nums=[2,2,1]))
