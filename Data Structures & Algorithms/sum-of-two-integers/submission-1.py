class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xffffffff
        MAX_INT = 0x7fffffff

        while b != 0:
            carry = ((a & b) << 1) & MASK
            a = (a ^ b) & MASK
            b = carry

        return a if a <= MAX_INT else ~(a ^ MASK)
        