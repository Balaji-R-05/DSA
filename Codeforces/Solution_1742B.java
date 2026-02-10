import java.util.HashSet;
import java.util.Scanner;

public class Solution_1742B {
        public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
 
        while (T-- > 0) {
            int n = sc.nextInt();
            HashSet<Long> set = new HashSet<>();
 
            for (int i = 0; i < n; i++) {
                long x = sc.nextLong();
                set.add(x);
            }
 
            if (set.size() == n) {
                System.out.println("YES");
            } else {
                System.out.println("NO");
            }
        }
        sc.close();
    }
}

// Time Complexity: O(T*N)
// Space Complexity: O(N).