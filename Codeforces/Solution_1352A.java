import java.util.*;

public class Solution_1352A {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int t = sc.nextInt();

    while (t-- > 0) {
      int n = sc.nextInt();
      int temp = n;
      int count = 0;

      while (temp > 0) {
        if (temp % 10 != 0) count++;
        temp /= 10;
      }
      System.out.println(count);
      
      int k = 1;
      while (n > 0) {
        int rem = n % 10;
        if (rem != 0) System.out.print(rem * k + " ");
        n /= 10;
        k *= 10;
      }
      System.out.println();
    }
    sc.close();
  }
}

// Time Complexity: O(log(N))
// Space Complexity: O(1)
