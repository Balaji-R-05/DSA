import java.util.HashSet;
import java.util.Scanner;

public class Solution_1791A {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        String s = "codeforces";
        
        HashSet<Character> set = new HashSet<>();
        for (char ch : s.toCharArray()) {
            set.add(ch);
        }
        while (T-- > 0) {
            char c = sc.next().charAt(0);
            if (set.contains(c)) {
                System.out.println("YES");
            } else {
                System.out.println("NO");
            }
        }
        sc.close();
    }    
}

// Time Complexity: O(1)
// Space Complexity: O(1)