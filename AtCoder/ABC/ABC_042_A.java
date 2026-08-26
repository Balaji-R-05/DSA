// Problem: ABC 042 A
// Link: https://atcoder.jp/contests/abc042/tasks/abc042_a

// Approach:
// 1. Read the three integers.
// 2. Check whether exactly two values are 5 and one value is 7.
// 3. Print "YES" if the condition is satisfied; otherwise, print "NO".

// Time Complexity: O(1)
// Space Complexity: O(1)

import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();

        int countOfFives = 0;
        int countOfSevens = 0;
        if (a == 5)
            countOfFives++;
        if (a == 7)
            countOfSevens++;
        if (b == 5)
            countOfFives++;
        if (b == 7)
            countOfSevens++;
        if (c == 5)
            countOfFives++;
        if (c == 7)
            countOfSevens++;

        if (countOfFives == 2 && countOfSevens == 1) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }
        sc.close();
    }
}
