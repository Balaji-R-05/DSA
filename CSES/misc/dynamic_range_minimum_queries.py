# Iterative Segment Tree for Dynamic Range Sum Queries

def main():
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))

    size = 1
    while size < n:
        size <<= 1
    tree = [0] * (2 * size)

    for i in range(n):
        tree[size + i] = arr[i]

    for i in range(size - 1, 0, -1):
        tree[i] = tree[2 * i] + tree[2 * i + 1]

    for _ in range(q):
        t, a, b = map(int, input().split())
        if t == 1:
            pos = size + a - 1
            tree[pos] = b
            pos //= 2
            while pos >= 1:
                tree[pos] = tree[2 * pos] + tree[2 * pos + 1]
                pos //= 2
        else:
            # Range sum query
            l = a - 1 + size
            r = b - 1 + size
            s = 0
            while l <= r:
                if l % 2 == 1:
                    s += tree[l]
                    l += 1
                if r % 2 == 0:
                    s += tree[r]
                    r -= 1
                l //= 2
                r //= 2
            print(s)


if __name__ == "__main__":
    main()