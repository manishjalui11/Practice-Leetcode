import math

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            l=[1]*(i+1)
            if i:
                for j in range(1,i):
                    l[j]=res[i-1][j-1]+res[i-1][j]
            res.append(l)
        return res