class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        count = 0
        while n>0:
            count += n&1
            n>>=1
        return count==1

# Time complexity: O(log(n))
# Space complexity: O(1)

solution = Solution()
print(solution.isPowerOfTwo(n = 16))

print(solution.isPowerOfTwo(n = 3))

# Edge Cases
# n == 0 
# n == 2**31-1 and n == -2**31
