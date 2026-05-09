class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        com_lst = list(set(nums1)&set(nums2))
        lst_1 = [nums1[i] for i in range(len(nums1)) if nums1[i] not in com_lst]
        lst_2 = [nums2[i] for i in range(len(nums2)) if nums2[i] not in com_lst]
        return [list(set(lst_1)), list(set(lst_2))]
        