# 3498. Reverse Degree of a String

class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            x = ord(s[i])
            x = abs(x-122) + 1
            ans += (x * (i+1))
        return ans
    
# Time Complexity: O(n)
# Space Complexity: O(1