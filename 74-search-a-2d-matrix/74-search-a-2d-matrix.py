class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for ele in matrix:
            if target<=ele[-1]:
                if target in ele:
                    return True