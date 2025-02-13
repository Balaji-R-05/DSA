# 121. Best Time to Buy and Sell Stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            if prices[i]<min_price:
                min_price = prices[i]
            elif prices[i]-min_price > profit:
                profit = prices[i]-min_price
        
        return profit
    
# Time complexity: O(n)
# Space complexity: O(1)

