from collections import deque

def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))

    maxD = deque()
    minD = deque()
    ans = 0

    for i in range(N):
        while maxD and H[maxD[-1]] <= H[i]:
            maxD.pop()
        maxD.append(i)

        while minD and H[minD[-1]] >= H[i]:
            minD.pop()
        minD.append(i)

        if maxD[0] <= i - K:
            maxD.popleft()
        if minD[0] <= i - K:
            minD.popleft()

        if i >= K - 1:
            ans = max(ans, H[maxD[0]] - H[minD[0]])

    print(ans)

if __name__ == "__main__":
    main()

# Time Complexity: O(N)
# Space Complexity: O(N)