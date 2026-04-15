class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_len = 0
        window_zero = 0
        left = 0
        for right in range(len(nums)):
            if nums[right]==0:
                window_zero += 1
            if window_zero>k:
                while left<=right and nums[left]==1:
                    left += 1
                left += 1
                window_zero -= 1
            max_len = max(max_len, right-left+1)
        return max_len
        