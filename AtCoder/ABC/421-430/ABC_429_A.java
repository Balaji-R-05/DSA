import java.util.*;

public class ABC_429_A {
  public static void main(String args[]) {
    Scanner sc = new Scanner(System.in);
    int N = sc.nextInt();
    int M = sc.nextInt();
    for(int i=0; i<N; i++) {
      if (i < M) {
        System.out.println("OK");
      } else {
        System.out.println("Too Many Requests");
      }
    }
    sc.close();
  }
}

// Time Complexity: O(N)
// Space Complexity: O(1)