from collections import defaultdict
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # 使用滑动窗口做
        count = 0
        window_prod = 1
        left = 0
        for right in range(len(nums)):
            window_prod *= nums[right]
            while left<=right and window_prod>=k:
                window_prod //= nums[left]
                left += 1
            if window_prod<k:
                count += right-left+1
        return count


        '''
        count = 0
        window_prod = 1
        left = 0
        for right in range(len(nums)):
            window_prod *= nums[right]
            while left<=right and window_prod>=k:
                window_prod //= nums[left]
                left += 1
            if window_prod < k:
                count += right-left+1
        return count
        '''

        