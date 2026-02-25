import java.util.*;
 
class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        String[] s = sc.nextLine().split("\\+");
        Arrays.sort(s);
        StringBuilder sb = new StringBuilder(s[0]);
        for(int i = 1; i < s.length; i++) {
            sb.append("+");
            sb.append(s[i]);
        }
        System.out.println(sb.toString());
        sc.close();
    }
}

// Time complexity: O(NlogN)
// Space complexity: O(N)