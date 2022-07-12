class Solution:
    def fillCups(self, amount: List[int]) -> int:
        result = 0
        amount.sort()
        
        while amount[1] and amount[2]:
            result += 1
            amount[1] -= 1
            amount[2] -= 1
            amount.sort()
        result += amount[2]
            
        return result