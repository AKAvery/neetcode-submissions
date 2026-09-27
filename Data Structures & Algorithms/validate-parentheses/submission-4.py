class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pDict = {')' : '(', '}' : '{', ']' : '['}
        for char in s:
            print(stack)
            if len(stack) == 0:
                stack.append(char)
            else:
                if char in pDict and pDict[char] == stack[-1]:
                    stack.pop()
                else: 
                    stack.append(char)

        if not stack:
            return True
        else:
            return False