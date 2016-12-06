class Solution(object):
    def calculate(self, s):
    	## no '('
        l= list(s)
        l = [x for x in l if x != ' ']
        res = 0
        i = len(l) - 1
        stack1 = []
        stack2 = []
        for i in l:
        	if i in ['+','-','*','/']:
        		stack2.append(i)
        	else:
        		stack1.append(i)
        print(stack1)
        print(stack2)

        while stack2:
        	if stack2.pop() == '+':
        		res = int(stack1.pop())
        		res += int(stack1.pop())
        		stack1.append(res)
        		print(stack1)
        		print(stack2)
        		# print(stack1)
        	if stack2.pop() == '-':
        		res = int(stack1.pop())
        		res -= int(stack1.pop())
        		stack1.append(res)
        		print(stack1)
        		print(stack2)
        		# print(stack1)
        	# if stack2.pop() == '*':
        	# 	res = res if res != 0 else 1
        		
        	# 	res *= int(stack1.pop())
        	# 	stack1.append(res)
        	# 	# print(stack1)
        	# if stack2.pop() == '/':
        	# 	res = res if res != 0 else 1
        	# 	res /= int(stack1.pop())
        	# 	stack1.append(res)
        		# print(stack1)
        	print(stack1)
        	print(stack2)
        return stack1.pop()

s ="1 + 1"
s = "2-1 + 2 "
# s = "(1+(4+5+2)-3)+(6+8)"

res = Solution().calculate(s)
print(res)