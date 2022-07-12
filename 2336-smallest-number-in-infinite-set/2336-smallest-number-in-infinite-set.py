class SmallestInfiniteSet:

    def __init__(self):
        self.s=[]
        for i in range(1000):
            self.s.append(i+1)
        
    def popSmallest(self) -> int:
        return self.s.pop(0)        

    def addBack(self, num: int) -> None:
        if not num in self.s:
            self.s.append(num)
            self.s.sort()

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)