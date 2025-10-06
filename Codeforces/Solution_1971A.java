import java.util.*;
 
public class Solution_1971A {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        while(T-- > 0) {
            int x = sc.nextInt();
            int y = sc.nextInt();
            if (x > y) {
                System.out.println(y + " " + x);
            } else {
                System.out.println(x + " " + y);
            }
        }
        sc.close();
    }
}

// Time complexity: O(T)
// Space complexity: O(l)