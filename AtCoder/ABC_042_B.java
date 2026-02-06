import java.util.*;

public class ABC_042_B {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        // int L = sc.nextInt();
        String[] arr = new String[N];
        for (int i = 0; i < N; i++) {
            arr[i] = sc.next();
        }
        Arrays.sort(arr);
        for (int i = 0; i < N; i++) {
            System.out.print(arr[i]);
        }
        sc.close();
    }
}

// Time Complexity: O(N log N)
// Space Complexity: O(N)