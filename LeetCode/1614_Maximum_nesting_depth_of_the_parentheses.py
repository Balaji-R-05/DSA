# 1614. Maximum Nesting Depth of the Parentheses

class Solution:
    def maxDepth(self, s: str) -> int:
        maxLength = 0
        stk = []
        count = 0
        for i in range(len(s)):
            if s[i]=='(':
                count+=1
            elif s[i]==')':
                maxLength = max(count, maxLength)
                count-=1

        return maxLength
    
# Time Complexity: O(n)
# Space Complexity: O(1)