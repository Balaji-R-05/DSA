def main():
    V = int(input())
    N = int(input())
    is_directed = True if input().strip().lower() == "yes" else False
    grid = [[0]*V for _ in range(V)]
    for _ in range(N):
        lst = list(map(int, input().split()))
        if is_directed:
            grid[lst[0]-1][lst[1]-1] = lst[2]
        else:
            grid[lst[0]-1][lst[1]-1] = lst[2]
            grid[lst[1]-1][lst[0]-1] = lst[2]
    print("Adjacency Matrix Representation:")
    for i in range(len(grid)):
        for j in range(len(grid)):
            print(grid[i][j], end=" ")
        print()
    
if __name__ == "__main__":
    main()

