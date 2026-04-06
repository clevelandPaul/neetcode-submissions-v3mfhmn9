from collections import deque
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        # BFS时间复杂度会超，这题不用BFS去解
        # 最优解法的思路
        # 先统计每一行有多少个server
        # 再统计每一列有多少个server
        # 最后遍历每个server, 看它所在行或列数量是否大于1 (完全被孤立的server就是所在行列只有它一个1)
        rows, cols = len(grid), len(grid[0])
        row_count = [0 for _ in range(rows)]
        col_count = [0 for _ in range(cols)]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    row_count[i]+=1
                    col_count[j]+=1
        ans = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1 and (row_count[i]>1 or col_count[j]>1):
                    ans += 1
        return ans

        '''
        rows, cols = len(grid), len(grid[0])
        used = [[0 for _ in range(cols)] for _ in range(rows)]
        num_servers = 0
        queue = deque()
        for i in range(rows):
            for j in range(cols):
                group_count = 0
                if grid[i][j]==1 and used[i][j]==0:
                    queue.append([i, j])
                    used[i][j] = 1
                    group_count += 1
                while queue:
                    r, c = queue.popleft()
                    for m in range(r+1, rows):
                        if grid[m][c]==1:
                            queue.append([m, c])
                            used[m][c] = 1
                            group_count += 1
                    for n in range(c+1, cols):
                        if grid[r][n]==1:
                            queue.append([r, n])
                            used[r][n] = 1
                            group_count += 1                
                if group_count>1:
                    num_servers+=group_count
        return num_servers
        '''
        
                
                            

        