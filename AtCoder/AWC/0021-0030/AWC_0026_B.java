import java.util.*;

public class AWC_0026_B {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        long N = sc.nextLong();
        long K = sc.nextLong();
        sc.nextLine();
        long t_score = 0L, a_score = 0L;
        for(int i=0; i<N; i++) {
            long num = sc.nextLong();
            if ((t_score + num) <= K) {
                t_score += num;
            } else {
                a_score += num;
            }
        }
        if (t_score > a_score) {
            System.out.println("Takahashi");
        } else if (a_score > t_score) {
            System.out.println("Aoki");
        } else {
            System.out.println("Draw");
        }
        sc.close();
    }
}