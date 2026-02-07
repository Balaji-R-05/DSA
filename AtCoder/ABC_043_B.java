import java.util.ArrayList;
import java.util.Scanner;

public class ABC_043_B {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<Character> arr = new ArrayList<>();
        String s = sc.nextLine();
        char[] crr = s.toCharArray();
        for (char c : crr) {
            if (c == 'B' && !arr.isEmpty()) {
                arr.remove(arr.size() - 1);
            } else if (c != 'B') {
                arr.add(c);
            }
        }
        for (char c : arr) {
            System.out.print(c);
        }
        sc.close();
    }
}
