// Problem: ABC 472 B
// Link: https://atcoder.jp/contests/abc472/tasks/abc472_b

// Approach:
// 1. Read the array size and elements.
// 2. Calculate the prefix sums in place.
// 3. For every possible split, calculate the left and right sums.
// 4. Update the minimum absolute difference.
// 5. Print the minimum difference.

// Time Complexity: O(N)
// Space Complexity: O(N)

import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] arr = new int[N];

        for (int i = 0; i < N; i++) {
            arr[i] = sc.nextInt();
        }
        for (int i = 1; i < N; i++) {
            arr[i] += arr[i - 1];
        }

        int minDiff = Integer.MAX_VALUE;
        for (int i = 0; i < N - 1; i++) {
            int leftSum = arr[i];
            int rightSum = arr[N - 1] - arr[i];
            minDiff = Math.min(minDiff, Math.abs(leftSum - rightSum));
        }

        System.out.println(minDiff);
        sc.close();
    }
}