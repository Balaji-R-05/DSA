import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

class Longest_Consecutive_Sequence {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number of elements: ");
        int N = sc.nextInt();

        int[] arr = new int[N];
        System.out.println("Enter the N elements: ");
        for(int i=0; i<N; i++) {
            arr[i] = sc.nextInt();
        }
        int res = longestConsecutive(arr);
        System.out.print("Longest Consecutive Sequence: ");
        System.out.println(res);
        sc.close();
    }


    public static int longestConsecutive(int[] nums) {
        Set<Integer> numSet = new HashSet<>();
        for (int num : nums) {
            numSet.add(num);
        }
        int longest = 0;
        for (int num : numSet) {
            if (!numSet.contains(num - 1)) {
                int current = num;
                int count = 1;

                while (numSet.contains(current + 1)) {
                    current++;
                    count++;
                }
                longest = Math.max(longest, count);
            }
        }
        return longest;
    }
}



// PS Z:\DSA\Trilogy Training> javac .\Longest_Consecutive_Sequence.java
// PS Z:\DSA\Trilogy Training> java Longest_Consecutive_Sequence        
// Enter the number of elements: 6
// Enter the N elements: 
// 100
// 200
// 1
// 2
// 3
// 4
// Longest Consecutive Sequence: 4