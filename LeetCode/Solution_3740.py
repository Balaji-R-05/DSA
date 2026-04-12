# 3740. Minimum Distance Between Three Equal Elements I

from typing import List

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        res = float("inf")
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if nums[i] == nums[j] == nums[k]:
                        dist = abs(i-j) + abs(j-k) + abs(k-i)
                        res = min(dist, res)
        return res if res != float("inf") else -1
    
# Time Complexity: O(n^3) - We have three nested loops to check all combinations of three indices
# Space Complexity: O(1) - We use a constant amount of space to store the