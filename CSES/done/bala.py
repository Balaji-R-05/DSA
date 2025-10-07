n,q=map(int, input().split())
arr=list(map(int, input().split()))
 
s=1
while s<n:
    s<<=1
tree=[0]*(2*s)
 
for i in range(n):
    tree[s+i]=arr[i]

for i in range(s-1,0,-1):
    tree[i]=(tree[2*i] ^ tree[2*i+1])

out=[]
for _ in range(q):
    a,b=map(int,input().split())
    l=a-1+s
    r=b-1+s
    mn=0
    while l<=r:
        if l%2==1:
            mn=(mn ^ tree[l])
            l+=1
        if r%2==0:
            mn=(mn ^ tree[r])
            r-=1
        l//=2
        r//=2
    out.append(str(mn))

print('\n'.join(out))