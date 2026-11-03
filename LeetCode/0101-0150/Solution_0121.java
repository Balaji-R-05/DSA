//  121. Best Time to Buy and Sell Stock

class Solution {
    public int maxProfit(int[] prices) {
        int profit = 0;
        int curr = prices[0];
        for(int i=1; i<prices.length; i++) {
            if (prices[i] < curr) {
                curr = prices[i];
            } else if (prices[i] - curr > profit) {
                profit = Math.max(profit, prices[i] - curr);
            }
        }
        return profit;
    }
}

// Time Complexity: O(n) - We traverse the list of prices once
// Space Complexity: O(1) - We use a constant amount of space