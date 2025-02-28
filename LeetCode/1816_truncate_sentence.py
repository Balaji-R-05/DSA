# 1816. Truncate Sentence

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s = s.split()
        return " ".join(s[:k])
    
# Time Complexity: O(n)
# Space Complexity: O(n)