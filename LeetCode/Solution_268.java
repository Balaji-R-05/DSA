class Solution {
    public int missingNumber(int[] nums) {
        int length = nums.length,curr = 0;
        int sum = (length*(length+1))/2;
        for(int i=0;i<length;i++){
            curr+=nums[i];
        }
        return sum-curr;
    }
}

// Time Complexity: O(n) - We traverse the list of numbers once
// Space Complexity: O(1) - We use a constant amount of space