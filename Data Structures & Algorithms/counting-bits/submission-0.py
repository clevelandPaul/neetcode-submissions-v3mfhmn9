class Solution:
    def countBits(self, n: int) -> List[int]:
        nums = [i for i in range(n+1)]
        res = []

        for n in nums:
            bit_len = n.bit_length()
            cnt1 = 0
            for b in range(bit_len):
                if (n>>b)&1:
                    cnt1+=1
            res.append(cnt1)

        return res        