// Given an array, print the Next Smaller Element (NSE) for every element. The NSE for an element x is the    first smaller element on the right side of x in the array. Elements for which no smaller element exist (on the right side), consider NSE as -1. 
// Input: [4, 8, 5, 2, 25]
// Output: [2, 5, 2, -1, -1]
// Explanation: 
//  The first element smaller than 4 having index > 0 is 2.
//  The first element smaller than 8 having index > 1 is 5.
//  The first element smaller than 5 having index > 2 is 2.
//  There are no elements smaller than 4 having index > 3.
//  There are no elements smaller than 4 having index > 4.
// Input: [13, 7, 6, 12]
// Output: [7, 6, -1, -1]
// Explanation: 
// The first element smaller than 13 having index > 0 is 7.
// The first element smaller than 7 having index > 1 is 6.
// There are no elements smaller than 6 having index > 2.
// There are no elements smaller than 12 having index > 3. 


import java.util.*;

public class Next_Smallest_Element {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] arr = new int[N];
        for(int i=0; i<N; i++) {
            arr[i] = sc.nextInt();
        }
        int next;
        for(int i=0; i<N; i++) {
            next = -1;
            for(int j=i+1; j<N; j++) {
                if (arr[j] < arr[i]) {
                    next = arr[j];
                    break;
                }
            }
            arr[i] = next;
        }
        for(int i=0; i<N; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
        sc.close();
    }
}

// Time Complexity:  O(N^2)
// Space Complexity: O(1)