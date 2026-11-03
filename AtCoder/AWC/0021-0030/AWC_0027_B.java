import java.util.*;

public class AWC_0027_B {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] arr = new int[N];
        for(int i=0; i<N; i++) {
            arr[i] = sc.nextInt();
        }
        int idx = 0;
        int leadVal = arr[idx];
        for(int i=1; i<N; i++) {
            if (arr[i] > leadVal) {
                leadVal = arr[i];
                idx = i;
            }
        }
        System.out.println((idx!=0) ? idx+1 : -1);
        sc.close();
    }
}

// Time Complexity: O(N)
// Space Complexity: O(1)