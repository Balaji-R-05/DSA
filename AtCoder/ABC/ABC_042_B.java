// Problem: ABC 042 B
// Link: https://atcoder.jp/contests/abc042/tasks/abc042_b

// Approach:
// 1. Read the strings.
// 2. Sort the strings lexicographically.
// 3. Concatenate them in sorted order.

// Time Complexity: O(N log N)
// Space Complexity: O(N)

import java.util.Arrays;
import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int L = sc.nextInt();
        sc.nextInt();
        String[] strings = new String[N];

        for (int i = 0; i < N; i++) {
            strings[i] = sc.next();
        }

        Arrays.sort(strings);
        StringBuilder sb = new StringBuilder();
        for (String value : strings) {
            sb.append(value);
        }

        System.out.println(sb);
        sc.close();
    }
}