class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        stack = []
        mapping = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        for c in s:
            if c in mapping: # if it is a closing paranthesis (keys of the map we made)
                if stack and stack[-1] == mapping[c]: # if the stack is not empty and the top of the stack matches the opening paranthesis of the current, then pop
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False # return true if stack is empty else false
            