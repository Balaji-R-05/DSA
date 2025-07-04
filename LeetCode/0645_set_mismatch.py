# 645. Set Mismatch

from typing import List
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        from collections import Counter
        count = Counter(nums)

        duplicate = missing = 0
        n = len(nums)
        
        for i in range(1, n + 1):
            if count[i] == 2:
                duplicate = i
            elif count[i] == 0:
                missing = i
        
        return [duplicate, missing]
    
# Time Complexity: O(n)
# Space Complexity: O(n)