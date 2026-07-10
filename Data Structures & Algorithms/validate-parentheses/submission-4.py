class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {'[':']','{':'}','(':')'}
        for i in s:
            if i in parentheses:
                stack.append(i)
            else:
                if stack == []:
                    return False
                elif i == parentheses[stack[-1]]:
                    stack.pop()
                else:
                    return False
        if stack == []:
            return True
        return False
