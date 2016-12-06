import sys

# No cycle graph, just find the path, shortest path, topo sort
g = {}
g[0] = set([1,3])
g[1] = set([2])
g[2] = set([5])
g[3] = set([4])
g[4] = set([7])
g[5] = set([6])
g[6] = set([7])
g[7] = set()
# print(g)
def printEdge(g):
	for v in g:
		print('edges from %s' % (v))
		for n in g[v]:
			print("%s -- > %s" % (v,n)),
		print('\b')

def isPath(g, v1, v2):
	q = [v1]
	while q:
		temp = q.pop(0)
		if temp == v2:
			return True
		for x in g[temp]:
			if x not in q:
				q.append(x)
	return False

def printPath(g, v1, v2):
	res = []
	def helper(res, v1, v2, sub):
		if v1 == v2 :
			res.append(sub + [v1])
		for v in g[v1]:
			helper(res, v, v2, sub + [v1])

	helper(res, v1, v2, [])
	print('All paths from %s to %s' % (v1, v2))
	print(res)
	return res

def shorestPath(g, v1, v2):
	q, res = [[v1]], []
	cnt = 1
	def helper(level):
		res = []
		for n in level:
			for x in g[n]:
				if x not in res:
					res.append(x)
		return res
	while q:
		temp = q.pop(0)
		for n in temp:
			if n == v2:
				print(cnt)
				return cnt
		level = helper(temp)
		if level:
			q.append(helper(temp))
			cnt += 1
	print('NO Path')


printEdge(g)
print(isPath(g, 2,3))
printPath(g,0,7)
shorestPath(g, 2, 3)

g = {}
g[0] = set([(1,1),(2,2),(4,0)])
g[1] = set([(4,4)])
g[2] = set([(3,3)])
g[3] = set([(4,1)])
g[4] = set([])

printEdge(g)
import heapq
# find the shortest path to all vertices from source
def Dijkstra(g, v):
	dis = {}
	heapmap = []
	parent = {}

	## in a heapmap, initialize all v with distance infinite
	for v in g:
		heapmap

#bipartie, cycle, trie
# anyway, maybe work on the bipartie graph first
g = {}
g[0] = set([3])
g[1] = set([3,4])
g[2] = set([4])
g[3] = set([0,1])
g[4] = set([1,2])

def biparte(g):
	d = {x: None for x in g}
	q = [0]
	while q:
		temp = q.pop(0)
		color = d[temp]
		for n in g[temp]:
			if d[n] == None:
				q.append(n)
				d[n] = not color
			if d[n] == color:
				return False
	print(d)
	return True

#if edges are numbered 
def biparte2(g):
	d = ['None' for x in g]
	d[0] = 'W'
	q = [0]
	while q:
		temp = q.pop(0)
		color = d[temp]	
		for n in g[temp]:
			if d[n] == 'None':
				q.append(n)
				if d[temp] == 'W':
					d[n] = 'B'
				if d[temp] == 'B':
					d[n] = 'W'
			if d[n] == d[temp]:
				return False
	return True

biparte2(g)


#cycle in a graph
g = {}
g[1] = set([2,3,4])
g[2] = set([3])
g[3] = set([])
g[4] = set([5])
g[5] = set([6])
g[6] = set([])
print(g)

def isCycle(g):
	white = g.keys()
	grey = []
	black = []

	while white:
		cur = white[0]
		if dfs(cur, white, grey, black):
			return True
	return False

def dfs (cur, white, grey, black):
	move_vertex (cur, white, grey)
	for n in g[cur]:
		if n in black:
			continue
		if n in grey:
			return True
		if dfs(n,white,grey,black):
			return True
	move_vertex(cur, grey, black)
	return False

def move_vertex(v, source, dest):
	print(v,source, dest)
	source.remove(v)
	dest.append(v)

print(isCycle(g))