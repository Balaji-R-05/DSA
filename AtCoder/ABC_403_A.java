import java.util.*;

public class ABC_403_A {
  public static void main(String args[]) {
    Scanner sc = new Scanner(System.in);
    int N = sc.nextInt();
    int[] arr = new int[N];
    int total = 0;
    for(int i=0; i<N; i++) {
      arr[i] = sc.nextInt();
      if (i%2==0) {
        total += arr[i];
      }
    }
    System.out.println(total);
    sc.close();
  }
}

// Time Complexity: O(N)
// Space Complexity: O(1)