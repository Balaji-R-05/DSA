import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;
 
public class Main2 {
    static class FastScanner {
        BufferedReader br;
        StringTokenizer st;
        FastScanner(InputStream in) { br = new BufferedReader(new InputStreamReader(in)); }
        String next() throws IOException {
            while (st == null || !st.hasMoreTokens()) st = new StringTokenizer(br.readLine());
            return st.nextToken();
        }
        int nextInt() throws IOException { return Integer.parseInt(next()); }
        long nextLong() throws IOException { return Long.parseLong(next()); }
    }
    private static void update(long[] nums,int index,int Nleft,int Nright,int Qleft,int Qright,int val){
        if(Nleft>Qright || Nright<Qleft){
            return;
        }
        if(Qleft<=Nleft && Qright>=Nright){
            nums[index]+=val;
            return;
        }
        int middle=(Nleft+Nright)>>>1;
        update(nums, index*2, Nleft, middle , Qleft, Qright, val);
        update(nums, index*2+1, middle+1, Nright, Qleft, Qright, val);
    };
    private static long Solve(long[] nums,int index,int Nleft,int Nright,int Qleft,int Qright){
        if(Nleft>Qright || Nright<Qleft){
            return 0L;
        } 
        if(Qleft==Nleft && Nright==Qright){
            return nums[index];
        }
        int middle=(Nleft+Nright)>>>1;
        long left=Solve(nums, index*2, Nleft, middle, Qleft, Qright);
        long right=Solve(nums, index*2+1, middle+1, Nright, Qleft, Qright);
        return left+right+nums[index];
    };
    public static void main(String[] args) throws IOException{
        FastScanner fc=new FastScanner(System.in);
        int pow=0;
        int size=fc.nextInt();
        int Q=fc.nextInt();
        while((1<<pow)<size) pow++;
        int newsize=1<<pow;
        long[] nums=new long[newsize*2];
        for(int i=0;i<size;i++){
            nums[i+newsize]=fc.nextLong();
        }
        StringBuilder sb=new StringBuilder();
        while(Q-->0){
            int num=fc.nextInt();
            if(num==2){
                int dest=fc.nextInt()-1;
                sb.append(Solve(nums,1,0,newsize-1,dest,dest)).append("\n");
            }else{
                int left=fc.nextInt()-1;
                int right=fc.nextInt()-1;
                int val=fc.nextInt();
                update(nums,1,0,newsize-1,left,right,val);
            }
        }
        System.out.println(sb);
    }
}