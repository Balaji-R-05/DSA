# 1047. Remove All Adjacent Duplicates In String

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for c in s:
            if not stack:
                stack.append(c)
                continue
            if c==stack[-1]:
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)
    
# Time complexity: O(n)
# Space complexity: O(n)