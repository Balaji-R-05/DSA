import java.util.*;

public class Move_Hash {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        int n = s.length();
        moveHash(s, n);
        sc.close();
    }

    public static void moveHash(String s, int n) {
        if (n == 0) {
            System.out.println("No String");
            return;
        }
        int count = 0;
        StringBuilder sb = new StringBuilder();
        
        for (int i = 0; i < n; i++) {
            char c = s.charAt(i);
            if (c == '#') {
                count++;
            } else {
                sb.append(c);
            }
        }

        StringBuilder result = new StringBuilder();
        for (int i = 0; i < count; i++) {
            result.append('#');
        }
        result.append(sb);

        System.out.println(result.toString());
    }
}


// PS Z:\DSA\Trilogy Training> javac .\Move_Hash.java
// PS Z:\DSA\Trilogy Training> java Move_Hash
// hello#world#i#am#balaji
// ####helloworldiambalaji