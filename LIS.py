import sys

from time import sleep  
class Solution(object):

	def lengthOfLIS(self, nums):
		parent = [0 for i in range(len(nums))]
		track = [-sys.maxsize]
		length = 0
		LIS= []
		for i in range(len(nums)):
			if nums[i] > track[-1]:
				pre = track[-1]
				track.append(nums[i])
				parent[i] = pre
				length += 1
			else:
				print("replacing {0}".format(nums[i]))
				print(track[1::][0])
				position = self.searchPos(track[1::], nums[i]) + 1
				print("position is {0}".format(position))
				track[position] = nums[i]
				parent[i] = track[position - 1]
		#print backtrack
		self.printArr(nums)
		self.printArr(track)
		self.printArr(parent)
		self.printArr(LIS)
		
		value = track[-1]
		
		while value != -sys.maxsize:
			
			LIS.insert(0,value)
			self.printArr(LIS)
			index = nums.index(value)
			pre = parent[index]
			value = pre
		
#		k = track[length]
#		for j in range(length - 1, -1, -1):
#			LIS[j] = nums.index(k)
#			k = parent[k]
#		int k 	= increasingSub[length];
#		for(int j=length-1; j>=0; j--)
#		{
#			LIS[j] =  X[k];
#			k = parent[k];
		self.printArr(LIS)
		return length

	def searchPos(self, arr, target):
# 		self.printArr(arr)
		start = 0
		end = len(arr) - 1
		while start + 1 < end:
			print(start,mid,end)
			mid = start + (end - start) // 2
			if arr[mid] <= target:
				start = mid
			else:
				end = mid
		if arr[start] > target:
			return start
		else:
			return end

	def searchPos(self, arr, target):
		start = 0
		end = len(arr) - 1
		while start + 1 < end:
			mid = start + (end - start) / 2
			if arr[mid] <= target:
				start = mid
			else:
				end = mid
		if arr[start] >= target:
			return start
		if arr[end] > target:
			return end
	def printArr(self, arr):
		print("["),
		for i in range(len(arr)):
			print("{0}, ".format(arr[i])),
		print("]")
		
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
arr1 = [3,5,6,2,5]
arr2 = [3,1,5,2,6,4,9]
matrix = [["a","b","c"],["d","e","f"],["g","h","i"]]

#Solution().printStrMatrix(word1, word2)
#matrix2 = Solution().makeMatrix(word1, word2)
#Solution().printMatrix(matrix2)
print(Solution().lengthOfLIS(arr1))

