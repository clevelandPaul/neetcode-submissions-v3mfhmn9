import random
import bisect

class Solution:
    # 先对w数组做一个前缀和
    # 然后去随机生成数字，如果在(w[i], w[i+1]]之间，返回index i+1
    # bisect_left: 在有序数组中，找到第一个>=target的位置

    def __init__(self, w: List[int]):
        self.prefix = []
        total = 0
        for x in w:
            total += x
            self.prefix.append(total)
        self.total = total

    def pickIndex(self) -> int:
        target = random.randint(1, self.total)
        return bisect.bisect_left(self.prefix, target)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()