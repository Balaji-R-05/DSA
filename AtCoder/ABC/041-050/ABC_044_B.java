// Problem: ABC 044 A
// Link: https://atcoder.jp/contests/abc044/tasks/abc044_a

// Approach:
// 1. Read the given string
// 2. Calculate the frequency of characters present in the string
// 3. If any character has odd frequency, print "No" and exit.
// 4. Else print "Yes"

// Time Complexity: O(N), where N is the length of the given string
// Space Complexity: O(1)

import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        int[] arr = new int[26];
        for(char ch: s.toCharArray()) {
            arr[ch - 'a']++;
        }
        for(int i=0; i<26; i++) {
            if (arr[i]%2 != 0) {
                System.out.println("No");
                sc.close();
                return;
            }
        }
        System.out.println("Yes");
        sc.close();
    }
}

// Time complexity: O(n)
// Space complexity: O(1)