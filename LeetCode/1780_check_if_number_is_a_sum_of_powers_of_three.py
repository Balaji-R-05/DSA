# 1780. Check if Number is a Sum of Powers of Three

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while (n>0):
            if n%3==2:
                return False
            n//=3
        
        return True
    
# Time complexity: O(logn)
# Space complexity: O(1)

# Hints
"""
- Let's note that the maximum power of 3 you'll use in your soln is 3^16
- The number can not be represented as a sum of powers of 3 if it's ternary presentation has a 2 in it
"""