import java.util.*;

public class ABC_429_B {
  public static void main(String args[]) {
    Scanner sc = new Scanner(System.in);
    int N = sc.nextInt();
    int K = sc.nextInt();
    int[] arr = new int[N];
    int total = 0;
    for(int i=0; i<N; i++) {
      arr[i] = sc.nextInt();
      total += arr[i];
    }
    for(int i=0; i<N; i++){
      if (total - arr[i] == K) {
        System.out.println("Yes");
        return;
      }
    }
    System.out.println("No");
    sc.close();
  }
}
