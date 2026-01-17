def main():
    N = int(input())
    arr = list(map(int, input().split()))
    res = [(i,val) for i,val in enumerate(arr)]
    res.sort(key=lambda x: x[1])
    ans = []
    for i in range(3):
        ans.append(res[i][0]+1)
    print(*ans, sep=" ")
    
if __name__ == "__main__":
    main()

# Time Complexity: O(NlogN)
# Space Complexity: O(N)