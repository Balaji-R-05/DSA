# 709. To Lower Case

class Solution:
    def toLowerCase(self, s: str) -> str:
        ans = s.lower()
        return ans
    

class Solution:
    def toLowerCase(self, s: str) -> str:
        ans = ""
        for i in s:
            if i.isupper():
                ans += chr(ord(i)+32)
            else:
                ans += i
        return ans
    
# Time Complexity: O(n)
# Space Complexity: O(n)