# 303. Range Sum Query - Immutable

from typing import List
class NumArray:
    def __init__(self, nums: List[int]):
        self.arr = nums

    def sumRange(self, left: int, right: int) -> int:
        ans = 0
        while left <= right:
            ans += self.arr[left]
            left+=1
        return ans

# Time Complexity: O(n) for initialization, O(n) for sumRange in the worst case
# Space Complexity: O(n) for storing the nums array