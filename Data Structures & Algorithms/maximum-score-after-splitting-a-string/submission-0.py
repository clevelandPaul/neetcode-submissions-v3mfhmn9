class Solution:
    def maxScore(self, s: str) -> int:
        left_zeros = [0 for _ in range(len(s))]
        right_ones = [0 for _ in range(len(s))]
        left_zeros[0] = 1 if s[0]=='0' else 0
        for i in range(1, len(s)):
            if s[i]=='0':
                left_zeros[i] = left_zeros[i-1]+1
            else:
                left_zeros[i] = left_zeros[i-1]
        right_ones[len(s)-1] = 1 if s[len(s)-1]=='1' else 0
        for j in range(len(s)-2, -1, -1):
            if s[j]=='1':
                right_ones[j] = right_ones[j+1]+1
            else:
                right_ones[j] = right_ones[j+1]
        current_sum = 0
        for i in range(len(s)-1):
            current_sum = max(current_sum, left_zeros[i]+right_ones[i+1])
        return current_sum
        