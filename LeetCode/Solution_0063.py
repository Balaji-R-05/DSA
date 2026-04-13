from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0

        res = [[0]*n for _ in range(m)]

        for j in range(n):
            if obstacleGrid[0][j] == 1:
                break
            res[0][j] = 1

        for i in range(m):
            if obstacleGrid[i][0] == 1:
                break
            res[i][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    res[i][j] = 0
                else:
                    res[i][j] = res[i-1][j] + res[i][j-1]

        return res[m-1][n-1]

# Time Complexity: O(m * n)
# Space Complexity: O(m * n)
