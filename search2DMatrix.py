class Solution(object):
	def searchMatrix(self, matrix, target):
		col = len(matrix[0])
		row = len(matrix)
		i = row - 1
		j = 0
		while i >= 0 and j < col:
			temp = matrix[i][j]
			if target == temp:
				return True
			elif target > temp:
				j += 1
			else:
				i -= 1
		return False