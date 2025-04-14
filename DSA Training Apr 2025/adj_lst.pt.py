def main():
    N = int(input())
    for _ in range(N):
        case = list(map(int, input().split()))
        adj = [[i] for i in range(case[0])]
        for i in range(case[1]):
            n, v = map(int, input().split())
            adj[n].append(v)
            adj[v].append(n)
        
        for s in adj:
            print(*s, sep="-> ")
        
if __name__ == "__main__":
    main()