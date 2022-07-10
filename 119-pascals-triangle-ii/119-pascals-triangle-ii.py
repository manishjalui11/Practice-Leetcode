class Solution:
    def getRow(self, rowIndex: int) -> List[int]:  
        temp = [1]
        for x in range(1, rowIndex+1):
            
            res = temp
            temp = [1]
            for y in range(1, len(res)):
                temp.append(res[y] + res[y-1])
            
            temp.append(1)
            
        return temp