# 63. Unique Paths II

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1: 
            return 0
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        grid = [[0] * n for _ in range(m)]
    
        grid[0][0] = 1
        
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    grid[i][j] = 0
                else:
                    if i > 0:
                        grid[i][j] += grid[i - 1][j]
                    if j > 0:
                        grid[i][j] += grid[i][j - 1]
        
        return grid[m - 1][n - 1]
    
# Time Complexity: O(m*n)
# Space Complexity: O(m*n)