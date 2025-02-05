# 2220. Minimum Bit Flips to Convert Number

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        flips = 0
        while start>0 or goal>0:
            bit_start = start & 1
            bit_goal = goal & 1
            if bit_start != bit_goal:
                flips += 1

            start >>= 1
            goal >>= 1

        return flips
    
# Time complexity: O(n)
# Space complexity: O(1)

solution = Solution()
print(solution.minBitFlips(start = 10, goal = 7))
print(solution.minBitFlips(start = 3, goal = 4))