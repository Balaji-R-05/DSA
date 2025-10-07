package misc;
import java.io.*;
import java.util.*;
 
public class SegmentTrees {
    static class FastIO {
        BufferedReader br;
        StringTokenizer st;
        PrintWriter pw;
        FastIO() {
            br = new BufferedReader(new InputStreamReader(System.in));
            pw = new PrintWriter(System.out);
        }
        String next() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }
        
        int nextInt() {
            return Integer.parseInt(next());
        }
        
        long nextLong() {
            return Long.parseLong(next());
        }
        
        void println(long x) {
            pw.println(x);
        }
        
        void flush() {
            pw.flush();
        }
    }
    
    static long[] seg;
    static int N;
    
    public static void main(String[] args) {
        FastIO io = new FastIO();
        int n = io.nextInt();
        int q = io.nextInt();
        N = 1;
        while (N < n) N <<= 1;
        seg = new long[N << 1];
        for (int i = 0; i < n; i++) {
            seg[N + i] = io.nextLong();
        }
        for (int i = N - 1; i > 0; i--) {
            seg[i] = seg[i << 1] + seg[(i << 1) | 1];
        }
        StringBuilder sb = new StringBuilder();
        while (q-- > 0) {
            int type = io.nextInt();
            if (type == 1) {
                int k = io.nextInt() - 1;
                long u = io.nextLong();
                update(k, u);
            } else {
                int a = io.nextInt() - 1;
                int b = io.nextInt() - 1;
                sb.append(query(a, b)).append('\n');
            }
        }
        
        io.pw.print(sb);
        io.flush();
    }
    static void update(int idx, long val) {
        int pos = N + idx;
        seg[pos] = val;
        for (pos >>= 1; pos > 0; pos >>= 1) {
            seg[pos] = seg[pos << 1] + seg[(pos << 1) | 1];
        }
    }
    static long query(int l, int r) {
        long res = 0;
        l += N;
        r += N;
        while (l <= r) {
            if ((l & 1) == 1) {
                res += seg[l];
                l++;
            }
            if ((r & 1) == 0) {
                res += seg[r];
                r--;
            }
            l >>= 1;
            r >>= 1;
        }
        
        return res;
    }
}