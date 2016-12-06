class Solution(object):
	def maxSumSubmatrix(self, matrix, k):
		dp = [[0 for i in range(len(matrix[0]) + 1)] for j in range(len(matrix) + 1)]
		for row in range(len(matrix)):
			for col in range(len(matrix[0])):
					cur = max(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])
					dp[i+1][j+1] = max(cur + matrix[i][j], cur)
		return dp[-1][-1]


