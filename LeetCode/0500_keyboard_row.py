# 500. Keyboard Row
from typing import List

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = [set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")]
        ans = []

        for word in words:
            flag1 = flag2 = flag3 = False
            for ch in word.lower():
                if ch in rows[0]: flag1 = True
                elif ch in rows[1]: flag2 = True
                elif ch in rows[2]: flag3 = True
            if (flag1 + flag2 + flag3) == 1:
                ans.append(word)
        return ans
    
# Time: O(n * m), where n is the number of words and m is the average length of the words
# Space: O(1), since we are using a fixed number of sets for the rows