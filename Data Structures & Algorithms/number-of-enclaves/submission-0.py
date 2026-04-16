from collections import deque
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        # 反着思考，先从边界上的陆地出发，把所有“能走到边界”的陆地全标记掉
        # 最后剩下没被标记的陆地

        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if min(r, c)<0 or r>=rows or c>=cols or grid[r][c]==0:
                return
            grid[r][c] = 0
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)

        for c in range(cols):
            if grid[0][c]==1:
                dfs(0, c)
            if grid[rows-1][c]==1:
                dfs(rows-1, c)
        for r in range(rows):
            if grid[r][0]==1:
                dfs(r, 0)
            if grid[r][cols-1]==1:
                dfs(r, cols-1)
        
        return sum(grid[r][c] for r in range(rows) for c in range(cols))

        