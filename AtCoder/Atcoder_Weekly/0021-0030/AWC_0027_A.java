import java.util.*;

public class AWC_0027_A {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int S = sc.nextInt();
        int T = sc.nextInt();
        sc.nextLine();
        int num, res = 0;
        for(int i=0; i<N; i++) {
            num = sc.nextInt();
            if (Math.abs(num - S) <= T) {
                res++;
            }
        }
        System.out.println(res);
        sc.close();
    }
}

// Time Complexity: O(N)
// Space Complexity: O(1)