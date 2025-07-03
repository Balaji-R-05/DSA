# 7. Reverse Integer

class Solution:
    def reverse(self, x: int) -> int:
        negative=x<0
        x=abs(x)
        rnum=0
        while(x!=0):
            rnum=rnum*10+(x%10)
            x//=10
        if rnum>2**31-1:
            return 0
        return -rnum if negative else rnum
    
# Time complexity: O(log(x))
# Space complexity: O(1)

