# 2278. Percentage of Letter in String

class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        count = 0
        n = len(s)
        for i in s:
            if i == letter:
                count += 1
        return floor((count/n)*100)
    
# Time complexity: O(n)
# Space complexity: O(1)