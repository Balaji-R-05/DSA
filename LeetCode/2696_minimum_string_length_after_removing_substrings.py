# 2696. Minimum String Length After Removing Substrings

class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for c in s:
            if not stack:
                stack.append(c)
                continue
            if c =="B" and stack[-1]=="A":
                stack.pop()
            elif c=="D" and stack[-1]=="C":
                stack.pop()
            else:
                stack.append(c)
        return len(stack)
    
# Time complexity: O(n)
# Space complexity: O(n)
