class Solution {
    public int strStr(String haystack, String needle) {
        int n = haystack.length();
        int k = needle.length();
        for(int i=0; i<n-k+1; i++) {
            boolean match = true;
            for(int j=0; j<k; j++) {
                if (haystack.charAt(i+j) != needle.charAt(j)) {
                    match = false;
                    break;
                }
            }
            if (match) {
                return i;
            }
        }
        return -1;
    }
}

// Time Complexity: O(n × k)
// Space Complexity: O(1)