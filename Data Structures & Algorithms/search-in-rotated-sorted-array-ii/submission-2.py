class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        right_1 = -1
        bFlag = True
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                right_1 = i
                bFlag = False
                break
            else:
                continue
        if bFlag:
            right_1 = len(nums)-1

        left_1 = 0
        left_2 = right_1+1
        right_2 = len(nums)-1
        while left_1<=right_1:
            mid = (left_1+right_1)//2
            if nums[mid]==target:
                return True
            elif nums[mid]<target:
                left_1 = mid+1
            else:
                right_1 = mid-1      

        while left_2<=right_2:
            mid = (left_2+right_2)//2
            if nums[mid]==target:
                return True
            elif nums[mid]<target:
                left_2 = mid+1
            else:
                right_2 = mid-1
        
        return False