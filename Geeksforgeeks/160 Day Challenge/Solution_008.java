class Solution_008 {
    public int maximumProfit(int prices[]) {
        int curr = prices[0];
        int maxProfit = 0;
        for(int price: prices) {
            if (price < curr) {
                curr = price;
            }
            maxProfit = Math.max(price - curr, maxProfit);
        }
        return maxProfit;
    }
}

// Time Complexity: O(N)
// Space Complexity: O(1)