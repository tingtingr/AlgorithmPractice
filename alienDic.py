class Graph(object):
    def __init__(self):
        self.v = set()
        self.e = set()
    def add(self, edge):
        print(edge)
        self.e.add(edge)
        self.v.add(edge[0])
        self.v.add(edge[1])
    
    
class Solution(object):
    def alienOrder(self, words):
        g = Graph()
        print(g.e)
        print(g.v)
        for w in words:
            i = 0
            j = i + 1
            while j < len(w):
                if w[i] != w[j]:
                    g.add((w[i],w[j]))
                i += 1
                j += 1
        print(g.e)

words = ["wrt","wrf","er","ett","rftt"]
Solution().alienOrder(words)