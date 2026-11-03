import java.util.*;

public class ABC_427_B {
  public static void main(String args[]) {
    Scanner sc = new Scanner(System.in);
    int N = sc.nextInt();
    int[] arr = new int[N+1];
    arr[0] = 1;
    for (int i=1; i<=N; i++) {
      int sum = 0;
      for(int j=0; j<i; j++) {
        sum += helper(arr[j]);
      }
      arr[i] = sum;
    }
    System.out.println(arr[N]);
    sc.close();
  }
  
  public static int helper(int n) {
    int res = 0;
    while (n > 0) {
      res += n%10;
      n /= 10;
    }
    return res;
  }
}