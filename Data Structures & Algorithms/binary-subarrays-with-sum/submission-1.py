from collections import defaultdict
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = 0
        prefix_sum = 0
        freq = defaultdict(int)
        freq[0] = 1

        for x in nums:
            prefix_sum += x
            count += freq[prefix_sum-goal]
            freq[prefix_sum]+=1

        return count

        '''
        count = 0
        window_sum = 0
        left = 0
        for right in range(len(nums)):
            window_sum += nums[right]
            while left<right and window_sum>goal:
                window_sum -= nums[left]
                left += 1
            if window_sum==goal:
                count+=1

        while left<right:
            window_sum -= nums[left]
            if window_sum==goal:
                count+=1
            left+=1

        return count
        '''
        