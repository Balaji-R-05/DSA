// Problem: ABC 043 A
// Link: https://atcoder.jp/contests/abc043/tasks/abc043_a

// Approach:
// 1. Read the given integer N.
// 2. Calculate the sum of natural numbers from 1 to N.

// Formula:
// Sum = (N * (N + 1)) / 2

// Time Complexity: O(1)
// Space Complexity: O(1)

import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int res = (N * (N + 1)) / 2;
        System.out.println(res);
        sc.close();
    }
}
