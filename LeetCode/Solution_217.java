import java.util.*;

class Solution_217 {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> seen = new HashSet<>();
        for(int num: nums) {
            if (seen.contains(num)) {
                return true;
            }
            seen.add(num);
        }
        return false;
    }
}

// Time Complexity - O(N)
// Space Complexity - O(N)