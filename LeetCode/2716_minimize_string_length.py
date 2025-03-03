# 2716. Minimize String Length

class Solution:
    def minimizedStringLength(self, s: str) -> int:
        return len(set(s))
    
# Time complexity: O(n)
# Space complexity: O(n)
