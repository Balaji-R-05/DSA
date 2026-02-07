import java.util.Scanner;

public class ABC_043_A {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int res = (N *(N+1)) / 2;
        System.out.println(res);
        sc.close();
    }
}

// Time Complexity: O(1)
// Space Complexity: O(1)