// // https://drive.google.com/file/d/1ChxPflgGLHwzg8CrhGpY80ujLbMlse8d/view

// import java.util.*;
// import java.lang.*;
// import java.io.*;
 
// class Black_Board

// {

//     public static int[] solve(char[][] field)

//     {

//         int nr=field.length;

//         int nc=field[0].length;

//         if(nr==0) return new int[]{0,0};

//         int min=0,max=0;

//         for(int r=0;r<nr;r++)

//         {

//             if(field[r][0]=='.')

//             {

//                 min++;

//                 int extra=simulate(field,r);

//                 max+=1+extra;

//             }

//         }

//         return new int[]{min,max};

//     }

//     private static int simulate(char[][] field, int r)

//     {

//         int nc=field[0].length;

//         int c=0;

//         while(c+1<nc && field[r][c+1]=='.')

//         {

//             c++;

//         }

//         field[r][c]='#';

//         return c;

//     }

// 	public static void main (String[] args) throws java.lang.Exception

// 	{

// 		// your code goes here

//         char[][] field = {

//             {'.', '.', '.', '#'},

//             {'#', '.', '.', '.'},

//             {'.', '#', '.', '.'}

//         };

//         int[] res = solve(field); 

//         System.out.println("minMoves = " + res[0] + ", maxMoves = " + res[1]);

// 	}

// }

 