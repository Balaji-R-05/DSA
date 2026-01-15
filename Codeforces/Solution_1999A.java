import java.util.Scanner;

public class Solution_1999A {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        int N, res;
        while (T-- > 0) {
          N = sc.nextInt();
          res = 0;
          while (N > 0) {
            res += N % 10;
            N /= 10;
          }
          System.out.println(res);
        }
        sc.close();
    }
}

// Time Complexity: O(1)
// Space Complexity: O(1)