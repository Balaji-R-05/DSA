def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
 
        if arr[0] == arr[1]:
            majority = arr[0]
        else:
            majority = arr[2]
 
        for i in range(n):
            if arr[i] != majority:
                print(i + 1)
                break
 
if __name__ == "__main__":
    main()