// 977. Squares of a Sorted Array

class Solution {
    public int[] sortedSquares(int[] nums) {
        int n = nums.length;
        int i = 0, j = n - 1;
        int[] res = new int[n];
        
        for (int k = n - 1; k >= 0; k--) {
            if (nums[i] * nums[i] > nums[j] * nums[j]) {
                res[k] = nums[i] * nums[i];
                i++;
            } else {
                res[k] = nums[j] * nums[j];
                j--;
            }
        }       
        return res;  
    }
}

// Time Complexity - O(N)
// Space Complexity - O(N)