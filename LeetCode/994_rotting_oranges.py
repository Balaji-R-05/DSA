# 994. Rotting Oranges

from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        
        rotten = []
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    rotten.append((row, col))
                elif grid[row][col] == 1:
                    count += 1

        minutes_passed = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while rotten and count > 0:
            new_rotten = []
            while rotten:
                x, y = rotten.pop(0)
                for dx, dy in directions:
                    xx, yy = x + dx, y + dy
                    if xx < 0 or yy < 0 or xx >= rows or yy >= cols or grid[xx][yy] != 1:
                        continue
                    grid[xx][yy] = 2
                    count -= 1
                    new_rotten.append((xx, yy))
            rotten = new_rotten
            minutes_passed += 1
            
        return minutes_passed if count == 0 else -1
    
# Time complexity: O(n*m)
# Space complexity: O(n*m)

# Approach: First find the number of rows and columns in the grid. Then find the number of fresh oranges