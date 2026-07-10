class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {'[':']','{':'}','(':')'}
        for i in s:
            if i in parentheses:
                stack.append(i)
                continue
            if not stack:
                return False
            if i != parentheses[stack[-1]]:
                return False
            stack.pop()
        return not stack