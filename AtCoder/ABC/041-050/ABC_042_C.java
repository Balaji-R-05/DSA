// Problem: ABC 042 C
// Link: https://atcoder.jp/contests/abc042/tasks/arc058_a

// Approach:
// 1. Read N and K.
// 2. Store the disliked digits in a HashSet for O(1) lookup.
// 3. Starting from N, check every number:
//    - Extract each digit.
//    - If any digit is disliked, reject the number.
//    - Otherwise, print the number and stop.
//
// Time Complexity: O(M * D)
// M = number of numbers checked from N until the answer is found.
// D = number of digits in each number.
//
// Space Complexity: O(K)
// K = number of disliked digits stored in the HashSet.


import java.util.*;

class ABC_042_C {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int K = sc.nextInt();

        Set<Integer> disliked = new HashSet<>();

        for (int i = 0; i < K; i++) {
            disliked.add(sc.nextInt());
        }

        for (int i = N; ; i++) {
            int num = i;
            boolean valid = true;

            while (num > 0) {
                int rem = num % 10;

                if (disliked.contains(rem)) {
                    valid = false;
                    break;
                }

                num /= 10;
            }

            // Special case when number is 0
            if (i == 0 && disliked.contains(0)) {
                valid = false;
            }

            if (valid) {
                System.out.println(i);
                break;
            }
        }

        sc.close();
    }
}