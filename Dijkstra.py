import heapq
import sys
class HeapMap(object):
	def __init__(self):
		self.data = {}
		self.heap = self.data.values()

	def popMin(self):
		temp = heapq.heappop(self.heap)
		k = self.getKey(temp)
		del self.data[k]
		return (k, temp)
	def getKey(self, value):
		for k,v in self.data.items():
			if v == value:
				return k
	def addValue(self, v, dis):
		self.data[v] = dis

g = {}
g[0] = set([(1,2),(2,5),(4,9)])
g[1] = set([(3,4)])
g[2] = set([(4,3)])
g[3] = set([(4,1)])
g[4] = set([])

g = {}
g[1] = set([(2,7),(3,9),(6,14)])
g[2] = set([(3,10),(4,15)])
g[3] = set([(6,2),(4,11)])
g[4] = set([(5,6)])
g[5] = set([(6,9)])
g[6] = set([(5,9)])
# g[1] = set([(2,7),(3,9),(6,14)])
# g[2] = set([(3,10),(4,15),(1,7)])
# g[3] = set([(1,9),(2,10),(6,2),(4,11)])
# g[4] = set([(5,6),(2,15),(3,11)])
# g[5] = set([(6,9),(4,16)])
# g[6] = set([(1,14),(3,2),(5,9)])


def dijk(g, source):
	parent = {}
	dis = {}
	heapmap = HeapMap()
	parent[source] = source
	## initialize heapmap
	for x in g.keys():
		if x != source:
			heapmap.addValue(x, sys.maxsize)

	heapmap.data[source] = 0
	heapmap.heap = heapmap.data.values()
	heapq.heapify(heapmap.heap)

	while heapmap.data:
		vertex, distance = heapmap.popMin()
		dis[vertex] = distance
		for v, d in g[vertex]:
			if v in heapmap.data and d + dis[vertex] < heapmap.data[v]:
				heapmap.data[v] = d + dis[vertex]
				parent[v] = vertex
				heapq.heapify(heapmap.heap)
		heapmap.heap = heapmap.data.values()
		heapq.heapify(heapmap.heap)
	print(dis)
	return dis
dijk(g,1)
