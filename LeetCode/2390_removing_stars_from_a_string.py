# 2390. Removing Stars From a String

class Solution:
    def removeStars(self, s: str) -> str:
        stk = []
        for i in s:
            if not stk or i != "*":
                stk.append(i)
            else:
                stk.pop()
        return "".join(stk)

# Time complexity: O(n)
# Space complexity: O(n)