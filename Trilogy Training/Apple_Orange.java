// Apple Orange Exchange


// Problem Description


// You have a certain number of apples in your garden, and your friend has a certain
// number of oranges. Both of you agree to exchange them. For each apple, your friend will
// give you exactly B oranges. However, you want the total count of fruits in your
// possession to be exactly A. You decide to exchange a specific set of apples with him,
// considering each apple as unique.
// You want to determine the number of distinct configurations for the resulting set of
// apples and oranges, ensuring that the total count of fruits in your possession is
// exactly A. Keep in mind that the answer can be a large number, so it should be printed
// modulo 1000000007 (10^9 + 7).


// Note:
// Two configurations are considered diƯerent if they involve a diƯerent number of apples
// or if the indices of the apples being exchanged diƯer.

// Problem Constraints
//  1 <= A <= 10^18
//  2 <= B <= 100
 
// Input Format
//  First argument is an integer A.
//  Second argument is an integer B.
 
// Output Format
//  Return an integer denoting the required answer.
 
// Example Input


// Input 1:
// 2 2
// Input 2:
// 4 2
 
// Example Output
// Output 1:
// 2
// Output 2:
// 5
 
// Example Explanation


// For Input 1:


// There are two distinct configurations:


//  Initially, you have one apple, and you exchange it for two oranges.


//  Initially, you have two apples, and you choose not to exchange them.


// In all the configurations, after the exchange, you will have two fruits.


// For Input 2:


// There are five distinct configurations:


//  Initially, you have three apples, and you exchange the first one for two oranges.


//  Initially, you have three apples, and you exchange the second one for two


// oranges.


//  Initially, you have three apples, and you exchange the third one for two oranges.


//  Initially, you have two apples, and you exchange both of them for four oranges.


//  Initially, you have four apples, and you choose not to exchange any.


// In all the configurations, after the exchange, you will have four fruits.


//  [execution time limit] 3 seconds (java)


//  [memory limit] 1 GB


//  [input] integer64 a


//  [input] integer b
//  [output] integer64
 



import java.util.*;

public class Apple_Orange {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long A = sc.nextLong();  // total fruits you want
        int B = sc.nextInt();    // oranges per apple
        sc.close();

        long MOD = 1000000007L;
        long ans = 0;

        for (long k = 0; k <= A / B; k++) {
            long x = A - (B - 1) * k;
            if (x < k) continue;
            ans = (ans + nCr(x, k)) % MOD;
        }

        System.out.println(ans);
    }

    // factorial function
    static long fact(long n) {
        long res = 1;
        for (long i = 2; i <= n; i++) {
            res *= i;
        }
        return res;
    }

    // nCr using factorial formula
    static long nCr(long n, long r) {
        if (r < 0 || r > n) return 0;
        long num = fact(n);
        long den = fact(r) * fact(n - r);
        return num / den;
    }
}







// import java.util.*;

// import java.lang.*;

// import java.io.*;
 
// class Codechef

// {

//     private static final long MOD=1_000_000_007;

//     public static long countcomb(int A,int B)

//     {

//         if(B<=0)

//         {

//             throw new IllegalArgumentException("B must be positive");

//         }

//         if(A<0)

//         {

//             return 0;

//         }

//         int i,k,max=A/B;

//         long[] fact=new long[A+1];

//         long[] invfact=new long[A+1];

//         fact[0]=1;

//         long tot=0L;

//         for(i=1;i<=A;i++)

//         {

//             fact[i]=(fact[i-1]*i)%MOD;

//         }

//         invfact[A]=modinv(fact[A]);

//         for(i=A;i>=1;i--)

//         {

//             invfact[i-1]=(invfact[i]*i)%MOD;

//         }

//         for(k=0;k<=max;k++)

//         {

//             int x=(int)(A-(B-1)*k);

//             if(x>=k && x>=0)

//             {

//                 tot=(tot+ncrmod(x,k,fact,invfact))%MOD;

//             }

//         }

//         return tot;

//     }

//     private static long ncrmod(int n,int r,long[] fact,long[] invfact)

//     {

//         if(r<0||r>n) return 0;

//         return (((fact[n]*invfact[r])%MOD)*invfact[n-r])%MOD;

//     }

//     private static long modinv(long a)

//     {

//         return modpow(a,MOD-2);

//     }

//     private static long modpow(long base,long exp)

//     {

//         long res=1L;

//         base%=MOD;

//         while(exp>0)

//         {

//             if((exp&1L)==1L)

//             {

//                 res=(res*base)%MOD;

//             }

//             base=(base*base)%MOD;

//             exp>>=1;

//         }

//         return res;

//     }

// 	public static void main (String[] args) throws java.lang.Exception

// 	{

// 		// your code goes here

//         int A = 4, B = 2;

//         System.out.println(countcomb(A, B));

// 	}

// }

 
// import java.util.*;
 
// public class AppleOrangeTopDown {

//     static int[] dp;

//     static int B;
 
//     static int solve(int n) {

//         if (n < B) return 1;
 
//         if (dp[n] != -1) return dp[n];
 
//         int keep = solve(n - 1);

//         int exchange = solve(n - B);

//         dp[n] = (keep + exchange);

//         return dp[n];

//     }
 
//     public static void main(String[] args) {
//         Scanner sc = new Scanner(System.in);
//         int A = sc.nextInt();  
//         int B = sc.nextInt();     
//         dp = new int[A + 1];
//         Arrays.fill(dp, -1);
//         int ans = solve(A);
//         System.out.println(ans);
//     }
// }

 