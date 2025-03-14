# 1502. Can Make Arithmetic Progression From Sequence

from typing import List

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff = arr[1]-arr[0]
        for i in range(1,len(arr)):
            if arr[i]-arr[i-1] != diff: return False
        return True
    
# Time: O(nlogn)
# Space: O(1)
