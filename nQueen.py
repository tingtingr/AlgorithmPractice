class Solution(object):
    def solveNQueens(self, n):
        #one solution matrix
        board = [[0 for i in range(n)] for j in range(n)]
        # collection of solution matrix
        ret = []        
        # result
        res = []
        self.helper(n,ret,board,0)
        for M in ret:
            #i is a matrix
            solu = []
            for j in range(len(M)):
                x = [str(y) for y in M[i]]
                s = ""
                r = s.join(x)
                solu.append(r)
            res.append(solu)

    def helper(n,ret,board,index):
        if



    def printMaxtrix(self, m):
        row = len(m)
        col = len(m[0])
        for i in range(row):
            for j in range(col):
                print(m[i][j]),
            print("\b")

Solution().solveNQueens(5)