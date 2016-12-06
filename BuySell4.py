class Solution(object):
	def maxProfit(self, k, prices):
		n = len(prices)
		dp = [[0 for i in range(n + 1)] for j in range(k + 1)]
		for i in range(k):
			for j in range(n):
				dp[i + 1][j + 1] = max(dp[i + 1][j], prices[j] - prices[j - 1] + dp[i][j])
		self.printMatrix(dp)
		return dp[-1][-1]

	def makeMatrix(self, str1, str2):
		col = len(str1)
		row = len(str2)
		matrix = [[0 for i in range(col + 1)] for j in range(row + 1)]
		for j in range(row):
			for i in range(col):
				matrix[j+1][i+1] = str1[i]+str2[j]
		return matrix
				
	def printMatrix(self, matrix):
		col = len(matrix[0])
		row = len(matrix)
		for i in range(row):
			for j in range(col):
				print (matrix[i][j]),
			print("\t")
		
	def printStrMatrix(self, str1, str2):
		len1 = len(str1)
		len2 = len(str2)
		for j in range(len2 + 1):
			if j == 0:
				print(0),
			else:
				print(str2[j - 1]),
			for i in  range(len1):
				if j == 0:
					print(str1[i] + " "),
				else:
					print(str1[i] + str2[j - 1]),
			print("\t")
		print(str1 + str2)

                
k = 3
arr = [4,5,1,6,2,7,5]

print(Solution().maxProfit(k,arr))

