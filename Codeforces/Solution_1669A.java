import java.util.Scanner;

public class Solution_1669A {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        while (T-- > 0) {
            int rating = sc.nextInt();
            if (rating >= 1900) {
                System.out.println("Division 1");
            } else if (rating >= 1600) {
                System.out.println("Division 2");
            } else if (rating >= 1400) {
                System.out.println("Division 3");
            } else {
                System.out.println("Division 4");
            }
        }
        sc.close();
    }
}