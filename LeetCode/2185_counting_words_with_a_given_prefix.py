# 2185. Counting Words With a Given Prefix

from typing import List

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        n = len(pref)
        for word in words:
            if word[:n]==pref:
                count+=1
        return count
    
# Time complexity: O(n)
# Space complexity: O(1)

# ------------------------------------------------------------------------------------------------------------------------


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for word in words:
            if word.startswith(pref):
                count+=1
        return count
    
# Time complexity: O(n)
# Space complexity: O(1)