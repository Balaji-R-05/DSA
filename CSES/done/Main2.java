import java.io.*;
import java.util.*;

public class Main2 {
    public static void main(String[] args) throws IOException {
        FastReader sc = new FastReader();

        int n = sc.nextInt(), q = sc.nextInt();
        int[] arr = new int[n + 1];
        for (int i = 1; i <= n; i++) arr[i] = sc.nextInt();

        int[] prefix = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            prefix[i] = prefix[i - 1] ^ arr[i];
        }

        StringBuilder sb = new StringBuilder();
        while (q-- > 0) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            sb.append(prefix[b] ^ prefix[a - 1]).append("\n");
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

    int nextInt() {
        return Integer.parseInt(next());
    }
}
