// Problem: ABC 044 A
// Link: https://atcoder.jp/contests/abc044/tasks/abc044_a

// Approach:
// 1. Read the given N, K, X, Y.
// 2. If N <= K, then total = (N*X)
// 3. Else total = (K*X) + ((N-K)*Y)

// Time Complexity: O(1)
// Space Complexity: O(1)

import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int K = sc.nextInt();
        int X = sc.nextInt();
        int Y = sc.nextInt();
        int total = (N <= K)? (N*X) : ((K*X) + (N-K)*Y);
        System.out.println(total);
        sc.close();
    }

    // public static void main(String[] args) {
    //     Scanner sc = new Scanner(System.in);
    //     int N = sc.nextInt();
    //     int K = sc.nextInt();
    //     int X = sc.nextInt();
    //     int Y = sc.nextInt();
    //     int totalCost = 0;
    //     for(int i=0; i<N; i++) {
    //         if (K > 0) {
    //             totalCost += X;
    //             K--;
    //         } else {
    //             totalCost += Y;
    //         }
    //     }
    //     System.out.println(totalCost);
    //     sc.close();
    // }

    // Time complexity: O(N)
    // Space complexity: O(1)
}

