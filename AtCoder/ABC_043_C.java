import java.util.Scanner;

public class ABC_043_C {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] a = new int[N];
        for (int i = 0; i < N; i++) {
            a[i] = sc.nextInt();
        }
        long answer = Long.MAX_VALUE;
        for (int x = -100; x <= 100; x++) {
            long cost = 0;
            for (int i = 0; i < N; i++) {
                long diff = a[i] - x;
                cost += diff * diff;
            }
            answer = Math.min(answer, cost);
        }
        System.out.println(answer);
        sc.close();
    }
}
