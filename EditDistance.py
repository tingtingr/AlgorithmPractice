
from time import sleep  
class Solution(object):

	def minDistance(self, word1, word2):
		len1 = len(word1)
		len2 = len(word2)
		if len1 == 0 or len2 == 0:
			return len1 + len2
		arr = [[0 for i in range(len1 + 1)] for j in range(len2 + 1)] 
		print("original matrix")
		#init
		arr[0][0] = 0
		self.printMatrix(arr)
		for i in range(len1):
		    arr[0][i + 1] = i + 1
		for j in range(len2):
		    arr[j + 1][0] = j + 1
		print("after initialization")
		self.printMatrix(arr)
		#dp
		for i in range(len2):
			for j in range(len1):
				print("current char in word1 is {0}, word2 is {1}".format(word1[j], word2[i]))
				if word2[i] != word1[j]:
					print("{0} is  NOT the same as {1}".format(word1[j], word2[i]))
					arr[i + 1][j + 1] = min(arr[i][j], arr[i][j + 1], arr[i + 1][j]) + 1
					self.printMatrix(arr)
				else:
					print("{0} is the same as {1}".format(word1[j], word2[i]))
					arr[i + 1][j + 1] = arr[i][j]
					self.printMatrix(arr)
		print("final matrix")
		self.printMatrix(arr)
		return arr[len2][len1]
        
		
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

