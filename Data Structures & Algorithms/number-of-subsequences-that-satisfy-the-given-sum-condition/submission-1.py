class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        # 使用滑动窗口
        nums.sort()
        count = 0
        MOD = 10**9 + 7
        left = 0
        right = len(nums)-1
        while left<=right:
            if nums[left]+nums[right]<=target:
                count = (count + 2**(right-left))%MOD
                left += 1
            else:
                right -= 1
        return count


        