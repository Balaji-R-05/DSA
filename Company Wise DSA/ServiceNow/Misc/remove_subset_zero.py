def main():
    N = int(input())
    arr = list(map(int, input().split()))
    sum_range = sum(abs(x) for x in arr)
    dp = [[False] * (2 * sum_range + 1) for _ in range(N + 1)]

    dp[0][sum_range] = True

    for i in range(1, N + 1):
        for s in range(-sum_range, sum_range + 1):
            index = s + sum_range
            if dp[i - 1][index]:
                dp[i][index] = True
            prev_index = index - arr[i - 1]
            if 0 <= prev_index <= 2 * sum_range and dp[i - 1][prev_index]:
                dp[i][index] = True

    if dp[N][sum_range]:
        print(f"({N}, {sum_range})")
        print("Zero-sum subset exists")
    else:
        print("No zero-sum subset")

    print(*dp, sep="\n")


if __name__ == "__main__":
    main()
