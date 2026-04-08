class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # 使用二维DP, dp[i][j]
        # dp[i][j]表示最多有i个0，最多有j个1，能选出的字符串最大数量
        # dp[i][j] = max(dp[i][j], dp[i-zero][j-one]+1)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for s in strs:
            zero = s.count('0')
            one = s.count('1')
            for i in range(m, zero-1, -1):
                for j in range(n, one-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-zero][j-one]+1)
        return dp[m][n]


        