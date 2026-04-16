from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # 使用BFS去做
        rows, cols = len(grid), len(grid[0])
        if grid[0][0]==1 or grid[rows-1][cols-1]==1:
            return -1
        directions = [(-1,0), (1,0), (0,-1), (0,1), (-1,-1), (-1,1), (1,-1), (1,1)]
        used = [[0 for _ in range(cols)] for _ in range(rows)]
        queue = deque()
        queue.append([0, 0])
        used[0][0] = 1
        level = 1
        
        while queue:
            cannot_add = True
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if r==rows-1 and c==cols-1:
                    return level
                for dr, dc in directions:
                    if min(r+dr, c+dc)>=0 and r+dr<rows and c+dc<cols and grid[r+dr][c+dc]==0 and used[r+dr][c+dc]==0:
                        cannot_add = False
                        queue.append([r+dr, c+dc])
                        used[r+dr][c+dc] = 1
            if cannot_add:
                return -1
            level+=1
        return level
            
        