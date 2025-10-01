def main():
    N, H = map(int, input().split())
    arr = list(map(int, input().split()))
    res = 0
    for i in arr:
        if i > H:
            res += 2
        else:
            res += 1
    print(res)
 
if __name__ == "__main__":
    main()