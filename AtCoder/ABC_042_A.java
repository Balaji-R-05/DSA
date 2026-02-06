import java.util.*;

public class ABC_042_A {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        int[] arr = new int[11];
        arr[a]++;
        arr[b]++;
        arr[c]++;
        if (arr[5] == 2 && arr[7] == 1) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }
        sc.close();
    }
}

// Time Complexity: O(1)
// Space Complexity: O(1)