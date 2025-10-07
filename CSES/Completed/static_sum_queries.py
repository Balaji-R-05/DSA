def build(arr):
    n = len(arr)
    tree = [0] * (2 * n)
    for i in range(n):
        tree[n + i] = arr[i]
    for i in range(n - 1, 0, -1):
        tree[i] = tree[i * 2] + tree[i * 2 + 1]
    return tree
    
def query(tree, n, l, r):
    res = 0
    l += n
    r += n
    while l < r:
        if l % 2:            
            res += tree[l]
            l += 1
        if r % 2:
            r -= 1
            res += tree[r]
        l //= 2
        r //= 2
    return res

def main():
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))

    tree = build(arr)

    for _ in range(q):
        a, b = map(int, input().split())
        print(query(tree, n, a - 1, b))
if __name__ == "__main__":
    main()
