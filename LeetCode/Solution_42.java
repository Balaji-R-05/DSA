// 42. Trapping Rain Water

class Solution {
    public int trap(int[] height) {
        int vol = 0;
        int i = 0, j = height.length - 1;
        int lmax = height[i], rmax = height[j];  // Initialize lmax and rmax correctly
        
        while (i < j) {
            if(height[i] <= height[j]) {
                if (height[i] < lmax) {
                    vol += lmax - height[i];
                }else {
                    lmax = height[i];
                }
                i++;
            }else{
                if(height[j] < rmax) {
                    vol += rmax - height[j];
                }else{
                    rmax = height[j];
                }
                j--;
            }
        }  
        return vol;
    }
}

// Time complexity: O(n)
// Space complexity: O(1)
