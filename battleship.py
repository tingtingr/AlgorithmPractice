class Solution(object):
    def countBattleships(self, board):
        cnt = [0]
        p = [x for x in range(len(board) * len(board[0]))]
        rank = [0 for i in p]
        
        def find(x):
            print('find', x)
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]
        def union(a,b, cnt):
            a1,b1 = a
            a2,b2 = b
            print(a,b)
            x = find(a1*len(board[0])+b1)
            y = find(a2 *len(board[0]) + b2)
            if x != y:
                if rank[x] < rank[y]:
                    p[x] = y
                elif rank[x] > rank[y]:
                    p[y] = x
                else:
                    p[y] = x
                    rank[x] += 1
                cnt[0] -= 1
                
        def getnbrs(board, i, j):
            vectors = [[0,1],[0,-1],[1,0],[-1,0]]
            res = []
            for v in vectors:
                a,b = v
                if 0 <= a+i < len(board) and 0 <= b + j < len(board[0]) and board[a+i][b+j] == 'X':
                    res.append((a+i, b+j))

            return res
                    
                    
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    cnt[0] += 1
                    nbrs = getnbrs(board, i, j)
                    print('nbrs',nbrs)
                    for n in nbrs:
                        union(n,(i,j),cnt)
                    
        print(cnt)
        return cnt
            
board = ["X..X","...X","...X"]
board =["XXX"]
board = ["X.X.X",".X.X.",".X...",".X..X",".X...","X.XXX",".X...",".X.X.","X.X.X",".X..X"]
Solution().countBattleships(board)