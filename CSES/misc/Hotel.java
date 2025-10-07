package misc;
import java.io.*;
import java.util.*;

public class Hotel {
    public static void main(String[] args) throws IOException {
        FastReader sc = new FastReader();
        
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
