// 2278. Percentage of Letter in String

class Solution {
    public int percentageLetter(String s, char letter) {
        int count = 0;
        int length = s.length();
        for (int i = 0; i < length; i++) {
            if (s.charAt(i) == letter) {
                count++;
            }
        }
        int res = (int) (((double) count / length) * 100);
        return res;
    }
}

// Time Complexity: O(n)
// Space Complexity: O(1)