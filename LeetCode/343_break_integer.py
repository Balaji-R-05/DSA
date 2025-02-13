# 343. Integer Break

class Solution:
    def integerBreak(self, n: int) -> int:
        if n==2: return 1
        if n==3: return 2
        res = 0
        if n%3==0:
            res = 3**(n//3)
        elif n%3==1:
            res = 2*2*(3**(n//3-1))
        else:
            res = 2*3**(n//3)
        return res
    

# Time: O(1)
# Space: O(1)

# Approach: Math

print(Solution().integerBreak(10)) # 36
print(Solution().integerBreak(2)) # 1