class Solution:
    def addDigits(self, num: int) -> int:
        li=list(map(int,str(num)))
        while len(li)>1:
            s=sum(li)
            li.clear()
            li.extend(list(map(int,str(s))))
        return li[0]