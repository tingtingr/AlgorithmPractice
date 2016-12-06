class Solution(object):
    def isValid(self, s):
        stack = []
        for c in s:
            if c in ['(','[','{']:
                stack.push(c)
            else:
                if not stack:
                    return False
                temp = stack.pop()
                if temp == '(' and c != ')':
                    return False
                if temp == '[' and c!= ']':
                    return False
                if temp == '{' and c != '}':
                    return False
        if len(stack) > 0:
            return False
        else:
            return True