class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        sort_lst = sorted(nums)
        n = len(nums)
        if n%2==0:
            small_half = sort_lst[:n//2]
            large_half = sort_lst[n//2:]
            print(large_half)
            for i in range(n//2):
                nums[2*i] = small_half[i]
                nums[2*i+1] = large_half[i]
        else:
            nums[0] = sort_lst[0]
            small_half = sort_lst[1:n//2+1]
            large_half = sort_lst[n//2+1:]
            for i in range(1, n//2+1):
                nums[2*i-1] = large_half[i-1]
                nums[2*i] = small_half[i-1]
        