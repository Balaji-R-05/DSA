import java.util.*;

public class ABC_431_B {
  public static void main(String args[]) {
    Scanner sc = new Scanner(System.in);
    int X = sc.nextInt();
    int N = sc.nextInt();
    int[] parts = new int[N];
    boolean[] flag = new boolean[N];
    for(int i=0; i<N; i++) {
      parts[i] = sc.nextInt();
    }
    int Q = sc.nextInt();
    while (Q-- > 0) {
      int cmd = sc.nextInt() - 1;
      if (!flag[cmd]) {
        flag[cmd] = true;
        X += parts[cmd];
      } else {
        flag[cmd] = false;
        X -= parts[cmd];
      }
      System.out.println(X);
    }
    sc.close();
  }
}

// Time Complexity: O(N)
// Space Complexity: O(1)