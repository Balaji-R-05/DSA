public class Solution_002 {
    public void moveZeros(int[] arr) {
        int count = 0;
        for(int i = 0; i < arr.length; i++) {
            if(arr[i] != 0) {
                arr[count] = arr[i];
                count++;
            }
        }
        while(count < arr.length) {
            arr[count] = 0;
            count++;
        }
    }
}

// Time Complexity: O(N)
// Space Complexity: O(1)
