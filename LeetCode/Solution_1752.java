// 1752. Check if Array Is Sorted and Rotated

class Solution {
    public boolean check(int[] nums) {
        int i, count = 0, numsLength = nums.length;
        for (i = 0; i < numsLength - 1; i++) {
            if (nums[i] > nums[i + 1]) {
                count++;
            }
        }
        if (nums[numsLength - 1] > nums[0]) {
            count++;
        }
        return count <= 1;
    }
}

// Time Complexity: O(n)
// Space Complexity: O(1)

