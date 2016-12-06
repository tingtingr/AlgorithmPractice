class Solution(object):
    def longestValidParentheses(self, s):
        stack=[]
        curL = 0
        maxL = 0
        for i in range(len(s)):
            print(stack)
            print(i,maxL)
            if s[i] == "(":
                stack.insert(0, (i, 0))
            else:
                if len(stack) == 0 or stack[0][1] == 1:
                    stack.insert(0, (i, 1))
                else:
                    print("temp is "),
                    del stack[0]
                    if len(stack) == 0:
                        curL = i + 1
                    else:
                        curL = i - stack[0][0]
                    print(curL)
                    maxL = max(maxL, curL)

        return maxL

s = "()(((())"
s= "(()()"
print(s)
print(Solution().longestValidParentheses(s))
