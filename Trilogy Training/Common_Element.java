// Return number of elements in all rows

import java.util.HashMap;
import java.util.HashSet;
import java.util.Scanner;

public class Common_Element {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[][] m = new int[N][N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                m[i][j] = sc.nextInt();
            }
        }
        int res = distinct(N, m);
        System.out.println(res);
        sc.close();
        // int[][] m1 = { { 2, 1, 4, 3 },
        // { 1, 2, 3, 2 },
        // { 3, 6, 2, 3 },
        // { 5, 2, 5, 3 } };
        // System.out.println("Distinct Common elements are " + distinct(4, m1));
        // int[][] m2 = { { 12, 1, 14, 3, 16 },
        // { 14, 2, 1, 3, 35 },
        // { 14, 1, 14, 3, 11 },
        // { 14, 5, 3, 2, 1 },
        // { 1, 18, 3, 21, 14 } };

        // System.out.println("Distinct Common elements are " + distinct(5, m2));
    }

    public static int distinct(int N, int[][] m) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int j = 0; j < N; j++) {
            map.put(m[0][j], 1);
        }

        for (int i = 1; i < N; i++) {
            HashSet<Integer> rowSet = new HashSet<>();
            for (int j = 0; j < N; j++) {
                int val = m[i][j];
                if (map.containsKey(val) && map.get(val) == i) {
                    map.put(val, i + 1);
                }
                rowSet.add(val);
            }
        }

        int count = 0;
        for (int key : map.keySet()) {
            if (map.get(key) == N) {
                count++;
            }
        }
        return count;
    }
}
