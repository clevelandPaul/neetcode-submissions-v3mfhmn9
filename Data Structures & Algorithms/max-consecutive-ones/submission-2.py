class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_len = -float('Inf')
        i = 0
        while i<len(nums):
            if nums[i]==1:
                j = i
                count = 1
                for j in range(i+1, len(nums)):
                    if nums[j]==1:
                        count+=1
                        j+=1
                    else:
                        break
                max_len = max(max_len, count)
                i = j+1
            else:
                i+=1
        return max_len if max_len!=-float('Inf') else 0