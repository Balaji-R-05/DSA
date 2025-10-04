// Count of pairs such that i < j and arr[i] > arr[j]

import java.util.*;

public class Count_Inversion {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the value of N:");
        int N = sc.nextInt();
        int[] arr = new int[N];
        int count = 0;
        System.out.println("Enter N elements:");
        for(int i=0; i<N; i++) {
            arr[i] = sc.nextInt();
        }
        for(int i=0; i<N; i++) {
            for(int j=i+1; j<N; j++) {
                if (arr[i] > arr[j]) {
                    count++;
                }
            }
        }
        System.out.print("Total possible pairs = ");
        System.out.println(count);
        sc.close();
    }
}
