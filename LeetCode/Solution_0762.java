// 762. Prime Number of Set Bits in Binary Representation

public class Solution_0762 {
    public int countPrimeSetBits(int left, int right) {
        int count = 0;
        for(int i=left; i<=right; i++) {
            int temp = 0;
            int j = i;
            while (j > 0) {
                temp += j & 1;
                j >>= 1;
            }
            if (isPrime(temp)) {
                count++;
            }
        }
        return count;
    }

    public boolean isPrime(int num) {
        if (num < 2) {
            return false;
        }
        for(int i=2; i*i <= num; i++) {
            if (num%i == 0) {
                return false;
            }
        }
        return true;
    }
}

// Time Complexity: O((R-L) * log R)
// Space Complexity: O(1)