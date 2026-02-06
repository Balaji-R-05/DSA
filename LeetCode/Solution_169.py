# 169. Majority Element

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = 0
        for num in nums:
            if num == candidate:
                count += 1
            elif count == 0:
                candidate = num
            else:
                count -= 1
        return candidate
    
# Time Complexity: O(n) - We traverse the list once
# Space Complexity: O(1) - We use a constant amount of space