// 11. Container With Most Water

class Solution {
    public int maxArea(int[] height) {
        int left = 0, right = height.length-1;
        int volume, max_volume = 0;
        while (left<right){
            volume = Math.min(height[right], height[left]) * (right-left);
            max_volume = Math.max(volume, max_volume);
            if (height[left]<height[right]){
                left++;
            }else{
                right--;
            }
        }
        return max_volume;
    }
}

// Time Complexity: O(N)
// Space Complexity: O(1)