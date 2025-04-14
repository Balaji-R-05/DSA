# 231. Power of Two

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        count = 0
        while n>0:
            count += n&1
            n>>=1
        return count==1
    


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0: return False
        while(n%2==0):
            n//=2
        return n==1
    
# Time complexity: O(log(n))
# Space complexity: O(1)

# Edge Cases
# n == 0 
# n == 2**31-1 and n == -2**31