package misc;
import java.io.*;
import java.util.*;

public class Main1 {
    static int[][] st;
    static int[] log;

    static void build(int[] arr, int n) {
        log = new int[n + 1];
        log[1] = 0;
        for (int i = 2; i <= n; i++) {
            log[i] = log[i / 2] + 1;
        }

        int K = log[n] + 1;
        st = new int[n][K];

        for (int i = 0; i < n; i++) {
            st[i][0] = arr[i];
        }

        for (int j = 1; j < K; j++) {
            for (int i = 0; i + (1 << j) <= n; i++) {
                st[i][j] = Math.min(st[i][j - 1], st[i + (1 << (j - 1))][j - 1]);
            }
        }
    }

    static int query(int L, int R) {
        int j = log[R - L + 1];
        return Math.min(st[L][j], st[R - (1 << j) + 1][j]);
    }

    public static void main(String[] args) throws IOException {
        FastReader sc = new FastReader();

        int n = sc.nextInt(), q = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();

        build(arr, n);

        StringBuilder sb = new StringBuilder();
        while (q-- > 0) {
            int a = sc.nextInt() - 1;
            int b = sc.nextInt() - 1;
            sb.append(query(a, b)).append("\n");
        }

        System.out.print(sb);
    }
}

class FastReader {
    BufferedReader br;
    StringTokenizer st;
    FastReader() {
        br = new BufferedReader(new InputStreamReader(System.in));
    }
    String next() {
        while (st == null || !st.hasMoreElements()) {
            try {
                String line = br.readLine();
                if (line == null) return null;
                st = new StringTokenizer(line);
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        return st.nextToken();
    }
    int nextInt() { return Integer.parseInt(next()); }
}
