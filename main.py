# 1
# 2 9
# 3 8 10
# 4 7 11 14
# 5 6 12 13 15

n = 5
res1 = 7
res2 = 2
for i in range(1, n+1):
    flag = 0
    for j in range(0,i):
        if j%2 == 1:
            print(i+res1, end=' ')
            flag = 1
        else:
            print(i, end=' ')
            flag = 0
            
    if flag == 1:
        res1-=2
    print()
