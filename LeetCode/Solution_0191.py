# 191. Number of 1 Bits

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while (n > 0):
            count += n & 1
            n >>= 1
        return count

# Time Complexity: O(1) - Since the number of bits in an integer is fixed (32 or 64 bits)
# Space Complexity: O(1) - No additional space is used that scales with input size