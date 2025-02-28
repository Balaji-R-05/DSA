# 2942. Find Words Containing Character

from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res = []
        for i in range(len(words)):
            if x in words[i]:
                res.append(i)
        return res
    
# Time complexity: O(n*m)
# Space complexity: O(1)
