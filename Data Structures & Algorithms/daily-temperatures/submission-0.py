from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 找右边第一个比它大的数出现的位置
        # 使用单调递减栈

        res = [0 for _ in range(len(temperatures))]
        stack = deque()
        stack.append([temperatures[0], 0]) # (val, pos)

        for i in range(1, len(temperatures)):
            while stack:
                if temperatures[i]>stack[-1][0]:
                    val, pos = stack.pop()
                    res[pos] = i-pos
                else:
                    break
            stack.append([temperatures[i], i])

        return res
