class Solution:
    def isPathCrossing(self, path: str) -> bool:
        # 如果在某个节点处，#N = #S = #E = #W, 回到之前的位置
        passed = [(0, 0)]
        current_pos = passed[-1]
        for p in path:
            if p=='N':
                d1 = current_pos[0]
                d2 = current_pos[1]+1
            elif p=='S':
                d1 = current_pos[0]
                d2 = current_pos[1]-1
            elif p=='W':
                d1 = current_pos[0]-1
                d2 = current_pos[1]
            else:
                d1 = current_pos[0]+1
                d2 = current_pos[1]
            if (d1, d2) in passed:
                return True
            passed.append((d1, d2))
            current_pos = passed[-1]
        return False
        