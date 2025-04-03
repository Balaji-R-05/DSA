# 62. Unique Paths

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0]*n for _ in range(m)]
        for i in range(m):
            grid[i][0] = 1
        for j in range(n):
            grid[0][j] = 1
        for row in range(1,m):
            for col in range(1,n):
                grid[row][col] += grid[row-1][col] + grid[row][col-1]
        
        return grid[m-1][n-1]


# Time Complexity: O(m*n)
# Space Complexity: O(m*n)

