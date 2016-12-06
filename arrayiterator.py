class Iterator(object):
	def __init__(self,arr):
		self.nextArr = 0
		self.nextInd = 0
		self.curArr = 0
		self.curInd = 0
		self.preArr = 0
		self.preInd = 0
		self.arr = arr

	def setnext(self):
		# print('moving')
		# print('cur')
		# print(self.curArr,self.curInd,self.arr[self.curArr][self.curInd])
		curLen = self.arr[self.curArr]
		res = False
		# print(curLen)
		if self.curInd < len(curLen) - 1:
			self.nextInd = self.curInd + 1
			self.nextArr = self.curArr
		else:
			while self.curArr + 1 < len(self.arr) and len(self.arr[self.curArr + 1]) == 0:
				self.curArr += 1
			if self.curArr + 1 >= len(self.arr):
				# print(res)
				return res
			self.nextArr = self.curArr + 1
			self.nextInd = 0
		res = True
		return res

	def hasnext(self):
		self.setnext()
		return self.nextArr < len(self.arr) and self.nextInd < len(self.arr[self.nextArr])

	def next(self):
		if self.nextArr == 0 and self.nextInd == 0:
			res = self.arr[self.curArr][self.curInd]
		else:
			res = self.arr[self.nextArr][self.nextInd]
			self.curArr = self.nextArr
			self.curInd = self.nextInd
			self.setnext()
		return res


	def remove(self):
		del self.arr[curArr][curInd]
		print(self.arr)


arr = [[1],[],[],[],[4,5,6],[]]

i = Iterator(arr)
print(i.hasnext())
print(i.next())
print(i.hasnext())
print(i.next())
print(i.hasnext())
print(i.next())
print(i.hasnext())
print(i.next())
print(i.hasnext())
print(i.next())
print(i.hasnext())
print(i.next())

# i.movetonext()
# i.curArr = i.nextArr
# i.curInd = i.nextInd
# i.movetonext()
# i.curArr = i.nextArr
# i.curInd = i.nextInd
# i.movetonext()
# i.curArr = i.nextArr
# i.curInd = i.nextInd
# i.movetonext()
# i.curArr = i.nextArr
# i.curInd = i.nextInd
# print(i.movetonext())