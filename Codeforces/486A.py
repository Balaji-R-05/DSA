def calc(n:int):
    res = 0
    for i in range(1,n+1):
        res = res + (-1**i)*i
        
    print(res)


if __name__ == "__main__":
    n = int(input())
    calc(n)