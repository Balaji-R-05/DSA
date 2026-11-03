import java.util.*;

public class AWC_0026_C {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int T = sc.nextInt();
        long E = sc.nextLong();
        sc.nextLine();
        long[] arr = new long[N];
        for(int i=0; i<N; i++) {
            arr[i] = sc.nextLong();
        }
        Arrays.sort(arr);
        int res = 0;
        long curr = 0;
        for(long snack: arr) {
            if (curr + (T*snack) <= E) {
                curr += T*snack;
                res++;
            } else {
                break;
            }
        }
        System.out.println(res);
        sc.close();
    }
}

// Time Complexity: O(N log N)
// Space Complexity: O(N).