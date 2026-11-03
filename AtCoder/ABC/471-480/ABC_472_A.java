// Problem: ABC 472 A
// Link: https://atcoder.jp/contests/abc472/tasks/abc472_a

// Approach:
// 1. Read the given string.
// 2. Replace every character except 'A' with '.'.
// 3. Print the modified string.

// Time Complexity: O(N)
// Space Complexity: O(1)

import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        StringBuilder sb = new StringBuilder();
        for (char ch : s.toCharArray()) {
            if (ch != 'A') {
                sb.append('.');
            } else {
                sb.append('A');
            }
        }
        System.out.println(sb.toString());
        sc.close();
    }
}