from collections import defaultdict

class TrieNode(object):
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False
        
        
class Trie(object):
    def __init__(self):
        self.root = TrieNode()
        
    def addword(self,word):
        cur = self.root
        for c in word:
            cur = cur.children[c]
        cur.is_word = True
    
    def isPrefix(self, prefix):
        cur = self.root
        for w in prefix:
            cur = cur.children.get(w)
            if cur is None:
                return False
        return True
        
class Solution(object):
    def findWords(self, board, words):
        trie = Trie()
        res = []
        for word in words:
            print(word,trie.isPrefix(word))
            if trie.isPrefix(word):
                
                res.append(word)
            else:
                if self.backtrack(word, board):
                    trie.addword(word)
                    res.append(word)
        print(res)
        return res
        
    # return bool, whether a word is in board
    def backtrack(self, word, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    print('we have a match',board[i][j],word[0])
                    isExist = [False]
                    visited = [[False for x in range(len(board[0]))] for y in range(len(board))]
                    self.helper(isExist, word, board, [], i, j, visited)
                    if isExist[0]:
                        return True
        return False
        
    def helper(self,isExist, word, board, sub, i, j, visited):
        print(word, sub, board[i][j],isExist,)
        if len(word) == 1:
            isExist[0] = True
            print(isExist[0])
            return
        vectors = [[0,1],[0,-1],[1,0],[-1,0]]
        candidates = []
        for v in vectors:
            a,b = v
            if 0 <= i+a <len(board) and 0 <= j+b < len(board[0]) and not visited[i+a][j+b] and board[i+a][j+b] == word[1]:
                candidates.append([i+a,j+b])
        if len(candidates) == 0:
            print(isExist[0])
            return
        else:
            for x,y in candidates:
                visited[x][y] = True
                self.helper(isExist, word[1:], board, sub+[word[0]],x,y,visited)


words = ["oath","pea","eat","rain"]
board =[['o','a','a','n'],['e','t','a','e'],['i','h','k','r'],['i','f','l','v']]
visited = [[False for i in range(len(board[0]))] for j in range(len(board))]
# Solution().helper([False],'rain',board,[],2,3,visited)
Solution().backtrack('oath',board)
Solution().findWords(board,words)