from collections import Counter
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = Counter(arr)
        curr = 0
        for k1, v1 in count.items():
            if v1==1:
                curr+=1
                if curr==k:
                    return k1
        return ""