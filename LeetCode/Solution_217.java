// 217. Contains Duplicate

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

// Time Complexity: O(n)
// Space Complexity: O(n)