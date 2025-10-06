import java.util.*;

public class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        sc.nextLine();
        int R = (int)(Math.log(N) / Math.log(2)) + 1;
        int[][] grid = new int[R][N];
        for(int i=0; i<N; i++) {
            grid[0][i] = sc.nextInt();
        }
        int k=1;
        for(int i=1; i<R; i++) {
            for(int j=0; j<N-k; j++) {
                grid[i][j] = Math.min(grid[i-1][j], grid[i-1][j+k]); 
            }
            k+=1;
        }
        for(int i=0; i<R; i++) {
            for(int j=0; j<N; j++) {
                System.out.print(grid[i][j] + " ");
            }
            System.out.println();
        }
        sc.close();
    }
}