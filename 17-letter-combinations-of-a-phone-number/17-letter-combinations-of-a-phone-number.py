class Solution:
    
    def mulList(self,s1,s2):
        r=[]
        for i in s1:
            for j in s2:
                
                r.append(i+j)
        return r
    
    
    def letterCombinations(self, digits: str) -> List[str]:
        num={2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}
        res=['']
        for ele in digits:
            res=self.mulList(res,num[int(ele)])
        if res==[""]:
            return []
        return res
    
    
    