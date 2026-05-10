class Solution:
    def reverseBits(self, n: int) -> int:
        # 看n的第几位上是1
        res = 0
        for b in range(32):
            if (n>>b)&1:
                res += 2**(32-b-1)
        return res
        