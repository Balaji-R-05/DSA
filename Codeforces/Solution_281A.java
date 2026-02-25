import java.util.*;
 
class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine().trim();
        System.out.println(Character.toUpperCase(str.charAt(0)) + str.substring(1));
        sc.close();
    }
}

// Time complexity: O(N)
// Space complexity: O(N)