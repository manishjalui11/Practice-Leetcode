class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        temp=[]
        for i,m in enumerate(mat):
            temp.append((sum(m),i))
        temp.sort()
        idx=[]
        for i in range(k):
            idx.append(temp[i][1])
        return idx