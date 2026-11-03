// Problem: ABC 043 B
// Link: https://atcoder.jp/contests/abc043/tasks/abc043_b

// Approach:
// 1. Read the input string
// 2. Process the input one character at a time using an ArrayList as a mutable string.
//  - '0' and '1': append the character to the end of the result.
//  - 'B': remove the last character if the result is not empty.
// 3. Finally, print the characters that remain.

// Time Complexity: O(N)
// Space Complexity: O(N)


import java.util.ArrayList;
import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<Character> arr = new ArrayList<>();
        String s = sc.nextLine();
        for (char c : s.toCharArray()) {
            if (c == 'B' && !arr.isEmpty()) {
                arr.remove(arr.size() - 1);
            } else if (c != 'B') {
                arr.add(c);
            }
        }
        for (char c : arr) {
            System.out.print(c);
        }
        sc.close();
    }
}
