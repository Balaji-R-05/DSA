class Solution_003 {
    public void reverseArray(int arr[]) {
        int i = 0;
        int j = arr.length - 1;
        int temp;
        while (i < j) {
            temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
            i++;
            j--;
        }
    }
}

// Time Complexity: O(N)
// Space Complexity: O(1)