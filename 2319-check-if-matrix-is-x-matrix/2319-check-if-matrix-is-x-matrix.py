class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == j or j == len(grid) - 1 - i:
                    if not grid[i][j]:
                        return False
                else:
                    if grid[i][j]:
                        return False
        return True