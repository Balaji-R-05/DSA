# 3190. Find Minimum Operations to Make All Elements Divisible by Three

from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            if i%3!=0: count+=1 #`count` stores the number of elements that are not divisible by 3

        return count
    
# Time complexity: O(n)
# Space complexity: O(1)

