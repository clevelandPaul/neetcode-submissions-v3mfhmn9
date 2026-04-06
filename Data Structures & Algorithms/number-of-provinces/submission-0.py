from collections import deque
'''
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        rows, cols = len(isConnected), len(isConnected[0])
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        used = [[0 for _ in range(cols)] for _ in range(rows)]
        num_province = 0
        for i in range(rows):
            for j in range(cols):
                if isConnected[i][j]==1 and used[i][j]==0:
                    used[i][j] = 1
                    queue = deque([(i, j)])
                    while queue:
                        r, c = queue.popleft()
                        for dr, dc in directions:
                            if min(r+dr, c+dc)>=0 and r+dr<rows and c+dc<cols and isConnected[r+dr][c+dc]==1 and used[r+dr][c+dc]==0:
                                queue.append((r+dr, c+dc))
                                used[r+dr][c+dc] = 1
                    num_province += 1
                
        return num_province
'''
# from collections import deque
from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        num_province = 0

        for i in range(n):
            if not visited[i]:
                num_province += 1
                queue = deque([i])
                visited[i] = True

                while queue:
                    city = queue.popleft()
                    for nei in range(n):
                        if isConnected[city][nei] == 1 and not visited[nei]:
                            visited[nei] = True
                            queue.append(nei)

        return num_province
                    
        