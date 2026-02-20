// 693. Binary Number with Alternating Bits

class Solution_0693 {
    public boolean hasAlternatingBits(int n) {
        String bits = Integer.toBinaryString(n);
        for (int i = 0; i < bits.length() - 1; i++) {
            if (bits.charAt(i) == bits.charAt(i+1)) {
                return false;
            }
        }
        return true;
    }
}

// Time Complexity: O(log N)
// Space Complexity: O(1)