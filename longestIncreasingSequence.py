#Given an unsorted array of integers, find the length of longest 
#increasing subsequence.

#For example,
#Given [10, 9, 2, 5, 3, 7, 101, 18],
#The longest increasing subsequence is [2, 3, 7, 101], therefore the
#length is 4. 
#Note that there may be more than one LIS combination, it is only 
#necessary for you to return the length.

#Your algorithm should run in O(n2) complexity.

#Follow up: Could you improve it to O(n log n) time complexity?

class Solution(object):

	def lengthOfLIS(self, nums):
		
        
		
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

                
word1 = "aerwreewrewrbc"
word2 = "aerwerwrwerwr"
matrix = [["a","b","c"],["d","e","f"],["g","h","i"]]

#Solution().printStrMatrix(word1, word2)
matrix2 = Solution().makeMatrix(word1, word2)
Solution().printMatrix(matrix2)
Solution().minDistance(word1,word2)

