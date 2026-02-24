import java.util.*;
 
public class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        long N = sc.nextLong();
        long M = sc.nextLong();
        long A = sc.nextLong();
        long res = ((N%A == 0) ? N/A : N/A+1) * ((M%A == 0) ? M/A : M/A+1);
        System.out.println(res);
        sc.close();
    }
}

// Time complexity: O(1)
// Space complexity: O(1)