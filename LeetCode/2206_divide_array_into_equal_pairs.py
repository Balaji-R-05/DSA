# 2206. Divide Array Into Equal Pairs

from typing import List
from collections import Counter

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        nums = Counter(nums)
        for i in nums:
            if nums[i]%2==1:
                return False
        return True
    
# Time complexity: O(n)
# Space complexity: O(n)