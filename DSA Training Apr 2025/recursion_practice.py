n = 39
r = 13

def fun(n, r):
    if n>0:
        return (n-r, fun(n//3, 13))
    else:
        return 0
    
print(fun(n,r))

