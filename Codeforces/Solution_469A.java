import java.util.Scanner;

public class Solution_469A {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        boolean[] arr = new boolean[N];
 
        int pCount = sc.nextInt();
        for (int i = 0; i < pCount; i++) {
            int x = sc.nextInt();
            arr[x - 1] = true;
        }
        int qCount = sc.nextInt();
        for (int i = 0; i < qCount; i++) {
            int x = sc.nextInt();
            arr[x - 1] = true;
        }
 
        boolean allPassed = true;
        for (boolean b : arr) {
            if (!b) {
                allPassed = false;
                break;
            }
        }
 
        if (allPassed) {
            System.out.println("I become the guy.");
        } else {
            System.out.println("Oh, my keyboard!");
        }
        sc.close();
    }
}