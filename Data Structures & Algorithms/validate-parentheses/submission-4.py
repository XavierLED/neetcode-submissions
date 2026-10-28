class Solution:
    def isValid(self, s: str) -> bool:
        #make the stack its self be the string
        stack = []
        valid = {'}':'{',')':'(',']':'['}
        for i in s:
            if stack and stack[-1] == valid.get(i):
                stack.pop()

            else:
                stack.append(i)
            
        if len(stack) == 0:
            return True
        
        return False