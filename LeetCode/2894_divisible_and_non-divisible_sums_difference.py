# 2894. Divisible and Non-divisible Sums Difference

class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1 = 0
        num2 = 0
        for x in range(m, n+1, m):
            num2 += x  # Sum of numbers divisible by m
        for x in range(1, n+1):
            num1 += x # Sum of numbers from 1 to n
        num1 -= num2  # Remove numbers divisible by m
        return num1-num2
    
# Time complexity: O(n)
# Space complexity: O(1)

