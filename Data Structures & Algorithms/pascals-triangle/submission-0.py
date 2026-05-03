class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==1:
            return [[1]]
        res = [[1], [1,1]]
        for i in range(2, numRows):
            new_array = [0 for _ in range(i+1)]
            new_array[0] = res[-1][0]
            for i in range(len(res[-1])-1):
                new_array[i+1] = res[-1][i]+res[-1][i+1]
            new_array[-1] = res[-1][-1]
            res.append(new_array)
        return res

        