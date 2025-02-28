# 1281. Subtract the Product and Sum of Digits of an Integer

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod = 1
        s = 0
        while(n>0):
            rem = n%10
            prod*=rem
            s+=rem
            n//=10
        return prod-s
    
# Time complexity: O(log(n))
# Space complexity: O(1)
