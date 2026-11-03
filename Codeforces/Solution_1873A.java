// 1873A - Short Sort

import java.util.*;

public class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int test = sc.nextInt();
        sc.nextLine();

        while (test-- > 0) {
            String S = sc.nextLine();
            String T = "abc";
            int count = 0;

            for(int i=0; i<3; i++) {
                if (S.charAt(i) != T.charAt(i)) {
                    count++;
                }
            }

            System.out.println((count==2 || count==0) ? "YES" : "NO");
        }
        sc.close();
    }
}