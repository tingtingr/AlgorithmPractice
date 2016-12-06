class Solution(object):
    def gameOfLife(self, board):
        m = [[board[i][j] for j in range(len(board[0]))] for i in range(len(board))]
        def getnbrs(i,j):
            vectors = [[1,1],[1,0],[1,-1],[0,1],[0,-1],[-1,1],[-1,0],[-1,-1]]
            cnt = 0
            for v in vectors:
                if 0 <= i + v[0] < len(board) and 0 <= j + v[1] < len(board[0]) and board[i+v[0]][j+v[1]] == 1:
                    cnt += 1
            return cnt
        for i in range(len(board)):
            for j in range(len(board[0])):
                c = getnbrs(i,j)
                if board[i][j] == 1:
                    if c > 3 or c < 2:
                        m[i][j] = 0
                if board[i][j] == 0 and c == 3:
                        m[i][j] = 1
        for i in range(len(board)):
            board[i] = m[i]

m = [[0,0,0,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,0,0,0]]
Solution().gameOfLife(m)
print(m)

use bit to save space
use % for infinite space ( donut shape)