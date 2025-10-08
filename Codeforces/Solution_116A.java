import java.util.*;
 
public class Solution_116A {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int tram = 0;
    int capacity = Integer.MIN_VALUE;
    int T = sc.nextInt();
    while (T-- > 0) {
      int outCount = sc.nextInt();
      int inCount = sc.nextInt();
      tram -= outCount;
      tram += inCount;
      capacity = Math.max(tram, capacity);
    }
    System.out.println(capacity);
    sc.close();
  }
}