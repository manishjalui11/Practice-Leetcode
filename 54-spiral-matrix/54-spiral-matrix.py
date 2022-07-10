class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m=len(matrix)
        n=len(matrix[0])
        l,t= 0,0
        r=n
        b=m
        res=[]
        while l < r and t < b:
            for i in range(l, r):
                if matrix[t][i]!=-111:
                    res.append(matrix[t][i])
                    matrix[t][i]=-111
            t+= 1
            for j in range(t, b):
                if matrix[j][r-1]!=-111:
                    res.append(matrix[j][r-1])
                    matrix[j][r-1]=-111
            r-= 1
            for k in range(r-1,-1,-1):
                if matrix[b-1][k]!=-111:
                    res.append(matrix[b-1][k])
                    matrix[b-1][k]=-111
            b-= 1
            for m in range(b-1, t-1,-1):
                if matrix[m][l]!=-111:
                    res.append(matrix[m][l])
                    matrix[m][l]=-111
            l+= 1          
        return res