import java.util.Scanner;

public class String_Compression {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        int n = s.length();
        shortString(s, n);
        sc.close();
    }

    public static void shortString (String s, int n) {
        if (n==0) {
            System.out.println();
            return;
        }
        StringBuilder sb = new StringBuilder();
        int count = 1;
        char curr = s.charAt(0);
        for(int i=1; i<n; i++) {
            if (curr != s.charAt(i)) {
                sb.append(curr);
                sb.append(count);
                curr = s.charAt(i);
                count = 1;
            } else {
                count++;
            }
        }
        sb.append(curr);
        sb.append(count);
        System.out.println(sb.toString());
    }
}

// PS Z:\DSA\Trilogy Training> javac .\String_Compression.java
// PS Z:\DSA\Trilogy Training> java String_Compression  
// aaabbbcccdddeee
// a3b3c3d3e3