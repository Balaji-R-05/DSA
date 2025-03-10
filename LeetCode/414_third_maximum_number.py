# 414. Third Maximum Number

from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = second = third = float("-inf")
        for num in nums:
            if num>first:
                third = second
                second = first
                first = num
            elif num<first and num>second:
                third = second
                second = num
            elif num>third and num<second:
                third = num

        return third if third!=float("-inf") else first
    
# Time Complexity: O(n)
# Space Complexity: O(1)