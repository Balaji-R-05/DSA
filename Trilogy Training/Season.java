import java.util.Scanner;

public class Season {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter month: ");
        int month = sc.nextInt();

        if (month < 1 || month > 12) {
            System.out.println("Invalid Month Entered");
        } else if (month >= 3 && month <= 5) {
            System.out.println("Season: Spring");
        } else if (month >= 6 && month <= 8) {
            System.out.println("Season: Summer");
        } else if (month >= 9 && month <= 11) { 
            System.out.println("Season: Autumn");
        } else {
            System.out.println("Season: Winter");
        }
        sc.close();
    }
}



// PS Z:\DSA\Trilogy Training> javac .\Season.java  
// PS Z:\DSA\Trilogy Training> java Season  
// Enter month: 2
// Season: Winter
// PS Z:\DSA\Trilogy Training> java Season
// Enter month: 15
// Invalid Month Entered
// PS Z:\DSA\Trilogy Training> java Season
// Enter month: 6
// Season: Summer