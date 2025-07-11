// 41. First Missing Positive

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int firstMissingPositive(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();
        for(int num:nums) {
            map.put(num, 1);
        }
        for (int ctr=1;; ctr++) {
            if (!map.containsKey(ctr)){
                return ctr;
            }
        }
    }
}

// Time Complexity: O(n)
// Space Complexity: O(n)