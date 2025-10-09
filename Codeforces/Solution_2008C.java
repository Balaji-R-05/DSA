import java.util.Scanner;

public class Solution_2008C {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        while (T-- > 0) {
            long l = sc.nextLong();
            long r = sc.nextLong();
 
            long diff = r - l;
            long res = 1;
            long temp = 1;
 
            while (diff >= temp) {
                diff -= temp;
                temp++;
                res++;
            }
 
            System.out.println(res);
        }
        sc.close();
    }
}

