import java.util.*;

public class AWC_0026_A {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        long N = sc.nextLong();
        long K = sc.nextLong();
        sc.nextLine();
        for(int i=0; i<N; i++) {
            long num = sc.nextLong();
            if ((i+1)%K == 0) {
                System.out.print(num + " ");
            }
        }
        System.out.println();
        sc.close();
    }
}

// Time Complexity: O(N)
// Space Complexity: O(1).