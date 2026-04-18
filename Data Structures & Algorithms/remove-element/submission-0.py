class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        valid_eles = []
        count_val = 0
        for num in nums:
            if num!=val:
                valid_eles.append(num)
            else:
                count_val+=1
        nums[0:len(nums)-count_val] = valid_eles
        nums[len(nums)-count_val:] = [val for _ in range(count_val)]
        return len(nums)-count_val