matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

def printM(m):
	for i in range(len(m)):
		for j in range(len(m[0])):
			print("%2d" % (m[i][j])),
		print('\b')
	print('\n')

def printDia(m):
	d = {}
	for i in range(len(m)+len(m[0])-1):
		d[i] = []
	print(d)
	for i in range(len(m)):
		for j in range(len(m[0])):
			d[i+j].append(m[i][j])

	for i in d.values():
		for j in i:
			print(j),
		print('\b')

printM(matrix)
printDia(matrix)