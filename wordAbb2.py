# abbreviate a word in a dictionary, is the abbreviation is equal or greater than the original word then
# use the word
from collections import defaultdict
class TriNode(object):
	def __init__(self):
		self.count = 0
		self.children = defaultdict(TriNode)
		