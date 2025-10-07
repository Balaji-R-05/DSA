package misc;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;
 
public class Main {
    static void upd(int[] seg,int node,int nl,int nr,int ql,int qr,int val){
        if(nl>qr || nr<ql) return;
        if(ql<=nl && nr<=qr){
            seg[node]=val;
            return;
        }
        int mid=(nl+nr)/2;
        upd(seg,2*node,nl,mid,ql,qr,val);
        upd(seg,2*node+1,mid+1,nr,ql,qr,val);
        seg[node]=Math.min(seg[node*2],seg[node*2+1]);
        return;
    }
    
    static int find(int[] seg,int node,int nl,int nr,int ql,int qr){
        if(nl>qr || nr<ql) return Integer.MAX_VALUE;
        if(ql<=nl && nr<=qr) return seg[node];
        int mid=(nl+nr)/2;
        int left=find(seg,2*node,nl,mid,ql,qr);
        int right=find(seg,2*node+1,mid+1,nr,ql,qr);
        return Math.min(left,right);
    }
    public static void main(String[] args) throws IOException {
        FastReader sc=new FastReader();
        int n=sc.nextInt(),q=sc.nextInt();
        int log=1;
        while((1<<log)<n){
            log++;
        }
        int siz=2*(1<<log);
        int[] seg=new int[siz];
        Arrays.fill(seg,Integer.MAX_VALUE);
        for(int i=siz/2;i<(siz/2)+n;i++){
            seg[i]=sc.nextInt();
        }
        for(int i=siz/2-1;i>=1;i--){
            seg[i]=Math.min(seg[i+i],seg[i+i+1]);
        }
        StringBuilder sb=new StringBuilder();
        while(q-->0){
            int type=sc.nextInt();
            if(type==1){
                int k=sc.nextInt(),u=sc.nextInt();
                upd(seg,1,0,siz/2-1,k-1,k-1,u);
            }
            else {
                int ql = sc.nextInt(), qr = sc.nextInt();
                int t=find(seg,1,0,siz/2-1,ql-1,qr-1);
                sb.append(t).append("\n");
            }
        }
        System.out.println(sb);
    }
}
 
class FastReader {
    BufferedReader br;
    StringTokenizer st;
 
    public FastReader() {
        br = new BufferedReader(new InputStreamReader(System.in));
    }
 
    String next() {
        while (st == null || !st.hasMoreElements()) {
            try {
                st = new StringTokenizer(br.readLine());
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        return st.nextToken();
    }
 
    int nextInt() {
        return Integer.parseInt(next());
    }
 
    long nextLong(){
        return Long.parseLong(next());
    }
}