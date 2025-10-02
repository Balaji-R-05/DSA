import java.util.HashSet;
import java.util.Scanner;

public class Course_List {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter no of course:");
        int N = sc.nextInt();
        sc.nextLine();
        if (N <= 0 || N > 20) {
            System.out.println("Invalid Range");
            sc.close();
            return;
        }
        HashSet<String> map = new HashSet<>();
        System.out.println("Enter course names:");
        for(int i=0; i<N; i++) {
            String course = sc.nextLine();
            map.add(course);
        }
        System.out.println("Enter the course to be searched:");
        String course = sc.nextLine();
        if (map.contains(course)) {
            System.out.println(course + " course is available!");
        } else {
            System.out.println(course + " course is not available!");
        }
        sc.close();
    }
}


// Test 1

// PS Z:\DSA\Trilogy Training> javac .\Course_List.java
// PS Z:\DSA\Trilogy Training> java Course_List
// Enter no of course:
// 5
// Enter course names:
// Java
// Oracle
// C++
// MySQL
// Dotnet
// Enter the course to be searched:
// C++
// C++ course is available!


// Test 2

// PS Z:\DSA\Trilogy Training> java Course_List        
// Enter no of course:
// 3
// Enter course names:
// Java
// Oracle
// Dotnet
// Enter the course to be searched:
// C++
// C++ course is not available!


// Test 3

// PS Z:\DSA\Trilogy Training> java Course_List        
// Enter no of course:
// 0
// Invalid Range