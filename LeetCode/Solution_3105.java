// 3105. Longest Strictly Increasing or Strictly Decreasing Subarray

class Solution {
    public int longestMonotonicSubarray(int[] nums) {
        if (nums.length == 1) return 1;
        int inc_length = 1, dec_length = 1, max_length = 1;
        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i] < nums[i + 1]) { 
                inc_length++;
                dec_length = 1;
            } 
            else if (nums[i] > nums[i + 1]) { 
                dec_length++;
                inc_length = 1;
            } 
            else { 
                inc_length = dec_length = 1;
            }
            max_length = Math.max(max_length, Math.max(inc_length, dec_length));
        }
        return max_length;
    }
}

// Time Complexity: O(N)
// Space Complexity: O(1)