class Solution_001 {
    public int getSecondLargest(int[] arr) {
        int num1 = Integer.MIN_VALUE;
        int num2 = Integer.MIN_VALUE;
        
        for(int num: arr) {
            if (num > num1) {
                num2 = num1;
                num1 = num;
            } else if (num != num1 && num > num2) {
                num2 = num;
            }
        }
        
        if (num2 == Integer.MIN_VALUE) {
            return -1;
        }
        return num2;
    }
}

// Time Complexity: O(N)
// Space Complexity: O(1)