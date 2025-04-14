# 200. Number of Islands

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        ans = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    self.helper(grid,row,col,rows,cols)
                    ans+=1
        return ans

    def helper(self,grid,i,j,m,n):
        if i<0 or i>=m or j<0 or j>=n or grid[i][j] == "0":
            return
        grid[i][j] = '0'
        self.helper(grid,i+1,j,m,n)
        self.helper(grid,i,j+1,m,n)
        self.helper(grid,i-1,j,m,n)
        self.helper(grid,i,j-1,m,n)

# Time complexity: O(R*C),  R- number of rows, C- number of columns
# Space complexity: O(1)