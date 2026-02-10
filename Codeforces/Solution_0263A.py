# 263A - Beautiful Matrix

def main():
    grid = []
    for _ in range(5):
        row = list(map(int, input().split()))
        grid.append(row)
    
    x = y = 0
    for i in range(5):
        for j in range(5):
            if grid[i][j] == 1:
                x = i
                y = j
                break
    
    print(abs(x-2) + abs(y-2))
 
if __name__ == "__main__":
    main()

# Time Complexity: O(25)
# Space Complexity: O(25)