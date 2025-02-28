# 2798. Number of Employees Who Met the Target

from typing import List

class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        return len([i for i in hours if i>=target])
    
# Time complexity: O(n)
# Space complexity: O(1)

