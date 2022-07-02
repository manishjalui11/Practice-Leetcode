class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }
        num= 0
        i = 0
        while i < (len(s)-1):
            
            if dic[s[i]] >= dic[s[i+1]] :
                num+=dic[s[i]]
            else:
                num+=dic[s[i+1]]- dic[s[i]]
                i+=1
            i+=1
            
        if dic[s[len(s)-2]] >= dic[s[len(s)-1]] :
            num +=dic[s[len(s)-1]]
        return num