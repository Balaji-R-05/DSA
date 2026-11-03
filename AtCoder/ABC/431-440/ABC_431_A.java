import java.util.*;

public class ABC_431_A {
  public static void main(String args[]) {
    Scanner sc = new Scanner(System.in);
    int H = sc.nextInt();
    int B = sc.nextInt();
    if (H > B) {
      System.out.println(H-B);
    } else {
      System.out.println(0);
    }
    sc.close();
  }
}

// Time Complexity: O(1)
// Space Complexity: O(1)