# 263. Ugly Number

class Solution:
    def isUgly(self, n: int) -> bool:
        if n<=0:
            return False
        while n>0:
            if n%2==0:
                n//=2
            elif n%3==0:
                n//=3
            elif n%5==0:
                n//=5
            else:
                break
        return n==1
    
# Time complexity: O(logn)
# Space complexity: O(1)

# Approach: Keep dividing the number by 2, 3 and 5 until the number becomes 1. If the number is not divisible
# by 2, 3 or 5 then return False. If the number becomes 1 then return True. If the number is less than or equal
# to 0 then return False.

print(Solution().isUgly(6)) # True
print(Solution().isUgly(8)) # True
print(Solution().isUgly(14)) # False