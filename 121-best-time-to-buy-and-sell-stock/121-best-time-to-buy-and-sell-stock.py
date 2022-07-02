class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=0
        buy=prices[0]
        for ele in prices:
            if buy<ele:
                res=max(ele-buy,res)
            else:
                buy=ele
                
        return res