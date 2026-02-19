import java.util.*;

public class ABC_043_D {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        int n = s.length();
        for (int i = 0; i + 1 < n; i++) {
            if (s.charAt(i) == s.charAt(i + 1)) {
                System.out.println((i + 1) + " " + (i + 2));
                sc.close();
                return;
            }
        }
        for (int i = 0; i + 2 < n; i++) {
            if (s.charAt(i) == s.charAt(i + 2)) {
                System.out.println((i + 1) + " " + (i + 3));
                sc.close();
                return;
            }
        }
        System.out.println("-1 -1");
        sc.close();
    }
}
