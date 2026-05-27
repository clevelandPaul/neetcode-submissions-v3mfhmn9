from collections import deque
class Solution:
    # 使用stack, 记录stack中左括号的数量，取最大
    def maxDepth(self, s: str) -> int:
        stack = deque()
        max_len = 0
        for ch in s:
            if ch=='(':
                stack.append(ch)
                max_len = max(max_len, len(stack))
            elif ch==')':
                stack.pop()
            else:
                continue
        return max_len
        