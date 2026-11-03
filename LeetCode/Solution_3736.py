# 3736. Minimum Moves to Equal Array Elements III

from typing import List

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        m = max(nums)
        count = 0
        for num in nums:
            count += m - num
        return count

# Time Complexity: O(N)
# Space Complexity: O(1)