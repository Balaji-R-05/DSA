import java.util.*;
 
public class Solution_1772A {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        sc.nextLine();
        
        while(T-- > 0) {
            String[] cmd = sc.nextLine().split("\\+");
            int a = Integer.parseInt(cmd[0]);
            int b = Integer.parseInt(cmd[1]);
            System.out.println(a+b);
        }
        
        sc.close();
    }
}

// Time complexity: O(T)
// Space complexity: O(l)