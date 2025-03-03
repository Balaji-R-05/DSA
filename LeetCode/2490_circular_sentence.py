# 2490. Circular Sentence

class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        s = sentence.split()
        for i in range(0,len(s)-1):
            if s[i][-1]!=s[i+1][0]:
                return False
        if s[0][0] != s[-1][-1]:
            return False
        return True
    
# Time complexity: O(n)
# Space complexity: O(1)