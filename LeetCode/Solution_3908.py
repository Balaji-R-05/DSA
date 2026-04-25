# 3908. Valid Digit Number

class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        n = str(n)
        x = str(x)
        if n[0] == x:
            return False
        if x in n:
            return True
        return False
    
# Time complexity: O(log(n))
# Space complexity: O(log(n))