from collections import defaultdict
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        d = defaultdict(int)
        for n in nums:
            d[n] = d.get(n, 0)+1
        m = 1
        while True:
            if d[m]==0:
                return m
            m+=1
        