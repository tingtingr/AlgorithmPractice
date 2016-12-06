class Solution(object):

    def countComponents(self, n, edges):
        p = range(n)
        def find(v):
            print(p)
            if p[v] != v:
                p[v] = find(p[v])
            return p[v]

        for e in edges:
            v, w = map(find, e)
            p[v] = w
            if v != w:
                n -= 1
        print(n)
        return n

n = 5
edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

Solution().countComponents(n,edges)