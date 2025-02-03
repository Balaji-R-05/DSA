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

print(solution.removeStars("leet**cod*e"))
print(solution.removeStars("erase*****"))