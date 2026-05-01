class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos_array = []
        neg_array = []
        for i in range(len(nums)):
            if nums[i]>0:
                pos_array.append(nums[i])
            else:
                neg_array.append(nums[i])
        for i in range(len(pos_array)):
            nums[2*i] = pos_array[i]
            nums[2*i+1] = neg_array[i]
        return nums
        