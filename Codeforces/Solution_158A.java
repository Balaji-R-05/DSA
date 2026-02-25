import java.util.*;

class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int k = sc.nextInt();
        int[] arr = new int[N];
        for(int i = 0; i < N; i++) {
            arr[i] = sc.nextInt();
        }

        int flag = arr[k - 1];
        int res = 0;
        for(int i = 0; i < N; i++) {
            if(arr[i] > 0 && arr[i] >= flag) {
                res++;
            }
        }
        System.out.println(res);
        sc.close();
    }
}