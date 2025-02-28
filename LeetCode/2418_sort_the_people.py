# 2418. Sort the People

from typing import List

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        combined = list(zip(names, heights))
        combined.sort(key=lambda x: x[1], reverse=True)
        sorted_names = [name for name, height in combined]
    
        return sorted_names
    
# Time complexity: O(nlogn)
# Space complexity: O(n)