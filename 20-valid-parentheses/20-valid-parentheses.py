class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        bracketSet={")":"(", "]":"[", "}":"{"}
        
        for c in s:
            if c in bracketSet:
                if stack and stack[-1]==bracketSet[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False