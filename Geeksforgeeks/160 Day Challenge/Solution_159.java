class Solution_159 {
    public int findUnique(int[] arr) {
        int res = 0;
        for(int num: arr) {
            res ^= num;
        }
        return res;
    }
}

// Time Complexity: O(N)
// Space Complexity: O(1)