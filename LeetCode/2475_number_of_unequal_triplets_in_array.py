# 2475. Number of Unequal Triplets in Array

from typing import List

class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if nums[i] != nums[j] and nums[i] != nums[k] and nums[j] != nums[k]:
                        count+=1
        
        return count
    
# Time complexity: O(n^3)
# Space complexity: O(1)