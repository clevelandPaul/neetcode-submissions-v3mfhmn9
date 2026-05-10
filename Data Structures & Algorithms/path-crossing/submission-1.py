class Solution:
    def isPathCrossing(self, path: str) -> bool:
        # 如果在某个节点处，#N = #S = #E = #W, 回到之前的位置
        # 使用set的话就是O(1)查找
        x, y = 0, 0
        passed = {(0, 0)}
        
        for p in path:
            if p=='N':
                y += 1
            elif p=='S':
                y -= 1
            elif p=='W':
                x -= 1
            else:
                x += 1
            if (x, y) in passed:
                return True
            passed.add((x, y))
        return False
        