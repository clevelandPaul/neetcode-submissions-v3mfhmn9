class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0 for _ in range(n)] for _ in range(n)]
        used = [[False for _ in range(n)] for _ in range(n)]
        res[0][0] = 1
        used[0][0] = True
        curr_direction = 'right'
        cur_num = 1
        i = 0
        j = 0
        while cur_num < n**2:
            if curr_direction=='right':
                if j+1<n and not used[i][j+1]:
                    res[i][j+1] = cur_num+1
                    used[i][j+1] = True
                    j+=1
                else:
                    res[i+1][j] = cur_num+1
                    used[i+1][j] = True
                    i+=1
                    curr_direction = 'down'
            elif curr_direction=='down':
                if i+1<n and not used[i+1][j]:
                    res[i+1][j] = cur_num+1
                    used[i+1][j] = True
                    i+=1
                else:
                    res[i][j-1] = cur_num+1
                    used[i][j-1] = True
                    j-=1
                    curr_direction = 'left'
            elif curr_direction=='left':
                if j-1>=0 and not used[i][j-1]:
                    res[i][j-1] = cur_num+1
                    used[i][j-1] = True
                    j-=1
                else:
                    res[i-1][j] = cur_num+1
                    used[i-1][j] = True
                    i-=1
                    curr_direction = 'up'
            else:
                if i-1>=0 and not used[i-1][j]:
                    res[i-1][j] = cur_num+1
                    used[i-1][j] = True
                    i-=1
                else:
                    res[i][j+1] = cur_num+1
                    used[i][j+1] = True
                    j+=1
                    curr_direction = 'right'
            cur_num += 1
        return res
        