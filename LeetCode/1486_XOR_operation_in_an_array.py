# 1486. XOR Operation in an Array

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        res = 0
        for i in range(n):
            res ^= start + 2*i
        
        return res
    
# Time complexity: O(n)
# Space complexity: O(1)

