from collections import deque
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 要找：连续若干根柱子组成的矩形里，面积最大的那个
        # 对区间[l,r]来说，area = (r-l+1)*min(heights[r:l+1])
        # 使用单调栈，找右边第一个比他小的height的位置
        # 单调递增栈

        n = len(heights)
        left = [-1] * n
        right = [n] * n

        stack = []

        # 求每个位置左边第一个更小的位置
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        stack = []

        # 求每个位置右边第一个更小的位置
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)

        ans = 0
        for i in range(n):
            ans = max(ans, heights[i] * (right[i] - left[i] - 1))

        return ans
        
        '''
        stack = deque()
        stack.append([0, heights[0]])
        pos_lst = [-1 for _ in range(len(heights))]
        for i in range(len(heights)):
            while stack:
                if stack[-1][1]>heights[i]:
                    pos, val = stack.pop()
                    pos_lst[pos] = i
                else:
                    break
            stack.append([i, heights[i]])

        max_area = -float('Inf')
        for i in range(len(heights)):
            if pos_lst[i]!=-1:
                area_1 = heights[i]*(pos_lst[i]-i)
                area_2 = heights[pos_lst[i]]*(len(heights)-i)
                max_area = max(max_area, area_1, area_2)
            else:
                max_area = max(max_area, heights[i]*(len(heights)-i))
        return max_area
        '''

        