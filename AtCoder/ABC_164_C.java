import java.util.*;

public class ABC_164_C {
  public static void main(String args[]) {
    Scanner sc = new Scanner(System.in);
    int N = sc.nextInt();
    HashSet<String> s = new HashSet<>();
    for(int i=0; i<N; i++) {
      String st = sc.next();
      s.add(st);
    }
    System.out.println(s.size());
    sc.close();
  }
}