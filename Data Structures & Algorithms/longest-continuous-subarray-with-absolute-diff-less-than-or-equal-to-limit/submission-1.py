from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # 需要维护一下窗口中的最小值和最大值
        # 单调递减队列维护最大值
        # 单调递增队列维护最小值
        if len(nums)==1:
            return 1

        max_queue = deque() # 单调递减队列
        min_queue = deque() # 单调递增队列
        left = 0
        max_window = 1
        max_queue.append(0)
        min_queue.append(0)

        for right in range(1, len(nums)):
            while max_queue and nums[max_queue[-1]]<nums[right]:
                max_queue.pop()
            max_queue.append(right)
            while min_queue and nums[min_queue[-1]]>nums[right]:
                min_queue.pop()
            min_queue.append(right)

            while nums[max_queue[0]]-nums[min_queue[0]]>limit:
                if max_queue[0]==left:
                    max_queue.popleft()
                if min_queue[0]==left:
                    min_queue.popleft()
                left+=1

            max_window = max(max_window, right-left+1)
        
        return max_window


        
        

        