# 1470. Shuffle the Array

from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for i in range(n):
            res.append(nums[i])
            res.append(nums[i+n])
        return res
    
# Time Complexity: O(n)
# Space Complexity: O(1)

