# 1335A - Candies and Two Sisters

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        if N%2==0:
            print(N//2-1)
        else:
            print((N+1)//2-1)
 
if __name__ == "__main__":
    main()