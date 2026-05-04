class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==0:
            return [1]
        elif rowIndex==1:
            return [1, 1]
        res = [[1], [1,1]]
        for i in range(2, rowIndex+1):
            new_array = [0 for _ in range(i+1)]
            new_array[0] = 1
            new_array[-1] = 1
            for i in range(len(res[-1])-1):
                new_array[i+1] = res[-1][i]+res[-1][i+1]
            res.append(new_array)
        return res[-1]
        