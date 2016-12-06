class Solution(object):
	def fib(self, n):
		a,b,c = 1,1,2
		for i in range(4, n + 1):
			a,b = b,c
			c= a+b
		return c
print(Solution().fib(9))

