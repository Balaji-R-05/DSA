// 3452. Sum of Good Numbers

class Solution {
    public int sumOfGoodNumbers(int[] nums, int k) {
        int n = nums.length;
        int sum = 0;
        int left, right;
        for(int i=0; i<n; i++){
            left = (i-k>=0)? nums[i-k]: Integer.MIN_VALUE;
            right = (i+k<n)? nums[i+k]: Integer.MIN_VALUE;
            if (left< nums[i] && right<nums[i]){
                sum += nums[i];
            }
        }
        return sum;
    }
}

// Time Complexity: O(n)
// Space Complexity: O(1)