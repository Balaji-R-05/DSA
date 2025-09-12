from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for num in nums:
            if num in s:
                return True
            s.add(num)
        return False
    
# Time Complexity: O(n) - We traverse the list of numbers once
# Space Complexity: O(n) - In the worst case, we may store all numbers in