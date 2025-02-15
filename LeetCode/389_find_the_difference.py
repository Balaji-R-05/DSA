# 389. Find the Difference

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        res = 0

        for char in s + t:
            res ^= ord(char)
        return chr(res)
    
# Time complexity: O(n)
# Space complexity: O(1)

print(Solution().findTheDifference("abcd", "abcde")) # "e"
print(Solution().findTheDifference("", "y")) # "y"