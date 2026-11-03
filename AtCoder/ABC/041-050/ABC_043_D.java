// Problem: ABC 043 D
// Link: https://atcoder.jp/contests/abc043/tasks/arc059_b

// Approach:
// 1. Read the string.
// 2. A substring is unbalanced if a character appears more than half of its length.
// 3. It is enough to check substrings of length 2 and 3:
//    - Length 2: two adjacent equal characters (xx).
//    - Length 3: same character with one character between them (x?x).
// 4. If such a substring is found, print its 1-based starting and ending positions.
// 5. If no such substring exists, print "-1 -1".

// Time Complexity: O(N)
// Space Complexity: O(1)

import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        int n = s.length();
        for (int i = 0; i < n - 1; i++) {
            if (s.charAt(i) == s.charAt(i + 1)) {
                System.out.println((i + 1) + " " + (i + 2));
                sc.close();
                return;
            }
        }
        for (int i = 0; i < n - 2; i++) {
            if (s.charAt(i) == s.charAt(i + 2)) {
                System.out.println((i + 1) + " " + (i + 3));
                sc.close();
                return;
            }
        }
        System.out.println("-1 -1");
        sc.close();
    }
}
