import java.util.Scanner;

public class ABC_044_B {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
        int[] arr = new int[26];
        for(char ch: str.toCharArray()) {
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