import java.util.Scanner;

public class Automorphic {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int square_N = N * N;

        int digits = (int)Math.log10(N) + 1;
        int last = square_N % (int)Math.pow(10, digits);

        if (last == N) {
            System.out.println("Automorphic");
        } else {
            System.out.println("Not Automorphic");
        }
        sc.close();
    }
}

// PS Z:\DSA\Trilogy Training> javac .\Automorphic.java    
// PS Z:\DSA\Trilogy Training> java Automorphic        
// 5
// Automorphic
// PS Z:\DSA\Trilogy Training> java Automorphic
// 6
// Automorphic
// PS Z:\DSA\Trilogy Training> java Automorphic
// 25
// Automorphic
// PS Z:\DSA\Trilogy Training> java Automorphic
// 7
// Not Automorphic



// public class Automorphic{
//     public static void main(String args[]) {
//         Scanner sc = new Scanner(System.in);
//         int N = sc.nextInt();
//         int square_N = N * N;
        
//         String s1 = Integer.toString(N);
//         String s2 = Integer.toString(square_N);

//         if (s2.endsWith(s1)) {
//             System.out.println("Automorphic");
//         } else {
//             System.out.println("Not Automorphic");
//         }
//         sc.close();
//     }
// }