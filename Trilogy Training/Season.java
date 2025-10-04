// Shraddha Kapoor’s professor suggested that she study hard and prepare well for the lesson on seasons. If her professor says month then, she has to tell the name of the season corresponding to that month. So write the program to get the solution to the above task?

// March to May – Spring Season
// June to August – Summer Season
// September to November – Autumn Season
// December to February – Winter Season
// Note: The entered month should be in the range of 1 to 12. If the user enters a month less than 1 or greater than 12 then the message “Invalid Month Entered” should get displayed.

// Sample Input 1:
// Enter month: 6

// Sample Output 1:
// Season: Summer

// Sample Input 2:
// Enter month: 15

// Sample Output 2:
// Invalid Month Entered



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