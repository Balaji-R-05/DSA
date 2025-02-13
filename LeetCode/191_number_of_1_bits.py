class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while(n>0):
            count += n&1
            n>>=1
        return count
    
# Time complexity: O(1)
# Space complexity: O(1)

solution = Solution()
n = 11
print(solution.hammingWeight(n)) # Output: 3

n = 128
print(solution.hammingWeight(n)) # Output: 1