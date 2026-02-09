import java.util.Scanner;

public class ABC_044_A {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int K = sc.nextInt();
        int X = sc.nextInt();
        int Y = sc.nextInt();
        int total = (N <= K)? (N*X) : ((K*X) + (N-K)*Y);
        System.out.println(total);
        sc.close();
    }
}

// Time complexity: O(1)
// Space complexity: O(1)