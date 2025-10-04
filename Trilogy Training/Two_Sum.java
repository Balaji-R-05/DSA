import java.util.HashMap;
import java.util.Scanner;

public class Two_Sum {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        sc.nextLine();
        int[] arr = new int[N];
        for(int i = 0; i < N; i++) {
            arr[i] = sc.nextInt();
        }
        int target = sc.nextInt();
        HashMap<Integer, Integer> map = new HashMap<>();
        
        for(int i = 0; i < N; i++) {
            int k = target - arr[i];
            if (map.containsKey(k)) {
                System.out.println(i + " " + map.get(k));
                return;
            } else {
                map.put(arr[i], i);
            }
        }
        sc.close();
    }
}


// PS Z:\DSA\Trilogy Training> javac .\Two_Sum.java
// PS Z:\DSA\Trilogy Training> java Two_Sum        
// 5
// 1 2 3 4 5
// 6
// 3 1