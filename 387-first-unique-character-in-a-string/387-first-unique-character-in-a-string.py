class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        for i,e in enumerate(s):
            if s.count(e) ==1:
                return i
        return -1