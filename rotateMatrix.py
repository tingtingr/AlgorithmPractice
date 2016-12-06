class Solution(object):
	def rotate(self, m):
		self.printM(m)
		for i in range(len(m)):
			for j in range(i,len(m[0])):
				# print(i,j)
				if i != j:
					temp = m[i][j]
					m[i][j] = m[j][i]
					m[j][i] = temp
		self.printM(m)
		for i in range(len(m)):
			for j in range(len(m[0])/2):
				x = len(m[0])-1 - j
				temp = m[i][j]
				m[i][j] = m[i][x]
				m[i][x] = temp
		self.printM(m)

	def printM(self,m):
		for i in range(len(m)):
			for j in range(len(m[0])):
				print(m[i][j]),
			print("\b")

	def swap(self,i,j):
		temp = i 
		i = j
		j = temp

m = [[1,2,3],[4,5,6],[7,8,9]]
# s = [[x for x in range(10)] for y in range(10)]
Solution().rotate(m)
