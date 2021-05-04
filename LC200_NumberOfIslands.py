from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0

        def dfs(grid, i, j):
            if i<0 or j < 0 or i>=len(grid) or j>= len(grid[0]) or grid[i][j]!='1':
                return None
            grid[i][j]='0'
            dfs(grid, i+1, j)
            dfs(grid, i-1, j)
            dfs(grid, i, j+1)
            dfs(grid, i, j-1)

        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    dfs(grid,r,c)
                    count+=1
        return count
