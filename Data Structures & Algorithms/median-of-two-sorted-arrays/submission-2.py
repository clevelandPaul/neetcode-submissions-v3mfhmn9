class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # first merge them in to a single ascending list
        n = len(nums1)
        m = len(nums2)
        target_lst = []
        i = 0
        j = 0
        while i<n and j<m:
            if nums1[i]<=nums2[j]:
                target_lst.append(nums1[i])
                i+=1
            else:
                target_lst.append(nums2[j])
                j+=1
        while i<n:
            target_lst.append(nums1[i])
            i+=1
        while j<m:
            target_lst.append(nums2[j])
            j+=1
        
        if len(target_lst)%2==0:
            i_1 = len(target_lst)//2
            i_2 = i_1 - 1
            return (target_lst[i_1]+target_lst[i_2])/2
        else:
            return target_lst[len(target_lst)//2]
        