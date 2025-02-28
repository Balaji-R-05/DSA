# 2006. Count Number of Pairs With Absolute Difference K

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = 0
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if abs(nums[i]-nums[j])==k: count+=1

        return count
    
# Time complexity: O(n^2)
# Space complexity: O(1)

# --------------------------------------------------------------------------------------------------------------------------------

from collections import Counter
from typing import List

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        freq = Counter(nums)
        count = 0
        
        for num in freq:
            if num + k in freq:  # Check if the complement exists
                count += freq[num] * freq[num + k]
        
        return count
    
# Time complexity: O(n)
# Space complexity: O(n)
