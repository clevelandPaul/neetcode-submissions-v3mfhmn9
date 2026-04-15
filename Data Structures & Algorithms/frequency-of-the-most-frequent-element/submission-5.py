class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # 题目的关键: 只能去增加元素
        # 所以在一个窗口中，这个操作只能让窗口中的所有数等于那个最大的数
        # 找最长的窗口
        
        nums.sort()
        max_len = 0
        window_sum = 0
        left = 0
        for right in range(len(nums)):
            window_sum += nums[right]
            while left<=right and nums[right]*(right-left+1)-window_sum>k:
                window_sum -= nums[left]
                left+=1
            max_len = max(max_len, right-left+1)
            print(max_len)
        return max_len
        
        
