class Solution:
    # 维护possible range [minOpen, maxOpen]
    # 表示: 当前可能剩余的左括号数量范围
    def checkValidString(self, s: str) -> bool:
        minOpen = 0
        maxOpen = 0
        for ch in s:
            if ch=='(':
                minOpen += 1
                maxOpen += 1
            elif ch==')':
                minOpen -= 1
                maxOpen -= 1
            else:
                minOpen -= 1
                maxOpen += 1
            if maxOpen<0:
                return False
            minOpen = max(minOpen, 0)
        return minOpen==0

        