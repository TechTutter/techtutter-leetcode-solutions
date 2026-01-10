class Solution:
    OPEN = {"(", "[", "{"}
    OPPOSITES = { ")": "(", "]": "[", "}": "{" }
    
    """
    stack = []
    for bracket in s:
        if bracket is open:
            stack.push(bracket)
        else if stack is not empty and bracket matches stack.top:
            stack.pop()
        else:
            return False
    return stack is empty
    """
    def isValid(self, s: str) -> bool:
        stack = []
        
        for p in s:
            if p in self.OPEN:
                stack.append(p)
            elif stack and self.OPPOSITES.get(p) == stack[-1]:
                stack.pop()
            else:
                return False
        
        return not stack