import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
 
public class ListRemove {
    static class FastScanner {
        BufferedReader br;
        StringTokenizer st;
        FastScanner(InputStream in) { br = new BufferedReader(new InputStreamReader(in)); }
        String next() throws IOException {
            while (st == null || !st.hasMoreTokens()) st = new StringTokenizer(br.readLine());
            return st.nextToken();
        }
        int nextInt() throws IOException { return Integer.parseInt(next()); }
        long nextLong() throws IOException { return Long.parseLong(next()); }
    };
    
    private static int find(int[] tree, int node, int nl, int nr, int k) {
        if (nl == nr) {
            tree[node] = 0;
            return nl;
        }
        int mid = (nl + nr) / 2;
        int lnode = node * 2;
        int rnode = node * 2 + 1;
        int ans;
        if (tree[lnode] >= k) {
            ans = find(tree, lnode, nl, mid, k);
        } else {
            ans = find(tree, rnode, mid + 1, nr, k - tree[lnode]);
        }
        tree[node] = tree[lnode] + tree[rnode];
        return ans;
    }
    
    public static void main(String[] args) throws IOException {
        FastScanner fc = new FastScanner(System.in);
        int n = fc.nextInt();
        
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = fc.nextInt();
        }
        
        int[] positions = new int[n];
        for (int i = 0; i < n; i++) {
            positions[i] = fc.nextInt();
        }
        
        int size = 1;
        while (size < n) size <<= 1;
        int[] tree = new int[2 * size];
        
        for (int i = 0; i < n; i++) {
            tree[size + i] = 1;
        }
        
        for (int i = size - 1; i > 0; i--) {
            tree[i] = tree[2 * i] + tree[2 * i + 1];
        }
        
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            int pos = positions[i];
            int index = find(tree, 1, 0, size - 1, pos);
            sb.append(arr[index]).append(" ");
        }
        
        System.out.println(sb.toString().trim());
    }
}