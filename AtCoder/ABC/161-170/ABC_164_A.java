import java.util.*;

public class ABC_164_A {
  public static void main(String args[]) {
    Scanner sc = new Scanner(System.in);
    int S = sc.nextInt();
    int W = sc.nextInt();
    if (W >= S) {
      System.out.println("unsafe");
    } else {
      System.out.println("safe");
    }
    sc.close();
  }
}

// Time Complexity: O(1)
// Space Complexity: O(1)