import java.util.*;

public class Solution_1829B {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        while (T-- > 0) {
            int N = sc.nextInt();
            int[] arr = new int[N];
            for(int i=0; i<N; i++) {
                arr[i] = sc.nextInt();
            }
            int maxLen = 0;
            int curr = 0;
            for(int i=0; i<N; i++) {
                if (arr[i] == 0) {
                    curr++;
                } else {
                    curr = 0;
                }
                maxLen = Math.max(curr, maxLen);
            }
            System.out.println(maxLen);
        }
        sc.close();
    }
}

// Time Complexity: O(T*N)
// Space Complexity: O(N).
