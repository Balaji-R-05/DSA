import java.util.Arrays;
import java.util.Scanner;

public class Solution_2037A {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        while (T-- > 0) {
            int N = sc.nextInt();
            int[] arr = new int[N];
            for (int k = 0; k < N; k++) {
                arr[k] = sc.nextInt();
            }
            boolean[] flag = new boolean[N];
            Arrays.fill(flag, true);
            int res = 0;
            for (int i = 0; i < N; i++) {
                for (int j = i + 1; j < N; j++) {
                    if (arr[i] == arr[j] && flag[i] && flag[j]) {
                        res++;
                        flag[i] = false;
                        flag[j] = false;
                    }
                }
            }
            System.out.println(res);
        }
        sc.close();
    }
}
