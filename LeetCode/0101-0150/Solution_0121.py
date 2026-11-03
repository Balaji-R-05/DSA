from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            if prices[i]<start:
                start = prices[i]
            elif prices[i]-start>profit:
                profit = prices[i]-start
        return profit

# Time Complexity: O(n) - We traverse the list of prices once
# Space Complexity: O(1) - We use a constant amount of space