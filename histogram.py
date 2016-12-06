class Solution(object):
	def histogram(self, arr):
		stack = []
		i = 0
		maxArea = 0
		arr.append(-1)
		while i < len(arr):
			if len(stack) == 0 or arr[i] >=  arr[stack[0]]:
				stack.insert(0, i)
				i += 1
			else:
				curArea = 0
				top = stack[0]
				del stack[0]
				if len(stack) == 0:
					curArea = arr[top] * i
				else:
					curArea = arr[top] * (i - stack[0] - 1)
				maxArea = max(curArea, maxArea)
		return maxArea

arr = [2,1,5,5,6,5,2,3]
# arr = [5,1,2,4,3,10,9]
print(arr)
print(Solution().histogram(arr))