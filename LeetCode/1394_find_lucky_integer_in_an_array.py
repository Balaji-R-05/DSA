# 1394. Find Lucky Integer in an Array

from typing import List

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        from collections import Counter

        arr = Counter(arr)
        maxNum = 0
        for i in arr:
            if i == arr[i] and i > maxNum:
                maxNum = i
        return maxNum if maxNum != 0 else -1
    
# Time Complexity: O(n)
# Space Complexity: O(n)