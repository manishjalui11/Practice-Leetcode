class Solution:
    def numberOfSteps(self, num: int) -> int:
        k=0
        while num:
            if num%2:
                num-=1
            else:
                num/=2
            k+=1
        return k