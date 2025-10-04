import java.util.HashSet;
import java.util.Scanner;

public class Longest_Substring_No_Repeat {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        
        int right = 0, left = 0, ans = 0;
        HashSet<Character> set = new HashSet<>();
        
        while (right < s.length()) {
            char c = s.charAt(right);
            while (set.contains(c)) {
                set.remove(s.charAt(left));
                left++;
            }
            set.add(c);
            ans = Math.max(ans, right - left + 1);
            right++;
        }
        
        System.out.println(ans);
        sc.close();
    }
}
