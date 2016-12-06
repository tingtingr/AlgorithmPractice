class UnionFind(object):
	def find(self, v, p):
		if p[v] != v :
			p[v] = self.find(p[v], p)
		return p[v]
	def union(self, a, b, p):
		print(a,b,p)
		px = self.find(a,p)
		py = self.find(b,p)
		p[py] = px
		print(p)
	def expand (self, x, p):
		for i in range(len(x)):
			if x[i] == 1:
				print(i)
				print(self.find(i,p))
				a = i
				self.union( a,i, p)
		return p

class QuickFind(object):
	def __init__(self, N):
		self.id = range(N)
		
	# if they are in the same subset
	def find(self, p, q):
		return id[p] == id[q]
 	
 	def unite(self, p, q):
 		pid = id[p]
 		for i in range(len(id)):
 			if id[i] == pid:
 				id[i] = id[q]

class QuickUnion(object):
	def __init__(self, N):
		self.id = []
		for i in range(N):
			id[i] = i
	def root(self, i):
		while i!= self.id[i]:
			i = self.id[i]
		return i
	def find(self, p, q):
		return self.root(p) == self.root(q)
	def unite(self,p,q):
		i = self.root(p)
		j = self.root(q)
		id[i] = j


Quick-find defect.
• Union too expensive (N steps).
• Trees are flat, but too expensive to keep them flat.
Quick-union defect.
• Trees can get tall.
• Find too expensive (could be N steps)
• Need to do find to do union
algorithm union find
Quick-find N     1
Quick-union N*   N
p= [0,1,2,3,4,5,6,7]
x=[0,1,1,1,1,1,0,0]

# print(UnionFind().union(0,2,p))
# print(p)

# print(UnionFind().union(2,5,p))
# print(p)

print(UnionFind().expand(x,p))

