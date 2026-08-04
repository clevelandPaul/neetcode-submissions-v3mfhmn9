class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        sum_1 = sum(nums)
        s = set(nums)
        sum_2 = sum(s)
        return (sum_1-sum_2)//(len(nums)-len(s))
        