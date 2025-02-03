# 20. Valid Parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)==1:
            return False
        stk = []
        d = {"(":")","{":"}","[":"]"}
        for i in s:
            if i in d:
                stk.append(i)
            elif stk!=[] and d[stk[-1]]==i:
                stk.pop()
            else:
                return False
        return stk==[]
    
solution = Solution()

s = "()"
print(solution.isValid(s))
s = "()[]{}"
print(solution.isValid(s))
s = "(]"
print(solution.isValid(s))
s = "([])"
print(solution.isValid(s))