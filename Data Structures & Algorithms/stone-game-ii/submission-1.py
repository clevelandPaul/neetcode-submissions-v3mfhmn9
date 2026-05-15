from functools import lru_cache
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        # 当前玩家最大收益 = 剩余总石子 - 对手在下一状态的最大收益
        # 因为两个人拿的综合固定，所以你让对手拿的越少，自己就拿的越多
        # dp(i, M): 从第i堆开始，当前M给定时，当前玩家最多能拿到多少石子
        # 关键转移，设suffix[i]为从i开始剩下的总石子数
        # 当前玩家如果拿X堆，对手最多能拿dp(i+X, max(M, X))
        # dp(i, M) = max (X) suffix[i]-dp(i+X, max(M, X))

        n = len(piles)
        suffix = [0 for _ in range(n+1)]
        for i in range(n-1, -1, -1):
            suffix[i] = suffix[i+1]+piles[i]

        @lru_cache(None)
        def dp(i, M):
            if i>=n:
                return 0

            if i+2*M>=n:
                return suffix[i]

            best = 0
            for X in range(1, 2*M+1):
                opponent = dp(i+X, max(M, X))
                cur = suffix[i]-opponent
                best = max(best, cur)
            return best

        return dp(0, 1)        