# def main():
#     n, m = map(int, input().split())
#     hotels = list(map(int, input().split()))
#     groups = list(map(int, input().split()))
#     for j in range(len(groups)):
#         for i in range(len(hotels)):
#             if hotels[i] >= groups[j]:
#                 print(i + 1, end=' ')
#                 hotels[i] -= groups[j]
#                 break
#         else:
#             print(0, end=" ")
    
# if __name__ == "__main__":
#     main()



import sys
input = sys.stdin.readline

def find(seg, node, nl, nr, t, N):
    if seg[node] < t:
        return -1
    
    if nl == nr:
        seg[node] -= t
        return node - N
    
    mid = (nl + nr) // 2
    
    lhot = find(seg, node * 2, nl, mid, t, N)
    if lhot != -1:
        seg[node] = max(seg[node * 2], seg[node * 2 + 1])
        return lhot
    
    rhot = find(seg, node * 2 + 1, mid + 1, nr, t, N)
    if rhot != -1:
        seg[node] = max(seg[node * 2], seg[node * 2 + 1])
        return rhot
    
    return -1


def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    
    size = 1
    while size < n:
        size *= 2
    
    seg = [0] * (2 * size)

    for i in range(n):
        seg[size + i] = a[i]
    
    for i in range(size - 1, 0, -1):
        seg[i] = max(seg[i * 2], seg[i * 2 + 1])
    
    res = []
    
    for _ in range(q):
        t = int(input())
        idx = find(seg, 1, 0, size - 1, t, size)
        res.append(idx + 1)
    
    print(' '.join(map(str, res)))


if __name__ == "__main__":
    main()
