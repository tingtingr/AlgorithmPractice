class myiter(object):
	def __init__(self, n):
		self.i = 0
		self.n = n-1
	def __iter__(self):
		return self

	def next(self):
		if self.i <= self.n:
			n = self.n
			self.n -= 1
			return n
		else:
			raise StopIteration()

# x = myiter(5)
# print(x.next())
# print(x.next())
# print(x.next())
# print(x.next())
# print(x.next())
# print(x.next())
# print(x.next())

def intergers():
	i = 1
	while True:
		yield i
		i = i + 1

def squares():
	for i in integers():
		yield i*i
def take(n,seq):
	seq = iter(seq)
	result = []
	try:
		for i in range(n):
			result.append(seq.next())
	except StopIteration:
		pass
	return result

print take(5, squares()) # prints [1, 4, 9, 16, 25]