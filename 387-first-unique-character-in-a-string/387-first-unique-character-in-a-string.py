class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        for c in s:
            if c not in dic:
                dic[c] = 0
            else:
                dic[c] += 1
        
        for k, v in dic.items():
            if v == 0:
                return s.index(k)
        
        return -1