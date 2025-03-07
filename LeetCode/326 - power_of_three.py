# 326. Power of Three

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0: return False
        while n % 3 == 0: n //= 3
        return n == 1
    
# Time complexity: O(log n)
# Space complexity: O(1)
