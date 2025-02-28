# 2652. Sum Multiples

class Solution:
    def sumOfMultiples(self, n: int) -> int:
        sumMultiples = 0
        for i in range(1,n+1):
            if i%3==0 or i%5==0 or i%7==0:
                sumMultiples += i
        
        return sumMultiples
    
# Time complexity: O(n)
# Space complexity: O(1)