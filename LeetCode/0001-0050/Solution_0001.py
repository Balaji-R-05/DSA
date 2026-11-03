from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in m:
                return [m[comp], i]
            m[num] = i
        return [-1, -1]

# Time complexity: O(n)
# Space complexity: O(n)