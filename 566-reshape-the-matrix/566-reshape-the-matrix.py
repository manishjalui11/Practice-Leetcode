class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n= len(mat), len(mat[0])
        if m*n!=r*c:
            return mat
        li=[[0 for i in range(c)] for j in range(r)]
        i=j=0
        for e in mat:
            for ele in e:
                li[i][j]=ele
                j+=1
                if j>=c:
                    j=0
                    i+=1
        return li