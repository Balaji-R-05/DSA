def main():
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    power = [0] * (n + 1)
    for i in range(2, n + 1):
        power[i] = power[i // 2] + 1

    K = power[n] + 1
    st = [[0] * K for _ in range(n)]

    for i in range(n):
        st[i][0] = arr[i]

    for j in range(1, K):
        interval_length = 2 ** j
        half_length = 2 ** (j - 1)
        for i in range(n - interval_length + 1):
            st[i][j] = min(st[i][j - 1], st[i + half_length][j - 1])

    def query(L, R):
        j = power[R - L + 1]
        length = 2 ** j
        return min(st[L][j], st[R - length + 1][j])

    for _ in range(q):
        a, b = map(int, input().split())
        print(query(a - 1, b - 1))

if __name__ == "__main__":
    main()
