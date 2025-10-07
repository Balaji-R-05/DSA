def build(arr):
    n = len(arr)
    tree = [float("inf")] * (2 * n)
    for i in range(n):
        tree[n + i] = arr[i]
    for i in range(n - 1, 0, -1):
        tree[i] = min(tree[i * 2], tree[i * 2 + 1])
    return tree


def query(tree,n, l, r):
    l += n
    r += n
    res = float("inf")
    while l < r:
        if l % 2:
            res = min(res, tree[l])
            l += 1
        if r % 2:
            r -= 1
            res = min(res, tree[r])
        l //= 2
        r //= 2
    return res

def main():
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    tree = build(arr)
    for _ in range(q):
        l, r = map(int, input().split())
        print(query(tree, n, l-1, r))

if __name__ == "__main__":
    main()