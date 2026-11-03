import java.util.*;

public class ABC_427_A {
  public static void main(String args[]) {
    Scanner sc = new Scanner(System.in);
    String s = sc.nextLine();
    int L = s.length();
    int mid = L/2;
    for(int i=0; i<L; i++) {
      char c = s.charAt(i);
      if (i==mid) {
        continue;
      }
      System.out.print(c);
    }
    System.out.println();
    sc.close();
  }
}