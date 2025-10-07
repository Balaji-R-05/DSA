#include <bits/stdc++.h>
using namespace std;
int find(vector<int>& seg,int node,int nl,int nr,int t,int N){
    if(seg[node]<t) return -1;
    if(nl==nr){
        seg[node]-=t;
        return node-N;
    }
    int mid=(nl+nr)>>1;
    int lhot=find(seg,node*2,nl,mid,t,N);
    if(lhot!=-1){
        seg[node]=max(seg[node*2],seg[node*2+1]);
        return lhot;
    }
    int rhot=find(seg,node*2+1,mid+1,nr,t,N);
    if(rhot!=-1){
        seg[node]=max(seg[node*2],seg[node*2+1]);
        return rhot;
    }
    return -1;
}
int main(){
    int n,q;
    cin>>n>>q;
    vector<int> a(n);
    for(int i=0;i<n;i++) cin>>a[i];
    int size=1;
    while(size<n) size*=2;
    vector<int> seg(size*2);
    vector<int> res;
    for(int i=0;i<n;i++){
        seg[size+i]=a[i];
    }
    for(int i=size-1;i>0;i--){
        seg[i]=max(seg[i*2],seg[i*2+1]);
    }
    while(q--){
        int t;
        cin>>t;
        res.push_back(find(seg,1,0,size-1,t,size)+1);
    }
    for(int r:res) cout<<r<<" ";
    
}