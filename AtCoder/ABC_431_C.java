import java.util.*;

public class ABC_431_C {
  public static void main(String args[]) {
    Scanner sc = new Scanner(System.in);
    int N = sc.nextInt();
    int M = sc.nextInt();
    int K = sc.nextInt();
    
    int[] headParts = new int[N];
    for(int i=0; i<N; i++) {
      headParts[i] = sc.nextInt();
    }
    
    int[] bodyParts = new int[M];
    for(int i=0; i<M; i++) {
      bodyParts[i] = sc.nextInt();
    }
    
    sc.close();
    Arrays.sort(headParts);
    Arrays.sort(bodyParts);
    
    for(int i=0; i<K; i++) {
      if (headParts[i] > bodyParts[M-K+i]) {
        System.out.println("No");
        return;
      }
    }
    System.out.println("Yes");
  }
}

