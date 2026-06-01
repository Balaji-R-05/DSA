# 2144. Minimum Cost of Buying Candies With Discount

from typing import List

class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        n = len(cost)
        res = 0
        i = 0
        while i < n:
            res += cost[i]
            i += 1
            if i >= n:
                break
            res += cost[i]
            i += 2
        return res

# Time Complexity: O(N log N)
# Space Complexity: O(1)
