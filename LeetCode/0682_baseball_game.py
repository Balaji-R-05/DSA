# 682. Baseball Game

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk = []
        s = set(["+", "C", "D"])
        for i in operations:
            if i not in s:
                stk.append(int(i))
            else:
                if i == "+":
                    stk.append(stk[-1] + stk[-2])
                elif i == "D":
                    stk.append(stk[-1]*2)
                elif i=="C":
                    stk.pop()

        return sum(stk)
    
# Time Complexity: O(N)
# Space Complexity: o(N)