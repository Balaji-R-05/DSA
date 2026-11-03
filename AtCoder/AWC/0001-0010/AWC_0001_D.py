def main():
    N, M, K = map(int, input().split())

    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())

    NEG = float("-inf")
    dp = [[NEG] * (M + 1) for _ in range(N)]

    ans = 0

    for i in range(N):
        if B[i] <= M:
            dp[i][B[i]] = A[i]
            ans = max(ans, A[i])
        for j in range(max(0, i - K), i):
            for cost in range(M + 1):
                if dp[j][cost] == NEG:
                    continue
                nc = cost + B[i]
                if nc <= M:
                    dp[i][nc] = max(dp[i][nc], dp[j][cost] + A[i])
                    ans = max(ans, dp[i][nc])

    print(ans)

if __name__ == "__main__":
    main()

# Time Complexity: O(N * M * K)
# Space Complexity: O(N * M)