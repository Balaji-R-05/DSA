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
    
solution = Solution()

# Time complexity: O(n)
# Space complexity: O(n)

print(solution.removeStars("leet**cod*e")) # lecoe
print(solution.removeStars("erase*****")) #

# Note: 
# The input will be generated such that the operation is always possible.
# It can be shown that the resulting string will always be unique.