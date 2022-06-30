class Solution:
    def countHousePlacements(self, n: int) -> int:
        a,b=0,1
        for i in range(n+1):
            a,b=b,a+b
        return (b*b)%((10**9)+7)