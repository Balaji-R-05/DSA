class Solution_010 {
    int maxSubarraySum(int[] arr) {
        int curr = arr[0];
        int maxSum = arr[0];
        for (int i=1; i<arr.length; i++) {
            curr = Math.max(curr + arr[i], arr[i]);
            maxSum = Math.max(maxSum, curr);
        }
        return maxSum;
    }
}

// Time Complexity: O(N)
// Space Complexity: O(1)