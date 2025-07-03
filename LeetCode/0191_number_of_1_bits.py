# 191. Number of 1 Bits

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while(n>0):
            count += n&1
            n>>=1
        return count
    
# Time complexity: O(n) where n is the number of bits in the integer
# Space complexity: O(1)