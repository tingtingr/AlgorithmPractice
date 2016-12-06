class TrieNode(object):
	def __init__(self):
		self.map = dict()
		self.endofword = False


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
    	node = self.root
        for c in word:
        	if c not in node.map:
        		node.map[c] = TrieNode()
        	node = node.map[c]
        node.endofword = True

    def search(self, word):
        node = self.root
        for c in word:
        	if c not in node.map:
        		return False
        	node = node.map[c]
        return node.endofword
        

    def startsWith(self, prefix):
        node = self.root
        for c in prefix:
        	if c not in node.map:
        		return False
        	node = node.map[c]
        return True
        

# no Trie object will be instantiated and called as such:
trie = Trie()
trie.insert("somestring")
trie.search("key")