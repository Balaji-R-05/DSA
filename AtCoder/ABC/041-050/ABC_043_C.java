// Problem: ABC 043 C
// Link: https://atcoder.jp/contests/abc043/tasks/arc059_a

// Approach:
// 1. Read the array size and elements.
// 2. Transforming an integer x into y costs (x - y)^2 dollars.
// 3. Calculate the cost for every target value x in the range -100 to 100.
// 4. Track the minimum cost found.
// 5. Print the minimum cost.

// Time Complexity: O(N * 201)
// Space Complexity: O(N)

import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] a = new int[N];
        for (int i = 0; i < N; i++) {
            a[i] = sc.nextInt();
        }
        long answer = Long.MAX_VALUE;
        for (int x = -100; x <= 100; x++) {
            long cost = 0;
            for (int i = 0; i < N; i++) {
                long diff = a[i] - x;
                cost += diff * diff;
            }
            answer = Math.min(answer, cost);
        }
        System.out.println(answer);
        sc.close();
    }
}
