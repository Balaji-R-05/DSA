import java.util.*;

public class ABC_164_B {
  public static void main(String args[]) {
    Scanner sc = new Scanner(System.in);
    int a = sc.nextInt();
    int b = sc.nextInt();
    int c = sc.nextInt();
    int d = sc.nextInt();
    if (a/d + (a%d == 1 ? 1:0) >= c/b + (c%b == 1 ? 1:0)) {
      System.out.println("Yes");
    } else {
      System.out.println("No");
    }
    sc.close();
  }
}

// Time Complexity: O(1)
// Space Complexity: O(1)