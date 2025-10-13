import java.util.*;

public class ABC_412_A {
  public static void main(String args[]) {
    Scanner sc = new Scanner(System.in);
    int N = sc.nextInt();
    int res = 0;
    int target, completed;
    while (N-- > 0) {
      target = sc.nextInt();
      completed = sc.nextInt();
      if (completed > target) {
        res++;
      }
    }
    System.out.println(res);
    sc.close();
  }
}