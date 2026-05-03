class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        if len(mat)==1:
            return mat[0][0]
        dig_sum = 0
        for i in range(len(mat)):
            dig_sum += mat[i][i]
            dig_sum += mat[i][len(mat)-i-1]
        if len(mat)%2==0:
            return dig_sum 
        else:
            return dig_sum - mat[len(mat)//2][len(mat)//2]


        