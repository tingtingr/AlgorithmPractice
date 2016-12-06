class Solution(object):
    def exist(self, board, word):
    	self.printM(board)
    	visited = [[False for i in range(len(board[0]))] for j in range(len(board))]
    	for i in range(len(board)):
    		for j in range(len(board[0])):
    			if self.getWords(board, word, i , j, visited, 0):
    				return True
    	return False

    def getWords(self,board, word, i, j, visited, pos):
    	self.printM(visited)
    	self.printM(board)
    	print('\n')
    	if pos == len(word):
    		return True

    	if i < 0 or i == len(board) or j < 0 or j == len(board[0]) or visited[i][j] or word[pos] != board[i][j]:
    		return False
    	visited[i][j] = True

    	res = self.getWords(board,word,i,j + 1,visited,pos + 1) or self.getWords(board,word,i,j - 1,visited,pos + 1) or self.getWords(board,word,i + 1,j,visited,pos + 1) or self.getWords(board,word,i - 1,j,visited,pos + 1)
    	## if this one finished and not return True we didn;t find an answer
    	# visited[i][j] = False

    	return res

    def printM(self, m):
    	for i in range(len(m)):
    		for j in range(len(m[0])):
    			print("{:<6}".format("%s" % m[i][j])),
    		print('\b')
        
board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]

word = 'ABCCED'


[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]


["CAA","AAA","BCD"]
"AAB"

# CAA
# AAA
# BCD
# AAB

# AAB
# [0][0] = False
# [0][1] = True res = [1][1], [-1][1], [0][0], [0][2]

# [1][1] =
# [0][2]
# i = 0, j = 1
# board[i][j] = A
# print(Solution().exist(board,word))
