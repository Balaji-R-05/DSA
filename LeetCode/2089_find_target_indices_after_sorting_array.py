# 2089. Find Target Indices After Sorting Array

from typing import List

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i]==target: res.append(i)
        
        return res
    
# Time complexity: O(nlogn)
# Space complexity: O(1)