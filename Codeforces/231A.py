def main():
    N = int(input())
    count = 0
    for _ in range(N):
        a,b,c = map(int, input().split())
        if (a+b+c > 1):
            count += 1
    print(count)
 
if __name__ == "__main__":
    main()