import java.util.*;

public class Minimun_Discount {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        sc.nextLine();
        String minProduct = "";
        double minDiscount = Double.MAX_VALUE;

        while (N-- > 0) {
            String[] productDetail = sc.nextLine().split(",");
            double discount = Double.parseDouble(productDetail[1]) * (Double.parseDouble(productDetail[2]) / 100);
            if (discount < minDiscount) {
                minProduct = productDetail[0];
                minDiscount = discount;
            }
        }
        System.out.println(minProduct);
        sc.close();
    }
}


// PS Z:\DSA\Trilogy Training> javac .\Minimun_Discount.java
// PS Z:\DSA\Trilogy Training> java Minimun_Discount
// 4
// mobile,10000,20
// shoe,5000,10
// watch,6000,15
// laptop,35000,5
// shoe